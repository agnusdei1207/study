---
title: "비바 모델(Biba Model)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T01:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기출 · 76%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "127회"
  priority: 76
  priority_note: "[출제(KPC):127]"
---

## 답안 골격
```text
[비바 모델(Biba Model)] ◀━━ 머리: Ⅶ 내 의견 (비인가 변조 통제 완성 → 무결성 레벨 기반 감사 파이프라인 및 BLP와의 상호보완 배치)
 ┃
 ┣━ Ⅰ 개요 ───── 군사 기밀 중심 BLP(기밀성)의 한계 극복 → 데이터 오염 및 비인가 변조를 방지하는 무결성(Integrity) 전용 수학적 상태 전이 모델
 ┣━ Ⅱ 특징 ───── 무결성 중심(데이터 정확성·신뢰성 보장) · 계층적 무결성 등급 부여 · 주체-객체 간 읽기/쓰기 통제 규칙
 ┣━ Ⅲ 구조 ───── 단순 무결성 속성(Simple Integrity, No Read Down) · 스타 무결성 속성(*-Integrity, No Write Up) · 호출 속성(Invocation Property)
 ┣━ Ⅳ 흐름 ───── 주체 무결성 수준 검증 → 하위 객체 읽기 차단(오염 방지) → 상위 객체 쓰기 차단(위조 방지)
 ┣━ Ⅴ 비교 ───── Biba(무결성, No Read Down, No Write Up) vs BLP(기밀성, No Read Up, No Write Down) vs Clark-Wilson(상용 무결성, CDI/UDI, 직무분리)
 ┗━ Ⅵ 실무 ───── 상용 시스템 적용 시 상위 등급 주체의 정보 수집 제약 / 엄격한 쓰기 금지로 인한 데이터 동기화 지연
```
- 필수 키워드: 비바 모델 · 무결성(Integrity) · No Read Down(단순 무결성) · No Write Up(*-무결성) · 호출 속성(Invocation Property) · BLP 모델 비교
- 배점 전략: 10점 = Ⅰ 개념 및 무결성 정의 → Ⅲ 2대 핵심 규칙 도식 → Ⅴ BLP와의 대칭 구조 비교표 / 25점 = Ⅰ~Ⅶ 전개, Biba 상태 전이 수학적 메커니즘과 상용 환경 적용 한계(Clark-Wilson 전환 이유) 상세화
- 기출: 127회 2교시 6번 `아래의 접근 통제 보안 모델에 대하여 설명하시오. 나. 비바(Biba) 모델` → Ⅰ Biba 개념 + Ⅲ 2대 무결성 속성 + Ⅴ BLP/Clark-Wilson 비교

## 한 줄 본질
- 기밀성 중심 모델이 허용하는 비인가 데이터 변조 및 오염 병목 → 무결성 등급 기반으로 하위 무결성 읽기 금지와 상위 무결성 쓰기 금지 강제 → 데이터 오염 및 비인가 변조 차단 / 고무결성 주체의 저무결성 데이터 참조 차단으로 업무 유연성 저하

## 핵심 그림
```text
[비바 모델(Biba Model)의 무결성 통제 규칙]

  [높은 무결성 등급 (High Integrity Level)]
        ▲                                │
        │ (쓰기 금지: No Write Up)        │ (읽기 금지: No Read Down)
        │ 오염된 데이터 주입 차단          │ 오염된 저급 정보 습득 차단
        │                                ▼
  [낮은 무결성 등급 (Low Integrity Level)]

  1. 단순 무결성 속성 (Simple Integrity): 주체는 자신보다 낮은 등급 객체 읽기 불가 (No Read Down)
  2. 스타 무결성 속성 (*-Integrity): 주체는 자신보다 높은 등급 객체 쓰기 불가 (No Write Up)
  3. 호출 속성 (Invocation): 주체는 자신보다 높은 무결성을 가진 주체를 호출 불가
```

