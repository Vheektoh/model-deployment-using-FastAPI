# import libraries
import uvicorn
from fastapi import FastAPI
from basemodel import HeartFailVariable
import numpy as np
import pickle

#create app object
app = FastAPI()
pickle_in = open('mlp.pkl', 'rb')
model = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message' : 'welcome to my first API deployment'}

@app.get('/{name}/')
def get_name(name:str):
    return {'this was done by' : f'{name}'}

@app.post('/predict')
def predict_heart_disease(data:HeartFailVariable):
    # creating the mini database for the model
    data = data.dict()

    Age = data['Age']
    Sex = data['Sex']
    ChestPainType = ['ChestPainType']
    RestingBP = ['RestingBP']
    Cholesterol = data['Cholesterol']
    FastingBS = data['FastingBS']
    RestingECG = data['RestingECG']
    MaxHR = data['MaxHR']
    ExerciseAngina = data['ExerciseAngina']
    Oldpeak = data['Oldpeak']
    ST_Slope = data['ST_Slope']

    prediction = model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])
    if (prediction[0] > 0.5):
        prediction = 'Heart disease prone'
    else:
        prediction = 'Not prone to heart disease'
    return {
        'prediction': prediction
    }

# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host = 'localhost', port =8000)

# uvicorn main:app --reload 
# first param = file name(main)
# second param = object name(app)