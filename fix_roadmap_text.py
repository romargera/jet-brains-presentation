import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

start_str = '## HOW: 6-Month Roadmap'
slide_start = content.find(start_str)

if slide_start != -1:
    next_delim = content.find('\n---\n', slide_start)
    if next_delim == -1:
        next_delim = len(content)
        
    new_slide = """## HOW: 6-Month Roadmap

<div class="roadmap-container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.6em; line-height: 1.25;">

  <!-- Phase 1 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 6px;">
    <div class="roadmap-timeline" style="margin-bottom: 4px; display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em; padding: 2px 6px; display: inline-block;">Month 1</span>
      <span style="font-size: 0.75em; font-weight: bold; color: rgba(255,255,255,0.7); text-transform: uppercase;">Phase 1: PoC</span>
    </div>
    <div class="roadmap-content" style="padding: 2px 6px;">
      <p style="font-size: 0.9em; margin: 0 0 6px 0;">Select core flow with 10–15 design partners via fast prototyping (spec-first, review assist). Author initial spec format draft.</p>
      <p style="font-size: 0.85em; margin: 0;"><span style="color: #64ffda; font-weight: bold;">Gate:</span> Core flow validated via repeated weekly use.</p>
    </div>
  </div>

  <!-- Phase 2 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 6px;">
    <div class="roadmap-timeline" style="margin-bottom: 4px; display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em; padding: 2px 6px; display: inline-block;">Month 2</span>
      <span style="font-size: 0.75em; font-weight: bold; color: rgba(255,255,255,0.7); text-transform: uppercase;">Phase 2: Monetization & OSS</span>
    </div>
    <div class="roadmap-content" style="padding: 2px 6px;">
      <p style="font-size: 0.9em; margin: 0 0 6px 0;">Secure commercial intent by gathering letters of intent from 3+ companies with defined pilot metrics. Package for the JB Ecosystem.</p>
      <p style="font-size: 0.85em; margin: 0;"><span style="color: var(--r-main-color); font-weight: bold;">OSS:</span> Build trust with format v1 and open validator.</p>
    </div>
  </div>

  <!-- Phase 3 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 6px;">
    <div class="roadmap-timeline" style="margin-bottom: 4px; display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em; padding: 2px 6px; display: inline-block;">Months 3-4</span>
      <span style="font-size: 0.75em; font-weight: bold; color: rgba(255,255,255,0.7); text-transform: uppercase;">Phase 3: Scale</span>
    </div>
    <div class="roadmap-content" style="padding: 2px 6px;">
      <p style="font-size: 0.9em; margin: 0 0 6px 0;">Launch IDE-plugin MVP focused on the core scenario with high-signal quality checks and seamless workflow integration. Run first paid pilots.</p>
      <p style="font-size: 0.85em; margin: 0;"><span style="color: #64ffda; font-weight: bold;">Gate:</span> 5+ paying teams or equivalent revenue signal.</p>
    </div>
  </div>

  <!-- Phase 4 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 6px;">
    <div class="roadmap-timeline" style="margin-bottom: 4px; display: flex; flex-direction: column; align-items: flex-start; gap: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em; padding: 2px 6px; display: inline-block;">Months 5-6</span>
      <span style="font-size: 0.75em; font-weight: bold; color: rgba(255,255,255,0.7); text-transform: uppercase;">Phase 4: Standard</span>
    </div>
    <div class="roadmap-content" style="padding: 2px 6px;">
      <p style="font-size: 0.9em; margin: 0 0 6px 0;">Solidify standard. Publish to JB Marketplace with team-ready features (shared templates, visibility). Drive open-source growth.</p>
      <p style="font-size: 0.85em; margin: 0;"><span style="color: #64ffda; font-weight: bold;">Gate:</span> Self-serve works across multi-user organizations.</p>
    </div>
  </div>

</div>
"""
    content = content[:slide_start] + new_slide + content[next_delim:]
    with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
        f.write(content)

print("Done")
