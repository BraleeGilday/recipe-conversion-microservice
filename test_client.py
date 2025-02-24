import requests

url = 'http://127.0.0.1:8000'

# data		Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url
# json		Optional. A JSON object to send to the specified url


request1 = {
    "ingredients": [
        {"name": "frozen pound cake", "quantity": 1, "unit": "package"},
        {"name": "sugar", "quantity": 2, "unit": "cup"},
        {"name": "boiling water", "quantity": 3 / 4, "unit": "cup"},
        {"name": "cold water", "quantity": 1 / 4, "unit": "cup"},
        {"name": "semi-sweet chocolate", "quantity": 1, "unit": "ounce"},
        {"name": "Thawed Cool Whip", "quantity": 2, "unit": "cups"},
        {"name": "Cherry Pie Filling", "quantity": 1 + 1 / 2, "unit": "cups"},
    ],
    "serving_size": 3
}


response = requests.post(url+'/conversion', json=request1)

# Check if the request was successful and print the response
if response.status_code == 200:
    print("Response from microservice:")
    print(response.json())  # Print the converted ingredients data
else:
    print(f"Error: {response.status_code}")
