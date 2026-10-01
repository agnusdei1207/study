---
title: "SBOM(Software Bill of Materials)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. SBOM(Software Bill of Materials)의 개요

- **개념** : 소프트웨어를 구성하는 모든 오픈소스 라이브러리, 상용 컴포넌트, 종속성 모듈, 라이선스, 버전 정보 및 패치 이력을 기계 판독 가능한 표준 형식으로 명세화한 소프트웨어 자재명세서.
- **배경 및 필요성** : SolarWinds, Log4j(Log4Shell), XZ Utils 백도어 등 소프트웨어 공급망(Supply Chain)을 노린 침해사고가 급증함에 따라, 미 행정명령(EO 14028) 및 국내 SW 공급망 가이드라인을 통해 SBOM 제출이 의무화되는 추세.
- **핵심 목적** : SW 공급망 전주기 투명성(Transparency) 확보, 컴포넌트 내 잠재 취약점(CVE)의 신속한 추적 및 식별, 오픈소스 라이선스 위반 법적 리스크 방지.

## Ⅱ. SBOM(Software Bill of Materials)의 핵심 아키텍처 및 동작 메커니즘

SBOM은 소프트웨어 빌드 및 배포 파이프라인에서 자동으로 생성(Generate)되며, 취약점 데이터베이스와 매핑(Analyze)된 후 취약성 악용 가능성 정보(VEX)와 함께 지속 관리(Operate)됨.

```text
[ CI/CD 파이프라인 연계 SBOM 생성 및 수명주기 관리 ]

  [ 개발자 커밋 ] -> [ CI/CD 파이프라인 빌드 (GitHub Actions, GitLab CI) ]
                               │
                               ▼ 1. 빌드 도구 플러그인 분석
  +-------------------------------------------------------------+
  | SBOM 자동 생성 엔진 (Syft, Trivy, cdxgen)                   |
  |  - 직접/간접 종속성 추적, 해시 무결성 검증, 메타데이터 추출 |
  +------------------------------┬------------------------------+
                                 │ 2. 표준 형식 출력 (SPDX / CycloneDX)
                                 ▼
  +-------------------------------------------------------------+
  | SBOM 저장소 및 취약점 분석 엔진 (Dependency-Track)          |
  |  - NVD / OSV / GitHub Advisory 실시간 CVE 매핑              |
  |  - VEX(Vulnerability Exploitability eXchange) 판별          |
  +------------------------------┬------------------------------+
                                 │ 3. 배포 차단 및 정책 집행
                                 ▼
  [ 런타임 클라우드 배포 (Kubernetes) ] -> [ 런타임 공급망 드리프트 감시 ]
```

- **컴포넌트 식별(Component Identification)** : 패키지 URL(purl) 및 CPE(Common Platform Enumeration)를 사용하여 SW 부품의 명칭, 버전, 제조사, 해시값 식별.
- **종속성 관계 그래프(Dependency Graph)** : 1차 직접 의존성뿐 아니라 2차, N차 전이적 종속성(Transitive Dependencies) 관계를 계층 트리로 구성.
- **표준 포맷 직렬화** : SPDX(ISO/IEC 5962 표준) 또는 CycloneDX(OWASP 주도 클라우드 네이티브 표준) 기반의 JSON/XML 형식으로 출력.
- **VEX(취약점 악용 정보) 연계** : CVE가 포함된 모듈이라도 실제 실행 경로에서 호출되지 않아 취약하지 않음을 증명(not_affected)하는 VEX 문서 결합 관리.

## Ⅲ. SBOM(Software Bill of Materials)의 세부 구성 요소 및 비교 분석

