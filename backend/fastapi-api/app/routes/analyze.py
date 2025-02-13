from fastapi import APIRouter, Request
from app.utils.preprocess import preprocess_text
from app.models.fraud_model import heuristic_score

router = APIRouter()

@router.post("/analyze")
async def analyze_text(request: Request):
    data = await request.json()  # Directly parse incoming JSON

    nft_metadata = data.get("nft_metadata", {})  # Ensure it's a dictionary
    description = data.get("description", "")
    print("nft_metadata python", nft_metadata)
    print("description python",description)
    # Process the received data
    processed_text = heuristic_score(nft_metadata, description)

    return {"processed": processed_text}