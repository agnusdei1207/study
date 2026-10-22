---
title: "인과관계(Causation)와 인과추론"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

**인과관계(Causation)**, **루빈 잠재결과(RCM)**, **Pearl DAG**, **RCT**, **PSM**, **DID**, **IV**, **Uplift Modeling**

## Ⅰ. 개요

- 핵심 요약 : **인과추론**은 개입(Intervention)이 결과에 미치는 인과 효과를 규명하는 분석 방법.
- 목적 : "행동 변경 시 어떤 일이 벌어질 것인가" 의사결정 지원.
- 배경 : 예측(상관)은 환경 변화 시 실패 → 인과 필요.
- 특징 : RCM(잠재결과), Pearl DAG(do-연산자), RCT/PSM/DID/IV.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **잠재결과·DAG·do-연산자**로 인과 효과 격리.
- **RCM** : $Y(1)-Y(0)$, 반사실 문제, ATE 추정.
- **Pearl DAG** : Backdoor Path 식별, do(T)로 화살표 절단.
- **RCT** : 무작위 배정으로 교란변수 균형 (골드 스탠다드).
- **PSM** : 성향점수 매칭으로 관측 교란 통제.
- **DID/IV** : 준실험 설계, 내생성 극복.

## Ⅲ. 인과추론 기법 흐름

- 핵심 요약 : **RCT → PSM → DID → IV** 4대 기법.
- RCM : 개별 인과 효과는 관측 불가 (반사실), ATE 추정.
- Pearl : DAG로 Backdoor Path 식별, do-연산자로 개입 효과.

```text
[ 인과 그래프 (DAG) ]

[교란변수 Z] (연령)
   /        \
  v          v
[처치 T] --> [결과 Y]
(Z->T 화살표 절단 = do(T) 개입)
```

```text
[ 4대 인과추론 기법 ]

RCT  : 무작위 배정 (골드 스탠다드)
PSM  : 성향점수 매칭 (관측 교란 통제)
DID  : 이중차분법 (평행 추세 가정)
IV   : 도구변수 (내생성 극복)
```

## Ⅳ. 4대 기법 비교

- 핵심 요약 : **RCT·PSM·DID·IV** 메커니즘·적용 조건·한계.

| 기법 | 메커니즘 | 적용 조건 | 한계 |
|---|---|---|---|
| RCT | 무작위 배정 | 실험 가능 | 윤리·비용 |
| PSM | 성향점수 매칭 | 관측 데이터 | 숨은 교란 |
| DID | 전후 차이 차감 | 평행 추세 | 추세 위반 |
| IV | 도구변수 활용 | 유효 도구변수 | 발굴 어려움 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **교란변수·평행 추세·고차원**을 IV·합성 대조군·DML로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 숨은 교란변수 | 관측 데이터에서 내생성 왜곡 | IV, IPW, 민감도 분석(Rosenbaum) | ATE 신뢰도 |
| 평행 추세 위반 | 사전 트렌드 상이 | Event Study 검증, Synthetic Control | 추세 검정 |
| 고차원 복합 상호작용 | 수백 교란·비선형 | DML, Causal Forests | 모델 적합도 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **DID·Uplift Modeling**으로 비즈니스 적용.
- A/B 불가 환경 : DID + 합성 대조군.
- Uplift Modeling : Persuadables 식별, CRM 마케팅.
- 상관≠인과 구분 필수.

## Ⅶ. 결론

- 핵심 요약 : 인과추론은 **개입 효과 규명** 기법으로 RCM·DAG·RCT/DID가 핵심.
- 답안에는 잠재결과, DAG, 4대 기법, 한계·대응을 연결.
- 참고 : [Causal Inference: The Mixtape](https://mixtape.scunning.com/).