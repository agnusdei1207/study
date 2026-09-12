---
sidebar:
  order: 55
  label: "055. GitOps"
  badge:
    text: "미출 · 50%"
    variant: note
title: "GitOps"
date: "2026-09-07T10:00:00+09:00"
tags:
  - "notes-software"
weight: 55
extra:
  question_no: "055"
  source_status: "기출"
  source_history: ""
  priority: 50
  priority_note: "선언적 인프라와 Git 기반 지속적 배포 및 자동 동기화"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **GitOps**: Git 저장소를 시스템의 단일 진실 공급원(SSOT)으로 삼고, 선언적(Declarative) 매니페스트를 클러스터에 자동 동기화하는 운영 모델.
- **SSOT(Single Source of Truth)**: 시스템의 목표 상태(Desired State)를 정의하는 유일한 단일 권위 저장소(Git).

</details>

- 정의/개념: Git 저장소를 **단일 진실 공급원(SSOT)** 으로 삼고, 클러스터 내부 컨트롤러가 목표 상태를 자동 수렴시키는 **GitOps** 운영 모델
- 배경/필요성: 전통적 Push 파이프라인의 CI 서버 관리자 자격증명 노출 취약점 및 **수동 명령(`kubectl`) 조작에 따른 형상 불일치(Drift) 한계**

#### 한줄 요약
- 선언적 인프라 명세를 Git에 버전 관리하고, 클러스터 내부 에이전트가 목표 상태를 자동 동기화한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **Pull-based Deployment**: 외부 CI가 클러스터에 접속하는 대신, 클러스터 내부의 ArgoCD/Flux가 Git을 아웃바운드로 감시하여 상태를 당겨오는 방식.
- **Reconciliation Loop(조정 루프)**: Git의 선언 상태(Desired)와 K8s 실제 상태(Actual)의 차이(Drift)를 주기적으로 비교하여 일치시키는 제어 루프.

</details>

- **OpenGitOps 4대 원칙**(선언형 명세, Git 버전 제어, 풀 기반 자동 인입, 지속적 조정) 준수
- 클러스터 인바운드 방화벽 오픈 없는 **풀 기반(Pull-based)** 배포로 제로 트러스트 보안 달성
- 런타임 임의 수정 발생 시 Git 선언 상태로 강제 복구하는 **자가 치유(Self-Healing)**

#### 한줄 요약
- 풀 기반 수렴은 드리프트와 권한 노출을 없애는 대신 모든 변경이 Git을 거치게 하므로, 신속성을 감사 가능성과 맞바꾼 구조다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **ArgoCD / FluxCD**: Kubernetes 클러스터 내부에서 동작하며 Git 리포지토리의 YAML 변경을 감지하여 K8s API로 동기화하는 GitOps 컨트롤러.

</details>

```text
[GitOps 동기화 체계]
  │
  ├─ [CI 파이프라인] (빌드 후 Git 매니페스트 태그 갱신)
  │
  ├─ [Git 배포 저장소] (선언적 SSOT·K8s YAML 버전 관리)
  │
  ├─ [GitOps 컨트롤러: ArgoCD] (Git 감시·Drift 감지 및 Sync)
  │
  └─ [Reconciliation Engine] (K8s API 호출·Self-Healing)
```
- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| Git 배포 저장소 (SSOT) | 시스템 목표 상태를 정의하는 K8s 매니페스트(YAML)의 완전한 버전 보관 |
| GitOps 컨트롤러 (ArgoCD) | Git 저장소와 실제 클러스터 상태를 비교하여 **차이(Drift) 감지 및 자동 Sync** |
| Reconciliation Engine | K8s API Server를 호출하여 파드 생성, 서비스 갱신 등 **자가 치유(Self-Healing)** |
| CI 파이프라인 | 앱 빌드 후 **배포 Git 저장소의 이미지 태그(`image.tag`)만 갱신** |

#### 한줄 요약
- 조정 엔진이 Git의 선언 상태와 클러스터 실제 상태를 계속 비교하므로, 배포가 명령의 실행이 아니라 차이의 수렴으로 정의된다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **OutOfSync**: Git에 정의된 매니페스트 내용과 실제 K8s 클러스터 리소스 상태 사이에 불일치가 발생한 상태.

</details>

```text
[GitOps 동기화 흐름] (진행 ①→⑥, 수동 조작 발생 시 자가 치유 갈래로 수렴)
  │
  ├─ [매니페스트 병합] (① 개발자가 배포 Git 저장소에 PR 병합(image.tag v2.0 등))
  │
  ├─ [커밋 감지] (② ArgoCD가 Webhook 또는 Polling으로 Git 신규 커밋 감지)
  │
  ├─ [Drift 판정] (③ Git 목표 상태(v2.0)와 클러스터 실제 상태(v1.0)를 비교, OutOfSync 판정)
  │
  ├─ [동기화 수행] (④ K8s API Server 호출로 신규 ReplicaSet 생성·롤링 배포)
  │
  ├─ [Synced 확인] (⑤ 클러스터 상태가 목표 상태(v2.0)와 일치(Synced)됨을 확인)
  │
  └─ [자가 치유] (⑥ 누군가 kubectl로 수동 조작 시 즉각 Self-Healing이 Git 매니페스트 기준으로 원상 복구)
```

