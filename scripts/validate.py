"""Validate with Python 3.11+ and jsonschema; pass the official schema path."""
import json
import re
import sys
import tomllib
from pathlib import Path

from jsonschema import Draft7Validator

root = Path(__file__).resolve().parents[1]
schema = json.loads(Path(sys.argv[1]).read_text())
Draft7Validator.check_schema(schema)
manifest = tomllib.loads((root / "extension.toml").read_text())
assert manifest["id"] == "zed-deep-blue"
assert manifest["name"] == "Trae Deep Blue"
assert manifest["version"] == "0.1.0"
assert manifest["schema_version"] == 1
assert manifest["authors"] == ["zetttt"]
assert manifest["themes"] == ["themes/trae-deep-blue.json"]
assert set(manifest) <= {
    "id", "name", "version", "schema_version", "authors", "description", "themes"
}
theme = json.loads((root / manifest["themes"][0]).read_text())
Draft7Validator(schema).validate(theme)
assert theme["name"] == "Trae Deep Blue"
assert theme["author"] == "zetttt"
assert len(theme["themes"]) == 1
content = theme["themes"][0]
assert content["name"] == "Trae Deep Blue" and content["appearance"] == "dark"
style = content["style"]
properties = schema["definitions"]["ThemeStyleContent"]["properties"]
assert set(style) == set(properties), "Missing or unknown official style fields"

def check_colors(value, path="style"):
    if isinstance(value, dict):
        for key, item in value.items():
            check_colors(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            check_colors(item, f"{path}[{index}]")
    elif isinstance(value, str) and path != "style.background.appearance":
        if path.endswith(".font_style"):
            assert value in {"normal", "italic", "oblique"}, path
        else:
            assert re.fullmatch(r"#[0-9A-Fa-f]{6}(?:[0-9A-Fa-f]{2})?", value), path

check_colors(style)
for capture in ["comment", "keyword", "function", "type", "variable", "variable.parameter",
                "string", "number", "tag", "attribute", "property.json_key", "title"]:
    assert capture in style["syntax"], capture
print(f"PASS: official Draft-07 Schema; {len(style)} style fields; "
      f"{len(style['syntax'])} syntax captures; colors and v0.1.0 manifest")
