from fastapi import APIRouter
from api.auth import router as auth_router
from api.articles import router as articles_router

router = APIRouter()

router.include_router(auth_router, prefix="/users")
router.include_router(articles_router, prefix="/articles")