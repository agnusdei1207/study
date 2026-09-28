import os
import re

batch_5_data = {
    "089_logistic_regression.md": {
        "title": "로지스틱 회귀",
        "insight": "이진 분류 확률을 모델링하기 위해 오즈비(Odds Ratio)에 로그를 취한 로짓 변환과 시그모이드 함수를 적용하고 교차 엔트로피 손실 함수로 최적화 필수",
        "rec_text": "분류 임계값(Threshold)을 단순 0.5로 고정하지 않고 ROC-AUC 및 정밀도-재현율 트레이드오프를 고려하여 비즈니스 비용 최소화 임계값 선정.",
        "diagram_title": "로지스틱 회귀 로짓 변환 및 시그모이드 매핑",
        "diagram": """[선형 결합: z = W^T * X + b (-∞ ~ +∞)]
         │
         ▼ (로지스틱 시그모이드 함수 통과)
[확률 매핑: p = σ(z) = 1 / (1 + e^(-z)) (0.0 ~ 1.0)]
         │
         ▼ (분류 임계치 판정: p ≥ Threshold ?)
   ├─ [YES] ──► Class 1 (사기/이탈/양성)
   └─ [NO]  ──► Class 0 (정상/유지/음성)""",
        "table_headers": ["구분", "선형 회귀 (Linear)", "로지스틱 회귀 (Logistic)"],
        "table_rows": [
            ["출력 범위", "연속형 실수 값 ($-\\infty \\sim +\\infty$)", "0과 1 사이의 사건 발생 확률 ($0 \\sim 1$)"],
            ["손실 함수", "평균제곱오차 (MSE)", "이진 교차 엔트로피 (Binary Cross-Entropy)"],
            ["해석 방식", "독립변수 1단위 증가 시 종속변수 변화량", "독립변수 1단위 증가 시 오즈비($e^{\\beta}$)의 승수 효과"]
        ],
        "history": [
            "- 정보관리기술사 118회 1교시: 로지스틱 회귀분석의 원리와 오즈비(Odds Ratio)의 개념",
            "- 정보관리기술사 127회 2교시: 분류 모델 평가 지표(혼동행렬, ROC-AUC, F1-Score)",
            "- Applied Logistic Regression Standard Guide"
        ],
        "links": [
            "- [다중공선성](./004_multicollinearity.md)",
            "- [가설검정](./041_hypothesis_testing.md)",
            "- [데이터 마이닝](./043_data_mining.md)"
        ]
    },
    "090_opinion_mining.md": {
        "title": "오피니언 마이닝",
        "insight": "단순 긍정/부정 극성 분류를 넘어 속성 기반 감성 분석(ABSA)을 적용하여 특정 제품 기능 및 서비스 품질 단위의 구체적 고객 여론 진단 필수",
        "rec_text": "도메인 특화 감성 사전을 구축하고 최신 사전학습 언어모델(LLM/KoBERT)을 파인튜닝하여 비꼬임(Sarcasm)과 다중 문맥을 정확히 판별하는 파이프라인 수립.",
        "diagram_title": "속성 기반 감성 분석(ABSA) 엔드투엔드 파이프라인",
        "diagram": """[고객 리뷰/VOC 텍스트 수집]
         │
         ▼
[형태소 분석 및 구문 분석 (KoNLPy / Spacy)]
         │
         ▼
[속성-의견 쌍 추출 (Aspect-Opinion Extraction)] : 예: [배송: 속도], [가격: 부담]
         │
         ▼
[문맥 기반 감성 분류 (BERT/RoBERTa)] ──► 속성별 긍정/부정 점수 산출
         │
         ▼
[VOC 대시보드 시각화 및 제품 개선 부서 자동 티켓팅]""",
        "table_headers": ["구분", "단순 문서 레벨 감성분석", "제언: 속성 기반 감성분석 (ABSA)"],
        "table_rows": [
            ["분석 정밀도", "문서 전체를 긍/부정 단일 라벨링", "제품 세부 속성(배송, 가격, 품질)별 다각 분석"],
            ["비즈니스 가치", "단순 여론 추이만 파악 가능", "구체적인 서비스 개선 타깃 즉각 도출"],
            ["문맥 해석", "복합 감정 문장 해석 실패", "속성별 극성 분리로 상반된 감정 완벽 수용"]
        ],
        "history": [
            "- 정보관리기술사 113회 1교시: 오피니언 마이닝(Opinion Mining)과 감성 분석(Sentiment Analysis)",
            "- 정보관리기술사 125회 2교시: 비정형 고객 피드백 분석을 위한 속성 기반 감성 분석 기법",
            "- Mining Text Data Standard Textbook"
        ],
        "links": [
            "- [텍스트 마이닝](./015_text_mining.md)",
            "- [데이터 시각화](./016_data_visualization.md)",
            "- [군집분석](./005_cluster_analysis.md)"
        ]
    },
    "091_optimizer.md": {
        "title": "옵티마이저(Optimizer)",
        "insight": "규칙 기반(RBO)의 한계를 극복하고 데이터 분포 통계에 기반하여 최소 비용의 최적 실행계획을 수립하는 비용 기반 옵티마이저(CBO) 중심 튜닝 필수",
        "rec_text": "옵티마이저가 최적의 결정을 내릴 수 있도록 DBMS 통계정보(Analyze/Histogram)를 주기적으로 갱신하고 극단적 편향 데이터는 바인드 변수 엿보기(Peeking) 통제.",
        "diagram_title": "비용 기반 옵티마이저(CBO) 실행계획 생성 절차",
        "diagram": """[SQL 파싱 및 문법/권한 검증]
         │
         ▼
[질의 변환기 (Query Transformer)] : 서브쿼리 언네스팅, 뷰 머징
         │
         ▼
[대안 경로 생성기 (Plan Generator)] : 조인 순서, 조인 방식, 인덱스 스캔 대안 도출
         │
         ▼ (오브젝트 통계정보 + 히스토그램 + 시스템 CPU/IO 비용 계산)
[비용 산정기 (Cost Estimator)] ──► 최저 Cost 실행계획 선택 ──► [실행 엔진 전달]""",
        "table_headers": ["구분", "규칙 기반 옵티마이저 (RBO)", "비용 기반 옵티마이저 (CBO)"],
        "table_rows": [
            ["경로 결정", "사전 정의된 15개 우선순위 규칙", "통계 기반 예상 I/O 및 CPU 소요 시간 계산"],
            ["데이터 반영", "실제 테이블 크기/분포 무시", "데이터 카디널리티 및 히스토그램 실시간 반영"],
            ["최적화 유연성", "고정된 패턴으로 비효율 발생", "인덱스 스캔 vs 풀스캔의 동적 최적 선택"]
        ],
        "history": [
            "- 정보관리기술사 103회 1교시: 관계형 데이터베이스의 옵티마이저 유형(RBO, CBO) 비교",
            "- 정보관리기술사 121회 2교시: CBO 환경에서 옵티마이저 통계정보와 실행계획 왜곡 해결 방안",
            "- Cost-Based Oracle Fundamentals"
        ],
        "links": [
            "- [인덱스](./047_index.md)",
            "- [데이터베이스 튜닝](./088_database_tuning.md)",
            "- [동시성 제어](./009_concurrency_control.md)"
        ]
    },
    "092_partitioning.md": {
        "title": "파티셔닝",
        "insight": "대용량 테이블의 I/O 경합과 관리 비용을 최소화하기 위해 범위(Range), 리스트(List), 해시(Hash), 컴포지트 파티셔닝을 워크로드에 맞게 설계 필수",
        "rec_text": "조회 쿼리 조건절에 파티션 키를 포함시켜 파티션 프루닝(Partition Pruning)을 유도하고 이력성 로그 데이터는 슬라이딩 윈도우 기반 자동 보관/삭제 구현.",
        "diagram_title": "파티션 프루닝(Partition Pruning) 메커니즘",
        "diagram": """[사용자 쿼리: WHERE sale_date BETWEEN '2026-03-01' AND '2026-03-31']
         │
         ▼
[옵티마이저 파티션 프루닝 판정]
         │
         ├─ [Partition 2026_01] ──► 스캔 스킵 (Pruned)
         ├─ [Partition 2026_02] ──► 스캔 스킵 (Pruned)
         ├─ [Partition 2026_03] ──► 대상 파티션만 직접 스캔 (Direct Access)
         └─ [Partition 2026_04] ──► 스캔 스킵 (Pruned)
         │
         ▼ (불필요한 I/O 75% 절감 및 고속 반환)""",
        "table_headers": ["구분", "범위 파티셔닝 (Range)", "해시 파티셔닝 (Hash)"],
        "table_rows": [
            ["분할 기준", "날짜, 숫자 등 연속적인 범위", "해시 함수 적용 결과값"],
            ["주요 목적", "시계열 이력 데이터 관리 및 아카이빙", "균등한 I/O 분산 및 경합 해소"],
            ["프루닝 지원", "범위 질의 시 완벽한 프루닝 지원", "동등(=) 조건 검색 시에만 프루닝 지원"]
        ],
        "history": [
            "- 정보관리기술사 116회 1교시: 테이블 파티셔닝의 유형(Range, List, Hash, Composite)",
            "- 정보관리기술사 128회 1교시: 파티션 프루닝(Partition Pruning)의 원리와 로컬/글로벌 인덱스",
            "- High Performance Database Partitioning Guide"
        ],
        "links": [
            "- [데이터베이스 분할·샤딩](./021_db_partitioning_sharding.md)",
            "- [인덱스](./047_index.md)",
            "- [데이터베이스 튜닝](./088_database_tuning.md)"
        ]
    },
    "094_text2sql.md": {
        "title": "Text2SQL",
        "insight": "자연어 질의를 정확한 SQL로 변환하기 위해 LLM 프롬프트에 스키마 메타데이터, Few-Shot 예제, 정적 SQL 구문 검증기를 결합한 에이전틱 파이프라인 구축 필수",
        "rec_text": "스키마 링킹(Schema Linking)을 통해 테이블·컬럼 환각을 방지하고 DDL 실행 전 SQLGlot 기반 AST 파싱 및 읽기 전용(SELECT) 권한 통제 강제.",
        "diagram_title": "에이전틱 Text2SQL 변환 및 검증 파이프라인",
        "diagram": """[자연어 질의 인입] ("지난달 VIP 고객별 총 구매액 조회해줘")
         │
         ▼
[스키마 링킹 (Schema Linking)] : 관련 테이블/컬럼 및 비즈니스 용어 사전 검색
         │
         ▼
[LLM SQL 생성 (Few-Shot Prompting)] ──► 생성된 Candidate SQL
         │
         ▼
[정적 구문 검증 및 보안 검사 (SQLGlot)]
  - 문법 오류 검증, DDL/DML 차단 (SELECT만 허용), 파티션 키 포함 확인
         │
         ▼
[안전한 읽기 전용 복제본 DB 질의 실행] ──► [자연어 결과 요약 응답]""",
        "table_headers": ["구분", "단순 LLM 프롬프트 생성", "제언: 에이전틱 Text2SQL 파이프라인"],
        "table_rows": [
            ["스키마 환각", "존재하지 않는 컬럼/조인 조건 날조", "사전 벡터 검색 기반 관련 스키마만 주입"],
            ["보안 위험", "SQL Injection 및 무단 갱신 위험", "AST 검증기로 SELECT 외 구문 원천 차단"],
            ["실행 성공률", "복잡한 중첩 쿼리 작성 실패 다발", "자가 수정(Self-Correction) 에이전트 루프 결합"]
        ],
        "history": [
            "- 정보관리기술사 133회 2교시: LLM 기반 Text2SQL 기술의 원리와 엔터프라이즈 도입 전략",
            "- 정보관리기술사 136회 1교시: RAG와 결합한 자연어 데이터베이스 질의 인터페이스",
            "- Spider & BIRD Text-to-SQL Benchmark Papers"
        ],
        "links": [
            "- [동적 SQL](./098_dynamic_sql.md)",
            "- [벡터 데이터베이스](./044_vector_database.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "097_data_driven_administration.md": {
        "title": "데이터기반행정",
        "insight": "직관과 경험 중심의 행정을 탈피하고 과학적 정책 수립을 위해 공공데이터 개방, 메타데이터 연계, 공동활용 플랫폼 기반의 제도적 거버넌스 정립 필수",
        "rec_text": "데이터기반행정 활성화에 관한 법률에 따라 데이터책임관(CDO)을 지정하고 기관 간 데이터 칸막이를 해소하는 범정부 데이터 통합 분석 인프라 확립.",
        "diagram_title": "데이터기반행정 추진 거버넌스 체계",
        "diagram": """[행정·공공기관 보유 데이터]
         │
         ▼
[범정부 데이터 관리체계 등록] : 공공데이터 카탈로그 및 메타데이터 표준화
         │
         ▼
[정부 데이터 통합 분석 플랫폼]
  - 기관 간 데이터 공유 및 결합
  - 빅데이터 기반 사회문제 진단 및 예측 모델링
         │
         ▼
[증거 기반 정책 수립 (Evidence-based Policy)] ──► [국민 맞춤형 행정 서비스 제공]""",
        "table_headers": ["구분", "전통적 관행 행정", "제언: 데이터기반 과학 행정"],
        "table_rows": [
            ["의사결정 근거", "공무원 개인 경험 및 직관", "객관적 빅데이터 및 통계 분석 결과"],
            ["기관 간 협업", "부처 간 데이터 칸막이로 고립", "공동활용 데이터 등록 의무화 및 실시간 공유"],
            ["정책 피드백", "사후 여론 반응 수동 수렴", "정책 효과성 데이터 실시간 모니터링"]
        ],
        "history": [
            "- 정보관리기술사 123회 1교시: 데이터기반행정 활성화에 관한 법률의 주요 내용과 기대효과",
            "- 정보관리기술사 129회 2교시: 공공데이터 개방과 디지털 플랫폼 정부(DPG) 추진 전략",
            "- 데이터기반행정 활성화에 관한 법률 및 행정안전부 기본계획"
        ],
        "links": [
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [데이터 거래·유통](./031_data_exchange.md)",
            "- [데이터 표준화](./008_data_standardization.md)"
        ]
    },
    "098_dynamic_sql.md": {
        "title": "동적 SQL",
        "insight": "가변적인 다중 검색 조건 처리를 위해 동적 SQL을 채택하되 SQL 인젝션 취약점과 하드 파싱(Hard Parsing) 오버헤드를 원천 차단하는 바인드 변수 적용 필수",
        "rec_text": "MyBatis의 `<if>`, `<where>` 태그 또는 Querydsl 등 Type-Safe 라이브러리를 활용하여 쿼리 정합성을 보장하고 `#` 파라미터 바인딩을 강제.",
        "diagram_title": "안전한 동적 SQL 파싱 및 실행 흐름",
        "diagram": """[사용자 동적 조건 입력 (이름, 날짜, 상태)]
         │
         ▼
[Type-Safe 동적 쿼리 빌더 (Querydsl / MyBatis)]
  - 조건별 동적 WHERE 절 안전 조립
  - 리터럴 문자열 치환($) 배제, 바인드 변수(#) 필수 매핑
         │
         ▼
[DBMS 공유 풀 (Shared Pool) 진입]
         │
         ├─ [바인드 변수 기반 동일 SQL 구조 식별] ──► 소프트 파싱 (Soft Parsing, 고속)
         │
         ▼
[사전 컴파일된 실행계획 재사용] ──► [SQL Injection 방어 및 즉각 실행]""",
        "table_headers": ["구분", "문자열 접합 동적 SQL ($)", "제언: 바인드 변수 동적 SQL (#)"],
        "table_rows": [
            ["보안성", "SQL Injection 공격에 완전 노출", "바인드 파라미터 처리로 인젝션 원천 차단"],
            ["파싱 부하", "조건값마다 매번 하드 파싱 발생", "SQL 문장 공유로 소프트 파싱 재사용 극대화"],
            ["타입 안정성", "런타임 SQL 문법 에러 다발", "Querydsl 도입으로 컴파일 타임 오류 검출"]
        ],
        "history": [
            "- 정보관리기술사 108회 1교시: 정적 SQL(Static SQL)과 동적 SQL(Dynamic SQL)의 비교",
            "- 정보관리기술사 122회 2교시: 소프트 파싱과 하드 파싱의 차이점 및 바인드 변수의 중요성",
            "- Secure Coding Guidelines for SQL"
        ],
        "links": [
            "- [옵티마이저](./091_optimizer.md)",
            "- [데이터베이스 튜닝](./088_database_tuning.md)",
            "- [Text2SQL](./094_text2sql.md)"
        ]
    },
    "101_generative_ai_privacy_guidelines.md": {
        "title": "생성형 AI 개인정보보호",
        "insight": "LLM 학습 및 추론 단계에서의 개인정보 유출을 방지하기 위해 데이터 수집 필터링, RAG 접근 제어, 모델 출력 가명화의 3중 방어 거버넌스 수립 필수",
        "rec_text": "개인정보보호위원회 생성형 AI 가이드라인에 입각하여 프롬프트 입력 단계에서 개인식별정보(PII)를 실시간 마스킹하고 데이터 삭제 요구권 보장.",
        "diagram_title": "생성형 AI 생애주기별 개인정보 보호 프레임워크",
        "diagram": """[1. 데이터 수집/학습 단계]
  - 웹 크롤링 데이터 내 주민번호, 금융정보 PII 필터링 및 가명처리
       │
       ▼
[2. RAG 및 검색 증강 단계]
  - 벡터 DB 내 문서별 역할 기반 접근 제어(RBAC) 및 보안 구획화
       │
       ▼
[3. 프롬프트 인입 및 서빙 단계]
  - 가드레일(NeMo Guardrails): 프롬프트 내 민감정보 실시간 탐지/마스킹
       │
       ▼
[4. 모델 출력 및 사후 감사]
  - 개인정보 재식별 가능성 필터링 및 질의 감사 로그(Audit) 영속화""",
        "table_headers": ["구분", "일반 생성형 AI 서빙", "제언: 개인정보보호 컴플라이언스 AI"],
        "table_rows": [
            ["입력 통제", "사용자 프롬프트 무단 학습 전용", "비학습(Zero Data Retention) API 계약 및 마스킹"],
            ["환각 유출", "기억된 개인정보가 답변에 노출", "출력 가드레일 필터를 통한 민감 데이터 차단"],
            ["법적 책임", "개인정보보호법 위반 과징금", "안전성 확보 조치 기준 및 개인정보 영향평가 완결"]
        ],
        "history": [
            "- 정보관리기술사 131회 1교시: 생성형 AI 환경에서 개인정보 유출 위협과 프라이버시 보호 대책",
            "- 정보관리기술사 134회 2교시: AI 신뢰성 확보를 위한 가드레일(Guardrails)과 데이터 거버넌스",
            "- 개인정보보호위원회 생성형 AI 개인정보보호 정책 가이드라인"
        ],
        "links": [
            "- [가명정보 결합·비정형 가명처리](./034_pseudonymized_data_guidelines_unstructured.md)",
            "- [데이터 거버넌스](./006_data_governance.md)",
            "- [벡터 데이터베이스](./044_vector_database.md)"
        ]
    },
    "103_dba.md": {
        "title": "DBA의 역할과 책임",
        "insight": "클라우드 매니지드 DB 환경에서 단순 설치·패치 중심 운영을 벗어나 데이터 아키텍처, 성능 튜닝, 보안 거버넌스 중심의 데이터 신뢰성 엔지니어(DRE)로 전환 필수",
        "rec_text": "백업/복구 RTO/RPO 검증을 자동화하고 IaC(Terraform) 기반 선언적 인프라 관리 및 FinOps 관점의 클라우드 스토리지 비용 최적화 주도.",
        "diagram_title": "현대적 DBA의 4대 핵심 직무 영역",
        "diagram": """[현대적 DBA (Data Reliability Engineer)]
       │
       ├─ [아키텍처 및 설계] : 논리/물리 데이터 모델링, 파티셔닝, 샤딩 설계
       ├─ [성능 및 튜닝]     : SQL 실행계획 분석, 인덱스 최적화, 커넥션 풀 통제
       ├─ [가용성 및 복구]   : 백업 자동화, 정기 DR 모의훈련, 쿼럼 HA 클러스터링
       └─ [보안 및 거버넌스] : 접근 통제, TDE 암호화, 메타데이터 표준화 통제""",
        "table_headers": ["구분", "전통적 온프레미스 DBA", "제언: 클라우드 시대의 Modern DBA"],
        "table_rows": [
            ["단순 인프라 작업", "OS 패치, DBMS 설치, 수동 백업", "클라우드 자동화 위임 및 IaC 파이프라인 관리"],
            ["주요 가치 창출", "단순 시스템 장애 복구", "데이터 아키텍처 고도화 및 SQL 성능 튜닝 집중"],
            ["비용 관리", "초기 서버 구매(CAPEX) 중심", "FinOps 기반 클라우드 자원 사용량 최적화"]
        ],
        "history": [
            "- 정보관리기술사 98회 1교시: 데이터베이스 관리자(DBA)의 주요 역할과 직무 범위",
            "- 정보관리기술사 127회 1교시: 클라우드 전환 환경에서 DBA의 역할 변화와 데이터 엔지니어링",
            "- DAMA DMBOK2 Data Operations Management"
        ],
        "links": [
            "- [데이터베이스 튜닝](./088_database_tuning.md)",
            "- [고가용성 아키텍처(HA)](./051_ha_architecture.md)",
            "- [데이터 거버넌스](./006_data_governance.md)"
        ]
    },
    "105_data_profiling.md": {
        "title": "데이터 프로파일링",
        "insight": "데이터 정제 및 마이그레이션 실패를 방지하기 위해 컬럼·구조·값 분포의 메타데이터를 통계적으로 전수 분석하는 사전 프로파일링 체계 확립 필수",
        "rec_text": "결측률, 유일성(Uniqueness), 포맷 적합성, 고립 외래키 관계를 자동 진단하여 데이터 품질 규칙(Data Quality Rules)을 역공학 도출.",
        "diagram_title": "데이터 프로파일링 3단계 분석 절차",
        "diagram": """[원천 데이터 소스]
         │
         ▼
[1. 컬럼 프로파일링 (Column Profiling)]
  - 결측치(Null) 비율, 데이터 타입 일치율, 값의 범위(Min/Max), 카디널리티
         │
         ▼
[2. 구조 프로파일링 (Structure Profiling)]
  - 패턴 적합성 (전화번호, 이메일 정규식), 후보키(Candidate Key) 유일성 판정
         │
         ▼
[3. 관계/교차 프로파일링 (Cross-Table Profiling)]
  - 테이블 간 외래키 참조 정합성 검증, 중복 튜플 및 고립 레코드 감지
         │
         ▼
[데이터 품질 지표 산출 및 품질 규칙 자동 등록]""",
        "table_headers": ["구분", "수작업 샘플링 검증", "제언: 자동화된 데이터 프로파일링"],
        "table_rows": [
            ["검증 범위", "일부 표본만 수기 엑셀 검토", "전체 데이터 세트 전수 통계 분석"],
            ["오류 탐지", "경계값 및 숨은 오류 누락", "패턴 분석 기반 비정형 오류 100% 적발"],
            ["연계 가치", "일회성 점검 보고서로 종결", "품질 룰 카탈로그 자동 등록 및 지속 모니터링"]
        ],
        "history": [
            "- 정보관리기술사 115회 1교시: 데이터 품질관리에서 데이터 프로파일링의 개념과 분석 기법",
            "- 정보관리기술사 126회 2교시: 공공데이터 마이그레이션 전 데이터 프로파일링 추진 방안",
            "- Data Quality Assessment Standard Handbook"
        ],
        "links": [
            "- [데이터 품질관리](./003_data_quality_management.md)",
            "- [데이터 표준화](./008_data_standardization.md)",
            "- [데이터 옵저버빌리티](./054_data_observability.md)"
        ]
    },
    "106_normal_distribution.md": {
        "title": "정규분포",
        "insight": "자연 현상과 통계적 추론의 기저를 형성하는 정규분포(가우스 분포)의 대칭성과 68-95-99.7 경험적 규칙을 표준화(Z-변환)와 연계 적용 필수",
        "rec_text": "데이터 분석 전 샤피로-윌크(Shapiro-Wilk) 검정으로 정규성을 확인하고 비정규 데이터는 Box-Cox 변환을 통해 모수적 통계 분석 적용.",
        "diagram_title": "표준정규분포 Z-변환 및 경험적 규칙",
        "diagram": """        정규분포 X ~ N(μ, σ²)  ──► [Z-변환: Z = (X - μ) / σ] ──► 표준정규분포 Z ~ N(0, 1)

                     [대칭 종형 곡선 (Bell Curve)]
                                 │
                            μ-1σ │ μ+1σ  (68.27% 구간)
                          ┌──────┴──────┐
                     μ-2σ │             │ μ+2σ (95.45% 구간)
                   ┌──────┴─────────────┴──────┐
              μ-3σ │                           │ μ+3σ (99.73% 구간)
            ───────┴───────────────────────────┴───────""",
        "table_headers": ["구분", "원시 데이터 직접 분석", "제언: 정규분포 표준화 (Z-Score)"],
        "table_rows": [
            ["단위 종속성", "측정 단위(cm, kg)에 따라 왜곡", "무차원 표준화 점수로 서로 다른 변수 직접 비교"],
            ["이상치 식별", "임의 기준에 따른 이상치 판정", "|Z| > 3 명확한 확률적 기준에 따른 이상치 적발"],
            ["통계적 검정", "비모수 검정만 적용 가능", "Z-검정, t-검정 등 강력한 모수적 추론 적용"]
        ],
        "history": [
            "- 정보관리기술사 111회 1교시: 정규분포의 성질과 표준정규분포의 68-95-99.7 규칙",
            "- Probability and Statistics for Engineers Standard Textbook"
        ],
        "links": [
            "- [중심극한정리](./014_central_limit_theorem.md)",
            "- [z-검정](./012_z_test.md)",
            "- [불편추정량](./011_unbiased_estimator.md)"
        ]
    },
    "109_reliability.md": {
        "title": "신뢰도",
        "insight": "데이터 측정 및 통계 분석의 내적 일관성을 확보하기 위해 크론바흐 알파(Cronbach's α) 계수를 산출하고 재검사 및 반분 신뢰도 검증 병행 필수",
        "rec_text": "설문 및 정성 평가 문항 개발 시 요인 분석을 선행하여 단일 차원성을 검증하고 알파 계수 0.7 이상을 확보하여 측정 신뢰성 보장.",
        "diagram_title": "측정 도구 신뢰도 및 타당도 검증 절차",
        "diagram": """[측정 도구 / 설문 문항 설계]
         │
         ▼
[1. 타당도 검증 (Validity)] : 내용 타당도, 구성 타당도 (요인 분석)
         │
         ▼
[2. 신뢰도 검증 (Reliability)]
  - 검사-재검사법 (안정성 측정)
  - 반분법 (Splitting)
  - 내적 일관성 평가 (크론바흐 알파 계수 α ≥ 0.7 검증)
         │
         ▼
[신뢰도 저해 문항 제거 및 최종 측정 도구 확정]""",
        "table_headers": ["구분", "신뢰도 (Reliability)", "타당도 (Validity)"],
        "table_rows": [
            ["개념 정의", "동일 대상을 반복 측정했을 때의 일관성", "측정하고자 하는 개념을 정확히 측정했는가"],
            ["평가 지표", "크론바흐 알파(Cronbach's α), 상관계수", "요인 분석(Factor Analysis), 상관 분석"],
            ["상호 관계", "타당도가 높기 위한 필수 조건", "신뢰도가 높아도 타당도가 낮을 수 있음"]
        ],
        "history": [
            "- 정보관리기술사 113회 1교시: 데이터 신뢰도(Reliability)와 타당도(Validity)의 개념 및 평가 기법",
            "- Research Methodology Standard Reference"
        ],
        "links": [
            "- [가설검정](./041_hypothesis_testing.md)",
            "- [편향](./038_bias.md)",
            "- [데이터 품질관리](./003_data_quality_management.md)"
        ]
    },
    "111_b_tree.md": {
        "title": "B-Tree·B+Tree",
        "insight": "디스크 I/O 횟수를 억제하기 위해 페이지 크기에 맞춘 높은 팬아웃(Fan-out)을 유지하고 범위 검색 가속화를 위한 B+Tree 리프 순차 연결 적용 필수",
        "rec_text": "루트부터 모든 리프까지 깊이가 동일한 완벽한 자가 균형을 유지하고, 인덱스 쓰기 부하 분산을 위한 버퍼 풀 튜닝 및 주기적 인덱스 재구성 확립.",
        "diagram_title": "B+Tree 다차원 분기 및 리프 순차 연결 2차원 아스키 구조",
        "diagram": """                  [ 루트 노드: | 20 | 50 | ]
                 /            |             \\
                /             |              \\
               ▼              ▼               ▼
      [ | 10 | ]         [ | 30 | 40 | ]     [ | 60 | 80 | ] (내부 분기 노드)
       /      \\          /      |      \\     /      |      \\
      ▼        ▼        ▼       ▼       ▼   ▼       ▼       ▼
    [5,8] ──► [12] ──► [25] ──► [35] ──► [45] ──► [55] ──► [70] (리프: 양방향 연결)
    (리프 순차 스캔: 범위 질의 BETWEEN 25 AND 55 수행 시 수평 포인터 고속 순회)""",
        "table_headers": ["구분", "B-Tree", "제언: B+Tree (엔터프라이즈 RDBMS)"],
        "table_rows": [
            ["데이터 저장 위치", "루트, 내부 노드, 리프 노드 모두 저장", "오직 리프 노드에만 실제 데이터/RID 저장"],
            ["내부 노드 팬아웃", "데이터 포함으로 분기 수 작음", "키 포인터만 저장하여 팬아웃 극대화 (트리 높이 축소)"],
            ["범위 검색 (BETWEEN)", "트리 상하 순회 반복으로 비효율", "리프 노드 간 연결 리스트를 통한 순차 고속 스캔"]
        ],
        "history": [
            "- 정보관리기술사 103회 1교시: B-Tree 인덱스의 구조와 검색 메커니즘",
            "- 정보관리기술사 121회 2교시: B-Tree와 B+Tree의 구조적 차이점 및 범위 검색 성능 비교",
            "- Douglas Comer, The Ubiquitous B-Tree (ACM Computing Surveys)"
        ],
        "links": [
            "- [이진 탐색 트리](./027_binary_search_tree.md)",
            "- [인덱스](./047_index.md)",
            "- [다차원 인덱스 구조](./052_multidimensional_index_structure.md)"
        ]
    }
}

for fname, data in batch_5_data.items():
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

    # 3. Special fix for 111 B-Tree in section III (replace tree diagram)
    if fname == "111_b_tree.md":
        content = re.sub(
            r'```text\n검색 키 → 루트의 키 구간 비교[\s\S]*?```',
            f'```text\n{data["diagram"]}\n```',
            content
        )

    # 4. Fix mechanical endings or '다.' endings in content if any
    content = re.sub(r'달라진다\.', '차이 발생.', content)
    content = re.sub(r'선택한다\.', '선택 체계 수립.', content)
    content = re.sub(r'확인한다\.', '확인 필요.', content)
    content = re.sub(r'적용한다\.', '적용 필요.', content)

    # 5. Fix Ⅵ. 제언
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
