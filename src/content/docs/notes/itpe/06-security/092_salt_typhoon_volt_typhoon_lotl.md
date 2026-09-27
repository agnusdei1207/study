---
title: "Salt Typhoon / Volt Typhoon (LotL)"
author: "Codex"
date: "2026-09-27T17:11:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 92
  label: "092. Salt Typhoon / Volt Typhoon (LotL)"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

위협 분석 → 정상 도구 악용(LotL) → 공개 침해 경보 비교

## 30초 인출

- 본질: LotL은 정상 도구·기능을 공격에 악용하는 전술이며 Volt Typhoon과 Salt Typhoon은 공개 경고의 대상·목적을 구분해야 하는 별개 활동
- 메커니즘: 엣지 장비·유효 계정 접근 → 정상 도구의 비정상 사용 → 계정·명령·네트워크 로그 상관분석으로 탐지

---

<details><summary>핵심 용어</summary>

- LotL: 공격자가 정상 관리 도구와 기능을 악용하는 전술.
- 엣지 장비: 외부와 내부 네트워크 사이에서 서비스·접속을 중개하는 장비.

</details>

## 1교시 예상문제 (10점)

> LotL 전술과 Volt Typhoon·Salt Typhoon 관련 공개 경고를 구분하여 설명하시오. (예상·10점)

---

## 1교시 10점 답안

**공통 개요**

| 구분 | 핵심 |
|---|---|
| 정의 | LotL은 기존 관리 도구·기능을 공격에 악용하는 전술이며 Volt Typhoon과 Salt Typhoon은 구분되는 공개 위협 활동 |
| 목적 | 활동별 경보 범위 구분과 계정·장비·행위의 이상 징후 탐지 |

LotL(Living off the Land)은 공격자가 시스템에 존재하는 정상 관리 기능·도구와 유효 계정을 악용하는 전술. CISA 등은 Volt Typhoon의 미국 핵심 인프라 접근·사전 배치 위험과 Salt Typhoon 관련 통신·네트워크 사업자 침해를 각각 경고. 두 활동을 동일한 공격 조직·단일 침해 경로로 합치지 않음. 정상 도구의 사용 자체보다 호출 계정·시간·명령·네트워크 목적지의 조합을 분석하고 엣지 장비·계정을 보호.

---

## 2~4교시 예상문제 (25점)

> Volt Typhoon과 Salt Typhoon의 공개 경고 범위를 구분하고, LotL 전술에 대한 엣지·계정·행위 분석 중심 방어를 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

**공통 개요**

| 구분 | 핵심 |
|---|---|
| 정의 | LotL은 기존 관리 도구·기능을 공격에 악용하는 전술이며 Volt Typhoon과 Salt Typhoon은 구분되는 공개 위협 활동 |
| 목적 | 활동별 경보 범위 구분과 계정·장비·행위의 이상 징후 탐지 |

### Ⅰ. 용어와 사건 구분
LotL은 정상 기능 악용 방식이며 악성코드가 전혀 없다는 뜻은 아님. Volt는 핵심 인프라 사전 배치 위협 평가, Salt 관련 활동은 통신 분야 첩보 침해 경고라는 발표 범위 구분.

### Ⅱ. 탐지 흐름
```text
엣지 장비·계정 로그 수집 → 평소 관리 작업과 다른 시간·주체·대상 식별
→ 명령 실행·네트워크 흐름 상관분석 → 자격증명 보호·격리·조사
```

### Ⅲ. 방어 통제
| 층위 | 조치 |
|---|---|
| 장비 | 인터넷 노출 엣지 자산 파악, 지원 종료 장비 교체, 패치 |
| 신원 | 관리자 계정 분리, 다중 인증, 최소 권한 |
| 탐지 | 정상 관리 도구의 비정상 사용·외부 통신과 중앙 로그 연계 |
| 복구 | 침해 범위 확인, 키·계정 교체, 서비스 연속성 훈련 |

공개 경보에 없는 특정 감청 대상, 실제 물리 파괴, 100% 탐지 회피 주장은 제외.

## 기술사적 제언

두 공개 경보의 대상·목적을 섞지 않고 엣지 자산과 정상 관리 도구의 사용 맥락을 함께 분석한다.

## 출제 이력과 검증 출처

- 확인한 제132~140회 공식 문제지에서 이 표제어의 직접 출제를 확인하지 못함. 그 밖의 회차는 원문 미대조.
- [CISA·NSA·FBI 등, Volt Typhoon 핵심 인프라 침해 공동 권고(AA24-038A)](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [CISA 등, 통신·네트워크 서비스 사업자 침해 공동 권고(AA25-239A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a)
