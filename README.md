# Microservice: Recipe Conversion
## Description:
This is a FastAPI-based microservice that provides ingredient scaling and unit conversions via a REST API.
It allows users to:
- Scale a recipe up or down based on serving size.
- Convert ingredient units between metric and customary systems.
- Perform both operations in a single request.

## Installation
1. Setup Python Environment
   - Clone the repository:
        git clone <repo_url>
        cd recipe-conversion-microservice

   - Create and activate virtual environment:
     - Windows: 
        python -m venv venv
        venv\Scripts\activate
     - Mac/Linux: 
        python -m venv venv
        source venv/bin/activate

   - Install dependencies:
        pip install -r requirements.txt

2. Run the Microservice
   - Start the FastAPI server:
        uvicorn app.main:api --reload
     - The microservice will now be running at:
        http://127.0.0.1:8080
     
## Communication Contract
### A. How to programmatically REQUEST data from the microservice:
Example Call:

      import requests
  
      url = 'http://127.0.0.1:8000'
      headers = {"Content-Type": "application/json"}
    
      data = {
        "ingredients": [
            {"name": "flour", "quantity": 2, "unit": "cup"},
            {"name": "sugar", "quantity": 4, "unit": "tablespoon"},
            {"name": "cherry pie filling", "quantity": 1, "unit": "package"},
        ],
        "serving_size": 2,                   # (Optional) That is, scale the recipe by 2. 
        "conversion_system": "customary"     # (Optional) or "metric", based on user's choice
      }

      # Send the POST request
      response = requests.post(url, json=data, headers=headers)

      # Check if the request was successful
      if response.status_code == 200:
         print(response.json()) 
      else:
         print(f"Error: {response.status_code}")

### B. How to programmatically RECEIVE data from the microservice:


    Example Call:

### C. UML Sequence diagram: 