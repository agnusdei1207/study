---
title: "SBOM(Software Bill of Materials)"
author: "agnusdei1207"
date: "2026-10-24T22:51:45+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- SBOM(Software Bill of Materials), 소프트웨어 공급망(Supply Chain), CVE(Common Vulnerabilities and Exposures), VEX(Vulnerability Exploitability eXchange)
- SPDX(Software Package Data Exchange), CycloneDX, SWID 태그(Software Identification), purl, CPE(Common Platform Enumeration)
- SCA(Software Composition Analysis), Binary SCA, 도달 가능성 분석(Reachability Analysis), Sigstore, In-Toto, AIBOM(AI Bill of Materials)

## Ⅰ. SBOM(Software Bill of Materials)의 개요

- 핵심 요약 : 빌드에 포함된 구성 요소와 버전, 라이선스를 기계 판독 가능한 목록으로 명세해 공급망의 투명성을 확보하는 문서.
- 개념 : 소프트웨어를 이루는 오픈소스 라이브러리, 상용 컴포넌트, 종속 모듈, 라이선스, 버전 정보를 표준 형식으로 적은 **소프트웨어 자재명세서** (SBOM, Software Bill of Materials).
- 배경 및 필요성 : SolarWinds 사고, Log4j 취약점(Log4Shell), XZ Utils 백도어 사건처럼 **소프트웨어 공급망** (Supply Chain, 외부 구성 요소와 빌드·배포 과정 전체)을 노린 침해가 잇따르면서, 미국 행정명령 EO 14028이 연방 조달 소프트웨어에 SBOM 제출을 요구하는 등 제출 의무화 흐름이 확산됨.
- 주요 목적 : 공급망 전 과정의 투명성 확보, 구성 요소 안의 **CVE** (Common Vulnerabilities and Exposures, 공개된 취약점 식별자)를 신속히 추적, 오픈소스 라이선스 위반 리스크 방지.

## Ⅱ. SBOM(Software Bill of Materials)의 특징 및 장점

- 핵심 요약 : 자동 생성되는 기계 판독형 명세가 취약점 매핑과 실제 악용 가능성 판단으로 이어져 대응 정밀도를 높이는 구조.

1. 자동 생성 : 빌드 파이프라인에서 종속성을 추적해 명세를 만듦 → 수작업 누락을 줄이고 최신 상태 유지.
2. 전이적 종속성 기록 : 직접 의존뿐 아니라 2차, N차 전이적 종속성까지 계층 그래프로 기록 → 간접 포함된 취약점까지 식별.
3. 표준 형식 직렬화 : **SPDX** (ISO/IEC 5962 국제 표준)나 **CycloneDX** (OWASP 주도 표준)의 JSON·XML로 출력 → 도구 사이에서 교환 가능.
4. **VEX** (Vulnerability Exploitability eXchange, 취약점의 실제 악용 가능성 정보) : 포함된 CVE가 실행 경로에서 호출되지 않아 영향이 없음(not_affected)을 문서로 증명 → 불필요한 패치 부담 감소.

## Ⅲ. SBOM(Software Bill of Materials)의 구조 (흐름)

- 핵심 요약 : SBOM은 빌드 단계에서 생성되고, 취약점 정보와 매핑된 뒤 배포 정책과 런타임 감시로 이어지는 수명주기.
- 컴포넌트 식별 : purl(Package URL)과 **CPE** (Common Platform Enumeration, 제품 명명 체계)를 사용해 부품의 명칭, 버전, 제조사, 해시값을 식별.
- 종속성 관계 그래프 : 1차 의존성과 전이적 의존성을 계층 트리로 구성해 취약 부품의 경로를 역추적.

```text
[ 빌드 파이프라인 연계 SBOM 수명주기 ]

빌드 파이프라인 (커밋 → 빌드)
   ↓ 1. SBOM 자동 생성
생성 도구 (Syft, Trivy, cdxgen)
   ↓ 2. SPDX·CycloneDX 출력
SBOM 저장소·분석 (Dependency-Track)
   ↓ 3. CVE 매핑 + VEX 판별
배포 정책 집행 (차단·허용)
   ↓
런타임 감시 (구성 드리프트 탐지)
```

## Ⅳ. SBOM(Software Bill of Materials)의 비교

- 핵심 요약 : SPDX는 라이선스 준수에, CycloneDX는 취약점 추적과 VEX 연계에 강점이 있어 목적에 따라 선택.

