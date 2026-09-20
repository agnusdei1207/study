---
title: "순차 다이어그램(Sequence Diagram)"
category: "02-software-engineering"
tags:
  - "UML"
  - "순차다이어그램"
  - "시퀀스다이어그램"
  - "복합프래그먼트"
  - "상호작용모델링"
  - "DiagramAsCode"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 객체지향 분석·설계 및 UML을 거쳐 순차 다이어그램으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>객체지향 분석·설계·UML</span>
  <strong>순차 다이어그램(Sequence Diagram)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 시스템 컴포넌트나 객체 간의 메서드 호출 순서와 생명주기를 파악하기 위해, 수평축에 참여 객체를 배치하고 수직축(시간 경과)을 따라 동기·비동기 메시지와 조건부 제어 흐름을 가시화하는 UML 동적 모델링 기법
- 메커니즘: 액터 및 객체 생명선(Lifeline) 정의 → 동기/비동기 메시지 전송 및 활성 구간(Activation Box) 실행 → 복합 프래그먼트(`alt`, `opt`, `loop`, `par`) 제어 분기 → 반환 메시지 회신
- 산출물: UML 순차 다이어그램(또는 PlantUML/Mermaid 코드) · API 상호작용 명세서 · 서비스 간 통신 시퀀스 정의서

<div class="itpe-flow-map" role="img" aria-label="순차 다이어그램의 메시지 송수신 및 제어 흐름 메커니즘">
  <div class="itpe-flow-node">
    <strong>1단계: 참여 객체 및 생명선(Lifeline) 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구성</strong><span>가로축에 액터 및 서비스/객체 인스턴스 나열 (상단 사각형 + 수직 점선)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 메시지 송수신 및 활성(Activation)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>유형</strong><span>동기 호출(실선+채운삼각형) · 비동기 호출(실선+열린화살표) · 반환(점선)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>3단계: 복합 프래그먼트 제어 구조화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>키워드</strong><span><code>alt</code>(조건분기) · <code>opt</code>(선택) · <code>loop</code>(반복) · <code>par</code>(병렬) · <code>ref</code>(참조)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 객체 소멸 및 완료</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>종료</strong><span>생명선 하단에 소멸자(X) 표기 또는 기본 수명 종료</span></div>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **생명선(Lifeline)**: 다이어그램 수평축 상단에 위치한 객체 사각형 아래로 뻗은 수직 점선으로, 해당 객체가 시스템 내에 존재하는 시간 경과를 표현
- **활성 상자(Activation Box)**: 생명선 위에 그려지는 좁은 직사각형으로, 객체가 실제 연산을 수행 중이거나 제어권을 점유하고 있는 실행 상태를 의미
- **복합 프래그먼트(Combined Fragment)**: UML 2.0에서 도입된 상호작용 제어 블록으로, 조건 분기(`alt`), 반복(`loop`), 병렬 처리(`par`) 등 복잡한 알고리즘 제어를 다이어그램 내에 구조화
- **Diagram as Code(DaC)**: 마우스 기반 드로잉 도구 대신 PlantUML, Mermaid 등 텍스트 코드로 다이어그램을 작성하여 Git 저장소에서 소스코드와 함께 버전 관리하는 기법
</details>

## 1. 개요 및 필요성

### 동적 상호작용 모델링의 필요성

클래스 다이어그램은 시스템의 정적인 구조와 관계(상속, 연관, 합성)를 잘 보여주지만, "실제 특정 기능(유스케이스)이 실행될 때 어떤 객체가 어떤 순서로 메서드를 호출하고 응답을 기다리는가?"라는 런타임 제어 흐름을 설명하지 못한다. 텍스트로 된 유스케이스 명세서 역시 복잡한 조건 분기나 비동기 메시지 교환을 명확히 전달하는 데 한계가 있다.

순차 다이어그램은 **시간의 흐름(위에서 아래로)에 따른 객체 간 상호작용을 2차원 평면에 명확히 시각화**하여, 비즈니스 로직의 호출 순서, 동기/비동기 지연 시간, 결합도, 분산 환경에서의 통신 병목을 설계 단계에서 검증할 수 있게 한다.

### 순차 다이어그램 vs 통신 다이어그램 비교

| 구분 | 순차 다이어그램 (Sequence Diagram) | 통신 다이어그램 (Communication Diagram) |
|---|---|---|
| **표현 초점** | 메시지의 **시간적 순서와 생명주기** | 객체들 간의 **공간적 링크 및 네트워크 관계** |
| **시간 흐름 표기** | 수직축(위 $\rightarrow$ 아래)으로 직관적 파악 가능 | 링크 선 위에 순서 번호(1, 1.1, 2)를 붙여 추적 |
| **공간적 연결 관계** | 객체가 가로로 나열되어 복잡한 링크 파악 어려움 | 객체 간 메시지 경로 및 결합 관계 파악 용이 |
| **주요 활용 단계** | API 호출 시퀀스, 마이크로서비스 간 트랜잭션 설계 | 아키텍처 초기 객체 간 협력 관계 및 결합도 분석 |

## 2. 아키텍처 및 핵심 메커니즘

### 순차 다이어그램 핵심 구성요소 및 표기법

