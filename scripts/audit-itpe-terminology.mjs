import fs from 'node:fs';
import path from 'node:path';

// Reviewed title names, not a global replacement dictionary for prose.
// Same spelling can have different meanings (IP, FP, MAC, TAM, SOM, etc.).
// This audit catches known regressions; it cannot prove all factual claims.
export const root = 'src/content/docs/notes/itpe';
export const names = {
  AI: 'Artificial Intelligence', IT: 'Information Technology', SW: 'Software',
  ISO: 'International Organization for Standardization', IEC: 'International Electrotechnical Commission',
  IEEE: 'Institute of Electrical and Electronics Engineers', NIST: 'National Institute of Standards and Technology',
  EU: 'European Union', UN: 'United Nations', KISA: 'Korea Internet & Security Agency',
  IITP: 'Institute of Information & Communications Technology Planning & Evaluation',
  ISMP: 'Information System Master Plan', ISP: 'Information Strategy Planning',
  PMO: 'Project Management Office', SCM: 'Supply Chain Management', SLA: 'Service Level Agreement',
  WBS: 'Work Breakdown Structure', BPR: 'Business Process Reengineering',
  ESG: 'Environmental, Social and Governance', BSC: 'Balanced Scorecard',
  RTO: 'Recovery Time Objective', RPO: 'Recovery Point Objective', DR: 'Disaster Recovery',
  DX: 'Digital Transformation', BCP: 'Business Continuity Plan', CRM: 'Customer Relationship Management',
  EVM: 'Earned Value Management', RMF: 'Risk Management Framework', POP: 'Point of Production',
  DRS: 'Disaster Recovery System', ITSM: 'IT Service Management',
  MECE: 'Mutually Exclusive, Collectively Exhaustive', RFP: 'Request for Proposal',
  PLM: 'Product Lifecycle Management', COQ: 'Cost of Quality', EA: 'Enterprise Architecture',
  ITA: 'Information Technology Architecture', CCPM: 'Critical Chain Project Management', TOC: 'Theory of Constraints',
  TAM: 'Total Addressable Market', SAM: 'Serviceable Addressable Market', SOM: 'Serviceable Obtainable Market',
  SWOT: 'Strengths, Weaknesses, Opportunities, Threats',
  '3C': 'Customer, Competitor, Company', PEST: 'Political, Economic, Social, Technological',
  DMAIC: 'Define, Measure, Analyze, Improve, Control',
  REST: 'Representational State Transfer', SOAP: 'Simple Object Access Protocol',
  UML: 'Unified Modeling Language', API: 'Application Programming Interface',
  FP: 'Function Point', LOC: 'Lines of Code', COCOMO: 'Constructive Cost Model',
  FTA: 'Fault Tree Analysis', FMEA: 'Failure Mode and Effects Analysis', HAZOP: 'Hazard and Operability Study',
  MSA: 'Microservice Architecture', SRS: 'Software Requirements Specification',
  TA: 'Technical Architect', AA: 'Application Architect', SQA: 'Software Quality Assurance',
  EDA: 'Event-Driven Architecture', SOLID: 'Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion',
  DIP: 'Dependency Inversion Principle', OOP: 'Object-Oriented Programming',
  MIL: 'Model-in-the-Loop', SIL: 'Software-in-the-Loop', PIL: 'Processor-in-the-Loop', HIL: 'Hardware-in-the-Loop',
  SPL: 'Software Product Line', SRGM: 'Software Reliability Growth Model', DAG: 'Directed Acyclic Graph',
  HTML5: 'HyperText Markup Language 5', LCNC: 'Low-Code/No-Code', GUI: 'Graphical User Interface',
  AWT: 'Abstract Window Toolkit', PM: 'Project Management',
  NoSQL: 'Not Only SQL', ERD: 'Entity-Relationship Diagram', HA: 'High Availability',
  AR: 'Autoregressive', MA: 'Moving Average', PCA: 'Principal Component Analysis',
  MDS: 'Multidimensional Scaling', ACID: 'Atomicity, Consistency, Isolation, Durability',
  CRUD: 'Create, Read, Update, Delete', LOD: 'Linked Open Data', MDM: 'Master Data Management',
  SQL: 'Structured Query Language', DBA: 'Database Administrator', DB: 'Database', DBMS: 'Database Management System',
  CAP: 'Consistency, Availability, Partition Tolerance',
  PACELC: 'Partition: Availability/Consistency; Else: Latency/Consistency',
  ELK: 'Elasticsearch, Logstash, Kibana', DW: 'Data Warehouse',
  PJNF: 'Project-Join Normal Form', MMDBMS: 'Main Memory Database Management System',
  MOLAP: 'Multidimensional Online Analytical Processing',
  CPU: 'Central Processing Unit', HBM4: 'High Bandwidth Memory 4',
  FTS: 'Fault-Tolerant System', IPC: 'Inter-Process Communication',
  VDI: 'Virtual Desktop Infrastructure', IDC: 'Internet Data Center', IaC: 'Infrastructure as Code',
  UCIe: 'Universal Chiplet Interconnect Express', GPU: 'Graphics Processing Unit',
  HPC: 'High-Performance Computing', NPU: 'Neural Processing Unit', PC: 'Personal Computer',
  CIDR: 'Classless Inter-Domain Routing', VLSM: 'Variable Length Subnet Mask',
  SATIN: 'Satellite-Air-Terrestrial Integrated Network', EHT: 'Extremely High Throughput',
  'AI-RAN': 'Artificial Intelligence-Radio Access Network',
  'CSMA/CA': 'Carrier Sense Multiple Access with Collision Avoidance',
  'CSMA/CD': 'Carrier Sense Multiple Access with Collision Detection',
  OSI: 'Open Systems Interconnection', CDMA: 'Code Division Multiple Access', TDMA: 'Time Division Multiple Access',
  DiffServ: 'Differentiated Services', IntServ: 'Integrated Services',
  SA: 'Standalone', UEC: 'Ultra Ethernet Consortium', UHR: 'Ultra High Reliability',
  WSN: 'Wireless Sensor Network', TCP: 'Transmission Control Protocol',
  ISMS: 'Information Security Management System', 'ISMS-P': 'Information Security and Personal Information Management System',
  NFT: 'Non-Fungible Token', DAC: 'Discretionary Access Control', MAC: 'Mandatory Access Control',
  RBAC: 'Role-Based Access Control', CSAP: 'Cloud Security Assurance Program', CSP: 'Cloud Service Provider',
  ICS: 'Industrial Control System', CC: 'Common Criteria', CSF: 'Cybersecurity Framework',
  N2SF: 'National Network Security Framework', GPKI: 'Government Public Key Infrastructure',
  CTEM: 'Continuous Threat Exposure Management', OWASP: 'Open Worldwide Application Security Project',
  BLP: 'Bell-LaPadula', SOC: 'Security Operations Center', IAM: 'Identity and Access Management',
  C2PA: 'Coalition for Content Provenance and Authenticity', CRA: 'Cyber Resilience Act',
  LotL: 'Living off the Land', COA: 'Ciphertext-Only Attack', RSA: 'Rivest-Shamir-Adleman',
  MPC: 'Multi-Party Computation', Tor: 'The Onion Router', DSA: 'Digital Services Act',
  FIDO: 'Fast IDentity Online',
  APEC: 'Asia-Pacific Economic Cooperation', EMP: 'Electromagnetic Pulse',
  FIPS: 'Federal Information Processing Standards', CFB: 'Cipher Feedback', OFB: 'Output Feedback',
  PIMS: 'Personal Information Management System',
  PR: 'Precision-Recall', ROC: 'Receiver Operating Characteristic', AX: 'AI Transformation',
  LLM: 'Large Language Model', LRM: 'Large Reasoning Model', RLHF: 'Reinforcement Learning from Human Feedback',
  LLMOps: 'Large Language Model Operations', VPP: 'Virtual Power Plant',
  GraphRAG: 'Graph-based Retrieval-Augmented Generation', ReAct: 'Reasoning and Acting',
  'Self-RAG': 'Self-Reflective Retrieval-Augmented Generation',
  LoRA: 'Low-Rank Adaptation', PEFT: 'Parameter-Efficient Fine-Tuning',
  CCTV: 'Closed-Circuit Television', DSML: 'Data Science and Machine Learning',
  'GPT-3': 'Generative Pre-trained Transformer 3', QR: 'Quick Response',
  SWIFT: 'Society for Worldwide Interbank Financial Telecommunication',
  RLAIF: 'Reinforcement Learning from AI Feedback', IoT: 'Internet of Things',
  VR: 'Virtual Reality', SNS: 'Social Networking Service', NLP: 'Natural Language Processing',
  ANN: 'Artificial Neural Network', CPO: 'Chief Privacy Officer',
  PIPA: 'Personal Information Protection Act', CAT: 'Certification of AI Trustworthiness',
  SaaS: 'Software as a Service', EGDI: 'E-Government Development Index',
  UI: 'User Interface', UX: 'User Experience', '5G': 'Fifth Generation', '6G': 'Sixth Generation',
  '2D': 'Two-Dimensional',
  ITSQF: 'IT Sectoral Qualifications Framework', OAS: 'OpenAPI Specification',
  AJAX: 'Asynchronous JavaScript and XML', XML: 'Extensible Markup Language', EJB: 'Enterprise JavaBeans',
  CXL: 'Compute Express Link', GPGPU: 'General-Purpose computing on Graphics Processing Units',
  IMT: 'International Mobile Telecommunications', ARQ: 'Automatic Repeat Request',
  'C-V2X': 'Cellular Vehicle-to-Everything', M2M: 'Machine-to-Machine', VXLAN: 'Virtual Extensible LAN',
  SBOM: 'Software Bill of Materials', SOAR: 'Security Orchestration, Automation and Response',
  JSON: 'JavaScript Object Notation', TOCTOU: 'Time-of-Check to Time-of-Use',
  A2A: 'Agent-to-Agent', VAE: 'Variational Autoencoder', AP2: 'Agent Payments Protocol',
  AIDT: 'AI Digital Textbook', BERT: 'Bidirectional Encoder Representations from Transformers',
  AAIF: 'Agentic AI Foundation', CRAG: 'Corrective Retrieval-Augmented Generation', XR: 'Extended Reality',
  ETRI: 'Electronics and Telecommunications Research Institute',
  CDR: 'Content Disarm and Reconstruction', CMP: 'Cloud Management Platform',
  NAS: 'Network-Attached Storage', SLM: 'Small Language Model',
  LIME: 'Local Interpretable Model-agnostic Explanations',
  STPA: 'System-Theoretic Process Analysis', BCI: 'Brain-Computer Interface',
  ERP: 'Enterprise Resource Planning', AHP: 'Analytic Hierarchy Process',
  SEM: 'Strategic Enterprise Management', CPM: 'Critical Path Method', CoE: 'Center of Excellence',
  BST: 'Binary Search Tree', ATAM: 'Architecture Tradeoff Analysis Method',
  CBAM: 'Cost Benefit Analysis Method', GS: 'Good Software', HCI: 'Human-Computer Interaction',
  AOP: 'Aspect-Oriented Programming', ALM: 'Application Lifecycle Management',
  CBD: 'Component-Based Development', EIP: 'Enterprise Integration Patterns',
  CMMI: 'Capability Maturity Model Integration', SAD: 'Software Architecture Description',
  OLAP: 'Online Analytical Processing', IMDF: 'Indoor Mapping Data Format',
  BCNF: 'Boyce-Codd Normal Form', BI: 'Business Intelligence', SNA: 'Social Network Analysis',
  FD: 'Functional Dependency', TPU: 'Tensor Processing Unit', DCI: 'Data Center Interconnect',
  SJF: 'Shortest Job First', IaaS: 'Infrastructure as a Service', PaaS: 'Platform as a Service',
  RAID: 'Redundant Array of Independent Disks', HPA: 'Horizontal Pod Autoscaler',
  UALink: 'Ultra Accelerator Link', DaaS: 'Desktop as a Service', FaaS: 'Function as a Service',
  HBM: 'High Bandwidth Memory', DAS: 'Direct-Attached Storage', SAN: 'Storage Area Network',
  DID: 'Digital Information Display', XaaS: 'Everything as a Service',
  NFV: 'Network Functions Virtualisation', NTN: 'Non-Terrestrial Network',
  WFQ: 'Weighted Fair Queuing', OSPF: 'Open Shortest Path First', NFC: 'Near Field Communication',
  IBN: 'Intent-Based Networking', QoS: 'Quality of Service', RIP: 'Routing Information Protocol',
  SCTP: 'Stream Control Transmission Protocol', SDN: 'Software-Defined Networking',
  WebRTC: 'Web Real-Time Communication', EGP: 'Exterior Gateway Protocol', IGP: 'Interior Gateway Protocol',
  VLAN: 'Virtual Local Area Network', IPS: 'Indoor Positioning System', NOMA: 'Non-Orthogonal Multiple Access',
  FSO: 'Free Space Optics', SDR: 'Software-Defined Radio', CDN: 'Content Delivery Network',
  CRC: 'Cyclic Redundancy Check', CoAP: 'Constrained Application Protocol',
  MQTT: 'Message Queuing Telemetry Transport', NAT: 'Network Address Translation',
  QKD: 'Quantum Key Distribution', PET: 'Privacy-Enhancing Technology', VPN: 'Virtual Private Network',
  RaaS: 'Ransomware as a Service', MCP: 'Model Context Protocol', CISO: 'Chief Information Security Officer',
  NHI: 'Non-Human Identities', SIEM: 'Security Information and Event Management',
  ECC: 'Elliptic Curve Cryptography', TTPs: 'Tactics, Techniques and Procedures',
  TLS: 'Transport Layer Security', CBPR: 'Cross-Border Privacy Rules',
  GADI: 'Global Architecture for Digital Identity', IDS: 'Intrusion Detection System', JWT: 'JSON Web Token',
  LDAP: 'Lightweight Directory Access Protocol', NAC: 'Network Access Control', BYOD: 'Bring Your Own Device',
  DDoS: 'Distributed Denial of Service', RAG: 'Retrieval-Augmented Generation', SVM: 'Support Vector Machine',
  GNN: 'Graph Neural Network', QML: 'Quantum Machine Learning',
  DBSCAN: 'Density-Based Spatial Clustering of Applications with Noise', MoE: 'Mixture of Experts',
  sLM: 'Small Language Model', IoB: 'Internet of Behavior',
  SNN: 'Spiking Neural Network', AGI: 'Artificial General Intelligence', CPS: 'Cyber-Physical System',
  DSLM: 'Domain-Specific Language Model', CNN: 'Convolutional Neural Network', MES: 'Manufacturing Execution System',
  MLOps: 'Machine Learning Operations', 'TF-IDF': 'Term Frequency-Inverse Document Frequency',
  ANI: 'Artificial Narrow Intelligence', DPO: 'Direct Preference Optimization',
  VLA: 'Vision-Language-Action', DeFi: 'Decentralized Finance', ISA: 'International Society of Automation',
  KYC: 'Know Your Customer',
  CI: 'Continuous Integration', CD: 'Continuous Delivery / Continuous Deployment',
  OSS: 'Open Source Software', SOA: 'Service-Oriented Architecture',
  RAN: 'Radio Access Network', V2X: 'Vehicle-to-Everything', LAN: 'Local Area Network',
  CVE: 'Common Vulnerabilities and Exposures', CBC: 'Cipher Block Chaining',
  TPM: 'Trusted Platform Module', APT: 'Advanced Persistent Threat',
};

