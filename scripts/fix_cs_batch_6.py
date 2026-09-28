import re
import glob

files = sorted(glob.glob('src/content/docs/notes/itpe/04-computer-system/*.md'))[94:]

for f in files:
    if 'index.md' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()

    orig = c

    # 1. Convert ### Ⅰ~Ⅴ to ## Ⅰ~Ⅴ
    c = re.sub(r'^###\s+([Ⅰ-Ⅴ]\.)', r'## \1', c, flags=re.MULTILINE)

    # 2. Remove stray '#' lines
    c = re.sub(r'^\s*#\s*$', '', c, flags=re.MULTILINE)

    # 3. Fix 106 ending
    c = c.replace(
        "리허설에서는 데이터 건수뿐 아니라 업무 합계·대표 기능·복구 소요시간을 실제 전환 시나리오와 비교한다.",
        "리허설 단계에서 데이터 건수뿐 아니라 업무 합계·대표 기능·복구 소요시간을 실제 전환 시나리오와 대조 실측."
    )

    # 4. Fix 107 ending
    c = c.replace(
        "백필 완료 상태만으로 업무 정합성을 보장하지 않는다. 논리 구간·시간대·워크플로 버전을 기록하고 결과를 검증한다.",
        "백필 완료 상태만으로 업무 정합성 담보가 불가하므로 논리 구간·시간대·워크플로 버전을 기록하고 결과를 정밀 대조 검증."
    )

    # 5. Fix 111 mechanical ending
    c = c.replace(
        "- 메커니즘: 각 행·열의 양 끝을 연결해 최단 경로가 경계를 넘어 순환하도록 함",
        "- 메커니즘: 각 행·열의 양 끝을 연결해 최단 경로가 경계를 넘어 환형 구조로 순환"
    )

    # 6. Fix 122 mechanical ending
    c = c.replace(
        "상한선(Bound)이 존재하여 기아 상태(Starvation)가 배제되어야 함",
        "상한선(Bound)이 존재하여 기아 상태(Starvation) 사전 방지 및 배제 보장"
    )

    # 7. Fix 123 ending
    c = c.replace(
        "복제·Snapshot·RAID·Erasure Coding·Versioning은 제품 구현 선택이므로 특정 저장 유형의 필수 속성으로 단정하지 않는다.",
        "복제·Snapshot·RAID·Erasure Coding·Versioning은 제품 구현 선택이므로 특정 저장 유형의 고유 필수 속성으로 단정 배제."
    )

    if c != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Fixed {f}")
print("Batch 6 fix completed.")
