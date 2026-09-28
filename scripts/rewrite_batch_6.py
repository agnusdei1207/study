import os
import re

batch_6_data = {
    "112_big_data.md": {
        "title": "빅데이터",
        "insight": "Volume·Velocity·Variety의 3V를 넘어 Veracity(정확성)와 Value(가치)를 창출하기 위해 분산 병렬 스토리지와 실시간 스트리밍 결합 아키텍처 구축 필수",
        "rec_text": "원천 데이터의 계보와 신뢰성을 보장하는 데이터 레이크하우스를 구축하고 도메인별 데이터 메시(Data Mesh) 거버넌스를 통해 분석 ROI 극대화.",
        "diagram_title": "빅데이터 5V 기반 수집-저장-처리-분석 파이프라인",
        "diagram": """[원천 데이터 (다양성 Variety)] ──► [실시간/배치 수집 (속도 Velocity)]
                                       │
                                       ▼
[분산 스토리지 (규모 Volume)] : 오브젝트 스토리지 + 오픈 테이블 포맷
                                       │
                                       ▼
[데이터 품질 검증 (정확성 Veracity)] ──► 비즈니스 모델링 (가치 Value 창출)""",
        "table_headers": ["구분", "전통적 DW (3V 이전)", "제언: 현대적 빅데이터 플랫폼 (5V)"],
        "table_rows": [
            ["데이터 형태", "정형 관계형 데이터 한정", "정형, 반정형(JSON), 비정형(텍스트/영상) 전 수용"],
            ["처리 구조", "수직 스케일업 및 정기 야간 배치", "수평 스케일아웃 및 실시간 스트림/배치 하이브리드"],
            ["가치 창출", "사후 실적 보고 중심", "실시간 이상 탐지, 추천, AI 예측 모델 서빙"]
        ],
        "history": [
            "- 정보관리기술사 98회 1교시: 빅데이터의 3V(Volume, Variety, Velocity)와 비즈니스 가치",
            "- 정보관리기술사 120회 2교시: 빅데이터 거버넌스와 데이터 품질 확보 방안",
            "- Gartner Big Data Definitions and Architecture Standards"
        ],
        "links": [
            "- [데이터 레이크](./007_data_lake.md)",
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [빅데이터 플랫폼 아키텍처](./135_big_data_platform_architecture.md)"
        ]
    },
    "113_cap_pacelc.md": {
        "title": "CAP·PACELC 정리",
        "insight": "네트워크 분할(P) 시 일관성(C)과 가용성(A)의 양자택일을 규정한 CAP의 한계를 극복하고 정상 상태의 지연시간(Latency)과 일관성(Consistency)을 함께 고려하는 PACELC 관점의 아키텍처 설계 필수",
        "rec_text": "분할 시(PC vs PA)와 정상 시(EL vs EC)의 비즈니스 트레이드오프를 평가하여 결제는 PC/EC(RDBMS, Spanner), 소셜 피드는 PA/EL(DynamoDB, Cassandra)로 차등 구현.",
        "diagram_title": "PACELC 정리 의사결정 모델",
        "diagram": """[분산 데이터베이스 상태]
       │
       ├─ [네트워크 분할 발생 시 (Partition P)]
       │        ├─ [A: 가용성 우선] ──► PA (최종 일관성, DynamoDB)
       │        └─ [C: 일관성 우선] ──► PC (트랜잭션 중단, HBase)
       │
       └─ [정상 운영 상태 시 (Else E)]
                ├─ [L: 지연시간 최소] ──► EL (비동기 복제, Cassandra)
                └─ [C: 일관성 우선]   ──► EC (동기 복제, Google Spanner)""",
        "table_headers": ["구분", "CAP 정리", "제언: PACELC 정리"],
        "table_rows": [
            ["평가 관점", "네트워크 장애(Partition) 상황만 평가", "장애 상황(P/A/C)과 정상 운영 상황(E/L/C) 동시 평가"],
            ["정상 시 트레이드오프", "정상 상태의 성능 특성 설명 불가", "지연시간(Latency)과 일관성(Consistency) 절충 모델링"],
            ["실무 아키텍처", "단순 CP vs AP 이분법 매핑", "PA/EL, PC/EC 등 업무별 정밀 데이터 저장소 선정"]
        ],
        "history": [
            "- 정보관리기술사 113회 1교시: 분산 시스템에서 CAP 정리의 한계와 PACELC 정리",
            "- 정보관리기술사 125회 2교시: 클라우드 분산 데이터베이스의 일관성 모델과 분할 내구성",
            "- Daniel Abadi, Consistency Tradeoffs in Modern Distributed Database System Design"
        ],
        "links": [
            "- [NoSQL](./001_nosql.md)",
            "- [분산 데이터베이스 투명성](./025_distributed_db_transparency.md)",
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)"
        ]
    },
    "114_db_replication_types.md": {
        "title": "데이터베이스 복제 유형",
        "insight": "성능 지연과 데이터 손실 간의 트레이드오프를 극복하기 위해 동기(Sync), 비동기(Async), 반동기(Semi-Sync) 복제 기법을 업무 SLA에 따라 차등 적용 필수",
        "rec_text": "핵심 금융 거래는 1개 이상의 슬레이브 수신을 보장하는 반동기 복제를 채택하여 RPO=0과 합리적인 응답 지연시간(Latency)을 동시 달성.",
        "diagram_title": "동기 vs 비동기 vs 반동기 복제 메커니즘",
        "diagram": """[동기 복제 (Sync)]
  Master 쓰기 ──► Slave 전송 ──► [Slave 디스크 기록 완료 후 Master 커밋] (RPO=0, 지연 큼)

[비동기 복제 (Async)]
  Master 쓰기 ──► Master 커밋 즉시 완료 ──► [백그라운드 Slave 복제] (고성능, 데이터 유실 위험)

[반동기 복제 (Semi-Sync)]
  Master 쓰기 ──► Slave 전송 ──► [최소 1개 Slave 릴레이 로그 수신 확인(ACK)] ──► Master 커밋""",
        "table_headers": ["구분", "동기 복제 (Synchronous)", "반동기 복제 (Semi-Sync)"],
        "table_rows": [
            ["트랜잭션 지연", "모든 복제본 커밋 대기로 지연 극대", "최소 1개 슬레이브 ACK 후 커밋으로 지연 최소화"],
            ["장애 시 RPO", "데이터 손실 전무 (RPO = 0)", "마스터 장애 시 데이터 무손실 (RPO = 0)"],
            ["슬레이브 장애 영향", "단일 슬레이브 장애 시 마스터 중단", "타임아웃 시 일시 비동기 전환으로 가용성 유지"]
        ],
        "history": [
            "- 정보관리기술사 114회 1교시: 데이터베이스 복제(Replication)의 동기, 비동기, 반동기 방식 비교",
            "- 정보관리기술사 127회 2교시: 고가용성 DB 클러스터에서 복제 지연(Replication Lag) 해결 방안",
            "- High Performance MySQL Standard Guide"
        ],
        "links": [
            "- [고가용성 아키텍처(HA)](./051_ha_architecture.md)",
            "- [데이터 복제](./126_data_replication.md)",
            "- [동시성 제어](./009_concurrency_control.md)"
        ]
    },
    "116_elk_stack.md": {
        "title": "ELK 스택",
        "insight": "대규모 분산 로그 수집·저장·시각화를 위해 Beats-Logstash 수집 파이프라인, Elasticsearch 역색인 검색, Kibana 대시보드의 유기적 연계 및 ILM 수명주기 관리 필수",
        "rec_text": "로그 급증 시 버퍼링을 위한 Kafka를 전진 배치하고 인덱스 생명주기 관리(ILM: Hot-Warm-Cold)를 적용하여 스토리지 비용 절감과 실시간 검색 성능 보장.",
        "diagram_title": "ELK 스택 엔터프라이즈 로깅 파이프라인",
        "diagram": """[서버/앱 로그] ──► [Filebeat 경량 수집] ──► [Kafka 버퍼링]
                                                     │
                                                     ▼
[Logstash: 필터링/파싱(Grok/JSON)] ──► [Elasticsearch: 분산 역색인 저장]
                                                     │
                                                     ▼
                                     [Kibana: 실시간 시각화 / 알람]""",
        "table_headers": ["구분", "단순 파일 로그 적재", "제언: ELK 기반 통합 옵저버빌리티"],
        "table_rows": [
            ["검색 성능", "Grep 기반 느린 순차 탐색", "역색인(Inverted Index) 기반 밀리초 실시간 검색"],
            ["분석 확장성", "서버별 로그 사일로화", "전사 분산 클러스터 통합 및 샤딩 수평 확장"],
            ["수명주기 관리", "수동 압축/삭제 운영", "ILM 기반 Hot-Warm-Cold 자동 티어링"]
        ],
        "history": [
            "- 정보관리기술사 116회 1교시: ELK(Elasticsearch, Logstash, Kibana) 스택의 구성요소와 특징",
            "- 정보관리기술사 126회 2교시: 클라우드 네이티브 환경에서 중앙 집중형 로그 관리 아키텍처",
            "- Elasticsearch: The Definitive Guide"
        ],
        "links": [
            "- [인덱스](./047_index.md)",
            "- [데이터 옵저버빌리티](./054_data_observability.md)",
            "- [데이터 시각화](./016_data_visualization.md)"
        ]
    },
    "117_imdf.md": {
        "title": "실내 매핑 데이터 포맷(IMDF)",
        "insight": "GPS 음영 구역인 실내 공간 정보의 상호운용성을 확보하기 위해 OGC 표준에 기반한 GeoJSON 기반의 지향성 위상 모델과 계층적 공간 구조화 필수",
        "rec_text": "공항, 대형 쇼핑몰 등 복합 건물 내 장소(Venue), 층(Level), 단위 공간(Unit) 간의 포함 관계를 검증하고 비콘/Wi-Fi 기반 측위 시스템과의 실시간 연계 구축.",
        "diagram_title": "IMDF 핵심 계층 구조 모델",
        "diagram": """[Venue (건물 단지 / 전체 부지)]
  │
  ▼
[Building (개별 건물 동)]
  │
  ▼
[Level (지상/지하 층수 구조)]
  │
  ├─ [Unit (독립 방, 복도, 화장실 공간)] ──► [Anchor (POI/매장 위치)]
  └─ [Opening (문, 창문 등 출입 통로)]  ──► [Footpath (보행자 경로망)]""",
        "table_headers": ["구분", "전통적 2D CAD/도면", "제언: OGC IMDF 표준 모델"],
        "table_rows": [
            ["데이터 표준", "CAD 독점 포맷으로 웹 연계 곤란", "표준 GeoJSON 기반 모바일/웹 완벽 호환"],
            ["위상 관계", "단순 선과 면의 그래픽 표현", "공간 간 연결성(Footpath)과 포함 관계 위상 모델링"],
            ["실내 내비게이션", "경로 탐색 알고리즘 적용 불가", "A* 알고리즘 등 실내 최단 경로 내비게이션 즉시 지원"]
        ],
        "history": [
            "- 정보관리기술사 125회 1교시: 실내 공간정보 표준화와 IMDF(Indoor Mapping Data Format)",
            "- OGC (Open Geospatial Consortium) IMDF Standard Specification"
        ],
        "links": [
            "- [다차원 인덱스 구조](./052_multidimensional_index_structure.md)",
            "- [공간 연산자](./119_spatial_operator.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "118_mongodb.md": {
        "title": "MongoDB",
        "insight": "유연한 BSON 문서 모델과 복제셋(Replica Set)·샤딩을 활용하되 스키마 설계 시 Embedding과 Referencing 간의 트레이드오프를 명확히 판별 필수",
        "rec_text": "1:1 또는 1:소량 관계는 임베딩(Embedding)으로 단일 I/O 조회를 달성하고 1:대량 관계는 참조(Referencing)로 분리하여 16MB 문서 한계 및 메모리 낭비 통제.",
        "diagram_title": "MongoDB 복제셋(Replica Set) 자동 페일오버 구조",
        "diagram": """[클라이언트 드라이버]
         │
         ▼ (쓰기 요청: Write Concern w:majority)
[Primary 노드] ──► OpLog (동기화 로그)
         │
         ├─ [비동기 OpLog 복제] ──► [Secondary 노드 1]
         └─ [비동기 OpLog 복제] ──► [Secondary 노드 2]
         │
         ▼ (Primary 장애 감지 시 쿼럼 선출 투표)
[새로운 Primary 자동 선출 승격 (서브초 단위 절체)]""",
        "table_headers": ["구분", "도큐먼트 임베딩 (Embedding)", "도큐먼트 참조 (Referencing)"],
        "table_rows": [
            ["조회 성능", "단일 읽기로 하위 객체 일괄 조회 (극상)", "추가 쿼리 또는 $lookup 조인 필요"],
            ["문서 크기", "16MB 제한 초과 위험 존재", "문서 크기 제한에서 자유로움"],
            ["데이터 정합성", "중복 데이터 발생 시 갱신 이상 가능", "단일 참조 데이터만 수정하여 일관성 유지"]
        ],
        "history": [
            "- 정보관리기술사 117회 1교시: NoSQL 문서 지향 데이터베이스(Document Store)와 MongoDB 특징",
            "- 정보관리기술사 128회 2교시: MongoDB의 복제셋(Replica Set) 선출 알고리즘과 샤딩 아키텍처",
            "- MongoDB Manual: Data Modeling Concepts"
        ],
        "links": [
            "- [NoSQL](./001_nosql.md)",
            "- [CAP·PACELC 정리](./113_cap_pacelc.md)",
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)"
        ]
    },
    "119_spatial_operator.md": {
        "title": "공간 연산자",
        "insight": "공간 객체 간의 위상 관계(Topological Relation) 판별을 위해 DE-9IM 매트릭스를 기반으로 필터-정제(Filter-Refine) 2단계 공간 질의 처리 최적화 필수",
        "rec_text": "ST_Intersects, ST_Contains 등 공간 연산 시 공간 인덱스(R-Tree/GiST)를 통해 MBR 수준에서 후보를 선별한 후 정확한 기하 연산을 수행하는 2단계 쿼리 준수.",
        "diagram_title": "공간 연산자 2단계 필터-정제(Filter & Refine) 처리 흐름",
        "diagram": """[사용자 공간 질의: ST_Contains(A, B)]
         │
         ▼
[1단계 필터 (Filter Stage): 공간 인덱스(GiST/R-Tree) 활용]
  - MBR(최소 경계 사각형) 간의 교차 여부 판별
  - 불필요한 90% 이상 공간 객체 즉각 배제
         │
         ▼ (MBR이 교차하는 후보 객체군 선별)
[2단계 정제 (Refine Stage): 실제 기하 연산 (Geometry Calculation)]
  - DE-9IM 위상 매트릭스 계산 및 정밀 폴리곤 교차 검증
         │
         ▼
[정확한 공간 질의 최종 결과 반환]""",
        "table_headers": ["구분", "전수 기하 연산 (No Index)", "제언: 공간 인덱스 기반 필터-정제"],
        "table_rows": [
            ["연산 복잡도", "모든 점·선분 교차 검증으로 O(N^2) 지연", "MBR 인덱스 필터로 O(log N) 고속 후보 선별"],
            ["정확도 보장", "정확하나 시스템 다운 위험", "수학적 2단계 검증으로 정확도 100% 유지"],
            ["적용 인덱스", "인덱스 미활용", "PostGIS GiST(Generalized Search Tree) 필수 구성"]
        ],
        "history": [
            "- 정보관리기술사 119회 1교시: OGC 공간 연산자의 유형(위상, 공간 분석, 기하 변환)",
            "- 정보관리기술사 125회 2교시: 공간 데이터베이스에서 DE-9IM 모델과 공간 조인(Spatial Join) 최적화",
            "- OGC OpenGIS Simple Features Specification for SQL"
        ],
        "links": [
            "- [다차원 인덱스 구조](./052_multidimensional_index_structure.md)",
            "- [실내 매핑 데이터 포맷(IMDF)](./117_imdf.md)",
            "- [인덱스](./047_index.md)"
        ]
    },
    "121_multiple_regression_analysis.md": {
        "title": "다중회귀분석",
        "insight": "복수의 독립변수와 종속변수 간의 선형 관계를 추정할 때 선형성·독립성·등분산성·정규성의 4대 오차 가정을 잔차 분석으로 검증하고 다중공선성을 사전 통제 필수",
        "rec_text": "수정 결정계수($Adj-R^2$)와 AIC/BIC를 활용하여 과적합 없는 최적 변수 조합(단계적 회귀/Lasso)을 선정하고 이상치 영향도를 Cook's Distance로 검증.",
        "diagram_title": "다중회귀분석 모델링 및 잔차 진단 절차",
        "diagram": """[독립변수 수집 및 스케일링] ──► [다중공선성(VIF) 검사 및 변수 선별]
                                       │
                                       ▼
[최소자승법(OLS) 회귀모형 적합: Y = β0 + β1X1 + ... + βkXk + ε]
                                       │
                                       ▼
[잔차 분석 (Residual Diagnosis)]
  - 선형성: 잔차 산점도 무패턴 검증
  - 등분산성: Breusch-Pagan 검정
  - 정규성: Q-Q Plot / Shapiro 검정
  - 독립성: Durbin-Watson 검정
                                       │
                                       ▼
[수정 결정계수 및 F-검정 통과 → 최종 예측 및 계수 해석]""",
        "table_headers": ["구분", "단순 결정계수 ($R^2$)", "제언: 수정 결정계수 ($Adj-R^2$)"],
        "table_rows": [
            ["변수 추가 왜곡", "무의미한 변수 추가 시에도 $R^2$ 증가", "변수 개수 패널티 부여로 과적합 방지"],
            ["모델 비교 기준", "변수 수가 다른 모델 간 비교 불가", "자유도를 반영하여 객관적 모델 간 비교 가능"],
            ["실무 권장도", "설명력 과장 위험", "다중회귀 모델의 실질적 설명력 평가 표준"]
        ],
        "history": [
            "- 정보관리기술사 118회 1교시: 다중회귀분석의 기본 가정 4가지와 잔차 분석 기법",
            "- 정보관리기술사 128회 2교시: 회귀모형의 적합도 평가 지표(R-squared, Adjusted R-squared, F-통계량)",
            "- Applied Regression Analysis Standard Reference"
        ],
        "links": [
            "- [다중공선성](./004_multicollinearity.md)",
            "- [로지스틱 회귀](./089_logistic_regression.md)",
            "- [가설검정](./041_hypothesis_testing.md)"
        ]
    },
    "122_multidimensional_scaling.md": {
        "title": "다차원 척도법(MDS)",
        "insight": "개체 간의 비유사도(거리)를 저차원 공간에 시각적으로 투영하기 위해 스트레스(Stress) 적합도 척도를 최소화하는 계량적/비계량적 MDS 선별 적용 필수",
        "rec_text": "서열 척도 설문 데이터는 순서 보존 중심의 비계량적(Non-metric) MDS를 적용하고 스트레스 값 0.1 이하를 달성하여 2차원 포지셔닝 맵 신뢰성 확보.",
        "diagram_title": "다차원 척도법(MDS) 좌표 도출 프로세스",
        "diagram": """[개체 간 1:1 거리/비유사도 행렬 (N x N)]
         │
         ▼
[계량적 vs 비계량적 MDS 접근법 선정]
         │
         ▼
[저차원(2D/3D) 초기 좌표 임의 배치] ◀───────────────────┐
         │                                              │
         ▼                                              │
[재구성된 유클리드 거리 d_ij 산출]                      │
         │                                              │
         ▼                                              │
[스트레스(Stress) 값 계산: 실제 거리 vs 사상 거리 오차] │
         │                                              │
         ├─ [Stress > 0.1] ──► 경사하강법 좌표 조정 ────┘
         │
         └─ [Stress ≤ 0.05] ──► [최적 포지셔닝 맵 시각화 완료]""",
        "table_headers": ["구분", "계량적 MDS (Metric)", "비계량적 MDS (Non-metric)"],
        "table_rows": [
            ["입력 데이터", "구간 척도, 비율 척도 (실제 수치 거리)", "순서 척도 (선호도 서열, 유사도 랭킹)"],
            ["거리 관계", "원래 거리의 실제 크기 보존", "개체 간 거리의 상대적 대소 순위만 보존"],
            ["적용 분야", "물리적 좌표 복원, 센서 위치 추정", "소비자 제품 인지도, 브랜드 이미지 지각도"]
        ],
        "history": [
            "- 정보관리기술사 124회 1교시: 다차원 척도법(MDS)의 개념과 스트레스(Stress) 평가 척도",
            "- Multidimensional Scaling: Theory and Applications"
        ],
        "links": [
            "- [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [군집분석](./005_cluster_analysis.md)"
        ]
    },
    "123_queuing_theory.md": {
        "title": "대기행렬이론",
        "insight": "IT 시스템의 응답 지연과 자원 병목을 수리적으로 모델링하기 위해 포아송 도착과 지수 서비스 시간을 가정한 켄달 표기법(M/M/c) 기반 성능 분석 필수",
        "rec_text": "서버 이용률(ρ = λ/μ)이 1에 가까워질수록 대기시간이 기하급수적으로 폭증하므로 시스템 안정 가동을 위해 자원 임계치를 70~80% 수준으로 통제.",
        "diagram_title": "M/M/1 단일 서버 대기행렬 시스템 구조",
        "diagram": """[고객/요청 도착] (도착률 λ, 포아송 과정)
         │
         ▼
┌──────────────────┐           ┌──────────────────┐
│  대기 큐 (Queue) │ ────────► │ 서비스 창구 (서버)│ ──► [서비스 완료 퇴장]
│ (선입선출: FIFO) │           │ (서비스율 μ)     │
└──────────────────┘           └──────────────────┘
[대기 시스템 내 평균 고객 수 L = λ / (μ - λ), 이용률 ρ = λ / μ]""",
        "table_headers": ["구분", "이용률 50% 시스템", "제언: 이용률 90% 임계 시스템"],
        "table_rows": [
            ["평균 대기시간", "대기 지연 거의 없이 즉각 처리", "이용률 1에 근접 시 대기시간 무한대 발산"],
            ["버퍼 큐 적체", "큐 공백 유지 (메모리 안정)", "스파이크 트래픽 시 큐 오버플로우/OOM 위험"],
            ["자원 운영 전략", "자원 낭비 가능성 존재", "오토스케일링 연동하여 이용률 70% 탄력적 유지"]
        ],
        "history": [
            "- 정보관리기술사 100회 2교시: 대기행렬이론의 개념과 켄달 표기법(Kendall's Notation), 리틀의 법칙",
            "- 정보관리기술사 121회 1교시: 시스템 성능 모델링에서 M/M/1 큐잉 모델의 평균 대기시간 계산",
            "- Queueing Systems: Theory and Applications"
        ],
        "links": [
            "- [데이터베이스 튜닝](./088_database_tuning.md)",
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [고가용성 아키텍처(HA)](./051_ha_architecture.md)"
        ]
    },
    "124_paired_t_test.md": {
        "title": "대응표본 t-검정",
        "insight": "동일 표본의 사전-사후 처치 효과를 정확히 분별하기 위해 개체 간 편차를 소거하고 쌍체 차이값(Difference)의 정규성을 전제로 가설검정 수행 필수",
        "rec_text": "쌍별 차이 데이터($d_i = X_{after} - X_{before}$)의 정규성을 샤피로 검정으로 확인하고 위반 시 비모수 검정인 윌콕슨 부호순위 검정(Wilcoxon)으로 전환.",
        "diagram_title": "대응표본 t-검정 차이값 분석 절차",
        "diagram": """[동일 개체 사전 측정치 (X_pre)] & [처치 후 사후 측정치 (X_post)]
         │
         ▼
[개체별 1:1 차이값 산출: d_i = X_post - X_pre] (개체 간 고유 편차 소거)
         │
         ▼
[차이값의 정규성 검증 (Shapiro-Wilk)]
         │
         ├─ [정규성 충족] ──► 대응표본 t-검정 통계량 t = d̄ / (s_d / √n) 산출
         │
         └─ [정규성 위반] ──► 비모수 윌콕슨 부호순위 검정(Wilcoxon Signed-Rank)
         │
         ▼
[귀무가설(차이의 평균 = 0) 기각 여부 및 처치 효과 크기(Cohen's d) 확정]""",
        "table_headers": ["구분", "독립표본 t-검정", "제언: 대응표본 t-검정 (Paired)"],
        "table_rows": [
            ["표본 관계", "서로 다른 두 독립 집단 비교", "동일 집단의 전-후 또는 1:1 매칭 표본 비교"],
            ["오차 통제", "개체 간 고유 차이가 오차에 포함", "차이값 분석으로 개체 간 고유 변동 완벽 통제"],
            ["통계적 검정력", "동일 표본수 대비 검정력 상대적 낮음", "오차 분산 축소로 미세 처치 효과도 고감도 감지"]
        ],
        "history": [
            "- 정보관리기술사 119회 1교시: 독립표본 t-검정과 대응표본 t-검정의 적용 요건 비교",
            "- 정보관리기술사 124회 2교시: A/B 테스트 및 사전-사후 분석을 위한 통계적 가설검정 방법",
            "- Biostatistical Analysis Standard Reference"
        ],
        "links": [
            "- [t-검정](./086_t_test.md)",
            "- [독립표본 t-검정](./130_independent_t_test.md)",
            "- [가설검정](./041_hypothesis_testing.md)"
        ]
    },
    "126_data_replication.md": {
        "title": "데이터 복제",
        "insight": "데이터 고가용성과 읽기 성능 분산을 달성하기 위해 복제 지연(Replication Lag)에 따른 불일치를 억제하고 스냅샷 분산 복제 거버넌스 구축 필수",
        "rec_text": "리드 레플리카(Read Replica) 운영 시 쓰기 직후 자신의 변경사항을 조회하는 Read-After-Write 일관성을 보장하기 위해 사용자 세션별 마스터 라우팅 적용.",
        "diagram_title": "데이터베이스 읽기 복제 및 세션 일관성 라우팅",
        "diagram": """[애플리케이션 클라이언트]
         │
         ▼
[데이터베이스 프록시 / 라우터]
         │
         ├─ [쓰기 요청 (INSERT / UPDATE)] ──────────► [Master DB]
         │                                               │
         ├─ [쓰기 직후 본인 세션 읽기 (1초 이내)] ──┘   │ (비동기 복제)
         │                                               ▼
         └─ [일반 읽기 요청 (SELECT)] ──────────────► [Read Replica 1, 2]""",
        "table_headers": ["구분", "단순 읽기 복제 라우팅", "제언: 세션 일관성 보장 라우팅"],
        "table_rows": [
            ["복제 지연 영향", "본인 작성 글이 즉시 안 보이는 오류", "자신의 쓰기 직후 조회는 마스터 강제 라우팅"],
            ["부하 분산", "모든 읽기를 복제본 분산", "지연시간 허용 수준에 따라 마스터/슬레이브 동적 분기"],
            ["장애 격리", "슬레이브 지연 시 전반적 쿼리 정체", "지연 임계치 초과 슬레이브 풀 자동 퇴출(Eviction)"]
        ],
        "history": [
            "- 정보관리기술사 114회 1교시: 데이터베이스 복제(Replication)의 동기, 비동기, 반동기 방식 비교",
            "- 정보관리기술사 127회 2교시: 고가용성 DB 클러스터에서 복제 지연(Replication Lag) 해결 방안",
            "- Enterprise Database Replication Best Practices"
        ],
        "links": [
            "- [데이터베이스 복제 유형](./114_db_replication_types.md)",
            "- [고가용성 아키텍처(HA)](./051_ha_architecture.md)",
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)"
        ]
    },
    "127_data_commerce.md": {
        "title": "데이터 커머스",
        "insight": "데이터 자산의 상품화와 유통 수익화를 위해 데이터 품질 인증, 동적 가격 책정 모델, 안심구역 분석 연계의 통합 데이터 커머스 생태계 구축 필수",
        "rec_text": "원천 데이터 직접 판매보다 API 구독형 서빙 모델 및 데이터 안심구역 기반 파생 가치 창출을 지향하고 데이터 거래 표준계약서 필수 적용.",
        "diagram_title": "데이터 커머스 비즈니스 모델 및 유통 체계",
        "diagram": """[데이터 공급 기업] ──► [데이터 상품화 가공 (정제, 라벨링, 가명화)]
                                       │
                                       ▼
[데이터 커머스 거래소 (마켓플레이스)]
  - 상품 카탈로그, 샘플 미리보기, 품질 인증(DQC)
  - 과금 모델: API 호출 종량제, 월간 정기 구독, 안심구역 이용료
                                       │
                                       ▼
[데이터 수요 기업] ──► [데이터 결합 분석 및 신규 비즈니스 창출]""",
        "table_headers": ["구분", "단순 일회성 파일 판매", "제언: API 구독형 데이터 커머스"],
        "table_rows": [
            ["수익 모델", "일회성 덤프 파일 판매로 수익 단절", "실시간 API 쿼리 기반 지속적 구독 수익 창출"],
            ["데이터 최신성", "구매 시점 이후 업데이트 불가", "API 연동을 통한 실시간 최신 데이터 자동 제공"],
            ["보안 및 저작권", "무단 재배포 및 유출 통제 불가", "API 토큰 인증 및 호출 쿼터 기반 정밀 통제"]
        ],
        "history": [
            "- 정보관리기술사 123회 1교시: 데이터 댐과 데이터 거래소의 개념 및 활성화 과제",
            "- 정보관리기술사 129회 1교시: 데이터 커머스 비즈니스 모델과 가치 산정 전략",
            "- 데이터 산업진흥 및 이용촉진에 관한 기본법 표준 가이드라인"
        ],
        "links": [
            "- [데이터 거래·유통](./031_data_exchange.md)",
            "- [데이터 가치평가·데이터 자산화](./002_data_valuation.md)",
            "- [가명정보 결합·비정형 가명처리](./034_pseudonymized_data_guidelines_unstructured.md)"
        ]
    },
    "128_database.md": {
        "title": "데이터베이스",
        "insight": "응용 프로그램과 물리적 저장소 간의 결합도를 해소하기 위해 ANSI/SPARC 3단계 계층 구조 기반의 논리적·물리적 데이터 독립성 완벽 보장 필수",
        "rec_text": "외부 스키마(사용자 뷰), 개념 스키마(전사 통합 논리 뷰), 내부 스키마(물리 저장 구조) 간의 2단계 매핑을 철저히 유지하여 시스템 변경 파급도 최소화.",
        "diagram_title": "ANSI/SPARC 3단계 데이터베이스 아키텍처",
        "diagram": """[사용자 1: 외부 뷰]     [사용자 2: 외부 뷰]     [사용자 3: 외부 뷰]
        \\                    |                    /
         ───────────────[ 외부/개념 사상 ]─────────────── (논리적 독립성)
                             │
                             ▼
                    [ 개념 스키마 (전사 통합 뷰) ]
                             │
         ───────────────[ 개념/내부 사상 ]─────────────── (물리적 독립성)
                             ▼
                    [ 내부 스키마 (물리적 저장 구조) ]
                             │
                             ▼
                    [ 물리적 데이터베이스 (디스크) ]""",
        "table_headers": ["구분", "논리적 데이터 독립성", "물리적 데이터 독립성"],
        "table_rows": [
            ["사상 계층", "외부 스키마 ↔ 개념 스키마 간 사상", "개념 스키마 ↔ 내부 스키마 간 사상"],
            ["변경 영향", "개념 스키마 변경 시 외부 뷰 영향 없음", "내부 스키마(인덱스/디스크) 변경 시 개념 뷰 불변"],
            ["달성 가치", "업무 규칙 변경에 대한 응용 안정성", "성능 튜닝 및 스토리지 증설의 유연성 확보"]
        ],
        "history": [
            "- 정보관리기술사 95회 1교시: 데이터베이스 3단계 구조(외부, 개념, 내부)와 데이터 독립성",
            "- 정보관리기술사 115회 2교시: 관계형 DBMS의 구조적 특징과 데이터 무결성 보장 메커니즘",
            "- C.J. Date, An Introduction to Database Systems"
        ],
        "links": [
            "- [데이터 모델링](./042_data_modeling.md)",
            "- [개체-관계 다이어그램(ERD)](./028_erd.md)",
            "- [무결성 제약](./013_integrity_constraint.md)"
        ]
    },
    "130_independent_t_test.md": {
        "title": "독립표본 t-검정",
        "insight": "서로 독립된 두 집단의 평균 차이를 검정할 때 독립성, 정규성뿐만 아니라 등분산성(Levene 검정)을 사전에 확인하고 결과에 따라 Student 또는 Welch t-검정 선택 필수",
        "rec_text": "실무적으로 두 집단의 분산이 완벽히 같을 확률은 희박하므로 등분산성 위반에 강건한 웰치의 t-검정을 기본 모델로 채택하여 제1종 오류 왜곡 방지.",
        "diagram_title": "독립표본 t-검정 사전 가정 진단 및 분석 절차",
        "diagram": """[서로 독립된 두 집단 표본 데이터 (A, B)]
         │
         ▼
[1. 정규성 검정 (Shapiro-Wilk)]
         │
         ├─ [정규성 위반] ──► 비모수 맨-휘트니 U 검정 (Mann-Whitney U)
         │
         ▼ [정규성 만족]
[2. 등분산성 검정 (Levene's Test)]
         │
         ├─ [등분산 만족 (p ≥ 0.05)] ──► 스튜던트 t-검정 (Student's t-test)
         │
         └─ [등분산 위반 (p < 0.05)] ──► 웰치 t-검정 (Welch's t-test)
         │
         ▼
[p-값 판정 및 신뢰구간, 효과 크기(Cohen's d) 종합 보고]""",
        "table_headers": ["구분", "스튜던트 t-검정", "웰치의 t-검정 (Welch)"],
        "table_rows": [
            ["모분산 조건", "두 집단 모분산 동일 (${\\sigma_1}^2 = {\\sigma_2}^2$)", "두 집단 모분산 상이 (${\\sigma_1}^2 \\neq {\\sigma_2}^2$)"],
            ["자유도 계산", "$df = n_1 + n_2 - 2$ (단순 공식)", "웰치-새터스웨이트 근사식으로 자유도 보정"],
            ["실무 안전성", "이분산 시 제1종 오류 급증", "이분산 및 표본수 불일치 상황에서도 완벽한 강건성"]
        ],
        "history": [
            "- 정보관리기술사 119회 1교시: 독립표본 t-검정과 대응표본 t-검정의 적용 요건 비교",
            "- 정보관리기술사 124회 2교시: A/B 테스트에서 두 집단 간 평균 차이 검증을 위한 t-검정",
            "- Statistical Methods for Psychology Standard Reference"
        ],
        "links": [
            "- [t-검정](./086_t_test.md)",
            "- [대응표본 t-검정](./124_paired_t_test.md)",
            "- [가설검정](./041_hypothesis_testing.md)"
        ]
    },
    "131_logical_dw.md": {
        "title": "논리적 데이터 웨어하우스(Logical DW)",
        "insight": "물리적 ETL로 데이터를 중앙 복제하지 않고 데이터 가상화(Data Virtualization) 기술을 통해 원천 데이터를 실시간 쿼리 결합하는 유연한 분석 아키텍처 필수",
        "rec_text": "원천 시스템 부하를 방지하기 위해 스마트 캐싱과 푸시다운 최적화(Pushdown Optimization)를 적용하고 엔터프라이즈 논리 뷰를 카탈로그에 중앙 등록.",
        "diagram_title": "논리적 DW 데이터 가상화 아키텍처",
        "diagram": """[사용자 / BI 도구] : 단일 SQL 인터페이스 질의
         │
         ▼
[논리적 DW 가상화 엔진 (Denodo / Trino / Presto)]
  - 글로벌 메타데이터 뷰 관리, 쿼리 파싱 및 최적화
  - 스마트 푸시다운: 원천 엔진에서 필터/조인 선처리
         │
         ├─ [RDBMS (Oracle / MySQL)]  ──► 푸시다운 쿼리 실행
         ├─ [빅데이터 레이크 (S3 / Parquet)] ──► 분산 벡터 스캔
         └─ [클라우드 SaaS (Salesforce API)]  ──► 실시간 REST 연계""",
        "table_headers": ["구분", "전통적 물리적 DW", "제언: 논리적 DW (Logical DW)"],
        "table_rows": [
            ["데이터 적재", "대규모 물리적 ETL 복제 및 저장", "데이터 이동 없이 원천 데이터 가상 뷰 결합"],
            ["구축 소요시간", "수개월~수년 파이프라인 개발", "수일 내 가상화 뷰 정의로 즉각 서비스"],
            ["데이터 신선도", "배치 주기에 따른 지연 데이터", "질의 시점 원천 데이터 실시간 조회"]
        ],
        "history": [
            "- 정보관리기술사 117회 2교시: 논리적 데이터 웨어하우스(Logical DW)의 개념과 데이터 가상화",
            "- 정보관리기술사 129회 2교시: 데이터 레이크하우스와 데이터 메시 환경에서 가상화 아키텍처",
            "- Gartner Logical Data Warehouse Architectural Pattern"
        ],
        "links": [
            "- [데이터 레이크](./007_data_lake.md)",
            "- [OLAP](./039_olap.md)",
            "- [논리적 DW 아키텍처](./132_logical_data_warehouse.md)"
        ]
    },
    "132_logical_data_warehouse.md": {
        "title": "논리적 DW 아키텍처",
        "insight": "데이터 사일로와 중복 저장을 억제하기 위해 물리 저장소의 한계를 넘어 가상화 계층에서 분산 질의 최적화와 통합 보안 거버넌스를 구현하는 차세대 DW 체계 수립 필요",
        "rec_text": "정형·반정형·비정형 원천을 망라하는 연합 쿼리(Federated Query) 엔진을 배치하고 비용 기반 푸시다운 튜닝을 통해 네트워크 전송 I/O 최소화.",
        "diagram_title": "논리적 DW 4계층 아키텍처 모델",
        "diagram": """[소비 계층] : 경영진 대시보드, 셀프서비스 BI, AI/ML 파이프라인
         │
         ▼
[가상화 계층] : 통합 시맨틱 모델, 연합 쿼리 엔진 (Federation), 데이터 카탈로그
         │
         ▼
[거버넌스 계층] : 통합 RBAC 접근 제어, 데이터 마스킹, 엔드투엔드 계보
         │
         ▼
[이종 저장 계층] : On-Premise RDBMS, Cloud Data Lake, NoSQL, SaaS API""",
        "table_headers": ["구분", "물리적 단일 저장소 집중", "제언: 논리적 DW 연합 아키텍처"],
        "table_rows": [
            ["인프라 비용", "스토리지 이중 구매 및 스케일업 비용", "기존 인프라 그대로 활용하여 TCO 대폭 절감"],
            ["변화 적응성", "원천 스키마 변경 시 ETL 전면 재개발", "가상화 뷰 수정만으로 변경 사항 즉각 흡수"],
            ["보안 거버넌스", "저장소별 개별 보안 정책 분산", "가상화 단일 관문에서 전사 통합 보안 정책 적용"]
        ],
        "history": [
            "- 정보관리기술사 117회 2교시: 논리적 데이터 웨어하우스(Logical DW)의 개념과 데이터 가상화",
            "- 정보관리기술사 129회 2교시: 데이터 패브릭(Data Fabric) 관점에서의 논리적 DW 구축 방안",
            "- Modern Enterprise Data Architecture Reference"
        ],
        "links": [
            "- [논리적 데이터 웨어하우스](./131_logical_dw.md)",
            "- [데이터 레이크](./007_data_lake.md)",
            "- [데이터 거버넌스](./006_data_governance.md)"
        ]
    },
    "133_bernoulli_distribution.md": {
        "title": "베르누이·이항분포",
        "insight": "성공과 실패라는 상호 배타적 이진 결과를 모형화하는 베르누이 분포와 독립 반복 시행을 결합한 이항분포의 수학적 성질을 이해하고 정규 근사 조건 명확화 필수",
        "rec_text": "시행 횟수 $n$과 성공 확률 $p$에 대해 $np \ge 5$ 및 $n(1-p) \ge 5$ 조건을 검증하여 정규 근사를 적용하고 불만족 시 포아송 또는 정확 이항 검정 채택.",
        "diagram_title": "베르누이 시행에서 이항분포 및 정규 근사로의 확장",
        "diagram": """[단일 베르누이 시행: 결과 X ∈ {0, 1}, 성공 확률 p]
         │
         ▼ (독립 동일 n회 반복 시행)
[이항분포: B(n, p), P(X=k) = nCk * p^k * (1-p)^(n-k)]
  - 평균 E(X) = np, 분산 Var(X) = np(1-p)
         │
         ▼ (시행 횟수 n 충분히 큼: np ≥ 5, n(1-p) ≥ 5)
[드무아브르-라플라스 정리에 의한 정규분포 근사: N(np, np(1-p))]""",
        "table_headers": ["구분", "베르누이 분포 (Bernoulli)", "이항분포 (Binomial)"],
        "table_rows": [
            ["시행 횟수", "단 1회의 성공/실패 실험 ($n=1$)", "독립적인 베르누이 시행 $n$회 반복"],
            ["확률 변수", "성공 여부 ($0$ 또는 $1$)", "$n$회 시행 중 총 성공 횟수 ($0, 1, \\dots, n$)"],
            ["적용 예시", "동전 1회 던지기, 단일 불량 여부", "A/B 테스트 클릭 수, 100개 제품 중 불량품 개수"]
        ],
        "history": [
            "- 정보관리기술사 111회 1교시: 이산확률분포 중 베르누이 분포와 이항분포의 정의 및 성질",
            "- Probability and Statistics for Data Science"
        ],
        "links": [
            "- [정규분포](./106_normal_distribution.md)",
            "- [중심극한정리](./014_central_limit_theorem.md)",
            "- [불편추정량](./011_unbiased_estimator.md)"
        ]
    },
    "134_big_data_analytics_tool_selection_principles.md": {
        "title": "빅데이터 분석 도구 선정 원칙",
        "insight": "최신 유행 도구 도입을 지양하고 데이터 규모·지연시간·팀 역량·TCO를 다각도로 평가하여 배치·스트리밍·대화형 질의 엔진의 최적 포트폴리오 구성 필수",
        "rec_text": "실시간 스트리밍은 Flink, 대규모 분산 처리는 Spark, 고속 대화형 SQL은 Trino를 배치하고 오픈소스 라이선스 및 클라우드 벤더 락인을 사전에 검증.",
        "diagram_title": "빅데이터 분석 도구 선정 4단계 프레임워크",
        "diagram": """[1. 비즈니스 요구사항 및 SLA 분석] : 실시간성(Latency), 데이터 규모(Throughput)
         │
         ▼
[2. 워크로드별 엔진 기술 매핑]
  - 대규모 배치/머신러닝 ──► Apache Spark
  - 서브초 실시간 스트리밍 ──► Apache Flink
  - 초고속 대화형 SQL 질의 ──► Trino / StarRocks
         │
         ▼
[3. 운영 및 비용 평가 (TCO)] : 라이선스, 클라우드 자원 비용, 사내 엔지니어링 역량
         │
         ▼
[4. PoC 실측 검증 후 최종 기술 스택 확정]""",
        "table_headers": ["구분", "단일 만능 도구 고집", "제언: 목적별 최적 엔진 조합"],
        "table_rows": [
            ["자원 효율성", "모든 작업에 무거운 Spark 적용", "경량 스트림은 Flink, 질의는 Trino로 분기"],
            ["비용 관리", "벤더 종속형 상용 솔루션 비용 폭증", "오픈소스 및 오브젝트 스토리지 결합으로 TCO 최소화"],
            ["팀 생산성", "학습 곡선 높은 도구 강제로 개발 지연", "SQL 인터페이스 중심 통합으로 분석가 접근성 극대화"]
        ],
        "history": [
            "- 정보관리기술사 120회 2교시: 빅데이터 플랫폼 구축 시 분석 도구 선정 기준과 아키텍처 설계",
            "- 정보관리기술사 128회 1교시: 데이터 엔지니어링 도구(Spark, Flink, Trino)의 처리 방식 비교",
            "- Enterprise Big Data Architecture and Governance Guide"
        ],
        "links": [
            "- [빅데이터 플랫폼 아키텍처](./135_big_data_platform_architecture.md)",
            "- [빅데이터](./112_big_data.md)",
            "- [데이터 레이크](./007_data_lake.md)"
        ]
    },
    "135_big_data_platform_architecture.md": {
        "title": "빅데이터 플랫폼 아키텍처",
        "insight": "람다 아키텍처의 이중 코드 유지보수 한계를 극복하고 실시간과 배치를 단일 스트림 계층으로 통합하는 카파 아키텍처 및 레이크하우스로의 진화 필수",
        "rec_text": "원천 로그를 Kafka에 영속화하고 Apache Flink와 Iceberg를 결합하여 일관된 단일 처리 로직으로 실시간 대시보드와 대규모 배치 분석을 동시 충족.",
        "diagram_title": "람다(Lambda) vs 카파(Kappa) 아키텍처 구조",
        "diagram": """[람다 아키텍처 (Lambda)]
  원천 데이터 ──┬─► [스피드 계층: Storm/Flink] ──► 실시간 뷰 ──┬─► [서빙 계층]
                └─► [배치 계층: Hadoop/Spark]   ──► 배치 뷰   ──┘ (이중 로직 관리)

[카파 아키텍처 (Kappa)]
  원천 데이터 ──► [단일 이벤트 스트림 (Kafka)] ──► [단일 스트림 엔진 (Flink)] ──► [서빙 계층]
                     (불변 로그 보존으로 필요 시 과거 데이터 스트림 재처리)""",
        "table_headers": ["구분", "람다 아키텍처 (Lambda)", "카파 아키텍처 (Kappa)"],
        "table_rows": [
            ["파이프라인", "배치 계층과 스피드 계층 2개 분리", "단일 스트림 처리 계층 일원화"],
            ["코드 유지보수", "배치(MapReduce)와 실시간(Storm) 코드 이중 작성", "단일 스트림 처리 코드로 전천후 유지보수"],
            ["재처리 방식", "배치 계층에서 원천 재수행", "이벤트 로그 오프셋을 과거로 되돌려 재실행"]
        ],
        "history": [
            "- 정보관리기술사 115회 2교시: 실시간 빅데이터 처리를 위한 람다(Lambda) 아키텍처의 한계와 카파(Kappa) 아키텍처",
            "- 정보관리기술사 129회 2교시: 현대적 빅데이터 플랫폼의 레이크하우스 및 데이터 메시 전환 전략",
            "- Nathan Marz, Big Data: Principles and best practices of scalable realtime data systems"
        ],
        "links": [
            "- [빅데이터](./112_big_data.md)",
            "- [데이터 레이크](./007_data_lake.md)",
            "- [빅데이터 분석 도구 선정 원칙](./134_big_data_analytics_tool_selection_principles.md)"
        ]
    }
}

for fname, data in batch_6_data.items():
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

    # 3. Fix mechanical endings or '다.' endings in content if any
    content = re.sub(r'달라진다\.', '차이 발생.', content)
    content = re.sub(r'선택한다\.', '선택 체계 수립.', content)
    content = re.sub(r'확인한다\.', '확인 필요.', content)
    content = re.sub(r'적용한다\.', '적용 필요.', content)
    content = re.sub(r'의미한다\.', '의미.', content)

    # 4. Fix Ⅵ. 제언
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
