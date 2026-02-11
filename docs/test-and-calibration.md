# Test and Calibration

## Required Equipment

- Regulated Eurorack power supply (or bench supply at +-12V)
- Digital multimeter (4.5+ digit resolution preferred)
- Frequency counter or oscilloscope
- Precision CV source (or calibrated DAC + DMM)

## 1. Preflight Checks (Before Powering On)

- [ ] Visual inspection complete (no solder bridges, no missing components)
- [ ] Continuity: no short between +12V and GND
- [ ] Continuity: no short between -12V and GND
- [ ] Continuity: no short between +12V and -12V
- [ ] Power header orientation verified (red stripe = -12V)

## 2. Initial Power-On

- [ ] Connect to power supply with current limiting if available
- [ ] Current draw +12V: ______ mA (expected: < ?? mA)
- [ ] Current draw -12V: ______ mA (expected: < ?? mA)
- [ ] No hot components after 30 seconds
- [ ] No unusual smells

## 3. Voltage Verification

| Test Point | Expected | Measured | Pass? |
|---|---|---|---|
| +12V rail | +12.0V +-0.5V | ______ V | [ ] |
| -12V rail | -12.0V +-0.5V | ______ V | [ ] |
| [Local +5V reg] | +5.00V +-0.05V | ______ V | [ ] |
| [Local -5V reg] | -5.00V +-0.05V | ______ V | [ ] |
| [VREF if applicable] | ______ V | ______ V | [ ] |

## 4. Functional Tests

- [ ] [Test 1: e.g., oscillation present on output]
- [ ] [Test 2: e.g., correct waveform shapes]
- [ ] [Test 3: e.g., full frequency range reached]
- [ ] [Test 4: e.g., CV inputs respond correctly]
- [ ] [Test 5: e.g., controls function as expected]

## 5. Calibration

### [Calibration Step 1: e.g., V/Oct Scale Trim]

1. [Detailed procedure]
2. [What to adjust]
3. [What to measure]
4. [Target values]

### [Calibration Step 2: e.g., High-Frequency Compensation]

1. [Detailed procedure]

## 6. Acceptance Criteria

| Parameter | Requirement | Measured | Pass? |
|---|---|---|---|
| [e.g., 1V/Oct tracking] | [< 5 cent over 5 oct] | ______ | [ ] |
| [e.g., Output amplitude] | [10Vpp +-10%] | ______ | [ ] |
| [e.g., Frequency range] | [20Hz - 20kHz] | ______ | [ ] |

## 7. Sign-Off

- **Tested by:** _______________
- **Date:** _______________
- **Board serial / revision:** _______________
- **Result:** PASS / FAIL
- **Notes:** _______________
