---
title: "Open API"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:30:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기출 · 92%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "122회, 123회, 125회, 133회, 134회"
  priority: 92
  priority_note: "[출제:133,134] · [출제(KPC):122,123,125] · 이전(KPC):83"
---

## 답안 골격
```text
[Open API] ◀━━ 머리: Ⅶ 내 의견 (API 게이트웨이 기반 트래픽 스로틀링과 OAuth 2.0 인증 거버넌스)
 ┃
 ┣━ Ⅰ 개요 ───── 폐쇄적 데이터 사일로 한계 → 표준 프로토콜 기반 외부 개방으로 비즈니스 생태계 확장
 ┣━ Ⅱ 특징 ───── 공개성(Openness) · 표준화(REST/JSON) · 인증/인가(API Key/OAuth 2.0) · 수익화(Monetization)
 ┣━ Ⅲ 구조 ───── Developer Portal · API Gateway · API Manager/Analytics · Backend Services
 ┣━ Ⅳ 흐름 ───── ① 개발자 등록/키 발급 → ② API 호출 → ③ 게이트웨이 인증/할당량(Quota) 검증 → ④ 서비스 응답
 ┣━ Ⅴ 비교 ───── Open API vs Private API vs Partner API
 ┗━ Ⅵ 실무 ───── 무차별 호출(DDoS/과금) 및 데이터 크롤링 / Throttling 및 Rate Limiting
```
- 필수 키워드: API Gateway · OAuth 2.0 · API Key · OpenAPI Specification(OAS) · Throttling · 마이데이터
- 배점 전략: 10점 = Ⅰ 개념 → Ⅲ 플랫폼 4대 구성요소 도식 → Ⅴ API 노출 범위 비교 / 25점 = Ⅰ~Ⅶ 전개, 마이데이터/오픈뱅킹 표준화 및 보안 위협 대응
- 기출: 134회 4교시 `개방형 API(Open API)` → Ⅰ·Ⅲ·Ⅵ / 123회 1교시 `OAS(OpenAPI Specification)` → Ⅲ·Ⅳ

## 한 줄 본질
- 기업 내부 데이터와 핵심 기능이 시스템 안에 고립되어 신규 비즈니스 창출이 제한되는 병목 → 표준화된 인터페이스(REST, JSON)를 공개하여 제3자 개발자가 자유롭게 서비스를 개발하도록 개방 → 플랫폼 생태계 확장 및 비즈니스 수익 창출 / 백엔드 과부하 및 민감정보 유출 보안 위험

## 핵심 그림
```text
[ 제3자 개발자 (App/Web) ]
           | 1. API 호출 (API Key, OAuth Bearer Token)
           v
+-----------------------------------------------------------+
| [ API Gateway ]                                           |
|  - 인증/인가 (OAuth 2.0, mTLS)   - 로깅/모니터링          |
|  - 트래픽 제어 (Rate Limiting, Throttling, Quota)         |
|  - 프로토콜 변환 (REST <-> gRPC) - 캐싱                   |
+-----------------------------------------------------------+
           | 2. 라우팅
           v
[ 내부 백엔드 서비스 (Microservices / Legacy) ]
```

## 핵심 용어
- OAS(OpenAPI Specification): 프로그래밍 언어에 구애받지 않고 REST API의 인터페이스(엔드포인트, 요청/응답 스키마)를 정의하는 표준 규격(YAML/JSON)
- 스로틀링(Throttling): 단위 시간당(초/분) 허용되는 최대 API 호출 건수를 제한하여 백엔드 시스템의 다운을 방지하는 트래픽 제어 기법

## 핵심 통찰
- Open API의 성공 요인은 API 엔드포인트 자체보다 개발자가 쉽게 테스트하고 연동할 수 있는 '개발자 포털(Developer Portal)'과 샌드박스 환경의 품질에 좌우됨
- 오픈뱅킹과 금융 마이데이터는 개별 기업의 선택이 아니라 법제화된 Open API 강제 적용의 대표적 엔터프라이즈 사례임
- 무제한 개방은 백엔드 리소스 고갈을 유발하므로 계정별 호출 제한(Rate Limiting)과 과금 모델(Pay-per-use)이 API 게이트웨이에 필수 탑재되어야 함

## 이웃 토픽과 구분
- Open API vs Private API: Open API = 불특정 다수 외부 개발자 대상, 엄격한 인증/과금 관리 / Private API = 사내 시스템 간 연계용, 유연한 변경 우선

## 문제·원인·대책
- 사례: 134회 기출 공공 데이터 포털 및 금융 마이데이터 Open API 운영 장애
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 특정 앱의 무한 루프 호출로 전체 API 서버 다운 | 클라이언트별 호출 한도(Rate Limit) 정책 미설정 | 토큰 버킷(Token Bucket) 알고리즘 기반 IP/Key별 Throttling 적용 | 개별 클라이언트 과부하 격리 및 전체 가용성 99.99% 보장 |
| API 명세서와 실제 서비스 간 파라미터 불일치로 연동 오류 | 수기 문서 작성으로 인한 버전 불일치 | Swagger/OAS 코드 퍼스트(Code-First) 자동 명세화 파이프라인 구축 | API 인터페이스 단일 진실 공급원(SSOT) 확립 |

## 이렇게 출제된다
- 제134회 4교시 4번: "개방형 API(Open API)에 대하여 설명하시오." → 요구 포인트: Ⅰ 개념 및 등장 배경 + Ⅲ 구성 아키텍처(게이트웨이, 포털) + Ⅵ 보안 및 거버넌스
- 제122회 2교시 3번: "개방형 API(Open Application Programming Interface)" → 요구 포인트: 웹 서비스 표준(REST, SOAP) 비교 및 플랫폼 비즈니스 모델

## 내 의견
- [API 게이트웨이 없는 위험천만한 API 직접 노출] 사내 내부 스프링 부트 서버의 IP/포트를 외부에 그대로 열어두고 Basic Auth 하나로 Open API를 서비스하다 DB가 털리는 보안 사고 목격 → 나라면: WAF와 결합된 엔터프라이즈 API 게이트웨이를 DMZ에 전진 배치하고, 모든 외부 접근에 대해 mTLS와 OAuth 2.0 PKCE 인증을 의무화하며, 실시간 비정상 호출 탐지 AI 모델 적용
