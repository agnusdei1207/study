from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/03-data")

fixes = {
    "137_star_schema.md": [
        ("Type 1 덮어쓰기는 과거 사실의 차원 속성도 현재 값으로 보이게 하므로 과거 시점 분석 요구와 구분한다.",
         "Type 1 덮어쓰기는 과거 사실의 차원 속성도 현재 값으로 보이게 하므로 과거 시점 분석 요구와 분리 검토 필요.")
    ],
    "138_voice_data_mining.md": [
        ("- 통찰: 음향·언어 모델 기반 음성 전사(STT)와 감성·키워드 마이닝 파이프라인을 연계하여 비정형 음성 로그에서 고객 통찰을 체계적으로 도출함.",
         "- 통찰: 음향·언어 모델 기반 음성 전사(STT)와 감성·키워드 마이닝 파이프라인을 연계하여 비정형 음성 로그에서 고객 통찰을 체계적으로 도출 체계화.")
    ],
    "143_inferential_statistics.md": [
        ("- 통찰: 표본 통계량의 확률분포와 오차 한계를 기반으로 모집단 모수를 추정하고 가설검정을 수행하여 데이터 기반 의사결정의 과학적 타당성을 확보함.",
         "- 통찰: 표본 통계량의 확률분포와 오차 한계를 기반으로 모집단 모수를 추정하고 가설검정을 수행하여 데이터 기반 의사결정의 과학적 타당성을 확보 수립.")
    ],
    "154_bi.md": [
        ("- 통찰: 기업 내 분산된 데이터를 수집·통합하여 다차원 분석 모델과 시각화 대시보드를 제공함으로써 데이터 주도적 의사결정을 지원함.",
         "- 통찰: 기업 내 분산된 데이터를 수집·통합하여 다차원 분석 모델과 시각화 대시보드를 제공함으로써 데이터 주도적 의사결정을 지원 체계화.")
    ],
    "163_point_vs_interval_estimation.md": [
        ("- 통찰: 표본 통계량 기반의 단일 대표값 추정인 점추정과 표본 오차를 반영하여 모수 포함 범위를 제시하는 구간추정을 상호 보완하여 활용함.",
         "- 통찰: 표본 통계량 기반의 단일 대표값 추정인 점추정과 표본 오차를 반영하여 모수 포함 범위를 제시하는 구간추정을 상호 보완하여 활용 체계화.")
    ]
}

for fname, pair_list in fixes.items():
    fpath = TARGET_DIR / fname
    text = fpath.read_text(encoding="utf-8")
    for old, new in pair_list:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"Warning: pattern not found in {fname}: {old[:30]}...")
    fpath.write_text(text, encoding="utf-8")
    print(f"Updated {fname}")
