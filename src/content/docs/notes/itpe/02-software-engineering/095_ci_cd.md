---
title: "CI/CD(Continuous Integration / Continuous Delivery / Continuous Deployment)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- CI/CD(Continuous Integration/Continuous Delivery/Continuous Deployment), 파이프라인, GitOps, Trunk-Based Development
- 무중단 배포(Blue-Green/Canary), 자동 롤백, 소프트웨어 공급망 보안, SBOM(Software Bill of Materials), DevSecOps

## Ⅰ. CI/CD의 개요

- 핵심 요약 : 코드 병합부터 검증된 배포까지 자동화하는 현대 소프트웨어 공학의 핵심 파이프라인.
- 개념 : 지속적 통합 CI(Continuous Integration)와 지속적 전달·배포 CD(Continuous Delivery/Continuous Deployment)의 결합 체계로, 소스코드의 공유 저장소 빈번한 병합(지속적 통합)과 빌드·자동화 테스트를 거친 검증 아티팩트의 스테이징 및 프로덕션 환경 안전 배포(지속적 전달/배포)를 자동화하는 현대 소프트웨어 공학의 핵심 파이프라인.
- 배경 및 필요성 : 개발 후반부 대규모 병합 지옥(Merge Hell) 방지, 수작업 배포 인적 오류(배포 사고) 근절, 비즈니스 가치의 사용자 신속 전달.
- 핵심 구분 : 지속적 통합(CI), 지속적 전달(언제든 배포 가능한 상태 유지, 수동 승인 전제), 지속적 배포(검증 통과 후 프로덕션 배포 자동화). CD는 후행 두 의미로 사용, 문맥 구분 필요.

## Ⅱ. CI/CD의 특징

- 핵심 요약 : 빈번한 통합과 자동 품질 게이트, 선언적 배포·자동 롤백의 결합 체계.

1. Trunk-Based Development : 장기 실행 브랜치 제거, 메인 트렁크 일일 병합을 통한 통합 충돌 최소화.
2. 빌드·정적 분석·보안 점검·테스트의 자동 실행 품질 게이트(SonarQube, Snyk).
3. 컨테이너 이미지 태깅과 아티팩트 레지스트리(Harbor, ECR(Elastic Container Registry)) 중심 버전 관리.
4. GitOps 모델 : Git 저장소의 단일 진실 공급원(Single Source of Truth)화, 클러스터 상태의 선언적 매니페스트 동기화(ArgoCD).
5. 카나리·블루그린 무중단 배포와 메트릭 기반 자동 롤백(Prometheus).

## Ⅲ. CI/CD 파이프라인의 구조 (흐름)

- 핵심 요약 : 커밋부터 CI 품질 검증, 아티팩트 저장, CD 배포·오케스트레이션까지의 엔드투엔드 흐름.
- 엔드투엔드 CI/CD 파이프라인 흐름.

```text
[ Git Commit / PR ]
   │
   ▼
[ 1. CI 단계: 빌드 및 품질 검증 ]
 - 의존성 다운로드, 바이너리 컴파일
 - 단위/통합 테스트 자동 실행 (JaCoCo)
 - 정적 분석, 보안 점검 (SonarQube, Snyk)
 - 통과 시 컨테이너 이미지 빌드 및 태깅
   │
   ▼
[ Artifact Registry ]
 - 도커 이미지 저장 (Harbor, ECR)
   │
   ▼
[ 2. CD 단계: 배포 및 오케스트레이션 ]
 - GitOps 컨트롤러(ArgoCD) 매니페스트 동기화
 - 스테이징 배포 및 E2E 자동 테스트 수행
 - 프로덕션 무중단 배포 (Canary/Blue-Green)
 - Prometheus 메트릭 이상 감지 시 자동 롤백
```

- CI 단계 : 의존성 다운로드와 바이너리 컴파일, 단위·통합 테스트(JaCoCo), 정적 분석·보안 점검(SonarQube, Snyk) 통과 시 컨테이너 이미지 빌드·태깅.
- CD 단계 : GitOps 컨트롤러(ArgoCD)의 매니페스트 동기화, 스테이징 배포와 E2E(End-to-End) 자동 테스트, 프로덕션 무중단 배포(Canary/Blue-Green), 메트릭 이상 감지 시 자동 롤백.

## Ⅳ. 지속적 통합·전달·배포의 비교

- 핵심 요약 : 프로덕션 배포 승인 주체와 자동화 성숙도 요구 수준의 차이.
- 자동화 범위 대조.

```text
[Commit]→[Build]→[Test]→[Artifact]→[Staging]→(수동 승인)→[Production]
 └─── CI ───┘
             └─────────── 지속적 전달 ───────────┘
             └────────────── 지속적 배포 (전 단계 자동) ──────────────┘
```

