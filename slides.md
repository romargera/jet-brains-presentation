<!-- markdownlint-disable MD033 -->

<div class="title-slide">
  <p class="title-label">Take-Home Task</p>
  <h1>Bonsai<br></h1>
  <p class="title-subtitle">Predictable AI-assisted Development<br>via Bi-directional Spec↔Code Control</p>
  <div class="title-author">
    <p class="author-name">Roman Babunts</p>
    <p class="author-date">March 2026</p>
  </div>
</div>

Notes:
привет. Меня зовут Роман Бабунц, и это мое тестовое задание. Я расскажу, какую проблему я решаю, почему выбираю именно это направление и подход и как я бы реализовал его в первые шесть месяцев.

---
<!-- .slide: id="agenda" -->

## Presentation Structure

<div style="width: 100%; max-width: 820px; margin: 0 auto;">
<div class="agenda-nav">
  <div class="agenda-section">
    <h4>WHAT</h4>
    <div style="font-size: 0.6em; color: var(--text-main); margin: 0 0 6px;">Define the problem and pick a direction</div>
  </div>
  <div class="agenda-section">
    <h4>WHY</h4>
    <div style="font-size: 0.6em; color: var(--text-main); margin: 0 0 6px;">Map the market and justify the approach</div>
  </div>
  <div class="agenda-section">
    <h4>HOW</h4>
    <div style="font-size: 0.6em; color: var(--text-main); margin: 0 0 6px;">Roadmap, MVP, metrics, risks</div>
  </div>
</div>

<ul class="distrust-notes">
  <span class="metric-badge">A</span> Assumptions are marked with this icon
</ul>
</div>

Notes:
Презентация разделена на три блока. WHAT, где я определяю проблему и выбираю направление. WHY, где я показываю рынок и обосновываю подход. И HOW, где речь про roadmap, MVP, метрики и риски.

Отдельно отмечу сразу: все допущения я пометил этим бейджем. Большинство из них я планирую верифицировать в первый месяц работы.

---
<!-- .slide: id="adoption-paradox" -->

## WHAT: The AI Adoption Paradox

<p class="slide-subtitle"></p>

<div style="width: 100%; max-width: 95%; margin: 0 auto;">
<div class="adoption-layout" style="margin: 10px 0; max-width: none; width: 100%; align-items: center;">
<div class="adoption-col adoption-col-left" style="flex: 1 1 50%; max-width: 50%; border-color: transparent; background: transparent !important;">
<div class="adoption-hero">
<span class="adoption-hero-number">90%</span>
<span class="adoption-hero-label">of developers use AI tools <a href="https://dora.dev/research/2025/dora-report/" target="_blank" style="color: var(--accent-blue); text-decoration: none;">[1]</a></span>
<span class="adoption-hero-delta">+14% YoY</span>
</div>
</div>
<div class="adoption-col adoption-col-left" style="flex: 1 1 50%; max-width: 50%; border-color: transparent; background: transparent !important;">
<div class="adoption-hero">
<span class="adoption-hero-number">46%</span>
<span class="adoption-hero-label">of devs distrust AI dev (somewhat + high) <a href="https://survey.stackoverflow.co/" target="_blank" style="color: var(--accent-blue); text-decoration: none;">[2]</a></span>
<span class="adoption-hero-delta" style="color: #ef4444;">+15 pp YoY</span>
</div>
</div>
</div>

<div class="adoption-takeaway">
  <p><strong>Takeaway:</strong> 90% adoption + 45% distrust → developers use AI for speed but reject unpredictable output → our opportunity: make AI-assisted dev predictable.</p>
</div>
</div>

Notes:
Согласно исследованию 5000 респондентов от Dora за 2025 AI-инструментами пользуются 90% разработчиков, это плюс 14% год к году. Но одновременно быстро растет недоверие: 46% разработчиков сообщают о среднем или высоком уровне distrust, это плюс 15 процентных пунктов за год.

Таким образом, мы видим парадокс: разработчики активно используют AI ради скорости, но все меньше доверяют тому, что он выдает. И именно разрыв между adoption и trust создает окно возможности. Если сделать AI-assisted development предсказуемым, мы решаем проблему, которая не уменьшается, а становится только острее.

---
<!-- .slide: id="what-icp-jtbd" -->

## WHAT: Issue signal*

<div style="width: 100%; max-width: 90%; margin: 0 auto;">
<div style="margin: 40px 0; max-width: none; width: 100%; background: #1a1a1a; border-left: 4px solid #81c784; border-radius: 4px; padding: 16px 18px; text-align: left; position: relative; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.3); box-sizing: border-box; display: grid; grid-template-columns: 64px 1fr; gap: 10px; align-items: start;">
  <img src="Personas/photo_2026-03-12_19-49-00.jpg" alt="Alex portrait" style="width: 64px; height: 64px; border-radius: 6px; border: 1px solid rgba(129, 199, 132, 0.45); object-fit: cover; display: block;">
  <div style="position: relative;">
    <div style="position: absolute; top: -8px; left: -2px; font-size: 2.8em; color: rgba(129, 199, 132, 0.15); font-family: serif; line-height: 1; pointer-events: none;">&ldquo;</div>
    <p style="font-size: 0.66em; line-height: 1.5; color: #e0e0e0; font-style: italic; margin: 0 0 8px 0; font-weight: 400; position: relative; z-index: 1;">"AI-generated code is often useful, but not production-ready. What used to be a 5-minute review can easily turn into 45 minutes of review, re-prompting, and cleanup."</p>
    <div style="font-size: 0.66em; color: var(--text-muted); position: relative; z-index: 1;"><span style="line-height: 1.5; color: #e0e0e0; font-style: italic; font-weight: 400;">(c) Alex</span>, <span style="font-style: italic;">Tech Lead, Kotlin + Gemini</span></div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 10px; border-left: 4px solid #34d399; background: rgba(16, 185, 129, 0.12); border-color: rgba(52, 211, 153, 0.35);">
  <p><strong>Takeaway:</strong> The core friction in AI adoption isn't writing code - it's the unpredictability and review bottlenecks caused by unscoped AI diffs.</p>
</div>

<ul class="distrust-notes">
  * Preliminary signal. N=1 exploratory interview. Systematic validation: Month 1.
</ul>
</div>

Notes:
Я провел интервью с пользователем. Александр, Tech Lead, который работает с Kotlin и Gemini. Александр говорит: AI-код часто полезен, но не готов к продакшену. То, что раньше занимало пять минут на review, легко превращается в сорок пять минут. В одном случае AI добавил зависимости, которые нужно было отдельно согласовывать с безопасниками, и затронул файлы, которые команда старается не менять. Reviewer потратил время не на логику, а на то, чтобы понять, что вообще произошло.

Важно, что это пока только один интервьюируемый, N=1. Это нельзя считать верификацией боли, но это сильный сигнал, который стоит проверять дальше. То, что описывает Александр, говорит о следующем: основная проблема в AI adoption не в самой генерации кода, а в непредсказуемости результата и в review overhead, который эта непредсказуемость создает. Поэтому в первый месяц я планирую провести качественное исследование, чтобы проверить, что этот сигнал системно повторяется.

---
<!-- .slide: id="stream-options" -->

## WHAT: Strategic Directions <span class="metric-badge">A</span>

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 10px;"><a href="./index.html#/stream-options-main-appendix" style="color: var(--accent-blue);">Prioritized</a> across <a href="./index.html#/distrust-issues" style="color: var(--accent-blue);">distrust</a>, <a href="./index.html#/time-spend" style="color: var(--accent-blue);">time spent</a>, and <a href="./index.html#/b2b-pains" style="color: var(--accent-blue);">B2B issues</a>.</p>

<div class="chosen-grid chosen-grid--small tile-text-match-summary" style="grid-template-columns: repeat(2, 1fr); gap: 10px; align-items: stretch; margin-top: 2px; width: 95%; margin-left: auto; margin-right: auto;">
  <div class="chosen-tile chosen-tile--green">
    <div>
      <p class="chosen-tile-label">1 Unscoped AI output</p>
      <div class="chosen-tile-body">
        <p style="line-height: 1.32; text-align: center;">AI diffs lack clear boundaries.</p>
      </div>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <div>
      <p class="chosen-tile-label">2 Post-generation review burden</p>
      <div class="chosen-tile-body">
        <p style="line-height: 1.32; text-align: center;">Reviews slow down after AI generates</p>
      </div>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin: 12px auto 0 auto; width: 95%; box-sizing: border-box; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Takeaway:</strong> Primary bet: unscoped AI output - strongest entry point because it constrains diffs before review, not after. Fallback: post-generation review burden - activates if month 1 gate fails (no validated hypothesis + not enough committed design partners). Pivot decision happens before MVP build.</p>
</div>

