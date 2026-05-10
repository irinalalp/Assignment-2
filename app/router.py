from fastapi import APIRouter
from app.schema import TranslationInput, TranslationResponse
from app.service import translate_text

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
def translate(body: TranslationInput):
    result = translate_text(body.text, body.target_language)
    return TranslationResponse(translated=result)