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
<tr class="highlight-row">
<td>Security/Compliance</td>
<td class="center">11.48%</td>
<td class="center">3.07%</td>
<td class="center score">8.40%</td>
<td class="center val-med">Med</td>
<td>Opportunity to impower on the planning step</td>
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
<tr class="highlight-row">
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
<!-- .slide: id="stream-options" -->

## WHAT: Strategic Directions

<p style="font-size: 0.45em; color: var(--text-muted); margin: 0 0 8px; line-height: 1.4;">Directions are derived from the top issues across three evidence layers: <strong style="color: var(--text-main);">Distrust</strong>, <strong style="color: var(--text-main);">Time Spent</strong>, and <strong style="color: var(--text-main);">B2B Issues</strong>.</p>

<table class="score-table">
  <thead>
    <tr>
      <th>Direction</th>
      <th>Source</th>
      <th>Impact <span class="metric-badge">A</span></th>
      <th>Effort <span class="metric-badge">A</span></th>
      <th>Conf. <span class="metric-badge">A</span></th>
      <th>Score <span class="metric-badge">A</span></th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>AI-dev transparency:</strong> code &amp; architecture</td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>High</td><td>High</td><td>Med</td><td>2.5</td>
    </tr>
    <tr>
      <td><strong>Security &amp; Compliance</strong> (proactive assist)</td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>Med</td><td>Med</td><td>Low</td><td>1.7</td>
    </tr>
    <tr>
      <td><strong>Review &amp; Debug assist</strong></td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>Med</td><td>High</td><td>Med</td><td>1.7</td>
    </tr>
    <tr>
      <td><strong>Spec Formalisation Assist</strong> (proactive assist)</td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>Med</td><td>Med</td><td>Low</td><td>1.7</td>
    </tr>
    <tr>
      <td><strong>Dev Env Simplification</strong></td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>Med</td><td>Med</td><td>Low</td><td>1.7</td>
    </tr>
    <tr>
      <td><strong>Delivery time variability</strong> (accurate forecasting)</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>Med</td><td>Med</td><td>Low</td><td>1.7</td>
    </tr>
    <tr>
      <td><strong>Token Spent Optimization</strong></td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>Low</td><td>Med</td><td>Med</td><td>1.3</td>
    </tr>
    <tr>
      <td><strong>Quality &amp; reliability risk</strong> from software errors</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>Med</td><td>High</td><td>Low</td><td>1.1</td>
    </tr>
  </tbody>
</table>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> AI-dev transparency: code &amp; architecture is the top-priority direction, uniquely positioned at the intersection of all three pain layers with the highest value-to-cost score.</p>
</div>

<ul class="distrust-notes">
<li>Score ranks directions by value vs cost: Score = (Impact × Confidence) / Effort.</li>
<li>Mapping: Impact/Effort High=3, Med=2, Low=1; Confidence High=1, Med=0.75, Low=0.5.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

Notes:
Directions are scored by value-to-cost ratio to make prioritization explicit and defensible.
Score = (Impact × Confidence) / Effort. Mapping: Impact/Effort High=3, Med=2, Low=1; Confidence High=1, Med=0.75, Low=0.5.
All scores are assumptions marked with A — to be validated through user interviews and early pilots.
Next: we define the chosen direction in detail with JTBD and early adopter segments.

---
<!-- .slide: id="jtbd-icp" -->

## WHAT: Chosen Direction

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Chosen Direction</p>
    <p class="chosen-tile-body">AI-dev transparency layer for code &amp; architecture: keeping AI output aligned with specs, reviewable, and predictable.</p>
  </div>

  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">The Problem (Pain)</p>
    <p class="chosen-tile-body">AI adoption hit 90%, yet distrust surged +15 pp YoY <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a>. 45% spend more time debugging AI code than expected <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[2]</a>. High-value tasks (architecture, coding) are crowded out by overhead: broken output, extra communication, security reviews, env drift <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf" target="_blank">[3]</a>.</p>
  </div>

  <div class="chosen-tile chosen-tile--green chosen-tile--wide">
    <p class="chosen-tile-label">Core JTBD</p>
    <p class="chosen-tile-body">When engineers build with AI in a production codebase, they want development to be predictable and controllable, so they can ship faster with confidence.</p>
  </div>