Notes:
Для того, чтобы рассмотреть ситуацию с непрозрачность AI разработки с разрых сторон, я проанализировал 3 источника: данные о проблемах доверия из исследований Stakeoverflow; исследованеи Microsoft о желаемом и фактическом распределении времени разработчика; боли b2b - продуктовых компаний, упомянутые в публичных источниках. По клику на гиперссылки есть слайды с более разобором списком направлений и источников.

По результату я приоритеризировал 2 основных направления: незапланированный AI OUTPUT и доп усилия на ревью после генерации.

В качестве основного направления я выбраю UNSCOPED AI OUTPUT, потому что review assist оптимизирует обнаружение проблем, но не предотвращает их. Если diff вышел за scope, даже идеальный review tool просто быстрее покажет, что всё плохо. Control нужен выше в рамках этой воронки воркфлоу. Review Assist я оставляю как fallback.

---
<!-- .slide: id="target-niche" -->

## WHAT: Target Niche

<div style="width: 90%; margin: 6px auto 10px auto; background: #1a1a1a; border-left: 4px solid #81c784; border-radius: 4px; padding: 8px 12px; text-align: left; position: relative; box-sizing: border-box; display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center;">
  <img src="Personas/Director.jpg" alt="Addy Osmani portrait" style="width: 40px; height: 40px; border-radius: 6px; border: 1px solid rgba(129, 199, 132, 0.45); object-fit: cover; display: block;">
  <div style="position: relative;">
    <div style="position: absolute; top: -5px; left: -1px; font-size: 1.8em; color: rgba(129, 199, 132, 0.2); font-family: serif; line-height: 1; pointer-events: none;">&ldquo;</div>
    <p style="margin: 0 0 3px 0; padding-left: 10px; font-size: 0.53em; line-height: 1.35; color: #e0e0e0; font-style: italic;">"AI may change how we do code reviews… The diff tells you what shipped. The conversation tells you why."</p>
    <p style="margin: 0; padding-left: 10px; font-size: 0.47em; color: var(--text-muted);"><a href="https://x.com/addyosmani/status/2011338548763664475" target="_blank" style="color: var(--accent-blue); text-decoration: none;">(c)</a> Addy Osmani, Director, Google Cloud AI</p>
  </div>
</div>

<div class="chosen-grid chosen-grid--2col chosen-grid--small tile-text-match-summary" style="width: 90%; margin-left: auto; margin-right: auto;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Early Adopters <span class="metric-badge">A</span></p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Who:</strong> Tech Leads &amp; Senior Engineers</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Where:</strong> Teams 10-50 devs, production JB IDE</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Problem:</strong> Unscoped AI diffs → review bottlenecks</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Trigger:</strong> 3+ review cycles on a single PR</p>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Scaling Stage <span class="metric-badge">A</span></p>
    <div class="chosen-tile-body">
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Who:</strong> Engineering Managers, Directors, Security</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Where:</strong> 100+ dev orgs, compliance pressure</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Problem:</strong> No standard for AI governance</p>
      <p style="margin-bottom: 5px;"><strong style="color: var(--r-main-color);">Trigger:</strong> AI policy violation or incident</p>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 10px; width: 90%; margin-left: auto; margin-right: auto;">
  <p><strong>Takeaway:</strong> We start narrow - Tech Leads feeling AI review pain in JB IDEs - and expand to org-wide governance once value is proven.</p>
</div>

<ul class="distrust-notes" style="margin: 10px auto 0 auto; width: 90%;">
  <li>Inputs so far: 1 exploratory interview, desk research, competitor pattern review. Systematic validation: Month 1.</li>
</ul>

Notes:
Эту боль хорошо резюмирует цитата Addy Osmani: именно непрозрачность того, что именно и почему было изменено при AI разработке, снижает доверие и делает AI-review болезненным.

Cделаем допущение и в качестве early adopters возьмем Tech Leads и Senior Engineers в относительно небольших компаниях на 10-50 разработчиков, работающих в JetBrains IDE, где unscoped AI diffs создают bottleneck в review. Триггер здесь - это три и более цикла review на одном PR.

Дальше есть понятный второй этап масштабирования, это engineering managers, directors и security/compliance организации, где проблема уже не только в review, а в отсутствии стандарта AI governance. Сначала нужно доказать ценность продукта.

---
<!-- .slide: id="why-competitor-landscape" -->

## WHY: Competitor Landscape

<div class="chosen-grid chosen-grid--small tile-text-match-summary" style="grid-template-columns: repeat(3, 1fr); width: 95%; margin: 0 auto;">
  <div class="chosen-tile" style="display: flex; flex-direction: column;">
    <p class="chosen-tile-label" style="color: #10b981; line-height: 1.12;">
      <span style="display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.85;">Direct</span>
      <span style="display: block;">Spec-driven</span>
    </p>
    <div class="chosen-tile-body" style="display: flex; flex-direction: column; flex: 1;">
      <p style="margin: 0 0 6px 0;">&nbsp;</p>
      <p style="margin-top: 0; margin-bottom: 8px; color: rgba(255,255,255,0.7);"><a href="https://speckit.org/" target="_blank" style="color: var(--accent-blue);">Spec Kit</a>, <a href="https://kiro.dev/" target="_blank" style="color: var(--accent-blue);">Kiro</a>, <a href="https://docs.bmad-method.org/" target="_blank" style="color: var(--accent-blue);">BMAD</a>, <a href="https://codespeak.dev/" target="_blank" style="color: var(--accent-blue);">CodeSpeak</a>, <a href="https://openspec.dev/" target="_blank" style="color: var(--accent-blue);">OpenSpec</a>, <span style="color: rgba(147,197,253,0.72);"><a href="https://www.task-master.dev/" target="_blank" style="color: rgba(147,197,253,0.72);">Taskmaster</a>, <a href="https://stately.ai/" target="_blank" style="color: rgba(147,197,253,0.72);">Stately</a>, <a href="https://buildermethods.com/agent-os" target="_blank" style="color: rgba(147,197,253,0.72);">Agent-OS</a>, <a href="https://ariel-frischer.github.io/autospec/" target="_blank" style="color: rgba(147,197,253,0.72);">Autospec</a>, <a href="https://specs.md/" target="_blank" style="color: rgba(147,197,253,0.72);">specs.md</a>, <a href="https://www.autok.dev/" target="_blank" style="color: rgba(147,197,253,0.72);">autok</a> / <a href="https://www.devplan.com/" target="_blank" style="color: rgba(147,197,253,0.72);">devplan</a></span></p>
      <p style="color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; margin-top: auto; text-align: left;">&bull; Strength: re-usable explicit spec artifact<br>&bull; Gap: weak IDE-native control, limited change containment, early maturity</p>
    </div>
  </div>
  <div class="chosen-tile" style="display: flex; flex-direction: column;">
    <p class="chosen-tile-label" style="color: #4fc3f7; line-height: 1.12;">
      <span style="display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.85;">Indirect</span>
      <span style="display: block;">IDE Assistants</span>
    </p>
    <div class="chosen-tile-body" style="display: flex; flex-direction: column; flex: 1;">
      <p style="margin: 0 0 6px 0;">&nbsp;</p>
      <p style="margin-top: 0; margin-bottom: 5px;"><strong><a href="https://cursor.com/" target="_blank" style="color: var(--accent-blue);">Cursor</a>, <a href="https://github.com/features/copilot" target="_blank" style="color: var(--accent-blue);">Copilot</a>, <a href="https://www.jetbrains.com/ai-assistant/" target="_blank" style="color: var(--accent-blue);">JB AI</a></strong></p>
      <p style="color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; margin-top: auto; text-align: left;">&bull; Strength: fast generation in the IDE<br>&bull; Gap: rules guide behavior but do not enforce persistent boundaries</p>
    </div>
  </div>
  <div class="chosen-tile" style="display: flex; flex-direction: column;">
    <p class="chosen-tile-label" style="color: #b388ff; line-height: 1.12;">
      <span style="display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.85;">Adjacent</span>
      <span style="display: block;">Post-facto &amp; Evals</span>
    </p>
    <div class="chosen-tile-body" style="display: flex; flex-direction: column; flex: 1;">
      <p style="margin: 0 0 6px 0;">&nbsp;</p>
      <p style="margin-top: 0; margin-bottom: 8px; color: rgba(255,255,255,0.7);"><a href="https://coderabbit.ai/" target="_blank" style="color: var(--accent-blue);">CodeRabbit</a>, <a href="https://www.qodo.ai/" target="_blank" style="color: var(--accent-blue);">Qodo</a>, <a href="https://docs.langchain.com/langsmith/home" target="_blank" style="color: var(--accent-blue);">LangSmith</a>, <a href="https://www.datadoghq.com/product/llm-observability/" target="_blank" style="color: var(--accent-blue);">Datadog LLM</a></p>
      <p style="margin: 0 0 6px 0;">&nbsp;</p>
      <p style="color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; margin-top: auto; text-align: left;">&bull; Strength: catches issues after generation<br>&bull; Gap: improves detection, not prevention</p>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin: 12px auto 0 auto; width: 95%; box-sizing: border-box; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Takeaway:</strong> Competition is fragmented: spec tools own planning artifacts, IDE assistants own generation speed, and post-facto tools own detection. Our entry point is IDE-native pre-merge control via spec-linked change containment.</p>
