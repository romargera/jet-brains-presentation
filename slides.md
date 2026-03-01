<!-- .slide: id="title" -->

<div class="title-slide">
  <p class="title-label">Take-Home Task</p>
  <h1>Bonsai<br></h1>
  <p class="title-subtitle">Predictable AI-assisted Development<br>via Spec-driven Control</p>
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
<tr>
<td>Security/Compliance</td>
<td class="center">11.48%</td>
<td class="center">3.07%</td>
<td class="center score">8.40%</td>
<td class="center val-med">Med</td>
<td>Opportunity to impower on the planning step</td>
</tr>
<tr>
<td>Communication</td>
<td class="center">12.95%</td>
<td class="center">6.57%</td>
<td class="center score">6.38%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Debugging</td>
<td class="center">11.20%</td>
<td class="center">7.48%</td>
<td class="center score">3.72%</td>
<td class="center val-high">High</td>
<td>Opportunity to keep usefull and updated spec</td>
</tr>
<tr>
<td>Customer Support</td>
<td class="center">7.49%</td>
<td class="center">3.98%</td>
<td class="center score">3.50%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Env Setup</td>
<td class="center">3.78%</td>
<td class="center">1.54%</td>
<td class="center score">2.24%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep usefull and updated spec</td>
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
<td>Opportunity to automize via agent orcestration</td>
</tr>
<tr>
<td>Code Refactoring</td>
<td class="center">5.25%</td>
<td class="center">4.75%</td>
<td class="center score">0.50%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep usefull and updated spec</td>
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
<td>Automazation already have widely adopted</td>
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
<tr>
<td>System Arch/Design</td>
<td class="center">8.89%</td>
<td class="center">15.37%</td>
<td class="center score">-6.49%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
<tr>
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
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> We see an opportunity to cut low-value overhead and reinvest the saved capacity into the core work developers value most: Coding, System Architecture/Design, Security/Compliance, Debugging, and Env Setup.</p>
</div>

<ul class="distrust-notes">
<li>Time spend data is based on <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf" target="_blank">Microsoft's Time-Warp Study</a>.</li>
<li>Prob.(Probability) = Probability to make a difference.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

Notes:
Here we look at how developers actually spend their time versus how they ideally want to spend it. The largest gaps—the overhead we can cut—are in Security & Compliance, Debugging, and Environment Setup. At the same time, we see massive negative gaps in Coding and System Architecture. Developers want to spend almost double the time on architecture and double the time on coding. If we can automate the high-gap overhead areas, we unlock capacity for the deep work that drives real product value and developer satisfaction.

---
<!-- .slide: id="stream-options" -->

## WHAT: Strategic Directions

<table class="score-table">
  <thead>
    <tr>
      <th>Direction</th>
      <th>Pain / Issue</th>
      <th>Impact</th>
      <th>Effort</th>
      <th>Conf.</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Review &amp; Debug Preparations:</strong> AI quality gates &amp; checklists to cut rework</td>
      <td><span class="tag tag-pain-review">Review &amp; Debug</span></td>
      <td>High</td><td>Med</td><td>High</td><td>14</td>
    </tr>
    <tr>
      <td><strong>Spec as Control Plane:</strong> executable constraints for agents &amp; PRs</td>
      <td><span class="tag tag-pain-quality">Quality/Accuracy</span></td>
      <td>High</td><td>Med</td><td>Med</td><td>13</td>
    </tr>
    <tr>
      <td><strong>Security &amp; Compliance Guardrails:</strong> spec-embedded checks to prevent violations early</td>
      <td><span class="tag tag-pain-quality">Quality/Accuracy</span></td>
      <td>High</td><td>Med</td><td>High</td><td>13</td>
    </tr>
    <tr>
      <td><strong>Token Spent Optimization:</strong> proactive &amp; reactive assist to cut LLM cost &amp; waste</td>
      <td><span class="tag tag-token-spent">Token Spent Opt.</span></td>
      <td>High</td><td>Med</td><td>Med</td><td>12</td>
    </tr>
    <tr>
      <td><strong>Spec Formalisation Assist:</strong> turn requirements into machine-readable specs</td>
      <td><span class="tag tag-time-spent">Time Spent Opt.</span></td>
      <td>Med</td><td>Med</td><td>Med</td><td>11</td>
    </tr>
    <tr>
      <td><strong>Dev Env Automation / Simplification:</strong> reproducible specs to cut setup overhead</td>
      <td><span class="tag tag-time-spent">Time Spent Opt.</span></td>
      <td>Med</td><td>Low</td><td>Med</td><td>11</td>
    </tr>
    <tr>
      <td><strong>Drift Detection:</strong> detect spec-to-code divergence before it compounds</td>
      <td><span class="tag tag-pain-quality">Quality/Accuracy</span></td>
      <td>Med</td><td>High</td><td>Med</td><td>10</td>
    </tr>
    <tr>
      <td><strong>Agent Plan Traceability:</strong> plan-to-action evidence with interruptibility &amp; control points</td>
      <td><span class="tag tag-time-spent">Time Spent Opt.</span></td>
      <td>Med</td><td>Med</td><td>Med</td><td>10</td>
    </tr>
  </tbody>
