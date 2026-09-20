---
title: "CI/CD(Continuous Integration/Continuous Delivery)"
tags:
  - "notes-software-engineering"
---

| 세부 토픽 키워드 | 핵심 다이어그램 / 개념 매핑 |
|---|---|
| 지속적 통합 (Continuous Integration) | 코드 커밋 → 자동 빌드 → 단위/통합 테스트 자동화 파이프라인 |
| 지속적 제공 vs 지속적 배포 (CD) | 프로덕션 수동 승인 배포(Delivery) vs 100% 무인 자동 릴리스(Deployment) |
| GitOps 풀(Pull) 기반 배포 아키텍처 | Git 단일 진실 공급원(SSOT) ↔ 쿠버네티스 인클러스터 에이전트(ArgoCD) |
| 파이프라인 DevSecOps 통합 | Shift-Left 보안 게이트(시크릿 스캔, SAST, DAST, SCA, Cosign 서명) |

## 답안 골격 (세로 피시본)

```text
[CI/CD 파이프라인] ◀━━ 머리: Ⅶ 내 의견 (GitOps 풀 기반 선언적 배포와 Shift-Left DevSecOps 품질 게이트 내재화)
 ┃
 ┣━ Ⅰ 개요 ───── 장기간 격리 개발로 인한 '통합 지옥(Integration Hell)' ↔ 빈번한 자동 빌드·테스트 및 무인 릴리스
 ┣━ Ⅱ 원칙 ───── 일 1회 이상 메인 통합(Trunk-Based) · 자동화 테스트 피드백 · 배포 파이프라인 가시화 · 멱등성 보장
 ┣━ Ⅲ 구조 ───── 형상관리(Git) ➔ CI 엔진(GitHub Actions, Jenkins) ➔ 저장소(Harbor) ➔ CD 엔진(ArgoCD, Spinnaker)
 ┣━ Ⅳ 단계별흐름 ─ Plan/Code(시크릿 스캔) → Build(SAST/단위테스트) → Package(SCA/서명) → Deploy(GitOps/Canary)
 ┣━ Ⅴ 비교 ───── 지속적 제공(Delivery, 수동 승인) vs 지속적 배포(Deployment, 완전 무인) vs DevOps
 ┗━ Ⅵ 실무 ───── 배포 파이프라인 자격증명 노출 · 런타임 결함 전파 · 취약점 유입 차단(보안 가드레일)
```

- 필수 키워드: 지속적 통합(CI), 지속적 제공(Continuous Delivery), 지속적 배포(Continuous Deployment), GitOps(ArgoCD), 트렁크 기반 개발, DevSecOps(SAST/DAST/SCA), 무중단 배포(Canary)
- 기출 이력: 135회 2교시 2번(CI/CD 파이프라인에서 DevSecOps 적용방안)

## 핵심 그림 (30초 인출용)

```text
+-------------------------------------------------------------------------+
|                CI/CD 단계별 파이프라인 및 DevSecOps 도구 체인           |
+-------------------------------------------------------------------------+
| [ Code ] ────> [ Build & Test ] ────> [ Package ] ────> [ Deploy & Ops ] |
|   │                     │                    │                 │        |
| IDE 보안 플러그인   정적 분석(SAST)      컨테이너 빌드     선언적 GitOps 배포   |
| 커밋 전 시크릿 스캔   (SonarQube)         오픈소스 검증(SCA) (ArgoCD Pull 동기화)|
| (TruffleHog)       단위·통합 테스트      (BlackDuck)       Canary / Blue-Green  |
|                     (JUnit, Mockito)     이미지 무결성 서명  동적 분석(DAST)     |
|                                          (Cosign, Notary)   (OWASP ZAP)         |
+-------------------------------------------------------------------------+
|                   푸시(Push) 기반 vs GitOps 풀(Pull) 기반 배포           |
|                                                                         |
| [전통적 Push 방식] CI 서버가 프로덕션 클러스터 관리자 권한을 소유 (보안 취약)|
|   CI Server ────── kubeconfig (클러스터 관리자 권한) ─────> K8s Cluster |
|                                                                         |
| [현대적 GitOps Pull] 클러스터 내부 에이전트가 Git 저장소를 감시 (보안 강화)   |
|   Git Repo (선언적 YAML) <── Pull 동기화 ── ArgoCD Agent (In-Cluster)   |
+-------------------------------------------------------------------------+
```

## 비교·연결 (유사 개념 간 차이점)

### 지속적 제공(Continuous Delivery) vs 지속적 배포(Continuous Deployment)

