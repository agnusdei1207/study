import os
import re
from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

DATA = {
    "027_hbm4.md": {
        "insight": "기존 1024비트에서 2048비트로 확장된 인터페이스와 로직 공정 기반 베이스 다이를 적용하여 2~3TB/s 초고대역폭과 전력 효율을 달성한 6세대 메모리임.",
        "text_replacements": [],
        "rec_text": "GPU 호스트와 HBM4 간의 2048비트 극미세 인터커넥트를 위해 첨단 2.5D/3D 패키징(CoWoS/I-Cube) 수율을 사전에 검증하고, 파운드리-메모리 협업 베이스 다이 설계 필수.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ HBM4 (6세대 고대역폭 메모리) 3D 수직 적층 구조 ]                     │
│                                                                        │
│   ┌────────────────────────────────────────────────────────┐           │
│   │ DRAM 다이 16층 수직 적층 (Advanced MR-MUF / 하이브리드 본딩) │    │
│   │  - 수만 개의 실리콘 관통 전극 (TSV)으로 층간 초고속 연결 │       │
│   └───────────────────────────┬────────────────────────────┘           │
│                               │                                        │
│                               ▼                                        │
│   ┌────────────────────────────────────────────────────────┐           │
│   │ 4나노/3나노 로직 공정 베이스 다이 (Base Die / Buffer Die)  │       │
│   │  - DFI 인터페이스 및 맞춤형 BIST (자체 진단 테스트) 내장│          │
│   │  - 전력 관리 회로 및 온다이 인터커넥트 최적화         │          │
│   └───────────────────────────┬────────────────────────────┘           │
│                               │                                        │
│                               ▼                                        │
│   ┌────────────────────────────────────────────────────────┐           │
│   │ 2048비트 초광대역 I/O 인터페이스 (기존 HBM3e 1024비트의 2배)│      │
│   │ 대역폭: 스택당 2.0 ~ 3.3 TB/s 초고속 데이터 전송       │          │
│   └────────────────────────────────────────────────────────┘           │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 규격 세대 | I/O 버스 폭 | 핀당 전송 속도 | 스택당 최대 대역폭 | 베이스 다이 공정 | 최대 적층 수 |
|---|---|---|---|---|---|
| **HBM2e** | 1024-bit | 3.2 Gbps | 410 GB/s | 레거시 DRAM 공정 | 8-Hi (16GB) |
| **HBM3** | 1024-bit | 6.4 Gbps | 819 GB/s | DRAM 공정 | 12-Hi (24GB) |
| **HBM3e** | 1024-bit | 9.6 Gbps | 1.2 TB/s | 첨단 DRAM 공정 | 12-Hi / 16-Hi (36GB/48GB) |
| **HBM4** | **2048-bit** | 8.0~10.0 Gbps | **2.0 ~ 3.3 TB/s** | **첨단 파운드리 로직 공정(4nm)** | **16-Hi (64GB)** |""",
        "sources": [
            "JEDEC Solid State Technology Association: HBM4 Standard Specification",
            "IEEE International Solid-State Circuits Conference (ISSCC): Next-Generation High Bandwidth Memory",
            "SK Hynix / Samsung Electronics HBM4 Mass Production Technology Whitepaper"
        ],
        "connections": "- 상위 토픽: [079 HBM](./079_hbm.md)\n- 연관 토픽: [066 SK하이닉스 HBM4 양산](./066_sk_hynix_hbm4_mass_production.md), [020 GPU](./020_gpu.md)"
    },

    "028_liquid_cooling.md": {
        "insight": "공기 대비 비열이 수천 배 높은 액체 냉매를 고발열 칩에 직접 순환시켜 랙당 100kW 이상의 AI 데이터센터 열밀도를 해소하고 PUE를 1.1 이하로 극대화함.",
        "text_replacements": [],
        "rec_text": "냉매 누출 시 IT 장비 훼손을 차단하기 위해 음압형 유체 루프와 절연성 불활성 냉매를 채택하고, 냉각탑 및 CDU(Cooling Distribution Unit) 이중화로 신뢰성 확보.",
        "rec_diagram": """```text
[ AI 고집적 서버 랙 (100kW+ per Rack) ]
  ┌────────────────────────────────────────────────────────┐
  │ [ GPU / CPU 직접 냉각 (Direct-to-Chip DLC) 콜드플레이트 ] │
  └───────────────────────────┬────────────────────────────┘
                              │ 뜨거운 냉매 회수 (Closed Loop)
                              ▼
┌──────────────────────────────────────────────────────────┐
│ [ CDU (냉각 분배 장치: Cooling Distribution Unit) ]       │
│   - 1차 냉수 루프와 2차 시설 냉각수 간 열교환기          │
│   - 정밀 유량 제어, 압력 조절 펌프, 필터링 및 누수 감지 │
└─────────────────────────────┬────────────────────────────┘
                              │ 온수 배출 (Facility Water Loop)
                              ▼
┌──────────────────────────────────────────────────────────┐
│ [ 외부 시설 냉각 시스템 (Cooling Tower / Dry Cooler) ]    │
│   - 외기 프리쿨링(Free Cooling) 연계로 압축기 전력 제로화 │
│   - 데이터센터 PUE 1.1 미만 달성                         │
└──────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 냉각 기술 유형 | 열전달 방식 | 랙당 감당 전력 밀도 | 냉각 효율 (PUE) | 유지보수 및 도입 난이도 |
|---|---|---|---|---|
| **공랭식 (Air Cooling)** | 팬 기반 공기 대류 | 15 ~ 30 kW 한계 | 1.3 ~ 1.6 | 단순, 인프라 표준화 완료 |
| **직접 칩 냉각 (DLC / D2C)** | 칩 상단 금속 콜드플레이트 순환 | 80 ~ 150 kW | 1.1 ~ 1.2 | 배관 누수 센서 필수, 기존 랙 호환 |
| **단상 액침 냉각 (Single-Phase)**| 비전도성 오일에 서버 완전 침전 | 100 ~ 200 kW | 1.05 ~ 1.1 | 누수 위험 제로, 유지보수 시 오일 제거 부담 |
| **2상 액침 냉각 (Two-Phase)** | 끓는점 낮은 냉매의 증발-응축 잠열 | 250 kW+ 초고밀도 | 1.02 ~ 1.05 | 초고효율, 냉매 증발 손실 및 환경 규제 리스크 |""",
        "sources": [
            "ASHRAE TC 9.9: Liquid Cooling Guidelines for Datacom Equipment Centers",
            "Open Compute Project (OCP): Advanced Cooling Facilities & Immersion Specs",
            "Uptime Institute: Data Center Liquid Cooling Trends and Reliability"
        ],
        "connections": "- 상위 토픽: [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md)\n- 연관 토픽: [043 데이터센터 입지 및 재해대응](./043_datacenter_location_disaster_response.md), [070 랙 스케일 AI 시스템](./070_rack_scale_ai_system.md)"
    },

    "029_quantum_error_correction_google_willow.md": {
        "insight": "다수의 물리적 큐비트를 얽어 표면 코드로 논리 큐비트를 구성하고, 물리 큐비트 수가 증가할수록 오류율이 지수함수적으로 감소하는 임계치를 실증함.",
        "text_replacements": [],
        "rec_text": "오류 억제 임계치(Threshold) 아래에서 신드롬 측정과 실시간 디코딩을 수행하는 전용 제어 하드웨어를 구성하고, 양자 우위(Quantum Supremacy)를 상용 내결함성 양자컴퓨터로 전이.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 표면 코드 (Surface Code) 기반 양자 오류 정정 메커니즘 ]              │
│                                                                        │
│       (Data Qubit) ○ ──── [ X-Check ] ──── ○ (Data Qubit)              │
│            │                                    │                      │
│        [ Z-Check ]                          [ Z-Check ]                │
│            │                                    │                      │
│       (Data Qubit) ○ ──── [ X-Check ] ──── ○ (Data Qubit)              │
│                                                                        │
│   - 데이터 큐비트: 양자 중첩 정보를 저장하는 물리 큐비트               │
│   - 보조(신드롬) 큐비트: 위상 반전(Phase) 및 비트 반전(Bit) 오류 비파괴 측정│
│   - 양자 얽힘을 통해 원본 데이터를 파괴하지 않고 오류 위치만 판별      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 구글 윌로우(Willow) 칩의 핵심 이정표 ]                               │
│   - 물리적 큐비트 확장 시 오류가 기하급수적으로 감소하는 '스케일링 법칙' 입증│
│   - 표준 벤치마크 계산 시간을 수백만 년에서 수 분 단위로 단축         │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 구분 항목 | 물리적 큐비트 (Physical Qubit) | 논리적 큐비트 (Logical Qubit) |
|---|---|---|
| **기본 정의** | 초전도 조셉슨 접합 등 실제 하드웨어 소자 | 표면 코드로 묶여 오류가 정정되는 가상 큐비트 |
| **오류율 수준** | $10^{-3} \\sim 10^{-4}$ (외부 노이즈에 극히 취약) | $10^{-9} \\sim 10^{-12}$ (상용 알고리즘 수행 가능 수준) |
| **필요 소자 수** | 1개 물리 소자 | 수백 ~ 수천 개의 물리 큐비트 + 보조 큐비트 묶음 |
| **결맞음 시간 (Coherence)**| 수 마이크로초 ($\mu s$) 수준 | 실시간 오류 정정을 통해 반영구적 유지 목표 |
| **주요 역할** | 신드롬 측정 및 기초 연산 게이트 | 쇼어 알고리즘, 신약 개발 등 실질적 양자 컴퓨팅 수행 |""",
        "sources": [
            "Nature: Google Quantum AI - Suppressing Quantum Errors by Scaling a Quantum Computer",
            "Google Willow Quantum Chip Technical Whitepaper",
            "IEEE Micro: Quantum Error Correction Architectures and Real-time Decoding"
        ],
        "connections": "- 상위 토픽: [072 양자 기술 NIA IITP](./072_quantum_technology_nia_iitp.md)\n- 연관 토픽: [115 위상학적 큐비트 마요라나 1](./115_topological_qubit_majorana_1.md), [116 하이브리드 컴퓨팅](./116_hybrid_computing.md)"
    },

    "030_chiplet_ucie_3_0.md": {
        "insight": "단일 모놀리식 다이의 제조 수율 한계를 극복하기 위해 기능별 다이를 개별 공정으로 분할 제작하고 표준화된 UCIe 버스로 초고속 통합하는 반도체 패키징 패러다임임.",
        "text_replacements": [
            ("송신 칩렛 데이터는 다이-투-다이 UCIe PHY를 거쳐 패키지 배선으로 전달되고, 수신 칩렛 PHY에서 클록을 복원해 링크 계층으로 넘겨 처리된다.",
             "송신 칩렛 데이터는 다이-투-다이 UCIe PHY를 거쳐 패키지 배선으로 전달되고 수신 칩렛 PHY에서 클록을 복원해 링크 계층으로 디스패칭.")
        ],
        "rec_text": "이기종 칩렛 간 다이-투-다이(D2D) 인터커넥트 구현 시 표준 프로토콜(UCIe) 호환성을 확보하고, 실리콘 브리지(EMIB) 또는 인터포저 기반 2.5D 패키징 열팽창 계수 일치화 필요.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ UCIe 3.0 기반 이기종 칩렛 (Heterogeneous Chiplet) 패키지 ]           │
│                                                                        │
│   ┌──────────────┐       ┌──────────────────────┐       ┌────────────┐ │
│   │ [ CPU 칩렛 ] │       │ [ 메인 로직 / AI ]   │       │ [ I/O 칩렛 ]│ │
│   │ (첨단 3nm)   │       │ (첨단 2nm 공정)      │       │ (레거시 7nm)│ │
│   └───┬──────┬───┘       └───┬──────────────┬───┘       └───┬────┬───┘ │
│       │      │               │              │               │    │     │
│       │ UCIe │   UCIe 링크   │              │   UCIe 링크   │    │     │
│       │ PHY  │<─────────────>│   UCIe PHY   │<─────────────>│    │     │
│       └──┬───┘               └───┬──────────┘               └──┬─┘     │
│          │                       │                             │       │
│   ┌──────┴───────────────────────┴─────────────────────────────┴─────┐ │
│   │ 초고밀도 실리콘 인터포저 (Advanced 2.5D Packaging Substrate)     │ │
│   └──────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 단일 칩 (Monolithic SoC) | 칩렛 아키텍처 (UCIe Chiplet) |
|---|---|---|
| **제조 수율** | 면적이 커질수록 결함 확률 급증으로 수율 급감 | 작은 다이로 분할 제작하여 제조 수율 90%+ 극대화 |
| **공정 최적화** | 고비용 첨단 미세공정(3nm)을 칩 전체에 일괄 적용 | 코어는 2/3nm, 아날로그/I/O는 저비용 7/12nm 최적 공정 혼용 |
| **개발 기간 및 TTM** | 사소한 회로 수정에도 전면 재설계(Respin) 필요 | 검증된 상용 칩렛 레고 블록식 재조합으로 개발기간 단축 |
| **인터커넥트 지연** | 단일 실리콘 내부로 최저 지연 및 최고 대역폭 | 다이 간 전송 지연 발생 (UCIe 표준화로 수 나노초 수준 압축) |
| **패키징 기술** | 전통적인 표준 기판 본딩 | 고난도 2.5D/3D 첨단 패키징 (EMIB, CoWoS) 필수 |""",
        "sources": [
            "Universal Chiplet Interconnect Express (UCIe) Specification 1.0 / 2.0 / 3.0",
            "IEEE Micro: The Era of Chiplets and Die-to-Die Interconnects",
            "Intel / TSMC Advanced Packaging & Chiplet Architecture Roadmap"
        ],
        "connections": "- 상위 토픽: [097 메모리 반도체](./097_memory_semiconductor.md)\n- 연관 토픽: [100 비메모리 반도체](./100_non_memory_semiconductor.md), [104 시스템 반도체 생태계](./104_system_semiconductor_ecosystem.md)"
    },

    "031_fts.md": {
        "insight": "시스템 구성 요소의 일부 결함이나 물리적 고장이 발생해도 서비스 중단 없이 정상 기능 또는 허용 가능한 수준의 기능을 지속 제공하는 신뢰성 기술임.",
        "text_replacements": [],
        "rec_text": "단일 장애점 배제를 위해 하드웨어 3중 모듈 중복(TMR)과 다수결 투표기를 배치하고, 소프트웨어 N-버전 프로그래밍과 복구 블록(Recovery Block) 기법을 상호 보완 적용.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────┐
│ [ 하드웨어 3중 모듈 중복 (TMR: Triple Modular Redundancy) ] │
│                                                        │
│   [ 입력 신호 X ]                                       │
│          │                                             │
│     ┌────┼────┐                                        │
│     ▼    ▼    ▼                                        │
│   ┌───┐┌───┐┌───┐                                      │
│   │ M1││ M2││ M3│ (동일 연산을 독립 수행하는 3개 모듈)   │
│   └───┘└───┘└───┘                                      │
│     │    │    │                                        │
│     ▼    ▼    ▼                                        │
│   ┌─────────────┐                                      │
│   │ 다수결 판정 │ (Majority Voter: 1개 모듈 결함 발생 시│
│   │ (Voter 회로)│  다수결 2:1로 정상 결과 채택)        │
│   └──────┬──────┘                                      │
│          │                                             │
│          ▼                                             │
│   [ 무장애 정상 출력 ]                                 │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| FTS 설계 개념 | 핵심 동작 메커니즘 | 고장 시 시스템 동작 상태 | 주요 적용 분야 |
|---|---|---|---|
| **페일 오버 (Fail-Over)** | 주 시스템 고장 시 예비 시스템으로 제어권 자동 이전 | 순간적인 전환 후 정상 서비스 복구 | 웹 서버, 데이터베이스 HA 클러스터 |
| **페일 세이프 (Fail-Safe)** | 고장 감지 시 사전에 정의된 가장 안전한 정지 상태로 전환 | 서비스 즉시 중단 (인명/물리적 피해 방지) | 철도 신호 제어, 원자력 발전소, 승강기 |
| **페일 소프트 (Fail-Soft)** | 비핵심 부가 기능 차단, 필수 핵심 기능만 축소 가동 | 기능 저하(Graceful Degradation) 유지 | 항공기 관제, 응급 의료 장비, 지진 관제 |
| **폴트 마스킹 (Fault Masking)**| 내부에서 오류를 은닉·정정하여 외부에 오류 미노출 | 성능 저하 없는 완벽한 정상 서비스 지속 | 항공 우주 비행 컴퓨터, 3중화 결함 허용 시스템 |""",
        "sources": [
            "Algirdas Avizienis et al. - Basic Concepts and Taxonomy of Dependable and Secure Computing (IEEE TDSC)",
            "Pradhan, D.K. - Fault-Tolerant Computer System Design (Prentice Hall)",
            "NASA Fault Tolerance Standards & System Reliability Engineering Handbook"
        ],
        "connections": "- 상위 토픽: [021 HA](./021_ha.md)\n- 연관 토픽: [042 HA 가용성 보장](./042_ha_availability_assurance.md), [106 마이그레이션 장애관리](./106_migration_fault_management.md)"
    },

    "032_container.md": {
        "insight": "호스트 OS 커널을 공유하면서 리눅스 네임스페이스와 cgroups를 통해 프로세스를 논리적으로 격리하는 경량 가상화 실행 환경임.",
        "text_replacements": [],
        "rec_text": "호스트 커널 공유로 인한 보안 탈출(Escape) 취약점을 차단하기 위해 비루트(Non-Root) 실행과 seccomp/AppArmor 프로파일을 강제하고, 멀티스테이지 빌드로 경량 이미지 배포.",
        "rec_diagram": """```text
┌─────────────────────────────────┐     ┌─────────────────────────────────┐
│ [ App A ]      │ [ App B ]      │     │ [ App C ]      │ [ App D ]      │
│ (User Process) │ (User Process) │     │ (User Process) │ (User Process) │
├────────────────┴────────────────┤     ├────────────────┴────────────────┤
│ [ 네임스페이스 격리 (Namespaces) ] │     │ [ cgroups 자원 한도 통제 ]       │
│  - PID (독립 프로세스 트리)     │     │  - CPU 사용량 제한 (Quota/Shares)│
│  - NET (독립 IP/라우팅 테이블)  │     │  - Memory OOM 한도 지정         │
│  - MNT (독립 파일시스템 루트)   │     │  - 블록 I/O 및 디바이스 격리     │
├─────────────────────────────────┴─────┴─────────────────────────────────┤
│ [ 단일 공유 호스트 OS 커널 (Shared Host Linux Kernel) ]                 │
├─────────────────────────────────────────────────────────────────────────┤
│ [ 물리 서버 하드웨어 인프라 (CPU, Memory, NIC, Storage) ]                │
└─────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 컨테이너 (Container) | 가상 머신 (Virtual Machine) |
|---|---|---|
| **가상화 계층** | OS 레벨 가상화 (호스트 커널 공유) | 하드웨어 레벨 가상화 (하이퍼바이저 기반) |
| **게스트 OS** | 미포함 (호스트 커널 직접 활용) | 독립 게스트 OS(커널 포함) 필수 설치 |
| **기동 시간** | 수 밀리초 ~ 수 초 (프로세스 실행 속도) | 수십 초 ~ 수 분 (전체 OS 부팅 과정 필요) |
| **자원 점유율** | 수십 MB 단위 경량 메모리/디스크 | 수 GB 단위 무거운 디스크 이미지 및 전용 메모리 할당 |
| **격리 강도** | 소프트웨어 네임스페이스 격리 (보안 취약점 위험) | 하드웨어 VT-x/AMD-V 기반의 완전한 물리적 격리 |""",
        "sources": [
            "Open Container Initiative (OCI) Runtime & Image Specification",
            "IEEE Cloud Computing: Containers and Virtual Machines at Scale",
            "NIST Special Publication 800-190: Application Container Security Guide"
        ],
        "connections": "- 상위 토픽: [012 쿠버네티스](./012_kubernetes.md)\n- 연관 토픽: [085 가상머신](./085_virtual_machine.md), [061 하이퍼바이저](./061_hypervisor.md)"
    },

    "033_fragmentation.md": {
        "insight": "연속 메모리 할당 과정에서 발생하는 내부/외부 메모리 유휴 낭비 현상으로, 비연속 페이징 기법과 버디 시스템 및 메모리 압축을 통해 해결함.",
        "text_replacements": [],
        "rec_text": "동적 메모리 할당 시 발생하는 외부 단편화를 해결하기 위해 불연속 고정 크기 페이징을 기본 적용하고, 가상 주소 공간의 페이지 내부 단편화는 슬랩 할당자(Slab Allocator)로 최소화.",
        "rec_diagram": """```text
[ 내부 단편화 (Internal Fragmentation) ]
 ┌──────────────────────┬───────────────┐
 │ 프로세스 사용 (17KB)  │ 낭비 공간(7KB)│  <── 고정 분할 블록 크기: 24KB
 └──────────────────────┴───────────────┘       (할당 블록 내부의 미사용 낭비)

[ 외부 단편화 (External Fragmentation) ]
 ┌──────────┬──────────┬──────────┬──────────┬──────────┐
 │ 점유 (A) │ 빈공간10K│ 점유 (B) │ 빈공간15K│ 점유 (C) │
 └──────────┴──────────┴──────────┴──────────┴──────────┘
  - 총 여유 공간 = 10KB + 15KB = 25KB
  - 신규 20KB 요청 발생 시 연속된 공간이 없어 할당 실패!
```""",
        "rec_table": """| 단편화 유형 | 발생 원인 | 발생 위치 | 방지 및 해소 기법 |
|---|---|---|---|
| **내부 단편화 (Internal)** | 고정 분할 할당 시 프로세스 크기가 블록보다 작음 | 할당된 파티션 또는 페이지 내부 | 슬랩 할당자, 가변 파티션, 작은 페이지 크기 |
| **외부 단편화 (External)** | 가변 크기 할당/해제 반복으로 빈 공간 조각화 | 할당된 파티션들 사이의 외부 공간 | 페이징(가상메모리), 메모리 압축(Compaction), 버디 시스템 |""",
        "sources": [
            "Abraham Silberschatz et al. - Operating System Concepts: Memory-Management Strategies",
            "Andrew S. Tanenbaum - Modern Operating Systems: Memory Management",
            "Linux Kernel Memory Management: The Slab Allocator and Buddy System"
        ],
        "connections": "- 상위 토픽: [023 가상 메모리](./023_virtual_memory.md)\n- 연관 토픽: [060 페이징](./060_paging.md), [058 세그멘테이션](./058_segmentation.md)"
    },

    "034_ipc.md": {
        "insight": "독립된 가상 주소 공간을 갖는 프로세스들이 데이터를 안전하게 교환하고 동기화할 수 있도록 OS 커널이 제공하는 통신 메커니즘임.",
        "text_replacements": [],
        "rec_text": "초저지연 대용량 데이터 전송에는 공유 메모리와 세마포어 조합을 적용하고, 마이크로서비스 및 분산 노드 간 통신에는 네트워크 확장성을 지원하는 소켓 및 gRPC 활용.",
        "rec_diagram": """```text
┌─────────────────────────────────┐             ┌─────────────────────────────────┐
│ [ Process A (독립 가상 주소) ]   │             │ [ Process B (독립 가상 주소) ]   │
└──────────────┬──────────────────┘             └──────────────────┬──────────────┘
               │                                                   │
    ┌──────────┴──────────┐                             ┌──────────┴──────────┐
    ▼                     ▼                             ▼                     ▼
[ 방식 1: 메시지 전달 ] [ 방식 2: 공유 메모리 ]    [ 방식 1: 메시지 전달 ] [ 방식 2: 공유 메모리 ]
(Message Passing)       (Shared Memory)         (Message Passing)       (Shared Memory)
    │                     │                             ▲                     ▲
    │ 커널 버퍼 경유      │ 매핑 후 직접 읽기/쓰기      │ 커널 버퍼 수신      │ 매핑 후 직접 참조
    ▼                     ▼                             │                     │
┌───────────────────────┐ ┌─────────────────────────────────────────────────┐ │
│ OS 커널 (Kernel Space)│ │ 물리 메모리(DRAM) 공유 영역                     │ │
│  - 파이프 / 메시지 큐 │ │  (커널 개입 없는 제로카피 초고속 전송)          │ │
│  - 소켓 버퍼링        │ │  * 세마포어/뮤텍스 기반 동기화 필수             │ │
└───────────────────────┘ └─────────────────────────────────────────────────┘─┘
```""",
        "rec_table": """| IPC 기법 | 데이터 공유 방식 | 통신 속도 | 동기화 메커니즘 | 통신 범위 |
|---|---|---|---|---|
| **파이프 (Pipe / FIFO)** | 단방향 바이트 스트림 (커널 버퍼) | 보통 | 자동 블로킹 (OS 지원) | 동일 시스템 내 부모-자식(단방향) |
| **메시지 큐 (Msg Queue)**| 구조화된 메시지 블록 전송 | 보통 | OS 커널 큐잉 지원 | 동일 시스템 내 다대다 프로세스 |
| **공유 메모리 (Shared)** | 동일 물리 메모리 영역 공동 매핑 | **최고 (Zero-Copy)** | **개발자 직접 구현 필수 (세마포어)** | 동일 시스템 내 독립 프로세스 |
| **유닉스 도메인 소켓 (UDS)**| 소켓 API 인터페이스 기반 로컬 통신 | 빠름 | 소켓 버퍼 및 핸드셰이크 | 동일 시스템 내 고신뢰성 통신 |
| **네트워크 소켓 (TCP/IP)** | IP 패킷 기반 양방향 스트림 전송 | 상대적 느림 | 프로토콜 수준 흐름 제어 | 네트워크로 분산된 원격 시스템 간 |""",
        "sources": [
            "W. Richard Stevens - UNIX Network Programming, Volume 2: Interprocess Communications",
            "Abraham Silberschatz et al. - Operating System Concepts: Processes and IPC",
            "Linux Manual: shmget, msgget, pipe, socket system calls"
        ],
        "connections": "- 상위 토픽: [010 스레드](./010_thread.md)\n- 연관 토픽: [122 프로세스 동기화](./122_process_synchronization.md), [091 경쟁 조건](./091_race_condition.md)"
    },

    "035_sjf.md": {
        "insight": "다음 CPU 버스트 시간이 가장 짧은 프로세스를 우선 배정하여 이론상 최소 평균 대기시간을 달성하지만 긴 작업의 기아 현상을 수반하는 스케줄링임.",
        "text_replacements": [],
        "rec_text": "미래 버스트 시간의 불확실성을 해결하기 위해 지수 평활법 기반의 예측치를 활용하고, 긴 작업의 무한 대기를 차단하기 위해 대기 시간에 비례한 에이징(Aging) 필수 적용.",
        "rec_diagram": """```text
[ 프로세스 버스트 시간: P1(6ms), P2(8ms), P3(7ms), P4(3ms) 도착 시 ]

[ FCFS 스케줄링 간트 차트 (평균 대기시간: 10.25ms) ]
 0       6              14             21           24
 ┌───────┬──────────────┬──────────────┬────────────┐
 │  P1   │      P2      │      P3      │     P4     │
 └───────┴──────────────┴──────────────┴────────────┘

[ SJF 스케줄링 간트 차트 (평균 대기시간: 7.0ms - 최소화 달성) ]
 0    3          9             16                   24
 ┌────┬──────────┬─────────────┬────────────────────┐
 │ P4 │    P1    │     P3      │         P2         │
 └────┴──────────┴─────────────┴────────────────────┘
  * 최단 작업 P4(3ms)를 가장 먼저 실행하여 전체 프로세스의 대기시간 합을 최소화
```""",
        "rec_table": """| 비교 축 | 비선점형 SJF | 선점형 SJF (SRTF: Shortest Remaining Time) |
|---|---|---|
| **스케줄링 시점** | 현재 실행 중인 프로세스가 CPU를 자진 반납할 때만 결정 | 신규 프로세스 도착 시 잔여 버스트 시간과 비교하여 즉시 선점 |
| **평균 대기시간** | FCFS 대비 크게 우수 | 모든 스케줄링 알고리즘 중 **이론상 최소 평균 대기시간** |
| **문맥 교환 오버헤드** | 적음 (프로세스 완료 시에만 발생) | 빈번함 (짧은 작업이 계속 도착할 때마다 선점 발생) |
| **기아 현상 (Starvation)**| 발생 가능 (짧은 작업 연속 유입 시 긴 작업 대기) | 심각하게 발생 (지속적인 선점으로 긴 작업 무한 연기) |""",
        "sources": [
            "Abraham Silberschatz et al. - Operating System Concepts: CPU Scheduling",
            "Remzi H. Arpaci-Dusseau - Operating Systems: Three Easy Pieces (Scheduling: Introduction)",
            "IEEE Transactions on Computers: Analysis of SJF and Priority Scheduling"
        ],
        "connections": "- 상위 토픽: [019 CPU 스케줄링](./019_cpu_scheduling.md)\n- 연관 토픽: [076 CPU](./076_cpu.md), [099 백필](./099_backfill.md)"
    },

    "036_saas.md": {
        "insight": "중앙에서 호스팅되는 애플리케이션을 웹 브라우저나 API를 통해 구독형으로 제공하고, 멀티테넌시 구조를 통해 규모의 경제와 지속적 기능 배포를 실현함.",
        "text_replacements": [],
        "rec_text": "고객 데이터의 엄격한 규제 준수와 비용 효율을 절충하기 위해 테넌트별 사일로(Silo) 모델과 풀링(Pool) 모델을 결합한 하이브리드 멀티테넌시 아키텍처 구축 권고.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ SaaS 멀티테넌시 (Multi-Tenancy) 데이터 격리 아키텍처 모델 ]          │
│                                                                        │
│ [ 1. 풀링 모델 (Pooled Architecture) : 고효율, 비용 최적화 ]           │
│   테넌트 A, B, C ──> [ 단일 공용 웹 서버 ] ──> [ 단일 공유 DB (Tenant_ID 컬럼 구분) ]│
│                                                                        │
│ [ 2. 사일로 모델 (Silo Architecture) : 고보안, 엔터프라이즈 전용 ]     │
│   테넌트 A (금융) ──> [ 독립 전용 웹/앱 ] ──> [ 독립 전용 DB 인스턴스 ]│
│   테넌트 B (공공) ──> [ 독립 전용 웹/앱 ] ──> [ 독립 전용 DB 인스턴스 ]│
│                                                                        │
│ [ 3. 브리지/하이브리드 모델 (Hybrid) ]                                 │
│   - 애플리케이션 컴퓨팅 계층은 풀링 공유, 데이터베이스는 스키마/인스턴스 분리│
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 멀티테넌시 격리 수준 | 데이터 격리 메커니즘 | 자원 비용 효율 | 테넌트 간 간섭(Noisy Neighbor) | 보안 및 규제 준수 |
|---|---|---|---|---|
| **공유 DB, 공유 테이블 (Pooled)** | 단일 테이블 내 `tenant_id` 컬럼으로 로우 분리 | 최고 (비용 최저) | 높음 (대형 테넌트가 DB 독점) | 낮음 (애플리케이션 버그 시 유출 위험) |
| **공유 DB, 분리 스키마 (Bridge)** | 동일 DB 인스턴스 내 테넌트별 독자 Schema | 높음 | 중간 수준 | 보통 (스키마 레벨 권한 통제) |
| **완전 분리 인스턴스 (Silo)** | 테넌트별 독립 전용 DB/컴퓨팅 인스턴스 배정 | 낮음 (비용 최고) | 완전 차단 (간섭 없음) | 최고 (GDPR, HIPAA 등 완벽 충족) |""",
        "sources": [
            "AWS SaaS Factory: SaaS Architecture Fundamentals and Multi-Tenancy Patterns",
            "NIST Special Publication 800-145: Software as a Service (SaaS)",
            "Microsoft Azure Architecture Center: Multitenant SaaS Database Tenancy Patterns"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [054 IaaS](./054_iaas.md), [055 PaaS](./055_paas.md), [119 XaaS](./119_xaas.md)"
    },

    "037_vdi.md": {
        "insight": "사용자의 데스크톱 환경을 중앙 데이터센터 서버의 가상머신에 격리 호스팅하고 화면 픽셀만을 암호화 스트리밍하여 보안성과 원격 근무 연속성을 보장함.",
        "text_replacements": [],
        "rec_text": "대규모 동시 출근 시 발생하는 부트 스톰(Boot Storm)을 방지하기 위해 올플래시 스토리지 캐싱과 사전 프로비저닝 풀을 구성하고, 네트워크 대역폭 적응형 화면 프로토콜(Blast/PCoIP) 적용.",
        "rec_diagram": """```text
[ 원격 사용자 단말 계층 ] (PC, 노트북, 모바일, 씬클라이언트)
                 │
                 │ 화면 픽셀 스트리밍 & 키보드/마우스 입력 전달 (HTTPS / UDP)
                 ▼
┌────────────────────────────────────────────────────────┐
│ [ 보안 게이트웨이 & 연결 브로커 (Connection Broker) ]  │
│   - 사용자 인증 (2FA/MFA) 및 권한 검증                 │
│   - 최적 호스트 가상 데스크톱(VM) 배정 및 세션 라우팅 │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ VDI 호스트 하이퍼바이저 팜 (Hypervisor Cluster) ]     │
│   ┌────────────────────┐      ┌────────────────────┐   │
│   │ [ VM 1 (Desktop) ] │      │ [ VM 2 (Desktop) ] │   │
│   │  - Windows/Linux OS│      │  - Windows/Linux OS│   │
│   │  - 전사 업무 앱/DRM│      │  - 사내 ERP/OA     │   │
│   └────────────────────┘      └────────────────────┘   │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ 중앙 집중 스토리지 (SAN/NAS) & vSAN 올플래시 계층 ]  │
│   - 부트 스톰(Boot Storm) 차단 IOPS 보장               │
│   - 사용자 프로파일 및 데이터 중앙 암호화 격리 저장    │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 데스크톱 가상화 방식 | 데스크톱 인스턴스 영속성 | 사용자별 커스터마이징 | 스토리지 용량 요구 | 적합 업무 영역 |
|---|---|---|---|---|
| **영속형 VDI (Persistent)** | 로그아웃 후에도 변경 상태 유지 | 자유로움 (개인화 완벽 지원) | 높음 (사용자별 전용 가상디스크) | 개발자, 엔지니어, 전문 직무 |
| **비영속형 VDI (Non-Persistent)**| 로그아웃 시 골든 이미지로 리셋 | 제한적 (프로파일 분리 저장) | 낮음 (단일 마스터 이미지 공유) | 콜센터, 교대근무, 공용 단말 |
| **DaaS (Cloud Hosted)** | CSP 관리형 완전 클라우드 호스팅 | 유연함 (라이선스 종량제) | 인프라 투자 불필요 (OPEX) | 원격 단기 프로젝트, 스타트업 |""",
        "sources": [
            "VMware Horizon / Citrix Virtual Apps and Desktops Architecture Reference Guide",
            "IEEE Transactions on Services Computing: Desktop Virtualization Performance Evaluation",
            "금융보안원: 금융분야 망분리 및 VDI 보안 가이드라인"
        ],
        "connections": "- 상위 토픽: [085 가상머신](./085_virtual_machine.md)\n- 연관 토픽: [077 DaaS](./077_daas.md), [061 하이퍼바이저](./061_hypervisor.md)"
    },

    "038_deadlock.md": {
        "insight": "두 개 이상의 프로세스가 서로 상대방이 점유한 자원을 무한 대기하며 실행이 영구 중단되는 현상으로, 4대 필요조건 중 하나를 원천 무력화하여 대응함.",
        "text_replacements": [],
        "rec_text": "환형 대기를 방지하기 위해 전사 모든 자원에 고유 순번을 부여하고 오름차순으로만 락을 획득하는 순서화 규칙을 수립하며, 락 타임아웃 및 교착 탐지 스레드 주기적 가동.",
        "rec_diagram": """```text
[ 교착상태 (Deadlock) 발생 4대 필요조건 동시 성립 구조 ]

        [ 프로세스 P1 ] ──(자원 R2 요청 대기)──> [ 자원 R2 ]
              ▲                                       │
              │ (자원 R1 점유)                        │ (점유 중)
              │                                       ▼
          [ 자원 R1 ] <──(자원 R1 요청 대기)── [ 프로세스 P2 ]

 1. 상호 배제 (Mutual Exclusion) : 한 번에 한 프로세스만 자원 사용
 2. 점유 대기 (Hold and Wait)   : 자원을 보유한 채 다른 자원 추가 요청
 3. 비선점 (No Preemption)      : 다른 프로세스의 자원을 강제 강탈 불가
 4. 환형 대기 (Circular Wait)   : P1->R2->P2->R1->P1 형태의 순환 대기 고리 형성
```""",
        "rec_table": """| 교착상태 해결 전략 | 주요 기법 및 알고리즘 | 시스템 오버헤드 | 장점 | 주요 단점 및 제약 |
|---|---|---|---|---|
| **예방 (Prevention)** | 환형 대기 차단 (자원 순서화), 일괄 요청 | 낮음 | 교착 발생 가능성 0% | 자원 낭비 및 동시성 심각 저하 |
| **회피 (Avoidance)** | 은행원 알고리즘, 자원 할당 그래프 검사 | 높음 (매 요청 검증) | 안전 상태에서만 할당 | 최대 자원 요구량 사전 선언 필수 |
| **탐지 및 복구** | WFG(대기 그래프) 사이클 탐색, 희생자 선정 | 주기적 오버헤드 | 자원 자유 할당, 고이용률 | 프로세스 강제 종료 및 롤백 손실 |
| **무시 (Ignore)** | 타조 알고리즘 (Ostrich) | 없음 | 구현 복잡도 0 | 재부팅 전까지 시스템 정지 위험 |""",
        "sources": [
            "E.G. Coffman et al. - System Deadlocks (ACM Computing Surveys)",
            "Abraham Silberschatz et al. - Operating System Concepts: Deadlocks",
            "Andrew S. Tanenbaum - Modern Operating Systems: Deadlock Detection and Recovery"
        ],
        "connections": "- 상위 토픽: [002 은행원 알고리즘](./002_bankers_algorithm.md)\n- 연관 토픽: [122 프로세스 동기화](./122_process_synchronization.md), [091 경쟁 조건](./091_race_condition.md)"
    },

    "039_thrashing.md": {
        "insight": "프로세스의 빈번한 페이지 부재로 인해 시스템이 실제 유효 연산 대신 디스크 I/O 스왑 처리에 전력을 다하면서 CPU 이용률이 급격히 0으로 수렴하는 붕괴 현상임.",
        "text_replacements": [],
        "rec_text": "스래싱 징후 포착 시 다중 프로그래밍 정도(MPD)를 강제로 낮추고 프로세스별 참조 국소성을 보장하는 워킹셋(Working Set) 모델 및 PFF(Page Fault Frequency) 알고리즘 적용.",
        "rec_diagram": """```text
[ 다중 프로그래밍 정도(MPD)와 CPU 이용률 간의 스래싱 곡선 ]

  CPU 이용률 (%)
   100 │                 정상 가동 영역         스래싱(Thrashing) 붕괴 영역
       │                       ┌───┐
       │                     ┌─┘   └─┐
       │                   ┌─┘       └─┐
       │                 ┌─┘           └──┐
       │               ┌─┘                └──┐
       │             ┌─┘                     └──┐
       │           ┌─┘                          └──┐  <── 페이지 부재 급증
       │         ┌─┘                               └──┐   I/O 큐 포화 상태
     0 └─────────┴────────────────────────────────────┴──────────
       0                                               MPD (프로세스 수)
                                                      ▲
                                            [ 임계점: 메모리 총합 부족 ]
```""",
        "rec_table": """| 스래싱 예방 및 해소 기법 | 핵심 제어 원리 | 장점 | 주요 고려사항 |
|---|---|---|---|
| **워킹셋 (Working Set) 모델** | 최근 시간 윈도우 $\\Delta$ 동안 참조된 페이지 집합을 메모리에 상주 보장 | 지역성 완벽 반영, 스래싱 사전 차단 | 적정 윈도우 크기($\\Delta$) 동적 산출 난이도 |
| **PFF (Page Fault Frequency)**| 프로세스의 페이지 부재 빈도 상한선/하한선 설정 기반 프레임 동적 조절 | 구현 용이, 직관적인 프레임 할당 | 급격한 지역성 이동 시 일시적 부재 급증 |
| **MPD 조절 (Degree of MPD)** | 스래싱 징후 감지 시 일부 프로세스를 디스크로 스왑아웃하여 유휴 프레임 확보 | 즉각적인 스래싱 해소 | 중단된 프로세스의 응답 지연 발생 |""",
        "sources": [
            "Peter J. Denning - The Working Set Model for Program Behavior (CACM)",
            "Abraham Silberschatz et al. - Operating System Concepts: Virtual Memory",
            "IEEE Transactions on Software Engineering: Paging and Thrashing Dynamics"
        ],
        "connections": "- 상위 토픽: [023 가상 메모리](./023_virtual_memory.md)\n- 연관 토픽: [060 페이징](./060_paging.md), [103 스래싱 (중복 토픽 정비)](./103_thrashing.md)"
    },

    "040_cache_coherence.md": {
        "insight": "멀티코어 시스템에서 각 코어의 로컬 캐시가 동일 메모리 주소에 대해 서로 다른 사본을 보유할 때 데이터 일치성을 하드웨어적으로 유지하는 프로토콜임.",
        "text_replacements": [],
        "rec_text": "소규모 SMP 멀티코어 환경에서는 버스 스누핑(MESI/MOESI)을 적용하고, 수십 개 이상의 대규모 NUMA/멀티소켓 서버에서는 인터커넥트 트래픽 확장을 위해 디렉터리 기반 프로토콜 채택.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ MESI 4대 캐시 상태 전이 다이어그램 ]                                │
│                                                                        │
│       ┌───────────────┐                  ┌───────────────┐             │
│       │ Modified (M)  │ ──(Bus Write)──> │  Invalid (I)  │             │
│       │ (수정됨, 유일) │ <──(Pr Write)─── │ (무효, 갱신필요)│            │
│       └───────┬───────┘                  └───────┬───────┘             │
│               │ (Bus Read)                       │ (Pr Read)           │
│               ▼                                  ▼                     │
│       ┌───────────────┐                  ┌───────────────┐             │
│       │  Shared (S)   │ <──(Pr Write)─── │ Exclusive (E) │             │
│       │ (공유됨, 동일)│ ──(Bus RdX)────> │ (클린, 단독)  │             │
│       └───────────────┘                  └───────────────┘             │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 일관성 유지 방식 | 제어 메커니즘 | 네트워크/버스 부하 | 시스템 확장성 (Scalability) | 주 적용 시스템 |
|---|---|---|---|---|
| **스누핑 (Snooping)** | 모든 코어가 공유 메모리 버스의 트래픽을 항상 감청 | 브로드캐스트 트래픽 급증 | 낮음 (최대 8~16개 코어 한계) | 소규모 데스크톱 CPU, SMP 서버 |
| **디렉터리 (Directory)** | 중앙 디렉터리에 캐시 블록의 공유 상태 및 위치 추적 | 점대점(Point-to-Point) 메시지 | 매우 높음 (수백~수천 코어 확장) | 대규모 분산 메모리, NUMA 서버 |""",
        "sources": [
            "John L. Hennessy, David A. Patterson - Computer Architecture: A Quantitative Approach (Chapter 5: Thread-Level Parallelism)",
            "Mark D. Hill - Multiprocessor Cache Coherence: A Primer on Memory Consistency and Cache Coherence",
            "Intel / AMD Multi-Core Cache Architecture Whitepaper"
        ],
        "connections": "- 상위 토픽: [051 캐시 메모리](./051_cache_memory.md)\n- 연관 토픽: [076 CPU](./076_cpu.md), [087 CMP](./087_cmp.md)"
    },

    "041_ai_hpc_infrastructure.md": {
        "insight": "초거대 AI 모델의 분산 학습과 초고속 추론을 지원하기 위해 고집적 가속기 팜, 무손실 로스리스 패브릭, 병렬 분산 파일시스템을 초밀집 결합한 인프라임.",
        "text_replacements": [],
        "rec_text": "GPU 간 올리듀스 통신 지연을 없애기 위해 InfiniBand NDR 또는 RoCEv2 기반의 레일 최적화(Rail-Optimized) 패브릭을 구축하고, GPUDirect Storage(GDS)로 스토리지 병목 제거.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 엔드투엔드 AI HPC 클러스터 인프라 아키텍처 ]                         │
│                                                                        │
│ [ 컴퓨팅 팜 ] GPU 노드 1 (8x H100) <───> GPU 노드 2 (8x H100)        │
│    │               │                          │               │        │
│    │ PCIe / NVLink │                          │ PCIe / NVLink │        │
│    ▼               ▼                          ▼               ▼        │
│ [ RoCEv2 / InfiniBand NDR 400G/800G 무손실 초저지연 패브릭 ]           │
│   - PFC (우선순위 흐름 제어) & ECN (명시적 혼잡 통지) 무손실 패킷 전송 │
│   - GPU 통신 버퍼 간 다이렉트 RDMA 초고속 동기화                       │
│    │                                                                   │
│    ▼ (GPUDirect Storage: CPU 메모리 경유 없는 제로카피 I/O)             │
│ [ 고성능 병렬 분산 파일시스템 (Lustre / GPFS / WekaIO NVMe All-Flash) ]│
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 인프라 계층 | 핵심 하드웨어 및 솔루션 | 해결하고자 하는 병목 | 핵심 성능 지표 |
|---|---|---|---|
| **컴퓨팅 계층** | 8x H100/B200 GPU 서버, HBM3e/HBM4 | 모델 파라미터 연산 지연 및 VRAM 용량 벽 | TFLOPS, MFU (Model Flops Utilization) |
| **네트워크 계층**| InfiniBand Quantum-2, 800G RoCEv2 | 분산 학습 올리듀스 통신 지연 및 패킷 드롭 | 레이턴시 (< 1$\mu s$), 유효 대역폭 |
| **스토리지 계층**| All-NVMe 병렬 파일시스템 (GDS 연계) | 체크포인트 I/O 정체 및 데이터 로딩 병목 | IOPS (수백만 단위), 읽기 대역폭 (GB/s) |
| **냉각/전력 계층**| 직접 칩 냉각(DLC), 액침 냉각, 100kW+ 랙 | 고발열로 인한 서멀 스로틀링(Throttling) | PUE (< 1.15), 수전 안정성 |""",
        "sources": [
            "NVIDIA SuperPOD Architecture Guidelines & High Performance Computing Best Practices",
            "IEEE Micro: Infrastructure for Giant AI Models: Challenges and Solutions",
            "Open Compute Project (OCP) High Performance Compute Sub-project Specs"
        ],
        "connections": "- 상위 토픽: [020 GPU](./020_gpu.md)\n- 연관 토픽: [028 액체 냉각](./028_liquid_cooling.md), [095 멀티 GPU 분산 학습](./095_multi_gpu_distributed_training.md)"
    },

    "042_ha_availability_assurance.md": {
        "insight": "단일 장애점(SPOF)을 제거하고 MTBF를 극대화하며 MTTR을 극소화하여 연간 중단 시간을 수 분 이내로 억제하는 고가용성 보증 프레임워크임.",
        "text_replacements": [],
        "rec_text": "가용률 99.999%(Five Nines) 달성을 위해 모든 인프라 계층(네트워크, 서버, 스토리지)에 n+1 또는 2n 이중화를 적용하고 카오스 엔지니어링 기반 주기적 장애 주입 시험 수행.",
        "rec_diagram": """```text
[ 가용도(Availability) 산식 체계 ]
                      MTBF (평균 무고장 시간)
  Availability = ─────────────────────────────────
                  MTBF + MTTR (평균 수리 복구 시간)

[ HA 가용성 보증을 위한 계층별 이중화 아키텍처 ]
┌────────────────────────────────────────────────────────┐
│ 전원/쿨링 계층: UPS 이중화, 비상 발전기 2N 구성        │
├────────────────────────────────────────────────────────┤
│ 네트워크 계층 : 이중화 L4/L7 로드밸런서, LACP 본딩     │
├────────────────────────────────────────────────────────┤
│ 서버 컴퓨팅  : Active-Active 클러스터, K8s Pod 다중화 │
├────────────────────────────────────────────────────────┤
│ 스토리지 계층: RAID 10/6, 실시간 동기 복제, 스냅샷     │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 가용성 지표 | 정의 | 최적화 목표 방향 | 기술적 단축/연장 방안 |
|---|---|---|---|
| **MTBF (Mean Time Between Failures)** | 고장과 다음 고장 사이의 평균 정상 가동 시간 | **최대화 (Maximize)** | 고품질 하드웨어, 예방 정비, 번인(Burn-in) 테스트 |
| **MTTR (Mean Time To Repair)** | 고장 발생 시점부터 정상 복구 완료까지 소요 시간 | **최소화 (Minimize)** | 핫스왑 부품, 자동 페일오버, 자동화된 재기동 스크립트 |
| **MTTD (Mean Time To Detect)** | 장애가 발생한 순간부터 모니터링이 인지하기까지 시간| **최소화 (Minimize)** | 실시간 Heartbeat, 합성 트랜잭션 모니터링, AIOps |""",
        "sources": [
            "IEEE Transactions on Reliability: High Availability System Design and Verification",
            "Evan Marcus, Hal Stern - Blueprints for High Availability (Wiley)",
            "Google Site Reliability Engineering (SRE) Handbook: Embracing Risk and Service Level Objectives"
        ],
        "connections": "- 상위 토픽: [021 HA](./021_ha.md)\n- 연관 토픽: [031 FTS](./031_fts.md), [065 멀티 리전 액티브-액티브 DR](./065_multi_region_active_active_dr.md)"
    },

    "043_datacenter_location_disaster_response.md": {
        "insight": "지진, 화재, 수해 등 광역 재난 상황에서도 전산 자원의 영속성을 보장하기 위해 지리적 안전 입지와 원격 재해복구(DR) 센터를 연계 구축하는 종합 방재 체계임.",
        "text_replacements": [
            ("재난 발생 시 인명 안전을 최우선으로 하고, 대체 센터 가동과 통신·전력 복구 상태를 확인한 뒤 핵심 업무 시스템부터 단계적으로 기동한다.",
             "재난 발생 시 인명 안전을 최우선으로 확보하고, 대체 센터 가동과 통신 및 전력 복구 상태를 검증한 뒤 핵심 업무 시스템부터 단계적 페일오버 수행.")
        ],
        "rec_text": "원거리 광역 재난에 대비하여 주 센터와 최소 30km 이상 이격된 원격 DR 센터를 배치하고, 비즈니스 영향 분석(BIA)에 근거한 RTO와 RPO 달성을 위한 데이터 복제 주기 수립.",
        "rec_diagram": """```text
┌──────────────────────────────┐               ┌──────────────────────────────┐
│ [ 주 데이터센터 (서울 주센터) ]│               │ [ 원격 DR 데이터센터 (영남권) ] │
│  - 내진 특등급 (진도 7.0 대응)│               │  - 동일 재난 영향권 밖 (>30km)│
│  - 수변전소 이중화 (2개 변전소)│               │  - 즉시 가동 대기 인프라     │
└──────────────┬───────────────┘               └──────────────┬───────────────┘
               │                                              │
               │ 실시간 비동기/준동기 데이터 복제 (DWDM 전송)   │
               ▼                                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ [ 재해 대응 페일오버 (DR Failover) 프로세스 ]                               │
│  재해 선포 ──> 글로벌 GSLB / DNS 라우팅 전환 ──> 원격 DR 센터 트랜잭션 수용│
│  (RTO: 복구 목표 시간 통제, RPO: 데이터 복구 시점 유실 제로화)              │
└─────────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| DR 복구 수준 | 복구 목표 시간 (RTO) | 복구 시점 목표 (RPO) | 인프라 구성 방식 | 비용 수준 |
|---|---|---|---|---|
| **Mirror Site** | 즉시 (수 초 이내) | 0 (실시간 동기 복제) | 완전 동일 이중화, Active-Active | 최고 |
| **Hot Site** | 수 시간 이내 | 수 분 ~ 수 시간 이내 | 대기 인프라 가동, Active-Standby | 높음 |
| **Warm Site** | 수 일 이내 | 수 일 이내 (주기적 백업) | 하드웨어 상시 구축, 데이터는 백업 복원 | 보통 |
| **Cold Site** | 수 주 이상 | 수 주 이전 백업 | 상면과 공조만 확보, 장비 사후 도입 | 최저 |""",
        "sources": [
            "ISO 22301: Business Continuity Management Systems (BCMS)",
            "행정안전부·한국지능정보사회진흥원(NIA) 국가정보자원관리원 재해복구체계 가이드라인",
            "Uptime Institute: Tier Standard: Topology and Operational Sustainability"
        ],
        "connections": "- 상위 토픽: [044 IDC 지리적 입지 선정](./044_idc_geographic_site_selection.md)\n- 연관 토픽: [014 DCI](./014_dci.md), [065 멀티 리전 액티브-액티브 DR](./065_multi_region_active_active_dr.md)"
    },

    "044_idc_geographic_site_selection.md": {
        "insight": "초대형 데이터센터의 무중단 가동을 보장하기 위해 특고압 수전 용량, 복수 변전소 인입, 냉각 수자원, 지반 안정성을 다각도로 검증하는 입지 선정 전략임.",
        "text_replacements": [
            ("목표 용량과 확장 단계에 맞춘 후보지를 선정하고, 전력 공급선·수자원·지반 안정성·위험 시설 이격 거리를 현장 실사와 공문서로 확인한다.",
             "목표 수전 용량과 단계별 확장 계획에 맞춘 복수 후보지를 선정하고, 전력 인입선, 냉각 수자원, 지반 안정성, 위험 시설 이격 거리를 현장 실사와 공문서로 전수 검증.")
        ],
        "rec_text": "한국전력 수전 용량 확보 여부를 최우선 검토하고, 서로 다른 154kV 변전소로부터의 이중 전력 인입 및 100년 빈도 홍수위/단층대 이격 거리를 철저히 조사.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ IDC 지리적 입지 선정 4대 핵심 검증 프레임워크 ]                     │
│                                                                        │
│ 1. 전력 인프라 (Power Grid)                                            │
│    - 154kV 이상 특고압 수전 가능성 (수십~수백 MW 용량 확보)             │
│    - 서로 다른 2개 이상의 변전소로부터 완전 물리적 이중 인입            │
│                                                                        │
│ 2. 냉각 수자원 및 기후 (Water & Climate)                               │
│    - 대용량 냉각수 공업용수 공급 능력 및 상하수도 인프라               │
│    - 외기 프리쿨링이 가능한 낮은 연평균 기온 및 습도 조건              │
│                                                                        │
│ 3. 지반 안정성 및 방재 (Geology & Hazards)                             │
│    - 활성 단층대 및 지진 위험 회피 (암반 지반 확보)                    │
│    - 100년 빈도 홍수 수위 이상의 고지대, 침수 위험 제로화              │
│                                                                        │
│ 4. 통신망 및 유해시설 이격 (Connectivity & Zoning)                     │
│    - 기간 통신 사업자(ISP) 복수 광케이블 인입로 확보                   │
│    - 위험물 저장소, 군사 기지, 공항 항로, 화학 공장 이격 거리 준수     │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 평가 항목 | 최적 적합 조건 | 부적합 판정 기준 | 비즈니스 영향도 |
|---|---|---|---|
| **전력망 (Power)** | 복수 변전소(154kV) 2N 물리 이중 인입 | 단일 변전소 의존 또는 전력 증설 불가 | 전력 차단 시 데이터센터 전면 셧다운 |
| **자연재해 (Natural Disaster)**| 단층대 밖 암반 지반, 백년 홍수위 5m 이상 | 침수 취약 저지대, 연약 지반 | 지진·침수로 인한 물리적 건물 붕괴 |
| **통신망 (Telecom)** | 3개사 이상 Tier-1 백본망 인입 경로 | 단일 통신사 독점 또는 맨홀 경로 단일화 | 굴착 공사 사고 시 네트워크 완전 고립 |
| **환경 규제 (Zoning)** | 공업용지, 데이터센터 전용 용도지역 | 주민 민원 다발 지역 (전자파/소음 논란) | 인허가 반려로 인한 사업 착공 불가 |""",
        "sources": [
            "ASHRAE Datacom Series: High Density Data Centers Location Selection",
            "Uptime Institute: Site Selection and Environmental Risk Standards",
            "한국데이터센터연합회(KDCC) 그린 데이터센터 인증 기준 및 입지 평가 지침"
        ],
        "connections": "- 상위 토픽: [043 데이터센터 입지 및 재해대응](./043_datacenter_location_disaster_response.md)\n- 연관 토픽: [014 DCI](./014_dci.md), [114 반도체 인프라 전력 용수](./114_semiconductor_infrastructure_power_water.md)"
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
