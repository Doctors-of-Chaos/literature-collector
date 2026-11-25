#!/usr/bin/env python3
"""Save a same-origin PDF from an OpenCLI session on the article's HTML page."""

import argparse
import base64
import binascii
import json
import os
from pathlib import Path
import subprocess
import tempfile


ERRORS = {
    b"WRONG_ORIGIN": "PDF 地址需要与当前论文页面同源。",
    b"NOT_PDF": "网页返回的文件没有 PDF 文件头，请检查登录状态和下载入口。",
    b"FETCH_FAILED": "当前页面取回失败，请检查链接、同源跳转和图书馆登录状态。",
}


def browser_expression(pdf_url):
    return f"""(async () => {{
      try {{
        const url = new URL({json.dumps(pdf_url)}, location.href);
        if (!['http:', 'https:'].includes(url.protocol) ||
            url.origin !== location.origin || url.username || url.password) {{
          return 'WRONG_ORIGIN';
        }}
        const response = await fetch(url, {{mode: 'same-origin', credentials: 'same-origin'}});
        if (!response.ok) return 'HTTP_' + response.status;
        const bytes = new Uint8Array(await response.arrayBuffer());
        if (String.fromCharCode(...bytes.subarray(0, 5)) !== '%PDF-') return 'NOT_PDF';
        const chunks = [];
        for (let offset = 0; offset < bytes.length; offset += 8192) {{
          chunks.push(String.fromCharCode(...bytes.subarray(offset, offset + 8192)));
        }}
        return btoa(chunks.join(''));
      }} catch {{
        return 'FETCH_FAILED';
      }}
    }})()"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("session", help="OpenCLI browser session name")
    parser.add_argument("pdf_url", help="PDF link from the article page")
    parser.add_argument("output", type=Path, help="destination PDF file")
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        parser.exit(1, "输出文件已存在，请选择新路径。\n")

    try:
        result = subprocess.run(
            ["opencli", "browser", args.session, "eval", browser_expression(args.pdf_url)],
            capture_output=True, check=True, timeout=120,
        )
    except FileNotFoundError:
        parser.exit(1, "找不到 opencli，请检查 OpenCLIApp 的命令安装。\n")
    except (subprocess.SubprocessError, OSError):
        parser.exit(1, "OpenCLI 执行失败，请检查浏览器连接和会话。\n")

    payload = result.stdout.strip()
    if payload in ERRORS:
        parser.exit(1, ERRORS[payload] + "\n")
    if len(payload) == 8 and payload.startswith(b"HTTP_") and payload[5:].isdigit():
        parser.exit(1, f"论文站点返回 HTTP {payload[5:].decode()}。\n")
    try:
        data = base64.b64decode(payload, validate=True)
    except binascii.Error:
        parser.exit(1, "OpenCLI 返回了无法识别的数据。\n")
    if not data.startswith(b"%PDF-"):
        parser.exit(1, ERRORS[b"NOT_PDF"] + "\n")

    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=args.output.parent) as temporary:
            staged = Path(temporary) / "paper.pdf"
            staged.write_bytes(data)
            os.link(staged, args.output)
    except OSError:
        parser.exit(1, "保存失败，请检查目标位置和权限，并确认文件尚未存在。\n")
    print(json.dumps({"file": str(args.output), "bytes": len(data)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
