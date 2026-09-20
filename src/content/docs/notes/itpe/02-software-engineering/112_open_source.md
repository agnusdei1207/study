---
title: "오픈소스 소프트웨어(OSS) 및 거버넌스"
category: "02-software-engineering"
tags:
  - "오픈소스"
  - "OSS"
  - "OSS거버넌스"
  - "OSPO"
  - "SCA"
  - "SBOM"
  - "공급망보안"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 품질 관리 및 공급망 보안을 거쳐 오픈소스 거버넌스로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>품질 관리·공급망 보안</span>
  <strong>오픈소스 소프트웨어(OSS) 및 거버넌스</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 상용 소프트웨어의 벤더 종속과 높은 라이선스 비용을 극복하기 위해 공개된 소프트웨어를 활용하되, 소스코드 강제 공개(Copyleft 감염) 위험과 공급망 보안 취약점(CVE)을 방어하기 위해 조직·프로세스·자동화 도구를 통합 통제하는 엔터프라이즈 관리 체계
- 메커니즘: 오픈소스 선정 심의(OSPO) → SCA(Software Composition Analysis) 정적 스캔 → 프라이빗 저장소 격리 반입 → CI/CD 빌드 시 기계 판독형 SBOM(SPDX/CycloneDX) 생성 → 라이선스 고지문 발행
- 산출물: 오픈소스 라이선스 정책서 · SCA 분석 보고서 · SBOM 명세서 · 오픈소스 고지문(Notices) 및 소스코드 공개 패키지

<div class="itpe-flow-map" role="img" aria-label="엔터프라이즈 오픈소스 거버넌스 생명주기 및 통제 체계">
  <div class="itpe-flow-node">
    <strong>1단계: 탐색 및 적합성 심의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>심의</strong><span>커뮤니티 활성도, 보안 이력, 조직(OSPO) 적합성 검토</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: SCA 스캔 및 반입 승인</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>검증</strong><span>라이선스 충돌 판정 · CVE 보안 취약점 점검 (<span class="itpe-keyword"><strong>SCA 도구</strong></span>)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>3단계: 프라이빗 저장소 격리 및 빌드</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>통제</strong><span>외부 무단 다운로드 차단 · 검증된 패키지만 사내 Repo(Harbor/Nexus) 허용</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: SBOM 생성 및 배포 고지</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>산출</strong><span><span class="itpe-keyword"><strong>SBOM(SPDX/CycloneDX)</strong></span> 자동 생성 · 저작권 고지문 배포</span></div>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **OSD(Open Source Definition)**: 오픈소스 이니셔티브(OSI)가 제정한 10대 조건으로, 소스코드 공개, 자유로운 재배포, 파생 저작물 허용, 개인/분야에 대한 차별 금지 등을 규정
- **OSPO(Open Source Program Office)**: 기업 내 오픈소스 라이선스 컴플라이언스 준수, 사내 오픈소스 정책 수립, 커뮤니티 기여를 총괄하는 전담 거버넌스 조직
- **SCA(Software Composition Analysis)**: 애플리케이션의 직접 및 간접 의존성(Transitive Dependencies)을 분석하여 오픈소스 라이선스 위반 및 알려진 취약점(CVE)을 탐지하는 소프트웨어 구성 분석 기술
- **SBOM(Software Bill of Materials)**: 소프트웨어를 구성하는 모든 오픈소스 및 서드파티 컴포넌트의 이름, 버전, 라이선스, 해시값을 기계가 판독할 수 있는 표준(SPDX, CycloneDX)으로 나열한 소프트웨어 자재명세서
</details>

## 1. 개요 및 필요성

### 오픈소스 확산과 법적·보안적 위험의 심화

현대 엔터프라이즈 소프트웨어의 80~90%는 오픈소스 컴포넌트로 구성되어 있다. 오픈소스는 개발 기간 단축과 비용 절감, 최신 기술 도입의 핵심 동력이지만, 동시에 **라이선스 법적 분쟁(지식재산권 침해)과 소프트웨어 공급망 보안 위협(Log4j, Spring4Shell 등)**이라는 심각한 리스크를 수반한다.

개발자가 무단으로 GPL 라이선스 라이브러리를 사내 핵심 비즈니스 로직에 정적 링크할 경우, 기업 고유의 독점 소프트웨어 소스코드를 외부에 전면 공개해야 하는 법적 재앙이 발생할 수 있다. 따라서 오픈소스의 탐색, 검증, 승인, 빌드, 배포 전 과정을 조직적이고 기술적으로 통제하는 **오픈소스 거버넌스(OSS Governance)** 체계 수립이 필수적이다.

### 오픈소스 라이선스 3대 유형 비교

| 구분 | Permissive (관용형) | Weak Copyleft (약한 상호형) | Strong Copyleft (강한 상호형) |
|---|---|---|---|
| **대표 라이선스** | **MIT, Apache 2.0, BSD** | **LGPL 2.1/3.0, MPL** | **GPL 2.0/3.0, AGPL 3.0** |
| **소스코드 공개 의무** | 공개 의무 없음 (상용 비공개 가능) | 해당 라이브러리 수정 부분만 공개 | 결합된 전체 파생 저작물 소스 공개 |
| **링크(Linking) 영향** | 정적/동적 링크 불문 독점 허용 | 동적 링크 시 비공개, 정적 링크 시 공개 | 동적/정적 링크 불문 전체 GPL 감염 |
| **특허권 조항** | Apache 2.0 (특허 라이선스 명시 부여) | 특허 보복 조항 포함 | 특허 소송 제기 시 라이선스 자동 종료 |
| **네트워크 서비스** | 비공개 SaaS 서비스 운영 가능 | 비공개 SaaS 서비스 운영 가능 | **AGPL은 네트워크 서비스 시에도 공개 의무** |

