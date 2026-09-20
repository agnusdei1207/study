import fs from 'fs';
import path from 'path';

// Parse CLI args: optional folder name, defaults to checking newly formatted folders
const targetDirArg = process.argv[2];

const keywordPrioritiesDir = 'C:/workspace/memories/contexts/cspe/current/keyword-priorities';

// Map of folder to priority file
const folderMap = {
  '01-basic-theory': 'basic-theory.md',
  '02-hardware': 'hardware.md',
  '03-software': 'software.md',
  '04-network': 'network.md',
  '05-security': 'security.md',
  '06-evaluation': 'evaluation.md',
  '07-law-policy': 'law-policy.md',
  '08-latest-tech': 'latest-tech.md',
};

// Load topic priorities
function loadTopicPriorities(priorityFile) {
  const filePath = path.join(keywordPrioritiesDir, priorityFile);
  if (!fs.existsSync(filePath)) return new Map();

  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  const topics = new Map();

  for (const line of lines) {
    // | 번호 | 토픽 | 등급 | 중요도 | 흡수한 하위 키워드 | 근거 |
    const match = line.match(/^\|\s*(\d{2}-\d{3})\s*\|\s*([^|]+)\s*\|\s*([ABC])\s*\|\s*(\d+)%\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|/);
    if (match) {
      const [_, no, name, grade, priority, absorbed, basis] = match;
      const absorbedList = absorbed.trim() === '-' ? [] : absorbed.split(',').map(s => s.trim()).filter(Boolean);
      const isOfficialExam = /\[출제:([^\]]+)\]/.test(basis);
      const examMatch = basis.match(/\[출제:([^\]]+)\]/);
      let sourceHistory = '';
      if (examMatch) {
        // e.g. "122,125" -> "122회, 125회"
        sourceHistory = examMatch[1].split(',').map(s => s.trim() + '회').join(', ');
      }
      topics.set(no, {
        no,
        name: name.trim(),
        grade,
        priority: parseInt(priority, 10),
        absorbed: absorbedList,
        basis: basis.trim(),
        sourceStatus: isOfficialExam ? '기출' : '미출',
        sourceHistory,
      });
    }
  }
  return topics;
}

