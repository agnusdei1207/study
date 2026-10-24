---
title: "Copilot+ PC NPU (NPU: Neural Processing Unit; PC: Personal Computer)"
author: "agnusdei1207"
date: "2026-10-24T22:41:35+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- Copilot+ PC, NPU(Neural Processing Unit), TOPS(Trillions of Operations Per Second)
- 온디바이스 AI(On-device AI), 수축기 어레이(Systolic Array), MAC(Multiply-Accumulate)
- DirectML, ONNX Runtime, SLM(Small Language Model), Windows Copilot Runtime
- Recall, Prism 에뮬레이션, 메모리 대역폭, 성능 대비 전력 효율(Performance-per-Watt)

## Ⅰ. Copilot+ PC NPU의 개요

- 핵심 요약 : 클라우드 연결 없이 PC에서 신경망 연산을 실행하기 위해 일정 수준 이상의 NPU를 요구하는 온디바이스 AI PC 표준.
- 개념 : 마이크로소프트가 정의한 AI PC 표준인 Copilot+ PC의 핵심 요건으로, 클라우드 연결 없이 로컬에서 신경망 모델을 실행하는 **신경망 처리 장치** (NPU, Neural Processing Unit)를 말함. 이 표준은 초당 40조 회 이상의 연산 성능을 뜻하는 **TOPS** (Trillions of Operations Per Second) 40 이상의 NPU를 요구함.
- 배경 및 필요성 : AI 추론을 전적으로 클라우드에 맡기면 개인정보 노출, 네트워크 지연, 서버 운영 비용이 문제가 되므로, 단말 안에서 AI 기능을 처리하는 **온디바이스 AI** (On-device AI) 요구가 커짐.
- 주요 목적 : 최소 40 TOPS 이상의 NPU 하드웨어 기준 충족, Windows의 AI 기능(리콜, 코크리에이터, 라이브 캡션) 가속, 배터리 사용 환경에서의 **성능 대비 전력 효율** (Performance-per-Watt) 확보.

## Ⅱ. Copilot+ PC NPU의 특징 및 장점

- 핵심 요약 : 행렬 연산에 특화된 하드웨어 설계와 OS 수준의 추론 런타임이 결합해 전력 효율과 개발 이식성을 함께 얻는 방식.

1. **수축기 어레이** (Systolic Array) : 행렬 곱셈 누적 연산인 **MAC** (Multiply-Accumulate) 결과를 메모리에 되돌리지 않고 인접 처리 요소로 파이프라인처럼 넘김 → 메모리 접근을 줄여 대역폭 소모와 전력 사용을 낮춤.
2. **DirectML** 및 ONNX(Open Neural Network Exchange) Runtime : 벤더별 NPU 차이를 OS 레벨에서 추상화 → 개발자가 하나의 ONNX 모델로 여러 NPU 하드웨어를 가속하여 이식 비용 절감.

## Ⅲ. Copilot+ PC NPU의 구조와 실행 스택

- 핵심 요약 : 기능 계층이 추론 런타임을 거쳐 NPU 드라이버로 내려가는 단방향 실행 경로이며, 메모리가 성능의 병목이 되는 구조.

```text
[ Copilot+ PC 실행 스택 ]

Windows AI 기능 (리콜, 라이브 캡션 등)
   ↓
Windows Copilot Runtime (온디바이스 소형 모델)
   ↓
DirectML / ONNX Runtime (추론 추상화)
   ↓
NPU 드라이버 실행
   ↓
NPU 하드웨어 (수축기 어레이, 온칩 버퍼)
```

- NPU는 전용 VRAM(Video Random-Access Memory)이 없어 시스템 메모리를 함께 쓰므로, 메모리 대역폭과 용량이 실제 AI 성능을 좌우하는 구조임.

## Ⅳ. 주요 Copilot+ PC 프로세서의 NPU 사양 비교

- 핵심 요약 : 세 플랫폼 모두 NPU 40 TOPS 이상을 충족하지만, NPU 아키텍처와 SoC 전체 성능, 호환성 측면의 차별점이 뚜렷함.

