import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# Locate the HOW: 6-Month Roadmap slide
start_str = '## HOW: 6-Month Roadmap'
slide_start = content.find(start_str)

if slide_start != -1:
    next_delim = content.find('---\n', slide_start)
    
    if next_delim != -1:
        # We replace the whole slide block to be extremely compact
        new_slide = """## HOW: 6-Month Roadmap

<div class="roadmap-container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; font-size: 0.6em; line-height: 1.1;">

  <!-- Phase 1 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 4px;">
    <div class="roadmap-timeline" style="margin-bottom: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.8em; padding: 2px 6px;">Month 1 <span class="roadmap-gate" style="margin-left:4px;">G1</span></span>
    </div>
    <div class="roadmap-content" style="padding: 4px 6px;">
      <div class="roadmap-content-title" style="font-size: 0.8em; margin-bottom: 3px;">PHASE 1: PoC</div>
      <div class="roadmap-content-body" style="font-size: 0.9em; line-height: 1.2;">
        <strong>Goal:</strong> Find entry point & core flow.<br>
        • 10-15 design partners (JB Power Users)<br>
        • 3 quick prototypes (spec-first, review assist)<br>
        • Draft spec format v1 + 5-10 examples<br>
        <span style="color: #64ffda; font-weight: bold; font-size: 0.85em; display: inline-block; margin-top: 3px;">Gate:</span> Core flow chosen, repeated ≥2x/week.
      </div>
    </div>
  </div>

  <!-- Phase 2 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 4px;">
    <div class="roadmap-timeline" style="margin-bottom: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.8em; padding: 2px 6px;">Month 2</span>
    </div>
    <div class="roadmap-content" style="padding: 4px 6px;">
      <div class="roadmap-content-title" style="font-size: 0.8em; margin-bottom: 3px;">PHASE 2: MONETIZATION & OSS</div>
      <div class="roadmap-content-body" style="font-size: 0.9em; line-height: 1.2;">
        <strong>Goal:</strong> Secure commercial demand.<br>
        • Letters of Intent from 3+ companies<br>
        • Pilot scope defined (promised outcomes)<br>
        • JB Ecosystem packaging (AI bundle or extra)<br>
        <span style="color: var(--r-main-color); font-weight: bold; font-size: 0.85em; display: inline-block; margin-top: 3px;">OSS:</span> Format v1 + validator + examples.
      </div>
    </div>
  </div>

  <!-- Phase 3 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 4px;">
    <div class="roadmap-timeline" style="margin-bottom: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.8em; padding: 2px 6px;">Months 3-4 <span class="roadmap-gate" style="margin-left:4px;">G2</span></span>
    </div>
    <div class="roadmap-content" style="padding: 4px 6px;">
      <div class="roadmap-content-title" style="font-size: 0.8em; margin-bottom: 3px;">PHASE 3: SCALE</div>
      <div class="roadmap-content-body" style="font-size: 0.9em; line-height: 1.2;">
        <strong>Goal:</strong> IDE-plugin soft launch & paid pilots.<br>
        • Plugin MVP focused on the core scenario<br>
        • 1 high-signal quality check w/o noise<br>
        • 1 workflow integration (PR/Commits)<br>
        <span style="color: #64ffda; font-weight: bold; font-size: 0.85em; display: inline-block; margin-top: 3px;">Gate:</span> 5+ paying teams or revenue signal.
      </div>
    </div>
  </div>

  <!-- Phase 4 -->
  <div class="roadmap-item" style="margin-bottom: 0; padding: 4px;">
    <div class="roadmap-timeline" style="margin-bottom: 2px;">
      <span class="roadmap-timeline-label" style="font-size: 0.8em; padding: 2px 6px;">Months 5-6 <span class="roadmap-gate" style="margin-left:4px;">G3</span></span>
    </div>
    <div class="roadmap-content" style="padding: 4px 6px;">
      <div class="roadmap-content-title" style="font-size: 0.8em; margin-bottom: 3px;">PHASE 4: STANDARD</div>
      <div class="roadmap-content-body" style="font-size: 0.9em; line-height: 1.2;">
        <strong>Goal:</strong> Solidify approach & ecosystem effects.<br>
        • JB Marketplace listing (onboarding)<br>
        • Team features (shared templates, visibility)<br>
        • OSS Growth (first external contributors)<br>
        <span style="color: #64ffda; font-weight: bold; font-size: 0.85em; display: inline-block; margin-top: 3px;">Gate:</span> Self-serve works, multi-user orgs.
      </div>
    </div>
  </div>

</div>

"""
        content = content[:slide_start] + new_slide + content[next_delim:]

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
    f.write(content)

print("Done")
