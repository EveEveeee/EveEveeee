# 每日 AI 资讯归档

以官方原文为主要来源，分别记录整理日期与事件日期。

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