| 비교 항목 | SPDX (Software Package Data Exchange) | CycloneDX | SWID 태그 (Software Identification) |
| --- | --- | --- | --- |
| 주도 기구 | Linux Foundation, ISO/IEC 5962 | OWASP Foundation | ISO/IEC 19770-2 |
| 설계 초점 | 오픈소스 라이선스 준수와 IP(Intellectual Property) 관리 | 애플리케이션 보안, VEX 연계 | 설치된 소프트웨어 자산 인벤토리 식별 |
| 데이터 형식 | JSON, YAML, RDF, XML, 태그-값 | JSON, XML, Protocol Buffers | XML |
| 강점 영역 | 국제 표준 호환성, 엄밀한 라이선스 모델 | 취약점 연동, CI(Continuous Integration)/CD(Continuous Delivery) 자동화 | 엔드포인트 소프트웨어 자산 관리 |
| 확장 방향 | 하드웨어·AI 등 프로파일 확장 | OBOM, SaaSBOM, ML-BOM 등 선제 지원 | 확장 범위 제한적 |

- SPDX는 라이선스 감사와 법적 준수에 적합하고, CycloneDX는 데브옵스 파이프라인의 취약점 추적과 VEX 관리에 적합하므로, 두 표준은 목적에 따라 선택하거나 병행함.

## Ⅴ. SBOM(Software Bill of Materials)의 한계와 방안

- 핵심 요약 : 명세 누락, 경보 과다, 명세 위변조라는 세 한계를 하이브리드 추출, 도달 가능성 분석, 서명 체계로 각각 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 런타임 종속성과 정적 링크 누락 | 소스 패키지 매니저만 분석하면 런타임 플러그인과 C/C++ 정적 링크 라이브러리가 빠져 BOM 블라인드 스팟 발생 | 소스 분석과 **Binary SCA** (Software Composition Analysis, 바이너리 기반 구성 요소 식별) 병행, eBPF(extended Berkeley Packet Filter) 기반 런타임 로딩 추적 | 런타임 대비 명세 누락률 |
| 취약점 알림 과다 (Alert Fatigue) | 식별된 CVE 중 실제 호출되지 않는 취약점이 많아 개발자의 패치 업무가 마비 | VEX 문서화와 **도달 가능성 분석** (Call Graph Reachability Analysis, 호출 그래프로 취약 함수 도달 여부 판정) | 실제 악용 가능 취약점 비율, 패치 소요 시간 |
| SBOM 자체의 위변조 | 빌드 파이프라인에 악성코드가 들어가도 SBOM에는 정상 구성만 기재되면 검증을 우회 | Sigstore(Cosign)로 개발사 서명, In-Toto로 공급망 단계 증명, 투명성 로그(Rekor) 기록 | 서명 검증 실패 건수 |

## Ⅵ. SBOM(Software Bill of Materials)에 대한 기술사적 제언

- 핵심 요약 : 조달 기준, 전사 관리 체계, AI 자재 확장을 묶어 SBOM을 일회성 제출물이 아닌 상시 관리 자산으로 운영하는 방향.

1. 공공과 금융의 SW 조달 제안요청서(RFP)에 SBOM 생성 표준(SPDX 또는 CycloneDX)과 취약점 조치 기준을 명시하여 공급사의 제출 책임을 분명히 하는 것이 필요.
2. 프로젝트별로 흩어진 명세를 전사 중앙 저장소로 모으고 SCA 체계를 두어, 공통 컴포넌트에 취약점이 공개되면 영향 범위를 신속히 파악할 수 있는 거버넌스를 구축하는 것이 필요.
3. LLM과 머신러닝 파이프라인이 늘어나는 흐름에 맞춰 모델 가중치, 학습 데이터셋, 파인튜닝 이력을 명세하는 **AIBOM** (AI Bill of Materials, AI 자재명세서) 관리 체계를 선제적으로 도입하는 것이 필요.

## Ⅶ. 결론

- 핵심 요약 : SBOM은 소프트웨어 자재를 기계 판독 가능한 명세로 드러내 공급망 대응의 기초 자료가 되는 문서.
- 시사점 : 명세의 정확성은 생성 범위와 검증 체계에 달려 있으므로, 서명과 VEX가 함께 운영되어야 신뢰를 확보할 수 있음.
