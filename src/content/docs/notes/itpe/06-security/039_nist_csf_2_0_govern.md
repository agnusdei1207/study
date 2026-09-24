---
title: "NIST CSF 2.0 (Govern 기능)"
author: "OpenAI"
date: "2026-09-24T22:25:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  model: "GPT-6"
  keyword_grade: "서브"

---

## 지식 로드맵 내 현재 위치

정보보호 관리체계 → 사이버보안 위험관리 프레임워크 → NIST CSF 2.0의 Govern

## 30초 인출

- **본질**: NIST CSF(Cybersecurity Framework) 2.0은 조직이 사이버보안 위험을 이해하고 관리하도록 돕는 프레임워크.
- **메커니즘**: Govern이 위험관리 방향과 책임을 정하고, 다섯 운영 기능이 조직의 위험을 지속해서 다룸.

<details><summary>핵심 용어</summary>

- **NIST(National Institute of Standards and Technology, 미국 국립표준기술연구소)**: CSF를 발간하는 미국 연방 기관.
- **CSF(Cybersecurity Framework, 사이버보안 프레임워크)**: 조직의 사이버보안 위험관리 성과를 정리하고 개선하는 체계.
- **Govern(GV)**: 사이버보안 위험관리 전략·정책·역할·감독을 정하는 CSF 기능.
- **조직 프로파일(Organizational Profile)**: 조직의 현재 또는 목표 사이버보안 성과를 CSF 결과와 대조해 표현한 것.
- **구현 티어(Implementation Tier)**: 조직의 위험관리 거버넌스·관리 관행이 갖춘 엄격성과 일관성의 특성을 설명하는 범주.

</details>

---

## 1교시 예상문제 (10점)

> NIST CSF 2.0의 목적과 여섯 기능을 설명하고 Govern의 역할을 기술하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **NIST CSF 2.0**은 조직이 사이버보안 위험을 이해·평가·우선순위화·소통하도록 돕는 위험관리 프레임워크. |
| 목적 | 조직의 사이버보안 활동을 업무 목표와 위험관리 책임에 연결. |

### Ⅱ. 여섯 기능과 Govern

```text
                    ┌─ Identify (ID): 위험 이해
                    ├─ Protect (PR): 위험 저감
Govern (GV) ────────┼─ Detect (DE): 이상 탐지
위험 방향·책임 설정 ├─ Respond (RS): 사고 대응
                    └─ Recover (RC): 복구
```

다섯 운영 기능은 고정된 순서가 아닌 동시·지속적 활동이며, Govern은 이를 조직의 위험관리 방향·책임과 연결.

### Ⅲ. 한 줄 제언

경영진이 위험 수용 기준과 책임자를 정하고 이를 보안 활동의 우선순위와 자원 배분에 반영.

---

## 2~4교시 예상문제 (25점)

> NIST CSF 2.0의 구조와 여섯 기능, 조직 프로파일·구현 티어를 설명하고 Govern 중심의 적용 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **NIST CSF 2.0**은 조직이 사이버보안 위험을 이해·평가·우선순위화·소통하도록 돕는 위험관리 프레임워크. |
| 목적 | 조직의 사이버보안 활동을 업무 목표와 위험관리 책임에 연결. |

## Ⅱ. 여섯 핵심 기능

| 기능 | 핵심 역할 |
|---|---|
| Govern (GV) | 위험관리 전략·정책·역할·감독 설정 |
| Identify (ID) | 자산·맥락·위험 이해 |
| Protect (PR) | 위험 저감 보호조치 적용 |
| Detect (DE) | 잠재적 사이버보안 사건 발견 |
| Respond (RS) | 탐지된 사건에 대응 |
| Recover (RC) | 사건 후 자산·서비스 복구 |

## Ⅲ. Govern의 관계

```text
                        ┌─ Identify
                        ├─ Protect
Govern ────────────────┼─ Detect
전략·정책·역할·감독 ──┤   각 기능은 동시·지속적으로 운영
                        ├─ Respond
                        └─ Recover
```

이 도식은 선후 단계가 아니라 Govern과 다른 기능 사이의 관리상 관계를 나타냄. 화살표 대신 연결선을 사용해 순차 진행의 오해를 피함.

## Ⅳ. 프로파일과 티어

| 도구 | 무엇을 나타내는가 | 적용 |
|---|---|---|
| 현재 프로파일 | 현재의 CSF 결과·성과 상태 | 보유 통제와 위험관리 성과 정리 |
| 목표 프로파일 | 달성하려는 결과·성과 상태 | 업무 목표·위험 허용도에 맞춰 설정 |
| 구현 티어 | 위험관리 거버넌스·관리 관행의 엄격성과 일관성 특성 | 조직의 위험관리 맥락을 설명하는 보조 관점 |

```text
현재 프로파일 ── 차이·우선순위 분석 ── 목표 프로파일
       │                                      │
       └──── 개선 과제·책임·진척 관리 ───────┘
구현 티어: 위험관리 관행의 특성을 설명하는 별도 관점
```

티어는 현재·목표 프로파일을 대신하는 점수나 일률적인 성숙도 등급으로 해석하지 않음.

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 여러 부서가 CSF 기능별 점검만 수행하면 핵심 업무의 위험 우선순위와 개선 책임이 분리될 가능성. | 중요 업무 서비스 하나를 선정해 현재·목표 프로파일을 작성하고, 차이별 책임자·예산·완료 판단 기준을 경영진 위험 검토 일정에 포함하는 적용을 제안. |

## 출제 이력과 검증 출처

- 공식 기출 확인 불가. CSF 2.0 구조와 적용을 묻는 예상문항.
- [NIST: NIST Releases Version 2.0 of Landmark Cybersecurity Framework](https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework) — CSF 2.0 여섯 기능.
- [NIST CSF FAQs](https://www.nist.gov/cyberframework/faqs) — 기능은 동시·지속적으로 수행된다는 점.
- [NIST Organizational Profiles](https://www.nist.gov/cyberframework/profiles) — 현재·목표 프로파일 설명.
- [NIST SP 1302](https://csrc.nist.gov/pubs/sp/1302/final) — 구현 티어의 의미와 사용 시 주의사항.
