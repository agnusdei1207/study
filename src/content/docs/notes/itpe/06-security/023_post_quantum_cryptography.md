---
title: "양자내성암호(Post-Quantum Cryptography)"
author: "OpenAI"
date: "2026-09-24T22:07:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "GPT-6"
---

## 지식 로드맵 내 현재 위치

암호기술 → 공개키 암호 → 양자내성암호 전환

## 30초 인출

- **본질:** **양자내성암호(PQC, Post-Quantum Cryptography)** 는 양자컴퓨터를 포함한 공격을 고려해 설계된 암호 알고리즘
- **위협·대응:** 양자 알고리즘이 기존 공개키 암호를 위협하므로 표준 PQC를 목적별로 적용하고 시스템을 단계적으로 전환
- **전환 기준:** 장기 기밀성·암호 사용처·상호운용성·검증된 구현을 함께 확인

<details>
<summary>핵심 용어</summary>

- **PQC (Post-Quantum Cryptography):** 양자컴퓨터 공격을 고려해 설계한 암호 알고리즘
- **KEM (Key-Encapsulation Mechanism):** 공개 채널을 통해 공유 비밀키를 설정하는 알고리즘 집합
- **ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism):** NIST FIPS 203의 격자 기반 키 캡슐화 알고리즘
- **ML-DSA (Module-Lattice-Based Digital Signature Algorithm):** NIST FIPS 204의 격자 기반 전자서명 알고리즘
- **SLH-DSA (Stateless Hash-Based Digital Signature Algorithm):** NIST FIPS 205의 무상태 해시 기반 전자서명 알고리즘
- **HNDL (Harvest Now, Decrypt Later):** 현재 암호문을 수집해 보관한 뒤 미래의 해독 능력으로 복호화를 시도하는 위협 시나리오
- **QKD (Quantum Key Distribution):** 양자 통신을 이용해 키를 분배하는 기술로, 암호 알고리즘인 PQC와 적용 방식이 다른 기술
- **FIPS (Federal Information Processing Standards):** 미국 NIST가 공표하는 연방 정보처리 표준군
- **NIST (National Institute of Standards and Technology):** 미국 연방의 표준·기술기관
- **Shor 알고리즘:** 양자 푸리에 변환을 활용해 인수분해·이산로그 문제를 효율적으로 풀도록 설계된 양자 알고리즘
</details>

---
## 1교시 예상문제 (10점)

> 양자내성암호의 개념과 목적, 주요 표준의 용도를 설명하시오. *(10점 예상문제)*

---
## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **양자내성암호(PQC, Post-Quantum Cryptography)** 는 양자컴퓨터를 포함한 공격을 고려해 설계된 암호 알고리즘 |
| 목적 | 양자 알고리즘에 취약할 수 있는 기존 공개키 암호를 대체·보완해 장기 보안 유지 |

### Ⅱ. 표준과 역할

| 표준 | 알고리즘 | 용도 |
|---|---|---|
| FIPS 203 | ML-KEM | 공개 채널의 공유 비밀키 설정 |
| FIPS 204 | ML-DSA | 전자서명 생성·검증 |
| FIPS 205 | SLH-DSA | 해시 기반 전자서명 생성·검증 |

**제언:** 암호 사용처와 데이터 보호기간을 파악한 뒤 표준·검증 구현에 맞춰 전환계획 수립

---
## 2~4교시 예상문제 (25점)

> 양자컴퓨터가 공개키 암호에 미치는 위협과 양자내성암호의 표준·전환 방안을 설명하고, 양자키분배와 비교하시오. *(25점 예상문제)*

---
## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **양자내성암호(PQC, Post-Quantum Cryptography)** 는 양자컴퓨터를 포함한 공격을 고려해 설계된 암호 알고리즘 |
| 목적 | 양자 알고리즘에 취약할 수 있는 기존 공개키 암호를 대체·보완해 장기 보안 유지 |

양자내성은 양자컴퓨터 공격을 고려한 설계 목표이며, 모든 공격·구현 결함에 대한 무조건적 안전 보증은 아님.

## Ⅱ. 위협과 전환 필요성

