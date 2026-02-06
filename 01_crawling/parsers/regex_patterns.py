import re
from re import Pattern

# ------------------------------
# onclick 기반 코드 추출
# ------------------------------

# 제조사 코드 (depth = 1)
RE_MAKER_CODE: Pattern[str] = re.compile(
    r"car_depth_lite\(\s*'(\d+)'\s*,\s*1\s*,"
)

# 차량 모델(그룹) 코드
RE_MODEL_CODE: Pattern[str] = re.compile(
    r"modelSel\(\s*(\d+)\s*,"
)

# 등급 코드 (depth = 3)
RE_GRADE_CODE: Pattern[str] = re.compile(
    r"car_depth_lite\(\s*'(\d+)'\s*,\s*3\s*,"
)

# 트림 코드 (depth = 4)
RE_TERM_CODE: Pattern[str] = re.compile(
    r"car_depth_lite\(\s*'(\d+)'\s*,\s*4\s*,"
)

# ------------------------------
# class명 기반 연결(카탈로그/세부모델)
# 예: class="... c_model_353 ..." -> group_no = 353
# ------------------------------
RE_GROUP_NO_FROM_CLASS: Pattern[str] = re.compile(r"\bc_model_(\d+)\b")

# ------------------------------
# URL query 파라미터 추출
# ------------------------------
RE_QUERY_PAGE: Pattern[str] = re.compile(r"[?&]page=(\d+)")
RE_QUERY_NO: Pattern[str] = re.compile(r"[?&]no=(\d+)")

# ------------------------------
# 숫자/단위 파싱 보조(정규식만)
# 변환 로직(to_int)은 utils로
# ------------------------------
RE_TO_INT: Pattern[str] = re.compile(r"(\d+)")
RE_INT_WITH_COMMA: Pattern[str] = re.compile(r"(\d[\d,]*)")

RE_PRICE_WAN: Pattern[str] = re.compile(r"([\d,]+)\s*만원")
RE_DISPLACEMENT_CC: Pattern[str] = re.compile(r"([\d,]+)\s*cc")

# ------------------------------
# 기간/개월 표기
# 예: "36 / 48개월", "36/48"
# ------------------------------
RE_REMAIN_TOTAL_MONTHS: Pattern[str] = re.compile(r"(\d+)\s*/\s*(\d+)")