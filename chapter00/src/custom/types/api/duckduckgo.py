from typing import TypedDict

from pydantic import FilePath, HttpUrl


class SearchAPIRelatedTopicIcon(TypedDict):
    Height: str
    URL: FilePath
    Width: str


class SearchAPIRelatedTopic(TypedDict):
    FirstURL: HttpUrl
    Icon: SearchAPIRelatedTopicIcon
    Result: str
    Text: str


class SearchAPIDeveloper(TypedDict):
    name: str
    type: str
    url: str


class SearchAPIMaintainer(TypedDict):
    github: str


class SearchAPISRCOption(TypedDict):
    directory: str
    is_fanon: int
    is_mediawiki: int
    is_wikipedia: int
    language: str
    min_abstract_length: str
    skip_abstract: int
    skip_abstract_paren: int
    skip_end: str
    skip_icon: int
    skip_image_name: int
    skip_qr: str
    source_skip: str
    src_info: str


class SearchAPIMeta(TypedDict):
    attribution: str | None
    blockgroup: str | None
    created_date: str | None
    description: str
    designer: str | None
    dev_date: str | None
    dev_milestone: str
    developer: list[SearchAPIDeveloper]
    example_query: str
    id: str
    is_stackexchange: str | None
    js_callback_name: str
    live_date: str | None
    maintainer: SearchAPIMaintainer
    name: str
    perl_module: str
    producer: str | None
    production_state: str
    repo: str
    signal_from: str
    src_domain: str
    src_id: int
    src_name: str
    src_options: SearchAPISRCOption
    src_url: str | None
    status: str
    tab: str
    topic: list[str]
    unsafe: int


class SearchAPIResponse(TypedDict):
    Abstract: str
    AbstractSource: str
    AbstractText: str
    AbstractURL: str
    Answer: str
    AnswerType: str
    Definition: str
    DefinitionSource: str
    DefinitionURL: str
    Entity: str
    Heading: str
    Image: str
    ImageHeight: int
    ImageIsLogo: int
    ImageWidth: int
    Infobox: str
    Redirect: str
    RelatedTopics: list[SearchAPIRelatedTopic]
    Results: list[str]
    Type: str
    meta: SearchAPIMeta
