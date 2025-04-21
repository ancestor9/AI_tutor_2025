import gradio as gr
from controllers.predict_controller import predict

def predict_interface(sex, age, parch):
    sex_code = 0 if sex == "male" else 1
    result = predict(sex_code, age, parch)
    return "생존" if result == 1 else "사망"

def build_ui():
    interface = gr.Interface(
        fn=predict_interface,
        inputs=[
            gr.Radio(["male", "female"], label="성별"),
            gr.Slider(0, 80, step=1, label="나이"),
            gr.Slider(0, 5, step=1, label="자녀 수(parch)")
        ],
        outputs="text",
        title="Titanic 생존 예측"
    )
    interface.launch()