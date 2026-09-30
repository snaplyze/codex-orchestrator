# Codex Orchestrator

<!-- Modified for this distribution: adaptive delegation guidance, setup URL, and maintainer details. -->

A configurable Codex setup for **Plus, Pro 100, Pro 200, and Pro 500**. Pro uses GPT-6.1 Sol for coordination and execution; Plus uses GPT-6 Luna. All profiles use Sol 6.1 for ordinary independent review and Standard speed.

Repository: [snaplyze/codex-orchestrator](https://github.com/snaplyze/codex-orchestrator).
For an existing installation, follow the [profile migration guide](guides/migration.md#subscription-profile-upgrade).

For maintenance and verification, see the [development guide](guides/development.md)
and [audit remediation plan](docs/audit-remediation.md). The plan separates confirmed
limitations from pending fixes and records their acceptance checks.

The Pro profiles permit two, three, and four concurrent child threads respectively.
Plus permits two. Astra is available as an escalation for difficult work rather
than the permanent root/reviewer. These are workload presets, not subscription
access restrictions or measured savings. See [model selection](guides/model-selection.md)
for official sources checked on September 30, 2026 and the account-access caveats.

## Layout

```text
profiles/
  pro-100/                 # Sol 6.1 root and execution, 2 child threads
  pro-200/                 # Same models, 3 child threads
  pro-500/                 # Same models, 4 child threads
  plus/                    # Luna root and execution, 2 child threads
  pro/                     # Compatibility copy of pro-100
  pro-max-2-subagents/      # Compatibility copy of pro-100
  plus-max-2-subagents/     # Compatibility copy of plus
guides/                    # Setup, model selection, workload and usage guides
docs/audit-remediation.md   # Audit history and subsequent verification checkpoints
scripts/token_usage.py     # Read-only rollout usage report
tests/                     # Profile, installer and usage regressions
setup.sh / setup.ps1        # Project installers
AGENTS.md                  # Maintainer rules and distributed instruction block
```

Each profile contains `codex/config.toml`, five `codex/agents/*.toml` roles, and
`agents/skills/codex-orchestrator/SKILL.md`. The shared skill is identical across
all canonical and compatibility bundles.

## Current profile configuration

| Role or setting | Plus | Pro 100 | Pro 200 | Pro 500 |
|---|---|---|---|---|
| Orchestrator | Luna — max | Sol 6.1 — medium | Sol 6.1 — medium | Sol 6.1 — medium |
| Explorer, researcher | Luna — high | Luna — high | Luna — high | Luna — high |
| Worker, tester | Luna — high | Sol 6.1 — medium | Sol 6.1 — medium | Sol 6.1 — medium |
| Default subagent | Luna — high | Luna — high | Luna — high | Luna — high |
| Independent reviewer | Sol 6.1 — medium | Sol 6.1 — medium | Sol 6.1 — medium | Sol 6.1 — medium |
| Concurrent child cap | 2 | 2 | 3 | 4 |
| Speed | Standard | Standard | Standard | Standard |

All Luna settings use `gpt-6-luna`; Sol 6.1 uses `gpt-6.1-sol`.
Root permissions remain `on-request` / `workspace-write`. Explorer, researcher,
and reviewer default to read-only; worker/tester can write in the workspace.
The cap excludes the root and does not limit total task usage. Role sandbox
settings are defaults: active client permission overrides can take precedence;
read-only role instructions still prohibit file and external writes.

The installer copies `profiles/<profile>/codex` to `.codex` and
`profiles/<profile>/agents` to `.agents` without rewriting configuration.
Choose `pro-100`, `pro-200`, `pro-500`, or `plus`.
Legacy `pro` and `pro-max-2-subagents` map to `pro-100`;
`plus-max-2-subagents` maps to `plus`. Their directories remain copy-ready.

These names select installer bundles. They are not native Codex `--profile`
entries: setup installs the selected bundle as the project's active configuration,
not a named CLI profile. To switch bundles, rerun setup and approve the updates.

Named role files pin their model and effort. Changing only the root or
`default_subagent_model` does not change worker/tester/reviewer settings.
Update configuration, roles, skill, and managed instructions together, then
start a new session. Active runtime overrides take precedence.

See [Pro settings](guides/full-orchestration.md) or [Plus settings](guides/plus-plan.md)
for copyable TOML. Independent review is a separate assessment; it does not
require keeping Astra in every task.

## Project setup

Clone this repository:

```bash
git clone https://github.com/snaplyze/codex-orchestrator.git
cd codex-orchestrator
```

The target project must already exist. Choose a separate directory outside this
source checkout. Setup rejects the source directory itself; it does not detect
every nested project layout, so this placement is part of the installation
instructions rather than a recursive containment guarantee.

### macOS and Linux

Run the shell installer:

```bash
./setup.sh
```

### Windows

Run the PowerShell installer from Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

With PowerShell 7, you can use:

```powershell
pwsh -File .\setup.ps1
```

### Installer prompts

When asked for the target repository, enter its absolute or relative path. For
example:

```text
Target repository path: ../my-project
```

Next, choose your Codex plan by number or explicit profile name:

```text
Codex plan:
  1) Pro 100 - Sol 6.1 root; Luna default children; Sol 6.1 reviewer; 2 child threads
  2) Plus    - Luna root; Luna default children; Sol 6.1 reviewer; 2 child threads
  3) Pro 200 - Sol 6.1 root; Luna default children; Sol 6.1 reviewer; 3 child threads
  4) Pro 500 - Sol 6.1 root; Luna default children; Sol 6.1 reviewer; 4 child threads
Select plan [1-4] (default 1):
```

The default is Pro 100. Names are case-insensitive; legacy names print a migration
notice. **Menu numbers 3 and 4 have changed** from the old max-2 variants to Pro
200 and Pro 500. Use explicit names in scripted input. The installer does not
detect or change your subscription, buy credits, or enable Fast/Ultrafast.

The installer then asks whether to install each component:

- `profiles/<plan>/codex` contains the root configuration and agent role profiles, installed as `.codex`.
- `profiles/<plan>/agents` contains the `codex-orchestrator` skill, installed as `.agents`.
- `AGENTS.md` gives Codex the project-level orchestration instructions. If it
  already exists, setup asks separately before appending to an unmanaged file or
  updating an older managed block, and preserves the user-owned contents.
  A new file receives only the managed project instructions; source-repository
  maintenance rules are not copied into your project.
  Re-running setup recognizes the managed block idempotently, including when the
  file uses CRLF line endings. Symbolic links and incompatible targets are
  skipped.

Press Enter or answer `y` to install a component; answer `n` to skip it. All
three components are selected by default.

If a component already exists, the installer lists the exact paths that would
be overwritten and asks again before making changes:

```text
WARNING: the following existing files will be overwritten:
  - .codex/config.toml
Update .codex? New files will be added; only paths listed above will be replaced. [y/N]
```

Existing-file updates default to `n`. If approved, missing files are added and
only the listed paths are replaced. When migrating an older installation, setup
also lists and archives the legacy skill outside `skills` before installing its
replacement. Other files already present in the target component remain untouched.
Changed files are journaled individually during the run and rolled back if a
later installation step fails. If you decline one or more
components, setup completes but reports that the installation is partial.

Setup stages file replacements in the destination directory, so replacing a
hardlinked config or `AGENTS.md` does not overwrite the linked external file.
Rollback restores only unchanged installer output. Concurrent edits or deletions
are preserved and reported, with recovery copies retained at the printed path;
unrelated files are left alone. Newly created directories are removed only when
empty. If `AGENTS.md` changes while its confirmation prompt is open, setup aborts
the stale update. See [recovery and migration](guides/migration.md#failed-updates-and-recovery)
for conflict handling and the limits of these safeguards.

After setup, launch Codex from the target repository:

```bash
cd ../my-project
codex
```

Use your actual target path. Complete Codex's normal project-trust flow if prompted;
project-scoped configuration is loaded only for trusted projects. In the new
session, inspect `/model` and `/status`, then send the skill prompt below. Check
that the root matches the chosen bundle and the named roles are loaded. A model
listed in configuration does not prove that your account can run it.

See `guides/` for copy-paste model presets and the Sol 6.1 + Luna topology. The
guides are intentionally separate from the installers so you can review and
adapt settings for your Codex version without changing a global config
automatically.

## Personal/global setup

For agents, copy the TOML files from `profiles/<plan>/codex/agents/` to:

```text
~/.codex/agents/
```

For the skill, copy `profiles/<plan>/agents/skills/codex-orchestrator/` to:

```text
~/.agents/skills/codex-orchestrator/
```

Merge the settings from `profiles/<profile>/codex/config.toml`, selecting
`pro-100`, `pro-200`, `pro-500`, or `plus`, into your existing:

```text
~/.codex/config.toml
```

Do not blindly overwrite your existing global config if you already have MCP servers, providers, permissions, or other settings.

For an existing global installation, also migrate the previous skill directory
and its instruction references as described in the [migration guide](guides/migration.md#manual-or-global-installations).

## Using the skill

Codex may select the skill automatically when the task matches its description.

You can also invoke it explicitly from Codex CLI or the IDE extension with:

```text
$codex-orchestrator
```

Example prompt, entered inside Codex (not in the shell):

```text
$codex-orchestrator

Normal mode. Implement the new invoice export endpoint.
Choose the lightest useful delegation for the existing code path.
Run the relevant tests and have reviewer independently assess the final diff.
Do not commit or publish.
```

For economy mode, start with `Economy mode: ...`; for additional risk-driven
validation use `Thorough mode: ...`. These phrases guide the shared skill; they
are not slash commands. Ask explicitly for `explorer`, `worker`, `tester`,
`researcher`, or `reviewer` when a specific role is useful. Codex starts agents
through its available tools; there is no separate role executable to launch.
In clients that expose `/agent`, it lets you inspect/switch existing agent threads.
See [official subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Suggested topology

All profiles choose delegation depth according to the task:

| Tier | Task | Workflow |
|---|---|---|
| 1 — Root-only | Small, localized work | Root implements and verifies directly |
| 2 — Lightweight delegation | Bounded work that benefits from separation | One worker completes the assignment; root verifies |
| 3 — Full orchestration | Risky or cross-cutting work with multiple workstreams | Add investigation, testing, and independent review as needed |

Start with the lightest tier that fits. Specialists are conditional, and review
depth follows risk. The root retains decisions and integration; children return
short findings and verification evidence. Reuse relevant context, batch related
small assignments, and avoid having several agents explore the same files.

## Work modes and tuning

The shared skill accepts task-level work modes independently of subscription:

- **Economy:** small tasks stay in the root; begin with one useful delegate,
  reuse its context, and reduce optional coordination.
- **Normal:** use the configured roles for independent work within the cap.
- **Thorough:** add independent checks for material risk, with higher reasoning
  or an Astra assessment when justified.

These are instructions, not extra TOML keys or installer switches. Every mode
preserves required tests, requested review, and the agreed completion criteria.
The cap is a ceiling, not a quota to fill. Modes do not silently change installed
models, permissions, or speed.

Keep Standard speed by default, including Pro 500. Choose acceleration explicitly
when latency justifies its additional usage. Use current `/status` or dashboard
evidence where available; stale or absent snapshots mean remaining quota is
unknown. There is no automatic quota controller or inferred subscription budget.

For routine work see [Luna settings](guides/routine-coding.md), for optional speed
see [fast iteration](guides/fast-iteration.md), and for escalation see
[complex repository work](guides/complex-repo-work.md). Profile-specific limits and
official subscription caveats are in [model selection](guides/model-selection.md).

## Token usage

Orchestration is not free: the root stays in the loop for the whole task and
every subagent carries its own context. Usage depends on repository size and
task shape, so there is no single number. `scripts/token_usage.py` reads the
rollout logs Codex already writes under `~/.codex/sessions` and reports usage
per thread, role, and model, plus available quota-window snapshots. Reports
identify partial scans, rollout segments and input/counter diagnostics:

```bash
scripts/token_usage.py --list --date 2026-09-07
scripts/token_usage.py --latest
```

See [`guides/token-usage.md`](guides/token-usage.md) for a measurement
protocol, one sample run with real numbers, and tips for reducing usage.

Plus users: long root threads can dominate usage; keeping the root on Luna
is the budget-oriented starting point. Measure representative tasks before
assuming savings. Selecting `Plus` in the installer does this for you; for a
manual or global setup see [`guides/plus-plan.md`](guides/plus-plan.md):

```toml
# Root
model = "gpt-6-luna"
model_reasoning_effort = "max"
```

## Important behavior

Before applying a custom role file, Codex resolves model/effort from explicit
spawn values, then `[agents]` defaults, then the parent. Model/effort pinned in
the custom role file take precedence over those resolved values. This is why
overriding a generic child default or merely requesting another model in a
role's brief does not change the installed role. Active tool schemas can also
restrict overrides; inspect the selected role before relying on a switch.

The selected profile determines the root model: all Pro presets use Sol 6.1,
while Plus uses Luna. Pro worker/tester and all reviewers use Sol 6.1.
Astra escalation must be selected through supported runtime controls; mentioning
a model in a task message does not change a fixed role's model.

New models roll out by account and workspace. Confirm availability with `/model`
and start a fresh session after updating files. Setup copies configuration; it
does not grant model access or change your global Codex installation.

## License

Maintained by [snaplyze](https://github.com/snaplyze) ([github@snaplyze.me](mailto:github@snaplyze.me)).

Copyright 2026 snaplyze. Applies to modifications in this distribution.

Licensed under the [Apache License 2.0](LICENSE).
