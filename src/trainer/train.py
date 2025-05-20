from sklearn.model_selection import KFold
import numpy as np
from models.tabnet_model import get_pretrainer, get_regressor

def train_with_kfold(X, y, cat_idxs, cat_dims, n_folds=5):
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    models = []
    cv_scores = []
    
    for fold, (train_idx, valid_idx) in enumerate(kf.split(X)):
        
        X_train, y_train = X.iloc[train_idx].values, y.iloc[train_idx].values.reshape(-1, 1)
        X_valid, y_valid = X.iloc[valid_idx].values, y.iloc[valid_idx].values.reshape(-1, 1)

        # 비지도 사전학습
        pretrainer = get_pretrainer(cat_idxs, cat_dims)
        pretrainer.fit(X_train=X_train, max_epochs=100, batch_size=512, virtual_batch_size=64)

        # 지도학습
        model = get_regressor(cat_idxs, cat_dims)
        model.fit(
            X_train=X_train, y_train=y_train,
            eval_set=[(X_valid, y_valid)],
            from_unsupervised=pretrainer,
            eval_metric=['mae'],
            max_epochs=100,
            patience=10
        )
        
        # 모델을 메모에 저장
        models.append(model)
        cv_scores.append(model.best_cost)

    return models, cv_scores