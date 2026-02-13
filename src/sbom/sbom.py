#!/usr/bin/env python3
import json
import yaml
import re
import os
from pathlib import Path
import tomllib  # Python 3.11+


def normalize_dep(name, version=None, ecosystem=None):
    return {
        "name": name.lower(),
        "version": version,
        "ecosystem": ecosystem,
    }


def parse_dockerfile(path):
    deps = []
    base_images = []

    if not Path(path).exists():
        return {"base_images": [], "os_packages": []}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if line.upper().startswith("FROM"):
                base_images.append(line.split()[1])

            if "apt-get install" in line or "apk add" in line:
                packages = re.split(r"install|add", line)[-1]
                for pkg in re.split(r"\s+", packages):
                    if pkg and not pkg.startswith("-"):
                        deps.append(normalize_dep(pkg, ecosystem="os"))

    return {
        "base_images": base_images,
        "os_packages": deps,
    }


def parse_package_json(path):
    deps = []

    if not Path(path).exists():
        return []

    with open(path) as f:
        data = json.load(f)

    for section in ["dependencies", "devDependencies"]:
        for name, version in data.get(section, {}).items():
            deps.append(normalize_dep(name, version, "npm"))

    return deps


def parse_pyproject(path):
    deps = []

    if not Path(path).exists():
        return []

    with open(path, "rb") as f:
        data = tomllib.load(f)

    # PEP 621
    for dep in data.get("project", {}).get("dependencies", []):
        if "==" in dep:
            name, version = dep.split("==")
        else:
            name, version = dep, None
        deps.append(normalize_dep(name.strip(), version, "python"))

    # Poetry
    poetry_deps = data.get("tool", {}).get("poetry", {}).get("dependencies", {})
    for name, version in poetry_deps.items():
        if name.lower() != "python":
            deps.append(normalize_dep(name, str(version), "python"))

    return deps


def detect_duplicates(deps):
    seen = {}
    duplicates = []

    for dep in deps:
        key = dep["name"]
        if key in seen:
            duplicates.append({
                "name": key,
                "ecosystems": [seen[key]["ecosystem"], dep["ecosystem"]],
            })
        else:
            seen[key] = dep

    return duplicates


def generate_manifest(repo_path):
    repo = Path(repo_path)

    docker_data = parse_dockerfile(repo / "Dockerfile")
    npm_deps = parse_package_json(repo / "package.json")
    py_deps = parse_pyproject(repo / "pyproject.toml")

    all_deps = docker_data["os_packages"] + npm_deps + py_deps
    duplicates = detect_duplicates(all_deps)

    manifest = {
        "base_images": docker_data["base_images"],
        "dependencies": all_deps,
        "duplicates": duplicates,
    }

    return manifest


if __name__ == "__main__":
    repo_path = "."
    manifest = generate_manifest(repo_path)

    # JSON output
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    # YAML output
    with open("manifest.yaml", "w") as f:
        yaml.dump(manifest, f)

    print("Generated:")
    print(" - manifest.json")
    print(" - manifest.yaml")
