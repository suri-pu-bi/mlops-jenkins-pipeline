import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data(train_path, test_path):
    """
    train_paht, test_path에 있는 CSV 파일을 읽어서 DataFrame으로 반환 
    """
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test