</table>

Notes:
This slide shows the solution space. We can invest in multiple streams, but for early adoption we should pick a wedge aligned with our mission: predictable, spec-driven agent work.
Scoring (assumption): Impact = Reach + Frequency + Probability (H=3/M=2/L=1). Total = Impact + Confidence + Effort (inverted, Low=3/Med=2/High=1). All values are assumptions, validated later via interviews and early pilots.
Next, we define JTBD and the early adopter segments for the chosen direction.

---
<!-- .slide: id="jtbd-icp" -->

## WHAT: Chosen Direction

<div style="display: flex; gap: 10px; margin-bottom: 10px;">
  <div style="flex: 1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 14px;">
    <h4 style="margin: 0 0 6px; font-size: 0.75em; color: var(--accent, #e05c5c); text-transform: uppercase; letter-spacing: 0.08em;">⚡ The Problem (Pain)</h4>
    <p style="margin: 0; font-size: 0.58em; line-height: 1.45; color: var(--text-muted);">AI adoption hit 90%, yet distrust surged 15 pp YoY. Developers spend 45% more time debugging AI code than expected. Architecture and coding — the tasks they value most — are being crowded out by low-value overhead: debugging broken AI output, security reviews, and environment drift.</p>
  </div>
  <div style="flex: 1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 14px;">
    <h4 style="margin: 0 0 6px; font-size: 0.75em; color: #4ade80; text-transform: uppercase; letter-spacing: 0.08em;">🎯 Chosen Direction</h4>
    <p style="margin: 0; font-size: 0.58em; line-height: 1.45; color: var(--text-muted);">Spec-driven control layer for AI agents inside JetBrains IDEs — turning living specs into a persistent source of truth that keeps AI output aligned, reviewable, and predictable. Wedge: <strong style="color: #4ade80;">spec-aware code review + drift detection</strong> for teams already using AI tools daily.</p>
  </div>
</div>

<div class="adoption-layout" style="gap: 10px;">
  <div class="adoption-col adoption-col-left" style="background: rgba(74,222,128,0.05); border: 1px solid rgba(74,222,128,0.25); border-radius: 8px; padding: 10px 14px;">
    <h4 style="margin: 0 0 8px; font-size: 0.75em; color: #4ade80; text-transform: uppercase; letter-spacing: 0.06em;">Segments</h4>
    <div style="margin-bottom: 8px;">
      <p style="margin: 0 0 3px; font-size: 0.62em; font-weight: 600; color: #a3f0c0;">① Tech Leads & Staff/Principal Engineers</p>
      <p style="margin: 0; font-size: 0.55em; line-height: 1.4; color: var(--text-muted);">Teams of 10–50+ devs · Strong PR & review culture · Complex systems with compliance/reliability constraints · Heavy JetBrains IDE users, daily AI tools</p>
    </div>
    <div>
      <p style="margin: 0 0 3px; font-size: 0.62em; font-weight: 600; color: #a3f0c0;">② Solution Architects & Platform Engineers</p>
      <p style="margin: 0; font-size: 0.55em; line-height: 1.4; color: var(--text-muted);">Own the spec & architecture layer · High cost of implementation drift · Responsible for AI tooling adoption across the org · Need auditability and traceability</p>
    </div>
  </div>

  <div class="adoption-col adoption-col-right" style="background: rgba(74,222,128,0.05); border: 1px solid rgba(74,222,128,0.25); border-radius: 8px; padding: 10px 14px;">
    <h4 style="margin: 0 0 8px; font-size: 0.75em; color: #4ade80; text-transform: uppercase; letter-spacing: 0.06em;">JTBD</h4>
    <ul style="margin: 0; padding-left: 14px; font-size: 0.56em; line-height: 1.5; color: var(--text-muted);">
      <li style="margin-bottom: 8px;"><span style="color: #d1fae5;">When</span> I ship AI-assisted code, <span style="color: #d1fae5;">I want to</span> ensure it matches the intended architecture and spec, <span style="color: #d1fae5;">so I can</span> merge with confidence without a full manual review.</li>
      <li style="margin-bottom: 8px;"><span style="color: #d1fae5;">When</span> the codebase drifts from the design, <span style="color: #d1fae5;">I want to</span> detect it instantly inside my IDE, <span style="color: #d1fae5;">so I can</span> fix it before it compounds into technical debt.</li>
      <li><span style="color: #d1fae5;">When</span> onboarding new devs or AI agents, <span style="color: #d1fae5;">I want to</span> give them a living, structured spec, <span style="color: #d1fae5;">so I can</span> reduce ramp-up time and prevent misaligned output from day one.</li>
    </ul>
  </div>
</div>