| 위협·요인 | 보안 영향 | 관리 방향 |
|---|---|---|
| 대규모 양자컴퓨터에서의 Shor 알고리즘 | 인수분해·이산로그 기반 공개키 암호의 키 설정·서명 위협 | 장기 보호 데이터·암호 의존성 파악 |
| **HNDL** (Harvest Now, Decrypt Later) 시나리오 | 지금 수집한 암호문을 미래에 복호화할 수 있는 위험 | 데이터 민감도·보호기간에 따라 우선순위 결정 |
| 암호 의존성이 코드·장비에 고정 | 알고리즘 변경 시 서비스·상호운용 영향 | 암호 사용현황과 교체 경로 관리 |

## Ⅲ. 표준 알고리즘의 기능

| 표준 | 알고리즘·기반 | 주요 기능 |
|---|---|---|
| FIPS 203 | ML-KEM, 모듈 격자 기반 | 키 캡슐화·공유 비밀키 설정 |
| FIPS 204 | ML-DSA, 모듈 격자 기반 | 전자서명 |
| FIPS 205 | SLH-DSA, 무상태 해시 기반 | 전자서명 |

KEM은 대칭 암호에 쓸 공유키 설정에 활용되며, 그 자체가 메시지 암호화 알고리즘을 뜻하지 않음.

## Ⅳ. 양자내성암호와 양자키분배 비교

| 비교 | PQC | QKD |
|---|---|---|
| 방식 | 양자 공격을 고려한 수학적 암호 알고리즘 | 양자 통신을 이용한 키 분배 |
| 적용 기반 | 기존 컴퓨팅·통신 프로토콜에 알고리즘 통합 | 광통신 등 양자 키 분배 인프라와 운용 구성 |
| 전환 검토 | 제품·프로토콜 지원, 키·서명 크기, 성능·상호운용성 | 거리·망구성·장비·운영조건과 기존 암호체계 연계 |

## Ⅴ. 단계적 전환과 구현 검증

```text
암호 사용처·데이터 수명 조사
              ↓
위험·전환 우선순위 결정
              ↓
표준·검증 구현 및 프로토콜 선택
              ↓
호환성·성능·보안 시험
              ↓
단계 배포·구현 갱신·잔여위험 점검
```

| 검증 항목 | 확인 내용 |
|---|---|
| 암호 민첩성 | 알고리즘 교체·인증서·키 갱신 경로 |
| 성능·호환성 | 실제 프로토콜·장비 조합의 크기·지연·상호운용성 |
| 구현 신뢰성 | 현행 표준·오류정정·검증된 라이브러리 및 구현 상태 |
| 병행 구성 | 하이브리드 적용 시 표준 지침·프로토콜 협상·장애 동작 |

## Ⅵ. 한계와 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 표준 채택만으로 기존 시스템의 암호 의존성과 취약 구현이 자동 교체되지 않음 | 자산·통신경로별 전환책임과 시험 기준을 두고 우선순위에 따라 교체·검증 |
| 구현·프로토콜 지원이 달라 일괄 전환 시 호환·성능 위험 | 검증된 구현과 대상별 호환성 시험을 거친 뒤 단계 배포, 관련 NIST 정오표·지침 재확인 |

---
## 검증 출처

- NIST, [FIPS 203: ML-KEM](https://csrc.nist.gov/pubs/fips/203/final) — NIST publication page includes potential update/errata notice
- NIST, [FIPS 204: ML-DSA](https://csrc.nist.gov/pubs/fips/204/final)
- NIST, [FIPS 205: SLH-DSA](https://csrc.nist.gov/pubs/fips/205/final)
- NIST, [SP 800-227: Recommendations for Key-Encapsulation Mechanisms](https://csrc.nist.gov/pubs/sp/800/227/final)
- NIST, [Post-Quantum Cryptography publications](https://csrc.nist.gov/Projects/post-quantum-cryptography/publications)
- NIST, [IR 8105: Report on Post-Quantum Cryptography](https://csrc.nist.gov/pubs/ir/8105/final)

## 연결 토픽

- [양자암호통신](./058_quantum_cryptography_communication/)
