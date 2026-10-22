---
title: "함수적 종속성 (Functional Dependency, FD)"
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

**함수적 종속성(FD)**, **결정자/종속자**, **FFD/PFD/TFD**, **Armstrong 공리**, **폐포(Closure)**, **정규화**

## Ⅰ. 개요

- 핵심 요약 : **FD**는 $X \to Y$로 $X$ 값에 대해 $Y$가 유일하게 결정되는 관계.
- 목적 : 정규화의 수학적 토대, 이상 현상 제거.
- 배경 : 릴레이션 내 속성 간 종속 관계 분석 필요.
- 특징 : FFD/PFD/TFD, Armstrong 공리, 폐포.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **FD 유형 분류와 공리**로 정규화 설계 근거 제공.
- **FFD(완전)** : 복합키 전체에 종속 (2NF 조건).
- **PFD(부분)** : 복합키 일부에 종속 (2NF 위반).
- **TFD(이행)** : $X \to Y \to Z$ (3NF 위반).
- **Armstrong 공리** : 6대 추론 규칙.
- **폐포(Closure)** : 후보키 자동 도출.

## Ⅲ. 3유형·공리 흐름

- 핵심 요약 : **FFD/PFD/TFD** 유형과 **Armstrong 6공리**.
- FFD : $(학번,과목) \to 성적$.
- PFD : $(학번,과목) \to 학부$ (학번만으로 결정).
- TFD : 사번→부서코드→부서위치.

```text
[ FD 3유형 ]

FFD : 복합키 전체 종속 (2NF 조건)
PFD : 복합키 일부 종속 (2NF 위반)
TFD : 이행 종속 (3NF 위반)
```

```text
[ Armstrong 6공리 ]

1. 반사 : Y⊆X ⇒ X→Y
2. 첨가 : X→Y ⇒ XZ→YZ
3. 이행 : X→Y, Y→Z ⇒ X→Z
4. 분해 : X→YZ ⇒ X→Y, X→Z
5. 결합 : X→Y, X→Z ⇒ X→YZ
6. 유사이행 : X→Y, WY→Z ⇒ WX→Z
```

## Ⅳ. 종속성 유형 비교

- 핵심 요약 : **FFD/PFD/TFD** 정의·예시·정규화 연계.

| 유형 | 정의 | 예시 | 정규화 |
|---|---|---|---|
| FFD | 복합키 전체 종속 | (학번,과목)→성적 | 2NF 조건 |
| PFD | 복합키 일부 종속 | (학번,과목)→학부 | 2NF 위반 |
| TFD | 이행 종속 | 사번→부서코드→부서위치 | 3NF 위반 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **복잡도·거짓 종속성·관리 사각지대**를 자동 발견·교차 검증·CI 린트로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 복잡도 | 속성 수십~수백 시 조합 폭발 | TANE/FASTFD 자동 발견, 도메인 중심 압축 | 발견 정확도 |
| 거짓 종속성 | 샘플 데이터 우연 일치 | 데이터·비즈니스 교차 검증 | FD 정확도 |
| 관리 사각지대 | 문서화 부재로 재발 | 메타데이터 사전, CI DDL Validator | FD 문서화율 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **폐포 연산·반정규화 경계**.
- 폐포(Closure) : FD 집합에 Armstrong 공리 적용으로 후보키 도출.
- 반정규화 시 새로운 FD 발생 → 동기화 트리거·무결성 검증.

## Ⅶ. 결론

- 핵심 요약 : FD는 **정규화의 수학적 토대**로 FFD/PFD/TFD·Armstrong 공리가 핵심.
- 답안에는 FD 정의, 3유형, 공리, 한계·대응을 연결.
- 참고 : [Functional Dependency](https://en.wikipedia.org/wiki/Functional_dependency).