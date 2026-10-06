# Getting started

[Documentation](README.md) · [Using the orchestrator](usage.md) · [Migration](migration.md)

Install the distribution into one existing project, then verify it in a fresh
Codex session. The project installers do not install or update Codex and do not
change your global configuration.

## Requirements

| Component | Needed for |
|---|---|
| A working Codex client with local skills and custom agents | Running the installed configuration; CLI examples below use `codex` |
| An existing target project outside this source checkout | Receiving project-scoped configuration and instructions |
| Git | Cloning or updating the distribution |
| A POSIX shell on Linux/macOS, or PowerShell on Windows | Running the corresponding installer |
| Python | Optional usage reporting and contributor checks; the test matrix uses Python 3.12 |

The installers and static tests do not prove that your account can use a model.
Inspect the active model picker and [profile caveats](model-selection.md).
Do not relax permissions or overwrite global settings to make setup appear to work.

## 1. Get the distribution

```bash
git clone https://github.com/snaplyze/codex-orchestrator.git
cd codex-orchestrator
```

These commands use the default branch. Published versions are listed under
[Releases](https://github.com/snaplyze/codex-orchestrator/releases).
For an existing checkout or a release pin, read [migration](migration.md)
before changing its ref or remote.

Keep the distribution and target separate, for example:

```text
projects/
  codex-orchestrator/    # Installer source
  my-project/            # Existing installation target
```

Setup rejects its own source directory. It does not detect every nested layout;
keeping the target outside the checkout is an installation requirement, not a
recursive containment guarantee.

## 2. Run the installer

### Linux and macOS

From the distribution directory:

```bash
sh ./setup.sh
```

### Windows

From the distribution directory, use PowerShell 7:

```powershell
pwsh -File .\setup.ps1
```

Or use Windows PowerShell 5.1:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

The latter sets execution policy for that process, not the machine-wide policy
([Microsoft reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe#-executionpolicy-executionpolicy)).
Review the script before executing it and respect any organization-managed policy.

## 3. Select the target and bundle

Enter the existing target's absolute path or a path relative to your current
working directory, such as `../my-project` or `..\my-project`.
Then choose an explicit bundle name:

| Menu | Bundle | Concurrent children |
|---|---|---:|
| 1 — default | `pro-100` | 2 |
| 2 | `plus` | 2 |
| 3 | `pro-200` | 3 |
| 4 | `pro-500` | 4 |

Names are case-insensitive. Legacy names print a migration notice.
**Choices 3 and 4 changed in v0.4.0**; use explicit names in scripted input.
See [model selection](model-selection.md) for model and effort defaults.
The installer does not detect your subscription, grant model access, buy credits,
or enable accelerated speed.

## 4. Review the component prompts

| Source | Installed location | Purpose |
|---|---|---|
| `profiles/<bundle>/codex/` | `<target>/.codex/` | Root settings and five named roles |
| `profiles/<bundle>/agents/` | `<target>/.agents/` | The shared `codex-orchestrator` skill |
| Managed block in the source `AGENTS.md` | `<target>/AGENTS.md` | Project orchestration instructions |

Press Enter or answer `y` to select a component; answer `n` to skip it.
All three components are selected by default. A complete installation needs all
three; declining one can leave a partial installation or migration.

For an existing component, setup lists the paths it would replace and asks again.
**Replacement defaults to no.** Approval adds missing files and replaces only the
listed paths; it does not merge custom TOML values inside those files.
Review custom root and role settings before approving.

Existing instructions outside the managed `AGENTS.md` block are preserved.
An unmanaged file has a separate append confirmation. A fresh target receives
only the managed project instructions, not this source repository's maintainer
rules. Symbolic links and incompatible targets are skipped.

Normal failures trigger rollback of installer-owned output, while detected
concurrent edits are preserved. Avoid editing managed paths during setup.
See [failure handling and its limits](migration.md#failed-updates-and-recovery)
for the existing installer's transaction behavior.

## 5. Verify a fresh session

Change to the target and launch Codex:

```bash
cd ../my-project
codex
```

Use your actual path and the client's normal project-trust flow. Project-scoped
configuration must be trusted before it is loaded. In the new session, inspect
`/model` and `/status` for the expected root settings. Review the five role
files against the selected bundle; these commands alone do not verify a child
role's effective settings. Inspect actual child-thread settings when delegating.
OpenAI documents [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
and [local skill discovery](https://learn.chatgpt.com/docs/build-skills).

A complete target includes:

```text
.codex/
  config.toml
  agents/
    explorer.toml
    researcher.toml
    reviewer.toml
    tester.toml
    worker.toml
.agents/skills/codex-orchestrator/SKILL.md
AGENTS.md
```

Invoke `$codex-orchestrator` inside Codex. A first task can be an audit with no
file or external writes; see the [copyable examples](usage.md#example-tasks).
A listed skill or model is evidence of discovery, not proof of effective role
settings, successful inference, or account allowance. Live tasks consume usage.

## Personal/global setup

Use project setup unless you deliberately need user-wide defaults. Manual global
installation uses the same bundle throughout. With the default user paths:

| From the selected bundle | User-level destination |
|---|---|
| `codex/agents/*.toml` | `~/.codex/agents/` |
| `agents/skills/codex-orchestrator/` | `~/.agents/skills/codex-orchestrator/` |
| Settings in `codex/config.toml` | Merge into `~/.codex/config.toml` |
| Managed block in the source `AGENTS.md` | Merge into `~/.codex/AGENTS.md` |

Copy only the managed instruction block, preserving existing global instructions.
An active `~/.codex/AGENTS.override.md` takes precedence over that global file;
review the instruction sources actually loaded rather than adding duplicate
blocks. See [OpenAI's instruction discovery rules](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Use your client's actual configuration paths when customized. Preserve unrelated
providers, MCP servers, plugins, permissions, and roles. Do not blindly replace
an existing global config. For an existing installation, follow
[manual/global migration](migration.md#manual-or-global-installations), including
old skill names and managed instruction references.

## Troubleshooting

| Symptom | Check first |
|---|---|
| `codex` is not found | Verify that the Codex CLI is installed and on this shell's PATH; this distribution does not install it. |
| The root or roles still use old settings | Confirm the target, trust state, selected bundle, and runtime overrides; restart after configuration changes. Changing only the root does not change pinned named roles. |
| The skill is missing | Check `.agents/skills/codex-orchestrator/SKILL.md`, the client's skill picker, and whether the `.agents` component was skipped. |
| A configured model is rejected | Record the rejected ID, check actual account/workspace access, and choose an explicitly approved available fallback; do not silently substitute. |
| Setup reports a partial installation | Rerun for the same target and review the missing component updates together. |
| Setup stops on a link, managed-block conflict, or concurrent edit | Read the reported path and the [migration guide](migration.md#failed-updates-and-recovery); do not bypass the safeguard or overwrite newer work. |

For a reproducible defect, [open an issue](https://github.com/snaplyze/codex-orchestrator/issues/new/choose)
with the distribution revision, OS, shell, Codex version, selected bundle, and
sanitized reproduction. Do not upload private configuration or raw rollout logs.
