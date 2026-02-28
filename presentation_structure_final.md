# Bonsai — Presentation Structure (15–20 min)

## WHAT (Problem, ICP, Direction)

### Slide 1 — Title

**Bonsai: Predictable AI-assisted Development via Spec-driven Control**

### Slide 2 — Presentation Structure

- WHAT: Problem + direction  
- WHY: Market + strategy + opportunity  
- HOW: MVP + validation + GTM + risks

### Slide 3 — Pain Story (Hook)

- One concrete scenario: AI speeds up delivery, but architecture diverges from intent
- Consequences: review time spikes, rework increases, specs decay, coordination overhead grows

### Slide 4 — Pain Map (Failure Modes)

- Spec rot: specs become stale and untrusted
- Architecture drift: implementation diverges from agreed design
- Review inflation: PR review time grows due to uncertainty and misalignment
- Onboarding slowdown: harder to understand “what matters” and “why”
- Ownership ambiguity: unclear source of truth for decisions and constraints

### Slide 5 — JTBD + ICP (Early Adopters)

- **JTBD**: Keep implementation aligned with intended architecture while shipping fast
- **Primary ICP**: Tech Leads, Staff/Principal Engineers, Architects in 10–50+ engineer teams
- Traits: heavy IDE usage, strong PR culture, measurable pain from drift

### Slide 6 — Direction: Wedge + Non-goals

- **Wedge**: IDE-native drift detection + “spec ↔ code” navigation
- **Non-goals**: full autonomous agent as the core, dashboard-first experience, multi-IDE support on day one

---

## WHY (Market, Competition, Strategic Choice)

### Slide 7 — Why Now

- AI writes more code, so drift risk scales with throughput
- Chat guidance is ephemeral and not a durable source of truth
- Teams need developer-native governance that fits existing workflows

### Slide 8 — Market Map (Key Concepts)

- AI coding assistants and agentic IDE workflows
- Spec management and architecture documentation
- Governance, policy, and quality gates (CI / review processes)
- **Bonsai position**: a “spec compiler” that continuously connects specs to code

### Slide 9 — Competitive Landscape (Direct + Indirect)

- **Direct**: spec-driven AI dev tools focused on specs, enforcement, and IDE integration
- **Indirect**: AI-first IDEs, docs platforms, CI policy tools
- Core gap: either code gen without governance, or docs without tight code linkage

### Slide 10 — Niche Choice: Low-hanging vs Moonshot

- **Low-hanging**: IntelliJ ecosystem + minimal spec format + drift detection
- **Moonshot**: universal spec standard + full multi-language translation pipeline
- **Choice**: start with low-hanging for fastest time-to-value and distribution leverage

---

## HOW (Product, Validation, GTM, Metrics)

### Slide 11 — Product Thesis (How Bonsai Works)

- Specs live in Git next to code and evolve with it
- Multi-stage translation pipeline into editable intermediate layers
- Bidirectional propagation: spec changes inform code guidance, code changes update specs
- Outcome: predictable, reviewable architectural control while shipping fast

### Slide 12 — MVP Scope (First Shippable)

**In scope**

- Minimal spec-as-code format and lifecycle (create, review, version, publish)
- IDE-native drift detection and alerts
- Spec → code and code → spec navigation
- Lightweight PR workflow integration

**Out of scope**

- Full autonomous coding agent as the core product
- Large dashboards as the primary surface
- Broad multi-IDE support on day one

### Slide 13 — First 30 Days: Validation Experiments (Go/No-Go)

- **Experiment 1: Spec creation behavior**
  - Prove engineers will write and maintain specs in the proposed format
- **Experiment 2: Drift detection value**
  - Prove drift alerts reduce review time and rework
- **Experiment 3: Pain ranking + willingness to pilot**
  - Confirm the problem is top-tier for ICP and teams commit to a pilot
- Define explicit Go/No-Go thresholds per experiment

### Slide 14 — GTM: First 100 Users

- Recruit 5–10 design partners with frequent PRs and architecture constraints
- Private alpha inside the IDE with high-touch onboarding
- Expand to an early access program once retention and value are proven
- Growth loop: drift alerts → spec updates → clearer reviews → more adoption

### Slide 15 — Metrics + Kill Signals

**North Star**

- Weekly Active Aligned Repos (or Weekly Active Aligned Specs)

**Leading indicators**

- Time-to-first-spec
- Drift alert engagement rate
- Spec update completion rate

**Guardrails**

- Drift false positive rate
- Disable / uninstall rate
- Perceived workflow friction

**Kill signals**

- Low repeat usage after initial setup
- No measurable improvement in cycle time / review time
- Teams refuse to maintain specs in the proposed workflow

### Slide 16 — Risks + 6-month Roadmap (Decision Gates)

**Top risks**

- Workflow friction outweighs value
- Drift detection accuracy issues
- Integration complexity across real-world stacks

**Roadmap with gates**

- Phase 1 (0–2 months): Wedge MVP + design partner validation
- Phase 2 (2–4 months): Hardening, retention, richer “spec ↔ code” flows
- Phase 3 (4–6 months): Expand patterns/stacks + early monetization tests
- Decision gates at the end of each phase

---

## Appendix (Not Presented Live)

- Competitor feature comparison matrix
- Workflow diagrams and sample spec format
- Interview guide and experiment instrumentation plan
- Sources list and assumptions log
