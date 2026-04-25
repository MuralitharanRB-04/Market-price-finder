import httpx
from app.config import settings

async def google_search_via_serper(query: str, num_results: int = 10):
    url = "https://google.serper.dev/search"
    payload = {
        "q": query,
        "num": num_results
    }
    headers = {
        'X-API-KEY': settings.SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for item in data.get("organic", [])[:10]:
            results.append({
                "title": item.get("title"),
                "snippet": item.get("snippet"),
                "link": item.get("link"),
                "price": None  # will be extracted by LLM
            })
        return results