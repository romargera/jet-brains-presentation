<!-- markdownlint-disable MD033 -->

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

<div style="width: 100%; max-width: 820px; margin: 0 auto;">
<div class="agenda-nav">
  <div class="agenda-section">
    <h4>WHAT</h4>
    <div style="font-size: 0.6em; color: var(--text-main); margin: 0 0 6px;">Define the problem and pick a direction</div>
  </div>
  <div class="agenda-section">
    <h4>WHY</h4>
    <div style="font-size: 0.6em; color: var(--text-main); margin: 0 0 6px;">Map the market and justify the approach</div>
  </div>
  <div class="agenda-section">
    <h4>HOW</h4>
    <div style="font-size: 0.6em; color: var(--text-main); margin: 0 0 6px;">Roadmap, MVP, metrics, risks</div>
  </div>
</div>

<ul class="distrust-notes">
  <span class="metric-badge">A</span> Assumptions are marked with this icon
</ul>
</div>

Notes:
The presentation has three parts. First, **What** — problem framing through a real user story, JTBD, and strategic direction choice. Second, **Why** — competitor landscape, approach comparison, niche and entry strategy, differentiation. Third, **How** — execution roadmap, MVP, monetization, metrics, risks, GTM, and first-month actions. Let's start with the problem.

---
<!-- .slide: id="what-icp-jtbd" -->

## WHAT: Issue signal*

<div style="width: 100%; max-width: 90%; margin: 0 auto;">
<div style="margin: 40px 0; max-width: none; width: 100%; background: #1a1a1a; border-left: 4px solid #81c784; border-radius: 4px; padding: 16px 18px; text-align: left; position: relative; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.3); box-sizing: border-box; display: grid; grid-template-columns: 64px 1fr; gap: 10px; align-items: start;">
  <img src="Personas/photo_2026-03-12_19-49-00.jpg" alt="Alex portrait" style="width: 64px; height: 64px; border-radius: 6px; border: 1px solid rgba(129, 199, 132, 0.45); object-fit: cover; display: block;">
  <div style="position: relative;">
    <div style="position: absolute; top: -8px; left: -2px; font-size: 2.8em; color: rgba(129, 199, 132, 0.15); font-family: serif; line-height: 1; pointer-events: none;">&ldquo;</div>
    <p style="font-size: 0.66em; line-height: 1.5; color: #e0e0e0; font-style: italic; margin: 0 0 8px 0; font-weight: 400; position: relative; z-index: 1;">"AI-generated code is often useful, but not production-ready. What used to be a 5-minute review can easily turn into 45 minutes of review, re-prompting, and cleanup."</p>
    <div style="font-size: 0.66em; color: var(--text-muted); position: relative; z-index: 1;"><span style="line-height: 1.5; color: #e0e0e0; font-style: italic; font-weight: 400;">(c) Alex</span>, <span style="font-style: italic;">Tech Lead, Kotlin + Gemini</span></div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 10px; border-left: 4px solid #34d399; background: rgba(16, 185, 129, 0.12); border-color: rgba(52, 211, 153, 0.35);">
  <p><strong>Takeaway:</strong> The core friction in AI adoption isn't writing code — it's the unpredictability and review bottlenecks caused by unscoped AI diffs.</p>
</div>

<ul class="distrust-notes">
  * Preliminary signal. N=1 exploratory interview. Systematic validation: Month 1.
</ul>
</div>

Notes:
We start with a concrete pain point. Alex, a Tech Lead on an 8-person backend team, uses JB AI Assistant daily. On Friday afternoon he gets a PR from a junior — 400+ lines of AI-refactored auth module. He can't tell if the session expiry logic actually changed. After 45 minutes of line-by-line review, the PR gets "Request Changes". Both are frustrated.
This maps directly to our Core JTBD: "When I use AI to write code, I want it to be predictable so I don't break production."

* The signal check quote comes from an exploratory conversation with a developer matching our target ICP. Full validation is planned for Month 1 with 10-15 design partners.

---
<!-- .slide: id="adoption-paradox" -->

## WHAT: The AI Adoption Paradox

<p class="slide-subtitle"></p>

<div style="width: 100%; max-width: 95%; margin: 0 auto;">
<div class="adoption-layout" style="margin: 10px 0; max-width: none; width: 100%;">
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
<span class="adoption-metric-name" style="color: var(--text-muted);">DISTRUST (SOMEWHAT + HIGH)</span>
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
<span class="adoption-metric-name" style="color: var(--text-muted);">UNFAVORABLE SENTIMENT</span>
</div>
</div>
<p class="adoption-source"><a href="https://survey.stackoverflow.co/" target="_blank">Stack Overflow Developer Survey 2025</a></p>
</div>
</div>

<div class="adoption-takeaway">
  <p><strong>Takeaway:</strong> 90% adoption + 15pp distrust surge → developers use AI for speed but reject unpredictable output → our opportunity: make AI-assisted dev predictable.</p>
</div>
</div>

Notes:
Let's start with the market signal. AI adoption among developers has hit 90% — up 14% year over year, according to Google's DORA report. But here's the paradox: adoption is up, yet trust is collapsing. Stack Overflow's 2025 survey shows unfavorable sentiment toward AI jumped 14 points in one year. Trust dropped from 43% to 33%. And active distrust — developers who say they distrust AI output — surged from 30% to nearly 46%. The takeaway is clear: developers use AI because it's fast, but they don't trust it — because the output is unpredictable and hard to control. This is the gap we're going after.

---
<!-- .slide: id="stream-options" -->

## WHAT: Strategic Directions

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 10px;"><a href="#/stream-options-main-appendix" style="color: var(--accent-blue);">Prioritized</a> across <a href="#/distrust-issues" style="color: var(--accent-blue);">distrust</a>, <a href="#/time-spend" style="color: var(--accent-blue);">time spent</a>, and <a href="#/b2b-pains" style="color: var(--accent-blue);">B2B issues</a>.</p>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 10px; align-items: stretch; margin-top: 2px; width: 95%; margin-left: auto; margin-right: auto;">
  <div class="chosen-tile chosen-tile--green">
    <div>
      <p class="chosen-tile-label">1 Spec-driven Control</p>
      <div class="chosen-tile-body">
        <p style="font-size: 0.82em; line-height: 1.32;">Makes AI output visible, reviewable, and predictable.</p>
      </div>
    </div>
  </div>

  <div class="chosen-tile" style="border: 1px solid rgba(96, 165, 250, 0.42); background: rgba(37, 99, 235, 0.12);">
    <div>
      <p class="chosen-tile-label">2 Review &amp; Debug Assist</p>
      <div class="chosen-tile-body">
        <p style="font-size: 0.82em; line-height: 1.32;">Use if spec-first control is too high-friction.</p>
      </div>
    </div>
  </div>

  <div class="chosen-tile" style="border: 1px solid rgba(248, 113, 113, 0.35); background: rgba(127, 29, 29, 0.18); opacity: 0.9;">
    <div>
      <p class="chosen-tile-label">3 Spec Authoring UX (Enabler)</p>
      <div class="chosen-tile-body">
        <p style="font-size: 0.82em; line-height: 1.32;">Reduces authoring friction with templates, defaults, and persistent context.</p>
      </div>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin: 12px auto 0 auto; width: 95%; box-sizing: border-box; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Takeaway:</strong> We considered three directions. The core problem is trust in AI output, not generic productivity. Within that space, spec-driven control is the strongest initial wedge because it makes AI changes inspectable and constrained before review. Review &amp; Debug Assist remains the fallback if proactive control creates too much workflow friction.</p>
</div>

Notes:
This is an executive decision slide: two lead directions converge on one path (spec-driven control), with a clear fallback if pre-hoc control friction is too high.

---
<!-- .slide: id="target-niche" -->

## WHY: Target Niche <span class="metric-badge">A</span>

<div class="chosen-grid chosen-grid--2col chosen-grid--small" style="width: 90%; margin-left: auto; margin-right: auto;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Primary Niche: Early Adopters</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Who:</strong> Tech Leads &amp; Senior Engineers</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Where:</strong> Teams 10-50 devs, production JB IDE</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Problem:</strong> Unscoped AI diffs → review bottlenecks</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Trigger:</strong> 3+ review cycles on a single PR</p>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Scaling Niche (after POC)</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Who:</strong> Eng Managers, Directors, Security</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Where:</strong> 100+ dev orgs, compliance pressure</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Problem:</strong> No standard for AI governance</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Trigger:</strong> AI policy violation or incident</p>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 10px;">
  <p><strong>Takeaway:</strong> We start narrow — Tech Leads feeling AI review pain in JB IDEs — and expand to org-wide governance once value is proven.</p>
