import pandas as pd
from typing import List
from .utils.request import PassengerData
from .utils.response import PassengerPrediction, PredictionResponse
from .utils.config import model, preprocessor


def predict_survival(passengers: List[PassengerData]):
    
    # base data
    base_data = [p.model_dump() for p in passengers]
    
    # Add computed properties
    for i, p in enumerate(passengers):
        base_data[i]["family_size"] = p.family_size
        base_data[i]["is_alone"] = p.is_alone
    
    # To DF for all columns
    df = pd.DataFrame(base_data)
    
    df_processed = preprocessor.transform(df)
    predictions = (model.predict(df_processed) > 0.5).astype("int32")

    pred_response = PredictionResponse(predictions=[
        PassengerPrediction(
            passenger_id=passenger.passenger_id,
            predicted="survived" if pred == 1 else "not survived"
        ) 
        for passenger, pred in zip(passengers, predictions.flatten())
    ])

    return pred_response
