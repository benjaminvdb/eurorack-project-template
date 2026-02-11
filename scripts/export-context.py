#!/usr/bin/env python3
"""Export KiCad schematic into LLM-friendly context files.

Usage:
    python scripts/export-context.py                              # auto-finds schematic
    python scripts/export-context.py hardware/my-module.kicad_sch # explicit path

Outputs to docs/context/ (gitignored, regenerable).
Requires: kicad-cli (ships with KiCad 8+)
"""

import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def find_kicad_cli():
    """Locate kicad-cli on any platform."""
    cli = shutil.which("kicad-cli")
    if cli:
        return cli

    # Platform-specific fallback locations
    candidates = [
        # macOS
        Path("/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"),
        # Windows (common install paths)
        Path("C:/Program Files/KiCad/9.0/bin/kicad-cli.exe"),
        Path("C:/Program Files/KiCad/8.0/bin/kicad-cli.exe"),
    ]
    for path in candidates:
        if path.is_file():
            return str(path)

    return None


def find_schematic(project_root):
    """Find the first .kicad_sch in hardware/."""
    hw_dir = project_root / "hardware"
    if not hw_dir.is_dir():
        return None
    for sch in sorted(hw_dir.rglob("*.kicad_sch")):
        if sch.name.startswith("_autosave-") or "-bak" in sch.name:
            continue
        return sch
    return None


def run_kicad_cli(cli, args, allow_failure=False):
    """Run a kicad-cli command, printing its stderr on failure."""
    cmd = [cli] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 and not allow_failure:
        print(f"  WARNING: command failed: {' '.join(cmd)}", file=sys.stderr)
        if result.stderr:
            print(f"  {result.stderr.strip()}", file=sys.stderr)
    return result.returncode == 0


def export_bom(cli, sch_file, output_path):
    """Export BOM as CSV with full component fields."""
    # Try detailed export first; fall back to defaults if it fails
    ok = run_kicad_cli(cli, [
        "sch", "export", "bom",
        "--fields", "Reference,Value,Footprint,${QUANTITY},${DNP},"
                     "MPN,Manufacturer,Description",
        "--labels", "Ref,Value,Footprint,Qty,DNP,MPN,Manufacturer,Description",
        "--group-by", "Value,Footprint,MPN",
        "--sort-field", "Reference",
        "--exclude-dnp",
        "--output", str(output_path),
        str(sch_file),
    ], allow_failure=True)

    if not ok:
        run_kicad_cli(cli, [
            "sch", "export", "bom",
            "--output", str(output_path),
            str(sch_file),
        ])


def export_netlist(cli, sch_file, output_path, fmt):
    """Export netlist in the given format."""
    run_kicad_cli(cli, [
        "sch", "export", "netlist",
        "--format", fmt,
        "--output", str(output_path),
        str(sch_file),
    ])


def export_pdf(cli, sch_file, output_path):
    """Export schematic as PDF."""
    run_kicad_cli(cli, [
        "sch", "export", "pdf",
        "--no-background-color",
        "--output", str(output_path),
        str(sch_file),
    ])


def export_svg(cli, sch_file, output_dir):
    """Export schematic as SVG (one per sheet)."""
    run_kicad_cli(cli, [
        "sch", "export", "svg",
        "--no-background-color",
        "--output", str(output_dir),
        str(sch_file),
    ])


def export_erc(cli, sch_file, output_path):
    """Run ERC and export JSON report."""
    run_kicad_cli(cli, [
        "sch", "erc",
        "--format", "json",
        "--severity-all",
        "--output", str(output_path),
        str(sch_file),
    ], allow_failure=True)  # ERC violations cause non-zero exit


def generate_summary(bom_path, spice_path, output_path):
    """Combine BOM and SPICE netlist into a compact text summary."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# Schematic Summary",
        f"# Generated: {now}",
        "",
    ]

    if bom_path.is_file():
        lines.append("## Components")
        lines.append("")
        lines.append(bom_path.read_text(encoding="utf-8"))

    if spice_path.is_file():
        lines.append("## SPICE Netlist")
        lines.append("")
        lines.append(spice_path.read_text(encoding="utf-8"))

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    context_dir = project_root / "docs" / "context"

    # --- Find kicad-cli ---
    cli = find_kicad_cli()
    if not cli:
        print("Error: kicad-cli not found.", file=sys.stderr)
        print("Install KiCad 8+ or add kicad-cli to your PATH.", file=sys.stderr)
        sys.exit(1)

    # --- Find schematic ---
    if len(sys.argv) > 1:
        sch_file = Path(sys.argv[1]).resolve()
    else:
        sch_file = find_schematic(project_root)

    if not sch_file or not sch_file.is_file():
        print("Error: No .kicad_sch file found.", file=sys.stderr)
        print(f"Usage: python {sys.argv[0]} [path/to/schematic.kicad_sch]",
              file=sys.stderr)
        sys.exit(1)

    name = sch_file.stem  # filename without .kicad_sch

    print(f"Exporting context for: {sch_file}")
    print(f"Output directory: {context_dir}")
    context_dir.mkdir(parents=True, exist_ok=True)

    # --- Run exports ---
    bom_path = context_dir / f"{name}-bom.csv"
    xml_path = context_dir / f"{name}-netlist.xml"
    spice_path = context_dir / f"{name}-netlist.spice"
    pdf_path = context_dir / f"{name}-schematic.pdf"
    erc_path = context_dir / f"{name}-erc.json"
    summary_path = context_dir / f"{name}-summary.txt"

    print("  [1/6] BOM (CSV)...")
    export_bom(cli, sch_file, bom_path)

    print("  [2/6] Netlist (XML)...")
    export_netlist(cli, sch_file, xml_path, "kicadxml")

    print("  [3/6] Netlist (SPICE)...")
    export_netlist(cli, sch_file, spice_path, "spice")

    print("  [4/6] Schematic PDF...")
    export_pdf(cli, sch_file, pdf_path)

    print("  [5/6] Schematic SVG...")
    export_svg(cli, sch_file, context_dir)

    print("  [6/6] ERC report (JSON)...")
    export_erc(cli, sch_file, erc_path)

    print("  [+] Generating compact text summary...")
    generate_summary(bom_path, spice_path, summary_path)

    # --- Summary ---
    print()
    print(f"Done. Context files in {context_dir}/:")
    for f in sorted(context_dir.iterdir()):
        if f.is_file():
            print(f"  {f.name}")

    print()
    print("For Claude Code, the most useful files are:")
    print(f"  {name}-summary.txt    -- compact text overview (lowest token cost)")
    print(f"  {name}-bom.csv        -- full component list")
    print(f"  {name}-schematic.pdf  -- visual schematic (use Read tool)")
    print(f"  {name}-netlist.xml    -- full connectivity details")


if __name__ == "__main__":
    main()
