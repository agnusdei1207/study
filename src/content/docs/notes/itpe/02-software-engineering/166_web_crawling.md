---
title: "웹 크롤링(Web Crawling)"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 웹 크롤링의 개요

- 개념 : **웹 크롤링** 이란 인터넷 상에 공개된 방대한 웹 페이지들을 하이퍼링크를 따라 순회하면서, 웹 문서(HTML(HyperText Markup Language), PDF(Portable Document Format) 등)를 자동으로 탐색하고 대규모로 수집하여 검색 엔진의 색인(Index) 데이터베이스나 AI(Artificial Intelligence) 학습용 빅데이터 코퍼스를 구축하는 분산 자동화 소프트웨어 기술.
- 배경 및 필요성 : 웹의 기하급수적 팽창 속에서 사용자가 원하는 정보를 실시간 검색할 수 있도록 사전에 웹 문서를 인덱싱하거나, 초거대 언어 모델(LLM, Large Language Model)의 사전 학습(Pre-training) 데이터를 확보하기 위해 필수적.
- 핵심 구성요소 : URL(Uniform Resource Locator) 프론티어(URL Frontier), **웹 다운로더** (Web Downloader), **콘텐츠 파서** (Parser), **중복 제거기** (Duplicate Eliminator)

## Ⅱ. 분산 웹 크롤러의 동작 아키텍처 및 순회 흐름

```text
   [ 시드 URL (Seed URLs) ] ──> [ URL 프론티어 (URL Frontier) ]
                                          │
                    ┌─────────────────────┴─────────────────────┐
                    ▼ (우선순위 및 예의 큐: Politeness Queue)    ▼
   ┌────────────────────────────────────────────────────────┐┌──────────────────────┐
   │ [ 분산 다운로더 워커 (Downloader Worker Pool) ]        ││ [ robots.txt 파서 ]  │
   │  - 비동기 HTTP 요청 (DNS 캐싱, 압축 해제)              ││ - 수집 허용 여부 판별│
   └──────────────────────────┬─────────────────────────────┘└──────────────────────┘
                              │ (HTML 본문 전송)
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │ [ 콘텐츠 처리 및 중복 검출 ]                          │
   │  - 텍스트 파싱 및 SimHash / Bloom Filter 중복 제거     │
   │  - 신규 하이퍼링크 URL 추출 (Link Extractor)          │
   └──────────┬─────────────────────────────────────────────┘
              │ (새로 발견된 URL 재입력)
              ▼
   [ URL 프론티어로 순환 피드백 ] ──> [ 문서 스토리지 / 인덱서 저장 ]
```

- **URL 프론티어** (URL Frontier) : 앞으로 방문해야 할 URL들을 보관하는 우선순위 큐로, 서버 과부하를 막는 '예의(Politeness)' 큐와 중요 페이지를 먼저 방문하는 '우선순위(Priority)' 큐로 구성.
- **크롤링 예의 정책** (Politeness Policy) : 동일한 호스트(도메인)에 대해 동시에 과도한 요청을 보내지 않도록 도메인별 딜레이(예: 1~2초)를 강제.

## Ⅲ. 웹 크롤링과 웹 스크래핑의 비교

| 비교 항목 | 웹 크롤링 (Web Crawling) | 웹 스크래핑 (Web Scraping) |
|---|---|---|
| 수집 목적 | 웹 전체의 탐색, 링크 추적 및 검색 인덱싱 | 특정 웹 페이지 내 타깃 데이터 핀포인트 추출 |
| 수집 범위 | 인터넷 전역의 무한한 웹 페이지 (대규모) | 사전에 정의된 특정 사이트의 상세 페이지군 |
| 탐색 방식 | 링크를 따라 자율적으로 이동 (Graph Traversal) | 지정된 URL 목록을 타깃하여 순차 방문 |
| 중복 통제 | 수십억 개의 URL 및 콘텐츠 중복 검출 필수 | 특정 식별자(상품 ID(Identifier) 등) 기반의 단순 검증 |
| 대표 솔루션 | Apache Nutch, Scrapy, Googlebot | BeautifulSoup, Playwright, Puppeteer |

## Ⅳ. 웹 크롤링(Web Crawling)의 주요 한계점 및 해결 방안

- 무한 루프(Spider Trap) 및 동적 URL 생성에 따른 크롤러 자원 고갈 :
  - 한계점 : 캘린더 링크, 세션 ID 파라미터, 동적 필터 URL로 인해 크롤러가 끝없는 중복 페이지 탐색 루프에 빠져 메모리와 스토리지 낭비.
  - 해결 방안 : **URL 정규화** (Canonicalization) 엔진 적용, 블룸 필터(Bloom Filter) 기반의 기방문 URL 초고속 판별 및 최대 탐색 깊이(Max Depth) 제한 정책 강제.
- 대상 웹 서버의 과부하 유발 및 WAF(Web Application Firewall)/안티봇 차단 :
  - 한계점 : 무분별한 병렬 크롤링 요청이 상대 서버의 DoS(Denial of Service) 장애를 유발하여 IP(Internet Protocol) 대역 차단 및 Captcha 검증에 직면.
  - 해결 방안 : robots.txt 엄격 준수, 도메인별 폴라이트니스 지연(Politeness Delay) 및 적응형 레이트 리미팅, 분산 프록시 풀 및 헤더 로테이션 기법 적용.
- 수집된 비정형 데이터의 품질 정제 및 중복 제거 난제 :
  - 한계점 : HTML 광고, 내비게이션 바 등 보일러플레이트 노이즈와 유사 중복 콘텐츠가 대량 적재되어 후속 분석 모델 오염.
  - 해결 방안 : 텍스트 추출 전용 보일러플레이트 제거 알고리즘(Boilerpipe) 적용, **SimHash/MinHash** 기반 근사 중복 문서(Near-Duplicate) 고속 필터링 체계 구축.

## Ⅴ. 대규모 분산 크롤러 구축을 위한 기술사적 제언

- **블룸 필터** (Bloom Filter)와 쉼해시(SimHash)를 활용한 대규모 중복 제거 : 수억 개의 URL 방문 여부를 메모리에 전부 저장할 수 없으므로 오탐(False Positive)은 미세하게 존재하나 공간 효율이 극도로 뛰어난 블룸 필터를 적용하고, 문서 간 유사도 판별에는 SimHash를 적용하여 중복 문서 수집 낭비 차단.
- **robots.txt** 규약 준수 및 적응형 백오프(Adaptive Backoff) 필수화 : 대상 서버의 가용성을 훼손하는 크롤링은 업무방해죄 및 DoS 공격으로 간주될 수 있으므로, `robots.txt` 규칙을 $100\%$ 준수하고 대상 서버의 응답 지연(HTTP 429 Too Many Requests) 감지 시 자동으로 수집 주기를 늦추는 적응형 백오프 알고리즘 구현 필수.
