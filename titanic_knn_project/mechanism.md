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
```---

# 🧠 Titanic KNN 생존 예측 프로젝트 - 실행 가이드

이 프로젝트는 Seaborn의 Titanic 데이터를 활용하여 생존 여부를 예측하는 시스템입니다.  
MVC 구조를 기반으로 FastAPI와 Gradio UI를 함께 제공합니다.

---

## ✅ 1. 패키지 설치
```bash
pip install -r requirements.txt
```

---

## ✅ 2. 데이터베이스 생성 및 모델 학습
```bash
python run_all.py
```
- `seaborn` Titanic 데이터 로드
- SQLite DB(`data/titanic.db`)로 저장
- `KNN 모델` 학습

---

## ✅ 3. FastAPI 실행 (API 확인용)
```bash
python app.py
```

- Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 주요 엔드포인트:
  - `/data/all`: 전체 원본 데이터
  - `/data/clean`: 전처리된 데이터
  - `/predict/?sex=male&age=22&parch=0`: 예측 결과 반환 (0: 사망, 1: 생존)

---

## ✅ 4. Gradio UI 실행 (웹 예측 인터페이스)
```bash
python gradio_app.py
```

- 로컬 주소: `http://127.0.0.1:7860`
- 외부 공개 주소: `https://xxxx.gradio.live` (자동 출력됨)
- 사용자는 `성별 / 나이 / 자녀 수`를 입력하고 생존 여부를 예측할 수 있음

---

## 🗂️ 전체 실행 흐름 요약

```plaintext
run_all.py
 ├── models/db.py              (DB 초기화)
 └── controllers/predict_controller.py
     └── models/knn_model.py   (KNN 학습/예측)

gradio_app.py
 ├── run_all.py                (학습 포함)
 └── views/gradio_view.py      (UI 실행)

app.py
 └── views/api_view.py         (FastAPI 서버)
```

---

## 💡 팁
- `run_all.py`는 학습 초기화를 포함하므로 Gradio 또는 API 실행 전 필수입니다.
- Gradio는 `share=True`를 통해 외부 공유 가능하게 설정되어 있습니다.

---