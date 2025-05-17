import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data(train_path, test_path):
    """
    train_path, test_path에 있는 CSV 파일을 읽어서 DataFrame으로 반환 
    """
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
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

    return train, test, encoders
        

def map_boolean_features(train, test, bool_features):
    """
    불리언 변수('Yes' / 'No')를 1과 0으로 매핑
    """
    bool_map = {"Yes" : 1, "No" : 0}
    
    for feature in bool_features:
        train[feature] = train[feature].map(bool_map)
        test[feature] = test[feature].map(bool_map)

    return train, test

