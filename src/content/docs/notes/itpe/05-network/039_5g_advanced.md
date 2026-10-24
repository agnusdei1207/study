---
title: "5G-Advanced"
author: "agnusdei1207"
date: "2026-10-24T22:49:07+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 5G-Advanced, 3GPP Release 18·19·20, RedCap, Ambient IoT
- 비지상망(NTN), 네트워크 에너지 절감(NES), AI/ML 네이티브 무선 인터페이스
- ISAC, 사이드링크(Sidelink), XR 인지 스케줄링, 도플러 사전 보상, 6G

## Ⅰ. 5G-Advanced의 개요

- 핵심 요약 : 5G 상용망의 한계를 AI 무선 인터페이스, 경량 IoT, 위성 연동으로 보완하며 6G로 이어지는 3GPP 고도화 규격.
- 개념 : 3GPP(3rd Generation Partnership Project) Release 18 이후 규격(Release 18·19·20)으로 정의되는 5G의 고도화 단계이며, 6G로 넘어가는 가교 역할을 하는 **5G-Advanced** 기술 규격.
- 배경 및 필요성 : 초기 5G는 상향 용량 부족, 대규모 IoT 수용 한계, 단말 전력 소모 문제를 드러냈고, 확장현실(XR, Extended Reality), 지능형 공장, 도심항공교통(UAM, Urban Air Mobility) 같은 신규 서비스를 수용할 규격이 요구됨.
- 주요 목적 :
  1. 인공지능(AI, Artificial Intelligence)·기계학습(ML, Machine Learning) 기반 무선 접속망(RAN, Radio Access Network) 최적화
  2. 경량 사물인터넷(IoT, Internet of Things) 기기 생태계 확장
  3. 비지상망(NTN, Non-Terrestrial Network) 연동 고도화
  4. 저전력 그린 네트워크 구현

## Ⅱ. 5G-Advanced의 특징 및 장점

- 핵심 요약 : 무선 물리 계층에 AI를 내장하고 서비스별 전송 특성에 맞춘 기능을 더해 효율과 실시간성을 함께 확보하는 구조.

1. **AI/ML 네이티브 무선 인터페이스** : 채널 상태 정보(CSI, Channel State Information) 피드백과 빔 관리, 측위에 학습 모델을 적용 → 피드백 부담 감소와 빔 선택 정확도 향상.
2. **XR 인지 스케줄링** : 프레임 크기와 주기적 발생 특성을 반영해 자원을 배분 → XR 패킷의 지연 지터 억제.
3. **RedCap** (Reduced Capability) : 대역폭과 수신 안테나 수를 줄인 경량 단말 규격 → 단말 원가와 전력 소모 절감, 웨어러블·센서 연결 확대.
4. **사이드링크(Sidelink)** : 기지국을 거치지 않고 단말끼리 직접 통신 → 차량 간 협력 주행과 무인 이동체 통신의 지연 단축.
5. **네트워크 에너지 절감** (NES, Network Energy Savings) : 트래픽 부하에 따라 송신 기능을 선택적으로 줄이는 절전 동작 → 기지국 운영 전력비 절감.
6. **통신-감지 융합** (ISAC, Integrated Sensing and Communication) : 무선 신호의 반사를 이용해 주변 객체를 감지하는 선행 기술 → 6G 감지 기능의 기반 확보.

## Ⅲ. 5G-Advanced의 구조 (흐름)

- 핵심 요약 : AI 네이티브 무선 인터페이스를 공통 기반으로 두고, 그 위에 XR·경량 단말·비지상망 기능이 얹히는 계층 구조.

```text
[ 5G-Advanced 기능 계층 ]

AI/ML 네이티브 무선 인터페이스
(CSI 피드백, 빔 관리, 측위)
          ↓
XR 인지 스케줄링 · RedCap · NTN
          ↓
네트워크 에너지 절감 (NES)
```

- **비지상망** (NTN, Non-Terrestrial Network) : 위성과 고고도 플랫폼을 포함하여 지상 기지국의 커버리지를 확장하는 망 구조.

