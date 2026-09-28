---
title: "웹 서버 보안"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "153. 웹 서버 보안"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 정보보안 → 애플리케이션 보안 → **웹 서버**

## 30초 인출

- **본질:** 웹 서버 소프트웨어(Nginx, Apache)의 기본 설정 결함을 제거하고 프로세스 권한 최소화, 파일 업로드 격리, TLS 암호화 및 보안 헤더를 강제하는 인프라 하드닝 체계
- **메커니즘:** 디렉터리 리스팅 차단 및 배너 은닉 $\rightarrow$ 허용 HTTP 메서드 제한 $\rightarrow$ 업로드 경로 실행 권한 박탈 $\rightarrow$ CSP/HSTS 보안 헤더 주입
- **통찰:** 웹셸 업로드 우회는 웹 루트 외부 분리 및 noexec 마운트로 원천 차단하고 서버별 수동 설정 드리프트는 IaC 기반 형상 감사로 해결 필수

<details>
<summary>핵심 용어</summary>

- **Web Server Hardening** : 웹 서버의 불필요한 모듈과 권한을 제거하고 안전한 설정 기준을 적용하는 보안 강화 작업.
- **Directory Listing** : 인덱스 파일(index.html)이 없을 때 디렉터리 내 전체 파일 목록이 브라우저에 노출되는 취약점.
- **Webshell (웹셸)** : 웹 서버에 업로드되어 공격자가 원격에서 시스템 명령을 실행할 수 있도록 지원하는 악성 스크립트.
- **CSP (Content Security Policy)** : 브라우저가 신뢰할 수 있는 스크립트 및 리소스 출처만 로드하도록 강제하는 HTTP 보안 헤더.

</details>

## 2~4교시 예상문제 (25점)

> 웹 서버(Apache, Nginx)의 주요 보안 취약점(디렉터리 리스팅, 웹셸 업로드, 정보 노출)을 설명하고, 프로세스 권한, 파일 시스템, HTTP 요청 통제 및 핵심 보안 헤더를 포함한 엔지니어링 하드닝 방안을 제시하시오. (예상·25점)

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 외부 인터넷에 직접 노출되는 웹 서버 소프트웨어(Nginx, Apache HTTP Server 등)의 프로세스 실행 권한, 파일 접근 제어, 네트워크 포트 및 프로토콜 설정을 최적화하여 침해 사고를 방어하는 인프라 보안 통제 체계 |
| 목적 | 웹 서버 결함을 악용한 루트 권한 획득, 웹셸(Webshell)을 통한 백도어 구축, 민감 설정 파일(DB 패스워드, 백업 파일) 유출 및 서비스 장애 예방 |

- 웹 애플리케이션 레벨의 시큐어 코딩과 더불어, 외부 공격자가 최초로 마주하는 네트워크 접점인 웹 서버 인프라 자체의 공격 표면을 극소화하는 필수 통제선

## Ⅱ. 웹 서버 보안 하드닝의 핵심 기술적 특성

| 특성 항목 | 세부 내용 및 기술적 의미 | 엔지니어링 구현 가치 |
|---|---|---|
| 최소 권한 프로세스 격리 | 웹 서버 데몬을 root가 아닌 권한이 극도로 제한된 전용 서비스 계정(`www-data`, `nginx`)으로 구동 | 웹 침해 발생 시 OS 루트 권한 탈취 및 횡적 이동 차단 |
| 공격 표면 및 정보 노출 최소화 | 불필요한 HTTP 메서드(PUT, DELETE, TRACE) 차단 및 서버 버전 배너 은닉 | 정찰 단계의 취약 버전 타깃 공격 및 정보 수집 무력화 |
| 파일 시스템 샌드박스 격리 | 정적 웹 자원, 업로드 디렉터리, 로그 저장소의 권한 및 마운트 속성을 엄격 분리 | 웹셸 파일이 업로드되더라도 런타임 실행 권한 박탈 |
| 브라우저 사이드 보안 강제 | HTTP 응답 헤더(HSTS, CSP, X-Frame-Options)를 서버 단에서 강제 주입 | 클라이언트 웹 브라우저의 XSS, 클릭재킹, 다운그레이드 방어 |

- CIS Benchmarks 표준 가이드라인에 기반하여 코드형 인프라(IaC)로 일관된 보안 설정을 배포·감사할 수 있는 재현성 특성 보유

## Ⅲ. 웹 서버 계층별 보안 하드닝 아키텍처 및 통제 프로세스

