---
title: "모듈성(결합도·응집도)"
category: "02-software-engineering"
tags:
  - "모듈성"
  - "결합도"
  - "응집도"
  - "Coupling"
  - "Cohesion"
  - "LCOM"
  - "마이어5대기준"
  - "FanInFanOut"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 설계 원칙과 아키텍처 품질을 거쳐 모듈성으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 설계 원칙·아키텍처 품질</span>
  <strong>모듈성(결합도·응집도)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 대규모 소프트웨어의 복잡성을 통제하고 분할 정복(Divide & Conquer)을 실현하기 위해, 소프트웨어를 자율적이고 독립적인 모듈 단위로 분해하고, 모듈 간 상호 의존성을 최소화(저결합도: Loose Coupling)하며 모듈 내부의 책임 집중도를 극대화(고응집도: High Cohesion)하여 변경 파급효과를 완벽히 격리하는 핵심 소프트웨어 공학 설계 원리
- 메커니즘: 도메인 요구 분석 $\rightarrow$ 단일 책임(SRP) 기반 모듈 분할 $\rightarrow$ 인터페이스 추상화 및 최소 데이터 전달 $\rightarrow$ 정량 메트릭(LCOM, Fan-in/out) 측정 $\rightarrow$ 고응집·저결합 모듈성 확정
- 산출물: 모듈 아키텍처 구조도 · 결합도/응집도 분석 보고서 · LCOM 정적 분석 리포트 · 모듈 인터페이스 정의서

<div class="itpe-flow-map" role="img" aria-label="모듈성 설계 및 정량적 품질 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 도메인 책임 분할 (고응집화)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분할</strong><span>단일 책임 원칙(SRP)에 따라 하나의 모듈이 오직 하나의 비즈니스 기능만 수행하도록 설계</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 인터페이스 캡슐화 (저결합화)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>격리</strong><span>정보 은닉을 적용하고 모듈 간에는 최소한의 원시 데이터(자료 결합도)만 전달</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량적 복잡도 계측</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>측정</strong><span>LCOM(응집도 결여) 및 Fan-in(호출 유입), Fan-out(호출 유출) 메트릭 산출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 모듈성 품질 적합성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>LCOM 수치가 낮고 결합도가 자료/스탬프 수준이며 Fan-out이 4 이하로 통제되었는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (독립 모듈 확정)</strong>
      <span>모듈 설계 승인 $\rightarrow$ 변경 파급효과 차단 및 독립적 단위 테스트·배포 실현</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (God Object / 결합 과다)</strong>
      <span>설계 반려 $\rightarrow$ 클래스 추출(Extract Class) 및 전략 패턴 적용 리팩토링</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **결합도(Coupling)**: 모듈과 모듈 사이의 상호 의존성 정도를 나타내며, 낮을수록(Loose Coupling) 독립성과 재사용성이 높아짐 (내용 > 공통 > 외부 > 제어 > 스탬프 > 자료)
- **응집도(Cohesion)**: 모듈 내부의 구성 요소들이 단일한 목적을 달성하기 위해 얼마나 긴밀하게 집중되어 있는지를 나타내며, 높을수록 우수함 (우연적 < 논리적 < 시간적 < 절차적 < 교환적 < 순차적 < 기능적)
- **LCOM(Lack of Cohesion in Methods)**: 클래스 내 메서드들이 인스턴스 필드를 공유하는 정도를 수치화한 메트릭으로, 값이 높을수록 응집도가 떨어져 리팩토링이 시급함을 의미
- **버트란드 마이어(Meyer) 5대 기준**: 모듈의 품질을 평가하는 5가지 공학적 척도(분해성, 조합성, 이해성, 연속성, 보호성)
</details>

## 1. 개요 및 필요성

### 스파게티 코드의 파멸과 모듈성의 공학적 가치

소프트웨어가 복잡해질수록 하나의 기능을 수정했을 때 전혀 무관한 수십 개의 다른 기능이 연쇄적으로 고장 나는 "변경 파급효과(Ripple Effect)"가 발생한다. 이는 시스템 내부가 거대한 덩어리로 엉켜있는 스파게티 아키텍처 때문이다.

모듈성은 시스템을 독립된 부품으로 분할하여 각 모듈을 독립적으로 개발, 테스트, 배포, 유지보수할 수 있도록 보장하는 소프트웨어 공학의 대원칙이다.

### 버트란드 마이어(Bertrand Meyer)의 모듈성 5대 평가 기준

| 평가 기준 | 핵심 질문 및 공학적 의미 |
|---|---|
| **분해성 (Decomposability)** | 대규모 문제를 독립적으로 개발 가능한 작은 하위 모듈들로 체계적으로 쪼갤 수 있는가? |
| **조합성 (Composability)** | 이미 만들어진 모듈들을 조립하여 새로운 시스템을 쉽게 재구축할 수 있는가? (재사용성) |
| **이해성 (Understandability)** | 다른 모듈의 내부를 깊이 알지 못해도 해당 모듈 단독으로 쉽게 이해할 수 있는가? |
| **연속성 (Continuity)** | 사소한 요구사항 변경이 발생했을 때 전체로 번지지 않고 1~2개 모듈에만 국한 전파되는가? |
| **보호성 (Protection)** | 런타임 오류나 예외가 발생했을 때 타 모듈로 확산되지 않고 해당 모듈 내에서 격리되는가? |

