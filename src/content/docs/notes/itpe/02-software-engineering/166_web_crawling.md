---
title: "웹 크롤링(Web Crawling)"
author: "agnusdei1207"
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

## 연관 키워드

- 웹 크롤링(Web Crawling), URL(Uniform Resource Locator) 프론티어(URL Frontier), robots.txt
- 크롤링 예의 정책(Politeness Policy), 중복 제거(블룸 필터, SimHash), URL 정규화(Canonicalization), 적응형 백오프(Adaptive Backoff)

## Ⅰ. 웹 크롤링의 개요

- 핵심 요약 : 하이퍼링크 순회를 통한 웹 문서의 대규모 자동 수집 기술로 검색 색인과 AI 학습 데이터 확보의 기반.
- 개념 : 웹 크롤링(Web Crawling)이란 인터넷 상에 공개된 방대한 웹 페이지들을 하이퍼링크를 따라 순회하면서, 웹 문서(HTML(HyperText Markup Language), PDF(Portable Document Format) 등)를 자동으로 탐색하고 대규모로 수집하여 검색 엔진의 색인(Index) 데이터베이스나 AI(Artificial Intelligence) 학습용 빅데이터 코퍼스를 구축하는 분산 자동화 소프트웨어 기술.
- 배경 및 필요성 : 웹의 기하급수적 팽창 속에서 사용자가 원하는 정보의 실시간 검색을 위한 사전 웹 문서 인덱싱, 초거대 언어 모델(LLM, Large Language Model)의 사전 학습(Pre-training) 데이터 확보 필요.
- 주요 목적 : URL(Uniform Resource Locator) 프론티어(URL Frontier), 웹 다운로더(Web Downloader), 콘텐츠 파서(Parser), 중복 제거기(Duplicate Eliminator)로 구성되는 수집 체계를 통한 고품질 웹 코퍼스 구축.

## Ⅱ. 웹 크롤링의 특징

- 핵심 요약 : 링크 기반 자율 순회, 예의 정책 준수, 대규모 중복 통제가 결합된 분산 수집 체계.

1. 시드(Seed) URL로부터 링크를 따라 이동하는 그래프 순회(Graph Traversal) 방식.
2. 동일 호스트 과부하 방지의 도메인별 지연을 강제하는 크롤링 예의 정책(Politeness Policy).
3. robots.txt 규약 기반의 수집 허용 범위 준수.
4. 블룸 필터(Bloom Filter)·SimHash 기반의 초대규모 중복 검출.
5. 분산 다운로더 워커 풀(Worker Pool)을 통한 병렬 수집 확장성.
6. URL 정규화(Canonicalization)를 통한 중복 URL의 통합 관리.

## Ⅲ. 웹 크롤링의 구조 (흐름)

- 핵심 요약 : 프론티어 큐에서 다운로더·파서·중복 검출로 이어지는 순환 피드백 구조의 분산 크롤링 파이프라인.
- 분산 웹 크롤러의 동작 아키텍처.

```text
[ 시드 URL (Seed URLs) ]
    │
    ▼
[ URL 프론티어 (URL Frontier) ]
  - 우선순위 큐 및 예의 큐
    (Politeness Queue)
    │
    ▼
[ robots.txt 파서 ]
  - 수집 허용 여부 판별
    │
    ▼
[ 분산 다운로더 워커 ]
  - Downloader Worker Pool
  - 비동기 HTTP(Hypertext Transfer
    Protocol) 요청, DNS(Domain Name
    System) 캐싱, 압축 해제
    │ (HTML 본문 전송)
    ▼
[ 콘텐츠 처리 및 중복 검출 ]
  - SimHash / Bloom Filter
  - 신규 링크 추출 (Link Extractor)
    │ (신규 URL 재입력)
    ▼
[ URL 프론티어 순환 피드백 ]
  -> 문서 스토리지 / 인덱서 저장
```

- URL 프론티어(URL Frontier) : 앞으로 방문할 URL의 보관 우선순위 큐로, 서버 과부하 방지의 예의(Politeness) 큐와 중요 페이지 우선 방문의 우선순위(Priority) 큐로 구성.
- 크롤링 예의 정책(Politeness Policy) : 동일 호스트(도메인)에 대한 과도한 동시 요청 방지를 위한 도메인별 딜레이(예: 1~2초) 강제.

## Ⅳ. 웹 크롤링과 웹 스크래핑의 비교

- 핵심 요약 : 웹 전역의 그래프 순회 수집과 특정 페이지의 타깃 데이터 추출 간의 목적·범위 차이.
- 탐색 방식의 구조 대조.

```text
[ 웹 크롤링 : 링크 순회 확산 ]
  사이트A ──링크──> 사이트B ──링크──> 사이트C
     │                                  │
     └──────────링크──> 사이트D <───────┘

[ 웹 스크래핑 : 타깃 목록 순차 방문 ]
  URL 목록 [P1, P2, P3] ──> 지정 페이지 파싱
```

