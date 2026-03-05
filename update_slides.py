import re

with open("slides.md", "r") as f:
    content = f.read()

# The sentence to move around
sentence = 'Directions are derived from the top issues across three evidence layers: <a href="#/distrust-issues">Distrust</a>, <a href="#/time-spend">Time Spent</a>, and <a href="#/b2b-pains">B2B Issues</a>.'
para_sentence = '<p style="font-size: 0.45em; color: var(--text-muted); margin: 0 0 8px; line-height: 1.4;">' + sentence + '</p>'
bullet_sentence = '<li>' + sentence + '</li>'

# Task 1: Add it over the JTBD tile on the WHAT: ICP, JTBD, Triggers slide
target_slide_1 = """## WHAT: ICP, JTBD, Triggers

<div class="chosen-grid chosen-grid--small">"""

replace_slide_1 = f"""## WHAT: ICP, JTBD, Triggers

{para_sentence}

<div class="chosen-grid chosen-grid--small">"""

if target_slide_1 in content:
    content = content.replace(target_slide_1, replace_slide_1)
else:
    print("Cannot find slide 1 target")

# Task 2: Create a NEW slide "HOW: Segmentation" with the two tiles "Early Adopters" and "Scaling"
segmentation_content = """---
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
"""

target_insert_segmentation = """When they are pushed by an upcoming compliance audit or a sudden drop in code quality across teams, they need a standardized, auditable way to manage AI-assisted development across the organization.

---"""

if target_insert_segmentation in content:
    content = content.replace(target_insert_segmentation, target_insert_segmentation + "\n" + segmentation_content.replace("---", "").strip() + "\n\n---")
else:
    print("Cannot find location to insert segmentation slide")

# Task 3: Remove the paragraph from Strategic Directions
target_slide_3_header = """## WHY: Strategic Directions

""" + para_sentence + "\n\n"

replace_slide_3_header = """## WHY: Strategic Directions

"""
if target_slide_3_header in content:
    content = content.replace(target_slide_3_header, replace_slide_3_header)
else:
    print("Cannot find slide 3 header to replace")

# Find the distrust-notes specifically under Strategic Directions slide to append the bullet
# We can search for the start of the Strategic Directions slide down to the end of its notes
start_idx = content.find("## WHY: Strategic Directions")
end_idx = content.find("<!-- .slide: id=", start_idx)

if start_idx != -1 and end_idx != -1:
    subcontent = content[start_idx:end_idx]
    
    ul_target = """<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>"""
    ul_replace = f"""<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
{bullet_sentence}
</ul>"""
    if ul_target in subcontent:
        new_subcontent = subcontent.replace(ul_target, ul_replace)
        content = content[:start_idx] + new_subcontent + content[end_idx:]
    else:
        print("Cannot find ul_target in subcontent")
else:
    print("Cannot find Strategic Directions boundaries")

with open("slides.md", "w") as f:
    f.write(content)
print("done")
