import os
import re

batch_2_data = {
    "021_db_partitioning_sharding.md": {
        "title": "데이터베이스 분할·샤딩",
        "insight": "단순 데이터 증가 대응을 넘어 샤드 키 편중(Hotspot)과 분산 트랜잭션 오버헤드를 사전에 통제하는 해시/범위 복합 파티셔닝 아키텍처 수립 필요",
        "rec_text": "단일 샤드 내 트랜잭션 완결성을 극대화하도록 비즈니스 접근 패턴(Entity Group) 기반의 샤드 키를 설계하고 라우팅 미들웨어를 통한 동적 리밸런싱 체계 확립.",
        "diagram_title": "데이터베이스 파티셔닝 및 샤딩 라우팅 아키텍처",
        "diagram": """[애플리케이션 요청]
         │
         ▼
[샤드 라우팅 계층 (Coordinator / Proxy)]
         │
         ├─ [샤드 키 해시 / 범위 판별]
         │        ├─ Shard A (Range: 1~10000) ──► 로컬 트랜잭션 수행
         │        └─ Shard B (Range: 10001~20000) ──► 로컬 트랜잭션 수행
         │
         └─ [다중 샤드 질의 시] ──► 2단계 분산 집계 및 병렬 스캔 통제""",
        "table_headers": ["구분", "단순 샤딩 (임의 키)", "제언: 비즈니스 친화적 샤딩"],
        "table_rows": [
            ["데이터 편중", "특정 샤드에 쓰기 핫스팟 집중", "해시 분산 및 가상 노드(Consistent Hashing) 적용"],
            ["조인 성능", "글로벌 크로스 샤드 조인 빈발", "자주 함께 조회되는 엔터티를 동일 샤드에 군집화"],
            ["트랜잭션", "2PC로 인한 지연 및 가용성 저하", "단일 샤드 로컬 트랜잭션 중심의 경계 격리"]
        ],
        "history": [
            "- 정보관리기술사 116회 2교시: 대용량 데이터베이스의 샤딩(Sharding) 기법과 샤드 키 선정 기준",
            "- 정보관리기술사 128회 1교시: 수평적 파티셔닝과 수직적 파티셔닝의 비교",
            "- High Performance MySQL Standard Guide"
        ],
        "links": [
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [NoSQL](./001_nosql.md)",
            "- [분산 데이터베이스 투명성](./025_distributed_db_transparency.md)"
        ]
    },
    "025_distributed_db_transparency.md": {
        "title": "분산 데이터베이스 투명성",
        "insight": "위치·분할·복제 등 6대 분산 투명성을 구현하되 네트워크 지연과 분산 2PC 오버헤드를 고려하여 업무별 투명성 보장 수준을 차등화하는 설계 필수",
        "rec_text": "글로벌 트랜잭션 코디네이터와 분산 데이터 카탈로그를 연계하여 애플리케이션의 물리적 데이터 위치 종속성을 배제하고 국소 장애 시 장애 투명성을 보장.",
        "diagram_title": "분산 데이터베이스 6대 투명성 계층 모델",
        "diagram": """[사용자 / 애플리케이션] : 단일 중앙 집중형 DB로 인식 (위치/분할 은닉)
         │
         ▼
[분산 트랜잭션 매니저] : 위치 투명성 + 분할 투명성 + 복제 투명성
         │
         ├─ [트랜잭션 투명성: 분산 2PC / SAGA 패턴]
         ├─ [장애 투명성: 쿼럼 합의 기반 자동 페일오버]
         └─ [병행 투명성: 분산 락 및 타임스탬프 순서화]""",
        "table_headers": ["구분", "완전 투명성 강제", "제언: 실무적 투명성 차등화"],
        "table_rows": [
            ["성능 트레이드오프", "엄격한 동기 복제로 지연 급증", "결제는 강한 일관성, 로그는 최종 일관성 적용"],
            ["장애 격리", "단일 노드 장애 시 전체 트랜잭션 차단", "서킷 브레이커 및 쿼럼 기반 로컬 가용성 확보"],
            ["복잡도 관리", "전사 단일 분산 DBMS 종속", "도메인 단위 마이크로서비스 DB 분할"]
        ],
        "history": [
            "- 정보관리기술사 106회 1교시: 분산 데이터베이스의 6대 투명성(위치, 분할, 복제, 병행, 장애, 중복)",
            "- 정보관리기술사 121회 2교시: CAP 정리 관점에서의 분산 데이터베이스 투명성과 일관성 모델",
            "- Principles of Distributed Database Systems Reference"
        ],
        "links": [
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)",
            "- [동시성 제어](./009_concurrency_control.md)",
            "- [트랜잭션 격리 수준](./020_isolation_level.md)"
        ]
    },
    "027_binary_search_tree.md": {
        "title": "이진 탐색 트리",
        "insight": "정렬된 데이터 삽입 시 편향 트리로 퇴보하는 O(N) 최악의 시간 복잡도를 방지하기 위해 AVL 트리 및 Red-Black 트리 기반의 자가 균형 메커니즘 적용 필수",
        "rec_text": "데이터 특성과 최악 탐색시간 요구조건에 따라 기본 BST 대신 Red-Black Tree를 채택하고 인메모리 인덱싱 환경에서는 캐시 라인을 고려한 노드 풀링 적용.",
        "diagram_title": "트리 구조 선정 및 적용 절차",
        "diagram": """데이터 특성 및 성능 요구 분석
    ↓
선정 판정
    ├─ 정적 대량 데이터 → 중간값 기준 정렬 후 기본 BST 일괄 빌드
    ├─ 읽기 중심 고속 탐색 → AVL Tree 선정
    └─ 삽입·삭제 빈번한 동적 환경 → Red-Black Tree 선정
    ↓
노드 메모리 풀링 및 동시성 제어 적용""",
        "table_headers": ["구분", "기본 BST", "제언: Red-Black Tree"],
        "table_rows": [
            ["최악 탐색 보장", "불가 (O(N) 편향 위험)", "보장 (O(log N) 상한 유지)"],
            ["쓰기 오버헤드", "추가 회전 비용 없음", "최대 2~3회 회전으로 비용 제한"],
            ["적용 권장 환경", "소규모 정적 데이터", "대규모 동적 시스템 인덱스"]
        ],
        "history": [
            "- 정보관리기술사 137회 1교시: 이진 탐색 트리(BST)",
            "- 정보관리기술사 139회 3교시: BST와 라우팅 테이블 탐색 알고리즘 상관관계",
            "- Thomas H. Cormen, Introduction to Algorithms (CLRS), Chapter 12"
        ],
        "links": [
            "- [인덱스](./047_index.md)",
            "- [B-Tree](./111_b_tree.md)",
            "- [다차원 인덱스 구조](./052_multidimensional_index_structure.md)"
        ]
    },
    "028_erd.md": {
        "title": "개체-관계 다이어그램(ERD)",
        "insight": "개념·논리·물리 모델링 단계별 목적을 엄격히 구분하고 도메인 비즈니스 규칙과 식별/비식별 관계를 정확히 모델링하는 정규화 기반 ERD 작성 필수",
        "rec_text": "개념 모델의 업무 본질을 보존하면서 물리 모델의 DBMS 특성(파티셔닝, 인덱스)을 체계적으로 반영하고 메타데이터 사전과 연계된 ERD 형상 관리 구축.",
        "diagram_title": "단계별 ERD 모델링 및 형상 관리 프로세스",
        "diagram": """[비즈니스 요구사항 분석] ──► [개념 ERD: 핵심 엔터티 및 M:N 관계 도출]
                                       │
                                       ▼
[논리 ERD: 정규화(1NF~3NF), M:N 해소, 식별/비식별 확정]
                                       │
                                       ▼
[물리 ERD: 데이터 타입 지정, 성능 반정규화, 인덱스/파티셔닝 설계]
                                       │
                                       ▼
[DB 메타데이터 시스템 동기화 및 DDL 자동 생성 배포]""",
        "table_headers": ["구분", "물리 중심 직접 모델링", "제언: 단계적 ERD 모델링"],
        "table_rows": [
            ["업무 반영도", "테이블 단위 설계로 비즈니스 맥락 유실", "개념→논리→물리 단계를 통한 업무 완벽 투영"],
            ["정규화 수준", "조기 반정규화로 데이터 중복/이상 빈발", "논리 3NF 완성 후 성능 측정 기반 물리 최적화"],
            ["유지보수성", "ERD와 실제 DB 스키마 간 불일치", "형상 관리 도구 연동을 통한 양방향 동기화"]
        ],
        "history": [
            "- 정보관리기술사 99회 1교시: 데이터 모델링의 3단계(개념, 논리, 물리)와 ERD 표기법",
            "- 정보관리기술사 124회 2교시: 식별 관계와 비식별 관계의 개념 및 성능/무결성 영향",
            "- Peter Chen, The Entity-Relationship Model Standard"
        ],
        "links": [
            "- [정규화](./019_normalization.md)",
            "- [무결성 제약](./013_integrity_constraint.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "029_k_means.md": {
        "title": "K-평균 군집화(K-Means)",
        "insight": "초기 중심점 선택의 민감성과 구형 군집 가정의 한계를 극복하기 위해 K-Means++ 초기화와 엘보우/실루엣 지표 기반의 클러스터 타당성 검증 필수",
        "rec_text": "대규모 고차원 데이터 처리 시 Mini-Batch K-Means 및 PCA 차원축소를 사전 결합하고 비구형 분포 데이터는 DBSCAN 등 밀도 기반 군집화로 우회.",
        "diagram_title": "K-Means++ 최적 군집화 프로세스",
        "diagram": """[데이터 표준화 (Z-Score / MinMax)]
         │
         ▼
[K-Means++ 초기 중심점 선정 (확률적 분산 배치)]
         │
         ▼
[거리 계산 및 클러스터 할당] ◀─────────────────────────┐
         │                                              │
         ▼                                              │
[새로운 군집 중심점(Centroid) 갱신]                     │
         │                                              │
         ├─ [중심점 이동 거리 > 임계값] ──► 반복 수행 ──┘
         │
         └─ [수렴 완료] ──► 실루엣 계수 평가 및 비즈니스 해석""",
        "table_headers": ["구분", "전통적 K-Means (랜덤 초기화)", "제언: K-Means++ 및 타당성 평가"],
        "table_rows": [
            ["초기점 민감도", "국소 최적해(Local Minima) 함정", "데이터 간 거리 확률 기반 스마트 중심점 선정"],
            ["군집 수 K 결정", "경험적 임의 추정", "엘보우 기법(Elbow)과 실루엣 계수 교차 검증"],
            ["대규모 처리량", "전체 데이터 반복 연산으로 지연", "Mini-Batch K-Means 도입으로 처리 속도 향상"]
        ],
        "history": [
            "- 정보관리기술사 110회 2교시: K-Means 알고리즘의 동작 절차와 초기 중심점 선정 문제점",
            "- 정보관리기술사 122회 1교시: 군집 분석 타당성 평가(Silhouette Coefficient)",
            "- Data Mining: Concepts and Techniques"
        ],
        "links": [
            "- [군집분석](./005_cluster_analysis.md)",
            "- [이상치](./010_outlier.md)",
            "- [데이터 시각화](./016_data_visualization.md)"
        ]
    },
    "031_data_exchange.md": {
        "title": "데이터 거래·유통",
        "insight": "데이터 독점과 유출 위험을 방지하고 가치를 정당하게 교환하기 위해 안심구역 기반의 가명처리 및 데이터 가치평가 연계 유통 거버넌스 수립 필요",
        "rec_text": "데이터 거래 계약 시 데이터 이용 목적, 재식별 방지 조치, 권리 귀속을 명문화하고 데이터 거래소(K-DATA 등)의 표준 계약 템플릿 준수.",
        "diagram_title": "신뢰 기반 데이터 거래·유통 라이프사이클",
        "diagram": """[공급자: 데이터 등록] ──► [데이터 품질/가치 평가 및 가명 결합]
                                       │
                                       ▼
[데이터 거래 플랫폼 (K-DATA)] ──► 스마트 계약 및 이용 목적 심의
                                       │
                                       ▼
[안심구역(Data Clean Room)]   ──► 원본 반출 없는 안전한 분석 수행
                                       │
                                       ▼
[수요자: 분석 결과 반출]     ◄── 비식별 무결성 검증 완료 통과""",
        "table_headers": ["구분", "단순 파일 직접 전달", "제언: 안심구역 기반 데이터 유통"],
        "table_rows": [
            ["보안 및 권리", "원본 데이터 무단 복제/유출 위험", "안심구역 내 분석 수행 및 결과만 반출"],
            ["가치 산정", "주관적 협상으로 가격 불신", "공인 데이터 가치평가 모델 연계"],
            ["법적 준거성", "개인정보보호법 위반 리스크", "가명정보 결합 전문기관 승인 및 표준계약서 적용"]
        ],
        "history": [
            "- 정보관리기술사 123회 1교시: 데이터 댐과 데이터 거래소의 개념 및 활성화 과제",
            "- 정보관리기술사 129회 2교시: 데이터 안심구역(Data Clean Room)의 아키텍처와 보안 통제",
            "- 데이터 산업진흥 및 이용촉진에 관한 기본법 표준 가이드라인"
        ],
        "links": [
            "- [데이터 가치평가·데이터 자산화](./002_data_valuation.md)",
            "- [가명정보 결합·비정형 가명처리](./034_pseudonymized_data_guidelines_unstructured.md)",
            "- [데이터 거버넌스](./006_data_governance.md)"
        ]
    },
    "032_sampling.md": {
        "title": "표본추출",
        "insight": "단순 무작위 추출에 편향되지 않고 모집단의 층화 구조와 클러스터 특성을 반영하여 최소 표본으로 추정 효율성을 극대화하는 표본설계 필수",
        "rec_text": "모집단 하위 그룹 간 이질성이 큰 경우 층화추출법을 적용하고 조사 비용 제약 시 집락추출법을 채택하여 표본오차와 조사 비용 최적화.",
        "diagram_title": "표본추출 방법론 선정 의사결정",
        "diagram": """[모집단 특성 분석]
       │
       ├─ [모집단이 동질적임] ──► 단순 무작위 추출 (SRS)
       │
       ├─ [하위 계층 간 이질적, 내부 동질적] ──► 층화 표본추출 (Stratified)
       │                                            └─ 추정의 정밀도 극대화
       │
       └─ [지리적/조직적 분산, 비용 절감 필요] ──► 집락 표본추출 (Cluster)
                                                    └─ 표본조사 비용 최소화""",
        "table_headers": ["구분", "단순 무작위 추출 (SRS)", "제언: 층화 표본추출 (Stratified)"],
        "table_rows": [
            ["표본 대표성", "소수 집단 누락 위험 존재", "모든 계층의 비율 반영으로 완벽한 대표성 확보"],
            ["추정 분산", "모집단 이질성 클 때 분산 큼", "계층 분리를 통해 표본평균의 분산 대폭 축소"],
            ["적용 비용", "추출 프레임만 있으면 간편", "사전 계층 분류 정보 및 프레임 구축 비용 수반"]
        ],
        "history": [
            "- 정보관리기술사 107회 1교시: 확률표본추출법의 4가지 유형(단순무작위, 계통, 층화, 집락)",
            "- Sampling Techniques Standard Reference"
        ],
        "links": [
            "- [중심극한정리](./014_central_limit_theorem.md)",
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [편향](./038_bias.md)"
        ]
    },
    "033_4nf_5nf.md": {
        "title": "제4정규형·제5정규형",
        "insight": "BCNF로 제거되지 않는 다치 종속(MVD)과 조인 종속(JD)을 수학적으로 분해하여 릴레이션 내 숨은 중복과 재결합 이상 현상 원천 배제 필요",
        "rec_text": "독립적인 1:N 관계가 한 테이블에 공존할 때 4NF로 분해하고, 3개 이상의 속성이 상호 제약되는 순환 관계는 5NF 무손실 조인 검증 후 분해.",
        "diagram_title": "4NF 및 5NF 분해 프로세스",
        "diagram": """[BCNF 만족 릴레이션 R(A, B, C)]
         │
         ├─ [다치 종속성 X ↠ Y 존재 (비자명 MVD)]
         │        ▼
         │   [제4정규형 (4NF) 분해: R1(A, B), R2(A, C)]
         │
         └─ [조인 종속성 *(R1, R2, R3) 존재 (순환 관계)]
                  ▼
             [제5정규형 (5NF / PJNF) 무손실 투영 분해]""",
        "table_headers": ["구분", "제4정규형 (4NF)", "제5정규형 (5NF / PJNF)"],
        "table_rows": [
            ["해결 종속성", "다치 종속성 (Multi-Valued Dependency)", "조인 종속성 (Join Dependency)"],
            ["이상 현상", "독립적 다중 속성에 따른 튜플 조합 폭증", "투영 복원 시 허위 튜플(Spurious Tuple) 발생"],
            ["실무 적용", "필수 적용 (과목-교수-교재 분리)", "도메인 규칙 검증 후 신중 적용 (조회 조인 비용)"]
        ],
        "history": [
            "- 정보관리기술사 112회 1교시: 제4정규형(4NF)과 다치 종속성(MVD)의 개념",
            "- 정보관리기술사 124회 2교시: 고급 정규화(BCNF, 4NF, 5NF)의 원리와 분해 절차",
            "- Fundamentals of Database Systems"
        ],
        "links": [
            "- [정규화](./019_normalization.md)",
            "- [반정규화](./017_denormalization.md)",
            "- [무결성 제약](./013_integrity_constraint.md)"
        ]
    },
    "034_pseudonymized_data_guidelines_unstructured.md": {
        "title": "가명정보 결합·비정형 가명처리",
        "insight": "텍스트·이미지 등 비정형 데이터의 개인 식별 위험을 방지하기 위해 AI 기반 개체명 인식(NER)과 위험도 평가 기반 차등 프라이버시 기법 적용 필수",
        "rec_text": "가명정보 결합 시 결합키 연계기관의 해시 솔트(Salt) 정책을 준수하고, 반출 단계에서 재식별 가능성 종합 검토위원회를 통한 사후 위험 통제 구축.",
        "diagram_title": "가명정보 결합 및 비정형 가명처리 절차",
        "diagram": """[공급자 A, B: 비정형 데이터] ──► [NER 기반 개인정보(PII) 탐지 및 마스킹]
                                            │
                                            ▼
[결합키 연계기관 (KISA 등)]    ──► 일방향 암호화 결합키(Salt) 생성 및 연계
                                            │
                                            ▼
[결합 전문기관]                ──► 결합 수행 및 추가 가명처리
                                            │
                                            ▼
[반출 심사위원회]              ──► 재식별 위험도 평가 후 최종 승인 반출""",
        "table_headers": ["구분", "정형 데이터 가명처리", "제언: 비정형 데이터 가명처리"],
        "table_rows": [
            ["식별자 탐지", "컬럼 스키마 기반 정적 탐지", "자연어 처리(NER) 및 비전 AI 기반 문맥 탐지"],
            ["가명화 기법", "삭제, 코드화, 범주화(K-익명성)", "텍스트 마스킹, 가상 인물 치환, 블러링"],
            ["재식별 위험", "준식별자 조합 분석으로 통제", "문맥적 유추 위험성 평가를 위한 반출 심사 필수"]
        ],
        "history": [
            "- 정보관리기술사 123회 2교시: 가명정보 결합 절차와 결합키 연계기관의 역할",
            "- 정보관리기술사 128회 1교시: 비정형 데이터(텍스트, 음성, 영상)의 가명·익명처리 가이드라인",
            "- 개인정보보호위원회 가명정보 처리 가이드라인"
        ],
        "links": [
            "- [데이터 거래·유통](./031_data_exchange.md)",
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [텍스트 마이닝](./015_text_mining.md)"
        ]
    },
    "036_descriptive_statistics.md": {
        "title": "기술통계",
        "insight": "평균 중심의 단일 수치 요약에 왜곡되지 않도록 중위수, 왜도, 사분위수 범위를 함께 제시하여 데이터의 실제 분포 형태를 직관적으로 전달 필요",
        "rec_text": "탐색적 데이터 분석(EDA) 단계에서 중심경향성, 산포도, 분포 형상 지표를 결합한 통계 대시보드를 구축하고 이상치 영향을 사전 격리.",
        "diagram_title": "기술통계 3대 분석 차원 및 지표 체계",
        "diagram": """[데이터 수집 및 전처리]
         │
         ├─ [중심 경향성 측정] : 평균 (Mean), 중위수 (Median), 최빈값 (Mode)
         │
         ├─ [산포도 측정]       : 분산 (Var), 표준편차 (SD), 사분위수 범위 (IQR)
         │
         └─ [분포 형상 측정]   : 왜도 (Skewness, 비대칭도), 첨도 (Kurtosis, 뾰족함)
         │
         ▼
[박스플롯 및 히스토그램 시각화 결합 종합 프로파일링]""",
        "table_headers": ["구분", "산술평균 단독 요약", "제언: 5수치 요약 및 왜도 결합"],
        "table_rows": [
            ["이상치 민감도", "극단값에 의해 평균 왜곡", "중위수와 IQR 병행으로 로버스트한 요약 제공"],
            ["분포 형상 파악", "좌우 대칭성 파악 불가", "왜도 측정을 통해 롱테일 분포 유무 판별"],
            ["의사결정 신뢰", "대표성 상실 위험", "박스플롯 기반의 전체 데이터 분포 가시화"]
        ],
        "history": [
            "- 정보관리기술사 115회 1교시: 기술통계와 추론통계의 비교 및 주요 기술통계량",
            "- Practical Statistics for Data Scientists Standard Reference"
        ],
        "links": [
            "- [이상치](./010_outlier.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [표본추출](./032_sampling.md)"
        ]
    },
    "038_bias.md": {
        "title": "편향",
        "insight": "데이터 수집, 라벨링, 모델 알고리즘 등 전 수명주기에서 발생하는 편향을 정량적으로 감사하고 공정성(Fairness) 지표를 검증하는 윤리적 AI 체계 필수",
        "rec_text": "표본 편향, 확증 편향, 알고리즘 편향의 유형별 체크리스트를 수립하고 Equalized Odds 등 수학적 공정성 평가를 파이프라인에 필수 통합.",
        "diagram_title": "AI 수명주기별 편향 진단 및 완화 파이프라인",
        "diagram": """[데이터 수집 단계] : 표본 추출 편향 (Selection Bias) 점검 및 리샘플링
         │
         ▼
[데이터 라벨링]    : 측정/보고 편향 감사 및 다중 검수자 교차 검증
         │
         ▼
[모델 학습 단계]   : 손실 함수에 공정성 제약(Fairness Penalty) 추가
         │
         ▼
[배포 및 운영]     : 그룹별 오탐/미탐 비율 모니터링 및 실시간 드리프트 통제""",
        "table_headers": ["구분", "단순 정확도 중심 평가", "제언: 공정성 결합 편향 통제"],
        "table_rows": [
            ["소수 그룹 성능", "다수 그룹 성능에 가려져 차별 발생", "인구통계학적 동등성(Demographic Parity) 보장"],
            ["편향 발생 원인", "사후 블랙박스로 추적 불가", "데이터 계보 및 특성 중요도(SHAP) 기반 원인 분해"],
            ["윤리적 위험", "규제 위반 및 사회적 신뢰 상실", "AI 윤리 가이드라인 준거 공정성 리포팅"]
        ],
        "history": [
            "- 정보관리기술사 122회 2교시: 머신러닝 모델의 편향-분산 트레이드오프(Bias-Variance Tradeoff)",
            "- 정보관리기술사 128회 1교시: 인공지능 신뢰성과 편향성(Fairness) 평가 지표",
            "- NIST AI Risk Management Framework (AI RMF)"
        ],
        "links": [
            "- [불편추정량](./011_unbiased_estimator.md)",
            "- [표본추출](./032_sampling.md)",
            "- [이상치](./010_outlier.md)"
        ]
    },
    "039_olap.md": {
        "title": "OLAP",
        "insight": "다차원 분석 성능을 극대화하기 위해 ROLAP의 유연성과 MOLAP의 초고속 연산 성능을 절충한 HOLAP 또는 클라우드 컬럼형 DW 아키텍처 채택 필요",
        "rec_text": "Roll-up, Drill-down, Slicing, Dicing의 다차원 연산을 지원하는 스타/스노우플레이크 스키마를 정립하고 인메모리 큐브 엔진 연동을 통한 실시간 응답 보장.",
        "diagram_title": "다차원 큐브 분석 및 OLAP 아키텍처",
        "diagram": """[원천 트랜잭션 DB (OLTP)]
         │
         ▼ (ETL 파이프라인 정제)
[엔터프라이즈 DW (Star Schema / Fact & Dimension)]
         │
         ├─ [MOLAP] : 사전 집계 다차원 큐브 (초고속 집계 질의)
         ├─ [ROLAP] : 관계형 테이블 직접 다차원 질의 (대용량 유연성)
         └─ [HOLAP] : 상세 데이터는 ROLAP + 요약 집계는 MOLAP
         │
         ▼
[사용자 대시보드 / BI 도구 (Roll-up, Drill-down, Slice & Dice)]""",
        "table_headers": ["구분", "ROLAP (Relational OLAP)", "MOLAP (Multidimensional OLAP)"],
        "table_rows": [
            ["저장 구조", "관계형 DB 테이블 직접 활용", "사전 구축된 다차원 배열 큐브(Cube)"],
            ["질의 성능", "대용량 조인 연산으로 지연 가능", "사전 계산 집계로 즉각적인 응답 속도"],
            ["확장성", "대규모 테라바이트급 데이터 수용", "데이터 큐브 크기 폭증(큐브 폭발) 한계"]
        ],
        "history": [
            "- 정보관리기술사 104회 1교시: OLAP의 주요 4대 연산(Roll-up, Drill-down, Slicing, Dicing)",
            "- 정보관리기술사 117회 2교시: ROLAP, MOLAP, HOLAP의 아키텍처 및 장단점 비교",
            "- The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling"
        ],
        "links": [
            "- [데이터 레이크](./007_data_lake.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [반정규화](./017_denormalization.md)"
        ]
    }
}

for fname, data in batch_2_data.items():
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
        # If no frontmatter, prepend
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