| 구분 | 지속적 통합(CI) | 지속적 전달(Continuous Delivery) | 지속적 배포(Continuous Deployment) |
|---|---|---|---|
| 범위 | 코드 커밋부터 빌드, 테스트, 아티팩트 생성 | 프로덕션 배포 직전 단계까지 모든 과정 자동화 | 프로덕션 환경 배포까지 인간 개입 없이 100% 자동화 |
| 프로덕션 배포 승인 | 배포 단계 포함하지 않음 | 비즈니스 담당자나 관리자의 수동 승인(One-Click) | 테스트 통과 즉시 자동으로 실운영 환경 배포 |
| 피드백 속도 | 코드 품질 및 결함 여부 즉각 피드백 | 릴리스 가능한 패키지 항시 대기 | 고객에게 신규 가치 실시간 제공(분당/시간당) |
| 요구되는 성숙도 | 단위 테스트 및 기본 빌드 파이프라인 | 스테이징 통합 테스트 및 회귀 테스트 자동화 | 완벽한 카나리 배포, 자동 롤백, 정밀 관측성 인프라 |

## Ⅴ. CI/CD의 장점과 한계

- 핵심 요약 : 신속한 가치 전달·낮은 배포 리스크의 장점, 공급망 보안·파이프라인 지연·롤백 복잡도의 한계.
- 장점
  1. 소규모 변경의 지속 통합을 통한 병합 지옥 방지와 결함 조기 발견.
  2. 자동화 배포로 배포 사고·인적 오류 최소화와 릴리스 리드타임 단축.
  3. 무중단 배포 전략과 자동 롤백을 통한 서비스 가용성 유지.
- 한계점 1 : 소프트웨어 공급망 보안(Software Supply Chain Security) 취약성
  - 한계점 : 파이프라인 스크립트 탈취, 비인가 의존성 주입(Dependency Confusion), 서명되지 않은 이미지 배포에 따른 보안 침해 사고 위험.
  - 해결 방안 : SLSA(Supply-chain Levels for Software Artifacts) 프레임워크 준수, Cosign/Notary 기반 컨테이너 이미지 전자서명 검증, 빌드 시 SBOM(Software Bill of Materials) 자동 생성과 SCA(Software Composition Analysis) 스캔 강제.
- 한계점 2 : 파이프라인 실행 시간 증가에 따른 개발 피드백 루프 지연
  - 한계점 : 코드베이스 확장에 따른 빌드·정적 분석·테스트 단계 비대화, PR(Pull Request) 검증 수십 분 이상 소요와 개발자 생산성 저하.
  - 해결 방안 : 멀티 스테이지 도커 캐싱, 분산 빌드 캐시(Bazel, Gradle Enterprise) 도입, 코드 변경 영향도 기반 병렬 분산 테스트 실행.
- 한계점 3 : 배포 실패 시 상태 롤백 복잡도 및 런타임 불일치
  - 한계점 : DB(Database) 스키마 마이그레이션 포함 배포 실패 시 애플리케이션 단독 롤백의 스키마 불일치, 시스템 전체 장애 확산.
  - 해결 방안 : 확장 및 수축(Expand and Contract) 패턴 기반 하위 호환 DB 마이그레이션 적용, GitOps(ArgoCD)와 블루그린·카나리 무중단 롤백 파이프라인 체계화.

## Ⅵ. 안정적인 CI/CD 정착을 위한 기술사적 제언

- 핵심 요약 : 시프트 레프트 기반 DevSecOps 게이트 내재화와 카나리 점진적 롤아웃의 결합.
- 시프트 레프트(Shift-Left) 기반 DevSecOps 품질 게이트웨이 내재화 : CI 단계 소스코드 보안약점 진단 SAST(Static Application Security Testing), 오픈소스 취약점 점검(SCA), 컨테이너 이미지 보안 스캔(Trivy)의 의무화, 기준 미달 빌드 차단 게이트 구축.
- 선언적 GitOps와 카나리 점진적 롤아웃(Progressive Delivery) : ArgoCD와 Argo Rollouts의 결합, 배포 후 오류율(HTTP 5xx)과 지연시간(Latency)의 프로메테우스 메트릭 실시간 분석, 이상 징후 시 자동 롤백 안전망 구축.

## Ⅶ. 결론

- 핵심 요약 : CI/CD는 신속성과 안정성을 동시에 확보하는 소프트웨어 납품 표준 체계.
- 요약 : 지속적 통합의 품질 게이트와 지속적 전달·배포의 무중단 롤아웃이 핵심 골격.
- 시사점 : 공급망 보안 강화, 파이프라인 속도 최적화, 하위 호환 마이그레이션 설계가 성숙한 CI/CD의 조건.