</div>

Notes:
Конкурентное поле с точки зрения нашей Core JTBD: когда инженеры используют AI в проде, им важны предсказуемость и контроль, чтобы быстрее выпускать продукт с уверенностью.

Рассмотрим прямых, непрямых конкурентов и тех, кто решают смежные джобы. Прямые конкуренты, spec-driven tools вроде Kiro, Spec Kit, CodeSpeak позволяют работать относительно подготовленного артефакта. Непрямые конкуренты, Cursor, Copilot, Antogravity, Codex, Claude Code, JetBrains AI, владеют скоростью генерации и лидируют всю индустрию, но не создают устойчивых boundary controls. Продукты со смешанными джобами, например CodeRabbit, Qodo, LangSmith, работают в первую очередь с тем, чтобы находить и помогать решать проблемы AI-разработки постфактум.

Ключевой вывод здесь в том, что почти никто не делает IDE-native pre-merge control основным продуктовым обещанием. Spec-tools помогают планировать, IDE assistants помогают генерировать, review tools помогают обнаруживать. Но почти никто не ограничивает diff до того, как он доходит до reviewer. Именно в этот gap и встает наш продукт.

---
<!-- .slide: id="learn-and-steal" -->

## WHY: Learn & Steal

<div class="chosen-grid chosen-grid--2col chosen-grid--small">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Git-Native Markdown</p>
    <p class="chosen-tile-body">Open and AI-friendly standard (SpecKit, BMAD). Zero vendor lock-in.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Bi-Directional Sync</p>
    <p class="chosen-tile-body">CodeSpeak validates direction. Our edge: code remains primary artifact.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">IDE-Native Surface</p>
    <p class="chosen-tile-body">Web-first creates context switch. Keep devs in-IDE.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Persistent Steering</p>
    <p class="chosen-tile-body">Already table stakes (Cursor Rules, CLAUDE.md, Kiro). Our edge: enforcement + drift detection on top.</p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 15px;">
  <p><strong>Takeaway:</strong> The market is converging on four useful patterns: Git-native specs, IDE-native workflow, persistent steering, and bi-directional sync. Our bet is to combine them into a control layer, not just a documentation layer.</p>
</div>

Notes:
При этом рынок уже явно сформировал нескольких полезных паттернов, которые нет смысла изобретать заново. Первый, Git-native Markdown для specs, открытый и AI-friendly формат без vendor lock-in. Второй, bi-directional sync между code и specs, который подтверждает, что двусторонняя связь действительно работает. Третий, web-first tools создают фрикшен, так как надо переключаться между контекстами. И четвертый, использование persistent steering, то есть постоянные правила и ограничения, которые не исчезают после одной chat-сессии.

Наша ставка в том, чтобы собрать эти четыре паттерна в единый control layer. Не просто слой документации, а слой управления с возможностью прозрачно отследить изменения поверх него.

---
<!-- .slide: id="competitive-approaches" -->

## WHY: Approaches

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 14px;">TOP-3 approaches prioritized across <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=549312952#gid=549312952&range=A1" target="_blank" style="color: var(--accent-blue);">observed solutions:</a></p>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 10px; align-items: stretch; margin-top: 2px; width: 95%; margin-left: auto; margin-right: auto;">
  <div class="chosen-tile chosen-tile--green" style="display: flex; flex-direction: column; justify-content: space-between; min-height: 190px;">
    <div>
      <p class="chosen-tile-label">1 SPEC-DRIVEN CONTROL</p>
      <p class="chosen-tile-body"><br><strong>Proactive, pre-merge.</strong><br>Prevents ambiguity before generation.<br>Turns intent into persistent, reviewable constraints.</p>
    </div>
    <p style="margin-top: 10px;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #6ee7b7; border: 1px solid rgba(110, 231, 183, 0.45); background: rgba(16, 185, 129, 0.15);">Primary bet</span></p>
  </div>

  <div class="chosen-tile" style="display: flex; flex-direction: column; justify-content: space-between; min-height: 190px; border: 1px solid rgba(96, 165, 250, 0.42); background: rgba(37, 99, 235, 0.12);">
    <div>
      <p class="chosen-tile-label">2 OBSERVABILITY &amp; EVALS</p>
      <p class="chosen-tile-body"><br><strong>Reactive, post-execution.</strong><br>Detects drift, regressions, and failures after execution.<br>Best for validation, not primary control.</p>
    </div>
    <p style="margin-top: 10px;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #93c5fd; border: 1px solid rgba(147, 197, 253, 0.45); background: rgba(59, 130, 246, 0.14);">Complementary</span></p>
  </div>

  <div class="chosen-tile" style="display: flex; flex-direction: column; justify-content: space-between; min-height: 190px; border: 1px solid rgba(248, 113, 113, 0.35); background: rgba(127, 29, 29, 0.18); opacity: 0.9;">
    <div>
      <p class="chosen-tile-label">3 REVIEW &amp; DEBUG ASSIST</p>
      <p class="chosen-tile-body"><br><strong>Reactive, post-generation.</strong><br>Reduce manual review effort post-generation.<br>Useful as a fallback if spec authoring friction is too high.</p>
    </div>
    <p style="margin-top: 10px;"><span style="display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 0.7em; line-height: 1.2; color: #fca5a5; border: 1px solid rgba(252, 165, 165, 0.45); background: rgba(127, 29, 29, 0.25);">Fallback</span></p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin: 12px auto 0 auto; width: 95%; box-sizing: border-box; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Decision:</strong> Start with spec-driven control as the initial entry point.<br><strong>Why:</strong> The core problem appears before merge, when change scope is unclear. Spec-driven control constrains the diff upstream; observability is better used later to validate drift.</p>
</div>

<ul class="distrust-notes" style="margin-top: 12px;">
<li>Estimates are expert-based and assumed.<span class="metric-badge">A</span> <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=549312952#gid=549312952&range=A1" target="_blank">Details →</a></li>
<li>Note: IDE-native steering files (Cursor Rules, CLAUDE.md, Windsurf Memory) partially solve persistent context but lack spec enforcement, drift detection, and structured generation pipelines.</li>
</ul>

Notes:
Ранее мы выбрали направление - UNSCOPED AI OUTPUT. Теперь давайте расмотрим типы решений, которые уже есть на рынке. Это три основных подхода.

Spec-driven control - основной выбор, потому что он снимает ambiguity до генерации и превращает нашу потребость в проверяемые ограничения, которыми мы можем управлять. Observability & evals - дополняющий слой, он лучше работает для проверки drift и деградации уже после выполнения. Review & Debug Assist - fallback, если окажется, что создание спецификаций в реальном workflow создает дополнительный фрикшен и не подойдут другие решения, например code to spec.

Приоритеризируем spec-driven control, тк ключевая проблема появляется до merge, в тот момент, когда scope изменения еще неясен. Значит, и контрольная точка должна находиться выше по воронке workflow, а не после выполнения.

---
<!-- .slide: id="why-specs-not-just-models" -->

## WHY: Why Specs, Not Just Better Models

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(2, 1fr); gap: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Better Models Are Not Boundaries</p>
    <p class="chosen-tile-body">Better models can reduce mistakes, but they do not create enforceable boundaries. The missing layer is workflow control, not just model quality.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Specs As Control Plane</p>
    <p class="chosen-tile-body">Specs create persistent intent, scope boundaries, and approval points that survive beyond a chat session.</p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px; padding: 10px 14px; border-left: 4px solid #34d399; text-align: left;">
  <p style="margin: 0; font-size: 0.62em; color: var(--text-main);"><strong>Takeaway:</strong> The primary problem is not smarter generation, but governed change.</p>
</div>

Notes:
Посмотрим на наше решение критически. А не решат ли все просто лучшие модели? Да, но не полностью. Более сильные модели могут уменьшить число ошибок, но они не предоставляют инструмента для управления ограничениями output-а. Например, модель может стать умнее, но она все равно не гарантирует, что не затронет файлы вне согласованного scope.

Недостающий слой здесь именно workflow control. Формализованная задача, границы scope и точки одобрения, которые живут дольше одной chat-сессии. Именно это и предоставляет specs-driven dev. То есть проблема не в том, что генерация недостаточно умная, а в том, что изменения должны быть управляемыми.

---
<!-- .slide: id="why-summary-v3-copy" -->

