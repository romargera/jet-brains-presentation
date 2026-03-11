import re

with open('/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md', 'r') as f:
    content = f.read()

# 1. Update Assumptions line
old_line = '<li>Assumptions <span class="metric-badge">A</span> for TAM/SAM/SOM are indicated in the linked calculations.</li>'
new_line = '<li>Assumptions <span class="metric-badge">A</span> for TAM/SAM/SOM and bottom up are indicated in the linked calculations <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=856599423#gid=856599423&range=A1" target="_blank">[1]</a><a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=A1" target="_blank">[2]</a>.</li>'

content = content.replace(old_line, new_line)

# 2. Delete the direct Competitor Landscape slide
start_str = '<!-- .slide: id="competitor-landscape" -->'
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
