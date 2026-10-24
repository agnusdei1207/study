---
title: "CSMA/CA(Carrier Sense Multiple Access with Collision Avoidance)"
author: "agnusdei1207"
date: "2026-10-24T22:41:50+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- CSMA/CA, CSMA/CD, ALOHA, 접근 제어, 반송파 감지, NAV, IFS
- 백오프, 경쟁 창(CW), 숨은 노드, 노출 노드, RTS/CTS, ACK
- OFDMA, Wi-Fi 6, BSS Coloring, RTS 임계치

## Ⅰ. CSMA/CA의 개요

- 핵심 요약 : 무선 매체에서는 충돌을 직접 검출할 수 없어, 송신 전에 채널을 감지하고 대기 시간을 두어 충돌을 미리 피하는 경쟁 기반 접근 제어 방식.
- 개념 : 무선 LAN(IEEE(Institute of Electrical and Electronics Engineers) 802.11)에서 송신 중 충돌을 검출할 수 없으므로, 데이터 전송 전 채널을 감지하고 임의의 대기 시간을 두어 충돌을 사전에 회피하는 **접근 제어**(MAC, Media Access Control) 프로토콜 (CSMA/CA, Carrier Sense Multiple Access with Collision Avoidance).
- 배경 및 필요성 : 유선 이더넷의 CSMA/CD(Carrier Sense Multiple Access with Collision Detection)는 송신 신호와 수신 신호를 비교해 충돌을 감지하지만, 무선에서는 자기 송신 신호가 수신 신호보다 압도적으로 강해 충돌 검출이 사실상 불가능하므로 회피 방식이 필수가 됨.
- 핵심 목적 : 공유 무선 매체의 충돌 확률 최소화, **숨은 노드**(Hidden Node) 문제 해결, 다수 단말의 공정한 무선 접속 기회 보장.

## Ⅱ. CSMA/CA의 특징 및 장점

- 핵심 요약 : 채널 감지, 프레임 간격, 가상 타이머, 난수 대기, 제어 프레임 교환을 겹쳐 충돌을 줄이는 분산형 접근 방식.

1. **반송파 감지**(Carrier Sensing) : 물리 계층 에너지 감지(CCA, Clear Channel Assessment)와 **NAV**(Network Allocation Vector, 프레임 헤더 Duration 값으로 설정되는 가상 타이머)를 함께 써서 채널 점유를 이중으로 확인 → 불필요한 송신 충돌 감소.
2. **IFS**(Inter-Frame Space) : 프레임 간 대기 시간을 SIFS(Short IFS, ACK·CTS), PIFS(PCF IFS, 폴링), DIFS(DCF IFS, 일반 데이터) 순으로 차등 적용 → 응답 프레임이 먼저 나가도록 우선순위 확보.
3. **백오프**(Random Backoff) : DIFS 이후 경쟁 창(CW, Contention Window) 안에서 난수를 골라 유휴 슬롯마다 줄이고, 충돌 시 CW를 두 배씩 넓혀 지수적으로 확장 → 여러 단말의 송신 시점이 분산됨.
4. **RTS/CTS 핸드셰이크**(RTS, Request to Send / CTS, Clear to Send) : 대용량 데이터 전송 전 제어 프레임을 교환해 주변 노드에 NAV를 설정 → 숨은 노드에 의한 충돌 차단.

## Ⅲ. CSMA/CA의 구조 (흐름)

- 핵심 요약 : 채널 감지부터 ACK 수신까지의 기본 절차와, 숨은 노드를 막기 위한 RTS/CTS 교환의 두 흐름으로 구성.

```text
[ CSMA/CA 기본 전송 절차 ]

채널 감지 (Carrier Sense)
   ↓  Busy면 Idle까지 대기
DIFS 대기
   ↓
랜덤 백오프 카운트다운 (CW 내 난수)
   ↓  타 노드 전송 시 카운트 정지
DATA 전송
   ↓  SIFS 후
ACK 수신 (미수신 시 CW 2배 확장 후 재시도)
```

```text
[ RTS/CTS 4-Way 핸드셰이크 ]

A → AP : RTS (NAV 설정 요청)
   ↓
AP → A : CTS (주변 노드 NAV 설정)
   ↓  숨은 노드 C는 CTS를 듣고 대기
A → AP : DATA
   ↓  SIFS 후
AP → A : ACK
```

## Ⅳ. CSMA/CA와 유선 CSMA/CD, ALOHA의 비교

