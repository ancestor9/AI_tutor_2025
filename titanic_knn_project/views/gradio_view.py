import gradio as gr
from controllers.predict_controller import predict

def predict_interface(sex, age, parch):
    try:
        sex_code = 0 if sex == "male" else 1
        age = float(age)
        parch = int(parch)
        result = predict(sex_code, age, parch)
        return "생존" if result == 1 else "사망"
    except Exception as e:
        return f"❌ 예측 중 오류 발생: {str(e)}"

def build_ui():
    interface = gr.Interface(
        fn=predict_interface,
        inputs=[
            gr.Radio(["male", "female"], label="성별"),
            gr.Slider(0, 80, step=1, label="나이"),
            gr.Slider(0, 5, step=1, label="자녀 수(parch)")
        ],
        outputs="text",
        title="Titanic 생존 예측",
        description="성별, 나이, 자녀 수를 기준으로 생존 여부를 예측합니다."
    )
    interface.launch(share=True)  # ✨ 외부 접속 허용