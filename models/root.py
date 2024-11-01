from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field, constr


class Root(BaseModel):
    films: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    people: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    planets: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    species: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    starships: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    vehicles: Annotated[str, StringConstraints(min_length=1, max_length=100)]
