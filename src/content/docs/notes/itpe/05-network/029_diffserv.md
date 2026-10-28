---
title: "DiffServ(Differentiated Services)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "029"
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- DiffServ(Differentiated Services), DS 필드(Differentiated Services Field), DSCP(Differentiated Services Code Point), PHB(Per-Hop Behavior)
- EF(Expedited Forwarding), AF(Assured Forwarding), 경계 라우터, 코어 라우터, SLA(Service Level Agreement), 트래픽 조절(Traffic Conditioning), WRED(Weighted Random Early Detection)

## Ⅰ. DiffServ의 개요

- 핵심 요약 : 경계에서 등급 표시를 부여하고 도메인 내 각 라우터가 표시에 정해진 홉별 행동으로 응답하는 클래스 기반 품질 구조.
- 개념 : IP 헤더의 **DS 필드**(Differentiated Services Field)에 기록된 **DSCP**(Differentiated Services Code Point, 서비스 등급 코드)에 따라 같은 등급의 트래픽 집합인 **클래스**(Class) 단위로 차등 처리를 적용하는 **차등 서비스** (DiffServ, Differentiated Services) 모델. IETF(Internet Engineering Task Force)의 RFC 2474·2475로 표준화.
- 배경 및 필요성 : 흐름마다 경로 전체에 상태를 유지하는 예약 기반 모델은 백본 규모에서 라우터 상태가 흐름 수에 비례해 폭증하는 확장성 한계 → 상태를 유지하지 않는 집약 처리의 필요.
- 주요 목적 : 대규모 망에서 확장 가능한 품질 차등, 코어 고속 포워딩의 유지, 사업자 간 품질 계약의 실행 수단 확보.

## Ⅱ. DiffServ의 특징 및 장점

- 핵심 요약 : 에지의 분류·마킹과 코어의 단순 실행으로 역할을 나누어, 상태 부담 없이 확장되는 차등 품질 구조.

1. DSCP 마킹 : DS 필드 상위 6비트로 64개의 코드 표현 → 분류 결과를 패킷에 기록 → 이후 홉은 헤더만 판독해 처리.
2. 홉별 행동 : **PHB**(Per-Hop Behavior, 같은 DSCP에 대해 노드가 수행하는 관측 가능한 전달 행동)를 도메인 단위로 일관 정의 → 도메인 내 동일 등급의 균일한 품질.
3. 역할 분담 : 복잡한 분류·계량·조절은 **경계 라우터**(Edge Router)가 담당, 코어는 DSCP 기반 큐잉만 수행 → 코어 부하가 흐름 수와 무관한 확장성.
4. 계약 기반 조절 : SLA(Service Level Agreement)로 합의한 프로파일을 **트래픽 조절**(Traffic Conditioning, 계량·재표시·폐기의 집합)로 집행 → 품질 계약의 근거 확보.
5. 표준 PHB 집합 : 저지연 전용 **EF**(Expedited Forwarding)와 4개 클래스×3단계 폐기 우선순위의 **AF**(Assured Forwarding), 규정 없는 트래픽의 **Default** 처리 → 음성·중요 데이터·일반 트래픽의 등급 운영.

## Ⅲ. DiffServ의 구조 (흐름)

- 핵심 요약 : 도메인 경계에서 분류·마킹·조절을 마친 패킷이 코어에서 홉별 행동으로 처리되는 2단계 구조.

```text
[ 도메인 내 처리 흐름 ]

인입 패킷
    ↓
경계 라우터
    (분류 → 마킹 → 계량·조절)
    ↓ DSCP 부여
코어 라우터
    (DSCP 판독 → PHB 실행)
    ↓
타 도메인 경계로 출력
```

```text
[ 표준 PHB 집합 ]

EF (DSCP 46) : 저지연 전용 큐
    ↓
AF (AF11~AF43) : 클래스별 큐
    + 폐기 우선순위 3단계
    ↓
Default (DSCP 0) : 일반 처리
```

- DS 필드는 8비트 중 상위 6비트가 DSCP, 하위 2비트는 ECN(Explicit Congestion Notification, 혼잡 통지) 용도의 구분.
- WRED(Weighted Random Early Detection) 같은 조기 폐기가 AF의 폐기 우선순위 집행에 활용되는 구성.

## Ⅳ. DiffServ와 IntServ의 비교

- 핵심 요약 : 클래스 단위 상대 보장의 DiffServ와 흐름 단위 절대 보장의 IntServ(Integrated Services)가 보장 수준과 확장성에서 대비되는 관계.
- 선택 기준 : 소규모 폐쇄망의 결정론적 보장이면 흐름 예약 모델, 대규모 공용 망의 등급 차등이면 DiffServ.

| 비교 축 | DiffServ (차등 서비스) | IntServ (통합 서비스) |
| --- | --- | --- |
| 제어 단위 | 클래스 단위 집약 | 개별 마이크로 플로우 |
| 보장 수준 | 통계적·상대적 차등 | 결정론적 절대 보장 |
| 라우터 상태 | 코어는 상태 비보유 | 경로 전체가 플로우 상태 보유 |
| 시그널링 | 사전 시그널링 불필요 | RSVP(Resource Reservation Protocol) 예약 필요 |
| 확장성 | 대규모 백본에 적합 | 흐름 수 증가에 취약 |
| 대표 적용처 | 기업망·ISP(Internet Service Provider) 백본 | 폐쇄망·방송망 |

## Ⅴ. DiffServ의 한계와 방안

- 핵심 요약 : 절대 보장 불가, 도메인 간 재마킹, 암호화 트래픽의 분류 곤란을 경로 설계, 계약 매핑, 응용 단 표시로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 절대 보장 불가 | 동시 혼잡 시에도 등급 내 지연·손실 발생 | MPLS-TE(Multiprotocol Label Switching Traffic Engineering)로 경로별 대역의 사전 설계 | 클래스별 지연·손실률 |
| 도메인 간 재마킹 | 타 사업자 경계에서 DSCP 초기화 → 종단 품질 단절 | 사업자 간 SLA와 802.1p CoS(Class of Service)·MPLS 표시 필드의 매핑 규약 준수 | 경계 DSCP 유지율 |
| 암호화 트래픽 분류 곤란 | 페이로드 암호화 확산으로 심층 검사의 식별력 저하 | 응용 단 DSCP 표시 정책과 흐름 통계 기반 분류의 병용 | 미분류 트래픽 비율 |

## Ⅵ. DiffServ에 대한 기술사적 제언

- 핵심 요약 : 무손실 데이터센터, 지능형 광역망, 임계치 거버넌스로 이어지는 운영 수준의 확장 제안.
- 데이터센터 운영 조직은 AI 분산 학습 같은 무손실 수요에 전용 DSCP 클래스를 두고 우선순위 기반 흐름 제어(PFC, Priority Flow Control)와 짝지은 설계를 적용하는 방안.
- 광역망 운영 조직은 소프트웨어 정의 광역 네트워크(SD-WAN, Software-Defined Wide Area Network)에서 응용 식별 결과를 DSCP에 연결하고 회선 품질에 따라 경로를 선택하는 체계 도입.
- 품질 관리 조직은 WRED 임계치를 등급별로 문서화하고 정기 튜닝 주기를 운영하는 품질 거버넌스 절차 마련.

## Ⅶ. 결론

- 핵심 요약 : DiffServ는 상태 비보유 코어와 6비트 등급 표시로 품질 차등을 확장 가능하게 만든 표준 아키텍처.
- 상대적 보장이라는 본질을 전제로 경로 설계와 계약 운영을 곁들일 때 체감 품질의 유지가 가능한 구조.
