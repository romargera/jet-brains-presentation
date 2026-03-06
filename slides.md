<!-- .slide: id="title" -->

<div class="title-slide">
  <p class="title-label">Take-Home Task</p>
  <h1>Bonsai<br></h1>
  <p class="title-subtitle">Predictable AI-assisted Development<br>via Bi-directional Spec↔Code Control</p>
  <div class="title-author">
    <p class="author-name">Roman Babunts</p>
    <p class="author-date">March 2026</p>
  </div>
</div>

Notes:
Good morning. I'm Roman Babunts. Today I'll walk you through Bonsai — a product concept for predictable, AI-assisted development through spec-driven control. I'll cover the problem space, market opportunity, and a concrete execution plan. Let's begin.

---
<!-- .slide: id="agenda" -->

## Presentation Structure

<div class="agenda-nav">
  <div class="agenda-section">
    <h4>WHAT</h4>
    <p>Pain Story</p>
    <p>Pain Map</p>
    <p>JTBD + ICP</p>
    <p>Direction: Wedge</p>
  </div>
  <div class="agenda-section">
    <h4>WHY</h4>
    <p>Why Now</p>
    <p>Market Map</p>
    <p>Competitive Landscape</p>
    <p>Niche Choice</p>
  </div>
  <div class="agenda-section">
    <h4>HOW</h4>
    <p>Product Thesis</p>
    <p>MVP Scope</p>
    <p>Validation Experiments</p>
    <p>GTM: First 100 Users</p>
    <p>Metrics + Kill Signals</p>
    <p>Risks + Roadmap</p>
  </div>
</div>

Notes:
The presentation has three parts. First, **What** — the problem AI teams face today and who we're building for. Second, **Why** — the market timing, competitive landscape, and our strategic choice. Third, **How** — the MVP, validation experiments, go-to-market, and risk management. Let's start with the problem.

---
<!-- .slide: id="adoption-paradox" -->

## WHAT: The AI Adoption Paradox

<p class="slide-subtitle"></p>

<div class="adoption-layout">
<div class="adoption-col adoption-col-left">
<div class="adoption-hero">
<span class="adoption-hero-number">90%</span>
<span class="adoption-hero-label">of developers use AI tools</span>
<span class="adoption-hero-delta">+14% YoY</span>
</div>
<p class="adoption-source"><a href="https://dora.dev/research/2025/dora-report/" target="_blank">DORA Report 2025</a></p>
</div>
<div class="adoption-col adoption-col-right">
<div class="adoption-metric metric-distrust">
<div class="adoption-metric-body">
<div class="adoption-metric-main negative">46%</div>
<div class="adoption-metric-sub">
<span class="adoption-metric-delta negative">↑ 15 pp</span>
<span class="adoption-metric-label">YOY INCREASE</span>
</div>
</div>
<div class="adoption-metric-header">
<span class="adoption-metric-name">DISTRUST (SOMEWHAT + HIGH)</span>
</div>
</div>
<div class="adoption-metric metric-unfavorable">
<div class="adoption-metric-body">
<div class="adoption-metric-main negative">20%</div>
<div class="adoption-metric-sub">
<span class="adoption-metric-delta negative">↑ 14 pp</span>
<span class="adoption-metric-label">YOY INCREASE</span>
</div>
</div>
<div class="adoption-metric-header">
<span class="adoption-metric-name">UNFAVORABLE SENTIMENT</span>
</div>
</div>
<p class="adoption-source"><a href="https://survey.stackoverflow.co/" target="_blank">Stack Overflow Developer Survey 2025</a></p>
</div>
</div>

<div class="adoption-takeaway">
  <p><strong>Takeaway:</strong> Developers adopt AI because of speed — but lose trust when output is unpredictable and hard to control.</p>
</div>

Notes:
Let's start with the market signal. AI adoption among developers has hit 90% — up 14% year over year, according to Google's DORA report. But here's the paradox: adoption is up, yet trust is collapsing. Stack Overflow's 2025 survey shows unfavorable sentiment toward AI jumped 14 points in one year. Trust dropped from 43% to 33%. And active distrust — developers who say they distrust AI output — surged from 30% to nearly 46%. The takeaway is clear: developers use AI because it's fast, but they don't trust it — because the output is unpredictable and hard to control. This is the gap we're going after.

---
<!-- .slide: id="what-icp-jtbd" -->

## WHAT: Core JTBD

<div class="distrust-takeaway">
  <p style="font-size: 0.45em; color: var(--text-muted); margin: 0 0 8px; line-height: 1.4;">Assumed <span class="metric-badge">A</span> after analyzing the top issues across three evidence layers: <a href="#/distrust-issues">Distrust</a>, <a href="#/time-spend">Time Spent</a>, and <a href="#/b2b-pains">B2B Issues</a>.</p>
</div>

<div class="chosen-grid chosen-grid--small">
  <div class="chosen-tile chosen-tile--green chosen-tile--wide">
    <p class="chosen-tile-label">Core JTBD</p>
    <p class="chosen-tile-body">When engineers build with AI in production, they want development to be predictable and controllable, so they can ship faster with confidence.</p>
  </div>
</div>

Notes:
Here we look at who we are targeting and why.
At the absolute core, our user has one main Job To Be Done: "When I use AI to write code, I want it to be predictable so I don't break production."
Our wedge starts with the Early Adopters—the Tech Leads and Staff Engineers. They are the ones feeling the immediate pain of unscoped AI pull requests and code drift. The triggers here are simple: a few painful AI-caused bugs, or just review fatigue.
Once we prove value at the team level, we hit the Scaling phase. Here, we target Engineering Managers, Heads of Platform, and Security leadership. Their headache is blast radius and policy enforcement across many repositories. When they are pushed by an upcoming compliance audit or a sudden drop in code quality across teams, they need a standardized, auditable way to manage AI-assisted development across the organization.

---
<!-- .slide: id="stream-options" -->

## WHAT: Strategic Directions

<table class="score-table">
  <thead>
    <tr>
      <th>Direction</th>
      <th>Source</th>
      <th>ICE Score <span class="metric-badge">A</span></th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>AI-dev transparency:</strong> code &amp; architecture</td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>2.5</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>Spec Formalisation Proactive Assist</strong></td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>2.5</td>
    </tr>
    <tr>
      <td><strong>Security &amp; Compliance</strong> (proactive assist)</td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>1.7</td>
    </tr>
    <tr>
      <td><strong>Review &amp; Debug assist</strong></td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>1.7</td>
    </tr>
    <tr>
      <td><strong>Dev Env Simplification</strong></td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>1.7</td>
    </tr>
    <tr>
      <td><strong>Delivery time variability</strong> (accurate forecasting)</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>1.7</td>
    </tr>
    <tr>
      <td><strong>Token Spent Optimization</strong></td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>1.3</td>
    </tr>
    <tr>
      <td><strong>Quality &amp; reliability risk</strong> from software errors</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>1.1</td>
    </tr>
  </tbody>
</table>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> AI-dev transparency: code &amp; architecture is the top-priority direction. Key risk: spec fatigue and enforcement resistance. Runner-up (Review &amp; Debug assist) becomes our fallback if ICP interviews disprove pre-hoc control preference.</p>
</div>

<ul class="distrust-notes">
<li>ICE Score ranks directions by value vs cost: ICE Score = (Impact × Confidence) / Effort. <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=1907182755#gid=1907182755&range=A1" target="_blank">Calculations</a>.</li>
<li>Mapping: Impact/Effort High=3, Med=2, Low=1; Confidence High=1, Med=0.75, Low=0.5.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
<li>Directions are derived from the top issues across three evidence layers: <a href="#/distrust-issues">Distrust</a>, <a href="#/time-spend">Time Spent</a>, and <a href="#/b2b-pains">B2B Issues</a>.</li>
</ul>

Notes:
Directions are scored by value-to-cost ratio to make prioritization explicit and defensible.
Score = (Impact × Confidence) / Effort. Mapping: Impact/Effort High=3, Med=2, Low=1; Confidence High=1, Med=0.75, Low=0.5.
All scores are assumptions marked with A — to be validated through user interviews and early pilots.

Key risks of chosen direction (AI-dev transparency): spec fatigue — developers approve without reading; enforcement resistance — teams reject mandatory gates. Both are tested in Phase 1 experiments.

What would change our mind on runner-ups:
• Review & Debug assist (1.7): if ICP interviews reveal developers prefer post-hoc review over pre-hoc control, we pivot to this direction — it shares the same trust JTBD but inverts the intervention point.
• Security & Compliance (1.7): if enterprise pilots show compliance gates drive faster budget approval than architecture governance, we re-scope the wedge.

Next: we define the chosen direction in detail with JTBD and early adopter segments.

---
<!-- .slide: id="competitor-landscape" -->

## WHAT: Competitor Landscape

