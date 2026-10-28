---
title: "CSMA/CA(Carrier Sense Multiple Access with Collision Avoidance)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "011"
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- CSMA/CA, CSMA/CD, 접근 제어, 반송파 감지, NAV, IFS, 백오프
- 경쟁 창(CW), 숨은 노드, 노출 노드, RTS/CTS, ACK, OFDMA, BSS Coloring

## Ⅰ. CSMA/CA의 개요

- 핵심 요약 : 충돌 검출이 불가능한 무선 매체에서 송신 전 감지와 임의 대기로 충돌을 사전에 회피하는 무선랜 접근 제어 방식.
- 개념 : 데이터 전송 전 채널을 감지하고 대기 시간을 두어 충돌을 피하는 **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance) 방식으로, 무선랜(IEEE(Institute of Electrical and Electronics Engineers) 802.11)의 매체 접근 제어(MAC, Medium Access Control) 계층의 동작 방식.
- 배경 및 필요성 : 유선 이더넷의 **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection)는 송신 신호와 수신 신호의 비교로 충돌을 즉시 검출하지만, 무선에서는 자기 송신 신호가 수신 신호보다 훨씬 강해 검출이 사실상 불가능함.
- 주요 목적 : 공유 무선 채널의 충돌 확률 최소화, **숨은 노드** (Hidden Node, 서로를 감지하지 못하는 단말 간 충돌) 문제 완화, 다수 단말의 공정한 접속 기회 보장.

## Ⅱ. CSMA/CA의 특징 및 장점

- 핵심 요약 : 이중 감지, 차등 간격, 난수 대기, 제어 프레임 교환이 겹쳐 충돌을 줄이는 분산형 접근 구조.

1. 이중 반송파 감지 : 물리 계층의 에너지 감지(CCA, Clear Channel Assessment)와 **NAV**(Network Allocation Vector, 프레임 Duration 값으로 설정하는 가상 채널 점유 타이머)를 함께 사용 → 채널 상태 판단의 정확도 향상.
2. 차등 프레임 간격 : **IFS**(Inter-Frame Space)를 용도별로 SIFS(Short IFS)·DIFS(DCF IFS) 등으로 구분 적용 → 응답 프레임의 송신 우선권 확보.
3. 랜덤 백오프 : 경쟁 창(CW, Contention Window) 범위에서 난수를 뽑아 대기하고, 충돌 시 CW를 지수적으로 확장 → 다수 단말 송신 시점의 분산 효과.
4. 제어 프레임 교환 : 데이터 전송 전 **RTS/CTS** (Request to Send / Clear to Send) 교환으로 수신 측 AP(Access Point)와 주변 노드에 NAV를 설정하고, 완료는 ACK(Acknowledgment)로 통보 → 숨은 노드 충돌의 사전 차단.

## Ⅲ. CSMA/CA의 구조 (흐름)

- 핵심 요약 : 감지부터 응답 수신까지의 기본 절차와 숨은 노드를 막는 제어 프레임 교환의 두 흐름.

```text
[ 기본 전송 절차 ]

채널 감지 (Busy면 Idle까지 대기)
   ↓
DIFS 대기
   ↓
백오프 카운트다운 (CW 내 난수)
   ↓  타 노드 전송 시 카운터 정지
DATA 전송
   ↓  SIFS 후
ACK 수신 (미수신 시 CW 확장 후 재시도)
```

```text
[ RTS/CTS 교환과 숨은 노드 차단 ]

A → AP : RTS 전송
   ↓
AP → A : CTS (주변 노드 NAV 설정)
   ↓  숨은 노드 C는 CTS를 듣고 대기
A → AP : DATA 전송
   ↓
AP → A : ACK 반환
```

- 백오프 카운터 : CW 범위의 난수로 시작해 유휴 슬롯마다 감소하는 대기 계수기.
- **노출 노드**(Exposed Node, 전송이 가능한데도 타 노드의 통신을 감지해 불필요하게 대기하는 상황) : 숨은 노드와 대비되는 가시성 문제.

## Ⅳ. CSMA/CA와 CSMA/CD·ALOHA의 비교

- 핵심 요약 : 충돌을 검출하던 유선 방식과 단순 재전송하던 초기 무선 방식을 회피 기반 구조로 보완한 결과.
- 비교 대상 : 무선 802.11의 CSMA/CA, 유선 802.3의 CSMA/CD, 초기 무선 방식인 **ALOHA**.

| 비교 축 | CSMA/CA (무선 802.11) | CSMA/CD (유선 802.3) | ALOHA (초기 무선) |
| --- | --- | --- | --- |
| 충돌 처리 | 사전 회피 | 즉시 검출 후 전송 중단 | 충돌 후 단순 재전송 |
| 충돌 검출 | 불가 (자기 신호가 강함) | 가능 (신호 비교) | 불가 (응답 부재로 인지) |
| 확인 응답 | 필수 | 불필요 | 필수 |
| 핵심 메커니즘 | IFS, 백오프, NAV, RTS/CTS | Jam 신호, 슬롯 타이머 | 타임아웃 재전송 |
| 이론상 최대 효율 | 중간 (오버헤드 부담) | 높음 | 약 18.4% (Pure), 약 36.8% (Slotted) |

- 선택 기준 : 무선 공유 매체에서는 CSMA/CA가 기본이고, 유선 전이중 스위치 환경에서는 CSMA/CD의 역할이 소멸한 상태.

## Ⅴ. CSMA/CA의 한계와 방안

- 핵심 요약 : 노드 가시성 문제, 밀집 환경의 처리량 저하, 제어 오버헤드를 선택적 교환, 스케줄링 접근, 임계치 운영으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 숨은 노드·노출 노드 | 서로 감지 못해 충돌하거나, 가능한 전송도 불필요하게 대기 | 임계치 이상 프레임에만 RTS/CTS 적용, AP 배치로 간섭 범위 관리 | 재전송률 |
| 고밀도 환경의 처리량 저하 | 다수 단말 경쟁으로 백오프 확장 반복 → 유효 속도 급락 | Wi-Fi 6의 OFDMA(Orthogonal Frequency-Division Multiple Access) 자원 분할과 AP 스케줄링 | 단말당 평균 대기 시간 |
| 제어 프레임 오버헤드 | 소형 패킷에서 교환 시간이 데이터 시간보다 김 | RTS 임계치(RTS Threshold) 조정으로 적용 대상 축소 | 제어 프레임 비율 |

## Ⅵ. CSMA/CA에 대한 기술사적 제언

- 핵심 요약 : 경쟁 방식과 스케줄링 방식의 공존 설계, 현장 파라미터 운영 절차, 공간 재사용 검증을 갖추는 방향.
- 설계 : 무선랜 운영 조직은 레거시 단말 공존 구간에 CSMA/CA를 유지하고 고성능 구간에 스케줄링 비중을 높이는 이원 설계 권장.
- 운영 : 현장 관리 조직은 파라미터 변경 이력과 재전송률 기록 절차로 임계치 조정 효과의 장기 추적 체계 마련.
- 검증 : 공간 재사용 기능(BSS Coloring) 도입 시 현장 간섭 측정 기반의 사전 검증 절차 구성 권장.

## Ⅶ. 결론

- 핵심 요약 : CSMA/CA는 무선 매체의 충돌 검출 불가 특성을 감지·대기·가상 타이머로 보완한 분산 접근 프로토콜임.
- 시사점 : 고밀도 환경일수록 경쟁 방식의 한계가 커지므로 경쟁과 스케줄링의 혼용이 무선랜 설계의 기본 방향이 됨.
