# Icon Library

This repository stores PNG icon files and automatically generates
`zhangjiawen.icons.json` for downstream scripts or projects.

## Structure

- `icon/`: icon asset directory, including nested subdirectories.
- `.github/scripts/generate_image_json.py`: builds the JSON manifest from `icon/`.
- `.github/workflows/blank.yml`: regenerates and commits the manifest when icons change.
- `zhangjiawen.icons.json`: published icon manifest.

## JSON format

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

## Automation behavior

- Changes under `icon/` trigger a manifest regeneration.
- On `pull_request`, the workflow validates and uploads the artifact without pushing back.
- On `push` or manual runs, the workflow commits the updated manifest only when it changed.

## Notes

- Keep icon files in `.png` format.
- Nested folders under `icon/` are supported.
- Raw file URLs follow the branch that triggered the workflow, so branch previews stay accurate.