<div class="competitor-layout">
<div class="competitor-col-left">
<table class="distrust-table">
  <colgroup>
    <col style="width: 8%">
    <col style="width: 17%">
    <col style="width: 75%">
  </colgroup>
  <thead>
    <tr>
      <th>Tier</th>
      <th>Direct competitors</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td rowspan="5"><strong>Tier 1</strong></td>
      <td><a href="https://speckit.org/" target="_blank">Spec Kit</a></td>
      <td>GitHub-supported, 73.6k★, markdown specs, phased plan-first workflow, CLI + in-agent</td>
    </tr>
    <tr class="highlight-row">
      <td><a href="https://kiro.dev/" target="_blank">Kiro</a></td>
      <td>Built on Amazon Bedrock, 1,5M MAU (Similarweb), Kiro IDE + CLI + in-agent</td>
    </tr>
    <tr class="highlight-row">
      <td><a href="https://docs.bmad-method.org/" target="_blank">BMAD</a></td>
      <td>38.9k★, 19 roles, CLI + in‑agent, adaptive depth, REPL-like</td>
    </tr>
    <tr class="highlight-row">
      <td><a href="https://openspec.dev/" target="_blank">OpenSpec</a></td>
      <td>Vendor-agnostic, Open Source, No API Keys, No MCP, REPL-like</td>
    </tr>
    <tr class="highlight-row">
      <td><a href="https://codespeak.dev/" target="_blank">CodeSpeak</a></td>
      <td>Specs compile to code, spec-diff → code-diff; code-to-spec coming soon</td>
    </tr>
    <tr>
      <td rowspan="7"><strong>Tier 2</strong></td>
      <td><a href="https://www.task-master.dev/" target="_blank">Taskmaster</a></td>
      <td>PRD → tasks + autonomous TDD autopilot (RED → GREEN → COMMIT per subtask)</td>
    </tr>
    <tr>
      <td><a href="https://stately.ai/" target="_blank">Stately</a></td>
      <td>Model-based approach: state machines as spec artifacts</td>
    </tr>
    <tr>
      <td><a href="https://buildermethods.com/agent-os" target="_blank">Agent-OS</a></td>
      <td>Standards loop. Extra JTBD: Auto-extracts repo conventions</td>
    </tr>
    <tr>
      <td><a href="https://github.com/ariel-frischer/autospec" target="_blank">Autospec</a></td>
      <td>Spec Kit fork, automated YAML pipeline</td>
    </tr>
    <tr>
      <td><a href="https://specs.md/" target="_blank">specs.md</a></td>
      <td>Formal AI-DLC, VS Code extension, CLI + in‑agent</td>
    </tr>
    <tr>
      <td><a href="https://www.autok.dev/" target="_blank">autok</a></td>
      <td>Knowledge-graph rails + bidirectional requirements sync via CLI + in‑agent (MCP)</td>
    </tr>
    <tr>
      <td><a href="https://www.devplan.com/" target="_blank">devplan</a></td>
      <td>Context graph (code + tickets + docs) → spec creation → agent prompts, CLI + browser</td>
    </tr>
  </tbody>
</table>
</div>
<div class="competitor-col-right" style="font-size: 0.28em;">
<h4 style="font-size: 1em; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.06em; margin: 0 0 4px; padding-bottom: 3px; border-bottom: 1px solid rgba(255,255,255,0.2);">Indirect Competitors</h4>
<div class="indirect-card" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-left: 3px solid #4fc3f7; border-radius: 6px; padding: 4px 6px; margin-bottom: 4px;">
  <p style="font-size: 1em; font-weight: 700; color: #e0e0e0; margin: 0 0 1px;">IDE AI Assistants (baseline)</p>
  <p style="font-size: 0.9em; margin: 0 0 1px;"><a href="https://cursor.com/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">Cursor</a>, <a href="https://github.com/features/copilot" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">Copilot</a>, <a href="https://www.jetbrains.com/ai-assistant/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">JB AI</a></p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.5); margin: 0; font-style: italic;">Have steering files (Rules, CLAUDE.md) but no spec enforcement or drift detection</p>
</div>
<div class="indirect-card" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-left: 3px solid #b388ff; border-radius: 6px; padding: 4px 6px; margin-bottom: 4px;">
  <p style="font-size: 1em; font-weight: 700; color: #e0e0e0; margin: 0 0 1px;">AI Code Reviewers</p>
  <p style="font-size: 0.9em; margin: 0 0 1px;"><a href="https://coderabbit.ai/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">CodeRabbit</a>, <a href="https://www.qodo.ai/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">Qodo</a></p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.5); margin: 0; font-style: italic;">Same trust pain, review stage</p>
</div>
<div class="indirect-card" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-left: 3px solid #69f0ae; border-radius: 6px; padding: 4px 6px; margin-bottom: 4px;">
  <p style="font-size: 1em; font-weight: 700; color: #e0e0e0; margin: 0 0 1px;">Observability + Evals</p>
  <p style="font-size: 0.9em; margin: 0 0 1px;"><a href="https://docs.langchain.com/langsmith/home" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">LangSmith</a>, <a href="https://www.datadoghq.com/product/llm-observability/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">Datadog LLM</a></p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.5); margin: 0; font-style: italic;">Trace agent steps, convergence risk</p>
</div>
</div>
</div>

Notes:
This slide maps the competitive landscape for spec-driven development. Tier 1 includes five players we consider direct competitors: Spec Kit leads by traction, Kiro is Amazon's bet on this category, BMAD differentiates with multi-agent depth, OpenSpec is uniquely vendor-agnostic, and CodeSpeak takes spec-driven to its purest form — specs compile directly to code. Tier 2 products are on our watch list — they address adjacent problems or are too early-stage to evaluate fully. The key insight: the market is fragmented and early, with no dominant player and no standard methodology.

---
<!-- .slide: id="learn-and-steal" -->

## WHAT: Learn & Steal

<div class="chosen-grid chosen-grid--2col chosen-grid--small">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Git-Native Markdown</p>
    <p class="chosen-tile-body">Open and AI-friendly standard (SpecKit, BMAD). Zero vendor lock-in.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Bi-Directional Sync</p>
    <p class="chosen-tile-body">CodeSpeak validates direction. Our edge: code remains primary artifact.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">IDE-Native Surface</p>
    <p class="chosen-tile-body">Web-first creates context switch. Keep devs in-IDE.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Persistent Steering</p>
    <p class="chosen-tile-body">Already table stakes (Cursor Rules, CLAUDE.md, Kiro). Our edge: enforcement + drift detection on top.</p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 15px;">
  <p><strong>Synthesis:</strong> The winning formula is a Git-native, bi-directional spec tool living entirely inside the IDE.</p>
</div>

Notes:
Here we look at what's actually working in the market. First, Git-native markdown specs are the standard—tools like SpecKit prove developers won't adopt proprietary formats. Second, bi-directional sync: specs compile to code, code updates specs (like CodeSpeak), which stops doc rot. Third, surface area: web-first SaaS creates a context switch; successful workflows are IDE-native or CLI-native. Finally, persistent steering and slash-commands give us a natural UX that prevents AI amnesia.

---
<!-- .slide: id="competitive-approaches" -->

## WHY: Approaches

