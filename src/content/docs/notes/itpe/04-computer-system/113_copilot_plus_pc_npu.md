---
title: "Copilot+ PC NPU (NPU: Neural Processing Unit; PC: Personal Computer)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- Copilot+ PC, NPU(Neural Processing Unit), TOPS(Trillions of Operations Per Second)
- 온디바이스 AI(On-device AI), 수축기 어레이(Systolic Array), MAC(Multiply-Accumulate)
- DirectML, ONNX Runtime, SLM(Small Language Model), Windows Copilot Runtime
- Prism 에뮬레이션, 리콜(Recall), 메모리 대역폭, 성능 대비 전력 효율(Performance-per-Watt)

## Ⅰ. Copilot+ PC NPU의 개요

- 핵심 요약 : 클라우드 의존 없이 PC 안에서 신경망 추론을 실행하기 위해 일정 성능 이상의 NPU 탑재를 요구하는 온디바이스 AI PC 표준.
- 개념 : 마이크로소프트가 정의한 AI PC 규격인 **Copilot+ PC**의 핵심 요건으로, 신경망 연산 전용 가속기인 **NPU** (Neural Processing Unit)의 성능이 **TOPS** (Trillions of Operations Per Second, 초당 조 단위 연산 횟수) 40 이상일 것을 요구하는 하드웨어 기준.
- 배경 및 필요성 : AI 기능을 클라우드에만 두면 개인정보 전송, 네트워크 지연, 서버 운영 비용이 상시 부담이 되므로 단말 안에서 추론을 끝내는 **온디바이스 AI** (On-device AI)가 필요.
- 주요 목적 : 배터리 환경에서의 성능 대비 전력 효율(Performance-per-Watt) 확보, Windows AI 기능의 로컬 가속, 데이터 단말 밖 반출의 최소화.

## Ⅱ. Copilot+ PC NPU의 특징 및 장점

- 핵심 요약 : 행렬 연산 특화 하드웨어와 OS 수준 추론 런타임의 결합이 전력 효율과 이식성을 함께 제공하는 원리.

1. **수축기 어레이** (Systolic Array) : 행렬 곱·누적 연산인 **MAC** (Multiply-Accumulate) 결과를 인접 처리 요소로 파이프라인 전달 → 메모리 접근 축소로 전력 효율 향상 효과.
2. 연산 장치 역할 분담 : NPU가 저전력 상시 추론을 담당하고 CPU(Central Processing Unit)와 GPU(Graphics Processing Unit)는 범용 연산·그래픽 처리에 집중 → 작업별 최적 가속으로 배터리 사용 시간 확보 효과.
3. 추상화 런타임 : **DirectML**과 ONNX(Open Neural Network Exchange) Runtime이 벤더별 NPU 차이를 흡수 → 하나의 모델로 여러 하드웨어를 지원하는 이식성 효과.
4. OS 통합 : Windows Copilot Runtime이 소형 모델과 추론 API(Application Programming Interface)를 OS에 포함 → 애플리케이션이 NPU를 쉽게 호출하는 생태계 효과.

## Ⅲ. Copilot+ PC NPU의 구조 (흐름)

- 핵심 요약 : 애플리케이션 기능에서 추론 런타임, NPU 드라이버, 하드웨어로 이어지는 단방향 실행 경로이며 메모리 대역폭이 성능 한계를 정함.

```text
[ 온디바이스 AI 실행 스택 ]

OS AI 기능 (요약, 검색, 자막)
   ↓
Windows Copilot Runtime (소형 모델)
   ↓
DirectML / ONNX Runtime
   ↓
NPU 드라이버
   ↓
NPU 하드웨어 (MAC 어레이)
```

```text
[ NPU 행렬 연산 파이프라인 ]

입력 데이터를 온칩 버퍼에 적재
   ↓
MAC 어레이의 곱셈·누산 수행
   ↓
결과를 인접 처리 요소로 전달
   ↓
메모리 왕복 없이 연산 지속
```

