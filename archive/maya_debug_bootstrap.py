# Start a debugpy debug server inside Maya and optionally wait for a client.
# Send this file to Maya via commandPort, or paste into Maya's Script Editor (Python).
# After running, attach from VS Code using the "Attach to Maya (debugpy 5678)" configuration.

import sys

try:
    import debugpy  # type: ignore
except Exception as exc:
    msg = (
        "debugpy is not installed in Maya's Python environment.\n"
        "Install it with mayapy, e.g.:\n"
        "  C\\Program Files\\Autodesk\\Maya2024\\bin\\mayapy.exe -m pip install --user debugpy\n"
        "(Adjust the Maya version/path as needed.)\n"
        f"Import error: {exc}\n"
    )
    print(msg)
    raise

# Listen on localhost:5678 (change port if needed)
HOST = "127.0.0.1"
PORT = 5678

# If already listening, this call is harmless and will reuse the listener.
debugpy.listen((HOST, PORT))
print(f"debugpy listening on {HOST}:{PORT} — attach from VS Code now.")

# Optionally wait for the client to attach before continuing
# debugpy.wait_for_client()
# debugpy.breakpoint()  # Uncomment to break here immediately once attached
