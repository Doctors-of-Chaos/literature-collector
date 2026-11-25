# Literature Collector

一个给研究者用的 Agent Skill。可以按主题或作者查文献，按篇名或 DOI 补全文，也可以把筛好的题录存进 Zotero。每篇分别记录题录核验、全文和入库状态。

## 使用

在 Codex 项目里，把本仓库的 `literature-collector` 整个子目录复制到项目的 `.agents/skills/` 下。在对话中用 `$literature-collector`，或直接描述任务。其他支持 `SKILL.md` 的 Agent 可以将这个子目录放到自己的技能目录。

- “帮我找远程康复的随机对照试验。先给 PubMed 的实际检索式和候选清单。”
- “按这份 DOI 清单补 PDF。先查本地和开放全文，再用我已登录的图书馆页面。”
- “把这批筛好的题录存到 Zotero 的远程康复收藏夹。库里已有的条目直接归入收藏夹，缺 PDF 的标出来。”

公开数据库检索可以独立运行。需要机构订阅时，这里分享的是我平时用的 **OpenCLIApp + Chrome** 流程。先在 Chrome 登录自己的图书馆，再让 OpenCLI 从论文页面取得 PDF。第一次先试一篇，确认能保存、打开并读到正文。 [下载步骤](literature-collector/references/opencli-pdf.md)

直连 Zotero 需要可用的 Zotero 工具。没有连接时，可以按需生成 RIS，之后在 Zotero 里导入。PDF 目录、机构入口和收藏夹都由使用者指定。

## 致谢

感谢 [ScanSci PDF](https://github.com/Rimagination/scansci-pdf) 的作者 Rimagination 和贡献者。这个 Skill 的全文获取流程，最早是从试用 ScanSci PDF 的经历中逐步整理出来的。

本项目采用 [MIT 许可证](LICENSE)。
