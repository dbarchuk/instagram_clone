from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.database import get_db
from .schemas import UserBase, UserDisplay
from . import db_users

router = APIRouter(
    tags=['users'],
    prefix="/users",
)


@router.get('')
def show_users():
    return {'detail': 'list of users'}


@router.post('/', response_model=UserDisplay, status_code=201)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_users.create_user(db, request)
