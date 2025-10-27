# Kostudo — VS Code ↔ Maya

Kostudo is a lightweight workflow to send Python scripts from VS Code to Autodesk Maya and optionally attach a debugger.

Repository: https://github.com/CrapyShit/Kostudo

## One-time setup in Maya

- Copy-paste and run `tools/maya_link_startup.py` in Maya's Script Editor (Python), or put it on a shelf button.
- It will:
  - Ensure `debugpy` is available (tries to install via mayapy if needed).
  - Start a debug server on `127.0.0.1:5678`.
  - Open a Maya commandPort on `:7002` to receive code from VS Code.

## Send the current file from VS Code

- Press Ctrl+Shift+P → “Run Task” → “Send current file to Maya”. It will send the file currently open in the active editor.
- Or bind a key to that task if you use it frequently.
- The task runs `tools/send_to_maya.ps1 ${file}`, which tells Maya to execute the file with `runpy.run_path()`.

Notes:
- Output and exceptions show up in Maya's Script Editor; the task only reports send status.
- If you see a connection error, make sure you ran `tools/maya_link_startup.py` in Maya so the commandPort is open on :7002.

## Debugging (optional)

- After running `tools/maya_link_startup.py`, use the included VS Code launch config:
  - Run → “Attach to Maya (debugpy 5678)”.
- Set breakpoints in your script; when you send the file, the debugger will hit them.

## Configuration

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

## License

No license has been chosen yet. If you plan to open-source this, consider adding MIT or Apache-2.0. I can add it on request.
