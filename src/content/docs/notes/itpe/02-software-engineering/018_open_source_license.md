---
title: "오픈소스 라이선스(Permissive·Copyleft)와 Source-Available 라이선스"
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

- 오픈소스 라이선스, 허용적(Permissive), 카피레프트(Copyleft), Source-Available
- GPL(GNU General Public License), AGPL, LGPL, SBOM(Software Bill of Materials), SCA(Software Composition Analysis), OSPO(Open Source Program Office)

## Ⅰ. 오픈소스 라이선스 체계의 개요

- 핵심 요약 : 소스코드의 복제·수정·배포 권한을 허용하면서 준수 조건을 명시하는 법적 계약.
- 개념 : 오픈소스 소프트웨어(OSS, Open Source Software)의 저작권자가 사용자에게 소스코드의 복제, 수정, 배포 권한을 허용하면서 준수해야 할 조건(저작권 고지, 소스코드 공개 의무 등)을 명시한 법적 계약.
- 배경 및 필요성 : 전 세계 소프트웨어의 대부분이 오픈소스를 기반으로 개발되고 있으나, 라이선스 위반 시 저작권 침해 소송, 제품 판매 금지 가처분, 기업 독점 소스코드의 강제 공개 위험 직면.
- 주요 목적 : 라이선스 조건의 사전 검증과 체계적 준수를 통한 법적 리스크 차단.
- 3대 분류 : 허용적(Permissive), 카피레프트(Copyleft), 소스 공개 비-오픈소스(Source-Available).

## Ⅱ. 오픈소스 라이선스의 특징

- 핵심 요약 : 조건 강도의 스펙트럼 구조와 카피레프트 계열의 전염성이 특징.
1. 허용적(Permissive) : MIT, Apache 2.0 — 소스 공개 의무 부재, 저작권 고지만 유지.
2. 약한 카피레프트(Weak Copyleft) : LGPL(GNU Lesser General Public License), MPL(Mozilla Public License) — 해당 라이브러리 수정분만 소스 공개.
3. 강한 카피레프트(Strong Copyleft) : GPL(GNU General Public License) v2/v3 — 결합 전체 파생 저작물의 소스 공개 의무.
4. 네트워크 카피레프트(Network Copyleft) : AGPL(GNU Affero General Public License) v3 — 네트워크 서비스 제공에도 전체 소스 공개.
5. 전염성(Viral Effect) : 카피레프트 계열 라이선스의 파생 저작물로의 소스 공개 의무 전파.
6. 특허 조항 차등 : Apache 2.0의 명시적 특허 라이선스 부여 및 특허 분쟁 방지 조항, MIT의 명시적 특허 조항 부재.
7. Source-Available(소스 공개형) : BSL(Business Source License), SSPL(Server Side Public License) — 소스코드는 공개되나 OSI(Open Source Initiative) 인증 오픈소스가 아니며 클라우드 제공업체의 상용 매니지드 서비스 재판매 금지.

## Ⅲ. 오픈소스 라이선스의 구조 (흐름)

- 핵심 요약 : 조건 강도별 라이선스 스펙트럼과 도입 심의→SBOM→SCA→감사의 관리 프로세스.

```text
[ 라이선스 스펙트럼 (조건 강화 방향) ]
[ 허용적(Permissive) ]
   MIT, Apache 2.0
   소스 공개 의무 없음, 저작권 고지만 유지
      │ 라이선스 조건 강화
      ▼
[ 약한 카피레프트 ]
   LGPL, MPL
   해당 라이브러리 수정분만 소스 공개
      │
      ▼
[ 강한 카피레프트 ]
   GPL v2/v3
   결합 전체 파생 저작물 소스 공개 의무
      │
      ▼
[ 네트워크 카피레프트 ]
   AGPL v3
   네트워크 서비스 제공에도 전체 소스 공개
```

```text
[ 오픈소스 관리 프로세스 ]
도입 심의 (라이선스 조건 검토)
      ↓
SBOM 자동 생성 (SPDX/CycloneDX 형식)
      ↓
SCA 검사 (고위험 라이선스 탐지)
      ↓
빌드 차단 (허용되지 않은 라이선스 유입 시)
      ↓
정기 감사 (라이선스 변경 모니터링)
```

- Source-Available 사례 : Redis, MongoDB, Elastic 등이 클라우드 벤더 견제를 위해 해당 라이선스로 전환.

## Ⅳ. 주요 오픈소스 라이선스별 의무사항의 비교

- 핵심 요약 : 공개 의무 범위와 특허 조항의 유무가 라이선스 선택의 핵심 기준.

