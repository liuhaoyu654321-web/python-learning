from pydantic import BaseModel,Field


class AIResponse(BaseModel):

    summary: str

    category: str

    urgent: bool

    confidence: float = Field(ge=0, le=1)