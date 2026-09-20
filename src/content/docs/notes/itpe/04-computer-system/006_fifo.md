---
title: "FIFO(First In First Out)"
author: "Codex"
date: "2026-09-20T19:50:48+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 19:50 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>자원 스케줄링</span><span>큐잉 규율</span><strong>FIFO</strong></div>

## 큰 그림과 30초 인출

- 본질: 도착 순서만으로 단일 대기열의 Head를 서비스하는 비선점 큐잉 규율임
- 메커니즘: Tail Enqueue → Head Dequeue → 선두 작업 완료 후 다음 작업 처리
- 산출: 구현 단순성과 순서 공평성을 얻지만 작업 크기·우선순위·지연 민감도를 구분하지 않아 Convoy Effect가 발생함

<div class="itpe-flow itpe-flow--vertical" aria-label="FIFO 큐 처리 흐름">
  <div class="itpe-flow__node"><strong>도착</strong><small><b>입력:</b> 패킷 · 프로세스 · I/O 요청</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Tail Enqueue</strong><small><b>처리:</b> 도착 순서대로 단일 큐 끝에 삽입</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Head Dequeue</strong><small><b>판정:</b> 우선순위 없이 가장 먼저 도착한 항목 선택</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>비선점 서비스</strong></span><small><b>산출:</b> 완료 후 다음 Head 처리</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- `FIFO(First In First Out)`: 먼저 들어온 항목을 먼저 내보내는 순서 규율 → 서비스 시간·긴급도는 판단하지 않음
- `Enqueue·Dequeue`: Tail 삽입과 Head 제거 연산 → 큐의 도착 순서를 보존
- `FCFS(First Come First Served)`: CPU 작업에 적용한 FIFO 스케줄링 → 비선점 실행과 긴 작업 영향을 고려
- `Convoy Effect(호위 효과)`: 긴 선두 작업 뒤의 짧은 작업이 함께 지연됨 → 순서 공평성과 지연 공평성을 구분
- `WFQ(Weighted Fair Queuing)`: Flow별 가상 완료시간과 가중치로 서비스 순서를 정함 → 차등 대역폭과 격리를 제공

</details>

## 예상문제

- FIFO 방식의 구조와 동작, 특징 및 한계를 설명하고 WFQ 방식과 비교한 후 지연 민감 트래픽의 큐잉 개선방안을 제시하시오.

## Ⅰ. 도착 순서를 보존하는 FIFO 개요

> FIFO는 예측 가능한 순서와 낮은 스케줄링 비용을 제공하지만, 서비스 시간과 업무 긴급도를 무시하므로 이질적 부하에서는 공평하지 않음.

- 정의: 항목을 **Tail에 Enqueue**하고 **Head에서 Dequeue**하여 도착 순서대로 **비선점 처리**하는 큐잉 규율
- 목적: 재정렬 없는 단순 스케줄링 → 순서 보존과 낮은 관리 복잡도

| 특징 | 메커니즘 | 결과 |
|---|---|---|
| 선입선출 | 도착 순서 고정 | 순서 예측 가능 |
| 비선점 | 선두 작업 완료까지 유지 | 긴 작업 영향 확대 |
| 단일 큐 | Class·Flow 미구분 | 구현·관리 단순 |
| 순서 공평 | 먼저 온 항목 우선 | 지연·대역폭 보장 없음 |

## Ⅱ. FIFO의 처리 구조와 한계 발생 원리

> 긴 선두 작업은 뒤의 모든 항목에 지연을 전파하므로, 평균 부하보다 작업 크기 분산과 지연 민감도 혼합이 성능을 좌우함.

<div class="itpe-flow itpe-flow--vertical" aria-label="FIFO 호위 효과 발생 흐름">
  <div class="itpe-flow__node"><strong>혼합 부하 도착</strong><small><b>활동:</b> 긴 작업 뒤에 짧은 작업·긴급 패킷 Enqueue</small><small><b>산출:</b> 도착 순서 단일 큐</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>선두 작업 점유</strong><small><b>활동:</b> 비선점 방식으로 서비스 완료까지 자원 사용</small><small><b>산출:</b> 후속 작업 대기</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>Convoy Effect</strong></span><small><b>판정:</b> 짧거나 긴급한 항목도 선두 완료 전 처리 불가</small><small><b>산출:</b> 응답지연 증가와 QoS 미보장</small></div>
</div>

- 적용 구분: CPU에서는 FCFS, 네트워크에서는 단일 패킷 큐, 페이지 교체에서는 가장 오래 적재된 Page 교체로 같은 순서 원리를 사용함
- 주의: FIFO 페이지 교체의 **Belady's Anomaly**는 Frame 증가에도 Page Fault가 늘 수 있는 별도 현상이며 네트워크 FIFO의 일반 속성으로 혼합하지 않음

## Ⅲ. FIFO와 WFQ 비교

> FIFO는 전체 도착 순서, WFQ는 Flow별 공정성과 가중치를 기준으로 하므로 트래픽 Class가 섞일수록 선택 결과가 달라짐.

| 축 | FIFO | WFQ |
|---|---|---|
| Queue | 단일 | Flow·Class별 분리 |
| 기준 | 도착 순서 | 가중치·가상 완료시간 |
| 대역폭 | 차등 없음 | 가중치 비례 배분 |
| 격리 | 선두 Flow 영향 전파 | Flow 간 영향 완화 |
| 지연 | 보장 없음 | 저용량 Flow 지연 완화 |
| 복잡도 | 낮음 | 분류·상태·계산 필요 |
| 적합 | 동질 부하·단순 장치 | 혼합 QoS 트래픽 |

