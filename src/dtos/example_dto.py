from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ExampleDto(BaseModel):
    id: str
    test: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
