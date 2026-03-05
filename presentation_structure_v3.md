# Bonsai — Presentation Structure v3 (15–20 min)

> This document reflects the actual content of existing slides and proposes new slides based on competitor analysis.
> Prefix convention: WHAT = facts & evidence, WHY = strategic reasoning, HOW = execution plan.
> Naming can be revisited later.

---

## WHAT (Problem, ICP, Direction) — DONE

### Slide 1 — Title ✅

**Bonsai: Predictable AI-assisted Development via Spec-driven Control**
Roman Babunts · March 2026

### Slide 2 — Presentation Structure ✅

- WHAT: Problem + direction
- WHY: Market + strategy + opportunity
- HOW: MVP + validation + GTM + risks

### Slide 3 — The AI Adoption Paradox ✅

- 90% adoption (+14% YoY, DORA 2025)
- But: 46% distrust AI output (+15 pp YoY), 20% unfavorable sentiment (+14 pp YoY)
- Takeaway: developers adopt AI for speed — but lose trust when output is unpredictable

### Slide 4 — Distrust Issues ✅

- Table: Trust points when utilizing AI, scored by Reach × Freq × Confidence
- Top: Skepticism (9), Review/Debug time (9), Security (7)
- Takeaway: developers don't trust AI code enough to ship without extra polishing

### Slide 5 — Dev Time Spent ✅

- Table: Actual vs Ideal time allocation (Microsoft Time-Warp Study)
- Biggest overhead: Security/Compliance (8.4% gap), Communication (6.4%), Debugging (3.7%)
- Biggest deficit: Coding (-11.2%), Architecture (-6.5%)
- Takeaway: cut low-value overhead → reinvest into coding & architecture

### Slide 6 — B2B Pains ✅

- Table: B2B pain points scored by Reach × Freq × Confidence
- Top: Delivery predictability (5), Quality & reliability risk (5)
- Takeaway: top B2B pains amplified by uncontrolled AI code in review pipelines

### Slide 7 — Strategic Directions ✅

- Table: Directions scored by (Impact × Conf) / Effort
- Top: AI-dev transparency (2.5) — sits at intersection of all three pain layers
- Takeaway: AI-dev transparency is the top-priority direction

### Slide 8 — Chosen Direction ✅

- Direction: AI-dev transparency layer for code & architecture
- Problem summary: adoption 90% but distrust +15 pp, 45% debug time increase
- Core JTBD: "When engineers build with AI in production, they want development to be predictable and controllable, so they can ship faster with confidence"

---

## WHAT (Market, Approaches, Competitors) — PARTIALLY DONE

### Slide 9 — Approaches ✅

- Table: 8 competitive approaches ranked by weighted ICE Score
- Top: Spec-driven development (3.3), Observability + evals (3.0)
- Includes: quality gates, security guardrails, AI code reviewer, task orchestration, deterministic LLM, human-freelancer
- Takeaway: Spec-driven development is the top-priority approach

### Slide 10 — Competitor Landscape ✅

- Two-column layout: Direct competitors table (Tier 1 + Tier 2) + Indirect competitors cards
- Tier 1 (5): Spec Kit, Kiro, BMAD, OpenSpec, CodeSpeak
- Tier 2 (7): Taskmaster, Stately, Agent-OS, Autospec, specs.md, autok, devplan
- Indirect: IDE AI Assistants (Cursor, Copilot, JB AI), AI Code Reviewers (CodeRabbit, Qodo), Observability (LangSmith, Datadog)

---

### Slide 11 — Learn & Steal (NEW)

**Title:** WHAT: Key Patterns from Competitors
**Format:** Table of strategic patterns (NOT per-competitor features)

