---
title: "Java GUI 툴킷(AWT, Swing, JavaFX)"
category: "02-software-engineering"
tags: ["JavaGUI", "AWT", "Swing", "JavaFX", "이벤트디스패치스레드"]
date: "2026-09-24T00:00:00+09:00"
author: "Codex"
sidebar:
  badge:
    text: "응용"
extra:
  model: "GPT-6"
  keyword_grade: "응용"
---

## 학습 위치

소프트웨어공학 → 사용자 인터페이스 → Java 데스크톱 GUI → **Java GUI 툴킷**

## 30초 인출

- **본질**: Java GUI 툴킷은 윈도우·컨트롤·이벤트 처리 기능으로 데스크톱 사용자 인터페이스를 구성하는 라이브러리
- **메커니즘**: 화면 컴포넌트 구성 → 이벤트 처리 → UI 스레드에서 화면 상태 갱신

<details>
<summary>핵심 용어</summary>

- **AWT(Abstract Window Toolkit)**: Java의 기본 GUI·이벤트·그래픽 기능을 제공하는 툴킷
- **Swing**: AWT 기반으로 다양한 경량 GUI 컴포넌트를 제공하는 툴킷
- **JavaFX**: Java 데스크톱·그래픽 애플리케이션을 위한 UI 플랫폼으로 OpenJFX로 제공
- **이벤트 디스패치 스레드(Event Dispatch Thread, EDT)**: Swing 이벤트 처리와 UI 갱신을 담당하는 스레드
- **JavaFX Application Thread**: JavaFX UI 이벤트와 장면 그래프 작업을 수행하는 스레드

</details>

---

## 1교시 예상문제 (10점)

> (예상) Java GUI 툴킷의 개념과 AWT·Swing·JavaFX의 특징을 설명하시오.

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Java GUI 툴킷**: Java 애플리케이션의 화면과 사용자 상호작용을 구성하는 GUI 라이브러리 |
| 목적 | 데스크톱 UI 구성 요소와 이벤트 처리 기능 제공 |

### Ⅱ. 주요 툴킷 비교

| 툴킷 | 특징 |
|---|---|
| AWT | 기본 GUI 기능과 네이티브 연계 기반 |
| Swing | AWT 위에서 다양한 경량 컴포넌트 제공 |
| JavaFX | 장면 그래프 기반 UI·미디어·그래픽 기능; OpenJFX로 배포 |

### Ⅲ. 이벤트 처리

```text
사용자 입력 → UI 이벤트 스레드
                ├─ 짧은 처리 → 화면 갱신
                └─ 긴 처리 → 백그라운드 작업
                               └─ 결과를 UI 스레드에 전달
```

**제언**: 화면 갱신은 UI 스레드에서 수행하고 오래 걸리는 작업은 분리해 반응성을 유지.

---

## 2~4교시 예상문제 (25점)

> (예상) AWT·Swing·JavaFX의 구조와 차이, 이벤트 처리 및 선택 시 고려사항을 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Java GUI 툴킷**: Java 애플리케이션의 화면과 사용자 상호작용을 구성하는 GUI 라이브러리 |
| 목적 | 데스크톱 UI 구성 요소와 이벤트 처리 기능 제공 |

## Ⅱ. 툴킷 구조와 계보

```text
Java 데스크톱 UI 도구
  ├─ AWT: 기본 GUI·이벤트 API
  │    └─ Swing: AWT 기반의 컴포넌트 확장
  └─ JavaFX·OpenJFX: 별도 UI 플랫폼
```

AWT는 일부 컴포넌트에서 네이티브 피어를 사용하며, Swing은 AWT 기반의 경량 컴포넌트를 제공. AWT와 Swing은 혼합 사용을 전제로 한 예외·제약도 있으므로 무조건 혼합 금지로 단정하지 않음. JavaFX는 현재 JDK에 항상 포함된 것으로 간주하지 않고 배포 환경을 확인.

## Ⅲ. 특성 비교

| 관점 | AWT | Swing | JavaFX |
|---|---|---|---|
| 기반 | Java 기본 GUI API와 네이티브 연계 | AWT 기반 컴포넌트 라이브러리 | 별도 UI 플랫폼·장면 그래프 |
| UI 구성 | 기본 컴포넌트 | 다양한 경량 컴포넌트·룩앤필 | UI 컨트롤·그래픽·미디어 기능 |
| 적용 검토 | 기존 AWT 애플리케이션·기본 UI | Swing 유지보수·데스크톱 UI | JavaFX 의존성과 현대 UI 요구 |

## Ⅳ. 이벤트·스레드 처리

```text
입력 이벤트 → UI 이벤트 큐
                  ↓
       EDT·JavaFX Application Thread
         ├─ 짧은 작업 → 화면 갱신
         └─ 긴 작업 → 백그라운드 스레드
                           └─ 결과를 UI 스레드로 전달
```

Swing 컴포넌트 접근은 일반적으로 EDT에서 수행하고, JavaFX 장면 그래프 변경은 JavaFX Application Thread에서 처리. 긴 작업이 UI 이벤트 스레드를 점유하면 입력·화면 갱신이 지연되므로 백그라운드 작업과 안전한 결과 전달 필요.

## Ⅴ. 선택 기준과 적용

| 기준 | 확인 내용 |
|---|---|
| 기존 자산 | 사용 중인 툴킷·컴포넌트·배포 방식 |
| UI 요구 | 접근성, 화면 복잡도, 그래픽·미디어 요구 |
| 운영 환경 | JDK·OpenJFX 버전, 설치·배포·지원 계획 |
| 유지보수 | 개발 역량, 의존성, 테스트 자동화 가능성 |

## Ⅵ. 문제와 해결 방안

| 한계 | 해결 방안 |
|---|---|
| UI 스레드에서 장시간 작업 수행 | 백그라운드 실행과 UI 스레드 결과 반영 분리 |
| 서로 다른 컴포넌트 모델 혼합으로 표시 문제 | AWT·Swing 혼합 지점과 피어 동작을 시험 환경에서 검증 |
| 런타임에 툴킷 의존성 누락 | JDK·JavaFX 런타임과 패키징 구성을 빌드·배포에서 검증 |

## Ⅶ. 기술적 제언

| 구분 | 내용 |
|---|---|
| 한계 | 툴킷을 화면 기능만으로 고르면 배포·지원 런타임과 UI 스레드 모델이 후속 운영 위험으로 남을 수 있음 |
| 해결 방안 | 선택 단계에서 화면 요구, 지원 런타임, 이벤트 스레드 규칙을 함께 검증하는 작은 배포 프로토타입을 구성 |

## 참고 및 연계 학습

- [Oracle Swing Concurrency Tutorial](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/dispatch.html)
- [OpenJFX Documentation](https://openjfx.io/openjfx-docs/introduction)
- [스프링 부트](./159_spring_boot.md)
- [추상 클래스와 인터페이스](./205_abstract_class_and_interface.md)
- [Enterprise Beans](./200_ejb.md)
- [HTML5 표준 API](./186_html5.md)
