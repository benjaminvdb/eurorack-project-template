# Project: [MODULE NAME] -- Eurorack Module

## Overview

[Brief description of the module, e.g., "A voltage-controlled oscillator based on the
SSI2131 for the Eurorack modular synthesizer format."]

- **Format:** Eurorack (3U, Doepfer A-100 compatible)
- **Width:** [??] HP
- **KiCad version:** [8.x / 9.x]
- **License:** CERN OHL v2 Permissive

## Repository Structure

```
hardware/          KiCad project files (schematic, PCB, design rules)
hardware/lib/      Project-local symbols, footprints, 3D models
panel/             Front panel (separate KiCad PCB project)
docs/              All documentation
docs/adr/          Architecture Decision Records
datasheets/        Local copies of component datasheets
simulation/        SPICE simulation files
firmware/          Embedded code (if applicable)
errata/            Known issues per board revision
```

## Key Files

- `docs/project-brief.md` -- Requirements, specs, block diagram
- `docs/theory-of-operation.md` -- How the circuit works
- `docs/design-notes.md` -- Analog rationale, calculations
- `docs/fabrication-notes.md` -- PCB specs, DFM constraints
- `docs/assembly.md` -- Build instructions
- `docs/test-and-calibration.md` -- Test procedures, acceptance criteria
- `docs/adr/*.md` -- Architecture Decision Records (see template)

## Conventions

### Documentation
- ADRs use Nygard format: Context, Decision, Alternatives, Consequences
- ADRs numbered: `0001-topic.md`, `0002-topic.md`, ...
- ADR status: Proposed | Accepted | Superseded by ADR-NNNN
- Inline ADR references: `(see ADR-NNNN)` or `See ADR-NNNN`
- Reference sections use: `[Title](URL) -- Description` (double-dash separator)
- CHANGELOG follows Keep a Changelog format
- Commits follow Conventional Commits: `feat(hw):`, `fix(pcb):`, `docs:`

### Units and Notation
- Current: `uA`, `mA` (ASCII `u` for micro, per ISO 2955)
- Resistance: `k` for kilo-ohm, `ohm` spelled out below 1k (e.g. `49.9k`, `267 ohm`)
- Capacitance: `nF`, `uF` (not `µF` in source files)
- Frequency: `Hz`, `kHz`, `MHz`
- Voltage: `V`, `mV` (e.g. `+5V`, `-12V`, `2.5V`)
- Temperature coefficient: `ppm/C`
- Approximate values: `~` prefix (e.g. `~50 Hz to ~60 kHz`)
- Equations in code blocks: spaces around operators (e.g. `I = 1V / 49.9k = 20 uA`)

### Datasheets
- Stored in `datasheets/`
- Named `<PartNumber>-<short-description>.pdf` (e.g. `SSI2131-vco-ic.pdf`)
- Part number first (matches BOM/schematic), lowercase description after
- Use hyphens as separators, no spaces or underscores
- One PDF per component (or component family if a single datasheet covers variants)

### KiCad
- All libraries are project-local under `hardware/lib/`
- Library paths use `${KIPRJMOD}/lib/...` (never absolute paths)
- Schematic is the single source of truth for the BOM
- BOM fields: Reference, Value, Footprint, MPN, Manufacturer, Supplier, SPN, Description
- Run ERC and DRC before every commit

### Git
- Work on `main` branch (linear history, no merge commits)
- Tag fabrication runs: `git tag -a v1.0-rev-a -m "Rev A for fab YYYY-MM-DD"`
- Never commit: `.kicad_prl`, `fp-info-cache`, `*-bak`, `_autosave-*`
- Commit schematic and PCB atomically (both in sync)

### Eurorack Electrical
- Power: +12V / -12V via 10-pin shrouded header
- Local regulation for +5V and other rails as needed
- Reverse polarity protection on power input
- Signal levels: 10Vpp (+-5V) audio, 0-10V or +-5V CV
- 100nF decoupling on every IC power pin

## Working with Claude Code

### Before making design changes
1. Read the relevant ADRs in `docs/adr/` for prior decisions
2. Check `docs/design-notes.md` for analog rationale
3. Review `docs/project-brief.md` for requirements

### When creating a new ADR
- Use the template in `docs/adr/0000-adr-template.md`
- Number sequentially after the highest existing ADR
- Set status to "Proposed" initially

### When updating documentation
- Keep docs consistent with schematic/PCB state
- Update CHANGELOG.md for notable changes
- Cross-reference ADRs when decisions change

### File types Claude should NOT edit
- `*.kicad_sch`, `*.kicad_pcb`, `*.kicad_pro` -- binary-like, edit in KiCad only
- `*.kicad_sym`, `*.kicad_mod` -- library files, edit in KiCad only
- `datasheets/*` -- reference PDFs, read-only
