---
title: "스토리지 유형 비교(블록·파일·오브젝트)"
author: "Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

<p class="itpe-byline">작성 모델 · GPT-6<br />작성 · 2026.09.24 21:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>컴퓨터 시스템</span><span>스토리지 아키텍처</span><strong>블록·파일·오브젝트 스토리지</strong></div>

## 30초 인출

- 본질: 스토리지 유형은 같은 데이터를 블록 주소·파일 경로·객체 키라는 서로 다른 논리 단위로 접근하는 방식
- 메커니즘: 블록은 상위 파일시스템에 의미 해석을 맡기고, 파일은 계층 Namespace를 제공하며, 오브젝트는 Data·Metadata·ID를 API로 관리
- 활용: DB·VM에는 블록, 공동 작업에는 파일, 대량 비정형·보관에는 오브젝트를 검토하고 지연·공유·갱신·확장 조건으로 선택

<div class="itpe-flow-map" role="img" aria-label="워크로드 요구에 따른 스토리지 3대 유형 병렬 선택">
  <div class="itpe-flow-node"><strong>데이터 접근 요구</strong><small>입력: 지연 · 공유 · 갱신 · 확장</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>스토리지 대안 선택</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Block</strong><span>판정: LUN·Block Address · 저지연 임의 I/O</span></div>
      <div class="itpe-flow-branch"><strong>File</strong><span>판정: Directory Path · 계층 공유·POSIX</span></div>
      <div class="itpe-flow-branch"><strong>Object</strong><span>판정: Bucket·Key · 대량 비정형 확장</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>업무별 저장 계층</strong><small>출력: DB·VM · 공동 작업 · Data Lake</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- **블록·파일·오브젝트 스토리지**: 데이터를 블록 주소·파일 경로·객체 키라는 서로 다른 접근 단위로 제공하는 저장 인터페이스
- `LUN(Logical Unit Number)`: 호스트에 블록 장치를 식별시킴 → 파일 의미는 상위 계층이 담당
- `Namespace`: 데이터 이름과 위치를 찾는 규칙 → 블록 주소·계층 경로·Bucket/Key를 구분
- `POSIX(Portable Operating System Interface)`: 파일 접근 의미와 API의 공통 기준 → 기존 애플리케이션 호환성을 가름
- `Object API`: Key 기반 PUT·GET·DELETE 인터페이스 → 수평 확장과 객체 단위 갱신 특성을 결정
- `Erasure Coding(삭제 코딩)`: 데이터를 조각과 패리티로 분산 보호 → 용량 효율과 복구 계산 비용을 교환

</details>

---

## 1교시 예상문제 (10점)

> 블록·파일·오브젝트 스토리지의 데이터 접근 방식과 특징을 비교하시오. (예상)

---

## 1교시 10점 답안

## Ⅰ. 스토리지 유형 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **블록·파일·오브젝트 스토리지**: 데이터를 블록 주소·파일 경로·객체 키 단위로 접근하는 인터페이스 유형 |
| 목적 | 지연·공유·확장·갱신 요구에 맞는 저장 구조를 선택 |

## Ⅱ. 접근 유형 비교

| 유형 | 접근 단위 | 대표 강점 | 대표 활용 |
|---|---|---|---|
| 블록 | Block Address·LUN | 저지연 임의 I/O | DB·VM |
| 파일 | Directory·Path | 계층 관리·공유 | 협업·공유 파일 |
| 오브젝트 | Bucket·Key·Metadata | 대량 수평 확장 | 백업·Data Lake |

제언: 워크로드의 접근·갱신·공유 요구에 따른 세 유형의 조합

---

## 2~4교시 예상문제 (25점)

> 블록·파일·오브젝트 스토리지의 구조와 접근방식을 비교하고, 업무별 활용 및 선택 시 고려사항을 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 접근 의미로 구분하는 스토리지 유형 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **블록·파일·오브젝트 스토리지**: 데이터를 블록 주소·파일 경로·객체 키 단위로 접근하는 인터페이스 유형 |
| 목적 | 지연·공유·확장·갱신 요구에 맞는 저장 구조를 선택 |

| 유형 | 논리 단위 | Namespace | 대표 업무 |
|---|---|---|---|
| **블록** | 고정 크기 블록 | 호스트 파일시스템 | DB·VM 디스크 |
| **파일** | 파일·디렉터리 | 계층 경로 | 공동 작업·홈 디렉터리 |
| **오브젝트** | Data·Metadata·ID | Bucket·Key | 백업·미디어·Data Lake |

## Ⅱ. 주소·메타데이터·갱신 구조

