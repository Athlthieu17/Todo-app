from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Path
import schemas
from models import Users
from database import get_db
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix= '/users',
    tags= ['users']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/information", status_code= status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None or user.get('role') == 'admin':
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = 'Authentication Failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put("/change_password}", status_code= status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: schemas.UsersVerification):
    if user is None:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = 'Authentication Failed')

    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = 'Error on changed password')

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)

    db.add(user_model)
    db.commit()
    db.refresh(user_model)

@router.put("/phone_number/{phone_number}", status_code= status.HTTP_204_NO_CONTENT)
async def change_phone_number(user: user_dependency, db: db_dependency, phone_number : str):
    if user is None:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = 'Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    user_model.phone_number = phone_number
    db.add(user_model)
    db.commit()



