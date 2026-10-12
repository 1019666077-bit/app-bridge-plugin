# App Bridge

**For Cursor and Grok Bot.**

**Free, MIT.** Thin plugin that connects agents to **local Windows apps** via UI Automation: list open windows, read on-screen text, take a screenshot. No tray exe.

## Free vs Pro

| Tier | In this plugin |
| --- | --- |
| **Free** | `Screenshot`, `Snapshot` (UI text / tree), `DisplayInventory` (+ upstream always keeps `ControlStatus`) |
| **Pro** | Placeholders only — click, type, scroll, shortcuts, launch/control apps — **not implemented** in Free (`mcp.json` whitelists Free tools only) |

WeChat / 微信 may appear in the window list like any other app. That is an **optional example**, not a supported automation target — do **not** promise reliable WeChat control.

## Important

This marketplace plugin **does not** ship a custom automation engine. Real desktop access is the local MCP server forked from [CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP) (MIT):

https://github.com/1019666077-bit/Windows-MCP

Vendored checkout for local runs: `_windows_mcp_src/` (git submodule-style folder; keep MIT attribution).

Homepage (coming soon): https://mymoying.com/app-bridge

## Install

1. Clone into `~/.cursor/plugins/local/app-bridge` with submodules:

   ```powershell
   git clone --recurse-submodules https://github.com/1019666077-bit/app-bridge-plugin.git "$env:USERPROFILE\.cursor\plugins\local\app-bridge"
   ```

   Or Cursor Marketplace / Grok Bot Connect Apps after listing, then **Reload Window**.
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (this machine uses `C:\Users\<user>\.local\bin\uv.exe`).
3. First start runs `uv sync` / pulls CPython **3.14+** for Windows-MCP (see `_windows_mcp_src/.python-version`).
4. Ask to list windows / read UI text / screenshot, or run `/list-windows`.

`mcp.json` uses an absolute `uv.exe` path so Cursor’s process PATH does not need `\.local\bin`. Adjust the path if your uv install differs.

## What’s inside

| Piece | Role |
| --- | --- |
| `mcp.json` | Starts forked `windows-mcp serve` with Free `--tools` only |
| `skills/app-bridge` | When to list / read / shoot; Pro guardrails |
| `rules/app-bridge.mdc` | Same playbook, always on |
| `commands/list-windows`, `read-ui`, `shot-window`, `check-app-bridge` | Common flows |
| `_windows_mcp_src/` | MIT fork of Windows-MCP |

## Local smoke test

```powershell
cd $env:USERPROFILE\.cursor\plugins\local\app-bridge
.\scripts\smoke-free.ps1
```

Writes acceptance notes to `Desktop\cc看这里\app-bridge-local.md` when that folder exists.

## Base choice

Preferred runnable base on this host: **Windows-MCP** (Python + uv). FlaUI-MCP needs a .NET runtime or a self-contained zip; not used for this thin plugin.

## License

MIT — see `LICENSE`. Upstream Windows-MCP is MIT (CursorTouch). Keep their `LICENSE.md` under `_windows_mcp_src/`.

## Author

Moying Studio · moying.studio@outlook.com
