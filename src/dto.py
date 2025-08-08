from pydantic import BaseModel, Field


class ImagePositionRequestDto(BaseModel):
    img: str = Field(..., description="Base64 encoded image string")


class CoordinateResponse(BaseModel):
    longitude: float
    latitude: float