- NPU는 전용 비디오 메모리 없이 시스템 메모리를 공유하므로 메모리 대역폭과 용량이 실측 추론 성능을 좌우하는 구조가 됨.
- 모델 경량화는 파라미터 정밀도를 낮추는 양자화(Quantization)로 이루어지며 정밀도와 출력 품질의 균형이 중요해짐.

## Ⅳ. Copilot+ PC 프로세서 플랫폼의 비교

- 핵심 요약 : 주요 세 플랫폼이 모두 NPU 40 TOPS 기준을 충족하지만 아키텍처 기반과 SoC 전체 성능 구성에서 차별점을 가짐.

| 비교 축 | Snapdragon X Elite | Intel Core Ultra 200V | AMD Ryzen AI 300 |
| :--- | :--- | :--- | :--- |
| NPU 아키텍처 | Hexagon NPU | Intel NPU 4 | AMD XDNA 2 |
| NPU 성능 (제조사 공개) | 45 TOPS | 48 TOPS | 50 TOPS |
| 명령어 기반 | ARM64 | x86-64 | x86-64 |
| 메모리 구성 | LPDDR5X 별도 탑재 | 패키지 내장 LPDDR5X | LPDDR5X 또는 DDR5 |
| 강점 | 배터리 사용 시간 | x86 호환과 저전력 설계 | NPU 성능 수준 |

- 선택 기준 :
  1. 이동 중 배터리 지속이 우선이면 ARM64 기반 플랫폼.
  2. 기존 x86 소프트웨어 자산이 많으면 x86-64 플랫폼.
  3. 로컬 모델 규모 확대 계획이 있으면 NPU 성능과 메모리 대역폭을 우선 평가.

- 수치는 각 제조사가 공개한 사양 기준이며 측정 조건과 워크로드에 따라 체감 성능은 달라질 수 있음.

## Ⅴ. Copilot+ PC NPU의 한계와 방안

- 핵심 요약 : 에뮬레이션 오버헤드, 화면 기록 기능의 프라이버시 위험, 메모리 경합을 네이티브 전환, 옵트인 기본값, 양자화로 일대일 완화.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| x86 앱 에뮬레이션 부담 | ARM64 기기에서 명령 변환 수행 → 성능 저하와 일부 드라이버 미호환 | Prism 에뮬레이션 고도화와 주요 소프트웨어의 ARM64 네이티브 전환 | 에뮬레이션 실행 앱 비율 |
| 리콜(Recall) 프라이버시 위험 | 화면을 주기 캡처해 로컬 저장 → 유출 시 민감 정보 일괄 노출 | 기본 비활성화(옵트인), Windows Hello 연동 인증, 암호화 보관 | 기능 활성화율 |
| 시스템 메모리 경합 | 전용 메모리 부재로 대형 **SLM** (Small Language Model) 적재 시 RAM(Random-Access Memory) 점유 | INT4 등 저정밀 양자화와 고속 SSD(Solid-State Drive) 기반 가중치 스트리밍 | 메모리 사용률, 로딩 시간 |

## Ⅵ. Copilot+ PC NPU에 대한 기술사적 제언

- 핵심 요약 : 업무용 AI를 로컬 우선 하이브리드 구조로 설계하고 자산 교체 기준을 NPU 중심으로 옮기는 방향.
- 설계 : 업무 부문 조직이 문서 요약·회의 기록 같은 민감 업무부터 로컬 모델 우선, 클라우드 보조의 하이브리드 서빙 구조를 적용.
- 정책 : 보안 조직이 단말 내 처리 범위와 클라우드 전송 범위를 데이터 분류 정책으로 구분.
- 조달 : 자산 관리 조직이 PC 교체 기준을 CPU 클록에서 NPU 성능과 메모리 대역폭 중심 지표로 전환.

## Ⅶ. 결론

- 핵심 요약 : Copilot+ PC NPU는 신경망 가속을 단말 안으로 가져와 AI 기능을 클라우드 의존에서 분리하는 온디바이스 AI 기반이 됨.
- 시사점 : 그 가치는 메모리 대역폭과 프라이버시 통제가 함께 뒷받침될 때 성립함.
