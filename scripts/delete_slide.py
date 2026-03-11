import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# 1. Delete "WHY: JetBrains Strategic Fit" slide
start_str = '<!-- .slide: id="jb-strategic-fit" -->'
slide_start = content.find(start_str)

if slide_start != -1:
    # Find the previous --- to delete the delimiter too
    prev_delim = content.rfind('---\n', 0, slide_start)
    
    # Find the end of the slide, which is the next ---
    next_delim = content.find('---\n', slide_start)
    
    if prev_delim != -1 and next_delim != -1:
        # Delete from prev_delim to just before next_delim
        content = content[:prev_delim] + content[next_delim:]

# 2. Delete the "Metrics" tile
# Searching for the specific tile content to remove
tile_pattern = r'\s*<div class="chosen-tile chosen-tile--green">\s*<p class="chosen-tile-label">Metrics</p>\s*<p class="chosen-tile-body">NSM: Devs w/ ≥1 spec-linked merge/wk\. Key: New MRR \(paid tiers\) & Attributed MRR \(JB core via attach rate/retention\)\.</p>\s*</div>'

content = re.sub(tile_pattern, '', content)

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
    f.write(content)

print("Done")