## WHY: Summary

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: 1fr; gap: 8px; margin-top: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Decision Summary</p>
    <div>
      <p class="chosen-tile-body" style="margin: 0 0 4px 0;"><strong>Thesis:</strong> We win if teams can predict PR review outcome before review, not after.</p>
      <p class="chosen-tile-body" style="margin: 0 0 4px 0;"><strong>Why now:</strong> AI adoption is <a href="./index.html#/adoption-paradox" style="color: var(--accent-blue); text-decoration: none;">90%, distrust is 46% (+15pp YoY)</a>.</p>
      <p class="chosen-tile-body" style="margin: 0 0 4px 0;"><strong>Why us:</strong> This entry point builds on JetBrains’ IDE and PSI advantage, complements the existing AI portfolio. <a href="./index.html#/jb-strategic-fit" style="color: var(--accent-blue); text-decoration: none;">JB Strategic Fit</a></p>
      <p class="chosen-tile-body" style="margin: 0;"><strong>How we win:</strong> Start with Tech Leads at 10-50 dev teams, prove paid pilot outcomes by month 3-4, then expand via JetBrains distribution.</p>
    </div>
  </div>
</div>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Market Size <span class="metric-badge">A</span></p>
    <p class="chosen-tile-body">Top-down targets a <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=856599423#gid=856599423&range=A1" target="_blank" style="color: var(--accent-blue); text-decoration: none;">$171.85M SOM</a> (5% of $4.91B). Bottom-up Year 1 base scenario estimates a <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=A1" target="_blank" style="color: var(--accent-blue); text-decoration: none;">$0.93M exit run-rate</a> <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=194025656#gid=194025656&range=C29" target="_blank" style="color: var(--accent-blue); text-decoration: none;">(~0.54% SOM)</a>, reflecting early funnel ramp versus steady-state.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Differentiation</p>
    <p class="chosen-tile-body">IDE-native spec↔code plus scope checks makes PR outcomes predictable before review. <a href="./index.html#/differentiation">Differentiation</a></p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Monetization</p>
    <p class="chosen-tile-body">Free for individuals and OSS trust level. Paid at team level when shared controls and PR/CI integrations are needed. <a href="./index.html#/pricing-monetization">Monetization</a> & <a href="./index.html#/growth-loops">Growth Loops</a></p>
  </div>
</div>

Notes:
Давайте суммаризируем то, что мы прошли и обсудим дополнительные аргументы, которые должны повысить нашу увереннось в выбранном направлении и походе.

Тезисно: мы выигрываем, если команда может предсказать outcome PR-review еще до review, а не разбираться с проблемой уже после. Это актуально сейчас, так как видно, что adoption AI уже 90%, но недоверие выросло так, что его выражает половина респондетов. И недоверие растет год к году несмотря на развитие качества моделей. Это должно получиться именно у Jet Brains, так как это ставка на преимущество JetBrains в IDE workflow и PSI-контексте. Также продукт хорошо встраивается и усиливает текущий AI-портфель, так как Bonsai усиливает текущие продукты JB и добавляет слой контроля, а не конкурирует с generation.

Как мы выигрываем. Мы начинаем с Tech Leads в командах на 10-50 разработчиков, доказываем outcome на платных pilot’ах к третьему-четвертому месяцу, а дальше расширяемся через дистрибуцию JetBrains. На этом же слайде я коротко показываю market size, differentiation и monetization logic. Полный разбор, как обычно, вынесен в appendix.

---
<!-- .slide: id="golden-path" -->

## HOW: Alex <img src="Personas/photo_2026-03-12_19-49-00.jpg" alt="Alex" style="width: 0.95em; height: 0.95em; border-radius: 50%; vertical-align: -0.08em; margin: 0 0.14em 0 0.08em; object-fit: cover;"> "Golden" Path <span class="metric-badge">A</span>

<div id="golden-path-steps" class="distrust-table-wrapper">
  <table class="distrust-table" style="table-layout: fixed; width: 100%; font-size: 0.43em;">
    <colgroup>
      <col style="width: 18%;">
      <col style="width: 41%;">
      <col style="width: 41%;">
    </colgroup>
    <thead>
      <tr>
        <th>Layer</th>
        <th>Before</th>
        <th>After</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Start</strong></td>
        <td>Junior asks AI to refactor auth directly, with no explicit contract.</td>
        <td>Junior writes a spec first, then generates from it.</td>
      </tr>
      <tr>
        <td><strong>Generation</strong></td>
        <td>AI returns a ~400-line unscoped diff.</td>
        <td>AI returns a scoped diff within the approved change boundaries.</td>
      </tr>
      <tr>
        <td><strong>Review</strong></td>
        <td>Blind line-by-line review; intent vs net-new code is unclear.</td>
        <td>Reviewer checks diff against spec in IDE; scope violations are blocked.</td>
      </tr>
      <tr class="highlight-row">
        <td style="width: 18%;"><strong>Outcome</strong></td>
        <td style="width: 41%;"><span style="color: #f87171; font-weight: 700;">~45 min</span>, "Request Changes", re-prompt loop.</td>
        <td style="width: 41%;"><span style="color: #4ade80; font-weight: 700;">~7 min</span>, PR-ready merge with traceability in Git.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 15px;">
  <p><strong>Result:</strong> Same task, same people - but the control point shifts from "review the output" to "verify against the contract".</p>
</div>

Notes:
Теперь давайте приземлим это в конкретный workflow. Здесь показан путь нашего респондента Александра, до и после использования нашего будущего продукта. До этого junior напрямую просит AI сделать auth refactor без явного контракта. AI возвращает diff, которого не было в скоупе примерно на 400 строк. Reviewer вынужден идти по строкам вручную, а задача и новый код плохо соотносятся друг с другом. Итог, Request Changes, новый prompt и повтор цикла.

После, при использовании продукта, junior сначала пишет spec, а потом генерирует изменения на ее основе. AI возвращает diff уже внутри согласованных границ, указанных в spec. Reviewer сравнивает результат со spec прямо в IDE, а нарушения scope блокируются. В итоге задача, люди и контекст те же самые, но исход меняется: мы экономим время, токены и энергию команды и получаем merge, готовый к Pull Request.

Здесь важно, что цифры пока являются допущениями, поэтому они помечены и должны быть валидированы в первых версиях продукта с пользователями. Но сам ключевой сдвиг уже понятен: контрольная точка смещается с review output на проверку against spec до review.

---

<!-- .slide: id="mvp-definition-simplified" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: MVP (month 3-4)</h2>
<p class="slide-subtitle" style="margin-bottom: 8px;">Product Definition</p>

<div class="chosen-grid chosen-grid--2col chosen-grid--small tile-text-match-summary">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">What It Is</p>
    <p class="chosen-tile-body">JetBrains IDE plugin that turns a spec (repo-native Markdown) into controlled code changes, with in-IDE review and traceability, so teams ship faster without unscoped diffs.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Who It Is For (MVP users)</p>
    <p class="chosen-tile-body">A small set of design partner teams on real JetBrains IDE repos, where scoped changes are common and review cycles are costly.</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Core Capabilities</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Spec-aware workflow (not a Markdown editor): run/validate/apply from spec in IDE.</li>
        <li>Change containment: hard scope boundaries + stop/ask on violations.</li>
        <li>In-IDE diff review with approve/apply loop.</li>
        <li>Traceability: links spec to diffs/commits + PR-ready summary.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Not In MVP</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>Full Code → Spec automation (validated via existing tools first).</li>
        <li>Broad language/framework coverage and edge cases.</li>
        <li>Full org governance (roles, audit, policy management at scale).</li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p>This scope is sufficient to prove the core hypothesis: spec-linked reviews are faster than blind reviews</p>
</div>

Notes:
MVP я определяю достаточно узко. Это JetBrains IDE plugin, который превращает spec, то есть Markdown-файл, в контролируемые code changes с review внутри IDE и полной отслеживаемость. Пользователь MVP, это небольшой число design partner teams на реальных JetBrains repos, где scoped changes часты, а review cycles дорогие.

В ядро MVP входят четыре вещи. Spec-aware workflow внутри IDE, а не просто редактор Markdown. Change containment через PSI-based анализ: plugin сравнивает файлы и символы в diff с разрешённым scope из spec и блокирует commit при выходе за границу. Именно то, что не позволит повториться ситуации Александра с лишними зависимостями и файлами. IDE diff review с approve/apply loop. И отслеживаемость, которая связывает spec, diff и commits.

Что сознательно не входит в MVP: полная автоматизация code-to-spec, широкое покрытие языков и edge cases, а также full org governance. С этим MVP хотим проверить главную гипотезу: spec-linked review значимо быстрее и предсказуемее, чем blind review.

---
<!-- .slide: id="metrics" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: Key Metrics</h2>

