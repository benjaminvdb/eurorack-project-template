# Pre-Fabrication Checklist

Run through this checklist before every fabrication order. Every item must be checked
or explicitly waived with a documented reason.

## Schematic Review

- [ ] ERC passes clean (or all warnings reviewed and accepted)
- [ ] All IC power pins connected with decoupling caps (100nF minimum)
- [ ] Unused op-amp inputs properly terminated
- [ ] Pull-up/pull-down resistors present where needed
- [ ] Connector pinouts verified against Eurorack standard
- [ ] Power header pin 1 = -12V (Doepfer convention)
- [ ] Reverse polarity protection present
- [ ] Voltage ratings on all capacitors adequate (>2x rail voltage)
- [ ] All component values verified against design calculations
- [ ] BOM fields populated: MPN, Manufacturer, Value, Footprint

## PCB Review

- [ ] DRC passes clean (or all violations reviewed and accepted)
- [ ] All copper zones filled and up to date
- [ ] Board outline (Edge.Cuts) present and correct dimensions
- [ ] Mounting holes present and correctly positioned
- [ ] Silkscreen legible (no overlapping text, component values readable)
- [ ] Revision number on silkscreen AND copper layer
- [ ] Power header orientation marked clearly on silkscreen
- [ ] Pin 1 / polarity markers on all polarized components

## Mechanical Verification

- [ ] Board dimensions fit within Eurorack HP width
- [ ] 3D view checked for component clearance conflicts
- [ ] Jack and pot positions align with front panel
- [ ] Component heights clear the available depth behind panel
- [ ] **Print footprints 1:1 and test-fit critical components on paper**

## Footprint Verification

- [ ] Every custom footprint verified against manufacturer datasheet
- [ ] Pin numbering matches datasheet (top view vs bottom view!)
- [ ] Pad sizes match manufacturer recommended land pattern
- [ ] Thermal pad / exposed pad handled correctly (if applicable)

## Fabrication Outputs

- [ ] Gerbers generated from clean, tagged commit
- [ ] Gerbers visually inspected in GerbView or online viewer
- [ ] Drill file present and correctly formatted
- [ ] Layer count in Gerbers matches the order
- [ ] BOM regenerated from current schematic state

## Final Checks

- [ ] Design has rested for at least 1 day since last change
- [ ] CHANGELOG.md updated
- [ ] Git tagged: `git tag -a vX.Y-rev-Z -m "..."`
- [ ] Fab order details match fabrication-notes.md specs

## Sign-Off

- **Reviewed by:** _______________
- **Date:** _______________
- **Revision:** _______________
- **Sent to fab:** [ ] Yes -- Fab house: _______________ Order #: _______________
