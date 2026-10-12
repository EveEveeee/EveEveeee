import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const escape = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const themes = {
  light: { bg: '#ffffff', border: '#d1d9e0', blue: '#0969da', text: '#59636e', strong: '#24292f', window: '#f8fafb', bar: '#f1f4f6', green: '#1a7f37' },
  dark: { bg: '#0d1117', border: '#30363d', blue: '#58a6ff', text: '#919ba7', strong: '#e6edf3', window: '#101820', bar: '#161b22', green: '#3fb950' }
};
const projects = [
  { id: 'product-foundry', title: 'Product Foundry', lines: ['From ideas to scoped requirements,', 'linked PRDs, and review-agent experiments.', 'Separate prototypes; integration in progress.'], category: 'AI product workflow', stage: 'Prototype + POC', color: '#a371f7', url: 'https://github.com/EveEveeee/product-foundry' },
  { id: 'muse10-ai-nails', title: 'Muse10 · AI Nails', lines: ['AI nail-design co-creation for store visits.', 'Product flows, prompts, and failure cases.', 'Co-built; personal-hand try-on in validation.'], category: 'AI product case', stage: 'Prototype + POC', color: '#f778ba', url: 'https://github.com/EveEveeee/muse10-ai-nails' },
  { id: 'child-knowledge-cocreation', title: 'Child-led Co-creation', lines: ['Age-aware, child-led story creation.', 'From a first idea to a saved storybook.', 'Local demo; family usability still to test.'], category: 'AI product case', stage: 'Local prototype', color: '#d29922', url: 'https://github.com/EveEveeee/child-knowledge-cocreation' },
  { id: 'evidence-led-teardown', title: 'Evidence-led Teardown', lines: ['Read the evidence before drawing conclusions.', 'Trace users, technology, models, and data.', 'Turn findings into a traceable HTML report.'], category: 'Product research', stage: 'Reusable skill', color: '#3fb950', url: 'https://github.com/EveEveeee/Eve/tree/main/skills/evidence-led-product-teardown' },
  { id: 'muse10-nail-visuals', title: 'Muse10 Nail Visuals', lines: ['From references to a ten-nail design plan.', 'Catalog masters, details, and visual checks.', 'A co-built workflow for consistent outputs.'], category: 'Visual workflow', stage: 'Reusable skill', color: '#f778ba', url: 'https://github.com/EveEveeee/Eve/tree/main/skills/muse10-nail-visuals' },
  { id: 'open-source-reviews', title: 'Open-source Reviews', lines: ['AI-assisted review of Open Code Review.', 'Issue reports and a related investigation.', 'Documenting risks, evidence, and follow-up.'], category: 'Open-source practice', stage: 'Reports + analysis', color: '#58a6ff', url: 'CONTRIBUTIONS.md' }
];
fs.mkdirSync(path.join(root, 'assets/projects'), { recursive: true });

for (const [mode, c] of Object.entries(themes)) {
  const hero = `<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="520" viewBox="0 0 1000 520" role="img" aria-labelledby="title desc">
  <title id="title">Eve's portfolio terminal</title>
  <desc id="desc">AI product manager. Explore product cases, reusable skills, and writing at wangyangjuan.surge.sh.</desc>
  <style>
    text { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace; }
    .title { fill: ${c.strong}; font-size: 18px; font-weight: 600; }
    .body { fill: ${c.text}; font-size: 17px; }
    .prompt { fill: ${c.blue}; font-size: 17px; }
    .ok { fill: ${c.green}; font-size: 17px; }
    .cursor { animation: blink 1.15s steps(1) infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    @media (prefers-reduced-motion: reduce) { .cursor { animation: none; } }
  </style>
  <rect x="1" y="1" width="998" height="518" rx="18" fill="${c.window}" stroke="${c.border}" stroke-width="2"/>
  <path d="M19 2H981Q998 2 998 19V53H2V19Q2 2 19 2Z" fill="${c.bar}"/>
  <path d="M2 53H998" stroke="${c.border}"/>
  <circle cx="24" cy="27" r="7" fill="#ff5f57"/><circle cx="47" cy="27" r="7" fill="#febc2e"/><circle cx="70" cy="27" r="7" fill="#28c840"/>
  <text x="500" y="31" text-anchor="middle" fill="${c.text}" font-size="12">eve@portfolio: ~</text>
  <text x="54" y="93" class="title">EVE / AI PRODUCT MANAGER</text>
  <text x="54" y="132" class="ok">[OK]</text><text x="115" y="132" class="body">Load product thinking and real-world questions</text>
  <text x="54" y="163" class="ok">[OK]</text><text x="115" y="163" class="body">Mount product cases, prototypes, and evaluations</text>
  <text x="54" y="194" class="ok">[OK]</text><text x="115" y="194" class="body">Connect reusable skills and writing</text>
  <text x="54" y="225" class="ok">[OK]</text><text x="115" y="225" class="body">Keep evidence, limits, and next steps visible</text>
  <text x="54" y="275" class="prompt">eve@portfolio:~$ whoami</text>
  <text x="54" y="307" class="body">A product manager turning AI ideas into testable experiences.</text>
  <text x="54" y="355" class="prompt">eve@portfolio:~$ open https://wangyangjuan.surge.sh</text>
  <rect class="cursor" x="586" y="340" width="10" height="20" fill="${c.blue}"/>
  <text x="54" y="397" class="ok">Ready. Explore the work behind the ideas.</text>
  <text x="500" y="457" text-anchor="middle" class="title">Click to open my personal website</text>
  <text x="500" y="487" text-anchor="middle" fill="${c.blue}" font-size="22">↗</text>
</svg>\n`;
  fs.writeFileSync(path.join(root, `assets/portfolio-launch-${mode}.svg`), hero);
  for (const p of projects) {
    const card = `<svg xmlns="http://www.w3.org/2000/svg" width="620" height="210" viewBox="0 0 620 210" role="img" aria-labelledby="title desc">
  <title id="title">${escape(p.title)}</title>
  <desc id="desc">${escape([...p.lines, p.stage].join(' '))}</desc>
  <style>text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }</style>
  <rect x=".75" y=".75" width="618.5" height="208.5" rx="9" fill="${c.bg}" stroke="${c.border}" stroke-width="1.5"/>
  <g transform="translate(24 25)" fill="none" stroke="${c.text}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 0h13v20H3a3 3 0 0 1-3-3V3a3 3 0 0 1 3-3Z"/><path d="M0 16h16M5 4v7M9 4v7"/></g>
  <text x="56" y="43" fill="${c.blue}" font-size="22" font-weight="600">${escape(p.title)}</text>
  <rect x="530" y="23" width="66" height="26" rx="13" fill="none" stroke="${c.border}"/>
  <text x="563" y="41" text-anchor="middle" fill="${c.text}" font-size="14" font-weight="500">Public</text>
  ${p.lines.map((line, i) => `<text x="24" y="${81 + i * 27}" fill="${c.text}" font-size="18">${escape(line)}</text>`).join('\n  ')}
  <circle cx="30" cy="175" r="6" fill="${p.color}"/>
  <text x="44" y="180" fill="${c.text}" font-size="15">${escape(p.category)}</text>
  <text x="596" y="180" text-anchor="end" fill="${c.text}" font-size="15">${escape(p.stage)}</text>
</svg>\n`;
    fs.writeFileSync(path.join(root, `assets/projects/${p.id}-${mode}.svg`), card);
  }
}

