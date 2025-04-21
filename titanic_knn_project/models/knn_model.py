import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class KNNPredictor:
    def __init__(self):
        self.model = None
        # 평균값 저장을 위한 변수 추가
        self.age_mean = None
        self.parch_mean = None

    def train(self, df):
        # 필요한 컬럼만 선택하고 복사본 생성
        df = df[["sex", "age", "parch", "survived"]].copy()
        
        # 결측치 현황 출력
        print("\n=== 초기 결측치 현황 ===")
        print(df.isnull().sum())
        
        # 성별 데이터 확인
        print("\n=== 성별 데이터 고유값 ===")
        print(df["sex"].unique())
        
        # 나이와 parch의 평균값 계산 및 저장
        self.age_mean = df["age"].mean()
        self.parch_mean = df["parch"].mean()
        
        # 결측치를 평균값으로 대체
        df["age"] = df["age"].fillna(self.age_mean)
        df["parch"] = df["parch"].fillna(self.parch_mean)
        
        # 최종 결측치 처리 후 확인
        print("\n=== 최종 결측치 처리 후 현황 ===")
        print(df.isnull().sum())

        # 학습 데이터 준비
        X = df[["sex", "age", "parch"]]
        y = df["survived"]
        
        # 학습 진행
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(X_train, y_train)

    def predict(self, sex, age, parch):
        # 모델 학습 여부 확인
        if self.model is None:
            raise ValueError("모델이 학습되지 않았습니다. train() 메서드를 먼저 호출하세요.")
        
        # 성별 입력 처리
        if isinstance(sex, str):
            sex = 1 if sex.lower() == "female" else 0
        
        # 결측치 처리
        if age is None or pd.isna(age):
            age = self.age_mean
        if parch is None or pd.isna(parch):
            parch = self.parch_mean
        
        # 입력값 형변환
        try:
            age = float(age)
            parch = float(parch)
        except (ValueError, TypeError) as e:
            raise ValueError("나이와 parch는 숫자 형식이어야 합니다.") from e
        
        return self.model.predict([[sex, age, parch]])[0]