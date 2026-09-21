---
title: "카오스 테스트(Chaos Test)"
category: "02-software-engineering"
tags:
  - "카오스테스트"
  - "카오스엔지니어링"
  - "ChaosEngineering"
  - "회복탄력성"
  - "폭발반경"
  - "서킷브레이커"
  - "넷플릭스"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 테스팅과 회복탄력성 엔지니어링을 거쳐 카오스 테스트로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 테스팅·회복탄력성 엔지니어링</span>
  <strong>카오스 테스트(Chaos Test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 분산 클라우드 환경에서 하드웨어 고장, 네트워크 지연, 인스턴스 크래시 등 불가피한 돌발 결함이 발생했을 때 시스템이 연쇄 장애로 붕괴하지 않고 스스로 복구하는지 검증하기 위해, 운영 및 유사 환경에 제어된 장애를 선제적으로 주입하여 시스템의 회복 탄력성(Resilience)을 실증하는 실험적 테스팅 기법
- 메커니즘: 비즈니스 정상 상태(Steady State) 정의 $\rightarrow$ 장애 내결함 가설 수립 $\rightarrow$ 최소 폭발 반경(Blast Radius) 내 장애 주입 실험 $\rightarrow$ 지표 관측 및 자가 치유 판정 $\rightarrow$ 취약점 개선
- 산출물: 카오스 실험 계획서 · 정상 상태 메트릭 정의서 · 회복력 검증 리포트 · 긴급 중단 롤백 절차서

<div class="itpe-flow-map" role="img" aria-label="카오스 엔지니어링 4단계 실험 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 정상 상태(Steady State) 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>계측</strong><span>초당 주문 성공 건수, p99 응답시간 등 정상 작동 대변 지표 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 가설 수립 및 폭발 반경 통제</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설계</strong><span>"결제 파드 1개가 급사해도 전체 결제 성공률은 99.9% 유지된다" 가설</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 통제된 결함 주입 (Fault Injection)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>주입</strong><span>Chaos Mesh/Litmus 기반 파드 강제 종료 및 500ms 네트워크 지연 발생</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 회복 탄력성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>서킷 브레이커와 오토스케일링이 작동하여 정상 상태 메트릭을 유지하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (가설 검증 성공)</strong>
      <span>자가 치유 확인 $\rightarrow$ 회복 탄력성 Baseline 승인 및 정기 자동화 실험 등록</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (연쇄 장애 전파)</strong>
      <span>비상 중단(Rollback) 즉각 발동 $\rightarrow$ 타임아웃/서킷 브레이커 설정 재설계</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Steady State(정상 상태)**: 시스템이 장애 없이 정상적으로 비즈니스를 수행하고 있음을 객관적으로 나타내는 측정 가능한 비즈니스 메트릭(예: 초당 결제 트랜잭션 수)
- **Blast Radius(폭발 반경)**: 카오스 장애 주입 시 실제 사용자나 연계 시스템에 미칠 수 있는 피해의 물리적·논리적 영향 범위
- **Resilience(회복 탄력성)**: 시스템에 예기치 않은 오류, 고장, 부하가 발생하더라도 기능을 정상 유지하거나 스스로 신속하게 원래 상태로 복구하는 능력
- **Simian Army**: 넷플릭스에서 개발한 카오스 도구군으로, Chaos Monkey(서버 강제 종료), Chaos Gorilla(가용 영역 AZ 다운), Chaos Kong(전체 리전 다운) 등으로 구성
</details>

## 1. 개요 및 필요성

### 클라우드 복잡성과 "고장 불가피성(Design for Failure)"

수천 개의 마이크로서비스로 구성된 분산 클라우드 환경에서는 네트워크 단절, 디스크 풀, 써드파티 API 먹통 등 장애가 일상적으로 발생한다. "장애를 100% 예방할 수 있다"는 전통적 관점은 클라우드에서 완전히 붕괴되었다.

카오스 테스트는 **"장애는 반드시 발생한다"**는 전제하에, 새벽에 돌발 장애로 시스템이 터지기 전에 **업무 시간 중에 엔지니어가 모니터링하는 상태에서 고의로 장애를 터뜨려** 아키텍처의 취약점을 선제적으로 도출하는 현대적 신뢰성 공학 기법이다.

### 전통적 장애 테스트 vs 카오스 테스트 비교

| 구분 | 전통적 장애 복구 테스트 (DR Test) | 카오스 테스트 (Chaos Test) |
|---|---|---|
| **수행 환경** | 격리된 테스트베드 / 사전 공지된 모의 훈련 | **실제 운영 환경 (또는 프로덕션 동등 환경)** |
| **장애 주입 방식** | 사전에 약속된 시나리오에 따른 수작업 차단 | **자동화된 도구를 통한 무작위·돌발적 결함 주입** |
| **초점 영역** | 백업 및 수동 페일오버(Failover) 매뉴얼 검증 | **소프트웨어 아키텍처의 자가 치유(Self-Healing) 검증** |
| **수행 주기** | 연 1~2회 대규모 정기 훈련 | **CI/CD 파이프라인 연계 지속적 상시 실험** |
| **핵심 지표** | RTO(목표 복구 시간), RPO(목표 복구 시점) | **정상 상태 메트릭 변동률, 서비스 가용성(SLO)** |

## 2. 아키텍처 및 핵심 메커니즘

### 카오스 엔지니어링 4단계 실험 및 폭발 반경 통제

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="ch-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Frame -->
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">카오스 엔지니어링 4단계 순환 실험 및 폭발 반경 통제</text>

    <!-- Step 1 -->
    <rect x="15" y="42" width="110" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="15" y="42" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="70" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">1. 정상 상태 정의</text>
    <text x="70" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">Steady State</text>
    <text x="70" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 초당 결제 성공률</text>
    <text x="70" y="114" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- p99 &lt; 500ms</text>
    <text x="70" y="138" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">[비즈니스 기준선]</text>

    <line x1="125" y1="97" x2="138" y2="97" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ch-arrow)"/>

    <!-- Step 2 -->
    <rect x="140" y="42" width="110" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="140" y="42" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="195" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">2. 가설 수립</text>
    <text x="195" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">Hypothesis</text>
    <text x="195" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 결제 파드 급사 시</text>
    <text x="195" y="114" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 서킷브레이커 오픈</text>
    <text x="195" y="138" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[복원력 설계]</text>

    <line x1="250" y1="97" x2="263" y2="97" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ch-arrow)"/>

    <!-- Step 3 -->
    <rect x="265" y="42" width="115" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#ef4444" stroke-width="1.4"/>
    <rect x="265" y="42" width="115" height="22" rx="6" fill="var(--color-bg-subtle, #fef2f2)"/>
    <text x="322" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#dc2626">3. 결함 주입</text>
    <text x="322" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">Fault Injection</text>
    <text x="322" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- LitmusChaos 주입</text>
    <text x="322" y="114" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 폭발반경: 카나리</text>
    <text x="322" y="138" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#dc2626">[통제된 재해]</text>

    <line x1="380" y1="97" x2="393" y2="97" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ch-arrow)"/>

    <!-- Step 4 -->
    <rect x="395" y="42" width="110" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#16a34a" stroke-width="1.4"/>
    <rect x="395" y="42" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #f0fdf4)"/>
    <text x="450" y="57" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#16a34a">4. 자가 치유 검증</text>
    <text x="450" y="80" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">Self-Healing</text>
    <text x="450" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 정상 상태 유지 여부</text>
    <text x="450" y="114" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">- 이상 시 자동 롤백</text>
    <text x="450" y="138" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#16a34a">[가설 입증]</text>

    <!-- Safety Bottom Switch -->
    <rect x="15" y="162" width="490" height="38" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="178" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#dc2626">안전장치(Dead Man's Switch): 비즈니스 에러율 임계치 초과 즉시 장애 주입 프로세스 자동 킬 및 원복</text>
    <text x="260" y="192" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">최소 폭발 반경(Blast Radius) 원칙을 준수하여 실제 고객 피해 발생을 0%로 완벽 차단</text>
  </svg>
