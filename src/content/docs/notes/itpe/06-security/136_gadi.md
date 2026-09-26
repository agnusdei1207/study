---
title: "GADI(Global Architecture for Digital Identity)"
author: "Codex"
date: "2026-09-20T01:00:00+09:00"
tags: ["notes-security"]
extra:
  model: "GPT-6"
---

## 한 줄 본질
- GADI는 DID Alliance가 제안한 디지털 신원 상호운용 아키텍처. 제안된 구조와 실제 국제 표준 채택·서비스 운영 여부를 구분해야 함

## 10점 답안
GADI(Global Architecture for Digital Identity)는 서로 다른 신원 시스템 사이에서 신뢰할 수 있는 디지털 신원 확인을 지원하려는 DID Alliance의 아키텍처 제안. 신원 발급자, 이용자, 검증자 사이에 식별자와 신뢰 관계를 연결하는 구상. 기술적 검증 외에도 발급기관 신뢰, 자격증명 상태, 개인정보 보호, 관할국의 법적 인정이 필요. W3C DID·VC나 FIDO와 동일한 단일 표준 또는 전 세계 통용 신분증으로 설명하면 부정확.

## 25점 답안
### Ⅰ. 배경과 목표
서로 다른 사업자·국가의 신원 체계가 분리될 때 검증자가 발급자를 신뢰하고 자격증명을 해석하기 어려운 문제에 대응하는 상호운용 구상.

### Ⅱ. 참여자와 처리
```text
신원 확인 기관 → 자격증명 발급 → 이용자 지갑 보관
이용자 → 필요한 속성 제시 → 서비스 검증자
검증자 → 발급기관·서명·유효기간·철회 상태 및 신뢰 관계 확인
```
GADI의 제안 구조는 발급자와 검증자 사이의 신뢰 연결을 지향. FIDO는 이용자 인증 수단, W3C DID·VC는 식별자·자격증명 표현에 해당하며 역할 구분 필요.

### Ⅲ. 적용 쟁점
발급기관 거버넌스, DID 메서드 호환성, 자격증명 스키마, 철회 정보, 국외 이전과 최소 정보 공개. 암호학적 검증 성공만으로 여권·법적 신분 증명의 국제 상호인정 성립 불가.

## 출제 근거
- 제123회로 기재된 문항의 공식 원문은 현재 확보하지 못함. 회차·문구 미검증, 예상 학습 항목으로 분류

## 출처
- [ITU 주최 DID Alliance GADI 발표 자료](https://www.itu.int/en/ITU-T/webinars/20200521/Documents/Ramesh%20Kesanupalli_DID%20Alliance%20-%20Brief%20May%202020.pdf)
- [DID Alliance GADI 백서 공개 이력](https://www.didalliance.org/content.php?catcode=10121100)
