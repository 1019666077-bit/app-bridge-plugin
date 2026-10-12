---
name: check-app-bridge
description: Verify uv, Windows-MCP Free tools whitelist, and App Bridge plugin files (no click/type)
---

Check App Bridge setup without clicking or typing into apps.

1. Confirm `uv` exists (`C:\Users\MOON\.local\bin\uv.exe` or on PATH).
2. Confirm plugin files under `~/.cursor/plugins/local/app-bridge` (or Marketplace install): `plugin.json`, `mcp.json`, `skills/app-bridge`, `rules/app-bridge.mdc`, `_windows_mcp_src`.
3. If the `app` MCP server is connected, list tools — expect only Free: `Screenshot`, `Snapshot`, `DisplayInventory`. Report an error if Click/Type appear.
4. If MCP is not connected, tell the user to enable App Bridge and Reload Window; first start may download CPython 3.14 and dependencies via uv.

Optional: run `scripts/smoke-free.ps1` for an offline Desktop API smoke (list windows / text / PNG). Do not call Pro placeholders.
