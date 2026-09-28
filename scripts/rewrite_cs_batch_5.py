import os
import re
from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

DATA = {
    "084_san.md": {
        "insight": "고속 광채널(Fibre Channel) 스위치 패브릭을 기반으로 서버와 대용량 스토리지 어레이 간에 블록 단위 초고속 I/O를 전용 격리 제공함.",
        "text_replacements": [
            ("호스트 식별자와 존·LUN 매핑이 일치해야 장치가 보인다. 여러 경로가 보이면 MPIO로 쓸 수 있는 경로를 묶는다.",
             "호스트 WWPN 식별자와 FC 패브릭 존(Zone) 및 LUN 마스킹이 일치해야 스토리지 볼륨이 인식. 복수 경로 인식 시 MPIO(Multi-Path I/O)로 액티브-패시브 또는 라운드로빈 묶음 구성.")
        ],
        "rec_text": "단일 패브릭 장애 시 서비스 중단을 막기 위해 SAN 스위치와 HBA 포트를 완전히 분리된 듀얼 패브릭(Fabric A/B)으로 이중화하고 MPIO 다중경로 로드밸런싱 적용.",
        "rec_diagram": """```text
┌─────────────────────────┐               ┌─────────────────────────┐
│ [ 호스트 서버 1 (DB) ]  │               │ [ 호스트 서버 2 (WAS) ] │
│  - HBA Port 1 / Port 2  │               │  - HBA Port 1 / Port 2  │
└───────┬─────────┬───────┘               └───────┬─────────┬───────┘
        │         │                               │         │
        │ 광섬유  │ 광섬유                        │         │
        ▼         └───────────────────────────────┼────┐    │
┌──────────────────────────────┐                  ▼    ▼    ▼
│ [ SAN Fabric A (광스위치 1) ] │        ┌──────────────────────────────┐
│  - 독립된 존 1, 존 2 관리    │        │ [ SAN Fabric B (광스위치 2) ] │
└──────────────┬───────────────┘        │  - 물리적 완전 분리 이중화    │
               │                        └──────────────┬───────────────┘
               │ 32Gbps FC / NVMe-oF                   │
               ▼                                       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ [ 고성능 엔터프라이즈 스토리지 어레이 (Dual Active Controller) ]      │
│   - LUN 0 (DB Data 볼륨), LUN 1 (Log 볼륨)                           │
│   - LUN 마스킹: 호스트 WWPN별 접근 인가 통제                         │
└──────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| SAN 전송 기술 | 전송 매체 | 전송 프로토콜 | 최대 대역폭 | 장점 및 특징 |
|---|---|---|---|---|
| **FC SAN (Fibre Channel)** | 광섬유 케이블 | FC-PH, SCSI over FC | 32G / 64G FC | 초저지연, 무손실(Lossless) 크레딧 기반 흐름제어 |
| **IP SAN (iSCSI)** | 표준 구리 UTP / 광 | SCSI over TCP/IP | 10G / 25G / 100G | 기존 이더넷 인프라 활용으로 구축 비용 대폭 절감 |
| **FCoE (FC over Ethernet)**| 인핸스드 이더넷 | FC 프레임 over 10GbE | 10G / 40G / 100G | LAN과 SAN 케이블 단일 통합 (CNA 어댑터 필요) |
| **NVMe-oF (over Fabric)** | FC 또는 RoCEv2 이더넷 | NVMe over RDMA/TCP | 100G / 200G / 400G | 차세대 초저지연 플래시 스토리지 전용 패브릭 |""",
        "sources": [
            "ANSI INCITS: Fibre Channel Physical and Signaling Interface (FC-PH) Standards",
            "Storage Networking Industry Association (SNIA) SAN Architecture Guide",
            "IEEE Communications Magazine: Evolution of Storage Area Networks"
        ],
        "connections": "- 상위 토픽: [123 스토리지 유형 비교](./123_storage_type_comparison.md)\n- 연관 토픽: [080 NAS](./080_nas.md), [081 스토리지 가상화](./081_storage_virtualization.md)"
    },

    "085_virtual_machine.md": {
        "insight": "하이퍼바이저를 통해 단일 물리 하드웨어를 추상화하여 독립된 게스트 OS와 가상 하드웨어를 갖춘 복수의 가상 컴퓨터 환경을 완벽히 격리 실행함.",
        "text_replacements": [
            ("vCPU 할당, 메모리 오버커밋·NUMA, 가상 디스크 형식, 가상 네트워크 분리를 함께 조정한다. 호스트 장애에 대비해 공유 스토리지 기반 실시간 마이그레이션(Live Migration) 경로를 둔다.",
             "vCPU 할당, 메모리 오버커밋 및 vNUMA 노드 바인딩, 가상 디스크 형식(Thick/Thin), 가상 브리지 네트워크 격리 조정. 호스트 장애 대비 공유 스토리지 기반 무중단 라이브 마이그레이션 구성.")
        ],
        "rec_text": "게스트 OS 간 CPU/메모리 경합을 방지하기 위해 가상 소켓-코어 토폴로지(vNUMA)를 물리 NUMA 노드와 1:1 정렬하고, SR-IOV로 가상 네트워크 지연을 극소화.",
        "rec_diagram": """```text
┌─────────────────────────────────┐     ┌─────────────────────────────────┐
│ [ Virtual Machine 1 ]           │     │ [ Virtual Machine 2 ]           │
│  - 게스트 애플리케이션 (App)    │     │  - 게스트 애플리케이션 (App)    │
│  - 게스트 OS (Linux Kernel)     │     │  - 게스트 OS (Windows Server)   │
│  - 가상 디바이스 (vCPU, vRAM)   │     │  - 가상 디바이스 (vCPU, vRAM)   │
├─────────────────────────────────┴─────┴─────────────────────────────────┤
│ [ Type-1 하이퍼바이저 가상화 계층 (VMware ESXi / Linux KVM) ]           │
│   - CPU 스케줄러 & vNUMA 토폴로지 매핑                                  │
│   - 가상 메모리 관리 (EPT/NPT 확장 페이지 테이블 하드웨어 가속)         │
│   - VirtIO 반가상화 드라이버 인터페이스                                 │
├─────────────────────────────────────────────────────────────────────────┤
│ [ 물리 서버 하드웨어 (Intel Xeon / AMD EPYC, 물리 메모리, NIC, HBA) ]   │
└─────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 가상 머신 (VM) | 운영체제 컨테이너 (Container) |
|---|---|---|
| **가상화 수준** | 하드웨어 수준 완전 가상화 (Hardware Virtualization) | OS 커널 수준 가상화 (OS-level Virtualization) |
| **운영체제 종속성**| 게스트 OS 완전 독립 (Windows 위에 Linux 구동 가능) | 호스트 OS 커널 공유 (Linux 컨테이너는 Linux 커널 필수) |
| **보안 격리도** | **최고 (하드웨어 VT-x/AMD-V 기반 완벽한 물리적 격리)**| 보통 (동일 커널 취약점 공유 시 탈출 가능) |
| **기동 시간 및 오버헤드**| 수십 초 ~ 수 분 (OS 전체 부팅), 기가바이트 메모리 점유 | 수 초 이내 즉시 기동, 수십 메가바이트 경량 오버헤드 |""",
        "sources": [
            "Gerald J. Popek, Robert P. Goldberg - Formal Requirements for Virtualizable Third Generation Architectures",
            "VMware vSphere Virtual Machine Administration and Best Practices Guide",
            "NIST Special Publication 800-125: Guide to Security for Full Virtualization Technologies"
        ],
        "connections": "- 상위 토픽: [061 하이퍼바이저](./061_hypervisor.md)\n- 연관 토픽: [032 컨테이너](./032_container.md), [037 VDI](./037_vdi.md)"
    },

    "086_intermittent_computing.md": {
        "insight": "배터리 없이 주변 환경 에너지(태양광, RF, 진동)를 수확하여 동작하는 극저전력 IoT 장치에서 잦은 정전 발생 시 비휘발성 메모리 체크포인팅으로 연산 연속성을 보장함.",
        "text_replacements": [
            ("외부 장치 쓰기나 입력 읽기는 재실행 때 중복되면 안 되므로 입력 식별자와 쓰기 커밋 시점을 분리한다. 확정되지 않은 원격 통신은 전원 복구 후 다시 확인한다.",
             "외부 I/O 쓰기나 입력 읽기는 정전 후 재실행 시 중복 방지를 위해 멱등적 트랜잭션과 비휘발성 체크포인트를 결합하여 커밋 분리. 미확정 통신은 전원 회복 후 재전송 프로토콜 수립.")
        ],
        "rec_text": "전원 차단 직전 전압 강하를 감지하여 핵심 레지스터와 프로그램 카운터를 FRAM/MRAM에 원자적으로 저장(JIT Checkpointing)하고, I/O 연산의 멱등성(Idempotency)을 설계.",
        "rec_diagram": """```text
[ 에너지 하베스팅 (태양광/RF/진동) ] ──> [ 커패시터 에너지 충전 ]
                                               │
                                               ▼
┌────────────────────────────────────────────────────────┐
│ 전원 공급 개시 (V_on 도달) ──> 이전 체크포인트 복원 후 실행│
│                                                        │
│ [ 에너지 고갈 위기 (V_warn 임계치 감지) ]               │
│   1. 즉시 외부 인터럽트 발생                           │
│   2. CPU 레지스터 및 콜 스택을 FRAM/ReRAM에 즉시 백업  │
│   3. 전원 차단 (V_off 도달 및 시스템 정지)             │
│                                                        │
│ [ 에너지 재충전 (V_on 재도달) ]                        │
│   1. 비휘발성 메모리로부터 레지스터 상태 복원          │
│   2. 중단된 지점부터 연산 재개 (Forward Progress 달성)  │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 체크포인팅 방식 | 동작 원리 | 체크포인트 오버헤드 | 에너지 활용 효율 |
|---|---|---|---|
| **정적 체크포인팅 (Static)** | 프로그래머나 컴파일러가 루프/함수 진입점에 코드 삽입 | 고정된 주기적 오버헤드 발생 | 정전 전까지 에너지가 남아도 조기 체크포인트 낭비 |
| **적시 체크포인팅 (Just-In-Time)**| 커패시터 전압 모니터링으로 전원 고갈 직전에만 캡처 | 평상시 런타임 오버헤드 0 | 전압 감지 회로 정밀도 및 초고속 비휘발성 쓰기 필수 |
| **작업 기반 (Task-Based)** | 시스템을 멱등성을 갖는 작은 원자적 태스크 단위로 분할 | 태스크 완료 시에만 상태 커밋 | 태스크 실행 도중 정전 시 해당 태스크 전체 재실행 |""",
        "sources": [
            "ACM Computing Surveys: Intermittent Computing on Energy-Harvesting Device Architecture",
            "IEEE Micro: Intermittent Computing: Challenges and Opportunities",
            "USENIX ASPLOS: Non-Volatile Memory and Checkpointing for Batteryless Sensors"
        ],
        "connections": "- 상위 토픽: [011 엣지 컴퓨팅](./011_edge_computing.md)\n- 연관 토픽: [073 에너지 고효율 컴퓨팅](./073_energy_efficient_computing.md), [097 메모리 반도체](./097_memory_semiconductor.md)"
    },

    "087_cmp.md": {
        "insight": "이종의 멀티 클라우드 및 온프레미스 자원을 단일 인터페이스에서 통합 오케스트레이션하여 자원 프로비저닝, 비용 최적화(FinOps), 보안 정책 통제를 일원화함.",
        "text_replacements": [
            ("동일 요청이라도 계정별 API·자원 한도가 다를 수 있어, 호출 인증, 한도 차감, 재시도·큐잉을 워크플로우에 둔다.",
             "클라우드 관리 플랫폼(CMP)에서 계정별 멀티테넌트 API 쿼터 및 자원 한도를 식별하고 인증, 비용 차감, 오케스트레이션 워크플로우 적용.")
        ],
        "rec_text": "단일 벤더 의존을 차단하기 위해 플러그인 기반 이기종 CSP 어댑터 아키텍처를 채택하고, 실시간 클라우드 자원 사용량과 비용 청구서를 분석하는 자동 FinOps 파이프라인 연계.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 클라우드 관리 플랫폼 (CMP: Cloud Management Platform) 아키텍처 ]     │
│                                                                        │
│   [ 셀프서비스 서비스 카탈로그 ]    [ FinOps 비용 대시보드 ]  [ 보안 거버넌스 ] │
│   └──────────────────────┬─────────────────┬───────────────────┬───────┘
│                          │                 │                   │
│                          ▼                 ▼                   ▼
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ CMP 중앙 오케스트레이션 및 정책 엔진 (Policy & Workflow Engine)│   │
│   │  - 멀티테넌시 권한 제어 (RBAC) 및 승인 워크플로우             │   │
│   │  - 프로비저닝 자동화 (Terraform / Ansible 연동)                │   │
│   └──────────────────────────────┬─────────────────────────────────┘   │
│                                  │ 표준 어댑터 계층 (API Adapters)    │
│         ┌────────────────────────┼────────────────────────┐            │
│         ▼                        ▼                        ▼            │
│ ┌──────────────┐         ┌──────────────┐         ┌──────────────┐     │
│ │ [ AWS 어댑터]│         │ [ Azure 어댑터]        │ │[온프레미스 vSphere]│
│ └──────────────┘         └──────────────┘         └──────────────┘     │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| CMP 핵심 기능 영역 | 세부 주요 기능 | 비즈니스 가치 |
|---|---|---|
| **프로비저닝 오케스트레이션** | 카탈로그 기반 셀프서비스 인프라 자동 생성 | 인프라 배포 리드타임 수 주에서 수 분으로 단축 |
| **비용 관리 및 최적화 (FinOps)**| 미사용 자원(Zombie VM) 탐지, RI/SP 추천, 쇼백/차지백 | 클라우드 인프라 낭비 비용 20~30% 절감 |
| **거버넌스 및 정책 준수** | 규정 위반 보안그룹 자동 차단, 태그(Tagging) 표준 강제 | 전사 클라우드 컴플라이언스 및 감사 리스크 통제 |
| **관측성 및 SLA 모니터링** | 이기종 클라우드 통합 인프라 헬스체크 및 성능 대시보드 | 단일 창(Single Pane of Glass) 운영 가시성 확보 |""",
        "sources": [
            "Gartner Magic Quadrant for Cloud Management Platforms (CMP)",
            "NIST Special Publication 500-325: Cloud Interoperability and Management",
            "FinOps Foundation: Framework for Multi-Cloud Cost Optimization"
        ],
        "connections": "- 상위 토픽: [009 멀티 클라우드](./009_multi_cloud.md)\n- 연관 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md), [053 IaC](./053_iac.md)"
    },

    "088_cloud_service_security_vulnerabilities.md": {
        "insight": "클라우드 공유 책임 모델 하에서 관리자의 설정 오류(Misconfiguration), 과다 권한, 비인가 API 노출로 인해 발생하는 데이터 침해 및 침해 사고 위험임.",
        "text_replacements": [
            ("관리 API 호출과 데이터 접근 로그를 같은 자산 ID로 묶어야 설정 변경과 유출 발생의 인과관계를 복원할 수 있다.",
             "관리 API 감사 로그와 객체 스토리지 접근 로그를 동일한 리소스 ARN/자산 ID로 상관분석하여 비인가 권한 상승 및 유출 경로 추적 체계화.")
        ],
        "rec_text": "오픈된 S3 버킷 및 비인가 포트 노출을 원천 차단하기 위해 CSPM(클라우드 보안 태세 관리) 도구를 연동하여 인프라 설정 드리프트를 실시간 탐지하고 자동 교정.",
        "rec_diagram": """```text
[ 클라우드 위협 행위자 ] ──(공격 표면 스캐닝: Shodan, API Enumeration)──>
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 클라우드 주요 취약점 공격 벡터 ]                                     │
│  1. 스토리지 설정 오류: S3 버킷 Public Read/Write 개방 -> 데이터 유출   │
│  2. IAM 과다 권한: 와일드카드(*) 권한 부여로 인한 권한 상승 (PrivEsc) │
│  3. 하드코딩된 API 키 노출: GitHub 퍼블릭 커밋으로 인한 크리덴셜 탈취 │
│  4. 인프라 메타데이터 서비스(IMDSv1) SSRF 공격 -> 임시 세션 토큰 탈취 │
└──────────────────────────────────────┬─────────────────────────────────┘
                                       │
                                       ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 클라우드 네이티브 보안 방어 체계 ]                                   │
│  - CSPM : 인프라 설정 오류 및 규제 위반 실시간 자동 탐지/치유         │
│  - CIEM : IAM 최소 권한(Least Privilege) 원칙 분석 및 미사용 권한 회수 │
│  - CWPP : 컨테이너 및 VM 런타임 이상 행위 및 취약점 탐지/격리          │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 클라우드 보안 솔루션 | 주요 방어 영역 | 핵심 동작 원리 | 해결하는 취약점 |
|---|---|---|---|
| **CSPM (태세 관리)** | 인프라 구성 및 스토리지/네트워크 | API를 통해 CIS 벤치마크 및 설정 오류 검사 | S3 버킷 공개 노출, 방화벽 0.0.0.0/0 허용 |
| **CIEM (권한 관리)** | 클라우드 IAM 사용자 및 역할(Role) | 권한 사용 이력을 분석하여 과다 권한 식별 | 불필요한 관리자 권한, 탈취된 토큰 악용 |
| **CWPP (워크로드 보호)**| VM 인스턴스, 컨테이너, 서버리스 | 에이전트/eBPF 기반 런타임 이상 프로세스 탐지 | 컨테이너 탈출, 악성 마이너 삽입, 웹 쉘 |
| **CNAPP (통합 플랫폼)**| 개발부터 런타임 전 수명주기 | CSPM + CIEM + CWPP 통합 플랫폼 | 사일로화된 클라우드 보안 도구의 일원화 |""",
        "sources": [
            "CSA (Cloud Security Alliance) - Top Threats to Cloud Computing (Pandora's Box)",
            "OWASP Cloud Top 10 Security Risks",
            "NIST Special Publication 800-145 / 800-53: Cloud Security Assessment Guidelines"
        ],
        "connections": "- 상위 토픽: [013 클라우드 컴퓨팅](./013_cloud_computing.md)\n- 연관 토픽: [110 CSP 위험관리](./110_csp_risk_management.md), [009 멀티 클라우드](./009_multi_cloud.md)"
    },

    "089_inode.md": {
        "insight": "리눅스/유닉스 파일시스템에서 파일 이름과 실제 데이터를 분리하여 파일의 메타데이터(크기, 권한, 소유자, 블록 주소 포인터)를 저장하는 핵심 자료구조임.",
        "text_replacements": [
            ("경로 문자열을 디렉터리 엔트리로 탐색해 대상 inode를 찾는다. 이름을 바꿔도 링크 수와 데이터 블록은 유지될 수 있다.",
             "경로 문자열을 디렉터리 엔트리(dentry)로 순차 탐색하여 고유 inode 번호 식별. 하드 링크 생성 시 동일 inode를 공유하며 링크 카운트 갱신.")
        ],
        "rec_text": "디스크 잔여 용량이 남아있어도 소형 파일 폭증 시 아이노드 고갈(No space left on device)이 발생하므로 `df -i` 명령으로 아이노드 사용률을 정기 모니터링.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 리눅스 파일시스템 Inode 구조체 및 데이터 블록 매핑 ]                 │
│                                                                        │
│   [ Inode 구조체 (보통 128 또는 256 바이트) ]                          │
│     - 파일 모드 (File Mode: 권한, 파일 유형)                           │
│     - 소유자 UID / 그룹 GID                                            │
│     - 파일 크기 (File Size in Bytes)                                   │
│     - 타임스탬프 (atime, mtime, ctime)                                 │
│     - 링크 카운트 (Hard Link Count)                                    │
│     ┌──────────────────────────────────────────────────────────────┐   │
│     │ 12개 직접 블록 포인터 (Direct Block Pointers: 0~11)          │───┼─> [ Data Block ]
│     ├──────────────────────────────────────────────────────────────┤   │
│     │ 1개 단일 간접 포인터 (Single Indirect Pointer: 12)           │───┼─> [ Pointer Block ] ──> [ Data Block ]
│     ├──────────────────────────────────────────────────────────────┤   │
│     │ 1개 이중 간접 포인터 (Double Indirect Pointer: 13)           │───┼─> [ Ptr Block ] ──> [ Ptr Block ] ──> [ Data ]
│     ├──────────────────────────────────────────────────────────────┤   │
│     │ 1개 삼중 간접 포인터 (Triple Indirect Pointer: 14)           │   │
│     └──────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 링크 유형 | Inode 참조 메커니즘 | 원본 파일 삭제 시 동작 | 다른 파일시스템(파티션) 연결 |
|---|---|---|---|
| **하드 링크 (Hard Link)** | 디렉터리 엔트리가 원본과 **완전히 동일한 Inode 번호** 가리킴 | 링크 카운트만 1 감소, 파일 데이터 유지 | **불가 (동일 파일시스템 내에서만 성립)** |
| **심볼릭 링크 (Soft Link)**| 독립된 신규 Inode 생성 후 원본 파일의 **경로 문자열** 저장 | 원본 삭제 시 깨진 링크(Dangling Link) 발생 | **완벽 지원 (원격/타 파티션 연결 가능)** |""",
        "sources": [
            "Maurice J. Bach - The Design of the UNIX Operating System: Inodes and File Systems",
            "Robert Love - Linux System Programming: File and Directory Management",
            "Ext4 Disk Layout Documentation: Inodes, Extents, and Block Allocation"
        ],
        "connections": "- 상위 토픽: [024 디스크 스케줄링](./024_disk_scheduling.md)\n- 연관 토픽: [080 NAS](./080_nas.md), [056 RAID](./056_raid.md)"
    },

    "090_did.md": {
        "insight": "원격 중앙 관리 서버(CMS)와 IP 네트워크로 연결된 디지털 디스플레이 단말을 통해 타깃 고객에게 맞춤형 미디어 콘텐츠와 공공 정보를 실시간 표출함.",
        "text_replacements": [
            ("CMS가 콘텐츠를 수신·스케줄링하고, 대상 단말을 지정해 플레이어 앱에 배포하면 화면에 표출한다. 화면 단절이 발생하면 로컬 캐시 콘텐츠를 비상 표출한다.",
             "중앙 CMS가 미디어 콘텐츠를 스케줄링하여 네트워크로 단말에 배포하면 사이니지 플레이어가 렌더링 표출. 통신 장애 시 로컬 스토리지 캐시를 활용한 비상 로컬 표출 수행.")
        ],
        "rec_text": "네트워크 단절 시 화면 멈춤(Blackout)을 방지하기 위해 로컬 스토리지에 콘텐츠를 캐싱하는 오프라인 비상 재생 모드를 구축하고 전용 펌웨어 보안 무결성 검증.",
        "rec_diagram": """```text
[ 중앙 콘텐츠 관리자 (CMS 운영자) ] ──(콘텐츠 제작, 편성표 스케줄링)──>
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ [ DID 중앙 서버 (Digital Information Display CMS) ]    │
│   - 미디어 트랜스코딩 및 편성 스케줄러                 │
│   - 단말 원격 상태 관제 (온도, 팬 속도, 전원 제어)    │
└────────────────────────┬───────────────────────────────┘
                         │
                         │ IP 네트워크 암호화 전송 (HTTPS / MQTT)
                         ▼
┌────────────────────────────────────────────────────────┐
│ [ 원격 옥외/실내 DID 디스플레이 단말 계층 ]            │
│   ┌────────────────────┐      ┌────────────────────┐   │
│   │ [ 사이니지 단말 1] │      │ [ 사이니지 단말 2] │   │
│   │  - 플레이어 앱     │      │  - 플레이어 앱     │   │
│   │  - 로컬 캐시 볼륨  │      │  - 로컬 캐시 볼륨  │   │
│   │  - 하드웨어 Watchdog│      │  - 하드웨어 Watchdog│  │
│   └────────────────────┘      └────────────────────┘   │
└────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| DID 구성 요소 | 핵심 기능 및 역할 | 주요 고려사항 |
|---|---|---|
| **중앙 CMS 서버** | 영상/이미지 트랜스코딩, 채널별 편성표 배포, 사용자 권한 관리 | 대규모 동시 배포 시 네트워크 트래픽 분산(CDN 연계) |
| **미디어 플레이어** | 디코딩 하드웨어 가속, 화면 렌더링, 오프라인 로컬 캐시 저장 | 24x365 가동을 위한 하드웨어 Watchdog 타이머 내장 |
| **디스플레이 패널** | 고휘도(Outdoor 2,500+ nit), 눈부심 방지, 방수/방진(IP66) | 옥외 환경 직사광선 서멀 스로틀링 및 잔상(Burn-in) 방지 |""",
        "sources": [
            "Digital Signage Federation (DSF) Standards and Architecture Guidelines",
            "IEEE Transactions on Broadcasting: Digital Signage Network Systems",
            "한국전자통신연구원(ETRI) 스마트 디지털 사이니지 기술 및 표준 동향"
        ],
        "connections": "- 상위 토픽: [011 엣지 컴퓨팅](./011_edge_computing.md)\n- 연관 토픽: [037 VDI](./037_vdi.md), [080 NAS](./080_nas.md)"
    },

    "091_race_condition.md": {
        "insight": "두 개 이상의 프로세스나 스레드가 동기화 없이 공유 메모리에 동시 접근할 때 실행 순서와 타이밍에 따라 최종 결과값이 달라지는 동시성 결함임.",
        "text_replacements": [],
        "rec_text": "경쟁 조건을 원천 방지하기 위해 임계구역(Critical Section) 진입 시 상호배제(Mutex/Semaphore)를 적용하고, 락 프리 원자적 연산(CAS: Compare-And-Swap) 활용.",
        "rec_diagram": """```text
[ 경쟁 조건 (Race Condition) 발생 시나리오: count = 0 초기 상태 ]

  [ 스레드 A (count++) ]                    [ 스레드 B (count++) ]
            │                                         │
  1. count(0) 로드 (RegA = 0)                         │
            │                                2. count(0) 로드 (RegB = 0)
  3. RegA + 1 = 1                                     │
            │                                4. RegB + 1 = 1
  5. count에 1 저장 (count = 1)                       │
            │                                6. count에 1 저장 (count = 1)
            ▼                                         ▼
  * 정상 결과는 2여야 하나, 실행 타이밍 경합으로 최종 결과값이 1로 덮어써짐!

[ 해결책: 뮤텍스 락(Mutex Lock)을 통한 상호 배제 보장 ]
  스레드 A: Lock 획득 ──> [ 임계구역 실행: count++ ] ──> Lock 반환
  스레드 B:              대기(Blocked) ─────────────────> Lock 획득 후 안전 실행
```""",
        "rec_table": """| 동기화 메커니즘 | 동작 원리 | 차단(Blocking) 방식 | 장점 및 주의점 |
|---|---|---|---|
| **뮤텍스 (Mutex)** | 단 하나의 스레드만 락을 소유 (이진 락) | 슬립 락 (Sleep Lock: 컨텍스트 스위칭) | 단순성 우수, 락 미반환 시 교착상태 위험 |
| **스핀락 (Spinlock)** | 락을 획득할 때까지 CPU를 점유하며 루프 확인 | 바쁜 대기 (Busy Waiting) | 짧은 임계구역에서 문맥 교환 비용 절감, 장시간 대기 시 CPU 낭비 |
| **세마포어 (Semaphore)**| 카운터 기반으로 N개의 스레드 동시 진입 허용 | 시그널링 (P/Wait, V/Signal) | 자원 풀 관리 최적, 잘못된 V 호출 시 동기화 파괴 |
| **CAS (Atomic CAS)** | 하드웨어 지원 원자적 비교 및 교체 연산 | 락-프리 (Lock-Free 동시성) | 락 오버헤드 전무, ABA 문제 해결책 필요 |""",
        "sources": [
            "Abraham Silberschatz et al. - Operating System Concepts: Process Synchronization",
            "Maurice Herlihy, Nir Shavit - The Art of Multiprocessor Programming: Mutual Exclusion",
            "CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization"
        ],
        "connections": "- 상위 토픽: [122 프로세스 동기화](./122_process_synchronization.md)\n- 연관 토픽: [010 스레드](./010_thread.md), [038 데드락](./038_deadlock.md)"
    },

    "092_docker_swarm.md": {
        "insight": "별도 외부 도구 설치 없이 도커 엔진에 기본 내장되어 복수의 도커 호스트를 단일 가상 클러스터로 묶어 컨테이너 배포와 서비스를 오케스트레이션함.",
        "text_replacements": [],
        "rec_text": "매니저 노드의 과반 결손 시 클러스터 불능 상태를 방지하기 위해 Raft 합의 알고리즘에 맞추어 홀수(3대 또는 5대) 매니저 노드를 구성하고 자동 복구 구성.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 도커 스웜 (Docker Swarm) 클러스터 아키텍처 ]                         │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 매니저 노드 쿼럼 (Manager Nodes: Raft 분산 합의)               │   │
│   │  - Manager 1 (Leader) <───> Manager 2 <───> Manager 3          │   │
│   │  - 클러스터 상태 유지, 서비스 스케줄링, 디스패칭                │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │ (인증된 mTLS 터널 통신)            │
│       ┌───────────────────────────┴───────────────────────────┐        │
│       ▼                                                       ▼        │
│ ┌──────────────────────────────┐        ┌──────────────────────────────┐
│ │ [ 워커 노드 1 (Worker Node) ]│        │ [ 워커 노드 2 (Worker Node) ]│
│ │   - Docker Engine / SwarmKit │        │   - Docker Engine / SwarmKit │
│ │   - Ingress Routing Mesh     │        │   - Ingress Routing Mesh     │
│ │   ┌────────┐    ┌────────┐   │        │   ┌────────┐    ┌────────┐   │
│ │   │ Task 1 │    │ Task 2 │   │        │   │ Task 3 │    │ Task 4 │   │
│ │   └────────┘    └────────┘   │        │   └────────┘    └────────┘   │
│ └──────────────────────────────┘        └──────────────────────────────┘
│   │                                                               │    │
│   └────── VXLAN 오버레이 네트워크 (Overlay Network: IPsec 암호화) ┴────┘
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비교 축 | 도커 스웜 (Docker Swarm) | 쿠버네티스 (Kubernetes) |
|---|---|---|
| **설치 및 복잡도** | 도커 엔진 자체 내장 (`docker swarm init`), 매우 단순 | 별도 마스터/워커 컴포넌트(etcd, API서버 등) 구성, 복잡도 극상 |
| **학습 곡선** | 표준 Docker CLI 명령어 문법 그대로 활용 (학습 비용 최저)| 방대한 선언적 YAML 객체 및 개념 숙지 필요 (학습 곡선 가파름) |
| **생태계 및 확장성** | 도커 단독 생태계, 수천 개 노드 이상의 초대형 클러스터 한계 | 사실상의 글로벌 클라우드 표준, CNCF 거대 에코시스템 지원 |
| **자동 확장 및 복구** | 서비스 복제본 유지 및 롤링 업데이트 지원, HPA 미지원 | Pod/노드 자동 확장(HPA/VPA/CA) 및 고도화된 자가 치유 지원 |""",
        "sources": [
            "Docker Documentation: Swarm Mode Overview and Key Concepts",
            "IEEE International Conference on Cloud Computing: Performance Comparison of Kubernetes and Docker Swarm",
            "Adrian Mouat - Using Docker: Developing and Deploying Software with Containers (O'Reilly)"
        ],
        "connections": "- 상위 토픽: [032 컨테이너](./032_container.md)\n- 연관 토픽: [012 쿠버네티스](./012_kubernetes.md), [013 클라우드 컴퓨팅](./013_cloud_computing.md)"
    },

    "093_little_endian.md": {
        "insight": "연속된 바이트 데이터의 최하위 바이트(LSB)를 가장 낮은 메모리 주소부터 순서대로 저장하는 방식으로, x86 및 최신 ARM 프로세서의 표준 바이트 순서임.",
        "text_replacements": [],
        "rec_text": "네트워크 패킷 송수신 시 빅 엔디안 표준인 네트워크 바이트 순서(Network Byte Order)와 호스트 순서 간의 변환 함수(`htonl`, `ntohl`)를 필수 호출하여 정합성 보장.",
        "rec_diagram": """```text
[ 4바이트 16진수 정수값: 0x12345678 (MSB=0x12, LSB=0x78) ]

  메모리 주소:    0x1000       0x1001       0x1002       0x1003
                ┌────────────┬────────────┬────────────┬────────────┐
  리틀 엔디안 : │    0x78    │    0x56    │    0x34    │    0x12    │  (LSB가 최저 주소)
                └────────────┴────────────┴────────────┴────────────┘
                 (x86, x64, 최신 스마트폰 ARM 프로세서 표준)

                ┌────────────┬────────────┬────────────┬────────────┐
  빅 엔디안   : │    0x12    │    0x34    │    0x56    │    0x78    │  (MSB가 최저 주소)
                └────────────┴────────────┴────────────┴────────────┘
                 (인터넷 네트워크 TCP/IP 표준, 사람의 가독 순서와 일치)
```""",
        "rec_table": """| 비교 축 | 리틀 엔디안 (Little-Endian) | 빅 엔디안 (Big-Endian) |
|---|---|---|
| **저장 순서** | 최하위 바이트(LSB)를 가장 낮은 주소에 저장 | 최상위 바이트(MSB)를 가장 낮은 주소에 저장 |
| **산술 연산 장점** | 덧셈/올림수(Carry) 연산 시 하위 바이트부터 즉시 계산 가능| 부호(Sign) 판별 및 크기 대소 비교를 최상위 바이트로 즉시 판별 |
| **타입 캐스팅** | 32비트 int를 16비트 short로 형변환 시 주소 변경 불필요 | 형변환 시 메모리 주소 오프셋 이동 연산 수반 |
| **표준 적용 영역** | x86, AMD64, ARM(LE 모드), RISC-V | TCP/IP 네트워크 헤더, 메인프레임, IBM AIX |""",
        "sources": [
            "Danny Cohen - On Holy Wars and a Plea for Peace (Internet Experiment Note 137: IEN 137)",
            "IETF RFC 791: Internet Protocol (Specification of Network Byte Order)",
            "Computer Systems: A Programmer's Perspective (CS:APP) - Data Sizes and Endianness"
        ],
        "connections": "- 상위 토픽: [105 엔디안](./105_endian.md)\n- 연관 토픽: [101 빅 엔디안](./101_big_endian.md), [076 CPU](./076_cpu.md)"
    },

    "094_multi_gpu.md": {
        "insight": "단일 서버 또는 클러스터 내에 복수의 GPU를 장착하고 초고속 인터커넥트(NVLink/NVSwitch)로 상호 연결하여 딥러닝 텐서 처리량과 VRAM 용량을 확장함.",
        "text_replacements": [],
        "rec_text": "CPU를 경유하지 않고 GPU 간 메모리를 고속 전송하기 위해 GPUDirect P2P 통신을 활성화하고, PCIe 토폴로지 상 동일 스위치 아래에 GPU 쌍을 배치하여 통신 지연 최소화.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 8-GPU 서버 노드 내부 토폴로지 (PCIe Switch vs NVLink Mesh) ]         │
│                                                                        │
│   ┌────────────────────┐                    ┌────────────────────┐     │
│   │ [ Host CPU 1 ]     │                    │ [ Host CPU 2 ]     │     │
│   └─────────┬──────────┘                    └─────────┬──────────┘     │
│             │ PCIe Gen5                               │ PCIe Gen5      │
│             ▼                                         ▼                │
│   ┌────────────────────┐                    ┌────────────────────┐     │
│   │ [ PCIe 스위치 1 ]  │                    │ [ PCIe 스위치 2 ]  │     │
│   └──┬──────┬────┬───┬─┘                    └──┬──────┬────┬───┬─┘     │
│      ▼      ▼    ▼   ▼                         ▼      ▼    ▼   ▼       │
│    GPU0   GPU1 GPU2 GPU3                     GPU4   GPU5 GPU6 GPU7     │
│      │      │    │   │                         │      │    │   │       │
│      └──────┴────┴───┴────── NVSwitch 패브릭 ──┴──────┴────┴───┴───────┘
│        (모든 GPU 간 양방향 900GB/s Full-Mesh 초고속 올-투-올 직결)     │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| GPU 인터커넥트 방식 | 물리적 매개체 | 전송 대역폭 (양방향) | 통신 지연 시간 | 병목 특성 |
|---|---|---|---|---|
| **전통적 PCIe Gen4/Gen5** | 메인보드 PCIe 슬롯 | 64 ~ 128 GB/s | 마이크로초 ($\mu s$) | 호스트 CPU 메모리 경유로 인한 병목 |
| **GPUDirect P2P (PCIe)**| PCIe 스위치 직결 | 64 ~ 128 GB/s | 1 $\mu s$ 미만 | CPU 경유 배제, PCIe 버스 대역폭 한계 |
| **NVLink 4.0 / 5.0** | 전용 고속 브리지/케이블 | 900 ~ 1,800 GB/s | **수백 나노초 ($ns$)** | 사실상의 칩 간 초고속 메모리 버스 |
| **NVSwitch 랙 패브릭**| 스위치 트레이 및 패브릭 | 130 TB/s (랙 전체) | 극저지연 무손실 | 고가의 전용 인프라 하드웨어 비용 |""",
        "sources": [
            "NVIDIA DGX Systems Architecture and NVLink Interconnect Technical Whitepaper",
            "IEEE Micro: NVLink and NVSwitch: The Architectural Fabric for Deep Learning",
            "Hot Chips: Scale-up and Scale-out Architectures for Modern GPU Supercomputers"
        ],
        "connections": "- 상위 토픽: [020 GPU](./020_gpu.md)\n- 연관 토픽: [095 멀티 GPU 분산 학습](./095_multi_gpu_distributed_training.md), [070 랙 스케일 AI 시스템](./070_rack_scale_ai_system.md)"
    },

    "095_multi_gpu_distributed_training.md": {
        "insight": "단일 GPU 메모리에 적재할 수 없는 초대형 모델을 훈련하기 위해 데이터 병렬(DDP), 파이프라인 병렬(PP), 텐서 병렬(TP), 완전 샤딩(FSDP)을 혼합 적용함.",
        "text_replacements": [
            ("FSDP는 모델 상태를 샤딩하고 순방향·역방향에 필요한 파라미터를 모은 뒤 그래디언트를 다시 줄인다. 모듈별 통신과 연산을 중첩한다.",
             "FSDP(Fully Sharded Data Parallel)는 모델 파라미터, 그래디언트, 옵티마이저 상태를 GPU 전역에 샤딩하고 순방향/역방향 계산 직전에 All-Gather 통신으로 복원한 뒤 즉시 해제.")
        ],
        "rec_text": "초대형 LLM 학습 시 통신 오버헤드를 줄이기 위해 노드 내부는 텐서 병렬화(Megatron-LM TP)를 적용하고, 노드 간에는 제로 버블 파이프라인 병렬화 및 FSDP를 결합한 3D 병렬화 채택.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ LLM 분산 훈련을 위한 3D 병렬화 (3D Parallelism: TP + PP + DP) ]      │
│                                                                        │
│   1. 텐서 병렬화 (Tensor Parallelism: TP)                              │
│      - 단일 Transformer 레이어 내부 행렬 곱셈을 복수 GPU에 분할       │
│      - 노드 내부(NVLink 초고대역)에서만 구동 필수 (All-Reduce 통신)    │
│                                                                        │
│   2. 파이프라인 병렬화 (Pipeline Parallelism: PP)                      │
│      - 모델 레이어들을 순차 그룹으로 나누어 다른 GPU 노드에 분적      │
│      - 활성화 값(Activation)만 노드 간 전송하여 네트워크 부하 절감    │
│                                                                        │
│   3. 데이터 병렬화 (FSDP / ZeRO-3)                                     │
│      - 파라미터, 그래디언트, 옵티마이저 상태 전체를 클러스터에 샤딩   │
│      - 연산 직전에만 All-Gather로 복원하고 연산 후 즉시 메모리 해제    │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 분산 학습 병렬화 기법 | 분할 대상 | 통신 빈도 및 패턴 | 권장 네트워크 환경 | 주 적용 목적 |
|---|---|---|---|---|
| **DDP (Data Parallel)** | 배치 데이터 분할 (모델 복제) | 매 스텝 역방향 시 All-Reduce | InfiniBand / 100GbE | 단일 GPU에 모델이 완전히 올라갈 때 |
| **ZeRO-3 / FSDP** | 파라미터, 그래디언트, 옵티마이저 | 순방향/역방향 매 레이어 All-Gather| RoCEv2 / InfiniBand | 거대 모델의 메모리 점유율을 1/N로 축소 |
| **텐서 병렬화 (TP)** | 선형 가중치 행렬 ($W_Q, W_K, W_V$)| 매 연산자마다 All-Reduce | **NVLink 필수 (초고대역)** | 거대 레이어 단일 GPU VRAM 초과 시 |
| **파이프라인 병렬 (PP)**| 수십 개의 전체 레이어 분할 | 스테이지 경계 간 P2P 통신 | 표준 노드 간 이더넷 가능 | 깊은 모델 분할 (버블 타임 제어 필요) |""",
        "sources": [
            "Samyam Rajbhandari et al. - ZeRO: Memory Optimizations Toward Training Trillion Parameter Models (DeepSpeed)",
            "Mohammad Shoeybi et al. - Megatron-LM: Training Multi-Billion Parameter Language Models",
            "PyTorch Documentation: Fully Sharded Data Parallel (FSDP) Architecture"
        ],
        "connections": "- 상위 토픽: [094 멀티 GPU](./094_multi_gpu.md)\n- 연관 토픽: [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md), [020 GPU](./020_gpu.md)"
    },

    "096_memory_hierarchy_interleaving.md": {
        "insight": "레지스터, 캐시, 메인 메모리, 스토리지로 이어지는 피라미드형 계층 구조와 뱅크 인터리빙을 결합하여 접근 비용을 낮추고 메모리 대역폭을 극대화함.",
        "text_replacements": [],
        "rec_text": "메모리 참조 지역성(시간적/공간적)을 극대화하도록 소스코드를 루프 타일링(Loop Tiling)하고, 하드웨어 레벨에서는 메모리 컨트롤러의 채널 및 뱅크 인터리빙을 활성화.",
        "rec_diagram": """```text
[ 메모리 피라미드 계층 구조 (Memory Hierarchy Pyramid) ]

         ▲       [ 레지스터 (Registers) ]       : < 1ns, 수백 Byte
        ╱ ╲      [ L1 / L2 / L3 SRAM 캐시 ]     : 1~10ns, 수십 MB
       ╱   ╲     [ 메인 메모리 (DRAM) ]          : 50~100ns, 수십~수백 GB
      ╱     ╲    [ 차세대 CXL / SCM 메모리 풀 ]  : 200~300ns, 수 TB
     ╱       ╲   [ NVMe SSD 스토리지 ]           : 수십 $\mu s$, 수십 TB
    ╱─────────╲  [ 네트워크 원격 스토리지 (NAS) ] : 수 $ms$, 페타바이트급
```""",
        "rec_table": """| 메모리 계층 | 주 소자 기술 | 평균 접근 지연 | 용량 범위 | 비트당 비용 | 휘발성 여부 |
|---|---|---|---|---|---|
| **CPU 레지스터** | 플립플롭 회로 | < 0.5 ns | 수백 바이트 | 최고가 | 휘발성 |
| **SRAM 캐시 (L1~L3)**| 6T SRAM | 1 ~ 15 ns | 수십 KB ~ 수십 MB | 고가 | 휘발성 |
| **메인 메모리 (DRAM)**| 1T1C DRAM | 50 ~ 80 ns | 16 GB ~ 수 TB | 보통 | 휘발성 |
| **솔리드 스테이트 (NAND)**| 3D V-NAND 플래시 | 20 ~ 100 $\mu s$ | 512 GB ~ 수십 TB | 저렴 | 비휘발성 |
| **광/마그네틱 테이프** | 자성 테이프 매체 | 수 초 ~ 수 분 | 페타바이트 (PB) | 최저가 | 비휘발성 |""",
        "sources": [
            "John L. Hennessy, David A. Patterson - Computer Architecture: A Quantitative Approach (Memory Hierarchy)",
            "Computer Systems: A Programmer's Perspective (CS:APP) - The Memory Hierarchy",
            "IEEE Transactions on Very Large Scale Integration (VLSI) Systems: Memory Interleaving"
        ],
        "connections": "- 상위 토픽: [051 캐시 메모리](./051_cache_memory.md)\n- 연관 토픽: [057 메모리 인터리빙](./057_memory_interleaving.md), [097 메모리 반도체](./097_memory_semiconductor.md)"
    },

    "097_memory_semiconductor.md": {
        "insight": "데이터를 저장하고 인출하는 반도체 소자로, 전하 기반의 DRAM/NAND에서 시작하여 3D TSV 기반 HBM과 CXL 솔루션으로 진화하고 있는 IT 핵심 인프라임.",
        "text_replacements": [
            ("HBM은 여러 DRAM 다이를 적층하고 TSV를 통해 초광대역 버스로 프로세서와 데이터를 교환한다.",
             "HBM은 복수의 DRAM 다이를 수직 적층하고 실리콘 관통 전극(TSV)으로 1024/2048비트 광대역 버스를 구성하여 호스트 GPU와 초고속 통신 수행.")
        ],
        "rec_text": "AI 가속기 병목을 해결하기 위해 HBM4와 로직 베이스 다이 협업을 강화하고, 서버 시스템에서는 메모리 용량 확장과 유휴 풀링을 위해 CXL 메모리 모듈 단계적 도입.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 차세대 메모리 반도체 기술 진화 축 ]                                  │
│                                                                        │
│   [ 1. 초고속/초광대역화 ]                                              │
│     - HBM3e (1.2TB/s) ──> HBM4 (2048비트 I/O, 3TB/s 대역폭)            │
│     - 첨단 2.5D 인터포저 및 하이브리드 본딩(Cu-Cu) 적층               │
│                                                                        │
│   [ 2. 용량 한계 극복 및 풀링화 ]                                      │
│     - 전통 DDR5 DIMM 슬롯 한계 극복                                    │
│     - CXL 3.0 / 4.0 메모리 확장기(CMM-D) 기반 랙 단위 메모리 공유     │
│                                                                        │
│   [ 3. 고밀도 비휘발성 대용량화 ]                                      │
│     - 3D V-NAND 300단/400단 초고층 수직 적층                          │
│     - QLC/PLC 기반 초고용량 엔터프라이즈 eSSD                          │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 메모리 반도체 분류 | 핵심 기술 구조 | 셀 동작 특성 | 장점 | 주요 단점 및 과제 |
|---|---|---|---|---|
| **DRAM (Dynamic RAM)** | 1 트랜지스터 + 1 커패시터 | 주기적 리프레시(Refresh) 필수 | 고집적, 빠른 접근 속도 | 미세화 물리적 한계, 휘발성 |
| **SRAM (Static RAM)** | 4~6개 트랜지스터 래치 회로 | 전원 유지 시 데이터 보존 | 최고속 (캐시 메모리) | 낮은 집적도, 고비용, 대면적 |
| **NAND Flash** | 플로팅 게이트 / 전하포획(CTF) | 블록 소거, 페이지 읽기/쓰기 | 비휘발성, 최고 집적도 | 쓰기 수명(Endurance) 한계 |
| **HBM (High Bandwidth)**| 다층 DRAM + 수직 TSV 관통 | 수천 비트 와이드 I/O 버스 | 테라비트급 대역폭 돌파 | 패키징 난이도, 고발열, 고비용 |""",
        "sources": [
            "IEEE International Solid-State Circuits Conference (ISSCC): Memory Technology Trends",
            "JEDEC Solid State Technology Association Standards (DDR5, HBM3, LPDDR5)",
            "한국반도체산업협회(KSIA) 차세대 메모리 반도체 기술 개발 로드맵"
        ],
        "connections": "- 상위 토픽: [079 HBM](./079_hbm.md)\n- 연관 토픽: [100 비메모리 반도체](./100_non_memory_semiconductor.md), [027 HBM4](./027_hbm4.md)"
    },

    "098_metaheuristics.md": {
        "insight": "복잡한 NP-난해 조합 최적화 문제에서 다항 시간 내에 최적해에 근접한 양질의 해를 도출하기 위해 자연 현상과 직관을 수리 모델링한 상위 수준 발견적 탐색 기법임.",
        "text_replacements": [],
        "rec_text": "탐색 공간의 전역 탐색(Exploration)과 국소 탐색(Exploitation) 간의 균형을 유지하기 위해 유전 알고리즘과 타부 서치(Tabu Search)를 결합한 하이브리드 메타휴리스틱 적용.",
        "rec_diagram": """```text
[ 메타휴리스틱 (Metaheuristics) 탐색 공간 균형 메커니즘 ]

                    [ 전체 해 탐색 공간 (Search Space) ]
                                    │
       ┌────────────────────────────┴────────────────────────────┐
       ▼                                                         ▼
 [ 다각화 (Diversification / Exploration) ]   [ 집중화 (Intensification / Exploitation) ]
  - 전역 공간을 폭넓게 탐색하여 미답 구역 방문 - 유망한 후보해 주변을 정밀하게 국소 집중 탐색
  - 지역 최적점(Local Optima) 탈출 기제 제공   - 우수한 해의 수렴 속도 가속화
  - 대표 기법: 돌연변이, 메트로폴리스 확률 수용 - 대표 기법: 교차 연산, 경사 하강, 타부 메모리
```""",
        "rec_table": """| 메타휴리스틱 분류 | 대표 알고리즘 | 영감을 얻은 원리 | 주요 특징 및 장점 |
|---|---|---|---|
| **진화 알고리즘 (Evolutionary)** | 유전 알고리즘 (GA), 유전자 프로그래밍 | 다윈의 생물 진화 및 적자생존 | 집단 기반 병렬 탐색, 복잡한 제약조건 최적화 |
| **물리/수학 기반 (Physics-based)**| 담금질 기법 (Simulated Annealing) | 금속을 가열 후 서서히 냉각하는 어닐링 | 나쁜 해를 확률적으로 수용하여 지역 최적점 탈출 |
| **군집 지능 (Swarm Intelligence)**| 입자 군집 최적화 (PSO), 개미 군집 (ACO)| 새 떼의 비행 군집, 개미의 페로몬 경로 | 단순 개체 간 상호작용으로 집단 지성 해 도출 |
| **궤적 기반 (Trajectory)** | 타부 탐색 (Tabu Search) | 인간의 기억 및 금지 목록(Tabu List) | 최근 방문 경로를 금지하여 무한 루프 회피 |""",
        "sources": [
            "Fred Glover, Gary A. Kochenberger - Handbook of Metaheuristics (Springer)",
            "Zong Woo Geem - Music-Inspired Harmony Search Algorithm and Applications",
            "IEEE Transactions on Evolutionary Computation: Metaheuristic Search Surveys"
        ],
        "connections": "- 상위 토픽: [074 유전 알고리즘](./074_genetic_algorithm.md)\n- 연관 토픽: [107 워크플로우 스케줄링 백필](./107_workflow_scheduling_backfill.md), [019 CPU 스케줄링](./019_cpu_scheduling.md)"
    },

    "099_backfill.md": {
        "insight": "HPC 클러스터에서 대규모 선두 작업의 예약 실행 시간을 지연시키지 않는 한도 내에서 큐 후순위의 작은 단기 작업을 유휴 노드에 끼워 넣어 가동률을 극대화함.",
        "text_replacements": [],
        "rec_text": "작업의 정확한 월타임(Walltime) 추정치가 백필 성공의 핵심이므로 사용자 선언 실행 시간에 패널티를 부여하고 기계학습 기반 실행 시간 예측 모델 결합 권고.",
        "rec_diagram": """```text
[ 백필 스케줄링 (Backfill Scheduling) 실행 원리 ]

 시간 축 ──>
 노드 0 │ [ 실행 중인 작업 A ] ───> [ 대형 예약 작업 C (노드 0~3 전체 요구) ]
 노드 1 │ [ 실행 중인 작업 A ] ───> [ 대형 예약 작업 C ]
 노드 2 │ [ 빈 공간 (Hole) ] ────> [ 대형 예약 작업 C ]  <── 작업 C 시작 전까지 노드 2, 3 유휴!
 노드 3 │ [ 빈 공간 (Hole) ] ────> [ 대형 예약 작업 C ]
        └─────────────────────────────────────────────────────────────
         * 후순위 단기 작업 B가 노드 2개를 2시간만 사용한다면?
           ──> 작업 C의 예약 시작 시점(Shadow Time) 전에 종료되므로 [빈 공간]에 백필 즉시 배치!
```""",
        "rec_table": """| 백필 기법 | 동작 기준 | 스케줄러 오버헤드 | 클러스터 이용률 |
|---|---|---|---|
| **EASY 백필 (Extensible Argonne)** | 오직 **가장 앞선 1순위 대형 작업의 시작 시간만 보장** | 낮음 (선두 1개 작업만 섀도우 타임 계산) | 매우 우수함 (현대 HPC 표준) |
| **보수적 백필 (Conservative)** | 큐에 대기 중인 **모든 작업의 예약 시작 시간을 절대 지연시키지 않음** | 높음 (모든 대기 작업의 미래 타임라인 시뮬레이션)| 상대적으로 낮음 (끼워넣기 제약 엄격) |""",
        "sources": [
            "David Lifka - High-Performance Job Scheduling on the IBM SP2: The EASY Scheduler",
            "Dror G. Feitelson - Workload Modeling for Computer Systems Performance Evaluation",
            "Slurm Workload Manager Documentation: Backfill Scheduling Plugin"
        ],
        "connections": "- 상위 토픽: [107 워크플로우 스케줄링 백필](./107_workflow_scheduling_backfill.md)\n- 연관 토픽: [019 CPU 스케줄링](./019_cpu_scheduling.md), [035 SJF](./035_sjf.md)"
    },

    "100_non_memory_semiconductor.md": {
        "insight": "단순 데이터 저장이 아닌 연산, 제어, 신호 처리 등 지능적 논리 처리를 수행하는 시스템 반도체로, 팹리스-파운드리-OSAT의 글로벌 분업 생태계가 핵심임.",
        "text_replacements": [],
        "rec_text": "초미세 공정 설계 비용 폭증과 물리적 한계를 극복하기 위해 검증된 서드파티 반도체 IP 라이브러리를 적극 활용하고 UCIe 표준 기반의 칩렛 모듈화 패키징 도입.",
        "rec_diagram": """```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 시스템/비메모리 반도체 글로벌 분업 가치사슬 생태계 ]                │
│                                                                        │
│   [ 반도체 IP 기업 (ARM, Synopsys) ]                                   │
│     - 회로 설계 자산 및 표준 IP 블록 라이선스 제공                    │
│                     │                                                  │
│                     ▼                                                  │
│   [ 팹리스 (Fabless: Apple, NVIDIA, Qualcomm) ]                        │
│     - 제조 공장 없이 혁신적인 시스템 반도체 칩 아키텍처 직접 설계      │
│                     │                                                  │
│                     ▼ (GDSII 포맷 설계 도면 전달)                      │
│   [ 디자인 하우스 (Design House) ]                                      │
│     - 파운드리 제조 공정에 최적화되도록 물리 레이아웃 설계 변환       │
│                     │                                                  │
│                     ▼                                                  │
│   [ 파운드리 (Foundry: TSMC, 삼성전자) ]                                │
│     - 극자외선(EUV) 노광 장비 기반 2nm/3nm 초미세 웨이퍼 위탁 생산     │
│                     │                                                  │
│                     ▼                                                  │
│   [ OSAT (패키징 및 테스트 외주 전문 기업) ]                            │
│     - 웨이퍼 다이 절단, 범핑, 2.5D/3D 첨단 패키징 및 최종 품질 검사    │
└────────────────────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 비메모리 반도체 분류 | 대표 제품 및 소자 | 주요 기능 및 역할 | 핵심 기술 지향점 |
|---|---|---|---|
| **컴퓨팅/프로세서** | CPU, GPU, NPU, AP (애플리케이션 프로세서) | 시스템 제어 및 범용/인공지능 연산 처리 | 고IPC, 고효율 병렬성, 저전력 |
| **통신/모뎀 반도체** | 5G 베이스밴드 모뎀, Wi-Fi/BT 칩, 광트랜시버 | 아날로그 고주파 신호의 디지털 변환 및 송수신 | 고대역폭, 초저지연, 주파수 수율 |
| **센서/이미지 반도체**| CIS (CMOS 이미지 센서), ToF, 라이다 센서 | 빛, 소리, 압력 등 물리 신호를 전기 신호로 변환 | 초고화소, 고감도, 노이즈 억제 |
| **전력 반도체 (Power)**| PMIC, SiC / GaN 전력 소자 | 전력 변환, 전압 제어 및 전력 소비 최적화 | 고내전압, 고내열성, 스위칭 손실 제로화 |""",
        "sources": [
            "IEEE Solid-State Circuits Magazine: Evolution of System-on-Chip (SoC) Architectures",
            "Semiconductor Industry Association (SIA) State of the Industry Report",
            "산업통상자원부 시스템 반도체 및 첨단 패키징 육성 전략 보고서"
        ],
        "connections": "- 상위 토픽: [104 시스템 반도체 생태계](./104_system_semiconductor_ecosystem.md)\n- 연관 토픽: [097 메모리 반도체](./097_memory_semiconductor.md), [030 칩렛 UCIe](./030_chiplet_ucie_3_0.md)"
    },

    "101_big_endian.md": {
        "insight": "데이터의 최상위 바이트(MSB)를 가장 낮은 메모리 주소부터 순서대로 배치하여 사람이 숫자를 읽는 직관성과 일치하며 TCP/IP 네트워크 전송 표준임.",
        "text_replacements": [],
        "rec_text": "이종 아키텍처 간 소켓 통신 시 엔디안 불일치로 인한 데이터 변조를 차단하기 위해 송신 측에서 `htons`/`htonl`로 네트워크 표준으로 직렬화하고 수신 측에서 역변환.",
        "rec_diagram": """```text
[ 4바이트 정수값: 0x0A0B0C0D (MSB=0x0A, LSB=0x0D) ]

  메모리 번지:    Addr 0       Addr 1       Addr 2       Addr 3
                ┌────────────┬────────────┬────────────┬────────────┐
  빅 엔디안   : │    0x0A    │    0x0B    │    0x0C    │    0x0D    │  (사람의 읽기 순서와 일치)
                └────────────┴────────────┴────────────┴────────────┘
                 (네트워크 바이트 순서 Network Byte Order 표준)
```""",
        "rec_table": """| 비교 축 | 빅 엔디안 (Big-Endian) | 리틀 엔디안 (Little-Endian) |
|---|---|---|
| **저장 순서** | 최상위 바이트(MSB)를 최저 주소에 배치 | 최하위 바이트(LSB)를 최저 주소에 배치 |
| **네트워크 표준** | **인터넷 표준 (RFC 791 Network Byte Order)** | 표준 아님 (호스트 바이트 순서) |
| **디버깅 가독성**| 메모리 덤프 시 사람이 읽는 숫자 표기와 동일 | 메모리 덤프 시 바이트 순서가 역순으로 표시 |
| **대표 시스템** | TCP/IP 헤더, IBM 메인프레임, SPARC, Java 가상머신 | Intel x86/x64, AMD64, ARM(리틀엔디안 모드) |""",
        "sources": [
            "IETF RFC 791: Internet Protocol Specification - Transmission Order",
            "Danny Cohen - On Holy Wars and a Plea for Peace (IEN 137)",
            "Computer Systems: A Programmer's Perspective (CS:APP) - Byte Ordering"
        ],
        "connections": "- 상위 토픽: [105 엔디안](./105_endian.md)\n- 연관 토픽: [093 리틀 엔디안](./093_little_endian.md), [076 CPU](./076_cpu.md)"
    },

    "102_interconnection_network.md": {
        "insight": "병렬 컴퓨터와 대규모 분산 클러스터에서 프로세서, 메모리, 스토리지 노드 간의 데이터 교환을 지원하는 내부 통신 토폴로지 및 스위칭 패브릭 기술임.",
        "text_replacements": [],
        "rec_text": "대규모 AI 클러스터 구축 시 통신 직경(Diameter)과 바이섹션 대역폭(Bisection Bandwidth)을 최적화하기 위해 논블로킹 팻 트리(Fat-Tree) 또는 다차원 토러스 토폴로지 적용.",
        "rec_diagram": """```text
[ 주요 상호연결망 토폴로지 (Interconnection Network Topologies) ]

  [ 1. 2차원 토러스 (2D Torus) ]         [ 2. 3단계 팻 트리 (Fat-Tree) ]
      ○ ─── ○ ─── ○ ─── (순환 고리)          ┌─── Core Switches ───┐
      │     │     │                          │                     │
      ○ ─── ○ ─── ○                        Aggregation           Aggregation
      │     │     │                          │                     │
      ○ ─── ○ ─── ○                      Edge Switches         Edge Switches
      (각 끝단이 반대편과 순환 연결)       ┌──┴──┐               ┌──┴──┐
                                          Host  Host            Host  Host
```""",
        "rec_table": """| 토폴로지 구조 | 네트워크 직경 (Diameter) | 바이섹션 대역폭 | 노드당 차수 (Degree) | 확장성 및 적용 시스템 |
|---|---|---|---|---|
| **공유 버스 (Shared Bus)** | $O(1)$ | $O(1)$ (병목 발생) | 고정 (1개 버스 공유) | 소규모 SMP 멀티코어 내부 |
| **크로스바 스위치 (Crossbar)**| $O(1)$ | $O(N)$ (논블로킹) | $O(N)$ (회로비용 $N^2$) | 중간 규모 스위치 패브릭 |
| **2D / 3D 토러스 (Torus)** | $O(\sqrt[k]{N})$ | $O(N^{(k-1)/k})$ | 고정 ($2k$개 포트) | 구글 TPU v4/v5p 포드, 슈퍼컴퓨터 |
| **팻 트리 (Fat-Tree)** | $O(\log N)$ | $O(N)$ (완전 논블로킹) | 고정 (상위 스위치 증설) | 엔비디아 슈퍼팟(SuperPOD), 대형 데이터센터 |""",
        "sources": [
            "William J. Dally, Brian Towles - Principles and Practices of Interconnection Networks",
            "IEEE Micro: Interconnection Networks for High-Performance Computing",
            "Charles Clos - A Study of Non-Blocking Switching Networks (Bell System Technical Journal)"
        ],
        "connections": "- 상위 토픽: [041 AI HPC 인프라](./041_ai_hpc_infrastructure.md)\n- 연관 토픽: [111 토러스](./111_torus.md), [014 DCI](./014_dci.md)"
    },

    "103_thrashing.md": {
        "insight": "가용 물리 메모리가 부족하여 프로세스들이 지속적으로 페이지 폴트를 일으키고, CPU가 디스크 스왑 입출력 처리에 갇혀 시스템 처리율이 급감하는 현상임.",
        "text_replacements": [],
        "rec_text": "스래싱 발생 시 스왑 공간을 무작정 늘리는 대신 다중 프로그래밍 정도(MPD)를 낮추고, 프로세스별 참조 국소성을 보호하는 워킹셋 윈도우 크기를 동적으로 최적화.",
        "rec_diagram": """```text
[ 스래싱(Thrashing) 발생 및 진단 제어 아키텍처 ]

 [ 프로세스 집합의 총 메모리 요구량(Working Set 합) > 실제 물리 메모리 ]
                               │
                               ▼
 [ 지속적인 페이지 부재 (Page Fault) 폭증 및 디스크 I/O 큐 포화 ]
                               │
                               ▼
 [ CPU 이용률 급감 감지 (OS 스케줄러가 오판하여 프로세스 추가 투입 시 악화) ]
                               │
                               ▼
 ┌────────────────────────────────────────────────────────┐
 │ 스래싱 제어 서브시스템                                │
 │  1. PFF (Page Fault Frequency) 모니터링                 │
 │  2. 상한선 초과 프로세스에 추가 프레임 할당            │
 │  3. 가용 프레임 부족 시 일부 프로세스를 스왑아웃 (MPD 감소) │
 └────────────────────────────────────────────────────────┘
```""",
        "rec_table": """| 스래싱 완화 기법 | 제어 메커니즘 | 장점 | 주의점 |
|---|---|---|---|
| **워킹셋 (Working Set) 관리** | 최근 시간 $\\Delta$ 동안 참조된 페이지 집합을 메모리에 상주 보장 | 지역성 충실 반영 | 적정 $\\Delta$ 산출 알고리즘 오버헤드 |
| **PFF (페이지 부재 빈도)** | 페이지 부재율 상한선/하한선 설정 기반 동적 프레임 할당 | 직관적인 프레임 조절 | 급격한 페이즈 전환 시 일시적 지연 |
| **ZRAM / ZSWAP 메모리 압축** | 디스크 I/O 대신 메모리 내부에서 페이지 압축 보관 | 디스크 I/O 병목 원천 차단 | 압축/해제에 따른 경미한 CPU 부하 |""",
        "sources": [
            "Peter J. Denning - Working Sets Past and Present (IEEE Transactions on Software Engineering)",
            "Abraham Silberschatz et al. - Operating System Concepts: Virtual Memory",
            "Linux Kernel Documentation: Memory Management and vm.swappiness Tuning"
        ],
        "connections": "- 상위 토픽: [039 스래싱](./039_thrashing.md)\n- 연관 토픽: [023 가상 메모리](./023_virtual_memory.md), [060 페이징](./060_paging.md)"
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