| 라이선스 | 구분 | 소스코드 공개 의무 범위 | 특허 조항 | 대표 프로젝트 |
|---|---|---|---|---|
| MIT | Permissive | 없음 (저작권 및 허가 고지만 표시) | 명시적 특허 조항 부재 | React, Vue.js, Node.js |
| Apache 2.0 | Permissive | 없음 (저작권 고지 및 변경사항 표시) | 명시적 특허 라이선스 부여 및 특허 분쟁 방지 | Kubernetes, Kafka, Spark |
| LGPL v3 | Weak Copyleft | LGPL 모듈 자체를 수정한 경우만 공개 (동적 링킹 시 메인 소스 비공개) | 특허 라이선스 포함 | FFmpeg, 7-Zip |
| GPL v3 | Strong Copyleft | 정적/동적 링킹된 전체 애플리케이션 소스코드 공개 의무 (전염성) | 특허 라이선스 포함 | Linux 커널, Git |
| AGPL v3 | Network Copyleft | 네트워크를 통해 서비스(SaaS, Software as a Service) 형태로 제공 시에도 전체 소스 공개 | 특허 라이선스 포함 | Grafana, Mastodon |
| SSPL / BSL | Source-Available | 경쟁 클라우드 호스팅 서비스 제공 시 제한 (OSI 인증 오픈소스 아님) | 각 사별 상이 | MongoDB, Redis(일부) |

## Ⅴ. 오픈소스 라이선스 관리의 장점과 한계

- 핵심 요약 : 재사용·생태계·비용 절감의 장점, 전염성·전이적 의존성·라이선스 전환의 한계.
- 장점
  1. 소스 재사용에 따른 개발 비용 절감 및 개발 생산성 향상.
  2. 검증된 커뮤니티 생태계를 통한 상호운용성 및 표준 준수.
  3. 특정 벤더 종속(Vendor Lock-in)의 회피.
- 한계점 1 : 카피레프트(GPL/AGPL) 라이선스의 전염성(Viral Effect)으로 인한 소스코드 공개 위험
  - 한계점 : GPL이나 네트워크 전염성을 가진 AGPL 라이선스 소프트웨어를 연계·통합할 경우 기업의 독점적(Proprietary) 핵심 비즈니스 로직과 알고리즘 소스코드 전체의 강제 공개 법적 리스크 발생.
  - 해결 방안 : 상용 서비스의 Permissive(MIT, Apache 2.0) 라이선스 우선 채택 원칙 수립, 부득이한 GPL/AGPL 컴포넌트의 REST(Representational State Transfer)/gRPC 기반 별도 독립 프로세스 분리 격리를 통한 법적 파급 차단.
- 한계점 2 : 전이적 의존성(Transitive Dependency) 속 고위험 라이선스 오염 사각지대
  - 한계점 : 직접 선언한 최상위 라이선스는 안전하더라도 빌드 시 다운로드되는 수백 개의 3~4차 하위 라이선스 중 비표준/고위험 라이선스가 침투하여 감지되지 않는 문제.
  - 해결 방안 : CI/CD(Continuous Integration/Continuous Delivery) 파이프라인의 SPDX·CycloneDX 형식 SBOM 자동 생성 및 SCA 도구(FOSSA, Snyk, Mend) 연동을 통한 허용되지 않은 라이선스 유입 시 빌드 자동 차단.
- 한계점 3 : Source-Available(BSL, SSPL) 전환에 따른 상용 서비스 라이선스 분쟁
  - 한계점 : Redis, Elastic, Terraform 등 주요 오픈소스 프로젝트의 클라우드 벤더 견제 목적 Source-Available 라이선스 전환에 따라 기존 사용 시스템의 라이선스 침해 리스크 급증.
  - 해결 방안 : 전사 오픈소스 거버넌스 위원회의 주요 의존성 패키지 라이선스 변경 지속 모니터링, 완전 오픈소스 포크 프로젝트(Valkey, OpenSearch, OpenTofu 등)로의 신속한 대체 마이그레이션 전략 수립.

## Ⅵ. 기업 오픈소스 거버넌스를 위한 기술사적 제언

- 핵심 요약 : SBOM·SCA 파이프라인 연계와 전담 조직(OSPO) 구축.
- 소프트웨어 자재명세서(SBOM) 및 SCA 도구 파이프라인 연계 : CycloneDX, SPDX(Software Package Data Exchange) 표준 기반의 SBOM을 빌드 시 자동 생성하고, Black Duck, Mend, Snyk 등 소프트웨어 구성 분석(SCA) 도구를 CI 파이프라인에 탑재하여 카피레프트 전염 방지.
- 오픈소스 전담 조직(OSPO, Open Source Program Office) 구축 : 오픈소스 도입 심의, 사내 IP(Intellectual Property) 보호를 위한 링킹(Dynamic vs Static) 아키텍처 가이드라인 수립 및 정기 감사 프로세스 정착.
- 라이선스 변경 모니터링 체계 : 주요 의존성 패키지의 라이선스 전환 조짐에 대한 조기 경보 및 포크 프로젝트 대체 전략의 사전 준비.

## Ⅶ. 결론

- 핵심 요약 : 오픈소스 라이선스 관리는 법적 리스크 차단을 위한 조직적 거버넌스의 문제.
- 요약 : Permissive 우선 원칙, 전염성 격리, SBOM/SCA 자동 검사의 3층 방어 체계 구축.
- 시사점 : Source-Available 전환 추세를 반영한 지속 모니터링과 OSPO 기반의 전사 거버넌스 정착 필요.
