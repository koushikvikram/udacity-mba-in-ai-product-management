# Philosophy & Guide

How this repository is designed, why it works that way, and how to use it throughout your MBA.

---

## Philosophy

### This repo is a knowledge base, not a transcript

Udacity owns your coursework, grades, and credentials. This repo owns **your understanding** — the ideas you keep, the connections you make, and the work you want to reference years from now.

The goal is not to copy every video or slide. It is to build a **personal, searchable body of knowledge** that outlasts any single Nanodegree classroom.

### Separate tracking from thinking

Progress (hours, completion status, deadlines) and content (notes, projects, reflections) pull in opposite directions:

- Trackers want to be **current and scannable**
- Notes want to be **deep and permanent**

Mixing them in one file leads to either shallow notes or cluttered trackers. This repo keeps them apart:

| Purpose | Where | Update cadence |
|---------|-------|----------------|
| *Where am I?* | `progress/` | Weekly or on milestone |
| *What did I learn?* | `core/`, `electives/`, `notes/` | During and after study |
| *How am I performing?* | `meta/` | Weekly meta review + post-mortems |
| *What am I building toward?* | `capstone/`, `electives/candidates.md` | Ongoing |

### Mirror the program, not duplicate it

Folder structure follows the **MBA curriculum tiers** (core → electives → capstone), not Udacity's internal lesson numbering. When you finish a lesson, you should know exactly where your note belongs without thinking.

Official sources stay authoritative:

- **Udacity learning plan** — unlock order, submissions, assessments
- **[PROGRAM.md](./PROGRAM.md)** — credit hours, program list, enrollment rules
- **This repo** — your synthesis, artifacts, and longitudinal view

If Udacity and this repo ever disagree, trust Udacity for *requirements* and this repo for *your record*.

### Write for future you

In six months you will not remember which lesson introduced a framework. Notes should answer:

1. **What is it?** (definition, mental model)
2. **Why does it matter?** (business or product context)
3. **When would I use it?** (link to work, capstone, interviews)

Templates in `notes/templates/` encode this habit so you do not start from a blank page.

### The Blank Sheet Method (primary note-taking approach)

Course notes in this repo use Shane Parrish's [Blank Sheet Method](https://fs.blog/blank-sheet-method/) — one **living sheet per course**, not one file per lesson.

| Step | When | What to do |
|------|------|------------|
| **Prime** | Before the first lesson | Fill in *Before I start — what I already know* (even if wrong) |
| **Add** | After each study session | Append a dated entry under *Session log* |
| **Review** | Before the next session | Re-read the entire sheet (30 seconds — 2 minutes) |
| **Correct** | When you learn you were wrong | Update *Misconceptions corrected*; trim outdated priming notes |
| **Synthesize** | When the course is done | Compress everything into *Synthesis — the compressed map* |

Why this fits an MBA better than transcript-style notes:

- **Video courses reward engagement, not copying** — compress ideas into your own words
- **One file per course** matches the repo's `notes/<course>.md` layout (linked from each `SYLLABUS.md`)
- **Git history replaces "different color ink"** — each commit shows what you added that session
- **Synthesis maps to capstone thinking** — connecting frameworks across modules is the degree's point

Template: [notes/templates/blank-sheet.md](./notes/templates/blank-sheet.md)

Use [module-notes.md](./notes/templates/module-notes.md) only for one-off deep dives (a single lesson or reading that deserves its own page).

### Epictetus operating model (how you perform)

The MBA is a multi-year endurance test. Curriculum tracking (`progress/`) and knowledge capture (blank sheets) are not enough — you also need **how you show up**.

This repo's **`meta/`** folder holds the [Epictetus operating model](./meta/epictetus-operating-model.md) (Viswanathan Anand / *Mind Master* frame):

| Layer | Question | Repo |
|-------|----------|------|
| **Practice** | What must I do? | Short bursts, post-mortems, ditch-the-ladder, AI co-evaluator |
| **Principles** | Why? | Doctrine in the operating model doc |
| **Meta** | Am I improving? | [meta/metrics.md](./meta/metrics.md) + weekly review |

**Spine (non-negotiable):** short bursts + post-mortems within 24h. Everything else is decoration until those hold.

**Integrated with blank sheets:** emotional anchors on misconceptions; revision schedule (+1d / +3d / +1w / +1m) on each course sheet; revision queue in `meta/metrics.md`.

**When to post-mortem:** failed quiz, rejected project, bad study week, mentor feedback that stings — copy [meta/templates/post-mortem.md](./meta/templates/post-mortem.md) to `meta/log/post-mortems/`.

