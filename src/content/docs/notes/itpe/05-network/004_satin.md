---
title: "위성·공중·지상 통합망(SATIN·NTN)"
author: "OpenAI Codex"
date: "2026-09-20T20:08:30+09:00"
tags: ["notes-network"]
sidebar: { badge: { text: "A" } }
extra: { keyword_grade: "A", model: "GPT-5.6 Sol" }
---
<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 20:08 KST</p>
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

## 예상문제
- SATIN과 NTN의 개념·구조·핵심 기술을 설명하고 지상망 연동 시 기술적 문제와 대책을 제시하시오.

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

## Ⅳ. 서비스 중심 통합 제어 결론
> 단일 Access 고정보다 서비스 SLA(Service Level Agreement)와 궤도 예측을 결합한 Multi-access 선택이 성능과 연속성을 함께 지킴.
### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 위성망의 넓은 Coverage는 지연·Doppler·용량 제약과 교환된다. 통합의 가치는 이를 숨기는 것이 아니라 예측 가능한 정책으로 노출하는 데 있다.
- `나라면`: 재난·해상 등 우선 서비스부터 지상망 Failover를 시험하고 Access별 품질을 측정해 확대하겠다.
### 실전 답안용 기술사적 제언
- 판정: 서비스별 지연·가용성·Handover 연속성 충족
- 대안: 궤도 예측과 Telemetry 기반 Multi-access Steering
- 검증: Gateway 장애·강우·Beam 전환 시나리오 시험
- 효과: 음영·단절 대응과 불필요한 위성 자원 사용 억제

<div class="itpe-flow itpe-flow--vertical" aria-label="SATIN 개선 제언"><div class="itpe-flow__node"><strong>Access 고정</strong><small><b>문제:</b> 환경 변화와 경로 품질 불일치</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>예측 Steering</strong><small><b>대안:</b> 궤도 · 품질 · 서비스 정책 결합</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>전환 시험</strong><small><b>판정:</b> 지연 · 가용성 · 연속성</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>통합 운용</strong><small><b>효과:</b> Coverage와 자원효율 균형</small></div></div>

## 1교시 10점 답안 발췌
- 정의: **SATIN(Satellite-Aerial-Terrestrial Integrated Network)**은 **NTN(Non-Terrestrial Network)**과 **지상망**을 통합하여 3차원 접속을 제공하는 아키텍처임
- 목적: 음영·재난 단절 보완 → 서비스 연속성 확보

<div class="itpe-flow itpe-flow--vertical" aria-label="SATIN 1교시 구조"><div class="itpe-flow__node"><strong>Space</strong><small><b>활동:</b> 광역 중계</small><small><b>산출:</b> Wide Coverage</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>Air</strong><small><b>활동:</b> 지역 보강</small><small><b>산출:</b> 임시 Coverage</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>Ground</strong><small><b>활동:</b> Core 연동</small><small><b>산출:</b> 서비스 연속성</small></div></div>

| 문제 | 대책 |
|---|---|
| Doppler·긴 RTT | 사전 보상·Timer 조정 |
| Moving Cell | 예측 Handover |
| Payload | Transparent: 지상 gNB·단순 위성 / Regenerative: 위성 처리·짧은 경로 |

- 결론: 궤도·품질·서비스 정책 기반 Steering을 장애 시나리오로 검증함

## 출제 이력과 검증 출처
- 제128·130회: 원문 미확보(회차만 확인)
- [3GPP TS 23.501, System architecture for the 5G System](https://www.3gpp.org/dynareport/23501.htm)
- [3GPP TR 38.811, NR to support non-terrestrial networks](https://www.3gpp.org/dynareport/38811.htm)
- [ITU-R M.2160-0, IMT-2030 Framework](https://www.itu.int/rec/R-REC-M.2160-0-202311-I/en)
- [IEEE Access, Satellite-Aerial-Terrestrial Integrated Network for 6G](https://ieeexplore.ieee.org/document/9350208)

## 학습 체크
- [ ] Ⅰ 개요: SATIN·NTN·지상망 관계와 목적을 재현할 수 있는가?
- [ ] 상단 그림: Space·Air·Ground의 역할과 산출을 연결할 수 있는가?
- [ ] Ⅱ 표: Transparent와 Regenerative Payload를 비교할 수 있는가?
- [ ] Ⅲ 표: Doppler·RTT·Moving Cell의 원인·대책·판정을 연결할 수 있는가?
- [ ] Ⅳ 제언: 문제·대안·판정·효과의 Steering 흐름을 재현할 수 있는가?

## 연결 토픽
- [NTN](./006_ntn/) · [6G 이동통신](./027_6g_mobile_communication/) · [5G-Advanced](./039_5g_advanced/)
