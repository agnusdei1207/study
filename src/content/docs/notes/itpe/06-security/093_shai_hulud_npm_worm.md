---
title: "Shai-Hulud npm 웜"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 93
  label: "093. Shai-Hulud npm 웜"
  badge:
    text: "기초"
    variant: note
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"

---

## 지식 로드맵 내 현재 위치

소프트웨어 공급망 보안 → 오픈소스 패키지 생태계 → Shai-Hulud npm 웜 공격

## 30초 인출

- **본질:** npm 패키지 설치 단계의 라이프사이클 스크립트(postinstall)와 개발자/CI 환경의 인증 토큰을 탈취하여, 자신이 접근 가능한 다른 npm 패키지에 악성코드를 자동 주입·재배포하는 자가 증식형(Self-Replicating) 공급망 웜.
- **메커니즘:** 악성 패키지 설치 실행 → postinstall 트리거로 로컬 `.npmrc` 및 환경변수(CI Secrets) 탈취 → 공격자 C2 유출 및 npm API 호출 → 개발자의 모든 관리 대상 패키지에 악성 버전 연속 배포.
- 통찰: 단순 스크립트 실행 제한(`--ignore-scripts`)을 넘어 npm Trusted Publishers(OIDC 기반 무토큰 배포) 도입 및 CI/CD 빌드 시크릿 격리, 락파일 무결성 검증 필수.

<details><summary>핵심 용어</summary>

- **Shai-Hulud**: SF 소설 '듄(Dune)'의 모래벌레에서 이름을 딴 npm 공급망 자가 증식 웜 캠페인.
- **라이프사이클 스크립트(postinstall)**: `npm install` 실행 시 패키지 다운로드 완료 직후 자동으로 셸 명령을 실행하는 메커니즘.
- **Trusted Publishers**: 장기 보관 npm API 토큰 대신 GitHub Actions 등 CI 워크플로우와 OIDC 단기 페더레이션을 통해 패키지를 발행하는 보안 메커니즘.
- **.npmrc**: npm CLI의 설정 파일로, 개발자 홈 디렉토리에 레지스트리 인증 토큰(`//registry.npmjs.org/:_authToken`)이 평문 저장되어 주요 탈취 대상이 됨.
- **자가 증식 웜(Supply Chain Worm)**: 단일 희생자 감염에 그치지 않고, 희생자의 권한을 도용하여 상위 저장소에 악성코드를 재게시함으로써 다운스트림 전체로 기하급수적 전파를 일으키는 공격.
</details>

---

## 2~4교시 예상문제 (25점)

> 오픈소스 생태계를 위협하는 자가 증식형 공급망 공격인 'Shai-Hulud npm 웜'의 침투 및 전파 메커니즘을 분석하고, 개발자 환경과 CI/CD 빌드 파이프라인 관점에서의 보안 취약점과 엔지니어링 방어 방안을 제시하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | npm 패키지 설치 시 실행되는 훅(postinstall)과 개발자 머신의 자격증명을 악용하여 감염된 개발자가 관리하는 모든 패키지로 악성코드를 자동 복제·재게시하는 오픈소스 공급망 웜 |
| 목적 | 단일 계정 탈취를 지렛대 삼아 수천 개의 오픈소스 패키지와 이를 사용하는 다운스트림 기업 환경으로 침해를 기하급수적으로 연쇄 확산 |

## Ⅱ. Shai-Hulud npm 웜의 핵심 특징