Hub: **[meta/README.md](./meta/README.md)**

### Projects are portfolio assets

Every Nanodegree project is a chance to produce something you can **show**, not just pass. The `projects/` folders hold:

- Write-ups and decisions (not just submission files)
- Reflections using the project template
- Links to repos, decks, or demos hosted elsewhere

Failed or resubmitted projects → also file a [post-mortem](./meta/templates/post-mortem.md) within 24h.

The capstone folder is structured as a **product initiative** (discovery → design → build → impact), not a homework dump.

### Low ceremony, high consistency

No rigid daily journaling requirement. Instead:

- **Short bursts** (1–3 × 25–50 min) with one artifact per burst — see [meta/epictetus-operating-model.md](./meta/epictetus-operating-model.md)
- Log bursts in [progress/study-log.md](./progress/study-log.md); update [meta/metrics.md](./meta/metrics.md) weekly
- Post-mortem setbacks within 24h — [meta/templates/post-mortem.md](./meta/templates/post-mortem.md)
- Update tracker on start/finish; blank sheet after each burst
- One project reflection per submission

Consistency beats volume. A focused burst + blank sheet entry beats a three-hour passive video grind.

### Git-friendly by design

Plain Markdown, minimal tooling, no database. You get:

- Full-text search in any editor
- Version history of how your thinking evolved
- Portability — this repo works without Udacity, Cursor, or any specific app

---

## Repo map

| Path | Purpose |
|------|---------|
| [README.md](./README.md) | Start here |
| [PROGRAM.md](./PROGRAM.md) | Official curriculum & enrollment |
| [GUIDE.md](./GUIDE.md) | Philosophy & how to use the repo |
| [ROUTINES.md](./ROUTINES.md) | Daily / weekly / monthly cadence & routing |
| [core/](./core/) | Core programs — SYLLABUS, blank sheets, projects |
| [electives/](./electives/) | Elective planning & future program folders |
| [capstone/](./capstone/) | Capstone phases & deliverables |
| [progress/](./progress/) | TRACKER + study log |
| [meta/](./meta/) | Operating model, metrics, post-mortems |
| [notes/](./notes/) | Cross-cutting glossary & templates |
| [rpl/](./rpl/) | Prior learning & remediation |
| [resources/](./resources/) | External links |
| [scripts/](./scripts/) | Scaffold generator for core programs |

---

### Start here

| If you want to… | Open |
|-----------------|------|
| See the big picture | [README.md](./README.md) |
| **Daily / weekly / monthly routines & routing** | **[ROUTINES.md](./ROUTINES.md)** |
| Understand program requirements | [PROGRAM.md](./PROGRAM.md) |
| Check what's done | [progress/TRACKER.md](./progress/TRACKER.md) |
| Plan electives | [electives/candidates.md](./electives/candidates.md) |
| Record prior Udacity work | [rpl/prior-learning.md](./rpl/prior-learning.md) |

---

### Weekly rhythm

→ **[ROUTINES.md](./ROUTINES.md)** (daily · weekly · monthly · end-of-module routing)

---

### Where to put things

```
Decision tree:

Is it a setback, failed submission, or sting you need to process?
  → meta/log/post-mortems/ (within 24h)

Is it an uncomfortable commitment or AI disagreement?
  → meta/log/ditch-the-ladder/ or meta/log/ai-disagreements/

Is it weekly performance review?
  → meta/metrics.md + meta/templates/weekly-meta-review.md

Is it about completion status or hours?
  → progress/

Is it a lesson note or concept for one program?
  → core/<module>/<program>/notes/
  → or core/<module>/notes/ if it spans programs in that module

Is it a project write-up or reflection?
  → core/<module>/<program>/projects/
  → or capstone/projects/ for capstone work

Is it a cross-cutting framework, glossary entry, or cheat sheet?
  → notes/ (top-level)

Is it an elective you have chosen?
  → electives/<nanodegree-slug>/  (create when selected)

Is it capstone research, design, or final deliverables?
  → capstone/research/, capstone/design/, capstone/deliverables/

Is it an external URL or reading list item?
  → resources/links.md
```

---

### Working through core modules

