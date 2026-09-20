# 05 시스템 보안 토픽

> 130개. 노트 폴더는 `src/content/docs/notes/cspe/05-security/`, 파일명은 `{3자리 번호}_{영문 snake_case}.md`다. 표기는 [README](../README.md)를 본다.

| 번호 | 토픽 | 등급 | 중요도 | 흡수한 하위 키워드 | 근거 |
|---|---|:---:|---:|---|---|
| 05-063 | 제로 트러스트 아키텍처 (Zero Trust Architecture) | A | 90% | 08-185 Zero Trust Architecture 제로트러스트 아키텍처 · 05-064 ZTNA 제로 트러스트 네트워크 접근 · 05-065 마이크로 세그멘테이션 | [출제:122,134,135,140] · 정보관리[135,136] · KPC 컴시응 4 |
| 05-103 | 정보보호 관리체계 ISMS-P (ISMS-P) | A | 90% | - | [출제:126,134,138] · 정보관리[138] · KPC 컴시응 3 |
| 05-159 | 제로트러스트 가이드라인 2.0 | A | 87% | - | KPC 컴시응 1 · 시사·트렌드 · 정보관리 목록 06-026에서 가져옴 |
| 05-098 | 개인정보 비식별 처리·가명화·익명화 (De-identification) | A | 85% | - | [출제:122,131,140] |
| 05-100 | 개인정보보호 강화기술 PET | A | 85% | - | [출제:134,138] · 정보관리[134,138] · KPC 컴시응 2 |
| 05-114 | 디지털 포렌식 — 증거 수집·체인 오브 커스터디 (Digital Forensics) | A | 85% | 04-097 네트워크 포렌식 증거 수집 · 05-115 모바일 포렌식 | [출제:128,140] · 정보관리[140] · KPC 컴시응 3 |
| 05-160 | AI 보안 안내서 (과기정통부·KISA) | A | 85% | - | 시사·트렌드 · 정보관리 목록 06-034에서 가져옴 |
| 05-161 | AI 보안 플랫폼 (AI Security Platform) | A | 85% | - | 시사·트렌드 · 정보관리 목록 06-035에서 가져옴 |
| 05-162 | KT 불법 펨토셀 무단 소액결제 | A | 85% | - | 시사·트렌드 · 정보관리 목록 06-038에서 가져옴 |
| 05-163 | SKT 유심 정보 유출 사고 | A | 85% | - | 시사·트렌드 · 정보관리 목록 06-040에서 가져옴 |
| 05-164 | 범부처 정보보호 종합대책 | A | 85% | - | 시사·트렌드 · 정보관리 목록 06-042에서 가져옴 |
| 05-165 | 비인간 신원(NHI, Non-Human Identities) | A | 85% | - | 정보관리[140] · 시사·트렌드 · 정보관리 목록 06-043에서 가져옴 |
| 05-166 | 온나라시스템·GPKI 인증서 유출 | A | 85% | - | 시사·트렌드 · 정보관리 목록 06-046에서 가져옴 |
| 05-023 | IDS·IPS 탐지 vs 차단 (IDS IPS) | A | 80% | 04-021 IDS·IPS | [출제:134,137] · KPC 컴시응 3 |
| 05-051 | 시큐어 코딩 가이드 (Secure Coding Guide) | A | 80% | 05-052 입력값 검증·파라미터 바인딩 | [출제:126,140] · KPC 컴시응 4 |
| 05-152 | 샌드박스 — 격리·동적 분석 (Sandbox) | A | 80% | - | [출제:126,137] |
| 05-088 | OWASP LLM Top 10 (OWASP LLM Top 10) | A | 75% | 08-125 OWASP LLM Top 10 · 08-126 LLM10 Unbounded Consumption | [출제:138] · 정보관리[136] · KPC 컴시응 1 |
| 05-156 | 국가 망 보안체계 N2SF (National Network Security Framework) | A | 75% | - | [출제:140] · 정보관리[137] · KPC 컴시응 1 |
| 05-001 | 대칭 암호화 (Symmetric Encryption) | A | 70% | 05-002 비대칭 암호화 · 05-003 하이브리드 암호 | 핵심 기초(수동 지정) |
| 05-007 | PKI 공개키 기반구조 (Public Key Infrastructure) | A | 70% | 05-008 X.509 인증서 · 05-009 CA 인증 기관·인증서 발급 절차 · 05-010 CRL·OCSP 인증서 폐지 | 핵심 기초(수동 지정) |
| 05-021 | 방화벽 - 패킷 필터·상태기반·NGFW (Firewall) | A | 70% | 04-020 방화벽 — 패킷 필터·상태기반·NGFW · 05-022 차세대 방화벽 NGFW vs WAF vs CASB 비교 | [출제:137] |
| 05-026 | 랜섬웨어 공격 분석·대응 (Ransomware) | A | 70% | - | [출제:138] |
| 05-029 | MITRE ATT&CK 프레임워크 (MITRE ATT&CK) | A | 70% | - | 핵심 기초(수동 지정) |
| 05-056 | 패스키 비밀번호 없는 인증 (Passkey Passwordless) | A | 70% | 05-054 MFA 다중 인증 · 05-055 FIDO2·WebAuthn | 핵심 기초(수동 지정) |
| 05-073 | 클라우드 네이티브 애플리케이션 보호 플랫폼 (Cloud-Native Application Protection Platform, CNAPP) | A | 70% | - | [출제:137] |
| 05-075 | 클라우드 CSAP 보안 인증 등급제 (Cloud Security Assurance Program) | A | 70% | 06-048 CSAP 클라우드 보안 인증 평가 · 08-184 CSAP 클라우드 보안인증 | [출제:129,134] · KPC 컴시응 1 |
| 05-078 | AI 보안 위협 전체 구조 (AI Security Threat Landscape) | A | 70% | - | [출제:137] |
| 05-087 | 모델 DoS (Model Denial of Service) | A | 70% | 08-124 모델 서비스 거부 | [출제:138] |
| 05-096 | 전송 요구권·마이데이터 (Data Portability MyData) | A | 70% | - | [출제:137] · KPC 컴시응 1 |
| 05-133 | 스마트팩토리 OT 보안 (OT Security Smart Factory) | A | 70% | - | [출제:123,126] · KPC 컴시응 4 |
| 05-154 | 보안 운영체제 (Secure OS) | A | 70% | - | [출제:137] |
| 05-155 | ASN.1 인코딩 규칙 — BER·DER·CER (ASN.1 Encoding Rules) | A | 70% | - | [출제:138] |
| 05-014 | QKD 양자 키 분배 (Quantum Key Distribution) | A | 65% | 04-100 QKD 양자 키 분배 · 08-217 QKD 양자키분배 | [출제:126] · 정보관리[135] · KPC 컴시응 1 |
| 05-102 | CBPR 국경 간 개인정보 규칙 (CBPR Cross-Border Privacy Rules) | A | 65% | - | [출제:131] · 정보관리[132] · KPC 컴시응 1 |
| 05-104 | ISMS-P 인증 심사 절차 (ISMS-P Certification) | A | 65% | - | 정보관리[138] · KPC 컴시응 3 |
| 05-153 | 접근통제 모델 — MAC·DAC (Mandatory and Discretionary Access Control) | A | 65% | 05-059 RBAC 역할 기반 접근 제어 · 05-060 ABAC 속성 기반 접근 제어 | [출제:135] · 정보관리[133] · KPC 컴시응 1 |
| 05-157 | TCP 래퍼 — 호스트 기반 서비스 접근통제 (TCP Wrapper) | A | 65% | - | [출제:125] · 정보관리[133,137] |
| 05-025 | DDoS 공격·대응 - SYN Flood·반사 증폭 (DDoS Attack) | A | 60% | 04-087 DDoS 공격 기법·대응 - SYN Flood·증폭 | [출제:125] · KPC 컴시응 5 |
| 05-132 | IoT 디바이스 보안 — AIoT (AIoT Security) | A | 60% | - | [출제:132] · KPC 컴시응 5 |
| 05-167 | AI 보안 | B | 84% | - | 정보관리[140] · 시사·트렌드 · 정보관리 목록 06-049에서 가져옴 |
| 05-168 | CrowdStrike 대규모 장애 | B | 75% | - | 시사·트렌드 · 정보관리 목록 06-086에서 가져옴 |
| 05-169 | Salt Typhoon / Volt Typhoon (LotL) | B | 75% | - | 시사·트렌드 · 정보관리 목록 06-092에서 가져옴 |
| 05-170 | 국가사이버안보전략 | B | 75% | - | 시사·트렌드 · 정보관리 목록 06-099에서 가져옴 |
| 05-171 | 섀도우 AI (Shadow AI) | B | 75% | - | 시사·트렌드 · 정보관리 목록 06-105에서 가져옴 |
| 05-172 | 정보보호 공시 전 상장사 의무화 | B | 75% | - | 시사·트렌드 · 정보관리 목록 06-109에서 가져옴 |
| 05-173 | 허위정보 보안 (Disinformation Security) | B | 75% | - | 시사·트렌드 · 정보관리 목록 06-110에서 가져옴 |
| 05-004 | 해시 알고리즘 (Hash Algorithm) | B | 65% | - | 정보관리[138] |
| 05-011 | TLS 1.3 핸드셰이크 (TLS 1.3 Handshake) | B | 65% | - | 정보관리[136] |
| 05-012 | 양자내성암호 PQC (Post-Quantum Cryptography) | B | 65% | 07-039 NIST PQC 표준화 — FIPS 203/204/205 · 08-216 Post-Quantum Cryptography 양자내성암호 | 정보관리[135] |
| 05-037 | SIEM vs SOAR 비교 (SIEM vs SOAR) | B | 65% | 04-095 SIEM vs SOAR 비교 · 05-035 SIEM - 보안 이벤트 집계·분석 · 05-036 SOAR - 보안 자동화·대응 · 05-121 보안 오케스트레이션 플레이북 · 04-094 SOAR 보안 오케스트레이션·자동화·대응 | 정보관리[135] |
| 05-040 | CTEM (Continuous Threat Exposure Management) | B | 65% | - | 정보관리[139] |
| 05-045 | OWASP Top 10 (OWASP Top 10) | B | 65% | - | 정보관리[136] · KPC 컴시응 1 |
| 05-076 | 소프트웨어 공급망 보안 (Supply Chain Security) | B | 65% | 03-185 소프트웨어 공급망 보안 · 08-188 Software Supply Chain Security 소프트웨어 공급망 보안 | 정보관리[136] |
| 05-079 | 프롬프트 인젝션 (Prompt Injection) | B | 65% | 05-080 간접 프롬프트 인젝션 · 08-116 프롬프트 인젝션 · 08-117 간접 프롬프트 인젝션 · 05-081 탈옥 Jailbreak 공격 · 08-118 탈옥 공격 | 정보관리[138] |
| 05-093 | AI 공급망 보안 (AI Supply Chain Security) | B | 65% | - | 정보관리[136] |
| 05-125 | 임베디드 시스템 보안 취약점 (Embedded Security Vulnerabilities) | B | 65% | 05-126 펌웨어 보안 — 하드코딩 자격증명 · 05-131 JTAG 디버그 포트 보안 · 02-069 펌웨어 보안 취약점 | 정보관리[136,137] |
| 05-144 | DevSecOps 보안 시프트 레프트 (DevSecOps Shift-Left) | B | 65% | 03-057 DevSecOps · 08-177 DevSecOps | 정보관리[135] |
| 05-158 | 아티팩트(Artifact) | B | 65% | - | 정보관리[137,140] · 정보관리 목록 06-008에서 가져옴 |
| 05-174 | 암호문 공격(암호 공격 모델 COA·KPA·CPA·CCA) | B | 65% | - | 정보관리[137] · 정보관리 목록 06-107에서 가져옴 |
| 05-175 | CC(공통평가기준)·정보보호제품 신속확인제 | B | 65% | - | 정보관리[136] · 정보관리 목록 06-037에서 가져옴 |
| 05-176 | 정보보호 컴플라이언스 | B | 65% | - | 정보관리[140] · 정보관리 목록 06-067에서 가져옴 |
| 05-005 | 디피-헬만 키 교환 (Diffie-Hellman Key Exchange) | B | 60% | - | [출제:128] |
| 05-013 | PQC 전환 로드맵·하이브리드 방식 (PQC Migration Hybrid) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-016 | 영지식 증명 ZKP (Zero-Knowledge Proof) | B | 60% | 08-222 영지식 증명 | [출제:132] |
| 05-019 | 기밀 컴퓨팅 (Confidential Computing) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-024 | 네트워크 스푸핑 - ARP·IP·DNS (Network Spoofing) | B | 60% | 04-086 네트워크 스푸핑 - ARP·IP·DNS | [출제:134] |
| 05-028 | 사이버 킬체인 (Cyber Kill Chain) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-042 | 제로데이 취약점·대응 체계 (Zero-Day Vulnerability) | B | 60% | - | [출제:134] |
| 05-048 | CSRF (Cross-Site Request Forgery) | B | 60% | - | [출제:131] |
| 05-049 | 버퍼 오버플로우 — 카나리·DEP·ASLR (Buffer Overflow Canary DEP ASLR) | B | 60% | - | [출제:123] |
| 05-050 | 쉘코드·ROP 공격 (Shellcode ROP) | B | 60% | - | [출제:125] |
| 05-069 | CAPTCHA·reCAPTCHA (CAPTCHA) | B | 60% | - | [출제:128] |
| 05-084 | 데이터 오염 공격 (Data Poisoning) | B | 60% | 08-120 모델 역전 · 08-119 모델 추출 · 08-121 데이터 오염 · 05-082 모델 역전 공격 · 05-083 모델 추출 공격 · 05-085 백도어 공격 · 08-122 백도어 공격 | 핵심 기초(수동 지정) |
| 05-086 | 적대적 예제 공격 (Adversarial Example) | B | 60% | 08-123 적대적 예제 | [출제:131] |
| 05-090 | 에이전트 보안 — 권한 통제·가드레일 (Agent Security) | B | 60% | 08-017 Agent Authorization & Control · 08-018 Agent Audit Log · 08-019 Human-in-the-Loop Agent · 08-020 Agent Sandbox · 08-022 Agent Guardrail · 08-023 Agent Observability | 핵심 기초(수동 지정) |
| 05-092 | 딥페이크 탐지 (Deepfake Detection) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-097 | 개인정보 영향평가 PIA (Privacy Impact Assessment) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-099 | 마이데이터 서비스 보안 | B | 60% | - | [출제:126] · KPC 컴시응 1 |
| 05-101 | ISO 29100·ISO 27701 (ISO 29100 ISO 27701) | B | 60% | - | [출제:126] |
| 05-112 | 정보보호 거버넌스 (Information Security Governance) | B | 60% | - | [출제:120] |
| 05-116 | 디스크 이미징·해시 무결성 (Disk Imaging Hash Integrity) | B | 60% | - | [출제:129] |
| 05-117 | 국가정보원 보안성 검토 (NIS Security Review) | B | 60% | - | [출제:131] |
| 05-118 | 망분리 — CC 인증·보안적합성 (Network Separation CC) | B | 60% | 05-140 망분리·망연계 솔루션 | 핵심 기초(수동 지정) |
| 05-130 | 사이드채널 공격 (Side-Channel Attack) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-138 | 만리장성 보안 모델 (Brewer-Nash Model) | B | 60% | - | [출제:132] |
| 05-142 | 데이터 보안 — DRM·DLP 비교 (DRM DLP) | B | 60% | - | [출제:128] |
| 05-143 | 보안 정보 공유 플랫폼 — ISAC (ISAC) | B | 60% | - | [출제:129] |
| 05-145 | SAST·DAST·IAST·RASP | B | 60% | 03-067 정적 분석 SAST · 03-068 동적 애플리케이션 보안 테스트 DAST | 핵심 기초(수동 지정) |
| 05-146 | 위협 모델링 — STRIDE·DREAD (Threat Modeling STRIDE) | B | 60% | - | 핵심 기초(수동 지정) |
| 05-148 | 래터럴 무브먼트 (Lateral Movement) | B | 60% | - | [출제:120] |
| 05-149 | 정보보안 3대 목표 — 기밀성·무결성·가용성 (CIA Triad) | B | 60% | - | [출제:122] |
| 05-150 | 드론 서비스 보안위협 (Drone Security Threats) | B | 60% | - | [출제:123] |
| 05-151 | OECD 프라이버시 8원칙 (OECD Privacy Guidelines 8 Principles) | B | 60% | - | [출제:123] |
| 05-015 | 동형 암호 (Homomorphic Encryption) | B | 55% | 08-114 Homomorphic Encryption 동형암호 | 정보관리[133] |
| 05-017 | 안전한 다자간 연산 MPC (Secure Multi-Party Computation) | B | 55% | - | 정보관리[133] |
| 05-046 | SQL 인젝션 (SQL Injection) | B | 55% | - | 정보관리[134] · KPC 컴시응 1 |
| 05-110 | BCP 업무 연속성 계획 (Business Continuity Plan) | B | 55% | - | 정보관리[133] · KPC 컴시응 2 |
| 05-006 | 전자 서명 (Digital Signature) | B | 50% | - | KPC 컴시응 2 |
| 05-018 | 차등 프라이버시 (Differential Privacy) | C | 50% | 08-113 Differential Privacy 차등 개인정보보호 | - |
| 05-020 | 키 관리 - HSM·KMS (Key Management HSM KMS) | C | 50% | - | - |
| 05-027 | APT 고급 지속 위협 (Advanced Persistent Threat) | C | 50% | - | - |
| 05-030 | 위협 헌팅 (Threat Hunting) | C | 50% | - | - |
| 05-031 | 사이버 위협 인텔리전스 CTI (Cyber Threat Intelligence) | C | 50% | 05-032 STIX·TAXII 위협 공유 · 05-033 MISP 위협 공유 플랫폼 · 05-122 인텔리전스 기반 CTI 자동화 · 04-096 위협 인텔리전스 - STIX·TAXII | - |
| 05-034 | SOC 보안 운영 센터 (Security Operations Center) | C | 50% | - | - |
| 05-038 | UEBA 사용자·엔티티 행동 분석 (UEBA) | C | 50% | - | - |
| 05-039 | XDR 확장 탐지·대응 (XDR Extended Detection Response) | C | 50% | - | - |
| 05-041 | 모의 침투 테스트 (Penetration Testing, 펜테스트) | C | 50% | - | - |
| 05-043 | 패치 관리·가상 패치 (Patch Management Virtual Patching) | C | 50% | - | - |
| 05-044 | 보안 구성 관리 (Security Configuration Management) | C | 50% | - | - |
| 05-057 | OAuth 2.0·OIDC (OAuth 2.0 OIDC) | C | 50% | 03-174 OAuth 2.0·OIDC | - |
| 05-061 | IAM 신원·접근 관리 (Identity and Access Management) | C | 50% | - | - |
| 05-062 | PAM 특권 접근 관리 (Privileged Access Management) | C | 50% | - | - |
| 05-066 | 디지털 신원 — DID·SSI (Decentralized Identity DID SSI) | C | 50% | 05-068 W3C DID 표준 · 08-220 DID 분산신원 | KPC 컴시응 1 |
| 05-067 | 검증가능 자격증명 VC (Verifiable Credential) | C | 50% | 08-221 검증가능 자격증명 | - |
| 05-070 | 생체 인식 — 지문·얼굴·홍채 (Biometric Authentication) | C | 50% | - | - |
| 05-071 | 클라우드 보안 공유 책임 모델 (Cloud Shared Responsibility) | C | 50% | 03-145 클라우드 공유 책임 모델 | - |
| 05-072 | CASB 클라우드 접근 보안 브로커 (Cloud Access Security Broker) | C | 50% | 04-092 CASB 클라우드 접근 보안 브로커 | - |
| 05-074 | DSPM 데이터 보안 형상 관리 (Data Security Posture Management) | C | 50% | - | - |
| 05-077 | 비밀 관리 - Vault·AWS Secrets (Secrets Management) | C | 50% | - | - |
| 05-089 | AI 레드팀 (AI Red Teaming) | C | 50% | 08-115 AI 레드팀 | - |
| 05-091 | 인공지능 워터마킹 (Artificial Intelligence Watermarking) | C | 50% | 08-127 C2PA 콘텐츠 출처 표준 | - |
| 05-108 | 정보 보호 위험 평가 — 자산·위협·취약점 (Information Security Risk Assessment) | C | 50% | 05-109 위험 처리 전략 — 수용·회피·전가·감소 | - |
| 05-113 | 내부자 위협 관리 (Insider Threat Management) | C | 50% | - | - |
| 05-119 | 사이버 레질리언스 (Cyber Resilience) | C | 50% | 03-196 사이버 레질리언스 — 예방·감지·대응·복구 | - |
| 05-120 | 취약점 우선순위 관리 — EPSS·CVSS (Vulnerability Prioritization EPSS CVSS) | C | 50% | - | - |
| 05-127 | Secure Boot 보안 부팅 (Secure Boot) | C | 50% | 02-064 Arm TrustZone 보안 확장 · 02-068 보안 부팅 · 05-128 ARM TrustZone · 05-129 PUF 물리적 복제 불가 함수 · 02-070 물리적 복제 불가 함수 | - |
| 05-134 | 차량 사이버 보안 — V2X 위협 (Vehicle Cybersecurity V2X) | C | 50% | 05-136 PKI 차량 인증 | - |
| 05-137 | 보안 설계 원칙 — 페일 세이프·최소 노출 (Security Design Principles) | C | 50% | - | - |
| 05-047 | XSS (Cross-Site Scripting) | C | 30% | - | - |
| 05-058 | SAML 2.0 (SAML 2.0) | C | 30% | - | - |

