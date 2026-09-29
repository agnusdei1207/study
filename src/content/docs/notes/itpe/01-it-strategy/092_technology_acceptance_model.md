---
title: "기술수용모델(TAM)"
author: "Claude Code"
date: "2026-09-29T22:46:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 정보시스템 도입·사용자 수용 → **기술수용모델(TAM)**

## 30초 인출

- 본질: 기술수용모델(TAM, Technology Acceptance Model)은 사용자가 정보기술을 받아들이는 이유를 유용하다는 믿음과 쉽게 쓸 수 있다는 믿음 두 가지로 설명하는 모델
- 메커니즘: 외부 변수가 지각된 사용 용이성(PEOU)과 지각된 유용성(PU)을 만들고, PEOU가 PU에 영향을 주며, 두 인식이 태도와 행동 의도(BI)를 거쳐 실제 사용으로 연결
- 통찰: 설문으로 잰 의도는 실제 사용과 어긋날 수 있고 PU를 낮추는 원인은 TAM만으로 구분되지 않으므로 사용 기록을 병행 측정하고 낮은 인식의 원인을 TAM2 요인으로 세분

<details>
<summary>핵심 용어</summary>

- **기술수용모델(TAM, Technology Acceptance Model)** : 지각된 유용성과 지각된 사용 용이성으로 정보기술의 사용 의도와 실제 사용을 설명하는 Davis의 모델
- **PU(Perceived Usefulness, 지각된 유용성)** : 특정 시스템을 쓰면 자신의 업무 성과가 나아질 것이라고 믿는 정도
- **PEOU(Perceived Ease of Use, 지각된 사용 용이성)** : 특정 시스템을 쓰는 데 노력이 들지 않을 것이라고 믿는 정도
- **BI(Behavioral Intention, 행동 의도)** : 기술을 사용하려는 의향. 실제 사용의 직접 선행 변수
- **외부 변수(External Variables)** : 시스템 특성처럼 PU·PEOU 인식에 영향을 주는 앞선 요인
- **TAM2** : PU의 형성 요인으로 사회적 영향 과정과 인지적 도구 과정을 추가한 Venkatesh·Davis의 확장 모델
- **UTAUT(Unified Theory of Acceptance and Use of Technology)** : 성과 기대·노력 기대·사회적 영향·촉진 조건으로 기술 수용을 설명하는 Venkatesh 등의 통합 이론

</details>

---

## 2~4교시 예상문제 (25점)

> 기술수용모델(TAM)의 개념과 주요 구성요소를 설명하고, 정보시스템 도입 평가에 적용할 때의 한계와 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 기술수용모델의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **기술수용모델(TAM, Technology Acceptance Model)** 은 지각된 유용성과 지각된 사용 용이성으로 정보기술의 사용 의도와 실제 사용을 설명하는 모델 |
| 목적 | 정보기술 수용·거부의 원인 설명과 도입 개선 요인의 도출 |

## Ⅱ. 두 가지 인식으로 수용을 설명하는 TAM의 특징

| 특징 | 의미 |
|---|---|
| 두 핵심 변수 | **PU** 와 **PEOU** 만으로 수용 설명 |
| 인식 중심 | 시스템의 객관적 성능이 아닌 사용자가 믿는 유용성·용이성 |
| 변수 간 경로 | PEOU가 PU에 영향을 주고, 두 변수가 의도를 거쳐 사용에 연결 |
| 의도와 사용의 구분 | 행동 의도와 실제 사용을 별개 변수로 취급 |

## Ⅲ. TAM의 구성요소와 TAM2의 PU 형성 요인

### TAM의 구성요소와 영향 경로

```text
외부 변수(시스템 특성 등)
    ↓
PEOU(지각된 사용 용이성) ── 쉬울수록 유용하다는 인식 ──→ PU(지각된 유용성)
    ↓                                                      ↓
    └────────────→ 태도(Attitude) ←────────────────────────┘
                       ↓
                  BI(행동 의도)
                       ↓
                   실제 사용
```

### PU 형성 요인 확대: TAM2

