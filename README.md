# JetBrains Presentation Repository

Presentation workspace for the Bonsai deck (Reveal.js + Markdown).

## Main files

- `slides.md` - primary presentation content.
- `index.html` - Reveal.js entry point.
- `css/theme.css` - theme and slide styling.
- `Take-home-task.md` - assignment context and constraints.

## Repository structure

- `scripts/` - one-off maintenance/update scripts used during deck iterations.
- `docs/planning/` - planning drafts and intermediate structure versions.
- `docs/archive/` - backup/temporary files kept for reference.
- `Competitors&Market/` - research inputs and supporting market materials.
- `Examples/` - reference presentations.

## Run locally

```bash
npm run dev
```

Then open `http://localhost:8001`.

## Export to PDF (DeckTape)

```bash
npx decktape reveal http://127.0.0.1:8001/index.html output.pdf
```

If needed, run a local server first:

```bash
python3 -m http.server 4173
npx decktape reveal http://127.0.0.1:4173/index.html output.pdf
```

## Notes

- Keep presentation edits in `slides.md` and style updates in `css/theme.css`.
- Generated PDFs are intentionally ignored via `.gitignore`.
