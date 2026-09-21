---
title: "성능 요구사항(Performance Requirement)"
category: "02-software-engineering"
tags:
  - "성능요구사항"
  - "비기능요구사항"
  - "ISO25010"
  - "아키텍처드라이버"
  - "품질속성시나리오"
  - "SLASLO"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 요구공학과 소프트웨어 아키텍처를 거쳐 성능 요구사항으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>요구공학·소프트웨어 아키텍처</span>
  <strong>성능 요구사항(Performance Requirement)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 제약된 컴퓨팅 자원(CPU, 메모리, 네트워크, 스토리지) 한계 내에서 시스템이 비즈니스 트랜잭션을 처리할 때 요구되는 시간 반응성(응답시간/지연시간), 처리 용량(TPS), 자원 활용률을 정량적으로 명세하여 전체 소프트웨어 아키텍처와 인프라 사이징을 결정짓는 핵심 아키텍처 드라이버(Architectural Driver)
- 메커니즘: 비즈니스 트래픽 프로파일링 $\rightarrow$ SEI 품질 속성 시나리오 6대 요소 명세 $\rightarrow$ 아키텍처 전술(자원 수요 조절·공급 관리) 설계 $\rightarrow$ 단계별 성능 부하 시험(Load/Stress Test) 및 SLA 적합성 검증
- 산출물: 성능 요구사항 명세서(SRS) · 품질 속성 시나리오 정의서 · 성능 테스트 결과서(BMT/부하 시험 성적서)

<div class="itpe-flow-map" role="img" aria-label="성능 요구사항 도출부터 아키텍처 반영 및 검증 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 비즈니스 부하 프로파일링</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>평상시/피크시 동시 사용자 수, 일일 트랜잭션 규모, 데이터 증가율 산정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 품질 속성 시나리오 정량 명세</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>명세</strong><span>자극(피크 5,000 TPS) 및 응답 측정(p95 1.0초 이하) 기반 객관적 수치화</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 성능 아키텍처 전술 수립</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설계</strong><span>인메모리 캐싱(Redis), 비동기 이벤트 큐(Kafka), DB 읽기 분제(CQRS) 적용</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 부하 테스트 성능 게이트 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>최대 부하 시험 시 응답시간(p95/p99)과 자원 사용률이 목표 SLA/SLO 기준을 만족하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (성능 Baseline 확정)</strong>
      <span>성능 검증 완료 $\rightarrow$ 프로덕션 배포 승인 및 APM 모니터링 연계</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (임계 초과 / 병목 발생)</strong>
      <span>APM 프로파일링 수행 $\rightarrow$ 슬로우 쿼리 튜닝 및 인프라 스케일아웃 재설계</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Architectural Driver(아키텍처 드라이버)**: 시스템의 골격 구조, 통신 방식, 컴포넌트 분할 등 핵심 설계 결정을 강제하는 가장 영향력 있는 비기능적 요구사항
- **품질 속성 시나리오(Quality Attribute Scenario)**: SEI(Software Engineering Institute)에서 제안한 명세 방식으로, 자극원·자극·대상·환경·응답·응답측정 6가지 요소로 모호한 비기능 요구를 정량화하는 기법
- **ISO/IEC 25010 성능 효율성(Performance Efficiency)**: 명시된 조건에서 사용되는 자원의 양 대비 시스템의 성능 수준을 나타내는 품질 특성(시간 반응성, 자원 활용성, 용량)
- **SLA/SLO/SLI**: 서비스 수준 협약(SLA), 서비스 수준 목표(SLO), 서비스 수준 지표(SLI)로 구성되는 정량적 성능 거버넌스 체계
</details>

## 1. 개요 및 필요성

### 기능 중심 소프트웨어 개발의 함정과 성능의 아키텍처 지배력

과거 소프트웨어 프로젝트는 "기능이 요구사항 명세서대로 동작하는가"에만 집중하고 성능은 개발 완료 후 튜닝으로 해결하려는 경향이 강했다. 그러나 동시 접속자가 폭증하거나 대용량 데이터가 누적되면, 데이터베이스 락(Lock) 경합, 네트워크 I/O 병목, 메모리 고갈로 인해 시스템 전체가 마비되는 참사가 발생한다.

성능은 단순한 코드 튜닝이 아니라 **데이터베이스 분할(Sharding), 캐시 아키텍처, 비동기 메시징 구조, 오토스케일링 인프라 설계**를 결정짓는 핵심 아키텍처 동인이므로 요구공학 초기 단계에서 반드시 정량적으로 명세되어야 한다.

### 기능 vs 성능 vs 신뢰성 요구사항 비교

