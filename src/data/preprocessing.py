import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from utils.feature_groups import category_features, numeric_features, bool_features


def load_data(train_path, test_path):
    """
    train_path, test_path에 있는 CSV 파일을 읽어서 DataFrame으로 반환 
    """
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    
    return train, test

def convert_types(train, test):
    """
    타입 변환 수행 
    """
       # 설립연도 타입 변환 (int -> object)
    # 왜 int를 object로 바꿀까?
    # - int 타입은 연속적인 수치형 변수로 간주됨. 즉, 2000, 2010, 2020 사이에 수학적 거리가 있다고 판단.
    # - 그런데 설립연도는 단순히 몇 년도 설립됐는가를 나타내는 범주형 정보이다!
    train['설립연도'] = train['설립연도'].astype('object')
    test['설립연도'] = test['설립연도'].astype('object')
    
    return train, test
    

def encode_categorical_feature(train, test, category_features):
    """
    범주형 변수에 대해 Label Encoding을 수행
    결측치는 Missing으로 대체 후 인코딩
    """    
    
    # LabelEncoder 객체를 각 범주형 feature별로 따로 저장하여 사용 
    # LabelEncoder - sklearn에서 제공하는 클래스, 문자형 값을 숫자형으로 바꾸는 인코더 
    encoders = {}
    for feature in category_features:
        encoders[feature] = LabelEncoder()
        train[feature] = train[feature].fillna('Missing')
        test[feature] = test[feature].fillna('Missing')
        train[feature] = encoders[feature].fit_transform(train[feature]) # train -> 학습 + 변환 
        test[feature] = encoders[feature].transform(test[feature]) # test -> 변환만 
        
    return train, test
        

def map_boolean_features(train, test, bool_features):
    """
    불리언 변수('Yes' / 'No')를 1과 0으로 매핑
    """
    bool_map = {"Yes" : 1, "No" : 0}
    
    for feature in bool_features:
        train[feature] = train[feature].map(bool_map)
        test[feature] = test[feature].map(bool_map)

    return train, test


def fill_numeric_missing(train, test, numeric_features):
    """
    수치형 변수의 결측값을 학습 데이터의 평균값으로 대체 
    """
    for feature in numeric_features:
        mean_value = train[feature].mean()
        train[feature] = train[feature].fillna(mean_value)
        # 테스트 데이터에도 학습 데이터의 평균값을 사용하는 이유 
        # - 만약 테스트 데이터의 평균값을 사용한다면, Data Leakage(데이터 누수) 발생 
        # - 테스트 데이터 = 미래에 들어올 데이터에 모델이 얼마나 잘 작동하느냐를 평가하는 시뮬레이션 도구 
        # - 테스트 데이터의 평균을 계산한다는 건, 미래 데이터 전체를 미리 다 살펴본 상태에서 값을 구한 셈! 학습과정에 포함시키는 것과 마찬가지. 
        # -> 테스트 데이터는 훈련할 때 사용한 전처리 규칙으로 데이터를 처리해야한다! 
        test[feature] = test[feature].fillna(mean_value)
        
    return train, test 