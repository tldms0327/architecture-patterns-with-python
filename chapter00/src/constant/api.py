from enum import Enum


class APIPrefix(str, Enum):
    SEARCH: str = "/search"


class APIErrorStatusCode(Enum):
    NOT_FOUND: int = 404
