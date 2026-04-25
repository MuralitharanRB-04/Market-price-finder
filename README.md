# Market-price-finder

Hallucination-Proof Price Retrieval System for international students.

## Architecture (Anti-Hallucination)
1. User query → Serper/Google Search (live results only)
2. Raw search results injected into LLM prompt
3. Strict extraction prompt + temperature=0 + JSON mode
4. Every price comes with `source_url`

Never lets LLM invent prices.

## Tech Stack
- FastAPI
- Serper.dev (search)
- OpenAI (grounded extraction)
- Zen Minimalist UI (as per brand)

## Next Phases
- Automated expense tracking
- Currency optimization
- Bank integration