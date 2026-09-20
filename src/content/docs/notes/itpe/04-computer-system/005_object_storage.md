---
title: "스토리지 유형 비교(블록·파일·오브젝트)"
author: "Codex"
date: "2026-09-20T19:47:31+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 19:47 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>컴퓨터 시스템</span><span>스토리지 아키텍처</span><strong>블록·파일·오브젝트 스토리지</strong></div>

## 큰 그림과 30초 인출

- 본질: 같은 데이터를 블록 주소, 파일 경로, 객체 Key라는 서로 다른 논리 단위와 인터페이스로 노출함
- 메커니즘: 블록은 상위 파일시스템이 의미를 부여하고, 파일은 계층 Namespace를 제공하며, 오브젝트는 Data·Metadata·ID를 API로 다룸
- 산출: DB·VM은 블록, 공유 작업은 파일, 대규모 비정형·보관은 오브젝트가 기본이며 실제 선택은 지연·공유·갱신·확장 조건으로 판정함

<div class="itpe-flow itpe-flow--vertical" aria-label="스토리지 유형별 접근 구조">
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>Block Storage</strong></span><small><b>접근:</b> Volume · LUN · Block Address</small><small><b>산출:</b> 파일시스템·DB가 해석하는 Raw Block</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↕</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>File Storage</strong></span><small><b>접근:</b> Directory Path · File Protocol</small><small><b>산출:</b> 계층형 공유 파일</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↕</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>Object Storage</strong></span><small><b>접근:</b> Bucket · Key · Object API</small><small><b>산출:</b> Data + Metadata + ID 객체</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- `LUN(Logical Unit Number)`: 호스트에 블록 장치를 식별시킴 → 파일 의미는 상위 계층이 담당
- `Namespace`: 데이터 이름과 위치를 찾는 규칙 → 블록 주소·계층 경로·Bucket/Key를 구분
- `POSIX(Portable Operating System Interface)`: 파일 접근 의미와 API의 공통 기준 → 기존 애플리케이션 호환성을 가름
- `Object API`: Key 기반 PUT·GET·DELETE 인터페이스 → 수평 확장과 객체 단위 갱신 특성을 결정
- `Erasure Coding(삭제 코딩)`: 데이터를 조각과 패리티로 분산 보호 → 용량 효율과 복구 계산 비용을 교환

</details>

## 예상문제

- 블록·파일·오브젝트 스토리지를 구조와 접근방식으로 비교하고, 데이터 생명주기 및 AI 데이터 인프라에서의 활용방안과 도입 고려사항을 설명하시오.

## Ⅰ. 접근 의미로 구분하는 스토리지 유형 개요

> 세 유형의 차이는 저장 매체가 아니라 애플리케이션에 노출하는 주소·Namespace·갱신 의미이며, 워크로드 접근 패턴이 선택 기준임.

- 정의: 데이터를 **Block Address**, **File Path**, **Object Key** 단위로 표현·접근하는 인터페이스 기반 스토리지 분류
- 목적: 지연·공유·확장·갱신 요구에 맞는 저장 의미 선택 → 성능과 운영 복잡성의 균형

| 유형 | 논리 단위 | Namespace | 대표 업무 |
|---|---|---|---|
| **블록** | 고정 크기 블록 | 호스트 파일시스템 | DB·VM 디스크 |
| **파일** | 파일·디렉터리 | 계층 경로 | 공동 작업·홈 디렉터리 |
| **오브젝트** | Data·Metadata·ID | Bucket·Key | 백업·미디어·Data Lake |

## Ⅱ. 주소·메타데이터·갱신 구조

> 블록에서 오브젝트로 갈수록 저장 서비스가 더 많은 데이터 의미를 맡지만, 세밀한 In-place Update와 POSIX 호환성은 줄어듦.

<div class="itpe-flow itpe-flow--vertical" aria-label="스토리지 접근별 처리 흐름">
  <div class="itpe-flow__node"><strong>블록 경로</strong><small><b>활동:</b> 호스트가 LUN의 Block Address 읽기·쓰기</small><small><b>산출:</b> DB·파일시스템이 관리하는 블록 상태</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>파일 경로</strong><small><b>활동:</b> 경로 탐색 · 권한 확인 · Byte Range 접근</small><small><b>산출:</b> 공유 File과 Directory Metadata</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>오브젝트 경로</strong><small><b>활동:</b> API로 Key 지정 · 객체 PUT/GET</small><small><b>산출:</b> 객체 단위 Data·Metadata·Version</small></div>
</div>

- 보호 방식: 복제·Snapshot·RAID·삭제 코딩·Versioning은 구현 선택이므로 어느 유형의 절대 속성으로 단정하지 않음

## Ⅲ. 워크로드 선택축 비교

> 저지연 임의 갱신·계층 공유·대량 수평 확장은 서로 다른 강점이므로 단일 유형 표준화보다 데이터 생명주기별 조합이 합리적임.

| 축 | 블록 | 파일 | 오브젝트 |
|---|---|---|---|
| 접근 | Device·Volume | Path·File Protocol | HTTP 기반 API |
| 갱신 | 블록 단위 | Byte Range·파일 | 객체 교체 중심 |
| 공유 | Cluster SW 필요 | 다중 Client 강점 | API 기반 분산 접근 |
| 지연 | 저지연 임의 I/O 강점 | Metadata·공유 조정 | 대량 순차·병렬 접근 강점 |
| 확장 | Array·Volume 구성 | Namespace·Metadata 병목 고려 | 대량 객체 수평 확장 강점 |
| 적합 | DB·VM·Transaction | 협업·POSIX 도구 | 비정형·보관·분석 원천 |