1. Open the module README under `core/` (e.g. `core/01-implementation-and-product-introduction/`)
2. Open the program's **[SYLLABUS.md](./core/01-implementation-and-product-introduction/product-manager/SYLLABUS.md)** — check off lessons as you complete them in Udacity
3. Mark the program **In progress** in [progress/TRACKER.md](./progress/TRACKER.md)
4. For each course, use the blank sheet in `notes/<course>.md` (linked from SYLLABUS) — see [Blank Sheet Method](https://fs.blog/blank-sheet-method/)
5. When you submit a project, complete the stub in `projects/`
6. Mark **Complete** in the tracker when Udacity shows graduation/pass

**RPL / remediation:** If you already completed a Nanodegree, do not create fake lesson notes. Log it in [rpl/prior-learning.md](./rpl/prior-learning.md), complete remediation in Udacity, and optionally add a short "remediation summary" note if the reading surfaces new ideas.

---

### Planning and taking electives

Electives are 875 hours (~7 Nanodegrees) of specialization. Treat them as a ** deliberate choice**, not filler.

1. Fill in goals and score options in [electives/candidates.md](./electives/candidates.md)
2. Lock in 7 choices with brief rationale
3. When you start one, create `electives/<slug>/` with `notes/` and `projects/` (mirror core structure)
4. Add a row to the elective section of [progress/TRACKER.md](./progress/TRACKER.md)

Revisit your elective plan after core module 1–2 — you will have a clearer picture of gaps and interests.

---

### Capstone workflow

Use [capstone/README.md](./capstone/README.md) as the single source for capstone phase tracking.

| Phase | Folder | Activity |
|-------|--------|----------|
| Discovery | `capstone/research/` | Problem statements, user research, competitive scan |
| Design | `capstone/design/` | PRD, architecture, success metrics |
| Build | `capstone/projects/` | Iterations, demos, pilot results |
| Close | `capstone/deliverables/` | Final report, presentation, portfolio link |

Start the ideas backlog early — concepts from core modules often seed capstone topics.

---

### Note-taking conventions

Primary method: **[Blank Sheet Method](https://fs.blog/blank-sheet-method/)** — one sheet per course ([template](./notes/templates/blank-sheet.md)).

- **Before studying:** re-read the course sheet; prime with what you know
- **After studying:** dated session entry only — not a full transcript
- **After course:** fill in the synthesis section; promote key terms to the glossary
- **File names:** match SYLLABUS slugs — e.g. `01-product-strategy.md`
- **Links:** paste Udacity lesson URLs inside session log entries
- **Tags:** inline — `#review`, `#capstone`, `#interview`
- **Glossary:** cross-cutting definitions in [notes/README.md](./notes/README.md)

---

### What not to put in this repo

- Udacity login credentials or `.env` files
- Full copyrighted course material copied verbatim from videos
- Large binary files — link to Google Drive, GitHub, or portfolio instead
- Submission-only dumps with no reflection (passing ≠ learning captured)

See [.gitignore](./.gitignore) for excluded patterns.

---

### Keeping the tracker honest

[progress/TRACKER.md](./progress/TRACKER.md) is your dashboard. Keep it lightweight:

| Event | Action |
|-------|--------|
| Start a program | Set status to 🟡, add start date |
| Finish a program | Set status to 🟢, add completion date |
| RPL remediation only | Set status to 🔵 |
| Pause subscription | Note in tracker; no need to delete progress |
| Finish capstone phase | Check off phase in capstone README and tracker |

Update the **Summary** section monthly — cumulative hours, average weekly pace, revised target date.

---

### Suggested evolution over time

| Stage | Focus |
|-------|-------|
| **Month 1** | RPL, first core program, blank sheet + burst habit, first meta metrics entry |
| **Months 2–8** | Core modules, glossary, project reflections, post-mortem routine |
| **Months 6–10** | Elective plan finalized, first electives scaffolded like `core/` |
| **Months 12–18** | Capstone discovery; AI co-evaluator on major capstone decisions |
| **Final stretch** | Capstone delivery, portfolio, degree completion |

The repo should get **richer** as you progress — empty folders at the start are expected.

---

## Summary

| Principle | Practice |
|-----------|----------|
| Knowledge over completion | Blank sheets + synthesis, not transcripts |
| Tracking ≠ content | `progress/` vs module folders |
| Performance ≠ curriculum | `meta/` — bursts, post-mortems, metrics |
| Mirror the MBA structure | core → electives → capstone |
| Memory is contextual | Emotional anchors + spaced revision on blank sheets |
| Ego loses to AI | Log disagreements accepted in `meta/log/ai-disagreements/` |
| Udacity is source of truth | Repo is your layer on top |

When in doubt:

- **Learned something?** → blank sheet in the program's `notes/`
- **Finished something?** → `progress/TRACKER.md`
- **Stung by a setback?** → `meta/log/post-mortems/` within 24h
