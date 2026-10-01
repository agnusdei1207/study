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

- **개념** : 오픈소스 소프트웨어(OSS)의 저작권자가 사용자에게 소스코드의 복제, 수정, 배포 권한을 허용하면서 준수해야 할 조건(저작권 고지, 소스코드 공개 의무 등)을 명시한 법적 계약.
- **배경 및 필요성** : 전 세계 소프트웨어의 80% 이상이 오픈소스를 기반으로 개발되고 있으나, 라이선스 위반 시 저작권 침해 소송, 제품 판매 금지 가처분, 기업 독점 소스코드의 강제 공개 위험 직면.
- **주요 3대 분류** : 허용적(Permissive), 카피레프트(Copyleft), 소스 공개 비-오픈소스(Source-Available).

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
| MIT | Permissive | 없음 (저작권 및 허가 고지만 표시) | 명시적 특허 조항 없음 | React, Vue.js, Node.js |
| Apache 2.0 | Permissive | 없음 (저작권 고지 및 변경사항 표시) | 명시적 특허 라이선스 부여 및 특허 분쟁 방지 | Kubernetes, Kafka, Spark |
| LGPL v3 | Weak Copyleft | LGPL 모듈 자체를 수정한 경우만 공개 (동적 링킹 시 메인 소스 비공개) | 특허 라이선스 포함 | FFmpeg, 7-Zip |
| GPL v3 | Strong Copyleft | 정적/동적 링킹된 전체 애플리케이션 소스코드 공개 의무 (전염성) | 특허 라이선스 포함 | Linux 커널, Git |
| AGPL v3 | Network Copyleft | 네트워크를 통해 서비스(SaaS) 형태로 제공 시에도 전체 소스 공개 | 특허 라이선스 포함 | Grafana, Mastodon |
| SSPL / BSL | Source-Available | 경쟁 클라우드 호스팅 서비스 제공 시 제한 (OSI 인증 오픈소스 아님) | 각 사별 상이 | MongoDB, Redis(일부) |

## Ⅳ. 기업 오픈소스 거버넌스를 위한 기술사적 제언

- **소프트웨어 자재명세서(SBOM) 및 SCA 도구 파이프라인 연계** : CycloneDX, SPDX 표준 기반의 SBOM을 빌드 시 자동 생성하고, Black Duck, Mend, Snyk 등 소프트웨어 구성 분석(SCA) 도구를 CI 파이프라인에 탑재하여 카피레프트 전염 방지.
- **사내 오픈소스 컴플라이언스(OSPO) 조직 구축** : 오픈소스 도입 심의, 사내 IP 보호를 위한 링킹(Dynamic vs Static) 아키텍처 가이드라인 수립 및 정기 감사 프로세스 정착.
