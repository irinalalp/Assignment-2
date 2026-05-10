from openai import OpenAI
from app.settings import settings

client = OpenAI(
    base_url=settings.openrouter_base_url,
    api_key=settings.openrouter_api_key
)

def translate_text(text: str, target_language: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are a translator. Translate the user's text to {target_language}. Reply with only the translated text, nothing else."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    response = completion.choices[0].message.content
    return response or "No translation returned"