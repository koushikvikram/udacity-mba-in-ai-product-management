# Scripts

## init_program_files.py

Scaffolds core MBA program folders from curriculum data baked into the script.

```bash
python3 scripts/init_program_files.py
```

### What it generates / refreshes

| Output | Behavior |
|--------|----------|
| `SYLLABUS.md` | Overwritten each run (lesson checklists) |
| `README.md` | Overwritten each run (program overview) |
| `notes/README.md` | Overwritten (course index) |
| `notes/<course>.md` | Created if missing; **not** overwritten if exists |
| `projects/*.md` | Created if missing; **not** overwritten if exists |
| `projects/README.md` | Overwritten when program has projects |

### When to run

- After Udacity updates a core program syllabus
- When adding new programs to the `PROGRAMS` list in the script

### Adding electives

Extend the `PROGRAMS` list in `init_program_files.py`, or scaffold manually using [electives/README.md](../electives/README.md).

See also: [ROUTINES.md](../ROUTINES.md) · [core/README.md](../core/README.md)
