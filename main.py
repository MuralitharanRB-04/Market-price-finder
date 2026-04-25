<<<<<<< Updated upstream
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.price import router as price_router

app = FastAPI(title="Meika - AI Price Finder (Hallucination-Proof)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(price_router, prefix="/api/v1", tags=["price"])

@app.get("/")
async def root():
    return {
        "message": "Meika Price Finder MVP - Hallucination-Proof",
        "status": "running",
        "documentation": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
=======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.price import router as price_router

app = FastAPI(title="Meika - AI Price Finder (Hallucination-Proof)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(price_router, prefix="/api/v1", tags=["price"])

@app.get("/")
async def root():
    return {
        "message": "Meika Price Finder MVP - Hallucination-Proof",
        "status": "running",
        "documentation": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
>>>>>>> Stashed changes
    uvicorn.run(app, host="0.0.0.0", port=8000)