## Ⅳ. 혼잡·지연의 원인과 개선방안

> 큐를 크게 만드는 것만으로 손실은 늦출 수 있지만 체류시간을 늘릴 수 있으므로, 분류·공정 큐잉·능동 큐 관리가 함께 필요함.

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 긴급 트래픽 지연 | 단일 큐·우선순위 미구분 | WFQ·Priority Queue | Class별 지연 차등 |
| Bufferbloat | 과도한 FIFO Buffer | **AQM(Active Queue Management)** | 큐 체류시간 억제 |
| Flow 독점 | 대용량 Flow의 연속 도착 | Flow별 큐 분리·가중치 | 영향 격리 |
| 기아 위험 | 절대 우선순위만 적용 | 최소 대역폭·Aging | 하위 Class 진행 보장 |

- 적용 판단: 트래픽이 동질적이고 순서 자체가 중요하면 FIFO, 지연·대역폭 SLA가 다르면 Class 기반 큐잉을 선택

## Ⅴ. 측정 기반 큐잉 규율 결론

> 큐잉 규율은 처리량만의 문제가 아니라 지연을 누구에게 배분할지 결정하는 정책이므로 Flow 분포와 SLA를 기준으로 검증해야 함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: FIFO는 기아를 줄이지만 모든 항목을 동일하게 대우할 뿐 서비스 시간과 긴급도를 반영하지 않으므로 결과의 공평성까지 보장하지 않는다.
- `나라면`: 기본 FIFO의 큐 체류시간과 Flow별 지연을 먼저 측정하고, 혼합 트래픽 구간에만 WFQ와 AQM을 단계적으로 적용하겠다.

### 실전 답안용 기술사적 제언

- 판정: 작업 크기 분산, Class별 지연 목표, Flow 독점 여부로 FIFO 적합성 판단
- 대안: Flow 분류·WFQ·AQM을 결합하고 최소 대역폭으로 기아 방지
- 검증: Class별 큐 체류시간, 손실, 처리량, 장기 대기 비교
- 효과: 단순성은 필요한 구간에 유지하고 호위 효과와 Bufferbloat는 혼합 부하 구간에서 격리

<div class="itpe-flow itpe-flow--vertical" aria-label="FIFO 큐잉 개선 흐름">
  <div class="itpe-flow__node"><strong>현행 한계</strong><small><b>문제:</b> 단일 FIFO에서 긴 Flow와 지연 민감 Flow 혼재</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Flow 분류</strong><small><b>대안:</b> Class별 큐 · 가중치 · 최소 대역폭</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>큐 능동 통제</strong><small><b>대안:</b> WFQ와 AQM으로 독점·체류시간 억제</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>SLA 검증</strong><small><b>판정:</b> Class별 지연·손실·처리량 충족</small><small><b>효과:</b> QoS와 기아 방지의 균형</small></div>
</div>

## 1교시 10점 답안 발췌

- 정의: 항목을 **Tail에 Enqueue**하고 **Head에서 Dequeue**하여 도착 순서대로 **비선점 처리**하는 FIFO(First In First Out) 큐잉 규율
- 목적: 재정렬 없는 단순 스케줄링 → 순서 보존과 낮은 관리 복잡도

<div class="itpe-flow itpe-flow--vertical" aria-label="FIFO 1교시 흐름">
  <div class="itpe-flow__node"><strong>Enqueue</strong><small><b>활동:</b> Tail에 도착 순서 삽입</small><small><b>산출:</b> 단일 대기열</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Dequeue</strong><small><b>활동:</b> Head 항목 선택</small><small><b>산출:</b> 비선점 서비스</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Convoy Effect</strong><small><b>판정:</b> 긴 선두 작업이 후속 지연 전파</small></div>
</div>

- 비교: FIFO는 단일 큐·도착 순서·낮은 복잡도, **WFQ(Weighted Fair Queuing)**는 Flow별 큐·가중치·대역폭 차등
- 결론: 혼합 QoS 트래픽에는 WFQ와 AQM을 결합하고 Class별 지연·기아를 검증

## 출제 이력과 검증 출처

- 제140회 정보관리기술사 2교시 5번: `FIFO(First In First Out) 방식과 웨이티드 페어큐잉(Weighted Fair Queuing) 방식을 비교 설명하시오.`
- [IETF RFC 2212, Specification of Guaranteed Quality of Service](https://www.rfc-editor.org/rfc/rfc2212)
- [IETF RFC 2309, Recommendations on Queue Management and Congestion Avoidance](https://www.rfc-editor.org/rfc/rfc2309)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 학습 체크

- [ ] Ⅰ 개요: Enqueue·Dequeue·비선점과 네 가지 특징을 재현할 수 있는가?
- [ ] Ⅱ 원리: 긴 선두 작업이 후속 지연을 만드는 Convoy Effect 흐름을 그릴 수 있는가?
- [ ] Ⅲ 비교: FIFO와 WFQ를 Queue·기준·대역폭·격리·지연·복잡도로 비교할 수 있는가?
- [ ] Ⅳ 개선: 긴급 지연·Bufferbloat·Flow 독점·기아의 원인과 대책을 연결할 수 있는가?
- [ ] Ⅴ 제언: 적합성 판정·Flow 분류·WFQ/AQM·SLA 검증 흐름을 설명할 수 있는가?

## 연결 토픽

- [WFQ](../../05-network/008_wfq/) · [CPU 스케줄링](./019_cpu_scheduling/) · [디스크 스케줄링](./024_disk_scheduling/) · [가상 메모리](./023_virtual_memory/)
