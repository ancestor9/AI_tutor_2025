 
import os
import sqlite3
import seaborn as sns

def init_db():
    os.makedirs("data", exist_ok=True)  # 데이터 폴더가 없으면 생성
    conn = sqlite3.connect("data/titanic.db")
    df = sns.load_dataset("titanic")
    # 2. NaN 전체 제거
    df = df.dropna()  # 모든 컬럼 기준으로 결측치 제거
    print(f'db.py > init_db > {df.isnull().sum()}')  # 결측치 확인
    # 3. 필요 없는 컬럼 제거
    df.to_sql("titanic", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