</div>

<ul class="distrust-notes" style="margin-top: 10px;">
  <li>Inputs so far: 1 exploratory interview, desk research, competitor pattern review. Systematic validation: Month 1.</li>
</ul>

Notes:
Our primary niche is Tech Leads and Senior Engineers working in teams of 10-50 developers who use JetBrains IDEs in production and already use AI code generation. Their specific pain: unscoped AI diffs cause review bottlenecks and unpredictable regressions. The trigger event is an AI-caused production incident or repeated review cycles on AI-generated PRs.
After proving value, we expand to the scaling niche: Engineering Managers, Directors, and Security leads who need org-wide AI governance standards.

---
<!-- .slide: id="why-competitor-landscape" -->

## WHY: Competitor Landscape

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); width: 95%; margin: 0 auto;">
  <div class="chosen-tile">
    <p class="chosen-tile-label" style="color: #10b981; line-height: 1.12;">
      <span style="display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.85;">Direct</span>
      <span style="display: block;">Spec-driven</span>
    </p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 2px; font-weight: 800; color: var(--text-main);"><strong>Tier 1: Direct Threats</strong></p>
      <p style="margin-bottom: 8px; font-size: 0.8em; color: rgba(255,255,255,0.7);"><a href="https://speckit.org/" target="_blank" style="color: var(--accent-blue);">Spec Kit</a>, <a href="https://kiro.dev/" target="_blank" style="color: var(--accent-blue);">Kiro</a>, <a href="https://docs.bmad-method.org/" target="_blank" style="color: var(--accent-blue);">BMAD</a>, <a href="https://codespeak.dev/" target="_blank" style="color: var(--accent-blue);">CodeSpeak</a>, <a href="https://openspec.dev/" target="_blank" style="color: var(--accent-blue);">OpenSpec</a></p>
      <p style="margin-bottom: 2px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-weight: 800; color: var(--text-main);"><strong>Tier 2: Watchlist</strong></p>
      <p style="margin-bottom: 8px; font-size: 0.8em; color: rgba(255,255,255,0.7);"><a href="https://www.task-master.dev/" target="_blank" style="color: var(--accent-blue);">Taskmaster</a>, <a href="https://stately.ai/" target="_blank" style="color: var(--accent-blue);">Stately</a>, <a href="https://buildermethods.com/agent-os" target="_blank" style="color: var(--accent-blue);">Agent-OS</a>, <a href="https://github.com/ariel-frischer/autospec" target="_blank" style="color: var(--accent-blue);">Autospec</a>, <a href="https://www.autok.dev/" target="_blank" style="color: var(--accent-blue);">autok</a> / <a href="https://www.devplan.com/" target="_blank" style="color: var(--accent-blue);">devplan</a></p>
      <p style="font-size: 0.85em; color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px;">&bull; Strength: explicit spec artifact and plan-first workflow<br>&bull; Gap: weak IDE-native control, limited change containment, early maturity</p>
    </div>
  </div>
  <div class="chosen-tile">
    <p class="chosen-tile-label" style="color: #4fc3f7; line-height: 1.12;">
      <span style="display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.85;">Indirect</span>
      <span style="display: block;">IDE Assistants</span>
    </p>
    <div class="chosen-tile-body">
      <p style="margin: 0 0 6px 0;">&nbsp;</p>
      <p style="margin-top: 0; margin-bottom: 5px;"><strong><a href="https://cursor.com/" target="_blank" style="color: var(--accent-blue);">Cursor</a>, <a href="https://github.com/features/copilot" target="_blank" style="color: var(--accent-blue);">Copilot</a>, <a href="https://www.jetbrains.com/ai-assistant/" target="_blank" style="color: var(--accent-blue);">JB AI</a></strong></p>
      <p style="font-size: 0.9em; color: var(--text-muted);">&bull; Strength: fast generation in the IDE<br>&bull; Gap: rules guide behavior but do not enforce persistent boundaries</p>
    </div>
  </div>
  <div class="chosen-tile">
    <p class="chosen-tile-label" style="color: #b388ff; line-height: 1.12;">
      <span style="display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.85;">Adjacent</span>
      <span style="display: block;">Post-facto &amp; Evals</span>
    </p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 2px; font-weight: 800; color: var(--text-main);"><strong>AI Code Reviewers</strong></p>
      <p style="margin-bottom: 8px; font-size: 0.8em; color: rgba(255,255,255,0.7);"><a href="https://coderabbit.ai/" target="_blank" style="color: var(--accent-blue);">CodeRabbit</a>, <a href="https://www.qodo.ai/" target="_blank" style="color: var(--accent-blue);">Qodo</a></p>
      <p style="margin-bottom: 2px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-weight: 800; color: var(--text-main);"><strong>Observability & Evals</strong></p>
      <p style="margin-bottom: 8px; font-size: 0.8em; color: rgba(255,255,255,0.7);"><a href="https://docs.langchain.com/langsmith/home" target="_blank" style="color: var(--accent-blue);">LangSmith</a>, <a href="https://www.datadoghq.com/product/llm-observability/" target="_blank" style="color: var(--accent-blue);">Datadog LLM</a></p>
      <p style="font-size: 0.85em; color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px;">&bull; Strength: catches issues after generation<br>&bull; Gap: improves detection, not prevention</p>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin: 12px auto 0 auto; width: 95%; box-sizing: border-box; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Takeaway:</strong> Competition is fragmented: spec tools own planning artifacts, IDE assistants own generation speed, and post-facto tools own detection. Our wedge is IDE-native pre-merge control via spec-linked change containment.</p>
</div>

---
<!-- .slide: id="learn-and-steal" -->

## WHY: Learn & Steal

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
  <p><strong>Takeaway:</strong> The market is converging on four useful patterns: Git-native specs, IDE-native workflow, persistent steering, and bi-directional sync. Our bet is to combine them into a control layer, not just a documentation layer.</p>
</div>

Notes:
Here we look at what's actually working in the market. First, Git-native markdown specs are the standard—tools like SpecKit prove developers won't adopt proprietary formats. Second, bi-directional sync: specs compile to code, code updates specs (like CodeSpeak), which stops doc rot. Third, surface area: web-first SaaS creates a context switch; successful workflows are IDE-native or CLI-native. Finally, persistent steering and slash-commands give us a natural UX that prevents AI amnesia.

---
<!-- .slide: id="competitive-approaches" -->

## WHY: Approaches

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 14px;">Prioritized approaches across <a href="#/roadmap-main-appendix" style="color: var(--accent-blue);">observed solutions</a>.</p>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 10px; align-items: stretch; margin-top: 2px; width: 95%; margin-left: auto; margin-right: auto;">
  <div class="chosen-tile chosen-tile--green" style="display: flex; flex-direction: column; justify-content: space-between; min-height: 190px;">
    <div>
      <p class="chosen-tile-label">1 SPEC-DRIVEN CONTROL</p>
      <p class="chosen-tile-body">Prevents ambiguity before generation.<br>Turns intent into persistent, reviewable constraints.</p>
    </div>
    <p style="margin-top: 10px;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #6ee7b7; border: 1px solid rgba(110, 231, 183, 0.45); background: rgba(16, 185, 129, 0.15);">Primary bet</span></p>
  </div>

  <div class="chosen-tile" style="display: flex; flex-direction: column; justify-content: space-between; min-height: 190px; border: 1px solid rgba(96, 165, 250, 0.42); background: rgba(37, 99, 235, 0.12);">
    <div>
      <p class="chosen-tile-label">2 OBSERVABILITY &amp; EVALS</p>
      <p class="chosen-tile-body">Detects drift, regressions, and failures after execution.<br>Best for validation, not primary control.</p>
    </div>
    <p style="margin-top: 10px;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #93c5fd; border: 1px solid rgba(147, 197, 253, 0.45); background: rgba(59, 130, 246, 0.14);">Complementary</span></p>
  </div>

  <div class="chosen-tile" style="display: flex; flex-direction: column; justify-content: space-between; min-height: 190px; border: 1px solid rgba(248, 113, 113, 0.35); background: rgba(127, 29, 29, 0.18); opacity: 0.9;">
    <div>
      <p class="chosen-tile-label">3 REVIEW &amp; DEBUG ASSIST</p>
      <p class="chosen-tile-body">Reduce manual review effort post-generation.<br>Useful as a fallback if spec authoring friction is too high.</p>
    </div>
    <p style="margin-top: 10px;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #fca5a5; border: 1px solid rgba(252, 165, 165, 0.45); background: rgba(127, 29, 29, 0.25);">Fallback</span></p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin: 12px auto 0 auto; width: 95%; box-sizing: border-box; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Decision:</strong> Start with spec-driven control as the initial wedge for JetBrains teams.<br><strong>Why:</strong> Review pain starts before merge, when change scope is unclear. Spec-driven control constrains the diff before generation; observability helps validate drift later.<br><strong>Implication:</strong> Use specs as the primary control plane, and use observability as a validation layer, not the entry wedge.<br><strong>Fallback:</strong> If authoring specs proves too heavy, start from diff containment / review assist and evolve toward spec-first.</p>
