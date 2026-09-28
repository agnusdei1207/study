import os
import re

batch_3_data = {
    "041_hypothesis_testing.md": {
        "title": "가설검정",
        "insight": "제1종 오류와 제2종 오류의 트레이드오프를 인식하고 p-값 맹신에서 벗어나 사전 검정력 분석과 효과 크기를 병행 보고하는 통계적 의사결정 체계 구축 필요",
        "rec_text": "비즈니스 손실 함수에 기반하여 유의수준(α)과 검정력(1-β)을 사전에 확정하고 표본 크기 산정부터 신뢰구간 해석까지 포괄하는 가설검정 거버넌스 수립.",
        "diagram_title": "가설검정 5단계 실행 프로세스",
        "diagram": """[1. 가설 수립: 귀무가설 H0 vs 대립가설 H1]
         │
         ▼
[2. 오류 통제: 유의수준 α 및 검정력 1-β 설정]
         │
         ▼
[3. 검정 통계량 산출 (Z, t, F, χ²)]
         │
         ▼
[4. 기각역 판정 및 p-값 비교] ──► [H0 기각 / 기각 실패 결정]
         │
         ▼
[5. 실무적 유의성 평가: 효과 크기(Effect Size) 및 신뢰구간 보고]""",
        "table_headers": ["구분", "p-값 중심 판정", "제언: 검정력·효과크기 결합 검정"],
        "table_rows": [
            ["표본수 왜곡", "표본 극대화 시 미세 차이도 p<0.05 기각", "효과 크기 병행 평가로 실질적 영향력 분별"],
            ["오류 통제", "제1종 오류(α)만 편향 통제", "사전 검정력 분석으로 제2종 오류(β) 동시 억제"],
            ["의사결정", "단순 기각 여부 이분법 판정", "추정치 신뢰구간 제시로 모수 불확실성 시각화"]
        ],
        "history": [
            "- 정보관리기술사 119회 1교시: 가설검정에서 제1종 오류(α)와 제2종 오류(β)의 관계",
            "- 정보관리기술사 127회 2교시: 데이터 기반 의사결정을 위한 가설검정 프로세스와 효과 크기",
            "- Applied Statistics and Probability for Engineers"
        ],
        "links": [
            "- [z-검정](./012_z_test.md)",
            "- [중심극한정리](./014_central_limit_theorem.md)",
            "- [편향](./038_bias.md)"
        ]
    },
    "042_data_modeling.md": {
        "title": "데이터 모델링",
        "insight": "애플리케이션 화면에 종속되지 않고 비즈니스 도메인의 본질적 규칙과 데이터 무결성을 개념·논리·물리 계층으로 형상화하는 체계적 데이터 모델링 필수",
        "rec_text": "도메인 주도 설계(DDD)의 핵심 엔터티를 기반으로 개념 모델을 수립하고, 논리 3NF 정규화 완성 후 실제 워크로드 측정을 통해 물리 최적화를 단행하는 단계적 방법론 준수.",
        "diagram_title": "데이터 모델링 3단계 생애주기 프로세스",
        "diagram": """[업무 요구사항 분석]
         │
         ▼
[개념 데이터 모델링] : 핵심 엔터티 도출, 관계 정의, 전사 주제영역 확립
         │
         ▼
[논리 데이터 모델링] : 식별자 확정, 정규화(1NF~3NF), M:N 해소, 참조무결성
         │
         ▼
[물리 데이터 모델링] : DBMS 선정, 반정규화, 인덱스/파티셔닝, 스토리지 용량 산정
         │
         ▼
[DDL 생성 및 형상 관리] ──► 지속적 스키마 변경 통제 및 품질 모니터링""",
        "table_headers": ["구분", "화면 종속적 모델링", "제언: 도메인 중심 3단계 모델링"],
        "table_rows": [
            ["데이터 중복", "화면별 개별 테이블 생성으로 중복 폭증", "전사 관점 통합 엔터티 모델링으로 중복 제거"],
            ["변경 유연성", "UI 변경 시 DB 구조 전면 개편 필요", "논리-물리 분리로 비즈니스 로직 독립성 확보"],
            ["데이터 품질", "업무 규칙 누락으로 무결성 훼손", "엔터티/참조 무결성 선언적 강제로 고품질 달성"]
        ],
        "history": [
            "- 정보관리기술사 99회 1교시: 데이터 모델링의 3단계(개념, 논리, 물리)와 주요 산출물",
            "- 정보관리기술사 125회 2교시: 마이크로서비스 아키텍처(MSA) 환경에서의 분산 데이터 모델링 전략",
            "- Data Model Resource Book Standard Reference"
        ],
        "links": [
            "- [개체-관계 다이어그램(ERD)](./028_erd.md)",
            "- [정규화](./019_normalization.md)",
            "- [반정규화](./017_denormalization.md)"
        ]
    },
    "043_data_mining.md": {
        "title": "데이터 마이닝",
        "insight": "단순 모델 학습에 매몰되지 않고 CRISP-DM 프로세스에 입각하여 비즈니스 이해부터 배포·가치 실현까지 포괄하는 엔드투엔드 지식 발견 체계 확립 필요",
        "rec_text": "분류, 예측, 군집, 연관규칙 등 비즈니스 문제 유형에 적합한 기법을 매핑하고 MLOps 파이프라인과 결합하여 모델 성능 저하(Drift)를 지속 모니터링.",
        "diagram_title": "CRISP-DM 기반 데이터 마이닝 반복 사이클",
        "diagram": """[비즈니스 이해] ◄──► [데이터 이해: EDA / 프로파일링]
         │                               │
         ▼                               ▼
   [데이터 준비: 정제, 변환, 특성 공학 (Feature Engineering)]
         │                               ▲
         ▼                               │ (반복 개선)
   [모델링: 분류, 군집, 연관규칙] ────────┘
         │
         ▼
   [평가: 성능 평가 및 비즈니스 효익 검증] ──► [배포 및 MLOps 운영]""",
        "table_headers": ["구분", "단순 알고리즘 중심", "제언: 비즈니스 중심 CRISP-DM"],
        "table_rows": [
            ["목표 설정", "정확도 지표(Accuracy) 단독 추종", "비즈니스 ROI 및 비용 절감 목표 연계"],
            ["전처리 비중", "모델 튜닝에 과도한 시간 집중", "데이터 정제/특성공학에 80% 자원 투입"],
            ["사후 운영", "모델 배포 후 모니터링 부재", "데이터/개념 드리프트 감지 및 지속적 재학습"]
        ],
        "history": [
            "- 정보관리기술사 101회 1교시: 데이터 마이닝의 추진 절차(CRISP-DM 6단계)",
            "- 정보관리기술사 120회 2교시: 빅데이터 분석을 위한 기계학습 기반 데이터 마이닝 기법 비교",
            "- Data Mining: Practical Machine Learning Tools and Techniques"
        ],
        "links": [
            "- [군집분석](./005_cluster_analysis.md)",
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [이상치](./010_outlier.md)"
        ]
    },
    "044_vector_database.md": {
        "title": "벡터 데이터베이스",
        "insight": "LLM의 환각 완화와 대규모 고차원 임베딩 검색을 위해 HNSW 등 근사 최근접 이웃(ANN) 인덱스와 메타데이터 하이브리드 검색 아키텍처 구축 필수",
        "rec_text": "임베딩 차원 수와 QPS 요건에 따라 Milvus, Pinecone, pgvector 등 적합 엔진을 선정하고 역색인(BM25)과 벡터 유사도(Dense)를 결합한 하이브리드 RAG 구현.",
        "diagram_title": "벡터 데이터베이스 RAG 하이브리드 검색 아키텍처",
        "diagram": """[문서/비정형 데이터] ──► [청킹(Chunking) 및 임베딩 모델(Embedding)]
                                       │
                                       ▼
[벡터 데이터베이스 적재 (HNSW / IVF-PQ 인덱싱)]
                                       │
[사용자 질의] ──► [질의 임베딩] ──────► [ANN 벡터 유사도 검색 (코사인/L2)]
                                       │
[키워드 질의] ────────────────────────► [BM25 역색인 검색]
                                       │
                                       ▼ (상호 순위 결합: RRF)
                          [최적 검색 결과 도출 → LLM 프롬프트 주입]""",
        "table_headers": ["구분", "전통적 관계형 DB", "제언: 벡터 데이터베이스 (ANN)"],
        "table_rows": [
            ["검색 방식", "정확한 키워드/범위 일치 검색", "고차원 벡터 공간의 의미적 유사도 검색"],
            ["인덱싱 구조", "B-Tree, Hash Index", "HNSW, IVF-PQ, ScaNN (Graph/Quantization)"],
            ["주요 활용", "OLTP 트랜잭션, 정형 데이터", "생성형 AI RAG, 이미지 검색, 추천 시스템"]
        ],
        "history": [
            "- 정보관리기술사 132회 1교시: 생성형 AI 환경에서 벡터 데이터베이스의 개념과 주요 기능",
            "- 정보관리기술사 135회 2교시: 대규모 RAG(Retrieval-Augmented Generation) 시스템 아키텍처",
            "- Milvus & Pinecone Architecture Technical Guides"
        ],
        "links": [
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [인덱스](./047_index.md)",
            "- [NoSQL](./001_nosql.md)"
        ]
    },
    "045_sharding.md": {
        "title": "샤딩",
        "insight": "데이터 폭증에 대응하는 수평 확장을 위해 샤드 키 핫스팟과 재분배 비용을 최소화하는 일관된 해싱(Consistent Hashing) 기반 아키텍처 확립 필수",
        "rec_text": "조회 조건에 샤드 키가 포함되도록 쿼리 패턴을 설계하여 브로드캐스트 스캔을 방지하고 가상 노드 기법을 통한 노드 증설 시 무중단 데이터 리밸런싱 달성.",
        "diagram_title": "일관된 해싱(Consistent Hashing) 기반 샤딩 구조",
        "diagram": """                   [샤드 해시 링 (0 ~ 2^32-1)]
                       Shard A (Virtual Node A1, A2)
                      /                             \\
                     /                               \\
    Shard C (Virtual C1, C2)                     Shard B (Virtual B1, B2)
                     \\                               /
                      \\                             /
                       [Key k 해시값 매핑 → 시계방향 노드 할당]""",
        "table_headers": ["구분", "모듈로(Modulo) 샤딩", "제언: 일관된 해싱 샤딩"],
        "table_rows": [
            ["노드 증설", "전체 데이터 전면 재배치 발생", "인접 노드의 국소 데이터만 이전 (최소 이동)"],
            ["부하 분산", "노드 용량 차이 반영 불가", "가상 노드(Virtual Node) 수 조절로 불균형 해소"],
            ["가용성", "리밸런싱 중 서비스 중단 위험", "점진적 데이터 마이그레이션 및 무중단 운영"]
        ],
        "history": [
            "- 정보관리기술사 116회 2교시: 대용량 데이터베이스의 샤딩(Sharding) 기법과 샤드 키 선정 기준",
            "- 정보관리기술사 126회 1교시: 일관된 해싱(Consistent Hashing)의 원리와 분산 캐시 적용",
            "- Designing Data-Intensive Applications Standard Reference"
        ],
        "links": [
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)",
            "- [분산 데이터베이스 투명성](./025_distributed_db_transparency.md)",
            "- [NoSQL](./001_nosql.md)"
        ]
    },
    "047_index.md": {
        "title": "인덱스",
        "insight": "조회 성능 향상과 DML 오버헤드 간의 트레이드오프를 정밀 계산하여 카디널리티가 높은 컬럼 중심의 복합 인덱스 설계 및 주기적 인덱스 재구성 필수",
        "rec_text": "인덱스 컬럼 가공을 금지하고 최좌측 접두사(Leftmost Prefix) 원칙을 준수하며 실행계획 분석을 통해 미사용 잉여 인덱스를 정기 정리하는 거버넌스 확립.",
        "diagram_title": "인덱스 설계 및 실행계획 검증 프로세스",
        "diagram": """[슬로우 쿼리 수집] ──► [실행계획(EXPLAIN) 분석: Full Table Scan 감지]
                                │
                                ▼
[선택도(Selectivity) 평가] : 카디널리티 높은 선행 컬럼 식별
                                │
                                ▼
[복합 인덱스 설계] : [동등 조건(=)] ──► [범위 조건(>, <, Between)]
                                │
                                ▼
[커버링 인덱스(Covering Index) 검토] ──► 테이블 랜덤 액세스 원천 배제""",
        "table_headers": ["구분", "무분별한 단일 인덱스 다발", "제언: 복합 커버링 인덱스 최적화"],
        "table_rows": [
            ["DML 성능", "Insert/Update 시 인덱스 갱신 오버헤드 극대", "필수 복합 인덱스 압축으로 쓰기 비용 최소화"],
            ["조회 성능", "테이블 랜덤 I/O 다발", "커버링 인덱스를 통한 테이블 미참조 고속 반환"],
            ["유지보수", "중복/미사용 인덱스 방치", "DBMS 통계 기반 미사용 인덱스 정기 삭제"]
        ],
        "history": [
            "- 정보관리기술사 103회 1교시: B-Tree 인덱스의 구조와 검색 메커니즘",
            "- 정보관리기술사 121회 2교시: 인덱스 스캔 방식(Index Range Scan, Full Scan, Skip Scan) 비교",
            "- SQL Antipatterns & High Performance MySQL"
        ],
        "links": [
            "- [이진 탐색 트리](./027_binary_search_tree.md)",
            "- [B-Tree](./111_b_tree.md)",
            "- [데이터베이스 튜닝](./088_database_tuning.md)"
        ]
    },
    "049_phantom_conflict.md": {
        "title": "팬텀 충돌",
        "insight": "기존 레코드 잠금만으로 방어할 수 없는 신규 튜플 삽입(Phantom)을 차단하기 위해 넥스트 키 락(Next-Key Lock)과 MVCC 스냅샷 격리 결합 필수",
        "rec_text": "범위 검색 트랜잭션 충돌 시 Serializable 대신 Gap Lock 기반의 Repeatable Read를 채택하여 동시성 처리량을 유지하면서 팬텀 읽기를 완벽 차단.",
        "diagram_title": "레코드 락 vs 갭 락 vs 넥스트 키 락 구조",
        "diagram": """        인덱스 레코드 10                인덱스 레코드 20
        ┌──────────────┐                ┌──────────────┐
... ───►│ Record Lock  │───► Gap Lock ──►│ Record Lock  │───► ...
        └──────────────┘ (신규삽입차단) └──────────────┘
        [                       Next-Key Lock          ]""",
        "table_headers": ["구분", "전통적 레코드 잠금", "제언: Next-Key Lock (Record+Gap)"],
        "table_rows": [
            ["팬텀 방어", "존재하지 않는 튜플 삽입 차단 불가", "인덱스 간격(Gap) 선제 잠금으로 팬텀 원천 차단"],
            ["동시성 수준", "Serializable 강제로 처리량 급감", "Repeatable Read 레벨에서 안전한 동시 처리"],
            ["데드락 제어", "잠금 순환 대기 가능성", "인덱스 순서화 잠금 및 즉각 타임아웃 통제"]
        ],
        "history": [
            "- 정보관리기술사 115회 1교시: 트랜잭션 동시성 이상 현상(Dirty Read, Non-repeatable, Phantom)",
            "- 정보관리기술사 127회 2교시: MySQL InnoDB의 Gap Lock과 Next-Key Lock 메커니즘",
            "- Database Systems: The Complete Book"
        ],
        "links": [
            "- [트랜잭션 격리 수준](./020_isolation_level.md)",
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [무결성 제약](./013_integrity_constraint.md)"
        ]
    },
    "050_extendible_hashing.md": {
        "title": "확장성 해싱",
        "insight": "데이터 증가 시 전체 재해싱(Rehashing) 오버헤드를 배제하기 위해 디렉터리 기반의 전역/지역 깊이(Depth) 제어로 점진적 버킷 분할 아키텍처 수립 필수",
        "rec_text": "대규모 키-값 저장소 설계 시 디렉터리 크기 폭증(디렉터리 폭발)을 방지하도록 초기 깊이를 적정 설계하고 오버플로우 체이닝과의 하이브리드 결합 고려.",
        "diagram_title": "확장성 해싱 디렉터리 및 버킷 분할 구조",
        "diagram": """[전역 깊이 Global Depth = 2]
디렉터리 00 ──► [버킷 A (지역 깊이 Local Depth = 2)] : 4, 8, 12
디렉터리 01 ──► [버킷 B (지역 깊이 Local Depth = 1)] : 1, 5, 9, 13
디렉터리 10 ──► [버킷 C (지역 깊이 Local Depth = 2)] : 2, 6, 10
디렉터리 11 ──┘ (버킷 B 공유)
       │
       ▼ (버킷 B 오버플로우 발생 시 Local Depth=2로 분할 및 포인터 재배치)""",
        "table_headers": ["구분", "전통적 정적 해싱", "제언: 확장성 해싱 (Extendible)"],
        "table_rows": [
            ["버킷 오버플로우", "긴 오버플로우 체인으로 O(N) 퇴보", "해당 버킷만 1:2 분할하여 점진적 수용"],
            ["재해싱 오버헤드", "테이블 전체 레코드 재배치 발생", "디렉터리 포인터만 갱신하여 무중단 확장"],
            ["메모리 효율", "초기 고정 크기 낭비 발생", "데이터 규모에 맞춰 선형적으로 저장소 증가"]
        ],
        "history": [
            "- 정보관리기술사 105회 1교시: 동적 해싱(Dynamic Hashing) 중 확장성 해싱의 원리와 깊이(Depth) 개념",
            "- Ronald Fagin, Extendible Hashing: A Fast Access Method for Dynamic Files",
            "- Fundamentals of Database Systems"
        ],
        "links": [
            "- [인덱스](./047_index.md)",
            "- [NoSQL](./001_nosql.md)",
            "- [이진 탐색 트리](./027_binary_search_tree.md)"
        ]
    },
    "051_ha_architecture.md": {
        "title": "고가용성 아키텍처(HA)",
        "insight": "단일 장애점(SPOF)을 제거하고 RTO/RPO 목표를 충족하기 위해 쿼럼 기반 자동 페일오버와 반동기 복제(Semi-Sync) 결합 고신뢰성 DB 아키텍처 구축 필수",
        "rec_text": "Active-Standby 구성 시 스플릿 브레인(Split-Brain) 방지를 위한 홀수 노드 쿼럼 합의(Raft/Paxos)를 도입하고 무중단 카나리 배포 파이프라인 연계.",
        "diagram_title": "고가용성 데이터베이스 클러스터 아키텍처",
        "diagram": """[클라이언트 트래픽] ──► [L4/L7 로드밸런서 (VIP / ProxySQL)]
                                       │
         ┌─────────────────────────────┴─────────────────────────────┐
         ▼                                                           ▼
[Primary 노드 (Active)] ──► [반동기 복제 (Semi-Sync)] ──► [Secondary 노드 (Standby)]
         │                                                           │
         └──────────────► [쿼럼 감시자 (Quorum Witness)] ───────────┘
                           (헬스체크 및 10초 이내 자동 페일오버)""",
        "table_headers": ["구분", "전통적 Active-Standby", "제언: 쿼럼 기반 고가용성 클러스터"],
        "table_rows": [
            ["페일오버 방식", "관리자 수동 절체 (수십 분 소요)", "헬스체크 기반 3초 이내 자동 무중단 절체"],
            ["스플릿 브레인", "네트워크 단절 시 양쪽 쓰기 충돌", "3노드 쿼럼(과반수) 합의로 스플릿 브레인 원천 차단"],
            ["데이터 손실", "비동기 복제로 RPO 불만족", "반동기 복제(Semi-Sync)로 RPO=0 달성"]
        ],
        "history": [
            "- 정보관리기술사 113회 2교시: 무중단 시스템 구축을 위한 데이터베이스 고가용성(HA) 구성 방식 비교",
            "- 정보관리기술사 127회 1교시: 재해복구(DR) 수준(Mirror, Hot, Warm, Cold)과 RTO, RPO",
            "- Enterprise High Availability Architecture Guide"
        ],
        "links": [
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)",
            "- [분산 데이터베이스 투명성](./025_distributed_db_transparency.md)",
            "- [동시성 제어](./009_concurrency_control.md)"
        ]
    },
    "052_multidimensional_index_structure.md": {
        "title": "다차원 인덱스 구조",
        "insight": "공간 및 다차원 데이터의 검색 가속화를 위해 MBR의 면적 확장과 겹침(Overlap)을 최소화하는 R*-Tree 및 공간 분할 결합 인덱싱 최적화 필수",
        "rec_text": "영역 질의와 K-최근접 이웃(KNN) 질의 빈도에 맞춰 MBR 분할 알고리즘(Linear vs Quadratic)을 선정하고 고차원 희소 데이터는 차원 축소와 병행.",
        "diagram_title": "R-Tree 공간 분할 MBR 계층 및 2차원 트리 구조",
        "diagram": """[공간 평면 MBR 분할]                      [2차원 R-Tree 인덱스 계층 구조]
┌─────────────────────────┐                        [ 루트 MBR (R0) ]
│ R1                      │                        /               \\
│  ┌─────┐       ┌─────┐  │                [ MBR R1 ]             [ MBR R2 ]
│  │ R3  │       │ R4  │  │                 /      \\               /      \\
│  │ (o1)│       │ (o2)│  │             [ R3 ]    [ R4 ]       [ R5 ]    [ R6 ]
│  └─────┘       └─────┘  │              /  \\      /  \\         /  \\      /  \\
├─────────────────────────┤            (o1)(o2)  (o3)(o4)     (o5)(o6)  (o7)(o8)
│ R2  ┌─────┐   ┌─────┐   │
│     │ R5  │   │ R6  │   │
│     └─────┘   └─────┘   │
└─────────────────────────┘""",
        "table_headers": ["구분", "전통적 B-Tree (1차원)", "제언: R-Tree (다차원 공간)"],
        "table_rows": [
            ["색인 대상", "단일 스칼라 값 (숫자, 문자열)", "2차원 이상 공간 객체 (Point, Line, Polygon)"],
            ["경계 표현", "단일 키 대소 범위 [A, B]", "최소 경계 사각형 (MBR: Minimum Bounding Box)"],
            ["질의 유형", "동등 검색, 단일 범위 검색", "영역 포함 질의(Range), K-최근접 이웃 질의(KNN)"]
        ],
        "history": [
            "- 정보관리기술사 106회 1교시: 공간 데이터베이스에서 R-Tree와 K-D Tree의 비교",
            "- 정보관리기술사 125회 2교시: 위치기반 서비스(LBS)를 위한 다차원 공간 인덱싱 기법과 질의 처리",
            "- Antonin Guttman, R-Trees: A Dynamic Index Structure for Spatial Searching"
        ],
        "links": [
            "- [인덱스](./047_index.md)",
            "- [이진 탐색 트리](./027_binary_search_tree.md)",
            "- [B-Tree](./111_b_tree.md)"
        ]
    },
    "054_data_observability.md": {
        "title": "데이터 옵저버빌리티",
        "insight": "데이터 다운타임을 근절하기 위해 신선도·분포·볼륨·스키마·계보의 5대 핵심 기둥을 실시간 모니터링하고 원인 규명을 자동화하는 파이프라인 구축 필수",
        "rec_text": "원천 수집부터 최종 BI 대시보드까지 전 구간 데이터 계보(Lineage)를 자동 추적하고 통계적 이상 탐지 알고리즘을 결합한 데이터 SLA 관리 체계 확립.",
        "diagram_title": "데이터 옵저버빌리티 5대 핵심 기둥 모니터링",
        "diagram": """[원천 데이터 유입] ──► [ETL/ELT 파이프라인] ──► [DW/레이크 적재] ──► [BI/AI 서빙]
         │                     │                      │                    │
         └─────────────────────┴──────────────────────┴────────────────────┘
                                       │
                                       ▼ (실시간 관측)
             ┌───────────────────────────────────────────────────┐
             │ 1. 신선도 (Freshness) : 데이터 갱신 지연 SLA 감시 │
             │ 2. 분포 (Distribution) : 이상치 및 통계 드리프트 │
             │ 3. 볼륨 (Volume)       : 데이터 유입량 이상 급감  │
             │ 4. 스키마 (Schema)     : 비호환 DDL 변경 즉시 차단│
             │ 5. 계보 (Lineage)      : 장애 원인 및 파급도 추적│
             └───────────────────────────────────────────────────┘""",
        "table_headers": ["구분", "전통적 시스템 모니터링", "제언: 데이터 옵저버빌리티"],
        "table_rows": [
            ["관측 대상", "CPU, 메모리, 네트워크 인프라 상태", "데이터 자체의 내용, 무결성, 통계적 분포"],
            ["이상 감지", "파이프라인 크래시/중단만 탐지", "정상 실행되었으나 빈 테이블 적재 등 조용한 오류 탐지"],
            ["장애 추적", "로그 수동 검색 및 역추적 곤란", "End-to-End 계보 기반 즉각적인 영향 분석"]
        ],
        "history": [
            "- 정보관리기술사 131회 1교시: 데이터 옵저버빌리티(Data Observability)의 5대 기둥과 구축 방안",
            "- Monte Carlo Data Observability Architecture Guide"
        ],
        "links": [
            "- [데이터 품질관리](./003_data_quality_management.md)",
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [데이터 레이크](./007_data_lake.md)"
        ]
    },
    "058_linear_vs_nonlinear_data_structures.md": {
        "title": "선형 vs 비선형 자료구조",
        "insight": "데이터의 접근 패턴과 관계 복잡도에 따라 선형 구조의 순차성과 비선형 구조의 계층·네트워크 탐색 효율을 최적으로 조합하는 하이브리드 설계 필수",
        "rec_text": "순차적 흐름 처리는 큐/스택을 적용하고 다대다 관계 및 계층 탐색은 트리/그래프를 채택하며 메모리 연속성과 캐시 친화성을 고려한 자료구조 선정.",
        "diagram_title": "자료구조 분류 체계 및 변환 관계",
        "diagram": """[컴퓨터 자료구조 분류]
       │
       ├─ [선형 자료구조 (1:1 선형 순서)] ──► 배열, 연결 리스트, 스택, 큐
       │        │
       │        ▼ (인덱싱 및 계층화)
       └─ [비선형 자료구조 (1:N, N:M 계층/망)]
                ├─ 트리 (Tree)   : 1:N 계층 구조 (BST, B-Tree, Heap)
                └─ 그래프 (Graph): N:M 네트워크 관계 (DAG, 인접리스트)""",
        "table_headers": ["구분", "선형 자료구조 (Linear)", "비선형 자료구조 (Non-linear)"],
        "table_rows": [
            ["관계 표현", "데이터 간 1:1 전후 연속 관계", "데이터 간 1:N 계층 또는 N:M 복합 관계"],
            ["순회 방식", "단일 방향 순차 순회", "전위/중위/후위 순회, DFS, BFS 다각 순회"],
            ["탐색 복잡도", "O(N) 선형 탐색", "트리 기반 O(log N) 고속 탐색"]
        ],
        "history": [
            "- 정보관리기술사 100회 1교시: 선형 자료구조와 비선형 자료구조의 비교 및 활용",
            "- Fundamentals of Data Structures in C++"
        ],
        "links": [
            "- [이진 탐색 트리](./027_binary_search_tree.md)",
            "- [B-Tree](./111_b_tree.md)",
            "- [인덱스](./047_index.md)"
        ]
    },
    "060_time_series_ar_ma_model.md": {
        "title": "시계열 AR·MA 모델",
        "insight": "시계열 데이터의 정상성(Stationarity)을 차분과 변환으로 확보한 후 자기상관함수(ACF)와 편자기상관함수(PACF)의 절단 특성 기반 최적 차수 선정 필수",
        "rec_text": "ADF 단위근 검정을 선행하여 비정상 시계열을 ARIMA로 변환하고 잔차의 백색잡음(White Noise) 여부를 Ljung-Box 검정으로 확인하는 검증 체계 확립.",
        "diagram_title": "Box-Jenkins 시계열 모델링 절차",
        "diagram": """[원시 시계열 데이터] ──► [정상성 진단 (ADF 검정)]
                                │
                                ├─ [비정상 시계열] ──► 차분(Difference) / 로그변환
                                │
                                ▼ [정상 시계열 확보]
[ACF / PACF 그래프 분석] ──► [AR(p), MA(q) 차수 식별]
                                │
                                ▼
[모수 추정 (MLE)] ──────► [잔차 진단 (백색잡음 검정)] ──► [최종 예측]""",
        "table_headers": ["구분", "자기회귀 모델 (AR)", "이동평균 모델 (MA)"],
        "table_rows": [
            ["핵심 원리", "과거 자신의 값들의 선형 결합", "과거 예측 오차(Shock)들의 선형 결합"],
            ["ACF 특성", "지수적 감소 또는 사인파 감쇠", "q차 이후 급격히 0으로 절단 (Cut-off)"],
            ["PACF 특성", "p차 이후 급격히 0으로 절단", "지수적 감소 또는 사인파 감쇠"]
        ],
        "history": [
            "- 정보관리기술사 118회 1교시: 시계열 분석에서 정상성(Stationarity)의 조건과 차분의 개념",
            "- 정보관리기술사 129회 2교시: Box-Jenkins 시계열 분석 방법론과 ARIMA(p,d,q) 모델 구축",
            "- Time Series Analysis: Forecasting and Control"
        ],
        "links": [
            "- [시계열 실시간 이상탐지](./061_time_series_realtime_anomaly_detection.md)",
            "- [기술통계](./036_descriptive_statistics.md)",
            "- [가설검정](./041_hypothesis_testing.md)"
        ]
    },
    "061_time_series_realtime_anomaly_detection.md": {
        "title": "시계열 실시간 이상탐지",
        "insight": "지연 시간을 최소화하고 거짓 경보(False Alarm)를 억제하기 위해 이동 동적 임계치와 비지도 학습(오토인코더, Isolation Forest)을 결합한 스트리밍 파이프라인 필수",
        "rec_text": "Kafka와 Flink 기반의 실시간 스트리밍 인프라에 EWMA 및 LSTM 오토인코더를 연동하여 트렌드 변화와 스파이크 이상을 즉각 분별 통제.",
        "diagram_title": "실시간 시계열 이상탐지 스트리밍 아키텍처",
        "diagram": """[센서/서버 실시간 메트릭] ──► [메시지 브로커 (Kafka)]
                                       │
                                       ▼
[스트림 프로세싱 엔진 (Apache Flink / Spark Streaming)]
  - 롤링 윈도우 집계 (Sliding Window)
  - 동적 임계치 계산 (EWMA / Dynamic Threshold)
  - 머신러닝 이상 점수 산출 (LSTM Autoencoder / Isolation Forest)
                                       │
         ┌─────────────────────────────┴─────────────────────────────┐
         ▼                                                           ▼
[이상 점수 > 임계치] : 즉각 알람/장애 격리            [정상 데이터] : 시계열 DB 적재""",
        "table_headers": ["구분", "정적 임계치 방식 (Static)", "제언: 실시간 동적 임계치 및 AI"],
        "table_rows": [
            ["패턴 변화 적응", "주간/야간 트래픽 변화 시 오탐 다발", "계절성 및 추세 반영한 동적 밴드(Band) 생성"],
            ["이상 탐지 유형", "단순 상한/하한 초과만 탐지", "복합 다변량 이상 및 미세 트렌드 붕괴 탐지"],
            ["처리 지연시간", "배치 분석으로 사후 인지", "스트림 엔진 기반 밀리초 단위 즉시 알람"]
        ],
        "history": [
            "- 정보관리기술사 124회 2교시: 대규모 시계열 데이터의 실시간 이상 탐지(Anomaly Detection) 아키텍처",
            "- 정보관리기술사 130회 1교시: AIOps 관점에서의 동적 임계치(Dynamic Threshold) 기반 장애 예측",
            "- Real-Time Anomaly Detection for Streaming Analytics"
        ],
        "links": [
            "- [시계열 AR·MA 모델](./060_time_series_ar_ma_model.md)",
            "- [이상치](./010_outlier.md)",
            "- [데이터 옵저버빌리티](./054_data_observability.md)"
        ]
    },
    "062_ensemble_bagging_boosting.md": {
        "title": "앙상블 배깅·부스팅",
        "insight": "단일 모델의 한계를 극복하기 위해 분산을 줄이는 병렬 배깅(Random Forest)과 편향을 줄이는 순차 부스팅(LightGBM, XGBoost)의 수학적 특성에 따른 차등 적용 필수",
        "rec_text": "노이즈가 많은 데이터는 배깅으로 과적합을 방지하고 고성능 예측이 요구되는 정형 데이터는 조기 종료(Early Stopping)를 결합한 그래디언트 부스팅 적용.",
        "diagram_title": "배깅(Bagging)과 부스팅(Boosting) 학습 메커니즘",
        "diagram": """[배깅 (Bagging): 병렬 분산 축소]
  원천 데이터 ──► 부트스트랩 샘플링 ──► [개별 독립 모델 병렬 학습] ──► 투표/평균 집계
                                           (Random Forest)

[부스팅 (Boosting): 순차 편향 축소]
  원천 데이터 ──► [약한 학습기 1] ──► [오답 가중치 부여] ──► [약한 학습기 2] ──► 최종 결합
                                           (XGBoost / LightGBM)""",
        "table_headers": ["구분", "배깅 (Bagging)", "부스팅 (Boosting)"],
        "table_rows": [
            ["학습 방식", "독립적인 표본 기반 병렬 학습", "이전 모델의 오차를 보완하는 순차적 학습"],
            ["오차 감소", "분산(Variance) 감소 (과적합 완화)", "편향(Bias) 감소 (예측력 극대화)"],
            ["노이즈 영향", "노이즈 및 이상치에 상대적 강건", "이상치에 가중치가 집중되어 과적합 위험 존재"]
        ],
        "history": [
            "- 정보관리기술사 114회 2교시: 머신러닝 앙상블 학습(Ensemble Learning)에서 배깅과 부스팅의 원리 비교",
            "- 정보관리기술사 126회 1교시: 그래디언트 부스팅(GBM) 알고리즘과 XGBoost, LightGBM 특징",
            "- The Elements of Statistical Learning Standard Reference"
        ],
        "links": [
            "- [편향](./038_bias.md)",
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [데이터 마이닝](./043_data_mining.md)"
        ]
    },
    "063_opensource_dbms_migration.md": {
        "title": "오픈소스 DBMS 마이그레이션",
        "insight": "상용 DBMS 종속(Lock-in)을 탈피하고 TCO를 절감하기 위해 SQL/PL 호환성 진단과 데이터 정합성 검증 도구를 연동한 단계적 전환 방법론 수립 필수",
        "rec_text": "오라클 등 상용 DB에서 PostgreSQL/MySQL 전환 시 비호환 오브젝트(프로시저/패키지)의 변환 전략을 사전 수립하고 CDC 무중단 마이그레이션 적용.",
        "diagram_title": "오픈소스 DBMS 마이그레이션 5단계 절차",
        "diagram": """[1. 전환 타깃 선정 및 TCO 평가]
         │
         ▼
[2. 스키마/오브젝트 호환성 진단: 자동 변환 도구(ora2pg) 적용]
         │
         ▼
[3. 비호환 SQL 및 저장 프로시저 리팩토링 (애플리케이션 계층 이전)]
         │
         ▼
[4. CDC 기반 무중단 데이터 복제 및 전수 정합성 검증 (Data Diff)]
         │
         ▼
[5. 모의 절체(Dry-run) 검증 후 본 컷오버 및 안정화 운영]""",
        "table_headers": ["구분", "빅뱅(Big-Bang) 일괄 전환", "제언: CDC 기반 점진적 마이그레이션"],
        "table_rows": [
            ["다운타임", "대규모 다운타임으로 비즈니스 마비", "CDC 실시간 복제로 수 분 이내 최소 컷오버"],
            ["리스크 관리", "전환 실패 시 즉각적 롤백 불가", "역방향 복제(Reverse CDC) 구성으로 즉시 롤백"],
            ["정합성 검증", "표본 검증으로 잠재적 불일치 잔존", "해시 체크섬 기반 데이터 전수 비교 검증"]
        ],
        "history": [
            "- 정보관리기술사 117회 1교시: 상용 DBMS에서 오픈소스 DBMS로의 전환 시 고려사항",
            "- 정보관리기술사 128회 2교시: 오픈소스 DBMS 마이그레이션 절차와 CDC를 활용한 무중단 전환 방안",
            "- AWS Database Migration Service Best Practices"
        ],
        "links": [
            "- [데이터베이스 튜닝](./088_database_tuning.md)",
            "- [고가용성 아키텍처(HA)](./051_ha_architecture.md)",
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)"
        ]
    }
}

for fname, data in batch_3_data.items():
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

    # 3. Special fix for 052 R-Tree 2D ASCII tree in section III
    if fname == "052_multidimensional_index_structure.md":
        content = re.sub(
            r'```text\n공간 질의\(영역·근접 조건\)[\s\S]*?```',
            f'```text\n{data["diagram"]}\n```',
            content
        )

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
