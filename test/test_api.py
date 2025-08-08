from fastapi.testclient import TestClient

from src.api import app
from src.dto import ImagePositionRequestDto, CoordinateResponse

client = TestClient(app)


def test_prediction_endpoint():
    """
    Test the prediction endpoint with a sample input.
    """

    request = ImagePositionRequestDto(img="base64_encoded_image_string")

    response = client.post(
        "/predict",
        json=request.model_dump(),
    )
    assert response.status_code == 200
    response_data = CoordinateResponse.model_validate(response.json())
    assert isinstance(response_data.longitude, float)
    assert isinstance(response_data.latitude, float)