| 구분 | 기능 요구사항 (Functional) | 성능 요구사항 (Performance) | 신뢰성 요구사항 (Reliability) |
|---|---|---|---|
| **핵심 질문** | "시스템이 **무엇을** 수행하는가?" | "시스템이 **얼마나 빠르고 효율적으로** 처리하는가?" | "시스템이 **장애 없이 지속적으로** 가동되는가?" |
| **명세 대상** | 입력 데이터 처리, 비즈니스 규칙, 계산 로직 | 응답시간, 처리량(TPS), CPU/메모리 한계 | 가용성(99.99%), MTBF, MTTR, 무장애 운영 시간 |
| **측정 방식** | 참/거짓(Pass/Fail) 기능 검증 | 초(sec), TPS, % 등 정량적 수치 계측 | 가동률(%), 평균 복구 시간(분) 계측 |
| **아키텍처 영향** | 도메인 모델, 비즈니스 레이어 구조 | **분산 캐시, 비동기 파이프라인, 데이터 파티셔닝** | 이중화, 페일오버(Failover), 서킷 브레이커 |

## 2. 아키텍처 및 핵심 메커니즘

### SEI 품질 속성 시나리오와 아키텍처 전술(Tactics) 연계

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="scen-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background Frame -->
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">SEI 품질 속성 시나리오 6요소 및 아키텍처 전술 연계</text>

    <!-- Left Box: Scenario 6 Elements -->
    <rect x="15" y="38" width="235" height="165" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="15" y="38" width="235" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="132" y="53" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">품질 속성 시나리오 6대 구성 요소</text>

    <text x="25" y="75" font-size="7" fill="var(--color-text, #1e293b)">1. 자극원: 모바일 앱 사용자</text>
    <text x="25" y="93" font-size="7" fill="var(--color-text, #1e293b)">2. 자극: 월말 피크 5,000 TPS 유입</text>
    <text x="25" y="111" font-size="7" fill="var(--color-text, #1e293b)">3. 대상: 결제 및 주문 코어 API</text>
    <text x="25" y="129" font-size="7" fill="var(--color-text, #1e293b)">4. 환경: 클라우드 정상 운영 모드</text>
    <text x="25" y="147" font-size="7" fill="var(--color-text, #1e293b)">5. 응답: 모든 트랜잭션 정상 완료</text>
    <text x="25" y="165" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">6. 응답측정: p95 &lt; 0.5초, CPU &lt; 70%</text>

    <text x="132" y="190" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">모호한 비기능 요구의 정량적 객관화</text>

    <!-- Transition Arrow -->
    <line x1="250" y1="120" x2="270" y2="120" stroke="var(--color-primary, #2563eb)" stroke-width="1.8" marker-end="url(#scen-arrow)"/>

    <!-- Right Box: Architecture Tactics -->
    <rect x="275" y="38" width="230" height="165" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.4"/>
    <rect x="275" y="38" width="230" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="390" y="53" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">성능 아키텍처 전술 (Tactics)</text>

    <!-- Tactic A: Demand Control -->
    <rect x="285" y="68" width="210" height="52" rx="4" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="390" y="84" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">자원 수요 조절 전술</text>
    <text x="390" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 인메모리 Redis 캐싱 (DB 부하 차단)</text>
    <text x="390" y="112" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- API Rate Limiting 및 정적 CDN</text>

    <!-- Tactic B: Supply Management -->
    <rect x="285" y="128" width="210" height="65" rx="4" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="390" y="144" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">자원 공급 관리 전술</text>
    <text x="390" y="158" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 비동기 메시지 큐 (Kafka Buffer)</text>
    <text x="390" y="172" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- KEDA 기반 파드 오토스케일링</text>
    <text x="390" y="185" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- DB 읽기 분제 (CQRS Read Replica)</text>
  </svg>
</div>