<div class="distrust-table-wrapper">
<table class="distrust-table">
  <thead>
    <tr>
      <th>Approach</th>
      <th>Description</th>
      <th>Key Players</th>
      <th>ICE Score <span class="metric-badge">A</span></th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>Spec-driven development</strong></td>
      <td>Spec-first: AI generates code &amp; checks from contracts. Spec becomes a reviewable, regression artifact.</td>
      <td><a href="https://kiro.dev/" target="_blank">Kiro</a>, <a href="https://speckit.org/" target="_blank">Spec Kit</a>, <a href="https://codespeak.dev/" target="_blank">CodeSpeak</a>, <a href="https://www.task-master.dev/" target="_blank">Taskmaster</a>, <a href="https://docs.bmad-method.org/" target="_blank">BMAD</a></td>
      <td>3.3</td>
    </tr>
    <tr>
      <td><strong>Observability + evals</strong></td>
      <td>Trace inputs/outputs &amp; agent steps; measure quality via datasets &amp; LLM-as-judge. Catch degradations pre-release.</td>
      <td><a href="https://docs.langchain.com/langsmith/home" target="_blank">LangSmith</a>, <a href="https://docs.wandb.ai/weave" target="_blank">W&amp;B Weave</a>, <a href="https://www.datadoghq.com/product/llm-observability/" target="_blank">Datadog LLM</a>, <a href="https://galileo.ai/" target="_blank">Galileo</a>, <a href="https://docs.ragas.io/" target="_blank">Ragas</a>, <a href="https://github.com/truera/trulens" target="_blank">TruLens</a>, <a href="https://www.braintrust.dev/docs" target="_blank">Braintrust</a></td>
      <td>3.0</td>
    </tr>
    <tr>
      <td><strong>Last mile quality gates</strong></td>
      <td>I/O guardrails + JSON Schema validation + AI test gen; CI blocks merge until checks pass.</td>
      <td><a href="https://github.com/guardrails-ai/guardrails" target="_blank">Guardrails AI</a>, <a href="https://docs.nvidia.com/nemo-guardrails/index.html" target="_blank">NeMo</a>, <a href="https://developers.openai.com/api/docs/guides/structured-outputs/" target="_blank">OpenAI Structured</a>, <a href="https://www.diffblue.com/diffblue-cover/" target="_blank">Diffblue</a>, <a href="https://keploy.io/" target="_blank">Keploy</a>, <a href="https://junit.org/" target="_blank">JUnit</a></td>
      <td>2.5</td>
    </tr>
    <tr>
      <td><strong>Security &amp; compliance guardrails</strong></td>
      <td>Static analysis + runtime protection: catch vulnerabilities &amp; prompt injection, enforce compliance policies.</td>
      <td><a href="https://snyk.io/product/snyk-code/" target="_blank">Snyk Code</a>, <a href="https://semgrep.dev/" target="_blank">Semgrep</a>, <a href="https://codeql.github.com/docs/" target="_blank">CodeQL</a>, <a href="https://www.lakera.ai/lakera-guard" target="_blank">Lakera Guard</a>, <a href="https://www.holisticai.com/" target="_blank">Holistic AI</a>, <a href="https://protectai.com/" target="_blank">Protect AI</a></td>
      <td>2.3</td>
    </tr>
    <tr>
      <td><strong>AI code reviewer</strong></td>
      <td>AI analyzes diffs &amp; repo context, finds issues, generates review summaries.</td>
      <td><a href="https://www.qodo.ai/" target="_blank">Qodo</a>, <a href="https://coderabbit.ai/" target="_blank">CodeRabbit</a>, <a href="https://github.com/qodo-ai/pr-agent" target="_blank">PR-Agent</a></td>
      <td>2.2</td>
    </tr>
    <tr>
      <td><strong>AI-driven task orchestration</strong></td>
      <td>Tasks get AI context; agents run on subtasks; code changes, PRs &amp; statuses flow in one managed pipeline.</td>
      <td><a href="https://vibekanban.com/" target="_blank">Vibe Kanban</a></td>
      <td>2.0</td>
    </tr>
    <tr>
      <td><strong>Deterministic LLM output</strong></td>
      <td>Force strictly validatable structure; retry/fix on schema mismatch.</td>
      <td><a href="https://ai.pydantic.dev/" target="_blank">PydanticAI</a>, <a href="https://github.com/567-labs/instructor" target="_blank">Instructor</a>, <a href="https://github.com/dottxt-ai/outlines" target="_blank">Outlines</a></td>
      <td>0.9</td>
    </tr>
    <tr>
      <td><strong>Human-Freelancer in the Loop</strong></td>
      <td>AI writes code; freelancer expert approves changes instead of the team.</td>
      <td><a href="https://tendem.ai/" target="_blank">Tendem</a></td>
      <td>0.9</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=549312952#gid=549312952&range=A1" target="_blank">Spec-driven development</a> is the top-priority approach for addressing trust, combining the highest ICE Score across impact, confidence, and effort factors.</p>
</div>

<ul class="distrust-notes">
<li>Impact is scored 1–3 across 9 criteria. Speed, DX, Quality, and JTBD time-saved are grouped as one "Delivery Outcomes" block (their weights sum to 1), equal to each of the other dimensions (Cost, Transparency, SDLC coverage, Adoption friction, Monetization), which all have equal weight. Impact Total is the weighted average. Total Score = Impact Total × Confidence ÷ Effort (Effort and Confidence both rated 1–3). <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=549312952#gid=549312952&range=A1" target="_blank">Details →</a></li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
<li>Note: IDE-native steering files (Cursor Rules, CLAUDE.md, Windsurf Memory) partially solve persistent context but lack spec enforcement, drift detection, and structured generation pipelines.</li>
<li>Each score was triangulated against: (1) Distrust + Time Spent + B2B evidence, (2) competitor traction signals, (3) JB SDK feasibility.</li>
</ul>

Notes:
This slide maps competitive approaches to improving trust in AI-assisted development, scored using a weighted ICE framework. Impact is scored 1–3 across 9 criteria. Speed, DX, Quality, and JTBD time-saved are grouped as one "Delivery Outcomes" block (weights sum to 1), equal to Cost, Transparency, SDLC coverage, Adoption friction, and Monetization. Impact Total is the weighted average. Total Score = Impact Total × Confidence ÷ Effort. Spec-driven development leads because it addresses ambiguity at the root — before code generation — delivering the highest combined score of 3.3.

---
<!-- .slide: id="niche-choice" -->

## WHY: Niche Choice

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 5%;">
    <col style="width: 25%;">
    <col style="width: 70%;">
  </colgroup>
  <thead>
    <tr>
      <th class="center">#</th>
      <th>Niche / Positioning</th>
      <th>Rationale & Focus</th>
    </tr>
  </thead>
  <tbody>
    <!-- GREEN PATH (Our Focus) -->
    <tr class="highlight-row">
      <td class="center"><strong>1</strong></td>
      <td><strong>IDE-Native Control (Wedge)</strong></td>
      <td>Zero context switch. Uncontested for structured spec control (steering files ≠ enforceable specs). Massive JB distribution moat.</td>
    </tr>
    <tr class="highlight-row">
      <td class="center"><strong>2</strong></td>
      <td><strong>Architecture Governance (Value)</strong></td>
      <td>Live spec↔code drift warnings. Combats doc rot directly.</td>
    </tr>
    <tr class="highlight-row">
      <td class="center"><strong>3</strong></td>
      <td><strong>Spec Compiler (Moonshot)</strong></td>
      <td>True bi-directional sync (100% predictability). Requires massive R&D (6-12m).</td>
    </tr>
    <!-- RED PATH (Rejected/Indirect) -->
    <tr>
      <td class="center">4</td>
      <td><strong>End-to-End Orchestration</strong></td>
      <td>Too bloated for MVP. PRD→Code→PR is too slow.</td>
    </tr>
    <tr>
      <td class="center">5</td>
      <td><strong>AI Code Review</strong></td>
      <td>Red Ocean (CodeRabbit, Qodo). Hard to win without unique advantage.</td>
    </tr>
    <tr>
      <td class="center">6</td>
      <td><strong>Auto Bug Bounties</strong></td>
      <td>Narrow security focus. Not our target ICP or core JTBD.</td>
    </tr>
    <tr>
      <td class="center">7</td>
      <td><strong>PRD-to-Ticket</strong></td>
      <td>Product-level tracking. Too far from the actual code.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Strategy:</strong> Own the IDE first (1), build the governance graph (2), aim for the compiler (3).</p>
</div>

Notes:
Here is our niche selection. We evaluated 7 potential paths. The green path is our strategy: our wedge is IDE-Native Control because no startup is targeting the IntelliJ SDK, giving us a massive distribution moat. Our core value driver is Architecture Governance—specifically live drift detection—which solves the "docs rot" pain. And our 6-12 month moonshot is the full Spec Compiler (true bi-directional sync), which is explicitly delayed because it requires massive R&D.
We explicitly rejected the red niches: End-to-end orchestration is too bloated for an MVP. AI Code Review is a Red Ocean with established players. Autonomous Bug Bounties is too narrow a security focus. And PRD-to-Ticket automation sits too far away from the actual codebase.

---
<!-- .slide: id="differentiation" -->

## WHY: Differentiation

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 35%;">
    <col style="width: 65%;">
  </colgroup>
  <thead>
    <tr>
      <th>Differentiator</th>
      <th>JB advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Native JB Integration</strong></td>
      <td>We go where Enterprise sits. Native plugin: editable intermediate layers, zero context switch.</td>
    </tr>
    <tr>
      <td><strong>Deep Semantic Context</strong></td>
      <td>PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade accuracy, zero hallucination on structure. Not a permanent moat — a 12–18 month head start we convert into data and workflow lock-in.</td>
    </tr>
    <tr>
      <td><strong>Continuous drift detection</strong></td>
      <td>Proactive inline warnings + bi-directional sync (code ↔ spec) to prevent divergence.</td>
    </tr>
    <tr>
      <td><strong>AI-Native BDD (Evals)</strong></td>
      <td>Extracts specs from code via PSI → validates AI output against them → blocks non-conformant changes.</td>
    </tr>
    <tr>
      <td><strong>Zero Vendor Lock-in</strong></td>
      <td>Open standard (Markdown in Git) + Premium JB Plugin. Keeps IP safe if tool is uninstalled.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="padding: 10px 15px; margin-top: 10px;">
  <p>We bridge the gap between developer freedom and enterprise-level control: turning chaotic AI-assisted development into a predictable, specified, and reviewable architectural workflow.</p>
</div>

Notes:
Why us? Let's look at our 5 core differentiators.
First, Native JetBrains Integration—we go where Enterprise sits. Instead of a rigid, one-way CLI, developers get editable intermediate layers right in their IDE with zero context switch.
Second, Deep Semantic Context using JetBrains PSI, completely eliminating the hallucinations you get with standard AST or vector search in complex codebases.
Third, Continuous Drift Detection. We don't just offer proactive inline warnings; we provide bi-directional sync (code ↔ spec) so that artifacts never diverge, unlike reactive CI breaks or flat docs that rot over time.
Fourth, AI-Native BDD (Behavior-Driven Development). We don't just 'generate and pray'—we treat specs as executable tests, automatically validating the LLM's output against the schema before it ever hits your code.
And finally, Zero Vendor Lock-in with an open markdown format combined with a premium plugin.
These differentiators culminate in our core value proposition: We bridge the gap between developer freedom and enterprise control. Instead of forcing rigid top-down workflows that developers hate, Bonsai embraces bottom-up intent extraction—turning chaotic "vibe-coding" into a predictable, reviewable architectural workflow, right inside the JetBrains IDE.

