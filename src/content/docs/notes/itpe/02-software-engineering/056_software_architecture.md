---
title: "소프트웨어 아키텍처(Software Architecture)"
author: "agnusdei1207"
date: "2026-10-24T23:57:08+09:00"
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

- 소프트웨어 아키텍처(Software Architecture), ISO/IEC/IEEE 42010, 4+1 뷰(View), 비기능 품질속성
- 아키텍처 기술서(AD, Architecture Description), 뷰(View)·관점(Viewpoint), ATAM, CBAM, ADD(Attribute-Driven Design), ADR(Architecture Decision Record)

## Ⅰ. 소프트웨어 아키텍처의 개요

- 핵심 요약 : 구성요소, 상호 관계, 속성, 원칙을 담아 시스템의 기본 구조를 그린 청사진.
- 개념 : 시스템의 **소프트웨어 아키텍처**(Software Architecture)는 다음 네 요소를 담은 기본 구조다.
  1. 구성요소(Elements)
  2. 구성요소 간 상호 관계(Relationships)
  3. 구성요소가 외부로 드러내는 속성(Properties)
  4. 설계와 진화에 적용되는 원칙(Principles)
- 배경 및 필요성 : 대규모 시스템에서는 이해관계자 사이의 공통 소통 기준이 없으면 초기 설계 오류가 뒤늦게 큰 재작업으로 돌아온다. 성능, 보안, 가용성, 유지보수성 같은 **비기능 품질속성**(Quality Attributes)을 설계 단계에서 확보할 필요가 여기서 생긴다.
- 주요 목적 : 이해관계자가 같은 그림을 보고 판단하도록 하고, 품질 목표를 구조로 실현하는 것.
- 국제 표준 : **ISO/IEC/IEEE 42010**은 ISO(International Organization for Standardization), IEC(International Electrotechnical Commission), IEEE(Institute of Electrical and Electronics Engineers)가 함께 제정한 아키텍처 기술 표준이다.

## Ⅱ. 소프트웨어 아키텍처의 특징 및 장점

- 핵심 요약 : 크루첸(Kruchten)의 **4+1 뷰 모델**은 유스케이스 뷰를 중심에 두고 네 개의 뷰로 시스템을 다각도로 기술.

1. 유스케이스 뷰(Use Case View, +1 View) : 최종 사용자 시나리오를 제시하고, 나머지 네 뷰를 도출하고 검증하는 중심 뷰 → 뷰 사이의 일관성 확보.
2. 논리 뷰(Logical View) : 기능 요구를 지원하는 클래스와 도메인 객체 구조를 다룸 → 기능 설계의 명확화.
3. 프로세스 뷰(Process View) : 동시성, 비동기 처리, 스레드 제어를 다룸 → 성능과 무결성 검토.
4. 구현 뷰(Development View) : 모듈과 패키지 계층, 라이브러리 의존성, 빌드 환경을 다룸 → 개발 생산성과 변경 용이성 확보.
5. 배포 뷰(Physical View) : 컴포넌트가 실행될 서버, 네트워크, 클라우드 자원의 매핑을 다룸 → 가용성과 운영 비용 판단 근거 제공.

## Ⅲ. 소프트웨어 아키텍처의 구조 (흐름)

- 핵심 요약 : 유스케이스 뷰가 중심이 되어 네 개 뷰를 관점별 이해관계자에게 나누어 제시하는 구조와, 표준이 정한 기술 절차.

```text
[ 유스케이스 뷰 (+1 View) ]
  시나리오로 나머지 뷰를 도출·검증
        ↓
[ 논리 뷰 ] 기능 구조 : 설계자
[ 프로세스 뷰 ] 동시성 : 통합자
[ 구현 뷰 ] 모듈·빌드 : 개발자
[ 배포 뷰 ] 물리 노드 : 운영자
```

```text
[ ISO/IEC/IEEE 42010 개념 흐름 ]

미션(Mission)·환경(Environment)
        ↓
이해관계자(Stakeholder)의 관심사(Concern)
        ↓
관점(Viewpoint) 선정 → 뷰(View) 작성
        ↓
아키텍처 기술서(AD, Architecture Description)
```

