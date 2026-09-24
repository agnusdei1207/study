---
title: "위성·공중·지상 통합망(SATIN·NTN)"
author: "OpenAI Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-network"]
sidebar: { badge: { text: "A" } }
extra: { keyword_grade: "A", model: "GPT-5.6 Sol" }
---
<p class="itpe-byline">작성 모델 · GPT-6<br />작성 · 2026.09.24 21:00 KST</p>
## 지식 로드맵 내 현재 위치
<div class="itpe-topic-path" aria-label="지식 경로"><span>차세대 이동통신</span><span>비지상 통합 접속</span><strong>SATIN·NTN</strong></div>

## 큰 그림과 30초 인출
- 본질: 위성·공중 플랫폼·지상망을 공통 서비스와 이동성 제어 아래 결합함
- 메커니즘: 궤도·전파·지연이 다른 Access를 위치·품질·부하 정책으로 선택하고 Handover함
- 산출: 음영지역·재난·해상·항공까지 이어지는 광역 연속 커버리지임
| 병렬 Access | 구성 | 역할 |
|---|---|---|
| Space | GEO(Geostationary Earth Orbit)·MEO(Medium Earth Orbit)·LEO 위성 | 광역 Coverage |
| Air | HAPS·UAV(Uncrewed Aerial Vehicle) | 지역 보강·재난 복구 |
| Terrestrial | 지상 기지국·5G Core | 고용량 접속·서비스 제어 |

<div class="itpe-flow itpe-flow--vertical" aria-label="SATIN 통합 관계"><div class="itpe-flow__node"><strong>병렬 Access</strong><small><b>입력:</b> Space · Air · Terrestrial Link 상태</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><span class="itpe-keyword"><strong>통합 제어</strong></span><small><b>처리:</b> 경로 선택 · 이동성 · 서비스 정책</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>서비스 연속성</strong><small><b>산출:</b> 광역 Coverage · 장애 우회</small></div></div>
<details><summary>핵심 용어</summary>

- `SATIN(Satellite-Aerial-Terrestrial Integrated Network)`: 이질 Access를 통합 제어하는 전체 망 관점임
- `NTN(Non-Terrestrial Network)`: 위성·공중 플랫폼을 이용하는 3GPP 비지상 접속망임
- `HAPS(High-Altitude Platform Station)`: 성층권에서 지역 커버리지를 제공함
- `LEO(Low Earth Orbit)`: 낮은 궤도로 지연을 줄이나 빠른 이동·Handover가 필요함
</details>

---

## 1교시 예상문제 (10점)
> SATIN과 NTN의 개념 및 구성 계층을 설명하시오. (예상)

---

## 1교시 10점 답안
### Ⅰ. 정의·목적
- 정의: **SATIN(Satellite-Aerial-Terrestrial Integrated Network)** 은 위성·공중 플랫폼·지상망을 통합해 3차원 접속을 제공하는 네트워크다.
- 목적: 지상망의 음영 지역과 재난 단절을 보완해 접속을 이어 간다.

| 계층 | 역할 |
|---|---|
| Space | 위성으로 광역 접속 제공 |
| Air | 공중 플랫폼으로 지역 보강 |
| Terrestrial | 지상 기지국·코어망으로 고용량 서비스 제공 |
| 통합 제어 | 링크 품질과 이동성에 따라 경로 선택·전환 |

- 제언: 지연·가용성·전환 연속성을 서비스별로 시험한다.

---

## 2~4교시 예상문제 (25점)
> SATIN·NTN의 구조와 Payload 유형을 설명하고, 위성·지상망 연동에서 발생하는 주요 문제와 대응책을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 3차원 커버리지를 제공하는 SATIN·NTN 개요
> SATIN은 계층을 단순 연결하는 망이 아니라 각 Access의 지연·용량·가용성을 서비스 정책으로 전환하는 통합망임.

- 정의: **SATIN(Satellite-Aerial-Terrestrial Integrated Network)**은 **NTN(Non-Terrestrial Network)**과 **지상 이동통신망**을 통합하여 3차원 접속을 제공하는 아키텍처임
- 목적: 지리적 음영과 지상 인프라 단절 보완 → 서비스 연속성과 재난 복원력 확보

## Ⅱ. 투명·재생 Payload와 링크 구성
> Payload 처리 위치는 위성 복잡도와 지상 의존성을 교환하므로 서비스 지연·수명·업그레이드 가능성으로 선택해야 함.

| 축 | Transparent Payload | Regenerative Payload |
|---|---|---|
| 처리 | RF(Radio Frequency) 중계 | On-board 처리 |
| gNB(next Generation Node B) | 지상 | 위성 전체·일부 |
| 지연 | Gateway 경유 | 경로 단축 가능 |
| 대가 | Feeder 의존 | 위성 복잡도·전력 |

## Ⅲ. Doppler·지연·이동성 문제와 대책
> NTN의 핵심 난제는 긴 전파지연과 빠른 위성 이동이 지상망의 Timing·주파수·Mobility 가정을 깨뜨리는 데 있음.

| 문제 | 원인 | 대책 | 판정 |
|---|---|---|---|
| 동기 이탈 | 큰 Doppler | Ephemeris·주파수 사전 보상 | 잔류 주파수 오차 |
| 접속 실패 | 긴 RTT(Round-Trip Time) | Timing Advance 확장·Timer 조정 | Random Access 성공 |
| 빈번한 전환 | Moving Cell | 예측 Handover·Multi-connectivity | 단절·재전송 |
| Link 불안 | 강우·차폐 | Link Adaptation·다중 경로 | 가용성·지연 |

## 기술사적 제언

| 문제 | 해결 방안 |
|---|---|
| 빠른 위성 이동과 링크 품질 변화로 고정 경로의 지연·전환 품질이 흔들림 | 궤도 예측과 링크 상태를 반영해 경로를 선택하고, 강우·Gateway 장애·Beam 전환 시험으로 확인 |

## 출제 이력과 검증 출처
- 제128·130회: 원문 미확보(회차만 확인)
- [3GPP TS 23.501, System architecture for the 5G System](https://www.3gpp.org/dynareport/23501.htm)
- [3GPP TR 38.811, NR to support non-terrestrial networks](https://www.3gpp.org/dynareport/38811.htm)
- [ITU-R M.2160-0, IMT-2030 Framework](https://www.itu.int/rec/R-REC-M.2160-0-202311-I/en)
- [IEEE Access, Satellite-Aerial-Terrestrial Integrated Network for 6G](https://ieeexplore.ieee.org/document/9350208)

## 연결 토픽
- [NTN](./006_ntn/) · [6G 이동통신](./027_6g_mobile_communication/) · [5G-Advanced](./039_5g_advanced/)
