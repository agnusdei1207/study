---
title: "양자내성암호(Post-Quantum Cryptography)"
author: "agnusdei1207"
date: "2026-10-24T22:59:28+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "023"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 양자내성암호(PQC, Post-Quantum Cryptography), 쇼어 알고리즘(Shor), RSA, ECC
- HNDL(Harvest Now, Decrypt Later), 패킷 단편화(Fragmentation)
- ML-KEM, ML-DSA, SLH-DSA, FN-DSA(FALCON), FIPS 203·204·205
- 하이브리드 전환(Hybrid Migration), 부채널 공격(Side-Channel Attack), 상수 시간 연산(Constant-Time)
- 마스킹(Masking), 셔플링(Shuffling), 크립토 애자일리티(Crypto-Agility), CBOM

## Ⅰ. 양자내성암호(Post-Quantum Cryptography)의 개요

- 핵심 요약 : 양자 컴퓨터로도 풀기 어려운 수학 난제에 기반해 공개키 암호를 바꾸려는 차세대 암호 체계.
- 개념 : 쇼어 알고리즘을 구동하는 양자 컴퓨터로도 다항식 시간 안에 풀 수 없는 것으로 알려진 수학적 난제(격자, 다변수, 해시, 부호 기반)에 기반해 설계된 차세대 공개키 암호 체계, 즉 **양자내성암호** (PQC, Post-Quantum Cryptography).
- 배경 및 필요성 : 양자 컴퓨터가 실용화되면 인터넷 보안의 근간인 RSA(소인수분해 기반)와 ECC(Elliptic Curve Cryptography, 타원곡선 기반)가 무력화되며, 공격자가 지금 암호화된 트래픽을 미리 수집해 두었다가 나중에 복호화하는 **Harvest Now, Decrypt Later** (HNDL) 위협에 대비할 필요가 있음.
- 주요 목적 : 양자 컴퓨팅 시대에도 기밀성과 전자서명 무결성을 지키고, 기존 인프라를 전면 교체하지 않고 소프트웨어 수준에서 암호 안전성을 유지하는 것.

## Ⅱ. 양자내성암호(Post-Quantum Cryptography)의 특징 및 장점

- 핵심 요약 : 서로 다른 수학 난제를 기반으로 한 표준 알고리즘군이 양자 위협에 대한 선택지를 넓히는 구조.

1. **ML-KEM** (Module-Lattice-Based Key-Encapsulation Mechanism, FIPS 203) : 모듈 격자 난제 기반의 키 캡슐화 방식 → 고속 연산과 상대적으로 작은 키 크기 제공.
2. **ML-DSA** (Module-Lattice-Based Digital Signature Algorithm, FIPS 204) : 격자 기반 전자서명 → 검증 속도가 빨라 범용 서명 표준으로 쓰기 적합.
3. **SLH-DSA** (Stateless Hash-Based Digital Signature Algorithm, FIPS 205) : 해시 함수의 안전성만 가정하는 서명 방식 → 격자 수학이 깨질 경우의 백업 선택지.
4. FN-DSA(FALCON) : 격자 기반으로 서명 크기를 줄이는 방식으로, 표준화가 진행 중이며 서명 크기 제약이 큰 환경의 후보.

## Ⅲ. 양자내성암호(Post-Quantum Cryptography)의 구조 (흐름)

- 핵심 요약 : NIST 공식 표준이 난제 계층별로 나뉘고, 전환기에는 고전 암호와 결합되는 흐름.
- NIST(National Institute of Standards and Technology)는 공개 경쟁 방식의 표준화 과정을 거쳐 2024년 FIPS 203, 204, 205를 최초의 PQC 공식 표준으로 발표함.

```text
[ NIST 공식 PQC 표준 (2024) ]

격자 기반 (Lattice)
  ML-KEM (FIPS 203) 키 캡슐화
  ML-DSA (FIPS 204) 전자서명
        ↓ 격자 수학 붕괴 시 대비
해시 기반 (Hash)
  SLH-DSA (FIPS 205) 전자서명
```

```text
[ 하이브리드 전환 구조 ]

고전 암호 (X25519, ECDSA)
        +
양자내성암호 (ML-KEM, ML-DSA)
        ↓
두 방식을 결합한 키·서명 생성
        ↓
한쪽이 깨져도 나머지가 안전성 유지
```

## Ⅳ. 양자내성암호(Post-Quantum Cryptography)와 고전 암호의 비교

