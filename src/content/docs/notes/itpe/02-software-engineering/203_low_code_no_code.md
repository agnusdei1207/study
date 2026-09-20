---
title: "로우코드·노코드(LCNC)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="소프트웨어 개발도구에서 로우코드 노코드까지의 지식 경로"><span>SW 공학·개발도구</span><span>개발 자동화</span><strong>Low-Code·No-Code</strong></div>

## 해당 토픽 큰 그림과 30초 인출

```text
시민개발자·전문개발자 → Visual Model·Workflow → Connector·API → Build·Deploy
                                 │
                     CoE: 승인·보안·품질·자산·Exit
```

- 인출어: `No-Code=구성`, `Low-Code=구성+확장코드`, `효과=속도·백로그`, `위험=Shadow IT·Lock-in`, `통제=CoE·ALM·Exit`

## 예상문제

> 로우코드·노코드의 개념과 플랫폼 구성, 적용효과를 설명하고 엔터프라이즈 도입 시 보안·품질·벤더 종속 대응방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| 노코드(No-Code) | 시민개발자, 사전 블록, 설정·조합 | Ⅰ·Ⅴ |
| 로우코드(Low-Code) | 시각 모델, 확장코드, 커넥터·API | Ⅰ·Ⅲ·Ⅴ |
| LCNC 거버넌스 | CoE, Shadow IT, ALM, 앱 카탈로그, Exit Plan | Ⅳ·Ⅵ |

## Ⅰ. 시각모델과 재사용부품 기반 LCNC 개요

**로우코드·노코드(LCNC)**는 시각적 모델, 사전 제작 컴포넌트와 자동화된 빌드·배포를 통해 소프트웨어를 구성하는 개발방식이다. 노코드는 현업 사용자의 구성 중심, 로우코드는 전문 개발자의 확장코드와 엔터프라이즈 연계까지 포괄하는 경향이 있으나 제품별 경계는 다르다.

## Ⅱ. 적용효과와 적합영역

| 관점 | 효과 | 적합영역 | 검증지표 |
|---|---|---|---|
| 속도 | 반복 UI·CRUD·워크플로 자동생성 | 부서업무, 프로토타입 | 리드타임, 배포빈도 |
| 협업 | 현업이 요구를 모델로 직접 확인 | 요구가시화, 업무자동화 | 재작업률, 수용시간 |
| 재사용 | 표준 컴포넌트·커넥터 활용 | 공통양식·SaaS 연계 | 재사용률, 결함률 |
| 집중 | 전문개발자가 코어 로직에 집중 | 혼합개발 | 백로그 대기시간 |

## Ⅲ. LCNC 플랫폼 구성

```text
[Persona·Portal]
       │
[Visual UI/Data Model] ─ [Workflow·Rule]
       │                       │
       └──── [Connector·API] ──┘
                    │
          [Build·Test·Deploy·Runtime]
                    │
     [IAM·Audit·Catalog·ALM·Monitoring]
```

- 시각 모델과 규칙엔진이 애플리케이션 메타모델을 구성한다.
- 커넥터·API 계층이 데이터와 외부 서비스를 연계한다.
- 런타임과 ALM 계층이 버전·시험·배포·모니터링·감사를 제공한다.

## Ⅳ. 선정에서 폐기까지의 도입절차

```text
업무분류 → 플랫폼 평가·PoC → CoE·가드레일 → 개발·검증 → 운영·Exit
```

1. 데이터 민감도, 업무중요도, 복잡도, 변경주기로 LCNC 적합성을 분류한다.
2. 기능뿐 아니라 확장성, 성능, 보안, 이식성, 비용과 공급자 지속성을 평가한다.
3. CoE가 템플릿·컴포넌트·개발권한·승인등급과 금지영역을 정의한다.
4. 시민개발과 전문개발 모두 버전관리, 분리환경, 시험·보안 게이트를 거친다.
5. 앱 카탈로그와 소유자, 데이터 흐름, 이용현황을 관리하고 반출·전환을 훈련한다.

## Ⅴ. No-Code·Low-Code·Pro-Code 비교

| 구분 | No-Code | Low-Code | Pro-Code |
|---|---|---|---|
| 주 사용자 | 현업 시민개발자 | 개발자·고급 사용자 | 전문개발자 |
| 구현 방식 | 사전 블록·설정 | 시각모델+확장코드 | 범용언어 직접구현 |
| 유연성 | 낮음~중간 | 중간~높음 | 높음 |
| 적합업무 | 단순 양식·승인·부서앱 | 업무앱·포털·통합 | 고성능·복잡 코어 |
| 핵심위험 | 섀도우 IT | 플랫폼 종속·확장 복잡도 | 개발기간·전문인력 |

## Ⅵ. 섀도우 IT와 벤더 종속 통제

| 위험 | 통제방안 | 검증자료 |
|---|---|---|
| 미승인 앱·데이터 노출 | SSO·RBAC, 환경분리, DLP, 앱 카탈로그 | 권한·데이터흐름·감사로그 |
| 품질·유지보수 부재 | 소유자 지정, 리뷰·시험·버전·폐기 절차 | ALM 이력, 시험결과 |
| 취약 컴포넌트·커넥터 | 승인 저장소, 입력검증, 의존성·비밀정보 점검 | 구성목록, 보안점검서 |
| 벤더 종속 | 모델·소스·데이터 반출, 표준 API, Exit PoC | 반출물·전환시험 결과 |
| 비용 확산 | 사용자·앱·환경별 비용 가시화와 승인 | TCO, 이용률, 미사용 앱 |

## Ⅶ. 빠른 개발보다 통제된 시민개발이 중요한 결론

LCNC의 가치는 개발자 수를 줄이는 데 있지 않고 반복업무를 표준화하고 현업 피드백을 앞당기는 데 있다. **업무 위험 기반 적용범위, CoE 가드레일, SDLC 수준의 ALM, Exit Plan**을 함께 두어야 속도와 통제를 동시에 얻는다.

## 1교시 10점 답안 발췌

```text
정의: 시각모델·재사용부품·자동 빌드/배포로 앱을 구성하는 개발방식
구조: UI·Data Model → Workflow·Rule → Connector·API → Runtime·ALM
비교: No-Code=구성 중심 / Low-Code=구성+확장 / Pro-Code=직접 구현
효과: 반복개발 단축, 현업협업, 재사용, 전문개발자의 코어 집중
통제: CoE·RBAC·환경분리·보안게이트·앱카탈로그·Exit Plan
```

## 공식·검증 근거, 학습 체크와 연결 토픽

- **공식·검증 근거**: [ISO/IEC 20741:2017 SW공학 도구 평가·선정 지침](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec%3A20741%3Aed-1%3Av1%3Aen), [ISO/IEC 25010:2023 제품 품질모델](https://www.iso.org/standard/78176.html), [OWASP Citizen Development Top 10 Security Risks](https://owasp.org/www-project-citizen-development-top10-security-risks/), 정보관리기술사 제138회 출제 이력
- **학습 체크**: □ 제품별 Low/No 경계가 다름을 밝혔는가 □ 구성-도입절차-비교표를 그렸는가 □ 보안·품질·종속·수명주기를 통제했는가
- **연결 토픽**: [요구공학](./040_requirements_engineering/) · [OpenAPI](./022_open_api/) · [보안 품질속성](./100_security_quality_attribute/) · [방법론 테일러링](./039_methodology_tailoring/)