```text
[웹 서버 엔드투엔드 보안 하드닝 및 업로드 격리 아키텍처]

  [외부 사용자 브라우저]
            │
            ▼ (HTTPS 요청: TLS 1.3 강제)
 ┌─────────────────────────────────────────────────────────────┐
 │  1. 네트워크 및 통신 계층 (Network & Transport Layer)       │
 │   - TLS 1.3 / 안전한 암호 스위트 적용                      │
 │   - HTTP 요청 메서드 제한 (GET, POST, HEAD만 허용)          │
 │   - 서버 배너 은닉 (ServerTokens Prod / server_tokens off)   │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────┴──────────────────────────────┐
 │  2. 프로세스 및 접근통제 계층 (Process & Access Control)    │
 │   - 최소 권한 비특권 서비스 계정 (User www-data, Group www) │
 │   - 디렉터리 리스팅 원천 차단 (Options -Indexes)            │
 │   - 관리자 페이지 접근 IP 화이트리스트 (Allow/Deny 통제)    │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────┴──────────────────────────────┐
 │  3. 파일 시스템 및 스토리지 계층 (Storage & Upload Isolation)│
 │   - 웹 루트(DocumentRoot) 읽기 전용 권한 설정 (chmod 555)   │
 │   - 업로드 디렉터리 실행 권한 전면 제거 (noexec 마운트)      │
 │   - 파일 저장 시 난수 파일명 치환 및 S3 오브젝트 스토리지 격리│
 └──────────────────────────────┬──────────────────────────────┘
                                │
                                ▼ (응답 패킷 전송)
 ┌─────────────────────────────────────────────────────────────┐
 │  4. 응답 헤더 강화 계층 (HTTP Response Headers)             │
 │   - Strict-Transport-Security: max-age=31536000; includeSubDomains │
 │   - Content-Security-Policy / X-Content-Type-Options: nosniff│
 └─────────────────────────────────────────────────────────────┘
```

| 하드닝 영역 | Apache HTTP Server 설정 지시어 | Nginx 설정 지시어 | 통제 효과 |
|---|---|---|---|
| 배너 정보 은닉 | `ServerTokens Prod`<br>`ServerSignature Off` | `server_tokens off;` | 웹 서버 종류 및 상세 버전 정보 유출 차단 |
| 디렉터리 리스팅 차단 | `Options -Indexes` | `autoindex off;` | 인덱스 파일 부재 시 디렉터리 내부 파일 노출 차단 |
| 불필요 메서드 차단 | `<LimitExcept GET POST HEAD>`<br>`Deny from all` | `if ($request_method !~ ^(GET\|POST\|HEAD)$) { return 405; }` | PUT, DELETE, TRACE를 악용한 임의 파일 수정 차단 |
| 파일 업로드 실행 차단 | `<Directory "/uploads">`<br>`php_flag engine off` | `location /uploads/ {`<br>`location ~ \.php$ { deny all; } }` | 업로드된 웹셸 스크립트 실행 원천 봉쇄 |

## Ⅳ. 핵심 HTTP 보안 응답 헤더 비교 분석

| 보안 응답 헤더 | 핵심 방어 위협 | 표준 권고 설정값 | 동작 메커니즘 |
|---|---|---|---|
| Strict-Transport-Security (HSTS) | SSL Stripping, 중간자 감청 | `max-age=31536000; includeSubDomains; preload` | 브라우저가 평문 HTTP 접속 시도시 즉시 HTTPS로 강제 전환 |
| Content-Security-Policy (CSP) | Cross-Site Scripting (XSS), 데이터 주입 | `default-src 'self'; script-src 'self' 'nonce-...';` | 브라우저가 허용된 출처 외의 외부 악성 스크립트 실행 거부 |
| X-Frame-Options | 클릭재킹 (Clickjacking) | `DENY` 또는 `SAMEORIGIN` | 타 사이트의 `<iframe>` 내에 본 사이트 프레임 렌더링 차단 |
| X-Content-Type-Options | MIME 스니핑 공격 | `nosniff` | 브라우저가 Content-Type을 무시하고 파일 내용을 임의 해석 방지 |
| Referrer-Policy | URL 파라미터 내 민감정보 유출 | `strict-origin-when-cross-origin` | 외부 사이트 이동 시 상세 경로 노출을 차단하고 도메인만 전달 |

## Ⅴ. 웹 서버 운영 시 엔지니어링 한계와 해결 방안