<div class="chosen-grid chosen-grid--2col chosen-grid--small tile-text-match-summary" style="text-align: left; grid-template-columns: 55% 45%;">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">1. NSM & Engagement</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>NSM:</b> Active users/wk with ≥1 spec-linked merge <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Engagement:</b> Activation to 1st merge, N-day retention, WAU/MAU <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Expansion:</b> % org with X+ users with ≥1 spec-merge <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Velocity:</b> Lead time & deployment frequency <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">2. Monetization</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>New MRR:</b> Activation to paid, ARPU, Churn (IC/seats) <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Attributed JB MRR:</b> Attach rate (JB paid with product), Cohort ARPU & Churn <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">3. Guardrails & Basic Quality</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>Safety:</b> CR to core JB actions, Sec/privacy incidents <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Quality:</b> False positive rate, added latency/Time to PR <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Drift:</b> Drift rate & severity, prevented incidents <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Qualitative:</b> CSAT & User Interviews on Spec View <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">4. Value & Outcomes</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><b>Cost:</b> Token spend per successful PR-ready outcome <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Quality:</b> % PRs passing checks on 1st try <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Scope Control:</b> Unscoped diff / scope-violation rate <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
        <li><b>Velocity:</b> Median time to PR-ready (from spec approved) <span style="display: inline-block; width: 8px; height: 8px; margin-left: 6px; border-radius: 2px; background: #22c55e; vertical-align: middle;"></span><span style="display: inline-block; width: 8px; height: 8px; margin-left: 2px; border-radius: 2px; background: #3b82f6; vertical-align: middle;"></span></li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> Metrics are tied to roadmap gates: month 1 qualitative validation + design partner recruitment, month 2 pilot agreements with concrete test plans, month 3-4 measurable MVP impact with design partners, month 5-6 commercial repeatability.</p>
</div>

<div class="distrust-notes" style="margin-top: 8px;">
  <span style="display: inline-block; width: 8px; height: 8px; border-radius: 2px; background: #22c55e; vertical-align: middle; margin-right: 6px;"></span>MVP stage metric,&nbsp;
  <span style="display: inline-block; width: 8px; height: 8px; border-radius: 2px; background: #3b82f6; vertical-align: middle; margin: 0 6px 0 10px;"></span>Scale stage metric.
</div>

Notes:
North Star - weekly active users с хотя бы одним spec-linked merge. Две gate-метрики для MVP: time-to-PR-approval и first-pass approval rate.

На слайде можно увидеть больше метрик. Они разделены по группам и помечены цветами в зависимости от приминимости на этапах MVP и Scale.

---
<!-- .slide: id="pricing-monetization" -->

## HOW: Monetization <span class="metric-badge">A</span>

<div class="chosen-grid chosen-grid--small tile-text-match-summary" style="grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px; text-align: left;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">What is free vs paid</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li><strong>OSS:</strong> spec format, validator, examples.</li>
        <li><strong>Free:</strong> single-user, small-scope workflow.</li>
        <li><strong>Paid team:</strong> templates, controls, visibility, PR/CI integrations, change containment.</li>
      </ul>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Commercial sequence</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li><strong>month 2:</strong> 3+ pilot agreements with concrete test plans.</li>
        <li><strong>month 3-4:</strong> paid pilots after plugin MVP.</li>
        <li><strong>month 5-6:</strong> commercial repeatability and expansion via JetBrains ecosystem.</li>
      </ul>
    </div>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Signals the model works</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px;">
        <li>1 paid conversion or 2 pilots entering procurement.</li>
        <li>One team expands inside the org.</li>
        <li>Clear package/pricing fit for team-level controls.</li>
      </ul>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Decision:</strong> Keep individual entry free, monetize team-level control (shared templates, governance visibility, PR/CI integration), and start charging at paid pilot stage once MVP value is proven.</p>
</div>

Notes:
Что касается монетизации. В open-source я бы оставил spec format, validator и examples, чтобы снизить недоверие и расширить верх воронки. Free tier, это single-user и небольшой workflow, чтобы достичь aha moment. Платный уровень начинается там, где появляется командная ценность: shared templates, controls, visibility, PR/CI integrations и change containment. Так же стоит рассмотреть вхождение продукта в существующие платные продукты JB.

Я делаю допущение, что на втором месяце я хочу получить pilot agreements с design partners: кто sponsor, какой use case, какие success metrics и какой procurement path. А платные pilot’ы запускать уже после появления рабочего MVP, то есть в третий-четвертый месяц.

---
<!-- .slide: id="roadmap" -->

## HOW: Roadmap <span class="metric-badge">A</span>

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%; font-size: 0.43em;">
  <colgroup>
    <col style="width: 14%;">
    <col style="width: 21.5%;">
    <col style="width: 21.5%;">
    <col style="width: 21.5%;">
    <col style="width: 21.5%;">
  </colgroup>
  <thead>
    <tr>
      <th></th>
      <th class="center" style="background: rgba(34, 197, 94, 0.09);">month 1</th>
      <th class="center" style="background: rgba(34, 197, 94, 0.13);">month 2</th>
      <th class="center" style="background: rgba(34, 197, 94, 0.17);">month 3-4</th>
      <th class="center" style="background: rgba(34, 197, 94, 0.21);">month 5-6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Phase</strong></td>
      <td style="background: rgba(34, 197, 94, 0.09);"><strong>Trust</strong></td>
      <td style="background: rgba(34, 197, 94, 0.13);"><strong>Design Partner Commitment</strong></td>
      <td style="background: rgba(34, 197, 94, 0.17);"><strong>MVP Launch</strong></td>
      <td style="background: rgba(34, 197, 94, 0.21);"><strong>Scale</strong></td>
    </tr>
    <tr>
      <td><strong>Goal</strong></td>
      <td style="background: rgba(34, 197, 94, 0.09);">Core hypothesis validated + 3+ design partner teams recruited</td>
      <td style="background: rgba(34, 197, 94, 0.13);">3+ pilot agreements with concrete test plans</td>
      <td style="background: rgba(34, 197, 94, 0.17);">MVP live with 3+ design partner teams + measurable impact</td>
      <td style="background: rgba(34, 197, 94, 0.21);">Commercial repeatability: conversion/procurement + expansion + pricing fit</td>
    </tr>
    <tr>
      <td><strong>Gate to next</strong></td>
      <td style="background: rgba(34, 197, 94, 0.09);">&ge;8 interviews + baseline captured (calculated) on all 3 design-partner teams using the same metrics (review time, PR iterations, scope violations)</td>
      <td style="background: rgba(34, 197, 94, 0.13);">3 pilot agreements with sponsor, success metrics, timeline, and procurement path; prototype tests in &ge;2 teams</td>
      <td style="background: rgba(34, 197, 94, 0.17);">MVP in 3+ teams; &ge;2 teams show measurable uplift in key outcomes</td>
      <td style="background: rgba(34, 197, 94, 0.21);">1 paid conversion or 2 pilots entering procurement + 1 org expansion + package/pricing fit evidence</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> Each phase requires passing a quantified gate before investment in the next.</p>
</div>

Notes:
Roadmap мы будем планировать вместе с командой, и пока это допущения. Month 1, это Trust. Month 2, Design Partner Commitment. Months 3-4, MVP Launch. Months 5-6, Commercial Repeatability, то есть scale: стандартизация workflow на уровне организации клиента и внутренняя дистрибуция через UGC spec и workflow templates. Для каждого этапа есть и цель, и gate для перехода дальше.

Я отдельно хочу уточнить, что я еще уточню с командой пороги с учетом специфики домена.

Поэтому gate на первый месяц такой: 8+ интервью и замерить текущий уровень (review time, PR iterations, scope violations) у 3 или более design partners. Дальше, на второй месяц, 3 pilot agreements, плюс Prototype tests хотя бы в двух командах. На третьем-четвертом месяце, MVP в 3+ командах и measurable uplift у минимум двух команд. На пятом-шестом месяце коммерческий gate, это 1 paid conversion or 2 пилотных закупки, плюс one org expansion и package/pricing fit evidence.

---
<!-- .slide: id="risks-mitigation" -->

## HOW: Risks & Mitigation

<p class="slide-subtitle" style="margin-top: 4px; margin-bottom: 10px;">Top risks below. Full Impact × Probability matrix is in <a href="./index.html#/risks-mitigation-main-appendix" style="color: var(--accent-blue);">appendix</a>.</p>

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%; font-size: 0.43em;">
  <colgroup>
    <col style="width: 18%;">
    <col style="width: 37%;">
    <col style="width: 37%;">
    <col style="width: 8%;">
  </colgroup>
  <thead>
    <tr>
      <th>Risk</th>
      <th>Why It Matters</th>
      <th>Mitigation</th>
      <th class="center">Priority</th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>PoC value</strong></td>
      <td>Spec-first may not prove repeatable value fast enough. If Month 1 fails to validate the core hypothesis with design partners, the thesis weakens.</td>
      <td>Run qualitative validation plus 3+ design partners, require evidence gate before MVP build, and switch entry point if outcomes do not outperform alternatives.</td>
      <td class="center score val-high">High</td>
    </tr>
    <tr>
      <td><strong>Partner speed</strong></td>
      <td>Not enough high-signal design partners fast enough.</td>
      <td>Warm network + OSS entry point.</td>
      <td class="center score val-med">Med</td>
    </tr>
    <tr>
      <td><strong>PSI complexity</strong></td>
      <td>Integration complexity can slow delivery.</td>
      <td>Kotlin-first, native PSI APIs.</td>
      <td class="center score val-med">Med</td>
    </tr>
    <tr>
      <td><strong>Dev friction</strong></td>
      <td>Adoption may feel too heavy for real workflows.</td>
      <td>Repo-native, zero-friction extraction, code-to-spec flow.</td>
      <td class="center score val-med">Med</td>
    </tr>
  </tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> The primary risk is failing to prove repeatable value for spec-first control in Month 1. Mitigation is explicit: qualitative evidence + 3+ design partners with a hard pivot gate before MVP build.</p>
