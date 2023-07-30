from pydantic import BaseModel, Field, HttpUrl
from src.schema.base_error import BaseError


class SearchResult(BaseModel):
    firstURL: HttpUrl = Field(
        default=...,
        title="검색 결과 조회 URL",
        description="실제 덕덕고 웹 브라우저에서 확인할 수 있는 검색 결과 조회 URL",
        examples=["https://duckduckgo.com/dachshund"],
    )
    text: str = Field(
        default=...,
        title="검색 결과 설명 텍스트",
        description="어떤 키워드를 검색했는지 설명해주는 간단한 텍스트",
        examples=["Sausage dog A short-legged, long-bodied, hound-type dog breed."],
    )


class SearchResultHTTPResponse(BaseModel):
    data: list[SearchResult] = Field(
        default=...,
        title="키워드 검색 결과 응답",
        description="덕덕고 API를 활용하여 특정 키워드에 대한 검색 결과 응답",
    )


class SearchResultNotFoundHTTPResponse(BaseModel):
    detail: BaseError = Field(
        default=...,
        title="존재하지 않는 키워드 검색 응답",
        description="키워드 검색 결과를 찾을 수 없는 경우에 대한 응답",
        examples=[
            {
                "loc": ["keyword"],
                "msg": "keyword duck does not exist",
                "type": "not_found",
            }
        ],
    )
