import re
from re import Pattern

# 제조사 코드 (level 1)
RE_MAKER_CODE: Pattern[str] = re.compile(
    r"car_depth_lite\(\s*'(\d+)'\s*,\s*1\s*,"
)

# 차량 모델 코드
RE_MODEL_CODE: Pattern[str] = re.compile(
    r"modelSel\(\s*(\d+)\s*,"
)

# 등급 코드 (level_no, depth = 3)
RE_GRADE_CODE: Pattern[str] = re.compile(
    r"car_depth_lite\(\s*'(\d+)'\s*,\s*3\s*,"
)

# 트림 코드 (level2_no, depth = 4)
RE_TERM_CODE: Pattern[str] = re.compile(
    r"car_depth_lite\(\s*'(\d+)'\s*,\s*4\s*,"
)

# 숫자만 추출 (등록대수, 연비, 배기량 등 범용)
RE_TO_INT: Pattern[str] = re.compile(r"(\d+)")
