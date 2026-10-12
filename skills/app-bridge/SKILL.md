---
name: app-bridge
description: List local Windows windows, read UI text, and screenshot via App Bridge Free MCP. Use when the user asks about on-screen apps, desktop UI text, or window captures. Click/type are Pro placeholders.
---

# App Bridge (MCP · Free)

## What this is

App Bridge is a **thin Cursor plugin** over local [Windows-MCP](https://github.com/1019666077-bit/Windows-MCP) (MIT fork of CursorTouch/Windows-MCP). Free tier is **read-only desktop context**:

| Need | Tool |
| --- | --- |
| List open windows | `Snapshot` (window metadata + UI tree; `Screenshot` skips tree/window enum for speed) |
| Read UI / accessibility text | `Snapshot` |
| Capture screen or region | `Screenshot` (`region` / `display` when useful) |
| Display layout | `DisplayInventory` |
| Control owner (always kept by upstream filter) | `ControlStatus` (read-only; ignore unless diagnosing takeover) |

Pro controls (click, type, scroll, shortcuts, launch apps) are **placeholders only** in Free — `mcp.json` does not expose those tools. Do not implement or simulate them.

WeChat is an **optional example** title that may show up in a window list. Never claim guaranteed WeChat automation.

Homepage (coming soon): https://mymoying.com/app-bridge

## When to use

If the user asks what apps are open or what text is on a window, call `Snapshot`. If they mainly want a picture, call `Screenshot`. Combine both when they need windows/text and a still.

## Image must be visible

Only describe a capture **after** the image is visible in this chat. If capture fails, say so — do not invent pixels.

## If tools are missing or fail

- Confirm the App Bridge plugin is enabled and Reload Window once.
- `uv` is required. Install from https://docs.astral.sh/uv/getting-started/installation/ — absolute path in `mcp.json` is preferred on Windows.
- Windows-MCP needs **Python 3.14+** (uv downloads it into `_windows_mcp_src/.venv` on first sync).
- Some apps expose poor accessibility trees; text may be incomplete — report what Snapshot returned.

## Completion

Summarize window titles / text / that the screenshot is in chat. Reminder: Free is observe-only; Pro input is not available.
