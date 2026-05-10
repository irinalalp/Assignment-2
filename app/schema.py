from pydantic import BaseModel, Field

class TranslationInput(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=300
    )
    target_language: str

class TranslationResponse(BaseModel):
    translated: str