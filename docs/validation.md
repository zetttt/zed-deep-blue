# v0.1.0 验证说明

验证环境：macOS，ZedG v1.23.3。日期：2026-10-15。

## 静态检查

使用 Python 3.11+ 与 `jsonschema`，下载 [官方 Theme Schema v0.2.0](https://zed.dev/schema/themes/v0.2.0.json)，将路径传给验证脚本：

```sh
python3 scripts/validate.py /path/to/zed-schema.json
python3 scripts/apply-appearance.py --check
git diff --check
```

已通过：

- 官方 Draft-07 Schema、142 个 style 字段、44 个语法 capture、颜色格式与扩展清单。
- 中英文 README 的 JSON 与设置示例一致，本地链接有效。
- 配置合并保留 JSONC 注释、嵌套字段和非外观设置；备份权限、重复执行、新文件与无效输入保护已检查。

`--check` 比较本机设置与推荐配置，有差异时返回非零状态。

## 实际显示

开发扩展已安装，主题选择和重新构建后生效。已观察以下场景：

| 场景 | 检查内容 |
| --- | --- |
| TypeScript / JavaScript / JSON | 关键字、类型、字符串、数字、属性与函数 |
| Vue / HTML / CSS | 标签、属性、选择器及嵌入语言 |
| Markdown / Agent | 标题、列表、引用、代码块、表格与消息背景 |
| 编辑器与面板 | 文件树状态、标签栏、菜单、选中项、边框与滚动条 |
| 终端 | 普通与 bright ANSI 色卡及中文显示 |

[README 截图](../README.md) 展示 in-echo 项目的实际外观；不代表该项目的构建或类型检查结果。`preview/` 是语法展示样例，无需安装业务依赖。

## 未覆盖范围

未逐项验证 Git gutter 增删改、协作光标、所有交互状态、系统亮暗切换、应用重启及 Windows/Linux。Schema 通过不代表这些场景已经完成视觉验证。

主题无法控制的布局和字体差异见 [appearance.md](appearance.md)，语法映射限制见 [mapping.md](mapping.md)。
