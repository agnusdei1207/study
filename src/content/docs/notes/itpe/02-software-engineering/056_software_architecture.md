---
title: "소프트웨어 아키텍처(Software Architecture)"
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

- 소프트웨어 아키텍처(Software Architecture), ISO/IEC/IEEE 42010, 4+1 뷰(View), 비기능 품질속성
- 아키텍처 기술서(AD, Architecture Description), 뷰(View)·관점(Viewpoint), ATAM, CBAM, ADD(Attribute-Driven Design), ADR(Architecture Decision Record)

## Ⅰ. 소프트웨어 아키텍처의 개요

- 핵심 요약 : 구성요소·상호 관계·속성·원칙을 망라한 시스템의 기본 구조 청사진.
- 개념 : 소프트웨어 시스템의 기본 구조로서 다음 4대 요소를 망라한 청사진.
  1. 구성요소(Elements)
  2. 구성요소 간의 상호 관계(Relationships)
  3. 구성요소들의 외부로 드러나는 속성(Properties)
  4. 시스템의 설계 및 진화에 적용되는 원칙(Principles)
- 배경 및 필요성 : 복잡한 대규모 시스템 구축 시 이해관계자 간의 원활한 의사소통 기준 제공, 초기 설계 결정 실패로 인한 막대한 재작업 비용 방지, 비기능 품질속성(성능, 보안, 가용성, 유지보수성)의 달성 필요.
- 국제 표준 : ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission)/IEEE(Institute of Electrical and Electronics Engineers) 42010(시스템 및 소프트웨어 엔지니어링 - 아키텍처 기술 표준).

## Ⅱ. 소프트웨어 아키텍처의 특징 (4+1 뷰 모델)

- 핵심 요약 : 크루첸(Kruchten)의 4+1 뷰 모델로 유스케이스 뷰를 중심에 두고 4개 뷰가 다각도 기술.
1. 유스케이스 뷰(Use Case View, +1 View) : 다른 4가지 뷰를 도출하고 검증하는 중심 뷰로, 최종 사용자 관점의 시나리오 제시.
2. 논리 뷰(Logical View) : 시스템이 제공해야 할 기능적 요구사항을 지원하는 객체 모델, 클래스 다이어그램, 도메인 엔티티 구조를 다루는 뷰.
3. 프로세스 뷰(Process View) : 런타임 시점의 동시성(Concurrency), 비동기 처리, 스레드 제어, 시스템 무결성과 성능을 다루는 뷰.
4. 구현/개발 뷰(Development View) : 소스코드 모듈 구조, 패키지 계층, 라이브러리 의존성, 빌드 관리 환경을 다루는 뷰.
5. 배포 뷰(Physical View) : 소프트웨어 컴포넌트가 실행될 물리적/가상 서버, 네트워크 토폴로지, 클라우드 인프라 매핑을 다루는 뷰.

## Ⅲ. 소프트웨어 아키텍처의 구조 (흐름)

- 핵심 요약 : 4+1 뷰 구조와 ISO/IEC/IEEE 42010의 관심사 → 뷰 → 아키텍처 기술서 전개 흐름.

```text
[ 유스케이스 뷰 (Use Case) ] : 중심 뷰 (+1)
 - 최종 사용자 관점, 시나리오로 뷰 도출·검증
   ├─ [ 논리 뷰 ] - 설계자, 클래스·객체 모델
   ├─ [ 프로세스 뷰 ] - 통합자, 동시성·성능
   ├─ [ 구현 뷰 ] - 프로그래머, 모듈·빌드
   └─ [ 배포 뷰 ] - 엔지니어, 물리 노드 매핑
```

```text
[ ISO/IEC/IEEE 42010 개념 흐름 ]
미션(Mission)·환경(Environment)
        ↓
이해관계자(Stakeholder)의 관심사(Concern) 도출
        ↓
관점(Viewpoint) 선정 → 뷰(View) 작성
        ↓
아키텍처 기술서(AD, Architecture Description) 확정
```

## Ⅳ. ISO/IEC/IEEE 42010 핵심 개념의 비교

- 핵심 요약 : 미션·환경·이해관계자·관심사·AD·뷰의 역할 구분.

