---
title: "해시 함수(Hash Function)"
author: "Antigravity"
date: "2026-09-28T23:41:48+09:00"
tags:
  - "notes-security"
sidebar:
  label: "010. 해시 함수(Hash Function)"
  badge:
    text: "기초"
    variant: note
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

정보보안 → 암호학 → 일방향 암호학적 해시 함수 및 메시지 무결성

## 30초 인출

- **본질:** 가변 길이의 임의 메시지를 고정 길이의 고유 다이제스트(Digest)로 변환하는 일방향 암호학적 함수
- **메커니즘:** Merkle-Damgard(압축 함수 반복) 및 Sponge(흡수·착유) 구조를 통해 제1역상, 제2역상, 충돌 저항성을 보장
- 통찰: 머클-담고르 구조의 길이 확장 공격과 GPU 기반 고속 무차별 대입을 방어하기 위해 HMAC 결합 및 메모리 집약적 Argon2id 패스워드 KDF 도입 필수

<details>
<summary>핵심 용어</summary>

- **제1역상 저항성(Preimage Resistance):** 주어진 해시값 $h$에 대해 $H(M) = h$를 만족하는 원래의 메시지 $M$을 찾는 것이 계산적으로 불가능한 성질
- **제2역상 저항성(Second Preimage Resistance):** 주어진 특정 메시지 $M$에 대해 $H(M) = H(M')$을 만족하는 다른 메시지 $M' \neq M$을 찾는 것이 계산적으로 불가능한 성질
- **충돌 저항성(Collision Resistance):** $H(M) = H(M')$을 만족하는 임의의 서로 다른 두 메시지 쌍 $(M, M')$을 찾는 것이 계산적으로 불가능한 성질 (생일 역설에 의해 $2^{n/2}$ 복잡도)
- **길이 확장 공격(Length Extension Attack):** $H(M)$과 $M$의 길이를 알고 있을 때, 비밀 값 $M$을 몰라도 $H(M \parallel \text{padding} \parallel M')$을 계산해낼 수 있는 머클-담고르 구조의 구조적 취약점
</details>

---
## 2~4교시 예상문제 (25점)

> 암호학적 해시 함수의 3대 보안 요구조건을 수식과 함께 설명하고, Merkle-Damgard 구조와 Sponge 구조의 내부 메커니즘을 비교하며, 길이 확장 공격 및 패스워드 크래킹에 대응하기 위한 엔지니어링 방안을 기술하시오. (예상·25점)

---
## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **암호학적 해시 함수(Cryptographic Hash Function)** 는 임의의 길이를 갖는 입력 데이터를 고정된 비트 크기의 고유한 출력값(다이제스트)으로 단방향 매핑하는 암호 알고리즘 |
| 목적 | 데이터 전송 및 저장 시 위변조 방지(무결성), 전자서명의 효율화, HMAC 메시지 인증, 블록체인 작업증명(PoW) 및 패스워드 안전 저장 지원 |

단순 체크섬(CRC)과 달리 역산이 불가능하고 충돌을 찾기 어려워 암호학적 안전성을 보장.

## Ⅱ. 암호학적 해시 함수의 3대 보안 특성

| 보안 특성 | 수학적 정의 | 공격자의 목표 | 안전성 강도 기준 ($n$비트 출력) |
|---|---|---|---|
| **제1역상 저항성**<br>(Preimage Resistance) | 주어진 $h$에 대해<br>$H(M) = h$인 $M$ 탐색 불가능 | 다이제스트 $h$로부터 원본 평문 $M$을 복원 | $2^n$ 전수 조사 복잡도 |
| **제2역상 저항성**<br>(2nd Preimage Resistance) | 주어진 $M$에 대해<br>$H(M') = H(M)$인 $M' \neq M$ 탐색 불가능 | 특정 정상 문서 $M$과 동일한 해시를 갖는 악성 위조 문서 $M'$ 생성 | $2^n$ 전수 조사 복잡도 |
| **충돌 저항성**<br>(Collision Resistance) | $H(M) = H(M')$인<br>임의의 서로 다른 쌍 $(M, M')$ 탐색 불가능 | 동일한 해시값을 출력하는 임의의 두 입력 쌍을 사전 탐색 | 생일 역설(Birthday Attack)로 인해 $2^{n/2}$ 복잡도 |

추가적으로 입력 비트가 단 1비트만 변경되어도 출력 비트의 약 50%가 무작위로 변경되는 **눈사태 효과(Avalanche Effect)** 가 필수 충족 요건임.

## Ⅲ. 해시 함수의 아키텍처 및 내부 구조

```text
[Merkle-Damgard 구조 vs Sponge 구조 비교]

1. Merkle-Damgard 구조 (MD5, SHA-1, SHA-2)
   메시지 분할: M1, M2, ..., Mk (각 b비트 블록)
   
     IV -> [압축함수 f] -> [압축함수 f] -> ... -> [압축함수 f] -> 최종 Digest
              ^                  ^                     ^
              |                  |                     |
              M1                 M2                    Mk (Padding 포함)

2. Sponge 구조 (SHA-3 Keccak)
       [  흡수 단계 (Absorbing)  ]          [  착유 단계 (Squeezing)  ]
   M1 -> (+) -> [ f (순열) ] -> (+) -> [ f ] ----> Z1 (출력 다이제스트)
          |                      |                   |
          v                      v                   v
     [비트 상태: Rate (r) + Capacity (c)]       [ f ] ----> Z2
```

### 1. 두 구조의 엔지니어링 메커니즘 상세

| 구조 | 내부 동작 프로세스 | 보안 설계 특징 |
|---|---|---|
| **Merkle-Damgard** | 1. 패딩 및 길이 추가 (MD-Strengthening)<br>2. 고정 크기 블록 분할 후 압축 함수 $f$ 순차 연산<br>3. 이전 압축 출력을 다음 블록의 체이닝 변수로 주입 | 압축 함수가 충돌에 안전하면 전체 해시 함수도 안전함이 수학적으로 증명됨. 단, 내부 상태가 외부에 노출되어 길이 확장 공격에 노출됨. |
| **Sponge** | 1. 내부 상태를 Rate($r$)와 Capacity($c$)로 분할<br>2. 흡수(Absorbing): 입력 블록을 $r$과 XOR 후 순열 $f$ 수행<br>3. 착유(Squeezing): $r$ 부분에서 원하는 길이만큼 출력 추출 | 내부 상태 $c$가 외부에 노출되지 않으므로 길이 확장 공격을 원천적으로 차단하며 가변 길이 출력 지원 |

## Ⅳ. 주요 해시 알고리즘 비교

| 비교 항목 | MD5 / SHA-1 | SHA-2 (SHA-256/512) | SHA-3 (Keccak) | BLAKE3 |
|---|---|---|---|---|
| **출시 연도** | 1992 / 1995 | 2001 | 2015 | 2020 |
| **기본 구조** | Merkle-Damgard | Merkle-Damgard | Sponge Construction | Bao 트리 (Merkle Tree 기반) |
| **출력 비트** | 128 / 160 비트 | 224, 256, 384, 512 비트 | 224, 256, 384, 512 비트 | 256 비트 (가변 지원) |
| **보안 안전성** | 충돌 공격 성공 (사용 금지) | 현재 표준 안전성 유지 | 고도 안전성 (대체 구조) | 최신 암호학적 안전성 |
| **연산 속도** | 빠름 | 보통 | 하드웨어 우수, SW 보통 | 극도로 빠름 (SIMD 병렬화) |
| **길이 확장 공격** | 취약 | 취약 (HMAC 결합 필수) | 안전 (구조적 면역) | 안전 (트리 구조) |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| **Merkle-Damgard의 길이 확장 공격(Length Extension Attack)**<br>$H(M)$의 상태가 최종 압축 함수의 출력이므로, 비밀키가 포함된 $H(\text{Key} \parallel \text{Data})$ 형태의 MAC 구성 시 키를 몰라도 뒤에 임의 데이터를 덧붙인 유효한 해시 $H(\text{Key} \parallel \text{Data} \parallel \text{Padding} \parallel \text{Extra})$를 공격자가 위조 가능 | **HMAC(Keyed-Hash MAC) 또는 Sponge/BLAKE3 구조 도입**<br>이중 해시 구조인 $\text{HMAC}(K, M) = H((K \oplus \text{opad}) \parallel H((K \oplus \text{ipad}) \parallel M))$를 적용하여 내부 체이닝 상태의 외부 직접 노출을 완벽 차단하거나, 구조적으로 면역인 SHA-3 및 BLAKE3 전환 |
| **GPU/ASIC 고속 연산에 의한 패스워드 크래킹 및 무차별 대입**<br>SHA-256 등 범용 고속 해시는 초당 수십억 번 계산이 가능하여 무차별 대입(Brute-force) 및 레인보우 테이블(Rainbow Table) 공격에 취약 | **메모리 집약적 Password KDF(Argon2id, scrypt) 적용**<br>단순 솔트(Salt) 추가를 넘어, 메모리 버퍼를 강제로 소모하게 설계된 메모리 하드(Memory-hard) KDF인 Argon2id를 적용하여 병렬 ASIC 가속 하드웨어 연산을 무력화 |

## Ⅵ. 제언

```text
[용도별 해시 알고리즘 아키텍처 선택 가이드]

                      [목적별 알고리즘 분류]
                                |
        +-----------------------+-----------------------+
        |                                               |
 [무결성 및 전자서명]                            [비밀번호 안전 저장]
        |                                               |
  SHA-256 / SHA-3                                Argon2id / PBKDF2
 (대량 데이터는 BLAKE3)                         (솔트 결합 + 비용 조정)
```

| 적용 업무 분야 | 권장 알고리즘 | 적용 기준 및 통제 사항 |
|---|---|---|
| **메시지 무결성 및 전자서명** | SHA-256, SHA-384, SHA-3 | 공인인증서, TLS 통신 서명 시 SHA-1 전면 금지 및 256비트 이상 사용 |
| **API 메시지 인증** | HMAC-SHA256, HMAC-SHA512 | 단순 해시 연결 대신 반드시 표준 RFC 2104 HMAC 체계 준수 |
| **사용자 패스워드 저장** | Argon2id (권장), PBKDF2 | 사용자별 최소 16바이트 솔트 생성 및 메모리 64MB, 반복 3회 이상 구성 |

---
## 출제 이력과 검증 출처

- 정보관리기술사 115회, 122회, 129회 암호학적 해시함수 및 충돌 저항성
- NIST FIPS 180-4 Secure Hash Standard (SHS)
- NIST FIPS 202 SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions
- RFC 2104 HMAC: Keyed-Hashing for Message Authentication

## 연결 토픽

- [디지털 포렌식](./006_digital_forensics/)
- [SBOM](./004_sbom/)
