"""App Bridge Free smoke: list windows, read UI text, screenshot (no click/type)."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from windows_mcp.desktop.service import Desktop


def main() -> int:
    out_dir = Path(__file__).resolve().parents[1] / ".smoke-out"
    out_dir.mkdir(parents=True, exist_ok=True)
    shot_path = out_dir / "free-screenshot.png"

    desktop = Desktop()
    state = desktop.get_state(
        use_annotation=False,
        use_vision=True,
        use_dom=False,
        use_ui_tree=True,
        as_bytes=False,
        scale=0.5,
    )

    titles: list[str] = []
    if state.active_window and state.active_window.name:
        titles.append(f"[active] {state.active_window.name}")
    for w in state.windows or []:
        if w.name:
            titles.append(w.name)

    text_bits: list[str] = []
    tree = state.tree_state
    if tree is not None:
        for chunk in (
            tree.interactive_elements_to_string(),
            tree.scrollable_elements_to_string(),
            tree.semantic_tree_to_string(),
        ):
            if chunk:
                for line in str(chunk).splitlines():
                    line = line.strip()
                    if line:
                        text_bits.append(line)

    if state.screenshot is None:
        raise RuntimeError("get_state returned no screenshot")
    state.screenshot.save(shot_path)

    report = {
        "ok": True,
        "tier": "free",
        "ts": datetime.now(timezone.utc).isoformat(),
        "window_count": len(titles),
        "windows": titles[:40],
        "text_sample": text_bits[:50],
        "text_line_count": len(text_bits),
        "screenshot": str(shot_path),
        "screenshot_bytes": shot_path.stat().st_size,
        "screenshot_size": list(state.screenshot.size),
        "pro_placeholders": ["Click", "Type", "Scroll", "Move", "Shortcut", "App"],
        "wechat_note": "WeChat title may appear in window list; not a supported control target.",
    }
    report_path = out_dir / "report.json"
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    report_path.write_text(payload, encoding="utf-8")
    sys.stdout.buffer.write((payload + "\n").encode("utf-8", errors="replace"))
    sys.stderr.buffer.write(f"REPORT={report_path}\n".encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