| 비교 항목 | SPDX (Software Package Data Exchange) | CycloneDX | SWID 태그 (Software Identification) |
| --- | --- | --- | --- |
| 주도 기구 | Linux Foundation / ISO (ISO/IEC 5962) | OWASP Foundation | ISO/IEC 19770-2 / NIST |
| 설계 초점 | 오픈소스 라이선스 규정 준수 및 IP 보호 | 애플리케이션 보안, SBOM/VEX/SaaS BOM | 설치된 소프트웨어 자산 인벤토리 식별 |
| 지원 데이터 형식 | JSON, YAML, RDF, XML, Tag-Value | JSON, XML, Protocol Buffers | XML |
| 강점 영역 | 국제 표준 호환성, 엄밀한 라이선스 모델 | 보안 취약점 연동(VEX), CI/CD 자동화 용이 | OS 수준 엔드포인트 소프트웨어 자산 관리 |
| 확장성 | 하드웨어 BOM, AI BOM 확장 추진 | OBOM, SaaS BOM, ML/AI BOM 선제 지원 | 확장 제한적 |

- SPDX는 라이선스 감사 및 국제 표준 규격으로서 법적 컴플라이언스에 적합하며, CycloneDX는 최신 데브옵스 보안 취약점 추적과 VEX 지원에 특화되어 상호 목적에 맞춰 선택됨.

## Ⅳ. SBOM(Software Bill of Materials)의 주요 한계점 및 해결 방안

- **동적 런타임 종속성 및 C/C++ 정적 빌드 컴포넌트 누락 위험** :
  - **한계점** : 소스코드 패키지 매니저(Maven, npm)만 분석할 경우 런타임 플러그인 로딩이나 C/C++ 정적 링크 라이브러리가 SBOM 생성에서 누락되는 'BOM 블라인드 스팟' 발생.
  - **해결 방안** : 소스 정적 분석과 함께 바이너리 역공학 스캐닝(Binary SCA) 및 eBPF 기반 런타임 동적 프로세스 로딩 추적을 결합하여 하이브리드 SBOM 추출.
- **취약점 알림 폭증(False Positive)과 보안 피로도(Alert Fatigue)** :
  - **한계점** : SBOM 분석 결과 수백 개의 CVE가 식별되지만 실제 코드에서 사용되지 않는 불감 취약점(Unreachable Code)으로 인해 개발자의 패치 업무 마비.
  - **해결 방안** : VEX(Vulnerability Exploitability eXchange) 프레임워크를 의무화하여 도달 가능성 분석(Call Graph Reachability Analysis)을 통해 실제 침해 가능한 취약점만 우선 조치.
- **SBOM 자체의 위변조 및 공급망 역공격 위험** :
  - **한계점** : 공격자가 빌드 파이프라인을 해킹하여 악성코드를 삽입한 후 SBOM 문서는 정상 라이브러리만 기재하여 검증을 우회하는 위변조 위협 존재.
  - **해결 방안** : Sigstore(Cosign) 및 In-Toto 프레임워크를 파이프라인에 통합하여 SBOM 파일에 개발사 디지털 서명을 부여하고, 불변 렛저(Rekor)에 투명성 로그 기록.

## Ⅴ. SBOM(Software Bill of Materials) 적용 및 발전을 위한 기술사적 제언

- **공공·금융 SW 조달 시 SBOM 제출 의무화 및 수용 기준 수립** : 제안요청서(RFP)에 최소 SBOM 생성 표준(CycloneDX/SPDX)과 취약점 임계치(Critical 0건)를 명시해야 함.
- **전사 통합 SCA 및 SBOM 거버넌스 플랫폼 구축** : 개별 프로젝트별 파편화된 SBOM 관리를 지양하고 중앙 리포지토리를 통해 전사 공통 컴포넌트의 제로데이 취약점 발생 시 1시간 내 영향도 파악 체계 구축.
- **AI 모델 자재명세서(AIBOM)로의 영역 확장** : LLM 및 머신러닝 파이프라인 확장에 대응하여 모델 가중치, 학습 데이터셋, 파인튜닝 기법을 명세화하는 AIBOM 관리 체계를 선제 도입해야 함.