| Pattern | Evidence | Who validated |
|---------|----------|---------------|
| **Spec = markdown in Git** — specs live next to code, versioned, reviewable | Standard across all leaders; maximizes adoption in dev workflows | SpecKit (73.6k★), BMAD (39k★), OpenSpec (27k★), CodeSpeak |
| **Bi-directional spec↔code** — changes in spec update code; changes in code update spec | Core differentiator of compiler-approach tools; matches task assignment ("bi-directionally propagate") | CodeSpeak (spec diff → code diff), Auto-K (graph sync), Devplan (context graph) |
| **IDE-native > Web-first** — tools that live inside IDE win adoption over browser-based platforms | Web-first tools (Devplan SaaS in browser) create context switch penalty; IDE-native tools have lower adoption friction | Kiro (dedicated IDE), OpenSpec (REPL-like), vs Devplan (browser-only) |
| **Compiler-like tight integration** — spec compiles directly to production code + tests | CodeSpeak shows 5-10x code shrink factor; spec becomes single source of truth instead of separate doc | CodeSpeak (alpha): proven case studies with beautifulsoup4, yt-dlp, Faker |
| **Slash-commands as UX pattern** — `/command` interface for spec operations | Low friction entry point; users interact in natural terminal/chat flow without learning new GUI | SpecKit (/spec, /plan), OpenSpec (/opsx:propose), BMAD (/bmad-help), Taskmaster (MCP tools) |
| **Adaptive depth by task scale** — framework adjusts planning rigor automatically | One-size-fits-all = friction; from hotfix to epic, tool must match context | BMAD ("scale-domain-adaptive"), specs.md (3 flows: Simple/FIRE/AI-DLC), Kiro (steering) |
| **Community & OSS drive adoption** — open-source tools dominate traction | All Tier 1 leaders by stars are OSS. Closed tools (CodeSpeak, Auto-K, Devplan) lag in community traction | SpecKit (73k★), BMAD (39k★), OpenSpec (27k★), Taskmaster (26k★) — all MIT |
| **Spec-delta: review intent, not just code** — show WHY code changed, not just WHAT | Reduces review cognitive load; addresses top distrust issue (review time) | OpenSpec (spec-delta concept), CodeSpeak (spec diff → code diff) |
| **Knowledge graph > flat docs for drift detection** — structured graph detects inconsistencies between specs, code, tasks | Flat markdown rots silently; graph can flag conflicts automatically | Auto-K (bi-directional sync, drift), Devplan (context graph from repos + trackers) |
| **Persistent context rules (steering)** — project-specific rules that persist across AI sessions | Without persistent rules, every AI session starts from scratch; quality degrades on long projects | Kiro (steering files), Agent-OS (standards extraction), BMAD (project constitution) |

**Assumption:** For developers, web-first is a disadvantage because it creates context switch out of IDE into browser.

**Takeaway:** Successful tools share these patterns. The gap: none of them combine IDE-native experience + compiler-level spec↔code integration + drift detection in one product.

---

### Slide 12 — Niche Choice (NEW)

**Title:** WHAT: Market Niches & Positioning
**Format:** Table of niches with type / effort / who's there / JB fit

Niches should be formulated as **positioning statements** (not just feature names):

| # | Positioning / Niche | Type | Effort | Who's there | Notes |
|---|---|---|---|---|---|
| ① | **IDE-native spec control** — specs live in IDE: navigation, inspections, drift warnings inline | 🍎 Low-hanging | Low | Nobody has native JB plugin. Kiro = separate IDE. All others = CLI/VS Code | Strongest distribution advantage for JB |
| ② | **Spec compiler** — spec compiles to code + tests, bi-directional, shrink factor 5-10x | 🚀 Moonshot | High | CodeSpeak (alpha, closed, no public repo) | Unique value prop. Highest differentiation |
| ③ | **Knowledge graph + drift detection** — structured graph of specs/code/tasks, flag inconsistencies | 🌙 Mid-term | Med | Auto-K (waitlist), Devplan ($24-49/mo, pre-revenue) | Addresses "docs rot" problem |
| ④ | **End-to-end agent orchestration** — PRD→tasks→agents→code→PR in managed pipeline | 🌙 Mid-term | Med | Taskmaster (26k★, MIT+Commons Clause), Vibe Kanban | Needs mature agent ecosystem |
| ⑤ | **AI pipeline observability** — trace agent steps, eval quality, debug regressions | 🍎 Low-hanging | Med | LangSmith, Datadog LLM, W&B Weave — established players | Red ocean. Low JB differentiation |
| ⑥ | **Multi-repo spec management** — specs across multiple repos, consistent context | 🌙 Mid-term | Med | Nobody does this yet | Unique gap. Relevant for enterprise |
| ⑦ | **Community spec marketplace** — shared spec templates, reusable patterns, OSS ecosystem | 🍎 Low-hanging | Low | BMAD has modules ecosystem, but no marketplace | Network effect moat |
| ⑧ | **Deterministic LLM validation** — schema-based validation, retry on mismatch | 🔧 Utility | Low | PydanticAI, Instructor, Outlines — commoditized | Low differentiation, library-level |