</div>

Notes:
Both Spec-driven development and Observability + Evals score 6.7 in ICE, but the tie-break comes from intervention point in the SDLC. For JetBrains teams, trust is won at review time, so pre-review constraint is a better first bet than post-facto detection.

---
<!-- .slide: id="why-specs-not-just-models" -->

## WHY: Why Specs, Not Just Better Models

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(2, 1fr); gap: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Better Models Are Not Boundaries</p>
    <p class="chosen-tile-body">Better models can reduce mistakes, but they do not create enforceable boundaries. The missing layer is workflow control, not just model quality.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Specs As Control Plane</p>
    <p class="chosen-tile-body">Specs create persistent intent, scope boundaries, and approval points that survive beyond a chat session.</p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Takeaway:</strong> The primary problem is not smarter generation, but governed change.</p>
</div>


---
<!-- .slide: id="why-summary-v2" -->

## WHY: Summary

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(2, 1fr); gap: 8px; margin-top: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Decision Summary</p>
    <p class="chosen-tile-body">AI adoption hit 90% but distrust surged +15pp YoY (46% in 2025). Start with Tech Leads in 10-50 dev teams using JetBrains IDEs, and solve blind review rework via spec-linked change containment while preserving high-signal review quality.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Market Size <span class="metric-badge">A</span></p>
    <p class="chosen-tile-body">While the <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=856599423#gid=856599423&range=A1" target="_blank" style="color: var(--accent-blue); text-decoration: none;">$171.85M top-down SOM</a> targets a 5% share of the $4.91B market, the <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=A1" target="_blank" style="color: var(--accent-blue); text-decoration: none;">$0.93M bottom-up Year 1</a> exit run-rate <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=C29" target="_blank" style="color: var(--accent-blue); text-decoration: none;">(~0.54% SOM)</a> reflects early funnel ramp-up versus a mature steady-state.</p>
  </div>
</div>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Differentiation</p>
    <p class="chosen-tile-body">IDE-native bi-directional spec↔code via PSI: extract intent, constrain the diff, detect drift early. <a href="#/differentiation">Differentiation</a></p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Monetization</p>
    <p class="chosen-tile-body">Free entry comes through JetBrains distribution and an OSS trust layer. Paid value starts when teams need shared controls, visibility, and PR/CI workflow integration. <a href="#/pricing-monetization">Monetization</a></p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Growth Loops</p>
    <p class="chosen-tile-body">Repo-native specs, reviewer reuse, CI gates, and ecosystem distribution reinforce team adoption over time. <a href="#/growth-loops">Growth Loops</a></p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> We are building a workflow moat (governed change vs unvetted generation) within JetBrains, monetizing team-level predictability rather than individual productivity.</p>
</div>

Notes:
This version is intentionally decision-first: market context plus three operating levers (differentiation, monetization, growth loops).

---
<!-- .slide: id="golden-path" -->

## HOW: Golden Path (Before vs. After)

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 12px;">Same workflow, different control point.</p>

<div class="chosen-grid chosen-grid--2col chosen-grid--small" style="grid-template-columns: 1fr 1fr; gap: 15px; align-items: stretch;">
  
  <div class="chosen-tile" style="display: flex; flex-direction: column; justify-content: space-between; border: 1px solid rgba(248, 113, 113, 0.35); background: rgba(127, 29, 29, 0.18);">
    <div>
      <p class="chosen-tile-label" style="color: #fca5a5;">BEFORE: 45-min bottleneck</p>
      <div class="chosen-tile-body">
        <ol style="margin: 0; padding-left: 16px;">
          <li style="margin-bottom: 6px;"><strong>Trigger:</strong> Junior prompts AI to refactor auth module.</li>
          <li style="margin-bottom: 6px;"><strong>AI generates:</strong> 400-line unscoped diff, no contract.</li>
          <li style="margin-bottom: 6px;"><strong>Review:</strong> Line-by-line blind review — can't tell what changed vs. what's new.</li>
          <li><strong>Outcome:</strong> 45 min wasted, "Request Changes", re-prompt cycle.</li>
        </ol>
      </div>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green" style="display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <p class="chosen-tile-label" style="color: #6ee7b7;">AFTER (Bonsai): 7-min guided flow</p>
      <div class="chosen-tile-body">
        <ol style="margin: 0; padding-left: 16px;">
          <li style="margin-bottom: 6px;"><strong>1. Author:</strong> Junior writes a spec: "extract session-expiry logic".</li>
          <li style="margin-bottom: 6px;"><strong>2. Generate:</strong> AI creates scoped diffs, strictly contained to contract.</li>
          <li style="margin-bottom: 6px;"><strong>3. Review:</strong> Reviewer checks "diff vs spec" in IDE (hard stop on violations).</li>
          <li><strong>4. Commit:</strong> 7 min to merge, persistent traceability stays in Git.</li>
        </ol>
      </div>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 15px;">
  <p><strong>Result:</strong> Same task, same people — but the control point shifts from "review the output" to "verify against the contract".</p>
</div>

Notes:
This slide shows the same workflow (junior refactors auth module using AI) from two perspectives. Without Bonsai, the reviewer gets a blind 400-line diff with no contract. With Bonsai, the spec exists first, and the review becomes a simple question: "Does this diff fulfill the spec?" The time drops from 45 minutes to 7, and the spec persists in the repo for future AI sessions.

---
<!-- .slide: id="roadmap" -->

## HOW: Roadmap

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(4, 1fr); gap: 8px; align-items: stretch;">
  <div class="chosen-tile chosen-tile--green" style="min-height: 182px; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <p class="chosen-tile-label">Month 1</p>
      <p style="margin: 0 0 6px 0; font-weight: 700; color: #a7f3d0;">Phase: Trust</p>
      <p class="chosen-tile-body" style="margin: 0;">Validate core trust in the workflow.</p>
    </div>
    <p style="margin: 10px 0 0 0;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #6ee7b7; border: 1px solid rgba(110, 231, 183, 0.45); background: rgba(16, 185, 129, 0.15);">Gate: 3 PoCs + repeat usage signal</span></p>
  </div>
  <div class="chosen-tile" style="min-height: 182px; display: flex; flex-direction: column; justify-content: space-between; border: 1px solid rgba(45, 212, 191, 0.55); background: rgba(20, 184, 166, 0.16); box-shadow: 0 0 0 1px rgba(45, 212, 191, 0.25) inset;">
    <div>
      <p class="chosen-tile-label">Month 2</p>
      <p style="margin: 0 0 6px 0; font-weight: 700; color: #99f6e4;">Phase: Paid Intent</p>
      <p class="chosen-tile-body" style="margin: 0;">Confirm budgeted demand before MVP.</p>
    </div>
    <p style="margin: 10px 0 0 0;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #99f6e4; border: 1px solid rgba(153, 246, 228, 0.5); background: rgba(13, 148, 136, 0.2);">Gate: 3 payment-intent commitments</span></p>
  </div>
  <div class="chosen-tile" style="min-height: 182px; display: flex; flex-direction: column; justify-content: space-between; border: 1px solid rgba(148, 163, 184, 0.35); background: rgba(51, 65, 85, 0.22);">
    <div>
      <p class="chosen-tile-label">Months 3-4</p>
      <p style="margin: 0 0 6px 0; font-weight: 700; color: #cbd5e1;">Phase: MVP Launch</p>
      <p class="chosen-tile-body" style="margin: 0;">Run a narrow MVP with paid pilots.</p>
    </div>
    <p style="margin: 10px 0 0 0;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.45); background: rgba(71, 85, 105, 0.25);">Gate: &ge;3 paid pilots + outcome signal</span></p>
  </div>
  <div class="chosen-tile" style="min-height: 182px; display: flex; flex-direction: column; justify-content: space-between; border: 1px dashed rgba(148, 163, 184, 0.4); background: rgba(30, 41, 59, 0.2); opacity: 0.9;">
    <div>
      <p class="chosen-tile-label">Months 5-6</p>
      <p style="margin: 0 0 6px 0; font-weight: 700; color: #cbd5e1;">Phase: Standardization</p>
      <p class="chosen-tile-body" style="margin: 0;">Standardize the governed-change workflow for JetBrains teams and partner organizations.</p>
    </div>
    <p style="margin: 10px 0 0 0;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.45); background: rgba(51, 65, 85, 0.22);">Gate: repeat usage + stable unit signal</span></p>
  </div>
