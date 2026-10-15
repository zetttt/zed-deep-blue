# 字体与间距

主题只提供配色。字体、字号和间距见 [settings/settings.example.json](../settings/settings.example.json)，可手动合并，或运行：

```sh
python3 scripts/apply-appearance.py
```

脚本需要 Python 3.11+，保留注释与其他设置，修改前自动备份。`--check` 仅检查差异；`--settings PATH` 指定目标文件。

## 推荐值

| 区域 | 配置 |
| --- | --- |
| 界面 | SF Pro Text，16 px |
| 编辑器 | JetBrains Mono，13 px，行高 1.75（22.75 px） |
| Agent 正文 / 用户消息 | 16 / 14 px |
| Markdown 独立预览 | 14 px |
| 终端 | JetBrains Mono，12 px，standard 行距 |
| 文件树 | standard 间距，20 px 缩进，关闭 sticky scroll |

字体示例面向 macOS，需安装对应字体；其他系统请替换为可用字体。中文回退交由系统处理。

Markdown 预览正文与代码块采用不同的行距规则；编辑器行高 1.75 不会覆盖预览正文行距。

## 对齐依据与限制

2026-10-15 在 Trae 3.6.2 DevTools 中读取同一份代码样例的字体与尺寸：代码为 JetBrains Mono 13 px / 22 px，常规界面文字为 SF Pro Text 13 px / 18.2 px。完整测量见 [trae-ui-metrics.json](trae-ui-metrics.json)。

Zed 的 UI 字号还会影响组件尺寸，推荐值优先保证可读性。标签栏、标题栏、状态栏的高度和独立字号，以及图标大小、圆角、阴影和表格内边距，不能通过主题单独设置。不同编辑器的文字渲染也存在差异。

## 恢复临时缩放

1. 聚焦代码编辑区，按 **⌘0**，恢复配置的代码字号。
2. 聚焦 Markdown 预览，按 **⌘0**，恢复预览字号。
3. 整体界面缩放后，在命令面板运行 **zed: reset ui font size**。

参考：[Zed 设置](https://zed.dev/docs/reference/all-settings)、[配色适配](mapping.md)。
