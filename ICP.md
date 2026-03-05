This slide should cover these questions "* b. Who will be our early-adopters? What problems / JTBDs do they have?"

## Сore JTBD

When engineers build with AI in a production codebase, they want development to be predictable and controllable, so they can ship faster with confidence.

## ICP

# Early adopters

Tech Lead, Staff Engineer, Senior Engineer, которые отвечают за качество и архитектуру в production codebase.
Уже пользуются AI ассистентами и страдают от непредсказуемости, дрейфа и лишнего времени на дебаг и проверку.
Средние и крупные продуктовые команды, где есть ощутимая цена ошибок и “docs rot”, и важна архитектурная дисциплина.

Sub JTBD: When engineers build with AI in a production codebase, they want AI-driven changes to be predictable and controllable at the PR/task level, so they can merge and ship faster with confidence.

Top problems
Unscoped AI diffs, hard to review
Spec ↔ code drift (chat vs repo)
Costly regressions from AI changes

Top triggers
1–2 painful AI-caused incidents/regressions
AI PR volume spikes, review churn rises
Major refactor/migration in a mature codebase

# Scaling

Engineering Manager / Director of Engineering / Head of Platform. Также Security/Compliance leadership в компаниях, где нужны политики и контроль изменений.

Sub JTBD: When engineering organizations adopt AI-assisted development across many repos and teams, they want spec-based governance to make changes predictable, controllable, and auditable at scale, so they can standardize delivery, reduce risk, and ship faster with confidence.

Top problems

No org-wide standard for AI-assisted dev
Hard to manage risk across many repos (blast radius)
Low auditability, weak policy enforcement

Top triggers

Rollout AI across many teams/repos
Security/compliance pressure or upcoming audit
Repeated incidents or quality drop tied to AI output
