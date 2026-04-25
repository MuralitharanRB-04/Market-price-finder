import json
from openai import AsyncOpenAI
from app.config import settings
from app.utils.prompt_templates import STRICT_GROUNDING_PROMPT

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def grounded_price_extraction(search_results: list, user_query: str):
    # Convert search results to readable text for LLM
    search_text = "\n\n".join([
        f"Title: {r['title']}\nSnippet: {r['snippet']}\nURL: {r['link']}" 
        for r in search_results
    ])

    prompt = STRICT_GROUNDING_PROMPT.format(
        search_results=search_text,
        user_query=user_query
    )

    response = await client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,          # Very important for consistency
        response_format={"type": "json_object"}
    )

    try:
        result = json.loads(response.choices[0].message.content)
        # Add source to each result
        for item in result.get("results", []):
            item["source_url"] = item.get("source_url") or "Not available"
        return result
    except:
        return {"results": [], "error": "Failed to parse LLM output"}