# Routines & Routing

Canonical cadence for this repo: **daily → weekly → monthly** habits, plus **what to do when you finish** a course, program, module group, or the degree.

Companion docs: [GUIDE.md](./GUIDE.md) (philosophy) · [meta/README.md](./meta/README.md) (operating model) · [progress/TRACKER.md](./progress/TRACKER.md) (status)

---

## At a glance

| Cadence | Time | Doc / template |
|---------|------|----------------|
| **Per burst** | 25–50 min | [§ Each burst](#each-burst) |
| **Daily** | Study days | [§ Daily](#daily-study-days) · [daily-study-session.md](./meta/templates/daily-study-session.md) |
| **Event (≤24h)** | After setback | [post-mortem.md](./meta/templates/post-mortem.md) · [§ Event-driven](#event-driven-within-24-hours) |
| **Weekly** | ~15–20 min | [§ Weekly](#weekly) · [weekly-meta-review.md](./meta/templates/weekly-meta-review.md) + [weekly-review.md](./notes/templates/weekly-review.md) |
| **Monthly** | ~20 min | [§ Monthly](#monthly-20-min-first-week-of-month) · [monthly-review.md](./meta/templates/monthly-review.md) |
| **End of course** | ~15 min | [§ End of course](#end-of-course-15-min) |
| **End of program** | ~30 min | [§ End of program](#end-of-program-30-min) |
| **End of module group** | ~20 min | [§ End of module group](#end-of-module-group-20-min) |
| **End of capstone** | ~1 hr | [capstone/README.md](./capstone/README.md) · [§ End of capstone](#end-of-capstone-1-hr) |
| **End of degree** | ~1 hr | [§ End of degree](#end-of-degree-1-hr) |

---

## Daily (study days)

**Spine:** short bursts + one artifact per burst. See [meta/epictetus-operating-model.md](./meta/epictetus-operating-model.md).

### Before first burst

- [ ] Open today's program in Udacity
- [ ] Open that course's **blank sheet** (`core/.../notes/<course>.md`)
- [ ] **Re-read the entire blank sheet** (30 sec – 2 min)
- [ ] If first session on this course: fill *Before I start*
- [ ] Check [meta/metrics.md](./meta/metrics.md) revision queue — anything due today?

<a id="each-burst"></a>

### Each burst (1–3 × 25–50 min)

- [ ] One focused problem (lesson block, project section, or assessment prep)
- [ ] Distractions blocked
- [ ] Study in Udacity
- [ ] **Artifact:** append dated entry to blank sheet *Session log* ([what is a session log?](./notes/README.md#session-log))
- [ ] Check off completed items in program [SYLLABUS.md](./core/01-implementation-and-product-introduction/product-manager/SYLLABUS.md)
- [ ] Jot burst in [progress/study-log.md](./progress/study-log.md) (can batch at end of day)

### End of study day (~2 min)

- [ ] Log bursts + minutes in [study-log.md](./progress/study-log.md)
- [ ] Note tomorrow's starting point (SYLLABUS item or course name)

### Optional daily (when applicable)

- [ ] **Ditch-the-ladder** rep if not done this week → [ditch-the-ladder.md](./meta/templates/ditch-the-ladder.md)
- [ ] **AI co-evaluator** on a decision you made today → [ai-co-evaluator.md](./meta/templates/ai-co-evaluator.md)
- [ ] **Objectivity drill** if stakes feel dire → [objectivity-drill.md](./meta/templates/objectivity-drill.md)

### Daily (non-study days)

- [ ] No guilt — rest is part of endurance
- [ ] If a setback happened yesterday and you skipped post-mortem: **do it now** (never >24h)

---

## Event-driven (within 24 hours)

Trigger: failed quiz, rejected project, bad session, mentor feedback that stings, missed week you planned to study.

- [ ] Copy [post-mortem.md](./meta/templates/post-mortem.md) → `meta/log/post-mortems/YYYY-MM-DD-<slug>.md`
- [ ] Fill while emotions are raw
- [ ] Link from project reflection if applicable
- [ ] One small adjustment to test next time
- [ ] Mark in [meta/metrics.md](./meta/metrics.md) setbacks table

---

<a id="weekly"></a>

## Weekly (~15–20 min, same day each week)

Do **both** reviews — they serve different purposes.

### 1. Performance (meta) — ~10 min

- [ ] Complete [weekly-meta-review.md](./meta/templates/weekly-meta-review.md)
- [ ] Update [meta/metrics.md](./meta/metrics.md) (all leading indicators)
- [ ] Optional: archive review → `meta/log/reviews/YYYY-MM-DD.md`
- [ ] **Spine check:** bursts + post-mortems still happening?

### 2. Curriculum — ~10 min

- [ ] Finish [study-log.md](./progress/study-log.md) week block
- [ ] Optional: [weekly-review.md](./notes/templates/weekly-review.md)
- [ ] Update [TRACKER.md](./progress/TRACKER.md) if status changed
- [ ] Set next week's program/course focus

### Weekly questions (from operating model)

- Where was I most predictable?
- Which pattern needs another revision pass?
- Which loss did I avoid post-mortem-ing — and why?

---

## Monthly (~20 min, first week of month)

- [ ] Complete [monthly-review.md](./meta/templates/monthly-review.md)
- [ ] Update **Summary** in [TRACKER.md](./progress/TRACKER.md) (cumulative hours, pace, target date)
- [ ] Update monthly rollup in [study-log.md](./progress/study-log.md) and [metrics.md](./meta/metrics.md)
- [ ] **Change one opening-repertoire variable** (study time, tool, elective angle, capstone framing)
- [ ] Revisit [electives/candidates.md](./electives/candidates.md) if still in core phase

---

## End of course (~15 min)

_When you finish the last lesson in a Udacity **course** within a Nanodegree (e.g. "Product Strategy" within Product Manager ND)._

| Step | Where |
|------|-------|
| [ ] Check off all items in program **SYLLABUS.md** for this course | `core/.../<program>/SYLLABUS.md` |
| [ ] Fill **Synthesis — the compressed map** on the course blank sheet | `notes/<course>.md` |
| [ ] Add **emotional anchors** for key misconceptions | Same blank sheet |
| [ ] Schedule revision: +1d, +3d, +1w, +1m on blank sheet | Same blank sheet |
| [ ] Add patterns to [meta/metrics.md](./meta/metrics.md) revision queue | `meta/` |
| [ ] Promote cross-cutting terms to [glossary](./notes/README.md) | Top-level `notes/` |

**Do not** archive the blank sheet — you will re-read it during revision passes.

---

## End of program (~30 min)

_When Udacity shows **graduation/pass** for a full Nanodegree or standalone course (e.g. nd036, st101)._

| Step | Where |
|------|-------|
| [ ] All SYLLABUS items checked | `SYLLABUS.md` |
| [ ] All course syntheses complete | Each `notes/*.md` |
| [ ] All project reflections complete | Each `projects/*.md` |
| [ ] Set status **🟢 Complete** + completion date | [TRACKER.md](./progress/TRACKER.md) |
| [ ] Update program README status line | Program `README.md` |
| [ ] If RPL/remediation only: status **🔵** | [rpl/prior-learning.md](./rpl/prior-learning.md) |
| [ ] Note 3 portfolio-ready artifacts | Program `projects/` or personal portfolio |
| [ ] Optional: weekly meta review — "what made this program predictable?" | `meta/` |

**Next routing:**

| You just finished… | Go to… |
|--------------------|--------|
| Product Manager or AI PM | Next program in [module 1](./core/01-implementation-and-product-introduction/) |
| Last program in a module group | [End of module group](#end-of-module-group-20-min) below |
| An elective | Next elective in [TRACKER.md](./progress/TRACKER.md) or [candidates.md](./electives/candidates.md) |
| Last core program | [electives/candidates.md](./electives/candidates.md) — finalize 7 choices |

---

## End of module group (~20 min)

_When you complete all programs in one of the five MBA **core groups** (625 h total across groups)._

| Module group | Programs | Folder |
|--------------|----------|--------|
| 1 — Implementation & Product Intro | Product Manager + AI Product Manager | [01-...](./core/01-implementation-and-product-introduction/) |
| 2 — Statistics & Data Analysis | st101 + ud201 + BI Analytics | [02-...](./core/02-statistics-and-data-analysis/) |
| 3 — Digital Marketing | Digital Marketing ND | [03-...](./core/03-digital-marketing/) |
| 4 — Growth PM | Growth PM ND | [04-...](./core/04-growth-product-management/) |
| 5 — Business Leadership | AI for Business Leaders + Digital Transformation | [05-...](./core/05-business-leadership-and-strategy/) |

### Checklist

- [ ] All programs in group **🟢** in [TRACKER.md](./progress/TRACKER.md)
- [ ] Cross-program patterns captured (optional) in module `notes/` folder
- [ ] Monthly review: any **opening repertoire** change for this domain?
- [ ] Capstone: seed ideas in [capstone/README.md](./capstone/README.md) backlog from this module

### Routing after each group

| Completed group | Consider next… |
|-----------------|----------------|
| **Module 1** (PM + AI PM) | Module 2 stats **or** continue momentum in module 1 review passes |
| **Module 2** (Stats) | Module 3 Marketing or Module 5 Leadership — per [core/README.md](./core/README.md) suggested order |
| **Module 3** (Marketing) | Module 4 Growth PM |
| **Module 4** (Growth) | Module 5 Leadership |
| **Module 5** (Leadership) | **All core done** → [electives/candidates.md](./electives/candidates.md); scaffold first elective |
| **All 5 core groups** | 875 h electives → then capstone (750 h) |

---

## End of capstone (~1 hr)

See [capstone/README.md](./capstone/README.md) phase checklist.

- [ ] All capstone phases checked in capstone README
- [ ] Final deliverables in `capstone/deliverables/`
- [ ] Portfolio link recorded
- [ ] Set capstone **🟢** in [TRACKER.md](./progress/TRACKER.md)
- [ ] Final post-mortem on the **process** (not just outcome) → `meta/log/post-mortems/`

---

## End of degree (~1 hr)

_When Woolf/Udacity confirms MBA conferral._

- [ ] [TRACKER.md](./progress/TRACKER.md) — all rows 🟢; degree milestone checked
- [ ] Archive final [monthly-review.md](./meta/templates/monthly-review.md)
- [ ] Portfolio: top 5 projects + capstone linked from README or external site
- [ ] Optional: one-page "MBA synthesis" in `notes/` — frameworks that survived 2,250 hours
- [ ] [rpl/prior-learning.md](./rpl/prior-learning.md) — final state for records

---

## Routing decision tree

```
Finished a lesson?
  → Check SYLLABUS · session log on blank sheet

Finished a course (within a program)?
  → End of course checklist

Submitted a project?
  → projects/<name>.md reflection
  → Failed/resubmit? → post-mortem within 24h

Graduated a program (Nanodegree/course)?
  → End of program checklist → TRACKER

Completed all programs in a core module group?
  → End of module group → routing table

Completed all core (625 h)?
  → electives/candidates.md → scaffold electives

Completed 7 electives (875 h)?
  → capstone/README.md

Degree conferred?
  → End of degree checklist
```

---

## Guardrails

1. **Post-mortems + short bursts** are the spine — restore before adding habits or metrics.
2. **SYLLABUS** = completion; **blank sheet** = understanding; **meta/** = performance.
3. **Udacity learning plan** overrides suggested order if they differ.
