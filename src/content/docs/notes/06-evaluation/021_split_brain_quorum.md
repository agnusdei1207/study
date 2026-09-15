---
sidebar:
  order: 21
  label: "021. Split Brain•쿼럼 (Split Brain Quorum)"
  badge:
    text: "기출 · 30%"
    variant: note
title: "분산 클러스터 정합성 및 이중 마스터 방어 : 스플릿 브레인과 쿼럼 (Split-Brain & Quorum Fencing)"
date: "2026-09-15T09:25:00+09:00"
tags:
  - "notes-evaluation"
weight: 21
extra:
  question_no: "021"
  source_status: "기출"
  source_history: "126회"
  priority: 30
  priority_note: "126회 기출, 분산 고가용성 클러스터의 핵심 결함인 스플릿 브레인(Split-Brain), 정족수 쿼럼(Quorum: 과반수 원칙 ⌊N/2⌋+1), 홀수 노드(Odd Node) 및 증인 노드(Witness/Arbiter), 세대 번호(Epoch/Term), STONITH 하드웨어 펜싱 및 SCSI-3 PR 스토리지 펜싱 메커니즘"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **스플릿 브레인(Split-Brain)**: 다중 노드 클러스터 환경에서 노드 간의 전용 하트비트(Heartbeat) 통신망이 단절(Network Partition)되었을 때, 각 격리된 진영(Partition)이 상대방 노드가 고장 났다고 오판하여 양쪽 모두 스스로를 '마스터(Active/Primary)'로 승격시켜 공유 스토리지나 데이터베이스에 동시 쓰기를 감행함으로써 데이터가 복구 불가능하게 파괴되는 치명적 클러스터 결함.
- **쿼럼(Quorum / 정족수)**: 스플릿 브레인을 방어하기 위해 클러스터 전체 노드 수($N$) 중 과반수($Q = \lfloor \frac{N}{2} \rfloor + 1$)의 투표 동의를 획득한 단 하나의 분할 그룹에게만 마스터 승격 및 쓰기 권한을 부여하고, 과반수를 얻지 못한 소수 진영은 스스로 쓰기를 중단(Self-fencing)하도록 강제하는 분산 합의(Consensus) 수리 원칙.

</details>

- 정의/개념: 분산 클러스터의 데이터 정합성과 단일 쓰기 원칙(Single-Writer Invariant)을 사수하기 위해 **하트비트 감시 $\rightarrow$ 네트워크 분할 발생 시 과반수 쿼럼($\lfloor \frac{N}{2} \rfloor + 1$) 투표 $\rightarrow$ 증인(Witness) 노드 캐스팅보트 $\rightarrow$ 단조 증가 세대 번호(Epoch/Term) 부여 $\rightarrow$ STONITH 및 SCSI-3 PR 펜싱(Fencing) 기반 패배 노드 물리적 격리** 를 집행하는 **분산 일관성 제어 체계**
- 배경/필요성: 다중 노드 클러스터 환경에서 노드 간 전용 하트비트(Heartbeat) 통신망이 단절(Network Partition)되었을 때, 고립된 양쪽 진영이 상대방 노드를 장애로 오판하여 동시에 자신을 마스터(Active)로 승격시키고 공유 스토리지나 데이터베이스에 동시 쓰기를 수행함으로써 데이터가 영구적으로 파괴되는 스플릿 브레인(Split-Brain) 재난이 발생하는 구조적 결함이 발생함에 따라, Raft 및 Paxos 분산 합의에 기반하여 전체 노드 수($N$)의 과반수($Q = \lfloor \frac{N}{2} \rfloor + 1$) 동의를 얻은 진영만 리더 승격을 허용하고 소수 진영은 STONITH 및 SCSI-3 PR로 물리 격리하는 쿼럼 펜싱 체계를 도입하여 **이중 마스터 출현의 선제적 차단, 단조 증가 세대 번호(Epoch/Term) 기반의 데이터 정합성 사수 및 단일 쓰기 원칙(Single-Writer Invariant) 보증**을 달성할 필요

#### 한줄 요약
- 스플릿 브레인은 네트워크 분할 시 이중 마스터가 발생하는 결함이며, 과반수 쿼럼과 STONITH 펜싱으로 방어한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **쿼럼 및 펜싱 3대 핵심 수리 메커니즘**:
  - **과반수 쿼럼 원칙 ($Q = \lfloor \frac{N}{2} \rfloor + 1$)**: $N$개 노드가 둘로 쪼개졌을 때 과반수를 만족하는 그룹은 수학적으로 오직 1개만 존재함을 보증.
  - **세대 번호 (Epoch / Term)**: 리더 선출 시마다 단조 증가하는 번호를 부여하여 구 마스터의 지연된 쓰기 요청을 스토리지에서 거부.
  - **노드 펜싱 (Fencing / STONITH)**: 과반수를 상실한 구 마스터 노드의 전원(IPMI)이나 스토리지 채널(SCSI-3 PR)을 물리적으로 강제 차단.

