---
title: "SOAP(Simple Object Access Protocol)"
description: "W3C 표준 XML 프로토콜, 웹 서비스 3대 표준, REST 비교, WS-* 복잡성 한계와 어댑터 제언"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  question_no: "026"
---

## 연관 키워드
- SOAP, XML, Envelope(봉투), WSDL, UDDI
- WS-Security, WS-*, Fault, REST

## Ⅰ. SOAP의 개요

- 핵심 요약 : SOAP은 XML 기반 봉투 메시지의 구조와 교환 규칙을 표준화해 이기종 시스템 간 서비스 호출을 지원하는 프로토콜.
- 개념 : W3C(World Wide Web Consortium) 표준인 **SOAP**(Simple Object Access Protocol)은 **XML**(Extensible Markup Language) 메시지를 **봉투**(Envelope) 구조로 감싸 교환하는 웹 서비스 메시징 프로토콜.
- 배경 및 필요성 : 플랫폼·언어가 다른 기관 간 연계에서 메시지 형식·오류 처리·보안의 공통 표준 부재로 상호운용 비용 증가.
- 주요 목적 : 구조화된 메시지 교환 표준으로 이기종 시스템의 상호운용성과 웹 서비스 생태계 결합 확보.

## Ⅱ. SOAP의 특징 및 장점

- 핵심 요약 : 봉투 구조·전송 독립성·계약 기반·표준 확장이 기업 간 연계의 신뢰성·감사 요구를 충족.

1. 봉투 기반 메시지 : Envelope 안의 Header(메타데이터)와 Body(본문) 분리 → 보안·트랜잭션 정보의 표준 자리 확보.
2. 전송 독립성 : HTTP·SMTP 등 다양한 프로토콜 바인딩 → 전송 수단 교체에도 메시지 계약 유지.
3. 계약 기반 개발 : **WSDL**(Web Services Description Language)이 연산·메시지·바인딩을 기술 → 클라이언트 코드 자동 생성·상호운용 지원.
4. 표준 확장 체계 : **WS-Security**(Web Services Security) 등 WS-* 표준군으로 메시지 서명·암호화·신뢰 전달 → 기업 간 보안 요구 대응.
5. 표준 오류 형식 : **Fault**(오류 보고 요소)가 오류 코드·사유를 구조화 → 구현체에 무관한 예외 처리.

## Ⅲ. SOAP의 구조 (흐름)

- 핵심 요약 : 봉투 구조의 메시지가 서비스 계약·등록 체계와 결합해 호출·오류 반환이 진행.

```text
SOAP 메시지 구조

Envelope (봉투)
   Header : 보안 토큰·라우팅 등 메타데이터
   Body : 요청·응답 데이터 또는 Fault
```

```text
웹 서비스 호출 흐름

서비스 제공자 : WSDL 발행 → UDDI 등록
   ↓
서비스 요청자 : UDDI 탐색 → WSDL 취득
   ↓
SOAP 요청 전송 → Body 처리
   ↓
SOAP 응답 또는 Fault 반환
```

- 웹 서비스 3요소 : SOAP(메시지 교환), WSDL(서비스 기술), **UDDI**(Universal Description, Discovery and Integration, 등록·탐색).

## Ⅳ. SOAP과 REST의 비교

- 핵심 요약 : SOAP은 표준 명세 중심의 메시징 프로토콜, REST는 HTTP 제약을 활용하는 자원 중심 아키텍처 스타일.
- 비교 개요 : **REST**(Representational State Transfer)는 자원과 HTTP 메서드 중심의 아키텍처 스타일로 웹 API 설계의 대표 대안.

| 비교 축 | SOAP | REST |
|---|---|---|
| 성격 | 메시징 프로토콜(W3C 표준) | 아키텍처 스타일(제약 집합) |
| 메시지 형식 | XML Envelope 필수 | JSON·XML 등 자원 표현 자유 |
| 서비스 계약 | WSDL 기반의 강한 계약 | OpenAPI 등 명세 선택적 활용 |
| 보안·확장 | WS-* 메시지 수준 표준 | HTTPS·HTTP 인프라 활용 |
| 전송·캐시 | 다양한 바인딩·캐시 별도 구현 | HTTP 중심·캐시·프록시 재사용 |
| 적합 영역 | 기업 간 엄격한 보안·트랜잭션 연계 | 웹·모바일 오픈 API |

## Ⅴ. SOAP의 한계와 방안

- 핵심 요약 : XML 비대·표준 조합 복잡성·구현체 편차·XML 보안 위협을 선별 적용과 계약 시험으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 메시지 비대 | XML 태그 오버헤드 → 전송량·모바일 환경 불리 | 압축·경량 API 병행·필요 표준만 선별 | 평균 응답 시간 |
| WS-* 복잡성 | 표준 조합 난이도 → 구현·디버깅 비용 증가 | 조직 표준 프로파일로 적용 범위 제한 | 적용 WS-* 수 |
| 구현체 간 편차 | 명세 해석 차이 → 연계 결함 | WS-I 프로파일 준수·계약 시험 | 상호운용 결함 수 |
| XML 보안 위협 | XXE(XML External Entity) 공격·대형 메시지 부하 | 외부 엔터티 비활성화·크기 제한·서명 검증 | 보안 취약점 수 |

- 상호운용 기준 : WS-I(Web Services Interoperability)의 Basic Profile이 구현체 간 편차를 줄이는 준수 기준.

## Ⅵ. SOAP에 대한 제언

- 핵심 요약 : 메시지 계약의 표준 관리·보안 정책 통합·레거시 자산 중계의 거버넌스로 SOAP 자산 가치 유지.

1. 통합 아키텍처 조직은 WSDL·XML 스키마·오류 코드 체계를 버전과 함께 표준 저장소에서 관리.
2. 보안 조직은 메시지 서명·암호화·재전송 방어 정책을 연계 심사 절차에 통합.
3. API 거버넌스 차원에서 게이트웨이·어댑터로 SOAP 자산과 현대 API를 중계하고 변환 손실 검증 절차 운영.

## Ⅶ. 결론

- 핵심 요약 : SOAP은 메시지 계약과 표준 확장으로 기업 간 연계의 상호운용성을 담보하는 프로토콜.
- 표준화 편익이 구현·운영 복잡성 비용을 상회하는 연계 영역에서 전략적 선택 가치 유지.
