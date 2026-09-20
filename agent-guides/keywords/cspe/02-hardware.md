# 02 하드웨어 시스템 토픽

> 87개. 노트 폴더는 `src/content/docs/notes/cspe/02-hardware/`, 파일명은 `{3자리 번호}_{영문 snake_case}.md`다. 표기는 [README](../README.md)를 본다.

| 번호 | 토픽 | 등급 | 중요도 | 흡수한 하위 키워드 | 근거 |
|---|---|:---:|---:|---|---|
| 02-012 | 캐시 메모리 구조 — 직접·연관·집합 연관 매핑 (Cache Memory Mapping) | A | 90% | - | [출제:131,132,135] · 정보관리[137] · KPC 컴시응 3 |
| 02-014 | 캐시 일관성 프로토콜 — MESI·MOESI (Cache Coherence Protocol) | A | 90% | - | [출제:131,132,135,140] · 정보관리[137] · KPC 컴시응 3 |
| 02-025 | HBM 고대역폭 메모리 (High Bandwidth Memory) | A | 90% | 08-145 HBM 고대역폭 메모리 · 08-228 차세대 메모리 기술 HBM·CXL·PIM | [출제:129,137,140] · 정보관리[134] · KPC 컴시응 3 |
| 02-013 | 캐시 쓰기 정책 — Write-Through vs Write-Back (Cache Write Policy) | A | 85% | - | [출제:129,132,135] |
| 02-028 | CXL 컴퓨트 익스프레스 링크 (Compute Express Link) | A | 85% | 08-147 CXL | [출제:129,140] · 정보관리[136] · KPC 컴시응 2 |
| 02-032 | RAID 레벨 0·1·5·6·10 비교 (RAID Levels) | A | 85% | 02-092 RAID 컨트롤러·JBOD | [출제:122,125,131] · KPC 컴시응 4 |
| 02-034 | 인터럽트 처리 방식 — 벡터·데이지체인 (Interrupt Handling) | A | 85% | - | [출제:120,123,132] |
| 02-041 | GPU 아키텍처·SIMT 모델 (GPU SIMT) | A | 85% | 08-141 GPU | [출제:120,122,137] |
| 02-099 | 무선충전 기술 (Wireless Power Transfer) | A | 85% | - | [출제:125,126,129] |
| 02-020 | MMU 메모리 관리 장치 (Memory Management Unit) | A | 80% | - | [출제:135,137] |
| 02-030 | SSD FTL 플래시 변환 계층 (Flash Translation Layer) | A | 80% | - | [출제:128,138] |
| 02-035 | DMA 직접 메모리 접근 (Direct Memory Access) | A | 80% | - | [출제:123,137] |
| 02-036 | 버스 중재 방식 (Bus Arbitration) | A | 80% | - | [출제:128,137] |
| 02-044 | NPU 신경망 처리 장치 (Neural Processing Unit) | A | 80% | 08-052 Neural Processing Unit | [출제:134,140] · KPC 컴시응 2 |
| 02-051 | 뉴로모픽 컴퓨팅 (Neuromorphic Computing) | A | 80% | 08-149 뉴로모픽 컴퓨팅 | [출제:128,138] |
| 02-063 | 인터럽트 레이턴시·우선순위 역전 | A | 80% | - | [출제:135,137] · KPC 컴시응 3 |
| 02-001 | 컴퓨터 구조 개요 — 폰 노이만 vs 하버드 아키텍처 (Von Neumann vs Harvard Architecture) | A | 70% | - | [출제:138] |
| 02-002 | CPU 구성 — ALU·CU·레지스터·버스 (CPU Components) | A | 70% | - | [출제:138] |
| 02-003 | 명령어 집합 구조 — RISC vs CISC (RISC and CISC Instruction Set Architectures) | A | 70% | - | 핵심 기초(수동 지정) |
| 02-004 | RISC-V 개방형 ISA (RISC-V Open Standard ISA) | A | 70% | - | [출제:137] |
| 02-005 | ARM 프로세서 아키텍처·동작 모드 (ARM Architecture) | A | 70% | - | [출제:120,126] |
| 02-006 | 파이프라이닝 기본 구조 5단계 (Pipelining) | A | 70% | - | 핵심 기초(수동 지정) |
| 02-016 | TLB 변환 색인 버퍼 (Translation Lookaside Buffer) | A | 70% | - | 핵심 기초(수동 지정) |
| 02-022 | 메모리 계층 구조 (Memory Hierarchy) | A | 70% | - | [출제:140] |
| 02-024 | DDR SDRAM과 리프레시 방식 (DDR SDRAM Refresh) | A | 70% | - | [출제:123,129] |
| 02-040 | ASIC AI 가속 (ASIC AI Acceleration) | A | 70% | 08-144 ASIC AI Acceleration | [출제:140] |
| 02-102 | FRAM 강유전체 메모리 (Ferroelectric RAM) | A | 70% | - | [출제:138] |
| 02-103 | ROM 종류 — PROM·EPROM·EEPROM (Read Only Memory Types) | A | 70% | - | [출제:138] |
| 02-104 | 메모리 벽 (Memory Wall) | A | 70% | - | [출제:140] |
| 02-043 | TPU 텐서 처리 장치 (Tensor Processing Unit) | A | 65% | 08-053 Edge TPU · 08-142 TPU · 02-045 Edge TPU | 정보관리[138] · KPC 컴시응 4 |
| 02-056 | 데이터센터 등급 (Tier I~IV·Rated 1~4) | A | 65% | 06-038 데이터센터 등급 표준 | [출제:129] · 정보관리[134,140] · KPC 컴시응 1 |
| 02-105 | AI 팩토리 / 기가와트급 AI 데이터센터 | B | 75% | - | 시사·트렌드 · 정보관리 목록 04-062에서 가져옴 |
| 02-106 | UALink 1.0 (스케일업 인터커넥트) | B | 75% | - | 시사·트렌드 · 정보관리 목록 04-067에서 가져옴 |
| 02-107 | 에너지 효율 컴퓨팅 | B | 75% | - | 시사·트렌드 · 정보관리 목록 04-073에서 가져옴 |
| 02-018 | 페이지 교체 알고리즘 — OPT·FIFO·LRU·LFU (Page Replacement) | B | 65% | - | 정보관리[140] · KPC 컴시응 1 |
| 02-054 | 데이터 센터 서버 아키텍처 (Data Center Server Architecture) | B | 65% | - | 정보관리[134,140] · KPC 컴시응 1 |
| 02-110 | 스토리지 유형 비교(블록·파일·오브젝트) | B | 65% | - | 정보관리[132,140] · 정보관리 목록 04-123에서 가져옴 |
| 02-007 | 파이프라인 해저드 — 데이터·제어·구조 (Pipeline Hazards) | B | 60% | - | [출제:135] |
| 02-008 | 파이프라인 포워딩·분기 예측 (Pipeline Forwarding Branch Prediction) | B | 60% | - | [출제:120] |
| 02-010 | 멀티코어 프로세서 (Multicore Processor) | B | 60% | - | [출제:123] |
| 02-011 | 폴락의 법칙 (Pollack's Rule) | B | 60% | - | [출제:132] |
| 02-015 | 버스 스누핑·디렉터리 기반 일관성 (Bus Snooping Directory Coherence) | B | 60% | - | [출제:123] |
| 02-021 | NUMA 비균등 메모리 접근 (Non-Uniform Memory Access) | B | 60% | 03-029 NUMA 인지 스케줄링 | 핵심 기초(수동 지정) |
| 02-023 | DRAM과 SRAM 비교 (DRAM vs SRAM) | B | 60% | - | [출제:125] |
| 02-026 | PIM 메모리 내 처리 (Processing-in-Memory) | B | 60% | 08-146 메모리 내 처리 | [출제:129] |
| 02-027 | PNM 메모리 근접 처리 (Processing Near Memory) | B | 60% | - | [출제:131] |
| 02-029 | NVMe·PCIe 인터페이스 (NVMe PCIe) | B | 60% | - | [출제:123] |
| 02-031 | 3D V-NAND와 2D NAND 비교 (3D vs 2D NAND) | B | 60% | - | [출제:126] |
| 02-033 | I/O 인터페이스 — 폴링·인터럽트·DMA·채널 I/O (I/O Interface) | B | 60% | - | [출제:128] |
| 02-037 | 3-상태 버퍼·트라이스테이트 (Tri-State Buffer) | B | 60% | - | [출제:129] |
| 02-038 | SoC 시스템온칩 (System on Chip) | B | 60% | - | [출제:128] |
| 02-046 | AI 가속기 비교 — CPU·GPU·NPU·FPGA·ASIC (AI Accelerator Comparison) | B | 60% | 08-140 AI Accelerator AI 가속기 | [출제:126] · KPC 컴시응 2 |
| 02-049 | 칩렛 (Chiplet) | B | 60% | 08-148 칩렛 | [출제:131] |
| 02-052 | 병렬 컴퓨터 분류 — Flynn 분류 (Flynn's Taxonomy) | B | 60% | 02-053 SIMD·MIMD 프로세서 | [출제:134] |
| 02-055 | 전원 공급 장치·UPS | B | 60% | - | [출제:126] |
| 02-057 | 냉각 시스템 (공랭·직접 수랭·액침냉각) | B | 60% | - | 핵심 기초(수동 지정) |
| 02-061 | 실시간 운영체제 (RTOS) | B | 60% | 02-062 하드·펌·소프트 실시간 | 핵심 기초(수동 지정) |
| 02-065 | JTAG 디버깅 인터페이스 (JTAG) | B | 60% | - | [출제:126] |
| 02-066 | CAN 통신 (Controller Area Network) | B | 60% | 04-081 CAN 버스 자동차 통신 | [출제:129] |
| 02-071 | 디바이스 DNA (Device DNA) | B | 60% | - | [출제:125] |
| 02-072 | 양자 컴퓨팅 큐비트 (Quantum Computing Qubit) | B | 60% | 02-073 초전도·이온 트랩 양자 프로세서 · 08-212 Quantum Computing 양자컴퓨팅 | [출제:129] |
| 02-085 | 하드웨어 가상화 — VT-x·AMD-V (Hardware Virtualization) | B | 60% | - | 핵심 기초(수동 지정) |
| 02-095 | 연관 메모리 CAM (Content-Addressable Memory) | B | 60% | - | [출제:120] |
| 02-096 | PWM 펄스폭 변조 (Pulse Width Modulation) | B | 60% | - | [출제:120] |
| 02-097 | 스케일업·스케일아웃 (Scale-Up vs Scale-Out) | B | 60% | - | [출제:122] |
| 02-098 | NAND 셀 유형 — SLC·MLC·TLC (NAND Cell Types) | B | 60% | - | [출제:123] |
| 02-100 | 디지털 정보 디스플레이 DID (Digital Information Display) | B | 60% | - | [출제:128] · KPC 컴시응 1 |
| 02-101 | 제어장치 구현 방식 — 마이크로프로그램·하드와이어드 (Control Unit Implementation) | B | 60% | - | [출제:132] |
| 02-081 | 스토리지 가상화 (Storage Virtualization) | B | 55% | - | 정보관리[134] · KPC 컴시응 1 |
| 02-080 | 스토리지 계층 — DAS·NAS·SAN (Storage DAS NAS SAN) | B | 50% | - | KPC 컴시응 2 |
| 02-084 | SoC AI 온디바이스 칩 (SoC On-Device AI Chip) | B | 50% | - | KPC 컴시응 2 |
| 02-108 | 위상 큐비트 (Microsoft Majorana 1) | C | 65% | - | 시사·트렌드 · 정보관리 목록 04-115에서 가져옴 |
| 02-109 | 하이브리드 컴퓨팅 | C | 65% | - | 시사·트렌드 · 정보관리 목록 04-116에서 가져옴 |
| 02-009 | 명령어 수준 병렬성 ILP (Instruction-Level Parallelism) | C | 50% | - | - |
| 02-039 | FPGA AI 가속 (FPGA AI Acceleration) | C | 50% | 08-143 FPGA AI Acceleration | - |
| 02-042 | CUDA 병렬 컴퓨팅 (CUDA Parallel Computing) | C | 50% | - | - |
| 02-047 | NVLink 고속 인터커넥트 (NVLink) | C | 50% | 04-105 NVLink 고대역폭 인터커넥트 · 08-150 NVLink | - |
| 02-050 | UCIe 칩렛 인터커넥트 (Universal Chiplet Interconnect Express) | C | 50% | - | - |
| 02-058 | 전력 사용 효율 (PUE) | C | 50% | 02-059 물 사용 효율 · 06-040 데이터센터 물 사용 효율 지표 · 08-198 Power Usage Effectiveness 전력사용효율 · 08-199 Water Usage Effectiveness 물사용효율 · 06-039 데이터센터 전력 효율 지표 | - |
| 02-060 | 임베디드 시스템 구조 (Embedded System Architecture) | C | 50% | - | - |
| 02-074 | 양자 오류 정정·표면 코드 | C | 50% | 08-213 Quantum Error Correction 양자 오류 정정 · 08-214 Surface Code 표면 코드 · 08-215 Logical Qubit 논리 큐비트 · 02-075 논리 큐비트 vs 물리 큐비트 | - |
| 02-079 | PCIe 스위칭 아키텍처 (PCIe Switching) | C | 50% | - | - |
| 02-082 | 퍼시스턴트 메모리 (Persistent Memory) | C | 50% | - | - |
| 02-086 | 입출력 메모리 관리 장치 (IOMMU) | C | 50% | - | - |
| 02-090 | 3D 적층 메모리 (3D Stacked Memory) | C | 50% | - | - |
| 02-093 | 멀티소켓 서버·SMP (Multi-Socket Server·SMP) | C | 50% | - | - |
| 02-094 | 인터커넥트 토폴로지 — 팻트리·토러스 (Interconnect Topology — Fat-Tree·Torus) | C | 50% | - | - |

## 다른 과목 토픽으로 넘긴 키워드

같은 주제가 다른 과목에도 등록돼 있어 그쪽 토픽에 합쳤다. 이 과목에는 노트를 두지 않는다.

| 번호 | 키워드 | 넘긴 토픽 |
|---|---|---|
| 02-017 | 가상 메모리 — 페이징·세그멘테이션 (Virtual Memory Paging Segmentation) | 03-015 가상 메모리·페이징·세그멘테이션 (Virtual Memory) |
| 02-019 | 세그멘테이션 (Segmentation) | 03-015 가상 메모리·페이징·세그멘테이션 (Virtual Memory) |
| 02-048 | InfiniBand (InfiniBand) | 04-104 InfiniBand 클러스터 인터커넥트 (InfiniBand Cluster) |
| 02-064 | Arm TrustZone 보안 확장 | 05-127 Secure Boot 보안 부팅 (Secure Boot) |
| 02-067 | AUTOSAR 소프트웨어 플랫폼 | 08-206 AUTOSAR Adaptive (AUTOSAR Adaptive) |
| 02-068 | 보안 부팅 (Secure Boot) | 05-127 Secure Boot 보안 부팅 (Secure Boot) |
| 02-069 | 펌웨어 보안 취약점 | 05-125 임베디드 시스템 보안 취약점 (Embedded Security Vulnerabilities) |
| 02-070 | 물리적 복제 불가 함수 (PUF) | 05-127 Secure Boot 보안 부팅 (Secure Boot) |
| 02-087 | 서버 가상화 — Type 1·Type 2 하이퍼바이저 (Hypervisor Types) | 03-018 가상화 — Type 1·Type 2 하이퍼바이저 (Virtualization·Hypervisor) |
