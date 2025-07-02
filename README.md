# Titanic Survival Prediction API
> A FastAPI service that predicts passenger survival probability using a trained neural network model.

### Project Structure
``` bash
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── src
    ├── inference.py
    ├── __init__.py
    ├── artifacts
    │   ├── best_model.keras
    │   └── preprocessor.joblib
    └── utils
        ├── config.py
        ├── request.py
        ├── response.py
        └── __init__.py
```
### Setup
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in the values

## Usage
Run the server:
```bash
uvicorn main:app --reload
```

#### The API will be available at `http://localhost:8000`
* Endpoints
    * GET /: Health check
    * POST /classify: Predict survival probability

### `Example Request`
``` bash
[
    {
        "passenger_id": 1,
        "age": 22.0,
        "fare": 7.25,
        "sex": "male",
        "embarked": "S",
        "parch": 0,
        "sibsp": 1,
        "pclass": 3
    },
    {
        "passenger_id": 2,
        "age": 29.0,
        "fare": 15.50,
        "sex": "female",
        "embarked": "C",
        "parch": 1,
        "sibsp": 0,
        "pclass": 2
    },
    {
        "passenger_id": 3,
        "age": 35.0,
        "fare": 50.00,
        "sex": "male",
        "embarked": "Q",
        "parch": 0,
        "sibsp": 0,
        "pclass": 1
    },
    {
        "passenger_id": 4,
        "age": 18.0,
        "fare": 5.00,
        "sex": "female",
        "embarked": "S",
        "parch": 2,
        "sibsp": 3,
        "pclass": 3
    },
    {
        "passenger_id": 5,
        "age": 42.0,
        "fare": 80.00,
        "sex": "male",
        "embarked": "C",
        "parch": 1,
        "sibsp": 0,
        "pclass": 1
    }
]
```