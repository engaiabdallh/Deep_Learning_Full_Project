from pydantic import BaseModel
from typing import Literal, List

class PassengerPrediction(BaseModel):
    passenger_id: int
    predicted: Literal["survived", "not survived"]


class PredictionResponse(BaseModel):
    predictions: List[PassengerPrediction]

