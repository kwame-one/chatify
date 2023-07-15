from pydantic import BaseModel, constr


class ExampleRequest(BaseModel):
    test: constr(strip_whitespace=True, min_length=1)
