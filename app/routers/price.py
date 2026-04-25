from fastapi import APIRouter, Query, HTTPException
from app.services.search_service import google_search_via_serper
from app.services.grounding_service import grounded_price_extraction

router = APIRouter()

@router.get("/search-price")
async def search_price(q: str = Query(..., min_length=2, description="Product name to search for")):
    try:
        raw_results = await google_search_via_serper(q)
        grounded = await grounded_price_extraction(raw_results, q)
        
        return {
            "query": q,
            "results": grounded.get("results", []),
            "search_results_count": len(raw_results),
            "note": "All prices are grounded from live search results only. Always verify on source URL."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))