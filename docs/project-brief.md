# Project Brief: [Module Name]

## Purpose

[What this module is and why it exists. What problem does it solve or what creative
capability does it provide?]

## Functional Requirements

### Inputs
- [ ] 1V/Oct CV input
- [ ] [Other CV inputs: FM, PWM, sync, ...]
- [ ] [Audio inputs if applicable]

### Outputs
- [ ] [Waveform outputs: triangle, sawtooth, pulse, ...]
- [ ] [Other outputs]

### Controls
- [ ] [Knobs: coarse tune, fine tune, ...]
- [ ] [Switches if applicable]

### Performance Targets
- [ ] [Tracking accuracy: e.g., <5 cent error over 5 octaves]
- [ ] [Frequency range: e.g., 20Hz - 20kHz]
- [ ] [Temperature stability if relevant]

## Electrical Constraints

| Parameter | Value | Notes |
|---|---|---|
| Supply voltage | +12V / -12V | Eurorack standard |
| Current budget (+12V) | ?? mA | Measured or estimated |
| Current budget (-12V) | ?? mA | Measured or estimated |
| Signal levels (audio) | 10Vpp (+-5V) | Eurorack standard |
| Signal levels (CV) | 0-10V or +-5V | Depends on function |

## Mechanical Constraints

| Parameter | Value | Notes |
|---|---|---|
| Width | ?? HP | 1 HP = 5.08mm |
| Panel height | 128.5mm | Doepfer A-100 standard |
| Depth target | < ?? mm | Skiff-friendly if possible |
| Mounting | Standard 3U rails | |

## Block Diagram

```
[Draw or describe signal flow, e.g.:]

CV Inputs --> Summing Node --> Expo Converter --> Oscillator Core
                                                      |
                                          +-----------+-----------+
                                          |           |           |
                                      Triangle    Sawtooth     Pulse
                                          |           |           |
                                      Buffer      Buffer      Buffer
                                          |           |           |
                                       Output     Output     Output
```

## References

- [Link to key datasheet]
- [Link to reference designs]
- [Link to relevant forum threads or application notes]