const picture = (base, alt) => `<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="${base}-dark.svg">\n  <source media="(prefers-color-scheme: light)" srcset="${base}-light.svg">\n  <img src="${base}-light.svg" alt="${escape(alt)}" width="${base.includes('/projects/') ? '49%' : '100%'}">\n</picture>`;
const cards = projects.map(p => `<a href="${p.url}">\n${picture(`assets/projects/${p.id}`, `${p.title} — ${p.stage}`)}\n</a>`);
const articles = JSON.parse(fs.readFileSync(path.join(root, 'content/articles.json'), 'utf8'));
const recent = articles.slice(0, 6).map(a => `- [${a.title}](${a.url}) · ${a.date}`).join('\n');
const readme = `# Hi, I'm Eve 👋

<a href="https://wangyangjuan.surge.sh/">
${picture('assets/portfolio-launch', "Eve's portfolio terminal — click to explore my personal website")}
</a>

<p align="center"><sub>Click the terminal to explore my personal website · wangyangjuan.surge.sh</sub></p>

I explore how AI can move from impressive demos to useful, trustworthy products.  
My work spans product discovery, workflow design, prompt iteration, and task-based evaluation.  
I use AI coding tools to build and test prototypes—and document what works, what fails, and what still needs evidence.

🌐 [Personal website](https://wangyangjuan.surge.sh/) · ✍️ [WeChat](https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzcwNzQzMDkxMw==&scene=124#wechat_redirect) · [Xiaohongshu](https://www.xiaohongshu.com/user/profile/634fb9e1000000001802b00f) · ✉️ [Email](mailto:wangyangjuanwyj@gmail.com)

## ⭐ Selected work

Product cases, practical tools, and reusable methods. Cards link to the work and its current stage.

${cards.slice(0, 2).join('\n\n')}

${cards.slice(2, 4).join('\n\n')}

${cards.slice(4, 6).join('\n\n')}

[Explore all projects →](PROJECTS.md) · [Open-source contributions →](CONTRIBUTIONS.md)

## 🔎 Currently exploring

- **Requirements to decisions:** keeping scope, PRDs, and review evidence aligned as an idea changes.
- **Visual AI for real visits:** consistent ten-nail designs, useful store workflows, and the limits of personal-hand try-on.
- **Child-led creation:** age-aware story flows that preserve a child's choices and make model output easier to assess.

These are ongoing experiments, not claims of production readiness or proven user impact.

## 📝 Evidence-led Product Teardown

A reusable research skill for product analysis grounded in screenshots, accessible pages, code, and operation records. It traces the user, technology, model, and data layers into an HTML report. When evidence is missing, it identifies the gaps instead of inventing an architecture.

[Explore the skill →](https://github.com/EveEveeee/Eve/tree/main/skills/evidence-led-product-teardown) · [See the workflow →](https://wangyangjuan.surge.sh/tools/product-teardown.html)

## ✍️ Writing

I write about AI products, agents, human–AI collaboration, and evaluation on **Manman Says AI**, my WeChat publication. Below are the six most recent posts; English titles link to the original Chinese articles.

${recent}

[Read all ${articles.length} articles →](ARTICLES.md) · [Personal website →](https://wangyangjuan.surge.sh/)

## About me

**AI Product Manager**

- Product discovery and first-release scope
- AI workflows, interaction design, and human handoffs
- Prompt design, task-based evaluation, and failure analysis
- AI-assisted prototyping and open-source practice
- Writing to clarify product decisions

**Define** the task and boundaries · **Design** the flow · **Evaluate** the outcome · **Iterate** from evidence

Think clearly. Build thoughtfully. Keep learning.
`;
fs.writeFileSync(path.join(root, 'README.md'), readme);
console.log(`Built ${projects.length * 2 + 2} SVG assets and README with ${articles.length} verified article entries.`);
