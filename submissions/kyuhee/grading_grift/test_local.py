#!/usr/bin/env python3
"""
Local test script for GradingGrift scenario.

This script registers the plugin dynamically and runs the scenario
without modifying the core framework files.

Usage:
    uv run python submissions/kyuhee/grading_grift/test_local.py
"""
import subprocess
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

# Register plugin before importing orchestrator
from submissions.kyuhee.grading_grift.plugin import GradingGriftPlugin
from scenarios.security_arena.plugins.registry import register_scenario

try:
    register_scenario("grading_grift", GradingGriftPlugin)
    print("Registered grading_grift plugin")
except ValueError:
    print("Plugin already registered")

# Now run the scenario
toml_path = Path(__file__).parent / "scenario_grading_grift.toml"
cmd = ["uv", "run", "agentbeats-run", str(toml_path), "--show-logs"]
print(f"Running: {' '.join(cmd)}")
subprocess.run(cmd, cwd=project_root)