</div>

Notes:
Главный риск - мы не сможем доказать repeatable value для spec-first control. Если это не подтвердится, то весь тезис ослабевает еще до того, как мы начали серьезно инвестировать в разработку. Поэтому mitigation здесь тоже жесткий и ранний: качественная валидация, 3+ design partner teams, явный evidence gate и возможность сменить core directions и подход до того, как мы строим полноценный plugin MVP.

Дальше есть еще несколько понятных рисков, скорость привлечения design partners, сложность PSI integration и потенциальное developer friction. У каждого есть свой mitigation, но по-настоящему критичен именно первый риск. Потому что если core value не повторяется. Полная матрица рисков с допущениями по оценке эффекта и вероятности по гиперссылке.

---

<!-- .slide: id="month1-actions" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: My 1st month actions</h2>

<div class="chosen-grid chosen-grid--small tile-text-match-summary" style="grid-template-columns: 0.9fr 24px 1.2fr 24px 0.9fr; gap: 6px; align-items: stretch; width: 100%; margin: 0 auto;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Week 1</p>
    <div class="chosen-tile-body">
      <p style="margin: 0 0 8px 0; font-weight: 700; color: var(--r-main-color); text-align: center;">Align &amp; Orient</p>
      <ul style="margin: 0; padding-left: 15px;">
        <li>Stakeholder alignment: map decision-makers, agree on success criteria.</li>
        <li style="margin-bottom: 0.9em;">Audit last 3 launches: what shipped, what moved metrics, what didn't.</li>
      </ul>
      <p style="margin: 6px 0 0 0; padding-top: 5px; border-top: 1px solid rgba(255,255,255,0.15);"><strong>DoD:</strong> Shared doc with aligned problem statement and known constraints.</p>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; color: #94a3b8;">
    <span style="font-size: 1.05em; line-height: 1;">&rarr;</span>
  </div>

  <div class="chosen-tile" style="border: 1px solid rgba(250, 204, 21, 0.45); background: rgba(234, 179, 8, 0.12);">
    <p class="chosen-tile-label" style="color: #facc15;">Weeks 2-3</p>
    <div class="chosen-tile-body">
      <p style="margin: 0 0 8px 0; font-weight: 700; color: var(--r-main-color); text-align: center;">Validate Problem &amp; Solution Direction</p>
      <ul style="margin: 0; padding-left: 15px;">
        <li>15 customer interviews -> synthesized pain points and willingness to pay.</li>
        <li style="margin-bottom: 1.8em;">Recruit 3+ design-partner teams, map core workflow, and capture baseline metrics (review time / PR iterations / scope violations).</li>
      </ul>
      <p style="margin: 6px 0 0 0; padding-top: 5px; border-top: 1px solid rgba(255,255,255,0.15);"><strong>DoD:</strong> Evidence brief + month 1 gate evidence (&ge;8 interviews + baseline captured (calculated) on all 3 design-partner teams using the same metrics: review time, PR iterations, scope violations).</p>
    </div>
  </div>

  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; color: #94a3b8;">
    <span style="font-size: 1.05em; line-height: 1;">&rarr;</span>
  </div>

  <div class="chosen-tile chosen-tile--red">
    <p class="chosen-tile-label">Week 4</p>
    <div class="chosen-tile-body">
      <p style="margin: 0 0 8px 0; font-weight: 700; color: var(--r-main-color); text-align: center;">Go / No-Go Gate</p>
      <ul style="margin: 0; padding-left: 15px;">
        <li>Present recommendation to leadership with evidence.</li>
        <li>Go -> draft roadmap + resourcing ask for next 90 days.</li>
        <li>No-Go -> document learnings, pivot thesis, or kill cleanly.</li>
      </ul>
      <p style="margin: 6px 0 0 0; padding-top: 5px; border-top: 1px solid rgba(255,255,255,0.15);"><strong>DoD:</strong> Decision made, next steps committed.</p>
    </div>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 15px;">
  <p><strong>30 days output:</strong> We will know whether spec-driven control creates repeatable value for real teams - backed by interview evidence, baseline workflow metrics, and committed design partners. If yes, we have a validated entry point and a resourced 90-day plan. If no, we pivot before spending engineering time on an MVP.</p>
</div>

Notes:
И в конце о том, что именно я делаю в первые 30 дней. Первая неделя, align and orient. Я быстро выравниваю stakeholders, фиксирую success criteria и разбираю исторические внедрения - что сработало, что не сработало и какие есть ограничения. Вторая и третья недели, validate. Здесь я провожу около 8 customer interviews, синтезирую pain points и willingness to pay, и параллельно набираю 3+ design partner teams, чтобы зафиксировать baseline метрики по текущему workflow и проверить сам сценарий. Четвертая неделя, Go / No-Go. Я приношу leadership recommendation, основанную на evidence.

В результате, у нас есть validated entry point и обоснованный план. Иначе мы сможем достаточно быстро развернуться в сторону другого направления или подхода. Спасибо.

---

<!-- .slide: id="appendix" -->

# Appendix

---
<!-- .slide: id="jb-strategic-fit" -->

## WHY: JetBrains Strategic Fit <span class="metric-badge">A</span>

<div class="chosen-grid chosen-grid--small" style="grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px;">
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Right to win</p>
    <p class="chosen-tile-body">JetBrains owns the IDE workflow and has PSI-native context.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Portfolio fit</p>
    <p class="chosen-tile-body">Bonsai complements AI Assistant and Junie by adding governance, not generation.</p>
  </div>
  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Business fit</p>
    <p class="chosen-tile-body">It increases enterprise retention and creates team-level attach potential.</p>
  </div>
</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> JetBrains is well positioned to own governed AI-assisted development, not just AI code generation.</p>
</div>

---
<!-- .slide: id="gtm" -->

<h2 style="font-size: 1.4em; margin-bottom: 5px;">HOW: GTM Strategy <span class="metric-badge">A</span></h2>

<div class="chosen-grid chosen-grid--2col chosen-grid--small tile-text-match-summary" style="text-align: left;">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">1. Pilot Teams & Early Adopters</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><strong>Target:</strong> JB Power Users, Tech Leads, DevEx.</li>
        <li><strong>Motion:</strong> "Golden path" to PR in 10 mins. <a href="./index.html#/golden-path">Details</a></li>
        <li><strong>Goal:</strong> Validate spec-first + diff control (change containment) via instrumented prototype before plugin MVP.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">2. Early Monetization</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><strong>Offer:</strong> Pilot agreement (scope, success metrics, sponsor, timeline, procurement path).</li>
        <li><strong>When we charge:</strong> paid pilots start once plugin MVP exists (month 3-4).</li>
        <li><strong>Model:</strong> Add-on to JB AI credits (shared quota).</li>
        <li><strong>Goal:</strong> Secure design partner commitment before MVP monetization.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">3. Scale Sales</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><strong>Distribution:</strong> JB IDE Promo, Toolbox, Marketplace.</li>
        <li><strong>Motion:</strong> PLG loop (Indiv. &rarr; Team org policy).</li>
        <li><strong>Goal:</strong> Zero-friction install to paid conversion.</li>
      </ul>
    </div>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">4. Market Standard</p>
    <div class="chosen-tile-body">
      <ul style="margin: 0; padding-left: 15px; margin-bottom: 4px;">
        <li><span class="metric-badge">A</span> <strong>OSS (risk mitigation first):</strong> Spec Format + validator + examples to widen partner funnel and reduce distrust; later OSS adds templates/hooks starter pack and compatibility assets.</li>
        <li><strong>Ecosystem:</strong> Marketplace for hooks and templates.</li>
        <li><strong>Enterprise:</strong> Hosted orchestration and governance.</li>
      </ul>
    </div>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> GTM sequencing is deliberate: prove workflow value, secure pilot agreements, convert to paid pilots, then scale through JetBrains distribution and OSS standardization.</p>
</div>

---
<!-- .slide: id="differentiation" -->

