---
title: "디자인 패턴(프록시 패턴)"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  model: "OpenAI Codex"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="소프트웨어 설계에서 프록시 패턴까지의 지식 경로"><span>SW 공학·설계</span><span>구조 패턴</span><strong>프록시 패턴</strong></div>

## 큰 그림과 30초 인출

```text
반복 설계문제
 ├─ 생성: 객체 생성 분리
 ├─ 구조: 객체·클래스 결합 ── [Client]→[Subject]←[RealSubject]
 │                                  └──────[Proxy]──────┘
 └─ 행위: 책임·알고리즘 분배

Proxy = 같은 Subject 인터페이스로 실제 객체 접근을 대리·통제
```

```text
패턴 = 문제 맥락 + 해결 구조 + 결과·상충
Proxy 흐름 = Client → Proxy → 접근통제/부가기능 → RealSubject
유형 = Virtual·Protection·Remote·Caching/Logging
주의 = 목적 없는 패턴 적용, 프록시 계층 누적, 우회 접근
```

## 예상문제

> 디자인 패턴의 개념과 분류를 설명하고, 프록시 패턴의 구조·동작·유형 및 적용 시 고려사항을 제시하시오.

## Ⅰ. 개요 ───── 반복 설계문제의 재사용 해법

디자인 패턴은 반복되는 소프트웨어 설계 문제의 맥락, 역할 간 협력 구조와 적용 결과를 이름 붙여 재사용하는 설계 지식이다. 코드를 복사하는 것이 아니라 변경 지점을 인터페이스 뒤에 분리하고 공통 설계 어휘를 제공한다.

## Ⅱ. 특징 ───── 생성·구조·행위의 역할 분리

| 분류 | 관심사 | 대표 패턴 |
|---|---|---|
| 생성 | 객체 생성과 구체 타입 결합 분리 | Factory Method, Builder, Singleton |
| 구조 | 객체·클래스를 더 큰 구조로 결합 | Adapter, Decorator, Proxy |
| 행위 | 책임과 알고리즘·통신 분배 | Strategy, Observer, Command |

| 효과 | 설명 | 상충 |
|---|---|---|
| 변경 격리 | 변동 부분을 추상화 | 클래스·간접 계층 증가 |
| 공통 어휘 | 설계 의도 공유 | 이름만 적용하는 Cargo Cult |
| 검증된 협력 | 알려진 역할 구조 재사용 | 맥락이 다르면 부적합 |

## Ⅲ. 구조 ───── 프록시의 동일 인터페이스 대리

```text
             ┌──────────────┐
Client ─────▶│ Subject      │◀────────────┐
             │ +request()   │             │
             └──────┬───────┘             │
                    │ implements          │ implements
          ┌─────────▼──────┐      ┌───────┴────────┐
          │ Proxy          │─────▶│ RealSubject    │
          │ -realSubject   │      │ +request()     │
          │ +request()     │      └────────────────┘
          └────────────────┘
       접근 전/후 통제·지연생성·캐시
```

| 구성요소 | 역할 |
|---|---|
| Subject | Client가 의존하는 공통 계약 |
| RealSubject | 실제 업무 기능 수행 |
| Proxy | RealSubject 참조와 접근 전후 정책 수행 |
| Client | 구체 구현이 아닌 Subject 호출 |

## Ⅳ. 동작 ───── 요청 중계와 정책 삽입

```text
① Client가 Subject.request 호출
 → ② Proxy가 인증·캐시·지연생성 등 사전 처리
 → ③ 필요 시 RealSubject 생성/원격 연결
 → ④ 실제 요청 위임
 → ⑤ 결과 기록·변환 후 Client에 반환
```

| 유형 | 대리 목적 | 적용 예 |
|---|---|---|
| Virtual Proxy | 고비용 객체 지연 생성 | 대용량 이미지·모델 로딩 |
| Protection Proxy | 권한별 접근 통제 | 서비스·데이터 접근 |
| Remote Proxy | 원격 객체를 로컬처럼 표현 | RPC Stub |
| Caching/Logging Proxy | 캐시·관측 등 횡단 기능 | API 호출 캐시·감사 |

## Ⅴ. 비교 ───── Proxy·Decorator·Adapter

| 구분 | Proxy | Decorator | Adapter |
|---|---|---|---|
| 목적 | 접근 대리·통제 | 기능의 동적 추가 | 인터페이스 변환 |
| 계약 | 대상과 동일 | 대상과 동일 | 서로 다른 계약 연결 |
| 대상 호출 | 통상 위임 | 장식 체인 위임 | 변환 후 위임 |
| 선택 기준 | 접근 시점·권한·원격성 | 조합 가능한 부가기능 | 기존 API 호환 |

아키텍처 스타일은 시스템 수준 구성 원칙이고, 디자인 패턴은 객체·컴포넌트 협력 수준의 반복 해법이다.

## Ⅵ. 고려 ───── 패턴 남용과 대리 경계 통제

| 문제 | 원인 | 대응 | 확인 |
|---|---|---|---|
| 불필요한 복잡성 | 문제 없이 패턴부터 선택 | 변화축·품질 요구부터 식별 | 제거 전후 복잡도 |
| 프록시 체인 지연 | 캐시·보안·로깅 중첩 | 책임 통합, 순서·Timeout 명시 | 종단 지연 |
| 우회 접근 | RealSubject 직접 참조 노출 | 생성·DI 경계에서 Proxy 강제 | 호출 경로 |
| 의미 불일치 | Proxy와 실제 계약 차이 | 대체 가능성·예외 계약 테스트 | Contract Test |
| 숨은 부작용 | 요청이 네트워크·권한 검사를 동반 | 이름·문서·관측으로 비용 명시 | Trace·Error |

## Ⅶ. 결론 ───── 패턴명보다 문제 맥락과 상충 검증

디자인 패턴은 정답 목록이 아니라 변경을 격리하는 설계 언어다. 프록시는 동일 계약으로 접근 정책을 삽입하되 지연·실패·권한이라는 새 의미가 생기므로, 대리 목적과 우회 방지·관측 가능성을 함께 검증해야 한다.

## 1교시 10점 발췌

```text
디자인 패턴은 반복 설계문제의 맥락·협력구조·결과를 재사용하는 설계 지식이다.
Proxy: Client → Subject ← Proxy → RealSubject
목적: 지연생성·접근통제·원격대리·캐시/로깅
비교: Proxy=접근 통제, Decorator=기능 추가, Adapter=계약 변환
```

## 공식 근거

- [Oracle Java Proxy API](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/Proxy.html)
- Q-Net 제136회 정보관리기술사 1교시 5번: 프록시 디자인 패턴

## 체크

- [ ] GoF 분류와 프록시의 위치를 표시했는가
- [ ] Subject·Proxy·RealSubject 관계를 그렸는가
- [ ] Decorator·Adapter와 목적 기준으로 비교했는가
- [ ] 지연·우회·계약 검증을 제시했는가

## 연결 토픽

- [리팩토링](./006_refactoring/)
- [의존성 주입](./042_dependency_injection/)
