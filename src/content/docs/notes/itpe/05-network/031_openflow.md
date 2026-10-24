---
title: "OpenFlow"
author: "agnusdei1207"
date: "2026-10-24T22:46:23+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- OpenFlow, SDN(Software-Defined Networking), 사우스바운드 인터페이스(SBI)
- 플로우 테이블, 플로우 엔트리, Packet-In, Flow-Mod, Packet-Out, 그룹 테이블
- TCAM, ONOS, P4, Fail-Standalone

## Ⅰ. OpenFlow의 개요

- 핵심 요약 : 제어 평면을 중앙 컨트롤러로 분리하고 스위치의 플로우 테이블을 외부에서 프로그래밍하는 개방형 표준 프로토콜.
- 개념 : **소프트웨어 정의 네트워킹** (SDN, Software-Defined Networking)에서 중앙 컨트롤러와 스위치를 잇는 **OpenFlow**는 스위치의 플로우 테이블을 소프트웨어로 설정하도록 규격화한 프로토콜이며, 이때 사용하는 연결 지점을 사우스바운드 인터페이스(SBI, Southbound Interface)라 부른다.
- 배경 및 필요성 : 기존 장비는 제어 기능과 전달 기능이 한 장비 안에 묶인 벤더 고유 구조여서, 새로운 프로토콜 시험과 정책 변경이 사실상 장비 단위 작업이 되었다. 이 한계를 풀기 위해 스탠퍼드 대학교의 Clean Slate 연구 프로그램에서 출발했다.
- 주요 목적 : 제어 평면과 데이터 평면의 물리적 분리, 개방형 인터페이스를 통한 벤더 종속 완화, 중앙 소프트웨어에 의한 트래픽 동적 제어.

## Ⅱ. OpenFlow의 특징 및 장점

- 핵심 요약 : 제어와 전달의 분리, 플로우 단위 프로그래밍, 표준 메시지 교환이 정책 변경 속도와 벤더 독립성으로 이어지는 구조.

1. 제어·전달 분리 : 컨트롤러가 전역 토폴로지를 보고 경로를 계산하고 스위치는 설치된 규칙만 수행 → 정책 변경을 중앙에서 일괄 적용.
2. 플로우 엔트리 기반 제어 : 매칭 필드, 우선순위, 카운터, 명령어, 타이머로 구성된 **플로우 엔트리**를 스위치가 실행 → 헤더 단위의 세밀한 트래픽 제어.
3. 표준 메시지 교환 : **Packet-In**(미매칭 패킷을 컨트롤러로 전달), **Flow-Mod**(플로우 엔트리 추가·수정·삭제), **Packet-Out**(컨트롤러가 만든 패킷을 지정 포트로 송출) → 신규 흐름 대응과 규칙 갱신의 자동화.
4. 벤더 중립 규격 : 개방형 표준을 따르는 장비끼리 상호 제어가 가능 → 벤더 종속 완화와 장비 선택 폭 확대.

## Ⅲ. OpenFlow의 구조 (흐름)

- 핵심 요약 : 중앙 컨트롤러가 제어 평면을 맡고, 스위치가 전달 평면에서 플로우 테이블 파이프라인을 실행하는 이원 구조.

```text
[ 제어 평면 ]
  SDN 컨트롤러
  (토폴로지·라우팅 로직)
        ↓ Flow-Mod (규칙 설치)
        ↑ Packet-In (미식별 패킷)
        ↕ OpenFlow 채널 (TLS 보안 연결)
[ 전달 평면 ]
  OpenFlow 스위치
  (플로우 테이블 파이프라인)
```

- **플로우 테이블** (Flow Table) : 스위치 안에 0번부터 순서대로 배치된 복수의 테이블로, 패킷이 차례로 통과하며 L2~L4 헤더를 단계별로 매칭.
- **그룹 테이블** (Group Table) : 멀티캐스트, 브로드캐스트, 고속 장애 우회(Fast Failover)처럼 복수 포트에 대한 액션을 묶어 처리.
- 타이머 : 유휴 시간(Idle Timeout)과 최대 유지 시간(Hard Timeout)이 지나면 플로우 엔트리를 자동 삭제.

```text
[ 패킷 처리 파이프라인 ]

[ 패킷 도착 ]
      ↓
[ Flow Table 0 ] 매칭 시 명령어 실행
      ↓ 미매칭 (Table-miss)
[ Flow Table 1 ~ n ] 다음 테이블 또는 액션
      ↓ 최종 미매칭
[ Packet-In ] → 컨트롤러로 전송
      ↓
[ 컨트롤러 ] Flow-Mod로 규칙 설치
```

