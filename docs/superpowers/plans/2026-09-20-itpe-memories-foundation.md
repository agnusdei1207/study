# ITPE Memories 정본·로드맵 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `memories`에 원본 PNG, 현행 과목 로드맵, 1,000개 이하 기초/코어 토픽 정본, 시각 중심 답안 작성법을 일관된 단일 정본으로 구축한다.

**Architecture:** 원본 이미지는 `sources/roadmap-images/`, 현재 적용할 로드맵과 키워드 판정은 `contexts/itpe/current/`, 재사용 가능한 작성 절차는 `skills/itpe/`가 각각 소유한다. 기존 749개 통합 토픽을 유지하되 누락만 추가하고, A는 코어·B/C는 기초를 기본 변환으로 사용한다.

**Tech Stack:** Markdown, PNG, PowerShell 검증기, Git

**Spec:** `docs/superpowers/specs/2026-09-20-itpe-roadmap-answer-system-design.md`

## Global Constraints

- 정본 토픽 수는 1,000개 이하이며 숫자를 채우려고 토픽을 추가하지 않는다.
- 원본의 상·중·하는 역사적 참고값이고 출제 확률이 아니다.
- ITIL 3.0, ISO 9126, ISO 17799, 클래스 기반 IPv4 같은 레거시 표현은 현행 개념과 관계를 명시한다.
- 큰 그림은 과목별 학습의 첫 항목이며 장문보다 관계도·흐름도·비교표를 우선한다.
- 기존 사용자 변경을 덮어쓰지 않고 작업 파일만 명시적으로 스테이징한다.

## Review Focus

- 원본 PNG 누락: 파일 13개와 SHA-256 목록이 모두 존재해야 한다.
- 로드맵 전사 누락: 이미지별 키워드가 정본·하위·연결·현행 보정 중 하나로 추적되어야 한다.
- 정본 중복: 같은 개념의 별칭이 독립 토픽으로 중복되지 않아야 한다.
- 뱃지 충돌: 한 토픽에 기초와 코어가 동시에 표시되지 않아야 한다.
- 레거시 오인: 구판 용어가 현행 표준인 것처럼 쓰이지 않아야 한다.

---

### Task 1: 원본 이미지 자산과 전사 목록

**Files:**
- Create: `C:/workspace/memories/contexts/itpe/sources/roadmap-images/README.md`
- Create: `C:/workspace/memories/contexts/itpe/sources/roadmap-images/*.png`

**Interfaces:**
- Consumes: 사용자 제공 모범답안 1장, 과목 로드맵 11장, SW 대체본 1장
- Produces: 파일명·주제·성격·현행화 주의점·SHA-256을 가진 원천 목록

- [ ] **Step 1: 원본 13개 존재 여부를 검사한다**

  Run: `Get-ChildItem contexts/itpe/sources/roadmap-images/*.png | Measure-Object`

  Expected: `Count : 13`

- [ ] **Step 2: README에 각 이미지의 구조와 한계를 전사한다**

  각 이미지마다 `파일`, `주요 축`, `핵심 키워드`, `현행화`, `적용 과목`을 기록한다. 모범답안에는 `제목 → 정의 1줄 → 분류도 → 방식 하나의 구조·흐름 → 짧은 특징` 형식을 기록한다.

- [ ] **Step 3: 해시 목록을 검증한다**

  Run: `Get-FileHash contexts/itpe/sources/roadmap-images/*.png -Algorithm SHA256`

  Expected: 13개 모두 64자리 해시 출력

- [ ] **Step 4: 원천 자산만 커밋한다**

  Run: `git add contexts/itpe/sources/roadmap-images; git diff --cached --check; git commit -m "docs(itpe): preserve roadmap source images"`

### Task 2: 8과목 현행 로드맵 정본

**Files:**
- Create: `C:/workspace/memories/contexts/itpe/current/subject-roadmaps.md`
- Modify: `C:/workspace/memories/contexts/itpe/INDEX.md`

**Interfaces:**
- Consumes: Task 1의 이미지별 전사
- Produces: 8과목별 `전체상 → 세부 영역 → 연결 과목 → 레거시 보정` 계약