export function notes() {
  return fs.readdirSync(root).filter(d => fs.statSync(path.join(root, d)).isDirectory())
    .flatMap(d => fs.readdirSync(path.join(root, d)).filter(f => /^\d{3}_.+\.md$/.test(f))
      .map(f => path.join(root, d, f))).sort();
}

export function namesForFile(file) {
  const context = { ...names };
  if (file.includes('technology_acceptance_model')) context.TAM = 'Technology Acceptance Model';
  if (file.includes('118_som')) context.SOM = 'Self-Organizing Map';
  if (file.includes('083_oop')) context.POP = 'Procedure-Oriented Programming';
  if (file.includes('111_mac')) context.MAC = 'Message Authentication Code';
  if (file.includes('053_ips')) context.IPS = 'Indoor Positioning System';
  if (file.includes('184_augmented_reality')) context.AR = 'Augmented Reality';
  return context;
}

// Company/product names, filenames and identifiers have no inferred expansion.
export const titleExceptions = new Set(['SK', 'SKT', 'KT', 'SGI', 'GB200', 'NVL72', 'XZ', 'R1', 'MODBUS', 'AGENTS', 'FIDO2', 'GPT']);

const normalize = text => text.toLowerCase().replace(/[^a-z0-9]/g, '');
const escape = text => text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

