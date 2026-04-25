import json
from openai import AsyncOpenAI
from app.config import settings
from app.utils.prompt_templates import STRICT_GROUNDING_PROMPT

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def grounded_price_extraction(search_results: list, user_query: str):
    if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY == "your_openai_api_key_here":
        return {"results": [], "error": "OPENAI_API_KEY is missing or placeholder in .env"}

    if not settings.SERPER_API_KEY or settings.SERPER_API_KEY == "your_serper_api_key_here":
        return {"results": [], "error": "SERPER_API_KEY is missing or placeholder in .env"}

    try:
        search_text = "\n\n".join([
            f"Title: {r.get('title', '')}\nSnippet: {r.get('snippet', '')}\nURL: {r.get('link', '')}" 
            for r in search_results
        ])

        prompt = STRICT_GROUNDING_PROMPT.format(
            search_results=search_text,
            user_query=user_query
        )

        response = await client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result

    except Exception as e:
        return {"results": [], "error": f"LLM Error: {str(e)}"}