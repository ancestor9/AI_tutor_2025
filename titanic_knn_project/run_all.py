from models.db import init_db
from controllers.predict_controller import train_model

if __name__ == "__main__":
    print("🔄 Initializing database and training model...")
    init_db()
    train_model()
    print("✅ Done.")