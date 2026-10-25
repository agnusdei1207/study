---
title: "오픈소스 소프트웨어(OSS, Open Source Software) 및 거버넌스"
description: "OSPO·SBOM·SCA·VEX, 라이선스·공급망·기여 3대 영역, 카피레프트·공급망 공격·유지보수 중단 한계와 방안"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- 오픈소스 소프트웨어(OSS, Open Source Software), OSPO(Open Source Program Office), SBOM(Software Bill of Materials)
- SCA(Software Composition Analysis), 라이선스 컴플라이언스(License Compliance), 공급망 보안(Supply Chain Security), VEX(Vulnerability Exploitability eXchange)

## Ⅰ. 오픈소스 소프트웨어(OSS) 및 거버넌스의 개요

- 핵심 요약 : 기업이 오픈소스를 안전하게 도입하도록 라이선스, 보안, 기여 문화를 전사적으로 통제하는 관리 체계.
- 개념 : 누구나 사용, 수정, 재배포할 수 있는 **오픈소스 소프트웨어** (OSS, Open Source Software)를 기업 시스템에 안전하게 도입하도록 라이선스 준수, 취약점 관리, 사내 기여를 통제하는 체계.
- 배경 및 필요성 : 현대 소프트웨어 대부분이 오픈소스 라이브러리로 조립되지만, 카피레프트 라이선스의 전염 효과와 Log4j 사태 같은 공급망 취약점에 노출됨.
- 주요 목적 : 라이선스 법적 위험 예방, 공급망 보안 강화, 오픈소스 기여를 통한 조직 역량 확보.

## Ⅱ. 오픈소스 거버넌스의 특징 및 장점

- 핵심 요약 : 라이선스 컴플라이언스, 공급망 보안, 기여 문화의 세 축을 SBOM과 자동 검증으로 운영하는 체계.

1. **라이선스 컴플라이언스** (License Compliance) : GPL(GNU General Public License) 계열 카피레프트 의무를 식별하고 고지문을 생성 → 독점 코드에 소스 공개 의무가 번지는 위험 차단.
2. **공급망 보안** (Supply Chain Security) : 구성 요소의 알려진 취약점(CVE, Common Vulnerabilities and Exposures)을 NVD(National Vulnerability Database)와 매핑 → 취약한 라이브러리를 조기에 교체.
3. 기여 문화 : 이너소스(InnerSource) 확산과 외부 프로젝트 기여 → 개발 협업과 기술 신뢰도 향상.
4. **SBOM** (Software Bill of Materials) 기반 가시성 : 구성 요소의 이름, 버전, 라이선스, 해시값을 명세로 생성 → 세 축 점검의 공통 데이터 제공.

## Ⅲ. 오픈소스 거버넌스의 구조 (흐름)

- 핵심 요약 : OSPO가 정책을 세우고, 라이선스 식별과 취약점 관리, 빌드 단계 검증이 이어지는 관리 흐름.
- **오픈소스 프로그램 오피스** (OSPO, Open Source Program Office) : 전사 오픈소스 정책을 세우고 법무, 보안, 개발 부서를 조율하는 전담 조직.

```text
[ OSPO : 정책 수립 · 부서 조율 ]
      ↓
[ 1. 라이선스 식별 · SBOM 생성 ]
      ↓
[ 2. 취약점 매핑 · 패치 계획 ]
      ↓
[ 3. 빌드 단계 자동 검증 · 차단 ]
```

- **소프트웨어 구성 분석** (SCA, Software Composition Analysis) : 빌드 파이프라인에서 오픈소스 구성 요소를 자동으로 식별하고 라이선스와 취약점을 판정하는 도구 계열.
- **VEX** (Vulnerability Exploitability eXchange) : 취약점이 실제 제품에서 악용 가능한지를 기록하는 문서로, SBOM과 짝을 이룸.

```text
[ SBOM 생성 및 검증 흐름 ]

[ SBOM 생성 ]
      ↓
[ 취약점(CVE) 매핑 ]
      ↓
[ 실제 호출 여부 판정 ]
      ↓
[ VEX 문서로 결과 기록 ]
      ↓ 주기적 재갱신
[ SBOM 재생성 ]
```