export function titleIssues(file, title) {
  const dictionary = namesForFile(file);
  const issues = [];
  let remaining = title;
  // Match compound names first so CSMA/CA and TF-IDF are not split into
  // unrelated acronym fragments. Existing English names are kept intact.
  for (const term of Object.keys(dictionary).sort((a, b) => b.length - a.length)) {
    remaining = remaining.replace(new RegExp(`(?<![A-Za-z0-9-])${escape(term)}(?![A-Za-z0-9-])`, 'g'), ' ');
  }
  for (const term of new Set(remaining.match(/\b[A-Z][A-Z0-9]{1,10}\b/g) || [])) {
    if (!dictionary[term] && !titleExceptions.has(term)) issues.push(`Unclassified title token: ${term}`);
  }
  for (const [term, fullName] of Object.entries(dictionary)) {
    // An English expansion is not a new title mention. Bare acronym lists
    // inside parentheses still count (e.g. "접근통제(DAC·MAC·RBAC)").
    const visible = title.replace(/\([^()]*[a-z][^()]*\)/g, '');
    const present = new RegExp(`(?<![A-Za-z0-9-])${escape(term)}(?![A-Za-z0-9-])`).test(visible);
    if (['5G', '6G', '2D'].includes(term)) continue; // generation/dimension notation
    if (present && !normalize(title).includes(normalize(fullName))) issues.push(`Missing title expansion: ${term}`);
  }
  return issues;
}