| 비교 항목 | Qualcomm Snapdragon X Elite | Intel Lunar Lake (Core Ultra 2) | AMD Strix Point (Ryzen AI 300) |
| :--- | :--- | :--- | :--- |
| NPU 아키텍처 | Hexagon NPU | Intel NPU 4 | AMD XDNA 2 |
| NPU 연산 성능 | 45 TOPS | 48 TOPS | 50 TOPS 수준 |
| SoC 전체 AI 성능 | 75 TOPS (CPU(Central Processing Unit), GPU(Graphics Processing Unit), NPU 합계) | 120 TOPS 수준 (GPU 포함) | 80 TOPS 이상 |
| 제조 공정 | TSMC 4nm | TSMC N3B | TSMC 4nm |
| 메모리 구성 | LPDDR5X-8448, 대역폭 약 135 GB/s | 패키지 내장 LPDDR5X | LPDDR5X 또는 DDR5 |
| 주요 차별점 | ARM64 기반의 긴 배터리 수명 | x86 호환성과 저전력 설계 | XDNA 2 기반의 높은 NPU 성능 |

- 위 수치는 각 제조사가 공개한 사양으로, 측정 조건에 따라 실제 체감 성능은 달라질 수 있음.

## Ⅴ. Copilot+ PC NPU의 한계와 방안

- 핵심 요약 : ARM 기기의 호환성 오버헤드, 화면 기록 기능의 보안 위험, 시스템 메모리 경합을 에뮬레이션 고도화, 기본 비활성화, 양자화로 각각 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| x86 소프트웨어 에뮬레이션 오버헤드 | ARM 기기에서 x86 및 x64 앱을 Prism 에뮬레이터로 실행하여 성능 저하와 일부 드라이버 호환 불가 | Prism 에뮬레이션의 JIT(Just-in-Time) 캐싱 고도화, 주요 상용 소프트웨어의 ARM64 네이티브 전환 | 에뮬레이션 실행 앱 비율, 앱별 응답 지연 |
| 리콜(Recall) 기능의 개인정보 노출 위험 | 화면을 주기적으로 캡처해 로컬 데이터베이스(DB, Database)에 저장하므로 악성코드 침투 시 화면 기록이 일괄 유출될 가능성 | 기본 비활성화(옵트인), Windows Hello 인증 연동, 가상화 기반 보안 영역 안에서 암호화 보관 | 기능 활성화율, 인증 실패 건수 |
| 시스템 메모리 경합 | 전용 VRAM(Video Random-Access Memory)이 없어 대형 SLM(Small Language Model)을 올리면 시스템 RAM(Random-Access Memory)을 점유 | 파라미터의 INT4 등 저정밀 양자화, 공유 메모리 페이징, 고속 SSD(Solid-State Drive) 기반 가중치 스트리밍 | 시스템 메모리 사용률, 모델 로딩 시간 |

```text
[ x86 앱 실행 경로 (ARM 기기) ]

x86 및 x64 앱
   ↓
Prism 에뮬레이터 (명령 변환)
   ↓
JIT 캐싱으로 변환 결과 재사용
   ↓
ARM64 네이티브 실행
```

## Ⅵ. 차세대 온디바이스 AI 컴퓨팅에 대한 기술사적 제언

- 핵심 요약 : 엔터프라이즈 업무 도구를 NPU 우선 구조로 설계하고, PC 자산 교체 기준을 CPU 클록에서 NPU 성능과 메모리 대역폭으로 옮기는 방향.

사내 메신저, 화상회의, 문서 요약처럼 민감도가 있는 업무는 고비용 클라우드 LLM(Large Language Model) API(Application Programming Interface) 호출을 줄이고, DirectML 기반으로 단말의 NPU를 활용하는 소형 언어 모델을 우선 검토하는 하이브리드 서빙 구조가 적절하다. 이때 데이터가 단말 밖으로 나가지 않는 범위와 클라우드로 넘기는 범위를 정책으로 구분해야 한다. 자산 교체 주기를 정할 때는 CPU 클록보다 NPU 성능과 메모리 대역폭을 기준 지표로 삼고, 향후 로컬 멀티모달 모델의 요구 수준이 높아질 가능성을 함께 반영하는 것이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : Copilot+ PC NPU는 40 TOPS 이상의 신경망 가속을 단말에서 제공해 AI 기능을 클라우드 의존에서 벗어나게 하는 온디바이스 AI 기반.
- 시사점 : 온디바이스 AI의 가치는 메모리 대역폭과 보안 통제가 함께 뒷받침될 때 성립하므로, 도입 시 성능 지표와 프라이버시 통제를 한 세트로 평가해야 함.