**Cost landscape** (from competitor data):

- **Free/OSS**: SpecKit, BMAD, OpenSpec, Taskmaster, Agent-OS, Autospec, specs.md — all MIT
- **Waitlist/pre-revenue**: Kiro (free, Amazon-backed), Auto-K (free beta), CodeSpeak (alpha, free)
- **Paid SaaS**: Devplan ($24/mo Builder, $49/mo Team, Enterprise custom)
- **Hybrid** (OSS core + paid premium): Nobody does this yet in this category → opportunity

**Takeaway:** Recommend focus on niche ① (IDE-native) as wedge, with ② (compiler) as mid-term differentiator and ③ (drift detection) as expansion. Niches ⑥ (multi-repo) and ⑦ (marketplace) are strategic moats for later phases.

---

### Slide 13 — Why Now (NEW)

**Title:** WHAT: Why Now
**Format:** 4 tiles or key points

| Signal | Evidence |
|--------|----------|
| **Trust is collapsing at scale** | AI adoption 90% but distrust surged +15 pp YoY (SO 2025). Window for trust-layer tools is NOW — before the market normalizes on "good enough" |
| **Category validated by Big Tech** | Amazon launched Kiro (dedicated IDE). GitHub released SpecKit (73k★ in months). Signals: spec-driven dev is real, not niche |
| **No dominant winner** | 12+ players, all pre-revenue or early-stage. Fragmented approaches, no standard methodology, no market leader. First-mover with distribution wins |
| **Uncontested territory: JetBrains IDE** | Zero competitors have native JB plugin. 35M+ IDE users = built-in distribution. IntelliJ SDK = barrier to entry for startups |

**Timing logic:** AI adoption creates the pain (high usage → more broken code → more distrust). The market response (spec-driven tools) is forming right now. Big Tech validation (Amazon + GitHub) confirms the category direction. But none of the tools serve JB ecosystem natively. The window to claim this position is 6-12 months before a competitor builds a JB plugin.

---

### Slide 14 — Differentiation (NEW)

**Title:** WHAT: Why Us (Differentiation)
**Format:** Table or visual comparison

| Differentiator | Current market | Bonsai advantage |
|---|---|---|
| **IDE-native experience** | All competitors: CLI, VS Code extensions, or separate IDE (Kiro) | Native JB plugin: gutter icons, inspections, quick-fixes, intentions, tool windows. No context switch |
| **Spec ↔ Code real-time navigation** | CodeSpeak does batch spec→code. No one does real-time IDE navigation | Click spec → jump to code. Click code → see governing spec. Like "Go to Definition" but for intent |
| **Continuous drift detection** | Auto-K promises but in waitlist. No one delivers live drift warnings in IDE | Inline warnings when code diverges from spec. Like type-checking but for architectural intent |
| **Multi-stage translation pipeline** | Competitors: single-pass generation | Editable intermediate layers: concept → spec → design → tasks. Each layer is reviewable, versionable |
| **JetBrains distribution** (35M+ users) | Nobody has access to this install base | JB Marketplace = instant reach to ICP. JB AI Assistant = existing AI surface to extend |
| **Open spec format + premium IDE** (hybrid model) | Either fully OSS (SpecKit, BMAD) or fully closed (CodeSpeak, Devplan) | Spec format is open (community, no lock-in). IDE plugin is premium (defensibility, monetization) |

**In one sentence:** Bonsai is the first spec-driven tool that works **inside the IDE** as a compiler — not outside as a CLI script — giving developers real-time drift detection, spec↔code navigation, and predictable AI output without leaving their workspace.

---

## HOW (Product, Validation, GTM, Metrics) — TO DO

> Content below is from the previous plan (v2) and needs updating based on the new competitor insights.

### Slide 15 — Product Thesis (How Bonsai Works)

- Specs live in Git next to code and evolve with it
- Multi-stage translation pipeline into editable intermediate layers
- Bidirectional propagation: spec changes inform code guidance, code changes update specs
- Outcome: predictable, reviewable architectural control while shipping fast

