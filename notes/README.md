# Notes

Cross-cutting notes that don't belong to a single module live here. **Course notes** live in each program's `notes/` folder as blank sheets.

For the repo philosophy, see **[GUIDE.md](../GUIDE.md)**. For daily/weekly/monthly cadence, see **[ROUTINES.md](../ROUTINES.md)**.

## Primary method: Blank Sheet

Each course gets **one living sheet** using the [Blank Sheet Method](https://fs.blog/blank-sheet-method/) (Farnam Street):

1. **Before** — write what you already know (priming)
2. **After each session** — append a dated entry with new learning
3. **Before next session** — re-read the whole sheet
4. **When done** — synthesize into a compressed map

Git commit history stands in for "different color ink" between sessions.

**Spaced revision + emotional anchors:** see [Revision schedule](./templates/blank-sheet.md) on each sheet; queue due reviews in [meta/metrics.md](../meta/metrics.md). Anchors go in the misconceptions table (what surprise made this stick?).

## Templates

| Template | Use for |
|----------|---------|
| **[blank-sheet.md](./templates/blank-sheet.md)** | **Default** — one per course (already in each program's `notes/`) |
| [module-notes.md](./templates/module-notes.md) | One-off deep dive on a single lesson or reading |
| [project-reflection.md](./templates/project-reflection.md) | Post-project retrospectives |
| [weekly-review.md](./templates/weekly-review.md) | Weekly curriculum recap |
| [monthly-review.md](../meta/templates/monthly-review.md) | Monthly review & repertoire change |

## Session log

The **session log** is the `## Session log` section at the bottom of each course blank sheet (e.g. `core/.../notes/01-product-strategy.md`). After every study burst, append a dated entry there — one chunk per session, not one file per lesson.

**What goes in it:** what you learned, in your own words — concepts that stuck, corrections to earlier beliefs, optional Udacity lesson links. Not a transcript; compress.

**Format:**

```markdown
### YYYY-MM-DD — [Lesson(s) or topic]

- Key idea in your words
- Something you had wrong before
- https://classroom.udacity.com/...  (optional)
```

**Example:**

```markdown
### 2026-06-08 — Product vision & OKRs

- Vision = where we're going; strategy = how we get there
- Misread "vision statement" as marketing copy — it's a decision filter
```

**Before the next session:** re-read the entire blank sheet (30 sec – 2 min), including past session log entries. When the course is done, compress the whole sheet into *Synthesis — the compressed map*.

### Session log vs study log

These sound similar but serve different purposes:

| | **Session log** | **Study log** |
|---|-----------------|---------------|
| **Where** | Course blank sheet (`core/.../notes/*.md`) | [`progress/study-log.md`](../progress/study-log.md) |
| **Tracks** | *What* you learned | *How much* you studied |
| **Granularity** | One dated entry per burst | Weekly table: bursts, minutes, module |
| **When** | After each burst (required artifact) | End of day or weekly rollup |

After a burst: append to the course session log first; jot bursts/minutes in the study log when convenient (can batch at end of day). See [ROUTINES.md](../ROUTINES.md) § Each burst.

## Conventions

- One blank sheet per **course**, not per lesson — paths linked from each `SYLLABUS.md`
- Session log entries: `### YYYY-MM-DD — topic` under the course file (see [Session log](#session-log) above)
- Tag ideas to revisit: `#review`, `#capstone`, `#interview`
- Promote reusable definitions to the glossary below

## General reference

### Glossary (starter)

| Term | Definition | Source module |
|------|------------|---------------|
| | | |