</div>

### GitOps 기반 Chaos-as-Code 및 K8s 복원력 지속 검증

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="k8s-c-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Frame -->
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">GitOps 기반 Chaos-as-Code (Litmus/Chaos Mesh) 자동화 구조</text>

    <!-- Git Repo -->
    <rect x="15" y="45" width="100" height="65" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="65" y="68" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Git 저장소</text>
    <text x="65" y="85" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">chaos-test.yaml</text>
    <text x="65" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">CRD 선언적 명세</text>

    <line x1="115" y1="78" x2="145" y2="78" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#k8s-c-arrow)"/>

    <!-- ArgoCD -->
    <rect x="145" y="45" width="105" height="65" rx="5" fill="var(--color-bg-subtle, #eff6ff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <text x="197" y="68" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">ArgoCD / GitOps</text>
    <text x="197" y="85" text-anchor="middle" font-size="7" fill="var(--color-text, #1e293b)">지속적 배포</text>
    <text x="197" y="98" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">정기 스케줄 동기화</text>

    <line x1="250" y1="78" x2="280" y2="78" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#k8s-c-arrow)"/>

    <!-- K8s Chaos Operator -->
    <rect x="280" y="45" width="225" height="65" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#ef4444" stroke-width="1.4"/>
    <text x="392" y="68" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#dc2626">Chaos Mesh Operator (K8s 클러스터)</text>
    <text x="392" y="85" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">- PodKill / NetworkDelay / I/O Chaos</text>
    <text x="392" y="98" text-anchor="middle" font-size="6.5" fill="#dc2626">사전 정의된 네임스페이스 격리 주입</text>

    <!-- Bottom Monitoring Feedback -->
    <rect x="15" y="125" width="490" height="55" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="145" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">Prometheus 관측 및 금융권 DORA(디지털 운영 탄력성) 감사 증적 연계</text>
    <text x="260" y="165" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">장애 주입 중 서킷 브레이커와 HPA 오토스케일링이 정상 가동되었음을 정량 리포트로 자동 생성</text>
  </svg>
