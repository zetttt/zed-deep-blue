# Trae Deep Blue

**简体中文** | [English](README.en.md)

基于 Trae Deep Blue 配色适配的 Zed 深色主题，包含代码高亮、编辑器、文件树、菜单、终端和 Git 状态配色。当前版本 **0.1.0**，扩展 ID 为 `zed-deep-blue`。

![Trae Deep Blue：in-echo 项目的 AI Markdown、TypeScript 代码、文件树与终端](docs/screenshots/in-echo.png)

## 安装

1. 在 Zed 命令面板运行 **zed: install dev extension**，选择本仓库根目录。
2. 运行 **theme selector: toggle**，选择 **Trae Deep Blue**。

也可直接安装主题文件（macOS/Linux）：

```sh
mkdir -p ~/.config/zed/themes
cp themes/trae-deep-blue.json ~/.config/zed/themes/
```

重新加载后选择主题。卸载时切回其他主题，再移除开发扩展或复制的主题文件。

## 推荐配置

主题负责配色；字体、字号和间距需要单独配置。下面是当前使用的主要外观设置，完整示例见 [settings/settings.example.json](settings/settings.example.json)。

将这些字段合并到 Zed 用户设置顶层，**不要覆盖整个 settings.json**；已有的 terminal、project_panel 按字段合并，保留其中其他配置。

```json
{
  "theme": "Trae Deep Blue",
  "ui_font_family": "SF Pro Text",
  "ui_font_size": 16,
  "buffer_font_family": "JetBrains Mono",
  "buffer_font_size": 13,
  "buffer_line_height": { "custom": 1.75 },
  "agent_ui_font_size": 16,
  "agent_buffer_font_size": 14,
  "markdown_preview": {
    "font_size": 14
  },
  "terminal": {
    "font_family": "JetBrains Mono",
    "font_size": 12,
    "line_height": "standard"
  },
  "project_panel": {
    "entry_spacing": "standard",
    "indent_size": 20,
    "sticky_scroll": false
  }
}
```

配套字体面向 macOS，需要本机已安装 **SF Pro Text** 和 **JetBrains Mono**；其他系统请换成可用字体。Markdown 预览正文与代码块的行距由不同渲染规则控制，代码行高 1.75 不代表预览正文也是 1.75。

也可以在仓库目录执行一次（Python 3.11+，无需额外依赖）：

```sh
python3 scripts/apply-appearance.py
```

脚本从同一示例文件合并配置，保留注释与非外观设置，更新前创建私有备份。加 `--check` 只检查差异；加 `--settings PATH` 可指定设置文件。

误缩放时，点击代码区或 Markdown 预览正文后按 **⌘0**，恢复该区域配置的字号。

## 高亮预览

上面的 JSON 配置可用于观察键名、字符串、数字和布尔值染色。下面是 TypeScript 示例：

```typescript
interface PreviewOptions {
  name: string;
  enabled: boolean;
}

// 中英文注释：观察类型、函数、关键字和字符串。
function describePreview(options: PreviewOptions): string {
  const count = 3;
  return options.enabled ? options.name + "：" + count + " 个样例" : "预览已关闭";
}
```

普通文本、**加粗文本**和行内代码 `font_size: 14` 可直接比较。行内代码通常保持单色；多行代码块需要标注语言，并安装对应的语言支持。更多样例见 [preview/](preview/)。

## 说明与许可

主题不能改变组件布局、圆角、图标、独立控件字号或表格内边距。Zed 与 Trae 的语法解析和文字渲染不同，不承诺逐像素还原。

- [配色来源与适配](docs/mapping.md)
- [字体与间距说明](docs/appearance.md)
- [验证记录](docs/validation.md)
- [Zed 主题文档](https://zed.dev/docs/themes)

采用 [MIT License](LICENSE)，保留上游版权声明。非 Trae 官方扩展，来源见 [第三方声明](THIRD_PARTY_NOTICES.md)。