PSI advantage is structural, not exclusive — any JB plugin can use PSI, and LSP + tree-sitter cover ~60-70% outside JB.
The defensibility comes from compounding: PSI accuracy → better specs → users trust and maintain specs → spec data becomes the real moat (not the parser).
Token savings estimate: 70-90% per file analysis vs raw LLM approach. At org scale (100 commits/day, 50 files/commit), this is ~$1,300/month cost difference.

---
<!-- .slide: id="jb-strategic-fit" -->

## WHY: JetBrains Strategic Fit

<div class="chosen-grid chosen-grid--small">

  <div class="chosen-tile chosen-tile--green chosen-tile--wide">
    <p class="chosen-tile-label">Positioning within JB AI Portfolio</p>
    <p class="chosen-tile-body">Bonsai is the <strong>governance layer</strong> for JB's AI stack: AI Assistant generates code, Junie executes autonomously, Bonsai ensures both stay aligned with architectural intent.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Complements (not competes)</p>
    <div class="chosen-tile-body">
      <table style="font-size: 0.75em; width: 100%; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 4px 0;"><strong>AI Assistant</strong></td>
          <td style="padding: 4px 0;">Generates code → Bonsai validates output against spec before merge</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 4px 0;"><strong>Junie</strong></td>
          <td style="padding: 4px 0;">Autonomous agent → Bonsai provides guardrails + drift alerts for agent actions</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 4px 0;"><strong>Fleet</strong></td>
          <td style="padding: 4px 0;">Not in MVP scope. Potential future surface once spec format stabilizes.</td>
        </tr>
        <tr>
          <td style="padding: 4px 0;"><strong>Marketplace</strong></td>
          <td style="padding: 4px 0;">Distribution channel: 1-click install, same billing, familiar UX</td>
        </tr>
      </table>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Business Case for JB</p>
    <div class="chosen-tile-body">
      <ul style="font-size: 0.85em; padding-left: 15px; margin: 0;">
        <li><strong>Attach rate ↑:</strong> Bonsai gives Enterprise buyers a reason to stay on JB IDE over Cursor/VS Code</li>
        <li><strong>ARPU ↑:</strong> Pro bundled with AI subscription; Team/Enterprise as separate SKU</li>
        <li><strong>Retention ↑:</strong> Spec data creates switching cost — specs are tied to JB PSI quality</li>
        <li><strong>Competitive moat:</strong> Only JB can offer PSI-grade analysis natively; competitors need LSP approximation</li>
      </ul>
    </div>
  </div>

</div>

Notes:
This slide is critical for internal alignment. Bonsai is not a standalone product — it's the missing governance piece in JB's AI portfolio.

The key strategic argument: as AI Assistants and autonomous agents generate more code, the need for a control layer grows proportionally. Without governance, AI-generated code becomes a liability for enterprise customers. Bonsai turns that liability into a selling point.

Specifically:

- AI Assistant users get spec-validated outputs → higher trust → higher usage → higher renewal
- Junie (autonomous agent) gets architectural guardrails → safer autonomy → enterprise adoption unlocked
- Enterprise buyers get audit trail + compliance artifacts → procurement unblocked

Revenue model: Bonsai Pro is bundled (increases AI subscription stickiness). Bonsai Team/Enterprise is a separate revenue stream via JB Sales.

Risk of NOT building this: if a competitor (Kiro/Amazon, CodeSpeak) becomes the governance standard, JB AI tools become "generation without control" — a weaker value proposition for enterprise.

---
<!-- .slide: id="why-summary" -->

## WHAT & WHY: Summary

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 8px;">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Strategic Alignment</p>
    <p class="chosen-tile-body">AI adoption hit 90% but distrust surged +15pp. Empowering JetBrains IDEs into the governance standard: powered by the community, built for the industry.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Market Size <span class="metric-badge">A</span></p>
    <p class="chosen-tile-body"><a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=856599423#gid=856599423&range=A1" target="_blank" style="color: inherit; text-decoration: underline;">TAM ($4.9B) → SAM ($3.4B) → SOM ($171M)</a><br><br><a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=A1" target="_blank" style="color: inherit; text-decoration: underline;">Bottom-up SOM (Year 1): $9.3M</a></p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Differentiation</p>
    <p class="chosen-tile-body">Bi-directional spec↔code in IDE via PSI. We extract specs from code (zero friction), push to CI, and locally detect drift.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Growth Loops</p>
    <p class="chosen-tile-body">Champion-driven adoption via repo-native specs + CI gates. Supported by reviewer loop & ecosystem distribution. <a href="#/growth-loops">Details</a></p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Metrics</p>
    <p class="chosen-tile-body">NSM: Devs w/ ≥1 spec-linked merge/wk. Key: New MRR (paid tiers) & Attributed MRR (JB core via attach rate/retention).</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Monetization</p>
    <p class="chosen-tile-body">Free (viral seed). Pro ($8-12/mo) for power users. Team ($15-20/seat) for org budgets. Enterprise ($30-50) for security & SSO.</p>
  </div>

</div>

<ul class="distrust-notes" style="margin-top: 15px;">
<li>Assumptions <span class="metric-badge">A</span> for TAM/SAM/SOM are indicated in the linked calculations.</li>
<li>Market Size Revenue base year 2024, adoption base year 2025.</li>
<li>We assumed a conservative $4.91B (2024) base TAM to avoid overvaluation.</li>
</ul>

<div style="height: 40px;"></div>

Notes:

- Рынок AI-тулзов оценивается по-разному (~$4–5B). Чтобы не завышать TAM, мы берем консервативную базу $4.91B (2024), сохраняя альтернативный апсайд-сценарий.
- Ожидаемый рост через Tech Lead'ов легко скейлится благодаря "repo-native loop" и CI/PR гейтам.

---
<!-- .slide: id="roadmap" -->

## HOW: 6-Month Roadmap

<div class="roadmap-container">

  <div class="roadmap-item">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Month 0-2 <span class="roadmap-gate">G1</span></span>
    </div>
    <div class="roadmap-content">
      <div class="roadmap-content-title">PHASE 1: MVP & VALIDATION</div>
      <div class="roadmap-content-body">
        • <strong>Ship MVP:</strong> code extraction + drift detection<br>
        • Recruit 10 design partners (Tech Leads, 5+ devs)<br>
        • <strong>Gate 1:</strong> ≥ 60% validation + 3 partners paying
      </div>
    </div>
  </div>

  <div class="roadmap-item">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Month 2-4 <span class="roadmap-gate">G2</span></span>
    </div>
    <div class="roadmap-content">
      <div class="roadmap-content-title">PHASE 2: HARDEN</div>
      <div class="roadmap-content-body">
        • <strong>Bi-directional sync:</strong> add spec→code generation<br>
        • PR integration: spec-delta visibility in code reviews<br>
        • <strong>Gate 2:</strong> ≥ 20% review reduction + 5 partners paying
      </div>
    </div>
  </div>

  <div class="roadmap-item">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Month 4-6 <span class="roadmap-gate">G3</span></span>
    </div>
    <div class="roadmap-content">
      <div class="roadmap-content-title">PHASE 3: SCALE</div>
      <div class="roadmap-content-body">
        • <strong>Orchestration:</strong> CI gate enforcement (rollout)<br>
        • Multi-repo spec management + Marketplace MVP<br>
        • <strong>Gate 3:</strong> ≥ 100 active users + positive economics signal
      </div>
    </div>
  </div>

</div>

<p class="chosen-tile-body" style="text-align: center; margin-top: 10px; font-size: 0.45em; opacity: 0.8;">
  <strong>Decision framework:</strong> Each gate requires quantitative metrics + qualitative signal + zero kill signals.
</p>

Notes:

Execution follows three strictly gated phases:

1) Phase 1 is all about value validation. Do devs actually review and maintain these extracted specs? If validation rate is low, we don't scale.
2) Phase 2 moves to bi-directional sync (our moonshot). We prove ROI by measuring actual time reduction in PR reviews.
3) Phase 3 is scale and monetization. Enterprise features like CI gates and multi-repo management are added here once the core loop is proven.
4) We focus on JetBrains ecosystem first to exploit our PSI integration advantage.

Team plan:
• Phase 1 (Mo 0–2): 1 PM + 2 engineers (1 JB plugin/PSI, 1 backend/LLM integration). Total: 3 people.
• Phase 2 (Mo 2–4): +1 engineer (CI/PR integration + spec-delta rendering). Total: 4 people.
• Phase 3 (Mo 4–6): +1 designer (onboarding UX + dashboard) + 1 DevRel (community, design partners, content). Total: 6 people.
• Assumption: engineers are familiar with Kotlin + IntelliJ Plugin SDK. If hired externally, add 2–4 weeks ramp-up to Phase 1 timeline.
• Budget note: Phase 1–2 headcount fits within a typical JB incubation team. Phase 3 expansion is gated on G2 pass.

---
<!-- .slide: id="segmentation" -->

