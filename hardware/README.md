# Hardware

This directory contains the KiCad project files for the main PCB.

## Files

- `[project].kicad_pro` -- KiCad project file
- `[project].kicad_sch` -- Schematic (root sheet + hierarchical sheets)
- `[project].kicad_pcb` -- PCB layout
- `[project].kicad_dru` -- Design rules (if customized)
- `sym-lib-table` -- Project symbol library table
- `fp-lib-table` -- Project footprint library table

## Libraries

All symbols, footprints, and 3D models used in this design are stored locally
under `lib/`. Library paths use `${KIPRJMOD}/lib/...` for portability.

**Never reference global KiCad libraries directly.** Copy any needed
symbols/footprints into the project-local library first.

## Setup

1. Open the `.kicad_pro` file in KiCad
2. All libraries are project-local; no additional configuration needed
3. If KiCad warns about missing libraries, ensure `sym-lib-table` and
   `fp-lib-table` are present and use `${KIPRJMOD}` paths
