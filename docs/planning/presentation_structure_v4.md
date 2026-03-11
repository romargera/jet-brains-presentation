# Bonsai — Presentation Structure v4

> Based on v3 + updated strategic framing: **bi-directional spec↔code** as core paradigm, **code-first extraction** as entry point, **drift detection** as uncontested differentiator.
> Changes from v3: updated Summary slide, 6 new HOW slides.

---

## Updated: Slide 15 — WHY: Summary & Market

**What changed vs current slide:**

- "Strategic Setup" tile: added code-first framing ("extracts specs from code")
- "Niche & ICP" tile: already updated in slides.md
- "Growth Loops" tile: "Champion-driven" label (already updated by user)
- New: added "Differentiation" tile (5th tile) to complete the summary

**Content:**

| Tile | Label | Body |
|---|---|---|
| 1 | Strategic Setup & AI Adoption | AI adoption hit 90% but distrust surged +15pp. High-value tasks are crowded out by overhead. The window for a trust-layer governance tool is now. |
| 2 | Market Size | TAM: $4.9B / SAM: $3.4B / SOM: $171M. [Calculations link]. Cross check via bottom up - tbd |
| 3 | Niche & ICP | Uncontested IDE-native wedge: code-first spec extraction + drift detection for Tech Leads wanting predictable architecture. |
| 4 | Differentiation | Bi-directional spec↔code in IDE via PSI. Unlike competitors: we extract specs from code (zero friction), then enforce + detect drift. |
| 5 | Growth Loops | Champion-driven adoption (1 repo = many devs) + spec-as-contract reviewer loop + PR/CI enforcement gates. |

**Notes (snoska):** keep existing assumptions + market size notes unchanged.

---

## HOW Section — 6 New Slides

### Slide 16 — HOW: MVP + Backlog

**Title:** HOW: MVP Scope & Backlog

**Format:** 2-column: MVP (left) + Backlog/Out of scope (right)

**MVP (Month 1-2):**

| Feature | What it does | Why first |
|---|---|---|
| Code→Spec extraction via PSI | Analyzes existing code, auto-generates architectural spec (.md in Git) | Zero adoption friction: dev writes code, Bonsai extracts spec. No new habits required |
| Spec validation (dev reviews) | Dev reviews/edits extracted spec in IDE (gutter icons, tool window) | Ensures spec accuracy without manual writing |
| Basic drift detection | Inline warning when code diverges from last validated spec | Core differentiator. No competitor ships this in prod |
| Git-native markdown specs | Specs stored as .md in `/specs` folder, versioned in Git | Industry standard (SpecKit, BMAD). Zero vendor lock-in |
| JetBrains Marketplace plugin | Native IntelliJ plugin, not CLI or web | Distribution moat. Zero context switch |

**Backlog (ordered by phase):**

| Phase | Feature | Depends on |
|---|---|---|
| Phase 2 (Month 3-4) | Spec→Code generation (reverse direction) | Validated extraction model |
| Phase 2 | PR integration: spec-delta in review | Drift detection works |
| Phase 2 | Slash commands (/spec, /drift, /align) | Plugin foundation |
| Phase 3 (Month 5-6) | Multi-repo spec management | Single-repo adoption proven |
| Phase 3 | CI gate enforcement (block non-conformant merges) | Drift detection + PR integration |
| Phase 3 | Spec templates / marketplace (community) | User base exists |
| Future | Full compiler (bi-directional sync, shrink factor) | Spec→Code + Code→Spec both mature |
| Future | Multi-IDE support (VS Code, Cursor) | JB plugin proven |

**Key message:** _"We start where developers already are (code). We extract specs — not demand them. Drift detection from day 1."_

---

### Slide 17 — HOW: Key Metrics + Kill Signals

**Title:** HOW: Key Metrics + Kill Signals

**Format:** 3 rows: North Star → Leading indicators → Kill Signals

**North Star Metric:** Weekly Active Validated Specs (WAVS)
> A spec counts as "active" if it was extracted, reviewed, or triggered a drift alert in the past 7 days.

**Leading Indicators:**

| Metric | Target (Month 2) | Why it matters |
|---|---|---|
| Time-to-first-spec | < 5 min from plugin install | Proves zero-friction extraction works |
| Spec validation rate | > 60% extracted specs get reviewed | Devs find value in extracted specs |
| Drift alert engagement | > 40% alerts resolved (not dismissed) | Drift detection is useful, not noisy |
| Weekly plugin opens | > 3x per user per week | Habit forming |