</div>

### 카오스 실험 4대 핵심 구성요소

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 정상 상태 메트릭</strong></span>
      <span class="itpe-badge">기준선 정의</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>CPU 등 단순 시스템 지표가 아닌 비즈니스 트랜잭션 지표 중심</li>
        <li>Prometheus/Datadog 메트릭과 연계하여 실시간 편차 감시</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 결함 주입기 (Injector)</strong></span>
      <span class="itpe-badge">실험 유발</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>컴퓨팅 장애: 프로세스 Kill, CPU 스로틀링, 메모리 릭</li>
        <li>네트워크 장애: 패킷 드롭, 지연시간 추가, DNS 확인 실패</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 폭발 반경 제어기</strong></span>
      <span class="itpe-badge">안전 격리</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>전체 시스템이 아닌 단일 네임스페이스나 특정 카나리 파드에 한정</li>
        <li>테스트용 모의 사용자(Synthetic User) 트래픽 대상 실험</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 비상 정지 (Emergency Stop)</strong></span>
      <span class="itpe-badge">자동 원복</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>SLA/SLO 허용 오차를 벗어나는 즉시 장애 주입 프로세스 강제 종료</li>
        <li>원래 정상 상태 인프라 구성으로 자동 복구(Auto-Rollback)</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 캐시 인스턴스 강제 종료 시 백엔드 DB로 대량 조회가 직격하여 쇼핑몰 전체가 마비되는 연쇄 장애 발생 | 서킷 브레이커(Resilience4j) 오픈 및 로컬 메모리 폴백(Fallback) 캐시 자동 반환 사전 구성 | 캐시 급사 시에도 백엔드 DB 장애 전파 100% 차단 |
| 카오스 장애 주입이 통제 범위를 벗어나 실제 VIP 고객들의 결제 요청에 오류 발생 | 카나리 배포 환경 및 모의 트래픽으로 폭발 반경 격리, 임계 에러율 초과 시 자동 중단 스위치 연동 | 프로덕션 비즈니스 피해 제로화 |
| 단위 테스트 및 모니터링 체계가 미흡한 상태에서 운영 카오스 테스트를 강행하다가 대형 참사 발생 | 단계적 카오스 성숙도 모델(스테이징 검증 $\rightarrow$ CI/CD 카오스 게이트 $\rightarrow$ 운영 카오스) 정립 | 시스템 성숙도 기반의 안전한 카오스 도입 |

## 4. 기술사 답안 차별화 포인트

### 쿠버네티스 네이티브 카오스(Litmus, Chaos Mesh)와 GitOps 결합