</div>

<p style="margin-top: 6px; font-size: 0.55em; color: rgba(148, 163, 184, 0.85);">Detailed month-by-month actions, metrics, and gates moved to <a href="#/roadmap-main-appendix" style="color: var(--accent-blue);">appendix</a>.</p>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> Execution is evidence-gated: trust signal (Mo1) -> budget intent (Mo2) -> paid pilot outcomes (Mo3-4) -> scale only with stable usage and unit economics (Mo5-6).</p>
</div>

Notes:
Roadmap is shown as a gated de-risking path, not a calendar-only plan: trust signal -> paid intent -> paid pilot proof -> conditional launch.

---

<!-- .slide: id="mvp-definition" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: MVP</h2>
<p class="slide-subtitle" style="margin-bottom: 8px;">Product Definition (Phase 3, Mo 3-4)</p>

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">What It Is</p>
    <p class="chosen-tile-body">JetBrains IDE plugin that turns a spec (repo-native Markdown) into controlled code changes, with in-IDE review and traceability, so teams ship faster without unscoped diffs.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Success Criteria <span class="metric-badge">A</span></p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Token spend per successful PR-ready outcome &darr; 10%</li>
        <li>% PRs where CI checks pass on 1st try &uarr; 10%</li>
        <li>Median time to PR-ready (from spec approved) &darr; 10-20%</li>
        <li>Target range: 10-20% fewer unscoped diffs / rework signals</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Who It Is For (MVP users)</p>
    <p class="chosen-tile-body">A small set of design partner teams on real JetBrains IDE repos (single repo each), where scoped changes are common and review cycles are costly.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Core User Flow</p>
    <div class="chosen-tile-body">
      <ol style="margin: 0; padding-left: 16px;">
        <li>Define a spec for a scoped change (Markdown in the repo).</li>
        <li>Run spec-aware workflow in IDE to generate plan + scoped diffs (change containment).</li>
        <li>Review and approve/apply changes in IDE (hard stop on scope violations).</li>
        <li>Produce PR-ready changeset with traceability (spec ↔ diff ↔ commits).</li>
      </ol>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Core Capabilities (MVP)</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Spec-aware workflow (not a Markdown editor): run/validate/apply from spec in IDE.</li>
        <li>Change containment: hard scope boundaries + stop/ask on violations.</li>
        <li>In-IDE diff review with approve/apply loop.</li>
        <li>Traceability: links spec to diffs/commits + PR-ready summary.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Not In MVP</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Full Code → Spec automation (validated via existing tools first).</li>
        <li>Broad language/framework coverage and edge cases.</li>
        <li>Full org governance (roles, audit, policy management at scale).</li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Decision:</strong> MVP is one governed change flow in JetBrains IDEs, optimized for measurable outcome lift (time-to-PR, first-pass CI, token efficiency), not broad feature coverage.</p>
</div>

Notes:
MVP scope is intentionally narrow: one real workflow on partner repos with strict containment and clear traceability.
Success criteria are repeat weekly usage, low-noise operation, and measurable review-cycle improvement before broader rollout.

---
<!-- .slide: id="mvp-definition-simplified" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: MVP (Simplified Version)</h2>
<p class="slide-subtitle" style="margin-bottom: 8px;">Product Definition (Phase 3, Mo 3-4)</p>

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">What It Is</p>
    <p class="chosen-tile-body">JetBrains IDE plugin that turns a spec (repo-native Markdown) into controlled code changes, with in-IDE review and traceability, so teams ship faster without unscoped diffs.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Who It Is For (MVP users)</p>
    <p class="chosen-tile-body">A small set of design partner teams on real JetBrains IDE repos, where scoped changes are common and review cycles are costly.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Core Capabilities (MVP)</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Spec-aware workflow (not a Markdown editor): run/validate/apply from spec in IDE.</li>
        <li>Change containment: hard scope boundaries + stop/ask on violations.</li>
        <li>In-IDE diff review with approve/apply loop.</li>
        <li>Traceability: links spec to diffs/commits + PR-ready summary.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Not In MVP</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Full Code → Spec automation (validated via existing tools first).</li>
        <li>Broad language/framework coverage and edge cases.</li>
        <li>Full org governance (roles, audit, policy management at scale).</li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Decision:</strong> MVP is one governed change flow in JetBrains IDEs, optimized for measurable outcome lift, not broad feature coverage.</p>
</div>

Notes:
MVP scope is intentionally narrow: one real workflow on partner repos with strict containment and clear traceability.

---
<!-- .slide: id="pricing-monetization" -->

## HOW: Monetization <span class="metric-badge">A</span>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px; text-align: left;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">What is free vs paid</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li><strong>OSS:</strong> spec format, validator, examples.</li>
        <li><strong>Free plugin:</strong> single-user, small-scope workflow.</li>
        <li><strong>Paid team:</strong> templates, controls, visibility, PR/CI integrations, change containment.</li>
      </ul>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">When we start charging</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li><strong>Mo 2:</strong> written budget intent + pilot terms.</li>
        <li><strong>Mo 3-4:</strong> paid pilots after plugin MVP.</li>
        <li><strong>Mo 5-6:</strong> repeatable upgrades via JetBrains ecosystem.</li>
      </ul>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Signals the model works</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Budget intent converts to paid pilot.</li>
        <li>One team expands inside the org.</li>
        <li>Weekly repeat usage of the core scenario.</li>
      </ul>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Decision:</strong> Keep individual entry free, monetize team-level control (shared templates, governance visibility, PR/CI integration), and start charging at paid pilot stage once MVP value is proven.</p>
</div>

Notes:
This version keeps monetization logic as three decisions: free vs paid, when charging starts, and how we know it works.


---
<!-- .slide: id="metrics" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: Key Metrics</h2>

<div class="chosen-grid chosen-grid--2col chosen-grid--small" style="text-align: left;">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">1. NSM & Engagement</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>NSM:</b> Active users/wk with ≥1 spec-linked merge</li>
        <li><b>Engagement:</b> Activation to 1st merge, N-day retention, WAU/MAU</li>
        <li><b>Expansion:</b> % org with X+ users with ≥1 spec-merge</li>
        <li><b>Velocity:</b> Lead time & deployment frequency</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">2. Monetization</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>New MRR:</b> Activation to paid, ARPU, Churn (IC/seats)</li>
        <li><b>Attributed JB MRR:</b> Attach rate (JB paid with product), Cohort ARPU & Churn</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">3. Guardrails & Basic Quality</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>Safety:</b> CR to core JB actions, Sec/privacy incidents</li>
        <li><b>Quality:</b> False positive rate, added latency/Time to PR</li>
        <li><b>Drift:</b> Drift rate & severity, prevented incidents</li>
        <li><b>Qualitative:</b> CSAT & User Interviews on Spec View</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">4. Value & Outcomes</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>Cost:</b> Token spend per successful PR-ready outcome</li>
        <li><b>Quality:</b> % PRs passing checks on 1st try</li>
        <li><b>Scope Control:</b> Unscoped diff / scope-violation rate</li>
        <li><b>Velocity:</b> Median time to PR-ready (from spec approved)</li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> Metrics are tied to roadmap gates: Mo1 repeat usage in PoCs, Mo2 payment-intent commitments, Mo3-4 paid-pilot outcome uplift (time-to-PR, first-pass CI, token efficiency), Mo5-6 stable usage and unit economics.</p>
