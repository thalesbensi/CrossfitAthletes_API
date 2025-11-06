from typing import Annotated

from pydantic import BaseModel, Field, PositiveFloat


class AthleteSchema(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    cpf: Annotated[str, Field(max_length=11)]
    age: Annotated[int]
    weight: Annotated[PositiveFloat]
    height: Annotated[PositiveFloat]
    gender = Annotated[str, Field(max_length=1)]
    category_id = Annotated[str, Field(max_length=1)]

    model_config = {
        "from_attributes": True
    }