| 비교 항목 | 웹 크롤링 (Web Crawling) | 웹 스크래핑 (Web Scraping) |
|---|---|---|
| 수집 목적 | 웹 전체의 탐색, 링크 추적 및 검색 인덱싱 | 특정 웹 페이지 내 타깃 데이터 핀포인트 추출 |
| 수집 범위 | 인터넷 전역의 무한한 웹 페이지 (대규모) | 사전 정의된 특정 사이트의 상세 페이지군 |
| 탐색 방식 | 링크를 따라 자율 이동 (Graph Traversal) | 지정된 URL 목록의 타깃 순차 방문 |
| 중복 통제 | 수십억 개 URL 및 콘텐츠 중복 검출 필수 | 특정 식별자(상품 ID(Identifier) 등) 기반 단순 검증 |
| 대표 솔루션 | Apache Nutch, Scrapy, Googlebot | BeautifulSoup, Playwright, Puppeteer |

## Ⅴ. 웹 크롤링의 장점과 한계

- 핵심 요약 : 대규모 데이터 확보의 장점, 스파이더 트랩·서버 부하·데이터 품질 측면의 한계.
- 장점
  1. 검색 색인과 LLM 사전 학습용 대규모 코퍼스의 자동·지속 확보.
  2. 분산 아키텍처를 통한 수집 규모의 수평 확장.
  3. 링크 구조 분석을 통한 웹 그래프·페이지랭크(PageRank) 기반 품질 평가 기반 제공.
- 한계점 1 : 무한 루프(Spider Trap) 및 동적 URL 생성에 따른 크롤러 자원 고갈
  - 한계점 : 캘린더 링크, 세션 ID 파라미터, 동적 필터 URL로 인한 끝없는 중복 페이지 탐색 루프와 메모리·스토리지 낭비.
  - 해결 방안 : URL 정규화(Canonicalization) 엔진 적용, 블룸 필터(Bloom Filter) 기반 기방문 URL 초고속 판별, 최대 탐색 깊이(Max Depth) 제한 정책 강제.
- 한계점 2 : 대상 웹 서버의 과부하 유발 및 WAF(Web Application Firewall)·안티봇 차단
  - 한계점 : 무분별한 병렬 크롤링 요청의 상대 서버 DoS(Denial of Service) 장애 유발, IP(Internet Protocol) 대역 차단 및 Captcha 검증 직면.
  - 해결 방안 : robots.txt 엄격 준수, 도메인별 예의 지연(Politeness Delay)과 적응형 레이트 리미팅, 분산 프록시 풀 및 헤더 로테이션 기법 적용.
- 한계점 3 : 수집 비정형 데이터의 품질 정제 및 중복 제거 난제
  - 한계점 : HTML 광고, 내비게이션 바 등 보일러플레이트(Boilerplate) 노이즈와 유사 중복 콘텐츠의 대량 적재에 따른 후속 분석 모델 오염.
  - 해결 방안 : 텍스트 추출 전용 보일러플레이트 제거 알고리즘(Boilerpipe) 적용, SimHash/MinHash 기반 근사 중복 문서(Near-Duplicate) 고속 필터링 체계 구축.

## Ⅵ. 대규모 분산 크롤러 구축을 위한 기술사적 제언

- 핵심 요약 : 블룸 필터·SimHash 중복 제거 체계와 robots.txt 준수·적응형 백오프의 의무화.
- 블룸 필터(Bloom Filter)와 쉼해시(SimHash) 활용 대규모 중복 제거 : 수억 개 URL 방문 이력의 전량 메모리 저장 불가를 감안하여, 공간 효율이 극도로 우수한 블룸 필터(미세한 오탐(False Positive) 허용) 기반 URL 중복 판별과 SimHash 기반 문서 간 유사도 판별을 통한 중복 문서 수집 낭비 차단.
- robots.txt 규약 준수 및 적응형 백오프(Adaptive Backoff) 필수화 : 대상 서버 가용성 훼손형 크롤링의 업무방해죄 및 DoS 공격 간주 위험을 감안하여, robots.txt의 전면 준수와 HTTP(Hypertext Transfer Protocol) 429 Too Many Requests 감지 시 수집 주기 자동 조절의 적응형 백오프 알고리즘 구현.

## Ⅶ. 결론

- 핵심 요약 : 웹 크롤링은 검색·AI 시대의 데이터 확보 인프라이자 예의·품질 관리가 전제되는 기술.
- 요약 : 프론티어·다운로더·파서·중복 제거기의 순환 구조를 통한 웹 전역 문서의 대규모 수집 실현.
- 시사점 : robots.txt 준수와 서버 예절, 중복·노이즈 통제가 법적·기술적 리스크 관리의 필수 전제.
