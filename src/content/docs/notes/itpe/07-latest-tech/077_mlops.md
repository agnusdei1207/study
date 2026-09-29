---
title: "MLOps(Machine Learning Operations)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "077. MLOps(Machine Learning Operations)"
  order: 77
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

<div class="itpe-topic-path" aria-label="지식 경로">
IT 운영·데이터 과학 > 머신러닝 시스템 라이프사이클 > MLOps
</div>

## 30초 인출

- 본질: 머신러닝 모델의 개발(Dev)과 운영(Ops)을 유기적으로 통합하여 데이터 수집, 모델 학습, 배포, 모니터링 등 전 주기를 자동화하고 반복 가능하게 관리하는 엔지니어링 실천 체계.
- 메커니즘: 데이터·코드·파이프라인 버전 제어 $\rightarrow$ 지속적 통합(CI) 및 지속적 훈련(CT) 기반 자동 평가 $\rightarrow$ 모델 레지스트리 검증·승인 $\rightarrow$ 지속적 배포(CD) 및 모니터링 $\rightarrow$ 드리프트 감지 기반 피드백 재학습.
- 통찰: 단순 재학습 자동화 파이프라인 구축에 치중할 경우 데이터 편향과 침묵적 성능 저하(Silent Failure)가 증폭되므로 모델 레지스트리 기반 전 주기 계보 추적과 실시간 드리프트 감지 통제 체계 확립 필수.

<details><summary>핵심 용어</summary>

- **MLOps(Machine Learning Operations):** 머신러닝 시스템의 개발, 배포, 운영 전 주기를 자동화하여 지속적인 모델 품질과 서비스 안정성을 보장하는 방법론.
- **지속적 통합(CI, Continuous Integration):** 파이프라인 코드와 데이터 검증 컴포넌트를 자동으로 빌드하고 단위·통합 테스트를 수행하는 체계.
- **지속적 배포(CD, Continuous Deployment):** 검증을 통과한 머신러닝 파이프라인 및 서빙 모델을 프로덕션 환경에 무중단 배포하는 자동화 과정.
- **지속적 훈련(CT, Continuous Training):** 운영 환경의 데이터 드리프트 또는 정해진 스케줄에 따라 학습 파이프라인을 자동 트리거하여 새 모델을 생성하는 고유 속성.
- **모델 레지스트리(Model Registry):** 학습된 모델 아티팩트의 메타데이터, 하이퍼파라미터, 성능 평가 지표, 버전 및 계보(Lineage)를 중앙 집중 관리하는 저장소.
- **데이터 드리프트(Data Drift):** 운영 환경에서 유입되는 입력 데이터의 통계적 분포가 학습 데이터의 분포와 달라져 모델 예측력이 저하되는 현상.
</details>

---

## 2~4교시 예상문제 (25점)

> 머신러닝 시스템 운영에서 발생하는 기술적 부채와 운영 복잡성을 해결하기 위한 MLOps(Machine Learning Operations)의 개념, 필요성, 핵심 구성요소를 설명하고, Google Cloud MLOps 성숙도 3단계(Level 0~2) 및 프로덕션 환경에서의 신뢰성 확보 방안을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 머신러닝 라이프사이클 통합 관리, MLOps의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 머신러닝 모델의 기획, 데이터 전처리, 모델 개발(Dev), 검증, 프로덕션 배포 및 운영(Ops) 전 과정을 자동화·표준화하는 엔지니어링 프레임워크 |
| 목적 | 데이터·모델의 재현성 확보, 배포 주기 단축, 프로덕션 환경 내 데이터 드리프트 대응, 고품질 예측 서비스의 지속적 제공 |

- 전통적 소프트웨어 공학과 달리 머신러닝 시스템은 코드(Code)뿐만 아니라 데이터(Data)와 모델(Model)이라는 3대 축의 상태 변화를 지속적으로 관리해야 하는 고유 특성 보유.
- 데이터 과학자와 운영 엔지니어 간의 협업 단절(Silo)을 해소하고 '숨은 기술 부채(Hidden Technical Debt)'를 최소화하기 위한 표준 파이프라인 필수.

## Ⅱ. MLOps의 핵심 특징 및 구성요소

