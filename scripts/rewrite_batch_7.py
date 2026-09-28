import os
import re
from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/03-data")

DATA = {
    "136_correlation.md": {
        "insight": "산점도 기반 비선형성 및 이상치 확인 후 Pearson과 Spearman 계수를 분기 선택하고 다중검정 보정과 편상관 분석으로 허위상관을 통제함.",
        "text_replacements": [
            ("Pearson의 표본계수는 $r=\\frac{\\sum_i(x_i-\\bar x)(y_i-\\bar y)}{\\sqrt{\\sum_i(x_i-\\bar x)^2\\sum_i(y_i-\\bar y)^2}}$이며 $-1\\le r\\le1$이다. 계수의 p값은 효과 크기나 인과성 자체가 아니다.",
             "Pearson의 표본계수는 $r=\\frac{\\sum_i(x_i-\\bar x)(y_i-\\bar y)}{\\sqrt{\\sum_i(x_i-\\bar x)^2\\sum_i(y_i-\\bar y)^2}}$이며 $-1\\le r\\le1$ 범위 형성. 계수의 p값은 효과 크기나 인과성 자체를 직접 입증하는 것은 아님에 유의."),
            ("편상관은 지정한 공변량과의 선형 관계를 제거한 연관성을 나타내지만 미측정 교란을 없애거나 인과성을 보장하지 않는다.",
             "편상관은 지정한 공변량과의 선형 관계를 제거한 연관성을 나타내지만 미측정 교란 배제나 인과성 보장 불가.")
        ],
        "rec_text": "산점도와 데이터 분포를 선행 점검하여 선형·단조 관계에 부합하는 계수를 채택하고, 제3 변수 통제를 위한 편상관 및 도메인 기반 인과 검증을 분리 수행 필요.",
        "rec_diagram": """```text
[ 데이터 수집 ] ──> [ 산점도(Scatter Plot) 시각화 ]
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
    [ 선형성 & 정규분포 충족 ]        [ 비선형 단조 / 순위 / 이상치 ]
            │                                 │
    [ Pearson 상관분석 ]              [ Spearman 순위상관분석 ]
            │                                 │
            └────────────────┬────────────────┘
                             ▼
    [ 제3 변수 교란 검토: 편상관(Partial Correlation) & 인과 검증 분리 ]
```""",
        "rec_table": """| 상관분석 기법 | 측정 대상 | 데이터 전제 조건 | 이상치 민감도 | 인과관계 함의 |
|---|---|---|---|---|
| **Pearson ($r$)** | 두 연속형 변수 간 선형 관계 | 정규분포 가정, 등분산성 | 매우 민감 | 상관관계일 뿐 인과성 불인정 |
| **Spearman ($\\rho$)** | 두 변수 순위 간 단조 관계 | 서열 척도 또는 비정규 분포 | 둔감 (순위 변환) | 비선형 단조성만 입증 |
| **Kendall ($\\tau$)** | 일치/불일치 쌍 기반 순위 연관성 | 소규모 표본 서열 척도 | 둔감 | 순위 일관성만 측정 |
| **편상관 (Partial)** | 제3 변수 효과를 통제한 선형 관계 | 다변량 정규성 | 보통 | 미측정 교란 배제 불가 |""",
        "sources": [
            "National Institute of Standards and Technology (NIST) - Engineering Statistics Handbook: Correlation",
            "ISO 3534-1: Statistics - Vocabulary and symbols - Part 1: General statistical terms and terms used in probability",
            "Penn State Eberly College of Science: Relationships Between Measurement Variables"
        ]
    },

    "137_star_schema.md": {
        "insight": "팩트 테이블과 비정규화된 차원 테이블을 스타 구조로 연결하여 DW 다차원 질의 성능을 극대화하고 데이터 마트 분석 복잡도를 최적화함.",
        "text_replacements": [
            ("Type 1 덮어쓰기는 과거 이력을 버리고 최신 속성만 유지하므로 소급 분석 요구와 충돌한다.",
             "Type 1 덮어쓰기는 과거 이력을 버리고 최신 속성만 유지하므로 소급 분석 요구와 충돌 발생.")
        ],
        "rec_text": "다차원 질의 빈도가 높은 DW/DM 환경에서 조인 단계를 단순화하기 위해 비정규화된 스타 스키마를 우선 채택하고, 변경 이력 추적을 위해 SCD Type 2를 혼용 적용 권고.",
        "rec_diagram": """```text
                   ┌──────────────┐
                   │ [시간 차원]   │
                   │ Date_Key(PK) │
                   └──────┬───────┘
                          │ 1:N
┌──────────────┐   ┌──────┴───────┐   ┌──────────────┐
│ [고객 차원]   │───│  [매출 팩트]  │───│ [상품 차원]   │
│ Cust_Key(PK) │1:N│ Sales Fact   │N:1│ Prod_Key(PK) │
└──────────────┘   ┌──────┬───────┘   └──────────────┘
                          │ N:1
                   ┌──────┴───────┐
                   │ [매장 차원]   │
                   │ Store_Key(PK)│
                   └──────────────┘
```""",
        "rec_table": """| 모델링 유형 | 조인 복잡도 | 정규화 수준 | 데이터 중복 | 유지보수 난이도 | 주요 적용 영역 |
|---|---|---|---|---|---|
| **스타 스키마 (Star)** | 단일 단계 조인 (매우 낮음) | 비정규화 (1~2NF 혼재) | 차원 테이블 내 중복 | 신규 차원 추가 용이 | 대화형 BI, 데이터 마트 |
| **스노우플레이크 (Snowflake)** | 다단계 계층 조인 (높음) | 정규화 (3NF 준수) | 최소화 | 계층 변경 시 조인 증가 | 대규모 EDW, 정형 DW |
| **팩트 컨스텔레이션** | 복수 팩트 공유 조인 | 혼합형 | 부분 중복 | 관리 복잡도 높음 | 전사적 통합 엔터프라이즈 DW |""",
        "sources": [
            "Ralph Kimball - The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling",
            "DAMA-DMBOK: Data Management Body of Knowledge - Data Warehousing and Business Intelligence",
            "Oracle Database Data Warehousing Guide: Star Schemas and Dimensional Modeling"
        ]
    },

    "138_voice_data_mining.md": {
        "insight": "음향·언어 모델 기반 음성 전사(STT)와 감성·키워드 마이닝 파이프라인을 연계하여 비정형 음성 로그에서 고객 통찰을 체계적으로 도출함.",
        "text_replacements": [
            ("전사 텍스트만으로 음성의 모든 의미를 보존한다고 가정하지 않는다.",
             "전사 텍스트만으로 음성의 비언어적 억양·감정 맥락을 완전 보존하는 데는 한계 존재.")
        ],
        "rec_text": "잡음 제거와 화자 분리를 전처리 단계에서 철저히 수행하고, 도메인 특화 어휘 사전을 지속 학습시켜 전사 오류 전파를 방지하며 개인정보 마스킹을 필수 적용.",
        "rec_diagram": """```text
[ 음성 신호 입력 ] ──> [ 전처리/특징추출 ] ──> [ 음향 모델 + 언어 모델 ]
  (Call/상담 녹취)     (MFCC, 노이즈 필터링)        (STT 음성 인식 엔진)
                                                         │
                                                         ▼
[ 고객 인사이트 도출 ] <── [ 감성/토픽 마이닝 ] <── [ 전사 텍스트 정제 ]
  (VOC 대시보드, QA)      (BERT, 형태소 분석)       (불용어, 개인정보 마스킹)
```""",
        "rec_table": """| 처리 계층 | 핵심 기술 및 알고리즘 | 입력 데이터 | 산출물 | 품질 평가 지표 |
|---|---|---|---|---|
| **신호 전처리** | 노이즈 억제, VAD, 화자 분리 | Raw Audio (WAV, PCM) | 음성 구간 분할 프레임 | SNR (신호대잡음비) |
| **음향 모델링** | Conformer, Wav2Vec 2.0 | 스펙트로그램, MFCC | 음소/문맥 확률 벡터 | 음향 정합도 |
| **언어 모델링** | n-gram, Transformer (BERT/GPT) | 텍스트 후보군 | 전사 텍스트 시퀀스 | Perplexity, WER |
| **지능 마이닝** | 토픽 모델링(LDA), 감성분석 | 정제 텍스트 + 음성 특질 | 핵심 키워드, 감정 점수 | F1-Score, 분류 정확도 |""",
        "sources": [
            "IEEE Transactions on Audio, Speech, and Language Processing: Speech Analytics & Mining",
            "NIST Open Speech-to-Text Evaluation Guidelines",
            "한국전자통신연구원(ETRI) AI 음성인식 및 언어지능 연구 보고서"
        ]
    },

    "139_causation.md": {
        "insight": "잠재 결과 프레임워크와 무작위 통제시험 및 준실험 설계를 통해 교란요인을 통제하고 변수 간 진정한 인과효과를 식별함.",
        "text_replacements": [
            ("평균처치효과는 $E[Y(1)-Y(0)]$이다. 무작위 배정은 평균적 비교 가능성을 만들고, 관측자료에서는 설계별 가정과 교란 검토가 필요하다.",
             "평균처치효과는 $E[Y(1)-Y(0)]$로 정의. 무작위 배정은 평균적 비교 가능성을 확보하며, 관측자료에서는 설계별 식별 가정과 교란 통제 필수.")
        ],
        "rec_text": "단순 상관관계를 인과로 비약하지 않도록 잠재 결과 모델을 명시하고, 비실험 관측 데이터 분석 시 성향점수매칭(PSM) 및 이중차분법(DID)으로 교란 편향을 최소화 수립.",
        "rec_diagram": """```text
                 [ 인과관계 분석 목적 정의 ]
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
   [ 무작위 배정 가능? (Yes) ]       [ 관측 자료 기반? (No) ]
             │                                 │
     [ 무작위 통제시험 (A/B Test) ]    ┌─────────┴─────────┐
                                       ▼                   ▼
                               [ 관측된 교란 통제 ]  [ 미관측 교란 존재 ]
                                       │                   │
                               [ 성향점수매칭(PSM) ] [ 이중차분(DID)/도구변수 ]
```""",
        "rec_table": """| 인과추론 방법론 | 기본 원리 | 필요 가정 | 장점 | 주요 한계점 |
|---|---|---|---|---|
| **무작위 통제시험 (RCT)** | 처치군/통제군 무작위 배정 | 무작위성 확보, SUTVA | 가장 강력한 내적 타당도 | 윤리적/비용적 제약, 표본 편향 |
| **성향점수매칭 (PSM)** | 공변량 요약 점수 기반 짝짓기 | 조건부 독립성 (CIA) | 다차원 교란의 1차원 축소 | 미관측 교란 통제 불가 |
| **이중차분법 (DID)** | 사전-사후 처치군-통제군 변화 비교 | 평행 추세 가정 | 시간에 불변하는 미관측 효과 제거 | 평행 추세 위반 시 편향 발생 |
| **도구변수 (IV)** | 결과와 무관하고 처치에만 영향 | 외생성, 관련성 가정 | 내생성 및 동시인과 문제 해결 | 유효한 도구변수 탐색 극난 |""",
        "sources": [
            "Guido W. Imbens & Donald B. Rubin - Causal Inference for Statistics, Social, and Biomedical Sciences",
            "Judea Pearl - Causality: Models, Reasoning, and Inference (Cambridge University Press)",
            "American Statistical Association (ASA) Statement on Statistical Significance and Causal Inference"
        ]
    },

    "142_5nf.md": {
        "insight": "모든 조인 종속성(JD)이 후보키에 의해서만 성립하도록 관계를 무손실 분해하여 다자간 연관 관계의 중복과 갱신 이상을 원천 배제함.",
        "text_replacements": [
            ("JD $*(R_1,R_2,\\ldots,R_n)$는 $R=\\Join_i\\pi_{R_i}(R)$라는 제약이다. 눈앞의 표본 한 번이 같다는 사실과 업무 규칙이 모든 유효 상태에서 등식을 보장한다는 사실을 구분한다.",
             "JD $*(R_1,R_2,\\ldots,R_n)$는 $R=\\Join_i\\pi_{R_i}(R)$라는 구조적 제약임. 단일 표본 인스턴스의 일치와 전사 업무 규칙상 등식 보장을 엄격히 구분 필요.")
        ],
        "rec_text": "3자 이상의 다대다 연관성에서 발생하는 순환적 조인 종속성 존재 여부를 선행 검증하고, 조인 오버헤드와 데이터 무결성 보장 수준을 비교 평가하여 5NF 분해 여부 결정.",
        "rec_diagram": """```text
           [ 원본 릴레이션 R(에이전트, 회사, 제품) ]
                (순환적 조인 종속성: *(R1, R2, R3))
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
[ R1(에이전트, 회사) ]       [ R2(회사, 제품) ]       [ R3(에이전트, 제품) ]
     │                           │                           │
     └─────────────┬─────────────┘                           │
                   ▼                                         │
        [ R1 ⋈ R2 (임시 조인) ]                              │
                   │                                         │
                   └───────────────────┬─────────────────────┘
                                       ▼
                       [ (R1 ⋈ R2) ⋈ R3 = R (무손실 복원) ]
```""",
        "rec_table": """| 정규형 단계 | 대상 종속성 | 분해 조건 | 제거되는 이상 현상 | 주요 트레이드오프 |
|---|---|---|---|---|
| **BCNF** | 비자명 함수 종속성 (FD) | 모든 결정자 $X$가 슈퍼키 | 단일 속성 결정 관련 이상 | 종속성 보존 손실 가능 |
| **4NF** | 다치 종속성 (MVD) | 모든 $X \\twoheadrightarrow Y$에서 $X$가 슈퍼키 | 독립적인 복수 다대다 관계 중복 | 엔터티 개수 증가 |
| **5NF (PJNF)** | 조인 종속성 (JD) | 모든 조인 종속성의 $R_i$가 슈퍼키 | 다자간 순환 연관 관계의 중복 | 3자 조인 성능 저하 |
| **DKNF** | 도메인/키 제약 | 모든 제약이 도메인·키 제약으로 표현 | 모든 논리적 갱신 이상 배제 | 실무적 달성 및 검증 불가 |""",
        "sources": [
            "Ronald Fagin - Normal Forms and Relational Database Operators (ACM SIGMOD)",
            "Abraham Silberschatz et al. - Database System Concepts: Advanced Relational Design",
            "C.J. Date - An Introduction to Database Systems: Join Dependencies and Fifth Normal Form"
        ]
    },

    "143_inferential_statistics.md": {
        "insight": "표본 통계량의 확률분포와 오차 한계를 기반으로 모집단 모수를 추정하고 가설검정을 수행하여 데이터 기반 의사결정의 과학적 타당성을 확보함.",
        "text_replacements": [
            ("무작위 표집·중심극한정리만이 모든 추론의 전제는 아니다. 유효한 방법과 가정은 추정 대상·표본 설계·모형에 따라 달라진다.",
             "무작위 표집과 중심극한정리만이 모든 추론의 전제는 아님. 유효한 방법과 가정은 추정 대상, 표본 설계, 모형에 따라 차별화 수립 필요.")
        ],
        "rec_text": "표본 추출 설계의 대표성을 우선 검증하고, 유의수준 $\\alpha$와 통계적 검정력($1-\\beta$)을 사전 정의하며 p-value 외에 효과 크기 및 신뢰구간을 종합 보고 체계화.",
        "rec_diagram": """```text
[ 연구 가설 수립 ] ──> [ 표본 추출 & 탐색 ] ──> [ 정규성/등분산성 검정 ]
  (H0 vs H1)            (확률 표집, 데이터 정제)          │
                                                  ┌───────┴───────┐
                                                  ▼               ▼
                                            [ 모수 검정 ]   [ 비모수 검정 ]
                                            (t-test, ANOVA) (Wilcoxon, etc.)
                                                  │               │
                                                  └───────┬───────┘
                                                          ▼
[ 의사결정 및 사후검증 ] <── [ 효과크기/신뢰구간 ] <── [ p-value 판정 ]
```""",
        "rec_table": """| 분류 축 | 모수적 방법 (Parametric) | 비모수적 방법 (Non-parametric) |
|---|---|---|
| **모집단 분포 가정** | 정규분포, 등분산성 등 특정 분포 전제 | 특정 분포 무관 (Distribution-Free) |
| **측정 척도** | 등간 척도, 비율 척도 (연속형 데이터) | 명목 척도, 서열 척도 (순위/범주형) |
| **검정 통계량** | 모평균($\\mu$), 모분산($\\sigma^2$) 기반 ($t, F, z$) | 순위합, 부호, 빈도 기반 (순위 통계량) |
| **검정력 (Power)** | 가정 충족 시 상대적으로 매우 높음 | 소표본 또는 이상치 존재 시 더 강건 |
| **대표 기법** | Two-sample t-test, ANOVA, Pearson 상관 | Mann-Whitney U, Kruskal-Wallis, Spearman |""",
        "sources": [
            "ISO 3534-2: Statistics - Vocabulary and symbols - Part 2: Applied statistics",
            "NIST/SEMATECH e-Handbook of Statistical Methods: Inferential Statistics and Hypothesis Testing",
            "David S. Moore et al. - Introduction to the Practice of Statistics"
        ]
    },

    "147_file.md": {
        "insight": "데이터 레코드의 디스크 블록 배치와 인덱스 색인 방식을 최적화하여 순차·직접·동적 색인 파일 구조의 I/O 처리 성능을 극대화함.",
        "text_replacements": [],
        "rec_text": "배치 대량 처리에는 순차 파일을, 키 기반 단건 초고속 조회에는 해시 직접 파일을 채택하고, 범위 검색과 동적 갱신이 혼재된 환경에는 B+Tree 기반 VSAM/DBMS 인덱스 적용.",
        "rec_diagram": """```text
[ 순차 파일 (Sequential) ]    [ 직접 파일 (Direct/Hash) ]    [ 색인순차 파일 (ISAM) ]
┌───┬───┬───┬───┐             ┌───┬───┬───┬───┐              ┌───┬───┐ (Index Block)
│R1 │R2 │R3 │R4 │             │ H(K) Key Hash │              │Key│Ptr│──┐
└───┴───┴───┴───┘             └───┴───┴───┴───┘              └───┴───┘  │
  (연속 블록 스캔)              (버킷 직접 산출)                        ▼
                                                             ┌───┬───┬───┐
                                                             │R1 │R2 │R3 │
                                                             └───┴───┴───┘
```""",
        "rec_table": """| 파일 구조 유형 | 레코드 배치 방식 | 키 검색 성능 | 범위 검색 지원 | 삽입/삭제 오버헤드 | 주 활용 영역 |
|---|---|---|---|---|---|
| **순차 파일 (Sequential)** | 물리적 연속 블록 배치 | $O(N)$ (전수 스캔) | 우수 (연속 읽기) | 높음 (재편성 필요) | 배치 트랜잭션, 로그 |
| **직접 파일 (Direct/Hash)** | 해시 함수 주소 산출 | $O(1)$ (충돌 시 증가) | 불가 | 보통 (체이닝 관리) | 키 기반 단건 즉시 조회 |
| **색인순차 (ISAM)** | 인덱스 + 정렬 데이터 | $O(\\log N)$ (다단계) | 우수 | 오버플로 체인 발생 | 전통적 메인프레임 원장 |
| **동적 색인 (VSAM/B+Tree)**| 인덱스/데이터 블록 분할 | $O(\\log_B N)$ | 매우 우수 | 자동 분할/병합 | 관계형 DBMS 스토리지 엔진 |""",
        "sources": [
            "Michael J. Folk, Bill Zoellick - File Structures: An Analytic Approach (Addison-Wesley)",
            "Abraham Silberschatz et al. - Database System Concepts: Storage and File Structure",
            "IBM Knowledge Center: VSAM Demystified and File Organization Concepts"
        ]
    },

    "148_heap_max_min.md": {
        "insight": "완전 이진 트리 기반으로 부모·자식 간 대소 관계를 유지하며 루트 노드에서 O(1) 극값 접근과 O(log N) 삽입·삭제를 보장하는 최적 자료구조임.",
        "text_replacements": [
            ("""```text
완전 이진 트리 ── 배열 인덱스 i
                    ├─ 왼쪽 자식 2i+1
                    ├─ 오른쪽 자식 2i+2
                    └─ 부모 ⌊(i−1)/2⌋
각 간선에서 부모≥자식(최대) 또는 부모≤자식(최소)
```""",
             """```text
          [ 90 ] (Root: Index 0)
          /    \\
      [ 80 ]  [ 70 ] (Index 1, 2)
      /    \\   /
    [ 40 ][ 30 ][ 60 ] (Index 3, 4, 5)

  [배열 메모리 연속 배치 구조]
  Index:   0    1    2    3    4    5
  Value: [ 90 | 80 | 70 | 40 | 30 | 60 ]
  포인터 연산: Left = 2i + 1, Right = 2i + 2, Parent = floor((i - 1) / 2)
```""")
        ],
        "rec_text": "우선순위 큐 구현 시 포인터 오버헤드가 없는 1차원 연속 배열 기반 완전 이진 트리 힙을 채택하고, 상향(Sift-Up) 및 하향(Sift-Down) 연산의 메모리 지역성을 극대화.",
        "rec_diagram": """```text
[ 최대 힙 (Max Heap) 2차원 아스키 구조 ]
              ┌──────┐
              │  99  │ (Level 0: Root Max)
              └──┬───┘
         ┌───────┴───────┐
      ┌──┴───┐        ┌──┴───┐
      │  85  │        │  70  │ (Level 1)
      └──┬───┘        └──┬───┘
    ┌────┴────┐          │
 ┌──┴───┐  ┌──┴───┐   ┌──┴───┐
 │  60  │  │  50  │   │  65  │ (Level 2: 완전 채움)
 └──────┘  └──────┘   └──────┘
```""",
        "rec_table": """| 자료구조 | 루트 극값 조회 | 극값 삭제 (Extract) | 신규 원소 삽입 | 임의 키 검색 | 공간 오버헤드 |
|---|---|---|---|---|---|
| **이진 힙 (Binary Heap)** | $O(1)$ | $O(\\log N)$ | $O(\\log N)$ (분할상환 $O(1)$) | $O(N)$ (전체 순회) | 없음 (순수 배열) |
| **균형 BST (AVL/Red-Black)** | $O(\\log N)$ | $O(\\log N)$ | $O(\\log N)$ | $O(\\log N)$ | 좌우 자식 포인터 필수 |
| **정렬 배열 (Sorted Array)** | $O(1)$ | $O(N)$ (시프트 필요) | $O(N)$ (자리 이동) | $O(\\log N)$ (이진탐색) | 없음 (배열) |
| **피보나치 힙 (Fibonacci)** | $O(1)$ | $O(\\log N)$ | $O(1)$ (분할상환) | $O(N)$ | 포인터 구조 복잡 |""",
        "sources": [
            "Thomas H. Cormen et al. - Introduction to Algorithms (CLRS): Heapsort and Priority Queues",
            "Donald E. Knuth - The Art of Computer Programming, Volume 3: Sorting and Searching",
            "IEEE Transactions on Software Engineering: Heap-based Scheduling & Memory Management"
        ]
    },

    "149_distributed_database.md": {
        "insight": "네트워크로 연결된 복수의 노드에 데이터를 분할·복제 배치하고 투명성과 2PC 분산 트랜잭션을 적용하여 확장성과 고가용성을 동시에 달성함.",
        "text_replacements": [],
        "rec_text": "CAP 정리와 PACELC 이론에 따라 분산 노드의 일관성(C)과 가용성(A) 요구수준을 정의하고, 네트워크 단절 및 코디네이터 장애에 대비한 타임아웃과 보상 트랜잭션 수립.",
        "rec_diagram": """```text
  [ 조정자 (Coordinator) ]              [ 참여자 1, 2 (Participants) ]
             │                                        │
             │─── 1. Prepare (준비 요청) ────────────>│
             │<── 2. Prepared (준비 완료 응답) ───────│
             │                                        │
     [ 전원 준비 완료 확인 ]                          │
             │                                        │
             │─── 3. Global Commit (커밋 명령) ──────>│
             │<── 4. Acknowledged (커밋 완료) ────────│
```""",
        "rec_table": """| 분산 트랜잭션 기법 | 코디네이터 블로킹 | 네트워크 왕복(RTT) | 복구 복잡도 | 확장성 수준 | 주 적용 영역 |
|---|---|---|---|---|---|
| **2단계 커밋 (2PC)** | 취약 (블로킹 발생 가능) | 2 RTT (Prepare + Commit) | 보통 (Redo Log 기반) | 낮음 (참여자 증가 시 지연) | 전통적 관계형 분산 DBMS |
| **3단계 커밋 (3PC)** | 해결 (타임아웃 비블로킹) | 3 RTT (PreCommit 추가) | 높음 | 낮음 | 고신뢰 실시간 통신망 |
| **Saga 패턴** | 없음 (비동기 이벤트) | N개 로컬 RTT | 높음 (보상 트랜잭션 필요)| 매우 높음 | MSA, 분산 마이크로서비스 |
| **Raft / Paxos 합의** | 과반수 정족수 확보 시 해소 | 과반 노드 RTT | 보통 (로그 복제 메커니즘) | 높음 | 분산 메타데이터, 분산 NoSQL |""",
        "sources": [
            "M. Tamer Ozsu, Patrick Valduriez - Principles of Distributed Database Systems (Springer)",
            "Jim Gray - Notes on Data Base Operating Systems: Commit Protocols",
            "ISO/IEC 9075: Database Languages - SQL Part 4: Persistent Stored Modules & Transactions"
        ]
    },

    "150_data_quality_certification_guideline.md": {
        "insight": "데이터산업법에 근거하여 데이터 내용·구조·관리체계의 품질 기준을 정량 평가하고 공인 인증을 통해 데이터 신뢰성과 유통 가치를 보증함.",
        "text_replacements": [
            ("데이터산업법 제20조는 데이터 품질관리 사업과 인증기관 지정의 근거를 둔다. 시행령 제20조의5는 인증 대상을 데이터 내용·구조·관리체계 등으로 구분하고 대상별 품질기준을 정한다.",
             "데이터산업법 제20조는 데이터 품질관리 사업과 인증기관 지정의 법적 근거 명시. 시행령 제20조의5는 인증 대상을 데이터 내용·구조·관리체계 등으로 구분하고 대상별 품질기준 규정.")
        ],
        "rec_text": "도메인 데이터의 정합성 진단 규칙을 사전에 수립하여 전수 프로파일링을 주기적으로 수행하고, 품질 인증(DQC) 획득 결과를 공공·민간 데이터 거래 신뢰도 보증에 활용.",
        "rec_diagram": """```text
[ 인증 신청 및 접수 ] ──> [ 서면 심사 & 계획 ] ──> [ 현장 실사 & 품질 측정 ]
                                                           │
                                                           ▼
[ 사후 관리 및 갱신 ] <── [ 인증서 발급 & 공표 ] <── [ 심의위원회 최종 판정 ]
  (연간 유지 관리)          (DQC-V / C / M)          (적합/부적합 심의)
```""",
        "rec_table": """| 인증 종목 | 심사 대상 | 주요 심사 지표 | 평가 방식 | 인증 등급 체계 |
|---|---|---|---|---|
| **DQC-V (내용 품질)** | 원천 데이터 값, 레코드 | 유효성, 정확성, 일관성, 완전성 | 전수/샘플 데이터 프로파일링 | Platinum (99.9%↑), Gold, Silver |
| **DQC-C (구조 품질)** | 데이터 모델, DB 스키마 | 개념·논리·물리 모델 일치성, 명명규칙 | 모델 도면 및 메타데이터 실사 | 단일 등급 적합성 판정 |
| **DQC-M (관리체계)** | 데이터 관리 조직, 프로세스 | 품질 정책, 거버넌스, 표준화, 보안 | CMMI 기반 성숙도 심사 | Level 1 ~ Level 5 (성숙도 등급) |""",
        "sources": [
            "과학기술정보통신부·한국지능정보사회진흥원(NIA) - 데이터 품질인증 가이드라인",
            "데이터 산업진흥 및 이용촉진에 관한 기본법 (데이터산업법) 제20조",
            "ISO/IEC 25012: Data quality model & ISO/IEC 25024: Measurement of data quality"
        ]
    },

    "153_bcnf.md": {
        "insight": "모든 비자명 함수 종속성에서 결정자가 슈퍼키가 되도록 강제하여 3NF의 주속성 예외로 인한 갱신 이상을 원천 제거함.",
        "text_replacements": [
            ("$$X \\text{는 } R \\text{의 슈퍼키(Super Key)이다.}$$",
             "$$X \\text{는 } R \\text{의 슈퍼키(Super Key) 성립}$$"),
            ("| 한계 | 방안 |\n|---|---|\n| BCNF 분해는 무손실이어도 일부 함수 종속성의 국소 검사가 어려워짐 | 업무 제약의 보존 요구를 평가해 3NF·BCNF를 선택하고 분해 후 제약 검증 위치를 지정 |",
             "| 한계 | 방안 |\n|---|---|\n| BCNF 분해는 무손실이어도 일부 함수 종속성의 국소 검사가 어려워짐 | 업무 제약의 보존 요구를 평가해 3NF·BCNF를 선택하고 분해 후 제약 검증 위치를 지정 |\n| 테이블 분해로 인한 다중 조인 발생 및 질의 성능 저하 | 빈번한 조인 질의에 대해 물리적 비정규화 또는 머티리얼라이즈드 뷰 적용 검토 |")
        ],
        "rec_text": "결정자가 슈퍼키가 아닌 복합 후보키 릴레이션에 대해 BCNF 분해를 우선 검토하되, 함수 종속성 보존 손실이 발생할 경우 3NF 유지 및 트리거 기반 제약 검증을 병행 수립.",
        "rec_diagram": """```text
                 [ 릴레이션 R과 함수 종속성 집합 F ]
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
       [ 모든 X->Y의 X가 슈퍼키 ]     [ 일부 X->Y의 X가 슈퍼키 아님 ]
               │                               │
           [ BCNF 충족 ]             ┌─────────┴─────────┐
                                     ▼                   ▼
                               [ Y가 주속성 ]      [ Y가 비주속성 ]
                                     │                   │
                                [ 3NF 충족 ]        [ 3NF 위반 ]
                                (BCNF 분해 검토)     (2NF/3NF 분해)
```""",
        "rec_table": """| 정규형 | 주요 판정 기준 | 주속성 예외 허용 | 무손실 조인 보장 | 종속성 보존 보장 | 잔존 이상 현상 |
|---|---|---|---|---|---|
| **2NF** | 부분 함수 종속성 제거 | 불가 | 항상 가능 | 항상 가능 | 이행적 함수 종속 이상 |
| **3NF** | 이행적 함수 종속성 제거 | 허용 ($Y$가 주속성이면 허용) | 항상 가능 | 항상 가능 (합성 알고리즘) | 비후보키 결정자 갱신 이상 |
| **BCNF** | 모든 비자명 FD의 결정자가 슈퍼키 | 불허 (주속성 예외 배제) | 항상 가능 (분해 알고리즘) | 손실 가능 (일부 보존 불가) | 다치 종속(MVD) 이상 |""",
        "sources": [
            "Raymond F. Boyce, Donald D. Chamberlin - Using a Relational Model in High-level Query Languages",
            "Abraham Silberschatz et al. - Database System Concepts (Chapter 14: Relational Database Design)",
            "C.J. Date - An Introduction to Database Systems: Functional Dependencies and Normalization"
        ]
    },

    "154_bi.md": {
        "insight": "기업 내 분산된 데이터를 수집·통합하여 다차원 분석 모델과 시각화 대시보드를 제공함으로써 데이터 주도적 의사결정을 지원함.",
        "text_replacements": [],
        "rec_text": "기간계 OLTP의 부하를 차단하기 위해 실시간 ELT 파이프라인과 비즈니스 세맨틱 계층을 구축하고, 셀프서비스 BI 도구와 통합 거버넌스를 결합하여 전사 데이터 활용도 극대화.",
        "rec_diagram": """```text
[ 기간계 시스템 ] ──> [ ETL / ELT 파이프라인 ] ──> [ 전사 DW / 데이터 레이크 ]
  (OLTP DB, ERP)      (추출, 변환, 적재)             (통합 저장소)
                                                           │
                                                           ▼
[ 비즈니스 사용자 ] <── [ 셀프서비스 BI / 리포팅 ] <── [ 다차원 DM / Semantic Layer ]
  (경영진, 현업)        (Tableau, PowerBI)           (Star Schema, Mart)
```""",
        "rec_table": """| 발전 세대 | 주요 특징 및 아키텍처 | 데이터 처리 방식 | 사용자 계층 | 핵심 가치 및 지향점 |
|---|---|---|---|---|
| **전통적 BI (1세대)** | 중앙집중형 EDW, 정적 배치 리포트 | 야간 배치 ETL | IT 개발자 중심 | 과거 실적 집계 및 정형 보고 |
| **셀프서비스 BI (2세대)** | 데이터 마트, 인메모리 시각화 도구 | 실시간/준실시간 ELT | 현업 비즈니스 분석가 | 가설 검증, 탐색적 애드혹 분석 |
| **증강 분석 BI (3세대)** | AI/ML 기반 자동 인사이트 도출 | 스트리밍 + 통합 세맨틱 | 전사 임직원 (대중화) | 원인 자동 진단, 예측적 통찰 |""",
        "sources": [
            "Gartner Magic Quadrant for Analytics and Business Intelligence Platforms",
            "DAMA International - DAMA-DMBOK: Data Management Body of Knowledge (DW/BI)",
            "Kimball Group - The Data Warehouse Lifecycle Toolkit"
        ]
    },

    "155_sna.md": {
        "insight": "개체 간의 상호작용 관계를 네트워크 그래프로 모델링하고 중심성 지표와 군집 구조를 정량화하여 핵심 매개자와 영향력을 탐색함.",
        "text_replacements": [],
        "rec_text": "단순 연결 횟수뿐만 아니라 정보 유통의 길목 역할을 하는 매개 중심성과 권력자 연결 기반 고유벡터 중심성을 종합 평가하여 금융 사기 적발 및 타깃 마케팅에 적용.",
        "rec_diagram": """```text
      (Node A) ─── (Node B)
         │  \\       /  │
         │   (Node C)  │     <── Node C: 높은 매개 중심성 (Broker)
         │  /       \\  │
      (Node D) ─── (Node E) ─── (Node F) <── Node F: 주변부 노드
```""",
        "rec_table": """| 중심성 지표 | 수학적 핵심 개념 | 네트워크상 역할 및 해석 | 비즈니스 실무 활용 사례 |
|---|---|---|---|
| **연결 중심성 (Degree)** | 한 노드에 직접 연결된 간선 수 | 즉각적인 접촉력, 대중적 인기 | 인플루언서 발굴, 단순 허브 식별 |
| **매개 중심성 (Betweenness)** | 노드 간 최단 경로상 위치 빈도 | 정보 통제권, 네트워크 중개자(Broker) | 이상 자금 세탁 중계 계좌 추적 |
| **근접 중심성 (Closeness)** | 다른 모든 노드까지 최단 경로의 합의 역수 | 정보 전파의 신속성, 전파 효율성 | 감염병 확산 거점 모니터링 |
| **고유벡터 (Eigenvector)** | 연결된 이웃 노드들의 중심성 가중 합 | 영향력 있는 노드들과의 네트워크 파워 | 학술 피인용 영향력(PageRank) |""",
        "sources": [
            "Stanley Wasserman, Katherine Faust - Social Network Analysis: Methods and Applications",
            "Mark Newman - Networks: An Introduction (Oxford University Press)",
            "IEEE Transactions on Computational Social Systems: Centrality Metrics and Network Community Detection"
        ]
    },

    "156_data_migration.md": {
        "insight": "레거시 시스템의 데이터를 목표 아키텍처로 무중단 이행하기 위해 CDC 실시간 복제와 단계별 정합성 검증 및 롤백 체계를 확립함.",
        "text_replacements": [],
        "rec_text": "대량 초기 적재 후 CDC 기반 실시간 변경 데이터 캡처를 동기화하고, 체크섬 기반 전수 대사 검증과 즉시 롤백 가능한 컷오버 시나리오를 사전에 모의 훈련.",
        "rec_diagram": """```text
[ 소스 레거시 DB ] ──> [ 1단계: 초기 대량 적재 (Initial Load) ] ──> [ 타깃 신규 DB ]
       │                                                                  ▲
       │ 2단계: 변경분 실시간 캡처 (CDC)                                  │
       └──────────> [ 메시지 큐 (Kafka) ] ──> [ 실시간 동기화 엔진 ] ─────┘
                                                      │
                                                      ▼
[ 3단계: 정합성 실시간 검증 (Hash/Checksum) & 컷오버 스위칭 (DNS/LB) ]
```""",
        "rec_table": """| 이행 방식 | 작업 프로세스 특성 | 다운타임 (Downtime) | 리스크 및 복구 용이성 | 권장 적용 시나리오 |
|---|---|---|---|---|
| **빅뱅 이행 (Big Bang)** | 일괄 정지 후 야간 단시간 전수 이행 | 장시간 정지 필수 | 이행 실패 시 롤백 극난 | 소규모 DB, 다운타임 허용 시스템 |
| **단계적 이행 (Phased)** | 업무 모듈별 순차 이행 | 모듈별 부분 다운타임 | 연계 모듈 간 양방향 동기화 부담 | 대규모 모놀리식의 순차 전환 |
| **무중단 CDC 이행** | 초기 적재 + 로그 기반 변경 실시간 복제 | 수 초~수 분 (스위칭 시) | 검증 완료 후 즉시 전환, 리스크 최소 | 24x365 금융·이커머스 미션크리티컬 |""",
        "sources": [
            "The Open Group - TOGAF Series Guide: Data Architecture and Migration Planning",
            "DAMA International - DAMA-DMBOK Chapter 10: Data Integration and Interoperability",
            "Oracle Database 2-Day Data Migration Guide & GoldenGate Replication Best Practices"
        ]
    },

    "157_key.md": {
        "insight": "유일성과 최소성을 기반으로 튜플 식별과 엔터티 무결성 및 참조 무결성을 보장하는 관계형 데이터 모델의 핵심 논리 구조임.",
        "text_replacements": [],
        "rec_text": "기본키 선정 시 비즈니스 변경에 영향받지 않도록 인조/대리키 채택을 우선 검토하고, 후보키에 유니크 인덱스를 지정하여 데이터 무결성과 조인 성능을 동시 확보.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────┐
│ 슈퍼키 (Super Key, 유일성 보장 속성 집합)                 │
│   ┌────────────────────────────────────────────────┐   │
│   │ 후보키 (Candidate Key, 유일성 + 최소성 충족)    │   │
│   │   ┌───────────────────┐    ┌─────────────────┐ │   │
│   │   │ 기본키 (Primary)   │    │ 대체키 (Alt)    │ │   │
│   │   └─────────┬─────────┘    └─────────────────┘ │   │
│   └─────────────┼──────────────────────────────────┘   │
└─────────────────┼──────────────────────────────────────┘
                  │ 참조 (FK)
                  ▼
          ┌───────────────┐
          │ 외래키 (FK)    │ (자식 테이블)
          └───────────────┘
```""",
        "rec_table": """| 키 분류 | 정의 및 제약 조건 | 유일성 (Uniqueness) | 최소성 (Minimality) | Null 허용 여부 | 주 역할 및 제약 |
|---|---|---|---|---|---|
| **슈퍼키 (Super Key)** | 튜플을 식별 가능한 속성 집합 | 만족 | 불만족 가능 | 허용 가능 | 튜플 유일 식별의 상위 개념 |
| **후보키 (Candidate)** | 슈퍼키 중 불필요한 속성 제거 | 만족 | 반드시 만족 | 원칙적 불허 | 기본키 후보군 형성 |
| **기본키 (Primary Key)** | 대표로 선정된 단 하나의 식별자 | 만족 | 반드시 만족 | 절대 불허 (엔터티 무결성) | 튜플의 물리/논리 식별 기준 |
| **대체키 (Alternate)** | 후보키 중 기본키로 미선정된 키 | 만족 | 반드시 만족 | 제약에 따라 상이 | 보조 유니크 인덱스 생성 |
| **외래키 (Foreign Key)** | 부모 릴레이션의 기본키 참조 | 부모 키 속성에 따름 | 부모 키 속성에 따름 | 비식별 관계 시 허용 | 참조 무결성 제약 보장 |""",
        "sources": [
            "E.F. Codd - A Relational Model of Data for Large Shared Data Banks (ACM)",
            "ISO/IEC 9075: Information technology - Database languages - SQL: Integrity Constraints",
            "Abraham Silberschatz et al. - Database System Concepts: Keys and Relational Integrity"
        ]
    },

    "158_process_mining.md": {
        "insight": "정보시스템의 이벤트 로그를 추출·분석하여 실제 비즈니스 프로세스 모델을 자동으로 발견하고 표준 준수 여부와 병목을 진단함.",
        "text_replacements": [],
        "rec_text": "이벤트 로그 추출 시 케이스 ID, 활동명, 타임스탬프 3대 필수 속성의 무결성을 사전에 확보하고, 프로세스 발견 및 적합도 진단을 병행하여 지속적 개선 체계(PI) 정착.",
        "rec_diagram": """```text
[ 이벤트 로그 (Event Log) ]
  (Case ID, Activity, Timestamp)
             │
   ┌─────────┼─────────────────────────┐
   ▼         ▼                         ▼
[ 발견 (Discovery) ]   [ 적합도 검사 (Conformance) ]   [ 향상 (Enhancement) ]
(실제 프로세스 도출)    (표준 모델과 괴리/병목 진단)   (재설계 및 병목 해소)
   │         │                         │
   └─────────┴────────────┬────────────┘
                          ▼
             [ 비즈니스 프로세스 최적화 ]
```""",
        "rec_table": """| 프로세스 마이닝 유형 | 입력 데이터 | 핵심 목적 | 분석 알고리즘 및 기법 | 실무 적용 효과 |
|---|---|---|---|---|
| **발견 (Discovery)** | 순수 이벤트 로그 | 실제 수행 프로세스 모델 생성 | Alpha Miner, Heuristics Miner, Inductive | 숨겨진 비공식 우회 경로 가시화 |
| **적합도 검사 (Conformance)** | 이벤트 로그 + 사전문서 모델 | 표준 프로세스 준수/이탈 측정 | Token Replay, Alignment 기술 | 감사 규정 위반 및 컴플라이언스 진단 |
| **향상 (Enhancement)** | 이벤트 로그 + 기존 모델 | 기존 모델의 보강 및 병목 해소 | 병목 소요시간 분석, 소셜 네트워크 | 대기시간 단축 및 프로세스 리엔지니어링 |""",
        "sources": [
            "Wil van der Aalst - Process Mining: Data Science in Action (Springer)",
            "IEEE Task Force on Process Mining - Process Mining Manifesto",
            "Celonis & Disco Academic Process Analytics Benchmarks"
        ]
    },

    "159_functional_dependency.md": {
        "insight": "업무 규칙 기반의 함수 종속성을 체계적으로 식별하고 무손실 분해와 종속성 보존을 동시에 검증하여 정규화 품질을 극대화함.",
        "text_replacements": [],
        "rec_text": "엔터티 속성 간의 결정자-종속자 관계를 도출할 때 암스트롱 공리를 적용하여 최소 종속성 커버를 산출하고, 2NF~BCNF 정규화 과정에서 무손실 조인과 종속성 보존을 함께 관리.",
        "rec_diagram": """```text
[ 기본 공리군 (Sound & Complete) ]
  1. 반사 규칙 (Reflexivity)  : Y ⊆ X  => X → Y
  2. 첨가 규칙 (Augmentation)  : X → Y  => XZ → YZ
  3. 이행 규칙 (Transitivity)  : X → Y & Y → Z => X → Z
               │
               ▼ (유도 공리군 확장)
  4. 분해 규칙 (Decomposition): X → YZ => X → Y, X → Z
  5. 결합 규칙 (Union)        : X → Y & X → Z => X → YZ
  6. 의사이행 (Pseudo-trans)  : X → Y & WY → Z => WX → Z
```""",
        "rec_table": """| 함수 종속성 유형 | 관계 표현식 | 정의 및 특징 | 위배 시 발생하는 문제 | 대응 정규형 |
|---|---|---|---|---|
| **완전 함수 종속 (FFD)** | $X \\rightarrow Y$ (어떤 $X' \\subset X$도 $X' \\rightarrow Y$ 불가) | 복합 기본키 전체에 의해서만 종속 | 일부 키 변경 시 데이터 불일치 | 2NF |
| **부분 함수 종속 (PFD)** | $X \\rightarrow Y$ ($X' \\subset X$인 $X'$에 대해 $X' \\rightarrow Y$ 성립) | 복합키의 일부 속성에 의해 종속 | 튜플 중복 적재 및 갱신 이상 | 2NF 분해 대상 |
| **이행적 함수 종속 (TFD)** | $X \\rightarrow Y \\land Y \\rightarrow Z \\implies X \\rightarrow Z$ | 비주요 속성을 거쳐 간접적으로 종속 | 변경 시 연쇄 갱신 누락 | 3NF 분해 대상 |
| **결정자 함수 종속** | $X \\rightarrow Y$ ($X$가 슈퍼키가 아님) | 비후보키가 다른 주속성을 결정 | 3NF 만족 후에도 중복 잔존 | BCNF 분해 대상 |""",
        "sources": [
            "William W. Armstrong - Dependency Structures of Data Base Relationships (IFIP Congress)",
            "Abraham Silberschatz et al. - Database System Concepts: Functional Dependencies",
            "C.J. Date - An Introduction to Database Systems: Relational Decomposition Algorithms"
        ]
    },

    "160_mmdbms.md": {
        "insight": "데이터 전체를 메인 메모리에 상주시켜 디스크 I/O 병목을 제거하고 고속 T-Tree 인덱스와 비동기 로깅으로 초저지연 트랜잭션을 실현함.",
        "text_replacements": [],
        "rec_text": "전력 장애로 인한 휘발성 데이터 유실을 방지하기 위해 NVRAM과 고속 SSD를 활용한 WAL 로깅 및 체크포인트 주기를 정밀 설계하고, T-Tree 기반 색인 효율을 극대화.",
        "rec_diagram": """```text
[ 애플리케이션 ]
      │ 초고속 트랜잭션 (In-Memory Access)
      ▼
┌─────────────────────────────────────────────────────┐
│ [ 메인 메모리 (DRAM) ]                               │
│   - 데이터베이스 버퍼 풀 (전체 데이터 상주)           │
│   - 메모리 전용 인덱스 (T-Tree, Hash Index)        │
│   - 로그 버퍼 (Log Buffer)                          │
└──────────────┬──────────────────────┬───────────────┘
               │ Checkpoint (주기적)   │ Flush (WAL 로그)
               ▼                      ▼
┌─────────────────────────────────────────────────────┐
│ [ 영속 저장소 (SSD / NVRAM) ]                       │
│   - 체크포인트 스냅샷 이미지                        │
│   - 트랜잭션 로그 파일 (Redo Log)                   │
└─────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 항목 | 메인 메모리 DBMS (MMDBMS) | 디스크 기반 DBMS (Disk DBMS) | 인메모리 분산 캐시 (Redis) |
|---|---|---|---|
| **기본 저장 위치** | DRAM (전체 데이터 메모리 상주) | 자기 디스크 / SSD 블록 | DRAM (키-값 구조) |
| **트랜잭션 지연 (Latency)**| 마이크로초 ($\mu s$) 단위 | 밀리초 ($ms$) 단위 (I/O 병목) | 서브 밀리초 ($ms$) 단위 |
| **대표 인덱스 구조** | T-Tree, Pointer 기반 해시 | B-Tree, B+Tree (블록 단위) | SkipList, Hash Table |
| **ACID 및 영속성** | 완전 지원 (로그 및 체크포인트) | 완전 지원 (WAL, Doublewrite) | 제한적 (RDB 스냅샷, AOF 옵션) |
| **주요 적용 분야** | 통신 과금, 증권 HTS, 실시간 빌링 | 기간계 ERP, 대규모 EDW | 웹 세션 관리, 캐싱 계층 |""",
        "sources": [
            "Hector Garcia-Molina, Kenneth Salem - Main Memory Database Systems: An Overview (IEEE TKDE)",
            "Tobin J. Lehman, Michael J. Carey - A Study of Index Structures for Main Memory Database Management Systems",
            "Oracle TimesTen In-Memory Database Architecture Guide"
        ]
    },

    "161_molap.md": {
        "insight": "다차원 배열 큐브에 사전 계산된 집계 데이터를 적재하여 고정된 다차원 질의에 대해 초고속 응답을 제공하는 분석 아키텍처임.",
        "text_replacements": [
            ("- 본질: **MOLAP은** 분석 데이터를 다차원 큐브에 저장·집계해 질의하는 OLAP 방식이다.",
             "- 본질: **MOLAP은** 분석 데이터를 다차원 큐브에 사전 저장·집계해 초고속 다차원 질의를 수행하는 OLAP 방식")
        ],
        "rec_text": "질의 응답 속도가 핵심인 정형 경영 리포팅에는 MOLAP 다차원 큐브를 활용하고, 차원 수가 많아 큐브 폭발(Cube Explosion)이 우려되는 대용량 데이터는 ROLAP/HOLAP으로 상호 보완.",
        "rec_diagram": """```text
           [ 다차원 큐브 (3D Cube) ]
              기간 (Time)
               /
              ┌─────────┐
             /         /│
            ┌─────────┐ │
            │ 매출액  │ │ ──> [ Slicing ]: 2026년 단일 슬라이스 추출
            │         │/      [ Dicing  ]: (서울, 스마트폰, 1Q) 부분 큐브
            └─────────┘       [ Roll-up ]: 일별 -> 월별 -> 분기별 집계
             지역 ─── 제품    [ Drill-down ]: 연도별 -> 월별 세분화
```""",
        "rec_table": """| 비교 축 | MOLAP (Multidimensional) | ROLAP (Relational) | HOLAP (Hybrid) |
|---|---|---|---|
| **데이터 저장 방식** | 전용 다차원 배열 큐브 (MDDB) | 관계형 테이블 (스타/눈꽃 스키마) | 요약은 MDDB, 세부는 RDBMS |
| **질의 응답 속도** | 매우 빠름 (사전 집계 큐브 참조) | 보통~느림 (대량 조인 수행 필요) | 빠름 (계층별 분기 질의) |
| **확장성 및 용량 한계**| 낮음 (희소 큐브, 용량 폭발 리스크) | 매우 높음 (테라바이트 이상 지원) | 우수 (절충형 설계) |
| **초기 데이터 적재** | 사전 집계로 인한 긴 적재 시간 | 단순 적재로 적재 시간 빠름 | 중간 수준 |
| **주요 사용 사례** | 고정 지표의 경영진 임원 대시보드 | 유연한 대규모 상세 트랜잭션 분석 | 대규모 전사 다차원 BI 분석 |""",
        "sources": [
            "E.F. Codd, S.B. Codd, C.T. Salley - Providing OLAP to User-Analysts: An IT Mandate",
            "Ralph Kimball - The Data Warehouse Toolkit: Practical Techniques for Dimensional Modeling",
            "Microsoft Analysis Services (SSAS) Multidimensional & Tabular Architecture Guide"
        ]
    },

    "163_point_vs_interval_estimation.md": {
        "insight": "표본 통계량 기반의 단일 대표값 추정인 점추정과 표본 오차를 반영하여 모수 포함 범위를 제시하는 구간추정을 상호 보완하여 활용함.",
        "text_replacements": [],
        "rec_text": "점추정량 선정 시 불편성과 최소 분산을 갖는 최량불편추정량(MVUE)을 채택하고, 표본오차와 신뢰수준($1-\\alpha$)을 수반하는 신뢰구간을 함께 보고하여 통계적 신뢰성을 확보.",
        "rec_diagram": """```text
                     표본 평균 (X̄, 점추정값)
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
   [ 하한값 (Lower Bound) ]          [ 상한값 (Upper Bound) ]
    X̄ - z*(σ/√n)                     X̄ + z*(σ/√n)
    ├─────────────────────────────────┤
    │◄────── 95% 신뢰구간 (CI) ──────►│
    
    * 해석: 동일 방식으로 무한 반복 표집 시 구성되는 신뢰구간 중 95%가 실제 모평균(μ)을 포함함
```""",
        "rec_table": """| 비교 항목 | 점추정 (Point Estimation) | 구간추정 (Interval Estimation) |
|---|---|---|
| **정의** | 모수 값 하나를 단일 수치로 직접 추정 | 모수가 포함될 가능성이 높은 구간 범위를 추정 |
| **산출 결과물** | 단일 점 (예: $\\hat{\\mu} = \\bar{X}$) | 신뢰구간 (Lower Limit $\\sim$ Upper Limit) |
| **표본오차 반영** | 표본 변동성 및 불확실성 미반영 | 오차 한계($z \\cdot \\frac{\\sigma}{\\sqrt{n}}$)를 반영하여 범위화 |
| **평가 기준** | 불편성, 효율성, 일치성, 충분성 | 신뢰수준($1-\\alpha$), 구간의 협소성(정밀도) |
| **실무적 한계** | 단일 추정값이 참 모수와 정확히 일치할 확률 0 | 구간 폭이 넓어질 경우 의사결정 모호성 증가 |""",
        "sources": [
            "ISO 3534-1: Statistics - Terms and symbols: Statistical estimation",
            "NIST/SEMATECH e-Handbook of Statistical Methods: Point and Interval Estimation",
            "George Casella, Roger L. Berger - Statistical Inference (Duxbury Press)"
        ]
    }
}

for fname, d in DATA.items():
    fpath = TARGET_DIR / fname
    if not fpath.exists():
        print(f"Error: {fname} does not exist!")
        continue
    content = fpath.read_text(encoding="utf-8")
    
    # 1. Frontmatter fixes
    content = re.sub(r'model:\s*"[^"]*"', 'model: "Gemini 3.8 Flash"', content)
    content = re.sub(r'author:\s*"[^"]*"', 'author: "Antigravity"', content)
    
    # Remove '컴퓨터시스템응용' mentions
    content = re.sub(r'제\d+회\s*컴퓨터시스템응용[^\n]*\n?', '', content)
    content = re.sub(r'컴퓨터시스템응용[^\n]*\n?', '', content)
    
    # 2. Fix 30초 인출
    # If 159, remove the table before 30s bullets
    if fname == "159_functional_dependency.md":
        content = re.sub(r'## 30초 인출\s*\n\s*\|[^\n]+\|\s*\n\s*\|[^\n]+\|\s*\n(\s*\|[^\n]+\|\s*\n)+', '## 30초 인출\n\n', content)

    # Replace insight line
    content = re.sub(
        r'- 통찰:[^\n]*',
        f"- 통찰: {d['insight']}",
        content
    )
    
    # 3. Text replacements (fixing bad endings, updating diagrams if needed)
    for old_txt, new_txt in d["text_replacements"]:
        if old_txt in content:
            content = content.replace(old_txt, new_txt)
        else:
            print(f"Warning: replacement target not found in {fname}: {old_txt[:40]}...")
            
    # 4. Replace Section VI, sources, and linked topics
    # We find where Section VI starts
    vi_match = re.search(r'## Ⅵ\.[^\n]*', content)
    if not vi_match:
        print(f"Error: Section VI not found in {fname}")
        continue
        
    pre_vi = content[:vi_match.start()].rstrip()
    
    # Extract linked topics from original if present
    linked_match = re.search(r'## 연결 토픽\s*\n(.*)$', content, re.DOTALL)
    if linked_match:
        linked_topics = linked_match.group(1).strip()
    else:
        linked_topics = "- 상위 토픽: [데이터베이스 일반](./001_database.md)"
        
    # Build clean sources
    sources_text = "\n".join([f"- {s}" for s in d["sources"]])
    
    # Build Section VI
    new_vi = f"""## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
{d['rec_text']}

### 2. 아키텍처 및 상세 메커니즘
{d['rec_diagram']}

### 3. 기술 유형 및 비교 평가
{d['rec_table']}

## 출제 이력과 검증 출처

{sources_text}

## 연결 토픽

{linked_topics}
"""
    
    final_content = pre_vi + "\n\n" + new_vi
    fpath.write_text(final_content, encoding="utf-8")
    print(f"Rewritten {fname}")
