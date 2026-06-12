# Udacity MBA in AI Product Management

Personal knowledge base and learning workspace for the [MBA in AI Product Management](https://www.udacity.com/learning-plan/mba-in-ai) — awarded by Woolf through the Udacity Institute of AI & Technology.

## Four layers

| Layer | Folder | Question |
|-------|--------|----------|
| Curriculum | `core/`, `electives/`, `capstone/` | What must I complete? |
| Knowledge | `notes/` (blank sheets per course) | What did I learn? |
| Progress | `progress/` | Where am I in the program? |
| Performance | `meta/` | How am I showing up? |

Full guide: **[GUIDE.md](./GUIDE.md)** · Cadence: **[ROUTINES.md](./ROUTINES.md)**

## Quick links

| Resource | Location |
|----------|----------|
| Program overview & requirements | [PROGRAM.md](./PROGRAM.md) |
| Master progress tracker | [progress/TRACKER.md](./progress/TRACKER.md) |
| Weekly study log | [progress/study-log.md](./progress/study-log.md) |
| Core curriculum | [core/](./core/) (each program has `SYLLABUS.md`) |
| Elective planning | [electives/](./electives/) |
| Capstone | [capstone/](./capstone/) |
| Prior learning (RPL) | [rpl/prior-learning.md](./rpl/prior-learning.md) |
| Note templates | [notes/templates/](./notes/templates/) |
| External links | [resources/links.md](./resources/links.md) |
| Init / scaffold script | [scripts/README.md](./scripts/README.md) |
| **Philosophy & how to use this repo** | **[GUIDE.md](./GUIDE.md)** |
| **Daily / weekly / monthly routines** | **[ROUTINES.md](./ROUTINES.md)** |
| **Performance operating model** | **[meta/](./meta/)** (Epictetus / Mind Master) |

## Optional local site

The repo remains Markdown-first. A lightweight MkDocs Material layer is available for local browsing and search without duplicating content into HTML.

Setup once:

```bash
uv sync
```

Preview the private/local study site:

```bash
uv run mkdocs serve
```

Build the private/local site:

```bash
uv run mkdocs build
```

Build a restricted public-safe version:

```bash
uv run mkdocs build -f mkdocs-public.yml
```

Deployments use GitHub Actions and GitHub Pages. Pull requests build the public-safe site as CI; pushes to `main` deploy it. Enable **Pages → Build and deployment → Source → GitHub Actions** in the GitHub repository settings.

Read [SITE.md](./SITE.md) before publishing anything. The default `mkdocs.yml` site is intended for private local use and includes operational study documents; public builds must use `mkdocs-public.yml`.

## How to use this repo

Read **[GUIDE.md](./GUIDE.md)** for philosophy and **[ROUTINES.md](./ROUTINES.md)** for daily/weekly/monthly cadence and end-of-module routing.

Quick start:

1. **Track progress** — [progress/TRACKER.md](./progress/TRACKER.md)
2. **Study in bursts** — [progress/study-log.md](./progress/study-log.md) + course blank sheets
3. **Perform deliberately** — [meta/metrics.md](./meta/metrics.md) + post-mortems
4. **Plan electives** — [electives/candidates.md](./electives/candidates.md)
5. **Capture RPL** — [rpl/prior-learning.md](./rpl/prior-learning.md)

## Program at a glance

| Component | Credit hours | Status |
|-----------|-------------|--------|
| Core modules | 625 | Not started |
| Electives | 875 | Not started |
| Capstone | 750 | Not started |
| **Total** | **2,250** | **0%** |

## Enrollment checklist

- [x] Udacity All Access subscription active
- [x] One-time $199 enrollment fee paid
- [x] Application submitted (ID verification)
- [x] Prior learning evaluated for credit (RPL)
- [x] Learning plan visible at [udacity.com/learning-plan/mba-in-ai](https://www.udacity.com/learning-plan/mba-in-ai)

## Reference

- Official program page: [udacity.com/mba-ai-product-management](https://www.udacity.com/mba-ai-product-management)
- Brochure: [udacity_mba_brochure.pdf](./udacity_mba_brochure.pdf)
- Udacity support: [About the Program](https://support.udacity.com/hc/en-us/articles/44221586096909-About-the-Program)