## HOW: Segmentation

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: 1fr 1fr;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Early Adopters</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Who:</strong> Tech Lead, Senior Engineer.</p>
      <p style="margin-bottom: 8px;"><strong style="color: var(--r-main-color);">Sub JTBD:</strong> Task-level predictability.</p>
      <p style="margin-bottom: 3px; font-weight: bold; color: var(--r-main-color);">Top Problems</p>
      <ul style="margin: 0 0 8px 0; padding-left: 18px;">
        <li>Unscoped AI diffs</li>
        <li>Spec ↔ code drift</li>
        <li>Costly regressions</li>
      </ul>
      <p style="margin-bottom: 3px; font-weight: bold; color: var(--r-main-color);">Top Triggers</p>
      <ul style="margin: 0; padding-left: 18px;">
        <li>AI-caused prod incidents</li>
        <li>Review churn rising</li>
        <li>Major codebase refactor</li>
      </ul>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Scaling</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Who:</strong> EM, Dir of Eng, Security.</p>
      <p style="margin-bottom: 8px;"><strong style="color: var(--r-main-color);">Sub JTBD:</strong> Org-wide governance.</p>
      <p style="margin-bottom: 3px; font-weight: bold; color: var(--r-main-color);">Top Problems</p>
      <ul style="margin: 0 0 8px 0; padding-left: 18px;">
        <li>No standard for AI dev</li>
        <li>Risk across many repos</li>
        <li>Low auditability</li>
      </ul>
      <p style="margin-bottom: 3px; font-weight: bold; color: var(--r-main-color);">Top Triggers</p>
      <ul style="margin: 0; padding-left: 18px;">
        <li>Scaling AI across teams</li>
        <li>Security/compliance audit</li>
        <li>Incidents across repos</li>
      </ul>
    </div>
  </div>
</div>

Notes:
We target two distinct segments. First, Early Adopters — Tech Leads feeling the immediate pain of AI-caused bugs and unscoped diffs.
Second, when expanding across the org, we target Scaling personas — Engineering Directors and Security who need standardization and auditability.

---
<!-- .slide: id="mvp-solution-draft" -->

<h2>HOW: MVP SOLUTION DRAFT</h2>

<div class="solution-draft-container">
<div class="solution-mockup">
<div style="padding: 2.5rem; width: 100%; text-align: left;">
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
<div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #10b981; padding-bottom: 0.75rem; margin-bottom: 1rem;">
<span style="font-weight: 900; color: #1e293b; font-size: 0.8em; letter-spacing: -0.02em;">Bonsai Spec View</span>
<span style="background: #10b981; color: white; border-radius: 12px; padding: 2px 10px; font-size: 0.4em; font-weight: 800;">SYNCED</span>
</div>
<div style="margin-bottom: 1.5rem;">
<p style="color: #64748b; font-size: 0.35em; margin-bottom: 0.5rem; font-weight: 600; text-transform: uppercase;">Extracted from <code>auth_engine.kt</code></p>
<div style="background: white; border-radius: 4px; padding: 1rem; border: 1px dashed #cbd5e1;">
<p style="color: #334155; font-size: 0.5em; line-height: 1.5; margin: 0;">
• <strong>Flow:</strong> User → OAuth → JWT Entry<br>
• <strong>Requirement:</strong> Session must expire in 2h<br>
• <strong>Security:</strong> All secrets via Vault
</p>
</div>
</div>
<div style="display: flex; gap: 8px;">
<div style="background: #f1f5f9; border-radius: 4px; flex: 1; height: 12px;"></div>
<div style="background: #10b981; border-radius: 4px; width: 60px; height: 32px; display: flex; align-items: center; justify-content: center; color: white; font-size: 0.35em; font-weight: 800;">APPROVE</div>
</div>
</div>
<p style="text-align: center; color: #94a3b8; font-size: 0.35em; margin-top: 1.5rem; font-style: italic;">"JetBrains PSI analyses code → Bonsai generates spec → Dev validates in-loop"</p>
</div>
</div>

<div class="chosen-grid chosen-grid--2col chosen-grid--small">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Strategic wedge</p>
    <p class="chosen-tile-body">JetBrains users (IntelliJ), 5+ devs, repo-native arch-specs (.md).</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Product</p>
    <p class="chosen-tile-body">Bonsai: Native JB Plugin. Zero context switch.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Core Logic</p>
    <p class="chosen-tile-body">Code-first: PSI-based spec gen + real-time drift detection.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Tech layer</p>
    <p class="chosen-tile-body">Kotlin / PSI Engine. High-precision alerts. Open .md standard.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Launch</p>
    <p class="chosen-tile-body">Canary rollout: 10 design partners → Private alpha.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Learning gate</p>
    <p class="chosen-tile-body">≥ 60% validation rate; alert engagement.</p>
  </div>
</div>
</div>

Notes:

1) **Strategic Wedge**: We don't change how devs work. They write code, we sync the spec. This removes the "documentation tax".
2) **Logic**: Bi-directional sync is the end-game, but we start with "Extraction First" because it's the fastest path to value.
3) **PSI Engine**: Using JetBrains' native engine means we have deeper understanding than generic LLM-based tools.
4) **Drift**: The moment code stops matching the spec, the dev gets a red light in the IDE.

---
<!-- .slide: id="pricing-monetization" -->

## HOW: Pricing & Monetization

<div class="distrust-table-wrapper">
<table class="distrust-table">
  <thead>
    <tr>
      <th style="width: 14%;">Tier</th>
      <th style="width: 6%;">Price</th>
      <th style="width: 50%;">Included</th>
      <th style="width: 30%;">Goal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Free</strong></td>
      <td>$0</td>
      <td>Spec extraction (≤3 repos), basic drift, markdown export</td>
      <td>Adoption, viral seed</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>Pro</strong></td>
      <td>$8–12/mo</td>
      <td>Unlimited repos, CI integration, spec history</td>
      <td>Prove WTP, convert power users</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>Team</strong></td>
      <td>$15–20/seat</td>
      <td>Shared library, org dashboard, PR spec-delta</td>
      <td>Land team budget, org expansion</td>
    </tr>
    <tr>
      <td><strong>Enterprise</strong></td>
      <td>$30–50 floor</td>
      <td>SSO, audit log, SLA, self-hosted option</td>
      <td>Security-driven buy</td>
    </tr>
  </tbody>
</table>
</div>

<div class="chosen-grid chosen-grid--2col chosen-grid--small">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Pricing Rationale & Integration</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li><strong>JB AI Add-on:</strong> Pro aligns with $8.33/mo base tool.</li>
        <li><strong>Team Budget:</strong> $15-20 competes with CodeRabbit/Cursor.</li>
        <li><strong>Integration:</strong> Pro bundled in JB AI; Team sold via Sales.</li>
      </ul>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Validation Experiments</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li><strong>WTP Test (Mo 2):</strong> 5 partners at $10/mo vs free trial.</li>
        <li><strong>Team Test (Mo 4):</strong> $15/seat vs $20/seat with CI gates.</li>
      </ul>
    </div>
  </div>
</div>

Notes:
Pricing rationale:

- JB AI Assistant = $8.33/month → Pro tier aligns as add-on (не дороже base tool)
- CodeRabbit = $12/seat/month → Team tier at $15–20 includes more SDLC coverage
- Cursor Pro = $20/month → в том же бюджетном «карман» разработчика

Two key experiments:

1. WTP test (Month 2): Offer 5 design partners «Pro for $10/month» — measure conversion vs «Pro for free extended trial». If <30% convert at $10, test $5.
2. Team pricing test (Month 4): Offer 3 orgs «Team at $15/seat» vs «Team at $20/seat with CI gates included». Measure which feature drives budget approval.

JB integration model (preferred):

- Bonsai Pro = included in JB AI Pro subscription (bundle uplift)
- Bonsai Team/Enterprise = separate SKU, sold via JB Sales
- Metric: attributed ARPU uplift on JB AI Pro cohort with Bonsai active

---
<!-- .slide: id="risks-mitigation" -->

<h2>HOW: Risks & Mitigation</h2>

<div class="risk-table-container">
  <table class="risk-table">
    <thead>
      <tr>
        <th class="col-num">#</th>
        <th class="col-risk">Risk Name</th>
        <th class="col-mitigation">Mitigation Strategy</th>
        <th class="col-status">Impact</th>
        <th class="col-status">Prob.</th>
        <th class="col-score">Score</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="col-num"><strong>0</strong></td>
        <td class="col-risk"><strong>Solution-Problem Fit: specs may not be what developers want</strong></td>
        <td class="col-mitigation">Phase 1 dual-track: (a) test spec extraction value with 10 partners, (b) parallel test of 2 alternative approaches (review assist, security gates) via lightweight prototypes. Gate 1 includes comparative signal.</td>
        <td class="col-status text-high"><strong>High</strong></td>
        <td class="col-status text-med"><strong>Med</strong></td>
        <td class="col-score"><strong>6</strong></td>
      </tr>
      <tr>
        <td class="col-num">1</td>
        <td class="col-risk">PSI Engine Complexity</td>
        <td class="col-mitigation">Focus on JetBrains ecosystem (Kotlin first), leverage native PSI APIs for stability.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">2</td>
        <td class="col-risk">Developer Friction</td>
        <td class="col-mitigation">Zero-friction code-first extraction. Repo-native .md format lives in current workflow.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">3</td>
        <td class="col-risk">Competitor Entry</td>
        <td class="col-mitigation">Deep IDE-native PSI integration provides a semantic moat generic LLMs lack.</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">4</td>
      </tr>
      <tr>
        <td class="col-num">4</td>
        <td class="col-risk">AI Hallucinations</td>
        <td class="col-mitigation">Human-in-the-loop "Approve" gate before syncing specs. High-precision prompt tuning.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-low">Low</td>
        <td class="col-score">3</td>
      </tr>
      <tr>
        <td class="col-num">5</td>
        <td class="col-risk">Adoption Tax</td>
        <td class="col-mitigation">Strategic wedge: extract from existing code, don't force devs to write from scratch.</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-low">Low</td>
        <td class="col-score">2</td>
      </tr>
    </tbody>
  </table>
