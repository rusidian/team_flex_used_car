from bobe_car import BobeCar
from decorators import register_progress_loggers_once
from load_csv import load_csv

PROGRESS_METHODS = {
    "get_soup": "HTML 수집",
    "get_maker_category": "제조사 수집",
    "get_maker_models": "차량 모델 수집",
    "standardize_dataframe": "DF 변환",
    "save_df_to_csv": "CSV 저장",
}

# PROGRESS_METHODS를 register_progress_loggers_once에 등록
register_progress_loggers_once(BobeCar, PROGRESS_METHODS)

car = BobeCar()

# # 차량 제조사 정보 추출
# car.get_maker_category('K')
# car.get_maker_category('I')

# 제조사 차량 모델 정보 추출

# maker에서 maker_code만 추출
makers = load_csv('makers.csv')
# maker_code의 열을 int로 형변환 하면서 list에 저장
maker_codes: list[int] = makers["maker_code"].astype(int).tolist()
maker_origins: list[str] = makers["origin"].astype(str).tolist()

for maker_code, maker_origin in zip(maker_codes, maker_origins):
    car.get_maker_models(maker_origin, maker_code)