## 핵심 용어
- 단순 무결성 속성(Simple Integrity Property): 주체는 자신보다 낮은 무결성 수준을 가진 객체를 읽을 수 없음. 오염된 저품질 데이터가 고신뢰 주체에 유입되는 현상 차단
- 스타 무결성 속성(*-Integrity Property): 주체는 자신보다 높은 무결성 수준을 가진 객체를 수정하거나 기록할 수 없음. 저신뢰 주체에 의한 고품질 핵심 시스템 변조 원천 통제
- 호출 속성(Invocation Property): 낮은 무결성 수준의 주체가 높은 무결성 수준의 주체나 프로세스를 직접 호출(Execute)하여 권한을 탈취하는 행위 제한

## 핵심 통찰
- BLP가 "비밀이 밖으로 새어나가는 것(기밀성)"을 막는다면, Biba는 "쓰레기가 핵심 데이터베이스 안으로 들어오는 것(무결성)"을 막는 대칭 모델임
- No Read Down 규칙은 현실 업무에서 심각한 병목을 유발함 → 관리자(고무결성)가 외부 웹사이트나 미검증 보고서(저무결성)를 읽지 못하게 강제하므로 상용 OS에서는 온전히 적용되지 못함
- 상용 엔터프라이즈 환경에서는 Biba의 순수 수학적 강제 대신 잘 정의된 트랜잭션(TP)과 직무 분리를 결합한 클락-윌슨(Clark-Wilson) 모델로 진화함

## 이웃 토픽과 구분
- Biba vs Bell-LaPadula(BLP): Biba = 무결성 보장(No Read Down, No Write Up) / BLP = 기밀성 보장(No Read Up, No Write Down) (두 모델은 정반대 방향으로 동작)

## 문제·원인·대책
- 사례: 군사 정보 체계에서 Biba 모델 적용 후 관리자 계정이 외부 현장 보고서(저무결성)를 열람하지 못해 긴급 작전 지시가 지연된 장애
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 고등급 주체의 저등급 데이터 열람 차단으로 상황 인지 마비 | Biba의 엄격한 단순 무결성(No Read Down) 규칙의 맹목적 강제 | 격리 샌드박스 및 데이터 검증 필터(Sanitizer) 프로세스 경유 도입 | 정제된 데이터의 무결성 승격(Declassification)을 통한 합법적 열람 보장 |
| 비인가 외부 프로세스에 의한 시스템 핵심 파일 변조 위험 | 다중 사용자 환경에서 쓰기 권한 통제 누락 | Biba의 *-무결성 규칙 기반 커널 무결성 검증 모듈 적용 | 저권한 악성코드의 시스템 바이너리 덮어쓰기 원천 봉쇄 |

## 이렇게 출제된다
- 제127회 2교시 6번: "아래의 접근 통제 보안 모델에 대하여 설명하시오. 가. 벨라파듈라(Bell-LaPadula) 모델 나. 비바(Biba) 모델 다. 클락-윌슨(Clark-Wilson) 모델" → 요구 포인트: 나. Biba 모델의 정의 및 2대 핵심 무결성 속성(No Read Down, No Write Up) + BLP/클락-윌슨과의 차이점

## 내 의견
- [Biba 모델의 현대적 재해석] 고전 Biba 모델을 순수하게 구현하려다 실패하는 프로젝트가 많음 → 나라면: 현대 윈도우 OS의 무결성 메커니즘(MIC, Mandatory Integrity Control)과 리눅스 IMA(Integrity Measurement Architecture)처럼 프로세스 권한 분리에 Biba의 무결성 레벨(Untrusted, Low, Medium, High, System)을 매핑하여 웹 브라우저 탭 격리 및 드라이버 변조 방지 체계로 경량화 구현

## 찾아볼 것
- Windows MIC(Mandatory Integrity Control)에서의 Biba 모델 변형 구현 방식
