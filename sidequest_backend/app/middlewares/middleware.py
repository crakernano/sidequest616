import time
import uuid
import logging

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

def register_middlewares(app:FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start
        response.headers["X-Process-Time"] = f"{process_time:.4f}s"
        return response

    @app.middleware("http")
    async def log_request(request: Request, call_next):
        logging.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logging.info(f"Response: {response.status_code} for {request.method} {request.url}")
        return response
    
    @app.middleware("http")
    async def add_request_id_header(request: Request, call_next):
        request_id = str(uuid.uuid4())
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
    
    @app.middleware("http")
    async def block_ip_middleware(request: Request, call_next):
        #ToDo: Obtener la BLACKLIST desde la base de datos
        BLACKLIST = {}
        client_ip = request.client.host
        if client_ip in BLACKLIST:
            logging.warning(f"Blocked request from IP: {client_ip}")
            raise HTTPException(status_code=403, detail="IP address blocked")
        return await call_next(request)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        )