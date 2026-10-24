---
title: "가치사슬(Value Chain)"
author: "agnusdei1207"
date: "2026-10-24T23:50:58+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "Claude Haiku 5.5"
---

## 연관 키워드

- 가치사슬 (Value Chain), 마이클 포터 (Michael Porter)
- 주 활동 (Primary Activities), 지원 활동 (Support Activities), 마진 (Margin)
- ABC (Activity-Based Costing, 활동기준원가계산), ISP (Information Strategy Planning), BPR (Business Process Reengineering)
- 가치 네트워크 (Value Network), 네트워크 효과, 양면 시장 (Two-sided Market), 락인 (Lock-in)
- SCM (Supply Chain Management), MES (Manufacturing Execution System), WMS (Warehouse Management System)
- CRM (Customer Relationship Management), ERP (Enterprise Resource Planning), API (Application Programming Interface)
- 탈중개 (Disintermediation)

## Ⅰ. 가치사슬의 개요

- 핵심 요약 : 기업 활동을 주 활동과 지원 활동으로 나눠 경쟁 우위의 원천을 찾는 포터의 분석 프레임워크.
- 개념 : 마이클 포터(Michael Porter)가 제시한 **가치사슬** (Value Chain) 모델로, 제품과 서비스가 고객에게 전달되기까지의 활동을 주 활동과 지원 활동으로 나눠 경쟁 우위와 **마진** (Margin, 활동이 만들어 낸 최종 부가가치)의 원천을 분석하는 도구.
- 배경 및 필요성 : 경쟁 우위는 단일 부서가 아니라 활동 전체의 결합에서 나오므로, 비즈니스 프로세스 전반의 강점과 약점을 체계적으로 파악하고 IT 혁신 영역을 찾을 기준이 필요.
- 주요 목적 : 활동별 원가 동인과 차별화 요인 파악, 비부가가치 활동 제거, **업무 프로세스 재설계** (BPR, Business Process Reengineering)와 **정보화 전략 계획** (ISP, Information Strategy Planning) 수립의 틀 제공.

## Ⅱ. 가치사슬의 특징 및 장점

- 핵심 요약 : 주·지원 활동 분류와 활동 간 연결을 분석해 원가와 차별화의 근거를 드러내는 모델.

1. **주 활동** (Primary Activities) : 투입, 운영, 산출, 마케팅·영업, 서비스의 흐름에서 고객 가치가 생기는 지점을 탐색 → 핵심 개선 대상 특정.
2. **지원 활동** (Support Activities) : 인프라, 인적자원, 기술 개발, 조달이 주 활동을 돕는 방식을 확인 → 지원 비용 효율화.
3. 활동 간 연결 : 한 단계의 변경이 다른 단계의 비용과 품질에 미치는 영향 파악 → 부분 최적화의 함정 회피.
4. **활동기준원가계산** (ABC, Activity-Based Costing) : 활동별 비용 동인을 측정 → 원가 구조와 투자 우선순위 정리.
5. 마진 관점 : 활동 전체가 만든 가치와 비용을 연결 → 경쟁 우위의 근거 설명.

## Ⅲ. 가치사슬의 구조 (흐름)

- 핵심 요약 : 지원 활동이 주 활동을 보조하고, 그 결과가 마진으로 수렴하는 구조.

```text
[ 지원 활동 ]
기업 인프라 · 인적자원 · 기술 개발 · 조달
          ↓ 보조
[ 주 활동 ]
투입 → 운영 → 산출 → 마케팅·영업 → 서비스
          ↓
[ 마진 ]
기업의 최종 부가가치
```

- 지원 활동은 기업 인프라, 인적자원 관리, 기술 개발, 조달 활동으로 구성됨.
- 주 활동은 물류 투입, 운영과 생산, 물류 산출, 마케팅과 영업, 서비스로 구성됨.

## Ⅳ. 전통적 가치사슬과 디지털 가치 네트워크의 비교

- 핵심 요약 : 선형 파이프라인의 전통 가치사슬과 참여자 간 상호작용에 기대는 가치 네트워크를 대비.

```text
[ 전통 가치사슬 ] 선형 파이프라인
          ↓ 디지털 전환
[ 가치 네트워크 ] 다면 플랫폼
```

| 비교 항목 | 전통적 가치사슬 | 디지털 가치 네트워크 (Value Network) |
| --- | --- | --- |
| 구조 형태 | 선형 파이프라인 (일방향 흐름) | 비선형 다면 플랫폼 (상호 연결) |
| 가치 창출 방식 | 기업 내부 단계별 부가가치 누적 | 고객, 파트너, 개발자 간 상호작용과 네트워크 효과 |
| IT의 역할 | 활동별 비용 절감과 프로세스 자동화 도구 | 생태계를 연결하는 비즈니스 모델 자체 |
| 핵심 성공 요인 | 규모의 경제, 제조 원가와 물류 최적화 | 네트워크 효과, 양면 시장 장악, 데이터 락인 |

## Ⅴ. 가치사슬 분석의 한계와 방안

- 핵심 요약 : 선형 구조, 연결 효과의 정량화 한계, 중개자 등장에 따른 가치 단계의 변화를 보완해야 디지털 사업에 적용 가능.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 플랫폼 네트워크 효과 표현 한계 | 선형 흐름으로는 참여자 간 상호작용 가치가 빠짐 | 고객과 파트너를 포함한 가치 네트워크 분석 병행 | 생태계 참여자 수 |
| 활동 간 시너지와 비용 전가의 정량화 곤란 | 공통 비용의 배분 기준이 불명확 | ABC와 프로세스 마이닝으로 활동별 시간과 원가 측정 | 활동별 원가 정확도 |
| **탈중개** (Disintermediation) 발생 | 디지털 중개자가 기존 가치 단계를 대체 | 산업 구조를 주기적으로 검토하고 **API** (Application Programming Interface) 기반 신규 연결 설계 | 단계별 매출 비중 |

## Ⅵ. 가치사슬 기반 IT 전략 수립에 대한 기술사적 제언

- 핵심 요약 : 엔드투엔드 디지털 연결, 핵심 활동 중심의 IT 투자, 개방형 가치 네트워크 전환을 세 축으로 삼는다.

1. 엔드투엔드 디지털 연결 : 공급망관리(SCM, Supply Chain Management), 제조실행시스템(MES, Manufacturing Execution System), 창고관리시스템(WMS, Warehouse Management System), 고객관계관리(CRM, Customer Relationship Management), 전사적 자원관리(ERP, Enterprise Resource Planning)를 끊김 없는 실시간 파이프라인으로 연결한다.

```text
[ 투입 ] SCM 연계
      ↓
[ 생산 ] MES 연동
      ↓
[ 산출 ] WMS 연계
      ↓
[ 영업 ] CRM 연동
      ↓
[ 결산 ] ERP 반영
```

2. 핵심 활동 중심의 IT 투자 : 모든 활동에 같은 예산을 배분하지 않고, 원가 우위나 차별화 같은 **본원적 경쟁 전략**을 뒷받침하는 활동에 투자 우선순위를 준다.
3. 개방형 가치 네트워크 전환 : 오픈 API를 열어 외부 파트너와 가치를 공동으로 만드는 방식으로 비즈니스 모델을 고도화한다.

## Ⅶ. 결론

- 핵심 요약 : 가치사슬은 경쟁 우위 분석과 IT 혁신 영역 도출의 기반이 되는 프레임워크.
- 시사점 : 활동별 원가 동인의 측정과 개방형 연결을 함께 추진해야 디지털 시대의 경쟁 우위가 지속됨.