- [ ] **Step 1: 실패 기준을 먼저 확인한다**

  Run: `rg -n "과목 큰 그림|Flynn|ITIL 4|ISO/IEC 25010|CIDR" contexts/itpe/current/subject-roadmaps.md`

  Expected: 파일 부재 또는 필수 항목 누락

- [ ] **Step 2: 전과목 관계도와 8개 과목 로드맵을 작성한다**

  각 과목은 `큰 그림`, `세부 도메인`, `코어 축`, `인접 과목`, `원본 대비 현행화` 순서로 작성한다. 04과목에는 Flynn 분류와 OS·자료구조·알고리즘을 포함한다.

- [ ] **Step 3: 필수 현행화 항목을 검사한다**

  Run: `rg -n "과목 큰 그림|Flynn|ITIL 4|ISO/IEC 25010|ISO/IEC 2700[12]|CIDR|AES" contexts/itpe/current/subject-roadmaps.md`

  Expected: 모든 패턴이 한 번 이상 출력

- [ ] **Step 4: 컨텍스트 인덱스에 정본 경로를 등록하고 커밋한다**

  Run: `git add contexts/itpe/current/subject-roadmaps.md contexts/itpe/INDEX.md; powershell -ExecutionPolicy Bypass -File scripts/validate-memory.ps1 -CheckStaged; git diff --cached --check; git commit -m "docs(itpe): add current subject roadmaps"`

### Task 3: 749개 토픽의 기초·코어 분류 계약

