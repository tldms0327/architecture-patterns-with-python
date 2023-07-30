from pydantic import HttpUrl
from requests import Response, Session  # type: ignore
from src.custom import SearchAPIResponse


class DuckDuckGoAPI:
    _SEARCH_FORMAT: str = "json"
    _SEARCH_API_URL: HttpUrl = "http://api.duckduckgo.com/?q="

    def __init__(self) -> None:
        self.session: Session = Session()

    def search(self, keyword: str) -> SearchAPIResponse:
        api_url: HttpUrl = "".join(
            [
                DuckDuckGoAPI._SEARCH_API_URL,
                keyword,
                f"&format={DuckDuckGoAPI._SEARCH_FORMAT}",
            ]
        )
        response: Response = self.session.get(url=api_url)
        if response.ok:
            return response.json()
