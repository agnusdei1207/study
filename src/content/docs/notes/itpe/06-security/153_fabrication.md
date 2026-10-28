---
title: "위조(Fabrication) 공격"
author: "agnusdei1207"
date: "2026-10-24T23:11:12+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  question_no: "153"
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 위조(Fabrication) 공격, 스푸핑(Spoofing), 진본성(Authenticity), 능동적 공격(Active Attack)
- ARP 스푸핑, DNS 포이즈닝, 반사 증폭 공격, 딥페이크(Deepfake)
- uRPF, DNSSEC, SPF·DKIM·DMARC, mTLS, HSM

## Ⅰ. 위조(Fabrication) 공격의 개요

- 핵심 요약 : 허위 신원과 데이터를 새로 만들어 주입해 진본성을 무너뜨리는 능동적 공격.
- 개념 : 공격자가 시스템에 없던 거짓 정보, 허위 패킷, 조작된 자격증명, 사칭된 발신자를 새로 생성해 주입하는 **능동적 공격** (Active Attack)으로, 데이터의 **진본성** (Authenticity, 주장한 발신자가 실제 발신자인지에 대한 속성)을 훼손하는 정보보호 침해 행위.
- 배경 및 필요성 : ARP(Address Resolution Protocol), IP(Internet Protocol), DNS(Domain Name System), SMTP(Simple Mail Transfer Protocol) 등 초기 인터넷 프로토콜은 발신지를 검증하는 인증 기능이 없이 설계되어, 공격자가 발신자를 바꾸는 **스푸핑** (Spoofing)으로 쉽게 신원을 위조할 수 있다. 이 구조적 빈틈에서 발생하는 피해를 막기 위해 발신자 검증 체계가 필요하다.
- 주요 목적 : 정당한 사용자나 서버로 위장해 보안 통제를 우회하고, 트래픽을 가로채거나 허위 요청으로 자원을 고갈시켜 서비스를 마비시키는 것.

## Ⅱ. 위조(Fabrication) 공격의 특징 및 장점

- 핵심 요약 : 발신자 검증이 없는 프로토콜 구조를 이용해 허위 신원을 만들고, 그 신원으로 다른 공격을 연쇄시키는 특징.

1. 신원 사칭 : IP 스푸핑, MAC(Media Access Control) 스푸핑, 이메일 헤더 위조로 정당한 발신인을 가장 → 공격자가 시스템 접근 권한을 획득.
2. 인증서·토큰 위조 : 탈취한 서명 키로 X.509 인증서를 발행하거나 JWT(JSON Web Token) 서명을 위조 → 관리자 세션 사칭으로 권한 상승.
3. 반사·증폭 공격의 도구화 : 출발지 IP를 피해자 주소로 위조한 뒤 DNS, NTP(Network Time Protocol) 서버에 질의 → 응답 트래픽이 피해자에게 집중되는 DDoS(Distributed Denial of Service) 효과.
4. AI 생성형 위조 : 음성 복제와 얼굴 합성으로 경영진을 실시간 가장 → 고액 송금을 요구하는 사회공학 사기로 이어짐.

## Ⅲ. 위조(Fabrication) 공격의 구조 (흐름)

- 핵심 요약 : 공격은 데이터링크, 네트워크, 애플리케이션 계층에 걸쳐 나타나며, 방어는 같은 계층마다 암호학적 검증을 대응시키는 구조.

```text
[ 계층별 위조 공격 경로 ]

L2(Layer 2) 데이터링크 계층
  ARP 스푸핑 : 가짜 ARP 응답으로
               피해자 ARP 캐시 오염
          ↓
L3 네트워크 계층
  IP 스푸핑 : 출발지 IP 위조 후
              반사 DDoS 수행
          ↓
L7(Layer 7) 애플리케이션 계층
  DNS 포이즈닝 : 가짜 사이트 유도
  이메일 위조 : 경영진 사칭 송금 사기
  딥페이크 : 경영진 음성·영상 위조
```

- **uRPF** (Unicast Reverse Path Forwarding) : 출발지 IP가 실제 역방향 경로와 맞는지 확인해 위조 패킷을 버리는 라우터 기능.
- **SPF** (Sender Policy Framework), **DKIM** (DomainKeys Identified Mail), **DMARC** (Domain-based Message Authentication, Reporting and Conformance) : 발신 서버 IP 검증, 메일 전자서명, 검증 실패 정책을 묶은 이메일 위조 방지 표준.