| 비교 항목 | 지속적 제공 (Continuous Delivery) | 지속적 배포 (Continuous Deployment) |
|---|---|---|
| **프로덕션 릴리스 주체** | **인간(비즈니스 결정자 / 운영자)의 수동 승인** | **파이프라인 통과 시 100% 완전 자동 무인 배포** |
| **자동화 범위** | 코드 커밋부터 스테이징 배포 및 검증까지 | 코드 커밋부터 최종 프로덕션 환경 서빙까지 |
| **적합한 시스템 도메인** | 규제 준수(금융, 의료) 및 릴리스 일정 조율 필요 시스템 | 빠른 피드백이 생명인 클라우드 SaaS, 이커머스 B2C |
| **선결 조건** | 자동화된 스테이징 테스트 및 아티팩트 보관 | **카나리(Canary) 배포 및 메트릭 기반 자동 롤백 체계** |

### CI/CD vs DevOps

| 구분 | DevOps (문화 및 철학) | CI/CD (기술 및 파이프라인) |
|---|---|---|
| **본질적 정의** | 개발(Dev)과 운영(Ops)의 사일로를 해체하는 조직적 협업 문화 | 소프트웨어 빌드·테스트·배포를 자동화하는 구체적 엔지니어링 도구 체계 |
| **목표 지향점** | 비즈니스 가치 전달 속도 극대화 및 공유 책임성 확보 | 변경 리드 타임(Lead Time) 단축 및 배포 실패율 최소화 |
| **관계성** | **전략적 상위 개념 (Culture & Philosophy)** | **DevOps 철학을 실현하는 핵심 실행 메커니즘 (Enabler)** |

## 실무 적용과 트레이드오프

- 적용 상황: 하루 수십 회 배포를 수행하는 대규모 분산 마이크로서비스(MSA) 환경

| 실패 증상 (위험) | 근본 원인 | 엔지니어링 대책 | 기대 효과 |
|---|---|---|---|
| **신규 배포 직후 치명적 런타임 오류로 전사 서비스 장애 발생** | 전체 인스턴스를 일괄 교체(Big-Bang)하는 수동 배포 방식 채택 | 카나리(Canary) 점진적 트래픽 전환 및 Prometheus 에러율 기반 자동 롤백(Argo Rollouts) | 장애 영향도를 전체 트래픽의 5% 미만으로 격리 및 1분 내 자동 복구 |
| **배포 로그 및 소스코드 저장소에 클라우드 API Key 자격증명 유출** | 환경변수 하드코딩 및 파이프라인 로그 마스킹 정책 부재 | Git 사전 커밋 훅(Gitleaks) 및 HashiCorp Vault 외부 시크릿 매니저 연동 | 중요 자격증명 및 API 토큰 유출 사고 100% 원천 차단 |
| **오염된 외부 오픈소스 패키지 유입으로 백도어 삽입 사고** | CI 단계에서 서드파티 라이브러리의 보안 취약점 점검 생략 | 파이프라인 내 SCA(Software Composition Analysis) 및 이미지 서명(Cosign) 검증 강제 | 소프트웨어 공급망 공격(Supply Chain Attack) 선제 방어 |

## 기술사의 눈 (주체적 차별화 제언)

- **[배포 속도 지상주의에 따른 보안 우회 딜레마]**: 비즈니스의 빠른 출시 압박으로 인해 많은 개발팀이 보안 검증을 '귀찮은 관문'으로 치부하고 우회함. 이는 결국 Log4j, SolarWinds 사태와 같은 치명적인 공급망 보안 참사로 이어짐.
- **[나라면: GitOps 풀 기반 선언적 배포와 Shift-Left DevSecOps 품질 게이트 확립]**:
  1. **Shift-Left 보안 게이트 내재화**: 개발자가 코드를 커밋하는 IDE 단계부터 시크릿 스캔을 실행하고, CI 빌드 서버에서 SAST(SonarQube)와 SCA(BlackDuck)를 가동하여 CVSS 7.0 이상의 취약점이 발견되면 빌드를 즉시 Fail 처리하는 엄격한 품질 게이트 적용.
  2. **무결성 검증 체인**: 빌드된 컨테이너 이미지에 전자 서명(Cosign)을 날인하고 사내 프라이빗 레지스트리에만 저장하여, 인가되지 않은 변조 이미지의 실행을 원천 차단.
  3. **GitOps 풀 기반 Zero-Trust 배포**: CI 서버에 프로덕션 K8s 클러스터 접근 권한을 일체 부여하지 않고, 클러스터 내부의 ArgoCD 에이전트가 Git 저장소의 선언적 명세만을 감시하여 일치시키는 GitOps 아키텍처를 도입함으로써, 배포 속도와 보안 신뢰성을 완벽히 양립시키겠음.