</div>

Notes:

1) **North Star**: Focus is on habitual usage (spec-linked merges), tracking both individual users and orgs.
2) **Monetization**: Tracking New MRR for the product, and rigorously attributing JB Core revenue via matched cohort uplifts.
3) **Safety & Quality**: Tracking latency and false positives alongside qualitative CSAT to ensure we don't harm the IDE experience.
4) **Value**: Proving cost efficiency and improved PR throughput (passing checks on 1st try).

<!-- .slide: id="risks-mitigation" -->

## HOW: Risks & Mitigation

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 10px;">Top risks below. Full Impact × Probability matrix is in <a href="#/risks-mitigation-main-appendix" style="color: var(--accent-blue);">appendix</a>.</p>

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%; font-size: 0.43em;">
  <colgroup>
    <col style="width: 18%;">
    <col style="width: 37%;">
    <col style="width: 37%;">
    <col style="width: 8%;">
  </colgroup>
  <thead>
    <tr>
      <th>Risk</th>
      <th>Why It Matters</th>
      <th>Mitigation</th>
      <th class="center">Priority</th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>PoC value</strong></td>
      <td>Spec-first may not prove repeatable value fast enough. If Month 1 lacks repeat usage and better outcomes, the thesis weakens.</td>
      <td>Run 3 parallel PoCs, require repeat-usage gate, and switch entry point if outcomes do not outperform alternatives.</td>
      <td class="center score val-high">High</td>
    </tr>
    <tr>
      <td><strong>Partner speed</strong></td>
      <td>Not enough high-signal design partners fast enough.</td>
      <td>Warm network + OSS wedge.</td>
      <td class="center score val-med">Med</td>
    </tr>
    <tr>
      <td><strong>PSI complexity</strong></td>
      <td>Integration complexity can slow delivery.</td>
      <td>Kotlin-first, native PSI APIs.</td>
      <td class="center score val-med">Med</td>
    </tr>
    <tr>
      <td><strong>Dev friction</strong></td>
      <td>Adoption may feel too heavy for real workflows.</td>
      <td>Repo-native, zero-friction extraction.</td>
      <td class="center score val-med">Med</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> The primary risk is failing to prove repeatable value for spec-first control in Month 1. Mitigation is explicit: 3 parallel PoCs with a hard pivot gate before MVP build.</p>
</div>


---

<!-- .slide: id="gtm" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: GTM Strategy <span class="metric-badge">A</span></h2>

<div class="chosen-grid chosen-grid--2col chosen-grid--small" style="text-align: left;">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">1. PoC & Early Adopters</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><strong>Target:</strong> JB Power Users, Tech Leads, DevEx.</li>
        <li><strong>Motion:</strong> "Golden path" to PR in 10 mins. <a href="#/golden-path">Details</a></li>
        <li><strong>Goal:</strong> Validate spec-first + diff control (change containment) via instrumented prototype before plugin MVP.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">2. Early Monetization</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><strong>Offer:</strong> Written budget intent + pilot agreement (scope, success metrics, buyer, procurement path).</li>
        <li><strong>When we charge:</strong> paid pilots start once plugin MVP exists (Mo 3-4).</li>
        <li><strong>Model:</strong> Add-on to JB AI credits (shared quota).</li>
        <li><strong>Goal:</strong> Prove WTP and secure team budget early.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">3. Scale Sales</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><strong>Distribution:</strong> JB IDE Promo, Toolbox, Marketplace.</li>
        <li><strong>Motion:</strong> PLG loop (Indiv. &rarr; Team org policy).</li>
        <li><strong>Goal:</strong> Zero-friction install to paid conversion.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">4. Market Standard</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><span class="metric-badge">A</span> <strong>OSS (risk mitigation first):</strong> Spec Format + validator + examples to widen partner funnel and reduce distrust; later OSS adds templates/hooks starter pack and compatibility assets.</li>
        <li><strong>Ecosystem:</strong> Marketplace for hooks and templates.</li>
        <li><strong>Enterprise:</strong> Hosted orchestration and governance.</li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> GTM sequencing is deliberate: prove workflow value, secure budget intent, convert to paid pilots, then scale through JetBrains distribution and OSS standardization.</p>
</div>

Notes:

1) **PoC**: We don't need a perfect product, we need a "golden path" that demonstrates value in 10 minutes.
2) **Monetization**: Early monetization starts as budget intent and pilot agreements. Charging starts when plugin MVP is usable.
3) **Scale**: The JetBrains ecosystem is our unfair advantage. One-click install via Toolbox/Marketplace.
4) **Standard**: We open-source the Spec Format and CLI to become the protocol, while monetizing the orchestration and governance.

---

<!-- .slide: id="month1-actions" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">My 1st month actions</h2>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 10px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Week 1</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong>Internal Ramp</strong></p>
      <p>Align stakes. Review past launches.</p>
    </div>
  </div>
  <div class="chosen-tile">
    <p class="chosen-tile-label">Weeks 2-3</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong>Validation</strong></p>
      <p>15 interviews. Pilot outreach [A].</p>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Week 4</p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong>Go / No-Go</strong></p>
      <p>Hard gate on commitments [A].</p>
    </div>
  </div>
</div>

Notes:
Detailed Action Plan:
Week 1: Meet stakeholders, align on success definition, burn-down assumptions (PSI signal, demand).
Weeks 2-3: Option A (Primary): 8+ discovery interviews, scheduling design partners. Option B: Fake door/Marketplace listing.
Week 4: Gate: Pilot commitments >=3, Top-3 problem rank for 5/8 devs, ICP waitlist >=15.
End Mo 1 Deliverable: Initial qualitative signal, updated roadmap, and MVP scope.
Tracking logs maintained in the validation dashboard.

---

<!-- .slide: id="appendix" -->

# Appendix

---
<!-- .slide: id="differentiation" -->

## WHY: Differentiation

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 80%;">
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
      <td><span class="metric-badge">A</span> PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade structural parsing substantially reduces hallucination risk on structure-sensitive tasks. Not a permanent moat — a 12–18 month head start we convert into data and workflow lock-in.</td>
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

<ul class="distrust-notes">
  <li>Note: PSI isn’t exclusive; defensibility compounds via accumulated spec data + workflow lock-in.</li>
</ul>

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
<!-- .slide: id="growth-loops" -->

## WHY: Growth Loops <span class="metric-badge">A</span>

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

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> Growth compounds when spec-linked review becomes default team behavior: reviewer reuse, cross-repo template reuse, and ecosystem compatibility turn local adoption into org-wide standards.</p>
</div>

Notes:
Here we detail the 4 main B2B growth mechanics that drive viral product-led expansion across an enterprise.