## 다른 과목 토픽으로 넘긴 키워드

같은 주제가 다른 과목에도 등록돼 있어 그쪽 토픽에 합쳤다. 이 과목에는 노트를 두지 않는다.

| 번호 | 키워드 | 넘긴 토픽 |
|---|---|---|
| 05-094 | 개인정보보호법 — 수집·이용·제공·파기 (Personal Data Protection Act) | 07-022 개인정보보호법 (Personal Information Protection Act) |
| 05-095 | 개인정보보호법 2023 개정 — 마이데이터·과징금 (PIPA 2023 Amendment) | 07-022 개인정보보호법 (Personal Information Protection Act) |
| 05-105 | ISO/IEC 27001 정보보안 경영 시스템 (ISO 27001) | 07-029 ISO/IEC 27001 정보보안 경영시스템 (ISO 27001) |
| 05-106 | ISO/IEC 27001:2022 주요 개정 (ISO 27001 2022) | 07-029 ISO/IEC 27001 정보보안 경영시스템 (ISO 27001) |
| 05-107 | ISO/IEC 27701 개인정보 경영 시스템 (ISO 27701) | 07-029 ISO/IEC 27001 정보보안 경영시스템 (ISO 27001) |
| 05-111 | NIST Cybersecurity Framework (NIST CSF) | 07-037 NIST Cybersecurity Framework 2.0 (NIST CSF 2.0) |
| 05-124 | EU DORA (디지털 운영 복원력 법) | 07-034 EU DORA 금융 디지털 운영 복원력 (EU DORA) |
| 05-135 | ISO/PAS 8800 AI 안전 (ISO PAS 8800) | 07-044 ISO/PAS 8800 자율주행 AI 안전 (ISO PAS 8800) |
| 05-141 | 보안 접근 서비스 경계(Secure Access Service Edge, SASE) 아키텍처 | 04-090 SASE - SD-WAN·CASB·SWG·ZTNA (SASE) |
