import sys

def main():
    with open("slides.md", "r") as f:
        lines = f.readlines()
    
    start_idx = -1
    end_idx = -1
    
    for i, line in enumerate(lines):
        if '<!-- .slide: id="golden-path" -->' in line:
            start_idx = i - 1 # Include the '---' before it
            break
            
    if start_idx == -1:
        print("Could not find start index")
        sys.exit(1)
        
    for i in range(start_idx + 1, len(lines)):
        if '<!-- .slide: id="pricing-monetization" -->' in lines[i]:
            end_idx = i - 1 # Include up to the line before '---'
            break
            
    if end_idx == -1:
        print("Could not find end index")
        sys.exit(1)
        
    print(f"Removing from line {start_idx} to {end_idx - 1} inclusive.")
    
    new_lines = lines[:start_idx] + lines[end_idx:]
    with open("slides.md", "w") as f:
        f.writelines(new_lines)
        
main()
