# ITPE Study 로드맵·1과목 적용 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `study`를 `memories` 정본을 따라 읽고, 그려 보고, 실제 답안을 쓰는 서브노트로 정리하고 01 정보 전략 및 관리 전 토픽에 적용한다.

**Architecture:** 루트와 과목 인덱스는 먼저 큰 그림을 보여 주고, 개별 노트는 기초/코어 뱃지와 실전 인출 블록을 제공한다. 작성법은 `study`에 복제하지 않고 짧은 사용 안내와 정본 동기화 정보만 둔다.

**Tech Stack:** Astro 7, Starlight, Markdown/MDX, TypeScript, PowerShell 감사 명령

**Spec:** `docs/superpowers/specs/2026-09-20-itpe-roadmap-answer-system-design.md`

## Global Constraints

- 02 소프트웨어 공학의 기존 사용자 변경은 읽기·수정·스테이징하지 않는다.
- 모든 과목 인덱스의 첫 본문은 `과목 큰 그림`이다.
- 개별 토픽은 기초 또는 코어 하나만 표시한다.
- 장문 산문보다 손으로 재현 가능한 ASCII 관계도·흐름도·비교표를 우선한다.
- 커밋은 `git commit --only -- <paths>`로 작업 경로만 포함한다.

## Review Focus

- 사용자 WIP 혼입: 최종 커밋에 02과목 파일이 하나도 없어야 한다.
- 스키마 호환: 기존 노트가 새 필드 부재로 빌드 실패하지 않아야 한다.
- 큰 그림 위치: 8개 과목 인덱스에서 다른 H2보다 먼저 나와야 한다.
- 링크 무결성: 로드맵의 토픽 링크가 실제 파일을 가리켜야 한다.
- 01과목 품질: 코어 노트가 그림·10점 답안·확장 골격·출처를 갖춰야 한다.

---

### Task 1: 콘텐츠 스키마와 읽기 전용 감사기

**Files:**
- Modify: `src/content.config.ts`
- Modify: `src/types/note.ts`
- Modify: `src/utils/noteBadges.ts`
- Create: `scripts/audit-itpe-content.ps1`
- Modify: `package.json`

**Interfaces:**
- Produces: `learning_level: '기초' | '코어'`, 허용 출처 상태, 로드맵·답안 블록 감사 결과

- [ ] **Step 1: 실패하는 감사기를 만든다**

  감사기는 토픽 수 상한, 배지 누락, 과목 인덱스 첫 H2, 01 코어 필수 절, 02 변경 금지를 검사하고 오류 수가 있으면 종료 코드 1을 반환한다.

- [ ] **Step 2: 감사기를 실행해 현재 실패를 확인한다**

  Run: `npm run audit:itpe`

  Expected: `learning_level`과 큰 그림 누락으로 실패

- [ ] **Step 3: 스키마를 하위 호환 방식으로 확장한다**

  기존 문서에는 필드가 없으므로 선택 필드로 시작하고, 감사기가 ITPE 대상에서 필수성을 강제한다.

- [ ] **Step 4: 타입 검사와 감사기 구조를 검증한다**

  Run: `npm run check`

  Expected: 종료 코드 0

- [ ] **Step 5: 작업 파일만 커밋한다**

  Run: `git commit --only -m "feat: add ITPE learning role audits" -- package.json scripts/audit-itpe-content.ps1 src/content.config.ts src/types/note.ts src/utils/noteBadges.ts`

### Task 2: 루트와 8과목 큰 그림

**Files:**
- Modify: `src/content/docs/notes/itpe/index.md`
- Modify: `src/content/docs/notes/itpe/01-it-strategy/index.md`
- Modify: `src/content/docs/notes/itpe/02-software-engineering/index.md`
- Modify: `src/content/docs/notes/itpe/03-data/index.md`
- Modify: `src/content/docs/notes/itpe/04-computer-system/index.md`
- Modify: `src/content/docs/notes/itpe/05-network/index.md`
- Modify: `src/content/docs/notes/itpe/06-security/index.md`
- Modify: `src/content/docs/notes/itpe/07-latest-tech/index.md`
- Modify: `src/content/docs/notes/itpe/08-law-policy/index.md`

**Interfaces:**
- Consumes: memories의 `subject-roadmaps.md`
- Produces: 각 과목 첫 화면의 큰 그림, 세부 영역, 코어/기초 목록, 연결 과목

- [ ] **Step 1: 현재 인덱스 실패를 확인한다**

  Run: `npm run audit:itpe`

  Expected: 8과목 큰 그림 누락

- [ ] **Step 2: 루트 전과목 흐름과 8개 과목 도식을 수작업으로 작성한다**

  02 인덱스는 사용자 토픽 WIP를 건드리지 않고 큰 그림 블록만 추가한다. 04에는 Flynn, OS, 구조, 자료구조·알고리즘의 위치를 함께 표시한다.

- [ ] **Step 3: 인덱스 순서와 링크를 검사한다**

  Run: `npm run audit:itpe`

  Expected: 큰 그림 관련 오류 0

- [ ] **Step 4: 인덱스만 커밋한다**

  Run: `git commit --only -m "docs: add ITPE subject roadmaps" -- src/content/docs/notes/itpe/index.md src/content/docs/notes/itpe/01-it-strategy/index.md src/content/docs/notes/itpe/02-software-engineering/index.md src/content/docs/notes/itpe/03-data/index.md src/content/docs/notes/itpe/04-computer-system/index.md src/content/docs/notes/itpe/05-network/index.md src/content/docs/notes/itpe/06-security/index.md src/content/docs/notes/itpe/07-latest-tech/index.md src/content/docs/notes/itpe/08-law-policy/index.md`

