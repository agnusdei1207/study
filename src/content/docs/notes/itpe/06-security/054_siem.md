---
title: "SIEM(Security Information and Event Management)"
author: "OpenAI"
date: "2026-09-24T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

보안 운영 → 보안 로그 통합·분석 → 탐지·조사와 자동화 연계

## 30초 인출

- **본질**: SIEM은 여러 보안 로그를 중앙에서 모아 검색·분석하고 보안 이벤트 탐지와 조사를 지원하는 플랫폼.
- **메커니즘**: 로그 생성·수집 → 정규화·저장 → 상관분석·경보 → 분석자 조사 → 대응 도구와 필요 시 연계.
- **핵심**: 유효한 탐지는 로그 품질·탐지 규칙·관제 절차의 결합에 좌우.

<details><summary>핵심 용어</summary>

- **SIEM(Security Information and Event Management)**: 다양한 로그를 중앙에 수집해 분석·경보하는 보안 정보·이벤트 관리 플랫폼.
- **SOAR(Security Orchestration, Automation and Response)**: 보안 도구와 절차를 조정하고 반복 대응의 자동화를 지원하는 방식·플랫폼.
- **SOC(Security Operations Center)**: 보안 경보를 감시·분석하고 사고 대응을 조정하는 조직·운영 기능.
- **정규화(Normalization)**: 서로 다른 로그 필드와 표현을 분석에 사용할 공통 구조로 변환하는 처리.
- **상관분석(Correlation Analysis)**: 여러 이벤트 사이의 시간·주체·대상 관계를 찾아 사건 후보를 식별하는 분석.
- **UEBA(User and Entity Behavior Analytics)**: 사용자·시스템 개체의 행위 기준선과 변화를 분석하는 기능.
- **NIST(National Institute of Standards and Technology)**: 미국 연방 기술표준 기관으로 로그관리 지침을 발간.
</details>

---

## 1교시 예상문제 (10점)

---

> SIEM의 개념과 로그 수집·분석 흐름, 관제 운영 시 고려사항을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **SIEM(Security Information and Event Management)**은 다양한 로그를 중앙에 수집해 분석·경보하는 보안 정보·이벤트 관리 플랫폼. |
| 목적 | 분산된 이벤트의 연관 분석과 침해사고 조사에 필요한 가시성·근거 제공. |

### Ⅱ. 로그 처리·분석 흐름

```text
서버·네트워크·클라우드 로그
              ↓ 수집
      파싱·정규화·시간 정합
              ↓
          저장·검색
              ↓ 상관분석·탐지
        경보·분석자 조사
              ↓
       사건 대응·규칙 개선
```

로그 발생시각 정합과 필드 품질, 누락 감시가 분석의 전제.

### Ⅲ. 한 줄 제언

제언: 위협 시나리오에 필요한 로그부터 선정하고 경보 처리 결과를 규칙 개선에 환류.

---

## 2~4교시 예상문제 (25점)

---

> SIEM(Security Information and Event Management)과 SOAR(Security Orchestration, Automation and Response)를 비교하고, 침해 탐지·대응을 위한 연계방안을 설명하시오. (제135회 1교시 5번 취지 반영)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **SIEM(Security Information and Event Management)**은 다양한 로그를 중앙에 수집해 분석·경보하는 보안 정보·이벤트 관리 플랫폼. |
| 목적 | 분산된 이벤트의 연관 분석과 침해사고 조사에 필요한 가시성·근거 제공. |

## Ⅱ. 구성과 탐지 흐름

```text
로그 발생원 → 수집기 → 파싱·정규화·시간 정합 → 검색·보관
                                              ↓
                                   상관분석·탐지 규칙
                                              ↓
                                        경보·사건 후보
                                              ↓
                                        SOC 분석·판단
```

SIEM은 중앙 로그 수집과 검색뿐 아니라 데이터 간 관계 분석·경보를 지원. 수집 대상은 자산과 위협 시나리오에 맞춰 선정하고, 시간 동기화·필수 필드·지연·누락을 함께 관리.

## Ⅲ. 관제 품질과 로그 보호

| 관리축 | 핵심 점검 |
|---|---|
| 데이터 품질 | 출처·시간·필드 매핑·수집 지연·누락 |
| 탐지 품질 | 규칙 근거·오탐·미탐·조사 결과 환류 |
| 조사 가능성 | 검색성능·보존기간·접근권한·무결성 |
| 운영 품질 | 경보 우선순위·분석 책임·사건 연결 |

로그관리는 생성·전송·저장·접근·분석·폐기까지의 전 과정이며, SIEM 제품 기능만으로 조직의 로그 정책과 관제 절차를 대신할 수 없음.

## Ⅳ. SIEM·SOAR 역할 구분과 연계

```text
SIEM: 로그 수집·정규화·상관분석 → 경보·사건 맥락
                                      ↓ 승인된 연계
SOAR: 플레이북 조정 → 담당자 확인·정책 검사 → 반복 조치 실행
                                      ↓
                         결과·오탐 정보를 관제 개선에 환류
```

| 구분 | SIEM | SOAR |
|---|---|---|
| 중심 역할 | 로그 통합·분석·경보·조사 지원 | 보안 도구·절차의 조정과 반복 대응 자동화 |
| 입력·연계 | 시스템 로그·위협정보 | SIEM 경보·사건 맥락·승인 정책 |
| 운영 판단 | 규칙·경보 분류와 조사 | 플레이북 승인·실행 범위·예외 처리 |

자동 대응 가능 범위는 제품 연계와 조직의 승인 기준에 따라 다르며, 모든 SIEM이 차단 조치를 수행하거나 SOAR가 사람의 판단을 대체하는 것은 아님.

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 경보를 무차별 수집·자동 처리하면 분석 피로와 오탐 차단 위험이 커질 수 있음. | 위협 시나리오별 로그·경보를 선정하고 영향이 큰 조치는 사람 승인을 거치게 하며, 조사 결과로 탐지와 플레이북을 함께 개선하는 방안. |

## 출제 이력과 검증 출처

- 기존 노트에 기록된 제135회 1교시 5번 SIEM·SOAR 비교 취지를 보존한 예상 확장문항.
- [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final) — 로그 관리의 조직 차원 기반과 프로세스.
- [NIST SP 800-92 Rev. 1 status](https://csrc.nist.gov/projects/log-management) — Rev. 1은 2026-09 현재 초안 상태.
- [NIST glossary: SIEM](https://csrc.nist.gov/glossary/term/security_information_and_event_management) — 중앙 로그 관리 기능 정의.