| 특징 | 세부 동작 양상 | 기술적 파급 효과 |
|---|---|---|
| 자동 실행 훅 악용 | `package.json`의 `preinstall`/`postinstall` 스크립트를 통해 설치 즉시 코드 실행 | 개발자가 코드를 실행해보기도 전에 인스톨 시점에 즉각 감염 |
| 자격증명 자동 수집 | `~/.npmrc`, 환경변수(`$NPM_TOKEN`), AWS/GitHub 시크릿 탐색 및 C2 유출 | 머신에 저장된 모든 배포 권한과 클라우드 접근 권한 일괄 피탈 |
| 자가 증식(Worm) 전파 | 탈취한 토큰으로 `npm access ls-packages`를 실행해 희생자의 관리 패키지 전수 파악 | 패치 버전 번호를 올린 뒤 웜 페이로드를 삽입하여 npm에 자동 재게시 |
| CI/CD 러너 표적화 | 로컬 개발자 PC뿐 아니라 GitHub Actions 러너 내부에서도 빌드 과정 중 실행 | 신뢰된 자동화 파이프라인을 악성코드 배포 기지로 악용 |
| 신뢰된 계정 남용 | 신규 생성된 의심 계정이 아닌 오랜 명성을 가진 기존 유명 패키지의 정상 계정 도용 | 보안 스캐너 및 개발자의 의심을 회피하고 다운로드 신뢰 악용 |

## Ⅲ. Shai-Hulud 자가 증식 메커니즘 및 공급망 방어 아키텍처

```text
[ 1. 최초 감염 단계 ]
개발자 / CI 환경에서 명령 실행: npm install <오염된 패키지>
       │
       ▼
[ 2. 인스톨 스크립트 실행 ]
npm 라이프사이클 트리거 ──▶ package.json 내 "scripts": {"postinstall": "node setup.js"} 실행
       │
       ▼
[ 3. 시크릿 수집 및 유출 ]
setup.js 실행 ──▶ ~/.npmrc 파싱 및 $NPM_TOKEN, $GITHUB_TOKEN 메모리 탈취 ──▶ 외부 C2 전송
       │
       ▼
[ 4. 웜 자가 증식 (Worm Propagation) ]
npm API 질의: npm access ls-packages (해당 토큰으로 쓰기 권한이 있는 모든 패키지 목록 획득)
       │
       ▼
루프 실행: 각 대상 패키지 다운로드 ──▶ postinstall 웜 코드 삽입 ──▶ 버전 범프 (1.0.1 -> 1.0.2)
       │
       ▼
공식 배포: npm publish (개발자 본인의 정식 인증 토큰으로 공식 레지스트리에 배포!)
       │
       ▼
[ 5. 다운스트림 대규모 확산 ]
해당 패키지를 의존하는 전 세계 수만 개 프로젝트로 연쇄 전파 (Supply Chain Pandemic)
```

| 방어 계층 | 도입 통제 기술 | 실무 구현 상세 |
|---|---|---|
| 패키지 설치 시점 | 스크립트 실행 차단 | `npm install --ignore-scripts`, `.npmrc` 내 `ignore-scripts=true` 강제 |
| 패키지 인증/배포 | OIDC 신뢰 게시 | 정적 `NPM_TOKEN` 영구 폐기, GitHub Actions OIDC 기반 Trusted Publishers 연동 |
| CI/CD 파이프라인 | 러너 권한 최소화 | 빌드 단계와 배포 단계의 Job 분리, 빌드 단계에서 네트워크 및 게시 권한 격리 |
| 의존성 무결성 | 락파일 해시 검증 | `package-lock.json`의 SHA-512 무결성 강제 검증(`npm ci`), 해시 불일치 시 빌드 중단 |
| 이상 행위 모니터링 | 레지스트리 감시 | 패키지 버전의 비정상적 심야 배포, 파일 크기 급증 탐지 시 배포 자동 격리 |

## Ⅳ. 전통적 악성 패키지(Typosquatting) vs 자가 증식 웜(Shai-Hulud) 비교

