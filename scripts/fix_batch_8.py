import os
import re

files_to_fix = [
    'src/content/docs/notes/itpe/02-software-engineering/166_web_crawling.md',
    'src/content/docs/notes/itpe/02-software-engineering/168_maintenance_and_3r.md',
    'src/content/docs/notes/itpe/02-software-engineering/176_chaos_test.md',
    'src/content/docs/notes/itpe/02-software-engineering/179_integration_test.md',
    'src/content/docs/notes/itpe/02-software-engineering/181_waterfall_methodology.md',
    'src/content/docs/notes/itpe/02-software-engineering/182_eip.md',
    'src/content/docs/notes/itpe/02-software-engineering/183_web_2_0.md',
    'src/content/docs/notes/itpe/02-software-engineering/184_public_sw_project_guide.md',
    'src/content/docs/notes/itpe/02-software-engineering/185_cmmi.md',
    'src/content/docs/notes/itpe/02-software-engineering/186_html5.md',
    'src/content/docs/notes/itpe/02-software-engineering/187_soa.md',
    'src/content/docs/notes/itpe/02-software-engineering/188_functional_safety.md',
    'src/content/docs/notes/itpe/02-software-engineering/190_modularity.md',
    'src/content/docs/notes/itpe/02-software-engineering/191_performance_test.md',
    'src/content/docs/notes/itpe/02-software-engineering/199_ajax.md',
    'src/content/docs/notes/itpe/02-software-engineering/200_ejb.md',
    'src/content/docs/notes/itpe/02-software-engineering/201_record_and_replay_testing.md',
    'src/content/docs/notes/itpe/02-software-engineering/202_sad.md',
    'src/content/docs/notes/itpe/02-software-engineering/203_low_code_no_code.md',
    'src/content/docs/notes/itpe/02-software-engineering/204_java_gui_toolkit.md',
    'src/content/docs/notes/itpe/02-software-engineering/205_abstract_class_and_interface.md',
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
    content = re.sub(r'적용 권장\.', '적용 필요.', content)
    content = re.sub(r'설계 권장\.', '설계 체계 확립.', content)
    content = re.sub(r'전환 권장\.', '전환 필요.', content)
    content = re.sub(r'권장\.', '필요.', content)

    # 2. Fix specific wide lines
    # 181_waterfall_methodology
    content = re.sub(
        r'\[구현/코딩 \(Implementation\)\]   ──► 소스코드 / 단위테스트 완료  ──► \[개발 기준선: Development Baseline\]',
        '[구현/코딩] ──► 소스코드/단위테스트 완료 ──► [개발 기준선]',
        content
    )
    content = re.sub(
        r'  \[Upfront Waterfall\]           \[Agile Sprint Iterations\]          \[Downstream Waterfall\]',
        '  [Upfront Waterfall]       [Agile Sprint Iterations]       [Downstream Waterfall]',
        content
    )
    # 182_eip
    content = re.sub(
        r'                                                                      └─ 실패 시 AWS SQS Dead Letter Queue 이관',
        '                                                                └─ 실패 시 DLQ 이관',
        content
    )
    # 186_html5
    content = re.sub(
        r'컴포넌트 설계 \(시맨틱 태그 \+ WAI-ARIA\) → 빌드/번들링 \(Polyfill 주입\) → Lighthouse 접근성\(A11y\) 100점 검증 → PWA 배포',
        '컴포넌트 설계 (시맨틱+ARIA) → 번들링 (Polyfill) → 접근성 100점 검증 → PWA 배포',
        content
    )
    # 187_soa
    content = re.sub(
        r'채널 영역 \(Cloud Native MSA / API Gateway\) ──► EIP/ESB 연계 계층 ──► 코어 백엔드 영역 \(전통적 SOA / 메인프레임\)',
        '채널 영역 (Cloud Native MSA) ──► EIP/ESB 연계 계층 ──► 코어 영역 (전통 SOA)',
        content
    )
    # 188_functional_safety
    content = re.sub(
        r'위험 분석 \(HARA \+ TARA\) → 복합 안전/보안 요구사항 도출 → MISRA 시큐어 코딩 → MC/DC 커버리지 & 결함 주입 시험 → Safety Case',
        '위험 분석 (HARA+TARA) → 안전 요구 도출 → MISRA 코딩 → MC/DC 검증 → Safety Case',
        content
    )
    # 199_ajax
    content = re.sub(
        r'사용자 클릭 ──► \[HTTP Request\] ──► 서버 처리 ──► \[전체 HTML Response\] ──► 브라우저 화면 백지화 후 전체 렌더링',
        '사용자 클릭 ──► [HTTP Request] ──► 서버 처리 ──► [HTML 응답] ──► 전체 렌더링',
        content
    )
    content = re.sub(
        r'                                              └──► Fetch API 백그라운드 통신 \(AbortController 취소 관리\)',
        '                                              └──► Fetch 통신 (AbortController 관리)',
        content
    )
    # 200_ejb
    content = re.sub(
        r'\[레거시 EJB 시스템\] ──► 비즈니스 로직 추출 \(POJO 화\) ──► Spring Boot / Quarkus 컨테이너 패키징 ──► Kubernetes 배포',
        '[레거시 EJB] ──► 비즈니스 로직 POJO화 ──► Spring Boot 패키징 ──► K8s 배포',
        content
    )
    # 201_record_and_replay_testing
    content = re.sub(
        r'                                └──► Shadow Pod v2 \(0% 비동기 검증 / DB Mocking\) ──► Datadog Diff 대시보드',
        '                                └──► Shadow Pod (DB Mocking) ──► Diff 대시보드',
        content
    )
    # 204_java_gui_toolkit
    content = re.sub(
        r'FXML\(마크업\) \+ CSS \+ 자바 컨트롤러 ──► 씬 그래프 \(Scene Graph\) ──► Prism 가속 엔진 \(DirectX/OpenGL\)',
        'FXML + CSS + 컨트롤러 ──► 씬 그래프 (Scene Graph) ──► Prism 가속 엔진',
        content
    )
    content = re.sub(
        r'                                          ├─ \[EDT에서 직접 수행\] ──► 화면 멈춤\(Freezing\) 발생 \(치명적\)',
        '                                          ├─ [EDT 직접 수행] ──► 화면 멈춤 발생',
        content
    )
    content = re.sub(
        r'                                               - done\(\) / SwingUtilities\.invokeLater\(\) 로',
        '                                               - done() / invokeLater() 로',
        content
    )
    content = re.sub(
        r'FXML \(뷰\) \+ CSS \(스타일\) ──► Controller \(MVVM 바인딩\) ──► 백그라운드 Service \(비동기 HTTP/DB\) ──► Prism 하드웨어 가속',
        'FXML + CSS ──► Controller (바인딩) ──► 비동기 Service ──► Prism 하드웨어 가속',
        content
    )

    # 3. Footer extraction & reordering
    m_conn = re.search(r'## 연결 토픽\s*\n(.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    conn_items = m_conn.group(1).strip() if m_conn else ""

    m_hist = re.search(r'## 출제 이력[^\n]*\n(.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    hist_raw = m_hist.group(1).strip() if m_hist else ""

    hist_lines = []
    if hist_raw:
        for line in hist_raw.split('\n'):
            line_clean = line.strip()
            if not line_clean:
                continue
            if '컴퓨터시스템응용' in line_clean:
                continue
            hist_lines.append(line_clean)

    if not hist_lines:
        hist_lines.append('- 정보관리기술사 출제기준: 소프트웨어공학 표준 및 실무 가이드라인')

    hist_formatted = '\n'.join(hist_lines)

    # Find where footer starts
    positions = [pos for pos in [content.find('## 연결 토픽'), content.find('## 출제 이력')] if pos != -1]
    if positions:
        first_footer_pos = min(positions)
        pre_content = content[:first_footer_pos].rstrip()
    else:
        pre_content = content.rstrip()

    if not pre_content.endswith('---'):
        pre_content = pre_content + '\n\n---'

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