**Files:**
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/INDEX.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/01-it-strategy.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/02-software-engineering.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/03-data.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/04-computer-system.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/05-network.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/06-security.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/07-latest-tech.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-keyword-priorities/08-law-policy.md`
- Modify: `C:/workspace/memories/contexts/itpe/current/itpe-exam-preparation.md`

**Interfaces:**
- Consumes: 기존 A/B/C, 공식 기출 근거, Task 2 로드맵
- Produces: 각 토픽의 상호 배타적 `기초/코어` 학습 역할

- [ ] **Step 1: 현재 토픽 수와 누락 상태를 측정한다**

  Run: `rg -c '^\| [0-9]{2}-[0-9]{3} ' contexts/itpe/current/itpe-keyword-priorities/*.md`

  Expected: 합계 749, 기초/코어 열 부재

- [ ] **Step 2: 분류 규칙과 표 열을 과목별로 적용한다**

  A는 코어, B/C는 기초를 기본값으로 삼는다. 반복 공식 기출·25점 답안성·과목 간 연결성이 확인된 B만 코어로 올리고, 모든 예외 이유를 인덱스에 기록한다.

- [ ] **Step 3: 개수·상호 배타성·상한을 검사한다**

  Run: `$rows=rg '^\| [0-9]{2}-[0-9]{3} ' contexts/itpe/current/itpe-keyword-priorities/*.md; if($rows.Count -gt 1000){throw 'topic cap exceeded'}; if(($rows | Where-Object {$_ -notmatch '\| (기초|코어) \|'}).Count){throw 'badge missing'}`

  Expected: 오류 없음, 토픽 수 1,000 이하

- [ ] **Step 4: 목록·전략 수치를 동기화하고 커밋한다**

  Run: `git add contexts/itpe/current/itpe-keyword-priorities contexts/itpe/current/itpe-exam-preparation.md; powershell -ExecutionPolicy Bypass -File scripts/validate-memory.ps1 -CheckStaged; git diff --cached --check; git commit -m "docs(itpe): classify canonical topics by learning role"`

### Task 4: 시각 중심 답안·서브노트 작성법

**Files:**
- Modify: `C:/workspace/memories/skills/itpe/write-itpe-answers/SKILL.md`
- Modify: `C:/workspace/memories/skills/itpe/write-itpe-answers/references/writing-principles.md`
- Modify: `C:/workspace/memories/skills/itpe/write-itpe-answers/references/answer-skeleton.md`
- Modify: `C:/workspace/memories/skills/itpe/write-itpe-answers/references/answer-checklist.md`
- Modify: `C:/workspace/memories/skills/itpe/write-study-notes/SKILL.md`
- Modify: `C:/workspace/memories/skills/itpe/write-study-notes/references/study-note-guide.md`
- Modify: `C:/workspace/memories/skills/itpe/plan-itpe-study/references/study-strategy.md`

**Interfaces:**
- Consumes: 모범답안 시각 구조, Task 2 큰 그림, Task 3 학습 역할
- Produces: `과목 큰 그림 → 토픽 위치 → 30초 그림 → 표 → 최소 설명` 작성 계약

- [ ] **Step 1: 기존 규칙의 실패 사례를 기록한다**

  Run: `rg -n "큰 그림|과목 로드맵|장문|기초/코어" skills/itpe`

  Expected: 과목 시작 로드맵과 새 뱃지 규칙이 불완전함

- [ ] **Step 2: 답안 작성법에 시각 우선순위를 추가한다**

  1교시는 `정의 2줄 → 핵심 그림/표 → 차별화 1~2줄`, 2~4교시는 `요구사항 목차 → 전체 구조도 → 본론 표/흐름 → 대책 → 결론`으로 고정한다. 산문은 그림·표를 읽어 주는 짧은 인과 문장만 허용한다.

- [ ] **Step 3: 학습 노트 작성법에 과목 로드맵 위치를 추가한다**

  각 노트가 `과목 로드맵의 어느 축인지`, `30초에 그릴 핵심 그림`, `기초/코어에 따른 인출 깊이`를 표시하도록 계약을 바꾼다.

- [ ] **Step 4: 체크리스트로 규칙 존재를 검사한다**

  Run: `rg -n "과목 큰 그림|30초|장문|기초|코어|정의 2줄" skills/itpe/write-itpe-answers skills/itpe/write-study-notes skills/itpe/plan-itpe-study`

  Expected: 세 스킬에서 각 역할에 맞는 규칙 출력

- [ ] **Step 5: 스킬 변경을 검증하고 커밋한다**

  Run: `git add skills/itpe/write-itpe-answers skills/itpe/write-study-notes skills/itpe/plan-itpe-study; powershell -ExecutionPolicy Bypass -File scripts/validate-memory.ps1 -CheckStaged; git diff --cached --check; git commit -m "docs(itpe): make roadmaps and visuals answer primitives"`

### Task 5: 인덱스·레거시 정합성 정리와 푸시

**Files:**
- Modify: `C:/workspace/memories/contexts/itpe/INDEX.md`
- Modify: `C:/workspace/memories/INDEX.md`
- Modify: `C:/workspace/memories/contexts/itpe/drafts/study-rewrite-plan.md`

**Interfaces:**
- Consumes: Tasks 1~4의 최종 경로와 실제 집계
- Produces: 깨진 CSPE/ITPE 명칭, 749/1107 혼동, 과목별 상태가 없는 탐색 인덱스

- [ ] **Step 1: 레거시·불일치 후보를 찾는다**

  Run: `rg -n "plan-cspe|write-cspe|776개|1107개 토픽|1,107개 토픽" INDEX.md contexts/itpe skills/itpe`

  Expected: 수정 대상만 출력

- [ ] **Step 2: 경로·명칭·집계를 실제 값으로 고친다**

  `749개 통합 토픽`, `1,107개 원래 키워드 풀`, `기초/코어`, 로드맵 정본 경로를 구분해서 적는다.

- [ ] **Step 3: 저장소 전체 검증을 실행한다**

  Run: `powershell -ExecutionPolicy Bypass -File scripts/validate-memory.ps1; git diff --check`

  Expected: 종료 코드 0

- [ ] **Step 4: 정합성 변경을 커밋하고 푸시한다**

  Run: `git add INDEX.md contexts/itpe/INDEX.md contexts/itpe/drafts/study-rewrite-plan.md; powershell -ExecutionPolicy Bypass -File scripts/validate-memory.ps1 -CheckStaged; git diff --cached --check; git commit -m "docs(itpe): reconcile roadmap and keyword indexes"; git push`