1) Repo-native: Viral spread inside a single team via PR checks. This forces adoption simply by interacting with code.
2) Collaboration: Bringing non-coding stakeholders (architects, security) into the review process using readable contracts.
3) Org-wide Expansion: A single spec scales across multiple projects, accelerating adoption as its value grows with every added repository.
4) Ecosystem Agnosticism: Being an open format means it can be adopted without massive migration or forcing developers out of their favorite IDE.

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
<td>45.7% distrust AI (up 15.3 pp YoY). 75% would ask a person for help when they don’t trust AI answers. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center score val-high">9.0</td>
</tr>
<tr class="highlight-row">
<td>Increased review and debugging time</td>
<td>45% say debugging AI code is more time-consuming. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center score val-high">9.0</td>
</tr>
<tr>
<td>Concerns regarding security and vulnerabilities</td>
<td>&gt;60% frequently have ethical / security-related concerns about AI-generated code. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center val-high">High</td>
<td class="center val-high">High</td>
<td class="center val-med">Med</td>
<td class="center score val-high">6.8</td>
</tr>
<tr>
<td>AI decision-making opacity and ambiguous accountability for errors</td>
<td>75% would ask a person for help when they don’t trust AI answers, keeping humans as final arbiters of correctness. <a href="https://arxiv.org/html/2502.18468v1" target="_blank">[1]</a> <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[2]</a></td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center score val-med">3.0</td>
</tr>
<tr>
<td>Risk of engineering skill degradation</td>
<td>60% believe AI tools lead to less skilled developers (web-dev firstly). <a href="https://2025.stateofdevs.com/en-US/" target="_blank">[1]</a></td>
<td class="center val-med">Med</td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center score val-low">2.0</td>
</tr>
<tr>
<td>Fear of data leaks and privacy concerns</td>
<td>40% of security incidents involve AI (incident-level). &gt;80% report concerns about data security and privacy. Frequency=Low because measured via incidents. <a href="https://www.microsoft.com/en-us/security/blog/2024/11/13/microsoft-data-security-index-annual-report-highlights-evolving-generative-ai-security-needs/" target="_blank">[1]</a> <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[2]</a></td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center val-med">Med</td>
<td class="center score val-low">1.5</td>
</tr>
<tr>
<td>Legal uncertainty regarding copyrights and licensing for AI-generated code</td>
<td>Survey of 574 GenAI users: broad disagreement and uncertainty about output ownership and copyright risk. <a href="https://arxiv.org/html/2502.18468v1" target="_blank">[1]</a> <a href="https://arxiv.org/html/2411.10877v1" target="_blank">[2]</a></td>
<td class="center val-med">Med</td>
<td class="center val-low">Low</td>
<td class="center val-med">Med</td>
<td class="center score val-low">1.5</td>
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
<td class="center">11.5%</td>
<td class="center">3.1%</td>
<td class="center score">8.4%</td>
<td class="center val-med">Med</td>
<td>Opportunity to improve on the planning step</td>
</tr>
<tr class="highlight-row">
<td>Communication</td>
<td class="center">12.9%</td>
<td class="center">6.6%</td>
<td class="center score">6.4%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>Debugging</td>
<td class="center">11.2%</td>
<td class="center">7.5%</td>
<td class="center score">3.7%</td>
<td class="center val-high">High</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Customer Support</td>
<td class="center">7.5%</td>
<td class="center">4.0%</td>
<td class="center score">3.5%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>Env Setup</td>
<td class="center">3.8%</td>
<td class="center">1.5%</td>
<td class="center score">2.2%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Monitoring/Dashboard</td>
<td class="center">2.9%</td>
<td class="center">2.2%</td>
<td class="center score">0.7%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Task Mgmt (ADO)</td>
<td class="center">2.0%</td>
<td class="center">1.3%</td>
<td class="center score">0.7%</td>
<td class="center val-med">Med</td>
<td>Opportunity to automate via agent orchestration</td>
</tr>
<tr>
<td>Code Refactoring</td>
<td class="center">5.2%</td>
<td class="center">4.8%</td>
<td class="center score">0.5%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Test Authoring</td>
<td class="center">4.8%</td>
<td class="center">5.2%</td>
<td class="center score">-0.3%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Documentation</td>
<td class="center">3.7%</td>
<td class="center">4.3%</td>
<td class="center score">-0.6%</td>
<td class="center val-med">Med</td>
<td>Automation already widely adopted</td>
</tr>
<tr>
<td>Mentoring/Onboarding</td>
<td class="center">2.6%</td>
<td class="center">3.7%</td>
<td class="center score">-1.1%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Tech Presentations</td>
<td class="center">0.6%</td>
<td class="center">1.7%</td>
<td class="center score">-1.1%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>PR/Code Review</td>
<td class="center">5.9%</td>
<td class="center">7.1%</td>
<td class="center score">-1.2%</td>
<td class="center val-low">Low</td>
<td>Human in the loop issue mostly depends on AI models base quality evolution</td>
</tr>
<tr>
<td>Learning New Tech</td>
<td class="center">2.5%</td>
<td class="center">6.6%</td>
<td class="center score">-4.0%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>System Arch/Design</td>
<td class="center">8.9%</td>
<td class="center">15.4%</td>
<td class="center score">-6.5%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
<tr class="highlight-row">
<td>Coding</td>
<td class="center">13.9%</td>
<td class="center">25.2%</td>
<td class="center score">-11.2%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> We cut low-value rework and unscoped review churn, then reinvest saved capacity into Coding and System Architecture without reducing high-signal code review quality.</p>
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
<td class="center val-high">3</td>
<td class="center val-med">2</td>
<td class="center val-med">0.75</td>
<td class="center score val-high">4.5</td>
</tr>
<tr class="highlight-row">
<td>Quality and reliability risk from software errors</td>
<td>Poor software quality costs US companies $2.08 trillion annually. <a href="https://raygun.com/blog/cost-of-software-errors/" target="_blank">[1]</a></td>
<td class="center val-high">3</td>
<td class="center val-high">3</td>
<td class="center val-low">0.5</td>
<td class="center score val-high">4.5</td>
</tr>
<tr>
<td>Documentation debt harming onboarding, satisfaction and speed</td>
<td>41% of developers report this as a major hindrance. 97% lose significant time to inefficiencies. <a href="https://www.atlassian.com/software/compass/resources/state-of-developer-2024" target="_blank">[1]</a></td>
<td class="center val-med">2</td>
<td class="center val-med">2</td>
<td class="center val-med">0.75</td>
<td class="center score val-med">3.0</td>
</tr>
<tr>
<td>Token Spent Optimization</td>
<td>On average, token consumption decreased by 15–20%. <a href="https://arxiv.org/html/2504.15989v2" target="_blank">[1]</a></td>
<td class="center val-med">2</td>
<td class="center val-med">2</td>
<td class="center val-med">0.75</td>
<td class="center score val-med">3.0</td>
</tr>
<tr>
<td>Developer burnout from cognitive load and on-call burden</td>
<td>83% of software engineers report feelings of burnout. <a href="https://www.softwareseni.com/developer-burnout-and-cognitive-load-in-the-devops-era/" target="_blank">[1]</a></td>
<td class="center val-med">2</td>
<td class="center val-med">2</td>
<td class="center val-low">0.5</td>
<td class="center score val-low">2.0</td>
</tr>
<tr>
<td>Productivity loss from technical debt waste</td>
<td>Developers waste on average 23% of their time due to technical debt. <a href="https://research.chalmers.se/publication/511450/file/511450_Fulltext.pdf" target="_blank">[1]</a></td>
<td class="center val-low">1</td>
<td class="center val-high">3</td>
<td class="center val-low">0.5</td>
<td class="center score val-low">1.5</td>
</tr>
<tr>
<td>Compliance overhead from AI and tooling</td>
<td>Compliance overhead increases 10–20% in regulated industries due to AI audit and privacy controls. <a href="https://www.softwareseni.com/the-real-economics-of-ai-coding-beyond-vendor-productivity-claims/" target="_blank">[1]</a></td>
<td class="center val-med">2</td>
<td class="center val-low">1</td>
<td class="center val-med">0.75</td>
<td class="center score val-low">1.5</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> The two highest-scoring B2B pains — delivery unpredictability and quality risk — are strongly aligned with control gaps in AI-assisted workflows; uncontrolled AI diffs are a likely accelerator, making change containment a high-leverage first wedge.</p>
</div>

<ul class="distrust-notes">
<li>Reach, Freq. (Frequency), Conf. (Confidence = probability to make a difference) and Score are subjectively estimated based on external report signals.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

Notes:
This slide zooms out from the developer to the business buyer. B2B buyers care about delivery predictability and software quality — both of which are threatened by unvetted AI output. The top two pains score equally at 4.5, driven by high reach across engineering orgs and strong argumentation from industry data. Compliance overhead is real but lower frequency, making it a secondary concern for the initial wedge.

---
<!-- .slide: id="stream-options-main-appendix" -->

## WHAT: Strategic Directions: detailed

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
      <td><strong>Spec-driven control (AI-dev transparency):</strong> code &amp; architecture</td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>6.7</td>
    </tr>
    <tr>
      <td><strong>Review &amp; Debug assist</strong></td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>4.4</td>
    </tr>
    <tr>
      <td><strong>Spec Authoring UX</strong> (enabler)</td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>2.2</td>
    </tr>
    <tr>
      <td><strong>Quality &amp; reliability risk</strong> from software errors</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>2.2</td>
    </tr>
    <tr>
      <td><strong>Security &amp; Compliance</strong> (proactive assist)</td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>1.5</td>
    </tr>
    <tr>
      <td><strong>Dev Env Simplification</strong></td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>1.5</td>
    </tr>
    <tr>
      <td><strong>Delivery time variability</strong> (accurate forecasting)</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>1.5</td>
    </tr>
    <tr>
      <td><strong>Token Spent Optimization</strong></td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> Spec-driven control (AI-dev transparency) is the top-priority direction. Key risk: spec fatigue and enforcement resistance. Runner-up (Review &amp; Debug assist) becomes our fallback if ICP interviews disprove pre-hoc control preference.</p>
