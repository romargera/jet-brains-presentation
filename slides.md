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
<td>45.7% distrust AI (up 15.3 pp YoY). 75% would ask a person for help when they don’t trust AI answers. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
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
  <p><strong>Takeaway:</strong> Developers don’t trust AI-generated code enough to ship it without extra time spent polishing, reviewing, and debugging.</p>
</div>

<ul class="distrust-notes">
<li><strong>Notes:</strong> Reach, Freq., Conf. and Score are subjectively estimated/measured based on synthesis of external report signals. All values are <span class="metric-badge">A</span> assumptions.</li>
<li><strong>Conf.</strong> (Confidence) = Probability to make a difference.</li>
</ul>

Notes:
Let's drill down into these distrust issues. We analyzed various market reports and extracted the major pain points. As you can see in this table, the top two issues—highlighted here—are skepticism regarding code accuracy and the increased review and debugging time. Both of these score a 9 when evaluating their Reach, Frequency, and our Confidence that solving them will make a difference. Security concerns are also very high but have slightly less consistent frequency of blocking daily workflows. Note that the scores and parameters are our subjective estimates based on these signals.
