import os
import logging

from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter, Depends
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.crud.save_files import save_file, get_files_for_plan
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

CARPETA_DESTINO = "archivos_subidos"
os.makedirs(CARPETA_DESTINO, exist_ok=True)

#ToDo: Los nombres de fichero se tienen que modificar par que sean unicos
@router.post("/upload/{plan_id}")
async def subir_fichero(plan_id: int, file: UploadFile = File(...),db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    ruta_destino = os.path.join(CARPETA_DESTINO, file.filename)
    
    # Guardar el archivo en el disco del servidor por bloques
    with open(ruta_destino, "wb") as buffer:
        while contenido := await file.read(1024 * 1024):  # Lee bloques de 1MB
            buffer.write(contenido)
    save_file(db, plan_id, file.filename, current_user.id)
    return {"mensaje": "Fichero subido con éxito", "nombre_archivo": file.filename, "plan_id": plan_id}

# ToDo: No permitir descargar ficheros si no se tiene permisos sobre ellos
@router.get("/download/{nombre_archivo}")
async def recuperar_fichero(nombre_archivo: str):
    ruta_fichero = os.path.join(CARPETA_DESTINO, nombre_archivo)
    
    if not os.path.exists(ruta_fichero):
        raise HTTPException(status_code=404, detail="El fichero no existe")
        
    return FileResponse(path=ruta_fichero, filename=nombre_archivo)


@router.get("/list_files/{plan_id}")
async def listar_ficheros(plan_id: int,db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return get_files_for_plan(db,plan_id)
    except Exception as e:
        logging.error(f"Error al listar ficheros para el plan {plan_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))