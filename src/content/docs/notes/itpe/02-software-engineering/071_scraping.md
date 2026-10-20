---
title: "스크래핑(Scraping)"
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

- 스크래핑(Scraping), 크롤링(Crawling), 헤드리스 브라우저(Headless Browser)
- HTML 파싱, DOM(Document Object Model), CSS 선택자
- Open API, robots.txt, 부정경쟁방지법, 레이트 리미팅(Rate Limiting)

## Ⅰ. 스크래핑의 개요

- 핵심 요약 : 웹 문서·앱 화면으로부터 특정 데이터를 프로그래밍 방식으로 자동 추출·가공하는 기술.
- 개념 : 웹 사이트의 HTML(HyperText Markup Language) 문서나 모바일 앱의 뷰 화면으로부터 필요한 특정 데이터(텍스트, 가격 정보, 이미지 등)를 프로그래밍 도구를 활용하여 자동으로 추출하고 가공하는 기술.
- 배경 및 필요성 : 공식 Open API(Application Programming Interface)를 제공하지 않는 웹 서비스로부터의 데이터 수집 필요, 가격 비교·마이데이터 서비스·금융 스크린 스크래핑·시장 동향 분석 활용.
- 주요 목적 : 비정형 웹 문서의 정형 데이터 전환과 수집 자동화를 통한 분석·서비스 데이터 파이프라인 구축.

## Ⅱ. 스크래핑의 특징

- 핵심 요약 : 요청·파싱·렌더링의 3대 기술 요소와 크롤링과의 범위 차이, 법적 제약 수반.
1. HTTP(Hypertext Transfer Protocol) 클라이언트 : Requests, Axios 등의 문서 요청 기반.
2. HTML 파서 : BeautifulSoup, Cheerio 등의 DOM(Document Object Model) 탐색·핵심 필드 추출.
3. 헤드리스 브라우저 : Puppeteer, Playwright, Selenium 등의 자바스크립트 렌더링·사용자 인터랙션 재현.
4. 크롤링(Crawling)과의 구별 : 특정 페이지 타깃 데이터의 핀포인트 추출 vs 하이퍼링크 순회 대량 수집.
5. 법적·윤리적 제약 수반 : robots.txt 규약, 저작권, 부정경쟁방지법 등의 준수 요구.

## Ⅲ. 스크래핑의 구조 (흐름)

- 핵심 요약 : URL 요청부터 정형 데이터 저장까지의 4단계 파이프라인과 수집 방식 선택 절차.

```text
[ 스크래핑 동작 프로세스 ]
[ 타겟 URL 요청 ]
 - HTTP GET / 헤드리스 브라우저 조작
   ↓
[ HTML 소스 획득 ]
 - 동적 렌더링 콘텐츠 대기
   ↓
[ DOM 파싱 및 탐색 ]
 - XPath(XML Path Language), CSS Selector,
   핵심 필드 추출
   ↓
[ 정형 데이터 저장 ]
 - RDB, NoSQL, CSV 정제 및 적재
```

```text
[ 데이터 수집 방식 선택 흐름 ]
공식 Open API 제공? ── 예 ──> API 연동
   ↓ 아니오
robots.txt 허용 범위 확인
   ↓
서버 부하 배려(레이트 리미팅)
   ↓
법적 검토(저작권·부정경쟁방지법)
   ↓
스크래핑 수행
```

- 스크래핑(Scraping) : 특정 웹 페이지 내 원하는 타깃 데이터(상품 가격, 리뷰 등)만을 정밀하게 핀포인트로 추출하는 작업.
- 크롤링(Crawling) : 하이퍼링크를 따라 웹 전체를 탐색하며 대량의 웹 페이지를 인덱싱·수집하는 광범위 작업(검색 엔진 봇의 역할).

## Ⅳ. 스크래핑 방식별 비교

- 핵심 요약 : 처리 속도·동적 콘텐츠 대응·안정성의 축에서 3가지 방식의 트레이드오프.

| 스크래핑 방식 | 장점 | 단점 | 대표 도구 |
|---|---|---|---|
| 정적 HTML 파싱 | 초고속 처리, 메모리·CPU(Central Processing Unit) 자원 소비 극소 | 자바스크립트 렌더링 SPA(Single Page Application) 데이터 수집 불가 | BeautifulSoup, Scrapy, Cheerio |
| 헤드리스 브라우저 조작 | 사용자 인터랙션(클릭, 스크롤, 로그인) 재현 가능 | 무거운 브라우저 렌더링 기인 저속·고자원 소모 | Puppeteer, Playwright, Selenium |
| 비공식 백엔드 API 후킹 | 가공되지 않은 순수 JSON(JavaScript Object Notation) 데이터의 직접 고속 수집 | API 스펙 변경 시 즉각 오작동, 인증 토큰 만료 위험 | 네트워크 패킷 분석(DevTools, Charles) |

