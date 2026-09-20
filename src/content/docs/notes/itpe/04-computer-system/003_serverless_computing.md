---
title: "서버리스 컴퓨팅(Serverless Computing)"
author: "Codex"
date: "2026-09-20T20:01:14+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 20:01 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>클라우드 컴퓨팅</span><span>클라우드 실행 모델</span><strong>서버리스 컴퓨팅</strong></div>

## 큰 그림과 30초 인출

- 본질: 서버가 없는 기술이 아니라 공급자가 실행 인프라의 프로비저닝·확장·운영을 맡는 클라우드 실행 모델임
- 메커니즘: 이벤트 수신 → **FaaS** 함수 실행 → **BaaS** 상태·공통 기능 연계 → 실행량 계측
- 산출: 부하 변화에 민첩한 서비스이며, 대가는 Cold Start·상태 외부화·벤더 종속·분산 관측 복잡성임

<div class="itpe-flow itpe-flow--vertical" aria-label="서버리스 실행 구조">
  <div class="itpe-flow__node"><strong>이벤트 소스</strong><small><b>입력:</b> HTTP · 메시지 · 파일 · 스케줄</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>이벤트 라우터</strong><small><b>처리:</b> 인증 · 트리거 · 라우팅</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>FaaS</strong></span><small><b>처리:</b> 실행환경 준비 · 함수 실행 · 자동 확장</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>BaaS</strong></span><small><b>산출:</b> DB · 객체 · 인증 · 메시징 연계 결과</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>관측·계측</strong><small><b>통제:</b> 로그 · 추적 · 메트릭 · 사용량</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- `FaaS(Function as a Service)`: 이벤트마다 함수 실행환경을 제공하는 계산 계층 → 짧은 수명과 실행 제한을 고려
- `BaaS(Backend as a Service)`: 인증·DB·메시징 등 공통 백엔드를 관리형 서비스로 제공 → 서비스 결합도를 통제
- `Cold Start`: 유휴 상태에서 실행환경을 새로 준비하며 생기는 초기 지연 → 지연 민감 업무를 가르는 기준
- `Stateless`: 함수 내부 상태에 다음 호출이 의존하지 않는 설계 → 상태를 외부 저장소로 이동
- `Idempotency(멱등성)`: 같은 이벤트가 반복돼도 결과가 달라지지 않는 성질 → 재시도 중복을 차단

</details>

## 예상문제

- 서버리스 컴퓨팅의 개념과 특징, FaaS·BaaS 기반 구성 및 동작을 설명하고, VM·컨테이너와 비교하여 도입 고려사항을 제시하시오.

## Ⅰ. 운영 책임을 추상화한 서버리스 컴퓨팅 개요

> 서버리스의 가치는 서버 제거가 아니라 운영 책임 경계의 이동이며, 업무가 이벤트 기반·무상태로 분해될 때 효과가 커짐.

- 정의: 클라우드 공급자가 **프로비저닝**, **자동 확장**, **실행환경 운영**을 담당하고 이용자가 이벤트 기반 코드와 관리형 서비스를 조합하는 실행 모델
- 목적: 인프라 운영 책임 위임 → 변동 부하 대응과 업무 로직 집중

| 특징 | 메커니즘 | 설계 의미 |
|---|---|---|
| **Event-driven** | 트리거별 함수 호출 | 이벤트 계약이 결합도 결정 |
| **Auto Scaling** | 동시 요청에 따라 인스턴스 증감 | 폭주·하위 서비스 한도 통제 |
| **Metering** | 호출·실행 자원 계측 | 유휴 비용 감소, 단위비용 변동 |
| **Stateless** | 실행환경 수명과 상태 분리 | DB·캐시로 상태 외부화 |

## Ⅱ. FaaS·BaaS 기반 구성과 실행 흐름

> FaaS는 계산, BaaS는 상태와 공통 기능을 맡으며, 재시도·실패 경로까지 이벤트 계약에 포함해야 운영 가능한 구조가 됨.

