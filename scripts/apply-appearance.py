"""Apply the appearance template to persistent Zed settings using Python 3.11+."""
import argparse
import json
import os
import tempfile
from datetime import datetime
from pathlib import Path


def tokens(source):
    result = []
    i = 0
    while i < len(source):
        if source[i].isspace():
            i += 1
            continue
        if source.startswith('//', i):
            end = source.find(chr(10), i)
            i = len(source) if end < 0 else end
            continue
        if source.startswith('/*', i):
            i = source.index('*/', i + 2) + 2
            continue
        start = i
        if source[i] == chr(34):
            i += 1
            while source[i] != chr(34):
                i += 2 if source[i] == chr(92) else 1
            i += 1
        elif source[i] in '{}[]:,':
            i += 1
        else:
            while i < len(source) and not source[i].isspace() and source[i] not in '{}[]:,':
                i += 1
        result.append((source[start:i], start, i))
    return result


def load_jsonc(source):
    items = tokens(source)
    clean = ''.join(raw for i, (raw, _, _) in enumerate(items)
                    if not (raw == ',' and items[i + 1][0] in ('}', ']')))
    return json.loads(clean)


def merge(base, overrides):
    result = dict(base)
    for key, value in overrides.items():
        result[key] = merge(result[key], value) if isinstance(value, dict) and isinstance(result.get(key), dict) else value
    return result


def patch_object(source, overrides):
    items = tokens(source)
    values = {}
    depth = 0
    key = None
    for i, (raw, _, _) in enumerate(items):
        if depth == 1 and raw == ':':
            key = json.loads(items[i - 1][0])
            start = items[i + 1][1]
        if depth == 1 and raw in (',', '}') and key is not None:
            if key in values:
                raise ValueError('Duplicate appearance setting: ' + key)
            values[key] = (start, items[i - 1][2])
            key = None
        depth += (raw in ('{', '[')) - (raw in ('}', ']'))
    edits = []
    additions = []
    for key, value in overrides.items():
        if key not in values:
            additions.append('  ' + json.dumps(key) + ': ' + json.dumps(value, ensure_ascii=False, indent=2) + ',')
            continue
        a, b = values[key]
        old = source[a:b]
        parsed = load_jsonc(old)
        if isinstance(value, dict) and isinstance(parsed, dict):
            replacement = patch_object(old, value)
        elif parsed == value:
            continue
        else:
            replacement = json.dumps(value, ensure_ascii=False, indent=2)
        edits.append((a, b, replacement))
    if additions:
        a = items[0][2]
        edits.append((a, a, chr(10) + chr(10).join(additions) + chr(10)))
    for a, b, value in sorted(edits, reverse=True):
        source = source[:a] + value + source[b:]
    return source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without writing settings')
    parser.add_argument('--settings', type=Path, default=Path.home() / '.config/zed/settings.json')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    overrides = json.loads((root / 'settings/settings.example.json').read_text())
    path = args.settings.expanduser()
    source = path.read_text() if path.exists() else '{}'
    before = load_jsonc(source)
    if not isinstance(before, dict):
        raise ValueError('Zed settings must be a JSON object')
    changed = [key for key in overrides if merge(before, {key: overrides[key]}) != before]
    if not changed:
        print('PASS: persistent appearance already matches the template')
        return
    if args.check:
        print('Appearance differs: ' + ', '.join(changed))
        raise SystemExit(1)
    updated = patch_object(source, overrides)
    if load_jsonc(updated) != merge(before, overrides):
        raise ValueError('Settings verification failed; no file written')
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    if path.exists():
        backup = path.with_name(path.name + '.before-trae-appearance-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
        with backup.open('x') as stream:
            os.chmod(backup, 0o600)
            stream.write(source)
        if path.read_text() != source:
            raise ValueError('Settings changed during update; no file written')
        print('Backup: ' + str(backup))
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.trae-appearance-')
    try:
        os.fchmod(fd, mode)
        with os.fdopen(fd, 'w') as stream:
            stream.write(updated)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print('Applied persistent appearance: ' + ', '.join(changed))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, IndexError, OSError) as error:
        raise SystemExit('Appearance update failed: ' + str(error))
