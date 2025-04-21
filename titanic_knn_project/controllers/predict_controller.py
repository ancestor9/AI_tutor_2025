from models.knn_model import KNNPredictor
from .data_controller import load_data, preprocess_data

predictor = KNNPredictor()

def train_model():
    df = load_data()
    clean_df = preprocess_data(df)
    print(f'predict_controller.py > train_model > {clean_df.isnull().sum()}')  # 결측치 확인
    predictor.train(clean_df)

def predict(sex, age, parch):
    return predictor.predict(sex, age, parch)