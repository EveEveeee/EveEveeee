# 每日 AI 资讯维护

发布目标：GitHub 个人主页 `EveEveeee/EveEveeee` 的「精选项目」下方，以及 `https://wangyangjuan.surge.sh/` 首页和独立 `#news` 栏目。

## 数据与生成

- 唯一内容源为 `data/ai-news.json`。字段：`updatedAt`、`items[].title`、`summary`、`eventDate`、`sourceLabel`、`url`。
- 全部摘要使用中文。优先阅读官方公告、发布说明、官方研究报告或原论文，核对事件日期与摘要。重点覆盖 AI 产品、模型、智能体与开发工具。
- 每次选 2–5 条值得关注的新动态，先看过去 24 小时，必要时放宽到 72 小时。按原文 URL 与事件去重。没有可靠新动态时，保留最近有效一期及其日期；不要把旧事件标成当日发布。
- 整理日期采用 Asia/Shanghai 的日期，事件日期采用官方原文的发布日期。两者明确分开。
- 更新后在本仓库执行 `python3 tools/sync-ai-news.py --site ../site-sync/wangyangjuan-site`。这会生成 README 资讯托管区块、`AI_NEWS.md`、按日 JSON 归档、网站内嵌数据和 `assets/ai-news.json`。
- 不改托管区块以外的简介、终端、封面、项目归属与链接。

## 同步与核验

本地目录为 `/Users/mima1234/Documents/划词翻译/profile-covers`；个人网站发布目录为同一父目录下的 `site-sync/wangyangjuan-site`。网站原始目录为 `/Users/mima1234/Documents/个人文件夹/wangyangjuan-site`。

更新前读取 GitHub 主分支与线上网站，确认本地没有需要保留的其他修改。对远端新增修改先合并；不要强制推送，不要覆盖并发更新。网站原始目录若有其他更新，也先合并后发布。

生成后检查 JSON、README 区块与网站内嵌数据一致，提取 HTML 的脚本并用 `node --check` 验证语法。核对来源链接能访问。提交仅与本期新闻有关的文件到 GitHub `main` 并推送；不添加密钥或身份凭据。

使用现有 Surge 登录，通过 `npx --offline surge <网站发布目录> wangyangjuan.surge.sh` 发布到原域名。同步原始目录的 `index.html` 和 `assets/ai-news.json` 前备份，并检查它们没有并发改变。无需改项目案例页、文章或分类封面。

发布后读取 GitHub 主分支和线上网站确认本期新闻与日期一致，并检查 `#news` 栏目。记录失败，不能把仅本地完成的更新报告为发布成功。
