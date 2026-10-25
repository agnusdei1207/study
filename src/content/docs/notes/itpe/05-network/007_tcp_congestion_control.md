---
title: "TCP 혼잡제어(TCP Congestion Control) (TCP: Transmission Control Protocol)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- TCP 혼잡제어(TCP Congestion Control), CWND(Congestion Window), AIMD(Additive Increase Multiplicative Decrease)
- 슬로우 스타트(Slow Start), 혼잡 회피(Congestion Avoidance), 빠른 재전송(Fast Retransmit), 빠른 복구(Fast Recovery)
- 혼잡 붕괴(Congestion Collapse), 버퍼블로트(Bufferbloat), 공평성(Fairness), BDP(Bandwidth-Delay Product)
- TCP Reno, CUBIC, BBR(Bottleneck Bandwidth and Round-trip propagation time), DCTCP(Data Center TCP), ECN(Explicit Congestion Notification), AQM(Active Queue Management)

## Ⅰ. TCP 혼잡제어의 개요

- 핵심 요약 : 라우터 버퍼 과부하를 막기 위해 송신단이 전송량을 동적으로 조절하는 전송 계층의 종단 간 제어 기법.
- 개념 : 전송 제어 프로토콜인 TCP(Transmission Control Protocol)의 송신단이 네트워크 혼잡 신호에 따라 **혼잡 윈도우** (CWND, Congestion Window) 크기를 조절해 망에 주입하는 트래픽 양을 통제하는 기법 (**TCP 혼잡제어**, TCP Congestion Control).
- 배경 및 필요성 : 1986년 인터넷에서 손실 패킷의 무분별한 재전송으로 망 전체 처리량이 급락하는 **혼잡 붕괴** (Congestion Collapse) 사례가 보고되었고, 자원의 안정적 배분을 위한 제어가 필수가 됨.
- 주요 목적 : 가용 대역폭의 최대 활용, 연결 간 **공평성** (Fairness) 보장, 큐 적체로 인한 **버퍼블로트** (Bufferbloat, 과대 버퍼가 만드는 지연 증가) 억제.

## Ⅱ. TCP 혼잡제어의 특징 및 장점

- 핵심 요약 : 손실과 지연 신호에 따라 윈도우를 조절하는 원리가 망의 안정성과 연결 간 공평성으로 이어지는 구조.

1. **AIMD** (Additive Increase Multiplicative Decrease, 가산 증가·승법 감소) : 정상 상태에서 왕복 시간마다 완만히 늘리고 손실 시 절반으로 줄임 → 여러 연결이 대역을 공평하게 나누며 안정 수렴.
2. **슬로우 스타트** (Slow Start) : 연결 초기나 타임아웃 이후 CWND를 작은 값에서 왕복 시간마다 두 배로 키움 → 비어 있는 대역을 짧은 시간에 탐색.
3. **혼잡 회피** (Congestion Avoidance) : CWND가 혼잡 임계치에 도달하면 선형 증가로 전환 → 과부하 직전에서 속도를 완만하게 유지.
4. **빠른 재전송** (Fast Retransmit)과 **빠른 복구** (Fast Recovery) : 확인 응답이 중복 3회 도착하면 손실로 보고 즉시 재전송하며 윈도우를 절반으로 낮춰 전송 지속 → 타임아웃 대기로 인한 처리량 급락 방지.

## Ⅲ. TCP 혼잡제어의 구조 (흐름)

- 핵심 요약 : 슬로우 스타트, 혼잡 회피, 손실 복구가 CWND의 상태 전이를 이끌고, 망 상태가 ACK를 통해 송신단에 되돌아오는 피드백 루프의 이중 구조.
- 혼잡 임계치 : 슬로우 스타트 구간과 혼잡 회피 구간을 나누는 기준값이며 손실 발생 시 갱신됨.
- 피드백 신호 : 망의 상태는 ACK 도착 타이밍, 중복 ACK, 타임아웃 형태로만 송신단에 전달됨.

```text
[ 전통적 혼잡제어 상태 전이 ]

연결 시작 또는 타임아웃
    ↓
슬로우 스타트 (지수 증가)
    ↓ 임계치 도달
혼잡 회피 (선형 증가)
    ↓ 중복 ACK 3회 감지
빠른 재전송 → 빠른 복구
    ↓
윈도우 절반 후 혼잡 회피 복귀
```

```text
[ 혼잡 피드백 루프 ]

송신단 전송 (CWND 크기만큼)
    ↓
라우터 큐 적체 또는 손실
    ↓
ACK 지연·중복 ACK 수신
    ↓
송신단의 CWND 재조정
```

## Ⅳ. TCP 혼잡제어 알고리즘의 비교