function validateFile(filePath, topicInfo) {
  const errors = [];
  const content = fs.readFileSync(filePath, 'utf8');

  // 1. Frontmatter validation
  const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fmMatch) {
    errors.push('frontmatter가 없습니다.');
    return errors;
  }
  const fm = fmMatch[1];

  if (topicInfo) {
    // Check badge text
    const badgeMatch = fm.match(/text:\s*["']?([^"'\r\n]+)["']?/);
    const expectedBadge = `${topicInfo.grade} · ${topicInfo.sourceStatus} · ${topicInfo.priority}%`;
    if (!badgeMatch || badgeMatch[1].trim() !== expectedBadge) {
      errors.push(`badge.text 불일치: '${badgeMatch ? badgeMatch[1].trim() : ''}' != '${expectedBadge}'`);
    }

    // Check source_status
    const statusMatch = fm.match(/source_status:\s*["']?([^"'\r\n]+)["']?/);
    if (!statusMatch || statusMatch[1].trim() !== topicInfo.sourceStatus) {
      errors.push(`source_status 불일치: '${statusMatch ? statusMatch[1].trim() : ''}' != '${topicInfo.sourceStatus}'`);
    }

    // Check priority
    const priorityMatch = fm.match(/priority:\s*(\d+)/);
    if (!priorityMatch || parseInt(priorityMatch[1], 10) !== topicInfo.priority) {
      errors.push(`priority 불일치: '${priorityMatch ? priorityMatch[1] : ''}' != '${topicInfo.priority}'`);
    }

    // Check absorbed keywords present in body
    for (const abs of topicInfo.absorbed) {
      // Extract keyword name from "04-065 채널 용량 — 섀넌 한계" -> "섀넌 한계" or "채널 용량"
      const absParts = abs.replace(/^\d{2}-\d{3}\s*/, '').split(/[—\-]/).map(s => s.trim()).filter(Boolean);
      const found = absParts.some(part => content.includes(part));
      if (!found) {
        errors.push(`흡수 키워드 누락: 본문에 '${abs}' 관련 내용이 없습니다.`);
      }
    }
  }

  const body = content.slice(fmMatch[0].length);

  // 2. First section must be "## 답안 골격"
  const firstHeadingMatch = body.match(/^##\s+([^\r\n]+)/m);
  if (!firstHeadingMatch || firstHeadingMatch[1].trim() !== '답안 골격') {
    errors.push(`첫 절이 '## 답안 골격'이 아닙니다: '${firstHeadingMatch ? firstHeadingMatch[1] : '없음'}'`);
  }

  // 3. Section structure check by grade
  const headings = [...body.matchAll(/^##\s+([^\r\n]+)/gm)].map(m => m[1].trim());

  if (topicInfo?.grade === 'C') {
    const forbiddenForC = ['문제·원인·대책', '내 의견', '찾아볼 것', '핵심 용어', '딸려 나오는 하위 토픽'];
    for (const f of forbiddenForC) {
      if (headings.includes(f)) {
        errors.push(`C등급에 허용되지 않는 절이 포함됨: '## ${f}'`);
      }
    }
    const requiredForC = ['답안 골격', '한 줄 본질', '핵심 그림', '핵심 통찰', '이웃 토픽과 구분', '이렇게 출제된다'];
    for (const r of requiredForC) {
      if (!headings.includes(r)) {
        errors.push(`C등급 필수 절 누락: '## ${r}'`);
      }
    }
  } else if (topicInfo?.grade === 'A' || topicInfo?.grade === 'B') {
    const requiredForAB = [
      '답안 골격',
      '한 줄 본질',
      '핵심 그림',
      '핵심 통찰',
      '이웃 토픽과 구분',
      '문제·원인·대책',
      '이렇게 출제된다',
      '내 의견'
    ];
    for (const r of requiredForAB) {
      if (!headings.includes(r)) {
        errors.push(`${topicInfo.grade}등급 필수 절 누락: '## ${r}'`);
      }
    }
    if (topicInfo.absorbed && topicInfo.absorbed.length > 0) {
      if (!headings.includes('딸려 나오는 하위 토픽')) {
        errors.push(`흡수 키워드가 있으나 '## 딸려 나오는 하위 토픽' 절이 누락됨`);
      }
    }
  }

  // 4. "핵심 그림" code block line count <= 15
  const coreDiagramMatch = body.match(/## 핵심 그림[\r\n]+([\s\S]*?)(?=\r?\n## |$)/);
  if (coreDiagramMatch) {
    const codeBlockMatch = coreDiagramMatch[1].match(/```(?:text)?\r?\n([\s\S]*?)\r?\n```/);
    if (codeBlockMatch) {
      const codeLines = codeBlockMatch[1].split(/\r?\n/).length;
      if (codeLines > 15) {
        errors.push(`핵심 그림 코드 블록이 15줄을 초과함 (${codeLines}줄)`);
      }
    }
  }

  // 5. "문제·원인·대책" section checks
  const problemSectionMatch = body.match(/## 문제·원인·대책[\r\n]+([\s\S]*?)(?=\r?\n## |$)/);
  if (problemSectionMatch) {
    const pText = problemSectionMatch[1];
    
    // Case line check
    const caseMatch = pText.match(/-\s*사례:([^\r\n]+)/);
    if (caseMatch) {
      const caseLine = caseMatch[1].trim();
      if (!caseLine.includes('(출처:') && !caseLine.endsWith(')')) {
        errors.push(`사례 줄에 (출처: ...) 표기가 없습니다: '- 사례: ${caseLine}'`);
      }
      if (/^\d+회\s*기출/.test(caseLine)) {
        errors.push(`사례 줄이 'N회 기출'로 시작합니다: '- 사례: ${caseLine}'`);
      }
    }

    // Check % or 배 in table
    const tableMatch = pText.match(/\|[\s\S]*?\|/);
    if (tableMatch) {
      const tableRows = pText.split(/\r?\n/).filter(line => line.startsWith('|') && !line.includes('---'));
      // skip header row
      const dataRows = tableRows.slice(1);
      for (const row of dataRows) {
        if (/\d+%/g.test(row)) {
          errors.push(`문제·원인·대책 표에 숫자+% 표기 포함: '${row.trim()}'`);
        }
        if (/\d+배/g.test(row)) {
          errors.push(`문제·원인·대책 표에 숫자+배 표기 포함: '${row.trim()}'`);
        }
      }
    }
  }

  // 6. "내 의견" section checks
  const opinionSectionMatch = body.match(/## 내 의견[\r\n]+([\s\S]*?)(?=\r?\n## |$)/);
  if (opinionSectionMatch) {
    const oText = opinionSectionMatch[1];
    if (/\d+%/g.test(oText)) {
      errors.push(`내 의견에 숫자+% 표기 포함: '${oText.trim()}'`);
    }
    if (/\d+배/g.test(oText)) {
      errors.push(`내 의견에 숫자+배 표기 포함: '${oText.trim()}'`);
    }
  }

  return errors;
}

// Run validation
let foldersToCheck = [];
if (targetDirArg) {
  foldersToCheck = [path.resolve(targetDirArg)];
} else {
  // Check any 01-basic-theory ~ 08-latest-tech in notes/cspe
  const cspeNotes = path.resolve('src/content/docs/notes/cspe');
  const baseNotes = fs.existsSync(cspeNotes) ? cspeNotes : path.resolve('src/content/docs/notes');
  for (const f of Object.keys(folderMap)) {
    const full = path.join(baseNotes, f);
    if (fs.existsSync(full)) {
      foldersToCheck.push(full);
    }
  }
}

if (foldersToCheck.length === 0) {
  console.log('검사할 대상 폴더가 없습니다.');
  process.exit(0);
}

let totalErrors = 0;
let totalFiles = 0;

for (const dir of foldersToCheck) {
  const folderName = path.basename(dir);
  const priorityFile = folderMap[folderName];
  const topicMap = priorityFile ? loadTopicPriorities(priorityFile) : new Map();

  console.log(`\n=== 검사 시작: ${folderName} (등록 토픽 수: ${topicMap.size}) ===`);

  const files = fs.readdirSync(dir).filter(f => f.endsWith('.md') && f !== 'index.md');
  totalFiles += files.length;

  for (const file of files) {
    const filePath = path.join(dir, file);
    // extract topic number: e.g. "028_hamming_code.md" -> "01-028"
    const prefix = folderName.slice(0, 2);
    const noMatch = file.match(/^(\d{3})_/);
    let topicInfo = null;
    if (noMatch) {
      const topicId = `${prefix}-${noMatch[1]}`;
      topicInfo = topicMap.get(topicId);
    }

    const errors = validateFile(filePath, topicInfo);
    if (errors.length > 0) {
      totalErrors += errors.length;
      console.log(`\n[오류] ${file} (토픽: ${topicInfo ? topicInfo.no + ' ' + topicInfo.name : '미식별'}):`);
      for (const e of errors) {
        console.log(`  - ${e}`);
      }
    }
  }
}

console.log(`\n========================================`);
console.log(`검사 완료: 총 ${totalFiles}개 파일 검사, 오류 ${totalErrors}건 발견`);
console.log(`========================================`);

if (totalErrors > 0) {
  process.exit(1);
} else {
  process.exit(0);
}
