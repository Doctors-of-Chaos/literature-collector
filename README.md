# Literature Collector

一个给研究者用的 Agent Skill。可以按主题或作者查文献，按篇名或 DOI 补全文，也可以把筛好的题录存进 Zotero。每篇分别记录题录核验、全文和入库状态。

## 使用

在 Codex 项目里，把本仓库的 `literature-collector` 整个子目录复制到项目的 `.agents/skills/` 下。在对话中用 `$literature-collector`，或直接描述任务。其他支持 `SKILL.md` 的 Agent 可以将这个子目录放到自己的技能目录。

- “帮我找远程康复的随机对照试验。先给 PubMed 的实际检索式和候选清单。”
- “按这份 DOI 清单补 PDF。先查本地和开放全文，再用我已登录的图书馆页面。”
- “把这批筛好的题录存到 Zotero 的远程康复收藏夹。库里已有的条目直接归入收藏夹，缺 PDF 的标出来。”

## 完整流程需要安装什么

跑完「检索 → 下载机构全文 → 自动存进 Zotero」需要下面两项。

- **Zotero 桌面端 + Zotero MCP**。从 `cookjohn/zotero-mcp` 的 Releases 下载 `.xpi`，在 Zotero 的「工具 → 附加组件」中安装。重启 Zotero，在插件设置中启用 MCP 服务，并把插件生成的客户端配置加到你的 Agent。自动查重、入库和挂 PDF 都通过这条连接。 [Zotero MCP 仓库](https://github.com/cookjohn/zotero-mcp) · [插件安装包](https://github.com/cookjohn/zotero-mcp/releases)
- **OpenCLIApp + Chrome + OpenCLI Browser Bridge 扩展**。先安装并打开 OpenCLIApp，再在用来登录图书馆的 Chrome 用户配置中单独安装商店里名为「OpenCLI」的扩展。使用 App 自带的 `opencli`，运行 `opencli doctor`，看到 `Extension: connected` 后再开始。附带的 PDF 保存脚本需要 Python 3。 [官方 App 下载](https://opencli.info/download/) · [GitHub 安装包镜像](https://github.com/jackwener/opencli-website/releases/latest) · [Chrome 扩展](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk) · [下载步骤](literature-collector/references/opencli-pdf.md)

只查公开数据库可以直接用。Zotero MCP 尚未连接时，可以先导出 RIS，再手动导入 Zotero。PDF 目录、机构入口和收藏夹都由使用者指定。

> **OpenCLIApp 桌面版**最近一次公开发布是 2026 年 8 月的 `0.1.38`。截至 2026 年 11 月 25 日，约三个月未见桌面版公开更新。后续维护情况，以及它与新版 Chrome、Browser Bridge 扩展配合时的稳定性，仍不明确。 [桌面版发布记录](https://github.com/jackwener/opencli-website/releases/tag/app-v0.1.38)

## 文献下载注意事项

> [!WARNING]
> 学生和研究人员在下载前，请自行查阅所在学校或研究单位的电子资源使用文件，并遵守单位和数据库平台的规定。先确认是否允许自动下载，以及适用的下载频率和数量限制。
>
> 短时间内大量下载文献，可能触发中国知网（CNKI）暂停下载或冻结账号。学校或研究单位也可能按规定封禁账号或暂停电子资源访问权限。 [中国知网会员服务使用协议](https://wap.oversea.cnki.net/cn/member/agreement.html) · [高校图书馆违规处理规则示例](https://library.sdu.edu.cn/page/id-232.html)
>
> 本项目为开源程序。对于因使用本项目超量下载或违反相关规定而导致的知网账号、学校账号被封禁，本项目概不负责。

## 致谢

- 感谢 **Rimagination** 和 ScanSci PDF 的贡献者。这个 Skill 的全文获取流程，最早是从试用该项目的经历中逐步整理出来的。 [ScanSci PDF](https://github.com/Rimagination/scansci-pdf)
- 感谢 **jackwener** 和 OpenCLI 项目的贡献者。OpenCLIApp 和 Browser Bridge 让这个流程能复用 Chrome 里的图书馆登录。 [OpenCLI](https://github.com/jackwener/OpenCLI) · [OpenCLIApp](https://opencli.info/download/)
- 感谢 **cookjohn** 和 Zotero MCP 的贡献者。这个插件提供了查询 Zotero、保存题录和挂载 PDF 的接口。 [Zotero MCP](https://github.com/cookjohn/zotero-mcp)

本项目采用 [MIT 许可证](LICENSE)。
