import re

file_path = '/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md'
with open(file_path, 'r') as f:
    content = f.read()

start_str = '## HOW: 6-Month Roadmap'
slide_start = content.find(start_str)

if slide_start != -1:
    next_delim = content.find('\n---\n', slide_start)
    if next_delim == -1:
        next_delim = len(content)
        
    new_slide = """## HOW: 6-Month Roadmap

<div class="roadmap-container" style="display: flex !important; flex-direction: column !important; gap: 8px !important; font-size: 0.52em !important; line-height: 1.2 !important; width: 100% !important;">

  <!-- Phase 1 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Month 1</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 1: PoC</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;">Select core flow with 10–15 partners via fast prototyping (spec-first, review assist). Author spec format v1 draft. <span style="color: #64ffda; font-weight: bold; margin-left: 8px;">Gate:</span> Core flow validated via repeat use.</p>
    </div>
  </div>

  <!-- Phase 2 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Month 2</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 2: Mon. & OSS</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;">Gather budget intent (LOIs) from 3+ companies with pilot metrics. Package for JB Ecosystem. <span style="color: var(--r-main-color); font-weight: bold; margin-left:8px;">OSS:</span> Broaden funnel with format v1 & validator.</p>
    </div>
  </div>

  <!-- Phase 3 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Months 3-4</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 3: Scale</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;">Launch IDE-plugin MVP with high-signal quality checks and workflow integration. Run first paid pilots. <span style="color: #64ffda; font-weight: bold; margin-left: 8px;">Gate:</span> 5+ paying teams or revenue signal.</p>
    </div>
  </div>

  <!-- Phase 4 -->
  <div class="roadmap-item" style="display: flex !important; flex-direction: row !important; align-items: flex-start !important; gap: 12px !important; padding: 6px !important; margin: 0 !important; width: 100% !important; background: rgba(255,255,255,0.03); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
    <div class="roadmap-timeline" style="flex: 0 0 100px !important; display: flex !important; flex-direction: column !important; align-items: flex-start !important; gap: 1px !important;">
      <span class="roadmap-timeline-label" style="font-size: 0.85em !important; padding: 1px 6px !important; background: var(--jb-purple); color: white; border-radius: 4px;">Months 5-6</span>
      <span style="font-size: 0.7em !important; font-weight: bold !important; color: rgba(255,255,255,0.6) !important; text-transform: uppercase !important;">Phase 4: Standard</span>
    </div>
    <div class="roadmap-content" style="flex: 1 !important; padding: 0 !important; text-align: left !important;">
      <p style="margin: 0 !important; display: block !important;">Publish to JB Marketplace with team-ready features (shared templates, visibility). Drive open-source growth. <span style="color: #64ffda; font-weight: bold; margin-left: 8px;">Gate:</span> Self-serve works across multi-user orgs.</p>
    </div>
  </div>

</div>
"""
    content = content[:slide_start] + new_slide + content[next_delim:]
    with open(file_path, 'w') as f:
        f.write(content)

print("Roadmap refactored with !important to override CSS classes.")
