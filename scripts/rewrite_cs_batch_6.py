import os
import re
from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

DATA = {
    "104_system_semiconductor_ecosystem.md": {
        "insight": "팹리스, 디자인하우스, 파운드리, OSAT로 고도화 분업화된 글로벌 협력 가치사슬을 통해 고성능 시스템 반도체 혁신을 가속화함.",
        "text_replacements": [
            ("가설계는 단일 행사가 아니라 전환 준비·리허설·본이행·초기 안정화의 단계별 진입·종료 조건을 통제하는 운영 체계다.",
             "가설계는 단일 이벤트가 아니라 전환 준비, 리허설, 본이행, 초기 안정화의 단계별 진입 및 종료 조건을 통제하는 종합 운영 체계임.")
        ],
        "rec_text": "초미세 공정 비용을 절감하기 위해 검증된 표준 칩렛(UCIe) 생태계를 구축하고, 파운드리-디자인하우스 원팀 체계로 공정 설계 키트(PDK) 최적화 필수.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 시스템 반도체 4대 핵심 분업 가치사슬 및 인터페이스 ]                 │
│                                                                        │
│   [ 팹리스 (Fabless) ] ──(RTL/GDSII 설계 도면)──> [ 디자인 하우스 ]    │
│    - 알고리즘 및 칩 아키텍처 설계                  - 물리 레이아웃 최적화│
│                                                          │             │
│                                                          ▼             │
│   [ OSAT (패키징 & 테스트) ] <──(가공된 웨이퍼 인도)── [ 파운드리 (Foundry) ]│
│    - 2.5D/3D 첨단 패키징                           - EUV 초미세 공정 생산│
│    - 전기적/신뢰성 최종 검사                        (2nm/3nm Gate-All-Around)│
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 가치사슬 주체 | 핵심 역량 | 대표 글로벌 기업 | 국내 산업 생태계 현주소 |
|---|---|---|---|
| **반도체 IP 기업** | 표준 인터페이스 및 연산 코어 회로 자산 | ARM, Synopsys, Cadence | 서드파티 라이선스 의존도 높음 |
| **팹리스 (Fabless)** | AI/통신/그래픽 전용 프로세서 아키텍처 | NVIDIA, Qualcomm, Apple | 스타트업 중심 NPU 성장 중 |
| **파운드리 (Foundry)**| 나노미터급 웨이퍼 대량 제조 및 수율 관리 | TSMC, 삼성전자, Intel | 대규모 설비투자 경쟁 심화 |
| **OSAT (패키징)** | 칩렛 통합, CoWoS, 인터포저 첨단 패키징 | ASE, Amkor, JCET | 차세대 어드밴스드 패키징 육성 시급 |""",
        "sources": [
            "Semiconductor Industry Association (SIA) Beyond Borders Report",
            "IEEE Micro: The Global Semiconductor Value Chain and Advanced Packaging",
            "산업통상자원부: 시스템 반도체 생태계 강화 및 파운드리 육성 전략"
        ],
        "connections": "- 상위 토픽: [100 비메모리 반도체](./100_non_memory_semiconductor.md)\n- 연관 토픽: [030 칩렛 UCIe](./030_chiplet_ucie_3_0.md), [097 메모리 반도체](./097_memory_semiconductor.md)"
    },

    "105_endian.md": {
        "insight": "연속된 다중 바이트 데이터를 메모리에 배열하는 순서 규약으로, 최하위 바이트 우선의 리틀 엔디안과 최상위 바이트 우선의 빅 엔디안으로 양분됨.",
        "text_replacements": [],
        "rec_text": "네트워크 통신 프로토콜 설계 시 표준 네트워크 바이트 순서(빅 엔디안)를 명시하고, 직렬화/역직렬화 계층에서 아키텍처 중립적인 프로토콜 버퍼(Protobuf) 채택.",
        "rec_diagram": """```text
[ 32비트 데이터: 0x1A2B3C4D (MSB=0x1A, LSB=0x4D) 메모리 배치 비교 ]

  주소 번지 :   0x00       0x01       0x02       0x03
               ┌──────────┬──────────┬──────────┬──────────┐
  빅 엔디안  : │   0x1A   │   0x2B   │   0x3C   │   0x4D   │ (MSB -> LSB)
               └──────────┴──────────┴──────────┴──────────┘
                * 네트워크 전송 표준 (TCP/IP 헤더)

               ┌──────────┬──────────┬──────────┬──────────┐
  리틀 엔디안: │   0x4D   │   0x3C   │   0x2B   │   0x1A   │ (LSB -> MSB)
               └──────────┴──────────┴──────────┴──────────┘
                * x86/x64, 최신 스마트폰 ARM 프로세서 표준
```""",
        "rec_table": """| 비교 항목 | 빅 엔디안 (Big-Endian) | 리틀 엔디안 (Little-Endian) |
|---|---|---|
| **바이트 정렬 기준** | 최상위 바이트(MSB)를 가장 낮은 메모리 주소에 저장 | 최하위 바이트(LSB)를 가장 낮은 메모리 주소에 저장 |
| **네트워크 표준** | **TCP/IP 표준 (Network Byte Order: RFC 791)** | 호스트 전용 바이트 순서 (Host Byte Order) |
| **산술 연산 효율** | 캐리(Carry) 전파 시 상위 바이트까지 이동 필요 | 하위 바이트부터 즉시 덧셈/올림수 연산 가능 |
| **적용 프로세서** | 메인프레임, SPARC, 네트워크 라우터 | Intel x86, AMD64, ARM(LE 모드), RISC-V |""",
        "sources": [
            "Danny Cohen - On Holy Wars and a Plea for Peace (IEN 137)",
            "IETF RFC 791: Internet Protocol Specification",
            "Computer Systems: A Programmer's Perspective (CS:APP) - Byte Ordering"
        ],
        "connections": "- 상위 토픽: [093 리틀 엔디안](./093_little_endian.md)\n- 연관 토픽: [101 빅 엔디안](./101_big_endian.md), [076 CPU](./076_cpu.md)"
    },

    "106_migration_fault_management.md": {
        "insight": "레거시에서 타깃 시스템으로의 데이터 이행 시 무결성 결함을 방지하기 위해 단계별 정합성 검증과 비상 롤백 및 종합 상황 통제 체계를 구축함.",
        "text_replacements": [
            ("가설계는 단일 행사가 아니라 전환 준비·리허설·본이행·초기 안정화의 단계별 진입·종료 조건을 통제하는 운영 체계다.",
             "가설계는 단일 이벤트가 아니라 전환 준비, 리허설, 본이행, 초기 안정화의 단계별 진입 및 종료 조건을 통제하는 종합 운영 체계임.")
        ],
        "rec_text": "본이행 전 최소 3회 이상의 전수 모의훈련(Dry-Run)을 수행하고, 체크섬 해시 기반의 자동 정합성 대사 도구와 시간대별 롤백 판정 기준(No-Go 데드라인) 수립.",
        "rec_diagram": """```text
[ 데이터 마이그레이션 장애 관리 및 단계별 롤백 통제 체계 ]

 [ 1단계: 전환 사전 검증 ] ──> [ 2단계: 본 이행 수행 ] ──> [ 3단계: 정합성 실시간 대사 ]
   - 리허설 결과 분석            - CDC 복제 정지/반영        - Row Count & Hash Checksum
   - 롤백 시나리오 확정          - 타깃 시스템 기동          - 불일치 발생 시 원인 분석
                                                                     │
                                                                     ▼
 [ 정상 서비스 오픈 ] <──(Yes)── [ 최종 Go / No-Go 판정 회의 (데드라인 시간 전) ]
                                 │
                                 └──(No: 치명적 정합성 오류)──> [ 즉각적 롤백 선언 ]
                                                                 (레거시 원장 재기동)
```""",
        "rec_table": """| 관리 단계 | 핵심 통제 활동 | 장애 발생 시 대응 방안 |
|---|---|---|
| **이행 준비 단계** | 이행 시나리오 수립, 전수 모의훈련(Dry-run) 3회 | 소요 시간 지연 시 이행 스크립트 병렬화 튜닝 |
| **본 이행 단계** | 레거시 데이터 덤프, 네트워크 전송, 타깃 적재 | 네트워크 단절 시 다중 회선 절체, 체크포인트 재시작 |
| **검증 및 판정** | 테이블 건수, 주요 원장 합계, 해시 체크섬 대사 | 불일치 건수 허용치 초과 시 즉시 No-Go 및 롤백 |
| **안정화 단계** | 결제/조회 핵심 트랜잭션 집중 모니터링 | 비상 핫픽스 패치 배포 및 데이터 수동 보정 |""",
        "sources": [
            "한국지능정보사회진흥원(NIA) 정보시스템 마이그레이션 및 이행 관리 가이드라인",
            "The Open Group TOGAF: Implementation and Migration Planning",
            "Project Management Institute (PMI) Standard for Risk Management"
        ],
        "connections": "- 상위 토픽: [047 시스템 장애 예방 및 컷오버](./047_system_failure_prevention_cutover.md)\n- 연관 토픽: [021 HA](./021_ha.md), [042 HA 가용성 보장](./042_ha_availability_assurance.md)"
    },

    "107_workflow_scheduling_backfill.md": {
        "insight": "DAG 기반 복합 태스크 의존성을 조정하는 워크플로우 엔진에서 후순위 단기 작업을 선두 예약 작업의 여유 슬롯에 선별 배치하여 클러스터 가동률을 극대화함.",
        "text_replacements": [
            ("태스크 완료 상태는 성공·실패뿐 아니라 타임아웃, 외부 취소, 부분 완료를 포함한다. 의존 관계는 데이터 준비, 선행 태스크 종료, 승인 이벤트처럼 조건별로 전이 규칙을 정한다.",
             "태스크 완료 상태는 성공, 실패뿐 아니라 타임아웃, 외부 취소, 부분 완료를 포괄. 의존 관계는 데이터 스테이징, 선행 작업 종료, 승인 이벤트 등 조건별 상태 전이 규칙 수립.")
        ],
        "rec_text": "DAG 의존 관계에서 실패한 특정 태스크만 선별 재실행하는 클리어(Clear) 기능을 활용하고, 슬롯 낭비를 방지하기 위해 작업 예상 시간을 기반으로 백필링 스케줄링 결합.",
        "rec_diagram": """```text
[ 비순환 방향 그래프 (DAG) 워크플로우 의존성 ]
      [ Task A (데이터 수집) ]
             │
      ┌──────┴──────┐
      ▼             ▼
  [ Task B ]    [ Task C ]
  (변환/정제)    (외부 API)
      │             │
      └──────┬──────┘
             ▼
      [ Task D (최종 적재) ]

[ 백필링(Backfilling) 결합 실행 ]
  노드 1 │ [ Task A ] ───> [ Task D (노드 1, 2 전체 예약) ]
  노드 2 │ [ 빈 슬롯 (Hole) ] ────> [ Task D ]  <── 노드 2 유휴 발생!
         └──────────────────────────────────────
          * 단기 Task C가 섀도우 타임 전에 끝난다면 빈 슬롯에 백필 즉시 투입!
```""",
        "rec_table": """| 워크플로우 관리 엔진 | 아키텍처 특성 | 동적 백필 지원 여부 | 주 활용 도메인 |
|---|---|---|---|
| **Apache Airflow** | 파이썬 코드 기반 선언적 DAG, 중앙 스케줄러 | 지원 (과거 데이터 백필 CLI) | 전사 데이터 파이프라인, ETL 오케스트레이션 |
| **Argo Workflows** | 쿠버네티스 CRD 네이티브, 컨테이너 기반 실행 | K8s Pod 스케줄러 위임 | 클라우드 네이티브 CI/CD, MLOps 파이프라인 |
| **SLURM Workload Mgr**| HPC 전용 고성능 큐 스케줄러 | 완벽 지원 (EASY / Conservative) | 슈퍼컴퓨팅 분산 병렬 연산, 대규모 AI 학습 |""",
        "sources": [
            "Apache Airflow Documentation: DAGs and Backfilling Concepts",
            "Slurm Workload Manager Architecture: Backfill Scheduling Plugin",
            "IEEE Transactions on Parallel and Distributed Systems: Scientific Workflow Scheduling"
        ],
        "connections": "- 상위 토픽: [099 백필](./099_backfill.md)\n- 연관 토픽: [019 CPU 스케줄링](./019_cpu_scheduling.md), [074 유전 알고리즘](./074_genetic_algorithm.md)"
    },

    "108_cloud_infrastructure_architecture.md": {
        "insight": "컴퓨팅, 스토리지, 네트워크 자원을 소프트웨어 정의 기술(SDDC)로 가상화하고 리전 및 가용영역(AZ) 단위로 격리 배치하여 고가용성을 달성함.",
        "text_replacements": [],
        "rec_text": "단일 데이터센터 물리 장애에 대비하여 복수의 가용영역(Multi-AZ)에 걸쳐 워크로드를 분산 배치하고, 인프라 계층 전반에 무신뢰(Zero Trust) 네트워크 세그멘테이션 수립.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 엔터프라이즈 클라우드 인프라 아키텍처 (Cloud Region Architecture) ] │
│                                                                        │
│ [ 클라우드 리전 (Cloud Region) : 지리적 독립 영역 ]                    │
│                                                                        │
│   ┌───────────────────────────┐      ┌───────────────────────────┐     │
│   │ [ 가용영역 1 (AZ-a) ]     │      │ [ 가용영역 2 (AZ-b) ]     │     │
│   │  - 독립 전산실, 독립 전력 │      │  - 독립 전산실, 독립 전력 │     │
│   │  - Public Subnet (L4/L7)  │      │  - Public Subnet (L4/L7)  │     │
│   │  - Private Subnet (App/DB)│      │  - Private Subnet (App/DB)│     │
│   └─────────────┬─────────────┘      └─────────────┬─────────────┘     │
│                 │                                  │                   │
│                 └────────── 초고속 전용 광패브릭 ──┘                   │
│                            (지연 시간 < 1ms, 완벽한 동기 복제 지원)    │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 인프라 계층 | 소프트웨어 정의 기술 (SDx) | 핵심 역할 및 기능 |
|---|---|---|
| **소프트웨어 정의 컴퓨팅 (SDC)**| KVM, VMware ESXi, Nitro Hypervisor | 물리 CPU/메모리를 가상머신 및 컨테이너로 추상화 |
| **소프트웨어 정의 스토리지 (SDS)**| Ceph, vSAN, AWS EBS | 분산 상용 디스크를 묶어 고성능 탄력적 블록/객체 풀 제공 |
| **소프트웨어 정의 네트워킹 (SDN)**| OpenFlow, OVS, AWS VPC, Calico | 오버레이 터널링(VXLAN) 기반 가상 격리 네트워크망 구축 |""",
        "sources": [
            "NIST Special Publication 800-145: Cloud Infrastructure Architecture",
            "AWS Well-Architected Framework: Reliability and Performance Efficiency",
            "The Open Group: Cloud Ecosystem Reference Technologies"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [054 IaaS](./054_iaas.md), [021 HA](./021_ha.md)"
    },

    "109_cloud_computing_service_models.md": {
        "insight": "고객과 클라우드 서비스 공급자 간의 관리 및 책임 영역 경계에 따라 IaaS, PaaS, SaaS로 계층화하여 맞춤형 IT 자원을 제공하는 서비스 분류 체계임.",
        "text_replacements": [],
        "rec_text": "공유 책임 모델(Shared Responsibility Model)에 따라 침해사고 대응 및 데이터 거버넌스 주체를 사전 식별하고, 비즈니스 특성에 맞춘 최적의 서비스 모델 선택.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 클라우드 3대 서비스 모델 책임 계층도 ]                              │
│                                                                        │
│   스택 계층        │ 온프레미스 │   IaaS   │   PaaS   │   SaaS         │
│  ──────────────────┼────────────┼──────────┼──────────┼──────────      │
│   데이터 및 접근   │   고객     │   고객   │   고객   │   고객         │
│   애플리케이션     │   고객     │   고객   │   고객   │   CSP          │
│   런타임/미들웨어  │   고객     │   고객   │   CSP    │   CSP          │
│   운영체제 (OS)    │   고객     │   고객   │   CSP    │   CSP          │
│   가상화 계층      │   고객     │   CSP    │   CSP    │   CSP          │
│   서버/스토리지    │   고객     │   CSP    │   CSP    │   CSP          │
│   물리 전산망      │   고객     │   CSP    │   CSP    │   CSP          │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 서비스 모델 | 핵심 통제 영역 (고객 관점) | 주요 가치 및 효용 | 대표 솔루션 예시 |
|---|---|---|---|
| **IaaS** | OS 선택, 커널 파라미터, 네트워크 방화벽, 전체 앱 | 최대의 시스템 제어권과 인프라 유연성 | AWS EC2, GCP Compute Engine |
| **PaaS** | 비즈니스 애플리케이션 코드, DB 스키마 | 개발 생산성 극대화 및 운영 자동화 | Heroku, Google App Engine, EKS |
| **SaaS** | 사용자 계정, 접근 권한, 데이터 관리 | 별도 설치 없는 즉시 업무 활용 | Microsoft 365, Salesforce, Slack |""",
        "sources": [
            "NIST Special Publication 800-145: Cloud Computing Service Models",
            "ISO/IEC 17788: Overview and Vocabulary of Cloud Computing",
            "Cloud Security Alliance (CSA): Security Guidance v4.0"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [054 IaaS](./054_iaas.md), [055 PaaS](./055_paas.md), [036 SaaS](./036_saas.md)"
    },

    "110_csp_risk_management.md": {
        "insight": "클라우드 서비스 공급자의 서비스 중단, 데이터 유실, 벤더 종속, 규제 위반 등 외부 아웃소싱에 따른 3자 위험을 종합 평가하고 통제하는 리스크 관리 체계임.",
        "text_replacements": [],
        "rec_text": "CSP의 단일 리전 장애 및 도산 리스크에 대비하여 계약서 내 출구 전략(Exit Strategy)과 데이터 이전 권리를 명시하고, 주기적인 BCP/DR 모의훈련 의무화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ CSP 제3자 위험 관리 (Third-Party Cloud Risk Management) 생명주기 ]   │
│                                                                        │
│ [ 1. 계약 전 실사 ] ──> [ 2. 계약 및 SLA ] ──> [ 3. 지속적 관제 ] ──> [ 4. 출구 전략 ]
│  - 재무 건전성 평가      - SLA 99.99% 보장     - CSPM 설정 감사      - 데이터 반환 보장
│  - 보안 인증 검증        - 위약금/배상 한도    - 가용성 실시간 측정  - 타 CSP 이전 계획
│   (SOC2, CSAP)           - 감사 수검 권한      - 접근 권한 정기 회수 - 백업 데이터 검증
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 주요 CSP 리스크 | 위험 내용 및 파급 효과 | 완화 및 통제 방안 |
|---|---|---|
| **서비스 가용성 중단** | CSP 데이터센터 화재/정전으로 인한 전면 서비스 마비 | 멀티 리전 액티브-액티브 DR 및 멀티 클라우드 분산 |
| **벤더 종속 (Vendor Lock-in)**| CSP 독점 기술 의존으로 타 플랫폼 이전 비용 폭증 | 컨테이너 표준화(K8s), 오픈소스 기술 및 IaC 코드화 |
| **데이터 주권 및 법적 규제** | 해외 정부 영장에 의한 데이터 열람 및 국외 반출 | 클라우드 보안인증(CSAP) 준수, 고객 관리 키(HYOK) 암호화 |
| **숨겨진 비용 폭증** | 데이터 이그레스(Egress) 및 API 호출 비용 통제 실패 | FinOps 모니터링, 예산 초과 시 자동 알람 및 자원 제한 |""",
        "sources": [
            "Financial Stability Board (FSB): Third-Party Risk Management and Cloud Services",
            "금융감독원: 금융기관 클라우드 서비스 이용 가이드라인",
            "NIST Special Publication 800-161: Cybersecurity Supply Chain Risk Management Practices"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [009 멀티 클라우드](./009_multi_cloud.md), [018 소버린 클라우드](./018_sovereign_cloud.md)"
    },

    "111_torus.md": {
        "insight": "격자형(Mesh) 네트워크의 양 끝단 노드를 순환 링으로 상호 연결하여 네트워크 직경을 절반으로 단축하고 대칭성을 확보한 고성능 슈퍼컴퓨팅 토폴로지임.",
        "text_replacements": [],
        "rec_text": "순환 링크로 인한 데드락(Routing Deadlock)을 원천 방지하기 위해 가상 채널(Virtual Channel) 기반의 비환형 차원 순서 라우팅(DOR) 알고리즘 적용 필수.",
        "rec_diagram": """```text
[ 2차원 토러스 (2D Torus: 3x3 구조) 2차원 아스키 도해 ]

        ┌────────────────(순환 링크)────────────────┐
        │                                           │
        ▼                                           ▼
      ( 0,0 ) ─────── ( 0,1 ) ─────── ( 0,2 ) <─────┤
        │   ▲           │   ▲           │   ▲
        │   │           │   │           │   │
        ▼   │           ▼   │           ▼   │
      ( 1,0 ) ─────── ( 1,1 ) ─────── ( 1,2 )
        │   │           │   │           │   │
        ▼   │           ▼   │           ▼   │
        │   ▼           │   ▼           │   ▼
      ( 2,0 ) ─────── ( 2,1 ) ─────── ( 2,2 ) <─────┤
        │                                           │
        └────────────────(순환 링크)────────────────┘
   * 모든 행과 열의 양 끝단 노드가 랩어라운드(Wrap-around) 링크로 연결되어 완전 대칭성 보장
```""",
        "rec_table": """| 비교 축 | 2D / 3D 메시 (Mesh) | 2D / 3D 토러스 (Torus) |
|---|---|---|
| **양 끝단 연결** | 끝단 노드가 개방되어 있음 (순환 링크 없음) | 끝단 노드가 반대편 끝단과 랩어라운드 링으로 연결 |
| **네트워크 직경 (Diameter)**| $k \times n$ (토러스 대비 2배 길어 지연 시간 증가) | $\lfloor k/2 \rfloor \times n$ (직경이 절반으로 대폭 단축) |
| **노드 대칭성** | 비대칭 (가운데 노드에 트래픽 집중 및 병목) | **완전 대칭 (모든 노드가 동일한 위상학적 위치 가짐)** |
| **라우팅 교착 위험** | 차원 순서 라우팅(DOR) 시 교착 없음 | **순환 링크로 인해 라우팅 교착 위험 존재 (가상 채널 필수)** |
| **대표 적용 시스템** | 인텔 제온 멀티코어 칩셋 내부 패브릭 | **구글 TPU v4/v5p 광학 토러스, 후지쯔 후가쿠 슈퍼컴퓨터** |""",
        "sources": [
            "William J. Dally - Performance Analysis of k-ary n-cube Interconnection Networks",
            "IEEE Micro: The Interconnection Network of the Google TPU Supercomputer",
            "John L. Hennessy, David A. Patterson - Computer Architecture: Interconnection Networks"
        ],
        "connections": "- 상위 토픽: [102 상호연결망](./102_interconnection_network.md)\n- 연관 토픽: [022 TPU](./022_tpu.md), [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md)"
    },

    "112_purdue_model.md": {
        "insight": "산업제어시스템(ICS/OT)과 공장 자동화 설비를 6단계 계층으로 분할하고 방화벽 및 산업용 DMZ를 통해 보안 위험 전파를 차단하는 참조 모델임.",
        "text_replacements": [],
        "rec_text": "IT 망과 OT 망 간의 직접 연결을 원천 차단하기 위해 Level 3.5 산업용 DMZ(IDMZ)를 구축하고 점프 호스트(Bastion)와 단방향 데이터 전송(Data Diode) 도입.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 퍼듀 엔터프라이즈 참조 아키텍처 (Purdue Model Hierarchy) ]          │
│                                                                        │
│ [ Level 5: 엔터프라이즈 기업망 ] ERP, SCM, 기업 전사 IT 네트워크       │
│ [ Level 4: 사이트 비즈니스망 ] 공장 운영 기획, 물류 관리 서버         │
├────────────────────────────────────────────────────────────────────────┤
│ [ Level 3.5: 산업용 보안 DMZ (IDMZ) ]                                 │
│   - 패치 관리 서버, 점프 호스트, 이중 방화벽, 프록시                   │
├────────────────────────────────────────────────────────────────────────┤
│ [ Level 3: 제조 운영 관리 (MOM/MES) ] 공정 생산 관리, 히스토리안 서버 │
│ [ Level 2: 제어 시스템 (Control) ] SCADA, HMI 분산 제어 감시           │
│ [ Level 1: 기본 제어 (Basic Control) ] PLC, DCS, RTU 컨트롤러         │
│ [ Level 0: 물리 공정 (Physical Process) ] 센서, 액추에이터, 모터, 로봇 │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 퍼듀 계층 | 핵심 장비 및 시스템 | 통신 프로토콜 | 보안 통제 핵심 |
|---|---|---|---|
| **Level 4/5 (IT 망)** | 전사 ERP, 이메일, 클라우드 연계 | TCP/IP, HTTPS, DNS | 전통적 IT 정보보안, 무신뢰(Zero Trust) 통제 |
| **Level 3.5 (IDMZ)** | 배스천 점프 호스트, 프록시, 미러 히스토리안 | TLS 암호화 세션 터널링 | **IT 망과 OT 망 간의 직접 라우팅 100% 차단** |
| **Level 2/3 (제어 관리)**| SCADA 서버, HMI 운영자 콘솔, MES | OPC-UA, 산업용 이더넷 | 접근 권한 통제, 비인가 USB 차단, OS 패치 관리 |
| **Level 0/1 (물리 제어)**| PLC, DCS, 현장 센서/액추에이터 | Modbus, Profibus, DNP3 | 가용성 최우선, 물리적 망 격리, 펌웨어 무결성 |""",
        "sources": [
            "ISA-95 / IEC 62264: Enterprise-Control System Integration Standards",
            "NIST Special Publication 800-82: Guide to Industrial Control Systems (ICS) Security",
            "CISA (Cybersecurity and Infrastructure Security Agency): Purdue Model Mapping"
        ],
        "connections": "- 상위 토픽: [011 엣지 컴퓨팅](./011_edge_computing.md)\n- 연관 토픽: [073 에너지 고효율 컴퓨팅](./073_energy_efficient_computing.md), [088 클라우드 보안 취약점](./088_cloud_service_security_vulnerabilities.md)"
    },

    "113_copilot_plus_pc_npu.md": {
        "insight": "마이크로소프트 윈도우 11 환경에서 40+ TOPS 성능의 NPU를 탑재하여 클라우드 연결 없이 로컬에서 Recall, 실시간 번역, Co-Creator를 저전력으로 구동하는 AI PC임.",
        "text_replacements": [],
        "rec_text": "로컬 추론 시 발열과 배터리 소모를 방지하기 위해 전용 NPU로 연산을 오프로딩하고, 화면 스냅샷 기록(Recall) 데이터의 암호화와 사용자 생체인증(Windows Hello) 필수 적용.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ Copilot+ PC 하드웨어 및 로컬 온디바이스 AI 런타임 아키텍처 ]         │
│                                                                        │
│   [ 생성형 AI 애플리케이션 계층 ]                                      │
│     - Windows Recall (화면 맥락 검색)   - Cocreator 실시간 드로잉     │
│     - Live Captions (40개 언어 실시간 음성 번역)                       │
│                         │                                              │
│                         ▼                                              │
│   [ Windows Copilot Runtime (DirectML / ONNX Runtime) ]                │
│     - 초경량 Small Language Model (SLM: Phi-3 Silico 로컬 상주)        │
│                         │                                              │
│                         ▼ (NPU 가속 연산자 오프로딩)                  │
│   [ 40+ TOPS 고성능 온디바이스 NPU 하드웨어 ]                          │
│     - Qualcomm Snapdragon X Elite / Intel Lunar Lake / AMD Strix Point│
│     - 저전력(TDP 15~30W)으로 20시간+ 배터리 연속 가동                  │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 전통적 클라우드 기반 AI PC | Copilot+ 온디바이스 AI PC |
|---|---|---|
| **연산 처리 위치** | 원격 거대 클라우드 데이터센터 GPU 서버 | **단말 PC 내부 전용 NPU 하드웨어 (40+ TOPS)** |
| **네트워크 의존도** | 인터넷 연결 필수 (단절 시 AI 기능 전면 중단) | **완전한 오프라인 독립 동작 (비행기 모드 가능)** |
| **개인정보 및 보안** | 민감 화면/음성 데이터의 외부 서버 전송 침해 우려 | **데이터가 단말 로컬 암호화 영역 밖으로 절대 미반출** |
| **추론 지연 및 비용**| 네트워크 RTT 지연 발생, 월 구독료/API 호출 과금 | **지연 시간 제로에 수렴, 추가 API 비용 없음** |""",
        "sources": [
            "Microsoft Windows Copilot+ PC Technical Architecture Whitepaper",
            "Qualcomm Snapdragon X Elite NPU Architecture Specifications",
            "IEEE Micro: On-Device AI Acceleration for Personal Computing"
        ],
        "connections": "- 상위 토픽: [007 NPU](./007_npu.md)\n- 연관 토픽: [020 GPU](./020_gpu.md), [011 엣지 컴퓨팅](./011_edge_computing.md)"
    },

    "114_semiconductor_infrastructure_power_water.md": {
        "insight": "첨단 반도체 팹(Fab) 가동의 필수 유틸리티인 수 기가와트급 특고압 전력 인프라와 초순수(UPW) 용수를 안정적으로 공급하고 정화하는 기반 인프라임.",
        "text_replacements": [],
        "rec_text": "정전 시 웨이퍼 전량 폐기를 막기 위해 복수 345kV 변전소 이중 인입과 비상 디젤 발전기(UPS)를 구축하고, 초순수 생산 시 용수 재이용률을 80% 이상으로 극대화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 첨단 반도체 팹(Fab) 에너지 및 유틸리티 공급 인프라 ]                 │
│                                                                        │
│ [ 1. 특고압 전력 인프라 ]                                              │
│   - 한국전력 345kV / 154kV 초고압 변전소 2N 물리 이중화 인입          │
│   - 무정전 전원 공급 장치 (초대형 회전형 Rotary UPS + 배터리)          │
│   - 순간 전압 강하(Sag) 방지 장치 및 전용 비상 가스 터빈              │
│                                                                        │
│ [ 2. 초순수 (UPW: Ultra Pure Water) 용수 공급 체계 ]                   │
│   - 원수 취수 ──> 활성탄/역삼투압(RO) ──> 이온교환수지 ──> 자외선(UV)살균│
│   - 18.2 MΩ·cm 극초순수 생산 (나노미터급 미세 불순물·유기물 100% 제거)│
│   - 사용된 폐수의 화학적 고도 정화 후 공정용수 재이용 (재활용률 80%+)  │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 핵심 유틸리티 인프라 | 필수 요구 조건 | 공급 중단 시 파급 효과 | 대응 인프라 구축 방안 |
|---|---|---|---|
| **특고압 전력 (Power)** | 1개 팹당 수백 MW, 클러스터 수 GW | 순간 전압 강하(Sag) 시 노광/증착 챔버 웨이퍼 전량 폐기 | 345kV 전용 변전소 2N 라인, 초고속 감지 로터리 UPS |
| **초순수 (UPW Water)** | 하루 수십만 톤 단위 초고순도 용수 | 웨이퍼 표면 미세 오염으로 인한 회로 단락 및 수율 급감 | 다단계 역삼투압(RO)/탈기 타워 정밀 공정, 국산화 실증 |
| **특수 가스 및 화학물질**| 불화수소, 포토레지스트, 특수가스 | 가스 공급 불균일 시 화학 기상 증착(CVD) 공정 중단 | 중앙 공급 밸브 매니폴드(VMB) 및 스크러버(Scrubber) |""",
        "sources": [
            "Semiconductor Industry Association (SIA) Environmental and Infrastructure Guide",
            "한국환경산업기술원(KEITI) 반도체용 초순수 국산화 및 재이용 실증 기술 보고서",
            "산업통상자원부: 용인 첨단 시스템 반도체 클러스터 전력·용수 공급 종합 대책"
        ],
        "connections": "- 상위 토픽: [104 시스템 반도체 생태계](./104_system_semiconductor_ecosystem.md)\n- 연관 토픽: [044 IDC 지리적 입지 선정](./044_idc_geographic_site_selection.md), [062 AI 팩토리 GW 데이터센터](./062_ai_factory_gw_datacenter.md)"
    },

    "115_topological_qubit_majorana_1.md": {
        "insight": "반도체-초전도체 나노와이어 양 끝단의 마요라나 제로 모드(MZM)를 공간적으로 땋는(Braiding) 방식으로 하드웨어 자체에 오류 내성을 갖는 위상 큐비트임.",
        "text_replacements": [],
        "rec_text": "국소적 환경 노이즈에 영향을 받지 않는 위상수학적 비국소성(Non-locality)을 활용하여 물리적 오류율을 획기적으로 낮추고 백만 큐비트 상용 양자컴퓨터로 스케일업.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 마요라나 제로 모드 (MZM) 기반 위상수학적 큐비트 (Topological Qubit) ]│
│                                                                        │
│   초전도체 나노와이어 (Semiconductor-Superconductor Nanowire)          │
│   ┌──────────────────────────────────────────────────────────────┐     │
│   │ γ1 (Majorana Zero Mode)                      γ2 (Majorana)   │     │
│   └──────────────────────────────────────────────────────────────┘     │
│    * 양자 정보가 와이어 양 끝단(γ1, γ2)에 비국소적으로 나뉘어 저장됨    │
│    * 국소적인 열 진동이나 전자기파 노이즈가 양자 정보를 파괴하지 못함  │
│                                                                        │
│   [ 브레이딩 연산 (Braiding Operations: 위상수학적 꼬임) ]             │
│    - 입자를 물리적으로 교환하여 땋는 궤적(Knot) 자체가 양자 게이트 연산│
│    - 미세한 진동 오류와 무관하게 꼬임의 위상 기하학적 성질만 보존됨    │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 전통적 초전도 큐비트 (Transmon) | 위상수학적 큐비트 (Topological MZM) |
|---|---|---|
| **양자 정보 저장 방식** | 조셉슨 접합 LC 회로의 국소적 전하/자속 | 나노와이어 양 끝단에 분리된 준입자의 **비국소적(Non-local) 위상** |
| **하드웨어 오류 보호** | 전무 (외부 노이즈에 극히 민감, 결맞음 수십 $\mu s$) | **하드웨어 자체에서 위상학적 보호 (Topological Protection)** |
| **오류 정정 오버헤드** | 논리 큐비트 1개당 수천 개의 물리 큐비트 필요 | 논리 큐비트 1개당 수 개~수십 개의 소수 큐비트로 달성 가능 |
| **게이트 연산 원리** | 마이크로파 펄스를 정밀 타이밍 인가 | 나노와이어 교차점 상에서 마요라나 입자를 **물리적으로 브레이딩(땋음)** |""",
        "sources": [
            "Microsoft Quantum Team - InAs-Al Hybrid Devices Passing the Topological Gap Protocol",
            "Cheitan Nayak et al. - Non-Abelian Anyons and Topological Quantum Computation (Reviews of Modern Physics)",
            "Nature Physics: Majorana Zero Modes in Semiconductor-Superconductor Heterostructures"
        ],
        "connections": "- 상위 토픽: [029 양자 오류 정정 윌로우](./029_quantum_error_correction_google_willow.md)\n- 연관 토픽: [072 양자 기술 NIA IITP](./072_quantum_technology_nia_iitp.md), [116 하이브리드 컴퓨팅](./116_hybrid_computing.md)"
    },

    "116_hybrid_computing.md": {
        "insight": "고전 컴퓨터(CPU/GPU)와 양자 컴퓨터(QPU)의 장점을 융합하여 전체 연산 흐름은 고전 슈퍼컴퓨터가 제어하고 지수적 난제만 QPU로 오프로딩하는 컴퓨팅 모델임.",
        "text_replacements": [],
        "rec_text": "NISQ 양자 컴퓨터의 큐비트 수와 노이즈 한계를 극복하기 위해 변분 양자 고유값 해석기(VQE)와 QAOA 같은 양자-고전 하이브리드 알고리즘을 우선 적용.",
        "rec_diagram": """```text
[ 사용자 최적화 / 화학 분자 시뮬레이션 문제 정의 ]
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ [ 고전 고성능 슈퍼컴퓨터 (CPU / GPU HPC Cluster) ]     │
│   - 전처리 및 파라미터 초기화                          │
│   - 고전적 경사 하강법 및 최적화 루프 (Optimizer)      │
└────────────────────────┬───────────────────────────────┘
                         │ 1. 파라미터화된 양자 회로 전달
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ 양자 프로세서 가속기 (QPU Co-Processor) ]            │
│   - 양자 얽힘 및 중첩 상태 생성 (Ansatz 준비)          │
│   - 지수적 양자 상태 기대값 측정                       │
└────────────────────────┬───────────────────────────────┘
                         │ 2. 양자 측정 결과값(에너지) 반환
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ 파라미터 수렴 판정 ] ──(미수렴 시 고전 루프로 재순환)│
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 하이브리드 양자 알고리즘 | 고전 컴퓨터 역할 | 양자 가속기(QPU) 역할 | 주요 적용 분야 |
|---|---|---|---|
| **VQE (변분 양자 고유값 해석기)**| 파라미터 갱신 및 손실함수 최소화 최적화 | 분자 파동함수 상태 준비 및 해밀토니안 기대값 측정 | 신약 분자 구조 시뮬레이션, 신소재 개발 |
| **QAOA (양자 근사 최적화)** | 그래프 매개변수 $\gamma, \beta$ 경사도 계산 | 양자 위상 중첩을 통한 조합 최적해 샘플링 | 물류 경로 최적화, 맥스컷(Max-Cut) 그래프 |
| **QML (양자 머신러닝)** | 신경망 가중치 갱신, 데이터 로딩 | 힐베르트 공간 커널 계산 및 양자 임베딩 | 금융 사기 이상 탐지, 복잡 패턴 분류 |""",
        "sources": [
            "Alberto Peruzzo et al. - A Variational Eigenvalue Solver on a Photonic Quantum Processor (Nature Communications)",
            "Edward Farhi et al. - A Quantum Approximate Optimization Algorithm (arXiv)",
            "IEEE Micro: Quantum-Classical Hybrid Computer Architecture and Systems"
        ],
        "connections": "- 상위 토픽: [072 양자 기술 NIA IITP](./072_quantum_technology_nia_iitp.md)\n- 연관 토픽: [029 양자 오류 정정 윌로우](./029_quantum_error_correction_google_willow.md), [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md)"
    },

    "117_hardware_sizing.md": {
        "insight": "신규 시스템 구축 시 비즈니스 목표 트랜잭션과 데이터 용량을 충족하도록 CPU, 메모리, 디스크 IOPS를 과학적 산식(TPC-C)으로 정량 산정하는 기법임.",
        "text_replacements": [],
        "rec_text": "오버스펙으로 인한 비용 낭비와 언더스펙으로 인한 성능 저하를 방지하기 위해 5개년 피크 트래픽과 시스템 확장 여유율(버퍼 30%)을 과학적으로 반영 산정.",
        "rec_diagram": """```text
[ 비즈니스 요구사항 분석 (동시 사용자 수, 일일 트랜잭션 건수) ]
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ [ 1단계: CPU 사이징 (tpmC 기반 산정 공식) ]             │
│   필요 tpmC = (일일 트랜잭션 수 / 유효 가동시간) * 피크율 * 보정계수 │
│   필요 Core = 필요 tpmC / (코어당 기준 tpmC * 코어 보정계수)│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ [ 2단계: 메모리 사이징 ] OS 기본(4GB) + WAS 힙 메모리 + DB 버퍼 캐시│
│ [ 3단계: 디스크 사이징 ] 데이터 원장 + 인덱스(50%) + 로그 + 여유율(30%)│
│ [ 4단계: I/O 성능 사이징 ] 초당 필요 IOPS 및 대역폭 검증│
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 사이징 산정 방식 | 산정 원리 | 장점 | 주요 단점 및 한계 |
|---|---|---|---|
| **TPC-C 기반 산정법** | 공인 벤치마크 tpmC 트랜잭션 처리량 환산 | 객관적이고 표준화된 비교 가능 | 실제 업무 쿼리의 복잡도(조인, 집계) 미반영 |
| **참조 시스템 비교법** | 기존 운영 중인 유사 레거시 시스템의 실측치 보정 | 현장 적합성 및 정확도 우수 | 신규 구축 비즈니스에선 비교 대상 부재 |
| **시뮬레이션/PoC 기법**| 실 환경 부하 테스트 도구(JMeter)로 한계 실측 | 가장 정확한 사이징 결과 도출 | 시간 및 고비용 테스트 환경 구축 소요 |""",
        "sources": [
            "TPC (Transaction Processing Performance Council) Benchmark C Standard Specification",
            "한국정보화진흥원(NIA) 정보시스템 하드웨어 규모산정 지침",
            "IEEE Transactions on Software Engineering: Capacity Planning and Sizing Methodologies"
        ],
        "connections": "- 상위 토픽: [120 성능 튜닝](./120_performance_tuning.md)\n- 연관 토픽: [076 CPU](./076_cpu.md), [024 디스크 스케줄링](./024_disk_scheduling.md)"
    },

    "118_android.md": {
        "insight": "리눅스 커널 기반에 안드로이드 런타임(ART)과 바인더(Binder) IPC를 결합하여 모바일 디바이스의 배터리 효율과 앱 샌드박스 보안을 최적화한 오픈소스 OS임.",
        "text_replacements": [],
        "rec_text": "프로세스 간 고속 통신을 위해 단일 복사 공유 메모리 기반의 바인더(Binder) IPC를 적용하고, 사전 AOT 컴파일과 프로파일 기반 JIT 컴파일을 혼합한 ART 런타임 최적화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 안드로이드 시스템 소프트웨어 스택 아키텍처 ]                        │
│                                                                        │
│   [ 시스템 앱 & 사용자 애플리케이션 (Java / Kotlin Apps) ]             │
│   └──────────────────────────────────┬─────────────────────────────────┘
│                                      ▼
│   [ Java API 프레임워크 (Activity, Service, ContentProvider, Broadcast)│
│   └──────────────────────────────────┬─────────────────────────────────┘
│                                      ▼
│   [ 안드로이드 런타임 (ART) ] & [ 네이티브 C/C++ 라이브러리 (WebKit, SQLite)│
│    - DEX 바이트코드 실행, AOT + JIT 혼합 컴파일, 백그라운드 컴팩션 GC  │
│   └──────────────────────────────────┬─────────────────────────────────┘
│                                      ▼
│   [ 하드웨어 추상화 계층 (HAL: Hardware Abstraction Layer) ]            │
│    - 카메라, 오디오, 블루투스 하드웨어 벤더 드라이버 표준 인터페이스   │
│   └──────────────────────────────────┬─────────────────────────────────┘
│                                      ▼
│   [ 리눅스 커널 (Linux Kernel) ] : 바인더 IPC 드라이버, 전원 관리(Wakelock)│
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 런타임 기술 | 컴파일 방식 | 앱 설치 속도 | 런타임 실행 속도 | 스토리지 점유율 |
|---|---|---|---|---|
| **Dalvik VM (레거시)** | 순수 인터프리터 + JIT (Just-In-Time) | 빠름 | 느림 (매번 기계어 변환) | 작음 |
| **초기 ART (Android 5.0)**| 순수 AOT (Ahead-Of-Time: 전수 사전 컴파일) | 매우 느림 | 최고속 (설치 시 기계어화) | 매우 큼 (바이너리 비대) |
| **현대 ART (프로파일 기반)**| JIT + AOT 혼합 (자주 쓰는 코드만 AOT) | 빠름 | 최고속 (PGO 프로파일 최적화) | 최적화 (균형 달성) |""",
        "sources": [
            "Android Open Source Project (AOSP) Architecture Documentation",
            "IEEE Pervasive Computing: The Evolution of the Android Runtime (ART)",
            "Google Developers: Android OS Architecture and Binder IPC Mechanism"
        ],
        "connections": "- 상위 토픽: [076 CPU](./076_cpu.md)\n- 연관 토픽: [034 IPC](./034_ipc.md), [121 아두이노](./121_arduino.md)"
    },

    "119_xaas.md": {
        "insight": "IaaS, PaaS, SaaS의 전통적 클라우드 서비스 범위를 넘어 데이터, 보안, AI 등 비즈니스의 모든 IT 자원을 네트워크 기반 종량제 서비스 형태로 제공하는 패러다임임.",
        "text_replacements": [],
        "rec_text": "초기 구축 비용(CAPEX)을 운영 비용(OPEX)으로 전환하고, 구독 경제 모델 하에서 서비스 수준 협약(SLA)과 데이터 주권(Data Residency) 컴플라이언스를 사전 정의.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ XaaS (Everything as a Service) 서비스 스펙트럼 확장 체계 ]           │
│                                                                        │
│   [ 1. 전통적 클라우드 3대 모델 ]                                      │
│     - IaaS (인프라)  ──>  PaaS (플랫폼)  ──>  SaaS (소프트웨어)        │
│                                                                        │
│   [ 2. 비즈니스 기능 및 기술 전문 서비스화 (XaaS 확장) ]               │
│     - DaaS (Desktop as a Service)   : 가상 데스크톱 호스팅 클라우드   │
│     - SECaaS (Security as a Service): 클라우드 기반 통합 관제 및 방화벽│
│     - AIaaS (AI as a Service)       : LLM API, 초거대 파운데이션 모델  │
│     - BaaS (Backend as a Service)   : 모바일/웹 공통 인증, 푸시, DB   │
│     - NaaS (Network as a Service)   : SD-WAN, 가상 전용 사설망        │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| XaaS 신규 서비스 유형 | 주요 제공 기능 | 고객 도입 효과 | 대표 서비스 예시 |
|---|---|---|---|
| **AIaaS (AI-as-a-Service)** | 생성형 AI LLM API, 비전/음성 추론 모델 | 거대 GPU 인프라 없이 즉각 AI 기능 탑재 | OpenAI API, Claude API, Bedrock |
| **SECaaS (보안 서비스)** | 클라우드 WAF, DDoS 방어, EDR, SIEM | 24x365 전문 보안 관제 인건비 절감 | Cloudflare, Zscaler, CrowdStrike |
| **BaaS (백엔드 서비스)** | 사용자 인증, NoSQL DB, 푸시 알림, 스토리지 | 프론트엔드 개발자가 서버 개발 없이 앱 완성 | Firebase, Supabase, AWS Amplify |
| **NaaS (네트워크 서비스)** | 가상 사설망, 글로벌 SD-WAN 오버레이 | 고가의 해외 전용선 구축 대체 | Cisco Plus, Aruba NaaS |""",
        "sources": [
            "NIST Special Publication 500-322: Cloud Computing Everything as a Service",
            "Gartner Top Strategic Technology Trends: The Rise of Everything as a Service (XaaS)",
            "Deloitte Insights: Enterprise IT Transformation Through XaaS Models"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [036 SaaS](./036_saas.md), [077 DaaS](./077_daas.md), [078 FaaS](./078_faas.md)"
    },

    "120_performance_tuning.md": {
        "insight": "시스템의 처리량(Throughput)을 극대화하고 응답 시간(Latency)을 단축하기 위해 하드웨어, OS 커널, 데이터베이스, 애플리케이션 전 계층의 병목을 진단하고 최적화함.",
        "text_replacements": [],
        "rec_text": "브렌던 그레그의 USE(Utilization, Saturation, Errors) 방법론에 입각하여 병목 자원을 과학적으로 식별하고, 단일 파라미터 변경 후 전후 성능을 정량 대조 검증.",
        "rec_diagram": """```text
[ 엔드투엔드 시스템 계층별 성능 튜닝 및 진단 파이프라인 ]

  [ 1. 애플리케이션 계층 ] ──> 알고리즘 복잡도 개선, 락 경합 완화, 비동기 논블로킹 I/O
            │
            ▼
  [ 2. 미들웨어/DB 계층 ] ──> 인덱스 최적화, 쿼리 리팩토링, 커넥션 풀(DBCP) 사이징
            │
            ▼
  [ 3. OS 및 커널 계층 ]  ──> TCP 버퍼 크기, 파일 디스크립터 한도, vm.swappiness 튜닝
            │
            ▼
  [ 4. 하드웨어/인프라 ]  ──> CPU 거버너 고성능 설정, NUMA 인터리빙, All-NVMe 교체
```""",
        "rec_table": """| 성능 분석 방법론 | 창안자/원칙 | 핵심 진단 지표 | 적용 대상 |
|---|---|---|---|
| **USE 방법론** | Brendan Gregg | **이용률(Utilization), 포화도(Saturation), 오류(Errors)** | CPU, 메모리, 디스크 등 하드웨어 자원 분석 |
| **RED 방법론** | Tom Wilkie | **요청율(Rate), 오류율(Errors), 지속시간(Duration)** | 마이크로서비스, 웹 API 요청 성능 분석 |
| **Four Golden Signals** | Google SRE | **지연시간(Latency), 트래픽(Traffic), 오류(Errors), 포화도(Saturation)** | 대규모 분산 시스템 모니터링 표준 |""",
        "sources": [
            "Brendan Gregg - Systems Performance: Enterprise and the Cloud 2nd Edition (Addison-Wesley)",
            "Google Site Reliability Engineering (SRE) Handbook: Monitoring Distributed Systems",
            "Computer Systems: A Programmer's Perspective (CS:APP) - Optimizing Program Performance"
        ],
        "connections": "- 상위 토픽: [117 하드웨어 사이징](./117_hardware_sizing.md)\n- 연관 토픽: [076 CPU](./076_cpu.md), [024 디스크 스케줄링](./024_disk_scheduling.md)"
    },

    "121_arduino.md": {
        "insight": "단일 칩 마이크로컨트롤러(MCU)와 표준 입출력 핀헤더를 갖춘 오픈소스 하드웨어 플랫폼으로, 센서 데이터 수집과 임베디드 액추에이터 제어를 신속히 프로토타이핑함.",
        "text_replacements": [],
        "rec_text": "제한된 8비트/32비트 MCU 메모리(SRAM 수 KB) 한계를 감안하여 동적 힙 메모리 할당(malloc)을 배제하고 정적 배열을 활용하며 인터럽트 서비스 루틴(ISR) 코드 최소화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 아두이노 (Arduino Uno) 하드웨어 아키텍처 및 핀맵 ]                  │
│                                                                        │
│   [ 전원 공급: USB / DC 잭 ] ──> 전압 레귤레이터 (5V / 3.3V 전원 레일)  │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ ATmega328P 8비트 AVR 마이크로컨트롤러 (MCU: 16MHz 클록)         │   │
│   │  - 32KB 플래시 메모리 (부트로더 및 사용자 스케치 코드 저장)    │   │
│   │  - 2KB SRAM (변수 및 런타임 스택) / 1KB EEPROM (영속 데이터)   │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │                                    │
│         ┌─────────────────────────┴─────────────────────────┐          │
│         ▼                                                   ▼          │
│   [ 14개 디지털 I/O 핀 ]                             [ 6개 아날로그 입력 ]
│   - 디지털 입출력, PWM 펄스 폭 변조                   - 10비트 ADC 내장 │
│   - 인터럽트 핀, UART/SPI/I2C 통신                    (0~5V 전압 측정)  │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 임베디드 플랫폼 | 주 제어 프로세서 | 연산 클록 및 메모리 | 주 용도 및 장점 | 차별점 |
|---|---|---|---|---|
| **아두이노 (Arduino)** | 8비트 AVR 또는 32비트 ARM MCU | 16 ~ 84 MHz, SRAM 수 KB | 센서 읽기, 모터 제어 등 하드웨어 직결 제어 | **OS 없음 (단일 펌웨어 루프 실행)** |
| **라즈베리 파이 (Raspberry Pi)**| 64비트 쿼드코어 ARM CPU | 1.5 GHz+, RAM 2~8 GB | 영상 처리, 웹 서버, 경량 AI 추론 | **완전한 리눅스 OS 구동 가능 (SBC)** |""",
        "sources": [
            "Massimo Banzi, Michael Shiloh - Getting Started with Arduino: The Open Source Electronics Platform",
            "Microchip Technology ATmega328P 8-bit AVR Microcontroller Datasheet",
            "IEEE Pervasive Computing: Open-Source Hardware for Rapid Prototyping"
        ],
        "connections": "- 상위 토픽: [011 엣지 컴퓨팅](./011_edge_computing.md)\n- 연관 토픽: [086 간헐적 컴퓨팅](./086_intermittent_computing.md), [118 안드로이드](./118_android.md)"
    },

    "122_process_synchronization.md": {
        "insight": "다중 프로세스/스레드가 공유 자원에 동시 접근할 때 상호배제, 진행, 유한대기 3대 조건을 만족시켜 데이터 일관성을 보장하는 동기화 이론임.",
        "text_replacements": [],
        "rec_text": "임계구역 설계 시 3대 조건(상호배제, 진행, 유한대기)을 충족하도록 뮤텍스 또는 세마포어를 적용하고, 동기화 오류를 방지하기 위해 언어 레벨 모니터(Monitor) 사용 권고.",
        "rec_diagram": """```text
[ 임계구역(Critical Section) 문제 해결 3대 필수 조건 ]

 1. 상호 배제 (Mutual Exclusion)
    - 한 프로세스가 임계구역에서 실행 중이면 다른 어떤 프로세스도 진입 불가

 2. 진행 (Progress)
    - 임계구역에 실행 중인 프로세스가 없을 때 진입하고자 하는 후보 프로세스들 중에서만
      다음 진입자를 결정하며, 결정이 무한정 연기되지 않아야 함

 3. 유한 대기 (Bounded Waiting)
    - 프로세스가 임계구역 진입을 요청한 후 허가될 때까지 다른 프로세스들의 진입 횟수에
      상한선(Bound)이 존재하여 기아 상태(Starvation)가 배제되어야 함
```""",
        "rec_table": """| 동기화 기법 | 동작 수준 | 핵심 메커니즘 | 장점 및 주의점 |
|---|---|---|---|
| **피터슨 알고리즘 (Peterson)** | 소프트웨어적 해결책 | `flag` 배열과 `turn` 변수 교차 확인 | 2개 프로세스에 한정, 현대 OoO CPU 메모리 배리어 필요 |
| **Test-And-Set / CAS** | 하드웨어 명령어 지원 | 메모리 워드를 원자적으로 읽고 쓰는 단일 기계어 | 락-프리 자료구조의 기반, 바쁜 대기(Spinlock) 오버헤드 |
| **세마포어 (Semaphore)** | OS 커널 서브시스템 | 정수 카운터 변수 $S$와 $P(wait), V(signal)$ 연산 | 범용 자원 풀 관리, 잘못된 시그널 호출 시 동기화 파괴 |
| **모니터 (Monitor)** | 고급 프로그래밍 언어 | 클래스 내 동기화 캡슐화, 조건 변수(Condition Var)| 동기화 실수를 컴파일러가 차단, 가장 안전한 고수준 기법 |""",
        "sources": [
            "Edsger W. Dijkstra - Cooperating Sequential Processes: Semaphores",
            "C.A.R. Hoare - Monitors: An Operating System Structuring Concept (CACM)",
            "Abraham Silberschatz et al. - Operating System Concepts: Process Synchronization"
        ],
        "connections": "- 상위 토픽: [091 경쟁 조건](./091_race_condition.md)\n- 연관 토픽: [038 데드락](./038_deadlock.md), [010 스레드](./010_thread.md)"
    },

    "123_storage_type_comparison.md": {
        "insight": "데이터 접근 프로토콜과 조직 방식에 따라 블록 스토리지, 파일 스토리지, 객체 스토리지를 워크로드 요구사항(지연 시간, 확장성, 메타데이터)에 맞춰 선택함.",
        "text_replacements": [
            ("Snapshot·RAID·Erasure Coding·Versioning의 적용 범위가 다르므로 특정 기능 지원 여부만으로 비교하지 않는다.",
             "Snapshot, RAID, Erasure Coding, Versioning의 적용 계층이 상이하므로 특정 기능 지원 여부만으로 단순 비교 지양.")
        ],
        "rec_text": "초저지연 무작위 쓰기가 필수인 RDBMS에는 블록 스토리지(SAN/EBS)를, 전사 협업 공유에는 파일 스토리지(NAS), 페타바이트급 AI 비정형 데이터레이크에는 객체 스토리지(S3) 채택.",
        "rec_diagram": """```text
[ 3대 스토리지 아키텍처 비교 도해 ]

 [ 1. 블록 스토리지 (Block) ]     [ 2. 파일 스토리지 (File) ]     [ 3. 객체 스토리지 (Object) ]
  ┌───┬───┬───┬───┐                ┌───────────────────────┐       ┌───────────────────────┐
  │B0 │B1 │B2 │B3 │                │ /root/data/report.pdf │       │ Key: images/logo.png  │
  └───┴───┴───┴───┘                └───────────┬───────────┘       │ Data: [Binary Bytes]  │
  - 고유 블록 주소 (LBA)           - 계층적 디렉터리 트리          │ Metadata: [Custom Tag]│
  - OS 파일시스템이 직접 제어      - POSIX 표준 파일 공유 (NFS)    └───────────────────────┘
  - 최고속 IOPS (SAN / EBS)        - 다중 서버 동시 공유 (NAS)     - RESTful HTTP API (S3)
                                                                   - 무한한 수평 확장성
```""",
        "rec_table": """| 비교 축 | 블록 스토리지 (Block) | 파일 스토리지 (File) | 객체 스토리지 (Object) |
|---|---|---|---|
| **데이터 접근 단위** | 고정 크기 로우 블록 (Block) | 계층적 파일 및 디렉터리 트리 | 고유 키(Key) 기반 객체 (Data+Metadata) |
| **통신 프로토콜** | FC, iSCSI, NVMe-oF | NFS, SMB/CIFS | RESTful API (HTTP GET/PUT/DELETE) |
| **지연 시간 (Latency)**| **극소 (수백 $\mu s$ 미만)** | 보통 (수 밀리초 단위) | 상대적 높음 (수십~수백 밀리초) |
| **용량 확장성** | 노드/스토리지 한계 내 제한적 | 파일시스템 규모 내 확장 가능 | **이론상 무한한 글로벌 수평 확장 (페타/엑사급)**|
| **최적 활용 영역** | 고성능 RDBMS, 가상머신 OS 디스크 | 사내 공용 파일서버, 콘텐츠 CMS | AI 데이터레이크, 클라우드 백업/아카이브 |""",
        "sources": [
            "Storage Networking Industry Association (SNIA) Dictionary of Storage Terms",
            "Amazon Web Services: Differences Between Block, File, and Object Storage",
            "IEEE Transactions on Knowledge and Data Engineering: Scalable Cloud Storage Architectures"
        ],
        "connections": "- 상위 토픽: [084 SAN](./084_san.md)\n- 연관 토픽: [080 NAS](./080_nas.md), [082 DAS](./082_das.md)"
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
    
    # 2. Fix 30초 인출 통찰
    content = re.sub(
        r'- 통찰:[^\n]*',
        f"- 통찰: {d['insight']}",
        content
    )
    
    # 3. Text replacements
    for old_txt, new_txt in d.get("text_replacements", []):
        if old_txt in content:
            content = content.replace(old_txt, new_txt)
        else:
            print(f"Warning: pattern not found in {fname}: {old_txt[:40]}...")
            
    # 4. Replace Section VI, sources, and linked topics
    vi_match = re.search(r'## Ⅵ\.[^\n]*', content)
    if not vi_match:
        print(f"Error: Section VI not found in {fname}")
        continue
        
    pre_vi = content[:vi_match.start()].rstrip()
    
    # Extract or use clean linked topics
    linked_match = re.search(r'## 연결 토픽\s*\n(.*)$', content, re.DOTALL)
    if linked_match and d.get("connections") is None:
        linked_topics = linked_match.group(1).strip()
    else:
        linked_topics = d.get("connections", "- 상위 토픽: [컴퓨터 시스템 일반](./index.md)")
        
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