export function terminologyIssues(file, source) {
  const issues = [];
  const invalid = [
    /Lightweight Interoperability of Model Explanations/,
    /AGI\(Specialized General Intelligence\)/,
    /FinOps, Financial Operations/,
    /AIGC, AI-Generated Content Tagging/,
    /Q-EVM\(Earned Value Management\)/,
    /CSMA\/CD\(Continuous Delivery\)/,
    /\*\*(?:CDelivery|CDeployment)\*\*/,
  ];
  for (const pattern of invalid) if (pattern.test(source)) issues.push(`Invalid term: ${pattern.source}`);
  if (file.includes('08-law-policy') && /FP, Floating Point/.test(source)) issues.push('Function Point expanded as Floating Point');
  if (file.includes('public_database_standardization_manual') && /MDS, Multidimensional Scaling/.test(source)) issues.push('Metadata system confused with dimensionality reduction');
  const ipContexts = ['smart_factory_security', 'llm_adoption_security_risks', 'code_obfuscation', 'copyleft_license', 'permissive_license'];
  if (ipContexts.some(context => file.includes(context)) && /IP, Internet Protocol/.test(source)) issues.push('Intellectual Property expanded as Internet Protocol');
  return issues;
}

export function auditNotes() {
  return notes().map(file => {
    const source = fs.readFileSync(file, 'utf8');
    const title = source.match(/^title: "(.*)"/m)?.[1] || '';
    return { file, title, issues: [...titleIssues(file, title), ...terminologyIssues(file, source)] };
  });
}

if (process.argv[1]?.endsWith('audit-itpe-terminology.mjs')) {
  const results = auditNotes();
  const violations = results.flatMap(({ file, issues }) => issues.map(issue => `${file}: ${issue}`));
  const subjects = new Set(results.map(({ file }) => path.dirname(file))).size;
  console.log(`${subjects} subjects, ${results.length} notes scanned; ${violations.length} known terminology/title violations.`);
  if (violations.length) console.log(violations.join('\n'));
  process.exitCode = violations.length ? 1 : 0;
}
