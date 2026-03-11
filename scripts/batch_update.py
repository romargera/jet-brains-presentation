import re

file_path = '/Users/roman/Documents/Pet Projects/jet_brains_presentation/slides.md'
with open(file_path, 'r') as f:
    content = f.read()

# 1. HOW: Risks & Mitigation
old1_a = 'Phase 1 dual-track: (a) test spec extraction value with 10 partners, (b) parallel test of 2 alternative approaches (review assist, security gates) via lightweight prototypes. Gate 1 includes comparative signal.'
new1_a = 'Phase 1: 3 parallel PoCs with instrumented prototype: (1) spec-first control, (2) review help, (3) diff control (change containment). Gate 1 based on repeat usage (2x/week) and signal vs alternatives. If we can’t recruit named partners fast, use narrow OSS (Spec Format + validator + examples) to widen the funnel and reduce distrust.'
content = content.replace(old1_a, new1_a)

old1_b = 'If Phase 1 shows <40% spec engagement AND alternative approaches score higher in partner feedback, we pivot before Phase 2.'
new1_b = 'If Phase 1 shows weak repeat usage (most partners don’t repeat the core scenario 2x in 7 days) and alternatives win on measured outcomes, we switch entry point before building the plugin MVP.'
content = content.replace(old1_b, new1_b)


# 2. HOW: GTM Strategy
old2_a = '<li><strong>Offer:</strong> Paid Design Partners, early Team packs.</li>'
new2_a = '<li><strong>Offer:</strong> Written budget intent + pilot agreement (scope, success metrics, buyer, procurement path).</li>\n      <li><strong>When we charge:</strong> paid pilots start once plugin MVP exists (Mo 3-4).</li>'
content = content.replace(old2_a, new2_a)

old2_b = '2) **Monetization**: We charge early to validate willingness to pay. Using JB AI credits makes purchasing familiar.'
new2_b = '2) **Monetization**: Early monetization starts as budget intent and pilot agreements. Charging starts when plugin MVP is usable.'
content = content.replace(old2_b, new2_b)

old2_c = '<li><strong>OSS Core:</strong> Spec Format v1, CLI, Validator.</li>'
new2_c = '<li><strong>OSS (risk mitigation first):</strong> Spec Format + validator + examples to widen partner funnel and reduce distrust.<br><strong>OSS (later growth):</strong> templates/hooks starter pack and compatibility assets.</li>'
content = content.replace(old2_c, new2_c)

old2_d = '<li><strong>Goal:</strong> Validate spec extraction & diff control.</li>'
new2_d = '<li><strong>Goal:</strong> Validate spec-first + diff control (change containment) via instrumented prototype, before plugin MVP.</li>'
content = content.replace(old2_d, new2_d)


# 3. WHAT & WHY: Summary
old3 = 'Bi-directional spec↔code in IDE via PSI. We extract specs from code (zero friction), push to CI, and locally detect drift.'
new3 = 'Bi-directional spec↔code in IDE via PSI: extract specs (zero friction), contain changes in diff (change containment), and detect drift early.'
content = content.replace(old3, new3)


# 4. WHY: Niche Choice
old4_a = '<td><strong>IDE-Native Control (Wedge)</strong></td>'
new4_a = '<td><strong>IDE-Native Control (Entry Point)</strong></td>'
content = content.replace(old4_a, new4_a)

old4_b = '<td>Zero context switch. Uncontested for structured spec control (steering files ≠ enforceable specs). Massive JB distribution moat.</td>'
new4_b = '<td>Zero context switch. Start with spec-first + diff control (change containment) inside JB IDE. Massive JB distribution moat.</td>'
content = content.replace(old4_b, new4_b)


# 5. HOW: MVP SOLUTION DRAFT
old5 = 'Canary rollout: 10 design partners → Private alpha.'
new5 = 'Month 1: instrumented prototype with design partners (no plugin MVP yet). Months 3-4: private alpha plugin MVP.'
content = content.replace(old5, new5)


# 6. Validation Experiments
old6_a = '<li><strong>WTP Test (Mo 2):</strong> 5 partners at $10/mo vs free trial.</li>'
new6_a = '<li><strong>Commercial intent test (Mo 2):</strong> written budget intent + pilot agreement terms vs extended free access.</li>'
content = content.replace(old6_a, new6_a)

content = content.replace('1. WTP test (Month 2): Offer 5 design partners «Pro for $10/month» — measure conversion vs «Pro for free extended trial». If <30% convert at $10, test $5.', '1. Commercial intent test (Mo 2): Test budget intent and pilot terms vs free trial. Charging starts with paid pilots once plugin MVP exists (Mo 3-4).')

# 7. HOW: Pricing & Monetization
old7_a = '<td>Prove WTP, convert power users</td>'
new7_a = '<td>Validate repeat usage and upgrade intent (after MVP exists)</td>'
content = content.replace(old7_a, new7_a)

old7_b = '<th style="width: 6%;">Price</th>'
new7_b = '<th style="width: 6%;">Packaging</th>'
content = content.replace(old7_b, new7_b)

old7_c = '1) **B2B Transition**: Start individual, hook teams via shared sync, flip to Enterprise via SCIM/Audit.'
new7_c = '1) **B2B Transition**: Start individual, hook teams via shared sync, flip to Enterprise via SCIM/Audit.\nEarly monetization in Mo 2 is budget intent, not paid subscription.'
content = content.replace(old7_c, new7_c)

with open(file_path, 'w') as f:
    f.write(content)

print("Batch updates completed successfully.")