## WHY: Differentiation

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 80%;">
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
      <td><span class="metric-badge">A</span> PSI extracts structured signal at 100–300 tokens (70–90% saving). Compiler-grade structural parsing substantially reduces hallucination risk on structure-sensitive tasks. Not a permanent moat - a 12–18 month head start we convert into data and workflow lock-in.</td>
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
  <p>We turn AI-assisted changes into a more predictable and reviewable workflow for teams that need enterprise-grade control.</p>
</div>

<ul class="distrust-notes">
  <li>Note: PSI isn’t exclusive; defensibility compounds via accumulated spec data + workflow lock-in.</li>
</ul>

---
<!-- .slide: id="growth-loops" -->

## WHY: Growth Loops <span class="metric-badge">A</span>

<div class="chosen-grid chosen-grid--2col chosen-grid--small">

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Champion-driven adoption</p>
    <p class="chosen-tile-body">1 dev adds <code>/specs</code> → CI gates & PR checks appear → whole team interacts → other teams copy →</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Invite-The-Reviewer Loop</p>
    <p class="chosen-tile-body">Specs make PR intent clearer -> domain reviewers join earlier -> review quality and speed improve -> trust in spec-linked PRs rises -> more changes start with specs</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Multi-Repo Value Growth</p>
    <p class="chosen-tile-body">Reusable spec added to repo A → then repo B → better compatibility & fewer diffs → massive incentive to maintain</p>
  </div>

  <div class="chosen-tile chosen-tile--green">
    <p class="chosen-tile-label">Ecosystem Distribution</p>
    <p class="chosen-tile-body">More tool compatibility -> lower adoption friction -> more teams try the format -> more templates / hooks / integrations appear -> compatibility improves further</p>
  </div>

</div>

<div class="adoption-takeaway distrust-takeaway" style="margin-top: 12px;">
  <p><strong>Takeaway:</strong> The product has credible compounding paths: reusable review patterns, cross-repo templates, and ecosystem compatibility can turn single-team wins into team-to-team adoption. The scaling challenge is to prove one repeatable expansion loop first, then standardize it across repos and teams.</p>
</div>

---
<!-- .slide: id="distrust-issues" -->

## WHAT: Distrust issues

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 35%;">
<col style="width: 53%;">
<col style="width: 12%;">
</colgroup>
<thead>
<tr>
<th>Trust points (when utilizing AI)</th>
<th>Details</th>
<th class="center">Score <span class="metric-badge">A</span></th>
</tr>
</thead>
<tr class="highlight-row">
<td>Skepticism regarding code accuracy and quality</td>
<td>45.7% distrust AI (up 15.3 pp YoY). 75% would ask a person for help when they don’t trust AI answers. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center score val-high">9.0</td>
</tr>
<tr class="highlight-row">
<td>Increased review and debugging time</td>
<td>45% say debugging AI code is more time-consuming. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center score val-high">9.0</td>
</tr>
<tr>
<td>Concerns regarding security and vulnerabilities</td>
<td>&gt;60% frequently have ethical / security-related concerns about AI-generated code. <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[1]</a></td>
<td class="center score val-high">6.8</td>
</tr>
<tr>
<td>AI decision-making opacity and ambiguous accountability for errors</td>
<td>75% would ask a person for help when they don’t trust AI answers, keeping humans as final arbiters of correctness. <a href="https://arxiv.org/html/2502.18468v1" target="_blank">[1]</a> <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[2]</a></td>
<td class="center score val-med">3.0</td>
</tr>
<tr>
<td>Risk of engineering skill degradation</td>
<td>60% believe AI tools lead to less skilled developers (web-dev firstly). <a href="https://2025.stateofdevs.com/en-US/" target="_blank">[1]</a></td>
<td class="center score val-low">2.0</td>
</tr>
<tr>
<td>Fear of data leaks and privacy concerns</td>
<td>40% of security incidents involve AI (incident-level). &gt;80% report concerns about data security and privacy. Frequency=Low because measured via incidents. <a href="https://www.microsoft.com/en-us/security/blog/2024/11/13/microsoft-data-security-index-annual-report-highlights-evolving-generative-ai-security-needs/" target="_blank">[1]</a> <a href="https://survey.stackoverflow.co/2025/ai" target="_blank">[2]</a></td>
<td class="center score val-low">1.5</td>
</tr>
<tr>
<td>Legal uncertainty regarding copyrights and licensing for AI-generated code</td>
<td>Survey of 574 GenAI users: broad disagreement and uncertainty about output ownership and copyright risk. <a href="https://arxiv.org/html/2502.18468v1" target="_blank">[1]</a> <a href="https://arxiv.org/html/2411.10877v1" target="_blank">[2]</a></td>
<td class="center score val-low">1.5</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> Developers mainly don’t trust AI-generated code enough to ship it without extra time spent polishing, reviewing, and debugging.</p>
</div>

<ul class="distrust-notes">
<li>Score is subjectively estimated/measured based on synthesis of external report signals.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

---
<!-- .slide: id="time-spend" -->

## WHAT: Dev Time Spent

<div class="timespend-table-wrapper">
<table class="timespend-table">
<thead>
<tr>
<th>Activity</th>
<th class="center">Actual</th>
<th class="center">Ideal</th>
<th class="center">Gap</th>
<th class="center">Prob. <span class="metric-badge">A</span></th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="highlight-row">
<td>Security/Compliance</td>
<td class="center">11.5%</td>
<td class="center">3.1%</td>
<td class="center score">8.4%</td>
<td class="center val-med">Med</td>
<td>Opportunity to improve on the planning step</td>
</tr>
<tr class="highlight-row">
<td>Communication</td>
<td class="center">12.9%</td>
<td class="center">6.6%</td>
<td class="center score">6.4%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>Debugging</td>
<td class="center">11.2%</td>
<td class="center">7.5%</td>
<td class="center score">3.7%</td>
<td class="center val-high">High</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Customer Support</td>
<td class="center">7.5%</td>
<td class="center">4.0%</td>
<td class="center score">3.5%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>Env Setup</td>
<td class="center">3.8%</td>
<td class="center">1.5%</td>
<td class="center score">2.2%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Monitoring/Dashboard</td>
<td class="center">2.9%</td>
<td class="center">2.2%</td>
<td class="center score">0.7%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Task Mgmt (ADO)</td>
<td class="center">2.0%</td>
<td class="center">1.3%</td>
<td class="center score">0.7%</td>
<td class="center val-med">Med</td>
<td>Opportunity to automate via agent orchestration</td>
</tr>
<tr>
<td>Code Refactoring</td>
<td class="center">5.2%</td>
<td class="center">4.8%</td>
<td class="center score">0.5%</td>
<td class="center val-med">Med</td>
<td>Opportunity to keep useful and updated spec</td>
</tr>
<tr>
<td>Test Authoring</td>
<td class="center">4.8%</td>
<td class="center">5.2%</td>
<td class="center score">-0.3%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Documentation</td>
<td class="center">3.7%</td>
<td class="center">4.3%</td>
<td class="center score">-0.6%</td>
<td class="center val-med">Med</td>
<td>Automation already widely adopted</td>
</tr>
<tr>
<td>Mentoring/Onboarding</td>
<td class="center">2.6%</td>
<td class="center">3.7%</td>
<td class="center score">-1.1%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>Tech Presentations</td>
<td class="center">0.6%</td>
<td class="center">1.7%</td>
<td class="center score">-1.1%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr>
<td>PR/Code Review</td>
<td class="center">5.9%</td>
<td class="center">7.1%</td>
<td class="center score">-1.2%</td>
<td class="center val-low">Low</td>
<td>Human in the loop issue mostly depends on AI models base quality evolution</td>
</tr>
<tr>
<td>Learning New Tech</td>
<td class="center">2.5%</td>
<td class="center">6.6%</td>
<td class="center score">-4.0%</td>
<td class="center val-low">Low</td>
<td>-</td>
</tr>
<tr class="highlight-row">
<td>System Arch/Design</td>
<td class="center">8.9%</td>
<td class="center">15.4%</td>
<td class="center score">-6.5%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
<tr class="highlight-row">
<td>Coding</td>
<td class="center">13.9%</td>
<td class="center">25.2%</td>
<td class="center score">-11.2%</td>
<td class="center val-high">High</td>
<td>Reduce time spent on low-value work, boosting satisfaction, retention, and tenure.</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> The largest recoverable capacity sits upstream: planning, debugging, and compliance consume outsized time before code lands. The product bet is to make changes better scoped and more reviewable, so effort shifts from avoidable rework into Coding and System Architecture.</p>
</div>

<ul class="distrust-notes">
<li>Time spend data is based on <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/11/Time-Warp-Developer-Productivity-Study.pdf" target="_blank">Microsoft's Time-Warp Study</a>.</li>
<li>Prob.(Probability) = Probability to make a difference.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

---
<!-- .slide: id="b2b-pains" -->

## WHAT: B2B Pains