</div>

<ul class="distrust-notes">
<li>Decomposed by target segments in the next slides.</li>
</ul>

Notes:
This slide synthesises the three evidence slides into a concrete product decision. The chosen direction — AI-dev transparency for code and architecture — directly addresses the top-scoring pains: distrust (Distrust Issues slide), time waste (Dev Time Spent slide), and quality risk (B2B Pains slide). The JTBD statement frames the problem from the user's perspective and defines the minimum valuable outcome.

---
<!-- .slide: id="competitive-approaches" -->

## WHAT: Approaches

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
</ul>

Notes:
This slide maps competitive approaches to improving trust in AI-assisted development, scored using a weighted ICE framework. Impact is scored 1–3 across 9 criteria. Speed, DX, Quality, and JTBD time-saved are grouped as one "Delivery Outcomes" block (weights sum to 1), equal to Cost, Transparency, SDLC coverage, Adoption friction, and Monetization. Impact Total is the weighted average. Total Score = Impact Total × Confidence ÷ Effort. Spec-driven development leads because it addresses ambiguity at the root — before code generation — delivering the highest combined score of 3.3.

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
      <td>GitHub-supported, 73.6k★, markdown specs, фазовый plan-first, CLI + in-agent</td>
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
      <td>Specs compile directly to production code, code-to-specs, compiler/ batch model</td>
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
      <td>Knowledge-graph planning→execution pipeline, CLI + in‑agent</td>
    </tr>
  </tbody>
</table>
</div>
<div class="competitor-col-right" style="font-size: 0.28em;">
<h4 style="font-size: 1em; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.06em; margin: 0 0 4px; padding-bottom: 3px; border-bottom: 1px solid rgba(255,255,255,0.2);">Indirect Competitors</h4>
<div class="indirect-card" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-left: 3px solid #4fc3f7; border-radius: 6px; padding: 4px 6px; margin-bottom: 4px;">
  <p style="font-size: 1em; font-weight: 700; color: #e0e0e0; margin: 0 0 1px;">IDE AI Assistants (baseline)</p>
  <p style="font-size: 0.9em; margin: 0 0 1px;"><a href="https://cursor.com/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">Cursor</a>, <a href="https://github.com/features/copilot" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">Copilot</a>, <a href="https://www.jetbrains.com/ai-assistant/" target="_blank" style="color: #4fc3f7; text-decoration: none; font-weight: 600;">JB AI</a></p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.5); margin: 0; font-style: italic;">Where 100% ICP already is</p>
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
    <p class="chosen-tile-body">Spec↔Code compiler (CodeSpeak). Prevents doc rot.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">IDE-Native Surface</p>
    <p class="chosen-tile-body">Web-first creates context switch. Keep devs in-IDE.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Persistent Steering</p>
    <p class="chosen-tile-body">Project rules (Kiro). Stops AI amnesia on long projects.</p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 15px;">
  <p><strong>Synthesis:</strong> The winning formula is a Git-native, bi-directional spec tool living entirely inside the IDE.</p>
</div>

Notes:
Here we look at what's actually working in the market. First, Git-native markdown specs are the standard—tools like SpecKit prove developers won't adopt proprietary formats. Second, bi-directional sync: specs compile to code, code updates specs (like CodeSpeak), which stops doc rot. Third, surface area: web-first SaaS creates a context switch; successful workflows are IDE-native or CLI-native. Finally, persistent steering and slash-commands give us a natural UX that prevents AI amnesia.

---
<!-- .slide: id="niche-choice" -->

## WHAT: Niche Choice

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
      <td>Zero context switch. Uncontested space. Massive JB distribution moat.</td>
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

