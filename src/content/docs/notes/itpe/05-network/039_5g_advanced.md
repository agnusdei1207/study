---
title: "5G-Advanced"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 5G-Advanced, 3GPP Release 18·19, RedCap(Reduced Capability)
- AI/ML 네이티브 무선 인터페이스, XR 인지 스케줄링
- NTN(Non-Terrestrial Network), NES(Network Energy Savings), Ambient IoT

## Ⅰ. 5G-Advanced의 개요

- 핵심 요약 : 상용 5G의 한계를 AI 무선 제어와 경량 단말, 위성 연동으로 보완하는 3GPP 고도화 단계.
- 개념 : 3GPP(3rd Generation Partnership Project) Release 18부터 시작되는 5G 규격의 고도화 단계인 **5G-Advanced**. Release 18·19를 거치며 6G로 이어지는 가교 역할을 수행함.
- 배경 및 필요성 : 초기 5G는 상향 용량 부족, 저가 IoT(Internet of Things) 단말의 대량 수용 한계, 기지국 전력 부담이 드러났고, XR(Extended Reality)과 지능형 공장 같은 신규 서비스의 규격적 뒷받침이 요구됨.
- 주요 목적 :
  1. 무선 인터페이스의 지능화
  2. 경량 IoT 생태계의 확장
  3. 위성을 포함한 커버리지 확장
  4. 망 에너지 효율의 개선

## Ⅱ. 5G-Advanced의 특징 및 장점

- 핵심 요약 : AI 기반 무선 제어와 서비스 맞춤형 기능이 효율과 실시간성을 동시에 높이는 구조.

1. **AI/ML 네이티브 무선 인터페이스** : 채널 상태 정보(CSI, Channel State Information) 피드백과 빔 관리·측위에 학습 모델을 적용 → 피드백 부담 감소와 빔 선택 정확도 향상.
2. XR 인지 스케줄링 : 프레임 주기와 트래픽 크기 특성을 스케줄러에 반영 → XR 트래픽의 지터 억제와 안정적 화질 유지.
3. **RedCap** (Reduced Capability) : 대역폭·안테나 수를 줄인 경량 단말 규격 → IoT 단말의 원가와 전력 소모 절감.
4. **NTN** (Non-Terrestrial Network) 고도화 : 위성·고고도 플랫폼과의 연동 규격 강화 → 지상망 음영 지역의 커버리지 보완.
5. **NES** (Network Energy Savings) : 트래픽 부하에 따른 기지국 절전 동작 → 운영 전력비 절감.
6. 사이드링크(Sidelink) 발전 : 단말 간 직접 통신 기능의 강화 → 차량 협력 주행과 무인 이동체 통신의 지연 단축.

## Ⅲ. 5G-Advanced의 구조 (흐름)

- 핵심 요약 : AI 네이티브 무선 인터페이스를 공통 기반으로 두고 서비스 기능과 절전·위성 연동이 얹히는 계층 구조.

```text
[ 기능 계층 구조 ]

AI/ML 네이티브 무선 인터페이스
(CSI 피드백 · 빔 관리 · 측위)
    ↓ 공통 기반
XR 인지 스케줄링 · RedCap · 사이드링크
    ↓ 서비스 기능
NTN 연동 · NES 절전
```

```text
[ NTN 연결 경로 ]

단말
    ↓ 서비스 링크
위성 (저궤도·중궤도·정지궤도)
    ↓ 피더 링크
지상 게이트웨이
    ↓
5G 코어망
```

- 규격 진행 방식 : Release 18에서 AI/ML 무선 적용과 XR 인지, 절전 기능을 연구·표준화하고, Release 19에서 배터리 없는 Ambient IoT(Ambient Internet of Things) 규격화와 통신-감지 융합(ISAC, Integrated Sensing and Communication) 연구를 이어감.

## Ⅳ. 5G와 5G-Advanced의 비교

- 핵심 요약 : 5G 인프라 위에 AI·경량 IoT·위성 연동을 추가해 성능 축을 넓힌 진화.

| 비교 축 | 5G (Release 15~17) | 5G-Advanced (Release 18~) |
| --- | --- | --- |
| AI/ML 적용 | 운영 관리 단계의 사후 분석 | 무선 물리 계층에 내장 |
| 상향 성능 | 하향 중심 설계 | 상향 다중 안테나·반송파 확장 |
| IoT 수용 | 고광대역과 저속 IoT의 양분 | RedCap·Ambient IoT의 중간층 형성 |
| 위성 연동 | NTN 기초 규격 | 연동 기능의 고도화 |
| 에너지 효율 | 상시 송신 중심 | 부하 기반 절전(NES) |
| 측위 정밀도 | 미터 수준 | 정밀 측위 규격의 강화 |

- 선택 기준 : 고성능 광대역 서비스는 기존 5G 기능으로, 저가 센서와 음영 지역 서비스는 5G-Advanced 규격으로 적용함.

## Ⅴ. 5G-Advanced의 한계와 방안

- 핵심 요약 : AI 모델 상호운용성과 위성 링크 전파 조건, 모델 보안을 생애주기 관리와 보상·검증 절차로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| AI 모델 상호운용성 부족 | 벤더별 모델 형식의 불일치로 기지국·단말 간 협업 실패 | 3GPP 기준의 모델 생애주기 관리(LCM, Life Cycle Management) 절차 적용 | 상호 시험 통과율 |
| NTN 도플러·전파 지연 | 저궤도 위성의 고속 이동으로 주파수 편이와 지연 증가 | 궤도 정보 기반 도플러 사전 보상과 핸드오버 타이밍 최적화 | 호 절단율 |
| AI 모델 변조 위험 | 무선 제어 모델의 조작 시 품질 저하·오동작 | 모델 서명과 무결성 검증, 배포 이력 관리 | 무결성 검증 실패율 |

## Ⅵ. 5G-Advanced에 대한 기술사적 제언

- 핵심 요약 : 6G 전환의 실증 기반과 산업 현장 적용, AI 보안 거버넌스를 병행 추진하는 방향.

1. 통신사업자와 연구기관은 AI 무선망·비지상망 기술을 5G-Advanced 시험망에서 검증하고, 그 결과를 6G 표준 대응 자산으로 축적할 필요가 있음.
2. 제조업 현장은 계측기·무인운반차(AGV, Automated Guided Vehicle)처럼 기존 5G 모듈이 과한 장비부터 RedCap 단말로 전환해 무선화 투자비를 낮춰야 함.
3. 정부와 표준화 단체는 무선 AI 모델의 공급망 검증 책임과 보안 기준을 규정해 상용 적용 전 안전성을 담보해야 함.

## Ⅶ. 결론

- 핵심 요약 : 5G-Advanced는 AI·경량 IoT·위성 연동으로 5G를 고도화하며 6G로 넘어가는 실증 단계임.
- 시사점 : 기능 확장의 지속성은 상호운용성과 보안 기준의 정비 속도에 의해 결정됨.