## 2. 아키텍처 및 핵심 메커니즘

### 결합도와 응집도의 2대 평가 스펙트럼

```text
+-------------------------------------------------------------------------+
|                  모듈성(Modularity) 2대 핵심 평가 축                    |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 1. 결합도 (Coupling) : 모듈 간 상호 의존성 (낮을수록 우수: Loose) ]  |
|  나쁨 <─── [내용] ── [공통] ── [외부] ── [제어] ── [스탬프] ── [자료] ───> 우수
|            (Content) (Common) (External) (Control) (Stamp)   (Data)     |
|            타모듈직접접근 전역변수공유 프로토콜공유 플래그간섭 DTO통째전달  원시값전달 |
|                                                                         |
|  [ 2. 응집도 (Cohesion) : 모듈 내부 책임 집중도 (높을수록 우수: High) ]  |
|  우수 <─── [기능적] ─ [순차적] ─ [교환적] ─ [절차적] ─ [시간적] ─ [논리적] ─ [우연적]
|            (Functional)(Sequential)(Comm.)(Procedural)(Temporal)(Logical)(Coincidental)
|            단일목적수행 출력이입력 동일입출력 순서실행   동시초기화 유사작업  무관한동거 |
+-------------------------------------------------------------------------+
```

### 결합도 6단계 상세 분석 [내 - 공 - 외 - 제 - 스 - 자]

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>자료 결합도 (Data)</strong></span>
      <span class="itpe-badge">최상 (Ideal)</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>모듈 간에 오직 필요한 원시 데이터 값(Primitive)만을 파라미터로 전달</li>
        <li>인터페이스가 극도로 단순하며 변경 파급효과가 전혀 없음</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>스탬프 결합도 (Stamp)</strong></span>
      <span class="itpe-badge">양호 (주의)</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>모듈 간에 복합 데이터 구조(DTO, 레코드) 전체를 매개변수로 전달</li>
        <li>필요하지 않은 필드까지 노출되어 DTO 구조 변경 시 연쇄 영향</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>제어 결합도 (Control)</strong></span>
      <span class="itpe-badge">보통 (지양)</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>상위 모듈이 하위 모듈에 제어 플래그(`boolean`)를 넘겨 내부 로직 지시</li>
        <li>하위 모듈의 처리 흐름을 상위 모듈이 침범하여 캡슐화 훼손</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>내용 결합도 (Content)</strong></span>
      <span class="itpe-badge">최악 (Very Bad)</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>한 모듈이 다른 모듈의 내부 코드나 비공개 변수 주소에 직접 접근</li>
        <li>정보 은닉이 완전 파괴되어 단 하나의 수정에도 전체 붕괴</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 100개 필드를 가진 거대 OrderDTO를 배송/정산 계층에 통째로 전달(스탬프 결합도)하여 필드 하나 변경 시 전사 재컴파일 | 메서드 파라미터에 꼭 필요한 최소 원시 데이터(자료 결합도)만 전달하도록 인터페이스 축소 | 모듈 간 변경 전파 완벽 격리 |
| 상위 컨트롤러가 boolean 플래그를 넘겨 하위 서비스의 if-else 분기를 조종(제어 결합도) | 전략 패턴(Strategy Pattern) 또는 상태 다형성을 적용하여 분기 로직을 객체 내부로 캡슐화 | OCP(개방 폐쇄 원칙) 충족 및 유지보수성 향상 |
| 잡다한 함수를 한곳에 몰아넣은 CommonUtil 클래스가 5,000라인짜리 God Object(우연적 응집도)로 변질 | 단일 책임 원칙(SRP) 적용 및 SonarQube LCOM 정적 분석 품질 게이트 연동(LCOM > 0.8 차단) | 클래스 책임 1개 한정 및 유지보수 공수 60% 절감 |

## 4. 기술사 답안 차별화 포인트

### 결합도와 응집도의 상보적 역학 관계 수식화

기술사 답안의 서두에서 **"응집도와 결합도는 동전의 양면"**임을 명시한다. 한 모듈의 응집도가 낮아 책임이 여러 곳으로 흩어지면, 그 흩어진 기능들을 호출하기 위해 다른 모듈들과의 결합도가 필연적으로 증가할 수밖에 없다. 따라서 **"높은 응집도를 달성하는 것이 곧 낮은 결합도를 실현하는 선결 조건"**이라는 공학적 인과관계를 피력한다.

### DDD(도메인 주도 설계)의 바운디드 컨텍스트 연계

전통적인 함수/클래스 수준의 논의를 넘어 현대 마이크로서비스 아키텍처(MSA) 수준으로 논의를 확장한다. **DDD의 바운디드 컨텍스트(Bounded Context)와 애그리게잇(Aggregate) 설계는 비즈니스 도메인 수준에서 '기능적 응집도'를 확보하고, 서비스 간 통신을 REST/이벤트로 한정하여 '자료 결합도'를 달성하는 현대적 실체**임을 결론으로 제시한다.

## 5. 참고 및 연계 학습

- [SOLID 원칙](./082_solid.md)
- [객체지향 프로그래밍(OOP)](./083_oop.md)
- [리팩토링(Refactoring)](./006_refactoring.md)
- [정보 은닉(Information Hiding)](./024_information_hiding.md)