## WHAT: Why Us (Differentiation)

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
      <td>Context via flat AST or text vectors. Leads to severe hallucinations in large mono-repos.</td>
      <td>Proprietary JB PSI engine. Understands code as deeply as the compiler.</td>
    </tr>
    <tr>
      <td><strong>Continuous drift detection</strong></td>
      <td>Reactive CI checks or flat doc rotting. (Auto-K waits in beta).</td>
      <td>Proactive inline warnings + bi-directional sync (code ↔ spec) to prevent divergence.</td>
    </tr>
    <tr>
      <td><strong>AI-Native BDD (Evals)</strong></td>
      <td>Blind generation ("generate and pray"). No automated validation of the LLM output.</td>
      <td>Generates tests and validates AI code against strict Spec schemas before the dev sees it.</td>
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

---
<!-- .slide: id="why-summary" -->

## WHY: Summary & Market

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Strategic Setup & AI Adoption</p>
    <p class="chosen-tile-body">AI adoption hit 90% but distrust surged +15pp. High-value tasks are crowded out by overhead. The window for a trust-layer governance tool is now.</p>
  </div>

  <div class="chosen-tile chosen-tile--green" style="padding: 10px;">
    <p class="chosen-tile-label">Market Size (USD, 2024 Base)</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0 0 10px 0; padding-left: 20px; font-size: 0.9em;">
        <li><strong>TAM:</strong> $4.9B</li>
        <li><strong>SAM:</strong> $3.4B</li>
        <li><strong>SOM:</strong> $171M</li>
      </ul>
      <div style="font-size: 0.7em; text-align: right; margin-top: 5px; color: var(--text-muted);">
        <em>* <a href="#" target="_blank">Top-down calculation</a> (Bottom-up to follow)</em><br/>
        <em>Data source: <a href="#" target="_blank">JetBrains test task prep - TAM SAM SOM</a></em>
      </div>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Niche & ICP</p>
    <p class="chosen-tile-body">Uncontested IDE-native wedge for Tech Leads wanting predictable architecture.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Growth Loops</p>
    <p class="chosen-tile-body">Repo-native viral adoption (1 repo = many devs) + strict PR/CI enforcement gates.</p>
  </div>

</div>

<ul class="distrust-notes">
<li>Assumptions: Based on 70% share of AI-using pros in production workflows, targeting 5% of SAM.</li>
<li>Revenue base year 2024, adoption base year 2025.</li>
</ul>

Notes:

* Рынок AI-тулзов оценивается по-разному (~$4–5B). Чтобы не завышать TAM, мы берем консервативную базу $4.91B (2024), сохраняя альтернативный апсайд-сценарий.
* Ожидаемый рост через Tech Lead'ов легко скейлится благодаря "repo-native loop" и CI/PR гейтам.

---
<!-- .slide: id="growth-loops" -->

## HOW: Growth Loops

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Repo-Native Viral Loop</p>
    <p class="chosen-tile-body">1 user adds <code>/specs</code>. Entire team interacts via PR gates. Fast intra-team spread.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">PR / CI Enforcement</p>
    <p class="chosen-tile-body">More compliance checks = fewer bugs. Value compounds, raising switching costs.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Spec Template Marketplace</p>
    <p class="chosen-tile-body">Community-built spec packs for standard flows (auth, billing). Accelerates new starts.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Ecosystem Standard</p>
    <p class="chosen-tile-body">Format works across IDEs & repos. Becomes an org-wide standard, not just a tool.</p>
  </div>

</div>

<ul class="distrust-notes">
<li>Invite-the-reviewer loop: sharing readable contracts draws non-devs into the process.</li>
</ul>

Notes:
Here we detail the growth engine.

1) Repo-native: one person installs it, but the whole team must interact with it through CI checks and PR comments.
2) Quality loop: the more rules teams add, the deeper integrated it becomes (high switching cost).
3) Content loop: shared templates for common architectures reduce cold-start friction.
4) Ecosystem / Multi-repo: a single specification scales across multiple repositories and works with any client (Cursor, VS Code, CLI), making Bonsai the standard protocol rather than just another IDE plugin.
