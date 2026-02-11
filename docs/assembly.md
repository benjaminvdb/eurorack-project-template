# Assembly Instructions

## Required Tools

- Soldering iron with fine tip (chisel or conical)
- Solder (leaded 63/37 or lead-free, 0.5-0.8mm diameter)
- Flush cutters
- Multimeter
- [Solder wick or desoldering pump for rework]
- [Tweezers if SMD components present]

## Before You Begin

- Read through these instructions completely before soldering
- Verify all components against the BOM
- Check the PCB for manufacturing defects (shorts, missing copper, scratches)

## Build Order

Solder components in order of height, lowest first:

### Step 1: [SMD components (if any)]
- [List specific components]
- [Orientation notes]

### Step 2: Resistors
- [List values and positions, or reference the interactive BOM]

### Step 3: Diodes
- **Check polarity!** Cathode band orientation marked on silkscreen.
- [List specific diodes and positions]

### Step 4: IC Sockets
- **Do NOT solder ICs directly.** Use sockets.
- Align the notch with the silkscreen marking.
- [List ICs and socket positions]

### Step 5: Capacitors
- Ceramic capacitors: no polarity
- **Electrolytic capacitors: check polarity!** Stripe = negative.
- [List specific capacitors]

### Step 6: Connectors
- **Power header (critical!):** Pin 1 / red stripe = -12V. Verify with silkscreen.
- Use a shrouded header to prevent reverse insertion.
- [Other connectors]

### Step 7: Mechanical Components (Jacks and Pots)

> **Important alignment step:** Place all jacks and pots but do NOT solder them.
> Attach the front panel and tighten the nuts to align components with the panel
> holes. THEN solder the pins from the back. This prevents misalignment.

### Step 8: Insert ICs
- Align pin 1 (dot/notch) with socket marking
- Press firmly and evenly; do not bend pins

## Polarity and Orientation Checklist

- [ ] Power header: red stripe = -12V
- [ ] All electrolytic capacitors: stripe = negative
- [ ] All diodes: cathode band matches silkscreen
- [ ] All ICs: pin 1 dot/notch aligned with socket

## Post-Assembly Inspection

- [ ] Visual check for solder bridges (especially around IC sockets)
- [ ] Check for cold joints (dull, lumpy solder)
- [ ] Continuity: no short between +12V and GND
- [ ] Continuity: no short between -12V and GND
- [ ] Continuity: no short between +12V and -12V
- [ ] Proceed to [Test and Calibration](test-and-calibration.md)
