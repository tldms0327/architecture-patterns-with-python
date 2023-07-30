from src.schema import BaseError


class NotFoundException(Exception):
    def __init__(self, model: BaseError) -> None:
        self.model: BaseError = model

    def json(self) -> dict[str, str | list[str]]:
        return self.model.model_dump()
