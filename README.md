# [Module Name]: [Brief Description]

> **Status:** [Work in Progress / Prototype / Verified / Released]
> **Hardware Revision:** [Rev A / Rev B / ...]
> **License:** [CERN OHL v2 Permissive](LICENSE)

## Overview

[What this module is. 2-3 sentences describing the module's function, key features,
and target use case.]

## Specifications

| Parameter | Value |
|---|---|
| Format | Eurorack 3U |
| Width | ?? HP |
| Depth | ?? mm |
| Power (+12V) | ?? mA |
| Power (-12V) | ?? mA |
| Frequency range | ?? Hz - ?? kHz |

## Features

- [Feature 1]
- [Feature 2]
- [Feature 3]

## Documentation

- [Project Brief](docs/project-brief.md) -- Requirements and specifications
- [Theory of Operation](docs/theory-of-operation.md) -- How the circuit works
- [Design Notes](docs/design-notes.md) -- Analog rationale and calculations
- [Assembly Instructions](docs/assembly.md) -- Build guide
- [Test and Calibration](docs/test-and-calibration.md) -- Tuning procedures
- [Decision Records](docs/adr/) -- Architecture Decision Records

## Safety

**Power connector orientation:** The 10-pin Eurorack power header must be connected
with the red stripe toward the **-12V** marking on the PCB. Reversing the cable may
damage the module and/or your power supply. Verify orientation before powering on.

## Generating Fabrication Outputs

Fabrication outputs (Gerbers, BOM, etc.) are generated manually from KiCad:

1. Ensure ERC and DRC pass clean
2. Tag the commit: `git tag -a v1.0-rev-a -m "Rev A for fab"`
3. Export via File -> Fabrication Outputs in KiCad
4. Visually inspect Gerbers in GerbView before ordering

## License

This project is licensed under the [CERN Open Hardware Licence Version 2 - Permissive](LICENSE).
