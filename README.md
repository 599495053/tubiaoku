# 图标库

这是一个用于集中管理图标资源的仓库，主要存放脚本或其他项目会用到的 PNG 图标，并自动生成对应的图标清单文件 `zhangjiawen.icons.json`。

仓库的核心作用有两部分：

1. 统一存放图标文件，方便集中维护和引用。
2. 在图标发生变化时，自动生成最新的 JSON 清单，供下游项目直接读取。

## 整体功能

- 存放图标资源：所有图标统一放在 `icon/` 目录下，支持继续按分类拆分子目录。
- 自动生成清单：仓库会根据 `icon/` 目录中的 PNG 文件生成 `zhangjiawen.icons.json`。
- 提供原始链接：JSON 中会为每个图标生成可直接访问的 Raw 地址，方便脚本、配置文件或其他项目引用。
- 自动化更新：当图标文件发生变化时，GitHub Actions 会自动重新生成清单文件。

## 目录结构

- `icon/`：图标资源目录。
- `.github/scripts/generate_image_json.py`：用于扫描图标并生成 JSON 清单的脚本。
- `.github/workflows/blank.yml`：用于自动执行生成流程的 GitHub Actions 工作流。
- `zhangjiawen.icons.json`：对外提供使用的图标清单文件。

## JSON 清单说明

生成后的 `zhangjiawen.icons.json` 结构如下：

```json
{
  "name": "张嘉文自用",
  "description": "收集一些自己脚本用到的图标",
  "icons": [
    {
      "name": "ChatGPT.png",
      "url": "https://raw.githubusercontent.com/599495053/tubiaoku/main/icon/ChatGPT.png"
    }
  ]
}
```

字段说明：

- `name`：图标集合名称。
- `description`：图标集合说明。
- `icons`：图标列表。
- `icons[].name`：图标名称；如果图标放在子目录中，会保留相对路径，例如 `social/ChatGPT.png`。
- `icons[].url`：图标对应的原始访问地址。

## 自动化流程

- 当 `icon/` 目录下的文件发生变化时，会触发 GitHub Actions。
- 工作流会重新生成 `zhangjiawen.icons.json`。
- 在 Pull Request 场景下，工作流只做生成和校验，不会直接回写主分支。
- 在推送到分支或手动触发时，如果清单内容有变化，工作流会自动提交最新结果。

## 本地使用

如果你想在本地手动生成最新清单，可以直接运行：

```bash
python .github/scripts/generate_image_json.py
```

脚本在本地运行时，会优先读取当前仓库的远程地址来生成正确的图标链接；如果在 GitHub Actions 中运行，则会自动使用当前工作流环境中的仓库信息。

## 使用建议

- 图标统一使用 `.png` 格式。
- 如果图标数量增加，建议按业务或用途拆分子目录。
- 修改或新增图标后，可以检查 `zhangjiawen.icons.json` 是否已同步更新。
- 如果其他项目需要引用图标，优先读取 JSON 清单中的地址，避免手动维护路径。