- 핵심 요약 : 혼잡 신호가 패킷 손실에서 대역폭·지연 측정과 큐 표시로 옮겨 가며 알고리즘이 다변화됨.
- 비교 대상 : 손실 기반의 TCP Reno와 **CUBIC** (리눅스 기본 알고리즘으로 시간 기준 3차 함수형 윈도우 증가를 쓰는 알고리즘), 측정 기반의 **BBR** (Bottleneck Bandwidth and Round-trip propagation time), 큐 표시 기반의 **DCTCP** (Data Center TCP).

| 비교 축 | TCP Reno | CUBIC | BBR | DCTCP |
| --- | --- | --- | --- | --- |
| 혼잡 신호 | 패킷 손실 | 패킷 손실 | 대역폭과 최소 RTT(Round-Trip Time) 측정 | 스위치 큐 표시 |
| 윈도우 증가 방식 | 선형 증가 (AIMD) | 시간 기준 3차 함수 곡선 | 전송률 모델 기반 | 표시 비율에 비례한 감소 |
| 고속·장거리망 적응 | 회복이 느려 취약 | 빠른 대역폭 회복 | 손실과 무관하게 동작 | 데이터센터 내부에 특화 |
| 버퍼블로트 내성 | 취약 | 취약 | 큐 적체를 줄이는 편 | 우수 |
| 주요 사용 환경 | 레거시·교육용 기준 | 리눅스 계열의 기본값 | 대형 웹·영상 서비스 | 사설 데이터센터 내부망 |

- 용어 : **ECN** (Explicit Congestion Notification, 명시적 혼잡 통지)은 스위치가 큐 임계치 초과 시 패킷에 표시를 남겨 손실 이전에 송신단에 혼잡을 알리는 방식임.
- 선택 기준 : **대역폭 지연 곱** (BDP, Bandwidth-Delay Product)이 큰 환경은 Reno 대신 CUBIC·BBR이 유리하고, 낮은 지연과 급격한 버스트가 공존하는 데이터센터 내부는 DCTCP가 적합함.

## Ⅴ. TCP 혼잡제어의 한계와 방안

- 핵심 요약 : 큐 적체 지연, 무선 구간의 오판, 고속 장거리망의 느린 회복을 큐 관리와 알고리즘 전환, 측정 기반 모델로 통제.
- 대응 기법 : **AQM** (Active Queue Management, 능동 큐 관리)을 라우터에 두면 큐 지연을 송신단 알고리즘과 별개로 줄일 수 있음.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 손실 기반 알고리즘의 버퍼블로트 | 버퍼가 찰 때까지 윈도우를 키워 손실은 없고 지연만 증가 → 실시간 서비스 품질 저하 | CoDel, FQ-CoDel, PIE 같은 AQM 도입과 송신단의 BBR 전환 | 큐 지연, RTT 변동폭 |
| 무선 구간의 손실 오판 | 무선 페이딩 손실을 혼잡으로 판단해 윈도우가 급감 → 처리량 저하 | 대역폭·지연 모델을 추정하는 BBR 적용, 링크 계층 재전송과의 연계 | 재전송률, 처리량 추이 |
| 고속 장거리망의 느린 회복 | 손실 후 선형 증가가 원래 속도 회복에 긴 시간 소요 → 대역 활용률 저하 | CUBIC의 시간 기반 증가 곡선, 패킷 페이싱(Packet Pacing) 적용 | 대역 활용률, 손실 후 회복 시간 |

## Ⅵ. TCP 혼잡제어에 대한 기술사적 제언

- 핵심 요약 : 알고리즘 표준화, 공동 운영 체계, 전송 프로토콜 유연성 확보의 세 방향으로 혼잡제어를 운영 역량으로 관리.

1. 서비스 운영 조직은 서비스 유형별 허용 혼잡제어 알고리즘을 표준화하고, 지연·재전송 지표를 근거로 교체 여부를 판단하는 거버넌스 절차를 갖추어야 한다.
2. 데이터센터 운영 조직은 네트워크 팀과 서버·AI 인프라 팀이 스위치의 ECN 임계치와 송신단 혼잡제어 파라미터를 공동 관리하는 협업 체계를 두어야 한다.
3. 아키텍처 설계 조직은 사용자 공간에서 알고리즘 교체가 가능한 QUIC 계열 전송 방식의 확산을 반영해, 신규 서비스 설계 기준에 전송 프로토콜과 혼잡제어의 유연성 항목을 포함해야 한다.

## Ⅶ. 결론

- 핵심 요약 : TCP 혼잡제어는 망 상태 신호를 읽어 윈도우를 조절하는 분산형 대역 배분 메커니즘임.
- 시사점 : 손실 신호만으로는 지연과 대역폭 특성이 다른 현대 망을 설명하기 어려워 측정 기반 모델과 큐 관리를 함께 쓰는 방향으로 진화 중임.
