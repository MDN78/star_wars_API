from decimal import Decimal
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field

'''Work rules with Pydantic - constract some functions'''


class Starships(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    model: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    starship_class: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    manufacturer: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    cost_in_credits: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    length: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    crew: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    passengers: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    max_atmosphering_speed: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    hyperdrive_rating: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    MGLT: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    cargo_capacity: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    consumables: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    films: list[Annotated[str, Field(strict=True)]]
    pilots: list[Annotated[str, Field(strict=True)]]
    url: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    created: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    edited: Annotated[str, StringConstraints(min_length=1, max_length=100)]


class ListStarships(BaseModel):
    count: Annotated[int, Field(strict=True)]
    next: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    # previous: Annotated[str, Field(allow_inf_nan=None)]
    # previous: bool
    results: list[Starships]