### 테일 레이턴시(Tail Latency) 및 SRE Error Budget 거버넌스

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <!-- Frame -->
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">응답시간 백분위수 (p99 Tail Latency) 및 SRE 거버넌스</text>

    <!-- Distribution Curve View (Left) -->
    <rect x="15" y="38" width="245" height="145" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="137" y="54" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">응답시간 확률 밀도 분포</text>

    <!-- Axis -->
    <line x1="30" y1="150" x2="245" y2="150" stroke="var(--color-border, #64748b)" stroke-width="1.2"/>
    <line x1="30" y1="150" x2="30" y2="65" stroke="var(--color-border, #64748b)" stroke-width="1.2"/>
    <text x="245" y="162" text-anchor="end" font-size="6.5" fill="var(--color-text-muted, #64748b)">지연시간 (ms)</text>

    <!-- Skewed Curve -->
    <path d="M 30 150 Q 60 70 85 95 T 160 142 T 240 148" fill="none" stroke="var(--color-primary, #2563eb)" stroke-width="2"/>

    <!-- Mean line -->
    <line x1="75" y1="85" x2="75" y2="150" stroke="#16a34a" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="75" y="78" text-anchor="middle" font-size="6.5" fill="#16a34a">평균 0.2s</text>

    <!-- p95 line -->
    <line x1="140" y1="130" x2="140" y2="150" stroke="var(--color-accent, #0284c7)" stroke-width="1" stroke-dasharray="3,2"/>
    <text x="140" y="125" text-anchor="middle" font-size="6.5" fill="var(--color-accent, #0284c7)">p95 0.5s</text>

    <!-- p99 tail line -->
    <line x1="210" y1="144" x2="210" y2="150" stroke="#ef4444" stroke-width="1.5"/>
    <text x="210" y="135" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#dc2626">p99 (테일) 2.8s</text>
    <text x="137" y="174" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">평균에 가려진 1% 지연이 MSA 전체 마비 유발</text>

    <!-- Right Box: SRE Error Budget Policy -->
    <rect x="270" y="38" width="235" height="145" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <rect x="270" y="38" width="235" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="387" y="53" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">SRE 에러 버짓(Error Budget) 연계</text>

    <text x="280" y="76" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">- SLI: 실제 계측된 p95 응답시간</text>
    <text x="280" y="94" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">- SLO: "p95 &lt; 0.5s 비율 99.9% 유지"</text>
    
    <rect x="280" y="106" width="215" height="65" rx="4" fill="var(--color-bg-subtle, #fef2f2)" stroke="#ef4444" stroke-width="1"/>
    <text x="387" y="122" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#dc2626">에러 버짓 소진 시 강제 정책</text>
    <text x="387" y="140" text-anchor="middle" font-size="6.5" fill="var(--color-text, #334155)">신규 기능 배포 전면 중단 (Freeze)</text>
    <text x="387" y="156" text-anchor="middle" font-size="6.5" fill="#dc2626">성능 튜닝 및 인프라 개선 스프린트 강제</text>
  </svg>
</div>

### ISO/IEC 25010 성능 효율성 3대 하위 품질 특성

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 시간 반응성 (Time Behaviour)</strong></span>
      <span class="itpe-badge">속도 측정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>응답시간(Response Time): 요청 전송 후 최종 결과 수신까지의 시간</li>
        <li>처리 시간(Turnaround Time) 및 지연 시간(Latency) 최소화</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 자원 활용성 (Resource Utilization)</strong></span>
      <span class="itpe-badge">효율성 측정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>CPU 점유율, 메모리 사용량, 네트워크 대역폭, 디스크 I/O 소비량</li>
        <li>피크 부하 시에도 하드웨어 자원 임계치(예: 70~80%) 이내 유지</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 용량 (Capacity)</strong></span>
      <span class="itpe-badge">한계 측정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>처리량(Throughput): 단위 시간당 처리 가능한 트랜잭션 수(TPS)</li>
        <li>동시 사용자 수(Concurrent Users) 및 최대 데이터베이스 저장 용량</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 프로젝트 종료 직전 통합 부하 시험 시 DB 락 경합으로 인한 성능 미달이 발견되어 오픈 연기 | Shift-Left 성능 공학 적용: 스프린트 단위로 k6 부하 테스트 자동화 및 아키텍처 조기 검증 | 성능 병목 조기 식별 및 아키텍처 재작업 비용 90% 절감 |
| "시스템이 사용자에게 신속하게 반응해야 한다"와 같은 정성적 문구로 인한 인수·감리 분쟁 | SEI 품질 속성 시나리오 6대 요소를 적용하여 95th 백분위 응답시간 및 TPS 수치 명시 | 모호성 100% 제거 및 명확한 검수 기준선 확립 |
| 과도하게 높은 성능 목표치(예: 상시 10만 TPS) 설정으로 인프라 구독료 및 TCO 폭증 | CBAM(비용 편익 분석 기법)을 활용하여 비즈니스 가치와 인프라 비용 간 트레이드오프 분석 | 불필요한 과대 사이징 방지 및 인프라 예산 40% 절감 |

## 4. 기술사 답안 차별화 포인트

### 테일 레이턴시(Tail Latency, p99/p99.9)와 롱테일 관리

