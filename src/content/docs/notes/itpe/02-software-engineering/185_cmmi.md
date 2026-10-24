---
title: "CMMI(Capability Maturity Model Integration)"
author: "agnusdei1207"
date: "2026-10-25T00:07:09+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- CMMI(Capability Maturity Model Integration), 성숙도 레벨(Maturity Level), 능력 레벨(Capability Level), 프로세스 영역(PA, Process Area)
- 단계적 표현(Staged Representation), 연속적 표현(Continuous Representation), SEI(Software Engineering Institute), CMMI V2.0, CMMI V3.0, ALM(Application Lifecycle Management)

## Ⅰ. CMMI의 개요

- 핵심 요약 : 조직의 소프트웨어 프로세스 성숙도를 평가·개선하기 위해 개별 능력 성숙도 모델을 하나로 통합한 프로세스 개선 모델.
- 개념 : 미국 카네기멜론 대학교의 SEI(Software Engineering Institute)가 개발한 **CMMI**(Capability Maturity Model Integration, 능력 성숙도 모델 통합)는 SW-CMM(Capability Maturity Model for Software), SE-CMM, IPD-CMM(Integrated Product Development CMM) 등 분리된 모델을 통합한 프로세스 개선 체계이다.
- 배경 및 필요성 : 개인의 역량에 의존하던 프로젝트 관행에서 벗어나, 조직 차원에서 표준화되고 반복 가능한 프로세스를 세워야 할 필요가 커짐.
- 평가 구조 : **단계적 표현**(Staged Representation)은 조직 전체에 **성숙도 레벨**(Maturity Level, 1~5단계)을 부여하고, **연속적 표현**(Continuous Representation)은 **프로세스 영역**(PA, Process Area)별로 **능력 레벨**(Capability Level)을 부여하는 이중 구조.
- 현행 기준 : 2023년 4월 발표된 V3.0이 현행 버전이며, 발표 주체는 ISACA 산하 CMMI Institute(2016년 ISACA가 인수)로 확인됨. V2.0은 이전 세대 버전.

## Ⅱ. CMMI의 특징 및 장점

- 핵심 요약 : 모델 통합과 이중 표현, PA 단위 관리가 표준화와 예측 가능성이라는 장점으로 이어지는 구조.

1. 모델 통합 : SW-CMM, SE-CMM, IPD-CMM 등 분리된 모델을 하나의 체계로 묶음 → 조직 전체가 공유하는 공통 프로세스 언어 확보.
2. PA 단위 설계 : 프로세스 영역마다 목표와 실천 관행을 정의 → 개선 대상을 항목별로 좁혀 추적 가능.
3. 이중 표현 : 조직 등급(단계적)과 항목 등급(연속적) 중 목적에 맞는 경로 선택 → 도입 범위를 사업 상황에 맞게 조정.
4. 정량 통제 : 측정 데이터와 통계적 통제를 활용 → 일정과 품질의 예측 가능성 향상.
5. 버전 진화 : V2.0에서 PA 체계를 재구성하고 V3.0에서 보안·데이터 관리 등 영역을 넓힘(ISACA 발표 기준) → 디지털 환경의 관리 범위 반영.

## Ⅲ. CMMI의 구조 (흐름)

- 핵심 요약 : 초기 단계에서 최적화 단계까지 한 단계씩 상향하는 5단계 성숙도 계층 구조.

```text
[ 단계적 표현: 성숙도 레벨 ]

Level 1 : 초기 (Initial)
      ↓
Level 2 : 관리 (Managed)
      ↓
Level 3 : 정의 (Defined)
      ↓
Level 4 : 정량 관리 (Quantitatively Managed)
      ↓
Level 5 : 최적화 (Optimizing)
```

- 레벨 상승 조건 : 하위 레벨의 PA를 충족한 상태에서만 상위 레벨 PA가 인정되는 누적 구조.

```text
[ 레벨 상승 조건 ]

Level 2 : 프로젝트 기본 관리 PA 충족
      ↓
Level 3 : 조직 표준 프로세스 PA 충족
      ↓
Level 4 : 통계적 정량 통제 PA 충족
      ↓
Level 5 : 지속적 혁신 PA 충족
```

## Ⅳ. CMMI의 표현 방식과 레벨별 PA 비교

- 핵심 요약 : 조직 등급을 일괄 부여하는 단계적 표현과 항목별 등급을 추적하는 연속적 표현의 판정 단위 차이.