- 법적·윤리적 리스크
  1. robots.txt 규약 준수 : 검색 봇·스크래핑의 접근 허용·거부 범위 명시.
  2. 부정경쟁방지법·정보통신망법 위반 위험 : 경쟁사의 상당한 투자로 구축된 데이터 무단 복제, 서버 과부하 유발 시 업무방해죄 성립 가능.
  3. 마이데이터(MyData) 스크린 스크래핑 금지 : 금융 분야에서 보안 취약 스크린 스크래핑의 표준 API 방식 전환 완료.

## Ⅴ. 스크래핑의 장점과 한계

- 핵심 요약 : Open API 부재 환경의 데이터 확보 수단이자 파서 파손·자원 고갈·법적 리스크의 보유.
- 장점
  1. 공식 API 미제공 서비스의 데이터 확보 수단 제공.
  2. 가격 비교·시장 동향 분석 등 데이터 기반 서비스의 기반.
  3. 수집 자동화를 통한 반복 작업 비용 절감.
- 한계점 1 : 웹 UI(User Interface) 잦은 변경에 따른 파서 파손(Parser Fragility)
  - 한계점 : 대상 웹 사이트의 HTML 태그, CSS(Cascading Style Sheets) 클래스명, DOM(Document Object Model) 계층 구조 변경 시 하드코딩된 선택자(Selector)의 즉시 무효화, 파이프라인 정지.
  - 해결 방안 : 시맨틱 태그·텍스트 앵커 기반 유연한 파싱 로직 적용, LLM(Large Language Model) 기반 지능형 자가 치유 파서(Self-Healing Parser) 도입으로 DOM 변동 자동 대응.
- 한계점 2 : 헤드리스 브라우저 자원 고갈 및 WAF(Web Application Firewall) 차단
  - 한계점 : SPA 렌더링용 Puppeteer·Playwright 실행 시 인스턴스당 메모리 점유율 급증, Cloudflare·Akamai 등 WAF 봇 탐지 솔루션의 IP(Internet Protocol) 차단 발생.
  - 해결 방안 : 헤드리스 브라우저 풀링(Resource Pooling)·경량 브라우저 컨테이너화, 주거용 프록시 풀(Residential Proxy Pool)·지능형 핑거프린트 우회 기술 적용.
- 한계점 3 : 비공식 수집 기인 법적 리스크 및 데이터 무결성 결여
  - 한계점 : robots.txt 무시, 저작권 침해, 부정경쟁방지법 위반 등 법적 분쟁 리스크와 실시간 데이터 검증 체계 부재 기인 결측치 발생.
  - 해결 방안 : 준법성 검토 프로세스 제도화, 정식 비즈니스 협약 기반 공식 Open API 및 CDC(Change Data Capture) 기반 데이터 수집 파이프라인 전환.

## Ⅵ. 지속 가능한 데이터 파이프라인 구축을 위한 기술사적 제언

- 핵심 요약 : 공식 표준 API 우선(API-First) 전환과 상대 서버 보호형 윤리적 수집 원칙.
- 스크래핑에서 공식 표준 API 우선(API-First)으로의 전환 : 상대 서버의 UI 변경 시 파싱 에러가 발생하는 스크래핑의 취약성 극복과 법적 분쟁 방지를 위한 정식 비즈니스 협약 기반 API 연동 우선 추진.
- 상대 서버 보호를 위한 레이트 리미팅(Rate Limiting) 준수 : 무분별한 멀티스레드 병렬 요청의 대상 서버 장애 유발 방지, 요청 간 임의의 지연 시간(Backoff Delay) 부여와 비피크 시간대 배치 분산 수행 등 윤리적 스크래핑 원칙 준수.

## Ⅶ. 결론

- 핵심 요약 : 스크래핑은 API 공백의 데이터 수집 수단이지만, 법적 준수와 서버 배려가 지속 가능성의 전제 조건.
- 요약 : 요청→파싱→저장 파이프라인과 방식별 트레이드오프에 근거한 상황별 수집 방식 선택 필요.
- 시사점 : API-First 전환과 레이트 리미팅·준법 검토 체계화로 기술적·법적 리스크의 동시 통제 필요.
