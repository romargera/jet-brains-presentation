# Dev workflow

1. Specification definition
2. Planning, grooming
3. Development (Sync with teams, integrations, PoC, Code review)
4. Testing (QA, Load testing, Security testing, Product Review, CI/CD)
5. Release (Feature flag, Canary release, metric monitoring)
6. Support (Monitoring, Bug fixing, Rollback, Reflection)
7. Documentation update

# Adoption & trust

Adoption

* AI adoption among software developers reached 90%, a 14% year-over-year increase (<https://dora.dev/research/2025/dora-report/>)

But:

* AI sentiment:
"how favorable is your stance?": "Unfavorable + Very unfavorable"
20.4% (2025) +14.0 п.п. YoY (<https://survey.stackoverflow.co/>)
* Trust
    (Highly + Somewhat): 43.04% (2024) -> 32.79% (2025) (−10.25 п.п.)
    Distrust (Somewhat + Highly): 30.37% -> 45.70% (+15.34 п.п.)
(<https://survey.stackoverflow.co/>)

# Dev demand \ pain

Documentation - top 1 желаемая задача для автоматизации согласно исследованию (<https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf>)
А именно:
"Creating & updating documentation, generating API docs from code comments, & maintaining
team knowledge bases. Efficiently understanding existing code, APIs, & systems from docu-
mentation & reports."
При этом фактическое время работы над документацией занимает 4% раб времени

* разработчики предпочтут в 1,5 раза больше времени тратить на написание кода и вопросы архитектуры
* env setup занимает в 2 раза больше времени, чем хочется
* security/compliance, communication, customer support, debugging занимают от 1,5 до 3 раз больше времени, чем хотелось бы. security/compliancе - топ нелюбимых задач по объему затрачиваемого времени
(<https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf>)

C точки зрения распределения рабочего времени разработчика:

* Documentation - top 1 желаемая задача для автоматизации согласно исследованию (<https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf>). При этом фактическое время работы над документацией занимает 4% раб времени
* env setup занимает в 2 раза больше времени, чем хочется
* security/compliance, communication, customer support, debugging занимают от 1,5 до 3 раз больше времени, чем хотелось бы. security/compliancе - топ нелюбимых задач по объему затрачиваемого времени
(<https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf>)

# Лучшая стратегия по сокращению времени на Security/Compliance

Не трогать то, что может быть связано с безопасниками

# Лучшая стратегия по сокращению времени на Documentation

Уже есть решения

# Для разработчика

* Боли разработчика

# Для бизнеса продуктовой компании

* Боли бизнеса

Для обоих

* Косты на токены
* Time spent

# Для Jet Brains

* Новая статья дохода
* Рост удержания в core продуктах
* Новые продажи core продуктов

Prompt engineering, ориентированный на экономию
“On average, token consumption decreased by 15–20%…” и “Imposing limits on output length or token budget led to a 20–30% reduction…”
<https://arxiv.org/html/2504.15989v2>

Не забыть про

* версионирование и drift detection
* мульти репозиторий
* AI-dev transparency: code & architecture): executable accuracy, task decomposition approach and easy interpretation.

Security/Compliance - снизить охват

Поддерживает стриминг, multi-agent workflows, durable execution и human-in-the-loop. Идеально для PM вроде вас, интегрирующего AI в продукты (например, travel/rental).

трассировка + слой качества/безопасности Evaluation: галлюцинации, prompt injection, PII, off-topic ответы и др.

Хороший FAQ <https://openspec.dev/>

“Vibe-coders” скорее не подходит тк нужна дисциплина
