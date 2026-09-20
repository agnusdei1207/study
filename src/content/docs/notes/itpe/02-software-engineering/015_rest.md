---
title: "REST(Representational State Transfer)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:25:00+09:00"
tags: ["notes-software-engineering"]
sidebar:
  badge:
    text: "A"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="분산 아키텍처에서 REST까지의 지식 경로"><span>SW 공학·아키텍처</span><span>분산 하이퍼미디어</span><strong>REST</strong></div>

## 큰 그림과 30초 인출

```text
[Client] ── URI·표현·표준 메서드 ── [Resource]
   │                                   │
무상태·캐시 ── 계층 시스템 ── 균일 인터페이스

REST = 자원을 식별하고 표현을 교환하는 아키텍처 스타일
핵심 제약 = C/S + Stateless + Cache + Uniform + Layered (+ Code-on-demand)
```

## 예상문제

REST의 개념과 제약조건, 균일 인터페이스를 설명하고 REST API 설계 시 고려사항을 기술하시오.

## Ⅰ. 개요

- REST는 분산 하이퍼미디어 시스템을 위한 아키텍처 스타일로, 자원을 식별하고 그 상태의 표현을 표준화된 인터페이스로 전달한다.
- HTTP를 사용하는 API가 곧 REST인 것은 아니며 제약조건을 지켜야 확장성·가시성·독립성을 얻는다.

## Ⅱ. REST 제약조건

| 제약 | 핵심 효과 |
|---|---|
| Client–Server | 관심사 분리와 독립 진화 |
| Stateless | 요청 자체에 처리 문맥 포함, 수평 확장 |
| Cache | 응답의 재사용 가능성 명시, 지연 감소 |
| Uniform Interface | 구성요소 결합도 완화 |
| Layered System | 중간 계층을 통한 보안·확장 |
| Code-on-demand | 실행 코드 전달, 선택 제약 |

## Ⅲ. 균일 인터페이스

```text
자원 식별 → 표현을 통한 조작 → 자기서술 메시지 → HATEOAS
   URI          JSON/XML             메타데이터          링크로 상태 전이
```

- URI는 행위보다 자원을 나타내고, 메서드 의미와 안전성·멱등성을 보존한다.
- 미디어 타입, 상태 코드, 캐시 지시자와 링크가 메시지를 해석할 문맥을 제공한다.

## Ⅳ. API 설계 절차

| 단계 | 활동 |
|---|---|
| 자원 모델링 | 도메인 개체와 관계 식별 |
| URI 설계 | 계층과 식별자 일관화 |
| 행위 매핑 | 조회·생성·대체·부분변경·삭제 구분 |
| 표현 설계 | 스키마, 오류, 링크, 버전 정책 정의 |
| 운영 설계 | 인증, 제한, 캐시, 관측성 적용 |

## Ⅴ. REST와 RPC 비교

| 구분 | REST | RPC |
|---|---|---|
| 중심 | 자원과 상태 표현 | 원격 동작 호출 |
| 계약 | URI·메서드·미디어 타입 | 서비스·메서드 명세 |
| 결합 | 균일 인터페이스로 완화 | 동작 계약에 상대적으로 강함 |
| 적합 | 공개·웹 API, 느슨한 통합 | 내부 고성능·명령 중심 호출 |

## Ⅵ. 적용 시 고려사항

- 인증·인가와 TLS, 입력 검증을 적용하고 오류에 내부 정보를 노출하지 않는다.
- 재시도는 멱등성을 고려하고 조건부 요청과 idempotency key 등으로 중복 처리를 막는다.
- 페이지네이션·요청 제한·캐시 무효화·버전 호환성을 운영 정책에 포함한다.
- REST 성숙도를 메서드 사용 여부만으로 판단하지 말고 링크와 메시지 의미까지 검토한다.

## Ⅶ. 결론

REST의 가치는 HTTP 형식이 아니라 제약조건에서 나온다. 자원 모델과 균일 인터페이스를 일관되게 설계하고 보안·호환성·관측성을 함께 운영해야 한다.

## 1교시 10점 발췌

```text
REST = 자원의 표현을 교환하는 분산 아키텍처 스타일
제약: C/S·무상태·캐시·균일 인터페이스·계층·선택적 코드 전송
균일 인터페이스: 식별·표현 조작·자기서술·HATEOAS
```

## 공식 근거

- [Roy Fielding Dissertation, REST](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm): REST 제약조건의 원전
- [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110): HTTP 메서드와 상태 코드 의미
- [Q-Net 정보관리기술사](https://www.q-net.or.kr/): 국가기술자격 시험 및 공개문제 공식 창구

## 체크

- [ ] REST를 단순 HTTP API와 동일시하지 않았는가?
- [ ] 여섯 제약조건과 균일 인터페이스를 설명했는가?
- [ ] 멱등성·캐시·보안·호환성을 포함했는가?

## 연결 토픽

- [MSA](./035_msa/)
- [DevOps](./002_devops/)
- [무중단 배포](./007_zero_downtime_deployment/)
