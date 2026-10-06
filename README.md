# Codex Orchestrator

<!-- Modified for this distribution: adaptive delegation, subscription presets, and project documentation. -->

**Codex orchestration profiles with specialized agents, adaptive delegation, and
project setup for focused and multi-agent coding workflows.**

[![CI](https://github.com/snaplyze/codex-orchestrator/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/snaplyze/codex-orchestrator/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/snaplyze/codex-orchestrator)](https://github.com/snaplyze/codex-orchestrator/releases/latest)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

[Getting started](guides/getting-started.md) · [Documentation](guides/README.md) · [Profiles](guides/model-selection.md) · [Migration](guides/migration.md) · [Contributing](CONTRIBUTING.md)

For developers and teams using Codex, these bundles combine model settings with
role instructions and a shared workflow for deciding when to delegate.

Keep small tasks in the root agent. Delegate larger tasks to a focused worker,
then add exploration, testing, research, or independent review when they help.
The root keeps ownership of scope, integration, and final verification.

This repository provides **configuration, role instructions, and a shared skill**.
It is not a separate agent server, scheduler, or billing controller, and it does
not install Codex itself. You use it inside an existing Codex project.

## What you get

- **Four profile bundles:** Plus and Pro 100/200/500, with explicit model,
  reasoning, permission, and concurrency settings.
- **Five named roles and one shared skill:** `explorer`, `researcher`, `worker`,
  `tester`, and `reviewer`, coordinated through `$codex-orchestrator`.
- **Project installers and usage reporting:** interactive shell/PowerShell setup
  and a read-only Python report for local Codex rollout logs.

<a id="project-setup"></a>

## Quick start

You need a working Codex CLI, Git to clone this repository, and an existing target
project **outside this source checkout**. Use a POSIX shell on Linux/macOS or
PowerShell on Windows. See [requirements and setup](guides/getting-started.md)
for the full walkthrough.

Clone the distribution:

```bash
git clone https://github.com/snaplyze/codex-orchestrator.git
cd codex-orchestrator
```

<a id="macos-and-linux"></a>
<a id="windows"></a>

Run the installer for your platform:

| Linux / macOS | Windows — PowerShell 7 |
|---|---|
| `sh ./setup.sh` | `pwsh -File .\setup.ps1` |

Windows PowerShell 5.1 instructions are in the
[Windows setup section](guides/getting-started.md#windows).

<a id="installer-prompts"></a>

At the prompts, enter your target path, such as `../my-project`, and choose
`plus`, `pro-100`, `pro-200`, or `pro-500`. Review the `.codex`, `.agents`, and
`AGENTS.md` prompts. Existing-file replacements require separate confirmation
and default to **no**; unrelated files and user-owned instructions are preserved.

Then start a **new Codex session in the target project**:

```bash
cd ../my-project
codex
```

<a id="using-the-skill"></a>

Use your actual target path. Complete the normal project-trust flow, check
`/model` and `/status`, and enter this prompt **inside Codex, not your shell**:

```text
$codex-orchestrator

Normal mode. Audit this project's test coverage without editing files.
Choose the lightest useful delegation. Return concrete gaps with file references
and verification evidence. Do not commit, publish, or change configuration.
```

Already installed? Follow [migration](guides/migration.md#subscription-profile-upgrade)
instead of treating an upgrade as a fresh installation.

<a id="personalglobal-setup"></a>

For user-wide defaults, see [personal/global setup](guides/getting-started.md#personalglobal-setup).
Do not overwrite unrelated global configuration.

<a id="current-profile-configuration"></a>

## Choose a profile

These are the **bundled defaults**, not guarantees of account access or savings.

| Bundle | Root | Worker / tester | Concurrent children |
|---|---|---|---:|
| `plus` | Luna `max` | Luna `high` | 2 |
| `pro-100` | Sol 6.1 `medium` | Sol 6.1 `medium` | 2 |
| `pro-200` | Sol 6.1 `medium` | Sol 6.1 `medium` | 3 |
| `pro-500` | Sol 6.1 `medium` | Sol 6.1 `medium` | 4 |

Every bundle uses Luna `high` for exploration, research, and generic children;
Sol 6.1 `medium` for independent review; and Standard speed. The exact model IDs
are `gpt-6-luna` and `gpt-6.1-sol`. The child cap excludes the root and is a
ceiling, not a target or a total usage budget.

> **Installer bundles are not native Codex `--profile` entries.** Setup installs
> the selected bundle as the target project's active configuration. To change
> bundles, rerun setup, review the updates, and start a new session.

See [model selection](guides/model-selection.md) for the full role matrix,
account-access caveats, compatibility names, and dated external sources.
Copyable configuration is in the [Pro](guides/full-orchestration.md) and
[Plus](guides/plus-plan.md) guides.

<a id="suggested-topology"></a>
<a id="work-modes-and-tuning"></a>
<a id="important-behavior"></a>

## Work at the right scale

| Task | Starting point |
|---|---|
| Small, localized change | Root implements and verifies directly. |
| Bounded task with a useful independent part | One specialist; root integrates and verifies. |
| Risky or cross-component work | Add investigation, testing, and independent review as needed. |

`Economy`, `Normal`, and `Thorough` are task instructions, not extra CLI commands
or installer flags. They do not silently change models, permissions, or speed,
and they retain required tests and requested review.
See [using the orchestrator](guides/usage.md) for roles, examples, and tuning.

<a id="token-usage"></a>

## Measure usage

From this distribution checkout, with Python available:

```bash
python3 scripts/token_usage.py --latest
```

On Windows, use `python` instead of `python3`. `--latest` selects the newest
recorded session that used non-guardian subagents; if none exists, use `--list`
and `--root <id>` for a root-only session. The report reads existing local
rollout logs; it does not call a model. Token totals and quota snapshots are not
a bill or proof of remaining subscription allowance. Date-filtered reports may
omit related threads. See [token usage](guides/token-usage.md) before comparing runs
or sharing output, which can contain private paths and session metadata.

<a id="layout"></a>

## Documentation and project layout

Use the [documentation index](guides/README.md) to choose a task-specific guide.
For changes to this distribution, start with [Contributing](CONTRIBUTING.md)
and [development and verification](guides/development.md).

<details>
<summary>Source and installed layout</summary>

```text
profiles/<bundle>/
  codex/config.toml                   → <target>/.codex/config.toml
  codex/agents/*.toml                 → <target>/.codex/agents/
  agents/skills/codex-orchestrator/    → <target>/.agents/skills/codex-orchestrator/
AGENTS.md (managed block only)        → <target>/AGENTS.md
setup.sh / setup.ps1                  # Interactive project installers
scripts/token_usage.py               # Read-only rollout usage report
guides/                              # User and contributor documentation
docs/audit-remediation.md             # Audit history and verification checkpoints
tests/                               # Profile, installer, and usage regressions
```

Canonical bundles are `plus`, `pro-100`, `pro-200`, and `pro-500`.
`pro` and `pro-max-2-subagents` are compatibility copies of `pro-100`;
`plus-max-2-subagents` is a compatibility copy of `plus`.

</details>

## License

Maintained by [snaplyze](https://github.com/snaplyze)
([github@snaplyze.me](mailto:github@snaplyze.me)).

Copyright 2026 snaplyze. Applies to modifications in this distribution.
Licensed under the [Apache License 2.0](LICENSE).