</div>

Notes:

Risk #0 is our highest-priority uncertainty. Developers report distrust in AI code (validated), but they do not explicitly ask for specs (hypothesis). If Phase 1 shows <40% spec engagement AND alternative approaches score higher in partner feedback, we pivot before Phase 2.

1) **Technical**: We are building on top of JetBrains' own infrastructure. It's complex, but it's where our advantage lies.
2) **Accuracy**: AI is the assistant, not the decider. The "Approve" button is our safety valve.
3) **Adoption**: Documentation fails when it's external. By making it part of the repo and extraction-based, we remove the "writing tax".
4) **Market**: Cursor/Copilot focus on code generation. We focus on structural alignment and predictability.

---

<!-- .slide: id="gtm" -->

<h2>HOW: GTM Strategy</h2>

<div class="grid-2x2" style="font-size: 0.85em;">

  <div class="feature-box">
    <div class="feature-title" style="color: var(--jb-blue);">1. PoC & Early Adopters</div>
    <ul class="text-sm" style="margin-top: 5px;">
      <li><strong>Target:</strong> JB Power Users, Tech Leads, DevEx.</li>
      <li><strong>Motion:</strong> "Golden path" to PR in 10 mins. <a href="#/golden-path">Details</a></li>
      <li><strong>Goal:</strong> Validate spec extraction & diff control.</li>
    </ul>
  </div>

  <div class="feature-box">
    <div class="feature-title" style="color: var(--jb-purple);">2. Early Monetization</div>
    <ul class="text-sm" style="margin-top: 5px;">
      <li><strong>Offer:</strong> Paid Design Partners, early Team packs.</li>
      <li><strong>Model:</strong> Add-on to JB AI credits (shared quota).</li>
      <li><strong>Goal:</strong> Prove WTP & secure team budget early.</li>
    </ul>
  </div>

  <div class="feature-box">
    <div class="feature-title" style="color: var(--jb-orange);">3. Scale Sales</div>
    <ul class="text-sm" style="margin-top: 5px;">
      <li><strong>Distribution:</strong> JB IDE Promo, Toolbox, Marketplace.</li>
      <li><strong>Motion:</strong> PLG loop (Indiv. &rarr; Team org policy).</li>
      <li><strong>Goal:</strong> Zero-friction install to paid conversion.</li>
    </ul>
  </div>

  <div class="feature-box">
    <div class="feature-title" style="color: var(--jb-green);">4. Market Standard</div>
    <ul class="text-sm" style="margin-top: 5px;">
      <li><strong>OSS Core:</strong> Spec Format v1, CLI, Validator.</li>
      <li><strong>Ecosystem:</strong> Marketplace for hooks & templates.</li>
      <li><strong>Enterprise:</strong> Hosted orchestration & governance.</li>
    </ul>
  </div>

</div>

Notes:

1) **PoC**: We don't need a perfect product, we need a "golden path" that demonstrates value in 10 minutes.
2) **Monetization**: We charge early to validate willingness to pay. Using JB AI credits makes purchasing familiar.
3) **Scale**: The JetBrains ecosystem is our unfair advantage. One-click install via Toolbox/Marketplace.
4) **Standard**: We open-source the Spec Format and CLI to become the protocol, while monetizing the orchestration and governance.

---

<!-- .slide: id="metrics" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: Key Metrics & Guardrails</h2>

<div class="grid-2x2" style="font-size: 0.7em; gap: 4px; height: 500px;">

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-purple); margin-bottom: 2px;">1. North Star & Depth</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>NSM:</strong> WAU/WAO with &ge;1 spec-merge.</li>
      <li><strong>Depth & Coverage:</strong> Merges per active User. % of PRs spec-linked.</li>
    </ul>
  </div>

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-blue); margin-bottom: 2px;">2. Monetization & JB Core</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>Product:</strong> Net MRR, GRR / NRR.</li>
      <li><strong>JB Core Attributed:</strong> Attach, ARPU (Cohort matched).</li>
    </ul>
  </div>

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-green); margin-bottom: 2px;">3. Value & Expansion</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>Value / Expansion:</strong> Review iters &darr;, Gate pass &uarr;. Orgs hit 3+/10+ users.</li>
      <li><strong>Outcomes:</strong> Lead time &darr;, Deploy freq &uarr;.</li>
    </ul>
  </div>

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-red); margin-bottom: 2px;">4. Guardrails & Quality</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>IDE Loop:</strong> Build/run times at baseline.</li>
      <li><strong>Risk:</strong> Latency added, Policy hits vs incidents.</li>
    </ul>
  </div>

</div>

Notes:

1) **North Star**: Focus is on habitual usage (spec-linked merges), tracking both individual users and orgs.
2) **Monetization**: Tracking Net MRR for the product, and rigorously attributing JB Core revenue via matched cohort uplifts.
3) **Value**: Faster reviews and passing CI gates are our leading indicators for expansion to team-wide usage.
4) **Guardrails**: Above all, we must not harm the core IDE experience. Performance degradation is a strict No-Go.

---

<!-- .slide: id="experiments" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: First 30 Days — Validation Experiments</h2>

<div class="grid-2x2" style="font-size: 0.7em; gap: 4px; height: 500px;">

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-purple); margin-bottom: 2px;">1. Extraction Quality (PSI)</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>Question:</strong> Accurate spec creation?</li>
      <li><strong>GO:</strong> &ge; 3.5/5 score, &le; 30% edits.</li>
      <li><strong>Fail:</strong> Manual rework > 60%.</li>
    </ul>
  </div>

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-blue); margin-bottom: 2px;">2. Drift Detection Value</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>Question:</strong> Does it catch real bugs?</li>
      <li><strong>GO:</strong> &ge; 40% fix rate, &ge; 1 catch/week.</li>
      <li><strong>Fail:</strong> Alerts noisy, disabled by devs.</li>
    </ul>
  </div>

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-green); margin-bottom: 2px;">3. ICP Pain Priority</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>Question:</strong> Is drift a top-3 problem?</li>
      <li><strong>GO:</strong> &ge; 8/15 rank top-3, &ge; 5 pilots.</li>
      <li><strong>Fail:</strong> Problem too low priority.</li>
    </ul>
  </div>

  <div class="feature-box" style="padding: 5px; display: flex; flex-direction: column; justify-content: center;">
    <div class="feature-title" style="color: var(--jb-red); margin-bottom: 2px;">4. Timeline (Weeks 1-4)</div>
    <ul class="text-sm" style="margin-top: 0; line-height: 1.2;">
      <li><strong>W1:</strong> Telemetry + Recruit partners.</li>
      <li><strong>W2-3:</strong> Run parallel experiments (1-2).</li>
      <li><strong>W4:</strong> ICP interviews & Gate 1 Decision.</li>
    </ul>
  </div>

</div>

Notes:

1) **Quick Feedback Loop**: Our initial month is entirely about proving the core hypothesis: "Devs find drift detection high-value, not noisy."
2) **Go/No-Go Decision**: If we fail the drift detection value test, we rethink the product narrative before further investment.
3) **PSI Depth**: Experiment 1 tells us if we need to refine the parser for Java/Kotlin or shift to LLM-heavy extraction.

---
<!-- .slide: id="appendix" -->

# Appendix

---
<!-- .slide: id="growth-loops" -->

## WHY: Growth Loops

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Champion-driven adoption</p>
    <p class="chosen-tile-body">1 dev adds <code>/specs</code> → CI gates & PR checks appear → whole team interacts → other teams copy →</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Invite-The-Reviewer Loop</p>
    <p class="chosen-tile-body">Specs create readable contracts → architects/sec engineers get invited to PRs → reviews speed up → format sticks →</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Multi-Repo Value Growth</p>
    <p class="chosen-tile-body">Reusable spec added to repo A → then repo B → better compatibility & fewer diffs → massive incentive to maintain</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Ecosystem Distribution</p>
    <p class="chosen-tile-body">Format works in Cursor, VS Code, CI → tried locally w/o migration → becomes org-wide standard, not just an app →</p>
  </div>

</div>

Notes:
Here we detail the 4 main B2B growth mechanics that drive viral product-led expansion across an enterprise.

1) Repo-native: Viral spread inside a single team via PR checks. This forces adoption simply by interacting with code.
2) Collaboration: Bringing non-coding stakeholders (architects, security) into the review process using readable contracts.
3) Org-wide Expansion: A single spec scales across multiple projects, accelerating adoption as its value grows with every added repository.
4) Ecosystem Agnosticism: Being an open format means it can be adopted without massive migration or forcing developers out of their favorite IDE.