| 한계 | 방안 |
|---|---|
| 파일 확장자 필터링 우회(대소문자 혼합 `.pHP`, 널바이트 `%00`, 다중 확장자 `.php.jpg`)를 통해 웹 루트 내에 웹셸이 업로드되어 RCE 발생 | 업로드 파일을 웹 루트 디렉터리와 완전히 분리된 외부 전용 스토리지(AWS S3, NAS)에 저장하고, 파일 시스템 마운트 시 `noexec, nosuid` 옵션을 적용하며, 원본 확장자를 제거하고 서버 측 무작위 UUID 파일명으로 강제 치환 |
| 관리자가 운영 편의를 위해 프로덕션 서버에 직접 접속하여 설정을 수동 변경함으로써 발생하는 서버 간 설정 불일치(Configuration Drift) | 모든 웹 서버 설정을 Git 레포지토리와 Ansible/Terraform 코드로 단일화하고, CI/CD 배포 시 CIS Benchmark 자동화 스캐너(OpenSCAP, Trivy)를 연동하여 미준수 설정 시 자동 배포 중단 |
| 복잡한 모던 웹 애플리케이션에서 CSP 헤더 적용 시 레거시 인라인 스크립트와 충돌하여 정상 기능이 마비되거나 `'unsafe-inline'` 남용 발생 | 세션마다 고유하게 생성되는 암호학적 논스(Nonce) 기반 CSP(`script-src 'nonce-{random}'`)를 적용하고, 초기 전환 시 `Content-Security-Policy-Report-Only` 모드로 정책 위반 로그를 수집·튜닝 후 점진적 차단 전환 |
| 대규모 트래픽 환경에서 웹 서버 로깅(Access Log)으로 인한 디스크 I/O 병목 및 디스크 풀(Full) 장애 발생 | 로컬 파일 직접 쓰기를 최소화하고, Fluentbit/Logstash 기반의 비동기 버퍼링 전송을 적용하여 중앙 로그 저장소(Elasticsearch/S3)로 오프로딩하며 로그 로테이션(Logrotate) 자동화 |

## Ⅵ. 웹 서버 제로 트러스트 하드닝 아키텍처 제언

```text
[웹 서버 제로 트러스트 및 불변 인프라(Immutable Infrastructure) 아키텍처]

 ┌─────────────────────────────────────────────────────────────┐
 │                 1. 불변 컨테이너 인프라 계층                │
 │   - 웹 서버 루트 파일시스템 읽기 전용(read-only-rootfs) 마운트│
 │   - 임시 쓰기 영역은 tmpfs(메모리) 격리 (파일 영구 저장 불가)│
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────┴──────────────────────────────┐
 │              2. 인라인 리버스 프록시 계층 (Reverse Proxy)    │
 │   - TLS 1.3 종단 및 HTTP/2, HTTP/3 고속 전송 처리          │
 │   - HSTS Preload, 엄격한 CSP, nosniff 보안 헤더 자동 주입   │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────┴──────────────────────────────┐
 │                 3. 스토리지 및 자산 분리 계층                │
 │   - 사용자 업로드 파일은 웹 서버 외부 S3 오브젝트 저장소 격리 │
 │   - WAF 연계 악성 요청(LFI, RFI, Path Traversal) 실시간 차단│
 └─────────────────────────────────────────────────────────────┘
```

| 관리 영역 | 핵심 엔지니어링 세부 과제 | 통제 목표치 |
|---|---|---|
| 설정 컴플라이언스 | CIS Apache / Nginx Benchmark 자동 진단 통과 | 벤치마크 준수율 > 98% 달성 |
| 웹셸 실행 차단 | 업로드 디렉터리 실행 권한 제거 및 오브젝트 스토리지 격리 | 업로드 파일에 의한 RCE 사고 0건 |
| 보안 헤더 적용 | 사내 전 대외 공개 웹 서버의 5대 필수 보안 헤더 적용 | 보안 헤더 평가 등급 A+ 획득 |

## 출제 이력과 검증 출처

- 제124회 정보관리기술사 예상 연계 주제: 웹 서버(Apache/Nginx) 보안 하드닝 및 보안 헤더 설정
- CIS (Center for Internet Security): CIS Apache HTTP Server Benchmark & CIS Nginx Benchmark
- OWASP Cheat Sheet Series: Web Server Security Cheat Sheet
- OWASP Cheat Sheet Series: HTTP Security Response Headers Cheat Sheet
- Mozilla Foundation: Mozilla Web Security Guidelines (Server Side TLS & Headers)