```text
[ NTN 연결 경로 ]

단말
    ↓  위성 서비스 링크
위성 (저·중·정지궤도)
    ↓  위성 피더 링크
지상 게이트웨이
    ↓
5G 코어망
```

## Ⅳ. 5G와 5G-Advanced의 비교

- 핵심 요약 : 5G가 세운 인프라 위에 AI, 경량 IoT, 위성 연동을 더해 성능 축을 넓힌 진화.

| 비교 축 | 5G (Release 15~17) | 5G-Advanced (Release 18~20) |
| --- | --- | --- |
| AI/ML 적용 | 코어망과 운영관리(OAM, Operation, Administration and Maintenance) 단계의 사후 분석 | 무선 물리 계층에 내장 |
| 상향 성능 | 하향 중심 설계, 상향 용량 부족 | 상향 다중 안테나 전송과 다중 반송파 확장 |
| 단말 측위 | 측위 정밀도 한계 | 정밀 측위 규격 강화 |
| IoT 수용 | 확장 광대역(eMBB, enhanced Mobile Broadband)과 저속 IoT로 양분 | RedCap 고도화, 배터리 없는 Ambient IoT 규격화 진행 |
| 위성 연동 | NTN 기초 규격 | 위성 연동 기능 확장, 단말 직접 위성 연결 논의 |
| 에너지 효율 | 상시 전력 소모 | 트래픽 적응형 절전 (NES) |

- 선택 기준 : 고성능 광대역 서비스는 5G 상용망 기능으로, 저가 센서와 위성 음영 구간은 5G-Advanced 규격으로 나누어 적용.

## Ⅴ. 5G-Advanced의 한계와 방안

- 핵심 요약 : 이기종 AI 모델의 상호운용성과 위성 링크의 전파 특성이 핵심 한계이며, 모델 생애주기 관리와 위성 보정 절차로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| AI 모델 상호운용성 | 벤더별로 다르게 학습된 기지국·단말 모델의 인코딩·디코딩 불일치로 통신 실패 가능 | 3GPP 기준의 AI 모델 생애주기 관리(LCM, Life Cycle Management) 절차와 공통 검증 데이터 정비 | 모델 호환 시험 통과율 |
| NTN 도플러와 전파 지연 | 저궤도 위성의 고속 이동으로 도플러 편이와 왕복 지연 증가 → 핸드오버 지연 | 궤도력(Ephemeris) 기반 도플러 사전 보상, 타이머 기반 핸드오버 | 핸드오버 지연 시간, 호 절단율 |
| AI 모델 변조·적대적 공격 | 무선 제어에 쓰이는 모델이 조작되면 전송 품질 저하 | 모델 서명과 무결성 검증, 배포 이력 관리 | 무결성 검증 실패 건수 |

## Ⅵ. 5G-Advanced에 대한 기술사적 제언

- 핵심 요약 : 5G-Advanced를 6G 전환의 시험 기반으로 삼고, 산업 현장 도입과 AI 보안 거버넌스를 함께 갖추는 방향.

1. 6G 전환 테스트베드 활용 : 통신사업자와 연구기관이 AI 네이티브 무선망과 비지상망 연동 기술을 5G-Advanced 망에서 검증하고, 그 결과를 6G 표준화 대응 자산으로 축적할 필요가 있음.
2. 산업 현장 RedCap 조기 도입 : 공장의 비전 카메라, 무인운반차(AGV, Automated Guided Vehicle), 계측기처럼 5G 모듈이 과한 장비부터 RedCap 단말로 옮기면 공장 무선화 투자비를 낮출 수 있음.
3. AI 무선 보안 거버넌스 확립 : 무선 인터페이스에 올라가는 AI 모델의 공급망과 벤더 간 검증 책임을 사업자와 정부 차원에서 규정해야 함.

## Ⅶ. 결론

- 핵심 요약 : 5G-Advanced는 AI·경량 IoT·비지상망을 5G에 얹어 6G로 넘어가는 실증 단계.
- 시사점 : 상호운용성과 보안 기준이 갖춰져야 기능이 현장에 안정적으로 확산되며, 이 검증 기반이 6G 전환의 출발점이 됨.
