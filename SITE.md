# Static Site Layer

This repository stays Markdown-first. The static site is an optional reading and navigation layer over the same files used for study in Cursor.

## Generator Choice

The site uses MkDocs Material because this workspace is documentation-shaped: course notes, syllabi, trackers, project reflections, and operating guides. MkDocs gives local search and browsable navigation without requiring hand-authored HTML or moving content out of its current folders.

## Source Of Truth

- Edit study content in the existing Markdown files.
- Do not duplicate notes, syllabi, trackers, or project reflections into HTML.
- Treat generated output as disposable; rebuild it from Markdown when needed.

## Local Study Site

The default `mkdocs.yml` configuration is for private local use. It includes operational documents such as the progress tracker so the site can act as a dashboard while studying.

## Site Tooling

Site dependencies are managed with `uv` in `pyproject.toml`.

- Run `uv sync` once to create the local environment.
- Run `uv run mkdocs serve` to preview the private/local study site.
- Run `uv run mkdocs build` to build the private/local site.
- Run `uv run mkdocs build -f mkdocs-public.yml` to build the restricted public-safe site.

## Public Boundary

Public builds must use `mkdocs-public.yml`.

Safe-by-default public areas:

- `README.md`, `PROGRAM.md`, `GUIDE.md`, `ROUTINES.md`, and this file.
- `core/` syllabi, notes, and project write-ups after manual review for personal details.
- `electives/` planning material after manual review.
- `capstone/` overview and selected showcase artifacts after manual review.
- `notes/` and `resources/` when they contain reusable frameworks or public links.

Private-only by default:

- `progress/` trackers and study logs.
- `meta/` metrics, operating logs, post-mortems, and AI disagreement logs.
- `rpl/` prior-learning records.
- Local environment files, scratch exports, credentials, and any generated site output.

Before publishing, run a fresh public build and review the generated pages for accidental personal, enrollment, credential, or performance details.