</div>

<ul class="distrust-notes">
<li>Scores are derived from the <a href="#/competitive-approaches-main-appendix">Core JTBD Landscape ICE framework</a>. Each direction is mapped to the closest approach and inherits its ICE Score. <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=1907182755#gid=1907182755&range=A1" target="_blank">Calculations</a>.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
<li>Directions are derived from the top issues across three evidence layers: <a href="#/distrust-issues">Distrust</a>, <a href="#/time-spend">Time Spent</a>, and <a href="#/b2b-pains">B2B Issues</a>.</li>
</ul>

Notes:
Direction scores inherit ICE scores from the Core JTBD Landscape framework (see Approaches appendix for methodology: Score = weighted-average Impact × Confidence ÷ Effort, where Impact is a weighted average across 9 criteria).
All scores are assumptions marked with A — to be validated through user interviews and early pilots.

Key risks of chosen direction (AI-dev transparency): spec fatigue — developers approve without reading; enforcement resistance — teams reject mandatory gates. Both are tested in Phase 1 experiments.

What would change our mind on runner-ups:
• Review & Debug assist (4.4): if ICP interviews reveal developers prefer post-hoc review over pre-hoc control, we pivot to this direction — it shares the same trust JTBD but inverts the intervention point.
• Security & Compliance (1.5): if enterprise pilots show compliance gates drive faster budget approval than architecture governance, we re-scope the wedge.

Next: we define the chosen direction in detail with JTBD and early adopter segments.

---
<!-- .slide: id="competitive-approaches-main-appendix" -->

## WHY: Approaches

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%; font-size: 0.42em;">
  <colgroup>
    <col style="width: 22%;">
    <col style="width: 36%;">
    <col style="width: 32%;">
    <col style="width: 10%;">
  </colgroup>
  <thead>
    <tr>
      <th>Approach</th>
      <th>Description</th>
      <th>Key Players</th>
      <th class="center">ICE Score <span class="metric-badge">A</span></th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>Spec-driven development</strong></td>
      <td>Spec-first: AI generates code &amp; checks from contracts. Spec becomes a reviewable, regression artifact.</td>
      <td><a href="https://kiro.dev/" target="_blank">Kiro</a>, <a href="https://speckit.org/" target="_blank">Spec Kit</a>, <a href="https://codespeak.dev/" target="_blank">CodeSpeak</a>, <a href="https://www.task-master.dev/" target="_blank">Taskmaster</a>, <a href="https://docs.bmad-method.org/" target="_blank">BMAD</a></td>
      <td class="center score">6.7</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>Observability + evals</strong></td>
      <td>Trace inputs/outputs &amp; agent steps; measure quality via datasets &amp; LLM-as-judge. Catch degradations pre-release.</td>
      <td><a href="https://docs.langchain.com/langsmith/home" target="_blank">LangSmith</a>, <a href="https://docs.wandb.ai/weave" target="_blank">W&amp;B Weave</a>, <a href="https://www.datadoghq.com/product/llm-observability/" target="_blank">Datadog LLM</a>, <a href="https://galileo.ai/" target="_blank">Galileo</a>, <a href="https://docs.ragas.io/" target="_blank">Ragas</a>, <a href="https://github.com/truera/trulens" target="_blank">TruLens</a>, <a href="https://www.braintrust.dev/docs" target="_blank">Braintrust</a></td>
      <td class="center score">6.7</td>
    </tr>
    <tr>
      <td><strong>Last mile quality gates</strong></td>
      <td>I/O guardrails + JSON Schema validation + AI test gen; CI blocks merge until checks pass.</td>
      <td><a href="https://github.com/guardrails-ai/guardrails" target="_blank">Guardrails AI</a>, <a href="https://docs.nvidia.com/nemo-guardrails/index.html" target="_blank">NeMo</a>, <a href="https://developers.openai.com/api/docs/guides/structured-outputs/" target="_blank">OpenAI Structured</a>, <a href="https://www.diffblue.com/diffblue-cover/" target="_blank">Diffblue</a>, <a href="https://keploy.io/" target="_blank">Keploy</a>, <a href="https://junit.org/" target="_blank">JUnit</a></td>
      <td class="center score">4.4</td>
    </tr>
    <tr>
      <td><strong>Security &amp; compliance guardrails</strong></td>
      <td>Static analysis + runtime protection: catch vulnerabilities &amp; prompt injection, enforce compliance policies.</td>
      <td><a href="https://snyk.io/product/snyk-code/" target="_blank">Snyk Code</a>, <a href="https://semgrep.dev/" target="_blank">Semgrep</a>, <a href="https://codeql.github.com/docs/" target="_blank">CodeQL</a>, <a href="https://www.lakera.ai/lakera-guard" target="_blank">Lakera Guard</a>, <a href="https://www.holisticai.com/" target="_blank">Holistic AI</a>, <a href="https://protectai.com/" target="_blank">Protect AI</a></td>
      <td class="center score">4.4</td>
    </tr>
    <tr>
      <td><strong>AI code reviewer</strong></td>
      <td>AI analyzes diffs &amp; repo context, finds issues, generates review summaries.</td>
      <td><a href="https://www.qodo.ai/" target="_blank">Qodo</a>, <a href="https://coderabbit.ai/" target="_blank">CodeRabbit</a>, <a href="https://github.com/qodo-ai/pr-agent" target="_blank">PR-Agent</a></td>
      <td class="center score">4.4</td>
    </tr>
    <tr>
      <td><strong>AI-driven task orchestration</strong></td>
      <td>Tasks get AI context; agents run on subtasks; code changes, PRs &amp; statuses flow in one managed pipeline.</td>
      <td><a href="https://vibekanban.com/" target="_blank">Vibe Kanban</a></td>
      <td class="center score">4.4</td>
    </tr>
    <tr>
      <td><strong>Deterministic LLM output</strong></td>
      <td>Force strictly validatable structure; retry/fix on schema mismatch.</td>
      <td><a href="https://ai.pydantic.dev/" target="_blank">PydanticAI</a>, <a href="https://github.com/567-labs/instructor" target="_blank">Instructor</a>, <a href="https://github.com/dottxt-ai/outlines" target="_blank">Outlines</a></td>
      <td class="center score">1.5</td>
    </tr>
    <tr>
      <td><strong>Human-Freelancer in the Loop</strong></td>
      <td>AI writes code; freelancer expert approves changes instead of the team.</td>
      <td><a href="https://tendem.ai/" target="_blank">Tendem</a></td>
      <td class="center score">1.5</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> Spec-driven and Observability share the top ICE Score (6.7), but spec-driven wins the tie-break: it is a <em>Shift-Left</em> (preventive) approach that constrains AI output before generation, while Observability is <em>Shift-Right</em> (reactive) — it detects issues after execution. For the trust JTBD, prevention > detection. JB PSI also gives spec-driven a native IDE advantage.</p>
</div>

<ul class="distrust-notes">
<li>Impact is scored 1–3 across 9 criteria. Speed, DX, Quality, and JTBD time-saved are grouped as one "Delivery Outcomes" block (their weights sum to 1), equal to each of the other dimensions (Cost, Transparency, SDLC coverage, Adoption friction, Monetization), which all have equal weight. Impact Total is the weighted average. Total Score = Impact Total × Confidence ÷ Effort (Effort and Confidence both rated 1–3). <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=549312952#gid=549312952&range=A1" target="_blank">Details →</a></li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
<li>Note: IDE-native steering files (Cursor Rules, CLAUDE.md, Windsurf Memory) partially solve persistent context but lack spec enforcement, drift detection, and structured generation pipelines.</li>
<li>Each score was triangulated against: (1) Distrust + Time Spent + B2B evidence, (2) competitor traction signals, (3) JB SDK feasibility.</li>
</ul>