| 핵심 개념 | 정의 및 역할 |
|---|---|
| 미션(Mission) | 시스템이 달성하고자 하는 궁극적인 비즈니스 목적 및 운영 목표 |
| 환경(Environment) | 시스템 개발 및 운영에 영향을 미치는 외부 환경적 요인(법규, 기술, 시장) |
| 이해관계자(Stakeholder) | 시스템에 관심과 책임을 가진 개인 또는 그룹(발주자, 사용자, 개발자, 운영자) |
| 관심사(Concern) | 이해관계자가 중요하게 여기는 시스템의 핵심 요구(비용, 성능, 보안, 납기) |
| 아키텍처 기술서(AD, Architecture Description) | 시스템의 아키텍처를 공식적으로 문서화한 기록물(SAD, Software Architecture Description) |
| 아키텍처 뷰(View) | 특정 관점(Viewpoint)에서 시스템의 관심사를 다룬 아키텍처 표현물 |

## Ⅴ. 소프트웨어 아키텍처의 장점과 한계

- 핵심 요약 : 의사소통 기준·품질 달성의 장점과 아키텍처 침식·상아탑 괴리·트레이드오프 실패의 한계.
- 장점
  1. 이해관계자 간 원활한 의사소통 기준 제공.
  2. 초기 설계 결정 실패로 인한 재작업 비용 방지.
  3. 비기능 품질속성(성능, 보안, 가용성, 유지보수성)의 체계적 달성.
- 한계점 1 : 개발 진행 중 아키텍처 침식(Architecture Erosion) 및 설계 붕괴
  - 한계점 : 초기 수립된 계층형 또는 헥사고날 아키텍처 원칙이 촉박한 개발 일정과 편법 핫픽스로 인해 무단 우회되면서 모듈 간 순환 참조가 발생하고 스파게티 코드로 퇴화.
  - 해결 방안 : ArchUnit, SonarQube 등 아키텍처 피트니스 함수(Fitness Function)를 CI/CD(Continuous Integration/Continuous Delivery) 파이프라인에 통합하여 패키지 간 의존성 규칙 위반 발생 시 빌드 자동 차단.
- 한계점 2 : 상아탑 아키텍처(Ivory Tower Architecture)와 구현 현장 간의 괴리
  - 한계점 : 아키텍트가 실제 코딩과 유리된 채 비현실적인 추상 다이어그램과 이론 중심의 문서만을 양산하여 실제 개발팀의 외면과 불신 초래.
  - 해결 방안 : 코딩하는 아키텍트(Hands-on Architect) 제도의 정착을 통한 핵심 프레임워크 스파이크 코드의 직접 작성, 실제 구현 난제의 페어 프로그래밍 기반 해결.
- 한계점 3 : 상충되는 품질 속성 간 트레이드오프 조율 실패
  - 한계점 : 고성능, 무중단 가용성, 완벽한 보안, 개발 유연성 등 상충되는 비기능 요구사항을 모두 만족하려다 시스템 복잡도가 폭증하고 비용이 통제 불능 상태로 치달음.
  - 해결 방안 : ATAM(Architecture Tradeoff Analysis Method) 및 CBAM(Cost Benefit Analysis Method) 기법의 적용을 통한 비즈니스 가치에 직결된 핵심 품질 속성 우선순위의 명시적 절충.

## Ⅵ. 엔터프라이즈 아키텍처 거버넌스를 위한 기술사적 제언

- 핵심 요약 : 품질속성 주도 설계(ADD) 체계화와 ADR 기반 거버넌스 정착.
- 품질속성 주도 설계(ADD, Attribute-Driven Design) 체계화 : 아키텍처는 기능적 요구사항보다 비기능 품질속성(NFR, Non-Functional Requirement)에 의해 결정되므로, SEI(Software Engineering Institute)의 ADD 방법론을 적용하여 유틸리티 트리에서 도출된 핵심 품질 시나리오를 만족하는 아키텍처 전술(Tactics)의 체계적 도출 필요.
- 아키텍처 결정 기록(ADR, Architecture Decision Record) 도입 : 왜 특정 기술이나 아키텍처 스타일을 선택했고 대안은 무엇이었는지를 마크다운 기반의 짧은 문서(ADR)로 버전 관리하여, 장기적 시스템 진화 과정에서 아키텍처 부패(Architecture Erosion) 방지를 위한 거버넌스 정착 필요.

## Ⅶ. 결론

- 핵심 요약 : 소프트웨어 아키텍처는 비기능 품질 달성의 청사진이며, 지속 거버넌스가 유지의 핵심.
- 요약 : 4+1 뷰와 ISO/IEC/IEEE 42010 프레임워크를 통한 시스템의 다각도 기술.
- 시사점 : 피트니스 함수 자동 검증과 ADR 기록을 통한 아키텍처 침식 방지 필요.
