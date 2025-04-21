# Titanic KNN Project (MVC + FastAPI + Gradio)

## 📁 구조
- `models/`: DB 연결, 모델 학습
- `controllers/`: 데이터 전처리, 예측 로직
- `views/`: FastAPI + Gradio UI
- `run_all.py`: 전체 초기화 및 학습 스크립트

## 🚀 실행 방법

### 1. 패키지 설치
```
pip install -r requirements.txt
```

### 2. DB 및 모델 학습
```
python run_all.py
```

### 3. FastAPI 실행
```
python app.py
# http://127.0.0.1:8000/docs 에서 API 확인
```

### 4. Gradio UI 실행
```
python gradio_app.py
```