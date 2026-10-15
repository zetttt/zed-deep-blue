# Trae → Zed 配色映射

配色来源：Trae 的 theme-icube v1.0.0，Deep Blue 主题。核验日期：2026-10-15。

按 dark_color.json → dark_vs.json → dark_plus.json → dark_blue.json 顺序合并 colors 与 semanticTokenColors；tokenColors 保留继承顺序，后层规则覆盖同一 scope。共 259 个源 UI 颜色、68 条 TextMate 规则、4 个语义 token。主题 JSON 是运行时唯一事实来源；本表记录来源，不参与加载。

## 源文件 SHA-256

| 文件 | SHA-256 |
| --- | --- |
| dark_color.json | 9a4c918f6db2f7be1800bab584caa2b646bae0862da9bac4824d4d25bc937189 |
| dark_vs.json | ce2467e3351e8bdaefb94ebade95a18e00027027b3893900a3f16078b2d5ee15 |
| dark_plus.json | 448ca233be827953d4e5898823bae6bce967e329b0677acd7faa93a803888ecd |
| dark_blue.json | 8efd4a403e8a0491c10595d239cd009b825ebf30fc087fb183ab609267104181 |

## 适配与限制

### 源码复核与语法视觉补偿

语法色在源色基础上小幅提亮，蓝色调整幅度稍大。下表区分源色与适配色；UI 和终端采用独立映射。

| Trae 原色 | Zed 语法适配色 | 类别 |
| --- | --- | --- |
| #80BBFF | #8CC4FF | 布尔、常量、转义等蓝色，提亮幅度稍大 |
| #81CFE0 | #86D1E1 | 类型青色 |
| #B38CFF | #B691FF | 关键字紫色 |
| #82D99F | #87DBA3 | 字符串绿色 |
| #F29D79 | #F3A17E | 函数橙色 |
| #DED47E | #DFD683 | 变量黄色 |
| #F48CCA | #F491CC | 数字粉色 |
| #F2858C | #F38A91 | 标签与特殊标点 |

其余七类约向白色混合 4%。语义分类遵循 Zed 的 Tree-sitter/LSP，因此相同代码在两个编辑器中可能使用不同的语法颜色。

- 源 button.separator 和 icube--special-bgtabsoverlay 均为非法 #ODOEOF2E（字母 O）。不猜测原意、不复制该值；Zed 分隔线采用合法源 icube.colorLine1，标签叠层采用 tab.activeBackground 与标签栏背景合成。
- Zed 共享 element.*、ghost_element.*、text.*、icon.* 状态；无法逐控件还原 Trae 的黑字浅色主按钮、独立菜单/quick-input 背景、活动标签白色上边框。按钮用暗色背景和浅色文字保持共享状态可读；选中/禁用状态遵循源透明叠层。
- 状态栏源为透明，Zed 使用编辑器背景合成后的 #181D27。菜单/浮层统一使用源 menu.background；标题栏和常规表面使用 #232A35。
- 原链没有终端 ANSI、Git gutter、编辑器空白符/折行导线专用值，按源语法/状态调色板补齐；ANSI dim 采用 2/3 色值与背景合成，不声称是 Trae 的默认终端值。
- Zed Tree-sitter capture 与 TextMate scope 不同，不能给同一个 tag capture 同时指定 HTML 粉色与 CSS 黄色。CSS selector、Vue 的嵌入范围、JSON key 与对象属性、TS 类型转换及内建对象会随语法查询/LSP 分类存在差异。语义 stringLiteral/numberLiteral 已应用；newOperator/customLiteral 无一对一 capture。
- editorUnnecessaryCode.opacity 无可直接迁移的透明度字段，使用 muted unreachable；Markdown underline/strikethrough 不属于当前 HighlightStyle 的字段，由渲染器决定。
- 布局、面板位置、圆角、控件尺寸、字体、图标、阴影和语言插件不能由此主题配置；字体与可配置行距/目录缩进另见 appearance.md 和 settings/settings.example.json。未修改 Zed 源码。

### 文件树与消息区块

普通文件名为 #D1D3DB，忽略项为 #737780，修改项为暖黄 #D9B775，新增项为绿 #188A64。新增色参考界面截图取样；这些是适配值。text.muted 与状态色也会影响其他共用字段的组件。

Agent 外围使用 panel.background = #141923；用户消息和代码块共用 editor.background = #181D27，略亮于外围。边框不透明度约为 12% / 18% / 24%。这些字段也用于侧栏和编辑器，不能单独控制聊天区块。主题保持 opaque，阴影由程序控制。

### Markdown 表格

Agent 表格默认单元格内边距为左右 4 px、上下 2 px；独立 Markdown 预览为左右 10 px、上下 4 px。这属于不同的程序渲染样式，主题不能调整 Agent 表格内边距。需要宽松排版时，可在独立 Markdown 预览中阅读。

