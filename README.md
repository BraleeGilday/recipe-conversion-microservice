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
     ```
        git clone https://github.com/BraleeGilday/recipe-conversion-microservice.git
        cd recipe-conversion-microservice
     ```

   - Create and activate virtual environment:
     - Windows: 
        ```
        python -m venv venv
        venv\Scripts\activate
        ```
     - Mac/Linux:
       ```
        python -m venv venv
        source venv/bin/activate
       ```
   - Install dependencies: `pip install -r requirements.txt`

2. Run the Microservice
   - Start the FastAPI server:
        `uvicorn app.main:api --reload`
   - The microservice will now be running at:
        `http://127.0.0.1:8080`
     
## Communication Contract
### A. How to programmatically REQUEST data from the microservice:
    
    Example Call:
    

### B. How to programmatically RECEIVE data from the microservice:


    Example Call:

### C. UML Sequence diagram: 
