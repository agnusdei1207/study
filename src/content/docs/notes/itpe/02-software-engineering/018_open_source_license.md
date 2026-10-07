---
title: "오픈소스 라이선스(Permissive·Copyleft)와 Source-Available 라이선스"
author: "Antigravity"
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

## Ⅰ. 오픈소스 라이선스 체계의 개요

- 개념 : **오픈소스 소프트웨어** (OSS, Open Source Software)의 저작권자가 사용자에게 소스코드의 복제, 수정, 배포 권한을 허용하면서 준수해야 할 조건(저작권 고지, **소스코드 공개 의무** 등)을 명시한 법적 계약.
- 배경 및 필요성 : 전 세계 소프트웨어의 대부분이 오픈소스를 기반으로 개발되고 있으나, 라이선스 위반 시 저작권 침해 소송, 제품 판매 금지 가처분, 기업 독점 소스코드의 **강제 공개** 위험 직면.
- 주요 3대 분류 : **허용적** (Permissive), **카피레프트** (Copyleft), **소스 공개 비-오픈소스** (Source-Available).

## Ⅱ. 오픈소스 라이선스 스펙트럼 및 의무사항 구조

```text
   [ 허용적 (Permissive) ] ──────> [ 약한 카피레프트 ] ──────> [ 강한 카피레프트 ] ──────> [ 네트워크 카피레프트 ]
      MIT, Apache 2.0                 LGPL, MPL                  GPL v2/v3                  AGPL v3
   - 소스코드 공개 의무 없음       - 해당 라이브러리 수정 시   - 결합된 전체 파생 저작물    - 네트워크 서비스(SaaS)로
   - 저작권 고지만 유지             수정분만 소스 공개          전체 소스코드 의무 공개      제공해도 전체 소스 공개
```

- **Source-Available (BSL, SSPL)** : 소스코드는 누구나 볼 수 있으나, 클라우드 제공업체가 이를 상용 매니지드 서비스로 재판매하는 것을 금지하는 라이선스 (Redis, MongoDB, Elastic 전환 사례).

## Ⅲ. 주요 오픈소스 라이선스별 의무사항 비교

| 라이선스 | 구분 | 소스코드 공개 의무 범위 | 특허 조항 | 대표 프로젝트 |
|---|---|---|---|---|
| **MIT** | Permissive | 없음 (저작권 및 허가 고지만 표시) | 명시적 특허 조항 없음 | React, Vue.js, Node.js |
| **Apache 2.0** | Permissive | 없음 (저작권 고지 및 변경사항 표시) | 명시적 특허 라이선스 부여 및 특허 분쟁 방지 | Kubernetes, Kafka, Spark |
| **LGPL v3** | Weak Copyleft | LGPL 모듈 자체를 수정한 경우만 공개 (동적 링킹 시 메인 소스 비공개) | 특허 라이선스 포함 | FFmpeg, 7-Zip |
| **GPL(GNU General Public License) v3** | Strong Copyleft | 정적/동적 링킹된 전체 애플리케이션 소스코드 공개 의무 (전염성) | 특허 라이선스 포함 | Linux 커널, Git |
| **AGPL(GNU Affero General Public License) v3** | Network Copyleft | 네트워크를 통해 서비스(SaaS) 형태로 제공 시에도 전체 소스 공개 | 특허 라이선스 포함 | Grafana, Mastodon |
| SSPL / BSL | Source-Available | 경쟁 클라우드 호스팅 서비스 제공 시 제한 (OSI(Open Source Initiative) 인증 오픈소스 아님) | 각 사별 상이 | MongoDB, Redis(일부) |

## Ⅳ. 오픈소스 라이선스 관리의 주요 한계점 및 해결 방안

- 카피레프트(GPL/AGPL) 라이선스의 전염성(Viral Effect)으로 인한 소스코드 공개 위험 :
  - 한계점 : GPL이나 네트워크 전염성을 가진 AGPL 라이선스 소프트웨어를 연계·통합할 경우 기업의 독점적(Proprietary) 핵심 비즈니스 로직과 알고리즘 소스코드 전체를 강제 공개해야 하는 법적 리스크 발생.
  - 해결 방안 : 상용 서비스에는 Permissive(MIT, Apache 2.0) 라이선스 우선 채택 원칙을 수립하고, 부득이한 GPL/AGPL 컴포넌트는 REST(Representational State Transfer)/gRPC 기반 별도 독립 프로세스로 분리 격리하여 법적 파급 차단.
- 전이적 의존성(Transitive Dependency) 속 고위험 라이선스 오염 사각지대 :
  - 한계점 : 직접 선언한 최상위 라이선스는 안전하더라도 빌드 시 다운로드되는 수백 개의 3~4차 하위 라이선스 중 비표준/고위험 라이선스가 침투하여 감지되지 않는 문제.
  - 해결 방안 : CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인에 SBOM(SPDX, CycloneDX) 자동 생성 및 SCA(Software Composition Analysis) 도구(FOSSA, Snyk, Mend)를 연동하여 허용되지 않은 라이선스 유입 시 빌드 자동 차단.
- Source-Available(BSL, SSPL) 전환에 따른 상용 서비스 라이선스 분쟁 :
  - 한계점 : Redis, Elastic, Terraform 등 주요 오픈소스 프로젝트가 클라우드 벤더 견제를 위해 상용 서비스 제공을 금지하는 Source-Available 라이선스로 전환함에 따라 기존 사용 시스템의 라이선스 침해 리스크 급증.
  - 해결 방안 : 전사 오픈소스 거버넌스 위원회를 통해 주요 의존성 패키지의 라이선스 변경을 지속 모니터링하고, 완전 오픈소스 포크 프로젝트(Valkey, OpenSearch, OpenTofu 등)로의 신속한 대체 마이그레이션 전략 수립.

## Ⅴ. 기업 오픈소스 거버넌스를 위한 기술사적 제언

- 소프트웨어 자재명세서(SBOM) 및 SCA 도구 파이프라인 연계 : CycloneDX, SPDX(Software Package Data Exchange) 표준 기반의 SBOM을 빌드 시 자동 생성하고, Black Duck, Mend, Snyk 등 소프트웨어 구성 분석(SCA) 도구를 CI 파이프라인에 탑재하여 카피레프트 전염 방지.
- 사내 오픈소스 컴플라이언스(OSPO, Open Source Program Office) 조직 구축 : 오픈소스 도입 심의, 사내 IP(Intellectual Property) 보호를 위한 링킹(Dynamic vs Static) 아키텍처 가이드라인 수립 및 정기 감사 프로세스 정착.