<div class="itpe-flow itpe-flow--vertical" aria-label="서버리스 처리 절차">
  <div class="itpe-flow__node"><strong>이벤트 계약</strong><small><b>활동:</b> 스키마 · 인증 · 라우팅 규칙 정의</small><small><b>산출:</b> 트리거와 실패 정책</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>실행환경 준비</strong><small><b>활동:</b> 런타임 로드 · 인스턴스 할당</small><small><b>산출:</b> 실행 가능한 함수 컨텍스트</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>함수·백엔드 실행</strong><small><b>활동:</b> <span class="itpe-keyword"><strong>FaaS</strong></span> 로직 · <span class="itpe-keyword"><strong>BaaS</strong></span> 상태 연계</small><small><b>산출:</b> 결과 또는 재시도 이벤트</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>관측·회수</strong><small><b>활동:</b> 로그 · 분산추적 · 메트릭 기록</small><small><b>산출:</b> 실행량·오류·지연과 유휴 환경 회수</small></div>
</div>

- 횡단 통제: 함수별 최소권한, Secret 분리, 상관 ID, Timeout, 재시도 제한, **DLQ(Dead Letter Queue)** 적용

## Ⅲ. VM·컨테이너·서버리스 비교

> 실행 단위가 작아질수록 운영 부담은 공급자로 이동하지만 실행 제약과 플랫폼 결합은 커지므로 업무 수명·지연·이식성으로 선택해야 함.

| 축 | VM | 컨테이너 | 서버리스 함수 |
|---|---|---|---|
| 단위 | Guest OS 이미지 | 애플리케이션 이미지 | 함수·의존성 |
| 책임 | OS 이상 이용자 관리 | 오케스트레이션 관리 | 실행환경 공급자 관리 |
| 확장 | VM | Pod·Task | 호출·함수 인스턴스 |
| 상태 | 장기 상태 가능 | 외부화 권장 | 외부화 원칙 |
| 적합 | 강한 격리·레거시 | 장기 서비스·이식성 | 간헐·급변 이벤트 |
| 대가 | 기동·유휴 자원 | 플랫폼 운영 | Cold Start·종속 |

## Ⅳ. 한계의 원인과 도입 통제

> 서버리스 장애는 함수 코드보다 재시도·동시성·관리형 서비스 사이에서 확산되므로 E2E 관측과 실패 격리가 핵심임.

| 문제 | 원인 | 대책 | 검증 |
|---|---|---|---|
| 초기 지연 | 런타임·의존성 준비 | 경량 패키지·사전 준비 | 지연 분포 |
| 중복 처리 | 비동기 전달·재시도 | **멱등키**, 조건부 쓰기·DLQ | 중복·실패 이벤트 |
| 연쇄 장애 | 동시성 폭주·하위 한도 | 동시성 제한·Backpressure | 오류 전파 경로 |
| 관측 단절 | 다수 함수·관리형 서비스 | 상관 ID·분산추적 | 추적 완결성 |
| 종속·비용 | 전용 API·전송·호출 계측 | Port·Adapter 경계·Exit Plan | 이동성·단위비용 |

## Ⅴ. 이벤트 계약과 운영 통제를 결합하는 결론

> 서버리스 도입은 함수 변환 프로젝트가 아니라 이벤트 계약·실패 의미·운영 책임을 다시 설계하는 아키텍처 결정임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 자동 확장은 계산 계층만 빠르게 늘릴 뿐 DB와 외부 API의 수용량까지 늘리지 않으므로 동시성 제한이 안정성 장치가 된다.
- `나라면`: 짧고 무상태인 이벤트 업무를 파일럿으로 선정하고, 멱등성·분산추적·단위비용을 통과한 뒤 범위를 넓히겠다.

### 실전 답안용 기술사적 제언

- 판정: 이벤트 독립성, 지연 허용도, 상태 외부화 가능성으로 적합성 판정
- 대안: 멱등키·동시성 제한·DLQ·상관 ID를 공통 실행 Baseline으로 적용
- 검증: E2E 지연, 중복 결과, 실패 이벤트, 하위 서비스 포화, 단위비용을 함께 관찰
- 효과: 자동 확장의 장애 증폭을 막고 민첩성과 운영가능성을 동시 확보

