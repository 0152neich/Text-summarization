from shared.base import BaseModel

class APIInput(BaseModel):
    text: str

class APIOutput(BaseModel):
    text: str