---
<!-- .slide: id="golden-path" -->

## HOW: "Golden" Path

<div class="chosen-grid chosen-grid--2col">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Persona</p>
    <div style="font-size: 0.8em; margin-top: 10px;">
      <p><strong>Alex, Tech Lead</strong></p>
      <ul>
        <li>8-person backend team</li>
        <li>Kotlin monorepo</li>
        <li>Daily JB AI Assistant user</li>
      </ul>
    </div>
  </div>
  
  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Trigger (Friday Afternoon)</p>
    <div style="font-size: 0.8em; margin-top: 10px;">
      <p>PR from junior: 400+ lines AI-refactored auth module.</p>
      <ul>
        <li>Alex can't tell if session logic changed.</li>
        <li>Spends 45m line-by-line review.</li>
        <li>PR gets "Request Changes". Junior frustrated.</li>
      </ul>
      <p style="margin-top: 10px; font-style: italic; color: #ff8a80;">"There has to be a better way."</p>
    </div>
  </div>
</div>

Notes:
Persona: Alex, Tech Lead, 8-person backend team, Kotlin monorepo, using JB AI Assistant daily.
Trigger: Friday afternoon. Alex reviews a PR from a junior dev who used AI to refactor the auth module. The diff is 400+ lines. Alex can't tell if the session expiry logic changed or not. He spends 45 minutes line-by-line. The PR gets "Request Changes". The junior is frustrated. Alex thinks: "There has to be a better way."

---
<!-- .slide: id="golden-path-steps" -->

## HOW: "Golden" Path

<div class="distrust-table-wrapper">
<table class="distrust-table">
  <thead>
    <tr>
      <th style="width: 8%;">Min</th>
      <th style="width: 12%;">Alex does</th>
      <th style="width: 33%;">Bonsai does</th>
      <th style="width: 47%;">Alex sees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>0:00</strong></td>
      <td>Installs Bonsai from JB Marketplace (1-click)</td>
      <td>—</td>
      <td>Plugin appears in sidebar</td>
    </tr>
    <tr>
      <td><strong>1:00</strong></td>
      <td>Right-clicks <code>auth_engine.kt</code> → "Extract Spec"</td>
      <td>PSI parses classes, methods, annotations, deps. Sends structured pre-prompt (200 tokens) to LLM.</td>
      <td>Loading spinner (2–3 sec)</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>1:30</strong></td>
      <td>Reads generated spec in side panel</td>
      <td>—</td>
      <td>[SYNCED] Flow: User→OAuth→JWT. Session: 2h. Secrets: Vault-only.</td>
    </tr>
    <tr>
      <td><strong>2:30</strong></td>
      <td>Edits: adds "Rate limit: 5 attempts/15 min"</td>
      <td>Saves as <code>/specs/auth_engine.spec.md</code></td>
      <td>[EDITED]</td>
    </tr>
    <tr>
      <td><strong>3:00</strong></td>
      <td>Alex goes home happy.</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>4:00</strong></td>
      <td>Junior pushes commit: session expiry → 4h</td>
      <td>Detects drift: spec says 2h, code says 4h</td>
      <td>[DRIFT]: 47 — Session changed 2h→4h</td>
    </tr>
    <tr>
      <td><strong>5:00</strong></td>
      <td>Alex opens PR — sees spec-delta summary at top</td>
      <td>Auto-generates: "1 drift detected, 1 new endpoint, 0 removed"</td>
      <td>Review time: 5 min instead of 45 min</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>7:00</strong></td>
      <td>Alex clicks "Update Spec" (accepts 4h change) OR "Request Fix"</td>
      <td>If accepted: spec auto-updates. If rejected: blocks merge until code reverts.</td>
      <td>[RESOLVED]</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Result:</strong> 45-minute blind review → 7-minute spec-guided review. Spec becomes the shared contract between author and reviewer.</p>
</div>

Notes:
This walkthrough shows the complete user journey in under 10 minutes.
Key moments: minute 1:30 (first spec extracted — immediate value), minute 4:00 (first drift caught — the "aha" moment), minute 7:00 (resolution — the workflow completes).
The critical insight: Alex never had to *write* a spec. He only had to *read and approve* one. That's the difference between Bonsai and every previous documentation tool.
The 45→7 minute improvement is our core value metric, tested in Phase 1 with design partners.

---
<!-- .slide: id="distrust-issues" -->

## WHAT: Distrust issues

<div class="distrust-table-wrapper">
<table class="distrust-table">
<thead>
<tr>
<th>Trust points (when utilizing AI)</th>
<th>Details</th>
<th class="center">Reach <span class="metric-badge">A</span></th>
<th class="center">Freq. <span class="metric-badge">A</span></th>
<th class="center">Conf. <span class="metric-badge">A</span></th>
<th class="center">Score <span class="metric-badge">A</span></th>
</tr>
</thead>
<tr class="highlight-row">
<td>Skepticism regarding code accuracy and quality</td>
<td>46% distrust AI (up 15 pp YoY). 75% would ask a person for help when they don’t trust AI answers. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center score val-high">9</td>
</tr>
<tr class="highlight-row">
<td>Increased review and debugging time</td>
<td>45% say debugging AI code is more time-consuming. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center score val-high">9</td>
</tr>
<tr>
<td>Concerns regarding security and vulnerabilities</td>
<td>&gt;60% frequently have ethical / security-related concerns about AI-generated code. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-med">Med</td>
<td class="center score val-high">7</td>
</tr>
<tr>
<td>AI decision-making opacity and ambiguous accountability for errors</td>
<td>75% would ask a person for help when they don’t trust AI answers, keeping humans as final arbiters of correctness. <a href="https://arxiv.org/html/2502.18468v1" target="_blank">[1]</a> <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[2]</a></td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center score val-med">3</td>
</tr>
<tr>
<td>Risk of engineering skill degradation</td>
<td>60% believe AI tools lead to less skilled developers (web-dev firstly). <a href="https://2025.stateofdevs.com/en-US/" target="_blank">[1]</a></td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center score val-low">2</td>
</tr>
<tr>
<td>Fear of data leaks and privacy concerns</td>
<td>40% of security incidents involve AI (incident-level). &gt;80% report concerns about data security and privacy. Frequency=Low because measured via incidents. <a href="https://www.microsoft.com/en-us/security/blog/2024/11/13/microsoft-data-security-index-annual-report-highlights-evolving-generative-ai-security-needs/" target="_blank">[1]</a> <a href="https://survey.stackoverflow.co/2025/a" target="_blank">[2]</a></td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center val-med">Med</td>
<td class="center score val-low">2</td>
</tr>
<tr>
<td>Legal uncertainty regarding copyrights and licensing for AI-generated code</td>
<td>Survey of 574 GenAI users: broad disagreement and uncertainty about output ownership and copyright risk. <a href="https://arxiv.org/html/2502.18468v1" target="_blank">[1]</a> <a href="https://arxiv.org/html/2411.10877v1" target="_blank">[2]</a></td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center val-med">Med</td>
<td class="center score val-low">2</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> Developers mainly don’t trust AI-generated code enough to ship it without extra time spent polishing, reviewing, and debugging.</p>
</div>

<ul class="distrust-notes">
<li>Reach, Freq. (Frequency), Conf. (Confidence, as a probability to make a difference) and Score are subjectively estimated/measured based on synthesis of external report signals. </li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

Notes:
Let's drill down into these distrust issues. We analyzed various market reports and extracted the major pain points. As you can see in this table, the top two issues—highlighted here—are skepticism regarding code accuracy and the increased review and debugging time. Both of these score a 9 when evaluating their Reach, Frequency, and our Confidence that solving them will make a difference. Security concerns are also very high but have slightly less consistent frequency of blocking daily workflows. Note that the scores and parameters are our subjective estimates based on these signals.

---
<!-- .slide: id="time-spend" -->

## WHAT: Dev Time Spent