<div class="distrust-table-wrapper">
<table class="distrust-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 35%;">
<col style="width: 53%;">
<col style="width: 12%;">
</colgroup>
<thead>
<tr>
<th>B2B Pain (Engineering / Product Teams)</th>
<th>Details</th>
<th class="center">Score <span class="metric-badge">A</span></th>
</tr>
</thead>
<tbody>
<tr class="highlight-row">
<td>Delivery predictability and lead time variability</td>
<td>Unpredictable reviewers make dependent work impossible to forecast reliably. <a href="https://axify.io/blog/lead-time-in-software-development" target="_blank">[1]</a></td>
<td class="center score val-high">4.5</td>
</tr>
<tr class="highlight-row">
<td>Quality and reliability risk from software errors</td>
<td>Poor software quality costs US companies $2.08 trillion annually. <a href="https://raygun.com/blog/cost-of-software-errors/" target="_blank">[1]</a></td>
<td class="center score val-high">4.5</td>
</tr>
<tr>
<td>Documentation debt harming onboarding, satisfaction and speed</td>
<td>41% of developers report this as a major hindrance. 97% lose significant time to inefficiencies. <a href="https://www.atlassian.com/software/compass/resources/state-of-developer-2024" target="_blank">[1]</a></td>
<td class="center score val-med">3.0</td>
</tr>
<tr>
<td>Token Spent Optimization</td>
<td>On average, token consumption decreased by 15–20%. <a href="https://arxiv.org/html/2504.15989v2" target="_blank">[1]</a></td>
<td class="center score val-med">3.0</td>
</tr>
<tr>
<td>Developer burnout from cognitive load and on-call burden</td>
<td>83% of software engineers report feelings of burnout. <a href="https://www.softwareseni.com/developer-burnout-and-cognitive-load-in-the-devops-era/" target="_blank">[1]</a></td>
<td class="center score val-low">2.0</td>
</tr>
<tr>
<td>Productivity loss from technical debt waste</td>
<td>Developers waste on average 23% of their time due to technical debt. <a href="https://research.chalmers.se/publication/511450/file/511450_Fulltext.pdf" target="_blank">[1]</a></td>
<td class="center score val-low">1.5</td>
</tr>
<tr>
<td>Compliance overhead from AI and tooling</td>
<td>Compliance overhead increases 10–20% in regulated industries due to AI audit and privacy controls. <a href="https://www.softwareseni.com/the-real-economics-of-ai-coding-beyond-vendor-productivity-claims/" target="_blank">[1]</a></td>
<td class="center score val-low">1.5</td>
</tr>
</tbody>
</table>
</div>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> The clearest B2B pains are delivery unpredictability and quality risk. That makes controlled change, not faster generation, the strongest entry point for AI-assisted teams: reduce variance first, then scale output on top of a more reviewable workflow.</p>
</div>

<ul class="distrust-notes">
<li>Score is subjectively estimated based on external report signals.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
</ul>

---
<!-- .slide: id="stream-options-main-appendix" -->

## WHAT: Strategic Directions: detailed

<table class="score-table">
  <thead>
    <tr>
      <th>Direction</th>
      <th>Source</th>
      <th>ICE Score <span class="metric-badge">A</span></th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight-row">
      <td><strong>Unscoped AI output: code &amp; architecture</strong></td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>18.0</td>
    </tr>
    <tr>
      <td><strong>Post-generation review burden</strong></td>
      <td><span class="tag tag-pain-review">Distrust issues</span></td>
      <td>12.0</td>
    </tr>
    <tr>
      <td><strong>Spec Formalisation Assist</strong></td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>6.0</td>
    </tr>
    <tr>
      <td><strong>Quality and reliability risk</strong> from software errors</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>6.0</td>
    </tr>
    <tr>
      <td><strong>Security &amp; Compliance</strong> (proactive assist)</td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>4.0</td>
    </tr>
    <tr>
      <td><strong>Dev Env Simplification</strong></td>
      <td><span class="tag tag-time-spent">Time Spent</span></td>
      <td>4.0</td>
    </tr>
    <tr>
      <td><strong>Delivery time variability</strong> (accurate forecasting)</td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>4.0</td>
    </tr>
    <tr>
      <td><strong>Token Spent Optimization</strong></td>
      <td><span class="tag tag-b2b">B2B Pains</span></td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>

<div class="adoption-takeaway distrust-takeaway">
  <p><strong>Takeaway <span class="metric-badge">A</span>:</strong> Spec-driven control (AI-dev transparency) is the top-priority direction. Key risk: spec fatigue and enforcement resistance. Runner-up (Review &amp; Debug assist) becomes our fallback if ICP interviews disprove pre-hoc control preference.</p>
</div>

<ul class="distrust-notes">
<li>Scores are derived from the <a href="./index.html#/competitive-approaches">Core JTBD Landscape ICE framework</a>. Each direction is mapped to the closest approach and inherits its ICE Score. <a href="https://docs.google.com/spreadsheets/d/1dJaYTAPnEGoDGKNcPKwCtwqx5y4589aNeUF5R1wia-o/edit?gid=1907182755#gid=1907182755&range=A1" target="_blank">Calculations</a>.</li>
<li>All subjective/estimated parameters are marked with <span class="metric-badge">A</span>.</li>
<li>Directions are derived from the top issues across three evidence layers: <a href="./index.html#/distrust-issues">Distrust</a>, <a href="./index.html#/time-spend">Time Spent</a>, and <a href="./index.html#/b2b-pains">B2B Issues</a>.</li>
</ul>

---
<!-- .slide: id="risks-mitigation-main-appendix" -->

<h2>HOW: Risks & Mitigation</h2>

<div class="risk-table-container">
  <table class="risk-table">
    <thead>
      <tr>
        <th class="col-num">#</th>
        <th class="col-risk">Risk Name</th>
        <th class="col-mitigation">Mitigation Strategy</th>
        <th class="col-status">Impact <span class="metric-badge">A</span></th>
        <th class="col-status">Prob. <span class="metric-badge">A</span></th>
        <th class="col-score">Score <span class="metric-badge">A</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="col-num"><strong>0</strong></td>
        <td class="col-risk"><strong>PoC risk: we can't prove repeatable value for spec-first + diff control</strong></td>
        <td class="col-mitigation">Month 1: run qualitative validation + recruit 3+ design partner teams. Gate: &ge;8 interviews + baseline captured (calculated) on all 3 design-partner teams using the same metrics (review time, PR iterations, scope violations). If not, switch the entry point before building the plugin MVP.</td>
        <td class="col-status text-high"><strong>High</strong></td>
        <td class="col-status text-med"><strong>Med</strong></td>
        <td class="col-score"><strong>6</strong></td>
      </tr>
      <tr>
        <td class="col-num">1</td>
        <td class="col-risk">Partner risk: can't recruit enough high-signal design partners fast</td>
        <td class="col-mitigation">Two-track recruitment: (a) warm network for named companies, (b) OSS narrow scope (Spec Format + validator + examples) to widen the funnel. Use OSS to attract credible teams, collect spec samples, and convert top contributors into pilots.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">2</td>
        <td class="col-risk">PSI Engine Complexity</td>
        <td class="col-mitigation">Focus on JetBrains ecosystem (Kotlin first), leverage native PSI APIs for stability.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">3</td>
        <td class="col-risk">Developer Friction</td>
        <td class="col-mitigation">Zero-friction code-first extraction. Repo-native .md format lives in current workflow.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">6</td>
      </tr>
      <tr>
        <td class="col-num">4</td>
        <td class="col-risk">Competitor Entry</td>
        <td class="col-mitigation">Deep IDE-native PSI integration provides a semantic moat generic LLMs lack.</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">4</td>
      </tr>
      <tr>
        <td class="col-num">5</td>
        <td class="col-risk">Monetization risk: value is clear, but buyers don't approve budget / packaging is confusing</td>
        <td class="col-mitigation">month 2: 3+ pilot agreements (sponsor, success metrics, test plan, procurement path). month 3-4: paid pilots once MVP exists. month 5-6: 1 paid conversion or 2 pilots entering procurement, plus one org expansion and pricing/package fit evidence.</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-med">Med</td>
        <td class="col-score">4</td>
      </tr>
      <tr>
        <td class="col-num">6</td>
        <td class="col-risk">AI Hallucinations</td>
        <td class="col-mitigation">Human-in-the-loop "Approve" gate before syncing specs. High-precision prompt tuning.</td>
        <td class="col-status text-high">High</td>
        <td class="col-status text-low">Low</td>
        <td class="col-score">3</td>
      </tr>
      <tr>
        <td class="col-num">7</td>
        <td class="col-risk">Adoption Tax</td>
        <td class="col-mitigation">Strategic entry point: extract from existing code, don't force devs to write from scratch.</td>
        <td class="col-status text-med">Med</td>
        <td class="col-status text-low">Low</td>
        <td class="col-score">2</td>
      </tr>
    </tbody>
  </table>
</div>
