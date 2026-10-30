# 每日 AI 资讯归档

以官方原文为主要来源，分别记录整理日期与事件日期。

## 2026-10-30

整理日期：**2026-10-30** · 关注 AI 产品、模型与工具动态。

- **Gemini 支持在聊天中直接生成和编辑文件**（事件日期：2026-10-29）
  可在聊天里生成、预览和修改文档、表格、演示、PDF 及代码，并支持全屏手动编辑或选中内容让 Gemini 调整。面向 Gemini 已支持的地区与语言用户开放；PDF 支持网页和移动端，其余格式目前仅支持网页。 [查看Google 官方博客原文](https://blog.google/innovation-and-ai/products/gemini-app/edit-files-directly/)

- **Mistral Large 4 开放权重，支持自部署与微调**（事件日期：2026-10-29）
  官方发布 FP8、NVFP4 权重，支持文本与图像输入，并提供 Transformers、vLLM、llama.cpp 推理及 TRL 微调支持。采用 Mistral 开放权重许可，模型即服务经营者的商用受额外许可约束。 [查看Hugging Face 官方博客原文](https://huggingface.co/blog/mistral-large4)

- **Hugging Face 发布 Swift 语音与决策开发包**（事件日期：2026-10-29）
  AnySpeechRecognizer 接入本地语音引擎并支持说话人分离；AnyDecisionModel 返回带概率的分类、选择和评分结果。最低要求 Swift 6.2、macOS/iOS 26 及以上，部分后端另有硬件、工具链及系统要求。 [查看Hugging Face 官方博客原文](https://huggingface.co/blog/anydecisionmodel)

## 2026-10-29

整理日期：**2026-10-29** · 关注 AI 产品、模型与工具动态。

- **ChatGPT 开始测试通过 iMessage 和 RCS 联系 dot**（事件日期：2026-10-28）
  美国 Pro 用户开始获得 dot 消息渠道测试，可通过 iMessage 或 Android RCS 进行一对一文字、照片及语音交流，并接收主动更新。需要审批时，dot 会发送链接让用户回到 ChatGPT 处理；当前仍为逐步开放的 beta。 [查看OpenAI 官方功能说明原文](https://learn.chatgpt.com/docs/whats-new/dots-october-28-2026)

- **Google 发布 Gemini 4 Carbon，强化多步编程与网络防御**（事件日期：2026-10-28）
  Gemini 4 Carbon 加强持续多步软件工程任务，以及漏洞检测、风险验证和代码修补能力。本周先向部分网络防御者开放，再通过 Fairwind 计划扩大受信伙伴范围；普通开发者、企业和消费者版本仍待推出。 [查看Google 官方公告原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

- **Google 预览 Connected Apps 平台，统一接入 Search 与 Gemini**（事件日期：2026-10-28）
  开发者可接入云端 MCP 或 Android AppFunctions，在统一控制台注册、测试并提交应用，选择发布至 Search、Gemini 或两者，并监测流量、延迟和错误。平台需报名并分阶段开放；部分 Gemini 集成已上线，Search 接入仍将在后续数周推出。 [查看Google 官方公告原文](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/)

- **英伟达发布 Nemotron 3.5 Transcribe，扩展多语语音处理**（事件日期：2026-10-28）
  模型面向录制音频，支持 40 语转录、31 语与英语互译及 13 语说话人归属。配套 Granary v2 公开 48 语的语料清单和处理流水线，源音频需按各上游语料许可另行获取。 [查看英伟达官方文章原文](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)

## 2026-10-28

整理日期：**2026-10-28** · 关注 AI 产品、模型与工具动态。

- **Liquid AI 开放 LFM3 多模态模型家族**（事件日期：2026-10-27）
  Liquid AI 发布六种约 20 亿参数的 LFM3 型号，覆盖文本、视觉、语音、全模态和结构化决策，开放权重及单 GPU 微调示例。文本型号采用 LFM Open License v1.0，官方不建议其用于复杂多步推理或智能体编程。 [查看Liquid AI 官方博客原文](https://huggingface.co/blog/LiquidAI/lfm3)

- **Gemini Robotics ER 2 进入 Google Cloud 公开预览**（事件日期：2026-10-27）
  开发者可通过 Gemini platform 的 Model Garden 试用 ER 2，将动作模型、导航 API 和自定义函数作为工具，结合视频、音频及文本开展任务规划、执行核验和多机器人协作。当前为公开预览，实际机器人控制仍需接入底层工具与硬件。 [查看Google Cloud 官方博客原文](https://cloud.google.com/blog/products/ai-machine-learning/gemini-robotics-embodied-reasoning-2-is-now-available-on-google-cloud)

- **OpenAI 发布 GPT-6.1 Terra，侧重视觉理解与电脑操作**（事件日期：2026-10-26）
  GPT-6.1 Terra 面向视觉推理、电脑操作与写作。API 支持文本和图像输入、文本输出，工具调用须使用 Responses API；Work、Codex 的可用性取决于订阅和管理设置，Chat 侧不提供。 [查看OpenAI 官方 API 更新记录原文](https://developers.openai.com/api/docs/changelog)

## 2026-10-27

整理日期：**2026-10-27** · 关注 AI 产品、模型与工具动态。

- **OpenAI 新增 Signals 工作活动数据，呈现 ChatGPT 的工作用途**（事件日期：2026-10-26）
  新增数据覆盖近 100 个国家、165 类工作活动，按季度呈现 2025 年一季度至 2026 年三季度的 ChatGPT 工作用途。统计经聚合和隐私保护处理，仅包含个人计划中的工作相关消息，不含企业消息或 Codex，不能直接推断就业替代或生产率因果关系。 [查看OpenAI 官方文章原文](https://openai.com/index/chatgpt-expanding-world-of-work/)

- **Hugging Face 汇总开发工具更新，强化共享缓存与任务自动化**（事件日期：2026-10-26）
  HF 介绍近期 CLI 与 huggingface_hub 更新，支持跨仓复用相同 Xet 文件、任务失败重试及 webhook 触发 Jobs，并提供实验性 CPU/GPU 云沙箱，方便智能体隔离运行代码。这是近期功能的集中介绍，云沙箱仍处于实验阶段。 [查看Hugging Face 官方博客原文](https://huggingface.co/blog/huggingface/whats-new-in-the-hf-cli-and-huggingface-hub-librar)

- **Google 正式推出 LookML 语义索引，为智能体提供统一业务指标**（事件日期：2026-10-26）
  Looker Core 的 LookML 业务逻辑现可自动同步至 Knowledge Catalog，让 Gemini Enterprise 和自建智能体查询指标定义、表连接规则及数据血缘。功能适用于 Google Cloud 上的 Looker Core，需启用相关索引和 API，数据访问仍受最终用户 IAM 权限约束。 [查看Google Cloud 官方博客原文](https://cloud.google.com/blog/products/business-intelligence/lookml-metadata-indexing-in-knowledge-catalog-is-now-ga/)

## 2026-10-25

整理日期：**2026-10-25** · 关注 AI 产品、模型与工具动态。

- **Hugging Face 提供 Trainium 模型兼容性查询工具**（事件日期：2026-10-23）
  查询 Space 可查看模型在 AWS Trainium2 上的运行结果、软件版本、核心数和峰值设备内存，并获取复现脚本与公开测试数据。目前仅覆盖文本与图文生成，最多 16 核；测试只生成 32 个 token，通过不代表吞吐表现或长文本质量。 [查看Hugging Face 官方博客原文](https://huggingface.co/blog/torch-neuronx-model-support)

- **GitHub Copilot 用量统计新增第三方客户端维度**（事件日期：2026-10-23）
  Usage Metrics API 新增 totals_by_client，可按 OpenCode、Claude Code、Codex 等客户端查看经 Copilot 发出的成功模型请求、会话和 token 用量。使用前需启用指标政策并具备相应权限；模型请求数不等于提示词次数，客户端名称为尽力识别的分组。 [查看GitHub 官方更新记录原文](https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode/)

## 2026-10-24

整理日期：**2026-10-24** · 关注 AI 产品、模型与工具动态。

- **Claude Code 扩展监控工具支持与企业会话权限**（事件日期：2026-10-23）
  Claude Code 2.1.310 将 Monitor 工具和插件监控扩展至 Bedrock、Vertex、Foundry，也支持关闭遥测的环境。Enterprise 自定义角色新增云会话与 Remote Control 权限，可分别控制访问。 [查看Anthropic 官方发布说明原文](https://github.com/anthropics/claude-code/releases/tag/v2.1.310)

- **GitHub 将 Teams 通知与 Copilot 整合，支持从问题通知发起修复**（事件日期：2026-10-23）
  新版 GitHub Teams 应用整合通知与 Copilot；用户可在频道或聊天的问题通知中，通过 @GitHub 发起调查、修复并创建 PR，再由团队审查和合并。现有通知应用需更新，旧版 GitHub 应用将于 11 月 16 日退役。 [查看GitHub 官方更新记录原文](https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams/)

- **Anthropic 将 Agent Skills 标准捐赠给 AAIF**（事件日期：2026-10-22）
  Anthropic 将 Agent Skills 名称、标志、GitHub 组织及域名捐赠给 Linux Foundation 旗下 AAIF，推动中立治理。开发者无需加入基金会即可继续使用和贡献；版本化发布、正式提案流程与安全指南仍属拟议路线图。 [查看Anthropic 官方公告原文](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)

## 2026-10-23

整理日期：**2026-10-23** · 关注 AI 产品、模型与工具动态。

- **Google CX Agent Studio 新增智能体开发助手 Arc**（事件日期：2026-10-22）
  Arc 是平台内置编程智能体，可协助设计多智能体架构、编写工具和回调、配置防护规则，并参与评测与诊断。用户可上传需求文档、样例数据或现有配置，为开发提供上下文。 [查看Google Cloud 官方文档原文](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc)

- **GitHub Copilot 使用统计新增自定义技能、智能体与 MCP 名称**（事件日期：2026-10-22）
  使用统计 API 开始显示组织自定义技能、智能体及 MCP 服务等配置名称，单组条目上限从 5 项增至 25 项。数据覆盖受支持版本的 CLI、Copilot 应用与 SDK；旧报告不补写，IDE 内置聊天遥测不报告这些名称。 [查看GitHub 官方更新记录原文](https://github.blog/changelog/2026-10-22-custom-skills-agents-and-mcp-servers-in-usage-metrics-api/)

- **Ai2 发布 OlmoEarth v1.3，开放全球卫星嵌入与探索器**（事件日期：2026-10-22）
  新模型提供 10 米分辨率的年度卫星嵌入及免登录地图探索器，可比较地表变化、寻找相似地区，并以少量标注生成地图。全球数据首发覆盖 2023—2025 年；权重、预训练数据与代码开放，采用 OlmoEarth Artifact License。 [查看Ai2 官方文章原文](https://huggingface.co/blog/allenai/olmoearth-v1-3)

## 2026-10-22

整理日期：**2026-10-22** · 关注 AI 产品、模型与工具动态。

- **IBM 发布 Granite Speech 5.0，强化多语转录与翻译**（事件日期：2026-10-21）
  新 20 亿参数模型支持英、法、德、西、葡、日六语转录，新增语言提示、最多 2000 个关键词引导，并改进长音频翻译。同步更新 Turbo CTC 与多人说话归属模型，三个模型均采用 Apache 2.0 许可，可从 Hugging Face 获取。 [查看IBM Granite 官方文章原文](https://huggingface.co/blog/ibm-granite/granite-speech-5)

- **NVIDIA 开放 Nemotron 3.5 多模态检索与文档解析模型**（事件日期：2026-10-21）
  新增 Embed 嵌入、Rerank 重排及 6.31 亿参数 Parse 模型，覆盖文本与图像检索、相关性排序和结构化文档提取。Parse 可保留阅读顺序及表格、图表结构；权重、数据与训练配方已开放，可通过 NIM 或合作推理平台部署。 [查看NVIDIA 官方文章原文](https://huggingface.co/blog/nvidia/nemotron-retriever-world-class-agentic-retrieval)

- **OpenAI 发布 PHP 版本检查工具与 Codex 技能**（事件日期：2026-10-21）
  OpenAI 随 AI 辅助发现的 PHP 漏洞披露，提供版本检查工具与 Codex 技能，可读取网站响应头或本地 PHP 版本。结果属于版本比较，隐藏版本时会返回未知；补丁是否适用需结合维护者与服务商指引。 [查看OpenAI 官方公告原文](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)

## 2026-10-21

整理日期：**2026-10-21** · 关注 AI 产品、模型与工具动态。

- **Mistral 发布 Voxtral 3 语音模型与实时智能体 SDK**（事件日期：2026-10-20）
  新一代转录和语音合成模型配合基于 LiveKit 的 SDK，串联聆听、推理、工具调用与播报。批量转录支持 50 多种语言，合成支持 35 多种语言，可通过 API 和 Studio 使用；完整私有部署需联系团队。 [查看Mistral 官方公告原文](https://mistral.ai/news/voxtral-3/)

- **Gemini 为小企业新增经营入口与品牌素材工具**（事件日期：2026-10-20）
  Google 宣布新增小企业专属入口，整合品牌素材、财务分析和客户洞察，并连接 Shopify、Canva、Xero 等应用。用户可上传并保留品牌风格，持续生成一致的营销素材；新入口、技能与应用连接将在未来几天向全球用户逐步开放。 [查看Google 官方博客原文](https://blog.google/innovation-and-ai/products/gemini-app/new-tools-small-business-owners/)

- **ChatGPT 逐步推出锁定聊天，支持 PIN 与设备验证**（事件日期：2026-10-20）
  用户可将所选对话从常规历史、置顶和搜索中隐藏，使用 4 位账户 PIN 或受支持的设备认证打开。功能逐步覆盖免费及付费方案；Codex 与本地 Work 对话不支持，锁定也不会改变数据保留或模型改进设置。 [查看OpenAI 官方帮助文档原文](https://help.openai.com/en/articles/20001411-using-locked-chats-in-chatgpt)

- **IBM 用学习记忆提升客服智能体，无需更新模型权重**（事件日期：2026-10-20）
  IBM Research 公布 ALTK-Evolve 客服评测结果，从训练轨迹提炼行为指南并加入提示词。在 τ²-bench 零售测试集上，GPT-4.1 智能体四次独立尝试均成功的任务比例从 57.5% 升至 67.5%，代价是更多输入 token。 [查看IBM Research 官方文章原文](https://huggingface.co/blog/ibm-research/altk-evolve-bc)

## 2026-10-20

整理日期：**2026-10-20** · 关注 AI 产品、模型与工具动态。

- **Gemini Notebook 新增幻灯片与视频生成前的审阅流程**（事件日期：2026-10-19）
  用户可先确认主题，再调整结构与视觉风格，并通过新的 Review 开关审阅幻灯片大纲或视频制作说明，确认后再生成。功能将在未来一周面向全球所有 Gemini Notebook 用户逐步推出。 [查看Google 官方博客原文](https://blog.google/innovation-and-ai/products/gemini-notebook/co-create-slides-videos/)

- **Claude Code 新增自动模式配置向导与智能体安全核查**（事件日期：2026-10-19）
  2.1.304 新增自动模式配置向导，根据项目与近期会话了解环境，并覆盖 Bedrock、Vertex、Foundry 等接入方式。另提供 Managed Agents 安全设置只读核查，对照官方指南检查配置，不自动修改设置。 [查看Anthropic 官方发布记录原文](https://github.com/anthropics/claude-code/releases/tag/v2.1.304)

- **OpenAI 开源跨语言编程评测 MultiLangBench**（事件日期：2026-10-19）
  MultiLangBench 测试模型用 20 种语言构建 SQLite 兼容引擎的能力，官方同时公布 COBOL 代码迁移评测。官方测试中，在最高推理强度下，GPT-6 Astra 的多语言平均通过率为 87.4%；迁移评测则要求可观察输出逐字节一致。 [查看OpenAI 官方研究文章原文](https://openai.com/index/low-resource-programming-languages/)

- **Hugging Face 宣布原生支持 TorchNeuron，简化 Trainium 模型运行**（事件日期：2026-10-19）
  Transformers、Diffusers 等库可直接使用 AWS Trainium，新后端支持即时执行、torch.compile 和 PyTorch 分布式接口。10 月 19 日公告称，TorchNeuron 公开测试将于 10 月 20 日开始。 [查看Hugging Face 官方博客原文](https://huggingface.co/blog/hf-torchneuron)

## 2026-10-19

整理日期：**2026-10-19** · 关注 AI 产品、模型与工具动态。

- **DeepSeek 更新 Flash 模型，开放搜索与网页提取 API**（事件日期：2026-10-17）
  Flash 已升级至 V4.1-Flash-1017，官网、App 和 API 同步更新，仍通过 deepseek-flash 调用，模型价格不变。同日开放 Search、Fetch 独立接口，分别用于网页搜索和 Markdown 内容提取。 [查看DeepSeek 官方更新记录原文](https://api-docs.deepseek.com/updates/)

- **Claude Code 2.1.302 扩展分叉子智能体，增加压缩开关**（事件日期：2026-10-16）
  分叉子智能体默认扩展至非交互命令、Agent SDK、桌面应用和 VS Code，并可在配置中关闭或重新启用空闲上下文压缩。同时修复部分 MCP 服务协商后无工具或调用失败的问题。 [查看Anthropic 官方发布记录原文](https://github.com/anthropics/claude-code/releases/tag/v2.1.302)

## 2026-10-17

整理日期：**2026-10-17** · 关注 AI 产品、模型与工具动态。

- **Beam 开放权重，Ollama Cloud 提供限时免费体验**（事件日期：2026-10-16）
  Reflection 的 Beam 采用约 5010 亿总参数、230 亿激活参数，支持百万 token 上下文，面向编程、推理和长流程智能体。权重采用 Apache 2.0 许可；Ollama Cloud 已接入并限时免费，可从终端或应用调用，无需下载模型。 [查看Ollama 官方公告原文](https://ollama.com/blog/reflection-beam)

- **Black Forest Labs 开放 FLUX 3 Image Klein 图像模型**（事件日期：2026-10-15）
  56 亿参数的图像生成器支持文生图、最多 10 张参考图的生成与编辑，以及边界框布局控制。发布包含基础版、蒸馏版和量化权重，已支持 ComfyUI、Diffusers 及 LoRA 训练；权重采用 FLUX Kommunity License，商用须满足许可条件。 [查看Black Forest Labs 官方公告原文](https://bfl.ai/blog/flux-3-image-klein)

- **Amp 支持查看并操控 macOS 与 Linux Runner 桌面**（事件日期：2026-10-16）
  开发者现在可以查看并操作 Runner 的桌面，便于检查智能体构建的原生应用。macOS 可在 Runner 设置中开启显示共享，也可通过 --desktop 参数启动 Runner；Amp 客户端直接连接 Runner，本地或邻近网络可降低交互延迟。 [查看Amp 官方更新原文](https://ampcode.com/news/runner-desktop)

- **GitHub 在 Slack 和 Teams 支持同一对话跨仓库工作**（事件日期：2026-10-15）
  用户可在 Slack 或 Teams 的同一对话中，让 @GitHub 跨多个仓库创建问题、修改代码、提交 PR 或调查故障。更新还改善了 Slack 消息与线程上下文使用、仓库切换，以及任务中断后的恢复。 [查看GitHub 官方更新日志原文](https://github.blog/changelog/2026-10-15-copilot-in-slack-and-teams-adds-model-and-repository-updates/)

- **Anthropic 展示 Claude 优化量子电路的研究成果**（事件日期：2026-10-16）
  研究团队让 Claude Mythos 5 根据文字要求设计电路，通过程序校验正确性并反馈资源评分。官方报告称，模型在八类基础任务中找到了更高效的设计；流程仍包含初始指导和少量人工提示，本次发布属于研究成果。 [查看Anthropic 官方研究文章原文](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

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
