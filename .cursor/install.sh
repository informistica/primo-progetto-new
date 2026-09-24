#!/usr/bin/env bash
set -euo pipefail

# The default Cloud Agent base image ships Python 3.12 but not the python3-venv
# package (ensurepip), which is required to create virtual environments.
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    sudo apt-get update -qq
    sudo apt-get install -y -qq python3-venv
fi

# Create the virtual environment if it does not already exist.
if [ ! -x ".venv/bin/python" ]; then
    python3 -m venv .venv
fi

# Install / refresh project dependencies from the lockfile-style requirements.
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt
