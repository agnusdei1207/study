---
title: "오픈소스 라이선스(Permissive·Copyleft)와 Source-Available 라이선스"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 공공 SW·거버넌스 → **오픈소스 라이선스**

## 30초 인출

- 본질: 오픈소스 라이선스(Open Source License)는 저작권자가 소프트웨어의 사용, 복제, 수정, 재배포 권한을 부여하며 준수해야 할 법적 의무와 조건을 명시한 이용 계약
- 메커니즘: 허용적(Permissive) · 약한 카피레프트(Weak Copyleft) · 강한 카피레프트(Strong Copyleft) · 네트워크 카피레프트(AGPL) 및 Source-Available 라이선스 분류 체계 적용
- 통찰: 바이너리 배포 및 SaaS 서비스 형태에 따라 소스코드 공개 의무가 전파되므로 SCA 도구와 SBOM 기반의 전 주기 오픈소스 컴플라이언스 체계 구축

<details>
<summary>핵심 용어</summary>

- **오픈소스 라이선스(Open Source License)** : 오픈소스 정의(OSD)를 충족하며 소프트웨어의 자유로운 활용과 재배포 조건을 규정한 저작권 이용 허락
- **Permissive License(허용적 라이선스)** : 저작권 고지 및 라이선스 전문 포함 외에 소스코드 공개 의무가 없는 라이선스 (MIT, Apache 2.0, BSD)
- **Copyleft(카피레프트)** : 파생 저작물이나 수정물을 배포할 때 동일한 오픈소스 라이선스 조건으로 소스코드를 공개하도록 강제하는 원칙 (GPL)
- **AGPLv3(Affero GPL v3)** : 네트워크를 통해 소프트웨어를 서비스(SaaS) 형태로 제공하는 경우에도 수정 소스코드 공개 의무를 부과하는 라이선스
- **Source-Available** : 소스코드 열람은 허용하되 클라우드 서비스 제공 등 상업적 활용을 제한하는 비OSI 승인 라이선스 (SSPL, BSL)
- **SBOM(Software Bill of Materials)** : 소프트웨어 제품을 구성하는 오픈소스 패키지 명칭, 버전, 라이선스, 공급망 정보를 기록한 명세서

</details>

---

## 2~4교시 예상문제 (25점)

> 오픈소스 소프트웨어(OSS) 라이선스의 유형별 의무사항을 설명하고, 허용적 라이선스와 카피레프트 라이선스의 차이 및 기업의 오픈소스 컴플라이언스 체계 구축 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 오픈소스 라이선스의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **오픈소스 라이선스(Open Source License)** 는 저작권자가 사용자에게 소스코드의 이용·수정·배포 권한을 부여하면서 일정한 의무 조건을 부과하는 법적 라이선스 계약 |
| 목적 | 오픈소스 저작권 침해 분쟁 예방, 지식재산권 보호 및 투명한 소프트웨어 공급망 보안 체계 확립 |

## Ⅱ. 오픈소스 라이선스의 핵심 특징

| 특징 | 의미 |
|---|---|
| 조건부 권한 부여 | 소프트웨어의 자유로운 활용을 보장하되 고지 의무, 소스 공개 등 조건 준수 강제 |
| 배포 방식 의존 | 단순 사내 이용과 외부 배포(바이너리 판매, 클라우드 SaaS 제공)에 따른 의무 차등 |
| 전파성(Viral Effect) | 카피레프트 계열 라이선스 결합 시 독점 소프트웨어의 소스코드까지 공개 위험 내포 |

## Ⅲ. 라이선스 유형별 의무 및 검증 메커니즘

### 오픈소스 라이선스 계열별 의무 강도 스펙트럼

```text
[Permissive] ───→ [Weak Copyleft] ───→ [Strong Copyleft] ───→ [Network Copyleft]
 (MIT, Apache)      (LGPL, MPL)             (GPL v2/v3)              (AGPL)
 ├─ 저작권 고지     ├─ 수정 모듈 공개       ├─ 전체 결합물 공개     ├─ 네트워크 서비스 시
 └─ 소스 비공개     └─ 동적 링킹 허용       └─ 정적/동적 링킹 전파   └─ 원격 사용자 소스 공개
```

### 소스코드 결합 방식에 따른 라이선스 의무 판정 흐름

```text
오픈소스 라이브러리 도입
    ↓
라이선스 유형 식별
    ├─ Permissive (MIT, Apache) → 저작권 고지문 작성 후 상용 결합 승인
    └─ Copyleft (LGPL, GPL, AGPL)
        ↓
결합 방식 및 서비스 형태 판정
    ├─ LGPL + 동적 링킹(Dynamic Linking) → 상용 코드 비공개 유지 가능
    ├─ GPL + 정적/동적 링킹 → 상용 코드 전체 소스코드 공개 의무 발생 (도입 차단)
    └─ AGPL + 웹 서비스 호스팅 → 서비스 이용자 대상 소스코드 다운로드 제공 의무
```

| 라이선스 계열 | 대표 라이선스 | 소스코드 공개 의무 범위 | 특허권 조항 | 상용 소프트웨어 위험도 |
|---|---|---|---|---|
| Permissive | MIT, Apache 2.0, BSD | 없음 (고지 의무 및 면책 조항만 준수) | Apache 2.0 명시적 특허 라이선스 부여 | 매우 낮음 (자유로운 상용화) |
| Weak Copyleft | LGPL 2.1/3.0, MPL | 오픈소스 자체 수정 시에만 공개, 동적 링킹 허용 | LGPL 3.0 특허 조항 포함 | 중간 (결합 방식 통제 필요) |
| Strong Copyleft | GPL 2.0/3.0 | 결합하여 배포되는 파생 저작물 전체 공개 | GPL 3.0 특허 보복 조항 포함 | 매우 높음 (영업비밀 유출 위험) |
| Network Copyleft | AGPL 3.0 | 네트워크를 통해 서비스 제공 시 원격 사용자 공개 | 특허 조항 포함 | 최고 위험 (SaaS 기업 치명적) |

## Ⅳ. 오픈소스 라이선스 컴플라이언스 체계

```text
[1단계: 식별] ──→ SCA 도구를 통한 의존성 스캔 및 SBOM 생성 (SPDX/CycloneDX)
      ↓
[2단계: 분석] ──→ 라이선스 의무 분석 및 상용 코드 결합 위험도(충돌 여부) 판정
      ↓
[3단계: 통제] ──→ 고위험 라이선스(GPL/AGPL) 유입 차단 및 대체재 선정
      ↓
[4단계: 이행] ──→ 오픈소스 고지문(Open Source Notice) 생성 및 요구 소스 배포
```

### Source-Available 라이선스와 오픈소스(OSI) 비교

| 비교 항목 | 오픈소스 (OSI 승인 라이선스) | Source-Available 라이선스 (SSPL, BSL) |
|---|---|---|
| 소스코드 열람 | 완전 공개 및 자유로운 접근 허용 | 소스코드 공개 및 수정 허용 |
| 상업적 이용 제한 | 차별 금지 원칙(OSD 5, 6조)에 따라 상업적 이용 보장 | 클라우드 서비스 제공업체(매니지드 서비스)의 무료 상용화 금지 |
| 대표 소프트웨어 | Linux, PostgreSQL, Apache HTTPD | MongoDB(SSPL), Redis(Source-Available 전환) |
| 법적 지위 | 공식 공인 오픈소스 소프트웨어 | 독점적 상용 소프트웨어와 오픈소스의 중간 형태 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 개발자의 무단 오픈소스 도입 및 복사-붙여넣기로 인한 GPL 오염 위험 | CI 파이프라인 내 **SCA(Software Composition Analysis)** 정적 스캔 게이트웨이 구축 |
| 오픈소스 간 라이선스 조항 상충(Incompatible Licenses)으로 인한 배포 불가 | 라이선스 호환성 매트릭스 수립 및 상충 시 Permissive 계열 모듈로 교체 |
| AI 코딩 도구(GitHub Copilot 등)에 의한 저작권 침해 코드 무단 유입 | AI 코드 생성 시 공개 오픈소스 매칭 필터링 활성화 및 코드 출처 검증 |

## Ⅵ. 제언

CI/CD 파이프라인과 연동된 오픈소스 거버넌스 자동화 및 표준 SBOM 공급망 보안 확립

### 오픈소스 거버넌스 CI/CD 자동화 파이프라인

```text
개발자: 패키지 의존성 추가 후 Git PR 생성
    ↓
SCA 분석 엔진 (Black Duck / Snyk / Sonatype):
    ├─ 컴포넌트 라이선스 식별
    ├─ 알려진 취약점(CVE) 탐지
    └─ 라이선스 허용 정책(Whitelisting) 대조
    ↓
품질 게이트 판정
    ├─ AGPL/GPL 등 금지 라이선스 탐지 시 → 빌드 실패 및 머지 자동 차단
    └─ 허용 라이선스(MIT/Apache) 확인 시 → 머지 승인
    ↓
배포 빌드 시 SPDX/CycloneDX 표준 SBOM 자동 생성 및 릴리스 아티팩트 보관
```

### 오픈소스 고지문 자동 발행 체계

```text
릴리스 태그 생성
    ↓
SBOM 데이터 추출 및 사용된 모든 오픈소스 라이선스 전문 집계
    ↓
법적 고지문(NOTICE.txt) 자동 생성 후 설치 바이너리 및 웹 포털 탑재
```

### 선택 근거: 수작업 컴플라이언스와 자동화 SCA 거버넌스 비교

| 구분 | 수작업 엑셀 관리 | 제언: CI/CD 연동 자동화 거버넌스 |
|---|---|---|
| 탐지 누락 | 간접 의존성(Transitive Dependency) 식별 불가 | 딥 스캔으로 수천 개 하위 종속성 전수 탐지 |
| 리스크 통제 | 배포 직전 사후 적발로 릴리스 지연 초래 | 코드 커밋 시점 즉각 차단으로 법적 리스크 제로화 |
| 공급망 보안 | 최근 정부/글로벌 SBOM 제출 의무화 대응 불가 | 표준 SPDX/CycloneDX 포맷 자동 생성 대응 |

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 3교시: 일부 오픈소스 라이선스 정책 변경의 배경과 산업 영향
- 제140회 정보관리기술사 2교시: AI 생성 코드·오픈웨이트 모델의 오픈소스 라이선스 위험과 컴플라이언스 점검
- Open Source Initiative, The Open Source Definition (OSD)
- Free Software Foundation, Frequently Asked Questions about the GNU Licenses
- ISO/IEC 5230:2020 Information technology — OpenChain specification (Open Source Compliance)

## 연결 토픽

- 이전 토픽: [기술 부채](./016_technical_debt.md)
- 연관 토픽: [오픈소스 거버넌스](./112_open_source.md), [형상관리](./011_configuration_management.md)
- 다음 토픽: [UML 다이어그램 체계](./020_uml_diagrams.md)
