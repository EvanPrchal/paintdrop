from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from passlib.context import CryptContext

from app.database import get_db
from app.models import Color, User, UserSchemeLink
from app.schemas import CreateColorRequest, CreateUserRequest, UpdateUserRequest

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"])

### GET ###
@router.get("")
def get_users(db: Session = Depends(get_db)) -> list[User]:
    return db.exec(select(User)).all()

@router.get("/{username}")
def get_user(username: str, db: Session = Depends(get_db)) -> User:
    user: User | None = db.get(User, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username: {username} not found")
    return user

### POST ###
@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(create_user_request: CreateUserRequest, db: Session = Depends(get_db)) -> None:
    hashed_password: str = pwd_context.hash(create_user_request.password)
    user: User = User(**create_user_request.model_dump(), hashed_password=hashed_password)
    db.add(user)
    db.commit()
    return None

### PATCH ###
@router.patch("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def update_user(update_user_request: UpdateUserRequest, username: str, db: Session = Depends(get_db)) -> None:
    user: User | None = db.get(User, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username: {username} not found")
    if update_user_request.hashed_password:
        update_user_request.hashed_password = pwd_context.hash(update_user_request.hashed_password)
    for k, v in update_user_request.model_dump(exclude_unset=True).items():
        setattr(user, k, v)
    db.commit()
    return None

@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(username: str, db: Session = Depends(get_db)) -> None:
    raise NotImplementedError
    user: User | None = db.get(User, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username: {username} not found")
    db.delete(user)
    db.commit()
    return None