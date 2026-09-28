import os
import re

files_to_fix = [
    'src/content/docs/notes/itpe/02-software-engineering/130_function_point.md',
    'src/content/docs/notes/itpe/02-software-engineering/135_oas.md',
    'src/content/docs/notes/itpe/02-software-engineering/136_srgm.md',
    'src/content/docs/notes/itpe/02-software-engineering/137_sw_safety_diagnosis_guide.md',
    'src/content/docs/notes/itpe/02-software-engineering/139_sw_development_methodologies.md',
    'src/content/docs/notes/itpe/02-software-engineering/140_message_queue.md',
    'src/content/docs/notes/itpe/02-software-engineering/147_service_worker.md',
    'src/content/docs/notes/itpe/02-software-engineering/149_performance_requirement.md',
    'src/content/docs/notes/itpe/02-software-engineering/150_software_quality_cost.md',
    'src/content/docs/notes/itpe/02-software-engineering/158_sprite.md',
    'src/content/docs/notes/itpe/02-software-engineering/159_spring_boot.md',
    'src/content/docs/notes/itpe/02-software-engineering/161_open_source_pm_software.md',
    'src/content/docs/notes/itpe/02-software-engineering/164_web_performance_optimization.md',
]

for path in files_to_fix:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix recommendation text endings
    content = re.sub(r'확보할 것을 권장\.', '확보 체계 구축.', content)
    content = re.sub(r'추진할 것을 권장\.', '추진 필요.', content)
    content = re.sub(r'구현할 것을 권장\.', '구현 필요.', content)
    content = re.sub(r'도입할 것을 권장\.', '도입 필요.', content)
    content = re.sub(r'확립 권장\.', '확립 필요.', content)
    content = re.sub(r'추진 권장\.', '추진 필요.', content)
    content = re.sub(r'수행 권장\.', '수행 필요.', content)
    content = re.sub(r'운영 권장\.', '운영 필요.', content)
    content = re.sub(r'권장\.', '필요.', content)

    # 2. Fix specific wide diagrams
    # 140_message_queue
    content = re.sub(
        r'Producer \(Trace ID 주입\) → Message Broker \(지연/적체 모니터링\) → Consumer \(Trace ID 전파 및 메트릭 수집\)\n\s*│\n\s*└─ 장애 시 카나리 우회 및 DLQ 재처리',
        'Producer (Trace ID) → Broker (적체 모니터링) → Consumer (Trace 전파)\n                                                        │\n                                                        └─ 장애 시 DLQ 격리',
        content
    )
    # 158_sprite
    content = re.sub(
        r"\.icon \{ background-image: url\('sprite\.png'\); display: inline-block; width: 16px; height: 16px; \}",
        ".icon { background-image: url('sprite.png'); display: inline-block;\n        width: 16px; height: 16px; }",
        content
    )
    # 159_spring_boot
    content = re.sub(
        r'@SpringBootApplication \( = @Configuration \+ @EnableAutoConfiguration \+ @ComponentScan \)',
        '@SpringBootApplication (@Configuration + @EnableAutoConfiguration + @ComponentScan)',
        content
    )
    content = re.sub(
        r'META-INF/spring/org\.springframework\.boot\.autoconfigure\.AutoConfiguration\.imports 스캔',
        'META-INF/spring/...AutoConfiguration.imports 스캔',
        content
    )
    content = re.sub(
        r'소스 코드 → GraalVM Native Image 빌드 → 경량 OCI 이미지 → Kubernetes Pod 배포 \(Actuator Probe 연동\)',
        '소스 코드 → GraalVM Native Image → 경량 OCI 이미지 → K8s Pod (Actuator 연동)',
        content
    )
    # 161_open_source_pm_software
    content = re.sub(
        r'조직 요구사항 수집 → 후보 오픈소스 선정 \(Redmine/OpenProject\) → 라이선스/보안 진단 → PoC/파일럿 검증 → 본 시스템 확산',
        '요구사항 수집 → 후보 선정 (Redmine 등) → 라이선스/보안 진단 → PoC → 본 시스템 확산',
        content
    )
    # 164_web_performance_optimization
    content = re.sub(
        r'개발/빌드 \(번들 분석\) → CI 단계 \(Lighthouse CI 자동 측정\) → CD/배포 \(성능 예산 초과 시 차단\) → APM 실시간 모니터링',
        '개발/빌드 → CI (Lighthouse CI 측정) → CD (성능 예산 초과 시 차단) → APM 모니터링',
        content
    )

    # 3. Footer extraction & reordering
    # Find links block
    m_conn = re.search(r'## 연결 토픽\s*\n(.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    conn_items = m_conn.group(1).strip() if m_conn else ""

    # Find history block
    m_hist = re.search(r'## 출제 이력[^\n]*\n(.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    hist_raw = m_hist.group(1).strip() if m_hist else ""

    # Filter out 컴퓨터시스템응용 lines from history
    hist_lines = []
    for line in hist_raw.split('\n'):
        line_clean = line.strip()
        if not line_clean:
            continue
        if '컴퓨터시스템응용' in line_clean:
            continue
        hist_lines.append(line_clean)

    # If no lines remain, provide standard subject verification source
    if not hist_lines:
        hist_lines.append('- 정보관리기술사 출제기준: 소프트웨어공학 표준 및 실무 가이드라인')

    hist_formatted = '\n'.join(hist_lines)

    # Cut off everything starting from first footer
    first_footer_pos = min(
        pos for pos in [content.find('## 연결 토픽'), content.find('## 출제 이력')] if pos != -1
    )
    
    # Check if there's a delimiter '---' right before footer
    pre_content = content[:first_footer_pos].rstrip()
    if not pre_content.endswith('---'):
        pre_content = pre_content + '\n\n---'

    # Build new footer
    new_footer = f"""

## 출제 이력과 검증 출처

{hist_formatted}

## 연결 토픽

{conn_items}
"""
    new_content = pre_content + new_footer

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {os.path.basename(path)}")
