from fastapi import FastAPI
from controllers.data_controller import load_data, preprocess_data
from controllers.predict_controller import predict

app = FastAPI()

@app.get("/data/all")
def get_all_data():
    return load_data().to_dict(orient="records")

@app.get("/data/clean")
def get_preprocessed_data():
    return preprocess_data(load_data()).to_dict(orient="records")

@app.get("/predict/")
def predict_api(sex: str, age: float, parch: int):
    sex_code = 0 if sex.lower() == "male" else 1
    return {"predicted_survival": int(predict(sex_code, age, parch))}