전통적인 평균 응답시간(Average Response Time)은 소수의 극단적인 지연(Tail Latency)을 완전히 은폐한다. 마이크로서비스 아키텍처에서는 한 사용자의 요청이 수십 개의 내부 서비스를 거치므로, 단 하나의 서비스에서 1%의 지연(p99)이 발생해도 전체 사용자 경험은 심각하게 붕괴된다. 기술사 답안에서는 **"평균치 대신 p95, p99, p99.9 백분위수 지표(Percentile)를 성능 요구사항의 표준 기준으로 설정해야 함"**을 강조한다.

### SRE(Site Reliability Engineering)의 에러 버짓(Error Budget) 연계

성능 요구사항은 고정된 정적 문서가 아니라 운영 단계의 SRE 거버넌스로 이어져야 한다. 성능 요구사항을 기반으로 **SLI(측정값)와 SLO(내부 목표)**를 정의하고, SLO를 위반할 경우 할당된 **에러 버짓(Error Budget)**이 소진되어 신규 기능 배포를 중단하고 성능 튜닝 스프린트를 강제하는 현대적 데브옵스 운영 체계를 결론으로 제시한다.

## 5. 결론 및 종합 제언

### 학습자 통찰 메모 — 답안 밖

[핵심 통찰]
성능 요구사항은 소프트웨어 개발이 다 끝난 뒤 부하를 걸어보는 '사후 시험 성적서'가 아니다. 시스템의 데이터 저장 방식, 분산 캐시 토폴로지, 비동기 큐 도입 여부를 결정짓는 **'최상위 아키텍처 드라이버(Architectural Driver)'**다. 정량적 시나리오가 초기에 수립되지 않으면 아키텍처는 반드시 침식된다.

나라면:
본 시험에서 성능 요구사항이 출제되면, SEI 품질 속성 시나리오의 6요소를 정확히 기술한 뒤 **(1) 평균값의 착시를 깨는 p95/p99 테일 레이턴시 관리, (2) 수요 조절(캐싱)과 공급 관리(오토스케일링) 아키텍처 전술 분기, (3) 성능 미달 시 기능 배포를 강제 중단시키는 SRE 에러 버짓(Error Budget) 거버넌스 파이프라인**을 3단락에 명쾌하게 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 통합 부하 시험 시 피크 트래픽(동시 5,000 TPS)에서 p99 응답시간 1.0초 초과 시 배포 부적격 판정
- **대응 방안**: Redis 분산 캐시 계층 신설 및 슬로우 쿼리 튜닝, KEDA 기반 이벤트 주도형 오토스케일링 전술 적용
- **검증 체계**: CI/CD 배포 파이프라인에 k6 성능 게이트를 연동하고 프로덕션 APM과 연계된 SLO/SLI 모니터링 가동
- **기대 효과**: 대규모 트래픽 폭증 시 시스템 무중단 보장 및 명확한 정량적 성능 지표 기반 인수 분쟁 원천 방지

<div class="itpe-pipeline-container" role="region" aria-label="성능 요구사항 엔지니어링 및 SRE 검증 파이프라인">
  <div class="itpe-pipeline-header">
    <span class="itpe-pipeline-title">성능 요구사항 엔지니어링 및 SRE 검증 파이프라인</span>
    <span class="itpe-pipeline-badge">성능 거버넌스</span>
  </div>
  <div class="itpe-pipeline-grid">
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">1단계: 정량 명세</div>
      <div class="itpe-card-title">시나리오 도출</div>
      <div class="itpe-card-body">SEI 6대 요소를 기반으로 피크 부하 및 p95/p99 백분위수 정량화</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">2단계: 전술 설계</div>
      <div class="itpe-card-title">아키텍처 반영</div>
      <div class="itpe-card-body">분산 캐시, 비동기 큐, CQRS 분리, 파드 오토스케일링 전술 구현</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">3단계: 조기 검증</div>
      <div class="itpe-card-title">Shift-Left 부하</div>
      <div class="itpe-card-body">스프린트 단위 k6 자동화 부하 시험으로 성능 병목 조기 식별</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">4단계: 운영 통제</div>
      <div class="itpe-card-title">SRE 에러 버짓</div>
      <div class="itpe-card-body">SLO 위반 모니터링 및 버짓 소진 시 배포 동결·튜닝 강제 집행</div>
    </div>
  </div>
</div>

## 6. 참고 및 연계 학습

- [소프트웨어 품질 비용(Cost of Quality)](./150_software_quality_cost.md)
- [기능 점수(Function Point) 산정](./130_function_point.md)
- [서비스 워커 및 웹 성능 최적화](./147_service_worker.md)
- [웹 성능 최적화 기법](./164_web_performance_optimization.md)
