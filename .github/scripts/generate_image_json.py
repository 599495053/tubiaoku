import json
import os
import subprocess
from pathlib import Path


DEFAULT_REPOSITORY = "599495053/tubiaoku"


def resolve_repository_slug():
    repository = os.environ.get("GITHUB_REPOSITORY")
    if repository:
        return repository

    try:
        remote_url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return DEFAULT_REPOSITORY

    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]

    if remote_url.startswith("git@github.com:"):
        return remote_url.removeprefix("git@github.com:")

    if "github.com/" in remote_url:
        return remote_url.split("github.com/", 1)[1]

    return DEFAULT_REPOSITORY


def iter_icons(image_folder):
    for root, _, files in os.walk(image_folder):
        _.sort()
        for filename in sorted(files):
            if not filename.lower().endswith(".png"):
                continue

            image_path = os.path.relpath(os.path.join(root, filename), os.getcwd())
            normalized_path = image_path.replace("\\", "/")
            display_name = normalized_path.removeprefix("icon/")
            yield normalized_path, display_name


def generate_json():
    image_folder = "icon"
    icons_base_ref = os.environ.get("ICONS_BASE_REF", "main")
    repository_slug = resolve_repository_slug()
    json_data = {
        "name": "\u5f20\u5609\u6587\u81ea\u7528",
        "description": "\u6536\u96c6\u4e00\u4e9b\u81ea\u5df1\u811a\u672c\u7528\u5230\u7684\u56fe\u6807",
        "icons": [],
    }

    for image_path, filename in iter_icons(image_folder):
        raw_url = (
            f"https://raw.githubusercontent.com/"
            f"{repository_slug}/{icons_base_ref}/{image_path}"
        )
        json_data["icons"].append({"name": filename, "url": raw_url})

    output_path = Path.cwd() / "zhangjiawen.icons.json"
    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)
        json_file.write("\n")


if __name__ == "__main__":
    generate_json()
