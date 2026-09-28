from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

fixes = {
    "065_multi_region_active_active_dr.md": [
        ("리전 상태가 나빠지면 글로벌 라우팅에서 해당 리전을 제외하고 잔여 리전의 처리 용량과 데이터 복제 시점을 확인한다. 복귀 시에는 재동기화와 충돌을 해소한 뒤 트래픽을 다시 분배한다.",
         "리전 상태 이상 감지 시 글로벌 GSLB 라우팅에서 해당 리전을 배제하고 잔여 리전의 처리 용량과 복제 지연을 확인. 리전 복구 시에는 변경 데이터 재동기화 및 쓰기 충돌을 해소한 뒤 트래픽을 점진 분배.")
    ],
    "066_sk_hynix_hbm4_mass_production.md": [
        ("DRAM 다이를 준비해 TSV를 형성·검사하고 베이스 다이 위에 적층·접합한다. 인터포저에서 가속기와 연결한 후 전기·열·신뢰성을 검증한다.",
         "DRAM 다이에 TSV를 형성하여 테스트를 거친 후 로직 베이스 다이 위에 수직 적층 및 접합. 인터포저 상에서 GPU 가속기와 결합한 후 전기적, 열적 신뢰성 전수 검증.")
    ],
    "068_multi_region_active_active_disaster_recovery.md": [
        ("장애 상태를 확인한 뒤 영향 지역의 요청을 차단·재분배하고 복제 지점과 잔여 용량을 점검한다. 장애 지역을 복구할 때는 재동기화·정합성을 확인한 후 점진적으로 트래픽을 되돌린다.",
         "장애 상태 확인 후 영향 지역의 인입 트래픽을 차단 및 재분배하고 복제 시점과 잔여 컴퓨팅 용량을 점검. 정상 복구 시에는 양방향 재동기화 및 데이터 정합성을 확인한 후 트래픽 점진적 롤백.")
    ],
    "069_dynamic_memory_allocation_segmentation_fault.md": [
        ("잘못된 주소로 접근하면 MMU가 변환·권한을 검사하고 커널이 정상적인 수요 적재인지 판단한다. 해결할 수 없는 미매핑·권한 위반은 `SIGSEGV` 등으로 통지한다.",
         "비인가 주소 접근 시 MMU가 주소 변환 및 페이지 권한을 검사하여 커널 트랩 발생. 해결 불가능한 미매핑 및 권한 위반에 대해 커널이 `SIGSEGV` 시그널 전달.")
    ],
    "081_storage_virtualization.md": [
        ("논리 볼륨을 제공할 때 물리 상태를 확인하고 풀을 구성한 뒤 호스트 접근 권한과 다중 경로를 매핑한다. 이후 I/O마다 논리 주소를 물리 위치로 변환하며 복제·스냅샷의 쓰기 순서를 관리한다.",
         "논리 볼륨 제공 시 물리 스토리지 상태를 점검하여 풀을 구성하고 호스트 접근 권한과 멀티패스 I/O를 매핑. I/O 트랜잭션마다 논리 주소를 물리 블록 주소로 변환하며 스냅샷의 쓰기 순서 관리.")
    ],
    "082_das.md": [
        ("서버의 장치 드라이버가 연결 인터페이스를 통해 블록을 읽고 쓰며, 로컬 RAID를 쓰더라도 별도 장애영역의 백업·복제는 따로 설계한다.",
         "서버의 장치 드라이버가 전용 인터페이스를 통해 블록 I/O를 직접 수행하며, 로컬 RAID 적용 시에도 장애 격리를 위한 원격 백업 및 복제 체계 별도 설계 필요.")
    ],
    "083_gpgpu.md": [
        ("스레드는 개별 데이터 계산, 블록은 스레드 협력·자원 배치 단위다. 실행 묶음의 크기와 세부 스케줄링은 GPU 아키텍처에 따라 다르다.",
         "스레드는 개별 데이터 연산, 블록은 공유 메모리 기반 협업 및 자원 할당 단위 형성. 워프(Warp) 실행 단위의 크기와 스케줄링 메커니즘은 GPU 아키텍처 세대별로 상이.")
    ]
}

for fname, pair_list in fixes.items():
    fpath = TARGET_DIR / fname
    text = fpath.read_text(encoding="utf-8")
    for old, new in pair_list:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"Warning: pattern not found in {fname}: {old[:30]}...")
    fpath.write_text(text, encoding="utf-8")
    print(f"Updated {fname}")
