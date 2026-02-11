# ADR-0001: Record Architecture Decisions

**Date:** YYYY-MM-DD
**Status:** Accepted

## Context

Design decisions in hardware projects are expensive to reverse. A PCB respin costs
weeks and money. We need a way to capture the "why" behind significant design choices
so that:

- Future-us remembers why we made a decision
- Contributors understand the rationale
- We avoid re-debating settled decisions
- We have a clear record when decisions need revisiting

## Decision

We will use Architecture Decision Records (ADRs) as described by Michael Nygard,
stored as numbered Markdown files in `docs/adr/`.

Each ADR captures: Context, Decision, Alternatives Considered, and Consequences.

We will create ADRs for decisions including but not limited to:
- IC and critical component selection
- Power architecture and protection topology
- PCB layer count and stackup
- Connector and interface choices
- Significant layout decisions

## Alternatives Considered

### Informal notes in design-notes.md
- **Pros:** Simpler, less overhead
- **Cons:** Decisions get buried in prose, hard to find, no clear status tracking
- **Why rejected:** ADRs provide better structure for retrieving specific decisions

### No formal decision tracking
- **Pros:** Zero overhead
- **Cons:** Decisions are lost; leads to circular discussions months later
- **Why rejected:** The cost of a bad or forgotten decision in hardware is too high

## Consequences

### Positive
- Clear, searchable record of all significant decisions
- Onboarding is easier for collaborators
- Claude Code can read ADRs for context before suggesting changes

### Negative
- Small overhead to write each ADR
- Must remember to create ADRs for significant decisions