## Ⅳ. ISO/IEC/IEEE 42010 핵심 개념의 비교

- 핵심 요약 : 미션과 환경이 설계 배경을 정하고, 이해관계자와 관심사가 뷰를 결정하며, AD가 그 결과를 묶는 역할 구분.

| 핵심 개념 | 정의 및 역할 |
| --- | --- |
| 미션(Mission) | 시스템이 달성하려는 비즈니스 목적과 운영 목표 |
| 환경(Environment) | 개발과 운영에 영향을 주는 법규, 기술, 시장 같은 외부 요인 |
| 이해관계자(Stakeholder) | 시스템에 관심과 책임을 가진 개인이나 집단(발주자, 사용자, 개발자, 운영자) |
| 관심사(Concern) | 이해관계자가 중시하는 요구(비용, 성능, 보안, 납기) |
| 관점(Viewpoint) | 관심사를 다루는 표현 방식과 규칙을 정한 틀 |
| 뷰(View) | 특정 관점에서 관심사를 다룬 아키텍처 표현물 |
| 아키텍처 기술서(AD) | 뷰와 관점, 결정 사항을 공식 문서로 묶은 기록물 |

## Ⅴ. 소프트웨어 아키텍처의 한계와 방안

- 핵심 요약 : 아키텍처 침식, 실무와의 괴리, 품질속성 간 상충이라는 한계를 자동 검증, 실무 참여, 트레이드오프 평가로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 아키텍처 침식(Architecture Erosion) | 계층이나 헥사고날 원칙이 촉박한 일정과 편법 수정으로 우회되어 순환 참조와 스파게티 코드 발생 | ArchUnit, SonarQube 같은 **피트니스 함수**(Fitness Function)를 CI/CD 파이프라인(CI/CD, Continuous Integration/Continuous Delivery)에 넣어 규칙 위반 시 빌드 차단 | 의존성 규칙 위반 건수 |
| 상아탑 아키텍처(Ivory Tower Architecture) | 아키텍트가 구현과 떨어져 추상 문서만 만들어 개발팀의 외면과 불신 초래 | 아키텍트가 핵심 프레임워크의 스파이크 코드를 직접 작성하는 방식과 페어 프로그래밍 기반 난제 해결 | 설계 문서의 구현 반영률 |
| 품질속성 간 트레이드오프 실패 | 고성능, 무중단, 완벽한 보안을 동시에 좇아 복잡도와 비용이 통제 불능이 됨 | **ATAM**(Architecture Tradeoff Analysis Method)으로 품질속성 간 충돌을 드러내고, **CBAM**(Cost Benefit Analysis Method)으로 비용 대비 효익을 비교해 우선순위 확정 | 우선순위 합의 건수, 변경 비용 |

## Ⅵ. 엔터프라이즈 아키텍처 거버넌스를 위한 기술사적 제언

- 핵심 요약 : 품질속성 중심의 설계 절차와 결정 기록을 거버넌스 체계로 묶어 아키텍처를 시간이 지나도 유지되게 할 것.

1. 품질속성 주도 설계의 체계화 : 아키텍처는 기능보다 비기능 품질속성에 의해 결정되는 경우가 많으므로, 설계 초기에 **ADD**(Attribute-Driven Design) 절차로 품질 시나리오를 정하고, 그 시나리오를 만족하는 아키텍처 전술(Tactics)을 단계적으로 도출하는 방식을 표준으로 삼는다.
2. 결정 기록의 거버넌스화 : 특정 기술과 스타일을 고른 이유와 기각한 대안을 **ADR**(Architecture Decision Record)로 짧게 남겨 버전 관리하면, 인력이 바뀌어도 설계 의도가 보존되어 아키텍처 침식을 억제할 수 있다.

## Ⅶ. 결론

- 핵심 요약 : 소프트웨어 아키텍처는 품질 목표를 구조로 옮긴 청사진이며, 설계 이후의 지속적인 거버넌스가 효과를 좌우.
- 시사점 : 4+1 뷰와 ISO/IEC/IEEE 42010 프레임으로 이해관계자를 맞추고, 자동 검증과 결정 기록으로 구조가 무너지지 않게 관리해야 한다.
