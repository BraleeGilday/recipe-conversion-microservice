from fastapi.testclient import TestClient

from .main import api

# Adapted from https://fastapi.tiangolo.com/tutorial/testing/#testing-file
client = TestClient(api)


def test_health_check():
    response = client.post("/conversion", json={})
    assert response.status_code == 422  # Unprocessable


# Valid conversion request (scaling only)
def test_conversion_scaling_up():
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


def test_conversion_system_up_mixed():
    response = client.post(
        "/conversion",
        json={
            "ingredients": [
                {"name": "frozen pound cake", "quantity": 1, "unit": "package"},
                {"name": "sugar", "quantity": 2, "unit": "cup"},
                {"name": "boiling water", "quantity": 3/4, "unit": "cup"},
                {"name": "cold water", "quantity": 1/4, "unit": "cup"},
                {"name": "semi-sweet chocolate", "quantity": 1, "unit": "ounce"},
                {"name": "Thawed Cool Whip", "quantity": 2, "unit": "cups"},
                {"name": "Cherry Pie Filling", "quantity": 1 + 1/2, "unit": "cups"},
            ],
            "serving_size": 3
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {"name": "frozen pound cake", "quantity": 3, "unit": "package"},
        {"name": "sugar", "quantity": 6, "unit": "cup"},
        {"name": "boiling water", "quantity": 2.25, "unit": "cup"},
        {"name": "cold water", "quantity": .75, "unit": "cup"},
        {"name": "semi-sweet chocolate", "quantity": 3, "unit": "ounce"},
        {"name": "Thawed Cool Whip", "quantity": 6, "unit": "cups"},
        {"name": "Cherry Pie Filling", "quantity": 4.5, "unit": "cups"},
    ]


# Valid conversion request (scaling only)
def test_conversion_scaling_down():
    response = client.post(
        "/conversion",
        json={
            "ingredients": [
                {"name": "flour", "quantity": 200, "unit": "grams"},
                {"name": "sugar", "quantity": 150, "unit": "grams"}
            ],
            "serving_size": 0.5
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {"name": "flour", "quantity": 100, "unit": "grams"},
        {"name": "sugar", "quantity": 75, "unit": "grams"}
    ]


# Valid conversion request (unit conversion only)
def test_conversion_system_1():
    response = client.post(
        "/conversion",
        json={
            "ingredients": [
                {"name": "flour", "quantity": 200, "unit": "grams"},
                {"name": "sugar", "quantity": 150, "unit": "grams"}
            ],
            "conversion_system": "customary"
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {"name": "flour", "quantity": 7.05, "unit": "ounce"},
        {"name": "sugar", "quantity": 5.29, "unit": "ounce"}
    ]


# Valid conversion request (unit conversion only)
def test_conversion_system_2():
    response = client.post(
        "/conversion",
        json={
            "ingredients": [
                {"name": "frozen pound cake", "quantity": 1, "unit": "package"},
                {"name": "sugar", "quantity": 2, "unit": "cup"},
                {"name": "boiling water", "quantity": 3/4, "unit": "cup"},
                {"name": "cold water", "quantity": 1/4, "unit": "cup"},
                {"name": "semi-sweet chocolate", "quantity": 1, "unit": "ounce"},
                {"name": "Thawed Cool Whip", "quantity": 2, "unit": "cups"},
                {"name": "Cherry Pie Filling", "quantity": 1 + 1/2, "unit": "cups"},
            ],
            "conversion_system": "metric"
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {"name": "frozen pound cake", "quantity": 1, "unit": "package"},
        {"name": "sugar", "quantity": 473.18, "unit": "mL"},
        {"name": "boiling water", "quantity": 177.44, "unit": "mL"},
        {"name": "cold water", "quantity": 59.15, "unit": "mL"},
        {"name": "semi-sweet chocolate", "quantity": 28.35, "unit": "g"},
        {"name": "Thawed Cool Whip", "quantity": 473.18, "unit": "mL"},
        {"name": "Cherry Pie Filling", "quantity": 354.88, "unit": "mL"},
    ]


# Valid request with both scaling and unit conversion
def test_conversion_both_1():
    response = client.post(
        "/conversion",
        json={
            "ingredients": [
                {"name": "frozen pound cake", "quantity": 1, "unit": "package"},
                {"name": "sugar", "quantity": 2, "unit": "cup"},
                {"name": "boiling water", "quantity": 3/4, "unit": "cup"},
                {"name": "cold water", "quantity": 1/4, "unit": "cup"},
                {"name": "semi-sweet chocolate", "quantity": 1, "unit": "ounce"},
                {"name": "Thawed Cool Whip", "quantity": 2, "unit": "cups"},
                {"name": "Cherry Pie Filling", "quantity": 1 + 1/2, "unit": "cups"},
            ],
            "serving_size": 2,
            "conversion_system": "metric"
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {"name": "frozen pound cake", "quantity": 2, "unit": "package"},
        {"name": "sugar", "quantity": 946.35, "unit": "mL"},
        {"name": "boiling water", "quantity": 354.88, "unit": "mL"},
        {"name": "cold water", "quantity": 118.29, "unit": "mL"},
        {"name": "semi-sweet chocolate", "quantity": 56.7, "unit": "g"},
        {"name": "Thawed Cool Whip", "quantity": 946.35, "unit": "mL"},
        {"name": "Cherry Pie Filling", "quantity": 709.76, "unit": "mL"},
    ]


# Missing required fields

# Invalid data types

# Negative or zero quantities
