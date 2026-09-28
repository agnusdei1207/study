---
title: "Copilot+ PC NPU"
author: "Gemini 3.8 Flash"
date: "2026-09-24T21:00:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  label: "113. Copilot+ PC NPU"
  order: 113
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 온디바이스 AI → Copilot+ PC NPU

## 30초 인출

- 본질: Copilot+ PC는 로컬 AI 기능을 겨냥해 Microsoft가 정의한 Windows PC 범주로, 40+ TOPS NPU를 포함
- 메커니즘: Windows ML이 기기와 모델에 맞는 실행 제공자를 선택해 NPU·GPU·CPU에서 로컬 추론
- 통찰: 한계: 40+ TOPS 조건만으로 모델 실행·기능 지원이 보장되지 않음 → 방안: 대상 기기의 모델 호환성과 지연·전력을 실측한다.

<details>
<summary>핵심 용어</summary>

- **NPU (Neural Processing Unit)** : 신경망 연산을 가속하도록 설계된 프로세서
- **TOPS (Tera Operations Per Second)** : 초당 1조 회 연산을 뜻하는 처리량 단위
- **Copilot+ PC** : 40+ TOPS NPU 등 정해진 하드웨어 요구를 갖춘 Windows PC 범주
- **Windows ML** : ONNX Runtime 기반으로 Windows 기기의 CPU·GPU·NPU 실행 제공자를 사용하는 추론 프레임워크
- **DirectML (Direct Machine Learning)** : Direct3D 12 기반의 기계학습 가속 API로, 지원되지만 신규 Windows ONNX 기능 개발은 Windows ML 중심

</details>

---
## 2~4교시 예상문제 (25점)

> Copilot+ PC의 NPU·소프트웨어 실행 구조를 설명하고, 온디바이스 AI 도입 시 고려사항을 제시하시오. (예상)

---
## 2~4교시 25점 답안

### Ⅰ. Copilot+ PC와 NPU의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Copilot+ PC NPU는** Copilot+ PC 범주의 40+ TOPS 요구에 포함되는 신경망 연산 가속기 |
| 목적 | 지원되는 AI 추론 작업을 기기에서 가속 |

### Ⅱ. Copilot+ PC NPU의 특징

| 특징 | 의미 |
|---|---|
| 하드웨어 기준 | Copilot+ PC 범주에 40+ TOPS NPU 요구 |
| 로컬 AI | 지원 모델의 추론을 기기에서 실행할 수 있음 |
| 실행 환경 의존 | 모델 연산자·실행 제공자·드라이버·Windows 버전에 따라 지원 차이 |

### Ⅲ. 로컬 추론 체계·프로세스

**핵심 실행 체계**

```text
응용·Windows AI API → Windows ML(ONNX Runtime)
                    → 기기·모델 호환 실행 제공자 선택
                    → NPU / GPU / CPU에서 추론 → 결과 반환
```

**하위 메커니즘: 모델 배포 전 검증**

```text
업무 모델 선정 → 대상 장치·Windows 버전 확인
              → 연산자·정밀도·실행 제공자 호환성 시험
              → 품질·지연·전력 측정 → 데이터 저장·전송 경로 확인
```

### Ⅳ. 평가 기준 비교

| 기준 | TOPS 사양 확인 | 실제 업무 모델 시험 |
|---|---|---|
| 의미 | NPU의 이론적 연산 처리량 | 해당 모델의 기기별 추론 결과 |
| 확인 가능 | 범주 진입 하드웨어 조건 | 호환성·지연·전력·정확도 |
| 남는 과제 | 연산자·런타임 지원 여부 | Windows 버전·배포·데이터 경로 관리 |

### Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| TOPS만으로 모델·앱 호환성이 정해지지 않음 | 모델·연산자·드라이버·실행 제공자 조합을 시험 |
| 기능 지원이 장치·OS 버전에 따라 다름 | 대상 기기·Windows 버전의 지원 매트릭스 관리 |
| 로컬 추론도 로그·동기화로 정보가 외부에 나갈 수 있음 | 저장·전송·백업 경로를 별도로 검증 |

### Ⅵ. 제언

TOPS 수치로 장비를 고르면 실제 업무 모델의 호환성이나 지속 성능을 놓칠 수 있다. **업무 모델과 대상 PC 조합을 먼저 확정**하고 Windows ML 실행 경로에서 정확도·응답시간·전력·데이터 흐름을 측정한 결과로 도입을 결정해야 한다.

## 출제 이력과 검증 출처

- [Microsoft Copilot+ PC developer guide](https://learn.microsoft.com/ko-kr/windows/ai/npu-devices/): 40+ TOPS·장치 내 NPU 개발
- [Microsoft Windows ML overview](https://learn.microsoft.com/windows/ai/new-windows-ml/overview): 최신 로컬 추론 프레임워크와 실행 제공자
- [Microsoft DirectML overview](https://learn.microsoft.com/en-us/windows/ai/directml/): DirectML 유지와 신규 개발 방향
