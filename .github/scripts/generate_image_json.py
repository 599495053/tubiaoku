import json
import os


def iter_icons(image_folder):
    for root, _, files in os.walk(image_folder):
        for filename in sorted(files):
            if not filename.lower().endswith(".png"):
                continue

            image_path = os.path.relpath(os.path.join(root, filename), os.getcwd())
            yield image_path.replace("\\", "/"), filename


def generate_json():
    image_folder = "icon"
    icons_base_ref = os.environ.get("ICONS_BASE_REF", "main")
    json_data = {
        "name": "\u5f20\u5609\u6587\u81ea\u7528",
        "description": "\u6536\u96c6\u4e00\u4e9b\u81ea\u5df1\u811a\u672c\u7528\u5230\u7684\u56fe\u6807",
        "icons": [],
    }

    for image_path, filename in iter_icons(image_folder):
        raw_url = (
            f"https://raw.githubusercontent.com/"
            f"{os.environ['GITHUB_REPOSITORY']}/{icons_base_ref}/{image_path}"
        )
        json_data["icons"].append({"name": filename, "url": raw_url})

    output_path = os.path.join(os.getcwd(), "zhangjiawen.icons.json")
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)
        json_file.write("\n")


if __name__ == "__main__":
    generate_json()