### Slide 16 — MVP Scope (First Shippable)

**In scope:**

- Minimal spec-as-code format (markdown, Git-native, open)
- IDE-native drift detection and alerts (IntelliJ plugin)
- Spec → code and code → spec navigation
- Lightweight PR workflow integration

**Out of scope:**

- Full compiler (spec→code generation) — phase 2
- Multi-repo support — phase 3
- Knowledge graph / drift detection across entities — phase 3
- Broad multi-IDE support — future

### Slide 17 — First 30 Days: Validation Experiments (Go/No-Go)

- **Experiment 1: Spec creation behavior** — prove engineers will write and maintain specs
- **Experiment 2: Drift detection value** — prove drift alerts reduce review time and rework
- **Experiment 3: Pain ranking + willingness to pilot** — ICP confirms problem is top-tier
- Define Go/No-Go thresholds per experiment

### Slide 18 — GTM: First 100 Users

- Recruit 5–10 design partners with frequent PRs and architecture constraints
- Private alpha inside JetBrains IDE with high-touch onboarding
- Growth loop: drift alerts → spec updates → clearer reviews → more adoption

### Slide 19 — Metrics + Kill Signals

**North Star:** Weekly Active Aligned Specs
**Leading:** Time-to-first-spec, drift alert engagement, spec update completion
**Guardrails:** False positive rate, uninstall rate, workflow friction
**Kill signals:** Low repeat usage, no measurable cycle time improvement, teams refuse to maintain specs

### Slide 20 — Risks + 6-month Roadmap (Decision Gates)

- Phase 1 (0–2 months): IDE plugin MVP + design partner validation
- Phase 2 (2–4 months): Hardening, retention, spec↔code navigation
- Phase 3 (4–6 months): Compiler approach, multi-repo, early monetization
- Decision gates at the end of each phase

---

## Appendix (Not Presented Live)

### Appendix A — Learn & Steal: Feature-level Detail
>
> Organized by insight (not by competitor) — what matters is the validated pattern, not who invented it

| Insight | Validated by | Details | Steal priority |
|---------|-------------|---------|---------------|
| Markdown + Git-native spec format | SpecKit, BMAD, OpenSpec, CodeSpeak | .md files living in repo alongside code. Versioned, diffable, reviewable in PRs | 🔴 High |
| Slash-command UX for spec operations | SpecKit (/spec), OpenSpec (/opsx:propose), BMAD (/bmad-help) | `/command` pattern is natural in terminal/chat. Low learning curve, high discoverability | 🟡 Medium |
| Structured spec lifecycle: requirements → design → tasks | Kiro (requirements.md → design.md → tasks.md), OpenSpec (proposal → specs → design → tasks) | Multi-artifact lifecycle, not single monolothic spec | 🔴 High |
| Steering / persistent context rules | Kiro (.kiro/steering/), Agent-OS (standards extraction), BMAD (project constitution) | Project-specific rules that persist across AI sessions. Prevents "starting from scratch" every time | 🟡 Medium |
| Spec diff → Code diff (compiler approach) | CodeSpeak (spec changes → code changes, proven on OSS projects) | Bi-directional: change spec → code updates. Change code → spec updates. 5-10x shrink factor | 🔴 High |
| Shrink factor metric (LOC reduction) | CodeSpeak case studies: 5.9x-9.9x shrink factor on real OSS code (beautifulsoup4, yt-dlp, Faker, markitdown) | Quantifiable value prop: "spec is 5-10x smaller than code" | 🟢 Low (marketing) |
| Adaptive depth by task scale | BMAD ("scale-domain-adaptive"), specs.md (3 flows), Kiro (steering adjusts) | From bug fix → feature → epic: same tool, different rigor level | 🟡 Medium |
| Spec-delta: review intent, not just code diff | OpenSpec (spec-delta = change in intent/requirements), CodeSpeak (spec diff) | Reduces reviewer cognitive load: "WHY did this change?" vs "WHAT line changed?" | 🔴 High |
| Vendor-agnostic, no API keys, no MCP dependency | OpenSpec: works with 20+ AI tools. No API keys needed. No MCP server required | Reduces adoption friction, avoids vendor lock-in | 🟡 Medium |
| Knowledge graph + drift detection | Auto-K (bi-directional sync, entities reference each other, conflicts self-flag), Devplan (context graph from repos + tickets) | Structured graph > flat docs for catching inconsistencies. "Unlike a doc that rots, the graph holds itself together" | 🟡 Medium |
| Community contribution model & OSS ecosystem | BMAD (5 modules, community Discord, YouTube), OpenSpec (Discord, Slack for teams), Taskmaster (community contributors) | OSS + community = faster adoption + ecosystem effects. All leaders are MIT-licensed | 🟡 Medium |
| LLM output validation by schema | PydanticAI, Instructor, Outlines | Force structured output with retry on mismatch. Commoditized but useful as building block | 🟢 Low |
| Visual language for specs (diagrams) | Stately/XState (state machine diagrams as source of truth, visual editor) | Visual representations make specs more accessible to non-devs and easier to review | 🟢 Low |
| Multi-agent role model | BMAD (12+ specialized agents: PM, Architect, Dev, UX, Scrum Master), specs.md (3-4 agents per flow) | Specialized AI personas for different lifecycle phases | 🟢 Low |
| Context graph from repos + trackers | Devplan (connects to code, tickets, website, product docs → rich context graph) | Every spec/prompt understands architecture and product. "No explaining from scratch" | 🟡 Medium |