분기 결과: 조정 루프 판정에서 갈리므로, Git과 일치하는 갈래는 배포가 차이 수렴으로 끝나 감사 가능성을 얻는 반면, 수동 조작 갈래는 Self-Healing 복구가 즉시 작동해 사람의 임의 변경이 무효화된다

#### 한줄 요약
- 사람이 클러스터를 직접 바꿔도 조정 루프가 다시 Git 상태로 되돌리므로, 자가치유는 곧 수동 개입을 무효로 만드는 성질이기도 하다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **Push 기반 CI/CD vs Pull 기반 GitOps**: Jenkins가 K8s kubeconfig 관리자 권한을 쥐고 밀어넣는 Push와 ArgoCD가 내부에서 당겨오는 Pull 비교.

</details>

| 비교 항목 | 전통적 Push 기반 CI/CD (Jenkins) | Pull 기반 GitOps 모델 (ArgoCD) |
|:---|:---|:---|
| 배포 실행 주체 | **외부 CI 서버 (Jenkins, GitHub Actions)** | **클러스터 내부 컨트롤러 (ArgoCD, Flux)** |
| 클러스터 보안 | CI 서버에 **K8s Admin Token 영구 보관** | **외부 접근 차단 (아웃바운드 Git 통신만 수행)** |
| 형상 드리프트 대응 | 수동 변경 발생 시 방치됨 | **주기적 조정 루프로 감지 후 즉시 원복** |
| 롤백 절차 | 이전 빌드 파이프라인 재실행 | **`git revert` 커밋 하나로 수 초 내 롤백** |

#### 한줄 요약
- Push 방식의 보안 위험과 형상 드리프트를 Pull 방식 GitOps의 자가 치유와 제로 인바운드로 해결한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **Sealed Secrets / External Secrets Operator**: Git에 비밀번호를 비대칭 암호화하여 커밋하고 클러스터 내부에서만 복호화하는 보안 솔루션.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| Git 저장소에 DB 암호 등 Secret 평문 노출 | **Sealed Secrets 또는 External Secrets Operator(Vault 연동)** | Git에 암호화된 비밀 저장 및 클러스터 안전 복호화 |
| 소스 코드와 배포 매니페스트 혼재로 인한 빌드 루프 | **애플리케이션 소스 레포와 배포 매니페스트 레포의 물리적 분리** | CI 무한 루프 차단 및 개발자/운영자 권한 격리 |
| 환경별(Dev, Stg, Prod) 매니페스트 중복 | **Kustomize Overlay 또는 Helm Chart** 템플릿 표준화 | 공통 Base 매니페스트 재사용 및 환경별 값만 오버레이 |
| 긴급 핫픽스 시 수동 변경의 원복 충돌 | 긴급 조치도 반드시 **Git 커밋/PR을 통해 수행하는 문화 정착** | 변경 이력 100% 추적성 및 거버넌스 사수 |

#### 한줄 요약
- 선언적 수렴은 드리프트와 권한 노출을 없애는 대신 긴급 상황에서도 Git을 거치게 만들므로, 핫픽스 경로까지 Git 기반으로 설계하고 기밀은 암호화해 저장소에 두어야 우회 유인이 사라진다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **코드 기반 정책(Policy as Code, PaC)**: 시스템 인프라 및 배포 매니페스트의 보안 컴플라이언스 규칙(예: Root 권한 금지, 리소스 Limit 필수)을 코드로 정의하고 사전 검증하는 기법(예: Kyverno, OPA).
- **쿠스토마이즈(Kustomize)**: 별도의 템플릿 문법 없이 순수 선언적 YAML 오버레이(Overlay)를 통해 개발·운영 등 환경별 차이점을 구조화하여 관리하는 쿠버네티스 네이티브 형상 관리 도구.
- **플랫폼 엔지니어링(Platform Engineering)**: 복잡한 인프라와 GitOps 파이프라인을 추상화하여 내부 개발자 플랫폼(IDP)을 구축하고 팀의 셀프서비스 운영을 지원하는 엔지니어링 체계.

</details>

- **차세대 발전 전망**: 멀티 클러스터 및 엣지 컴퓨팅 환경에서 **코드 기반 정책(Policy as Code)** 및 **플랫폼 엔지니어링** 기반 내부 개발자 플랫폼(IDP)과 결합되어, 인프라 선언과 보안 검증을 통합 자동화하는 전사 표준 운영 모델로 진화 추세.
- **실무 공학적 통찰**: 소스 코드와 배포 매니페스트 저장소의 물리적 분리를 철저히 집행하고, **쿠스토마이즈(Kustomize)** 기반 오버레이 관리와 비대칭 암호화 시크릿 거버넌스를 정착시켜 임의 변경(Drift) 없는 자가 치유 무결성 확보 필요.

#### 한줄 요약
- GitOps는 Policy as Code 및 플랫폼 엔지니어링과 융합하여 선언적 자가 치유를 실현하되, 저장소 물리 분리와 Kustomize 기반 환경 거버넌스가 운영 신뢰성의 핵심이다.
