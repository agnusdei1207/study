---
title: "XaaS(Everything as a Service)"
author: "Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  label: "119. XaaS(Everything as a Service)"
  order: 119
  badge:
    text: "응용"
extra:
  model: "GPT-6"
  keyword_grade: "응용"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 클라우드 컴퓨팅 → XaaS

## 30초 인출

- 본질: XaaS는 IT 기능과 자원을 서비스로 제공하고 사용자가 필요에 따라 이용하는 모델
- 메커니즘: 이용자가 API로 기능을 요청하면 제공자가 운영·계량하고 계약에 따라 책임·비용을 나눔
- 통찰: 한계: 서비스 이름만으로 책임·종료 비용을 알 수 없음 → 방안: 업무별 책임·사용량·반출 조건을 도입 전에 시험한다.

<details>
<summary>핵심 용어</summary>

- **XaaS(Everything as a Service):** 인프라·플랫폼·소프트웨어 등 기능을 서비스 형태로 제공하는 모델
- **IaaS(Infrastructure as a Service):** 컴퓨팅·스토리지·네트워크 기반 자원을 제공하는 서비스
- **PaaS(Platform as a Service):** 애플리케이션 개발·실행에 필요한 플랫폼을 제공하는 서비스
- **SaaS(Software as a Service):** 완성된 애플리케이션을 네트워크로 제공하는 서비스
- **공유 책임 모델(Shared Responsibility Model):** 제공자와 이용자의 보안·운영 책임을 서비스 경계에 따라 나누는 원칙

</details>

---

## 2~4교시 예상문제 (25점)

> XaaS의 개념과 주요 서비스 유형을 설명하고, 도입 시 고려사항과 적용 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. XaaS의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **XaaS(Everything as a Service):** IT 기능·자원을 서비스로 제공해 네트워크로 이용하는 모델 |
| 목적 | 초기 구축 부담을 낮추고 필요한 기능을 수요에 맞게 이용 |

### Ⅱ. XaaS의 특징

| 특징 | 의미 |
|---|---|
| 서비스 추상화 | 인프라·플랫폼·응용 기능을 네트워크/API로 이용 |
| 수요 기반 이용 | 사용량에 따라 확장·축소하고 계량·과금 |
| 책임 분담 | 제공자 운영 범위와 이용자 설정·데이터 책임을 계약으로 확정 |

### Ⅲ. 서비스 이용 체계·프로세스

**핵심 서비스 프레임**

```text
이용자 업무·API 요청 → 계약·권한 확인 → 제공자 서비스(I/P/SaaS 등)
                                     → 인프라·플랫폼·응용 운영
                    ← 결과·상태·사용량 계량 ← 서비스 자원
                      ↓ 과금·SLA 검증·확장/회수
```

**하위 메커니즘: 서비스 종료·전환**

```text
종료 요청 → 계정·데이터·API 의존 확인 → 데이터 반출
          → 대체 서비스 복구·검증 → 접근권 회수·잔여 데이터 삭제 확인
```

### Ⅳ. 주요 유형과 이용자 책임 비교

| 유형 | 제공자 운영 범위 | 이용자 관리 초점 |
|---|---|---|
| IaaS | 물리 인프라·가상화 | OS·응용·데이터 |
| PaaS | 인프라·실행 플랫폼 | 응용·데이터·설정 |
| SaaS | 인프라·플랫폼·응용 | 계정·데이터·설정 |

### Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 제공자 API·데이터 형식에 종속 | 표준 인터페이스와 실제 반출·대체 경로 시험 |
| 사용량 변동으로 비용 예측 어려움 | 태그·예산·경보로 비용을 계량·재평가 |
| 제공자와 이용자의 통제 책임 혼선 | 서비스별 책임 매트릭스와 운영 절차 명시 |
| 외부 서비스 장애가 업무에 전파 | 복구 목표와 대체 경로를 업무 단위로 시험 |

### Ⅵ. 제언

도입 속도만 보면 사용량 증가와 종료 시 종속 비용이 가려진다. **핵심 업무는 책임·총비용·반출 가능성을 먼저 실증**하고, 운영 지표와 종료 조건을 계약에 반영한 뒤 적용 범위를 넓혀야 한다.

## 출제 이력과 검증 출처

- 제89회 1교시: `클라우드 서비스의 진화 모델인 XaaS(Everything as a Service)의 정의와 주요 구성 요소를 설명하시오.`
- 제101회 1교시: `XaaS(Everything as a Service)의 등장 배경, 서비스 유형 및 성공적인 도입을 위한 고려사항을 설명하시오.`
- [NIST SP 800-145 — The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final)
- [NIST SP 800-210 — General Access Control Guidance for Cloud Systems](https://csrc.nist.gov/pubs/sp/800/210/final)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 연결 토픽

- [클라우드 컴퓨팅](./013_cloud_computing/) · [클라우드 서비스 모델](./109_cloud_computing_service_models/)