<div class="timespend-table-wrapper">
<table class="timespend-table">
<thead>
<tr>
<th>Activity</th>
<th class="center">Actual</th>
<th class="center">Ideal</th>
<th class="center">Gap</th>
<th class="center">Prob. <span class="metric-badge">A</span></th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="highlight-row">
<td>Security/Compliance</td>
<td class="center">11.48%</td>
<td class="center">3.07%</td>
<td class="center score">8.40%</td>
<td class="center val-med">Med</td>
<td>Opportunity to improve on the planning step</td>
</tr>
<tr class="highlight-row">
<td>Communication</td>
<td class="center">12.95%</td>
<td class="center">6.57%</td>
<td class="center score">6.38%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>Debugging</td>
<td class="center">11.20%</td>
<td class="center">7.48%</td>
<td class="center score">3.72%</td>
<td class="center val-high">High</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Customer Support</td>
<td class="center">7.49%</td>
<td class="center">3.98%</td>
<td class="center score">3.50%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>Env Setup</td>
<td class="center">3.78%</td>
<td class="center">1.54%</td>
<td class="center score">2.24%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Monitoring/Dashboard</td>
<td class="center">2.94%</td>
<td class="center">2.24%</td>
<td class="center score">0.70%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Task Mgmt (ADO)</td>
<td class="center">2.03%</td>
<td class="center">1.33%</td>
<td class="center score">0.70%</td>
<td class="center val-med">Med</td>
<td>Opportunity to automate via agent orchestration</td>
</tr>
<tr>
<td>Code Refactoring</td>
<td class="center">5.25%</td>
<td class="center">4.75%</td>
<td class="center score">0.50%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Test Authoring</td>
<td class="center">4.83%</td>
<td class="center">5.17%</td>
<td class="center score">-0.34%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Documentation</td>
<td class="center">3.71%</td>
<td class="center">4.26%</td>
<td class="center score">-0.55%</td>
<td class="center val-med">Med</td>
<td>Automation already widely adopted</td>
</tr>
<tr>
<td>Mentoring/Onboarding</td>
<td class="center">2.59%</td>
<td class="center">3.70%</td>
<td class="center score">-1.11%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Tech Presentations</td>
<td class="center">0.56%</td>
<td class="center">1.68%</td>
<td class="center score">-1.12%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>PR/Code Review</td>
<td class="center">5.88%</td>
<td class="center">7.13%</td>
<td class="center score">-1.25%</td>
<td class="center val-low">Low</td>
<td>Human in the loop issue mostly depends on AI models base quality evolution</td>
</tr>
<tr>
<td>Learning New Tech</td>
<td class="center">2.52%</td>
<td class="center">6.57%</td>
<td class="center score">-4.05%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>System Arch/Design</td>
<td class="center">8.89%</td>
<td class="center">15.37%</td>
<td class="center score">-6.49%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
<tr class="highlight-row">
<td>Coding</td>
<td class="center">13.93%</td>
<td class="center">25.16%</td>
<td class="center score">-11.23%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> We see an opportunity to cut low-value overhead and reinvest the saved capacity into the core work developers value most: Coding & System Architecture/Design.</p>
</div>

<ul class="distrust-notes">
<li>Time spend data is based on <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf" target="_blank">Microsoft's Time-Warp Study</a>.</li>
<li>Prob.(Probability) = Probability to make a difference.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

Notes:
Here we look at how developers actually spend their time versus how they ideally want to spend it. The largest gaps—the overhead we can cut—are in Security & Compliance, Debugging, and Environment Setup. At the same time, we see massive negative gaps in Coding and System Architecture. Developers want to spend almost double the time on architecture and double the time on coding. If we can automate the high-gap overhead areas, we unlock capacity for the deep work that drives real product value and developer satisfaction.

---
<!-- .slide: id="b2b-pains" -->

## WHAT: B2B Pains

<div class="distrust-table-wrapper">
<table class="distrust-table">
<thead>
<tr>
<th>B2B Pain (Engineering / Product Teams)</th>
<th>Details</th>
<th class="center">Reach <span class="metric-badge">A</span></th>
<th class="center">Freq. <span class="metric-badge">A</span></th>
<th class="center">Conf. <span class="metric-badge">A</span></th>
<th class="center">Score <span class="metric-badge">A</span></th>
</tr>
</thead>
<tbody>
<tr class="highlight-row">
<td>Delivery predictability and lead time variability</td>
<td>Unpredictable reviewers make dependent work impossible to forecast reliably. <a href="https://axify.io/blog/lead-time-in-software-development" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center score val-high">5</td>
</tr>
<tr class="highlight-row">
<td>Quality and reliability risk from software errors</td>
<td>Poor software quality costs US companies $2.08 trillion annually. <a href="https://raygun.com/blog/cost-of-software-errors/" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-low">Low</td>
<td class="center score val-high">5</td>
</tr>
<tr>
<td>Documentation debt harming onboarding, satisfaction and speed</td>
<td>41% of developers report this as a major hindrance. 97% lose significant time to inefficiencies. <a href="https://www.atlassian.com/software/compass/resources/state-of-developer-2024" target="_blank">[1]</a></td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center score val-med">3</td>
</tr>
<tr>
<td>Developer burnout from cognitive load and on-call burden</td>
<td>83% of software engineers report feelings of burnout. <a href="https://www.softwareseni.com/developer-burnout-and-cognitive-load-in-the-devops-era/" target="_blank">[1]</a></td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center score val-low">2</td>
</tr>
<tr>
<td>Productivity loss from technical debt waste</td>
<td>Developers waste on average 23% of their time due to technical debt. <a href="https://research.chalmers.se/publication/511450/file/511450_Fulltext.pdf" target="_blank">[1]</a></td>
<td class="center val-low">Low</td>
<td class="center val-high">High</td>
<td class="center val-low">Low</td>
<td class="center score val-low">2</td>
</tr>
<tr>
<td>Compliance overhead from AI and tooling</td>
<td>Compliance overhead increases 10–20% in regulated industries due to AI audit and privacy controls. <a href="https://www.softwareseni.com/the-real-economics-of-ai-coding-beyond-vendor-productivity-claims/" target="_blank">[1]</a></td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center val-med">Med</td>
<td class="center score val-low">2</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> The two highest-scoring B2B pains — delivery unpredictability and quality risk — are directly amplified by uncontrolled AI-generated code entering review pipelines.</p>
</div>

<ul class="distrust-notes">
<li>Reach, Freq. (Frequency), Conf. (Confidence = probability to make a difference) and Score are subjectively estimated based on external report signals.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

Notes:
This slide zooms out from the developer to the business buyer. B2B buyers care about delivery predictability and software quality — both of which are threatened by unvetted AI output. The top two pains score equally at 5, driven by high reach across engineering orgs and strong argumentation from industry data. Compliance overhead is real but lower frequency, making it a secondary concern for the initial wedge.

---

---
<!-- .slide: id="differentiation-full" -->

## WHY: Differentiation - Full

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 35%;">
    <col style="width: 40%;">
  </colgroup>
  <thead>
    <tr>
      <th>Differentiator</th>
      <th>Current market</th>
      <th>JB advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Native JB Integration</strong></td>
      <td>Rigid one-way CLI terminal flows, Web SaaS, or separate IDEs.</td>
      <td>We go where Enterprise sits. Native plugin: editable intermediate layers, zero context switch.</td>
    </tr>
    <tr>
      <td><strong>Deep Semantic Context</strong></td>
      <td>Context via flat AST or text vectors. 1000–3000 tokens per file for LLM analysis.</td>
      <td>PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade accuracy, zero hallucination on structure. Not a permanent moat — a 12–18 month head start we convert into data and workflow lock-in.</td>
    </tr>
    <tr>
      <td><strong>Continuous drift detection</strong></td>
      <td>Steering files (Cursor Rules, CLAUDE.md) give persistent context but no enforcement. CI checks are reactive.</td>
      <td>Proactive inline warnings + bi-directional sync (code ↔ spec) to prevent divergence.</td>
    </tr>
    <tr>
      <td><strong>AI-Native BDD (Evals)</strong></td>
      <td>Blind generation ("generate and pray"). No automated validation of the LLM output.</td>
      <td>Extracts specs from code via PSI → validates AI output against them → blocks non-conformant changes.</td>
    </tr>
    <tr>
      <td><strong>Zero Vendor Lock-in</strong></td>
      <td>Closed SaaS databases (Devplan) or heavy IDE lock-in (Kiro).</td>
      <td>Open standard (Markdown in Git) + Premium JB Plugin. Keeps IP safe if tool is uninstalled.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="padding: 10px 15px; margin-top: 10px;">
  <p>We bridge the gap between developer freedom and enterprise-level control: turning chaotic AI-assisted development into a predictable, specified, and reviewable architectural workflow.</p>
</div>

Notes:
Why us? Let's look at our 5 core differentiators.
First, Native JetBrains Integration—we go where Enterprise sits. Instead of a rigid, one-way CLI, developers get editable intermediate layers right in their IDE with zero context switch.
Second, Deep Semantic Context using JetBrains PSI, completely eliminating the hallucinations you get with standard AST or vector search in complex codebases.
Third, Continuous Drift Detection. We don't just offer proactive inline warnings; we provide bi-directional sync (code ↔ spec) so that artifacts never diverge, unlike reactive CI breaks or flat docs that rot over time.
Fourth, AI-Native BDD (Behavior-Driven Development). We don't just 'generate and pray'—we treat specs as executable tests, automatically validating the LLM's output against the schema before it ever hits your code.
And finally, Zero Vendor Lock-in with an open markdown format combined with a premium plugin.
These differentiators culminate in our core value proposition: We bridge the gap between developer freedom and enterprise control. Instead of forcing rigid top-down workflows that developers hate, Bonsai embraces bottom-up intent extraction—turning chaotic "vibe-coding" into a predictable, reviewable architectural workflow, right inside the JetBrains IDE.

PSI advantage is structural, not exclusive — any JB plugin can use PSI, and LSP + tree-sitter cover ~60-70% outside JB.
The defensibility comes from compounding: PSI accuracy → better specs → users trust and maintain specs → spec data becomes the real moat (not the parser).
Token savings estimate: 70-90% per file analysis vs raw LLM approach. At org scale (100 commits/day, 50 files/commit), this is ~$1,300/month cost difference.
