# Contributing

Thank you for your interest in contributing to this project!

## How to Contribute

### Reporting Issues
- Use GitHub Issues to report bugs, design errors, or suggest improvements
- Include your KiCad version, board revision, and clear description of the issue
- Photos of physical issues (solder bridges, mechanical interference) are very helpful

### Suggesting Changes
- Open an issue describing the proposed change before starting work
- For significant changes, write an ADR (see `docs/adr/0000-adr-template.md`)

### Submitting Changes
1. Work on the `main` branch (linear history preferred)
2. Use Conventional Commits format:
   - `feat(hw): add soft sync input`
   - `fix(pcb): widen decoupling return path`
   - `docs: update calibration procedure`
3. Ensure ERC and DRC pass clean before committing
4. Commit schematic and PCB changes atomically (both files in sync)

## Development Setup

### Requirements
- KiCad [version]
- Git

### Getting Started
1. Clone the repository
2. Open the `.kicad_pro` file in `hardware/`
3. All libraries are project-local; no additional setup needed

## Code of Conduct

Be respectful. We're here to build cool synthesizer modules together.