```text
[ 계층별 위조 방어 대응 ]

L2 : 802.1X 포트 인증, ARP 검사
          ↓
L3 : IPsec 암호화, uRPF 역경로 검증
          ↓
L7 : DNSSEC(DNS Security Extensions) 서명
     SPF·DKIM·DMARC 메일 인증
```

## Ⅳ. 위조와 인접 침해 유형의 비교

- 핵심 요약 : 위조는 허위 데이터를 새로 만들어 진본성을 해치는 점에서, 변조·가로채기·가로막기와 침해 속성이 구분됨.

| 비교 항목 | 위조 (Fabrication) | 변조 (Modification) | 가로채기 (Interception) | 가로막기 (Interruption) |
| --- | --- | --- | --- | --- |
| 행위 본질 | 허위 메시지와 신원을 새로 생성해 주입 | 정상 메시지의 내용을 수정하거나 삭제 | 정상 트래픽을 몰래 엿봄 (도청) | 통신 회선이나 자원을 파괴해 차단 |
| 침해 속성 | 진본성, 무결성 | 무결성 | 기밀성 | 가용성 |
| 주요 사례 | ARP 스푸핑, 가짜 송장 발송, 딥페이크 | 결제 파라미터 변조, DB 데이터 변경 | 패킷 스니핑, 트래픽 도청 | DDoS 트래픽 공격, 파일 파괴형 랜섬웨어 |
| 대응 기술 | 상호 인증, 전자서명, DNSSEC | 무결성 해시, 전자서명 | 종단간 암호화(TLS, Transport Layer Security), VPN(Virtual Private Network) | 이중화 인프라, DDoS 방어 장비 |

- 선택 기준 : 공격이 새 데이터를 만드는지, 기존 데이터를 바꾸는지, 훔쳐보는지, 멈추게 하는지에 따라 대응 속성을 나눔.

## Ⅴ. 위조(Fabrication) 공격의 한계와 방안

- 핵심 요약 : 발신지 검증 부재, 탈취된 서명 키, 딥페이크 기반 사기를 경계 필터링, 키 격리, 다중 승인으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 발신지 검증 부재 | UDP는 핸드셰이크가 없어 라우터가 출발지 IP를 검증하지 않고 중계 | 경계 라우터의 uRPF 필터링 적용 | 위조 출발지 IP 차단 건수 |
| 탈취된 인증서·개인키 악용 | 사설 CA(Certificate Authority)나 코드 서명 키가 탈취되면 악성코드가 정상 서명으로 신뢰됨 | 개인키를 HSM(Hardware Security Module)에 격리, CT(Certificate Transparency) 로그로 이상 발급 탐지 | 이상 발급 탐지 건수 |
| 딥페이크 기반 사회공학 | 실시간 영상 통화에서 직원의 육안 판단이 위조를 구별하지 못함 | 멀티모달 포렌식 탐지 도입, 자금 이체 시 다중 승인 강제 | 다중 승인 우회 시도 건수 |

## Ⅵ. 위조(Fabrication) 공격에 대한 기술사적 제언

- 핵심 요약 : 이름 해석과 라우팅, 메일, 세션 신뢰 체계를 암호학적 검증으로 바꾸고, 사람이 개입하는 송금 절차까지 포함해 진본성 검증을 상시 체계로 정착.

1. 네트워크 조직은 DNSSEC을 전사 도메인에 적용하고, BGP(Border Gateway Protocol) 경로 정보의 출처를 RPKI(Resource Public Key Infrastructure)로 검증하는 방향으로 인프라를 정비하는 것이 바람직하다.
2. 정보보안 조직은 SPF, DKIM, DMARC를 검증 실패 메일을 격리하거나 거부하는 정책까지 단계적으로 올려, 사내 도메인을 사칭하는 메일이 수신 단계에서 차단되도록 해야 한다.
3. 인증 체계 조직은 네트워크 위치를 신뢰하지 않고 모든 세션에서 상호 인증(mTLS, Mutual TLS)과 단기 토큰 검증을 수행하는 제로 트러스트 구조로 전환해야 한다.
4. 경영진과 재무 조직은 고액 송금 승인에 기술 탐지만 의존하지 않고, 별도 채널을 통한 본인 확인과 다중 승인을 의무화하는 업무 절차를 함께 설계해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 위조 공격은 발신자 검증의 빈틈을 이용해 허위 신원과 데이터를 만들어 내는 능동적 공격.
- 시사점 : 진본성을 암호학적으로 확인하는 체계와 사람이 개입하는 절차가 결합되어야 위조 공격의 피해가 줄어든다.
