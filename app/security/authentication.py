import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()



def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    """Takes Username and Password as input from users and confirms it is correct

    Args:
        credentials (HTTPBasicCredentials, optional): _description_. Defaults to Depends(security).

    Raises:
        HTTPException: Raises an exception when credentials are invalid
    """
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"Johnny"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"Done"

    #Compare the imputed user to the one stored
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )