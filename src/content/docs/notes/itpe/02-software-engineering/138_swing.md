---
title: "SWING"
author: "Gemini 3.8 Flash"
date: "2026-09-20T09:56:00+09:00"
tags:
  - "notes-software-engineering"
extra:
  model: "Gemini 3.8 Flash"

---

## 답안 골격
```text
[SWING(Java Swing)] ◀━━ 머리: Ⅶ 내 의견 (MVC 기반 경량 GUI 컴포넌트의 가치와 현대적 크로스플랫폼 클라이언트 전환)
 ┃
 ┣━ Ⅰ 개요 ───── AWT의 OS 종속 렌더링 및 기능 제약 한계 → 순수 자바 기반으로 픽셀을 직접 그리는 경량(Lightweight) GUI 프레임워크
 ┣━ Ⅱ 특징 ───── 경량 컴포넌트(Lightweight Component) · 플러그형 룩앤필(Pluggable Look and Feel) · 수정된 MVC(Model-UI) 아키텍처
 ┣━ Ⅲ 구조 ───── JComponent 기반 계층(JFrame, JPanel, JButton, JTable) + UI-Delegate + Look and Feel 모듈
 ┣━ Ⅳ 흐름 ───── 사용자 인터랙션 → 이벤트 디스패치 스레드(EDT) 등록 → UI-Delegate 렌더링 호출 → 화면 픽셀 버퍼 갱신
 ┣━ Ⅴ 비교 ───── AWT(Heavyweight, OS 피어) vs Swing(Lightweight, 100% Java) vs JavaFX(현대적 SceneGraph, CSS)
 ┗━ Ⅵ 실무 ───── EDT(Event Dispatch Thread) 블로킹으로 인한 화면 멈춤 / 고해상도(HiDPI) 스케일링 결함 / SwingWorker 비동기 처리
```
- 필수 키워드: 스윙 · JComponent · 경량 컴포넌트 · 플러그형 룩앤필(PLAF) · EDT(Event Dispatch Thread) · SwingWorker · MVC
- 기출: 125회 1교시 `자바 AWT와 Swing의 특징 및 차이점` → Ⅱ·Ⅲ·Ⅴ

## 한 줄 본질
- OS 네이티브 윈도우 피어 객체에 의존하여 플랫폼마다 UI 모양과 동작이 달라졌던 AWT의 병목 → 모든 화면 요소를 운영체제 피어 없이 순수 자바 2D 그래픽스로 직접 렌더링하는 경량 크로스플랫폼 GUI 라이브러리 / 초기 렌더링 속도 저하 및 복잡한 스레드 모델

## 핵심 그림
```text
+-------------------------------------------------------------------------+
|                  Swing 경량 컴포넌트 및 UI-Delegate 아키텍처            |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 사용자 화면 (Pixel Canvas) ] <── 직접 렌더링 (No Native Peer)        |
|               ▲                                                         |
|               │ Graphics2D paint() 호출                                 |
|  +------------┴───────────────────────────────────────────────────────+ |
|  | Swing 컴포넌트 (예: JButton)                                       | |
|  |                                                                    | |
|  |   [ Model (데이터/상태) ] <───> [ UI-Delegate (View + Controller) ]| |
|  |   (ButtonModel)                 (BasicButtonUI, WindowsButtonUI)   | |
|  |                                                ▲                   | |
|  +────────────────────────────────────────────────┼───────────────────+ |
|                                                   │ Look & Feel 교체    |
|                                        [ Pluggable Look and Feel ]      |
|                                        (Metal, Windows, Nimbus 등)      |
|                                                                         |
|  * EDT(Event Dispatch Thread) 단일 스레드 규칙: UI 갱신은 오직 EDT에서만! |
+-------------------------------------------------------------------------+
```

## 핵심 용어
- 경량 컴포넌트(Lightweight Component): 운영체제의 네이티브 창(Window Handle)을 소비하지 않고, 상위 최상위 컨테이너(JFrame)의 캔버스 위에 자바 코드로 픽셀을 직접 그려내는 컴포넌트
- 이벤트 디스패치 스레드(EDT, Event Dispatch Thread): GUI 컴포넌트의 렌더링 및 키/마우스 이벤트 처리를 전담하는 단일 백그라운드 스레드

## 핵심 통찰
- Swing은 전통적인 MVC 패턴에서 뷰(View)와 컨트롤러(Controller)가 너무 강하게 결합된다는 현실을 반영하여, 이 둘을 하나로 합친 "UI-Delegate(위임자)" 구조를 채택함
- Swing의 가장 흔한 장애 패턴은 네트워크 통신이나 DB 조회 같은 무거운 I/O 작업을 EDT에서 직접 수행하여 화면 전체가 하얗게 멈추는 "UI 락업(Lock-up)" 현상이며, 이를 방지하기 위해 반드시 `SwingWorker`나 백그라운드 스레드를 써야 함
- Swing의 플러그형 룩앤필(PLAF) 기술은 런타임에 단 한 줄의 코드로 UI 테마를 윈도우 스타일, 맥 스타일, 독자 스타일(Nimbus)로 동적 전환할 수 있는 뛰어난 확장성을 제공함

## 이웃 토픽과 구분
- Swing vs JavaFX: Swing = 레거시 자바 GUI 표준, 복잡한 커스텀 / JavaFX = XML 기반 레이아웃(FXML), CSS 스타일링, 하드웨어 가속 3D 그래픽을 지원하는 모던 자바 GUI

## 문제·원인·대책
- 적용 상황: 금융권 증권사 트레이딩 HTS 데스크톱 단말
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 대량의 실시간 체결 데이터를 수신하는 순간 화면 클릭이 먹통이 되고 UI 멈춤 | 체결 데이터 파싱 및 소켓 통신을 GUI 렌더링을 담당하는 EDT에서 직접 실행함 | `SwingWorker` 백그라운드 스레드로 I/O 분리 후 `publish()/process()`로 EDT에 결과만 전달 | UI 반응성 100% 보장 및 프리징 해소 |
| 4K 고해상도 모니터에서 단말을 실행했을 때 폰트와 아이콘이 돋보기 수준으로 작아짐 | 구형 Swing 엔진이 HiDPI 자동 스케일링을 지원하지 못함 | Java 9+ DPI 인식 JVM 옵션 활성화 및 벡터 아이콘/동적 폰트 메트릭 적용 | 고해상도 디스플레이 가독성 확보 |

## 이렇게 출제된다
- 제125회 1교시: "자바 Swing의 개념 및 AWT 대비 개선점과 EDT(Event Dispatch Thread)의 역할을 설명하시오." → 요구 포인트: 경량 컴포넌트 정의 + AWT vs Swing 비교 + EDT 단일 스레드 모델 원칙

## 내 의견
- [기존 레거시 Swing 자산의 단계적 현대화 전략] 수십만 라인의 비즈니스 로직이 Swing 폼 클래스에 하드코딩되어 웹 전환이 불가능하다고 방치하는 기업 다수 → 나라면: 프레젠테이션 계층과 비즈니스 로직을 분리하는 MVVM/Clean Architecture 리팩토링을 먼저 거치고, 브라우저 없는 환경이 필수라면 Electron/웹 기술 또는 Flutter 데스크톱으로 UI만 점진적으로 교체하는 현대화 파이프라인 수립
