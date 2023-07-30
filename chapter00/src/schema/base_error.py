from pydantic import BaseModel, Field


class BaseError(BaseModel):
    loc: list[str]
    msg: str
    type: str
