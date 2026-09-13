#!/usr/bin/env python3
import sys
import argparse

TARGET_MAP = {
    "disneyplus": "DisneyPlus",
    "primevideo": "PrimeVideo",
    "netflix": "Netflix",
    "hbomax": "HBOMax",
    "peacock": "Peacock",
    "tubi": "Tubi",
    "vix": "ViX",
    "plutotv": "PlutoTV",
    "paramountplus": "ParamountPlus",
    "twitch": "Twitch",
    "espn": "ESPN",
}

def main():
    parser = argparse.ArgumentParser(description="Configure config.toml with custom build parameters")
    parser.add_argument("--config", default="config.toml", help="Path to config.toml")
    parser.add_argument("--target", default="all", choices=["all"] + list(TARGET_MAP.keys()), help="Target app to build")
    parser.add_argument("--app-version", default="auto", help="APK version to build (e.g. 'auto' or specific version)")
    parser.add_argument("--patches-version", default="latest", help="Patches version to build")
    parser.add_argument("--patches-source", default="", help="Custom patches source repository (optional)")
    parser.add_argument("--included-patches", default="", help="Custom included patches (optional)")
    parser.add_argument("--excluded-patches", default="", help="Custom excluded patches (optional)")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sections = {}
    current_sec = "main"
    sections[current_sec] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            current_sec = stripped[1:-1].strip()
            sections[current_sec] = [line]
        else:
            sections[current_sec].append(line)

    # Filter target
    if args.target != "all" and args.target in TARGET_MAP:
        selected_section = TARGET_MAP[args.target]
        for sec in list(sections.keys()):
            if sec != "main" and sec != selected_section:
                sections.pop(sec, None)

    # Apply custom overrides to remaining tables
    for sec_name in list(sections.keys()):
        if sec_name == "main":
            continue
        
        sec_lines = sections[sec_name]

        # App version override
        if args.app_version and args.app_version.strip() not in ("auto", ""):
            new_lines = []
            replaced = False
            for l in sec_lines:
                if l.strip().startswith("version"):
                    new_lines.append(f'version = "{args.app_version.strip()}"\n')
                    replaced = True
                else:
                    new_lines.append(l)
            if not replaced:
                new_lines.append(f'version = "{args.app_version.strip()}"\n')
            sec_lines = new_lines

        # Patches version override
        if args.patches_version and args.patches_version.strip() not in ("latest", ""):
            new_lines = []
            replaced = False
            for l in sec_lines:
                if l.strip().startswith("patches-version"):
                    new_lines.append(f'patches-version = "{args.patches_version.strip()}"\n')
                    replaced = True
                else:
                    new_lines.append(l)
            if not replaced:
                new_lines.append(f'patches-version = "{args.patches_version.strip()}"\n')
            sec_lines = new_lines

        # Patches source override
        if args.patches_source and args.patches_source.strip():
            new_lines = []
            replaced = False
            for l in sec_lines:
                if l.strip().startswith("patches-source"):
                    new_lines.append(f'patches-source = "{args.patches_source.strip()}"\n')
                    replaced = True
                else:
                    new_lines.append(l)
            if not replaced:
                new_lines.append(f'patches-source = "{args.patches_source.strip()}"\n')
            sec_lines = new_lines

        # Included patches override
        if args.included_patches and args.included_patches.strip():
            inc = args.included_patches.strip()
            if not ((inc.startswith("'") and inc.endswith("'")) or (inc.startswith('"') and inc.endswith('"'))):
                inc = f"'{inc}'"
            new_lines = []
            replaced = False
            for l in sec_lines:
                if l.strip().startswith("included-patches"):
                    new_lines.append(f'included-patches = "{inc}"\n')
                    replaced = True
                else:
                    new_lines.append(l)
            if not replaced:
                new_lines.append(f'included-patches = "{inc}"\n')
            sec_lines = new_lines

        # Excluded patches override
        if args.excluded_patches and args.excluded_patches.strip():
            exc = args.excluded_patches.strip()
            if not ((exc.startswith("'") and exc.endswith("'")) or (exc.startswith('"') and exc.endswith('"'))):
                exc = f"'{exc}'"
            new_lines = []
            replaced = False
            for l in sec_lines:
                if l.strip().startswith("excluded-patches"):
                    new_lines.append(f'excluded-patches = "{exc}"\n')
                    replaced = True
                else:
                    new_lines.append(l)
            if not replaced:
                new_lines.append(f'excluded-patches = "{exc}"\n')
            sec_lines = new_lines

        sections[sec_name] = sec_lines

    output = ""
    for sec_name, sec_lines in sections.items():
        output += "".join(sec_lines)
        if not output.endswith("\n\n"):
            output += "\n"

    with open(args.config, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Successfully configured {args.config} for target={args.target}, app_version={args.app_version}, patches_version={args.patches_version}")

if __name__ == "__main__":
    main()
