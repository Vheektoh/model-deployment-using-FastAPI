from pydantic import BaseModel
# Class variables which describes the heart failure

class HeartFailVariable(BaseModel):
    Age:int
    Sex:int
    ChestPainType:int
    RestingBP:int
    Cholesterol:int
    FastingBS:int
    RestingECG:int
    MaxHR:int
    ExerciseAngina:int
    Oldpeak:float
    ST_Slope:int 