```text
PU(지각된 유용성)
    │
    ├─ 사회적 영향 과정 ── 주관적 규범·이미지 (조절: 자발성·경험)
    │
    └─ 인지적 도구 과정 ── 직무 관련성·산출물 품질·결과 입증성·PEOU
```

## Ⅳ. TAM·TAM2·UTAUT의 비교

| 비교축 | TAM | TAM2 | UTAUT |
|---|---|---|---|
| 핵심 변수 | PU·PEOU | PU 형성 요인이 추가된 PU·PEOU | 성과 기대·노력 기대·사회적 영향·촉진 조건 |
| 추가 관점 | 개인의 인식 | 사회적 영향과 인지적 도구 | 사용 환경을 뜻하는 촉진 조건 |
| 조절변수 | 없음 | 자발성·경험 | 나이·성별·경험·자발성 |
| 사용에 영향 | 행동 의도 | 행동 의도 | 행동 의도와, 촉진 조건의 직접 영향 |

## Ⅴ. TAM 적용의 한계와 방안

| 한계 | 방안 |
|---|---|
| 설문으로 잰 의도와 실제 사용의 불일치 | 설문과 함께 접속·기능 사용 기록의 병행 측정 |
| PU가 낮게 나온 원인 구분 불가 | 직무 관련성·산출물 품질·결과 입증성 문항을 추가한 TAM2 요인 진단 |
| 의무 사용·조직 환경에서 사회적 영향과 사용 환경의 미반영 | 자발성 조절을 두는 TAM2, 촉진 조건을 포함한 UTAUT의 선택 |
| 사용 빈도 중심 측정이 업무 성과에 준 영향을 반영하지 못함 | 사용 빈도와 함께 업무 성과 지표의 별도 확인 |

## Ⅵ. 제언

정보시스템 도입 평가 때 PU·PEOU 설문과 실제 사용 기록을 함께 측정하고, 낮게 나온 변수의 원인을 TAM2 요인으로 세분해 개선 대상 선정

### 수용 측정 구조

```text
도입 평가
    │
    ├─ 인식 ── PU·PEOU·BI 설문
    │
    └─ 행동 ── 접속·핵심 기능 사용 기록
```

### 측정 결과 확대: 낮은 변수의 원인 진단

```text
설문값과 사용 기록 대조
    ├─ PEOU 낮음 → 화면·절차 단순화, 사용 교육
    ├─ PU 낮음 → TAM2 요인 문항으로 원인 세분
    │       (직무 관련성·산출물 품질·결과 입증성·주관적 규범)
    └─ BI 높고 사용 낮음 → 권한·지원·인프라 등 사용 환경 점검
```

### 선택 근거: 전반 만족도 설문 중심 평가와의 비교

| 구분 | 만족도 설문 중심 평가 | 제언: 인식·행동 병행 측정 |
|---|---|---|
| 측정 대상 | 전반적 만족도 | PU·PEOU·BI와 실제 사용 기록 |
| 저조 원인 식별 | 변수별 구분 불가 | 낮은 변수와 TAM2 요인으로 구분 |
| 개선 조치 | 일괄 교육·홍보 | 변수별 조치 선택 |

## 출제 이력과 검증 출처

- 제133회 1교시 6번: 기술수용모델(Technology Acceptance Model; TAM)의 개념과 주요 구성요소
- Fred D. Davis(1989), Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology, MIS Quarterly 13(3)
- Davis·Bagozzi·Warshaw(1989), User Acceptance of Computer Technology: A Comparison of Two Theoretical Models, Management Science 35(8)
- Venkatesh·Davis(2000), A Theoretical Extension of the Technology Acceptance Model: Four Longitudinal Field Studies
- Venkatesh·Morris·Davis·Davis(2003), User Acceptance of Information Technology: Toward a Unified View, MIS Quarterly 27(3)

## 연결 토픽

- 연관 토픽: [전문성의 민주화](./098_democratization_of_expertise.md), [CoE](./082_coe.md)
- 비교 토픽: [TAM·SAM·SOM](./089_tam_sam_som.md)
