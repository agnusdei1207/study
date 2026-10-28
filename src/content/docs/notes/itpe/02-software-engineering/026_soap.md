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
- SOAP, XML, Envelope, WSDL, WS-Security, Fault, REST

### Ⅰ. SOAP의 개요

- 핵심 요약 : SOAP은 XML 메시지의 구조와 교환 규칙을 정의해 이기종 시스템 간 서비스 통신을 지원하는 프로토콜.
- 개념 : SOAP Envelope 안에 Header와 Body를 담아 요청·응답·Fault를 전달하며 다양한 전송 바인딩과 결합 가능(**SOAP**, Simple Object Access Protocol).
- 배경 및 필요성 : 기관·플랫폼 간 계약·보안·메시지 처리의 명확한 표준이 필요.
- 주요 목적 : 구조화된 메시지 교환과 WS-* 확장 기반 상호운용 제공.

### Ⅱ. SOAP의 특징 및 장점

- 핵심 요약 : 명시적 XML 봉투·스키마·오류형식과 WS-* 표준이 강한 계약·보안 요구에 적합.

1. 메시지 구조 : Envelope·Header·Body·Fault → 확장 메타데이터·오류 표현.
2. 계약 기반 : WSDL로 서비스·메시지·바인딩 기술 → 생성형 클라이언트·상호운용 지원.
3. 확장 표준 : WS-Security·WS-ReliableMessaging 등 → 기업간 보안·신뢰성 요구 대응.

### Ⅲ. SOAP 메시지 구조와 호출 (흐름)

- 핵심 요약 : WSDL 계약에 맞는 SOAP Envelope를 생성하고 서비스가 Body 처리 결과나 Fault 반환.

```text
SOAP Envelope
├─ Header: 보안 토큰·라우팅·트랜잭션 메타데이터
└─ Body: 요청/응답 데이터 또는 Fault
```

```text
서비스 계약(WSDL) → 요청 XML 생성 → HTTP 등 전송 바인딩
     → Header 검증·Body 처리 → SOAP 응답 또는 Fault
```

- 웹서비스 표준 조합 예 : SOAP 메시지, WSDL 서비스 기술, UDDI 서비스 등록·탐색.

### Ⅳ. SOAP과 REST 비교

- 핵심 요약 : SOAP은 명세·확장표준 중심 메시징, REST는 자원·HTTP 제약을 이용하는 아키텍처 스타일.

| 비교 축 | SOAP | REST |
|---|---|---|
| 메시지 | XML Envelope·Header·Body | JSON 등 자원 표현, HTTP 메서드·상태코드 |
| 계약 | WSDL로 강한 서비스 계약 | OpenAPI 등 별도 계약 활용 가능 |
| 확장 | WS-Security·신뢰성·트랜잭션 표준 | 웹 캐시·프록시·HTTP 인프라 활용 |
| 선택 | 엄격한 기업간 계약·WS-* 요구 | 웹·모바일 API의 단순성·캐시성 |

### Ⅴ. SOAP의 한계와 방안

- 핵심 요약 : XML·WS-* 구현 복잡성과 메시지 크기를 계약·게이트웨이·상호운용 시험으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| XML·확장 규약 복잡 | 개발·디버깅·성능 부담 | 필요한 WS-*만 선택하고 스키마 검증 자동화 | WS-* 적용 수 |
| 상호운용 차이 | 구현체별 해석 불일치 | WSDL·정책 프로파일·계약시험 공유 | 상호운용 결함 |
| 취약한 XML 처리 | XXE·과대 메시지 등 공격 | 외부엔티티 비활성화·크기 제한·서명 검증 | 보안 취약점 |

### Ⅵ. SOAP 적용 제언

- 핵심 요약 : 통합 아키텍트는 메시지 계약·전송바인딩·보안정책을 기준화하고 기존 소비자를 보호.

1. 서비스 오너는 WSDL·XSD·오류코드·버전 호환 정책을 저장소에서 관리.
2. 보안팀은 WS-Security 토큰·서명·암호화·재전송 방어를 위협모델과 함께 검토.
3. API 게이트웨이·어댑터로 SOAP과 현대 API를 중계하되 변환 손실·오류 의미 보존 시험.

### Ⅶ. 결론

- 핵심 요약 : SOAP은 XML 메시지 계약과 표준 확장으로 기업간 서비스 통신을 구조화하는 프로토콜.
- 시사점 : 강한 표준화의 편익이 구현·운영 복잡도보다 큰 통합 요구에서 선택.