## Ⅳ. 오픈소스 거버넌스 3대 관리 영역 비교

- 핵심 요약 : 컴플라이언스, 공급망 보안, 기여 문화의 세 영역별 목적과 통제 활동의 차이.

| 영역 | 핵심 목적 | 주요 통제 활동 | 대표 도구 |
| --- | --- | --- | --- |
| 컴플라이언스(Legal) | 저작권 침해 방지와 라이선스 의무 준수 | 카피레프트 전염 방지, 고지문 자동 생성 | Black Duck, FOSSA, FOSSID |
| 공급망 보안(Security) | 알려진 취약점과 악성 코드 유입 차단 | 취약 라이브러리 탐지, CVSS(Common Vulnerability Scoring System) 점수 기반 우선순위 | Snyk, Mend, GitHub Dependabot |
| 기여(Culture) | 사내 개발 문화 혁신과 생태계 기여 | 이너소스 활성화, 외부 프로젝트 기여 | GitHub Enterprise, CLA(Contributor License Agreement) 관리 도구 |

- 선택 기준 : 법적 리스크가 큰 조직은 컴플라이언스 도구를, 공급망 공격 노출이 큰 조직은 보안 도구를 우선 도입.

## Ⅴ. 오픈소스 거버넌스의 한계와 방안

- 핵심 요약 : SBOM 기반 가시성과 자동 차단의 장점, 카피레프트 위반, 공급망 공격, 유지보수 중단의 한계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 카피레프트 라이선스 위반 | 소스 공개 의무가 있는 구성 요소가 독점 코드에 섞여 침해와 소송 위험 발생 | 빌드 파이프라인에 SCA 도구를 연동하고 허용 라이선스 목록 기준으로 자동 차단 | 금지 라이선스 검출 건수 |
| 공급망 공격과 취약점 | 타이포스쿼팅, 악성 코드 주입, Log4j 사태와 같은 제로데이 취약점으로 전사 침해 위험 | 검증된 사내 아티팩트 저장소 미러링, SPDX(Software Package Data Exchange)와 CycloneDX 형식의 SBOM 자동 생성 | 취약 구성 요소 조치 기간 |
| 유지보수 중단 | EOL(End of Life) 상태나 메인테이너 이탈로 긴급 패치와 최신 런타임 호환이 불가 | 정기적인 프로젝트 건강도 진단, 대체 라이브러리 교체 로드맵 수립, 상류 기여 | EOL 구성 요소 비율 |

## Ⅵ. 오픈소스 거버넌스에 대한 기술사적 제언

- 핵심 요약 : 전사 승인 체계, 납품물 표준, 기여 정책을 함께 세워 오픈소스 관리를 일회성 점검이 아닌 상시 체계로 만드는 것이 필요.
- 오픈소스 도입 전 라이선스와 보안을 점검하는 승인 절차를 오픈소스 프로그램 오피스가 주관하고, 법무와 보안 부서가 함께 허용 라이선스 기준을 제정하도록 해야 한다.
- 고객에게 전달하는 산출물에는 SBOM을 기본으로 포함하고, 실제 호출 여부를 VEX로 함께 제시하는 계약 관행을 정착시키면 고객 측 보안 검토 부담을 줄일 수 있다.
- 외부 프로젝트 기여와 이너소스 활동을 개발자 평가에 반영하고, 상용 제품에 필요한 수정 사항을 상류 프로젝트에 되돌려 보내는 기여 정책을 두어야 한다.

## Ⅶ. 결론

- 핵심 요약 : 오픈소스 거버넌스는 라이선스와 취약점을 자동으로 통제하는 SBOM 기반 관리 체계.
- 시사점 : 프로그램 오피스, 자동 검증, 표준 SBOM과 VEX 체계가 함께 있을 때 오픈소스 활용의 법적, 보안 리스크를 관리할 수 있음.