## Ⅳ. OpenFlow의 비교

- 핵심 요약 : 중앙 제어로 개방성을 얻는 OpenFlow는 고정된 헤더 필드라는 제약을 가지며, 이 제약을 넘기 위해 P4(Programming Protocol-independent Packet Processors)가 등장함.

| 비교 항목 | OpenFlow 기반 SDN | 전통적 분산 라우팅 | P4 기반 프로그래머블 데이터 평면 |
| --- | --- | --- | --- |
| 제어 평면 위치 | 중앙 집중식 컨트롤러 | 장비 내부에 분산 탑재 | 중앙 컨트롤러와 P4 런타임 |
| 포워딩 제어 방식 | OpenFlow 규칙 설치 | 벤더 고유 OS와 표준 프로토콜 | P4 프로그램 컴파일 후 설치 |
| 파싱 가능 헤더 | 고정된 표준 헤더 필드 | 고정된 표준 프로토콜 | 사용자 정의 헤더 파싱 가능 |
| 포워딩 실행부 | 하드웨어 ASIC(Application-Specific Integrated Circuit) 기반 | 하드웨어 ASIC 기반 | 프로그래머블 ASIC 기반 |
| 표준화 주체 | ONF(Open Networking Foundation) | IETF(Internet Engineering Task Force), IEEE(Institute of Electrical and Electronics Engineers) | P4(Programming Protocol-independent Packet Processors) 커뮤니티 |

- 선택 기준 : 표준 헤더 범위 안에서 중앙 제어 자동화가 목적이면 OpenFlow 기반 SDN이 적합하고, 새로운 헤더 처리나 데이터 평면 기능이 필요하면 P4 계열을 검토함.

## Ⅴ. OpenFlow의 한계와 방안

- 핵심 요약 : 컨트롤러 병목, 하드웨어 메모리 제약, 제어 채널 단절을 클러스터링, 규칙 집약, 폴백 모드로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 컨트롤러 병목 | 신규 흐름마다 Packet-In이 중앙 컨트롤러로 몰려 플로우 셋업 지연 증가 | 경로를 미리 설치하는 사전(Proactive) 규칙 배포, 분산 컨트롤러 클러스터 운영(ONOS(Open Network Operating System) 등) | 플로우 셋업 지연, 컨트롤러 CPU 사용률 |
| 메모리 용량 제약 | 고가의 TCAM(Ternary Content Addressable Memory) 용량 한계로 수용 가능한 플로우 엔트리 수 제한 | 와일드카드 규칙 집약, 테이블 분할 파이프라인 활용 | 테이블 사용률 |
| 제어 채널 단절 | 컨트롤러와 스위치 연결이 끊기면 신규 흐름 처리 불가로 전체 포워딩 마비 | Fail-Standalone 모드(스위치 구현에 따라 제공)로 일반 L2/L3 스위칭 폴백, 컨트롤러 이중화 | 제어 채널 가용률 |

## Ⅵ. OpenFlow에 대한 기술사적 제언

- 핵심 요약 : OpenFlow를 전면 도입하기보다 역할을 나누어 적용하고, 컨트롤러 이중화와 P4 전환 준비를 함께 진행하는 것이 현실적임.
- 데이터센터 패브릭은 VXLAN(Virtual Extensible LAN)과 BGP(Border Gateway Protocol) 기반 EVPN(Ethernet VPN) 같은 검증된 표준을 기본 구조로 두고, OpenFlow는 세부 패킷 조향처럼 범위가 좁은 영역에만 제한적으로 적용하는 편이 운영 복잡도를 낮춤.
- 컨트롤러는 단일 인스턴스로 두지 않고 3노드 이상의 클러스터로 구성하며, Raft 같은 합의 알고리즘으로 상태를 동기화해야 중앙 장애점을 피할 수 있음.
- 고정 헤더 필드의 한계를 넘는 서비스를 계획한다면, P4 기반 프로그래머블 데이터 평면과 DPU(Data Processing Unit) 스마트NIC 적용을 중장기 로드맵에 포함하는 것이 타당함.

## Ⅶ. 결론

- 핵심 요약 : OpenFlow는 제어와 전달을 분리해 SDN의 출발점을 연 개방형 사우스바운드 표준임.
- 시사점 : 중앙 제어의 개방성과 고정 헤더라는 제약이 함께 드러났으므로, 이후 기술 선택은 제어 확장성과 데이터 평면 유연성의 균형으로 판단하는 것이 타당함.
