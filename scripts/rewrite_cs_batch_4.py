import os
import re
from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

DATA = {
    "065_multi_region_active_active_dr.md": {
        "insight": "복수의 지리적 리전에 동일한 애플리케이션을 상시 동시 가동하고 양방향 데이터 복제와 지능형 GSLB를 적용하여 다운타임 제로를 달성함.",
        "text_replacements": [
            ("각 리전의 상태와 지연을 글로벌 라우팅에 반영하고, 장애 시 트래픽을 재분배하며 잔여 용량을 확인한다.",
             "각 리전의 상태와 네트워크 RTT 지연을 글로벌 GSLB 라우팅에 실시간 반영하고, 장애 시 트래픽을 즉시 재분배하며 잔여 용량 확인.")
        ],
        "rec_text": "원거리 네트워크 지연(Latency)으로 인한 트랜잭션 충돌을 차단하기 위해 데이터 쓰기 샤딩을 적용하고, 비동기 복제 환경에서는 CRDT 또는 LWW 충돌 해결 정책 필수.",
        "rec_diagram": """```text
                        [ 글로벌 사용자 트래픽 ]
                                   │
                                   ▼
             ┌───────────────────────────────────────────┐
             │ [ Anycast DNS / 글로벌 로드밸런서 (GSLB) ] │
             │  - 지연 시간 기반 최적 리전 트래픽 라우팅 │
             └─────────────┬───────────────────────────┬─┘
                           │                           │
         ┌─────────────────┴─────────┐       ┌─────────┴─────────────────┐
         ▼                           ▼       ▼                           ▼
┌──────────────────────────────┐                   ┌──────────────────────────────┐
│ [ Region A (서울 리전) ]     │                   │ [ Region B (도쿄 리전) ]     │
│  - Active 웹/앱 서비스 클러스터│<─────────────────>│  - Active 웹/앱 서비스 클러스터│
│  - 글로벌 분산 데이터베이스  │ 양방향 비동기 복제│  - 글로벌 분산 데이터베이스  │
│  (CockroachDB / Spanner)     │ (CRDT / Raft 합의)│  (CockroachDB / Spanner)     │
└──────────────────────────────┘                   └──────────────────────────────┘
```""",
        "rec_table": """| DR 아키텍처 모델 | RTO (복구 목표 시간) | RPO (복구 시점 목표) | 인프라 가동률 | 데이터 일관성 복잡도 |
|---|---|---|---|---|
| **Active-Standby (Hot)** | 수 분 ~ 수십 분 | 수 초 ~ 수 분 (비동기) | 50% (Standby 유휴 자원) | 단순 (단방향 복제) |
| **Active-Active (동일존)**| 즉시 (수 초 이내) | 0 (동기 복제) | 100% (양 노드 부하 분산) | 보통 (동기 잠금 오버헤드) |
| **멀티 리전 Active-Active**| **0 (즉시 무중단)** | **~ 0 (준동기/글로벌 합의)**| **100% (글로벌 트래픽 분산)**| **최고 (원거리 지연 및 충돌 제어)**|""",
        "sources": [
            "AWS Well-Architected Framework: Multi-Region Active-Active Architecture",
            "Google Cloud Spanner: TrueTime and External Consistency Architecture",
            "IEEE Transactions on Parallel and Distributed Systems: Multi-Region Disaster Recovery"
        ],
        "connections": "- 상위 토픽: [043 데이터센터 입지 및 재해대응](./043_datacenter_location_disaster_response.md)\n- 연관 토픽: [049 클라우드 네이티브 DR](./049_cloud_native_disaster_recovery.md), [021 HA](./021_ha.md)"
    },

    "066_sk_hynix_hbm4_mass_production.md": {
        "insight": "SK하이닉스가 TSMC와의 원팀 전략으로 첨단 로직 공정 베이스 다이와 Advanced MR-MUF를 결합하여 2048비트 I/O 기반 HBM4 양산 체제를 구축함.",
        "text_replacements": [
            ("DRAM 웨이퍼를 얇게 가공해 TSV를 형성하고 테스트를 거친 베이스 다이 위에 순차 적층한다. 적층 후 MR-MUF 또는 하이브리드 본딩으로 결합하고 최종 패키징과 테스트를 거쳐 출하한다.",
             "DRAM 웨이퍼 박막화 후 초미세 TSV를 형성하고 검증된 로직 베이스 다이 위에 순차 적층. 적층 후 Advanced MR-MUF 또는 하이브리드 본딩으로 물리 결합하고 최종 패키징 테스트 수행.")
        ],
        "rec_text": "로직 공정 베이스 다이 도입으로 인한 열팽창 계수 불일치를 해결하기 위해 Advanced MR-MUF 공정의 방열성을 극대화하고, 향후 16단 이상의 적층에서는 하이브리드 본딩 기술을 선제 확보.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ SK하이닉스 HBM4 원팀 양산 아키텍처 및 공정 협업 모델 ]               │
│                                                                        │
│   [ DRAM 코어 다이 (SK하이닉스) ]                                      │
│     - 1b/1c 나노 DRAM 웨이퍼 박막화 및 고밀도 TSV 홀 가공              │
│     - Advanced MR-MUF 액체 보호재 주입으로 열 방출 효율 2.5배 개선     │
│                     │                                                  │
│                     ▼ (3D 마이크로 범프 / 하이브리드 본딩 적층)         │
│   [ 베이스 다이 (Base Die: TSMC 첨단 4nm 로직 공정 위탁 생산) ]        │
│     - 2048비트 초광대역 호스트 버스 인터페이스 직접 라우팅             │
│     - 자체 전력 제어 유닛(PMIC) 및 온다이 테스트(BIST) 내장            │
│                     │                                                  │
│                     ▼ (CoWoS 첨단 2.5D 패키징)                         │
│   [ 엔비디아 / 빅테크 AI 가속기(GPU)와 단일 인터포저 위에 최종 실장 ]   │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 핵심 공정 기술 | 적용 방식 | 주요 장점 | 극복 과제 |
|---|---|---|---|
| **Advanced MR-MUF** | 에폭시 액체 성형 컴파운드를 다이 사이에 주입 | 칩 간 간격 극소화, 방열 특성 및 수율 최고 | 초미세 피치 갭 필링(Gap Filling) 정밀도 |
| **하이브리드 본딩 (Direct)**| 솔더 범프 없이 구리(Cu-Cu) 직접 접합 | 인터커넥트 밀도 10배 이상 향상, 칩 높이 축소 | 나노미터급 웨이퍼 평탄화(CMP) 및 초고비용 |
| **TSMC CoWoS 협업** | 실리콘 인터포저 상에 GPU와 HBM4 통합 | 신호 무결성 및 2048비트 와이드 I/O 지원 | 첨단 패키징 라인 쇼티지(병목) 리스크 |""",
        "sources": [
            "SK Hynix Technology Leadership Whitepaper: HBM4 Architecture and Packaging",
            "IEEE International Electron Devices Meeting (IEDM): Advanced Packaging for HBM",
            "TSMC Open Innovation Platform (OIP): CoWoS and 3DFabric Alliances"
        ],
        "connections": "- 상위 토픽: [027 HBM4](./027_hbm4.md)\n- 연관 토픽: [079 HBM](./079_hbm.md), [030 칩렛 UCIe](./030_chiplet_ucie_3_0.md)"
    },

    "067_ualink_1_0.md": {
        "insight": "엔비디아 NVLink 독점에 대응하여 빅테크 연합이 수립한 개방형 AI 가속기 인터커넥트 표준으로, 단일 포드 내 최대 1,024개 가속기를 스케일업 연결함.",
        "text_replacements": [],
        "rec_text": "단일 팟(Pod) 내 초대형 텐서 병렬 학습 시 UALink 스위치를 통해 가속기 간 200Gbps 차동 레인 메모리 직접 접근(Load/Store)을 활성화하고 통신 지연 극소화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ UALink (Ultra Accelerator Link) 1.0 단일 포드 스케일업 패브릭 ]       │
│                                                                        │
│   [ AI 가속기 1 (GPU/TPU) ] <─── UALink 1.0 (200Gbps per Lane) ───> [ AI 가속기 2 ]
│             │                                                              │
│             └──────────────────────────────┬───────────────────────────────┘
│                                            │
│                                            ▼
│                 ┌───────────────────────────────────────┐
│                 │ [ UALink 스위치 패브릭 (Switch Fabric) ]│
│                 │  - 로드/스토어 메모리 직접 의미론     │
│                 │  - 단일 포드 내 최대 1,024개 가속기 │
│                 │  - 제로 카피 캐시 일관성 패브릭       │
│                 └───────────────────────────────────────┘
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | UALink (Ultra Accelerator Link) | NVLink 5.0 (NVIDIA 독점) | PCIe Gen 6 / CXL |
|---|---|---|---|
| **표준화 주체** | 개방형 컨소시엄 (AMD, Intel, Google, MS 등) | NVIDIA 독점 폐쇄 표준 | PCI-SIG / CXL 컨소시엄 |
| **레인당 전송률** | 200 Gbps PAM4 | 200 Gbps PAM4 | 64 GT/s PAM4 |
| **스케일업 규모** | 단일 포드 내 1,024개 가속기 직접 연결 | 단일 랙 내 72개 GPU (NVL72) | 노드 내부 또는 소규모 풀링 |
| **통신 의미론** | 로드/스토어(Load/Store) 공유 메모리 | NVLink 네트워크 메모리 의미론 | 호스트-디바이스 간 I/O 및 메모리 확장 |""",
        "sources": [
            "Ultra Accelerator Link (UALink) Consortium Specification 1.0",
            "IEEE Micro: Interconnect Technologies for Scaled-Up AI Clusters",
            "Hot Chips: Next-Generation Accelerator Fabrics and Protocols"
        ],
        "connections": "- 상위 토픽: [020 GPU](./020_gpu.md)\n- 연관 토픽: [070 랙 스케일 AI 시스템](./070_rack_scale_ai_system.md), [094 멀티 GPU](./094_multi_gpu.md)"
    },

    "068_multi_region_active_active_disaster_recovery.md": {
        "insight": "지리적으로 분리된 다중 리전에 트래픽을 상시 분산하고 데이터베이스의 멀티 마스터 복제를 통해 단일 리전 재난 시에도 RTO/RPO 제로를 실현함.",
        "text_replacements": [
            ("리전 상태를 확인한 뒤 트래픽을 분배하고, 장애 리전의 부하를 정상 리전으로 전환한다. 양방향 복제와 충돌 해결 규칙을 유지한다.",
             "리전 헬스 상태를 확인한 뒤 GSLB로 트래픽을 지능 분배하고, 장애 리전 부하를 잔여 정상 리전으로 무중단 전환. 양방향 데이터 복제와 LWW(Last Write Wins) 충돌 해결 규칙 유지.")
        ],
        "rec_text": "원거리 데이터 정합성을 유지하기 위해 데이터 쓰기 위치를 사용자 로컬 리전으로 고정하는 데이터 로컬리티(Data Locality) 패턴을 적용하고 비동기 복제 지연을 상시 관측.",
        "rec_diagram": """```text
[ 글로벌 DNS 라우팅 (Route53 / Cloudflare) ]
       │                                  │
       ▼ (정상 상태: 트래픽 50:50 분산)   ▼
┌──────────────────────────────┐   ┌──────────────────────────────┐
│ [ 리전 1: 서울 주센터 ]      │   │ [ 리전 2: 부산 백업센터 ]    │
│  - Active 앱 서버 클러스터   │   │  - Active 앱 서버 클러스터   │
│  - 분산 DB 멀티 리더         │   │  - 분산 DB 멀티 리더         │
└──────────────┬───────────────┘   └──────────────┬───────────────┘
               │                                  │
               └───────── 양방향 비동기 복제 ─────┘
                         (Conflict Resolution)
```""",
        "rec_table": """| 복구 설계 핵심 요소 | 기술적 구현 방안 | 해결해야 할 트레이드오프 |
|---|---|---|
| **트래픽 라우팅** | Anycast BGP, DNS 가중치 기반 라우팅 | DNS TTL 캐싱으로 인한 장애 전환 지연 |
| **데이터 동기화** | 멀티 마스터 양방향 CDC 복제 | 동시 갱신 시 쓰기 충돌(Conflict) 해결 복잡도 |
| **인프라 자동화** | GitOps 기반 인프라 동기화 (IaC) | 리전 간 인프라 형상 드리프트(Drift) 방지 |""",
        "sources": [
            "AWS Architecture Center: Active-Active Multi-Region Disaster Recovery",
            "Google Cloud: Disaster Recovery for Cloud Applications",
            "ISO/IEC 27031: Information technology - Security techniques - ICT readiness for business continuity"
        ],
        "connections": "- 상위 토픽: [065 멀티 리전 액티브-액티브 DR](./065_multi_region_active_active_dr.md)\n- 연관 토픽: [043 데이터센터 입지 및 재해대응](./043_datacenter_location_disaster_response.md), [021 HA](./021_ha.md)"
    },

    "069_dynamic_memory_allocation_segmentation_fault.md": {
        "insight": "런타임 동적 힙 메모리 할당 및 해제 오류로 인해 프로세스가 할당되지 않은 가상 주소나 읽기 전용 영역에 접근할 때 커널이 SIGSEGV로 강제 종료시키는 결함임.",
        "text_replacements": [
            ("잘못된 주소로 접근하면 MMU가 주소 변환을 검사하고 커널이 보호 위반 인터럽트를 전달한다. 시그널 핸들러가 없으면 기본 동작으로 프로세스가 종료되고 코어 덤프가 생성된다.",
             "비인가 가상 주소 접근 시 MMU가 세그먼트/페이지 폴트 트랩을 발생시키고 커널이 SIGSEGV 시그널을 전달. 시그널 핸들러 부재 시 기본 동작으로 프로세스 비정상 강제 종료 및 코어 덤프 생성.")
        ],
        "rec_text": "메모리 오염 및 세그폴트를 원천 방지하기 위해 정적 메모리 정합성 검사(Coverity)와 런타임 AddressSanitizer(ASan)를 CI 단계에 의무 연동하고 스마트 포인터 사용.",
        "rec_diagram": """```text
[ 동적 메모리 할당 결함 및 세그멘테이션 폴트(SIGSEGV) 발생 메커니즘 ]

 1. 힙 메모리 할당: ptr = (char*)malloc(100);
 2. 메모리 조기 해제: free(ptr);
 3. 허상 포인터(Dangling Pointer) 역참조 시도: *ptr = 'A';
                          │
                          ▼
 ┌────────────────────────────────────────────────────────┐
 │ 하드웨어 MMU (Memory Management Unit) 주소 변환 검사    │
 │  - 해당 가상 주소가 현재 유효하지 않거나 권한 위반 감지 │
 └────────────────────────┬───────────────────────────────┘
                          │
                          ▼
 ┌────────────────────────────────────────────────────────┐
 │ OS 커널 트랩 핸들러: SIGSEGV (Signal 11) 프로세스 전송 │
 └────────────────────────┬───────────────────────────────┘
                          │
                          ▼
 ┌────────────────────────────────────────────────────────┐
 │ 프로세스 비정상 종료 (Crash) & 코어 덤프(Core Dump) 생성│
 └────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 동적 메모리 결함 유형 | 발생 원인 | 결과 및 위험성 | 예방 및 검출 방안 |
|---|---|---|---|
| **Use-After-Free (UAF)** | free()로 해제된 힙 메모리 블록을 재참조 | 데이터 오염 및 원격 코드 실행 취약점 | 스마트 포인터, 포인터 해제 후 NULL 대입 |
| **이중 해제 (Double Free)**| 이미 반환된 메모리를 다시 free() 호출 | 메모리 관리자 메타데이터 파괴 | 스마트 포인터, 메모리 할당 래퍼 사용 |
| **버퍼 오버플로우 (Heap)**| 할당된 힙 경계를 초과하여 쓰기 수행 | 인접 데이터 손상 및 임의 코드 실행 | 경계 검사 표준 함수(strlcpy), ASan |
| **널 포인터 역참조** | malloc 실패로 NULL 반환된 포인터 참조 | 프로세스 즉각 크래시 (SIGSEGV) | 할당 후 NULL 검사 의무화, RAII |""",
        "sources": [
            "CWE-416: Use After Free & CWE-415: Double Free Documentation",
            "GNU C Library Reference Manual: Memory Allocation and Freeing",
            "AddressSanitizer (ASan) Architecture: A Fast Memory Error Detector (USENIX ATC)"
        ],
        "connections": "- 상위 토픽: [071 세그멘테이션 폴트](./071_segmentation_fault.md)\n- 연관 토픽: [050 프로세스 메모리 구조](./050_process_memory_layout.md), [052 메모리 누수](./052_memory_leak.md)"
    },

    "070_rack_scale_ai_system.md": {
        "insight": "수십 개의 고성능 GPU와 CPU를 랙 단위의 초고속 NVLink 스위치와 수랭식 인프라로 결합하여 단일 거대 슈퍼 GPU처럼 동작시키는 랙 스케일 컴퓨팅 시스템임.",
        "text_replacements": [],
        "rec_text": "GB200 NVL72 등 100kW 이상의 초고열밀도 AI 랙 도입 시 100% 직접 칩 액체 냉각(DLC)을 필수 구축하고, 랙 내부의 모든 GPU가 단일 NVLink 공유 메모리 공간을 형성하도록 구성.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ NVIDIA GB200 NVL72 랙 스케일 AI 시스템 아키텍처 ]                    │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 18개 컴퓨트 노드 (총 72개 Blackwell GPU + 36개 Grace CPU)     │   │
│   │  - 완전 밀폐형 수랭식 콜드플레이트 순환 (Liquid Cooling)       │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │ 5,184개 구리선 NVLink 카트리지     │
│                                   │ (초저전력 130TB/s 양방향 대역폭)   │
│                                   ▼                                    │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 9개 NVLink 스위치 트레이 (NVLink 5.0 패브릭)                   │   │
│   │  - 72개 GPU 간 논리적 단일 통합 HBM 메모리 공간 (30TB VRAM)    │   │
│   │  - 1.4 ExaFLOPS AI 연산 성능 발휘                              │   │
│   └────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 전통적 서버 클러스터 (Node-Scale) | 랙 스케일 시스템 (Rack-Scale NVL72) |
|---|---|---|
| **GPU 간 연결 방식** | 노드 내부는 NVLink, 노드 간은 InfiniBand/RoCE | **랙 내 72개 GPU 전체가 순수 NVLink 패브릭 직결** |
| **통신 지연 (Latency)**| 노드 간 통신 시 NIC/스위치 경유 (마이크로초) | 순수 구리선 NVLink 다이렉트 전송 (나노초 단위) |
| **단일 메모리 공간** | 노드당 8개 GPU 메모리만 공유 (최대 1~2TB) | **72개 GPU 전체가 단일 30TB VRAM 공유 풀 형성** |
| **전력 및 냉각** | 공랭식 가능 (랙당 15~40kW) | **100% 직접 액체 냉각(DLC) 필수 (랙당 120kW+)** |""",
        "sources": [
            "NVIDIA GB200 NVL72 Architecture Technical Whitepaper",
            "Open Compute Project (OCP) Rack & Power Architecture Specifications",
            "IEEE Micro: The Shift Towards Rack-Scale AI Computing"
        ],
        "connections": "- 상위 토픽: [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md)\n- 연관 토픽: [028 액체 냉각](./028_liquid_cooling.md), [067 UALink 1.0](./067_ualink_1_0.md)"
    },

    "071_segmentation_fault.md": {
        "insight": "프로세스가 자신에게 할당되지 않은 가상 메모리 주소를 참조하거나 읽기 전용 구역에 쓰기를 시도할 때 하드웨어 MMU 트랩을 거쳐 OS가 강제 종료시키는 결함임.",
        "text_replacements": [],
        "rec_text": "세그폴트 발생 시 코어 덤프 파일(`core_pattern`)을 자동 수집하여 GDB로 충돌 스택 트레이스를 분석하고, 정적 분석(SonarQube)과 경계 검사 라이브러리를 의무화.",
        "rec_diagram": """```text
[ 세그멘테이션 폴트(Segmentation Fault) 발생 및 디버깅 시퀀스 ]

 [ C/C++ 프로그램 실행 중 유효하지 않은 포인터 접근 ]
                       │
                       ▼
 [ 하드웨어 MMU 트랩 발생 : Page Fault / Protection Fault ]
                       │
                       ▼
 [ OS 커널 인터럽트 처리 -> 해당 프로세스에 SIGSEGV 전달 ]
                       │
                       ▼
 [ 프로세스 비정상 종료 (Exit Code 139) & 코어 덤프 파일 기록 ]
                       │
                       ▼
 [ GDB 사후 분석: gdb ./app core -> bt (Backtrace) 명령으로 결함 라인 특정 ]
```""",
        "rec_table": """| 세그멘테이션 폴트 주요 원인 | 코드 예시 | 하드웨어/커널 레벨 감지 원리 |
|---|---|---|
| **널 포인터 역참조** | `int *p = NULL; *p = 10;` | 0번지 페이지(첫 4KB)는 MMU에서 미매핑 상태로 보호 |
| **읽기 전용 텍스트 영역 쓰기** | `char *s = "hello"; s[0] = 'H';` | 해당 가상 페이지의 PTE 쓰기(Write) 권한 비트 0 위반 |
| **스택 버퍼 오버플로우** | 큰 배열 선언으로 스택 가드 페이지 침범 | 스택 끝단의 가드 페이지(Guard Page) 접근 트랩 발생 |
| **해제된 힙 메모리 접근** | `free(p); *p = 20;` | glibc 메모리 할당자 메타데이터 훼손 또는 미매핑 페이지 |""",
        "sources": [
            "IEEE Standard for Information Technology - Portable Operating System Interface (POSIX.1): Signal Concepts",
            "Computer Systems: A Programmer's Perspective (CS:APP) - Signals and Virtual Memory",
            "Debugging with GDB: Examining the Stack and Core Files"
        ],
        "connections": "- 상위 토픽: [069 동적 메모리 할당 및 세그폴트](./069_dynamic_memory_allocation_segmentation_fault.md)\n- 연관 토픽: [050 프로세스 메모리 구조](./050_process_memory_layout.md), [058 세그멘테이션](./058_segmentation.md)"
    },

    "072_quantum_technology_nia_iitp.md": {
        "insight": "미래 산업 및 안보 패러다임을 바꿀 3대 축인 양자 컴퓨팅, 양자 암호통신(QKD), 양자 센싱의 핵심 원천 기술 확보를 위한 국가 표준 로드맵임.",
        "text_replacements": [],
        "rec_text": "양자 컴퓨터의 양자 우위 달성에 대비하여 양자내성암호(PQC)로의 선제적 보안 전환을 추진하고, 국가 양자 테스트베드를 활용한 산학연 실증 지원 체계 확립.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 국가 양자 과학기술 3대 축 (Quantum Technology Pillars) 로드맵 ]      │
│                                                                        │
│ 1. 양자 컴퓨팅 (Quantum Computing)                                     │
│    - 초전도 / 이온트랩 / 중성원자 기반 1,000+ 물리 큐비트 시스템 개발   │
│    - 표면 코드 기반 오류 정정 및 양자 알고리즘 실증                   │
│                                                                        │
│ 2. 양자 암호통신 (Quantum Communication)                               │
│    - 양자키분배(QKD) 기반 국가 시험망 구축 및 신뢰 노드 확장           │
│    - 양자내성암호(PQC) 전환 마이그레이션 가이드라인 수립               │
│                                                                        │
│ 3. 양자 센싱 (Quantum Sensing)                                         │
│    - 다이아몬드 NV 센터 기반 극미세 자기장/전기장 정밀 측정            │
│    - GPS 음영 지역 항법, 뇌자도 의료 영상 등 초정밀 센서 상용화        │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 양자 기술 분류 | 핵심 물리 원리 | 주요 활용 영역 | 상용화 성숙도 |
|---|---|---|---|
| **양자 컴퓨팅** | 양자 중첩(Superposition), 양자 얽힘(Entanglement) | 신약 분자 시뮬레이션, 금융 포트폴리오 최적화 | NISQ 단계, 오류 정정 연구 활발 |
| **양자키분배 (QKD)**| 불확정성 원리, 광자 복제 불가능성(No-Cloning) | 금융망, 국가 기밀 통신망 도청 원천 차단 | 상용 통신망 구축 및 표준화 단계 |
| **양자내성암호 (PQC)**| 양자 알고리즘으로 풀기 어려운 수학적 난제(격자) | 전자서명, SSL/TLS 인증서, 암호화 소프트웨어 | NIST 표준 제정 완료, 마이그레이션 시작 |
| **양자 센싱** | 원자 스핀의 외부 환경 극미세 반응 | 지하 매설물 탐사, 양자 중력계, 양자 레이더 | 일부 고정밀 분야 기 상용화 |""",
        "sources": [
            "과학기술정보통신부·한국지능정보사회진흥원(NIA) 국가 양자과학기술 전략 로드맵",
            "정보통신기획평가원(IITP) ICT R&D 중장기 기술 로드맵: 양자 기술",
            "NIST Post-Quantum Cryptography (PQC) Standardization Project"
        ],
        "connections": "- 상위 토픽: [029 양자 오류 정정 윌로우](./029_quantum_error_correction_google_willow.md)\n- 연관 토픽: [115 위상학적 큐비트 마요라나 1](./115_topological_qubit_majorana_1.md), [116 하이브리드 컴퓨팅](./116_hybrid_computing.md)"
    },

    "073_energy_efficient_computing.md": {
        "insight": "컴퓨팅 파워 요구량 폭증과 탄소중립 규제에 대응하여 칩 아키텍처, 펌웨어, OS, 전산실 공조 전 계층에서 전력 대비 연산 효율(TOPS/Watt)을 극대화함.",
        "text_replacements": [],
        "rec_text": "칩셋 수준의 동적 전압/주파수 조절(DVFS)과 클록 게이팅을 활성화하고, 데이터센터 레벨에서는 고효율 액체 냉각과 전력 캡핑(Power Capping)을 결합하여 PUE 1.1 달성.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 전력 효율 컴퓨팅 계층별 최적화 체계 ]                                │
│                                                                        │
│ 1. 실리콘/회로 계층  : FinFET/GAA 3D 트랜지스터, 클록/파워 게이팅       │
│ 2. 프로세서 아키텍처 : ARM big.LITTLE / Intel big.SMALL 이종 코어 결합 │
│ 3. OS 및 커널 계층  : CPU 주파수 동적 스케일링 (DVFS), C-State 수면   │
│ 4. 시설 및 공조 계층 : 직접 칩 액체 냉각(DLC), 외기 프리쿨링 (PUE 1.1) │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 에너지 절감 기술 | 동작 계층 | 핵심 동작 메커니즘 | 절감 효과 |
|---|---|---|---|
| **DVFS (Dynamic Voltage Frequency)**| 프로세서/OS 커널 | 부하에 따라 전압과 동작 클록 주파수를 동적 조절 | 유휴 및 저부하 시 전력 소비 급감 |
| **클록 게이팅 (Clock Gating)** | 하드웨어 논리 회로| 동작하지 않는 연산 유닛의 클록 신호를 차단 | 동적 스위칭 전력 손실 제거 |
| **파워 게이팅 (Power Gating)** | 하드웨어 반도체 | 미사용 회로 블록의 전원 공급 자체를 차단 | 누설 전류(Leakage Current) 차단 |
| **P-State / C-State** | ACPI 표준 인터페이스| 성능 상태(P-State) 및 유휴 수면 상태(C-State) 전환 | OS 레벨 저전력 수면 제어 |""",
        "sources": [
            "John L. Hennessy, David A. Patterson - Computer Architecture: Energy Efficiency and Power Wall",
            "Advanced Configuration and Power Interface (ACPI) Specification",
            "Green Grid Consortium: Data Center Power Usage Effectiveness (PUE) Metrics"
        ],
        "connections": "- 상위 토픽: [028 액체 냉각](./028_liquid_cooling.md)\n- 연관 토픽: [062 AI 팩토리 GW 데이터센터](./062_ai_factory_gw_datacenter.md), [114 반도체 인프라 전력 용수](./114_semiconductor_infrastructure_power_water.md)"
    },

    "074_genetic_algorithm.md": {
        "insight": "다윈의 자연선택과 적자생존 진화론을 모델링하여 선택, 교차, 변이 연산을 반복함으로써 복잡한 비선형 조합 최적화 문제의 전역 최적해를 탐색함.",
        "text_replacements": [],
        "rec_text": "조기 수렴(Premature Convergence)으로 인한 지역 최적점 고착을 방지하기 위해 세대 경과에 따라 변이율을 동적 조정하는 적응형 유전 알고리즘(AGA) 도입 권고.",
        "rec_diagram": """```text
[ 유전 알고리즘 (Genetic Algorithm) 실행 파이프라인 ]

 1. 초기 염색체 모집단 생성 (Random Initialization)
            │
            ▼
 2. 개체별 적합도 함수(Fitness Function) 평가
            │
            ▼
 3. 종료 조건 만족? (최적해 도달 또는 최대 세대수 초과) ──(Yes)──> [ 최적해 반환 ]
            │ (No)
            ▼
 4. 우수 유전자 선택 (Selection: 룰렛 휠, 토너먼트)
            │
            ▼
 5. 유전자 교차 (Crossover: 1점 교차, 2점 교차, 균등 교차)
            │
            ▼
 6. 유전자 돌연변이 (Mutation: 확률적 비트 반전으로 다양성 확보)
            │
            └───────────> [ 차세대 모집단 형성 후 2단계로 루프 ]
```""",
        "rec_table": """| 유전 연산자 | 주요 기법 | 핵심 역할 | 파라미터 영향도 |
|---|---|---|---|
| **선택 (Selection)** | 룰렛 휠(Roulette Wheel), 토너먼트(Tournament) | 적합도가 높은 우수 개체에게 더 높은 번식 기회 부여 | 선택압이 너무 높으면 조기 수렴 위험 |
| **교차 (Crossover)** | 1점(Single-point), 다점(Multi-point), 균등(Uniform) | 부모 염색체의 우수 유전자 조합으로 우수한 자손 생성 | 교차율($P_c$ 보통 0.7~0.9)로 탐색 주도 |
| **변이 (Mutation)** | 비트 반전(Bit-flip), 교환(Swap), 삽입(Insert) | 모집단의 유전적 다양성 유지 및 지역 최적점 탈출 | 변이율($P_m$ 보통 0.001~0.05) 과도 시 무작위 탐색화 |""",
        "sources": [
            "David E. Goldberg - Genetic Algorithms in Search, Optimization, and Machine Learning",
            "John H. Holland - Adaptation in Natural and Artificial Systems (MIT Press)",
            "IEEE Transactions on Evolutionary Computation: Genetic Algorithms and Optimization"
        ],
        "connections": "- 상위 토픽: [098 메타휴리스틱](./098_metaheuristics.md)\n- 연관 토픽: [107 워크플로우 스케줄링 백필](./107_workflow_scheduling_backfill.md), [019 CPU 스케줄링](./019_cpu_scheduling.md)"
    },

    "075_speculative_decoding.md": {
        "insight": "경량의 소형 초안 모델이 K개의 토큰을 선제적으로 생성하고 거대 검증 모델이 이를 단 한 번의 순방향 연산으로 병렬 검증하여 LLM 추론 속도를 2~3배 가속함.",
        "text_replacements": [],
        "rec_text": "초안 모델의 토큰 채택률(Acceptance Rate)을 높이기 위해 타깃 모델과의 어휘 사전(Vocabulary) 일치도를 사전에 확보하고, 거절 샘플링(Rejection Sampling)으로 생성 분포 왜곡 차단.",
        "rec_diagram": """```text
[ 소형 초안 모델 (Draft Model: 1B/3B) ] ──(초고속 순차 자기회귀 생성)──> [ K개 후보 토큰 생성 ]
                                                                             │
                                                                             ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 거대 검증 모델 (Target Model: 70B+) ]                                │
│   - K개 후보 토큰을 입력받아 단 1회의 병렬 순방향 연산(Forward Pass) 수행 │
│   - 거절 샘플링(Rejection Sampling) 기반으로 토큰 수락/거절 여부 판정 │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │
       ┌─────────────────────────────┴─────────────────────────────┐
       ▼                                                           ▼
 [ 수락된 토큰 (Accepted Tokens: m개) ]                      [ 첫 번째 거절 토큰 수정 배정 ]
  - 타깃 모델의 수학적 확률 분포 100% 보존                    - 타깃 모델의 새로운 정답 토큰 1개 추가
```""",
        "rec_table": """| 비교 축 | 표준 자기회귀 디코딩 (Standard AR) | 투기적 디코딩 (Speculative Decoding) |
|---|---|---|
| **토큰 생성 방식** | 매 스텝마다 거대 모델 1회 실행하여 1개 토큰 생성 | 소형 모델이 K개 토큰 선제안 후 거대 모델이 1회 병렬 검증 |
| **GPU 메모리 대역폭**| 매 토큰마다 대규모 가중치를 메모리에서 로드 (메모리 병목)| K개 토큰을 1회 가중치 로드로 병렬 검증 (대역폭 병목 극복) |
| **출력 품질** | 기준 정답 확률 분포 | **기준 모델의 원래 확률 분포와 수학적으로 100% 동일 보장** |
| **추론 지연 시간** | 1x (기준 속도) | **2x ~ 3x+ 대폭 단축 (추론 가속 달성)** |""",
        "sources": [
            "Charlie Chen et al. - Accelerating Large Language Model Decoding with Speculative Sampling (DeepMind)",
            "Yaniv Leviathan et al. - Fast Inference from Transformers via Speculative Decoding (Google Research)",
            "vLLM Documentation: Speculative Decoding and Speculative Models Support"
        ],
        "connections": "- 상위 토픽: [020 GPU](./020_gpu.md)\n- 연관 토픽: [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md), [070 랙 스케일 AI 시스템](./070_rack_scale_ai_system.md)"
    },

    "076_cpu.md": {
        "insight": "메모리에서 명령어를 인출, 해독, 실행하는 컴퓨터의 두뇌로, 파이프라이닝, 슈퍼스칼라, 비순차 실행을 통해 단일 스레드 명령어 처리율(IPC)을 극대화함.",
        "text_replacements": [],
        "rec_text": "분기 예측 실패(Branch Misprediction)로 인한 파이프라인 플러시 페널티를 완화하기 위해 TAGE 분기 예측기와 대용량 비순차 실행(Out-of-Order) 재배치 큐 최적화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 전통적인 현대 고성능 슈퍼스칼라 CPU 코어 아키텍처 ]                 │
│                                                                        │
│   [ 명령어 인출 (Fetch) ] ──> [ 명령어 해독 (Decode) ]                  │
│             │                           │                              │
│             ▼                           ▼                              │
│   [ 분기 예측기 (Branch Predictor) & 명령어 버퍼 ]                     │
│                                         │                              │
│                                         ▼                              │
│   [ 비순차 실행 엔진 (Out-of-Order Execution / Rename Engine) ]        │
│                                         │                              │
│             ┌───────────────────────────┼───────────────────────────┐  │
│             ▼                           ▼                           ▼  │
│        [ ALU 포트 1 ]              [ ALU 포트 2 ]             [ FPU/SIMD ]│
│             │                           │                           │  │
│             └───────────────────────────┼───────────────────────────┘  │
│                                         ▼                              │
│                         [ 명령어 완료 및 퇴역 (Retire / Commit) ]      │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| CPU 성능 향상 기법 | 핵심 메커니즘 | 해결하는 병목 | 주요 리스크 및 한계 |
|---|---|---|---|
| **명령어 파이프라이닝** | 명령어 실행 단계를 N개로 쪼개어 중첩 동시 실행 | CPI 단축, 클록 주파수 향상 | 구조적/데이터/제어 해저드 발생 |
| **슈퍼스칼라 (Superscalar)**| 단일 사이클에 복수의 명령어를 다중 실행 유닛에 동시 발행 | IPC 1 초과 달성 | 회로 복잡도 폭증, 다중 의존성 검사 오버헤드 |
| **비순차 실행 (OoO)** | 데이터 준비가 완료된 명령어부터 순서와 무관하게 선행 실행 | 메모리 로드 지연으로 인한 정체 회피 | 명령어 순서 복원(ROB) 하드웨어 비용 |
| **분기 예측 (Branch Prediction)**| 조건문 분기 방향을 사전 예측하여 투기적 실행 | 파이프라인 정지(Stall) 제거 | 예측 실패 시 파이프라인 플러시 페널티 |""",
        "sources": [
            "John L. Hennessy, David A. Patterson - Computer Architecture: A Quantitative Approach (Instruction-Level Parallelism)",
            "Intel 64 and IA-32 Architectures Software Developer's Manual: Instruction Set Architecture",
            "IEEE Micro: Top Challenges in Modern Microprocessor Architecture"
        ],
        "connections": "- 상위 토픽: [019 CPU 스케줄링](./019_cpu_scheduling.md)\n- 연관 토픽: [020 GPU](./020_gpu.md), [051 캐시 메모리](./051_cache_memory.md)"
    },

    "077_daas.md": {
        "insight": "클라우드 서비스 공급자(CSP)가 가상 데스크톱 환경 전체를 완전 관리형 서비스로 호스팅하여 초기 구축비 없이 즉시 배포하는 구독형 VDI 솔루션임.",
        "text_replacements": [],
        "rec_text": "원격 접속 단말의 개인정보 및 기업 기밀 유출을 방지하기 위해 화면 캡처 방지, 클립보드 차단, 로컬 드라이브 리디렉션 통제를 표준 보안 정책으로 강제.",
        "rec_diagram": """```text
[ 사용자 단말 (BYOD PC / 태블릿 / 씬클라이언트) ]
       │
       │ 암호화된 전용 원격 프로토콜 스트리밍 (PCoIP / Blast / HDX)
       ▼
┌────────────────────────────────────────────────────────┐
│ [ CSP 완전 관리형 DaaS 플랫폼 (AWS WorkSpaces / AVD) ] │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ 인증 및 브로커링 서비스 (SAML 2.0 / Entra ID)   │   │
│   └───────────────────────┬────────────────────────┘   │
│                           ▼                            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 가상 데스크톱 풀 (Windows 11 / Linux VM)       │   │
│   │  - 오토 스케일링 기반 인스턴스 전원 관리       │   │
│   │  - 공유 이미지 배포 및 영속 프로파일 마운트    │   │
│   └───────────────────────┬────────────────────────┘   │
│                           ▼                            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 기업 사내망 전용 연결 (IPsec VPN / Direct Connect)│ │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 사내 구축형 VDI (On-Premises VDI) | 클라우드 서비스형 데스크톱 (DaaS) |
|---|---|---|
| **초기 투자 비용 (CAPEX)**| 서버, SAN 스토리지, VDI 라이선스 등 막대한 초기 투자 | 초기 인프라 구매 비용 전무 (월정액 구독형 OPEX) |
| **운영 및 유지보수** | 하이퍼바이저 패치, 스토리지 용량 증설을 기업이 직접 수행| CSP가 인프라 전 계층(서버, 스토리지, 네트워크) 완전 관리 |
| **확장성 (Scalability)** | 신규 서버 구매 및 랙 실장까지 수 주 ~ 수 개월 소요 | 콘솔 클릭 몇 번으로 수 분 이내 수백 대 즉시 증설/반납 |
| **규제 준수 (망분리)** | 공공/금융의 물리적·논리적 망분리 인증 충족 용이 | 클라우드 보안인증(CSAP) 및 전용 전송망 점검 필수 |""",
        "sources": [
            "Gartner Magic Quadrant for Desktop as a Service (DaaS)",
            "Amazon WorkSpaces / Microsoft Azure Virtual Desktop Architecture Guides",
            "금융보안원: 클라우드 기반 가상 데스크톱(DaaS) 활용 보안 가이드"
        ],
        "connections": "- 상위 토픽: [037 VDI](./037_vdi.md)\n- 연관 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md), [036 SaaS](./036_saas.md)"
    },

    "078_faas.md": {
        "insight": "이벤트 트리거에 반응하여 무상태(Stateless) 단일 함수 단위로 코드를 실행하고 실행 시간과 메모리 소비량에 대해서만 비용을 지불하는 서버리스 핵심 서비스임.",
        "text_replacements": [],
        "rec_text": "콜드 스타트 완화를 위해 경량 컨테이너(Firecracker 마이크로VM)를 활용하고, 영속적 상태 저장이 필요한 경우 외부 분산 캐시(Redis) 및 서버리스 DB와 결합.",
        "rec_diagram": """```text
[ 이벤트 프로듀서 (Event Producer) ] (API Gateway / Kafka / S3 Upload)
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ [ FaaS 플랫폼 오케스트레이터 (AWS Lambda / Cloud Run) ] │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ 샌드박스 라이프사이클 관리 (Firecracker MicroVM)│   │
│   │  - Cold Start: 런타임 인출 -> 컨테이너 초기화  │   │
│   │  - Warm Start: 메모리 상주 인스턴스 즉시 실행  │   │
│   └───────────────────────┬────────────────────────┘   │
│                           ▼                            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 비즈니스 함수 실행 (handler(event, context))   │   │
│   └───────────────────────┬────────────────────────┘   │
│                           ▼                            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 사후 수명주기: 유휴 시간 경과 시 컨테이너 파기 │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | FaaS (Function as a Service) | PaaS (Platform as a Service) |
|---|---|---|
| **배포 및 관리 단위** | 단일 함수 단위 (Function, 수십 라인) | 전체 애플리케이션 서비스 단위 (App Stack) |
| **수명주기 (Lifecycle)** | 이벤트 발생 시 기동되어 수 밀리초~수 분 내 종료 | 항시 구동되는 롱러닝 프로세스 (24x365 가동) |
| **자동 확장 단위** | 수신되는 요청/이벤트당 1:1 자동 확장 (0 to N) | 컨테이너 수평 확장 (HPA, 최소 1개 이상 유지) |
| **과금 기준** | 실제 실행 시간(1ms 단위) 및 할당 메모리 | 할당된 인스턴스/컨테이너 수량 시간당 고정 과금 |""",
        "sources": [
            "CNCF Serverless Working Group Whitepaper",
            "NIST Special Publication 800-145: Serverless Architecture and FaaS",
            "Alexandre Sanchez et al. - An Analysis of Serverless Computing Latency and Cold Starts (IEEE Cloud)"
        ],
        "connections": "- 상위 토픽: [003 서버리스 컴퓨팅](./003_serverless_computing.md)\n- 연관 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md), [055 PaaS](./055_paas.md)"
    },

    "079_hbm.md": {
        "insight": "다수의 DRAM 다이를 수직 적층하고 실리콘 관통 전극(TSV)과 2.5D 인터포저로 초광대역 버스를 구성하여 폰 노이만 메모리 벽을 돌파한 고성능 메모리임.",
        "text_replacements": [],
        "rec_text": "초고집적 적층으로 인한 발열과 인터포저 휨(Warpage) 현상을 방지하기 위해 MR-MUF 첨단 패키징을 적용하고, GPU와 최단 배선으로 직결하여 신호 감쇄 최소화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 2.5D 첨단 패키징 기반 HBM 및 GPU 인터포저 집적 아키텍처 ]           │
│                                                                        │
│   ┌───────────────┐                  ┌───────────────────────────────┐ │
│   │ [ AI 가속기 ] │                  │ [ HBM 수직 적층 스택 ]        │ │
│   │   (GPU/NPU)   │                  │  - DRAM 다이 (4~16층 적층)    │ │
│   │               │                  │  - 수만 개의 수직 TSV 관통    │ │
│   │               │                  │  - 최하단 베이스 다이 (로직)  │ │
│   └───┬───────┬───┘                  └───┬───────────────────────┬───┘ │
│       │ 마이크로 범프                    │ 마이크로 범프             │ │
│   ┌───┴───────┴──────────────────────────┴───────────────────────┴───┐ │
│   │ 실리콘 인터포저 (Silicon Interposer: 수천 비트 와이드 I/O 버스)   │ │
│   └───────────────────────────┬──────────────────────────────────────┘ │
│                               │ 솔더 C4 범프                           │
│   ┌───────────────────────────┴──────────────────────────────────────┐ │
│   │ 패키지 서브스트레이트 기판 (Package Substrate PCB)                │ │
│   └──────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 규격 세대 | I/O 버스 폭 | 최대 대역폭 (스택당) | 적층 단수 | 주요 적용 가속기 |
|---|---|---|---|---|
| **HBM1** | 1024-bit | 128 GB/s | 4-Hi | AMD Fury 시리즈 |
| **HBM2** | 1024-bit | 256 GB/s | 4-Hi / 8-Hi | NVIDIA V100 |
| **HBM2e** | 1024-bit | 460 GB/s | 8-Hi | NVIDIA A100 |
| **HBM3** | 1024-bit | 819 GB/s | 12-Hi | NVIDIA H100 |
| **HBM3e** | 1024-bit | 1.2 TB/s | 12-Hi / 16-Hi | NVIDIA H200, B200 |
| **HBM4** | **2048-bit** | **2.0 ~ 3.3 TB/s** | **16-Hi** | 차세대 초거대 AI 가속기 |""",
        "sources": [
            "JEDEC Standard JESD235: High Bandwidth Memory (HBM) DRAM",
            "IEEE Micro: High-Bandwidth Memory (HBM): Breakthrough in High-Performance Memory",
            "SK Hynix / Samsung Electronics HBM Product and Packaging Technology Roadmap"
        ],
        "connections": "- 상위 토픽: [027 HBM4](./027_hbm4.md)\n- 연관 토픽: [066 SK하이닉스 HBM4 양산](./066_sk_hynix_hbm4_mass_production.md), [020 GPU](./020_gpu.md)"
    },

    "080_nas.md": {
        "insight": "전용 OS와 파일시스템을 탑재한 저장장치를 표준 이더넷 LAN 망에 직결하여 복수의 이기종 클라이언트가 파일 레벨(NFS/SMB)로 데이터를 공유하는 스토리지임.",
        "text_replacements": [],
        "rec_text": "네트워크 혼잡으로 인한 파일 I/O 지연을 방지하기 위해 10G/25G 전용 이더넷 격리망과 LACP 링크 본딩을 구성하고, 대용량 파일 공유에는 NVMe 오버 이더넷(NVMe-oF) 도입.",
        "rec_diagram": """```text
[ 이기종 클라이언트 계층 ] (Linux 서버, Windows PC, K8s Pod)
            │                           │
            │ NFS v4.2 (Linux)          │ SMB 3.1.1 (Windows)
            ▼                           ▼
┌────────────────────────────────────────────────────────┐
│ [ 표준 TCP/IP 이더넷 스위치 망 (10GbE / 25GbE LAN) ]   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ [ NAS (Network Attached Storage) 장치 ]                │
│   - 스토리지 전용 경량화 커널 OS                       │
│   - 파일시스템 엔진 (ZFS, Btrfs, XFS)                  │
│   - 볼륨 공유, 스냅샷, 접근 제어(ACL) 관리            │
│   ┌────────────────────────────────────────────────┐   │
│   │ 하드웨어 RAID 스토리지 어레이 (HDD / SSD 팜)   │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | DAS (Direct Attached) | NAS (Network Attached) | SAN (Storage Area Network) |
|---|---|---|---|
| **연결 방식** | 전용 케이블 (SAS/SATA/PCIe) | 표준 이더넷 LAN 망 (TCP/IP) | 전용 고속 광섬유망 (Fibre Channel) |
| **데이터 접근 단위**| **블록 단위 (Block-level)** | **파일 단위 (File-level)** | **블록 단위 (Block-level)** |
| **네트워크 프로토콜**| SCSI, SATA, NVMe 프로토콜 | NFS, SMB/CIFS, AFP | FC-SCSI, FCoE, iSCSI, NVMe-oF |
| **파일 시스템 위치**| 호스트 컴퓨터에 설치 | **NAS 전용 장치 내부에서 관리**| 호스트 컴퓨터에 설치 |
| **주요 장단점** | 단순·최저지연 / 공유 불가 | 손쉬운 파일 공유 / LAN 대역폭 공유 | 초고속·고확장성 / 고비용·구축 복잡 |""",
        "sources": [
            "Storage Networking Industry Association (SNIA) Storage Networking Architecture Guide",
            "IETF RFC 7530: Network File System (NFS) Version 4 Protocol",
            "Microsoft Learn: Server Message Block (SMB) Protocol Overview"
        ],
        "connections": "- 상위 토픽: [123 스토리지 유형 비교](./123_storage_type_comparison.md)\n- 연관 토픽: [084 SAN](./084_san.md), [082 DAS](./082_das.md), [056 RAID](./056_raid.md)"
    },

    "081_storage_virtualization.md": {
        "insight": "이기종의 복수 물리 스토리지를 논리적인 단일 스토리지 풀로 통합 추상화하여 볼륨 동적 할당, 무중단 데이터 마이그레이션, 자동 계층화를 구현하는 기술임.",
        "text_replacements": [
            ("이기종 스토리지를 연결해 풀을 구성하고, 가상 볼륨을 생성해 호스트에 매핑한다. 씬 프로비저닝과 계층화를 적용해 사용률을 관리한다.",
             "이기종 스토리지를 연결하여 스토리지 풀을 구성하고 가상 LUN 볼륨을 생성해 호스트에 매핑. 씬 프로비저닝과 자동 계층화(Tiering)를 적용하여 스토리지 활용률 관리.")
        ],
        "rec_text": "실제 쓰인 공간만 선별 할당하는 씬 프로비저닝(Thin Provisioning)을 기본 적용하되, 풀 용량 고갈로 인한 전체 볼륨 셧다운을 방지하기 위해 80% 임계치 알람 필수 설정.",
        "rec_diagram": """```text
[ 호스트 서버 계층 (Host Servers / Hypervisors) ]
            │ (단일 가상 LUN 볼륨 인식)
            ▼
┌────────────────────────────────────────────────────────┐
│ [ 스토리지 가상화 제어 계층 (Storage Virtualization) ] │
│   - 가상 볼륨 생성 및 LUN 매핑                         │
│   - 씬 프로비저닝 (Thin Provisioning)                   │
│   - 무중단 볼륨 마이그레이션 (Volume Mobility)          │
│   - 자동 계층화 (Tiering: 핫 데이터는 SSD, 콜드는 HDD) │
└───────────────────────────┬────────────────────────────┘
                            │ (물리 블록 I/O 변환 매핑)
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
┌──────────────────┐┌──────────────────┐┌──────────────────┐
│ [ 물리 스토리지 A]││ [ 물리 스토리지 B]││ [ 물리 스토리지 C]│
│ (All-Flash NVMe) ││ (SAS SAN Array)  ││ (대용량 SATA 팜) │
└──────────────────┘└──────────────────┘└──────────────────┘
```""",
        "rec_table": """| 가상화 구현 위치 | 동작 메커니즘 | 장점 | 주요 단점 및 한계 |
|---|---|---|---|
| **호스트 기반 (Host-based)** | 호스트 LVM 또는 가상화 OS 소프트웨어 | 추가 하드웨어 불필요, 비용 저렴 | 호스트 CPU/메모리 부하, OS별 종속성 |
| **네트워크 기반 (Network)** | SAN 패브릭 스위치나 전용 어플라이언스 | 이기종 스토리지 완벽 통합, 중앙 집중 제어 | 어플라이언스 단일 장애점(SPOF) 및 지연 발생 |
| **스토리지 기반 (Array)** | 스토리지 컨트롤러 내부 가상화 | 컨트롤러 전용 가속 ASIC, 고성능 | 해당 제조사 스토리지 간에만 제한적 지원 |""",
        "sources": [
            "Storage Networking Industry Association (SNIA) Storage Virtualization Taxonomy",
            "IEEE Transactions on Computers: Architecture and Performance of Storage Virtualization",
            "IBM SAN Volume Controller (SVC) & NetApp Virtualization Architecture Guide"
        ],
        "connections": "- 상위 토픽: [084 SAN](./084_san.md)\n- 연관 토픽: [080 NAS](./080_nas.md), [056 RAID](./056_raid.md)"
    },

    "082_das.md": {
        "insight": "스토리지 장치를 네트워크 경유 없이 전용 호스트 버스 어댑터(HBA)와 케이블을 통해 서버에 일대일 직결하여 초저지연 블록 I/O를 제공하는 스토리지 방식임.",
        "text_replacements": [
            ("호스트 버스 어댑터를 통해 디스크 어레이를 전용 연결하고, 로컬 파일시스템을 생성해 애플리케이션에 마운트한다.",
             "호스트 버스 어댑터(HBA)를 통해 전용 케이블로 외장 디스크를 직결하고 로컬 파일시스템을 포맷하여 마운트.")
        ],
        "rec_text": "네트워크 스위치 오버헤드가 없어 단일 노드 초저지연 I/O가 필요한 빅데이터 하둡/카프카 노드나 고성능 단독 DB에 적용하되, 다른 서버와의 자원 공유 불가 한계 인지 필요.",
        "rec_diagram": """```text
┌─────────────────────────────────┐
│ [ 호스트 서버 (Host Server) ]   │
│   - 운영체제 및 파일시스템 직접 관리│
│   - 호스트 버스 어댑터 (HBA)    │
└────────────────┬────────────────┘
                 │ 전용 직결 케이블 (SAS / SATA / NVMe Direct)
                 │ (네트워크 스위치 경유 없음 -> 레이턴시 0에 수렴)
                 ▼
┌─────────────────────────────────┐
│ [ DAS 외장 스토리지 인클로저 ]  │
│   - JBOD / RAID 컨트롤러        │
│   - 고속 하드디스크 / NVMe SSD  │
└─────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | DAS (Direct Attached) | SAN (Storage Area Network) |
|---|---|---|
| **연결 구조** | 서버와 스토리지가 1:1 전용 케이블 직결 | 광 스위치 패브릭을 통한 N:M 다중 네트워크 연결 |
| **I/O 지연 시간** | **최저 지연 (극소, 프로토콜 변환 없음)** | 네트워크 전송 및 스위치 라우팅 지연 수반 |
| **자원 공유성** | **불가 (직결된 단일 서버만 독점 사용)** | **완벽 지원 (모든 서버가 풀의 볼륨을 공유/할당)** |
| **용량 확장성** | 물리적 포트 수 및 섀시 한계로 확장 제한 | 무한에 가까운 스케일아웃 및 스토리지 통합 증설 |
| **도입 비용** | 최저 (케이블 및 HBA만 필요) | 최고 (FC 광스위치, 광케이블, 고가 어레이 필요) |""",
        "sources": [
            "Storage Networking Industry Association (SNIA) Direct Attached Storage Guide",
            "Serial Attached SCSI (SAS) & Non-Volatile Memory Express (NVMe) Standards",
            "Computer Architecture: Mass Storage Systems and Interface Protocols"
        ],
        "connections": "- 상위 토픽: [123 스토리지 유형 비교](./123_storage_type_comparison.md)\n- 연관 토픽: [080 NAS](./080_nas.md), [084 SAN](./084_san.md)"
    },

    "083_gpgpu.md": {
        "insight": "그래픽 렌더링에 국한되던 GPU의 초병렬 연산 능력을 CUDA 및 OpenCL 프레임워크를 통해 범용 수치 연산, 딥러닝, 암호 해독, 물리 시뮬레이션에 확장 적용한 기술임.",
        "text_replacements": [
            ("호스트 CPU가 데이터를 GPU 메모리로 복사하고, 커널 함수를 대규모 스레드로 병렬 실행한다. 연산이 끝나면 결과를 CPU 메모리로 다시 복사한다.",
             "호스트 CPU가 데이터를 GPU 글로벌 메모리로 DMA 복사하고, 대규모 워프(Warp) 스레드로 커널 함수를 병렬 실행한 뒤 연산 결과를 호스트 메모리로 복귀.")
        ],
        "rec_text": "호스트 CPU-GPU 간 PCIe 데이터 전송 병목을 줄이기 위해 통합 메모리(Unified Memory)와 비동기 스트림(CUDA Stream) 파이프라이닝을 적용하여 연산과 전송을 중첩 수행.",
        "rec_diagram": """```text
[ 호스트 CPU 프로세서 ]                               [ 디바이스 GPGPU 가속기 ]
        │                                                         │
        │ 1. cudaMemcpy(HostToDevice): 입력 데이터 전송 (PCIe)      │
        ├────────────────────────────────────────────────────────>│
        │                                                         │
        │ 2. 커널 함수 실행 명령 (kernel<<<Grid, Block>>>)         │
        ├────────────────────────────────────────────────────────>│
        │                                                         │ 3. 대규모 SIMT 병렬 연산 수행
        │                                                         │   (수만 개 스레드가 동시 실행)
        │                                                         │
        │ 4. cudaMemcpy(DeviceToHost): 최종 연산 결과 복원        │
        │<────────────────────────────────────────────────────────┤
        ▼                                                         ▼
```""",
        "rec_table": """| 개발 프레임워크 | 개발 주체 | 하드웨어 호환성 | 에코시스템 및 성능 최적화 |
|---|---|---|---|
| **CUDA** | NVIDIA 독점 | NVIDIA GPU 전용 | 업계 표준, 최고 수준의 딥러닝 라이브러리(cuDNN, TensorRT) 지원 |
| **OpenCL** | Khronos 그룹 | 개방형 표준 (Intel, AMD, ARM, Apple) | 범용성 우수, 벤더별 최적화 난이도 높음 |
| **ROCm** | AMD | AMD Radeon / Instinct GPU | 오픈소스 기반, 최근 PyTorch 지원 및 생태계 급성장 |""",
        "sources": [
            "David B. Kirk, Wen-mei W. Hwu - Programming Massively Parallel Processors: A Hands-on Approach",
            "NVIDIA CUDA C++ Programming Guide and Best Practices",
            "ACM Computing Surveys: General-Purpose Computing on Graphics Processing Units (GPGPU)"
        ],
        "connections": "- 상위 토픽: [020 GPU](./020_gpu.md)\n- 연관 토픽: [007 NPU](./007_npu.md), [094 멀티 GPU](./094_multi_gpu.md)"
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
