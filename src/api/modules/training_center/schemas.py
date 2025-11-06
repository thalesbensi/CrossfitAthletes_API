from typing import Annotated

from fastapi.openapi.models import Schema
from pydantic import Field


class TrainingCenterSchema(Schema):
    name: Annotated[str, Field(max_length=20)]
    adress: Annotated[str, Field(max_length=20)]
    owner: Annotated[str, Field(max_length=20)]

    model_config = {
        "from_attributes": True
    }