#!/usr/bin/env python3
"""Initialize SYLLABUS.md, course notes, and project stubs for MBA core programs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NOTE_STUB = """# {title}

**Program:** {program}  
**Udacity link:** {url}  
**Status:** ⬜ Not started

> One sheet per course — [Blank Sheet Method](https://fs.blog/blank-sheet-method/)

---

## Before I start — what I already know

-

---

## Misconceptions corrected

| Was wrong about | Now understand | Emotional anchor |
|-----------------|----------------|------------------|
| | | |

---

## Revision schedule

| Pattern / concept | +1d | +3d | +1w | +1m |
|-------------------|-----|-----|-----|-----|
| | ⬜ | ⬜ | ⬜ | ⬜ |

Also track in `meta/metrics.md`.

---

## Session log

_Before each session: re-read this sheet. After each session: add a dated entry._

### YYYY-MM-DD — [Lesson(s) or topic]

-

---

## Synthesis — the compressed map

### Core ideas (few words each)

-

### How pieces connect

_

### Useful for capstone / work?

_

---

## Quick review checklist

- [ ] Re-read sheet before next session
- [ ] Course complete — synthesis filled in
- [ ] Key terms added to top-level `notes/README.md` glossary if cross-cutting
"""

PROJECT_STUB = """# Project: {title}

**Program:** {program}  
**Status:** ⬜ Not started  
**Date completed:**  
**Udacity project link:** {url}

---

## Objective

_

## Approach

_

## Artifacts

| Artifact | Location |
|----------|----------|
| Submission | |
| Portfolio | |

## What I learned

-

## What I'd do differently

-

## One-liner for resume / LinkedIn

_
"""

PROGRAMS = [
    {
        "path": "core/01-implementation-and-product-introduction/product-manager",
        "id": "nd036",
        "title": "Product Manager Nanodegree",
        "url": "https://www.udacity.com/course/product-manager-nanodegree--nd036",
        "hours": 50,
        "mba_group": "Implementation & Product Introduction (250 h)",
        "courses": [
            {
                "name": "Welcome to the Nanodegree Program",
                "slug": "00-welcome",
                "skip_notes": True,
                "items": ["Welcome!", "Getting Help"],
            },
            {
                "name": "Product Strategy for Product Managers",
                "slug": "01-product-strategy",
                "items": [
                    "Introduction to Product Management",
                    "Role of a PM",
                    "Problem Identification",
                    "Vision & Strategy",
                    "Communication Skills",
                    "PROJECT: Pitch a Product Vision",
                ],
            },
            {
                "name": "Product Design",
                "slug": "02-product-design",
                "items": [
                    "Intro to Design Sprint",
                    "Phase 1: Understand",
                    "Phase 2: Define",
                    "Phase 3: Sketch",
                    "Phase 4: Decide",
                    "Phase 5: Prototype",
                    "Phase 6: Validate",
                    "Next Steps",
                    "PROJECT: Run a Design Sprint",
                ],
            },
            {
                "name": "Product Development",
                "slug": "03-product-development",
                "items": [
                    "Introduction to Product Development",
                    "Influencing without Authority",
                    "Development Methodologies, Collaboration, & Tools",
                    "Testing, Feedback, and Preparing for Launch",
                    "PROJECT: Managing Product Development",
                ],
            },
            {
                "name": "Product Launch",
                "slug": "04-product-launch",
                "items": [
                    "Introduction to Product Launch",
                    "Set Up the Launch Process",
                    "Marketing Strategy",
                    "Prepare Your Partner Teams for Launch",
                    "Launch and Post-launch Feedback",
                    "PROJECT: Deliver a Product to Market",
                ],
            },
            {
                "name": "Congratulations",
                "slug": "05-congratulations",
                "skip_notes": True,
                "items": ["Program completion / next steps"],
            },
        ],
        "projects": [
            ("pitch-a-product-vision", "Pitch a Product Vision"),
            ("run-a-design-sprint", "Run a Design Sprint"),
            ("managing-product-development", "Managing Product Development"),
            ("deliver-a-product-to-market", "Deliver a Product to Market"),
        ],
    },
    {
        "path": "core/01-implementation-and-product-introduction/ai-product-manager",
        "id": "nd088",
        "title": "AI Product Manager Nanodegree",
        "url": "https://www.udacity.com/course/ai-product-manager-nanodegree--nd088",
        "hours": 18,
        "mba_group": "Implementation & Product Introduction (250 h)",
        "courses": [
            {
                "name": "Welcome",
                "slug": "00-welcome",
                "skip_notes": True,
                "items": ["An Introduction to Your Nanodegree Program", "Getting Help"],
            },
            {
                "name": "Leveraging Data with AI",
                "slug": "01-leveraging-data-with-ai",
                "items": [
                    "Using AI and Machine Learning in Business",
                    "AI Personalization and Unsupervised Machine Learning",
                    "Predicting the Future with AI",
                    "PROJECT: PRD for AI-Enabled Gift Recommendation System MVP",
                ],
            },
            {
                "name": "Bespoke Datasets for Multimodal AI Products",
                "slug": "02-bespoke-datasets",
                "items": [
                    "Supervised Machine Learning and Computer Vision",
                    "Data Annotation for AI Products",
                    "AI Stakeholders and Roadmaps",
                    "PROJECT: Roadmap for Tasty Cuts (AI Video Creation App)",
                ],
            },
            {
                "name": "Generative AI Products",
                "slug": "03-generative-ai-products",
                "items": [
                    "NLP and Conversational AI",
                    "Building Products with Large Language Models (LLMs)",
                    "Measuring Impact and Mitigating Bias in AI Products",
                    "PROJECT: Innovative Business Solutions with LLMs",
                ],
            },
        ],
        "projects": [
            ("gift-recommendation-prd", "PRD for AI-Enabled Gift Recommendation System MVP"),
            ("tasty-cuts-roadmap", "Roadmap for Tasty Cuts: AI-Powered Video Creation App"),
            ("llm-business-solutions", "Innovative Business Solutions with LLMs"),
        ],
    },
    {
        "path": "core/02-statistics-and-data-analysis/intro-to-statistics",
        "id": "st101",
        "title": "Intro to Statistics",
        "url": "https://www.udacity.com/course/intro-to-statistics--st101",
        "hours": None,
        "mba_group": "Statistics & Data Analysis (175 h)",
        "courses": [
            {
                "name": "Visualization",
                "slug": "01-visualization",
                "items": [
                    "Teaser",
                    "Explore More",
                    "Looking at Data",
                    "Scatter Plots",
                    "Bar Charts",
                    "Pie Charts",
                    "Admissions Case Study",
                    "Problem Set 1: Visualization",
                ],
            },
            {
                "name": "Probability",
                "slug": "02-probability",
                "items": [
                    "Probability",
                    "Conditional Probability",
                    "Bayes Rule",
                    "Programming Bayes Rule (Optional)",
                    "Probability Distributions",
                    "Correlation vs. Causation",
                    "Problem Set 2: Probability",
                ],
            },
            {
                "name": "Estimation",
                "slug": "03-estimation",
                "items": [
                    "Estimation",
                    "Averages",
                    "Variance",
                    "Programming Estimators (Optional)",
                    "Problem Set 3: Estimators",
                ],
            },
            {
                "name": "Normal Distribution & CLT",
                "slug": "04-normal-clt",
                "items": [
                    "Outliers",
                    "Binomial Distribution",
                    "Central Limit Theorem",
                    "Central Limit Theorem Programming (Optional)",
                    "The Normal Distribution",
                    "Manipulating Normals",
                    "Most Better than Average",
                    "Problem Set 4",
                    "Sebastian's Weight and Proofs (Optional)",
                ],
            },
            {
                "name": "Inference",
                "slug": "05-inference",
                "items": [
                    "Confidence Intervals",
                    "Normal Quantiles",
                    "Hypothesis Test",
                    "Hypothesis Test 2",
                    "Programming Tests and Intervals (Optional)",
                    "Problem Set 5: Inference",
                ],
            },
            {
                "name": "Regression & Case Studies",
                "slug": "06-regression-cases",
                "items": [
                    "Regression",
                    "Correlation",
                    "Monty Hall Problem (Optional)",
                    "Problem Set 6: Regression and Correlation",
                    "Weight Case Studies",
                    "Flash Crash Example",
                    "Challenger Example",
                    "Final Exam",
                    "What's Next",
                ],
            },
        ],
        "projects": [],
    },
    {
        "path": "core/02-statistics-and-data-analysis/intro-to-inferential-statistics",
        "id": "ud201",
        "title": "Intro to Inferential Statistics",
        "url": "https://www.udacity.com/course/intro-to-inferential-statistics--ud201",
        "hours": None,
        "mba_group": "Statistics & Data Analysis (175 h)",
        "courses": [
            {
                "name": "Review & Estimation",
                "slug": "01-estimation",
                "items": ["Introduction and Lesson 7 Review", "Estimation", "Problem Set 8"],
            },
            {
                "name": "Hypothesis Testing",
                "slug": "02-hypothesis-testing",
                "items": ["Hypothesis Testing", "Problem Set 9"],
            },
            {
                "name": "t-Tests",
                "slug": "03-t-tests",
                "items": [
                    "t-Tests, Part 1",
                    "Problem Set 10a",
                    "t-Tests, Part 2",
                    "Problem Set 10b",
                    "t-Tests, Part 3",
                    "Problem Set 11",
                ],
            },
            {
                "name": "ANOVA",
                "slug": "04-anova",
                "items": ["One-Way ANOVA", "Problem Set 12", "ANOVA, Continued", "Problem Set 13"],
            },
            {
                "name": "Correlation & Regression",
                "slug": "05-correlation-regression",
                "items": ["Correlation", "Problem Set 14", "Regression", "Problem Set 15"],
            },
            {
                "name": "Chi-Square & Final",
                "slug": "06-chi-square-final",
                "items": [
                    "χ² Tests",
                    "Problem Set 16",
                    "Final Project",
                    "Google Spreadsheet Tutorial",
                ],
            },
        ],
        "projects": [("final-project", "Final Project")],
    },
    {
        "path": "core/02-statistics-and-data-analysis/business-intelligence-analytics",
        "id": "nd098",
        "title": "Business Intelligence Analytics Nanodegree",
        "url": "https://www.udacity.com/course/business-intelligence-analyst-nanodegree--nd098",
        "hours": 40,
        "mba_group": "Statistics & Data Analysis (175 h)",
        "courses": [
            {
                "name": "Business Metrics with Spreadsheets",
                "slug": "01-business-metrics-spreadsheets",
                "items": [
                    "Introduction to Data",
                    "Business Metrics",
                    "Introduction to Spreadsheets",
                    "Spreadsheet Data Analysis",
                    "Spreadsheet Data Visualization",
                    "PROJECT: Analyze Profits for E-commerce Company",
                ],
            },
            {
                "name": "SQL for Data Analysis",
                "slug": "02-sql-data-analysis",
                "items": [
                    "SQL Operators",
                    "JOINs",
                    "SQL Aggregation",
                    "Subqueries & CTEs",
                    "SQL Window Functions",
                    "SQL Data Cleaning",
                    "PROJECT: Retail Analysis",
                ],
            },
            {
                "name": "Data Visualization in Tableau",
                "slug": "03-tableau-visualization",
                "items": [
                    "Design Principles",
                    "Getting Started with Tableau",
                    "Core Chart Types",
                    "Interactive Dashboards and Stories",
                    "PROJECT: Build Tableau Visualizations",
                ],
            },
        ],
        "projects": [
            ("ecommerce-profits", "Analyze Profits for E-commerce Company"),
            ("retail-analysis", "Retail Analysis"),
            ("tableau-visualizations", "Build Tableau Visualizations"),
        ],
    },
    {
        "path": "core/03-digital-marketing",
        "id": "nd018",
        "title": "Digital Marketing Nanodegree",
        "url": "https://www.udacity.com/course/digital-marketing-nanodegree--nd018",
        "hours": 73,
        "mba_group": "Digital Marketing (125 h)",
        "courses": [
            {
                "name": "Welcome",
                "slug": "00-welcome",
                "skip_notes": True,
                "items": ["An Introduction to Your Nanodegree Program", "Getting Help"],
            },
            {
                "name": "Marketing Fundamentals",
                "slug": "01-marketing-fundamentals",
                "items": [
                    "Introduction to Digital Marketing Framework",
                    "Your Business Value",
                    "Your Customer",
                    "Marketing Channels",
                    "Marketing Objectives and Performance",
                    "Plan Your Content",
                    "Working in Digital Marketing Roles",
                    "PROJECT: Get Ready to Market",
                ],
            },
            {
                "name": "Marketing Data and Technology",
                "slug": "02-marketing-data-technology",
                "items": [
                    "Introduction to Marketing Data and Technology",
                    "Marketing Data for Your Business",
                    "AB Testing and Attribution Models",
                    "Google Analytics (Part 1) - Getting Started & Audience",
                    "Google Analytics (Part 2) - Acquisition, Behaviors, and Conversion",
                    "Marketing Technology and eCommerce",
                    "The Future of Digital Marketing",
                    "PROJECT: Draw Insights from Marketing Data",
                ],
            },
            {
                "name": "Social Media Marketing",
                "slug": "03-social-media-marketing",
                "items": [
                    "Social Media Marketing Fundamentals",
                    "Organic Social Media Campaigns",
                    "Paid Social Media Campaigns",
                    "Introduction to Facebook-Meta Ads",
                    "Creating and Managing Ad Campaigns",
                    "PROJECT: Marketing Your Content",
                ],
            },
            {
                "name": "Search Engine Optimization (SEO)",
                "slug": "04-seo",
                "items": [
                    "Introduction to SEO",
                    "Keywords",
                    "On-Site SEO: Optimize UX & Design",
                    "Off-Site SEO: Link-Building",
                    "SEO Audit",
                    "PROJECT: Conduct an SEO Audit",
                ],
            },
            {
                "name": "Search Engine Marketing (SEM)",
                "slug": "05-sem",
                "items": [
                    "Introduction to SEM",
                    "Keywords",
                    "Ads",
                    "Ad Rank and Maximum CPC bid",
                    "Metrics and Optimization",
                    "PROJECT: Evaluate a Google Ads Campaign",
                ],
            },
            {
                "name": "Digital Advertising",
                "slug": "06-digital-advertising",
                "items": [
                    "Introduction to Digital Advertising",
                    "Audience Fundamentals",
                    "Multichannel Formats",
                    "Programmatic Technology",
                    "Campaign Planning",
                    "Campaign Management",
                    "PROJECT: Plan a Multichannel Ad Campaign",
                ],
            },
            {
                "name": "Email Marketing",
                "slug": "07-email-marketing",
                "items": [
                    "Introduction to Email Marketing",
                    "Email List Generation",
                    "Create an Effective Email Campaign",
                    "Create an Email Plan",
                    "Measure Results",
                    "PROJECT: Market with Email",
                ],
            },
        ],
        "projects": [
            ("get-ready-to-market", "Get Ready to Market"),
            ("draw-insights-marketing-data", "Draw Insights from Marketing Data"),
            ("marketing-your-content", "Marketing Your Content"),
            ("conduct-seo-audit", "Conduct an SEO Audit"),
            ("evaluate-google-ads", "Evaluate a Google Ads Campaign"),
            ("multichannel-ad-campaign", "Plan a Multichannel Ad Campaign"),
            ("market-with-email", "Market with Email"),
        ],
    },
    {
        "path": "core/04-growth-product-management",
        "id": "nd037",
        "title": "Growth Product Manager Nanodegree",
        "url": "https://www.udacity.com/course/growth-product-manager-nanodegree--nd037",
        "hours": 57,
        "mba_group": "Growth Product Management (100 h)",
        "courses": [
            {
                "name": "Welcome",
                "slug": "00-welcome",
                "skip_notes": True,
                "items": ["An Introduction to Your Nanodegree Program", "Getting Help"],
            },
            {
                "name": "Growth and Acquisition Strategy",
                "slug": "01-growth-acquisition",
                "items": [
                    "Introduction to Growth and Acquisition Strategy",
                    "Examining the Growth Landscape",
                    "Creating a Growth Loop",
                    "Validating a Growth Loop",
                    "Expanding a Growth Loop",
                    "PROJECT: Crafting a Growth Loop",
                ],
            },
            {
                "name": "Activation and Retention Strategy",
                "slug": "02-activation-retention",
                "items": [
                    "Introduction to Activation and Retention Strategy",
                    "Sign-up Flow Optimization",
                    "Defining the Activation Funnel",
                    "Conducting a Retention Cohort Analysis",
                    "Analyzing Impacts of Churn Rate across the Business",
                    "PROJECT: Let It Grow",
                ],
            },
            {
                "name": "Monetization Strategy",
                "slug": "03-monetization",
                "items": [
                    "Introduction to Monetization Strategy",
                    "Buyer Targeting",
                    "Path to Purchase",
                    "Premium Value",
                    "Pricing",
                    "PROJECT: Priceless Penny",
                ],
            },
        ],
        "projects": [
            ("crafting-a-growth-loop", "Crafting a Growth Loop"),
            ("let-it-grow", "Let It Grow"),
            ("priceless-penny", "Priceless Penny"),
        ],
    },
    {
        "path": "core/05-business-leadership-and-strategy/ai-for-business-leaders",
        "id": "nd054",
        "title": "AI for Business Leaders",
        "url": "https://www.udacity.com/course/ai-for-business-leaders--nd054",
        "hours": 25,
        "mba_group": "Business Leadership & Strategy (75 h)",
        "courses": [
            {
                "name": "Welcome",
                "slug": "00-welcome",
                "skip_notes": True,
                "items": ["AI for Business Leaders Executive Program Introduction", "Getting Help"],
            },
            {
                "name": "Machine Learning and AI for Business Leaders",
                "slug": "01-ml-ai-business",
                "items": [
                    "Introduction to Machine Learning and AI for Business",
                    "Demystifying ML Models",
                    "Implementing ML and AI in the Real World",
                    "Scaling and Leading with Machine Learning and AI",
                    "PROJECT: Zap! Accelerating from Gas to Electric with ML",
                ],
            },
            {
                "name": "Generative AI for Business Leaders",
                "slug": "02-generative-ai-business",
                "items": [
                    "Introduction to Generative AI",
                    "How to Think about Generative AI from a Business Perspective",
                    "Launching Generative AI for your Business",
                    "Ensuring You Have the Right Human Capital for GenAI Adoption",
                    "Process to Ready the Business for Generative AI",
                    "Platforms to Ready the Business for Generative AI",
                    "Optional: Generative AI: Savior or Saboteur of the Digital Workforce?",
                    "PROJECT: Build a Generative AI Strategy and Project Roadmap",
                ],
            },
            {
                "name": "Agentic AI for Business Leaders",
                "slug": "03-agentic-ai-business",
                "items": [
                    "Course Overview",
                    "TQ: Agentic AI",
                    "Is Your Organization Ready?",
                    "Technical Essentials You Need (Minus the Coding)",
                    "Spotting the Right Problems for Agentic AI",
                    "Evaluating Solutions and Talking Tech",
                    "Ethics, Governance, and Risk in the Real World",
                    "Your Agentic AI Roadmap",
                    "PROJECT: Agentic Expense Reporting System",
                ],
            },
        ],
        "projects": [
            ("zap-gas-to-electric", "Zap! Accelerating from Gas to Electric with ML"),
            ("generative-ai-strategy-roadmap", "Build a Generative AI Strategy and Project Roadmap"),
            ("agentic-expense-reporting", "Agentic Expense Reporting System"),
        ],
    },
    {
        "path": "core/05-business-leadership-and-strategy/digital-transformation",
        "id": "nd055",
        "title": "Digital Transformation for Business Leaders",
        "url": "https://www.udacity.com/course/digital-transformation-for-business-leaders--nd055",
        "hours": 7,
        "mba_group": "Business Leadership & Strategy (75 h)",
        "courses": [
            {
                "name": "Welcome",
                "slug": "00-welcome",
                "skip_notes": True,
                "items": ["Welcome"],
            },
            {
                "name": "Transformation Basics",
                "slug": "01-transformation-basics",
                "items": [
                    "Your Digital Mindset",
                    "What Transformation Means",
                    "Your Digital Milestones",
                ],
            },
            {
                "name": "Transformative Technologies",
                "slug": "02-transformative-technologies",
                "items": [
                    "Intro to Transformative Technologies",
                    "Cloud Computing",
                    "Artificial Intelligence and Machine Learning",
                    "Data Science and Analytics",
                    "Cybersecurity",
                ],
            },
            {
                "name": "Leader Perspectives",
                "slug": "03-leader-perspectives",
                "items": [
                    "Intro to Leader Perspectives",
                    "Effective Change Management",
                    "Building a Digital Culture",
                    "Agile Teams and Talent",
                ],
            },
            {
                "name": "Leading Into and In the Unknown",
                "slug": "04-leading-unknown",
                "items": ["Leading Into and In the Unknown"],
            },
            {
                "name": "Digital Transformation Roadmap and Talent Plan",
                "slug": "05-roadmap-talent-plan",
                "items": [
                    "Key decisions for piloting, implementing, and scaling digital initiatives",
                    "Prioritize digital initiatives",
                    "Build talent & transformation plan; agile governance and monitoring",
                    "CAPSTONE: Digital Transformation Roadmap + Talent Transformation Plan",
                ],
            },
        ],
        "projects": [
            (
                "transformation-roadmap-talent-plan",
                "Digital Transformation Roadmap + Talent Transformation Plan",
            ),
        ],
    },
]


def write_syllabus(prog: dict, base: Path) -> None:
    hours = prog["hours"]
    hours_line = f"**Udacity hours:** {hours}" if hours else "**Udacity hours:** Not published (self-paced)"
    lines = [
        f"# Syllabus: {prog['title']}",
        "",
        f"**Program ID:** {prog['id']}  ",
        f"**URL:** [{prog['url']}]({prog['url']})  ",
        hours_line + "  ",
        f"**MBA module:** {prog['mba_group']}  ",
        "**Status:** ⬜ Not started",
        "",
        "Check off items as you complete them in Udacity. Add lesson URLs from your classroom when note-taking.",
        "",
    ]
    depth = len(Path(prog["path"]).parts)
    tracker = "../" * depth + "progress/TRACKER.md"
    lines.extend([
        f"See also: [notes/](./notes/) · [projects/](./projects/) · [{tracker}]({tracker})",
        "",
        "---",
        "",
    ])
    for i, course in enumerate(prog["courses"], 1):
        lines.append(f"## Course {i}: {course['name']}")
        lines.append("")
        if course.get("skip_notes"):
            lines.append("_Orientation — no separate note file._")
            lines.append("")
        else:
            slug = course["slug"]
            lines.append(f"Notes: [notes/{slug}.md](./notes/{slug}.md)")
            lines.append("")
        for item in course["items"]:
            prefix = "- [ ] "
            if item.startswith("PROJECT:") or item.startswith("CAPSTONE:"):
                lines.append(f"{prefix}**{item}**")
            else:
                lines.append(f"{prefix}{item}")
        lines.append("")
    if prog["projects"]:
        lines.extend(["---", "", "## Projects index", ""])
        for slug, title in prog["projects"]:
            lines.append(f"- [ ] [{title}](./projects/{slug}.md)")
        lines.append("")
    base.joinpath("SYLLABUS.md").write_text("\n".join(lines), encoding="utf-8")


def write_notes(prog: dict, base: Path) -> None:
    notes_dir = base / "notes"
    notes_dir.mkdir(parents=True, exist_ok=True)
    index_lines = [
        f"# Notes: {prog['title']}",
        "",
        "One **blank sheet** per course ([Blank Sheet Method](https://fs.blog/blank-sheet-method/)).",
        "Before each session: re-read the sheet. After each session: add a dated entry.",
        "",
        "| Course | Blank sheet | Status |",
        "|--------|-------------|--------|",
    ]
    for course in prog["courses"]:
        if course.get("skip_notes"):
            continue
        slug = course["slug"]
        path = notes_dir / f"{slug}.md"
        if not path.exists():
            path.write_text(
                NOTE_STUB.format(
                    title=course["name"],
                    program=prog["title"],
                    course=course["name"],
                    url=prog["url"],
                ),
                encoding="utf-8",
            )
        index_lines.append(f"| {course['name']} | [{slug}.md](./{slug}.md) | ⬜ |")
    notes_dir.joinpath("README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def write_projects(prog: dict, base: Path) -> None:
    projects_dir = base / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)
    index_lines = [
        f"# Projects: {prog['title']}",
        "",
        "Complete reflections as you submit each project in Udacity.",
        "",
        "| Project | File | Status |",
        "|---------|------|--------|",
    ]
    for slug, title in prog["projects"]:
        path = projects_dir / f"{slug}.md"
        if not path.exists():
            path.write_text(
                PROJECT_STUB.format(title=title, program=prog["title"], url=prog["url"]),
                encoding="utf-8",
            )
        index_lines.append(f"| {title} | [{slug}.md](./{slug}.md) | ⬜ |")
    if prog["projects"]:
        projects_dir.joinpath("README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def write_program_readme(prog: dict, base: Path) -> None:
    depth = len(Path(prog["path"]).parts)
    prefix = "../" * depth
    rpl = f"{prefix}rpl/prior-learning.md"
    meta = f"{prefix}meta/README.md"
    guide = f"{prefix}GUIDE.md"

    post_mortem = f"{prefix}meta/log/post-mortems/"
    lines = [
        f"# {prog['title']}",
        "",
        f"**Program ID:** {prog['id']}  ",
        f"**Udacity:** [{prog['url']}]({prog['url']})  ",
        f"**MBA module:** {prog['mba_group']}  ",
        "**Status:** ⬜ Not started",
        "",
        "## Files",
        "",
        "| Resource | Link |",
        "|----------|------|",
        "| Lesson & project checklist | [SYLLABUS.md](./SYLLABUS.md) |",
        "| Course blank sheets | [notes/](./notes/) |",
    ]
    if prog["projects"]:
        lines.append("| Project reflections | [projects/](./projects/) |")
    else:
        lines.append("| Project reflections | _none — course-only program_ |")
    lines.extend([
        "",
        "## How to study this program",
        "",
        "1. Check off lessons in [SYLLABUS.md](./SYLLABUS.md) as you complete them in Udacity",
        "2. **Before each course:** prime the blank sheet (*Before I start*)",
        "3. **After each burst:** add a dated session log entry in the course's `notes/` file",
    ])
    if prog["projects"]:
        lines.append("4. **On project submit:** complete the matching file in `projects/`")
        lines.append(f"5. **On setback:** post-mortem within 24h → [`meta/log/post-mortems/`]({post_mortem})")
        lines.append(f"6. See [{guide}]({guide}) and [{meta}]({meta}) for the full workflow")
    else:
        lines.append(f"4. **On setback:** post-mortem within 24h → [`meta/log/post-mortems/`]({post_mortem})")
        lines.append(f"5. See [{guide}]({guide}) and [{meta}]({meta}) for the full workflow")
    lines.append("")
    if prog["projects"]:
        lines.extend([
            "## Projects",
            "",
            "See [projects/README.md](./projects/README.md) for the full index.",
            "",
        ])
    lines.extend([
        "## Remediation (RPL)",
        "",
        f"If previously completed: remediation reading + assessment only. Track in [{rpl}]({rpl}).",
        "",
    ])
    base.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for prog in PROGRAMS:
        base = ROOT / prog["path"]
        base.mkdir(parents=True, exist_ok=True)
        write_syllabus(prog, base)
        write_notes(prog, base)
        write_projects(prog, base)
        write_program_readme(prog, base)
        print(f"Initialized: {prog['path']}")


if __name__ == "__main__":
    main()
