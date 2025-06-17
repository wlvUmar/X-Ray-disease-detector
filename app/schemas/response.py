from pydantic import BaseModel, Field

class DiagnosisResponse(BaseModel):
    diagnosis: str = Field(..., description="The predicted diagnosis")
    confidence: float = Field(..., description="Confidence score of the prediction", ge=0, le=1)
    image_type: str = Field(..., description="Type of image (X-Ray or Skin)") 