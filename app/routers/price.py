from fastapi import APIRouter, Query
from app.services.search_service import google_search_via_serper
from app.services.grounding_service import grounded_price_extraction

router = APIRouter()

@router.get("/search-price")
async def search_price(q: str = Query(..., description="Product to search (e.g. 'iPhone 15 128GB Seoul')")):
    # Step 1: Search
    raw_results = await google_search_via_serper(q)
    
    # Step 2: Grounded Extraction (No hallucination)
    grounded = await grounded_price_extraction(raw_results, q)
    
    return {
        "query": q,
        "search_results_count": len(raw_results),
        "grounded_results": grounded.get("results", []),
        "warning": "All prices are extracted ONLY from live search results. Always verify on the source URL."
    }