## 2. 아키텍처 및 핵심 메커니즘

### 오픈소스 거버넌스 3대 축 (조직 · 프로세스 · 도구)

```text
+-------------------------------------------------------------------------+
|                  엔터프라이즈 OSS 거버넌스 3대 핵심 축                  |
+-------------------------------------------------------------------------+
| [ 1. 거버넌스 조직 (OSPO) ]                                             |
|    - 오픈소스 전담 부서(OSPO, Open Source Program Office) 운영          |
|    - 개발팀, 보안팀, 법무팀 간 라이선스 정책 심의 및 컴플라이언스 총괄 |
|                                    │                                    |
| [ 2. 반입 및 배포 프로세스 ]       │ [ 3. 자동화 도구 체계 (SCA & SBOM) ]|
|    - 도입 전 사전 승인 절차        │    - CI/CD 파이프라인 SCA 정적 스캔 |
|    - 사내 프라이빗 레포지토리 운영 │    - SPDX / CycloneDX 표준 SBOM 생성|
|    - 릴리스 전 라이선스 고지서 발행│    - 실시간 NVD CVE 취약점 모니터링 |
+-------------------------------------------------------------------------+
```

### 전주기 오픈소스 통제 파이프라인

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① IDE 개발 단계 (Shift-Left)</strong></span>
      <span class="itpe-badge">사전 예방</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>개발자 IDE 플러그인을 통해 비인가 라이선스(GPL 등) 임포트 시 실시간 경고</li>
        <li>보안 취약점이 존재하는 라이브러리의 안전한 최신 버전 대체 추천</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 사내 프라이빗 저장소 격리</strong></span>
      <span class="itpe-badge">반입 통제</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>공용 레지스트리(npm, PyPI, Maven) 직접 다운로드 차단</li>
        <li>Harbor, Nexus 프록시를 통해 보안·라이선스 검증 완료 패키지만 캐싱</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ CI/CD 빌드 단계 SCA 검증</strong></span>
      <span class="itpe-badge">품질 게이트</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>Black Duck, FOSSID, Snyk 기반 직접·간접 의존성 전수 스캔</li>
        <li>Critical/High CVE 발견 또는 라이선스 충돌 시 빌드 자동 차단(Fail)</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 배포 및 SBOM 거버넌스</strong></span>
      <span class="itpe-badge">사후 통제</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>빌드 아티팩트와 함께 SPDX/CycloneDX 기계 판독형 SBOM 산출</li>
        <li>제품 패키지에 오픈소스 저작권 고지문 자동 포함 및 감사 대응</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 상용 독점 서비스 배포 후 강한 카피레프트(GPL) 라이선스 위반으로 소스코드 강제 공개 소송 접수 | 사내 프라이빗 저장소 경유 강제 및 CI 파이프라인에서 SCA 도구를 통한 라이선스 화이트리스트 자동 검증 | 지식재산권 침해 분쟁 및 비즈니스 핵심 자산 노출 원천 차단 |
| 수많은 중첩 간접 의존성(Transitive Dependency)으로 인해 신규 제로데이 취약점 영향도 파악 지연 | 빌드 시 CycloneDX 기반 SBOM 자동 생성 및 사내 취약점 관제 플랫폼과 실시간 CVE 연동 | 제로데이 발생 시 영향받는 전사 시스템 역추적 시간을 수일에서 수분 이내로 단축 |
| 오픈소스 커뮤니티 개발 중단(Abandonware)으로 인한 장기 유지보수 단절 | OSPO 주관 도입 평가 시 커밋 빈도, 컨트리뷰터 수, 기업 스폰서십 등 프로젝트 건전성 심의 의무화 | 의존성 고립 방지 및 안정적인 장기 운영성 확보 |

## 4. 기술사 답안 차별화 포인트

### 소프트웨어 공급망 보안(Executive Order 14028)과 SBOM 표준

답안 작성 시 단순한 라이선스 컴플라이언스를 넘어 **미국 백악관 행정명령(EO 14028)에 따른 소프트웨어 공급망 보안 의무화** 흐름을 언급해야 한다. 공급망 공격(SolarWinds 참사) 이후 전 세계적으로 공공·금융 조달 시 기계 판독형 SBOM 제출이 법제화되고 있음을 밝히고, 대표 표준인 **SPDX(Linux Foundation 제정 ISO 표준)**와 **CycloneDX(OWASP 경량 표준)**의 포맷 차이와 적용 방안을 제시하면 최신 정책과 기술을 완벽히 꿰뚫고 있음을 보여줄 수 있다.

### Shift-Left IDE 연동 및 정책 기반 Gatekeeper 전략

많은 기업의 실패 요인은 릴리스 직전에야 수작업 엑셀로 오픈소스를 점검하여 출시가 지연되거나 형식적 승인으로 끝나는 데 있다. 이를 극복하기 위해 개발 단계(IDE 린터), PR 단계(SCA 자동 분석), 배포 단계(컨테이너 이미지 Cosign 서명)로 이어지는 **Shift-Left 자동화 파이프라인**을 3단락 또는 전문가 제언으로 제시한다.

## 5. 참고 및 연계 학습

- [CI/CD 파이프라인 구축](./095_ci_cd.md)
- [상용SW 직접구매 제도](./101_commercial_sw_direct_purchase.md)
- [ALM(애플리케이션 수명주기 관리)](./107_alm.md)
- [소프트웨어 안전성 가이드라인](./097_sw_safety_guidelines.md)