</details>

- 동률을 방지하는 **홀수 노드 쿼럼**
- 2노드 동률을 해소하는 **Witness 중재**
- 구 마스터의 전원을 끊는 **STONITH 펜싱**

#### 한줄 요약
- 과반수 쿼럼($\lfloor N/2 \rfloor + 1$), 홀수/증인 노드 구성, 세대 번호(Epoch), STONITH 하드웨어 펜싱을 제공한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **스플릿 브레인 방어 4대 아키텍처 계층**:
  1. **Consensus & Quorum Layer**: Corosync, etcd, Zookeeper (Raft/Paxos 쿼럼 합의).
  2. **Monotonic Epoch Tracker**: 리더 세대 번호(Term), 분산 임대권(Lease).
  3. **Storage Fencing Layer**: SCSI-3 Persistent Reservation (PR), SAN 스위치 포트 차단.
  4. **Power Fencing Layer (STONITH)**: IPMI, iLO, BMC, 네트워크 PDU 전원 차단기.

</details>

```text
[스플릿 브레인 방어 체계]
├── [Consensus·Quorum Layer]
│   └── 과반수 합의 및 Witness 투표
├── [Monotonic Epoch Tracker]
│   └── 세대 번호 기반 지연 쓰기 차단
├── [Storage Fencing Layer]
│   └── SCSI-3 PR 기반 디스크 락
└── [Power Fencing Layer]
    └── STONITH 기반 전원 강제 차단
```

- 선들의 의미:
  - `──`: 계층 간 논리적 연계
  - `├──`, `└──`: 하위 보호 계층 분기

| 구성요소 | 책임 |
|:---|:---|
| Consensus·Quorum Layer | 과반수 합의와 Witness 투표로 리더 선출 |
| Monotonic Epoch Tracker | 구 세대의 지연 쓰기 거부 |
| Storage Fencing Layer | SCSI-3 PR로 패배 노드의 디스크 차단 |
| Power Fencing Layer | STONITH로 고립 노드 전원 차단 |

#### 한줄 요약
- 쿼럼 계층은 다수 진영을 판정하고, 세대 번호와 SCSI-3 PR 및 STONITH가 스토리지·전원 수준에서 물리적으로 차단해 이중 쓰기 손상을 원천 방어한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **스플릿 브레인 방어 및 쿼럼 페일오버 5단계 프로세스**:
  1. 평시 Node 1(Primary), Node 2(Standby), Node 3(Witness) 간 3자 하트비트 교환
  2. 네트워크 스위치 장애로 Node 1이 고립되는 1:2 분할 발생
  3. Node 2와 3이 과반수(2/3) 쿼럼을 달성하고 신규 세대 번호(Term 2) 발급
  4. Node 2가 Node 1에 대해 IPMI STONITH 전원 강제 차단 신호 전송
  5. Node 1의 스토리지 쓰기가 차단된 것을 확인 후 Node 2가 New Primary로 승격

</details>

```text
[3-Node Cluster] (① 평시 하트비트 교환 및 Term 1 정상 가동)
└── [Network Partition 발생] (② AZ 간 광케이블 단선으로 1:2 진영 분할)
    └── [Quorum Voting Engine] (③ 과반수 2/3 형성 진영 판정 및 Term 2 단조 증가)
        ├── [STONITH Fencing] (④ Out-of-band IPMI로 고립된 구 Primary 전원 강제 OFF)
        └── [Shared Storage (SCSI-3 PR)] (⑤ 구 세대 쓰기 키 등록 해제 및 New Primary 단일 쓰기 승격)

- 분기 결과: 과반수 획득 진영(2/3)은 승격 및 단일 쓰기 재개, 소수 진영(1/3)은 STONITH 전원 차단 및 디스크 쓰기 거부로 이중 마스터 원천 차단
```

#### 한줄 요약
- 소수 진영은 쓰기를 동결하고 과반수 진영만 승격하며, STONITH 펜싱을 통해 구 마스터를 물리 격리함으로써 분산 정합성을 보증한다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **클러스터 쿼럼 구성 2대 방식 비교**:
  - 홀수 노드 쿼럼 (3-Node / 5-Node): 노드 간 완전 대등 투표 (표준 Raft/Paxos).
  - 짝수 노드 + 증인 쿼럼 (2-Node + Witness): 2노드 Active-Standby에 경량 증인 추가.

</details>