> 블록에서 오브젝트로 갈수록 저장 서비스가 더 많은 데이터 의미를 맡지만, 세밀한 In-place Update와 POSIX 호환성은 줄어듦.

<div class="itpe-flow-map" role="img" aria-label="공통 애플리케이션에서 3대 스토리지 접근 구조로의 분기">
  <div class="itpe-flow-node"><strong>애플리케이션 I/O</strong><small>입력: 데이터와 접근 연산</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>접근 인터페이스 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Block 경로</strong><span>처리: LBA 읽기·쓰기 → DB·파일시스템 상태</span></div>
      <div class="itpe-flow-branch"><strong>File 경로</strong><span>처리: Path·권한·Byte Range → 공유 File</span></div>
      <div class="itpe-flow-branch"><strong>Object 경로</strong><span>처리: Key·PUT/GET → Data·Metadata·Version</span></div>
    </div>
  </div>
</div>

- 보호 방식: 복제·Snapshot·RAID·삭제 코딩·Versioning은 구현 선택이므로 어느 유형의 절대 속성으로 단정하지 않음

## Ⅲ. 워크로드 선택축 비교

> 저지연 임의 갱신·계층 공유·대량 수평 확장은 서로 다른 강점이므로 단일 유형 표준화보다 데이터 생명주기별 조합이 합리적임.

| 축 | 블록 | 파일 | 오브젝트 |
|---|---|---|---|
| 접근 | Device·Volume·LBA | Path·NFS/SMB | HTTP 기반 Object API |
| 갱신 | 블록 단위 | Byte Range·파일 | 객체 교체 중심 |
| 공유 | Cluster SW 필요 | 다중 Client 강점 | API 기반 분산 접근 |
| 지연 | 저지연 임의 I/O 강점 | Metadata·공유 조정 | 대량 순차·병렬 접근 강점 |
| 확장 | Array·Volume 구성 | Namespace·Metadata Server 병목 고려 | 대량 객체 수평 확장 강점 |
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

| 한계 | 원인 | 대책 | 검증 |
|---|---|---|---|
| 소형 파일·객체 비효율 | Path 탐색·요청·Metadata 비용 | 묶음 포맷·Partition·병렬 파일시스템 | 크기별 처리량·Metadata Ops |
| 데이터 중력 | 대용량 계층 이동 | 계산의 데이터 인접 배치 | 이동시간·전송량 |
| 일관성 오해 | 제품·연산별 보장 차이 | API 의미와 요구 수준 대조 | 동시 읽기·쓰기 시험 |
| 복제 확산 | 계층별 사본 증가 | Catalog·Lineage·수명주기 | 원천 추적·복구시험 |

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 한 가지 스토리지 인터페이스로 모든 업무를 맞추면 접근 지연·공유·갱신 요구가 충돌 | 업무 단계별 접근 패턴을 시험해 원본·공유 작업·저지연 갱신 계층을 배치하고, 사본 수명·권한·복구 책임을 데이터 카탈로그에 연결 |

| 선택 축 | 평가 기준 |
|---|---|
| 접근 | 주소 단위와 API·파일시스템 호환 요구 |
| 성능 | 대표 부하의 지연·처리량·동시성 |
| 운영 | 일관성·장애 복구·데이터 이동·사본 통제 |

## 출제 이력과 검증 출처

- 제132회 정보관리기술사 1교시 12번: `블록 스토리지, 파일 스토리지, 오브젝트 스토리지의 데이터 접근방식`
- 제140회 정보관리기술사 3교시 5번: `클라우드 컴퓨팅 환경에서 대규모 AI 학습 데이터 구축 및 서비스 인프라 구성을 위해 다양한 스토리지 아키텍처가 활용된다. 블록 스토리지(Block Storage), 파일 스토리지(File Storage), 오브젝트 스토리지(Object Storage)를 비교하여 설명하고, 각 스토리지의 최적 활용 방안에 대하여 설명하시오.`
- [SNIA Dictionary](https://www.snia.org/education/online-dictionary)
- [NVM Express — NVMe over Fabrics](https://nvmexpress.org/specifications/)
- [IETF RFC 8881 — NFS Version 4 Minor Version 1 Protocol](https://www.rfc-editor.org/rfc/rfc8881)
- [NIST SP 800-209, Security Guidelines for Storage Infrastructure](https://csrc.nist.gov/pubs/sp/800/209/final)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 연결 토픽

- [스토리지 가상화](./081_storage_virtualization/) · [스토리지 연결 방식](./080_nas/) · [RAID](./056_raid/) · [클라우드 컴퓨팅](./013_cloud_computing/)