**Guardrail Metrics (watch but don't optimize):**

| Metric | Threshold | Red flag |
|---|---|---|
| False positive rate (drift) | < 20% | Noise kills trust. If > 30% → retune algorithm before scaling |
| Uninstall rate (7-day) | < 15% | If > 25% → fundamental UX problem |
| Spec staleness (no update > 30d) | < 40% specs | If > 50% → specs are rotting, same as docs |

**Kill Signals (hard stop if any is true after Month 3):**

| Signal | Threshold | Action |
|---|---|---|
| < 5% of extracted specs get reviewed | After 50+ users | Core value prop invalid: devs don't care about specs |
| Zero measurable reduction in review time | After 3 months of usage data | No ROI → no willingness to pay |
| Teams actively disable drift alerts | > 50% disable rate | Drift detection is perceived as noise, not value |
| No design partner willing to continue after free trial | 0 out of 10 | Product doesn't solve a real problem |

---

### Slide 18 — HOW: 6-Month Roadmap (Decision Gates)

**Title:** HOW: 6-Month Roadmap

**Format:** Horizontal timeline with 3 phases + decision gates

**Phase 1: Validate (Month 0-2)**

- Ship MVP: code→spec extraction + basic drift detection
- Recruit 10 design partners (JB users, 5+ devs, frequent PRs)
- Goal: prove devs review & maintain extracted specs
- **Gate 1:** ≥ 60% spec validation rate AND ≥ 3 partners request to continue → Go to Phase 2

**Phase 2: Harden (Month 2-4)**

- Add spec→code generation (reverse direction → bi-directional)
- PR integration: spec-delta in code reviews
- Slash commands for common operations
- Goal: prove drift detection reduces review time
- **Gate 2:** ≥ 20% review time reduction (measured) AND ≥ 5 partners paying or committed → Go to Phase 3

**Phase 3: Scale (Month 4-6)**

- CI gate enforcement (organizational rollout)
- Multi-repo spec management
- Spec templates / marketplace MVP
- Early monetization: freemium plugin + paid team features
- **Gate 3:** ≥ 100 active users AND positive unit economics signal → Continue investment

**Decision framework:** Each gate requires: (1) quantitative metric met, (2) qualitative signal from design partners, (3) no kill signals triggered.

---

### Slide 19 — HOW: Risks & Mitigation

**Title:** HOW: Risks & Mitigation

**Format:** Table with risk / probability / impact / mitigation

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| **Devs ignore extracted specs** ("not my docs") | Med | High | Make specs actionable (drift alerts, not just docs). If < 5% review rate → kill signal |
| **JB locks us into small market** (VS Code = 73%) | Med | Med | Start JB (enterprise, Java/Kotlin). Phase 3: LSP-based extraction for multi-IDE. Spec format is IDE-agnostic |
| **Big Tech ships native drift detection** (GitHub/Amazon) | Low | High | Our 6-month head start + PSI depth > their generic approach. Deepening PSI integration = barrier. Worst case: acquisition target |
| **False positive drift alerts erode trust** | High | Med | Conservative threshold at launch (high precision, lower recall). User-tunable sensitivity. Guardrail: < 20% FP rate |
| **Spec format fragmentation** (every tool invents own) | Med | Med | Open format from day 1 (markdown). Compatibility with SpecKit format. Contribute to emerging standards |
| **No willingness to pay** (all competitors are free) | Med | High | Freemium IDE plugin (free extraction) + paid team features (CI gates, multi-repo, analytics). Design partners validate pricing by Month 4 |

---

### Slide 20 — HOW: GTM — First 100 Users

**Title:** HOW: GTM — First 100 Users

**Format:** Funnel visualization or phased plan

**Phase 1: Design Partners (Users 1-10) — Month 1-2**

- Source: JB community forums, Kotlin/Java meetups, internal JB teams (if available)
- Criteria: 5+ devs, regular PRs, architecture constraints, JB IDE users
- Offer: free plugin + weekly 1:1 feedback sessions
- Goal: validate extraction quality, drift detection accuracy

**Phase 2: Private Alpha (Users 10-30) — Month 2-3**

- Source: JB Marketplace (early access listing), dev Twitter/X, spec-driven dev communities (SpecKit Discord, BMAD Discord)
- Offer: free plugin, Slack community for feedback
- Activation metric: first spec extracted within 10 min of install
- Goal: validate self-serve onboarding, collect NPS

**Phase 3: Public Beta (Users 30-100) — Month 3-5**

- Source: JB Marketplace featured listing, blog posts ("Code-first specs: why we don't ask devs to write documentation"), conference talks (JB events, DevOps Days)
- Content loop: design partner case studies → blog → social proof → organic installs
- Goal: reach 100 WAU, validate retention curve

**Key channels:**

| Channel | Cost | Expected yield | Why |
|---|---|---|---|
| JB Marketplace | Free | 40% of installs | Built-in distribution to 35M+ users |
| Dev communities (Discord, Reddit) | Free | 20% of installs | Spec-driven dev is a hot topic |
| Content (blog, case studies) | Time | 25% of installs | "Code-first specs" is a novel narrative |
| Conferences (JB events) | Low | 15% of installs | Direct access to ICP (Tech Leads at JB events) |

---

### Slide 21 — HOW: First 30 Days — Validation Experiments

**Title:** HOW: First 30 Days — Validation Experiments

**Format:** 3 experiment cards with Go/No-Go thresholds

**Experiment 1: Spec Extraction Quality**

- Question: Does PSI-based extraction produce specs that devs find accurate and useful?
- Method: Extract specs from 5 real repos (design partners). Devs rate accuracy 1-5 and edit % needed
- Go: ≥ 3.5/5 accuracy, ≤ 30% manual edits needed
- No-Go: < 2.5/5 accuracy OR > 60% edits → extraction model needs fundamental rework

**Experiment 2: Drift Detection Value**

- Question: Do drift alerts reduce rework or catch real issues before PR merge?
- Method: Track drift alerts for 2 weeks. Measure: alerts triggered, alerts resolved, false positives, issues caught
- Go: ≥ 40% alert resolution rate, < 20% false positive rate, ≥ 1 real issue caught per dev per week
- No-Go: > 50% dismiss rate AND devs report alerts as "noisy" in feedback

**Experiment 3: ICP Pain Ranking & Willingness to Pilot**

- Question: Do Tech Leads rank "spec↔code drift" as a top-3 pain? Would they pilot Bonsai?
- Method: 15 structured interviews (10 Tech Leads, 5 EMs). Pain stack-ranking + willingness to install
- Go: ≥ 8 out of 15 rank drift as top-3 pain, ≥ 5 agree to install/pilot
- No-Go: < 4 rank drift as top-3 → problem isn't painful enough for ICP

**Timeline:**

- Week 1: Recruit design partners, set up telemetry
- Week 2-3: Run experiments 1 & 2 (parallel)
- Week 3-4: Run experiment 3 (interviews)
- Week 4: Analyze results → Go/No-Go decision at Gate 1

---

## Slide Order Summary

| # | Section | Title | Status |
|---|---|---|---|
| 1 | WHAT | Title | ✅ Done |
| 2 | WHAT | Presentation Structure | ✅ Done |
| 3 | WHAT | The AI Adoption Paradox | ✅ Done |
| 4 | WHAT | Distrust Issues | ✅ Done |
| 5 | WHAT | Dev Time Spent | ✅ Done |
| 6 | WHAT | B2B Pains | ✅ Done |
| 7 | WHAT | Strategic Directions | ✅ Done |
| 8 | WHAT | Chosen Direction | ✅ Done (updated: bi-directional framing) |
| 9 | WHY | Approaches | ✅ Done (updated: steering files note, triangulation) |
| 10 | WHY | Competitor Landscape | ✅ Done (updated: CodeSpeak, Devplan descriptions) |
| 11 | WHY | Key Patterns (Learn & Steal) | ✅ Done (updated: persistent steering, bi-directional) |
| 12 | WHY | Niche Choice | ✅ Done (updated: steering files ≠ enforceable specs) |
| 13 | WHY | Why Us (Differentiation) | ✅ Done (updated: code-first extraction, drift detection) |
| 14 | WHY | ICP, JTBD, Triggers | ✅ Done |
| 15 | WHY | Summary & Market | 🔄 Update needed (add Differentiation tile) |
| 16 | HOW | Growth Loops | ✅ Done (updated: champion-driven label) |
| 17 | HOW | MVP + Backlog | 📝 New |
| 18 | HOW | Key Metrics + Kill Signals | 📝 New |
| 19 | HOW | 6-Month Roadmap (Decision Gates) | 📝 New |
| 20 | HOW | Risks & Mitigation | 📝 New |
| 21 | HOW | GTM — First 100 Users | 📝 New |
| 22 | HOW | First 30 Days — Validation Experiments | 📝 New |
