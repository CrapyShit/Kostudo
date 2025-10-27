# Kostudo — Research Project + Tooling

Animation & Rigging in Unreal Engine: Unlocking the workflow between industry standards and new horizons

This repository hosts my research project and its supporting tooling. It explores a practical, reliable pipeline between Autodesk Maya and Unreal Engine 5 (UE5) for character rigs and animation, and provides scripts/utilities to iterate quickly (send code to Maya, debug, etc.).

Repository: https://github.com/CrapyShit/Kostudo

— The code enables rapid prototyping inside Maya.
— The documentation tracks research questions, plan, experiments, and outcomes.

If you’re here only for the tooling, jump to Developer workflow.

## Research overview

Context and motivation
- Many studios lack a smooth rigging/animation workflow between Maya and UE5. Current workarounds (baked animations, Alembic, simplified rigs) often block late animation edits inside UE5 and introduce compatibility overhead.
- UE5’s pipeline and ecosystem are evolving; there is no widely adopted, standardized “rig to game” path for full-fidelity rigs today.

Objectives
- Evaluate whether a structured and dependable Maya ↔ UE5 pipeline can be built with today’s tools and formats.
- Compare alternatives and quantify trade‑offs (complexity, robustness, iteration speed, data fidelity).
- Prototype scripts to automate data prep/transfer, aiming at repeatable steps a small team could adopt.

Hypothesis and approach
- With targeted automation and careful format choices (e.g., FBX, JSON sidecars, Python APIs), it should be possible to reconstruct enough rig logic inside UE5 to support useful iterations—without full re‑rigging or excessive manual labor.

Key questions
- Which export format(s) and metadata are minimally sufficient to reproduce the required rig behavior inside UE5?
- What is the breakpoint where baked animation becomes preferable over reconstructed controls?
- How much developer time does automation save compared to manual prep in DCC tools?

Methodology (high‑level)
- Iterate on a test character and animation set; export from Maya with different strategies (baked, partial controls, metadata sidecars).
- Use Python automation (Maya cmds/OpenMaya; UE‑side import steps if applicable) to minimize human error.
- Measure: round‑trip time, failure modes, editability in UE5, and visual parity.

## Research plan and milestones

Timeline (academic year)
1) Literature review — October
   - Survey rig/animation transfer methods; collect pros/cons and studio feedback.
   - Assess feasibility of refined UE5 pipelines for small/indie filmmaking teams.

2) UE5 Rigging Pipeline Development — November → July
   2.1 Early development (November)
     - Select languages/APIs (Python, JSON, FBX, command ports) and set up this repo/workspace.
     - Prepare test assets for repeatable experiments.
   2.2 Pipeline Part 01 (December → January)
     - Extract rig data from Maya with the most workable formats (JSON sidecars, FBX).
     - Establish repository structure and automation entry points.
   2.3 Pipeline Part 02 (February → April)
     - Prototype multiple export strategies; validate on different rigs/animations.
     - Refine scripts to meet export needs and reduce manual steps.
   2.4 Pipeline Part 03 (May → July)
     - Integrate in UE; verify import correctness and data integrity.
     - Evaluate add‑on UE5 tools for final polish; fix issues found in end‑to‑end trials.

3) Thesis writing — August → September
   - Document methods, experiments, and final pipeline.
   - Analyze results and position them vs. industry standards and alternative workflows.

Deliverables tracked in this repo
- Scripts and automation glue (PowerShell and Python).
- Experiment notes and results summaries (to be added in docs/).
- Minimal test assets references and instructions (actual large assets may require Git LFS or external links).

## Developer workflow (tooling)

### One-time setup in Maya

- Copy-paste and run `tools/maya_link_startup.py` in Maya's Script Editor (Python), or put it on a shelf button.
- It will:
  - Ensure `debugpy` is available (tries to install via mayapy if needed).
  - Start a debug server on `127.0.0.1:5678`.
  - Open a Maya commandPort on `:7002` to receive code from VS Code.

### Send the current file from VS Code

- Press Ctrl+Shift+P → “Run Task” → “Send current file to Maya”. It will send the file currently open in the active editor.
- Or bind a key to that task if you use it frequently.
- The task runs `tools/send_to_maya.ps1 ${file}`, which tells Maya to execute the file with `runpy.run_path()`.

Notes:
- Output and exceptions show up in Maya's Script Editor; the task only reports send status.
- If you see a connection error, make sure you ran `tools/maya_link_startup.py` in Maya so the commandPort is open on :7002.

### Debugging (optional)

- After running `tools/maya_link_startup.py`, use the included VS Code launch config:
  - Run → “Attach to Maya (debugpy 5678)”.
- Set breakpoints in your script; when you send the file, the debugger will hit them.

### Configuration

- Host/port for the sender can be overridden:
  ```powershell
  # PowerShell (examples)
  # Send with defaults (127.0.0.1:7002):
  .\tools\send_to_maya.ps1 .\scripts\my_script.py

  # Send to a different port
  .\tools\send_to_maya.ps1 .\scripts\my_script.py -MayaPort 7003
  ```
- You can also use the Python sender directly if you prefer:
  ```powershell
  py -3 .\tools\send_to_maya.py .\scripts\my_script.py --host 127.0.0.1 --port 7002
  ```
- The task already uses PowerShell, so no local Python is required.

## Troubleshooting

- Connection refused when sending a file
  - Make sure you ran `tools/maya_link_startup.py` in Maya so the commandPort is open (default: 127.0.0.1:7002).
  - Firewalls can block localhost ports; allow Maya to listen on the chosen port.
- Git warnings on Windows (safe.directory)
  - If you see "detected dubious ownership" on external drives, run:
    - `git config --global --add safe.directory E:/Kotsudo`
- PATH not refreshed after installing Git/gh
  - Open a new PowerShell window or restart VS Code so the new PATH is picked up.

## Repository structure (high‑level)

- `tools/` — Sending and bootstrap utilities for Maya integration.
- `scripts/` — Place your experiment scripts here (examples, exporters, tests).
- `maya-stubs/` — Typing stubs for Maya modules to improve editor assistance.
- `imageAssets/` — Images/diagrams for documentation (consider Git LFS for large files).
- `README.md` — This document; research scope and developer workflow.
- `pyrightconfig.json` — Static type checking configuration for Python.

## License

- Code: PolyForm Noncommercial License 1.0.0 — noncommercial use allowed; commercial use requires permission.
  - See `LICENSE` and https://polyformproject.org/licenses/noncommercial/1.0.0/
- Documentation and media: Creative Commons Attribution‑NonCommercial 4.0 (CC BY‑NC 4.0).
  - See `LICENSE-DOCS` and https://creativecommons.org/licenses/by-nc/4.0/

Commercial licensing: open an issue on GitHub to request permission or discuss terms.

## Acknowledgements

Thanks to community resources and studio discussions referenced during the literature review. Specific citations and links will be added in the documentation as the research progresses.