- 핵심 요약 : 유선 CSMA/CD가 충돌을 검출해 채널 낭비를 줄였다면, CSMA/CA는 무선의 검출 불가 특성을 시간 간격과 가상 타이머로 보완한 방식.
- 비교 대상 : 무선 802.11의 CSMA/CA, 유선 802.3의 CSMA/CD, 초기 무선 방식인 **ALOHA**.

| 비교 축 | CSMA/CA (무선 802.11) | CSMA/CD (유선 802.3) | ALOHA (초기 무선) |
| --- | --- | --- | --- |
| 통신 매체 | 공유 무선 채널 (RF) | 유선 케이블 | 무선 패킷 통신 |
| 충돌 처리 방식 | 사전 회피 | 즉시 검출 후 중단 | 충돌 시 단순 재전송 |
| 충돌 검출 | 불가능 (자기 송신 신호가 강함) | 가능 (신호 전압 비교) | 불가능 (ACK 미수신으로 인지) |
| 확인 응답 (ACK) | 필수, 수신 즉시 반환 | 불필요 (충돌 없으면 성공 간주) | 필수 |
| 주요 메커니즘 | IFS, 백오프, RTS/CTS, NAV | Jam 신호, 슬롯 시간, 백오프 | 타임아웃 후 재전송 |
| 채널 이용 효율 | 오버헤드로 중간 수준 | 높음 | 최대 약 18.4% (Pure), 약 36.8% (Slotted) |

- 선택 기준 : 무선 공유 매체에서는 CSMA/CA가 기본이며, 유선 구간에서는 전이중 스위치 환경이라면 CSMA/CD 자체가 거의 쓰이지 않음.

## Ⅴ. CSMA/CA의 한계와 방안

- 핵심 요약 : 숨은·노출 노드, 단말 밀집에 따른 백오프 지연, 제어 프레임 오버헤드를 선택적 RTS/CTS, OFDMA 스케줄링, 임계치 조정으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 숨은 노드와 노출 노드 문제 | 숨은 노드는 서로 감지하지 못해 AP에서 충돌하고, 노출 노드는 전송이 가능한데도 불필요하게 대기 | 임계치를 넘는 프레임에만 RTS/CTS를 적용하고 AP 배치로 간섭 범위를 관리 | 재전송률, 노드별 대기 시간 |
| 단말 밀집 시 백오프 지연 증가 | 다수 단말의 경쟁으로 CW 충돌이 잦아 지수 백오프가 늘고 유효 처리량이 급락 | Wi-Fi 6 이상의 OFDMA(Orthogonal Frequency-Division Multiple Access)로 자원 단위를 나누고 AP의 트리거 프레임으로 스케줄링 | 단말당 평균 대기 시간, 재전송 횟수 |
| RTS/CTS 제어 오버헤드 | 소형 패킷에서는 제어 프레임 교환 시간이 데이터 전송 시간보다 길어져 대역폭 낭비 | RTS 임계치(RTS Threshold)를 조정해 일정 크기 이상의 패킷에만 RTS/CTS 적용 | 제어 프레임 비율, 패킷 크기 분포 |

## Ⅵ. CSMA/CA에 대한 기술사적 제언

- 핵심 요약 : 경쟁 방식과 스케줄링 방식의 공존, 현장 단위의 파라미터 관리, 공간 재사용 정책의 검증을 갖춰야 무선랜 품질을 장기적으로 유지할 수 있음.
- 무선랜 운영자는 Wi-Fi 6/7 환경에서 레거시 단말과의 공존을 위해 CSMA/CA를 기본으로 유지하되, 고성능 단말 구간에는 AP 중심의 스케줄링 비중을 점진적으로 높이는 설계를 택하는 것이 바람직하다.
- 간섭이 심한 대강당이나 물류창고를 운영하는 조직은 파라미터 변경 이력과 재전송률을 함께 기록하는 운영 절차를 두어, 임계치 조정의 효과를 장기적으로 추적하는 것이 필요하다.
- 공간 재사용(BSS Coloring) 정책을 쓰는 조직은 간섭 세기에 따라 동시 전송을 허용하는 기능을 현장 검증 후에 도입해, 노출 노드로 인한 손실을 완화하는 방향으로 나아가는 것이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : CSMA/CA는 무선 매체에서 충돌을 검출할 수 없는 한계를 회피 기법과 가상 타이머로 보완한 분산 접근 프로토콜임.
- 시사점 : 고밀도 환경에서는 경쟁 방식의 한계가 드러나므로, 경쟁 방식과 스케줄링 방식을 함께 쓰는 무선랜 설계가 기본 방향이 됨.
