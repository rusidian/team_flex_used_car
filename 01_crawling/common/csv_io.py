from typing import Optional

import pandas as pd

from .paths import DATA_DIR


def load_csv(filename: str, encoding: str = 'utf-8') -> Optional[pd.DataFrame]:
    """
    프로젝트 data/ 디렉터리의 CSV 파일을 읽어 DataFrame으로 반환합니다.

    - 파일이 없으면 None을 반환합니다.
    - CSV 파싱 중 오류가 발생하면 예외를 발생시킵니다. (상위에서 처리)
    """
    # filename에서 .csv가 빠져 있으면 추가
    if not filename.lower().endswith('.csv'):
        filename = f'{filename}.csv'

    # file_path -> PROJECT_ROOT/data/filename
    file_path = DATA_DIR / filename

    # DATA_DIR경로에 filename의 파일이 없으면 None을 반환
    if not file_path.exists():
        print(f'[WARN] CSV not found: {filename}')
        return None

    
    try:
        # csv를 읽어서 (df)DataFrame으로 반환
        df = pd.read_csv(file_path, encoding=encoding)

        # csv에 내용이 없으면 빈 df를 반환
        if df.empty:
            print(f'[WARN] CSV is empty: {filename}')
            return df

        # 내용이 있으면 csv을 읽는데 성공이라고 터미널에 출력 후 df반환
        print(f'[INFO] CSV loaded: {filename}')
        return df

    except Exception as e:
        # 에러가 발생하면 ERROR라고 사용자에게 알려주고 에러코드 전달
        print(f"[ERROR] Failed to load CSV: {file_path} | {e}")

        # 예외를 숨기지 않고 다시 발생시켜 상위 로직에서 처리 가능하게 함
        raise