## 逐项映射

| Zed 字段 | Trae 源 token / 适配 | 色值 | 备注 |
| --- | --- | --- | --- |
| background | editor.background | #181D27 | 整体背景 |
| surface.background | titleBar.activeBackground | #232A35 |  |
| elevated_surface.background | menu.background | #2E3743 |  |
| border | icube.colorLine1，适度增强不透明度 | #B0C0F41F | 用户消息等共享边框 |
| border.variant | icube.colorLine2，适度增强不透明度 | #B0C0F42E | Markdown 代码块等共享边框 |
| border.focused | icube.colorLine3，适度增强不透明度 | #B0C0F43D | 保持焦点层级 |
| border.selected | icube.colorStatusRegular | #387BFF |  |
| border.disabled | icube.colorLine1 | #B0C0F414 |  |
| border.transparent | icube.colorTransparent | #ffffff00 |  |
| element.background | input.background | #B0C0F40A |  |
| element.hover | toolbar.hoverBackground | #B0C0F40F |  |
| element.active | toolbar.activeBackground | #B0C0F417 |  |
| element.selected | list.activeSelectionBackground | #B0C0F417 |  |
| element.disabled | icube.colorBgTr0 | #B0C0F40A |  |
| ghost_element.background | icube.colorTransparent | #ffffff00 |  |
| ghost_element.hover | toolbar.hoverBackground | #B0C0F40F |  |
| ghost_element.active | toolbar.activeBackground | #B0C0F417 |  |
| ghost_element.selected | list.activeSelectionBackground | #B0C0F417 |  |
| ghost_element.disabled | icube.colorTransparent | #ffffff00 |  |
| drop_target.background | list.dropBackground | #B0C0F40F |  |
| text | foreground | #D1D3DB |  |
| text.muted | descriptionForeground，提亮适配 | #D1D3DB | 普通文件名及共享次要文字 |
| text.placeholder | input.placeholderForeground | #9599A6 |  |
| text.disabled | disabledForeground | #666B75 |  |
| text.accent | icube.colorBrand | #DADDE5 |  |
| icon | icon.foreground | #9599A6 |  |
| icon.muted | descriptionForeground | #9599A6 |  |
| icon.placeholder | input.placeholderForeground | #9599A6 |  |
| icon.disabled | disabledForeground | #666B75 |  |
| icon.accent | icube.colorBrand | #DADDE5 |  |
| status_bar.background | editor.background | #181D27 |  |
| title_bar.background | titleBar.activeBackground | #232A35 |  |
| title_bar.inactive_background | titleBar.inactiveBackground | #232A35 |  |
| toolbar.background | editor.background | #181D27 |  |
| tab_bar.background | editorGroupHeader.tabsBackground | #17191A |  |
| tab.inactive_background | tab.inactiveBackground | #17191A |  |
| panel.background | sideBar.background，压暗适配 | #141923 | Agent 外围及侧栏等共享面板 |
| panel.focused_border | icube.colorLine3 | #B0C0F42E |  |
| panel.indent_guide | tree.indentGuidesStroke | #B0C0F414 |  |
| panel.indent_guide_active | icube.colorLine3 | #B0C0F42E |  |
| panel.indent_guide_hover | icube.colorLine2 | #B0C0F41F |  |
| pane.focused_border | icube.colorLine3 | #B0C0F42E |  |
| pane_group.border | tab.border | #B0C0F414 |  |
| search.match_background | editor.findMatchHighlightBackground | #DADDE552 |  |
| editor.foreground | editor.foreground | #D1D3DB |  |
| editor.background | editor.background | #181D27 |  |
| editor.gutter.background | editor.background | #181D27 |  |
| editor.subheader.background | sideBarSectionHeader.background | #181D27 |  |
| editor.active_line.background | editor.lineHighlightBackground | #282B3A |  |
| editor.highlighted_line.background | editor.hoverHighlightBackground | #264f7840 |  |
| editor.line_number | editorLineNumber.foreground | #979AA4 |  |
| editor.active_line_number | editorLineNumber.activeForeground | #E0E3EE |  |
| editor.invisible | icube.colorLine3 | #B0C0F42E |  |
| editor.wrap_guide | icube.colorLine1 | #B0C0F414 |  |
| editor.active_wrap_guide | icube.colorLine3 | #B0C0F42E |  |
| editor.indent_guide | editorIndentGuide.background1 | #B0C0F414 |  |
| editor.indent_guide_active | editorIndentGuide.activeBackground1 | #B0C0F42E |  |
| editor.document_highlight.read_background | editor.selectionHighlightBackground | #ADD6FF26 |  |
| editor.document_highlight.write_background | editor.selectionBackground | #3579FF47 |  |
| editor.document_highlight.bracket_background | editorBracketMatch.background | #D5D8E03D |  |
| link_text.hover | editorLink.activeForeground | #4E94CE |  |
| scrollbar.thumb.background | icube.scrollbarBgColor | #DDE2E940 |  |
| scrollbar.thumb.hover_background | icube.scrollbarHoverBgColor | #DDE2E959 |  |
| scrollbar.thumb.border | icube.colorTransparent | #ffffff00 |  |
| scrollbar.track.background | icube.colorTransparent | #ffffff00 |  |
| scrollbar.track.border | icube.colorTransparent | #ffffff00 |  |
| terminal.background | editor.background | #181D27 |  |
| terminal.foreground | editor.foreground | #D1D3DB |  |
| terminal.bright_foreground | icube.colorHighlightText | #F5F9FE |  |
| terminal.dim_foreground | icube.colorGrayText2 | #737780 |  |
| terminal.ansi.background | editor.background | #181D27 |  |
| tab.active_background | adapted | #202327 | 源半透明背景与标签栏背景合成，避免底层主题透出。 |
| background.appearance | adapted | opaque |  |
| error | icube.colorError | #F65A5A |  |
| error.background | icube.colorErrorTransparent | #D02A232E |  |
| error.border | icube.colorError | #F65A5A |  |
| warning | icube.colorWarning | #DC8730 |  |
| warning.background | icube.colorWarningTransparent | #DC873029 |  |
| warning.border | icube.colorWarning | #DC8730 |  |
| success | icube.colorSuccess | #33C192 |  |
| success.background | icube.colorSuccessTransparent | #00A56E2E |  |
| success.border | icube.colorSuccess | #33C192 |  |
| info | icube.colorStatusRegular | #387BFF |  |
| info.background | icube.colorStatusRegularTransparent | #3579FF2E |  |
| info.border | icube.colorStatusRegular | #387BFF |  |
| hint | icube.colorGrayText | #9599A6 |  |
| hint.background | icube.colorBgTr0 | #B0C0F40A |  |
| hint.border | icube.colorGrayText | #9599A6 |  |
| created | 适配：Git 新增状态 | #188A64 | 深饱和绿色 |
| created.background | 适配：新增色透明叠层 | #188A6424 |  |
| created.border | 适配：深绿色 | #188A64 |  |
| deleted | icube.colorError | #F65A5A |  |
| deleted.background | diffEditor.removedLineBackground | #D02A2347 |  |
| deleted.border | icube.colorError | #F65A5A |  |
| modified | 适配：Git 修改状态 | #D9B775 | 暖黄色 |
| modified.background | 适配：修改色透明叠层 | #D9B77524 |  |
| modified.border | 适配：暖黄色 | #D9B775 |  |
| renamed | icube.colorC5 | #04CBE5 |  |
| renamed.background | icube.colorBgTr0 | #B0C0F40A |  |
| renamed.border | icube.colorC5 | #04CBE5 |  |
| conflict | icube.colorWarning | #DC8730 |  |
| conflict.background | icube.colorWarningTransparent | #DC873029 |  |
| conflict.border | icube.colorWarning | #DC8730 |  |
| ignored | icube.colorGrayText2 | #737780 |  |
| ignored.background | icube.colorBgTr0 | #B0C0F40A |  |
| ignored.border | icube.colorGrayText2 | #737780 |  |
| hidden | icube.colorDisableText | #666B75 |  |
| hidden.background | icube.colorTransparent | #ffffff00 |  |
| hidden.border | icube.colorDisableText | #666B75 |  |
| unreachable | icube.colorDisableText | #666B75 |  |
| unreachable.background | icube.colorTransparent | #ffffff00 |  |
| unreachable.border | icube.colorDisableText | #666B75 |  |
| predictive | icube.colorGrayText2 | #737780 |  |
| predictive.background | icube.colorTransparent | #ffffff00 |  |
| predictive.border | icube.colorGrayText2 | #737780 |  |
| terminal.ansi.black | adapted | #181D27 | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_black | adapted | #737780 | 源调色板适配。 |
| terminal.ansi.dim_black | adapted | #181D27 | 2/3 色值与终端背景合成。 |
| terminal.ansi.red | adapted | #F2858C | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_red | adapted | #FF9392 | 源调色板适配。 |
| terminal.ansi.dim_red | adapted | #A9626A | 2/3 色值与终端背景合成。 |
| terminal.ansi.green | adapted | #82D99F | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_green | adapted | #5ED4AD | 源调色板适配。 |
| terminal.ansi.dim_green | adapted | #5F9A77 | 2/3 色值与终端背景合成。 |
| terminal.ansi.yellow | adapted | #DED47E | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_yellow | adapted | #DCB364 | 源调色板适配。 |
| terminal.ansi.dim_yellow | adapted | #9C9761 | 2/3 色值与终端背景合成。 |
| terminal.ansi.blue | adapted | #80BBFF | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_blue | adapted | #7BB8FF | 源调色板适配。 |
| terminal.ansi.dim_blue | adapted | #5D86B7 | 2/3 色值与终端背景合成。 |
| terminal.ansi.magenta | adapted | #B38CFF | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_magenta | adapted | #EC93FF | 源调色板适配。 |
| terminal.ansi.dim_magenta | adapted | #7F67B7 | 2/3 色值与终端背景合成。 |
| terminal.ansi.cyan | adapted | #81CFE0 | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_cyan | adapted | #04CBE5 | 源调色板适配。 |
| terminal.ansi.dim_cyan | adapted | #5E94A2 | 2/3 色值与终端背景合成。 |
| terminal.ansi.white | adapted | #D1D3DB | 源未显式指定 ANSI，按源调色板适配。 |
| terminal.ansi.bright_white | adapted | #F5F9FE | 源调色板适配。 |
| terminal.ansi.dim_white | adapted | #93969F | 2/3 色值与终端背景合成。 |
| syntax.comment | TextMate: comment | #737780 |  |
| syntax.comment.doc | TextMate: comment | #737780 |  |
| syntax.keyword | TextMate: keyword，视觉补偿 | #B691FF | 原色见补偿表 |
| syntax.boolean | TextMate: constant.language，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.constant | TextMate: variable.other.constant，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.constant.builtin | TextMate: constant.language，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.enum | TextMate: variable.other.enummember，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.variant | TextMate: variable.other.enummember，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.function | TextMate: entity.name.function，视觉补偿 | #F3A17E | 原色见补偿表 |
| syntax.constructor | TextMate: entity.name.type，视觉补偿 | #86D1E1 | 原色见补偿表 |
| syntax.type | TextMate: entity.name.type，视觉补偿 | #86D1E1 | 原色见补偿表 |
| syntax.type.builtin | TextMate: support.type，视觉补偿 | #86D1E1 | 原色见补偿表 |
| syntax.variable | TextMate: variable，视觉补偿 | #DFD683 | 原色见补偿表 |
| syntax.variable.parameter | TextMate: variable，视觉补偿 | #DFD683 | 原色见补偿表 |
| syntax.variable.special | TextMate: variable.language，视觉补偿 | #DFD683 | 原色见补偿表 |
| syntax.property | TextMate: variable.other.property | #E0E3EE |  |
| syntax.property.json_key | TextMate: meta.object-literal.key | #E0E3EE |  |
| syntax.attribute | TextMate: entity.other.attribute-name，视觉补偿 | #DFD683 | 原色见补偿表 |
| syntax.tag | TextMate: entity.name.tag，视觉补偿 | #F38A91 | 原色见补偿表 |
| syntax.tag.doctype | TextMate: entity.name.tag，视觉补偿 | #F38A91 | 原色见补偿表 |
| syntax.number | TextMate: constant.numeric，视觉补偿 | #F491CC | 原色见补偿表 |
| syntax.operator | TextMate: keyword.operator | #D5D8E0 |  |
| syntax.punctuation | TextMate: keyword.operator | #D5D8E0 |  |
| syntax.punctuation.bracket | TextMate: keyword.operator | #D5D8E0 |  |
| syntax.punctuation.delimiter | TextMate: keyword.operator | #D5D8E0 |  |
| syntax.punctuation.special | TextMate: punctuation.definition.template-expression.begin，视觉补偿 | #F38A91 | 原色见补偿表 |
| syntax.punctuation.list_marker | TextMate: punctuation.definition.list.begin.markdown，视觉补偿 | #F38A91 | 原色见补偿表 |
| syntax.string | TextMate: string，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.string.escape | TextMate: constant.character.escape，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.string.regex | TextMate: string.regexp，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.string.special | TextMate: string，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.string.special.symbol | TextMate: constant.character，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.text.literal | TextMate: markup.inline.raw，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.preproc | TextMate: meta.preprocessor，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.label | TextMate: entity.name.label，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.title | TextMate: markup.heading，视觉补偿 | #8CC4FF | 原色见补偿表 |
| syntax.emphasis | TextMate: markup.italic | #D1D3DB |  |
| syntax.emphasis.strong | TextMate: markup.bold | #D5D8E0 |  |
| syntax.embedded | TextMate: meta.embedded，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.link_text | TextMate: string，视觉补偿 | #87DBA3 | 原色见补偿表 |
| syntax.link_uri | TextMate: string，视觉补偿 | #87DBA3 | 原色见补偿表 |
