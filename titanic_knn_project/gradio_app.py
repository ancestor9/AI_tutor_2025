from models.db import init_db
from controllers.predict_controller import train_model
from views.gradio_view import build_ui

if __name__ == "__main__":
    print("🔄 DB 초기화 및 모델 학습 중...")
    init_db()
    train_model()
    print("✅ 학습 완료. Gradio UI 실행 중...")
    build_ui()