## Ⅳ. 데이터 생명주기 배치와 통제

> AI 데이터 플랫폼은 오브젝트의 용량 확장만으로 완성되지 않으며, 학습 중 소형 파일·체크포인트·Metadata 병목을 파일·블록 계층으로 분리해야 함.

<div class="itpe-flow itpe-flow--vertical" aria-label="데이터 생명주기별 스토리지 배치">
  <div class="itpe-flow__node"><strong>수집·원천 보존</strong><small><b>활동:</b> 원본·대규모 비정형 객체 적재</small><small><b>산출:</b> Object Raw Zone과 Metadata</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>공유 전처리</strong><small><b>활동:</b> POSIX 도구·공동 Dataset 접근</small><small><b>산출:</b> File 작업 Dataset</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>학습·서비스</strong><small><b>활동:</b> 저지연 임의 I/O와 Checkpoint 처리</small><small><b>산출:</b> Block 작업영역과 Model Artifact</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>보관·복구</strong><small><b>활동:</b> 수명주기 이동 · Version · 복구시험</small><small><b>산출:</b> 추적 가능한 Archive</small></div>
</div>

| 문제 | 원인 | 대책 | 검증 |
|---|---|---|---|
| 소형 객체 비효율 | 요청·Metadata 비용 | 묶음 포맷·Partition | 크기별 처리량 |
| 데이터 중력 | 대용량 계층 이동 | 계산의 데이터 인접 배치 | 이동시간·전송량 |
| 일관성 오해 | 제품·연산별 보장 차이 | API 의미와 요구 수준 대조 | 동시 읽기·쓰기 시험 |
| 복제 확산 | 계층별 사본 증가 | Catalog·Lineage·수명주기 | 원천 추적·복구시험 |

## Ⅴ. 혼합 배치와 데이터 거버넌스 결론

> 스토리지 선정은 유형의 우열이 아니라 데이터 접근 의미를 업무 단계에 배치하고 사본·권한·복구를 하나의 거버넌스로 닫는 설계 문제임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 오브젝트의 Prefix는 파일시스템 Directory처럼 보여도 동일한 계층·잠금·갱신 의미를 보장하지 않으므로 인터페이스 호환을 별도 검증해야 한다.
- `나라면`: 원본은 오브젝트에 한 번 보존하고, 파일·블록 작업 사본은 수명과 소유자를 명시해 데이터 중력과 고아 사본을 줄이겠다.

### 실전 답안용 기술사적 제언

- 판정: 접근 단위·갱신·공유·지연·확장·복구 요구로 유형 선택
- 대안: 원본 Object, 공유 File, 저지연 Block의 계층형 Reference Architecture 수립
- 검증: 대표 Dataset으로 처리량·지연·일관성·복구·이동 경로 시험
- 효과: 업무 적합성을 유지하며 병목과 불필요한 사본을 축소

<div class="itpe-flow itpe-flow--vertical" aria-label="스토리지 선정 개선 흐름">
  <div class="itpe-flow__node"><strong>현행 한계</strong><small><b>문제:</b> 단일 유형 표준화와 무계획 사본 확산</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>생명주기 배치</strong><small><b>대안:</b> Object 원본 · File 공유 · Block 작업영역</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>워크로드 검증</strong><small><b>판정:</b> 지연 · 처리량 · 일관성 · 복구의 충족 여부</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>거버넌스 운영</strong><small><b>효과:</b> 병목 제거와 사본·권한 추적성 확보</small></div>
</div>

## 1교시 10점 답안 발췌

- 정의: 데이터를 **Block Address**, **File Path**, **Object Key**라는 논리 단위와 인터페이스로 제공하는 스토리지 유형
- 목적: 지연·공유·확장·갱신 요구에 맞는 접근 의미 선택 → 성능과 운영 복잡성 균형

| 유형 | 구조 | 강점 | 업무 |
|---|---|---|---|
| 블록 | Volume·LUN·Block | 저지연 임의 I/O | DB·VM |
| 파일 | Directory·File | 계층·공유·POSIX | 협업·도구 |
| 오브젝트 | Bucket·Key·Metadata | 대량 수평 확장 | 백업·Data Lake |

- 결론: 원본 Object, 공유 File, 저지연 Block을 생명주기에 맞춰 배치하고 Catalog·복구시험으로 통제

## 출제 이력과 검증 출처

- 제132회·제140회 정보관리기술사: 공식 문제지는 Q-Net 자료실에서 원문 확인
- [SNIA Dictionary](https://www.snia.org/education/online-dictionary)
- [NIST SP 800-209, Security Guidelines for Storage Infrastructure](https://csrc.nist.gov/pubs/sp/800/209/final)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 학습 체크

- [ ] Ⅰ 개요: 블록·파일·오브젝트를 논리 단위·Namespace·대표 업무로 구분할 수 있는가?
- [ ] Ⅱ 구조: 세 유형의 접근 활동과 산출을 그리며 보호 방식을 절대 속성으로 단정하지 않을 수 있는가?
- [ ] Ⅲ 비교: 접근·갱신·공유·지연·확장·적합 업무의 여섯 축으로 비교할 수 있는가?
- [ ] Ⅳ 배치: 수집·공유 전처리·학습·보관 단계별 유형과 네 문제의 원인·대책을 연결할 수 있는가?
- [ ] Ⅴ 제언: 요구 판정·계층형 배치·워크로드 검증·거버넌스의 흐름을 설명할 수 있는가?

## 연결 토픽

- [블록 스토리지](./016_block_storage/) · [파일 스토리지](./017_file_storage/) · [스토리지 가상화](./081_storage_virtualization/) · [스토리지 연결 방식](./080_nas/)
