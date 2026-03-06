import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# Make the competitor layout more balanced by adjusting the gap and font sizes
old_layout_start = '<div class="competitor-layout">'
new_layout_start = '<div class="competitor-layout" style="display: flex; gap: 15px; align-items: stretch; justify-content: space-between;">'
content = content.replace(old_layout_start, new_layout_start)

# Adjust left column width and styling to match right column better
old_left = '<div class="competitor-col-left" style="font-size: 0.28em;">'
new_left = '<div class="competitor-col-left" style="font-size: 0.28em; flex: 1;">'
content = content.replace(old_left, new_left)

# Adjust right column width and styling
old_right = '<div class="competitor-col-right" style="font-size: 0.28em;">'
new_right = '<div class="competitor-col-right" style="font-size: 0.28em; flex: 1;">'
content = content.replace(old_right, new_right)

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
    f.write(content)

print("Done")
