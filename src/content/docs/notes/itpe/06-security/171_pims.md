---
title: "PIMS(Personal Information Management System)"
author: "Codex"
date: "2026-10-08T15:46:11+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GPT-6"
---

## Ⅰ. PIMS의 개요

- **PIMS**(Personal Information Management System)는 국내에서 개인정보보호 관리체계를 평가하던 인증제도의 명칭. 정보보호 관리체계(ISMS, Information Security Management System)와 통합되어 2018년 정보보호 및 개인정보보호 관리체계(ISMS-P, Information Security and Personal Information Management System)로 발전.
- 목적 : 수집·보유·이용·제공·파기에 걸친 보호 활동과 조직의 위험관리 체계를 함께 평가.
- 명칭 구분 : 국제표준 ISO/IEC 27701의 PIMS는 Privacy Information Management System을 뜻하며 국내 구 PIMS의 영문명과 다름.

## Ⅱ. 현행 통합 인증기준과 심사

| 영역 | 일반 인증기준 수 | 주된 내용 |
|---|---|---|
| 관리체계 수립·운영 | 16 | 책임, 범위, 위험관리, 운영 및 개선 |
| 보호대책 요구사항 | 64 | 접근 통제, 암호화, 운영·개발 보안, 사고 대응 |
| 개인정보 처리단계별 요구사항 | 21 | 수집·이용·제공·파기 및 정보주체 권리 |

- 일반 ISMS-P는 총 101개 인증기준. 간편인증 등은 별도 대상·기준을 확인하여 일반 인증과 구분.
- 인증 유효기간은 3년이며 유효기간 중 정기 사후심사 수행. 매년 신규 인증을 취득해야 한다는 의미가 아님.

## Ⅲ. 의무 적용과 국제표준의 구분

- **ISMS 의무 대상** : 정보통신망법에 따른 사업자 유형·매출·이용자 규모 등 적용 요건 확인. 모든 병원·대학교가 무조건 대상인 것은 아님.
- **ISMS-P 의무화** : 2026년 개정 개인정보 보호법이 정한 주요 개인정보처리자 대상 의무화 규정은 2027년 7월 1일 시행 예정. 2026년 10월 현재의 적용 의무와 미래 시행 규정 구분.
- **ISO/IEC 27701:2025** : 독립적인 개인정보 관리체계 표준. 2019판의 ISO/IEC 27001 확장 구조를 현행판에 그대로 적용하지 않도록 구분.
- 국내 인증과 국제 인증은 범위·기준·심사 절차가 달라 자동 상호 인정이나 모든 개인정보 법규 준수를 보장하지 않음.
- 참고 : [개인정보 포털의 인증기준](https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=59), [KISA 인증 절차](https://isms.kisa.or.kr/cert/aply/selectCertPrcdDetail.do), [개인정보위의 2026년 개정 안내](https://m.korea.kr/news/policyNewsView.do?newsId=148960564), [ISO/IEC 27701:2025](https://www.iso.org/standard/27701).

## Ⅳ. 개인정보 관리체계의 한계점 및 해결 방안

- 문서와 운영의 괴리 : 통제 이행 기록과 실제 설정·권한·로그를 대조하여 효과 검증.
- 클라우드 책임 범위의 혼동 : 제공자 인증 범위와 이용자 책임을 구분하고 위탁·국외 이전·접근 통제를 별도로 확인.
- 개인정보 흐름의 변화 : 서비스·모델·외부 연계 변경 시 인증 범위와 위험평가 갱신.

## Ⅴ. 개인정보 관리체계 운영을 위한 제언

- 인증 심사 기간에 집중하는 방식에서 벗어나 자산·처리 흐름·권한·사고 대응을 상시 관리.
- 개인정보보호책임자의 보고·예산·전문 인력 관리 역할을 실제 업무 절차와 연결하고 적용 법령의 규모 요건·시행일 확인.
