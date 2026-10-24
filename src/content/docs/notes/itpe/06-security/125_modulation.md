---
title: "데이터 변조(Modification)와 위조(Fabrication)"
author: "agnusdei1207"
date: "2026-10-24T23:07:38+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 데이터 변조(Modification), 데이터 위조(Fabrication), 무결성(Integrity), 진본성(Authenticity)
- 중간자 공격(MITM, Man-in-the-Middle), ARP 스푸핑(ARP Spoofing), DNS 포이즈닝(DNS Poisoning), 재전송 공격(Replay Attack)
- HMAC(Hash-based Message Authentication Code), 디지털 서명(Digital Signature), 상호 TLS(mTLS), 부인 방지(Non-repudiation)

## Ⅰ. 데이터 변조(Modification)와 위조(Fabrication)의 개요

- 핵심 요약 : 변조는 정상 데이터를 불법 수정하는 무결성 침해이고, 위조는 허위 주체와 데이터를 새로 만드는 진본성 침해.
- 개념 : **데이터 변조** (Modification)는 전송 중이거나 저장된 정상 데이터를 제3자가 수정·삭제·추가하는 무결성 침해이며, **데이터 위조** (Fabrication)는 허위 메시지나 자원을 정당한 송신자가 보낸 것처럼 만들어 주입하는 인증 및 진본성 침해.
- 배경 및 필요성 : 초기 인터넷 프로토콜인 IP(Internet Protocol), TCP(Transmission Control Protocol), ARP(Address Resolution Protocol), DNS(Domain Name System)는 상대방을 검증하는 암호학적 인증 없이 설계되어, 중간자 공격과 스푸핑, 세션 하이재킹이 일상적으로 나타남.
- 주요 목적 : 3대 보안 목표인 무결성, 인증, **부인 방지** (Non-repudiation)를 깨뜨리는 공격 메커니즘을 규명하고, 암호학적 수단으로 원본의 진본성을 보장하는 것.

## Ⅱ. 데이터 변조(Modification)와 위조(Fabrication)의 특징 및 장점

- 핵심 요약 : 두 공격은 대상 속성이 다르므로 방어 수단도 달라지며, 암호학적 키가 결합된 인증이 두 공격을 모두 막는 기반이 됨.

1. 변조의 특징 : 전송 패킷의 필드 값을 바꾸거나 데이터베이스 질의어 SQL(Structured Query Language)에 악성 구문을 넣는 **SQL 삽입** (SQL Injection)으로 수정 → 무결성이 깨져 잘못된 결제나 데이터 훼손이 발생함.
2. 위조의 특징 : 발신 IP나 MAC(Media Access Control) 주소를 도용해 ARP 응답(Reply)을 뿌리거나 허위 DNS 응답을 먼저 보냄 → 가짜 서버로 유도되어 진본성이 깨짐.
3. 키 기반 인증 : 단순 체크섬(CRC, Cyclic Redundancy Check)은 재계산이 가능해 방어가 어렵고, **HMAC** (Hash-based Message Authentication Code, 비밀키 기반 메시지 인증 코드)과 **디지털 서명** (Digital Signature)을 쓰면 위변조가 드러남.

## Ⅲ. 데이터 변조(Modification)와 위조(Fabrication)의 구조 (흐름)

- 핵심 요약 : 변조는 기존 메시지를 중간에서 바꾸는 흐름이고, 위조는 존재하지 않는 메시지를 주입하는 흐름이다.

```text
[ 변조 (Modification) ]

송신자 → 중간자 (Attacker) → 수신자
          가로채기 후 내용 변경
          "송금 100원" → "10만 원"
```

```text
[ 위조 (Fabrication) ]

공격자 (Spoofed IP)
   ↓ 허위 메시지 신규 발행
수신자 (속아서 처리)
   : 정상 송신자는 메시지를 보내지 않음
```

## Ⅳ. 데이터 변조와 위조의 비교 분석

- 핵심 요약 : 변조와 위조는 능동 공격으로 신뢰성을 훼손하고, 가로채기와 가로막기는 기밀성과 가용성을 노리는 공격으로 구분됨.

