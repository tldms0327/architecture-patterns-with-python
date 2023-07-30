from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.constant import APIErrorStatusCode, APIPrefix
from src.custom import NotFoundException
from src.schema import (
    SearchResult,
    SearchResultHTTPResponse,
    SearchResultNotFoundHTTPResponse,
)
from src.service import DuckDuckGoAPI, SearchService

router: APIRouter = APIRouter()
search_client: DuckDuckGoAPI = DuckDuckGoAPI()
search_service: SearchService = SearchService(search_client=search_client)


@router.get(
    path=APIPrefix.SEARCH.value,
    response_model=SearchResultHTTPResponse,
    responses={
        APIErrorStatusCode.NOT_FOUND.value: {"model": SearchResultNotFoundHTTPResponse}
    },
    summary="검색 API",
    description="검색 대상이 되는 키워드 문자를 쿼리 매개변수로 활용하여 덕덕고 API를 통해 검색하는 API",
)
def search(
    keyword: Annotated[
        str,
        Query(
            min_length=2,
            max_length=10,
            title="검색 키워드",
            description="덕덕고 API를 활용하여 검색하기 위한 2글자 이상, 10글자 미만 키워드 문자",
            example="sausage",
        ),
    ]
) -> JSONResponse:
    try:
        result: list[SearchResult] = search_service.search(keyword=keyword)
        return JSONResponse(
            content={"data": jsonable_encoder(obj=result)},
            status_code=status.HTTP_200_OK,
        )

    except NotFoundException as not_found_execption:
        return JSONResponse(
            content={"detail": not_found_execption.json()},
            status_code=status.HTTP_404_NOT_FOUND,
        )
