from datetime import datetime
from decimal import Decimal
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field, constr


class Films(BaseModel):
    title: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    episode_id: Annotated[int, Field(strict=True)]
    opening_crawl: Annotated[str, StringConstraints(min_length=1, max_length=5000)]
    director: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    producer: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    release_date: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    characters: list[Annotated[str, Field(strict=True)]]
    planets: list[Annotated[str, Field(strict=True)]]
    starships: list[Annotated[str, Field(strict=True)]]
    vehicles: list[Annotated[str, Field(strict=True)]]
    species: list[Annotated[str, Field(strict=True)]]
    created: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    edited: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    url: Annotated[str, StringConstraints(min_length=1, max_length=100)]


class ListFilms(BaseModel):
    count: Annotated[int, Field(strict=True)]
    # next: bool
    # previous: Annotated[bool, Field(strict=True)]
    results: list[Films]