- 핵심 요약 : PQC는 양자 안전성을 얻는 대신 공개키와 서명, 암호문 크기가 커지는 트레이드오프를 가짐.

| 비교 항목 | RSA-2048 | ECDH / ECDSA (P-256) | ML-KEM-768 | ML-DSA-65 |
| --- | --- | --- | --- | --- |
| 기반 난제 | 소인수분해 | 타원곡선 이산대수 | 모듈 격자 난제 (MLWE, Module Learning With Errors) | 모듈 격자 난제 (MLWE) |
| 양자 안전성 | 취약 (Shor 알고리즘에 붕괴) | 취약 (Shor 알고리즘에 붕괴) | 안전 (NIST 보안 레벨 3) | 안전 (NIST 보안 레벨 3) |
| 공개키 크기 | 256바이트 | 64바이트 | 1,184바이트 | 1,952바이트 |
| 암호문·서명 크기 | 256바이트 | 64바이트 | 1,088바이트 (암호문) | 3,309바이트 (서명) |
| 연산 속도 | 보통 | 빠름 | 고속 | 검증 속도 우수 |

- PQC는 공개키와 서명, 암호문이 커지므로 **패킷 단편화** (Fragmentation)를 고려해 프로토콜 설계를 다시 점검해야 함.

## Ⅴ. 양자내성암호(Post-Quantum Cryptography)의 한계와 방안

- 핵심 요약 : 패킷 크기 증가, 구현 측면 부채널 노출, 검증 기간 부족을 프로토콜 최적화, 구현 방어, 하이브리드 전환으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 패킷 단편화 | TLS(Transport Layer Security) 1.3 핸드셰이크에서 PQC 키와 서명이 최대 전송 단위(MTU, Maximum Transmission Unit) 1,500바이트를 넘어 TCP(Transmission Control Protocol) 단편화와 지연 발생 | 압축 기법 적용, 키 캡슐화 중심의 핸드셰이크 최적화, 서명 크기가 작은 FN-DSA(FALCON) 표준화 후 채택 검토 | 핸드셰이크 지연 시간, 단편화 발생률 |
| **부채널 공격** (Side-Channel Attack) | 가우스 샘플링이나 다항식 곱셈 구현에서 실행 시간과 전력 패턴으로 비밀키 누출 | **상수 시간 연산** (Constant-Time) 구현 표준화, **마스킹** (Masking)과 **셔플링** (Shuffling)을 암호 라이브러리에 내재화 | 부채널 시험 통과율 |
| 표준 직후 검증 기간 부족 | 수십 년간 검증된 RSA와 달리 격자 암호는 비교적 새로운 수학 체계라 향후 취약점 발견 우려 | **하이브리드 전환** (Hybrid Migration)으로 고전 암호와 PQC를 함께 적용해 단일 알고리즘 결함 위험 분산 | 하이브리드 적용 비율 |

## Ⅵ. 양자내성암호(Post-Quantum Cryptography)에 대한 기술사적 제언

- 핵심 요약 : 암호 민첩성 확보, 암호 자산 식별, 국가 전환 로드맵 연계를 PQC 전환의 기본 방향으로 제시.

1. **크립토 애자일리티** (Crypto-Agility) 확보 : 특정 알고리즘을 코드에 고정하지 않고 설정과 라이브러리 교체로 암호 체계를 바꿀 수 있도록 설계 단계부터 반영하는 것이 바람직하다.
2. 암호 자산 식별 : **CBOM** (Cryptographic Bill of Materials, 암호 자산 목록) 기준으로 시스템, 데이터베이스, 인증서에 쓰인 고전 암호 현황을 파악해 전환 준비도를 평가하는 것이 필요하다.
3. 국가 로드맵 연계 : 국가정보원과 한국인터넷진흥원(KISA, Korea Internet & Security Agency)이 제시하는 국가 PQC 전환 로드맵에 맞춰 전자서명, VPN(Virtual Private Network), 웹 인증서부터 단계적으로 전환하는 계획을 세우는 것이 좋다.

## Ⅶ. 결론

- 핵심 요약 : 양자내성암호는 양자 컴퓨터 등장 이후에도 공개키 기반 신뢰를 유지하기 위한 암호 체계 전환의 출발점.
- 시사점 : 암호 전환은 알고리즘 교체만으로 끝나지 않으므로, 자산 식별과 설계, 하이브리드 전환을 장기 과제로 관리해야 한다.