Notes:
This slide maps competitive approaches to improving trust in AI-assisted development, scored using a weighted ICE framework. Impact is scored 1–3 across 9 criteria. Speed, DX, Quality, and JTBD time-saved are grouped as one "Delivery Outcomes" block (weights sum to 1), equal to Cost, Transparency, SDLC coverage, Adoption friction, and Monetization. Impact Total is the weighted average. Total Score = Impact Total × Confidence ÷ Effort.
Spec-driven and Observability both score 6.7 — the tie-break is the intervention point. Spec-driven is Shift-Left: it constrains ambiguity before code generation via a reviewable contract. Observability is Shift-Right: it detects drift and regressions after execution. For the trust JTBD ("I want AI output to be predictable so I don't break production"), preventive control is the stronger fit — the developer needs trust before merging, not post-merge diagnostics. Additionally, JetBrains PSI enables bi-directional spec↔code within the IDE, giving spec-driven a native platform advantage that observability (infrastructure-layer) does not benefit from.

---
<!-- .slide: id="roadmap-main-appendix" -->

## HOW: Roadmap <span class="metric-badge">A</span>

<div class="roadmap-container" style="display: flex !important; flex-direction: column !important; gap: 8px !important; font-size: 0.48em !important; line-height: 1.18 !important; width: 100% !important;">

  <!-- Phase 1 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; justify-content: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Month 1</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 1: PoC</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;"><strong style="color: var(--r-main-color);">Goal:</strong> Pick the entry point and primary data scenario pre-product.<br><strong style="color: var(--r-main-color);">Do:</strong> 10-15 partners (power JB users, JB dev employees, large friendly client teams); 3 prototypes (spec-first control, review assist, diff change containment); one measurable repeatable flow with fail/error log; spec format v1 + 5-10 examples.<br><span style="color: #64ffda; font-weight: bold;">Gate:</span> <span class="metric-badge">A</span><br>&bull; Pilot commitments &ge;3<br>&bull; Problem ranks top-3 for &ge;5/8 respondents in AI dev<br>&bull; Qualified waitlist signups (ICP) &ge;15<br>&bull; Core risk: demand for spec-first is a hypothesis; Month 1 runs 3 PoCs with a hard gate on repeat usage.</p>
    </div>
  </div>

  <!-- Phase 2 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; justify-content: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Month 2</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 2: Monetization & OSS</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;"><strong style="color: var(--r-main-color);">Goal:</strong> Lock commercial demand before MVP.<br><strong style="color: var(--r-main-color);">Do:</strong> Get payment-intent verification from &ge;3 companies (named budget owner + pilot terms), define pilot KPI/outcomes/client inputs, and package JetBrains ecosystem offer (standalone plugin vs AI plans). OSS track: spec format v1 + validator + examples to widen funnel and reduce trust risk.<br><span style="color: #64ffda; font-weight: bold;">Gate:</span> <span class="metric-badge">A</span> &ge;3 payment-intent commitments with named budget owners and agreed pilot terms.</p>
    </div>
  </div>

  <!-- Phase 3 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(90, 65, 65, 0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; justify-content: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Months 3-4</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 3: MVP Launch</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;"><strong style="color: var(--r-main-color);">Goal:</strong> Soft-launch a minimal IDE plugin and start paid pilots.<br><strong style="color: var(--r-main-color);">Do:</strong> MVP on one primary scenario, one low-noise quality check (change containment or drift signal), one workflow integration (PR/commits), first paid partner pilots.<br><span style="color: #64ffda; font-weight: bold;">Gate:</span> <span class="metric-badge">A</span><br>&bull; Paid partner pilots &ge;3<br>&bull; Token spend per successful PR-ready outcome &darr; 10%<br>&bull; % PRs where CI checks pass on 1st try &uarr; 10%<br>&bull; Median time to PR-ready (from spec approved) &darr; 10-20%<br>&bull; Target range: 10-20% fewer unscoped diffs / rework signals</p>
    </div>
  </div>

  <!-- Phase 4 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; justify-content: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Months 5-6</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 4: Standardization</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;"><strong style="color: var(--r-main-color);">Goal:</strong> Standardize the governed-change workflow for JetBrains teams and partner organizations, and start ecosystem effects.<br><strong style="color: var(--r-main-color);">Do:</strong> Publish in JB ecosystem (listing, onboarding, activation), add team features (shared templates, baseline settings, usage visibility), and push OSS growth (format refresh, starter templates, first external contributors).<br><span style="color: #64ffda; font-weight: bold;">Gate:</span> <span class="metric-badge">A</span><br>&bull; MRR target: $5-15k from paid pilots by Month 4-6<br>&bull; Usage: most active teams run core scenario &ge;2x/week<br>&bull; &ge;70% with clear qualitative wins (CS + SMM)<br>&bull; Guardrail: alert disable rate stable + cost per outcome stable<br>&bull; Active users per org target: 3-5 by Month 6</p>
    </div>
  </div>

</div>


---
<!-- .slide: id="risks-mitigation-main-appendix" -->

<h2>HOW: Risks & Mitigation</h2>

<div class="risk-table-container">
  <table class="risk-table">
    <thead>
      <tr>
        <th class="col-num">#</th>
        <th class="col-risk">Risk Name</th>
        <th class="col-mitigation">Mitigation Strategy</th>
        <th class="col-status">Impact <span class="metric-badge">A</span></th>
        <th class="col-status">Prob. <span class="metric-badge">A</span></th>
        <th class="col-score">Score <span class="metric-badge">A</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="col-num"><strong>0</strong></td>
        <td class="col-risk"><strong>PoC risk: we can't prove repeatable value for spec-first + diff control</strong></td>
        <td class="col-mitigation">Month 1: 3 parallel PoCs with an instrumented prototype: (1) spec-first control, (2) review help, (3) diff control (change containment). Gate: most partners repeat the core scenario 2x in 7 days and outcomes beat alternatives. If not, switch the entry point before building the plugin MVP.</td>
        <td class="col-status text-high"><strong>High</strong></td>
        <td class="col-status text-med"><strong>Med</strong></td>
        <td class="col-score"><strong>6</strong></td>
      </tr>
      <tr>
        <td class="col-num">1</td>
        <td class="col-risk">Partner risk: can't recruit enough high-signal design partners fast</td>
        <td class="col-mitigation">Two-track recruitment: (a) warm network for named companies, (b) OSS narrow scope (Spec Format + validator + examples) to widen the funnel. Use OSS to attract credible teams, collect spec samples, and convert top contributors into pilots.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">2</td>
        <td class="col-risk">PSI Engine Complexity</td>
        <td class="col-mitigation">Focus on JetBrains ecosystem (Kotlin first), leverage native PSI APIs for stability.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">3</td>
        <td class="col-risk">Developer Friction</td>
        <td class="col-mitigation">Zero-friction code-first extraction. Repo-native .md format lives in current workflow.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">4</td>
        <td class="col-risk">Competitor Entry</td>
        <td class="col-mitigation">Deep IDE-native PSI integration provides a semantic moat generic LLMs lack.</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">4</td>
      </tr>
      <tr>
        <td class="col-num">5</td>
        <td class="col-risk">Monetization risk: value is clear, but buyers don't approve budget / packaging is confusing</td>
        <td class="col-mitigation">Mo 2: written budget intent + pilot terms (buyer, success metrics, procurement path). Mo 3-4: paid pilots once MVP exists. Keep pricing simple and tie value to measurable outcomes (fewer review iterations, faster time-to-PR, fewer unscoped diffs).</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">4</td>
      </tr>
      <tr>
        <td class="col-num">6</td>
        <td class="col-risk">AI Hallucinations</td>
        <td class="col-mitigation">Human-in-the-loop "Approve" gate before syncing specs. High-precision prompt tuning.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-low">Low</td>
        <td class="col-score">3</td>
      </tr>
      <tr>
        <td class="col-num">7</td>
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

Risk #0 is our highest-priority uncertainty. Developers report distrust in AI code (validated), but they do not explicitly ask for specs (hypothesis). If Phase 1 shows weak repeat usage (most partners don’t repeat the core scenario 2x in 7 days) and alternatives win on measured outcomes, we switch entry point before building the plugin MVP.
Separate risk: if partner recruitment is slow, OSS narrow scope is used to widen the funnel and generate pilots from community pull.

1) **Technical**: We are building on top of JetBrains' own infrastructure. It's complex, but it's where our advantage lies.
2) **Accuracy**: AI is the assistant, not the decider. The "Approve" button is our safety valve.
3) **Adoption**: Documentation fails when it's external. By making it part of the repo and extraction-based, we remove the "writing tax".
4) **Market**: Cursor/Copilot focus on code generation. We focus on structural alignment and predictability.
