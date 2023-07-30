from fastapi import APIRouter

from src.router import search

router: APIRouter = APIRouter()

router.include_router(router=search.router, tags=["검색 API"])