<div class="itpe-flow itpe-flow--vertical" aria-label="서버리스 도입 개선 흐름">
  <div class="itpe-flow__node"><strong>현행 한계</strong><small><b>문제:</b> 함수 중심 전환으로 실패·상태·관측 누락</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>이벤트 Baseline</strong><small><b>대안:</b> 멱등성 · 동시성 · DLQ · 상관 ID 표준화</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>파일럿 검증</strong><small><b>판정:</b> 지연 · 중복 · 포화 · 비용의 허용 여부</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>단계 확산</strong><small><b>효과:</b> 장애 격리와 운영 책임의 명확화</small></div>
</div>

## 1교시 10점 답안 발췌

- 정의: 공급자가 **프로비저닝·Auto Scaling·실행환경 운영**을 담당하고 이용자가 이벤트 기반 **FaaS(Function as a Service)**와 **BaaS(Backend as a Service)**를 조합하는 클라우드 실행 모델
- 목적: 서버 운영 책임 위임 → 변동 부하 대응과 업무 로직 집중

<div class="itpe-flow itpe-flow--vertical" aria-label="서버리스 1교시 구조">
  <div class="itpe-flow__node"><strong>Event</strong><small><b>입력:</b> HTTP · 메시지 · 파일 · 스케줄</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>FaaS</strong><small><b>처리:</b> 함수 실행 · 자동 확장</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>BaaS</strong><small><b>산출:</b> 상태 · 인증 · 메시징 연계</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Observability</strong><small><b>통제:</b> 로그 · 메트릭 · 분산추적</small></div>
</div>

- 장점: 이벤트별 탄력 실행, 인프라 관리 감소, 유휴 자원 축소
- 한계: Cold Start, 상태 외부화, 벤더 종속, 분산 관측 복잡성

| 축 | VM | 컨테이너 | 서버리스 함수 |
|---|---|---|---|
| 단위 | Guest OS | 이미지 | 함수·이벤트 |
| 운영 | OS부터 이용자 책임 | 오케스트레이션 필요 | 실행환경 공급자 책임 |
| 적합 | 레거시·강한 격리 | 장기 서비스 | 간헐·급변 부하 |

| 문제 | 원인 | 대책 |
|---|---|---|
| 중복 처리 | 이벤트 재시도 | 멱등키·조건부 쓰기 |
| 연쇄 장애 | 무제한 동시성 | 동시성 제한·DLQ |
| 관측 단절 | 분산 함수 호출 | 상관 ID·분산추적 |

- 결론: 멱등성·동시성 제한·DLQ를 이벤트 계약과 함께 설계

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 1교시 9번: `서버리스 컴퓨팅(Serverless Computing)`
- 제140회 정보관리기술사 2교시 1번: `서버리스 컴퓨팅(Serverless Computing)에 대하여 다음을 설명하시오. 가. 정의 및 특징 나. 구성 요소 및 장·단점`
- [CNCF Serverless Whitepaper](https://github.com/cncf/wg-serverless/tree/master/whitepapers/serverless-overview)
- [Google Cloud — What is serverless computing?](https://cloud.google.com/discover/what-is-serverless-computing)
- [Google Cloud — What is FaaS?](https://cloud.google.com/discover/what-is-function-as-a-service-faas)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 학습 체크

- [ ] Ⅰ 개요: 서버가 없다는 뜻이 아니라 운영 책임 경계가 이동한다는 정의와 네 특징을 재현할 수 있는가?
- [ ] Ⅱ 구조: Event·Router·FaaS·BaaS·관측의 흐름과 각 단계 활동·산출을 그릴 수 있는가?
- [ ] Ⅲ 비교: VM·컨테이너·서버리스를 실행 단위·책임·확장·상태·적합 업무로 비교할 수 있는가?
- [ ] Ⅳ 통제: Cold Start·중복·연쇄 장애·관측·종속의 원인과 대책을 1:1로 연결할 수 있는가?
- [ ] Ⅴ 제언: 적합성 판정부터 Baseline·파일럿·단계 확산까지 설명할 수 있는가?

## 연결 토픽

- [클라우드 컴퓨팅](./013_cloud_computing/) · [FaaS](./078_faas/) · [컨테이너](./032_container/) · [클라우드 서비스 모델](./109_cloud_computing_service_models/)