### Task 3: 01과목 기초·코어 메타데이터

**Files:**
- Modify: `src/content/docs/notes/itpe/01-it-strategy/*.md`

**Interfaces:**
- Consumes: memories 01 토픽 정본의 학습 역할
- Produces: 81개 노트의 단일 `learning_level`과 화면 배지

- [ ] **Step 1: 01과목 파일 수와 누락을 측정한다**

  Run: `$f=Get-ChildItem src/content/docs/notes/itpe/01-it-strategy/*.md | Where-Object Name -ne 'index.md'; $f.Count; rg -L 'learning_level:' $f.FullName`

  Expected: 81개, 81개 누락

- [ ] **Step 2: 노트 하나씩 정본과 대조해 메타데이터를 추가한다**

  제목·토픽 ID·기존 기출 근거를 유지하고, 정본의 기초/코어 값만 옮긴다. 토픽 내용은 이 단계에서 바꾸지 않는다.

- [ ] **Step 3: 배지와 개수를 검사한다**

  Run: `npm run audit:itpe`

  Expected: 01과목 뱃지 오류 0

- [ ] **Step 4: 01 메타데이터만 커밋한다**

  Run: `git commit --only -m "docs: classify IT strategy notes by learning role" -- src/content/docs/notes/itpe/01-it-strategy`

### Task 4: 01과목 실전 서브노트 전수 교정

**Files:**
- Modify: `src/content/docs/notes/itpe/01-it-strategy/*.md`

**Interfaces:**
- Consumes: memories 작성법과 01 로드맵
- Produces: 코어 10점형 실전 답안·25점 확장 골격, 기초 30초 그림·구분축, 검증 출처

- [ ] **Step 1: 코어 노트 한 개를 기준 샘플로 교정한다**

  `001_ismp.md`를 `로드맵 위치 → 10점형 답안 → 30초 그림 → 25점 확장 → 문제 변형 → 보충 학습 → 검증 출처` 순서로 교정한다.

- [ ] **Step 2: 샘플의 실패 조건을 검사한다**

  Run: `npm run audit:itpe`

  Expected: 샘플 오류 0, 나머지 코어 노트 누락 보고

- [ ] **Step 3: 코어 노트를 중요도 순으로 하나씩 교정한다**

  매 파일마다 정의·그림·표가 같은 내용을 반복하지 않는지, 그림이 15줄 이내인지, 근거 없는 수치가 없는지 확인한 뒤 다음 파일로 이동한다.

- [ ] **Step 4: 기초 노트를 하나씩 짧게 교정한다**

  `한 줄 본질 → 30초 그림/표 → 이웃 토픽 구분 → 출제 형태`만 남기고 25점용 장문을 만들지 않는다.

- [ ] **Step 5: 01과목 전체 감사를 실행한다**

  Run: `npm run audit:itpe; npm run check; npm run build`

  Expected: 모두 종료 코드 0

- [ ] **Step 6: 01과목 본문만 커밋한다**

  Run: `git commit --only -m "docs: reshape IT strategy notes for answer practice" -- src/content/docs/notes/itpe/01-it-strategy`

### Task 5: 중복 가이드 제거·최종 정합성·푸시

**Files:**
- Modify: `agent-guides/ITPE_AUTHORING_GUIDE.md`
- Modify: `agent-guides/ITPE_ROADMAP_CROSSWALK.md`
- Modify: `agent-guides/keywords/README.md`
- Modify: `src/content/docs/notes/index.md`
- Modify: `src/content/docs/index.md`
- Modify: `docs/superpowers/specs/2026-09-20-itpe-roadmap-answer-system-design.md`

**Interfaces:**
- Consumes: 실제 8과목 파일 수와 memories 정본 경로
- Produces: 정본을 복제하지 않는 짧은 동기화 안내와 정확한 진행 집계

- [ ] **Step 1: 749/1102/1107 혼용과 중복 작성법을 찾는다**

  Run: `rg -n "749|1102|1,102|1107|1,107|A ·|B ·|C ·" agent-guides src/content/docs/index.md src/content/docs/notes/index.md src/content/docs/notes/itpe/index.md`

  Expected: 정리 대상 출력

- [ ] **Step 2: 안내 문서를 정본 포인터와 실제 집계로 축약한다**

  사용자 화면에는 기초/코어와 실제 토픽 수만 보이고, 작성 규칙 전문과 A/B/C 전략은 두지 않는다.

- [ ] **Step 3: 전체 검증과 사용자 WIP 보호를 확인한다**

  Run: `npm run audit:itpe; npm run check; npm run build; git diff --check; git diff --name-only HEAD -- src/content/docs/notes/itpe/02-software-engineering`

  Expected: 앞 세 명령 종료 코드 0, 마지막 명령은 Task 2에서 의도한 `index.md` 외 신규 변경 없음

- [ ] **Step 4: 가이드·집계·설계만 커밋한다**

  Run: `git commit --only -m "docs: align ITPE study guidance with canonical roadmaps" -- agent-guides/ITPE_AUTHORING_GUIDE.md agent-guides/ITPE_ROADMAP_CROSSWALK.md agent-guides/keywords/README.md src/content/docs/index.md src/content/docs/notes/index.md docs/superpowers/specs/2026-09-20-itpe-roadmap-answer-system-design.md docs/superpowers/plans/2026-09-20-itpe-memories-foundation.md docs/superpowers/plans/2026-09-20-itpe-study-application.md`

- [ ] **Step 5: 커밋 범위와 원격 상태를 확인해 푸시한다**

  Run: `git log --stat --oneline -6; git status --short; git push`

  Expected: 작업 커밋에 사용자 02 WIP 미포함, 푸시 성공

