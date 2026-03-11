import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# 1. Duplicate "WHAT: Competitor Landscape" slide
slide_start = content.find('<!-- .slide: id="competitor-landscape" -->')
slide_end = content.find('\n---\n', slide_start)

if slide_start != -1 and slide_end != -1:
    orig_slide = content[slide_start:slide_end]
    
    # Create the duplicated slide
    new_slide = orig_slide.replace('id="competitor-landscape"', 'id="why-competitor-landscape"')
    new_slide = new_slide.replace('## WHAT: Competitor Landscape', '## WHY: Competitor Landscape')
    
    # Replace the left column table with indirect-card tiles
    # Extract left column content to replace
    tbl_start = new_slide.find('<table class="distrust-table">')
    tbl_end = new_slide.find('</table>') + len('</table>')
    
    if tbl_start != -1:
        new_left_col = '''<h4 style="font-size: 1em; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.06em; margin: 0 0 4px; padding-bottom: 3px; border-bottom: 1px solid rgba(255,255,255,0.2);">Direct Competitors</h4>
<div class="indirect-card" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-left: 3px solid #10b981; border-radius: 6px; padding: 4px 6px; margin-bottom: 4px;">
  <p style="font-size: 1em; font-weight: 700; color: #e0e0e0; margin: 0 0 1px;">Tier 1: Direct Threats</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://speckit.org/" target="_blank" style="color: #10b981; text-decoration: none; font-weight: 600;">Spec Kit</a>: GitHub-supported, 73.6k★, phased plan-first workflow, CLI + in-agent</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://kiro.dev/" target="_blank" style="color: #10b981; text-decoration: none; font-weight: 600;">Kiro</a>: Built on Amazon Bedrock, 1.5M MAU, IDE + CLI + in-agent</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://docs.bmad-method.org/" target="_blank" style="color: #10b981; text-decoration: none; font-weight: 600;">BMAD</a>: 38.9k★, 19 roles, CLI + agent, adaptive depth</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://openspec.dev/" target="_blank" style="color: #10b981; text-decoration: none; font-weight: 600;">OpenSpec</a>: Vendor-agnostic, Open Source, No APIs</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://codespeak.dev/" target="_blank" style="color: #10b981; text-decoration: none; font-weight: 600;">CodeSpeak</a>: Specs compile to code, diff sync</p>
</div>
<div class="indirect-card" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-left: 3px solid #ffb74d; border-radius: 6px; padding: 4px 6px; margin-bottom: 4px;">
  <p style="font-size: 1em; font-weight: 700; color: #e0e0e0; margin: 0 0 1px;">Tier 2: Watchlist</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://www.task-master.dev/" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">Taskmaster</a>: PRD→tasks + TDD autopilot</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://stately.ai/" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">Stately</a>: State machines as specs</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://buildermethods.com/agent-os" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">Agent-OS</a>: Auto-extract repo conventions</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://github.com/ariel-frischer/autospec" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">Autospec</a>: Spec Kit fork, YAML pipeline</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://specs.md/" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">specs.md</a>: Formal AI-DLC, VS Code ext</p>
  <p style="font-size: 0.85em; color: rgba(255,255,255,0.6); margin: 0 0 2px;"><a href="https://www.autok.dev/" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">autok</a> / <a href="https://www.devplan.com/" target="_blank" style="color: #ffb74d; text-decoration: none; font-weight: 600;">devplan</a>: Graph context + sync</p>
</div>'''
        new_slide = new_slide[:tbl_start] + new_left_col + new_slide[tbl_end:]
        content = content[:slide_end] + "\n\n---\n" + new_slide + content[slide_end:]

# 2. Remove empty slide 28
content = re.sub(r'\n---\n\s*\n---\n', '\n---\n', content)

# 3. Modify "Market Size"
old_market_size = '''<a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=856599423#gid=856599423&range=A1" target="_blank" style="color: inherit; text-decoration: underline;">TAM ($4.9B) → SAM ($3.4B) → SOM ($171M)</a><br><br><a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=A1" target="_blank" style="color: inherit; text-decoration: underline;">Bottom-up SOM (Year 1): $9.3M</a>'''

new_market_size = '''<a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=856599423#gid=856599423&range=A1" target="_blank" style="color: inherit; text-decoration: underline;">Top-down SOM is $171.85M</a>, based on a $4.91B 2024 market, a 70% production workflows share, and a 5% achievable share, while the <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=A1" target="_blank" style="color: inherit; text-decoration: underline;">bottom-up Year 1 cross-check yields ~$0.93M</a>.'''

content = content.replace(old_market_size, new_market_size)

# 4. Modify Key Metrics & Guardrails
metrics_start = content.find('<!-- .slide: id="metrics" -->')
metrics_end = content.find('\n---\n', metrics_start)

if metrics_start != -1 and metrics_end != -1:
    old_metrics_slide = content[metrics_start:metrics_end]
    
    new_metrics_content = '''<!-- .slide: id="metrics" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: Key Metrics & Guardrails</h2>

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

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
    <p class="chosen-tile-label">2. Monetization (MRR)</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>New MRR:</b> Activation to paid, ARPU, Churn (IC/seats)</li>
        <li><b>Attributed JB MRR:</b> Attach rate (JB paid with config), Cohort ARPU & Churn</li>
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
        <li><b>Cost:</b> Total avg token spend, Token cost per governed change</li>
        <li><b>Quality:</b> % PRs passing checks on 1st try</li>
      </ul>
    </div>
  </div>

</div>

Notes:

1) **North Star**: Focus is on habitual usage (spec-linked merges), tracking both individual users and orgs.
2) **Monetization**: Tracking New MRR for the product, and rigorously attributing JB Core revenue via matched cohort uplifts.
3) **Safety & Quality**: Tracking latency and false positives alongside qualitative CSAT to ensure we don't harm the IDE experience.
4) **Value**: Proving cost efficiency and improved PR throughput (passing checks on 1st try).'''
    
    content = content.replace(old_metrics_slide, new_metrics_content)

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
    f.write(content)

print("Done")