```text
+-------------------------------------------------------------------------+
|                  순차 다이어그램(Sequence Diagram) 핵심 표기법           |
+-------------------------------------------------------------------------+
|  [ :Client ]              [ :OrderService ]         [ :PaymentGateway ] |
|      │                           │                           │          |
|      │ 1: createOrder() (동기)   │                           │          |
|      │ ─────────────────────────>│ (활성 구간)               │          |
|      │                           │                           │          |
|      │                           │ 2: requestPayment()       │          |
|      │                           │ ─────────────────────────>│          |
|      │                           │                           │          |
|  +───[ alt : 결제 결과 조건 분기 ]┼───────────────────────────┼────────+ |
|  │ [결제 성공]                   │                           │        │ |
|  │   │                           │ 3: 200 OK (반환 메시지)   │        │ |
|  │   │                           │ < - - - - - - - - - - - - │        │ |
|  │   │ 4: orderSuccess()         │                           │        │ |
|  │   │ < - - - - - - - - - - - - │                           │        │ |
|  ├───[ else : 잔액 부족 ]─────────┼───────────────────────────┼────────┤ |
|  │   │                           │ 5: 400 Fail               │        │ |
|  │   │                           │ < - - - - - - - - - - - - │        │ |
|  │   │ 6: throw Exception        │                           │        │ |
|  │   │ < - - - - - - - - - - - - │                           │        │ |
|  +───┴───────────────────────────┴───────────────────────────┴────────+ |
|      │                           │                           │          |
|      v                           v                           v          |
|    시간의 흐름 (수직축: 상단에서 하단으로 진행)                          |
+-------------------------------------------------------------------------+
```

### 메시지 유형 및 복합 프래그먼트 상세

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 동기 메시지 (Synchronous)</strong></span>
      <span class="itpe-badge">실선 + 채운 화살표</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>메서드 호출 후 호출자가 제어권을 넘겨주고 결과를 받을 때까지 대기(블로킹)</li>
        <li>REST API GET/POST 동기 호출, 함수 직접 호출에 사용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 비동기 메시지 (Asynchronous)</strong></span>
      <span class="itpe-badge">실선 + 열린 화살표</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>메시지 송신 후 응답을 기다리지 않고 즉시 자신의 다음 로직을 계속 실행</li>
        <li>Kafka/RabbitMQ 메시지 큐 발행, 백그라운드 이벤트 처리에 사용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 반환 메시지 (Reply/Return)</strong></span>
      <span class="itpe-badge">점선 + 열린 화살표</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>호출된 작업이 완료되어 호출자에게 실행 결과(Return Value)를 반환</li>
        <li>필요 시 화살표 위에 반환 변수명 또는 상태 코드 표기</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 복합 프래그먼트 (Fragments)</strong></span>
      <span class="itpe-badge">UML 2.0 제어 구조</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li><code>alt</code>: 배타적 조건 분기(if-else), 각 구획은 가드 조건([guard]) 명시</li>
        <li><code>opt</code>: 특정 조건 만족 시에만 실행되는 단일 선택 분기(if)</li>
        <li><code>loop</code>: 반복 실행(for, while), 가드 조건에 반복 횟수/조건 명시</li>
        <li><code>par</code>: 두 개 이상의 상호작용이 동시에 일어나는 병렬 처리</li>
        <li><code>ref</code>: 다른 순차 다이어그램을 서브루틴처럼 참조하여 복잡도 감소</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 마이크로서비스 간 동기(REST) 호출 연쇄 과정에서 역방향 동기 호출 발생으로 분산 데드락 발생 | 순차 다이어그램 작성 시 양방향 동기 호출을 사전 검증하고 비동기 이벤트(Kafka) 메시지로 리팩토링 | 서비스 간 결합도 제거 및 런타임 분산 교착 상태 100% 예방 |
| 단일 다이어그램에 모든 예외 케이스와 반복문을 과도하게 표현하여 가독성 상실 | 정상 경로(Happy Path)를 기본 다이어그램으로 유지하고, 복잡 예외 처리는 `ref` 프래그먼트로 별도 분할 | 다이어그램 가독성 유지 및 유지보수성 향상 |
| 소스코드 변경 시 그래픽 툴(Visio 등)로 그린 이미지 다이어그램이 갱신되지 않아 불일치 발생 | PlantUML 또는 Mermaid 텍스트 기반 다이어그램(Diagram as Code) 도입 및 Git PR 리뷰 연동 | 설계 문서와 소스코드 간의 1:1 일치성 상시 보장 |

## 4. 기술사 답안 차별화 포인트

### MSA 분산 트랜잭션(Saga 패턴)과의 연계 표현

순차 다이어그램은 단순히 클래스 수준의 메서드 호출뿐만 아니라 **마이크로서비스 아키텍처(MSA)의 Saga 패턴(오케스트레이션 및 코레오그래피)**을 설명할 때 가장 강력한 도구가 된다. 보상 트랜잭션(Compensating Transaction)이 롤백되는 과정을 `alt` 프래그먼트와 비동기 화살표로 명확히 시각화하여 분산 환경의 정합성 통제 역량을 답안에 드러내면 높은 평가를 받는다.

### Diagram as Code(DaC)와 CI/CD 자동화 전략

현대 소프트웨어 공학에서 손으로 그리는 정적 이미지는 지속 가능하지 않다. Git 저장소 내에 `.puml` 또는 `.mmd` 텍스트 파일로 순차 다이어그램을 보관하고, CI 파이프라인에서 SVG/HTML 문서로 자동 빌드하여 배포하는 **Diagram as Code** 파이프라인 체계를 3단락 또는 맺음말로 제시하여 실무 엔지니어링 감각을 부각한다.

## 5. 참고 및 연계 학습

- [마이크로서비스 아키텍처(MSA)](./070_microservice_architecture.md)
- [서비스 메시(Service Mesh)](./088_service_mesh.md)
- [ALM(Application Lifecycle Management)](./107_alm.md)
- [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
