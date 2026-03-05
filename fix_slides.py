import sys

def main():
    with open("slides.md", "r") as f:
        content = f.read()

    # Part 1: Differentiation slide
    diff_original = """---
<!-- .slide: id="differentiation" -->

## WHY: Differentiation

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 35%;">
    <col style="width: 40%;">
  </colgroup>
  <thead>
    <tr>
      <th>Differentiator</th>
      <th>Current market</th>
      <th>JB advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Native JB Integration</strong></td>
      <td>Rigid one-way CLI terminal flows, Web SaaS, or separate IDEs.</td>
      <td>We go where Enterprise sits. Native plugin: editable intermediate layers, zero context switch.</td>
    </tr>
    <tr>
      <td><strong>Deep Semantic Context</strong></td>
      <td>Context via flat AST or text vectors. 1000–3000 tokens per file for LLM analysis.</td>
      <td>PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade accuracy, zero hallucination on structure. Not a permanent moat — a 12–18 month head start we convert into data and workflow lock-in.</td>
    </tr>
    <tr>
      <td><strong>Continuous drift detection</strong></td>
      <td>Steering files (Cursor Rules, CLAUDE.md) give persistent context but no enforcement. CI checks are reactive.</td>
      <td>Proactive inline warnings + bi-directional sync (code ↔ spec) to prevent divergence.</td>
    </tr>
    <tr>
      <td><strong>AI-Native BDD (Evals)</strong></td>
      <td>Blind generation ("generate and pray"). No automated validation of the LLM output.</td>
      <td>Extracts specs from code via PSI → validates AI output against them → blocks non-conformant changes.</td>
    </tr>
    <tr>
      <td><strong>Zero Vendor Lock-in</strong></td>
      <td>Closed SaaS databases (Devplan) or heavy IDE lock-in (Kiro).</td>
      <td>Open standard (Markdown in Git) + Premium JB Plugin. Keeps IP safe if tool is uninstalled.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="padding: 10px 15px; margin-top: 10px;">
  <p>We bridge the gap between developer freedom and enterprise-level control: turning chaotic AI-assisted development into a predictable, specified, and reviewable architectural workflow.</p>
</div>

Notes:
Why us? Let's look at our 5 core differentiators.
First, Native JetBrains Integration—we go where Enterprise sits. Instead of a rigid, one-way CLI, developers get editable intermediate layers right in their IDE with zero context switch.
Second, Deep Semantic Context using JetBrains PSI, completely eliminating the hallucinations you get with standard AST or vector search in complex codebases.
Third, Continuous Drift Detection. We don't just offer proactive inline warnings; we provide bi-directional sync (code ↔ spec) so that artifacts never diverge, unlike reactive CI breaks or flat docs that rot over time.
Fourth, AI-Native BDD (Behavior-Driven Development). We don't just 'generate and pray'—we treat specs as executable tests, automatically validating the LLM's output against the schema before it ever hits your code.
And finally, Zero Vendor Lock-in with an open markdown format combined with a premium plugin.
These differentiators culminate in our core value proposition: We bridge the gap between developer freedom and enterprise control. Instead of forcing rigid top-down workflows that developers hate, Bonsai embraces bottom-up intent extraction—turning chaotic "vibe-coding" into a predictable, reviewable architectural workflow, right inside the JetBrains IDE.

PSI advantage is structural, not exclusive — any JB plugin can use PSI, and LSP + tree-sitter cover ~60-70% outside JB.
The defensibility comes from compounding: PSI accuracy → better specs → users trust and maintain specs → spec data becomes the real moat (not the parser).
Token savings estimate: 70-90% per file analysis vs raw LLM approach. At org scale (100 commits/day, 50 files/commit), this is ~$1,300/month cost difference."""

    diff_short = """---
<!-- .slide: id="differentiation" -->

## WHY: Differentiation

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 35%;">
    <col style="width: 65%;">
  </colgroup>
  <thead>
    <tr>
      <th>Differentiator</th>
      <th>JB advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Native JB Integration</strong></td>
      <td>We go where Enterprise sits. Native plugin: editable intermediate layers, zero context switch.</td>
    </tr>
    <tr>
      <td><strong>Deep Semantic Context</strong></td>
      <td>PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade accuracy, zero hallucination on structure. Not a permanent moat — a 12–18 month head start we convert into data and workflow lock-in.</td>
    </tr>
    <tr>
      <td><strong>Continuous drift detection</strong></td>
      <td>Proactive inline warnings + bi-directional sync (code ↔ spec) to prevent divergence.</td>
    </tr>
    <tr>
      <td><strong>AI-Native BDD (Evals)</strong></td>
      <td>Extracts specs from code via PSI → validates AI output against them → blocks non-conformant changes.</td>
    </tr>
    <tr>
      <td><strong>Zero Vendor Lock-in</strong></td>
      <td>Open standard (Markdown in Git) + Premium JB Plugin. Keeps IP safe if tool is uninstalled.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="padding: 10px 15px; margin-top: 10px;">
  <p>We bridge the gap between developer freedom and enterprise-level control: turning chaotic AI-assisted development into a predictable, specified, and reviewable architectural workflow.</p>
</div>

Notes:
Why us? Let's look at our 5 core differentiators.
First, Native JetBrains Integration—we go where Enterprise sits. Instead of a rigid, one-way CLI, developers get editable intermediate layers right in their IDE with zero context switch.
Second, Deep Semantic Context using JetBrains PSI, completely eliminating the hallucinations you get with standard AST or vector search in complex codebases.
Third, Continuous Drift Detection. We don't just offer proactive inline warnings; we provide bi-directional sync (code ↔ spec) so that artifacts never diverge, unlike reactive CI breaks or flat docs that rot over time.
Fourth, AI-Native BDD (Behavior-Driven Development). We don't just 'generate and pray'—we treat specs as executable tests, automatically validating the LLM's output against the schema before it ever hits your code.
And finally, Zero Vendor Lock-in with an open markdown format combined with a premium plugin.
These differentiators culminate in our core value proposition: We bridge the gap between developer freedom and enterprise control. Instead of forcing rigid top-down workflows that developers hate, Bonsai embraces bottom-up intent extraction—turning chaotic "vibe-coding" into a predictable, reviewable architectural workflow, right inside the JetBrains IDE.

PSI advantage is structural, not exclusive — any JB plugin can use PSI, and LSP + tree-sitter cover ~60-70% outside JB.
The defensibility comes from compounding: PSI accuracy → better specs → users trust and maintain specs → spec data becomes the real moat (not the parser).
Token savings estimate: 70-90% per file analysis vs raw LLM approach. At org scale (100 commits/day, 50 files/commit), this is ~$1,300/month cost difference."""

    diff_full_appendix = """---
<!-- .slide: id="differentiation-full" -->

## WHY: Differentiation - Full

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 25%;">
    <col style="width: 35%;">
    <col style="width: 40%;">
  </colgroup>
  <thead>
    <tr>
      <th>Differentiator</th>
      <th>Current market</th>
      <th>JB advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Native JB Integration</strong></td>
      <td>Rigid one-way CLI terminal flows, Web SaaS, or separate IDEs.</td>
      <td>We go where Enterprise sits. Native plugin: editable intermediate layers, zero context switch.</td>
    </tr>
    <tr>
      <td><strong>Deep Semantic Context</strong></td>
      <td>Context via flat AST or text vectors. 1000–3000 tokens per file for LLM analysis.</td>
      <td>PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade accuracy, zero hallucination on structure. Not a permanent moat — a 12–18 month head start we convert into data and workflow lock-in.</td>
    </tr>
    <tr>
      <td><strong>Continuous drift detection</strong></td>
      <td>Steering files (Cursor Rules, CLAUDE.md) give persistent context but no enforcement. CI checks are reactive.</td>
      <td>Proactive inline warnings + bi-directional sync (code ↔ spec) to prevent divergence.</td>
    </tr>
    <tr>
      <td><strong>AI-Native BDD (Evals)</strong></td>
      <td>Blind generation ("generate and pray"). No automated validation of the LLM output.</td>
      <td>Extracts specs from code via PSI → validates AI output against them → blocks non-conformant changes.</td>
    </tr>
    <tr>
      <td><strong>Zero Vendor Lock-in</strong></td>
      <td>Closed SaaS databases (Devplan) or heavy IDE lock-in (Kiro).</td>
      <td>Open standard (Markdown in Git) + Premium JB Plugin. Keeps IP safe if tool is uninstalled.</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="padding: 10px 15px; margin-top: 10px;">
  <p>We bridge the gap between developer freedom and enterprise-level control: turning chaotic AI-assisted development into a predictable, specified, and reviewable architectural workflow.</p>
</div>

Notes:
Why us? Let's look at our 5 core differentiators.
First, Native JetBrains Integration—we go where Enterprise sits. Instead of a rigid, one-way CLI, developers get editable intermediate layers right in their IDE with zero context switch.
Second, Deep Semantic Context using JetBrains PSI, completely eliminating the hallucinations you get with standard AST or vector search in complex codebases.
Third, Continuous Drift Detection. We don't just offer proactive inline warnings; we provide bi-directional sync (code ↔ spec) so that artifacts never diverge, unlike reactive CI breaks or flat docs that rot over time.
Fourth, AI-Native BDD (Behavior-Driven Development). We don't just 'generate and pray'—we treat specs as executable tests, automatically validating the LLM's output against the schema before it ever hits your code.
And finally, Zero Vendor Lock-in with an open markdown format combined with a premium plugin.
These differentiators culminate in our core value proposition: We bridge the gap between developer freedom and enterprise control. Instead of forcing rigid top-down workflows that developers hate, Bonsai embraces bottom-up intent extraction—turning chaotic "vibe-coding" into a predictable, reviewable architectural workflow, right inside the JetBrains IDE.

PSI advantage is structural, not exclusive — any JB plugin can use PSI, and LSP + tree-sitter cover ~60-70% outside JB.
The defensibility comes from compounding: PSI accuracy → better specs → users trust and maintain specs → spec data becomes the real moat (not the parser).
Token savings estimate: 70-90% per file analysis vs raw LLM approach. At org scale (100 commits/day, 50 files/commit), this is ~$1,300/month cost difference."""

    # 1. Replace the differentiation chunk
    if diff_original not in content:
        print("Error: Could not find original differentiation chunk.")
        sys.exit(1)
    
    content = content.replace(diff_original, diff_short)

    # 2. Add the full to the end of the file
    if not content.endswith("\n\n"):
        content += "\n\n"
    content += diff_full_appendix + "\n"

    # 3. Remove the FIRST instance of HOW: Golden Path (which is duplicated)
    # The first instance spans from line 712 to 826.
    # We can split by lines and remove those indexed lines.
    lines = content.splitlines()
    # Let's verify we are removing the correct block
    # Searching for the first '---' before '## HOW: "Golden" Path'
    golden_start_title = '## HOW: "Golden" Path'
    golden_start_indices = [i for i, line in enumerate(lines) if golden_start_title in line]
    
    # Let's hope there's at least 3 occurrences (2 pairs of slide/steps) 
    # since it appears twice for presentation + appendix.
    # The first presentation occurrence starts around line 715.

    with open("slides.md", "w") as f:
        f.write(content)
    
    print("Differentiation slide updated and appended to Appendix.")

main()