| 핵심 특징 | 세부 내용 | 구현 메커니즘 |
|---|---|---|
| 데이터·코드 결합 관리 | 단순 소스코드 외 대규모 학습 데이터셋과 피처의 버전 동시 추적 | DVC(Data Version Control), Feast 피처 스토어 기반 데이터셋 형상 관리 |
| 지속적 훈련(CT) | 운영 데이터의 변화 감지 시 자동으로 모델을 재학습하는 파이프라인 구비 | Kubeflow Pipelines, Airflow 기반 이벤트 트리거 워크플로우 엔진 |
| 모델 계보(Lineage) 추적 | 배포된 모델이 어떤 데이터, 코드, 하이퍼파라미터로 학습되었는지 역추적 | MLflow Tracking, Weights & Biases 기반 아티팩트 메타데이터 로깅 |
| 드리프트 모니터링 | 예측 정확도 외 입력 데이터의 통계적 분포 및 개념 드리프트 실시간 감시 | Evidently AI, Prometheus 기반 통계 모니터링 및 알람 체계 |

| 3대 핵심 구성요소 | 주요 역할 | 대표 기술 스택 |
|---|---|---|
| Feature Store | 온/오프라인 피처의 일관성 보장, 학습-서빙 편향(Skew) 방지 | Feast, Hopsworks, AWS SageMaker Feature Store |
| Model Registry | 학습 완료 모델의 패키징, 거버넌스 승인 상태 관리, 카나리 롤아웃 제어 | MLflow Model Registry, Vertex AI Model Registry |
| CI/CD/CT Pipeline | 코드 통합, 컨테이너 빌드, 자동 학습, 모델 성능 검증 및 무중단 배포 | GitHub Actions, Argo Workflows, Kubeflow, KServe |

## Ⅲ. MLOps 파이프라인 아키텍처 및 라이프사이클 프로세스

```text
+-------------------------------------------------------------------------------------------------+
|                                    MLOps End-to-End Architecture                                |
+-------------------------------------------------------------------------------------------------+
 [Data Sources] ---> [Data Engineering] ---> [Feature Store] ---> [Continuous Training (CT)]
   - Raw DB / Log      - Ingestion / Cleansing   - Feature Repo     - Auto Feature Extraction
   - Event Stream      - Validation (TFDV)       - Online/Offline   - Distributed Training
                                                                            |
                                                                            v
 [Monitoring & Ops] <--- [Serving & CD] <--- [Model Registry] <--- [Evaluation & Validation]
   - Data Drift Check      - Triton / KServe   - Versioning/Staging - Benchmark Test
   - Concept Drift Check   - Canary / Shadow   - Governance Approve - Fairness / Explainability
   - Silent Failure Log    - API Endpoint      - Artifact Metadata  - Quality Gate Pass
           |
           +-------------------- [Trigger Retraining Loop] --------------------+
```

| 파이프라인 단계 | 핵심 수행 절차 및 제어 기법 |
|---|---|
| 1. 데이터 검증 및 관리 | TFDV(TensorFlow Data Validation)를 통한 스키마 이상치 검출, 피처 스토어 등록 |
| 2. 지속적 훈련(CT) | 분산 컴퓨팅 클러스터(Ray, Spark) 기반 하이퍼파라미터 튜닝(HPO) 및 모델 재학습 |
| 3. 모델 검증 및 등록 | 베이스라인 모델 대비 성능 비교, 공정성·설명가능성 검증 통과 시 Model Registry 등록 |
| 4. 지속적 배포(CD) | 컨테이너 이미지 패키징 후 카나리(Canary) 또는 섀도(Shadow) 배포로 무중단 롤아웃 |
| 5. 운영 관측 및 피드백 | KS-Test, PSI(Population Stability Index) 기반 드리프트 측정 시 CT 파이프라인 재호출 |

## Ⅳ. Google Cloud MLOps 성숙도 모델 및 타 패러다임 비교

