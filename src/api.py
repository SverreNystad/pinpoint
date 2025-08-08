from fastapi import FastAPI
from loguru import logger
from src.dto import ImagePositionRequestDto, CoordinateResponse

app = FastAPI()


@app.post("/predict")
def predict(request: ImagePositionRequestDto) -> CoordinateResponse:
    """
    Endpoint to predict coordinates based on an image input.
    Args:
        request (ImagePositionRequestDto): The request containing the image data.
    Returns:
        CoordinateResponse: The predicted coordinates.
    """
    # TODO: Implement actual prediction logic here
    logger.info(f"Received prediction request with image data. {request.img}")
    return CoordinateResponse(longitude=12.34, latitude=56.78)
