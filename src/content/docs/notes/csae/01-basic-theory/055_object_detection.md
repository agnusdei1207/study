---
title: "객체 탐지 — YOLO·R-CNN(Object Detection)"
date: "2026-09-20T11:00:00+09:00"
tags:
  - "notes-basic-theory"
sidebar:
  badge:
    text: "B · 기출 · 60%"
extra:
  source_status: "기출"
  source_history: "126회"
  priority: 60
  priority_note: "[출제:126]"
---

## 답안 골격
```text
[객체 탐지] ◀━━ 머리: Ⅶ 내 의견 (실시간성과 소형 객체 탐지 정확도 양립을 위한 FPN 결합 1-Stage 구조 채택)
 ┃
 ┣━ Ⅰ 개요 ───── 단순 이미지 분류 한계 → 객체의 위치 좌표(Bounding Box)와 클래스 분류를 동시 수행하는 컴퓨터 비전
 ┣━ Ⅱ 양대 ───── 2-Stage Detector(영역 제안 후 분류: R-CNN 계열) vs 1-Stage Detector(단일 통합 추론: YOLO 계열)
 ┣━ Ⅲ 구조 ───── 백본(Backbone) $\to$ 넥(Neck: FPN) $\to$ 헤드(Head: 바운딩 박스 회귀 + 클래스 확률)
 ┣━ Ⅳ 흐름 ───── 이미지 입력 $\to$ 그리드 분할 및 앵커 박스 매칭 $\to$ IoU 계산 $\to$ 비최대 억제(NMS) 중복 제거
 ┣━ Ⅴ 비교 ───── Faster R-CNN vs YOLO vs SSD (검출 속도 FPS, mAP 정확도, 하드웨어 요구사항)
 ┗━ Ⅵ 실무 ───── 비최대 억제(NMS) 연산 병목 · 소형 객체(Small Object) 미탐 · 온디바이스 NPU 실시간성
```
- 필수 키워드: 바운딩 박스 · 2-Stage Detector · 1-Stage Detector · RPN · YOLO · IoU · NMS
- 배점 전략: 10점 = Ⅰ 개요 → Ⅱ 2-Stage vs 1-Stage 아키텍처 비교도 → Ⅳ NMS 후처리 흐름 → Ⅴ 종합 비교표

## 한 줄 본질
- 이미지 안에 무엇이 어디에 있는지를 동시에 찾아내기 위해 영역 제안과 분류를 분리하거나 단일 그리드 회귀로 통합 → 실시간 객체 추적 달성 / 1-Stage의 소형 객체 정확도와 2-Stage의 연산 속도 상충

## 핵심 그림
```text
[2-Stage: Faster R-CNN]                   [1-Stage: YOLO]
 [입력 이미지]                              [입력 이미지]
      |                                          |
      v                                          v
 [Feature Map]                              [단일 통합 신경망 (S x S 그리드)]
      |                                          |
      +---> [ RPN: 영역 제안 ]                     v
      |            |                         [그리드 셀별 바운딩 박스 + 클래스]
      v            v                             |
 [ RoI Pooling / Align ]                         v
      |                                    [비최대 억제 (NMS)]
      v                                          |
 [분류 및 박스 미세조정]                           v
 (정확도 우수, 속도 느림)                    [최종 탐지 결과 (초고속 실시간)]
```

## 핵심 통찰
- Faster R-CNN은 RPN(Region Proposal Network)을 통해 객체가 있을 법한 후보 영역을 먼저 수천 개 추려낸 후 별도의 분류망을 태우므로 정확도가 높지만 FPS가 낮음
- YOLO는 전체 이미지를 $S \times S$ 그리드로 분할하고 각 셀에서 바운딩 박스 좌표와 클래스 확률을 단 1회의 순전파(End-to-End)로 한꺼번에 예측하므로 60 FPS 이상의 초고속 실시간성을 확보함
- 겹치는 수많은 후보 박스 중 신뢰도가 가장 높은 박스만 남기고 나머지를 제거하는 NMS(Non-Maximum Suppression) 후처리 알고리즘이 필수적임

## 이웃 토픽과 구분
- 2-Stage (Faster R-CNN) vs 1-Stage (YOLO):
| 비교 항목 | Faster R-CNN (2-Stage) | YOLO (1-Stage) |
|---|---|---|
| 파이프라인 | 영역 제안(RPN) $\to$ 세부 분류 2단계 | 단일 신경망에서 좌표 회귀와 분류 동시 수행 |
| 추론 속도 | 느림 (5~15 FPS 수준) | 극도로 빠름 (30~100+ FPS) |
| 탐지 정확도 (mAP) | 소형 객체 및 고밀도 객체 탐지에 우수 | 과거 낮았으나 최신 버전(v8/v10)에서 대등 수준 |
| 주 활용 분야 | 정밀 의료 영상 판독, 위성 사진 분석 | 자율주행, 실시간 CCTV 관제, 로봇 비전 |

## 문제·원인·대책
- 적용 상황: 고속도로 자율주행 차량 전방 카메라 실시간 장애물 인지
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 원거리 소형 낙하물 미탐지(False Negative) | 고해상도 이미지가 다운샘플링되면서 소형 객체의 특성 맵 정보 소실 | 다양한 스케일의 특성 맵을 상하로 결합하는 특성 피라미드(FPN) 구조 채택 | 멀티 스케일 객체 탐지율 향상 |
| 동일 객체에 대한 중복 바운딩 박스 다수 발생 | 복수의 앵커 박스가 높은 신뢰도를 가져 단일 객체에 박스 중첩 | IoU 기반 NMS 또는 소프트 NMS(Soft-NMS) 임계값 필터링 적용 | 중복 제거 및 깔끔한 단일 박스 도출 |

## 이렇게 출제된다
- 제126회 1교시: "객체 탐지(Object Detection)에서 1-Stage Detector와 2-Stage Detector의 동작 메커니즘 및 장단점 비교" → 요구 포인트: RPN 기반 2-Stage vs 통합 그리드 1-Stage 구조도, IoU 및 NMS 개념, 실시간성 vs 정확도 트레이드오프

## 내 의견
- [실시간성과 소형 객체 탐지 정확도 양립을 위한 FPN 결합 1-Stage 구조 채택] 자율주행 임베디드 보드에서 2-Stage 모델은 연산량이 과중하여 30 FPS를 충족하지 못하고, 단순 1-Stage는 원거리 소형 장애물을 놓치는 안전성 결함이 존재함 → 나라면: 백본과 헤드 사이에 경로 집합 네트워크(PANet)와 FPN(Feature Pyramid Network)을 결합한 최신 YOLO 아키텍처를 적용하고, TensorRT를 활용한 FP16 엔진 컴파일 및 NMS의 GPU 커널 병렬화를 통해 60 FPS의 고속 실시간성과 원거리 장애물 인지 정확도를 동시 확보
