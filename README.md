

# API Test Automation with pytest and FastAPI

## Getting Started

### Prerequisites

Before running the tests, you need to have the following prerequisites installed on your system:

- Python 3.6+
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/almeidaleo1995/ApiTestsPytest.git

2. Navigate to the project directory:

   ```bash
   cd ApiTestsPytest

3. Create a virtual environment (optional but recommended):
    ```bash
     python -m venv venv

4. Activate the virtual environment:

    On Windows:
    ```bash
    venv\Scripts\activate

On Linux/Mac:

     source venv/bin/activate


5. Install the project dependencies:
    ```bash
     pip install -r requirements.txt

6. Run Server API (optional):
    ```bash
     uvicorn main:app --reload

Swagger API

      http://127.0.0.1:8000/docs

7. Running the Tests:
    ```bash
     pytest tests\api\test_main.py

## Configuration     
You can configure the test environment and parameters in the pytest.ini file.

## Contributing     
If you would like to contribute to this project, please follow the standard GitHub workflow:

1.Fork the repository.

2.Create a new branch for your feature or bug fix.

3.Make your changes and commit them.

4.Push your changes to your fork.

5.Create a pull request to the main repository.

## Acknowledgments  
FastAPI: https://fastapi.tiangolo.com/

pytest: https://docs.pytest.org/en/latest/

TestClient: https://fastapi.tiangolo.com/tutorial/testing/
