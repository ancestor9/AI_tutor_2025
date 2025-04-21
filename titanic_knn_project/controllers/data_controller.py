import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect("data/titanic.db")
    df = pd.read_sql("SELECT * FROM titanic", conn)
    conn.close()
    return df

def preprocess_data(df):
    df = df.dropna(subset=["age", "sex", "survived"])
    df.loc[:, "sex"] = df["sex"].map({"male": 0, "female": 1})
    print(f'data_controller.py > preprocess_data> {df.isnull().sum()}')  # 결측치 확인
    return df[["sex", "age", "parch", "survived"]]


def plot_survival(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.histplot(data=df, x="age", hue="survived", multiple="stack", kde=False)
    plt.title("Survival by Age")
    plt.savefig("data/survival_age.png")