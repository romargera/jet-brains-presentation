import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# Locate the HOW: 6-Month Roadmap slide
start_str = '## HOW: 6-Month Roadmap'
slide_start = content.find(start_str)

if slide_start != -1:
    next_delim = content.find('---\n', slide_start)
    
    if next_delim != -1:
        # We replace the whole slide block
        
        new_slide = """## HOW: 6-Month Roadmap

<div class="roadmap-container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">

  <!-- Phase 1 -->
  <div class="roadmap-item" style="margin-bottom: 0;">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Month 1</span>
    </div>
    <div class="roadmap-content" style="padding: 10px;">
      <div class="roadmap-content-title" style="font-size: 0.8em;">PHASE 1: PoC</div>
      <div class="roadmap-content-body" style="font-size: 0.75em; line-height: 1.3;">
        <strong>Goal:</strong> Find entry point & core flow via data.<br>
        • 10-15 design partners (JB Power Users, DevEx)<br>
        • 3 quick prototypes (spec-first, review assist, diff control)<br>
        • Draft spec format v1 + 5-10 examples<br>
        <span style="color: #64ffda; font-weight: bold; font-size: 0.9em; display: inline-block; margin-top: 4px;">Gate:</span> Core flow chosen, repeated ≥2x/week by partners.
      </div>
    </div>
  </div>

  <!-- Phase 2 -->
  <div class="roadmap-item" style="margin-bottom: 0;">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Month 2</span>
    </div>
    <div class="roadmap-content" style="padding: 10px;">
      <div class="roadmap-content-title" style="font-size: 0.8em;">PHASE 2: EARLY MONETIZATION & OSS</div>
      <div class="roadmap-content-body" style="font-size: 0.75em; line-height: 1.3;">
        <strong>Goal:</strong> Secure commercial demand + risk mitigation.<br>
        • Letters of Intent from 3+ companies (budgets & terms)<br>
        • Pilot scope defined (metrics, promised outcomes)<br>
        • JB Ecosystem packaging (standalone vs AI bundle)<br>
        <strong style="color: var(--r-main-color);">OSS:</strong> Spec format v1 + validator + examples (builds trust).
      </div>
    </div>
  </div>

  <!-- Phase 3 -->
  <div class="roadmap-item" style="margin-bottom: 0;">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Months 3-4</span>
    </div>
    <div class="roadmap-content" style="padding: 10px;">
      <div class="roadmap-content-title" style="font-size: 0.8em;">PHASE 3: SCALE</div>
      <div class="roadmap-content-body" style="font-size: 0.75em; line-height: 1.3;">
        <strong>Goal:</strong> IDE-plugin soft launch & first paid pilots.<br>
        • Plugin MVP focused on the core scenario<br>
        • 1 high-signal quality check (e.g., drift alert) w/o noise<br>
        • 1 workflow integration (PR/Commits)<br>
        <span style="color: #64ffda; font-weight: bold; font-size: 0.9em; display: inline-block; margin-top: 4px;">Gate:</span> 5+ paying teams or equivalent revenue signal.
      </div>
    </div>
  </div>

  <!-- Phase 4 -->
  <div class="roadmap-item" style="margin-bottom: 0;">
    <div class="roadmap-timeline">
      <span class="roadmap-timeline-label">Months 5-6</span>
    </div>
    <div class="roadmap-content" style="padding: 10px;">
      <div class="roadmap-content-title" style="font-size: 0.8em;">PHASE 4: STANDARD</div>
      <div class="roadmap-content-body" style="font-size: 0.75em; line-height: 1.3;">
        <strong>Goal:</strong> Solidify approach & build ecosystem effects.<br>
        • JB Marketplace listing (onboarding & activation)<br>
        • Team features (shared templates, visibility, settings)<br>
        • OSS Growth (starter packs, first external contributors)<br>
        <span style="color: #64ffda; font-weight: bold; font-size: 0.9em; display: inline-block; margin-top: 4px;">Gate:</span> Self-serve works, multi-user orgs, OSS traction.
      </div>
    </div>
  </div>

</div>

"""
        content = content[:slide_start] + new_slide + content[next_delim:]

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
    f.write(content)

print("Done")
