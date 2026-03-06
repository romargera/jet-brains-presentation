import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# Delete "WHY: Differentiation - Full" slide
start_str = '<!-- .slide: id="differentiation-full" -->'
slide_start = content.find(start_str)

if slide_start != -1:
    prev_delim = content.rfind('---\n', 0, slide_start)
    next_delim = content.find('---\n', slide_start)

    if prev_delim != -1 and next_delim != -1:
        # Delete from prev_delim to just before next_delim
        content = content[:prev_delim] + content[next_delim:]


with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'w') as f:
    f.write(content)

print("Done")
