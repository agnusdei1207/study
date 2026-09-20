import fs from 'fs';
import path from 'path';

const memoryBase = 'C:/workspace/memories/contexts/cspe/current';
const cspeSrcDir = path.join(memoryBase, 'keyword-priorities');
const itpeSrcDir = path.join(memoryBase, 'itpe-keyword-priorities');

const cspeTargetDir = path.resolve('agent-guides/keywords/cspe');
const itpeTargetDir = path.resolve('agent-guides/keywords/itpe');

fs.mkdirSync(cspeTargetDir, { recursive: true });
fs.mkdirSync(itpeTargetDir, { recursive: true });

const cspeSubjects = [
  { id: '01', file: 'basic-theory.md', folder: '01-basic-theory', title: '01 컴퓨터 기초이론 토픽', count: 59 },
  { id: '02', file: 'hardware.md', folder: '02-hardware', title: '02 하드웨어 시스템 토픽', count: 87 },
  { id: '03', file: 'software.md', folder: '03-software', title: '03 시스템·응용 SW 토픽', count: 157 },
  { id: '04', file: 'network.md', folder: '04-network', title: '04 통신·네트워크 토픽', count: 116 },
  { id: '05', file: 'security.md', folder: '05-security', title: '05 시스템 보안 토픽', count: 130 },
  { id: '06', file: 'evaluation.md', folder: '06-evaluation', title: '06 시스템 평가 토픽', count: 41 },
  { id: '07', file: 'law-policy.md', folder: '07-law-policy', title: '07 법규·정책·표준 토픽', count: 73 },
  { id: '08', file: 'latest-tech.md', folder: '08-latest-tech', title: '08 최신 기술 동향 토픽', count: 113 },
];

for (const sub of cspeSubjects) {
  const srcPath = path.join(cspeSrcDir, sub.file);
  const content = fs.readFileSync(srcPath, 'utf8');
  const body = content.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');

  const tableMatch = body.match(/(\| 번호 \|[\s\S]*?)(?=\r?\n## |$)/);
  if (!tableMatch) continue;
  const table = tableMatch[1].trim();

  let transferredSection = '';
  const transferredMatch = body.match(/(## 다른 과목 토픽으로 넘긴 키워드[\s\S]*?)(?=\r?\n## 보류|\r?\n## |$)/);
  if (transferredMatch) {
    transferredSection = '\n\n' + transferredMatch[1].trim();
  }

  const publicContent = `# ${sub.title}

> ${sub.count}개. 노트 폴더는 \`src/content/docs/notes/cspe/${sub.folder}/\`, 파일명은 \`{3자리 번호}_{영문 snake_case}.md\`다. 표기는 [README](../README.md)를 본다.

${table}${transferredSection}
`;

  const destPath = path.join(cspeTargetDir, `${sub.folder}.md`);
  fs.writeFileSync(destPath, publicContent, 'utf8');
}

const itpeSubjects = [
  { id: '01', file: '01-it-strategy.md', folder: '01-it-strategy', title: '01 정보 전략 및 관리 토픽', count: 87 },
  { id: '02', file: '02-software-engineering.md', folder: '02-software-engineering', title: '02 소프트웨어 공학 토픽', count: 139 },
  { id: '03', file: '03-data.md', folder: '03-data', title: '03 자료처리·데이터·통계 토픽', count: 110 },
  { id: '04', file: '04-computer-system.md', folder: '04-computer-system', title: '04 컴퓨터 시스템 토픽', count: 89 },
  { id: '05', file: '05-network.md', folder: '05-network', title: '05 정보통신 토픽', count: 52 },
  { id: '06', file: '06-security.md', folder: '06-security', title: '06 정보보안 토픽', count: 119 },
  { id: '07', file: '07-latest-tech.md', folder: '07-latest-tech', title: '07 최신 기술 동향 토픽', count: 99 },
  { id: '08', file: '08-law-policy.md', folder: '08-law-policy', title: '08 법규 및 정책 토픽', count: 54 },
];

for (const sub of itpeSubjects) {
  const srcPath = path.join(itpeSrcDir, sub.file);
  if (!fs.existsSync(srcPath)) continue;
  const content = fs.readFileSync(srcPath, 'utf8');
  const body = content.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');

  const tableMatch = body.match(/(\| 번호 \|[\s\S]*?)(?=\r?\n## |$)/);
  if (!tableMatch) continue;
  const table = tableMatch[1].trim();

  let transferredSection = '';
  const transferredMatch = body.match(/(## 다른 과목 토픽으로 넘긴 키워드[\s\S]*?)(?=\r?\n## 보류|\r?\n## |$)/);
  if (transferredMatch) {
    transferredSection = '\n\n' + transferredMatch[1].trim();
  }

  const publicContent = `# ${sub.title}

> 노트 폴더는 \`src/content/docs/notes/itpe/${sub.folder}/\`, 파일명은 \`{3자리 번호}_{영문 snake_case}.md\`다. 표기는 [README](../README.md)를 본다.

${table}${transferredSection}
`;

  const destPath = path.join(itpeTargetDir, `${sub.folder}.md`);
  fs.writeFileSync(destPath, publicContent, 'utf8');
}

console.log('Synchronized public keyword lists for both CSPE and ITPE.');
