from pydantic import BaseModel
from typing import Literal


class PassengerData(BaseModel):
    passenger_id: int
    age: float
    fare: float
    sex: Literal["male", "female"]
    embarked: Literal['S', 'C', 'Q']
    parch: int
    sibsp: int
    pclass: int

    @property
    def family_size(self) -> int:
        return self.parch + self.sibsp + 1
    
    @property
    def is_alone(self) -> int:
        return 1 if self.family_size == 1 else 0


