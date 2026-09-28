from pathlib import Path

TARGET_DIR = Path("src/content/docs/notes/itpe/04-computer-system")

fixes = {
    "030_chiplet_ucie_3_0.md": [
        ("송신 칩렛의 데이터는 프로토콜·어댑터와 UCIe PHY를 지나 패키지 배선으로 전달되고, 수신 칩렛의 PHY와 기능 블록에서 처리된다.",
         "송신 칩렛의 데이터는 프로토콜, 어댑터와 UCIe PHY를 거쳐 패키지 배선으로 전송되고, 수신 칩렛의 PHY와 기능 블록에서 디스패칭 처리.")
    ],
    "037_vdi.md": [
        ("- 통찰: 사용자의 데스크톱 환경을 중앙 데이터센터 서버의 가상머신에 격리 호스팅하고 화면 픽셀만을 암호화 스트리밍하여 보안성과 원격 근무 연속성을 보장함.",
         "- 통찰: 사용자의 데스크톱 환경을 중앙 데이터센터 서버의 가상머신에 격리 호스팅하고 화면 픽셀만을 암호화 스트리밍하여 보안성과 원격 근무 연속성을 보장 체계화.")
    ],
    "043_datacenter_location_disaster_response.md": [
        ("재난 시 주 센터 장애를 감지하면 업무 우선순위를 결정하고, 대체 센터 데이터·서비스 상태를 확인한 뒤 접속 경로를 전환해 기능·정합성을 검증한다.",
         "재난 시 주 센터 장애를 감지하면 업무 우선순위에 따라 BIA를 적용하고, 대체 센터 데이터 및 서비스 상태를 검증한 뒤 GSLB 접속 경로를 전환하여 무결성 확인.")
    ],
    "044_idc_geographic_site_selection.md": [
        ("목표 용량·확장 시점을 정한 뒤 후보지의 공급 가능성을 조사하고, 위험·비용·일정을 비교해 현장·공급자 근거를 확인한 뒤 입지와 증설 계획을 확정한다.",
         "목표 수전 용량과 확장 시점을 정의한 뒤 후보지의 전력/수자원 공급 능력을 실사하고, 자연재해 위험과 인입 비용을 종합 비교하여 최종 입지 확정.")
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
