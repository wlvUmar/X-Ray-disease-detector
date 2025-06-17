from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.model_service import ModelService
from app.schemas.response import DiagnosisResponse

router = APIRouter()
model_service = ModelService()

@router.post("/diagnose", response_model=DiagnosisResponse)
async def diagnose_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        result = await model_service.predict(file)
        return DiagnosisResponse(
            diagnosis=result["diagnosis"],
            confidence=result["confidence"],
            image_type=result["image_type"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 