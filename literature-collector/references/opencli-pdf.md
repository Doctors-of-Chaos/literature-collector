# 用 OpenCLIApp 下载机构全文

公开 PDF 实测组合为 OpenCLIApp `0.1.38`（自带 `opencli` `1.8.6`）和 Browser Bridge `1.0.27`。首次接入图书馆后先下载一篇，确认 PDF 能打开并读到正文。

1. 安装并打开 OpenCLIApp，使用它配套的 `opencli` 命令。在要访问图书馆的 Chrome 用户配置中，单独安装商店里名为「OpenCLI」的 Browser Bridge 扩展。运行 `opencli doctor`，确认输出含 `Extension: connected`。附带的保存脚本需要 Python 3。 [官方 App 下载](https://opencli.info/download/) · [GitHub 安装包镜像](https://github.com/jackwener/opencli-website/releases/latest) · [Chrome 扩展](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk)
2. 通过自己的图书馆入口，在 Chrome 中打开出版社的**论文正文页面**。需要登录或验证码时，在 Chrome 中操作。多套 Chrome 用户配置同时连接时，按本机 `opencli profile --help` 选择刚登录图书馆的那套。
3. 把 Chrome 切到这篇论文的 HTML 标签页，用一个会话名接手它。根据页面显示核对题名，并从 PDF 按钮或链接取得实际地址。若是代理改写过的地址，保留其域名和查询参数。临时链接仅用于本次下载，结果清单使用 DOI 或论文页面链接。

   ```bash
   opencli browser paper bind
   opencli browser paper state
   ```

4. 如果 PDF 地址和正文页面同源，在技能目录运行以下命令。将 `PDF_URL` 设为刚从页面得到的地址，将输出位置换成这次任务的目标路径。脚本借用当前标签的登录状态读取 PDF，只输出本地文件路径和大小。Chrome 如果直接打开内联 PDF 阅读器，可能没有下载事件，因此这一步保留在 HTML 页面执行。

   ```bash
   python3 scripts/save_opencli_pdf.py paper "$PDF_URL" ./paper.pdf
   ```

   如果出版社的下载按钮会跳到另一域名，按网页提供的按钮在当前浏览器中下载，再从 Chrome 的下载位置取文件。

5. 打开保存的文件，核对题名或 DOI，确认有完整正文。技术检查通过也可能拿到摘要页或封面，应记为待补全文。批量处理先确认第一篇，之后逐篇记录结果。遇到失效链接或登录问题，先确认原因再重试一次。缺订阅就保留题录，继续其余条目。
6. 完成后解绑这次会话，Chrome 标签页继续留给用户。

   ```bash
   opencli browser paper unbind
   ```