현대 클라우드 환경에서는 카오스 실험을 수작업으로 돌리지 않는다. **LitmusChaos나 Chaos Mesh**는 카오스 실험을 쿠버네티스 CRD(Custom Resource Definition)로 선언한다. 이를 통해 **"카오스 실험 자체를 코드로 관리(Chaos-as-Code)"**하고, ArgoCD와 연계하여 매주 무작위 시간에 프로덕션 클러스터의 복원력을 지속적으로 검증하는 **GitOps 기반 카오스 자동화 파이프라인**을 답안의 차별화로 제시한다.

### 금융권 DORA(디지털 운영 탄력성) 및 전산사고 규제 대응

금융보안원 및 유럽 DORA(Digital Operational Resilience Act) 규정에 따라, 금융기관의 IT 시스템은 정기적인 위협 기반 침투 시험과 운영 탄력성 입증이 법제화되고 있다. 카오스 엔지니어링은 단순 개발 기법을 넘어 **"금융 IT 거버넌스 규제 준수와 재해 복구(DR) 실효성을 입증하는 핵심 감사 증적"**임을 결론으로 강조한다.

## 5. 결론 및 종합 제언

### 학습자 통찰 메모 — 답안 밖

[핵심 통찰]
카오스 엔지니어링은 '무책임하게 운영 서버를 부수는 파괴 행위'가 아니다. **"결함은 필연적이므로, 예상치 못한 새벽에 시스템이 무너지기 전에 엔지니어가 준비된 대낮에 통제된 장애를 먼저 일으켜 자가 치유력을 검증하는 고도의 신뢰성 과학"**이다.

나라면:
본 시험에서 카오스 테스트가 출제되면, 정상상태-가설-주입-검증의 4단계 프레임워크와 폭발 반경(Blast Radius) 통제 원칙을 명시한 뒤 **(1) K8s CRD 기반 Chaos-as-Code(Litmus/Chaos Mesh)와 GitOps 연동, (2) 서킷 브레이커(Resilience4j)와 폴백 캐시를 통한 연쇄 장애 전파 차단, (3) 금융권 DORA 규제 준수 및 DR 실효성 감사 증적 확보**를 3단락에 명쾌하게 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 마이크로서비스 인프라에서 단일 파드/노드 장애 발생 시 정상 상태 비즈니스 처리율 99.9% 유지
- **대응 방안**: LitmusChaos 기반의 주기적 카오스 실험을 카나리 네임스페이스에 선제 적용하고 비상 정지 연동
- **검증 체계**: 서킷 브레이커 오픈 시 폴백 로직 정상 작동 여부 및 Prometheus 가용성 지표 실시간 검증
- **기대 효과**: 미지의 분산 시스템 결함 사전 색출 및 대규모 운영 장애 사고 예방, 디지털 운영 복원력(DORA) 완벽 입증

<div class="itpe-pipeline-container" role="region" aria-label="카오스 엔지니어링 기반 디지털 복원력 검증 파이프라인">
  <div class="itpe-pipeline-header">
    <span class="itpe-pipeline-title">카오스 엔지니어링 기반 디지털 복원력 검증 파이프라인</span>
    <span class="itpe-pipeline-badge">회복 탄력성</span>
  </div>
  <div class="itpe-pipeline-grid">
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">1단계: 기준선 정의</div>
      <div class="itpe-card-title">Steady State</div>
      <div class="itpe-card-body">비즈니스 정상 가동을 입증하는 핵심 트랜잭션 지표(TPS, 성공률) 확정</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">2단계: 선언적 실험</div>
      <div class="itpe-card-title">Chaos-as-Code</div>
      <div class="itpe-card-body">K8s CRD 기반 결함 시나리오 작성 및 최소 폭발 반경 카나리 격리</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">3단계: 결함 주입</div>
      <div class="itpe-card-title">통제된 장애 유발</div>
      <div class="itpe-card-body">Chaos Mesh 기반 파드 삭제 및 네트워크 레이턴시 주입 후 자가치유 관측</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">4단계: 규제 대응</div>
      <div class="itpe-card-title">DORA 탄력성 입증</div>
      <div class="itpe-card-body">복원력 성적서 자동 발행 및 시스템 취약점 조기 개선 사이클 완결</div>
    </div>
  </div>
</div>

## 6. 참고 및 연계 학습

- [마이크로서비스 아키텍처(MSA)](./035_msa.md)
- [서비스 메시(Service Mesh)](./088_service_mesh.md)
- [성능 요구사항(Performance Requirement)](./149_performance_requirement.md)
- [성능 테스트(Performance Test)](./191_performance_test.md)