| 비교 축 | 단계적 표현 (Staged) | 연속적 표현 (Continuous) |
| --- | --- | --- |
| 판정 단위 | 조직 전체 성숙도 레벨 | PA별 능력 레벨 |
| 개선 순서 | 정해진 PA 묶음을 단계별로 이행 | 조직이 고른 PA를 자유 순서로 개선 |
| 결과 | 레벨 1~5 등급 | PA별 능력 등급 |
| 적합 상황 | 조직 전반의 표준화와 대외 신뢰 확보 | 특정 영역 집중 개선 |

| 성숙도 레벨 | 핵심 포커스 | 대표 프로세스 영역(PA) |
| --- | --- | --- |
| Level 1: Initial | 예측 불가능한 결과, 개인 역량 의존 | 해당 PA 없음 |
| Level 2: Managed | 프로젝트 단위의 체계화와 반복성 | REQM(요구관리), PP(프로젝트계획), PMC(프로젝트감시통제), CM(형상관리), PPQA(품질보증) |
| Level 3: Defined | 전사적 표준화와 프로세스 자산화 | RD(요구개발), TS(기술솔루션), VER(검증), VAL(확인), DAR(의사결정분석), OT(조직훈련) |
| Level 4: Quantitatively Managed | 데이터 기반의 통계적 통제 | QPM(정량적 프로젝트관리), OPP(조직 프로세스 성과) |
| Level 5: Optimizing | 지속적 혁신과 원인 제거 | CAR(원인분석과 해결), OPM(조직 성과관리) |

※ 위 PA 목록은 V1.3 기준 대표 항목이며, V2.0 이후 PA 체계가 재구성되었으므로 현행 버전은 공식 자료로 확인이 필요함.

## Ⅴ. CMMI의 장점과 한계

- 핵심 요약 : 프로세스 표준화와 예측 가능성은 확보되지만, 형식 산출물 증가·애자일 마찰·도입 비용이 한계로 남음.
- 장점 : 표준화된 반복 프로세스 확립, 정량 기반 품질·일정 관리, 레벨 기반 개선 로드맵, 공공·국방 발주에서의 조직 신뢰도 제고.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 형식적 산출물 양산 | 심사 목적의 문서·증빙 작성 → 실무 생산성 저하와 구성원 피로 누적 | 형상관리와 ALM(Application Lifecycle Management, 애플리케이션 생명주기 관리) 도구의 기록을 심사 증적으로 활용 | 문서 작성 공수 비율 |
| 애자일·DevOps와의 마찰 | 단계별 승인 절차 → 팀의 자율 의사결정과 신속 릴리스 방해 | 최신 버전의 실무 지침을 참고한 경량 테일러링, 팀 릴리스 주기 보호 | 릴리스 리드타임 |
| 심사·컨설팅 비용과 기간 | 공인 심사와 갭 분석에 드는 비용·기간 → 중소 기업의 진입 장벽 | 필수 PA 선별 적용, 단계별 예산 통제 | 심사 준비 기간, 비용 대비 효과 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : 인증 취득을 목적으로 하기보다 프로세스 개선 목표를 먼저 정하고, 경영진 주도 거버넌스로 조직 전체에 확산하는 방향.

조직은 CMMI 도입 목표를 인증 등급이 아니라 프로젝트 결과의 개선으로 먼저 정하고, 그 목표에 맞는 성숙도 수준을 단계적으로 설정하는 것이 바람직하다. 프로세스 개선을 전담하는 조직을 두고 경영진이 성과 지표를 직접 검토하면, 현장이 형식 문서를 늘리려는 유인을 줄일 수 있다. 공공·국방 발주 대응이 목적이라면 인증 범위를 발주 요구에 맞춰 한정하고, 사내 개선 활동은 별도 기준으로 운영하는 이원화가 현실적이다.

```text
[ 도입 로드맵 ]

목표 정의 (사업 목적 기준)
      ↓
핵심 프로젝트 파일럿 적용
      ↓
조직 표준 프로세스 자산 축적
      ↓
전사 확산과 인증 범위 결정
```

## Ⅶ. 결론

- 핵심 요약 : CMMI는 인증 등급이 아니라 프로세스 성숙도를 측정하고 개선하는 공통 체계.
- 시사점 : V3.0이 관리 영역을 넓힌 만큼, 소프트웨어 개발을 넘어 조직 전반의 관리 체계로 활용 범위가 확대될 전망.
