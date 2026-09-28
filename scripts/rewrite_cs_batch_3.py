import os
import re
from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

DATA = {
    "046_cloud_deployment_models.md": {
        "insight": "조직의 보안 규제 준수와 비용 효율을 최적화하기 위해 퍼블릭, 프라이빗, 하이브리드, 멀티 클라우드를 비즈니스 요구에 맞춰 배포함.",
        "text_replacements": [],
        "rec_text": "핵심 원장 및 개인정보는 프라이빗에 배치하고 대고객 웹 서비스는 퍼블릭으로 탄력 확장하는 하이브리드 아키텍처를 채택하며, Direct Connect로 안전한 전용선 구성.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 클라우드 4대 배포 모델 (Cloud Deployment Models) 아키텍처 ]          │
│                                                                        │
│ [ 퍼블릭 (Public) ]     [ 프라이빗 (Private) ]   [ 하이브리드 (Hybrid) ] │
│  - CSP 공유 인프라      - 단일 조직 전용 구축    - 퍼블릭 + 온프레미스   │
│  - 멀티테넌시 공유      - 데이터 완벽한 통제    - Direct Connect 전용선 │
│  - 확장성 최고/종량제   - 초기 CAPEX 발생        - 클라우드 버스팅(Burst)│
│                                                                        │
│ [ 커뮤니티 (Community) ] : 유사 규제·목적을 공유하는 특정 산업군 공동망 │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 배포 모델 | 인프라 소유 및 위치 | 멀티테넌시 수준 | 보안 및 규제 준수 | 초기 투자비 (CAPEX) |
|---|---|---|---|---|
| **퍼블릭 (Public)** | CSP 소유, 공용 데이터센터 | 다중 테넌트 공유 | CSP 보안 체계 의존 | 전무 (순수 OPEX 종량제) |
| **프라이빗 (Private)** | 기업 단독 소유, 사내/호스팅 | 단일 조직 전용 | 최고 (완전한 통제권) | 매우 높음 (서버/스토리지 구매) |
| **하이브리드 (Hybrid)** | CSP + 온프레미스 혼합 | 영역별 분리 혼용 | 민감 데이터 사내 격리 | 중간 (기존 인프라 활용) |
| **커뮤니티 (Community)**| 복수 기관 공동 소유/운영 | 특정 산업 참여자 | 공통 산업 규정 준수 | 참여 기관 간 분담 |""",
        "sources": [
            "NIST Special Publication 800-145: The NIST Definition of Cloud Computing",
            "ISO/IEC 17788: Cloud computing - Overview and vocabulary",
            "CSA (Cloud Security Alliance) Security Guidance for Critical Areas of Cloud Computing"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [009 멀티 클라우드](./009_multi_cloud.md), [018 소버린 클라우드](./018_sovereign_cloud.md)"
    },

    "047_system_failure_prevention_cutover.md": {
        "insight": "차세대 시스템 오픈 시 서비스 중단 리스크를 제로화하기 위해 단계별 전환 시나리오와 명확한 판정 기준의 Go/No-Go 의사결정 체계를 구축함.",
        "text_replacements": [],
        "rec_text": "오픈 리스크를 최소화하기 위해 전수 데이터 검증 툴과 롤백 절차를 사전 모의훈련하고, 컷오버 당일 시간대별 타임라인과 마일스톤별 판정 기준서 수립.",
        "rec_diagram": """```text
[ 컷오버(Cutover) 단계별 전환 및 Go/No-Go 의사결정 파이프라인 ]

[ 1단계: 전환 사전 준비 ] ──> [ 2단계: 레거시 정지 & 백업 ] ──> [ 3단계: 신규 시스템 적재 ]
 - 모의 훈련 (Dry-Run)       - 트랜잭션 차단 및 배치 종료    - DB 초기 적재 + CDC 반영
 - 정합성 검증 스크립트      - 최종 콜드 백업 수행           - 인터페이스 연계 가동
                                                                      │
                                                                      ▼
[ 최종 서비스 오픈 ] <── [ 5단계: 대고객 오픈 ] <── [ 4단계: 1차 Go/No-Go 판정 ]
 (안정화 집중 모니터링)    (DNS / LB 트래픽 신규 전환)   - 정합성 100% 검증 확인
                                                          - 미충족 시 즉시 롤백 선언
```""",
        "rec_table": """| 컷오버 방식 | 작업 특성 | 다운타임 | 리스크 수준 | 권장 적용 환경 |
|---|---|---|---|---|
| **빅뱅 컷오버 (Big Bang)** | 연휴 기간 중 일괄 전면 전환 | 수 시간 ~ 수십 시간 | 최고 (실패 시 복구 극난) | 연계 복잡도가 높은 코어뱅킹 |
| **단계적 컷오버 (Phased)** | 업무 모듈별 순차 오픈 | 모듈별 부분 다운타임 | 중간 (데이터 동기화 오버헤드)| 독립 모듈 구성이 가능한 ERP/CRM |
| **병행 가동 (Parallel)** | 구/신 시스템 동시 운영 대사 | 전무 (다운타임 없음) | 최저 (운영비 2배 소요) | 초고신뢰 국방/항공/원자력 |""",
        "sources": [
            "Project Management Institute (PMI) - Practice Standard for Project Risk Management",
            "한국정보화진흥원(NIA) 공공 정보시스템 전환 및 컷오버 이행 가이드",
            "The Open Group TOGAF Standard: Implementation and Migration Transition Planning"
        ],
        "connections": "- 상위 토픽: [021 HA](./021_ha.md)\n- 연관 토픽: [042 HA 가용성 보장](./042_ha_availability_assurance.md), [106 마이그레이션 장애관리](./106_migration_fault_management.md)"
    },

    "048_zombie_process.md": {
        "insight": "자식 프로세스가 종료되었으나 부모 프로세스가 wait() 계열 시스템 콜로 종료 상태를 회수하지 않아 프로세스 테이블 엔트리를 점유하는 유령 프로세스임.",
        "text_replacements": [],
        "rec_text": "좀비 프로세스의 누적으로 인한 PID 고갈을 방지하기 위해 SIGCHLD 시그널 핸들러에서 non-blocking waitpid()를 호출하고, 고아 프로세스는 init/systemd가 입양하도록 설계.",
        "rec_diagram": """```text
[ 정상 프로세스 수명주기 ]
  부모 프로세스 ──(fork)──> 자식 프로세스 실행 ──(exit)──> [ Zombie 상태 ]
         │                                                      │
         └─────────────(wait() 시스템 콜 호출로 상태 회수)───────┘
                                     │
                                     ▼
                     [ PCB 및 PID 자원 메모리 완전 해제 ]

[ 좀비 프로세스 누적 메커니즘 ]
  자식 프로세스 종료 (exit) ──> [ Zombie (State: Z) ] (PCB 잔존, PID 점유)
                                      │
  부모 프로세스가 wait() 호출 태만 ───┴──> 시스템 PID 풀 고갈 ──> 신규 프로세스 생성 실패!
```""",
        "rec_table": """| 구분 항목 | 좀비 프로세스 (Zombie Process) | 고아 프로세스 (Orphan Process) |
|---|---|---|
| **정의** | 실행은 종료되었으나 부모가 상태를 회수하지 않은 프로세스 | 부모 프로세스가 먼저 종료되어 홀로 남겨진 프로세스 |
| **자원 점유** | CPU/메모리는 반환 완료, **PID 및 PCB 엔트리만 점유** | 정상적인 CPU 및 메모리 자원을 계속 점유하며 실행 중 |
| **시스템 영향** | 누적 시 PID 고갈로 인한 신규 프로세스 생성 불가 (Fork Fail)| 시스템 자원 지속 소모 (의도치 않은 백그라운드 연산) |
| **해결 방안** | 부모 프로세스 종료(init/systemd 입양 후 자동 회수) | init(PID 1) 프로세스가 입양하여 정상 수명주기 관리 |""",
        "sources": [
            "W. Richard Stevens, Stephen A. Rago - Advanced Programming in the UNIX Environment: Process Control",
            "Abraham Silberschatz et al. - Operating System Concepts: Processes",
            "Linux Programmer's Manual: wait(2), waitpid(2), fork(2), signal(7)"
        ],
        "connections": "- 상위 토픽: [050 프로세스 메모리 구조](./050_process_memory_layout.md)\n- 연관 토픽: [010 스레드](./010_thread.md), [076 CPU](./076_cpu.md)"
    },

    "049_cloud_native_disaster_recovery.md": {
        "insight": "멀티 리전 분산 아키텍처와 선언적 GitOps 파이프라인을 결합하여 대규모 클라우드 장애 발생 시 인프라와 서비스를 신속하고 탄력적으로 자동 복구함.",
        "text_replacements": [
            ("장애를 감지하면 데이터 복제 상태를 확인하고, 보조 사이트의 트래픽·용량을 준비한 뒤 라우팅을 전환한다. 서비스가 정상화되면 변경 데이터를 동기화하고 주 사이트로 복귀할 수 있다.",
             "장애 감지 시 데이터 복제 지연을 확인하고, 보조 사이트의 트래픽 라우팅을 전환하여 서비스를 복구하며 변경 데이터를 동기화한 뒤 정상 시 주 사이트로 롤백 수행.")
        ],
        "rec_text": "인프라 형상 전체를 Git 리포지토리에 선언적 코드로 관리(IaC/GitOps)하고, 데이터 계층은 글로벌 분산 DB(CockroachDB/DynamoDB Global Table)를 적용하여 RPO 제로 달성.",
        "rec_diagram": """```text
┌──────────────────────────────┐               ┌──────────────────────────────┐
│ [ Cloud Region A (Primary) ] │               │ [ Cloud Region B (Secondary) ]│
│  - EKS / GKE 클라우드 클러스터│               │  - EKS / GKE 클러스터 (대기) │
│  - 글로벌 로드밸런서 (Route53)│<─────────────>│  - 글로벌 로드밸런서 (Route53)│
└──────────────┬───────────────┘  GSLB 헬스체크 └──────────────┬───────────────┘
               │                                              │
               │ 실시간 비동기/준동기 데이터 복제             │
               ▼                                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ [ GitOps 기반 지속적 복원 엔진 (ArgoCD / Flux) ]                            │
│  - Git 형상 저장소(SSOT)로부터 장애 리전에 인프라 및 컨테이너 즉시 재프로비저닝│
└─────────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 클라우드 DR 전략 | 아키텍처 구성 방식 | 복구 목표 시간 (RTO) | 복구 시점 목표 (RPO) | 비용 효율성 |
|---|---|---|---|---|
| **백업 및 복원 (Backup & Restore)** | 스토리지 스냅샷 및 S3 복제 | 수 시간 ~ 수 일 | 수 시간 단위 | 최고 (유휴 비용 없음) |
| **파일럿 라이트 (Pilot Light)** | 핵심 데이터 실시간 복제 + 최소 코어 가동| 수십 분 이내 | 수 초 ~ 수 분 | 높음 (컴퓨팅 비용 최소화) |
| **웜 스탠바이 (Warm Standby)** | 축소된 규모의 보조 인프라 항시 구동 | 수 분 이내 | 실시간에 근접 | 중간 수준 |
| **멀티 사이트 액티브-액티브** | 복수 리전 트래픽 분산 완전 동시 가동 | **즉시 (수 초 이내)** | **0 (Zero RPO)** | 최저 (완전 중복 비용) |""",
        "sources": [
            "AWS Disaster Recovery of Workloads on AWS: Cloud-Native DR Whitepaper",
            "Google Cloud Architecture Center: Disaster Recovery Planning Guide",
            "CNCF Disaster Recovery and High Availability Best Practices"
        ],
        "connections": "- 상위 토픽: [043 데이터센터 입지 및 재해대응](./043_datacenter_location_disaster_response.md)\n- 연관 토픽: [065 멀티 리전 액티브-액티브 DR](./065_multi_region_active_active_dr.md), [012 쿠버네티스](./012_kubernetes.md)"
    },

    "050_process_memory_layout.md": {
        "insight": "OS가 프로세스에 부여하는 독립된 가상 주소 공간으로, 정적 영역(Text, Data, BSS)과 동적 영역(Heap, Stack)으로 구분되어 메모리 보호와 실행을 제어함.",
        "text_replacements": [
            ("운영체제는 실행 파일의 헤더를 읽어 코드·데이터를 배치하고 런타임에 힙을 늘리거나 스택 프레임을 쌓는다. 힙은 낮은 주소에서 높은 주소로, 스택은 높은 주소에서 낮은 주소로 자란다.",
             "운영체제는 실행 파일의 헤더를 읽어 텍스트 및 데이터 세그먼트를 배치하고 런타임에 힙과 스택을 동적 확장. 힙은 저위 주소에서 고위 주소로 확장되며 스택은 고위 주소에서 저위 주소로 확장되는 구조 형성.")
        ],
        "rec_text": "스택 버퍼 오버플로우 공격을 원천 무력화하기 위해 ASLR(주소 공간 무작위화)과 실행 방지 비트(NX/DEP)를 커널 레벨에서 활성화하고 동적 할당 메모리 해제 철저.",
        "rec_diagram": """```text
[ 32비트 / 64비트 가상 메모리 프로세스 주소 공간 배치 구조 ]

  높은 주소 (0xFFFFFFFF)
  ┌────────────────────────────────────────────────────────┐
  │ 커널 공간 (Kernel Space) : 시스템 콜 호출 시에만 접근   │
  ├────────────────────────────────────────────────────────┤
  │ 사용자 스택 (User Stack) : 지역 변수, 함수 매개변수, 반환 주소
  │       │ (아래로 확장: High -> Low Address)             │
  │       ▼                                                │
  │                                                        │
  │       ▲                                                │
  │       │ (위로 확장: Low -> High Address)               │
  │ 사용자 힙 (User Heap) : malloc(), new() 동적 할당 공간 │
  ├────────────────────────────────────────────────────────┤
  │ BSS 세그먼트 : 초기화되지 않은 전역 및 정적(Static) 변수│
  ├────────────────────────────────────────────────────────┤
  │ 데이터 세그먼트 (Data) : 초기화된 전역 및 정적 변수     │
  ├────────────────────────────────────────────────────────┤
  │ 텍스트 세그먼트 (Text / Code) : 컴파일된 기계어 코드 (읽기 전용)
  └────────────────────────────────────────────────────────┘
  낮은 주소 (0x00000000)
```""",
        "rec_table": """| 세그먼트 영역 | 저장 데이터 | 할당 시점 | 크기 변화 특성 | 접근 권한 |
|---|---|---|---|---|
| **Text (Code)** | 컴파일된 실행 기계어 코드 | 프로그램 적재 시 | 고정 (Fixed) | Read-Only, Execute |
| **Data (Initialized)** | 초기값이 지정된 전역/정적 변수 | 컴파일/적재 시 | 고정 (Fixed) | Read, Write |
| **BSS (Uninitialized)**| 초기값이 없는 전역/정적 변수 (0 초기화) | 적재 시 | 고정 (Fixed) | Read, Write |
| **Heap** | 런타임 동적 할당 메모리 | 런타임 동적 | 가변 (저위 -> 고위 주소 확장)| Read, Write |
| **Stack** | 함수 호출 프레임, 로컬 변수, 반환 주소 | 함수 호출 시 | 가변 (고위 -> 저위 주소 확장)| Read, Write |""",
        "sources": [
            "Abraham Silberschatz et al. - Operating System Concepts: Processes and Memory Layout",
            "Michael Kerrisk - The Linux Programming Interface: Process Memory",
            "Computer Systems: A Programmer's Perspective (CS:APP) - Virtual Memory"
        ],
        "connections": "- 상위 토픽: [023 가상 메모리](./023_virtual_memory.md)\n- 연관 토픽: [052 메모리 누수](./052_memory_leak.md), [071 세그멘테이션 폴트](./071_segmentation_fault.md)"
    },

    "051_cache_memory.md": {
        "insight": "CPU와 저속 메인 메모리 간의 속도 격차를 완화하기 위해 참조 국소성(Locality)을 바탕으로 초고속 SRAM 계층을 다단계로 배치한 임시 저장소임.",
        "text_replacements": [],
        "rec_text": "캐시 미스 페널티를 줄이기 위해 L1/L2/L3 계층적 캐시 사이징을 최적화하고, 데이터 배열 순회 시 시간적/공간적 지역성을 보장하도록 캐시 친화적(Cache-Friendly) 알고리즘 설계.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────┐
│ [ CPU 코어 및 다계층 캐시 메모리 계층 구조 ]           │
│                                                        │
│  [ CPU Core (ALU / Register) ]                         │
│            │ (< 1ns)                                   │
│            ▼                                           │
│  [ L1 캐시 (명령어 I-Cache / 데이터 D-Cache 각 32~64KB) ]│
│            │ (~ 1ns, 코어 내부 전용)                    │
│            ▼                                           │
│  [ L2 캐시 (코어 전용 중형 캐시, 512KB ~ 1MB) ]        │
│            │ (~ 3ns)                                   │
│            ▼                                           │
│  [ L3 캐시 (모든 코어가 공유하는 Last Level Cache, 수십 MB) ]│
│            │ (~ 10ns, 코어 간 데이터 공유 및 일관성 허브)│
│            ▼                                           │
│  [ 메인 메모리 (DRAM, 50~100ns 지연 시간 발생) ]        │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 캐시 매핑 방식 | 동작 메커니즘 | 하드웨어 복잡도 | 캐시 적중률 | 주요 장단점 |
|---|---|---|---|---|
| **직접 매핑 (Direct Mapping)** | 메모리 블록이 정해진 1개 캐시 슬롯에만 매핑 | 가장 단순 | 가장 낮음 | 검색 속도 최고, 동일 슬롯 충돌 미스 빈발 |
| **연관 매핑 (Fully Associative)**| 메모리 블록이 캐시의 빈 슬롯 어디든 저장 가능 | 최고 (복잡) | 가장 높음 | 충돌 미스 전무, 모든 태그 병렬 비교 비용 폭증 |
| **세트 연관 매핑 (Set-Associative)**| 캐시를 여러 세트로 나누고 세트 내 N개 슬롯 배치 | 중간 수준 | 우수함 | 직접 매핑과 연관 매핑의 장점 절충 (현대 CPU 표준) |""",
        "sources": [
            "John L. Hennessy, David A. Patterson - Computer Architecture: Memory Hierarchy Design",
            "Intel 64 and IA-32 Architectures Optimization Reference Manual: Cache Considerations",
            "ACM Computing Surveys: Cache Memories and Memory Hierarchy"
        ],
        "connections": "- 상위 토픽: [076 CPU](./076_cpu.md)\n- 연관 토픽: [040 캐시 일관성](./040_cache_coherence.md), [057 메모리 인터리빙](./057_memory_interleaving.md)"
    },

    "052_memory_leak.md": {
        "insight": "할당받은 동적 메모리를 참조 해제하지 않거나 포인터를 유실하여 가용 메모리가 점진적으로 고갈되고 시스템 OOM 다운을 초래하는 결함 현상임.",
        "text_replacements": [
            ("부하를 주며 반복 실행해 메모리 추세를 관찰하고 할당·해제 지점을 추적하거나 덤프를 분석해 누수 객체나 미반환 핸들을 찾는다.",
             "부하 테스트를 반복 실행하여 힙 메모리 증가 추세를 프로파일링하고 힙 덤프 분석을 통해 누수 객체 및 미해제 핸들 식별.")
        ],
        "rec_text": "C/C++에서는 RAII 패턴과 스마트 포인터(unique_ptr)를 강제하고, Java/JVM 환경에서는 static 컬렉션 잔존 참조를 방지하며 CI/CD 파이프라인에 정적 메모리 분석 도구 연동.",
        "rec_diagram": """```text
[ 메모리 누수 발생 및 OOM Killer 동작 시퀀스 ]

 1. 힙 메모리 할당 (malloc / new)
       │
 2. 비즈니스 로직 수행 완료
       │
 3. 메모리 해제 누락 (free 누락 / 정적 컬렉션 무한 참조)
       │
       ▼
 [ 시간 경과에 따른 가용 물리 메모리 점진적 고갈 ]
       │
       ▼
 [ OS 스왑 메모리까지 포화 및 극심한 스래싱 발생 ]
       │
       ▼
 [ 리눅스 OOM Killer(Out of Memory Killer) 발동 ] ──> [ 핵심 비즈니스 프로세스 강제 강등 종료 ]
```""",
        "rec_table": """| 진단 및 예방 도구 | 동작 방식 | 적용 개발 언어 | 주요 특징 및 검출 대상 |
|---|---|---|---|
| **Valgrind (Memcheck)** | 가상화 런타임 기반 동적 분석 | C, C++ | 미해제 힙 블록, 초기화되지 않은 메모리 접근 |
| **AddressSanitizer (ASan)** | 컴파일러 계측 기반 고속 검출 | C, C++, Rust | 런타임 오버헤드 2배 수준으로 CI 연계 가능 |
| **Eclipse MAT / JProfiler** | JVM 힙 덤프 스냅샷 분석 | Java, Kotlin | GC되지 않는 GC Root 참조 체인 추적 |
| **Pprof** | 프로파일링 샘플링 툴 | Go | 활성 할당 객체 및 고루틴 누수 추적 |""",
        "sources": [
            "CWE-401: Improper Release of Memory Before Removing Last Reference ('Memory Leak')",
            "Oracle JVM Garbage Collection Tuning and Memory Leak Troubleshooting Guide",
            "Valgrind User Manual: Memcheck: A Memory Error Detector"
        ],
        "connections": "- 상위 토픽: [050 프로세스 메모리 구조](./050_process_memory_layout.md)\n- 연관 토픽: [039 스래싱](./039_thrashing.md), [071 세그멘테이션 폴트](./071_segmentation_fault.md)"
    },

    "053_iac.md": {
        "insight": "컴퓨팅, 네트워크, 스토리지 등 인프라 구성을 코드로 정의하고 버전 관리하여 반복 가능하고 일관된 인프라 프로비저닝을 자동화함.",
        "text_replacements": [
            ("코드를 작성하고 상태 저장소와 대조해 실행 계획을 확인한다. 변경을 적용해 인프라를 프로비저닝하고 실제 상태를 저장소에 갱신한다.",
             "인프라 정의 코드를 작성하고 상태 파일(tfstate)과 대조하여 실행 계획(Plan)을 사전 검증. 변경 사항을 적용(Apply)하여 리소스를 프로비저닝하고 형상 갱신.")
        ],
        "rec_text": "인프라 드리프트(Drift)를 실시간 감지하기 위해 상태 파일의 원격 잠금(Locking)을 적용하고, GitOps 워크플로우를 통해 변경 사항의 코드 리뷰와 사전 보안 스캐닝을 의무화.",
        "rec_diagram": """```text
[ 인프라 개발자 ] ──(선언적 HCL 코드 작성: main.tf)──> [ Git 형상 관리 리포지토리 ]
                                                                 │
                                                                 ▼ (CI 파이프라인 트리거)
┌────────────────────────────────────────────────────────────────────────┐
│ [ Terraform Cloud / Runner Engine ]                                    │
│   1. terraform plan : 현재 상태(State)와 원하는 상태(Desired) 비교     │
│   2. tflint & Checkov: 보안 취약점 및 컴플라이언스 정적 분석           │
│   3. terraform apply : 실제 CSP API 호출 프로비저닝                    │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
       ┌───────────────────────────┴───────────────────────────┐
       ▼                                                       ▼
┌──────────────────────────────┐        ┌──────────────────────────────┐
│ [ CSP 원격 인프라 리소스 ]   │        │ [ 원격 상태 저장소 (State) ] │
│  - VPC, 서브넷, 보안그룹     │        │  - AWS S3 + DynamoDB Lock    │
│  - K8s 클러스터, DB 인스턴스 │        │  - 인프라 현실 상태 원장 저장│
└──────────────────────────────┘        └──────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 선언적 IaC (Declarative) | 명령형 IaC (Imperative) |
|---|---|---|
| **접근 방식** | 인프라의 '최종 원하는 상태(What)' 정의 | 상태에 도달하기 위한 '구체적 실행 절차(How)' 정의 |
| **멱등성 (Idempotency)** | 완벽히 보장 (재실행해도 결과 동일) | 보장이 어려움 (스크립트 내 추가 검증 로직 필수) |
| **상태 관리 (State)** | 명시적 상태 파일(tfstate) 유지 관리 | 상태 파일 없음 (현재 인프라 상태 직접 질의) |
| **대표 도구** | Terraform, CloudFormation, Kubernetes YAML | Ansible, Chef, Puppet, AWS CDK |""",
        "sources": [
            "Kief Morris - Infrastructure as Code: Dynamic Systems for the Cloud Age (O'Reilly)",
            "HashiCorp Terraform Architecture and State Management Documentation",
            "NIST Special Publication 800-145: Cloud Automation and Orchestration"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [012 쿠버네티스](./012_kubernetes.md), [054 IaaS](./054_iaas.md)"
    },

    "054_iaas.md": {
        "insight": "가상화된 서버, 스토리지, 네트워크 자원을 온디맨드로 제공하여 사용자가 OS 이상의 소프트웨어 스택 전체를 자유롭게 제어할 수 있는 인프라 서비스임.",
        "text_replacements": [
            ("용량과 네트워크 요구를 정해 자원을 할당하고 게스트 OS와 기본 에이전트를 설치한다. 운영 중에는 패치·백업·모니터링을 직접 수행한다.",
             "컴퓨팅 용량과 네트워크 인터페이스를 정의하여 가상머신을 프로비저닝하고 게스트 OS 및 모니터링 에이전트를 설치. 운영 단계에서는 OS 보안 패치 및 백업을 고객 책임으로 수행.")
        ],
        "rec_text": "OS 및 미들웨어 계층의 보안 패치 책임이 고객에게 귀속되므로 자동화된 골든 이미지(AMI/Packer) 파이프라인과 중앙 형상 관리 툴을 결합하여 운영 부채를 최소화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ IaaS (Infrastructure as a Service) 책임 및 구성 아키텍처 ]           │
│                                                                        │
│ ┌──────────────────────────────────────────────────────────────────┐   │
│ │ [ 고객 직접 관리 영역 (Customer Responsibility) ]                │   │
│ │   - 사용자 애플리케이션 코드 및 데이터베이스                     │   │
│ │   - 미들웨어 (Web, WAS, Message Queue)                           │   │
│ │   - 게스트 OS (Linux, Windows) 설치, 커널 파라미터, 보안 패치    │   │
│ │   - 방화벽 룰 (보안 그룹), 라우팅 테이블, IAM 접근 권한          │   │
│ └──────────────────────────────────┬───────────────────────────────┘   │
│                                    │ (API 제어 및 가상화 추상화)       │
│ ┌──────────────────────────────────┴───────────────────────────────┐   │
│ │ [ 클라우드 공급자 관리 영역 (CSP Responsibility) ]               │   │
│ │   - 하이퍼바이저 가상화 계층 (KVM, Nitro)                        │   │
│ │   - 물리 서버 하드웨어, 스토리지 랙, 척추망(Spine-Leaf) 패브릭   │   │
│ │   - 전산실 물리 보안, 전력 공급 및 냉각 공조 시설                │   │
│ └──────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| IaaS 핵심 구성 요소 | 기술적 구현체 | 주요 기능 및 역할 | 성능 및 안정성 고려사항 |
|---|---|---|---|
| **컴퓨팅 (Compute)** | 가상 머신 (AWS EC2, Azure VM) | CPU, 메모리 자원 할당 및 인스턴스 구동 | vCPU 오버커밋 비율, 인스턴스 타입 최적화 |
| **스토리지 (Storage)** | 블록(EBS), 객체(S3), 파일(EFS) | 영속 데이터 저장 및 마운트 볼륨 제공 | IOPS 프로비저닝, 데이터 암호화(KMS) |
| **네트워크 (Network)** | VPC, 서브넷, 인터넷 게이트웨이 | 논리적 격리 가상 네트워크망 구축 | 대역폭 한도, 보안 그룹 최소 권한 원칙 |""",
        "sources": [
            "NIST Special Publication 800-145: The IaaS Service Model Definition",
            "ISO/IEC 17788: Cloud computing - Infrastructure as a Service",
            "AWS Well-Architected Framework: Infrastructure Reliability and Security"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [055 PaaS](./055_paas.md), [036 SaaS](./036_saas.md)"
    },

    "055_paas.md": {
        "insight": "애플리케이션 개발, 배포, 실행에 필요한 하드웨어 및 소프트웨어 런타임을 플랫폼 형태로 제공하여 인프라 관리 부담을 제거하고 개발 생산성을 극대화함.",
        "text_replacements": [
            ("코드·설정을 준비해 플랫폼에 배포하면 컨테이너나 런타임에 적재된다. 로깅·모니터링을 확인하고 필요하면 설정을 바꾸거나 확장한다.",
             "소스 코드와 매니페스트를 빌드 팩에 전달하여 런타임 컨테이너로 패키징 및 배포. 관측성 대시보드를 통해 로깅 및 메트릭을 점검하고 오토 스케일링 정책 적용.")
        ],
        "rec_text": "특정 PaaS 벤더의 독점 API 종속을 탈피하기 위해 OCI 표준 컨테이너 및 Knative 기반의 오픈소스 PaaS 아키텍처를 도입하고 CI/CD 파이프라인과 완벽 연동.",
        "rec_diagram": """```text
[ 개발자 (Developer) ] ──(git push / 코드 및 매니페스트 배포)──>
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ [ PaaS 엔진 (Cloud Foundry / OpenShift / App Engine) ]  │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ 빌드팩 (Buildpacks) : 코드 분석 후 런타임 생성 │   │
│   └───────────────────────┬────────────────────────┘   │
│                           ▼                            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 자동 오토 스케일링 & 헬스 체크 컨트롤러        │   │
│   └───────────────────────┬────────────────────────┘   │
│                           ▼                            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 관리형 미들웨어 (Managed DB, Cache, MQ 서비스) │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | IaaS (Infrastructure as a Service) | PaaS (Platform as a Service) |
|---|---|---|
| **개발자 집중 영역** | OS 설정, 미들웨어 구성, 네트워크 방화벽 등 인프라 관리 | 순수 비즈니스 로직 코드 개발 및 데이터베이스 모델링 |
| **운영 및 관리 부담** | 패치, 백업, 스케일링 등 모든 운영 책임이 개발자에게 귀속 | 플랫폼 엔진이 자동 패치, 자동 스케일링, 모니터링 수행 |
| **배포 속도** | VM 프로비저닝 및 소프트웨어 스택 구성에 장시간 소요 | 소스 코드 푸시만으로 수 분 이내 즉각적 빌드 및 배포 완료 |
| **유연성 vs 종속성** | 높은 시스템 제어권과 커스터마이징 가능 (락인 없음) | 플랫폼이 제공하는 언어/프레임워크 제약 및 벤더 락인 위험 |""",
        "sources": [
            "NIST Special Publication 800-145: Platform as a Service (PaaS)",
            "Cloud Native Computing Foundation (CNCF) Cloud Native Application Architecture",
            "Red Hat OpenShift / VMware Tanzu Enterprise PaaS Architecture Guide"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [054 IaaS](./054_iaas.md), [003 서버리스 컴퓨팅](./003_serverless_computing.md)"
    },

    "056_raid.md": {
        "insight": "복수의 물리적 디스크를 단일 논리 볼륨으로 묶고 스트라이핑, 미러링, 패리티 연산을 조합하여 I/O 성능 향상과 내고장성을 동시에 달성하는 스토리지 기술임.",
        "text_replacements": [
            ("디스크 장애를 감지하면 중복 데이터로 오류를 복구한다. 정상 서비스를 유지하면서 새 디스크로 교체하고 백그라운드 리빌드를 진행한다.",
             "디스크 장애 발생 시 패리티 또는 미러링 데이터를 기반으로 데이터를 실시간 복구. 핫스페어 디스크 자동 투입 및 백그라운드 리빌드 수행.")
        ],
        "rec_text": "대용량 고밀도 드라이브 리빌드 시 발생하는 URE(Unrecoverable Read Error)와 추가 디스크 장애를 방지하기 위해 단일 패리티(RAID 5) 대신 이중 패리티(RAID 6) 또는 RAID 10 적용.",
        "rec_diagram": """```text
┌────────────────────────┐              ┌────────────────────────┐
│ [ RAID 0: 스트라이핑 ] │              │ [ RAID 1: 미러링 ]     │
│  - 성능 극대화, 무복구 │              │  - 무손실 복구, 50%용량│
│  [Disk 1]    [Disk 2]  │              │  [Disk 1]    [Disk 2]  │
│  ┌──────┐    ┌──────┐  │              │  ┌──────┐    ┌──────┐  │
│  │ A1   │    │ A2   │  │              │  │ A1   │    │ A1   │  │
│  │ A3   │    │ A4   │  │              │  │ A2   │    │ A2   │  │
│  └──────┘    └──────┘  │              │  └──────┘    └──────┘  │
└────────────────────────┘              └────────────────────────┘
┌────────────────────────────────────────────────────────────────┐
│ [ RAID 5: 분산 단일 패리티 ]            [ RAID 6: 분산 이중 패리티 ] │
│  - 1개 디스크 장애 허용                - 2개 디스크 동시 장애 허용│
│  [Disk 1]  [Disk 2]  [Disk 3]           [Disk 1]  [Disk 2]  [Disk 3]  [Disk 4]│
│  ┌──────┐  ┌──────┐  ┌──────┐           ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐│
│  │ A1   │  │ A2   │  │ Ap   │ (Parity)  │ A1   │  │ A2   │  │ Ap   │  │ Aq   ││
│  │ B1   │  │ Bp   │  │ B2   │           │ B1   │  │ Bp   │  │ Bq   │  │ B2   ││
│  └──────┘  └──────┘  └──────┘           └──────┘  └──────┘  └──────┘  └──────┘│
└────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| RAID 레벨 | 최소 디스크 수 | 가용 용량 효율 | 읽기/쓰기 성능 | 허용 장애 디스크 수 | 주 활용 분야 |
|---|---|---|---|---|---|
| **RAID 0** | 2 | 100% (N) | 최고 / 최고 | **0개 (결함 허용 전무)**| 임시 영상 렌더링, 스크래치 디스크 |
| **RAID 1** | 2 | 50% (N/2) | 빠름 / 보통 | 1개 | OS 부팅 디스크, 소규모 트랜잭션 로그 |
| **RAID 5** | 3 | $(N-1)/N$ | 빠름 / 쓰기 패리티 저하| 1개 | 범용 파일 서버, 웹 데이터 저장소 |
| **RAID 6** | 4 | $(N-2)/N$ | 빠름 / 이중 패리티 오버헤드| **2개** | 대용량 아카이브, 고밀도 HDD 팜 |
| **RAID 10**| 4 | 50% (N/2) | 매우 빠름 / 매우 빠름 | 세트당 1개 (최대 N/2) | 고성능 RDBMS, 금융 핵심 원장 DB |""",
        "sources": [
            "David A. Patterson, Garth Gibson, Randy H. Katz - A Case for Redundant Arrays of Inexpensive Disks (RAID)",
            "Storage Networking Industry Association (SNIA) RAID Technology Guide",
            "IEEE Transactions on Reliability: Data Reliability and Rebuild Analysis of RAID"
        ],
        "connections": "- 상위 토픽: [024 디스크 스케줄링](./024_disk_scheduling.md)\n- 연관 토픽: [084 SAN](./084_san.md), [080 NAS](./080_nas.md)"
    },

    "057_memory_interleaving.md": {
        "insight": "연속된 메모리 주소를 여러 개의 독립 메모리 뱅크에 교차 배치하여 메모리 접근을 동시 병렬 처리함으로써 시스템 버스 대역폭을 극대화함.",
        "text_replacements": [],
        "rec_text": "연속 메모리 순회 시 단일 뱅크 충돌(Bank Conflict)을 원천 방지하기 위해 하위 비트 인터리빙을 채택하고, 멀티소켓 서버 환경에서는 NUMA 인터리빙 메모리 정책을 워크로드별 최적화.",
        "rec_diagram": """```text
[ 하위 비트 메모리 인터리빙 (Low-Order Interleaving: 4-Way Bank) ]

  연속 물리 주소 스트림: 0, 1, 2, 3, 4, 5, 6, 7 ...
                         │
        ┌────────────────┼────────────────┬────────────────┐
        ▼                ▼                ▼                ▼
   [ Bank 0 ]       [ Bank 1 ]       [ Bank 2 ]       [ Bank 3 ]
   ┌────────┐       ┌────────┐       ┌────────┐       ┌────────┐
   │ Addr 0 │       │ Addr 1 │       │ Addr 2 │       │ Addr 3 │
   │ Addr 4 │       │ Addr 5 │       │ Addr 6 │       │ Addr 7 │
   └────────┘       └────────┘       └────────┘       └────────┘
       ▲                ▲                ▲                ▲
       └────────────────┴───────┬────────┴────────────────┘
                                │
                  [ 병렬 동시 데이터 읽기/쓰기 버스 ]
                  (메모리 모듈 사이클 시간의 1/4로 접근 지연 단축)
```""",
        "rec_table": """| 인터리빙 방식 | 주소 비트 매핑 방식 | 메모리 뱅크 접근 패턴 | 연속 블록 전송 효율 | 주 활용 영역 |
|---|---|---|---|---|
| **하위 인터리빙 (Low-Order)** | 주소의 최하위 비트(LSB)로 뱅크 결정 | 연속된 주소가 서로 다른 뱅크에 분산 | **최고 (모든 뱅크 동시 가동)** | 고성능 CPU 메인 메모리, 캐시 라인 채움 |
| **상위 인터리빙 (High-Order)**| 주소의 최상위 비트(MSB)로 뱅크 결정 | 한 뱅크가 완전히 찬 후 다음 뱅크 접근| 낮음 (한 시점에 1개 뱅크만 동작) | 메모리 뱅크 단위 모듈 확장, 결함 격리 |""",
        "sources": [
            "John L. Hennessy, David A. Patterson - Computer Architecture: A Quantitative Approach (Memory Hierarchy)",
            "IEEE Transactions on Computers: Performance of Interleaved Memory Systems",
            "JEDEC DDR4/DDR5 SDRAM Standard: Bank Architecture and Burst Operation"
        ],
        "connections": "- 상위 토픽: [096 메모리 계층 및 인터리빙](./096_memory_hierarchy_interleaving.md)\n- 연관 토픽: [051 캐시 메모리](./051_cache_memory.md), [023 가상 메모리](./023_virtual_memory.md)"
    },

    "058_segmentation.md": {
        "insight": "프로그램을 코드, 데이터, 스택, 서브루틴 등 의미론적 논리 단위(세그먼트)로 가변 분할하여 보호와 공유를 용이하게 하는 메모리 관리 기법임.",
        "text_replacements": [],
        "rec_text": "가변 크기 할당으로 인한 심각한 외부 단편화를 해결하기 위해 순수 세그멘테이션 대신 세그먼트를 내부적으로 고정 크기 페이지로 재분할하는 세그멘테이션 페이징 혼용 기법 적용.",
        "rec_diagram": """```text
[ 세그멘테이션 논리 주소 (Logical Address) : < s (세그먼트 번호), d (변위 Offset) > ]
                                               │
                                               ▼
                              ┌───────────────────────────────────┐
                              │ [ 세그멘테이션 테이블 검색 ]       │
                              │  Segment s: < Limit 한도, Base 기준 >│
                              └─────────────────┬─────────────────┘
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 │ 변위 d < Limit 검증 성공                                    │ 변위 d >= Limit 위반
                 ▼                                                             ▼
┌─────────────────────────────────┐                          ┌───────────────────────────────────┐
│ 물리 주소 = Base + d 즉시 산출  │                          │ 트랩 (Trap): 세그멘테이션 폴트     │
└────────────────┬────────────────┘                          └───────────────────────────────────┘
                 │
                 ▼
[ 실제 물리 메모리(DRAM) 접근 완료 ]
```""",
        "rec_table": """| 비교 축 | 페이징 (Paging) | 세그멘테이션 (Segmentation) |
|---|---|---|
| **분할 기준** | 물리적 고정 크기 블록 (예: 4KB Page) | 프로그래머 관점의 논리적 가변 크기 단위 (함수, 객체) |
| **주소 구조** | 1차원 선형 주소 (페이지 번호 + 오프셋) | 2차원 논리 주소 (세그먼트 이름/번호 + 오프셋) |
| **단편화 문제** | 내부 단편화 발생 (마지막 페이지 여분 낭비) | **외부 단편화 발생** (메모리 홀 조각화 현상) |
| **공유 및 보호** | 페이지 단위 일괄 적용 (세분화 어려움) | 세그먼트별 읽기/쓰기/실행 권한 부여 및 공유 용이 |""",
        "sources": [
            "Abraham Silberschatz et al. - Operating System Concepts: Memory-Management (Segmentation)",
            "Andrew S. Tanenbaum - Modern Operating Systems: Segmentation",
            "Intel 64 and IA-32 Architectures Software Developer's Manual, Volume 3A: System Programming Guide (Segmentation)"
        ],
        "connections": "- 상위 토픽: [023 가상 메모리](./023_virtual_memory.md)\n- 연관 토픽: [060 페이징](./060_paging.md), [071 세그멘테이션 폴트](./071_segmentation_fault.md)"
    },

    "059_priority_inversion.md": {
        "insight": "낮은 우선순위 태스크가 점유한 공유 자원을 높은 우선순위 태스크가 대기하는 동안 중간 우선순위 태스크가 선점하여 최고 우선순위 태스크의 실행이 무한 지연되는 현상임.",
        "text_replacements": [
            ("낮은 우선순위 L이 락을 쥔 상태에서 중간 M이 CPU를 가로채면 높은 H가 무한정 밀린다. L의 우선순위를 임시로 높이거나 천장을 적용해 지연을 줄인다.",
             "저우선순위 L이 자원을 선점한 상태에서 중우선순위 M이 CPU를 가로채 고우선순위 H가 무한정 블로킹되는 현상 발생. 우선순위 상속(PIP) 또는 우선순위 천장(PCP) 프로토콜을 적용하여 역전 방지.")
        ],
        "rec_text": "실시간 임베디드 및 미션크리티컬 시스템에서 상호배제 락 사용 시 우선순위 상속(Priority Inheritance) 또는 우선순위 천장(Priority Ceiling) 프로토콜을 커널 뮤텍스에 의무 적용.",
        "rec_diagram": """```text
[ 우선순위 역전 (Priority Inversion) 발생 시나리오 ]

 우선순위
   High (H) ───[H 도착]──────────────┐대기(Blocked)───────────────────>
                                      │ (L이 점유한 자원 R 대기)
   Mid  (M) ──────────────────────────┼────────[M이 L을 선점하여 계속 실행]──>
                                      │
   Low  (L) ──[자원 R 점유]───────────┴───────────────────────────────>
  ───────────────────────────────────────────────────────────────────────> 시간
  * 결과: 최고 우선순위 H가 자원 R과 무관한 중간 우선순위 M 때문에 실행되지 못하는 역전 발생!

[ 해결책: 우선순위 상속 (Priority Inheritance Protocol) ]
  - L이 자원 R을 보유하고 있는 동안, L의 우선순위를 대기 중인 H의 우선순위로 일시 승격!
  - 중간 M이 L을 선점할 수 없도록 방어하여 L이 신속히 자원을 반납하게 유도
```""",
        "rec_table": """| 해결 프로토콜 | 동작 원리 | 교착상태 (Deadlock) 방지 | 다중 블로킹 방지 |
|---|---|---|---|
| **우선순위 상속 (PIP)** | 고우선순위 태스크가 락을 요청하면 락 보유자의 우선순위를 즉시 상속 승격 | 불가 (환형 대기 교착 가능) | 불가 (체인 형태의 연쇄 블로킹 가능) |
| **우선순위 천장 (PCP)** | 자원에 최고 잠재 우선순위(Ceiling)를 부여하고 시스템 천장보다 높아야만 락 획득 | **완벽 방지 (교착 배제 보장)** | **완벽 방지 (최대 1회 단일 블로킹 보장)** |""",
        "sources": [
            "Lui Sha, Ragunathan Rajkumar, John P. Lehoczky - Priority Inheritance Protocols: An Approach to Real-Time Synchronization (IEEE Transactions on Computers)",
            "NASA Mars Pathfinder Priority Inversion Problem Official Case Study",
            "POSIX.1-2008 Standard: Mutex Priority Inheritance and Ceiling Protocols"
        ],
        "connections": "- 상위 토픽: [019 CPU 스케줄링](./019_cpu_scheduling.md)\n- 연관 토픽: [038 데드락](./038_deadlock.md), [122 프로세스 동기화](./122_process_synchronization.md)"
    },

    "060_paging.md": {
        "insight": "가상 주소 공간과 물리 메모리를 동일한 고정 크기 블록(페이지/프레임)으로 분할하여 외부 단편화를 근본적으로 없애는 비연속 메모리 할당 기술임.",
        "text_replacements": [
            ("가상 페이지 번호로 TLB를 조회하고, 미스면 페이지 테이블을 읽어 프레임 번호를 확인한다. 유효하지 않으면 페이지 부재 인터럽트로 처리한다.",
             "가상 페이지 번호로 TLB를 조회하고, 미스 시 페이지 테이블 엔트리(PTE)를 참조하여 프레임 번호 획득. 유효 비트가 0일 경우 페이지 부재 인터럽트로 전이.")
        ],
        "rec_text": "대규모 메모리 환경에서 페이지 테이블 자체의 공간 오버헤드를 줄이기 위해 다단계 계층 페이징 또는 역페이지 테이블(Inverted Page Table)을 적용하고 대용량 HugePage 활용.",
        "rec_diagram": """```text
[ 페이징 가상 주소 -> 물리 주소 변환 아키텍처 ]

 가상 주소 (VA) : [ 가상 페이지 번호 (VPN: 20-bit) | 변위 오프셋 (Offset: 12-bit) ]
                         │                                         │
                         ▼                                         │
               ┌──────────────────────────────┐                    │
               │ [ 페이지 테이블 (Page Table) ]│                    │
               │  Index (VPN) -> Entry (PFN)  │                    │
               └──────────────┬───────────────┘                    │
                              │ 물리 프레임 번호 (PFN: 20-bit)      │
                              ▼                                    ▼
 물리 주소 (PA) : [ 물리 프레임 번호 (PFN: 20-bit) | 변위 오프셋 (Offset: 12-bit) ]
                              │
                              ▼
               [ 물리 메모리(DRAM) 프레임 직접 접근 ]
```""",
        "rec_table": """| 페이징 구조 | 주소 변환 방식 | 페이지 테이블 메모리 점유 | 검색 속도 |
|---|---|---|---|
| **단일 계층 페이징** | 1차원 선형 배열 인덱싱 | 매우 큼 (사용하지 않는 가상 공간도 엔트리 생성) | 가장 빠름 (메모리 참조 1회) |
| **다단계 페이징 (Multi-level)**| 트리 형태의 계층적 분할 참조 | 작음 (실제 사용 중인 영역만 하위 테이블 생성) | 계층 수만큼 메모리 추가 참조 발생 |
| **역페이지 테이블 (Inverted)** | 물리 프레임 번호당 1개 엔트리 (해싱) | 극소 (물리 메모리 크기에 비례) | 해시 충돌 체이닝으로 검색 시간 가변 |""",
        "sources": [
            "Abraham Silberschatz et al. - Operating System Concepts: Paging",
            "Andrew S. Tanenbaum - Modern Operating Systems: Paging and Page Tables",
            "Intel 64 and IA-32 Architectures Software Developer's Manual: 4-Level and 5-Level Paging"
        ],
        "connections": "- 상위 토픽: [023 가상 메모리](./023_virtual_memory.md)\n- 연관 토픽: [058 세그멘테이션](./058_segmentation.md), [039 스래싱](./039_thrashing.md)"
    },

    "061_hypervisor.md": {
        "insight": "단일 물리 하드웨어 상에서 복수의 이기종 게스트 운영체제를 동시에 독립 실행할 수 있도록 CPU, 메모리, I/O 자원을 가상화하고 중재하는 핵심 소프트웨어 계층임.",
        "text_replacements": [
            ("게스트가 vCPU·메모리·장치를 요청하면 에뮬레이션 또는 반가상화 드라이버를 통해 물리 자원에 매핑된다. 호스트 커널이나 하드웨어 확장이 이를 중재한다.",
             "게스트 OS의 가상 하드웨어 요청을 VT-x 하드웨어 가속 또는 VirtIO 반가상화 인터페이스를 통해 물리 자원에 직결 매핑.")
        ],
        "rec_text": "엔터프라이즈 가상화 환경에서는 하이퍼바이저 오버헤드가 최소화된 Type-1 베어메탈(KVM/ESXi)을 채택하고, SR-IOV 및 DPDK를 결합하여 물리 장치 수준의 I/O 처리량 달성.",
        "rec_diagram": """```text
┌─────────────────────────────────┐     ┌─────────────────────────────────┐
│ [ Type-1 : 베어메탈 하이퍼바이저 ]│     │ [ Type-2 : 호스티드 하이퍼바이저 ]│
│                                 │     │                                 │
│  ┌───────────┐   ┌───────────┐  │     │  ┌───────────┐   ┌───────────┐  │
│  │ Guest OS1 │   │ Guest OS2 │  │     │  │ Guest OS1 │   │ Guest OS2 │  │
│  └─────┬─────┘   └─────┬─────┘  │     │  └─────┬─────┘   └─────┬─────┘  │
│        ▼               ▼        │     │        ▼               ▼        │
│  ┌───────────────────────────┐  │     │  ┌───────────────────────────┐  │
│  │ Hypervisor (ESXi, KVM, Xen)│ │     │  │ Hypervisor (VirtualBox, etc)│ │
│  └─────────────┬─────────────┘  │     │  └─────────────┬─────────────┘  │
│                ▼                │     │                ▼                │
│  ┌───────────────────────────┐  │     │  ┌───────────────────────────┐  │
│  │ 물리 하드웨어 (Bare-Metal) │  │     │  │ 호스트 OS (Windows / Linux)│ │
│  └───────────────────────────┘  │     │  └─────────────┬─────────────┘  │
│                                 │     │                ▼                │
│                                 │     │  ┌───────────────────────────┐  │
│                                 │     │  │ 물리 하드웨어 (Host HW)   │  │
│                                 │     │  └───────────────────────────┘  │
└─────────────────────────────────┘     └─────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | Type-1 하이퍼바이저 (Bare-Metal) | Type-2 하이퍼바이저 (Hosted) |
|---|---|---|
| **설치 계층** | 베어메탈 물리 서버 하드웨어 바로 위에 직접 설치 | 기존 호스트 운영체제(Windows/Linux) 상에 앱 형태로 설치 |
| **성능 및 지연**| 고성능, 초저지연 (하드웨어 직접 제어) | 호스트 OS 오버헤드로 인해 상대적으로 느림 |
| **주요 적용 영역** | 데이터센터 전산실, 엔터프라이즈 클라우드 인프라 | 개인 개발자 PC 테스트 환경, 데스크톱 가상화 실습 |
| **대표 제품** | VMware ESXi, Linux KVM, Xen, Microsoft Hyper-V | Oracle VirtualBox, VMware Workstation |""",
        "sources": [
            "Gerald J. Popek, Robert P. Goldberg - Formal Requirements for Virtualizable Third Generation Architectures (CACM)",
            "VMware vSphere Architecture and Performance Best Practices",
            "Red Hat Enterprise Linux Virtualization Guide: KVM Architecture"
        ],
        "connections": "- 상위 토픽: [085 가상머신](./085_virtual_machine.md)\n- 연관 토픽: [032 컨테이너](./032_container.md), [037 VDI](./037_vdi.md)"
    },

    "062_ai_factory_gw_datacenter.md": {
        "insight": "초거대 파운데이션 모델 학습을 위해 기가와트(GW)급 전력 수전 인프라와 첨단 액체 냉각 및 초고속 광패브릭을 집적한 산업 혁명형 AI 전용 데이터센터임.",
        "text_replacements": [],
        "rec_text": "원전 연계 및 소형 모듈 원자로(SMR) 기반의 독립 전력망을 구축하고, 랙당 100kW 이상의 열밀도를 해소하기 위해 100% 액체 냉각(Direct Liquid Cooling) 인프라 도입 필수.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 기가와트(GW)급 AI 팩토리 데이터센터 에너지-컴퓨팅 통합 아키텍처 ]   │
│                                                                        │
│   [ 에너지 인프라 ] SMR 원자력 발전 / 대규모 신재생 ──(특고압 GW 수전)──┐
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 초고밀도 AI 컴퓨팅 클러스터 (수만~수십만 개 가속기 집적)       │   │
│   │   - 100kW ~ 200kW 초고밀도 수랭식 서버 랙 (Direct Liquid)     │   │
│   │   - 800G / 1.6T 광학 서킷 스위칭(OCS) 무손실 패브릭 망        │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │                                    │
│   ┌───────────────────────────────┴────────────────────────────────┐   │
│   │ 폐열 재활용 및 지속 가능성 계층                                │   │
│   │   - 냉각수 폐열을 지역 난방 및 산업 온수로 100% 재활용         │   │
│   │   - PUE 1.1 이하 및 무탄소(Carbon-Free) 달성                   │   │
│   └────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 인프라 영역 | 전통적 데이터센터 (IDC) | 기가와트(GW)급 AI 팩토리 |
|---|---|---|
| **수전 전력 규모** | 20 ~ 50 MW 수준 (변전소 인입) | **1 ~ 5 GW+ (원자력/SMR 단독 발전소 연계)** |
| **랙당 전력 밀도** | 5 ~ 15 kW (공랭식 쿨링) | **100 ~ 250 kW+ (전면 액체 냉각/액침 냉각)** |
| **핵심 워크로드** | 웹/앱 서빙, 데이터베이스, ERP | 수천억 파라미터 LLM 분산 사전학습 및 멀티모달 |
| **내부 네트워크** | 10G/40G Spine-Leaf IP 망 | 800G/1.6T RoCEv2 / InfiniBand 무손실 패브릭 |""",
        "sources": [
            "NVIDIA AI Factory Architecture Whitepaper: Building the Infrastructure of the Intelligence Age",
            "Uptime Institute: The Impact of AI Workloads on Data Center Power and Cooling Infrastructure",
            "International Energy Agency (IEA): Electricity Grids and Data Centers Energy Outlook"
        ],
        "connections": "- 상위 토픽: [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md)\n- 연관 토픽: [028 액체 냉각](./028_liquid_cooling.md), [114 반도체 인프라 전력 용수](./114_semiconductor_infrastructure_power_water.md)"
    },

    "063_cxl.md": {
        "insight": "PCIe 물리 계층 위에서 CPU, GPU, 메모리, 가속기 간의 고속 캐시 일관성과 메모리 공유를 지원하는 개방형 산업 표준 인터커넥트 기술임.",
        "text_replacements": [],
        "rec_text": "초대형 LLM 추론 시 호스트 메모리 부족 문제를 해결하기 위해 CXL Type 3 메모리 확장기를 도입하고, CXL 3.0 스위치를 통해 서버 랙 단위 메모리 풀링 및 동적 세분화 적용.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ CXL (Compute Express Link) 3대 프로토콜 스택 아키텍처 ]              │
│                                                                        │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐     │
│   │      CXL.io      │  │    CXL.cache     │  │     CXL.mem      │     │
│   │ (초기화/장치제어)│  │ (가속기 캐싱지원)│  │ (호스트 메모리접근)│   │
│   └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘     │
│            │                     │                     │               │
│            ▼                     ▼                     ▼               │
│   ┌──────────────────────────────────────────────────────────────┐     │
│   │ CXL 링크 및 중재 계층 (Arbitration & Multiplexing: ARB/MUX)   │     │
│   └──────────────────────────────┬───────────────────────────────┘     │
│                                  │                                     │
│                                  ▼                                     │
│   ┌──────────────────────────────────────────────────────────────┐     │
│   │ PCIe 5.0 / 6.0 물리 계층 (32 GT/s ~ 64 GT/s PAM4 초고속 전송) │     │
│   └──────────────────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| CXL 장치 유형 | 지원 프로토콜 조합 | 대표 디바이스 | 핵심 동작 특징 |
|---|---|---|---|
| **Type 1** | CXL.io + CXL.cache | 스마트 NIC, DPU, 보안 가속기 | 가속기가 호스트 CPU 메모리를 직접 캐싱하여 초고속 처리 |
| **Type 2** | CXL.io + CXL.cache + CXL.mem | 고성능 GPU, AI FPGA 가속기 | 호스트와 디바이스가 서로의 메모리를 양방향 캐시 일관성 공유 |
| **Type 3** | CXL.io + CXL.mem | CXL 메모리 확장기, 메모리 풀 | 호스트 CPU가 CXL 버스 상의 외부 메모리를 바이트 단위 직접 접근 |""",
        "sources": [
            "Compute Express Link (CXL) Consortium Standard Specifications 1.1 / 2.0 / 3.0 / 3.1",
            "IEEE Micro: Compute Express Link: An Open Industry-Standard Interconnect",
            "Samsung / SK Hynix CXL Memory Module and Software Ecosystem Roadmap"
        ],
        "connections": "- 상위 토픽: [026 CXL 4.0 메모리 풀링](./026_cxl_4_0_memory_pooling.md)\n- 연관 토픽: [079 HBM](./079_hbm.md), [096 메모리 계층 및 인터리빙](./096_memory_hierarchy_interleaving.md)"
    },

    "064_hpa.md": {
        "insight": "쿠버네티스 파드의 리소스 부하(CPU/메모리) 및 사용자 정의 비즈니스 메트릭을 실시간 감지하여 파드 복제본 수를 자동 동적 증감시키는 오토 스케일러임.",
        "text_replacements": [],
        "rec_text": "CPU 등 단순 반응형 지표 외에 메시지 큐 적재량 기반의 KEDA(Kubernetes Event-driven Autoscaling)를 결합하여 트래픽 스파이크 발생 전 선제적 파드 스케일아웃 달성.",
        "rec_diagram": """```text
[ 트래픽 유입 급증 ] ──> [ Pod CPU / Custom Metrics 상승 ]
                                  │
                                  ▼
┌────────────────────────────────────────────────────────┐
│ [ Kubernetes Metrics Server & Prometheus Adapter ]      │
│   - Pod 리소스 실시간 수집 (15초 주기)                 │
│   - Custom Metrics API 제공                            │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ HPA 컨트롤러 루프 (Horizontal Pod Autoscaler Loop) ] │
│                                                        │
│             ┌                                   ┐      │
│   원하는 복제본 =  현재 복제본 * ┌ 현재 메트릭 값  ┐   │
│             │                  └ 목표 메트릭 값  ┘     │
│             └                                   ┘      │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ Deployment / ReplicaSet Spec 업데이트 ]              │
│   - Scale-Out: 신규 Pod 스케줄링 및 트래픽 분산        │
│   - Scale-In : 쿨다운(Stabilization Window) 후 Pod 종료 │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 스케일링 메트릭 유형 | 수집 경로 | 대표 지표 예시 | 실무 활용 시 고려사항 |
|---|---|---|---|
| **자원 메트릭 (Resource)** | Metrics Server | CPU 이용률, 메모리 사용량 | 메모리 누수 시 불필요한 무한 확장 위험 |
| **커스텀 메트릭 (Custom)** | Prometheus Adapter | 초당 HTTP 요청 수(RPS), 활성 세션 수 | 애플리케이션 실제 부하와 직결되는 핵심 지표 |
| **외부 메트릭 (External)**| KEDA / CloudWatch Adapter | SQS 대기 큐 길이, Kafka 컨슈머 랙 | 이벤트 기반 백엔드 작업자(Worker) 스케일링 최적 |""",
        "sources": [
            "Kubernetes Documentation: Horizontal Pod Autoscaling Architecture",
            "CNCF KEDA (Kubernetes Event-driven Autoscaling) Specification",
            "Google Cloud: Best Practices for Autoscaling Kubernetes Pods"
        ],
        "connections": "- 상위 토픽: [012 쿠버네티스](./012_kubernetes.md)\n- 연관 토픽: [025 오토 스케일링](./025_auto_scaling.md), [003 서버리스 컴퓨팅](./003_serverless_computing.md)"
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