| 성숙도 단계 | 운영 방식 | 배포 주기 및 파이프라인 특징 | 자동화 수준 |
|---|---|---|---|
| Level 0: 수동 프로세스 | 데이터 과학자가 로컬 스크립트로 학습 및 파일 전달 | 수개월 소요, 수동 배포, 피드백 루프 부재 | 완전 수동, 재현성 취약 |
| Level 1: ML 파이프라인 자동화 | 모델 학습 파이프라인 자동화, 지속적 훈련(CT) 구현 | 수일~수주 소요, 자동 재학습, 데이터 유효성 검사 | CT 자동화, 코드 배포는 수동 |
| Level 2: CI/CD 파이프라인 자동화 | 파이프라인 코드 자체의 빌드·테스트·배포 자동화 | 수시간~수일 소요, 모듈식 파이프라인, 풀 자동화 | CI/CD/CT 완벽 통합 |

| 비교 항목 | DevOps | MLOps | LLMOps |
|---|---|---|---|
| 핵심 관리 대상 | 소스코드, 빌드 아티팩트 | 코드, 데이터셋, 모델 가중치, 피처 | 프롬프트, 파운데이션 모델, RAG 벡터DB |
| 변경 유발 요인 | 비즈니스 요구, 버그 수정 | 데이터 드리프트, 환경 변화, 성능 저하 | 지식 업데이트, 환각(Hallucination), 정렬 |
| 테스팅 중점 | 단위/통합 테스트, 부하 테스트 | 데이터 스키마, 모델 성능 지표, 편향 검증 | 프롬프트 평가, RAG 검색 정확도, 안전성 |
| 배포 산출물 | 실행 파일, 컨테이너 이미지 | 추론 서비스 컨테이너, 모델 바이너리 | LLM API 엔드포인트, 벡터 인덱스 파이프라인 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 학습-서빙 편향(Training-Serving Skew) 및 데이터 드리프트 발생에 따른 무음 성능 저하 | 오프라인 배치 피처와 온라인 실시간 피처를 단일 정의로 공유하는 Feature Store 구축 및 PSI 기반 통계 모니터링 알람 체계 연동 |
| 재학습(CT) 트리거의 오작동 및 오염된 데이터셋 학습으로 인한 모델 붕괴 위험 | 섀도 배포(Shadow Deployment)를 통한 프로덕션 실트래픽 검증 및 자동 품질 게이트(Quality Gate) 실패 시 즉시 이전 모델 롤백 체계 수립 |
| 데이터·코드·모델 가중치·하이퍼파라미터 간 다차원 의존성으로 인한 재현성 결여 | 불변(Immutable) 스토리지 기반 메타데이터 계보 관리 및 컨테이너화된 파이프라인(Kubeflow/MLflow) 환경 고정 |

## Ⅵ. 제언

MLOps는 개별 툴 도입이 아닌 데이터 거버넌스와 배포 신뢰성을 연결하는 전사적 엔지니어링 문화 정착 필수.

```text
[Engineering Culture] ---> [Feature/Model Governance] ---> [Automated Drift Retraining]
  - Data/ML/DevOps 협업       - Immutable Lineage Log        - PSI 기반 이상 감지
  - 규제 준수 및 승인 절차     - Quality Gate 자동 통과       - Canary 트래픽 점진 전환
```

| 관점 | 단기 구축 과제 | 중장기 성숙 과제 |
|---|---|---|
| 기술 관점 | MLflow 기반 실험 추적 및 모델 레지스트리 표준화 | 온/오프라인 통합 피처 스토어 및 완전 자동화 CI/CD/CT 파이프라인 |
| 조직 관점 | 데이터 과학자와 MLOps 엔지니어 간 R&R 정의 | 전사 모델 거버넌스 위원회 운영 및 AI 신뢰성 모니터링 체계 내재화 |

## 출제 이력과 검증 출처

- 제130회 정보관리기술사 2교시: MLOps의 개념, 필요성, 핵심 구성요소 및 Google MLOps 성숙도 Level 0~2 단계별 특징.
- Google Cloud Architecture Center, MLOps: Continuous delivery and automation pipelines in machine learning.
- Sculley et al., Hidden Technical Debt in Machine Learning Systems, NeurIPS.

## 연결 토픽

- 모델 수명주기 거버넌스: [모델옵스(ModelOps)](./020_modelops.md)
- 대규모 언어모델 운영: [LLMOps](./053_llmops.md)
- 딥러닝 아키텍처 기초: [인공신경망(ANN)](./084_ann.md)
