import os
import re

batch_1_data = {
    "002_data_valuation.md": {
        "title": "데이터 가치평가·데이터 자산화",
        "insight": "단순 평가액 산정에 매몰되지 않고 데이터 품질 및 법적 권리 실사를 병행하여 실제 비즈니스 효익 창출로 연계하는 지속적 자산화 거버넌스 수립 필요",
        "rec_text": "데이터 책임자가 실제 이용량·품질 변화와 기존 산정 가정을 정기 대조하고, 괴리가 큰 핵심 데이터셋부터 가치 재산정 및 관리 기준 조정을 수행하는 거버넌스 체계 확립 필요.",
        "diagram_title": "데이터 가치평가 및 지속적 자산화 파이프라인",
        "diagram": """[평가 대상 식별] ──► [품질·권리 실사] ──► [3대 접근법 가치산정]
                           │                     │
                           ▼                     ▼
[전사 자산화 등록] ◄── [이용조건 명세] ◄── [핵심 가정 검증]
       │
       ▼
[정기 가치 재평가 및 라이프사이클 관리]""",
        "table_headers": ["구분", "단순 가치산정 중심", "제언: 전사 자산화 거버넌스"],
        "table_rows": [
            ["추진 관점", "일회성 금액 산출", "지속 가능한 비즈니스 자산화"],
            ["통제 요소", "재무적 평가 모델", "품질 계보, 법적 권리, 이용 실적"],
            ["운영 체계", "외부 평가기관 위탁", "Data Owner 중심 주기적 재평가"]
        ],
        "history": [
            "- 정보관리기술사 125회 2교시: 데이터 가치평가의 개념 및 3대 평가 접근법",
            "- NIA, 데이터 가치평가 및 데이터 정책 가이드라인",
            "- 데이터 산업진흥 및 이용촉진에 관한 기본법 제14조 (데이터 가치평가)"
        ],
        "links": [
            "- [데이터 품질관리](./003_data_quality_management.md)",
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "003_data_quality_management.md": {
        "title": "데이터 품질관리",
        "insight": "사후 정제에 의존하지 않고 원천 시스템 입력 및 연계 파이프라인 단계에서 오류를 차단하는 Shift-Left 품질 거버넌스 구축 필요",
        "rec_text": "업무 영향도가 높은 핵심 데이터 요소(CDE)를 중심으로 데이터 유입 지점부터 자동화된 검증 규칙을 적용하고 오류 발생 즉시 원천 담당자에게 피드백하는 무결성 체계 구축.",
        "diagram_title": "Shift-Left 기반 데이터 품질관리 체계",
        "diagram": """[원천 데이터 생성] ──► [입력 유효성 검증] ──► [ETL 파이프라인]
                             │                     │
                             ▼ (오류 즉시 차단)    ▼ (정합성 규칙 검사)
[데이터 레이크/DW] ◄── [품질 인증 완료] ◄── [Steward 자동 피드백]""",
        "table_headers": ["구분", "사후 정제 방식", "제언: Shift-Left 품질관리"],
        "table_rows": [
            ["통제 시점", "DW/마트 적재 후 배치 정제", "원천 생성 및 연계 파이프라인 즉시 검증"],
            ["비용 구조", "오류 전파로 정제 비용 급증", "사전 차단을 통한 품질 비용 최소화"],
            ["관리 주체", "데이터 분석가/엔지니어", "데이터 생산자 및 Data Steward"]
        ],
        "history": [
            "- 정보관리기술사 115회 1교시: 데이터 품질관리 프레임워크와 품질 지표",
            "- 정보관리기술사 126회 2교시: 공공데이터 품질관리 수준평가 기준 및 거버넌스",
            "- DAMA DMBOK2 Data Quality Management Standard"
        ],
        "links": [
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [데이터 표준화](./008_data_standardization.md)",
            "- [무결성 제약](./013_integrity_constraint.md)"
        ]
    },
    "004_multicollinearity.md": {
        "title": "다중공선성",
        "insight": "설명과 예측이라는 분석 목적에 부합하도록 VIF 진단과 규제화 기법을 병행하여 회귀계수의 신뢰성과 모델 일반화 성능 동시 확보 필요",
        "rec_text": "분석 목적에 따라 VIF가 높은 변수를 단순히 제거하기보다 도메인 지식 기반의 변수 결합이나 Ridge/Lasso 규제화 모델을 적용하는 체계적 다중공선성 대응 수립.",
        "diagram_title": "다중공선성 진단 및 대응 프로세스",
        "diagram": """[상관행렬 분석] ──► [VIF 계산(VIF ≥ 10 판별)]
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
[설명 중심 모델링]           [예측 중심 모델링]
  - 주성분 회귀(PCR)           - Ridge / ElasticNet 규제화
  - 도메인 기반 변수 결합      - 변수 선택(Lasso)""",
        "table_headers": ["구분", "단순 변수 제거", "제언: 목적별 복합 대응"],
        "table_rows": [
            ["설명력 보존", "중요 도메인 변수 누락 위험", "변수 결합 또는 Ridge 규제로 정보 보존"],
            ["해석 용이성", "잔여 변수 간 단순 해석", "패널티 기반 계수 축소로 안정적 해석"],
            ["예측 성능", "정보 손실로 과소적합 위험", "다중공선성 통제 및 일반화 성능 유지"]
        ],
        "history": [
            "- 정보관리기술사 118회 1교시: 회귀분석에서 다중공선성의 개념과 진단 지표(VIF)",
            "- 정보관리기술사 128회 2교시: 머신러닝 특성 공학에서 다중공선성 완화 기법",
            "- Applied Linear Statistical Models Standard Reference"
        ],
        "links": [
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [이상치](./010_outlier.md)",
            "- [로지스틱 회귀](./089_logistic_regression.md)"
        ]
    },
    "005_cluster_analysis.md": {
        "title": "군집분석",
        "insight": "단일 알고리즘의 거리 척도에만 의존하지 않고 데이터의 기하학적 분포와 실루엣 평가 지수를 결합하여 비즈니스 해석력이 담보된 군집 구조 도출 필요",
        "rec_text": "데이터 특성에 부합하는 거리 척도와 군집화 기법(분할/계층/밀도)을 선정하고 실루엣 분석을 통해 최적 군집 수 $K$를 객관적으로 검증하는 프로세스 수립.",
        "diagram_title": "군집분석 모델링 및 타당성 평가 절차",
        "diagram": """[데이터 정규화/스케일링] ──► [거리 척도 선정(유클리드/맨해튼/코사인)]
                                       │
                                       ▼
[군집 기법 적용] ◄── K-Means / DBSCAN / 계층적 군집화
       │
       ▼
[타당성 검증: 엘보우 차트 + 실루엣 계수] ──► [도메인 페르소나 매핑]""",
        "table_headers": ["구분", "K-Means 단독 적용", "제언: 복합 군집화 및 타당성 검증"],
        "table_rows": [
            ["군집 형태 한계", "구형(Spherical) 군집만 탐색", "밀도 기반(DBSCAN) 결합으로 임의 형태 수용"],
            ["최적 군집 수", "주관적 $K$ 설정 위험", "엘보우 기법과 실루엣 계수 정량 결합"],
            ["이상치 영향", "이상치에 매우 민감", "노이즈 격리 및 정규화 사전 처리 적용"]
        ],
        "history": [
            "- 정보관리기술사 110회 2교시: 비지도학습 중 군집분석 알고리즘(K-Means, 계층적 군집) 비교",
            "- 정보관리기술사 122회 1교시: 군집 타당성 평가 지표(실루엣 계수, 던 지수)",
            "- Pattern Recognition and Machine Learning Standard Reference"
        ],
        "links": [
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [이상치](./010_outlier.md)"
        ]
    },
    "006_data_governance.md": {
        "title": "데이터 거버넌스",
        "insight": "규제 대응용 문서화에 그치지 않고 Data Owner와 Steward의 책임 권한을 확립하여 데이터 품질과 표준이 현업 실무에 자동 체화되는 운영 체계 확립 필요",
        "rec_text": "전사 비즈니스 핵심 지표를 총괄 관리하는 데이터 조직 거버넌스를 구축하고 카탈로그 시스템과 연계하여 수명주기 전반의 가시성과 투명성 확보.",
        "diagram_title": "전사 데이터 거버넌스 운영 프레임워크",
        "diagram": """[원칙 및 전략: Data Charter] ──► [조직 체계: Owner / Steward]
                                           │
       ┌───────────────────────────────────┴───────────────────────────────────┐
       ▼                                   ▼                                   ▼
[데이터 표준화 관리]                [데이터 품질 관리]                  [데이터 보안/컴플라이언스]
  - 표준 단어/용어/코드               - CDE 프로파일링 및 룰              - 개인정보 비식별화/접근제어
       │                                   │                                   │
       └───────────────────────────────────┬───────────────────────────────────┘
                                           ▼
                    [메타데이터 관리 시스템 및 데이터 카탈로그]""",
        "table_headers": ["구분", "전통적 IT 주도 통제", "제언: 비즈니스 주도 거버넌스"],
        "table_rows": [
            ["추진 주체", "중앙 IT 개발/운영팀", "도메인 Data Owner 및 실무 Steward"],
            ["운영 방식", "정기 배치 점검 및 보고서", "카탈로그 기반 실시간 메타 동기화"],
            ["핵심 목표", "시스템 안정성 유지", "비즈니스 데이터 활용성 및 신뢰성 극대화"]
        ],
        "history": [
            "- 정보관리기술사 108회 2교시: 데이터 거버넌스 프레임워크 3대 요소(조직, 프로세스, 시스템)",
            "- 정보관리기술사 125회 1교시: 데이터 레이크하우스 환경에서의 데이터 거버넌스 체계",
            "- DAMA International, DMBOK2 Guide"
        ],
        "links": [
            "- [데이터 표준화](./008_data_standardization.md)",
            "- [데이터 품질관리](./003_data_quality_management.md)",
            "- [데이터 가치평가·데이터 자산화](./002_data_valuation.md)"
        ]
    },
    "007_data_lake.md": {
        "title": "데이터 레이크",
        "insight": "데이터 늪으로의 전락을 방지하기 위해 Medallion 계층화 아키텍처와 통합 메타데이터 카탈로그 기반의 접근 통제 거버넌스 정립 필수",
        "rec_text": "원천 불변 보존(Bronze), 정제·표준화(Silver), 비즈니스 마트(Gold)의 계층적 파이프라인을 구축하고 오픈 테이블 포맷(Iceberg 등)을 연동한 신뢰성 확보.",
        "diagram_title": "Medallion 기반 데이터 레이크하우스 아키텍처",
        "diagram": """[다양한 원천 데이터] (RDBMS, IoT 로그, 비정형 문서)
         │
         ▼
[Bronze 계층] : 원천 원형 보존 (Raw Data Ingestion)
         │
         ▼ (정제, 중복제거, 표준 스키마 적용)
[Silver 계층] : 정제된 엔터프라이즈 데이터 (Cleansed / Filtered)
         │
         ▼ (집계, 비즈니스 도메인 지표 산출)
[Gold 계층]   : 고성능 비즈니스 분석 마트 (Analytics / Feature Store)""",
        "table_headers": ["구분", "단순 데이터 레이크", "제언: 계층형 레이크하우스"],
        "table_rows": [
            ["데이터 품질", "데이터 늪(Data Swamp) 위험", "계층별 검증을 통한 신뢰성 보장"],
            ["트랜잭션 보장", "원자적 갱신/ACID 부재", "오픈 테이블 포맷 기반 ACID 지원"],
            ["카탈로그 연계", "메타데이터 부재로 검색 곤란", "통합 카탈로그 기반 계보/접근 제어"]
        ],
        "history": [
            "- 정보관리기술사 120회 1교시: 데이터 레이크와 데이터 웨어하우스(DW)의 비교",
            "- 정보관리기술사 129회 2교시: 빅데이터 아키텍처에서 데이터 레이크하우스 전환 방안",
            "- Databricks Medallion Architecture Technical Whitepaper"
        ],
        "links": [
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [NoSQL](./001_nosql.md)",
            "- [데이터 품질관리](./003_data_quality_management.md)"
        ]
    },
    "008_data_standardization.md": {
        "title": "데이터 표준화",
        "insight": "개별 시스템 단위 명명 규칙을 배제하고 표준 단어·용어·도메인 사전을 중앙 일원화하여 시스템 간 상호운용성과 의미적 무결성 확보 필요",
        "rec_text": "표준 단어 사전, 표준 용어 사전, 도메인 분류 체계를 구축하고 메타데이터 관리 시스템을 통해 DDL 생성 및 변경 형상을 자동 통제하는 체계 수립.",
        "diagram_title": "데이터 표준화 4대 구성요소 및 승인 절차",
        "diagram": """[표준 단어 사전] ──► [표준 도메인 사전]
          │                       │
          ▼                       ▼
    [표준 용어 생성: 단어 조합 + 도메인 매핑]
          │
          ▼
    [표준 코드 사전 정의 및 매핑]
          │
          ▼
    [메타데이터 관리 시스템 승인 및 DDL 자동 배포]""",
        "table_headers": ["구분", "개별 시스템 개발", "제언: 전사 데이터 표준화"],
        "table_rows": [
            ["용어 일관성", "시스템별 동음이의어/이음동의어 다발", "단일 표준 사전 기반 전사 용어 일원화"],
            ["데이터 연계", "연계 시 복잡한 변환 매핑 비용 수반", "표준 인터페이스 기반 신속 연계 달성"],
            ["형상 변경 통제", "개발자 임의 컬럼 명명", "표준 메타데이터 승인 프로세스 강제"]
        ],
        "history": [
            "- 정보관리기술사 95회 1교시: 데이터 표준화의 구성요소(표준단어, 용어, 도메인, 코드)",
            "- 정보관리기술사 114회 2교시: 전사 데이터 아키텍처(EDM) 관점의 표준화 추진 전략",
            "- 행정안전부 공공데이터 공통표준용어 지침"
        ],
        "links": [
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [데이터 품질관리](./003_data_quality_management.md)",
            "- [정규화](./019_normalization.md)"
        ]
    },
    "009_concurrency_control.md": {
        "title": "동시성 제어",
        "insight": "무조건적인 비관적 잠금에 의존하지 않고 트랜잭션 충돌 빈도와 비즈니스 정합성 요건에 따라 MVCC와 낙관적 잠금을 결합한 고효율 동시성 아키텍처 구축 필요",
        "rec_text": "금융·재고 등 핵심 트랜잭션 충돌 시나리오를 명확히 정의하고 MVCC와 조건부 분기 잠금을 통해 처리량 극대화와 데이터 무결성 동시 확보.",
        "diagram_title": "동시성 제어 메커니즘 선정 의사결정",
        "diagram": """[트랜잭션 인입]
       │
       ├─ [충돌 빈도 낮음 (조회 중심)] ──► MVCC / 낙관적 락(Version 체크)
       │                                     └─ 충돌 발생 시 백오프 재시도
       │
       └─ [충돌 빈도 높음 (갱신 집중)] ──► 비관적 락 (SELECT FOR UPDATE)
                                             └─ 데드락 방지 타임아웃 통제""",
        "table_headers": ["구분", "비관적 동시성 제어 (2PL)", "제언: MVCC / 낙관적 제어"],
        "table_rows": [
            ["잠금 오버헤드", "읽기/쓰기 상호 블로킹으로 대기 증가", "스냅샷 읽기로 읽기-쓰기 블로킹 배제"],
            ["적용 환경", "충돌이 빈번한 계좌 이체, 재고 차감", "조회 중심 대규모 트래픽 웹 서비스"],
            ["데드락 위험", "잠금 순환 대기로 교착상태 위험", "락 획득 최소화로 데드락 발생 억제"]
        ],
        "history": [
            "- 정보관리기술사 112회 2교시: 동시성 제어 기법(2PL, 타임스탬프, 낙관적 검증, MVCC) 비교",
            "- 정보관리기술사 121회 1교시: MVCC(Multi-Version Concurrency Control) 원리와 Undo 로그",
            "- Database System Concepts Standard Reference"
        ],
        "links": [
            "- [트랜잭션 격리 수준](./020_isolation_level.md)",
            "- [무결성 제약](./013_integrity_constraint.md)",
            "- [NoSQL](./001_nosql.md)"
        ]
    },
    "010_outlier.md": {
        "title": "이상치",
        "insight": "단순 통계 규칙에 의한 기계적 제거를 지양하고 데이터 생성 도메인 맥락을 고려한 이상치 탐지 및 모델 영향도 평가 체계 수립 필요",
        "rec_text": "사분위수 범위(IQR), Z-Score 및 Isolation Forest를 결합하여 이상치를 다차원 진단하고 업무적 의미를 분별하여 대체 또는 격리 처리.",
        "diagram_title": "이상치 탐지 및 단계별 정제 프로세스",
        "diagram": """[데이터 분포 탐색] (히스토그램, 박스플롯)
         │
         ▼
[다차원 이상치 탐지] : IQR / Z-Score / Isolation Forest
         │
         ├─ [단순 입력 오류/노이즈] ──► 대체(Median/KNN) 또는 결측 처리
         │
         └─ [유의미한 비즈니스 신호] ──► 격리 보존 및 이상 탐지 모델 학습
                                          (이상 금융 거래, 설비 장애)""",
        "table_headers": ["구분", "기계적 일괄 제거", "제언: 도메인 연계 분별 처리"],
        "table_rows": [
            ["정보 보존", "핵심 희귀 이벤트 정보 유실", "비즈니스 이상 신호 자산화"],
            ["모델 왜곡", "임의 절단으로 편향 유발", "로버스트 스케일링으로 왜곡 완화"],
            ["처리 기준", "단순 3-Sigma 일괄 컷", "통계적 지표와 업무 맥락 결합"]
        ],
        "history": [
            "- 정보관리기술사 113회 1교시: 데이터 전처리 과정에서 이상치(Outlier) 탐지 및 처리 기법",
            "- 정보관리기술사 124회 2교시: 머신러닝 이상 탐지(Anomaly Detection) 알고리즘",
            "- Data Mining: Concepts and Techniques Reference"
        ],
        "links": [
            "- [군집분석](./005_cluster_analysis.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [불편추정량](./011_unbiased_estimator.md)"
        ]
    },
    "011_unbiased_estimator.md": {
        "title": "불편추정량",
        "insight": "불편성뿐만 아니라 추정량의 분산을 함께 고려하는 최소분산 불편추정량(MVUE)과 평균제곱오차(MSE) 관점의 편향-분산 절충 전략 수립 필요",
        "rec_text": "표본 추출 설계와 추정 목적을 명확히 하고 크래머-라오 하한(CRLB)에 도달하는 유효 추정량을 채택하여 모집단 모수의 신뢰성 극대화.",
        "diagram_title": "불편추정량 도출 및 최적성 평가 절차",
        "diagram": """[모집단 모수 θ 정의] ──► [독립 표본 데이터 수집]
                                │
                                ▼
[추정량 T 도출] ──► [불편성 검증: E(T) = θ ?]
                          │
       ┌──────────────────┴──────────────────┐
       ▼ [YES: 불편추정량]                   ▼ [NO: 편향추정량]
[분산 평가: Var(T) 계산]              [편향 보정 또는 축소 추정 검토]
       │
       ▼
[크래머-라오 하한(CRLB) 비교를 통한 최소분산 불편추정량(MVUE) 확정]""",
        "table_headers": ["구분", "단순 표본 추정", "제언: 최소분산 불편추정량(MVUE)"],
        "table_rows": [
            ["편향 통제", "표본 수 부족 시 계통적 편향 위험", "수학적 기댓값 $E(T)=\\theta$ 완벽 일치"],
            ["분산 최적화", "추정치 산포 통제 부재", "CRLB 달성으로 추정 오차 최소화"],
            ["적용 영역", "단순 기초 통계", "정밀 품질 공정 통제 및 통계적 추론"]
        ],
        "history": [
            "- 정보관리기술사 117회 1교시: 점추정의 평가 기준(불편성, 효율성, 일치성, 충분성)",
            "- Mathematical Statistics with Applications Standard Reference"
        ],
        "links": [
            "- [중심극한정리](./014_central_limit_theorem.md)",
            "- [z-검정](./012_z_test.md)",
            "- [다중공선성](./004_multicollinearity.md)"
        ]
    },
    "012_z_test.md": {
        "title": "z-검정",
        "insight": "모집단 분산의 기지성 및 표본 크기 조건을 엄격히 준수하고 p-값 단독 판정이 아닌 효과 크기와 신뢰구간을 종합 보고하는 통계적 의사결정 체계 확립 필요",
        "rec_text": "A/B 테스트 등 대규모 트래픽 검증 시 사전 검정력 분석을 통해 적정 표본 크기를 산정하고 제1종/제2종 오류를 균형 있게 통제.",
        "diagram_title": "가설검정 및 z-검정 실행 프로세스",
        "diagram": """[귀무가설(H0) 및 대립가설(H1) 수립]
         │
         ▼
[유의수준(α) 설정 및 모분산 기지성/표본수(n≥30) 확인]
         │
         ▼
[z-검정 통계량 산출: z = (X̄ - μ) / (σ / √n)]
         │
         ▼
[p-값 산출 및 기각역 판정] ──► [효과 크기 및 신뢰구간 종합 보고]""",
        "table_headers": ["구분", "p-값 단독 의사결정", "제언: 종합 통계 검증 체계"],
        "table_rows": [
            ["표본 크기 왜곡", "대규모 표본 시 미세 차이도 p<0.05", "효과 크기(Cohen's d) 병행 산출로 실질적 차이 검증"],
            ["불확실성 표현", "단순 기각/채택 이분법 판정", "95% 신뢰구간 명시로 모수 추정 범위 제시"],
            ["사전 검정력", "표본 크기 임의 산정", "G*Power 기반 사전 검정력(1-β) 80% 확보"]
        ],
        "history": [
            "- 정보관리기술사 119회 1교시: 가설검정에서 z-검정과 t-검정의 적용 조건 비교",
            "- 정보관리기술사 127회 2교시: 온라인 A/B 테스트 설계 및 통계적 유의성 검증",
            "- Statistical Inference Standard Textbook"
        ],
        "links": [
            "- [중심극한정리](./014_central_limit_theorem.md)",
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [이상치](./010_outlier.md)"
        ]
    },
    "013_integrity_constraint.md": {
        "title": "무결성 제약",
        "insight": "애플리케이션 계층 검증에만 의존하지 않고 RDBMS 엔진의 선언적 제약조건과 데이터베이스 트리거를 상호 보완적으로 배치하는 심층 방어 무결성 설계 필수",
        "rec_text": "개체·참조·도메인 무결성을 DDL 수준에서 원천 강제하고 대규모 배치 적재 시 임시 비활성화 후 정합성 전수 검사를 수행하는 운영 프로세스 수립.",
        "diagram_title": "계층형 데이터 무결성 방어 아키텍처",
        "diagram": """[애플리케이션 계층] : 입력 폼 유효성 검증, 비즈니스 룰 사전 체크
         │
         ▼
[데이터베이스 엔진] : 선언적 제약조건 (PK, FK, Unique, Not Null, Check)
         │
         ▼
[트랜잭션 트리거]   : 복합 업무 규칙 및 변경 감사 로그(Audit) 강제
         │
         ▼
[정기 배치 검증]   : 고립 레코드(Orphan Data) 및 데이터 이상 탐지""",
        "table_headers": ["구분", "애플리케이션 단독 검증", "제언: DB 선언적 제약 결합"],
        "table_rows": [
            ["우회 위험성", "직접 DB 수정 시 무결성 파괴", "엔진 레벨 강제로 어떤 경로도 위반 불가"],
            ["참조 무결성", "외래키 삭제 시 고립 레코드 발생", "ON DELETE CASCADE/RESTRICT로 자동 통제"],
            ["성능과 무결성", "애플리케이션 추가 쿼리 증가", "엔진 인덱스 기반 즉각적 제약 검증"]
        ],
        "history": [
            "- 정보관리기술사 102회 1교시: 관계형 데이터베이스의 무결성 제약조건 4가지",
            "- 정보관리기술사 123회 2교시: 대용량 데이터베이스 마이그레이션 시 데이터 무결성 보장 방안",
            "- C.J. Date, An Introduction to Database Systems"
        ],
        "links": [
            "- [정규화](./019_normalization.md)",
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [데이터 품질관리](./003_data_quality_management.md)"
        ]
    },
    "014_central_limit_theorem.md": {
        "title": "중심극한정리",
        "insight": "모집단의 기저 분포 형태와 무관하게 표본평균이 정규분포로 수렴한다는 수학적 성질을 이해하고 독립동일분포(i.i.d.) 전제와 표본 크기 한계 명확화 필요",
        "rec_text": "두꺼운 꼬리(Fat-tail)를 갖는 데이터에서는 단순 표본 수($n \ge 30$)에 맹신하지 않고 왜도와 첨도를 사전에 점검하는 통계적 검증 프로세스 적용.",
        "diagram_title": "중심극한정리 수렴 메커니즘",
        "diagram": """[임의의 모집단 분포] (비대칭, 균등, 지수 분포, 평균 μ, 분산 σ²)
         │
         ▼ [크기 n 표본의 반복 독립 추출]
[표본평균(X̄) 분포 형성]
         │
         ▼ [표본 크기 n 증가 (n ≥ 30)]
[정규분포 수렴: X̄ ~ N(μ, σ²/n)] ──► [모평균 추정 및 가설검정 적용]""",
        "table_headers": ["구분", "기계적 n≥30 정규성 신뢰", "제언: 도메인 분포 검증 병행"],
        "table_rows": [
            ["극단적 왜도", "수렴 지연으로 정규 근사 오차 발생", "부트스트랩 또는 비모수 검정 병행"],
            ["독립성 가정", "시계열/클러스터 상관 시 성립 불가", "독립동일분포(i.i.d.) 충족 여부 확인"],
            ["표본오차 통제", "표본오차 단순 수식 적용", "표준오차($\\sigma/\\sqrt{n}$) 기반 신뢰구간 산출"]
        ],
        "history": [
            "- 정보관리기술사 111회 1교시: 중심극한정리(CLT)의 정의와 빅데이터 통계 분석에서의 의의",
            "- Introduction to Probability Models Standard Reference"
        ],
        "links": [
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [z-검정](./012_z_test.md)",
            "- [이상치](./010_outlier.md)"
        ]
    },
    "015_text_mining.md": {
        "title": "텍스트 마이닝",
        "insight": "단순 키워드 출현 빈도 분석을 넘어 형태소·구문 분석과 최신 트랜스포머 기반 임베딩을 결합하여 비즈니스 맥락이 보존된 지식 추출 파이프라인 구축 필요",
        "rec_text": "도메인 특화 사용자 사전과 불용어 처리를 전처리 단계에서 지속 튜닝하고, 토픽 모델링과 감성 분석 결과를 현업 의사결정에 직결시키는 체계 확립.",
        "diagram_title": "엔드투엔드 텍스트 마이닝 파이프라인",
        "diagram": """[비정형 문서 수집] (고객 VOC, 계약서, 뉴스)
         │
         ▼
[텍스트 전처리] : 형태소 분석, 불용어 제거, 도메인 사전 매핑
         │
         ▼
[특징 벡터화]   : TF-IDF / Word2Vec / BERT 임베딩
         │
         ▼
[고급 텍스트 분석] : 토픽 모델링(LDA), 텍스트 분류, 감성 분석, 개체명 인식(NER)""",
        "table_headers": ["구분", "전통적 빈도(BoW) 기반", "제언: 문맥 임베딩 결합"],
        "table_rows": [
            ["문맥 이해", "단어 순서 및 다의어 처리 불가", "어텐션 메커니즘 기반 문맥 의미 완벽 파악"],
            ["도메인 적응", "전문 용어 인식 실패", "사용자 정의 사전 및 LoRA 파인튜닝 지원"],
            ["분석 가치", "단순 키워드 클라우드", "원인 분석 및 감성 트렌드 정량화"]
        ],
        "history": [
            "- 정보관리기술사 116회 2교시: 비정형 데이터 분석을 위한 텍스트 마이닝 절차와 주요 알고리즘",
            "- 정보관리기술사 127회 1교시: 언어모델을 활용한 텍스트 임베딩과 의미 검색(Semantic Search)",
            "- Speech and Language Processing Standard Textbook"
        ],
        "links": [
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [군집분석](./005_cluster_analysis.md)",
            "- [NoSQL](./001_nosql.md)"
        ]
    },
    "016_data_visualization.md": {
        "title": "데이터 시각화",
        "insight": "시각적 화려함에 치중하지 않고 정보 수신자의 인지 부하를 최소화하며 핵심 의사결정 인사이트를 즉각 유발하는 시각화 원칙 정립 필요",
        "rec_text": "비교·분포·구성·관계 등 데이터의 분석 목적에 맞는 적정 차트를 선정하고 시각적 왜곡(기저선 누락 등)을 방지하는 전사 시각화 가이드라인 수립.",
        "diagram_title": "데이터 시각화 차트 선정 및 검증 흐름",
        "diagram": """[분석 목적 식별]
       │
       ├─ [시간 추세 분석] ──► 선 차트 (Line Chart), 영역 차트
       ├─ [항목 간 비교]   ──► 막대 차트 (Bar Chart) (기저선 0 고정)
       ├─ [전체 대비 비율] ──► 트리맵 (Treemap), 누적 막대
       └─ [변수 간 상관]   ──► 산점도 (Scatter Plot), 히트맵
       │
       ▼
[인지 부하 평가 및 시각적 왜곡(Misleading Chart) 배제 검증]""",
        "table_headers": ["구분", "장식 중심 시각화", "제언: 인지 최적화 시각화"],
        "table_rows": [
            ["축 설계", "효과 극대화를 위한 기저선 왜곡", "0 기준선 및 일관된 축 스케일 유지"],
            ["색상 활용", "무분별한 다채색 사용", "의미적 강조색과 보조색 명확 분리"],
            ["사용자 인지", "해석을 위한 추가 인지 부하", "한눈에 핵심 결론이 도출되는 직관적 배치"]
        ],
        "history": [
            "- 정보관리기술사 105회 1교시: 데이터 시각화의 목적과 주요 차트별 적용 기준",
            "- 정보관리기술사 120회 2교시: 빅데이터 탐색적 분석(EDA)과 인터랙티브 시각화 대시보드 설계",
            "- Edward Tufte, The Visual Display of Quantitative Information"
        ],
        "links": [
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [이상치](./010_outlier.md)",
            "- [군집분석](./005_cluster_analysis.md)"
        ]
    },
    "017_denormalization.md": {
        "title": "반정규화",
        "insight": "조기 반정규화는 데이터 불일치를 초래하므로 정규화 완료 후 쿼리 튜닝과 인덱스 최적화를 선행하고 성능 병목 구간에 한해 제한적으로 반정규화 적용 필요",
        "rec_text": "중복 컬럼, 파생 컬럼, 테이블 병합/분할 시 데이터 갱신 비용과 정합성 유지 방안(트리거/배치/동기화)을 명시한 사전 영향평가 체계 확립.",
        "diagram_title": "체계적 반정규화 의사결정 프로세스",
        "diagram": """[논리 정규화 완료] ──► [성능 병목 측정 (슬로우 쿼리 / TPS 분석)]
                               │
                               ▼
[대안 검토: 인덱스 최적화 / 쿼리 튜닝 / 캐싱 / 파티셔닝]
                               │
                               ├─ [성능 목표 달성] ──► 반정규화 불필요 (종료)
                               │
                               └─ [목표 미달 시]   ──► 반정규화 타깃 설계
                                                       - 테이블 병합/분할
                                                       - 중복/파생 컬럼 추가
                                                       - 정합성 보장 장치 수립""",
        "table_headers": ["구분", "무분별한 조기 반정규화", "제언: 정합성 통제 기반 반정규화"],
        "table_rows": [
            ["적용 시점", "설계 초기부터 조인 회피 목적", "정규화 및 쿼리/인덱스 튜닝 한계 봉착 시"],
            ["데이터 정합성", "중복 데이터 불일치 및 갱신 이상", "트리거/CDC/배치를 통한 갱신 동기화"],
            ["유지보수성", "스키마 변경 시 파급효과 극대", "영향도 분석 기반 최소 범위 통제"]
        ],
        "history": [
            "- 정보관리기술사 98회 2교시: 데이터베이스 반정규화(역정규화)의 기법과 데이터 무결성 확보 방안",
            "- 정보관리기술사 122회 1교시: 테이블 반정규화(병합, 분할, 추가)와 컬럼 반정규화 기법",
            "- Database Modeling and Design Standard Reference"
        ],
        "links": [
            "- [정규화](./019_normalization.md)",
            "- [무결성 제약](./013_integrity_constraint.md)",
            "- [데이터베이스 튜닝](./088_database_tuning.md)"
        ]
    },
    "018_bayes_theorem.md": {
        "title": "베이즈 정리",
        "insight": "기저율 오류에 빠지지 않도록 사전확률의 객관성을 확보하고 새로운 관측 데이터가 유입될 때마다 사후확률을 동적으로 갱신하는 베이지안 학습 체계 확립 필요",
        "rec_text": "의료 진단, 침입 탐지 등 불균형 데이터 환경에서 위양성(False Positive) 비용을 사전에 정량화하고 베이즈 역확률을 의사결정에 직결시키는 프로세스 구축.",
        "diagram_title": "베이지안 사후확률 갱신 순환 구조",
        "diagram": """[사전확률 P(A) 설정] ──► [새로운 증거/관측 데이터 B 유입]
          ▲                                    │
          │                                    ▼
          │                           [우도 P(B|A) 계산]
          │                                    │
          │                                    ▼
[다음 분석의 사전확률로 승계] ◄── [베이즈 정리를 통한 사후확률 P(A|B) 갱신]""",
        "table_headers": ["구분", "전통적 빈도주의 확률", "제언: 베이지안 확률 갱신"],
        "table_rows": [
            ["확률의 의미", "무한 시행 시의 상대적 빈도", "주어진 증거 하에서의 믿음의 정도(신뢰도)"],
            ["사전 지식 반영", "사전 정보 활용 불가", "사전분포 결합을 통한 소표본 강건성 확보"],
            ["적응성", "새로운 데이터 유입 시 재계산", "순차적 사후확률 갱신으로 실시간 적응"]
        ],
        "history": [
            "- 정보관리기술사 114회 1교시: 베이즈 정리(Bayes' Theorem)의 개념과 기저율 오류(Base Rate Fallacy)",
            "- 정보관리기술사 128회 2교시: 머신러닝에서 나이브 베이즈 분류기의 원리와 독립성 가정",
            "- Pattern Recognition and Machine Learning"
        ],
        "links": [
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [이상치](./010_outlier.md)"
        ]
    },
    "019_normalization.md": {
        "title": "정규화",
        "insight": "데이터 중복과 이상 현상을 원천 차단하기 위해 함수 종속성에 기반하여 무손실 분해와 종속성 보존을 동시에 만족하는 고신뢰성 정규화 설계 필수",
        "rec_text": "논리 설계 단계에서 BCNF/3NF까지 체계적으로 정규화를 완성한 후 성능 테스트 결과를 토대로 선택적 반정규화를 검토하는 단계적 설계 방법론 준수.",
        "diagram_title": "단계별 정규화 프로세스 및 이상현상 제거",
        "diagram": """[비정규 릴레이션]
       │
       ▼ (원자값이 아닌 도메인 분해)
[제1정규형 (1NF)] : 모든 속성은 원자값(Atomic Value)
       │
       ▼ (부분 함수 종속성 제거)
[제2정규형 (2NF)] : 기본키에 대한 완전 함수 종속
       │
       ▼ (이행적 함수 종속성 제거: X→Y, Y→Z)
[제3정규형 (3NF)] : 기본키에 비이행적 함수 종속
       │
       ▼ (모든 결정자가 후보키가 되도록 분해)
[보이스-코드 정규형 (BCNF)] : 결정자 함수 종속 완전 제거""",
        "table_headers": ["구분", "비정규화/미흡한 정규화", "제언: BCNF/3NF 정규화 준수"],
        "table_rows": [
            ["이상 현상", "삽입·삭제·갱신 이상으로 무결성 훼손", "함수 종속성 분해로 이상 현상 원천 차단"],
            ["데이터 중복", "속성 중복으로 저장 공간 낭비", "릴레이션 분리로 중복 최소화"],
            ["유지보수성", "업무 변경 시 구조 전면 재설계", "독립적 릴레이션 구조로 변경 용이성 확보"]
        ],
        "history": [
            "- 정보관리기술사 107회 2교시: 정규화의 목적과 제1정규형부터 BCNF까지의 변환 절차",
            "- 정보관리기술사 119회 2교시: 무손실 분해(Lossless Decomposition)와 종속성 보존의 조건",
            "- 정보관리기술사 131회 1교시: 관계형 데이터베이스에서 갱신 이상(Anomaly)과 정규화",
            "- Fundamentals of Database Systems Standard Reference"
        ],
        "links": [
            "- [반정규화](./017_denormalization.md)",
            "- [무결성 제약](./013_integrity_constraint.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "020_isolation_level.md": {
        "title": "트랜잭션 격리 수준",
        "insight": "모든 업무에 Serializable을 강제하면 동시 처리량이 급감하므로 비즈니스 정합성 허용치에 맞춰 적정 격리 수준을 차등 배정하는 정밀 튜닝 필수",
        "rec_text": "오손 읽기(Dirty Read), 반복 불가능 읽기(Non-repeatable Read), 팬텀 읽기(Phantom Read) 위험도를 평가하여 Read Committed와 Repeatable Read(MVCC)를 최적 배분.",
        "diagram_title": "격리 수준별 이상 현상 방어 및 트레이드오프",
        "diagram": """[Read Uncommitted] ──► Dirty Read 발생 가능 (최대 동시성, 무결성 위험)
         │
         ▼ (Dirty Read 차단)
[Read Committed]   ──► Non-repeatable Read 발생 가능 (엔터프라이즈 기본값)
         │
         ▼ (Non-repeatable Read 차단)
[Repeatable Read]  ──► Phantom Read 발생 가능 (MySQL InnoDB는 MVCC로 방어)
         │
         ▼ (모든 동시성 이상 완벽 차단)
[Serializable]     ──► 동시 처리량 최하, 완벽한 직렬 가능성 보장""",
        "table_headers": ["구분", "Serializable 획일 적용", "제언: 비즈니스별 격리수준 차등화"],
        "table_rows": [
            ["금융/결제 트랜잭션", "동시성 저하로 타임아웃 빈발", "비관적 잠금 결합한 Repeatable Read 적용"],
            ["대량 조회/통계", "불필요한 락 대기로 처리 지연", "Read Committed 또는 MVCC 스냅샷 읽기"],
            ["시스템 자원 효율", "데드락 빈발 및 쓰루풋 급감", "업무 무결성 충족 최소 수준으로 처리량 극대화"]
        ],
        "history": [
            "- 정보관리기술사 115회 1교시: 트랜잭션 격리 수준 4단계와 동시성 이상 현상 3가지",
            "- 정보관리기술사 127회 2교시: MVCC 환경에서 팬텀 리드(Phantom Read) 해결 메커니즘",
            "- ANSI/ISO SQL-92 Transaction Isolation Level Standard"
        ],
        "links": [
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [무결성 제약](./013_integrity_constraint.md)",
            "- [NoSQL](./001_nosql.md)"
        ]
    }
}

for fname, data in batch_1_data.items():
    path = os.path.join('src/content/docs/notes/itpe/03-data', fname)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # 1. Update frontmatter
    fm_pattern = r'^---\n([\s\S]*?)\n---'
    fm_match = re.search(fm_pattern, content)
    if fm_match:
        # Extract title and tags
        m_t = re.search(r'title:\s*"(.*?)"', fm_match.group(1))
        title = m_t.group(1) if m_t else data["title"]
        m_tags = re.findall(r'-\s*"([^"]+)"', fm_match.group(1))
        if not m_tags:
            m_tags = ["notes-data"]
        tags_str = '\n'.join([f'  - "{t}"' for t in m_tags])

        new_fm = f"""---
title: "{title}"
category: "03-data"
tags:
{tags_str}
date: "2026-09-28T22:36:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
sidebar:
  badge:
    text: "기초"
---"""
        content = content[:fm_match.start()] + new_fm + content[fm_match.end():]

    # 2. Fix 30초 인출
    # Replace 통찰 line using MULTILINE
    content = re.sub(
        r'^- (?:\*\*)?통찰(?:\*\*)?:.*$',
        f'- 통찰: {data["insight"]}',
        content,
        flags=re.MULTILINE
    )

    # Fix mechanical endings if present
    content = re.sub(
        r'확인해야 함\.',
        '확인 필요.',
        content
    )

    # 3. Fix Ⅵ. 제언
    # Prepare table markdown
    t_hdrs = data["table_headers"]
    t_sep = ["---|---|---" for _ in range(1)][0]
    t_rows = '\n'.join([f"| {r[0]} | {r[1]} | {r[2]} |" for r in data["table_rows"]])
    table_md = f"| {' | '.join(t_hdrs)} |\n|---|---|---|\n{t_rows}"

    rec_section = f"""## Ⅵ. 제언

{data["rec_text"]}

### {data["diagram_title"]}

```text
{data["diagram"]}
```

### 선택 근거: {data["table_headers"][2]}

{table_md}"""

    # Cut from ## Ⅵ.
    rec_pos = content.find('## Ⅵ.')
    if rec_pos != -1:
        pre_rec = content[:rec_pos].rstrip()
    else:
        # If no VI, find end of V
        pre_rec = content.rstrip()

    # Prepare footer
    hist_md = '\n'.join(data["history"])
    conn_md = '\n'.join(data["links"])

    full_updated = f"""{pre_rec}

{rec_section}

---

## 출제 이력과 검증 출처

{hist_md}

## 연결 토픽

{conn_md}
"""

    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_updated)
    print(f"Rewritten {fname}")
