from fastapi.testclient import TestClient

from .main import api

# Adapted from https://fastapi.tiangolo.com/tutorial/testing/#testing-file
client = TestClient(api)


def test_health_check():
    response = client.post("/conversion", json={})
    assert response.status_code == 422  # Unprocessable


# Valid conversion request (scaling only)
def test_conversion_scaling():
    response = client.post(
        "/conversion",
        json={
            "ingredients": [
                {"name": "flour", "quantity": 200, "unit": "grams"},
                {"name": "sugar", "quantity": 150, "unit": "grams"}
            ],
            "serving_size": 2
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {"name": "flour", "quantity": 400, "unit": "grams"},
        {"name": "sugar", "quantity": 300, "unit": "grams"}
    ]

# Valid conversion request (unit conversion only)


# Valid request with both scaling and unit conversion


# Missing required fields


# Invalid data types


# Negative or zero quantities
