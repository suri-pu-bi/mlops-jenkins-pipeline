import torch
from pytorch_tabnet.pretraining import TabNetPretrainer
from pytorch_tabnet.tab_model import TabNetRegressor

def get_pretrainer(cat_idxs, cat_dims):
    """
    비지도 사전학습을 위한 TabNetPretrainer 모델 생성
    """
    return TabNetPretrainer(
        cat_idxs=cat_idxs,
        cat_dims=cat_dims,
        seed=42,
        verbose=0
    )

def get_regressor(cat_idxs, cat_dims):
    """
    지도 학습을 위한 TabNetRegressor 모델 생성 
    """
    return TabNetRegressor(
        cat_idxs=cat_idxs,
        cat_dims=cat_dims,
        seed=42,
        verbose=0,
        optimizer_fn=torch.optim.AdamW
    )
