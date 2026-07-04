from fastapi import HTTPException, status

def raise_expired_token():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token has expired",
        headers={"WWW-Authenticate": "Bearer"},
    )

def raise_forbidden_exc():
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access forbidden",
        headers={"WWW-Authenticate": "Bearer"},
    )

def raise_credentials_exc():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )