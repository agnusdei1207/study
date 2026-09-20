# 03 시스템·응용 SW 토픽

> 157개. 노트 폴더는 `src/content/docs/notes/cspe/03-software/`, 파일명은 `{3자리 번호}_{영문 snake_case}.md`다. 표기는 [README](../README.md)를 본다.

| 번호 | 토픽 | 등급 | 중요도 | 흡수한 하위 키워드 | 근거 |
|---|---|:---:|---:|---|---|
| 03-245 | 데이터 가치평가·데이터 자산화 | A | 100% | - | 정보관리[135,139,140] · 시사·트렌드 · 정보관리 목록 03-002에서 가져옴 |
| 03-004 | 프로세스 스케줄링 알고리즘 — FCFS·SJF·RR·MLFQ·CFS (Process Scheduling) | A | 90% | 03-005 멀티레벨 피드백 큐 MLFQ · 03-006 CFS 완전 공정 스케줄러 | [출제:135,138,140] · 정보관리[137] |
| 03-141 | 클라우드 서비스 모델 — IaaS·PaaS·SaaS (Cloud Service Models) | A | 90% | - | [출제:122,125,131,137] · 정보관리[134] · KPC 컴시응 4 |
| 03-009 | 교착상태 조건·예방·회피·탐지·복구 (Deadlock) | A | 85% | - | [출제:132,134,138] |
| 03-012 | 세마포어·뮤텍스·모니터 (Semaphore Mutex Monitor) | A | 85% | 03-013 스핀락 vs 뮤텍스 | [출제:120,126,132,138] |
| 03-015 | 가상 메모리·페이징·세그멘테이션 (Virtual Memory) | A | 85% | 02-017 가상 메모리 — 페이징·세그멘테이션 · 02-019 세그멘테이션 | [출제:126,138] · 정보관리[139] · KPC 컴시응 2 |
| 03-056 | DevOps 파이프라인 (DevOps Pipeline) | A | 85% | 03-054 지속적 배포 | [출제:131,138] · 정보관리[136] · KPC 컴시응 2 |
| 03-246 | AI 네이티브 개발 플랫폼 | A | 85% | - | 시사·트렌드 · 정보관리 목록 02-046에서 가져옴 |
| 03-011 | 기아·에이징 (Starvation Aging) | A | 80% | - | [출제:137,140] |
| 03-080 | SP 소프트웨어 프로세스 품질 인증 (SP Quality Certification) | A | 80% | - | [출제:134,137] |
| 03-159 | 서버리스 컴퓨팅·FaaS (Serverless Computing·FaaS) | A | 75% | 08-160 Serverless Computing 서버리스 · 08-161 서비스형 함수 | [출제:140] · 정보관리[136,140] · KPC 컴시응 1 |
| 03-165 | SLO·SLA·SLI (SLO·SLA·SLI) | A | 75% | 03-166 오류 예산 · 06-015 SLO·SLI · 06-016 오류 예산 · 08-173 SLO 서비스수준목표 · 08-174 Error Budget 오류 예산 | [출제:138] · 정보관리[134,137,139] · KPC 컴시응 1 |
| 03-001 | 프로세스 vs 스레드 (Process vs Thread) | A | 70% | - | 핵심 기초(수동 지정) |
| 03-010 | 은행원 알고리즘 (Banker's Algorithm) | A | 70% | - | 핵심 기초(수동 지정) |
| 03-018 | 가상화 — Type 1·Type 2 하이퍼바이저 (Virtualization·Hypervisor) | A | 70% | 02-087 서버 가상화 — Type 1·Type 2 하이퍼바이저 | KPC 컴시응 3 · 핵심 기초(수동 지정) |
| 03-028 | 다중 프로세서 스케줄링 — SQMS·MQMS (Multiprocessor Scheduling SQMS MQMS) | A | 70% | - | [출제:129,135] |
| 03-034 | XP — 페어 프로그래밍·TDD (Extreme Programming) | A | 70% | - | [출제:123,129] |
| 03-053 | CI/CD 파이프라인 (CI/CD Pipeline) | A | 70% | - | [출제:140] · KPC 컴시응 1 |
| 03-063 | 카나리 배포·블루-그린 배포 (Canary Blue-Green Deployment) | A | 70% | - | [출제:132,135] |
| 03-086 | 트랜잭션 격리 수준 4단계 (Transaction Isolation Levels) | A | 70% | - | 정보관리[134,137] · 핵심 기초(수동 지정) |
| 03-089 | 데이터베이스 정규화 1NF~BCNF (Database Normalization) | A | 70% | - | 핵심 기초(수동 지정) |
| 03-093 | 인덱스 구조 — B+Tree·해시·복합 (Index Structure) | A | 70% | 03-094 클러스터드 인덱스·커버링 인덱스 | 핵심 기초(수동 지정) |
| 03-097 | B-Tree vs LSM-Tree 비교 (B-Tree vs LSM-Tree) | A | 70% | - | [출제:140] |
| 03-151 | VM vs 컨테이너 비교 (VM vs Container) | A | 70% | - | [출제:128,132] |
| 03-152 | 쿠버네티스 아키텍처 (Kubernetes Architecture) | A | 70% | 08-158 Kubernetes 쿠버네티스 · 08-159 Container Orchestration 컨테이너 오케스트레이션 · 03-153 쿠버네티스 Pod 생명주기 · 03-154 쿠버네티스 Pod 스케줄링 · 03-155 쿠버네티스 서비스·인그레스 · 03-157 쿠버네티스 스토리지 — PVC·PV·StorageClass · 04-062 쿠버네티스 네트워킹 - CNI·Ingress · 03-156 쿠버네티스 NetworkPolicy·CNI | 정보관리[133,137] · 핵심 기초(수동 지정) |
| 03-161 | 클라우드 네이티브 관측성 (Cloud Native Observability) | A | 70% | 08-169 클라우드 네이티브 관측성 · 03-162 OpenTelemetry · 03-163 분산 추적 · 08-170 OpenTelemetry · 08-171 Distributed Tracing 분산 추적 | [출제:140] |
| 03-177 | 분산 합의 — Raft·Paxos (Distributed Consensus Raft Paxos) | A | 70% | - | 핵심 기초(수동 지정) |
| 03-202 | MLOps 파이프라인 (MLOps Pipeline) | A | 70% | 08-128 MLOps · 03-204 피처 스토어 · 03-205 모델 레지스트리 · 03-206 모델 모니터링·드리프트 감지 · 08-132 피처 스토어 · 08-133 모델 레지스트리 | [출제:138] · KPC 컴시응 1 |
| 03-215 | 카오스 엔지니어링 (Chaos Engineering) | A | 70% | - | [출제:140] |
| 03-234 | 기능안전 IEC 61508·SIL (Functional Safety IEC 61508 SIL) | A | 70% | - | [출제:120,123] · KPC 컴시응 3 |
| 03-238 | SIL·HIL 테스팅 (Software/Hardware-in-the-Loop Testing) | A | 70% | - | [출제:137] |
| 03-239 | 시스템 콜 (System Call) | A | 70% | - | [출제:138] |
| 03-240 | 상속보다 조합 원칙 (Composition over Inheritance) | A | 70% | - | [출제:140] |
| 03-058 | 소프트웨어 테스트 — 단위·통합·시스템·인수 (Software Testing) | A | 65% | - | [출제:122] · 정보관리[133,134,139] · KPC 컴시응 1 |
| 03-071 | ATAM 아키텍처 트레이드오프 분석 방법 (Architecture Tradeoff Analysis Method) | A | 65% | 03-072 CBAM 비용 편익 분석 방법 · 06-037 ATAM 아키텍처 트레이드오프 분석 · 03-221 소프트웨어 아키텍처 품질 속성 트레이드오프 | [출제:131] · 정보관리[140] · KPC 컴시응 2 |
| 03-091 | 데이터베이스 무결성 제약 조건 (Database Integrity Constraints) | A | 65% | - | [출제:134] · 정보관리[135,138] · KPC 컴시응 2 |
| 03-092 | 개체 무결성·참조 무결성 (Entity Referential Integrity) | A | 65% | - | [출제:128] · 정보관리[138] · KPC 컴시응 1 |
| 03-125 | 데이터 레이크 (Data Lake) | A | 65% | - | [출제:122] · 정보관리[137,139] · KPC 컴시응 1 |
| 03-143 | 멀티 클라우드 전략 (Multi Cloud Strategy) | A | 65% | - | [출제:135] · 정보관리[132,135] · KPC 컴시응 1 |
| 03-170 | SOAP vs REST 비교 (SOAP vs REST) | A | 65% | - | [출제:135] · 정보관리[133,134] · KPC 컴시응 2 |
| 03-183 | SBOM 소프트웨어 자재명세서 (SBOM) | A | 65% | 08-187 SBOM 소프트웨어 자재명세서 · 03-184 취약점 악용 가능성 교환 | [출제:134] · 정보관리[134,136] · KPC 컴시응 1 |
| 03-191 | PMO 프로젝트 관리 위탁 (PMO) | A | 65% | - | [출제:132] · 정보관리[135,136,140] · KPC 컴시응 5 |
| 03-211 | 메모리 누수·힙 고갈 (Memory Leak Heap Exhaustion) | A | 65% | - | [출제:123] · 정보관리[136] · KPC 컴시응 1 |
| 03-039 | 마이크로서비스 아키텍처 MSA (Microservice Architecture) | A | 60% | - | [출제:120] · KPC 컴시응 3 |
| 03-070 | CMMI 성숙도 모델 (Capability Maturity Model Integration) | A | 60% | - | [출제:125] · KPC 컴시응 3 |
| 03-078 | 기능 안전 ISO 26262·ASIL (Functional Safety ISO 26262) | A | 60% | - | [출제:134] · KPC 컴시응 3 |
| 03-022 | I/O 관리·디스크 스케줄링 (I/O Management Disk Scheduling) | B | 65% | - | 정보관리[137] |
| 03-037 | UML 다이어그램 유형 (UML Diagrams) | B | 65% | - | 정보관리[137] · KPC 컴시응 2 |
| 03-047 | 디자인 패턴 — GoF 23종 (Design Patterns GoF) | B | 65% | - | 정보관리[136] |
| 03-060 | 화이트박스·블랙박스 테스트 (White-box Black-box Testing) | B | 65% | - | 정보관리[134,137,139] |
| 03-114 | 분산 데이터베이스 (Distributed Database) | B | 65% | - | 정보관리[132,139] |
| 03-126 | 데이터 레이크하우스 (Data Lakehouse) | B | 65% | 08-189 Data Lakehouse 데이터 레이크하우스 · 03-127 Delta Lake · 03-128 Apache Iceberg · 03-129 오픈 테이블 포맷 비교 · 03-130 메달리온 아키텍처 · 08-192 Open Table Format 오픈 테이블 포맷 · 08-190 Delta Lake · 08-191 Apache Iceberg | 정보관리[137,139] · KPC 컴시응 1 |
| 03-149 | 오토 스케일링 HPA·VPA (Auto Scaling HPA VPA) | B | 65% | - | 정보관리[133,137] |
| 03-241 | 좀비 프로세스(Zombie Process) | B | 65% | - | 정보관리[140] · 정보관리 목록 04-048에서 가져옴 |
| 03-242 | 프로세스 메모리 영역(코드·데이터·힙·스택) | B | 65% | - | 정보관리[138] · 정보관리 목록 04-050에서 가져옴 |
| 03-243 | 메타모픽 테스트(Metamorphic Test) | B | 65% | - | 정보관리[135,140] · 정보관리 목록 02-030에서 가져옴 |
| 03-244 | 로우코드·노코드(LCNC) | B | 65% | - | 정보관리[138] · 정보관리 목록 02-203에서 가져옴 |
| 03-002 | PCB·컨텍스트 스위칭 (PCB Context Switching) | B | 60% | 03-003 프로세스 생성·종료·상태 전이 | 핵심 기초(수동 지정) |
| 03-007 | 실시간 스케줄링 — Rate Monotonic·EDF (Real-Time Scheduling) | B | 60% | - | [출제:135] |
| 03-014 | 프로세스 스레싱 (Process Thrashing) | B | 60% | - | [출제:131] |
| 03-016 | 워킹 셋·페이지 폴트 (Working Set·Page Fault) | B | 60% | - | [출제:123] |
| 03-019 | 전가상화·반가상화·컨테이너 비교 (Full·Para·Container Virtualization) | B | 60% | - | 핵심 기초(수동 지정) |
| 03-023 | UNIX 커널·쉘·파일시스템 3요소 (UNIX Kernel Shell) | B | 60% | - | [출제:125] |
| 03-024 | 마이크로커널 vs 모놀리식 커널 (Microkernel vs Monolithic) | B | 60% | - | 핵심 기초(수동 지정) |
| 03-031 | 폭포수 모델 vs 애자일 (Waterfall vs Agile) | B | 60% | - | [출제:134] |
| 03-044 | Saga 패턴 — 분산 트랜잭션 (Saga Pattern) | B | 60% | 03-179 마이크로서비스 사가 패턴 vs 2PC | 핵심 기초(수동 지정) |
| 03-046 | SOLID 원칙 (SOLID Principles) | B | 60% | - | [출제:132] · KPC 컴시응 1 |
| 03-049 | DDD 도메인 주도 설계 (Domain-Driven Design) | B | 60% | 03-050 바운디드 컨텍스트 | 핵심 기초(수동 지정) |
| 03-051 | 모놀리식 vs 마이크로서비스 비교 (Monolith vs Microservice) | B | 60% | - | [출제:135] |
| 03-062 | 알파·베타·인수 테스트 (Alpha Beta Acceptance Testing) | B | 60% | - | [출제:129] |
| 03-065 | 소프트웨어 리팩터링·기술부채 (Refactoring Technical Debt) | B | 60% | - | [출제:129] |
| 03-069 | ISO/IEC 25010 소프트웨어 제품 품질 모델 (Software Product Quality Model) | B | 60% | 06-029 소프트웨어 품질 모델 ISO/IEC 25010 · 06-030 품질 특성 | [출제:125] |
| 03-073 | SW 기능점수 FP 측정 (Function Point) | B | 60% | 06-034 기능점수(FP) 기반 규모·생산성 산정 | 핵심 기초(수동 지정) |
| 03-074 | SW 기능점수 간이법·정통법 (FP Estimation Method) | B | 60% | - | [출제:126] |
| 03-077 | 소프트웨어 안전 — GAMAB·ALARP (Software Safety GAMAB ALARP) | B | 60% | - | [출제:128] |
| 03-079 | ISO 29119 테스트 설계 (ISO 29119 Test Design) | B | 60% | - | [출제:128] |
| 03-082 | 플랫폼 엔지니어링 IDP (Platform Engineering IDP) | B | 60% | 08-175 Platform Engineering 플랫폼 엔지니어링 · 08-176 Internal Developer Platform 내부 개발자 플랫폼 · 03-216 플랫폼 엔지니어링 셀프서비스 · 03-083 내부 개발자 플랫폼 골든 패스 | [출제:134] · KPC 컴시응 1 |
| 03-085 | 트랜잭션 ACID (Transaction ACID) | B | 60% | - | [출제:131] · KPC 컴시응 2 |
| 03-087 | MVCC 다중 버전 동시성 제어 (MVCC) | B | 60% | - | KPC 컴시응 1 · 핵심 기초(수동 지정) |
| 03-099 | 샤딩 — 수평 분할 (Sharding) | B | 60% | - | 핵심 기초(수동 지정) |
| 03-101 | 데이터베이스 용량 산정 (DB Capacity Planning) | B | 60% | - | [출제:131] |
| 03-103 | CAP 정리 (CAP Theorem) | B | 60% | - | [출제:131] · KPC 컴시응 1 |
| 03-109 | Neo4j 그래프 DB (Neo4j Graph Database) | B | 60% | - | [출제:122] |
| 03-111 | 데이터 독립성 - 논리·물리 (Data Independence) | B | 60% | - | [출제:128] |
| 03-119 | Apache Kafka 이벤트 스트리밍 (Apache Kafka) | B | 60% | 03-120 Apache Flink 스트림 처리 · 03-121 정확히 한 번 처리 Exactly-Once · 03-122 실시간 스트리밍 플랫폼 · 08-195 Real-time Streaming 실시간 스트리밍 | 핵심 기초(수동 지정) |
| 03-124 | 데이터 웨어하우스 (Data Warehouse) | B | 60% | - | [출제:122] |
| 03-142 | 클라우드 배포 모델 — 퍼블릭·프라이빗·하이브리드·멀티 (Cloud Deployment Models) | B | 60% | - | [출제:131] |
| 03-164 | SRE 사이트 신뢰성 공학 (Site Reliability Engineering) | B | 60% | 08-172 SRE 사이트 신뢰성 공학 · 03-214 SRE 온콜 관리·인시던트 대응 | 핵심 기초(수동 지정) |
| 03-175 | 이벤트 기반 아키텍처 (Event-Driven Architecture) | B | 60% | - | 핵심 기초(수동 지정) |
| 03-182 | IaC 인프라스트럭처 코드 (Infrastructure as Code) | B | 60% | - | 핵심 기초(수동 지정) |
| 03-209 | RPA 로보틱 프로세스 자동화 (Robotic Process Automation) | B | 60% | - | [출제:131] |
| 03-230 | ISO/IEC 20547 빅데이터 참조 아키텍처 (Big Data Reference Architecture) | B | 60% | - | [출제:120] |
| 03-231 | 원격 프로시저 호출 (Remote Procedure Call) | B | 60% | - | [출제:120] |
| 03-232 | 인메모리 데이터 그리드 (In-Memory Data Grid) | B | 60% | - | [출제:122] |
| 03-233 | 동적 연결 라이브러리 (Dynamic Linking Library) | B | 60% | - | [출제:123] |
| 03-235 | 이중 모드 구조 — 커널모드·사용자모드 (Dual Mode Operation) | B | 60% | - | [출제:125] |
| 03-236 | 리먼의 소프트웨어 진화 법칙 (Lehman's Laws of Software Evolution) | B | 60% | - | [출제:129] |
| 03-237 | 데이터베이스 트랜잭션 회복 기법 — REDO·UNDO·체크포인트 (Database Recovery Techniques) | B | 60% | - | [출제:135] |
| 03-061 | 뮤테이션 테스트 (Mutation Testing) | B | 55% | - | 정보관리[133] |
| 03-102 | NoSQL 유형 — 문서·키값·컬럼·그래프 (NoSQL Types) | B | 55% | 03-106 MongoDB 도큐먼트 DB · 03-107 Redis 인메모리 DB · 03-108 Cassandra 컬럼 패밀리 DB | 정보관리[133] · KPC 컴시응 1 |
| 03-104 | BASE vs ACID (BASE vs ACID) | B | 50% | - | KPC 컴시응 2 |
| 03-150 | Docker 컨테이너 (Docker Container) | B | 50% | - | KPC 컴시응 3 |
| 03-038 | 소프트웨어 아키텍처 패턴 — MVC·MSA·이벤트드리븐 (Architecture Patterns) | B | 30% | - | KPC 컴시응 3 |
| 03-008 | 스레드 스케줄링·스레드 풀 (Thread Scheduling·Thread Pool) | C | 50% | - | - |
| 03-020 | 파일 시스템 — FAT·NTFS·ext4·APFS (File System) | C | 50% | 03-021 파일 시스템 저널링 | - |
| 03-026 | 비동기 I/O·이벤트 루프 (Async I/O Event Loop) | C | 50% | - | - |
| 03-030 | 소프트웨어 개발 생명주기 SDLC (Software Development Lifecycle) | C | 50% | - | - |
| 03-032 | 애자일 스크럼 (Agile Scrum) | C | 50% | - | - |
| 03-036 | 요구사항 분석·명세 (Requirements Analysis) | C | 50% | - | - |
| 03-040 | API 게이트웨이 (API Gateway) | C | 50% | - | - |
| 03-041 | 서킷 브레이커 패턴 (Circuit Breaker Pattern) | C | 50% | - | - |
| 03-042 | 서비스 메시 — Istio·Envoy (Service Mesh) | C | 50% | 03-160 서비스 메시 Istio · 08-162 서비스 메시 · 08-163 이스티오 · 08-164 사이드카 프록시 · 03-218 사이드카 패턴 | - |
| 03-043 | 이벤트 소싱·CQRS (Event Sourcing CQRS) | C | 50% | - | - |
| 03-045 | 12 팩터 앱 (12 Factor App) | C | 50% | - | - |
| 03-048 | 헥사고날 아키텍처 — 포트·어댑터 (Hexagonal Architecture) | C | 50% | - | - |
| 03-052 | 형상 관리 — Git·브랜치 전략 (Configuration Management Git) | C | 50% | - | - |
| 03-055 | GitOps | C | 50% | - | - |
| 03-059 | 테스트 주도 개발 TDD (Test-Driven Development) | C | 50% | - | - |
| 03-064 | 피처 플래그 (Feature Flag) | C | 50% | 03-220 피처 토글·실험 플랫폼 | - |
| 03-081 | AI 코드 생성 — GitHub Copilot (AI Code Generation) | C | 50% | - | - |
| 03-090 | 반정규화·성능 트레이드오프 (Denormalization) | C | 50% | - | - |
| 03-095 | 실행 계획·쿼리 최적화 (Query Execution Plan Optimization) | C | 50% | - | - |
| 03-096 | 조인 알고리즘 — NLJ·Hash Join·Merge Join (Join Algorithms) | C | 50% | - | - |
| 03-098 | 파티셔닝 — 범위·해시·리스트 (Partitioning) | C | 50% | - | - |
| 03-100 | 데이터베이스 복제 — 마스터-슬레이브·멀티마스터 (Database Replication) | C | 50% | - | - |
| 03-105 | CRDT 충돌 없는 복제 데이터 (Conflict-free Replicated Data Type) | C | 50% | - | - |
| 03-112 | 3단계 스키마 - 외부·개념·내부 (Three-Level Schema) | C | 50% | - | - |
| 03-115 | NewSQL — CockroachDB·Spanner (NewSQL) | C | 50% | - | - |
| 03-118 | 람다 아키텍처 (Lambda Architecture) | C | 50% | - | - |
| 03-123 | 변경 데이터 캡처 CDC (Change Data Capture) | C | 50% | - | - |
| 03-131 | 데이터 메시 (Data Mesh) | C | 50% | 08-193 Data Mesh 데이터 메시 | - |
| 03-132 | 데이터 패브릭 (Data Fabric) | C | 50% | 08-194 Data Fabric 데이터 패브릭 | - |
| 03-135 | 데이터 거버넌스 (Data Governance) | C | 50% | 03-133 데이터 카탈로그 · 03-134 데이터 계보 Data Lineage | - |
| 03-136 | 마스터 데이터 관리 MDM (Master Data Management) | C | 50% | - | KPC 컴시응 1 |
| 03-137 | 데이터 품질 관리 — 완전성·정확성·일관성 (Data Quality Management) | C | 50% | - | KPC 컴시응 1 |
| 03-138 | ETL·ELT 파이프라인 (ETL ELT Pipeline) | C | 50% | 03-139 데이터 파이프라인 오케스트레이션 — Airflow | KPC 컴시응 1 |
| 03-144 | 하이브리드 클라우드 (Hybrid Cloud) | C | 50% | 08-181 Hybrid Cloud 하이브리드 클라우드 | - |
| 03-146 | 클라우드 마이그레이션 6R (Cloud Migration 6R) | C | 50% | 08-179 Cloud Migration 6R | - |
| 03-147 | FinOps 클라우드 비용 최적화 (FinOps) | C | 50% | 08-178 FinOps 클라우드 비용관리 · 03-148 예약 인스턴스·스팟 인스턴스 | - |
| 03-158 | 컨테이너 보안 — Seccomp·AppArmor·OPA (Container Security) | C | 50% | - | - |
| 03-167 | AIOps (Artificial Intelligence for IT Operations) | C | 50% | 08-130 AIOps | - |
| 03-168 | 소버린 클라우드 (Sovereign Cloud) | C | 50% | 08-182 Sovereign Cloud 소버린 클라우드 | - |
| 03-169 | 클라우드 회귀 (Cloud Repatriation) | C | 50% | - | - |
| 03-171 | RESTful API 설계 원칙 (RESTful API Design) | C | 50% | - | - |
| 03-172 | GraphQL (GraphQL) | C | 50% | - | - |
| 03-173 | gRPC (gRPC) | C | 50% | - | - |
| 03-176 | 분산 시스템 일관성 모델 (Distributed System Consistency) | C | 50% | - | - |
| 03-180 | 캐싱 전략 — Cache-Aside·Write-Through (Caching Strategy) | C | 50% | - | - |
| 03-195 | 소프트웨어 그린 엔지니어링 SCI 지수 (Green Software SCI) | C | 50% | 08-196 Green Software 그린 소프트웨어 | - |
| 03-201 | 멱등성 설계 (Idempotency Design) | C | 50% | - | - |
| 03-203 | LLMOps (LLMOps) | C | 50% | 08-129 LLMOps | - |
| 03-207 | AI 기반 테스트 자동화 (AI Test Automation) | C | 50% | - | - |
| 03-212 | 소프트웨어 리팩터링 패턴 (Refactoring Patterns) | C | 50% | - | - |
| 03-213 | 기술부채 측정·관리 (Technical Debt Measurement) | C | 50% | 03-066 소프트웨어 기술부채 사분면 | - |
| 03-088 | 락 관리 — 2단계 잠금 프로토콜 (2PL Two-Phase Locking) | C | 30% | - | - |
| 03-110 | 시계열 데이터베이스 (Time Series Database) | C | 30% | - | - |
| 03-116 | 빅데이터 분산 처리 — Hadoop·MapReduce·HDFS (Hadoop MapReduce) | C | 30% | 03-117 Apache Spark | - |

## 다른 과목 토픽으로 넘긴 키워드

같은 주제가 다른 과목에도 등록돼 있어 그쪽 토픽에 합쳤다. 이 과목에는 노트를 두지 않는다.

| 번호 | 키워드 | 넘긴 토픽 |
|---|---|---|
| 03-029 | NUMA 인지 스케줄링 (NUMA-aware Scheduling) | 02-021 NUMA 비균등 메모리 접근 (Non-Uniform Memory Access) |
| 03-057 | DevSecOps | 05-144 DevSecOps 보안 시프트 레프트 (DevSecOps Shift-Left) |
| 03-067 | 정적 분석 SAST (Static Application Security Testing) | 05-145 SAST·DAST·IAST·RASP |
| 03-068 | 동적 애플리케이션 보안 테스트 DAST (Dynamic Application Security Testing) | 05-145 SAST·DAST·IAST·RASP |
| 03-075 | 소프트웨어 대가산정 (SW Cost Estimation) | 07-018 소프트웨어 대가 산정 (SW Cost Estimation) |
| 03-145 | 클라우드 공유 책임 모델 (Shared Responsibility Model) | 05-071 클라우드 보안 공유 책임 모델 (Cloud Shared Responsibility) |
| 03-174 | OAuth 2.0·OIDC (OAuth 2.0 OIDC) | 05-057 OAuth 2.0·OIDC (OAuth 2.0 OIDC) |
| 03-181 | CDN 콘텐츠 전송 네트워크 (CDN Content Delivery Network) | 04-107 글로벌 CDN 아키텍처 (Global CDN Architecture) |
| 03-185 | 소프트웨어 공급망 보안 | 05-076 소프트웨어 공급망 보안 (Supply Chain Security) |
| 03-186 | TTA 소프트웨어 품질 시험 | 06-031 소프트웨어 품질 평가 검증 (TTA & GS 인증) |
| 03-187 | ISMP 정보화 마스터플랜 (ISMP) | 07-003 ISMP (Information System Master Plan) |
| 03-188 | ISP 정보화 전략 계획 (ISP Information Strategy Planning) | 07-002 ISP (Information Strategy Plan) |
| 03-189 | EA 전사적 아키텍처 (Enterprise Architecture) | 07-001 EA와 TOGAF (Enterprise Architecture & TOGAF) |
| 03-190 | 범정부 EA 참조 모형 TRM·DRM (Government EA TRM DRM) | 07-001 EA와 TOGAF (Enterprise Architecture & TOGAF) |
| 03-192 | 소프트웨어 사업 영향 평가 (SW Business Impact Assessment) | 07-017 소프트웨어 사업 영향 평가 (SW Business Impact Assessment) |
| 03-193 | SW 조달 — 상용SW 직접구매 (SW Direct Purchase) | 07-016 상용SW 직접 구매 (Commercial SW Direct Purchase) |
| 03-194 | 디지털 접근성 — WCAG 2.1 (Digital Accessibility WCAG) | 07-013 디지털 접근성과 WCAG (Digital Accessibility & WCAG) |
| 03-196 | 사이버 레질리언스 — 예방·감지·대응·복구 (Cyber Resilience) | 05-119 사이버 레질리언스 (Cyber Resilience) |
| 03-197 | 재해 복구 RTO·RPO (Disaster Recovery RTO RPO) | 06-020 RTO·RPO 정의·측정 (RTO RPO) |
| 03-198 | 고가용성 설계 — Active-Active·Active-Standby (High Availability Design) | 06-017 고가용성 설계 - Active-Active·Active-Standby (High Availability Architecture) |
| 03-199 | 단일 장애점 SPOF 제거 (SPOF Elimination) | 06-017 고가용성 설계 - Active-Active·Active-Standby (High Availability Architecture) |
| 03-200 | 자동 페일오버 (Auto Failover) | 06-017 고가용성 설계 - Active-Active·Active-Standby (High Availability Architecture) |
| 03-208 | 온디바이스 AI 모델 배포 — LiteRT·ONNX (On-Device Model Deployment) | 08-050 On-Device AI (온디바이스 AI) |
| 03-222 | 성능 테스트 지표 — TPS·응답시간·동시 사용자 (Performance Test Metrics) | 06-007 TPS 계산 - 동시 사용자·응답 시간 공식 (TPS Calculation) |
| 03-223 | APM 애플리케이션 성능 관리 (Application Performance Management) | 06-008 APM 애플리케이션 성능 관리 (Application Performance Management) |
| 03-224 | 소프트웨어 기술성 평가 (SW Technology Evaluation) | 07-019 소프트웨어 기술성 평가 (SW Technology Evaluation) |
| 03-225 | BMT 벤치마크 테스트 (Benchmark Test BMT) | 06-010 BMT 벤치마크 테스트 방법론 (BMT Methodology) |
| 03-226 | 지능정보화 기본법 (Framework Act on Intelligent Informatization) | 07-021 지능정보화 기본법 (Intelligent Informatization Basic Act) |
| 03-227 | 소프트웨어 진흥법 (Software Promotion Act) | 07-015 소프트웨어 진흥법 |
| 03-228 | AI 소프트웨어 감리 점검 항목 (AI Software Audit) | 06-044 감리 점검 항목 (Audit Checklist) |
| 03-229 | 디지털 서비스 성숙도 모형 (Digital Service Maturity Model) | 06-051 디지털 서비스 성숙도 모형 평가 (Digital Service Maturity Evaluation) |
