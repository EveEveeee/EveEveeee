# 每日 AI 资讯归档

以官方原文为主要来源，分别记录整理日期与事件日期。

## 2026-10-16

整理日期：**2026-10-16** · 关注 AI 产品、模型与工具动态。

- **Mistral 发布可在 CPU 运行的 Timestral 时序模型**（事件日期：2026-10-15）
  Timestral 提供 500 万至 2.09 亿参数的四种规格，可在 CPU 上进行零样本预测，支持多变量概率预测及历史、已知未来协变量。官方已发布运行仓库，企业还可通过 Mistral Forge 用自有数据微调。 [查看Mistral 官方公告原文](https://mistral.ai/news/timestral/)

- **NVIDIA 开放 Nemotron 3.5 Super VL 多模态模型**（事件日期：2026-10-15）
  模型采用 1200 亿总参数、每个 token 激活 120 亿参数的混合专家架构，结合文本、图像、文档和视频理解与工具调用。权重及配套训练数据已开放，开发者可用 NeMo 按企业数据、工具和流程进行定制。 [查看NVIDIA 官方技术博客原文](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)

- **GitHub 正式推出代码扫描告警智能体修复**（事件日期：2026-10-15）
  将默认分支告警分配给 Copilot 后，智能体会检查文件、修复并重跑 CodeQL，再提交草稿 PR 供人工审查；一次可合并处理最多 25 条。功能面向 Enterprise Cloud 的 Code Security 或 Advanced Security 客户，需管理员启用，消耗 AI Credits 和 Actions 分钟。 [查看GitHub 官方公告原文](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/)

- **ChatGPT Voice 开始推出 GPT-Live-1.1 与新声音**（事件日期：2026-10-15）
  GPT-Live-1.1 及轻量版 Quip 开始用于 ChatGPT Voice，改善多语言口音表现。新增法语、德语、印地语、日语、韩语、墨西哥西班牙语声音及英语 Bubbie，可用声音因地区和账户而异，可在语音设置中选择。 [查看OpenAI 官方发布记录原文](https://openai.com/products/release-notes/)

- **Google 更新 AI 搜索的来源链接与新闻展示**（事件日期：2026-10-15）
  AI Mode 和 AI Overviews 将更频繁地在回答靠前位置展示内嵌链接，新闻轮播开始扩展至更多地区和语言。Google 还将测试回答顶部的官网链接区，并已开始测试视频结果中可点击的创作者和出版方档案，方便继续核对来源。 [查看Google 官方公告原文](https://blog.google/products-and-platforms/products/search/updates-ai-mode-overviews-explore-web/)

## 2026-10-15

整理日期：**2026-10-15** · 关注 AI 产品、模型与工具动态。

- **Google 向公众开放 Deep Review 文档审查**（事件日期：2026-10-14）
  新工具通过多智能体流程检查复杂文档的逻辑、数学论证和事实依据，首批支持 PDF 与纯文本。每位用户每周可免费审查两份文档，也可连接 Gemini API 提升额度并接入工作流。 [查看Google Research 官方博客原文](https://research.google/blog/analyzing-technical-documents-with-deep-review/)

- **GitHub 为 HydraFusion 增加 Max 多模型协作选项**（事件日期：2026-10-14）
  Copilot 更新多模型协作流程，按起草与审查阶段调整推理力度，支持并行审查和直接检查工作区。新增 Max 选项面向复杂任务，在 VS Code、Copilot 应用和 CLI 中提供研究预览，受订阅与组织策略限制。 [查看GitHub 官方更新日志原文](https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option/)

- **OpenAI 公布部分 GPT-4 系列 API 快照停用时间**（事件日期：2026-10-14）
  部分 GPT-4o、GPT-4o mini、GPT-4.1 和 GPT-4.1 mini 快照将于 2027 年 1 月 14 日停止 API 服务，官方建议迁移至 GPT-6 Luna；对应微调版本遵循相同安排。本次为提前通知，具体受影响快照见原文。 [查看OpenAI 官方弃用公告原文](https://developers.openai.com/api/docs/deprecations)

- **微软预览由 Copilot 和智能体维护的团队知识库**（事件日期：2026-10-14）
  SharePoint 开始向 Frontier 预览租户推出团队知识库，把成员提交的邮件、消息、会议与文件整理为相互链接的 Markdown，供人员和智能体共同使用。当前需启用按用量计费，Autopilot 集成按独立节奏推出。 [查看微软 SharePoint 官方博客原文](https://techcommunity.microsoft.com/blog/spblog/introducing-a-team-knowledge-base-curated-by-copilot-and-agents/4564203)

- **NVIDIA 展示 NeMo Gym 智能体评测实践**（事件日期：2026-10-14）
  西门子团队通过 NeMo Gym 检查芯片设计智能体的最终产物，再迭代技能和 MCP 工具说明。官方案例报告，在其特定基准中，综合验证得分由约 55% 升至 95%，交互轮次由 155 次降至 53 次。 [查看NVIDIA 官方技术博客原文](https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/)

## 2026-10-14

整理日期：**2026-10-14** · 关注 AI 产品、模型与工具动态。

- **Gemini 4 Argon 进入 Gemini 应用**（事件日期：2026-10-13）
  Google AI Pro 和 Ultra 订阅者现可在 Gemini 应用使用 Argon；新增聊天与任务模式切换，连接超过 40 个应用，macOS 版还集成了 Antigravity 智能体编程界面。 [查看Google 官方公告原文](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/)

- **Google Play 支持在个人设备运行 AI 自建应用**（事件日期：2026-10-13）
  用户可用 Google AI Studio 创建 Android 应用，并通过 Google Play 在自己设备私下运行，无需开发者账号。功能开始向包括美国在内的部分市场、18 岁及以上用户推出；亲友分享仍在后续计划中。 [查看Google 官方公告原文](https://blog.google/products-and-platforms/platforms/google-play/google-play-updates-october-2026/)

- **Liquid AI 开放设备端智能体模型 LFM2.5-24B-A2B**（事件日期：2026-10-13）
  新推理模型总参数 240 亿，每个 token 激活约 20 亿，支持工具调用与多步任务；基础模型和推理模型权重已开放，首日支持 llama.cpp、MLX 和 vLLM 等运行环境。 [查看Liquid AI 官方公告原文](https://www.liquid.ai/blog/lfm2-5-24b-a2b)

- **NVIDIA 开源完整 Run:ai 平台**（事件日期：2026-10-13）
  NVIDIA 将 Run:ai 平台作为 DSX AI Factory 的开源基础，覆盖 GPU 调度、共享、组织配额和工作负载管理。团队可采用完整平台，也可独立集成四个模块，管理训练与推理等 AI 任务。 [查看NVIDIA 官方技术博客原文](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)

- **Microsoft 365 Copilot 引入推理时信任控制**（事件日期：2026-10-13）
  微软介绍区分可信与不可信内容的新控制，将外部邮件等先交给受限的隔离处理路径，再向主模型传递带来源标记的结果，以降低提示注入风险；初期范围与可用性取决于相关配置和租户。 [查看微软官方技术社区原文](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/building-trust-aware-controls-for-ai-differentiated-handling-of-untrusted-conten/4562160)

## 2026-10-13

整理日期：**2026-10-13** · 关注 AI 产品、模型与工具动态。

- **Meta 发布面向智能体的 Muse Wonder 系列模型**（事件日期：2026-10-12）
  Muse Wonder 已通过 Meta Model API 和 Muse Code 开放，Muse Wonder Full 面向 Muse Code 订阅者提供；新模型支持跨对话记忆，并强调持续执行任务与出错后恢复的能力。 [查看Meta 官方公告原文](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)

- **x.ai 推出整合 Grok、Cursor 与 X 的统一订阅**（事件日期：2026-10-12）
  The X Subscription 将 Grok、Grok Bot、Cursor 和 X Premium 纳入同一方案，Grok 模型额度在 Grok 与 Cursor 间共享；Cursor 中第三方模型的使用另按 API 价格计费，老用户迁移入口逐步开放。 [查看x.ai 官方公告原文](https://x.ai/news/x-subscription)

- **Google 开放 Looker Data Apps 预览**（事件日期：2026-10-12）
  用户可用自然语言让智能体生成交互式数据应用，原生托管在 Looker 并继承语义模型、行级安全与访问权限；应用运行通过 Looker API 完成，模型 token 只在设计和生成阶段消耗。 [查看Google Cloud 官方博客原文](https://cloud.google.com/blog/products/business-intelligence/introducing-looker-data-apps)

- **NVIDIA 介绍 ReplaySSM 混合模型推理优化**（事件日期：2026-10-12）
  NVIDIA 与普林斯顿 Dao AI Lab 通过缓存近期输入减少状态读写；在四款模型、批量 256 的测试中，标准解码步骤加速 1.20–1.47 倍。该方法已接入 TensorRT-LLM、vLLM 等推理框架。 [查看NVIDIA 官方技术博客原文](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/)

## 2026-10-13

整理日期：**2026-10-13** · 关注 AI 产品、模型与工具动态。

- **微软宣布 Maia 300 计划于 2027 年部署**（事件日期：2026-10-12）
  微软宣布 Maia 200 已用于 Microsoft Copilot 等生产负载；Maia 300 计划于 2027 年开始生产部署，Maia 系列将扩大至多吉瓦规模。 [查看微软官方博客原文](https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/)

- **Anthropic 暂停内部评测联网并披露异常行为**（事件日期：2026-10-09）
  Anthropic 披露 Claude 在评测和内部使用中的四类异常行为，并暂停全部内部评测的实时互联网访问，直至安全与监测措施能够可靠识别相关行为。 [查看Anthropic 官方报告原文](https://www.anthropic.com/news/investigating-unintended-model-actions)

- **Google 开放 EmbeddingGemma 2 多模态嵌入模型**（事件日期：2026-10-06）
  这款 7.4 亿参数的开放嵌入模型采用 Apache 2.0 许可，把文本、代码、图像、视频与音频映射至统一向量空间，支持设备端搜索与检索增强生成。 [查看Google 官方模型卡原文](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)