### Appendix B — Competitor Cost & Business Model Detail

| Competitor | Pricing | Model | Revenue stage |
|---|---|---|---|
| Spec Kit | Free, OSS (MIT) | Community/GitHub-backed | Pre-revenue (GitHub funds) |
| Kiro | Free | Amazon-backed (Bedrock) | Pre-revenue (Amazon subsidy) |
| BMAD | Free, OSS (MIT). "100% free, no paywalls, no gated content" | Donations (Buy Me a Coffee), Corporate sponsorship | Pre-revenue |
| OpenSpec | Free, OSS (MIT) | Community | Pre-revenue |
| CodeSpeak | Free alpha | Unknown (hiring, closed) | Pre-revenue |
| Taskmaster | Free, OSS (MIT + Commons Clause: no reselling) | Community + building Hamster (paid product) | Pre-revenue, transitioning |
| Stately | Free + paid Studio tiers | OSS core (XState) + SaaS (Stately Studio, Stately Sky) | Revenue-generating |
| Agent-OS | Free + paid Builder Methods Pro community | OSS + community monetization | Pre-revenue |
| Autospec | Free, OSS (MIT) | Community | Pre-revenue |
| specs.md | Free, OSS (MIT). VS Code extension on marketplace | Community | Pre-revenue |
| Auto-K | Free beta (waitlist) | Unknown (closed) | Pre-revenue |
| Devplan | $24/mo (Builder), $49/mo (Team, 3 users included, +$19/user), Enterprise (custom) | SaaS | Revenue-generating |

### Appendix C — Full Competitor Feature Matrix (for reference, not for slide)

| Capability | SpecKit | Kiro | BMAD | OpenSpec | CodeSpeak | Taskmaster | Stately | Agent-OS | specs.md | Auto-K | Devplan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Spec formalization | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bi-directional spec↔code | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Drift detection | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅(promised) | ❌ |
| IDE integration (native plugin) | ❌ | ✅(own IDE) | ❌ | ❌ | ❌ | ❌ | ✅(VS Code) | ❌ | ✅(VS Code) | ❌ | ❌ |
| JetBrains plugin | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Slash commands | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ |
| Adaptive depth | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Agent orchestration | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Task management | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Knowledge graph | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Multi-repo | ❌ | ❌ | ❌ | ❌ | ✅(mixed) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Versioning | ✅(Git) | ✅(Git) | ✅(Git) | ✅(Git) | ✅(Git) | ✅(Git) | ❌ | ✅(Git) | ✅(Git) | ❌ | ❌ |
| OSS | ✅ | ❌ | ✅ | ✅ | ❌ | ✅* | ✅ | ✅ | ✅ | ❌ | ❌ |
| Community contrib | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Eval harness | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| LLM validation | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Visual language | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| IDE lock-in | ❌ | ✅(Kiro IDE) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Monetization | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |

*Taskmaster = MIT + Commons Clause (no reselling)