| 비교 항목 | 홀수 노드 구성 (3-Node Quorum) | 짝수 노드 + 증인 (2-Node + Witness) | 2노드 무증인 구성 (2-Node No Witness) |
|:---|:---|:---|:---|
| 클러스터 노드 수 | 3대 (모두 데이터 저장 및 연산) | 2대 (데이터) + 1대 (경량 Witness) | 2대 (증인 없음, 비추천) |
| 과반수 쿼럼 기준 | 2표 이상 (2/3) | 2표 이상 (2/3) | 2표 전원 일치 (2/2) |
| 단일 노드 장애 시 | 1대 다운되어도 2대로 정상 가동 | 1대 다운되어도 Witness와 2대로 가동 | 1대 다운 시 쿼럼 상실로 전체 셧다운 |
| 스플릿 브레인 방어 | 안정적 방어 (과반수 자동 판정) | 안정적 방어 (Witness가 캐스팅보트) | 방어 불가 (50:50 동률로 양쪽 마스터) |
| 인프라 구축 비용 | 중간 ($3\times$ 하드웨어) | 경제적 ($2\times$ + 초경량 VM 1대) | 최저 ($2\times$ 하드웨어) |
| 적용 시스템 | etcd, Kafka, ZooKeeper, Ceph | Oracle Data Guard, MySQL MHA | 단순 개발 환경 |

#### 한줄 요약
- 3노드는 자체 과반수 해결, 2노드+Witness는 경제적 동률 해결, 2노드 무증인은 스플릿 브레인에 취약하다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **증인 노드(Witness Node / Arbiter)**: 실제 비즈니스 데이터를 저장하거나 처리하지 않고 오직 클러스터 쿼럼 투표권(1표)만을 행사하여 2노드 환경의 50:50 동률을 방지하는 경량 컴포넌트이다.
- **STONITH(Shoot The Other Node In The Head)**: 스플릿 브레인 방어를 위해 IPMI, iLO, 네트워크 관리형 PDU 등을 통해 응답이 없는 상대 노드의 전원을 강제로 차단하는 물리적 펜싱 기법이다.
- **아웃오브밴드 관리망(Out-of-band IPMI)**: 운영 업무 트래픽망과 물리적으로 완전히 분리된 전용 원격 하드웨어 제어 네트워크로, OS나 네트워크 스위치가 다운되어도 서버 전원 제어 및 콘솔 접속을 보장한다.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 2개 노드 분할 시 50:50 동률로 이중 마스터 발생 및 DB 파괴 | 독립된 제3 가용영역(AZ-3)에 경량 Witness 노드 배치 | 과반수(2/3) 판정으로 스플릿 브레인 원천 방어 |
| 구 마스터 잔여 I/O 및 백그라운드 지연 쓰기로 인한 블록 손상 | Out-of-band IPMI/PDU 기반 STONITH 하드웨어 펜싱 강제 적용 | 구 노드 전원 차단으로 비정상 쓰기 물리적 봉쇄 |
| 단일 랙 전원 단락 시 3개 노드 동시 셧다운으로 쿼럼 붕괴 | 쿼럼 노드를 전원·네트워크가 분리된 Multi-AZ에 분산 배치 | 단일 AZ 정전 시에도 2개 노드로 무중단 쿼럼 유지 |

#### 한줄 요약
- Witness 노드로 동률을 막고, STONITH로 잔여 I/O를 차단하며, Multi-AZ 분산으로 쿼럼 붕괴를 방어한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **Raft / etcd**: 분산 시스템에서 상태 머신 복제를 위해 고안된 리더 기반의 합의 알고리즘과 이를 구현한 분산 키-값 저장소로, 과반수 쿼럼을 통해 일관성을 보장한다.
- **SCSI-3 PR(Persistent Reservation)**: 공유 스토리지(SAN) 레벨에서 등록된 키(Key)를 가진 정상 마스터 노드에게만 LUN에 대한 읽기/쓰기 권한을 부여하고 구 마스터의 예약을 해제(Preempt)하는 스토리지 펜싱 기술이다.
- **세대 번호(Epoch / Term)**: 새로운 리더가 선출될 때마다 1씩 단조 증가하는 논리적 시계 번호로, 구 리더가 보낸 지연된 패킷이나 쓰기 요청을 스토리지나 팔로워 노드가 즉시 식별하여 무효화하도록 돕는다.

</details>

- **기술 위상/발전**: 과반수 쿼럼($\lfloor N/2 \rfloor + 1$)과 단조 증가 세대 번호(Epoch) 기반 분산 합의 및 이중 마스터 방어 표준 확립
- **실무 적용/통제**: 제3 가용영역 증인(Witness) 노드 배치, Out-of-band IPMI 기반 STONITH 펜싱 및 Multi-AZ 분산 배치 적용

#### 한줄 요약
- 과반수 쿼럼과 STONITH 하드웨어 펜싱을 통해 스플릿 브레인을 체계적으로 방어하고 분산 데이터 정합성을 보증해야 한다.
