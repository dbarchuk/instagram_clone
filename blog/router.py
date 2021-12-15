from fastapi import APIRouter
from .schemas import Blog

router = APIRouter(
    tags=['blog'],
    prefix="/blog",
)


@router.post('/create/')
def create_post(blog: Blog):
    return {'data': blog}