| 비교 항목 | 데이터 변조 (Modification) | 데이터 위조 (Fabrication) | 데이터 가로채기 (Interception) | 데이터 가로막기 (Interruption) |
| --- | --- | --- | --- | --- |
| 공격 성격 | 능동 공격 | 능동 공격 | 수동 공격 | 능동 공격 |
| 침해 속성 | 무결성 | 인증성, 진본성 | 기밀성 | 가용성 |
| 공격 행위 | 기존 데이터의 수정, 삽입, 순서 변경 | 허위 데이터와 가짜 신원 생성 | 도청, 패킷 스니핑, 불법 복제 | 네트워크 단절, 서비스 거부(DoS, Denial of Service), 파일 삭제 |
| 대표 사례 | 결제 파라미터 조작, 웹페이지 변조 | ARP 스푸핑, DNS 캐시 포이즈닝 | 무선 구간 패킷 도청 | 분산 서비스 거부(DDoS, Distributed Denial of Service), 랜섬웨어 암호화 |
| 핵심 방어책 | HMAC, 전자 서명, 무결성 검증 | 상호 TLS(mTLS, mutual TLS), DNSSEC(DNS Security Extensions), 802.1X 인증 | 엔드-투-엔드 암호화 (TLS, Transport Layer Security) | 이중화, DDoS 방어, 백업 복구 |

- 선택 기준 : 무결성이 문제이면 키 기반 무결성 검증을, 출처가 문제이면 상호 인증과 서명을 우선 적용한다.

## Ⅴ. 데이터 변조와 위조의 한계와 방안

- 핵심 요약 : 해시 재계산, 재전송, 개인키 노출이라는 세 가지 빈틈을 키 기반 무결성, 일회성 값, 하드웨어 키 보관으로 막아야 함.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 단순 해시의 재계산 변조 | 데이터와 해시를 함께 보내면 중간자가 새 해시를 만들어 변조 감지가 불가능 | 비밀키 기반 HMAC 또는 타원 곡선 전자 서명(ECDSA, Elliptic Curve Digital Signature Algorithm) 의무화 | 서명 검증 실패율 |
| 재전송 공격 | 정상 서명된 거래 요청을 녹음해 반복 전송하면 위조 효과가 발생 | 난수(Nonce), 타임스탬프, 증가 시퀀스 번호로 재사용 메시지 폐기 | 재전송 차단 건수 |
| 개인키 노출 | 엔드포인트 탈취로 개인키가 유출되면 합법적 서명으로 위조가 가능 | 개인키를 하드웨어 보안 모듈(HSM, Hardware Security Module)이나 TPM(Trusted Platform Module) 내부에 보관, 인증서 폐기 정보의 실시간 확인 | 키 노출 탐지 시간 |

## Ⅵ. 데이터 변조와 위조에 대한 기술사적 제언

- 핵심 요약 : 서비스 간 상호 인증, 인터넷 코어의 경로와 이름 검증, 감사 증적의 변조 탐지를 함께 설계하는 것이 변조와 위조를 구조적으로 차단하는 방향이다.
- 마이크로서비스 간 통신에는 클라이언트와 서버가 서로의 인증서를 검증하는 상호 TLS(mTLS)를 기본으로 적용하여, 내부망에서 주입되는 위조 패킷을 차단하는 것이 필요하다.
- DNS 캐시 포이즈닝을 막기 위해 DNSSEC 서명을 도입하고, BGP(Border Gateway Protocol) 하이재킹을 막기 위해 RPKI(Resource Public Key Infrastructure) 기반 경로 검증을 구축하는 것이 인터넷 코어 차원의 기본 방어가 된다.
- 설정 로그와 접근 기록, 전자 계약 데이터는 해시를 블록체인에 기록하는 방식으로 앵커링하여, 사후 변조 시도를 증명할 수 있게 하는 편이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : 변조와 위조는 데이터의 신뢰성을 근본적으로 흔드는 능동 공격이며, 키가 결합된 무결성 검증과 상호 인증이 핵심 방어 수단.
- 시사점 : 단순 해시만으로는 두 공격을 막을 수 없으므로, 인증과 무결성을 한 체계로 설계하는 것이 필요하다.
