import os
import re

batch_4_data = {
    "068_jackknife_bootstrap.md": {
        "title": "잭나이프·부트스트랩",
        "insight": "모집단 분포를 알 수 없는 소표본 환경에서 모수의 신뢰구간과 표준오차를 추정하기 위해 복원 추출 기반의 부트스트랩과 체계적 1개 제외 잭나이프 결합 필수",
        "rec_text": "표본 크기와 계산 복잡도를 감안하여 일반적인 신뢰구간 추정에는 B=1000 이상의 부트스트랩을 채택하고 편향(Bias) 추정에는 결정론적 잭나이프를 적용.",
        "diagram_title": "부트스트랩(Bootstrap)과 잭나이프(Jackknife) 리샘플링 절차",
        "diagram": """[원래 표본 데이터 (크기 n)]
         │
         ├─ [부트스트랩: 복원 추출 (Replacement)]
         │        ├─ 크기 n 표본 B회 반복 추출 ──► [추정량 B개 산출] ──► 신뢰구간 도출
         │
         └─ [잭나이프: 비복원 1개 제외 (Leave-One-Out)]
                  ├─ 데이터 i번째 원소 제외 (n회) ──► [의사값(Pseudo-value)] ──► 편향 보정""",
        "table_headers": ["구분", "부트스트랩 (Bootstrap)", "잭나이프 (Jackknife)"],
        "table_rows": [
            ["추출 메커니즘", "확률적 복원 추출 (중복 허용)", "결정론적 1개 제외 비복원 추출 (총 n회)"],
            ["적용 영역", "복잡한 통계량의 신뢰구간 및 분포 추정", "모수 추정량의 편향(Bias) 및 분산 추정"],
            ["계산 비용", "B회(보통 1,000회 이상) 시뮬레이션", "표본 크기 n회만 계산 (비교적 경량)"]
        ],
        "history": [
            "- 정보관리기술사 115회 1교시: 데이터 통계 분석에서 리샘플링(부트스트랩, 잭나이프) 기법",
            "- An Introduction to the Bootstrap Standard Reference"
        ],
        "links": [
            "- [표본추출](./032_sampling.md)",
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [앙상블 배깅·부스팅](./062_ensemble_bagging_boosting.md)"
        ]
    },
    "069_dimensionality_reduction_pca_mds.md": {
        "title": "차원 축소(PCA·MDS)",
        "insight": "차원의 저주와 다중공선성을 극복하기 위해 분산 보존 중심의 주성분 분석(PCA)과 객체 간 거리 유사도 보존 중심의 다차원 척도법(MDS)의 목적별 선별 적용 필수",
        "rec_text": "설명 분산 비율(Explained Variance Ratio) 80% 이상을 만족하는 최소 주성분을 선택하고, 고차원 비선형 매니폴드 구조는 t-SNE 또는 UMAP으로 보완.",
        "diagram_title": "주성분 분석(PCA) 4단계 수학적 파이프라인",
        "diagram": """[고차원 데이터 정규화] (평균 0, 분산 1 표준화)
         │
         ▼
[공분산 행렬(Covariance Matrix) 산출]
         │
         ▼
[고유값 분해 (Eigenvalue Decomposition)] : 고유벡터(주성분 축) 및 고유값 산출
         │
         ▼
[누적 설명 분산 비율 평가] ──► 최적 k개 주성분 투영 (고차원 → 저차원 변환)""",
        "table_headers": ["구분", "주성분 분석 (PCA)", "다차원 척도법 (MDS)"],
        "table_rows": [
            ["목적 함수", "데이터의 사상 분산(Variance) 극대화", "개체 간 거리/비유사도(Dissimilarity) 보존"],
            ["입력 형태", "변수 기반 수치형 데이터 행렬", "개체 간 1:1 거리/근접도 행렬"],
            ["주요 활용", "특성 추출, 다중공선성 제거, 압축", "소비자 지각도, 시각화, 브랜드 포지셔닝"]
        ],
        "history": [
            "- 정보관리기술사 112회 2교시: 머신러닝 차원 축소 기법 중 PCA(주성분분석)의 수학적 원리",
            "- 정보관리기술사 124회 1교시: 다차원 척도법(MDS)의 개념과 스트레스(Stress) 지수",
            "- Pattern Recognition and Machine Learning"
        ],
        "links": [
            "- [다중공선성](./004_multicollinearity.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [군집분석](./005_cluster_analysis.md)"
        ]
    },
    "070_referential_integrity.md": {
        "title": "참조 무결성",
        "insight": "고립 레코드(Orphan Data)와 외래키 참조 불일치를 방지하기 위해 DDL 수준의 외래키 제약조건과 애플리케이션 수준의 변경 이벤트 전파를 유기적으로 결합 필요",
        "rec_text": "부모 테이블 삭제 시 비즈니스 영향도에 따라 CASCADE 또는 RESTRICT 정책을 명확히 설정하고 대용량 배치 적재 시 외래키 인덱스를 필수 구성.",
        "diagram_title": "참조 무결성 위반 방어 및 삭제 옵션",
        "diagram": """[부모 테이블: Customer (PK: cust_id)]
         │
         ▼ (외래키 참조 관계: FK cust_id)
[자식 테이블: Orders (FK: cust_id)]
         │
         ├─ [CASCADE]  ──► 부모 레코드 삭제 시 관련 주문 레코드 자동 연쇄 삭제
         ├─ [RESTRICT] ──► 주문 레코드가 존재하면 부모 고객 삭제 원천 차단
         ├─ [SET NULL] ──► 부모 삭제 시 자식의 외래키 값을 NULL로 자동 변경
         └─ [NO ACTION]──► 트랜잭션 종료 시점까지 제약조건 지연 검증""",
        "table_headers": ["구분", "외래키(FK) 미설정 운영", "제언: 선언적 참조 무결성 강제"],
        "table_rows": [
            ["데이터 정합성", "고립된 유령 데이터(Orphan) 잔존", "DBMS 차원의 완벽한 부모-자식 일치 보장"],
            ["성능 오버헤드", "쓰기 시 검사 비용 없음", "외래키 컬럼 인덱스 생성으로 검증 성능 최적화"],
            ["트랜잭션 안전", "수동 롤백 실패 시 불일치 발생", "원자적 삭제/수정 무결성 100% 보장"]
        ],
        "history": [
            "- 정보관리기술사 102회 1교시: 관계형 데이터베이스의 무결성 제약조건 중 참조 무결성",
            "- 정보관리기술사 120회 1교시: 외래키 제약조건의 옵션(CASCADE, RESTRICT, SET NULL)",
            "- Database Systems: The Complete Book"
        ],
        "links": [
            "- [무결성 제약](./013_integrity_constraint.md)",
            "- [정규화](./019_normalization.md)",
            "- [개체-관계 다이어그램(ERD)](./028_erd.md)"
        ]
    },
    "071_filtering.md": {
        "title": "추천 시스템 필터링",
        "insight": "협업 필터링의 콜드 스타트(Cold Start) 및 희소성 문제와 콘텐츠 기반 필터링의 과적합(오버스페셜라이제이션)을 극복하는 하이브리드 추천 아키텍처 필수",
        "rec_text": "신규 사용자/아이템은 메타데이터 기반 콘텐츠 필터링을 적용하고 인터랙션 축적 후 행렬 분해(Matrix Factorization) 및 딥러닝 추천 모델로 동적 전환.",
        "diagram_title": "하이브리드 추천 시스템 2단계 파이프라인",
        "diagram": """[사용자 행동 로그 및 아이템 메타데이터]
         │
         ├─ [1단계 후보 생성 (Candidate Generation)]
         │        ├─ 콘텐츠 기반 필터링 (TF-IDF / 임베딩 유사도)
         │        └─ 협업 필터링 (Item-based CF / 행렬 분해)
         │
         ▼ (Top-K 후보 수백 개 추출)
[2단계 정밀 랭킹 (Re-ranking / Deep Learning)]
         │ : 딥러닝 랭킹 모델 (Wide & Deep / DLRM) 적용
         ▼
[개인화 추천 결과 서빙 (다양성/신선도 보정 필터)]""",
        "table_headers": ["구분", "협업 필터링 (Collaborative)", "콘텐츠 기반 필터링 (Content-based)"],
        "table_rows": [
            ["추천 원리", "유사한 취향의 다른 사용자 행동 기반", "사용자가 선호한 아이템의 속성 유사도 기반"],
            ["콜드 스타트", "신규 사용자/아이템에 추천 불가 (치명적)", "아이템 속성만으로 신규 아이템 추천 가능"],
            ["추천 의외성", "새로운 관심사 발견(Serendipity) 가능", "이전 선호 범위에 갇히는 과적합 발생"]
        ],
        "history": [
            "- 정보관리기술사 118회 2교시: 추천 시스템의 협업 필터링(CF)과 콘텐츠 기반 필터링(CBF) 비교",
            "- 정보관리기술사 129회 1교시: 대규모 추천 시스템을 위한 2단계(Retrieval, Ranking) 아키텍처",
            "- Recommender Systems Handbook Standard Reference"
        ],
        "links": [
            "- [군집분석](./005_cluster_analysis.md)",
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [벡터 데이터베이스](./044_vector_database.md)"
        ]
    },
    "072_association_rule_mining.md": {
        "title": "연관 규칙 마이닝",
        "insight": "지지도(Support), 신뢰도(Confidence), 향상도(Lift)의 3대 지표를 균형 있게 적용하고 Apriori의 반복 DB 스캔 한계를 극복하는 FP-Growth 트리 알고리즘 채택 필수",
        "rec_text": "최소 지지도 임계치를 동적으로 설정하여 무의미한 규칙의 조합 폭발을 억제하고, 향상도(Lift > 1) 검증을 통해 실질적인 교차 판매 인사이트 도출.",
        "diagram_title": "FP-Growth 기반 빈발 항목 집합 마이닝 절차",
        "diagram": """[트랜잭션 데이터베이스]
         │
         ▼ (1차 스캔: 빈발 1-항목 집합 식별 및 내림차순 정렬)
[FP-Tree 구축 (단 2회의 DB 스캔으로 트리 압축)]
         │
         ▼ (조건부 패턴 베이스 도출 및 재귀적 분할)
[빈발 패턴 마이닝 (후보 생성 없는 초고속 추출)]
         │
         ▼
[연관 규칙 생성: 지지도 ≥ min_sup, 신뢰도 ≥ min_conf, 향상도 > 1]""",
        "table_headers": ["구분", "Apriori 알고리즘", "FP-Growth 알고리즘"],
        "table_rows": [
            ["DB 스캔 횟수", "항목 집합 크기 $k$마다 반복 스캔 ($k$회)", "단 2회의 DB 스캔으로 완료"],
            ["후보 생성", "대규모 후보 항목 집합($C_k$) 생성 오버헤드", "후보 생성 없이 FP-Tree 구조에서 직접 추출"],
            ["실행 속도", "대용량 데이터 환경에서 극도로 느림", "메모리 트리 기반으로 수십~수백 배 고속"]
        ],
        "history": [
            "- 정보관리기술사 104회 1교시: 연관성 분석의 3대 평가 지표(지지도, 신뢰도, 향상도)",
            "- 정보관리기술사 119회 2교시: Apriori 알고리즘과 FP-Growth 알고리즘의 동작 원리 및 성능 비교",
            "- Jiawei Han, Mining Frequent Patterns without Candidate Generation"
        ],
        "links": [
            "- [데이터 마이닝](./043_data_mining.md)",
            "- [군집분석](./005_cluster_analysis.md)",
            "- [데이터 시각화](./016_data_visualization.md)"
        ]
    },
    "078_transaction.md": {
        "title": "트랜잭션(ACID)",
        "insight": "데이터베이스 무결성을 보장하기 위해 원자성(Undo 로그), 일관성(제약조건), 격리성(2PL/MVCC), 영속성(Redo 로그/WAL)의 ACID 메커니즘을 엔진 차원에서 완결 필수",
        "rec_text": "원자성과 영속성을 보장하는 WAL(Write-Ahead Logging)을 최적화하고 격리성 수준을 비즈니스 허용 한도에 맞춰 튜닝하여 고속 트랜잭션 처리량 확보.",
        "diagram_title": "ACID 보장을 위한 DBMS 엔진 메커니즘",
        "diagram": """[트랜잭션 시작] ──► [버퍼 풀(Buffer Pool) 데이터 변경]
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
[Undo Log (원자성 A)]             [Redo Log / WAL (영속성 D)]
  - 롤백 시 이전 상태 복원          - 장애 발생 시 복구(Redo 재실행)
         │                                 │
         └────────────────┬────────────────┘
                          ▼
             [동시성 제어: MVCC/2PL (격리성 I)] ──► [커밋 완료 (일관성 C)]""",
        "table_headers": ["구분", "ACID (전통적 RDBMS)", "BASE (분산 NoSQL)"],
        "table_rows": [
            ["일관성 보장", "강한 일관성 (Strict Consistency)", "최종 일관성 (Eventual Consistency)"],
            ["가용성 수준", "네트워크 분할 시 일관성 우선(CP)", "가용성 우선 타협(AP / Soft State)"],
            ["적용 영역", "금융, 결제, 재고 등 엄격한 트랜잭션", "소셜 피드, IoT 로그, 대규모 분산 캐시"]
        ],
        "history": [
            "- 정보관리기술사 101회 1교시: 트랜잭션의 4대 특징(ACID)과 구현 기술",
            "- 정보관리기술사 123회 1교시: WAL(Write-Ahead Logging)의 원리와 ARIES 회복 알고리즘",
            "- Jim Gray, Transaction Processing: Concepts and Techniques"
        ],
        "links": [
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [트랜잭션 격리 수준](./020_isolation_level.md)",
            "- [무결성 제약](./013_integrity_constraint.md)"
        ]
    },
    "081_crud_matrix.md": {
        "title": "CRUD 매트릭스",
        "insight": "비즈니스 프로세스와 데이터 엔터티 간의 누락과 고립을 방지하기 위해 생성(C)과 읽기(R)의 완결성을 2차원 교차 행렬로 전수 검증하는 모델링 필수",
        "rec_text": "모든 엔터티에 최소 하나의 C(Create)와 R(Read)이 존재하는지 검증하고 복합 프로세스의 트랜잭션 경계를 도출하여 마이크로서비스 DB 분할에 활용.",
        "diagram_title": "CRUD 매트릭스 정합성 검증 원칙",
        "diagram": """[비즈니스 기능 / 단위 프로세스] (행)
         │
         ▼ (교차 매트릭스 작성: C, R, U, D)
[데이터 엔터티] (열)
         │
         ├─ [모든 엔터티 검증 규칙]
         │        ├─ C(Create)가 없는 엔터티? ──► 유입 경로 누락 (오류)
         │        ├─ R(Read)이 없는 엔터티?   ──► 낭비되는 더미 데이터 (오류)
         │        └─ 복수 C가 존재하는 엔터티?──► 단일 책임 원칙(SRP) 위배
         ▼
[단위 시스템 및 서비스 바운디드 컨텍스트 경계 확정]""",
        "table_headers": ["구분", "단순 기능 목록 중심", "제언: CRUD 매트릭스 교차 검증"],
        "table_rows": [
            ["누락 탐지", "프로세스-데이터 불일치 방치", "생성/조회 주체 누락 100% 사전 적발"],
            ["서비스 분할", "임의적 마이크로서비스 분할", "CRUD 군집 분석(Affinity) 기반 서비스 경계 도출"],
            ["영향도 분석", "엔터티 변경 시 파급력 예측 곤란", "관련 프로세스 즉시 식별로 변경 영향 통제"]
        ],
        "history": [
            "- 정보관리기술사 95회 1교시: CRUD 매트릭스의 개념과 작성 목적 및 진단 규칙",
            "- 정보관리기술사 117회 1교시: 소프트웨어 설계에서 비즈니스 기능과 엔터티 간 상관분석",
            "- Information Engineering Methodology Standard Guide"
        ],
        "links": [
            "- [개체-관계 다이어그램(ERD)](./028_erd.md)",
            "- [데이터 모델링](./042_data_modeling.md)",
            "- [정규화](./019_normalization.md)"
        ]
    },
    "082_lod.md": {
        "title": "링크드 오픈 데이터(LOD)",
        "insight": "데이터 사일로를 해소하고 웹 스케일의 의미적 연결을 달성하기 위해 W3C 5-Star 모델에 입각한 URI 식별체계 및 RDF/SPARQL 표준 연계 필수",
        "rec_text": "공공/엔터프라이즈 데이터 개방 시 단순 파일 제공(CSV)을 넘어 온톨로지 매핑과 글로벌 고유 URI를 부여하여 시맨틱 웹 생태계와의 상호운용성 확보.",
        "diagram_title": "W3C 5-Star LOD 발전 단계 및 구조",
        "diagram": """★☆☆☆☆ (1 Star) : 웹상에 공개 (포맷 무관, PDF/이미지)
★★☆☆☆ (2 Star) : 구조화된 기계 판독 포맷 (Excel 등)
★★★☆☆ (3 Star) : 비독점 오픈 포맷 (CSV, XML, JSON)
★★★★☆ (4 Star) : W3C 오픈 표준 URI 식별자 및 RDF 트리플(Triple) 적용
★★★★★ (5 Star) : 타 데이터셋과의 외부 링크(Linked Data) 연결 확립""",
        "table_headers": ["구분", "단순 공공데이터 개방 (CSV)", "제언: 5-Star 링크드 데이터 (LOD)"],
        "table_rows": [
            ["의미적 연계", "이질적 시스템 간 데이터 결합 곤란", "온톨로지(OWL/RDFS) 기반 의미적 자동 통합"],
            ["질의 유연성", "파일 다운로드 후 개별 분석", "SPARQL 엔드포인트를 통한 글로벌 분산 질의"],
            ["데이터 가치", "단순 개별 정보 자산에 머뭄", "지식 그래프(Knowledge Graph) 형성으로 부가가치 극대화"]
        ],
        "history": [
            "- 정보관리기술사 104회 2교시: 링크드 오픈 데이터(LOD)의 4대 원칙과 5-Star 배포 단계",
            "- 정보관리기술사 122회 1교시: 시맨틱 웹을 위한 온톨로지와 RDF 트리플(Triple) 구조",
            "- Tim Berners-Lee, Linked Data Design Issues (W3C)"
        ],
        "links": [
            "- [데이터 거래·유통](./031_data_exchange.md)",
            "- [데이터 표준화](./008_data_standardization.md)",
            "- [데이터 레이크](./007_data_lake.md)"
        ]
    },
    "083_mdm.md": {
        "title": "마스터 데이터 관리(MDM)",
        "insight": "전사 단일 진실 공급원(Single Source of Truth)을 확립하기 위해 고객·상품 마스터의 통합 허브 아키텍처와 생애주기 변경 통제 거버넌스 수립 필수",
        "rec_text": "레지스트리, 허브, 하이브리드 아키텍처 중 비즈니스 실시간성 요건에 맞는 MDM 모델을 선정하고 골든 레코드(Golden Record) 생성 규칙을 표준화.",
        "diagram_title": "MDM 골든 레코드 생성 및 통합 아키텍처",
        "diagram": """[원천 시스템 A (ERP)] ──┐
[원천 시스템 B (CRM)] ──┼─► [MDM 통합 허브 엔진]
[원천 시스템 C (Web)] ──┘         │
                                  ▼
[정제/표준화] ──► [중복 제거 및 매칭(Match & Merge)] ──► [골든 레코드 확정]
                                                                │
                                                                ▼ (동기화 배포)
                                  [전사 다운스트림 시스템 및 데이터 웨어하우스(DW)]""",
        "table_headers": ["구분", "개별 시스템 마스터 분산", "제언: 중앙 집중형 MDM 허브"],
        "table_rows": [
            ["진실 공급원", "시스템별 고객 정보 불일치 (다중 버전)", "단일 진실 공급원(Single Version of Truth) 확립"],
            ["데이터 중복", "중복 등록으로 마케팅/물류 낭비", "결합 룰 기반 자동 머징으로 데이터 단일화"],
            ["통합 품질", "사후 수작업 대사로 오류 누적", "실시간 마스터 동기화로 전사 데이터 정합성 보장"]
        ],
        "history": [
            "- 정보관리기술사 105회 2교시: 마스터 데이터 관리(MDM)의 개념과 구현 방식(Registry, Repository, Hybrid)",
            "- 정보관리기술사 126회 1교시: 데이터 품질 향상을 위한 MDM 골든 레코드(Golden Record) 구축 방안",
            "- DAMA DMBOK2 Master and Reference Data Management"
        ],
        "links": [
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [데이터 품질관리](./003_data_quality_management.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "086_t_test.md": {
        "title": "t-검정",
        "insight": "모분산을 알지 못하는 소표본 환경에서 독립표본, 대응표본, 일표본 t-검정의 적용 조건을 명확히 구분하고 정규성 및 등분산성 가정을 선행 검증 필수",
        "rec_text": "등분산성 위반 시 Welch's t-test로 우회하고, 전후 비교 시 쌍체(Paired) t-검정을 적용하며 p-값과 함께 효과 크기(Cohen's d)를 필수 병행 보고.",
        "diagram_title": "t-검정 방법론 선정 의사결정",
        "diagram": """[연속형 데이터의 집단 간 평균 비교]
       │
       ├─ [단일 집단 vs 기준 모평균] ──► 일표본 t-검정 (One-Sample)
       │
       ├─ [동일 집단의 사전-사후 비교] ──► 대응표본 t-검정 (Paired t-test)
       │                                     └─ 개체 내 차이값의 정규성 검증
       │
       └─ [서로 독립된 두 집단 비교] ──► 독립표본 t-검정 (Independent)
                                            ├─ [등분산 만족] ──► 스튜던트 t-검정
                                            └─ [등분산 위반] ──► 웰치 t-검정 (Welch's)""",
        "table_headers": ["구분", "스튜던트 t-검정 (Student)", "웰치의 t-검정 (Welch)"],
        "table_rows": [
            ["등분산성 가정", "두 집단의 모분산이 동일함을 전제", "두 집단의 분산이 서로 달라도 성립"],
            ["자유도 계산", "$df = n_1 + n_2 - 2$ (단순 정수)", "복잡한 근사 수식으로 유효 자유도 계산"],
            ["실무 권장도", "등분산 검정(Levene) 선행 필수", "실무적으로 더 안전하고 강력하여 기본 권장"]
        ],
        "history": [
            "- 정보관리기술사 119회 1교시: 가설검정에서 z-검정과 t-검정의 적용 조건 비교",
            "- 정보관리기술사 124회 2교시: 독립표본 t-검정과 대응표본 t-검정의 원리 및 가설 검증 절차",
            "- Statistical Inference for Data Science"
        ],
        "links": [
            "- [z-검정](./012_z_test.md)",
            "- [가설검정](./041_hypothesis_testing.md)",
            "- [불편추정량](./011_unbiased_estimator.md)"
        ]
    },
    "088_database_tuning.md": {
        "title": "데이터베이스 튜닝",
        "insight": "병목 구간의 과학적 식별을 위해 비즈니스 모델링부터 SQL, 인덱스, 인스턴스, OS/하드웨어 계층까지 하향식(Top-Down) 체계적 튜닝 파이프라인 정립 필수",
        "rec_text": "비용 대비 효과가 가장 높은 SQL 및 인덱스 튜닝을 우선 실행하고 대량 I/O 병목은 파티셔닝과 버퍼 풀 최적화를 통해 밀리초 단위 쿼리 응답 보장.",
        "diagram_title": "데이터베이스 튜닝 4계층 접근법",
        "diagram": """[1계층: 비즈니스/데이터 모델 튜닝] (효과 극대, 비용 극소)
  - 정규화/반정규화 최적화, 파티셔닝 설계, 아카이빙
       │
       ▼
[2계층: SQL 및 인덱스 튜닝] (실무 핵심, 80% 성능 개선 달성)
  - 실행계획 분석, 커버링 인덱스, 힌트(Hint), 조인 순서 최적화
       │
       ▼
[3계층: DBMS 인스턴스 튜닝]
  - 버퍼 풀(Buffer Pool) 확대, 동시성 락 파라미터, 체크포인트 튜닝
       │
       ▼
[4계층: OS 및 하드웨어 튜닝]
  - NVMe SSD 도입, 커널 I/O 스케줄러, 파일시스템 마운트 옵션 최적화""",
        "table_headers": ["구분", "하드웨어 증설 중심 (Scale-Up)", "제언: 소프트웨어 계층 튜닝"],
        "table_rows": [
            ["개선 비용", "클라우드 인스턴스 비용 지속 증가", "비용 발생 없이 SQL/인덱스 최적화로 성능 극대화"],
            ["근본 해결", "비효율 쿼리 존속으로 재차 병목 도달", "Full Table Scan 제거 등 근본 원인 해결"],
            ["확장 한계", "서버 단일 스케일업 한계 도달", "아키텍처 최적화로 처리량 수배 이상 확장"]
        ],
        "history": [
            "- 정보관리기술사 103회 2교시: 데이터베이스 성능 튜닝의 절차와 3단계(설계, 환경, SQL) 튜닝 기법",
            "- 정보관리기술사 121회 2교시: 대용량 데이터베이스에서 SQL 실행계획(Execution Plan) 분석 및 튜닝",
            "- Database Performance Tuning Handbook"
        ],
        "links": [
            "- [인덱스](./047_index.md)",
            "- [반정규화](./017_denormalization.md)",
            "- [동시성 제어](./009_concurrency_control.md)"
        ]
    }
}

for fname, data in batch_4_data.items():
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
        m_tags = re.findall(r'-\s*"([^"]+)"', fm_match.group(1))
        if not m_tags:
            m_tags = ["notes-data"]
        tags_str = '\n'.join([f'  - "{t}"' for t in m_tags])
        new_fm = f"""---
title: "{data['title']}"
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
    else:
        new_fm = f"""---
title: "{data['title']}"
category: "03-data"
tags:
  - "notes-data"
date: "2026-09-28T22:36:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
sidebar:
  badge:
    text: "기초"
---
"""
        content = new_fm + content

    # 2. Fix 30초 인출 통찰
    content = re.sub(
        r'^- (?:\*\*)?통찰(?:\*\*)?:.*$',
        f'- 통찰: {data["insight"]}',
        content,
        flags=re.MULTILINE
    )

    # 3. Fix Ⅵ. 제언
    t_hdrs = data["table_headers"]
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

    rec_pos = content.find('## Ⅵ.')
    if rec_pos != -1:
        pre_rec = content[:rec_pos].rstrip()
    else:
        pre_rec = content.rstrip()

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