| 비교 항목 | 전통적 타이포스쿼팅 (Typosquatting) | 자가 증식 웜 (Shai-Hulud npm Worm) |
|---|---|---|
| 패키지 명칭 | 유명 패키지와 유사한 오타 유도 (예: `cross-env` vs `crossenv`) | 이미 널리 쓰이는 원본 정식 패키지 명칭 그대로 사용 |
| 배포 주체 | 공격자가 급조한 신규 익명 계정 | 침해당한 원본 유명 패키지 관리자의 공인 계정 |
| 전파 메커니즘 | 개발자의 수작업 오타 입력에 의존 (수동적) | 탈취된 자격증명을 통해 웜이 다른 패키지로 자동 확산 (능동적) |
| 확산 속도 | 매우 느림 (오타를 친 일부 사용자만 감염) | 기하급수적 (CI/CD 자동 빌드 트리거를 타고 순식간에 확산) |
| 탐지 난이도 | 신규 패키지 명칭 및 신규 계정 스캔으로 탐지 용이 | 공식 버전 업데이트로 인식되어 기존 보안 룰 우회 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| `--ignore-scripts` 옵션을 전역 적용할 경우 C/C++ 바인딩을 컴파일하는 네이티브 모듈(node-gyp 등)의 빌드 실패 발생 | 화이트리스트 기반 스크립트 허용 도구(`@lavamoat/allow-scripts` 등)를 도입하여 검증된 패키지만 선택적으로 스크립트 실행 허용 |
| npm 2단계 인증(2FA)을 적용하더라도 CLI 자동 배포용으로 생성된 Automation Token은 2FA를 우회하는 취약점 | 장기 보존 API Automation Token 발급을 전면 금지하고 OIDC 기반 단기 신뢰 게시(Trusted Publishers)로 100% 강제 전환 |
| 패키지가 수십 개 이상의 서브 의존성(Transitive Dependencies)을 가질 때 심층 계층에 은닉된 웜 코드의 육안 식별 불가 | CI 단계에서 소켓(Socket.dev)이나 Snyk 등 AST(추상구문트리) 기반 의존성 행위 분석기를 연동하여 네트워크 호출 및 파일 접근 훅 실시간 차단 |
| 개발자 로컬 PC가 감염되었을 때 레지스트리에 이미 오염된 버전이 게시된 후 회수(Unpublish) 지연으로 인한 피해 확산 | 패키지 게시 즉시 샌드박스 동적 분석을 거쳐 30분간 다운로드를 보류하는 카나리아 릴리즈(Canary Release) 정책 도입 |

## Ⅵ. 제언

```text
[ 오픈소스 패키지 공급망 3중 잠금(Lock-down) 체계 ]

+-------------------------+      +-------------------------+      +-------------------------+
|     1. 무토큰 배포      | ---> |     2. 스크립트 격리    | ---> |     3. 락파일 무결성    |
| (OIDC Trusted Publisher)|      | (Allow-scripts 화이트)  |      | (npm ci + SHA-512 검증) |
+-------------------------+      +-------------------------+      +-------------------------+
```

| 관리 영역 | 엔지니어링 구현 과제 | 비즈니스 가치 |
|---|---|---|
| 자격증명 현대화 | 사내 모든 오픈소스 저장소의 npm 토큰 제거 및 OIDC Trusted Publishers 전환 | 영구 API 키 유출로 인한 웜 전파 위험 원천 차단 |
| 개발 환경 하드닝 | 개발자 PC 및 CI 환경에 `allow-scripts` 정책 도입 및 `.npmrc` 접근 통제 | 악성 패키지 유입 시에도 임의 코드 실행 및 시크릿 탈취 방지 |
| 공급망 거버넌스 | 내부 프라이빗 아티팩토리(Artifactory) 캐시 운영 및 신규 패키지 24시간 격리 검증 | 검증된 안전 버전만 사내 배포하여 제로데이 웜 전파 차단 |

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 (오픈소스 소프트웨어 공급망 침해 위협 및 대책)
- GitHub Security Lab, Securing the npm Supply Chain
- npm Official Documentation, Trusted Publishers with OIDC
- OpenSSF (Open Source Security Foundation), Malicious Packages Incident Report

## 연결 토픽

- 소프트웨어 공급망 보안
- 2026 상반기 침해사고 위협 점검
- 비인간 신원(NHI)
- XZ Utils 백도어
