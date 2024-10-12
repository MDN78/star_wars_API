from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field, constr

'''Work rules with Pydantic - constract some functions'''


class People(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    height: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    mass: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    hair_color: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    skin_color: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    eye_color: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    birth_year: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    gender: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    homeworld: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    films: list[Annotated[str, Field(strict=True)]]
    species: list[Annotated[str, Field(strict=True)]]
    vehicles: list[Annotated[str, Field(strict=True)]]
    starships: list[Annotated[str, Field(strict=True)]]
    created: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    edited: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    url: Annotated[str, StringConstraints(min_length=1, max_length=100)]


class ListPeople(BaseModel):
    count: Annotated[int, Field(strict=True)]
    next: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    results: list[People]