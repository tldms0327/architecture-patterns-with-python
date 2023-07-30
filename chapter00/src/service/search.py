from src.constant import ErrorType
from src.custom import NotFoundException, SearchAPIRelatedTopic
from src.schema import BaseError, SearchResult
from src.service.api import DuckDuckGoAPI


class SearchService:
    def __init__(self, search_client: DuckDuckGoAPI) -> None:
        self.search_client: DuckDuckGoAPI = search_client

    def _has_result(self, related_topics: list[SearchAPIRelatedTopic]) -> bool:
        if not related_topics:
            return False
        return True

    def search(self, keyword: str) -> list[SearchResult]:
        related_topics: list[SearchAPIRelatedTopic] = self.search_client.search(
            keyword=keyword
        ).get("RelatedTopics")
        if not self._has_result(related_topics=related_topics):
            raise NotFoundException(
                model=BaseError(
                    loc=["keyword"],
                    msg=f"keyword {keyword} does not exist",
                    type=ErrorType.NOT_FOUND.value,
                )
            )

        return [
            SearchResult(
                firstURL=related_topic.get("FirstURL"), text=related_topic.get("Text")
            )
            for related_topic in related_topics
        ]
