# Using the orchestrator

[Documentation](README.md) · [Getting started](getting-started.md) · [Model selection](model-selection.md)

Start in the target project after installation. The root owns scope, architecture,
integration, and final verification. Delegation should solve a useful independent
part of the task, not turn every edit into a five-agent pipeline.

## Invoke the skill

Enter this in Codex, **not in your shell**:

```text
$codex-orchestrator
```

Codex may also select the skill when a task matches its description. Role names
such as `worker` and `reviewer` are not standalone executables. Codex starts them
through the tools available to the active client. In clients exposing `/agent`,
that command inspects or switches existing threads; it is not a role launcher.
See OpenAI's [subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents)
and [skill guide](https://learn.chatgpt.com/docs/build-skills).

## Choose the lightest useful delegation

| Scope | Starting point |
|---|---|
| Small and localized | The root implements and verifies directly. |
| Bounded work that benefits from separation | One capable specialist can complete the assignment; the root integrates and verifies. |
| Risky or cross-cutting | Add investigation, implementation, testing, and independent review where the risk warrants them. |

Each delegate needs an objective, relevant context, writable scope or an explicit
read-only assignment, permitted Git/external actions, and acceptance checks.
Keep one implementation owner per file. Reuse relevant context, batch related
small assignments, and queue excess work within the configured child cap.
Delegation never expands the user's authorization.

## Roles and boundaries

| Role | Assignment | Bundled sandbox default |
|---|---|---|
| `explorer` | Map repository paths, dependencies, and existing checks | Read-only |
| `researcher` | Verify current technical facts against primary sources | Read-only |
| `worker` | Complete a bounded implementation and focused checks | Workspace-write |
| `tester` | Reproduce failures, add relevant tests, and verify behavior | Workspace-write |
| `reviewer` | Independently assess the actual diff for material defects | Read-only |

The root defaults to `on-request` approvals and `workspace-write`.
Client permission overrides can take precedence over sandbox defaults. Read-only
role instructions still prohibit file and external writes; verify effective
permissions when that boundary matters. Required tests and explicitly requested
review remain part of completion, whichever routing tier is used.

## Profiles, modes, and runtime settings

These are three different layers:

| Layer | What it controls | How to change it |
|---|---|---|
| Installer bundle: `plus`, `pro-100`, `pro-200`, `pro-500` | Bundled model, effort, speed, role, and child-cap settings | Rerun setup, review updates, and start a new session. These are not installed native `--profile` entries. |
| Task mode: Economy, Normal, Thorough | How much useful delegation and risk-driven checking to use | State the mode in the task. These are instructions, not CLI flags or new TOML keys. |
| Active runtime | The settings and role definitions actually loaded, plus client overrides | Inspect the running client and supported controls; configuration edits do not retroactively change old sessions. |

**Economy** keeps small work in the root and reduces optional coordination.
**Normal** uses configured specialists for useful independent work.
**Thorough** adds checks or escalation for material risk. None silently changes
models, permissions, speed, or the definition of done.

Named role files pin model and effort. Changing only the root or generic child
default does not change `worker`, `tester`, or `reviewer`. A model name written
in a delegation message is not a runtime model switch. For custom-role precedence
and explicit escalation, see [model selection](model-selection.md) and
[complex repository work](complex-repo-work.md).

## Example tasks

Replace the task and file scope with your own. Enter each prompt inside Codex.

### Audit without changes

```text
$codex-orchestrator

Normal mode. Audit the installation flow and its regression tests.
Read the project instructions and choose the lightest useful delegation.
Do not edit files, commit, publish, or change local/global configuration.
Return reproducible findings with file references, impact, and verification gaps.
```

### Bounded implementation

```text
$codex-orchestrator

Economy mode. Fix the date-validation error in the existing usage report.
Limit changes to the report, its focused tests, and directly affected documentation.
Preserve unrelated user changes. Delegate only a useful independent part.
Run the focused regressions and applicable full checks. Do not commit or publish.
Report changed paths, actual commands/results, and any checks not run.
```

### Higher-risk work with independent review

```text
$codex-orchestrator

Thorough mode. Fix the installer failure described in the issue provided below.
Reproduce it using a disposable target, never a real user's project.
Preserve unrelated files, custom instructions, and permission defaults.
Implement within the issue's scope and run the relevant regression/full checks.
Have reviewer independently assess the final diff and verification evidence.
Do not commit, publish, change global settings, or buy credits.
Resolve material findings and report any remaining verification limits.

Issue: <paste the issue and its acceptance criteria here>
```

The last example deliberately requests review. A root self-check is not an
independent review. If delegation is unavailable, report that limitation instead
of claiming a specialist ran. No example authorizes work outside its stated scope.

## Usage, speed, and escalation

The child cap is a concurrency ceiling, not a quota to fill or a total token
budget. Long root threads and repeated exploration still consume usage.
Use current client/account evidence when available; missing or stale snapshots
mean remaining allowance is unknown.

Keep the bundled Standard speed unless acceleration is explicitly chosen.
Higher subscriptions and urgent tasks do not authorize buying credits or
changing speed. Astra is an optional escalation for difficult decisions, not a
mandatory root or reviewer. Report unavailable models and explicit fallbacks.

For deliberate tuning, use [routine coding](routine-coding.md),
[fast iteration](fast-iteration.md), or [complex work](complex-repo-work.md).
Compare representative tasks with the [measurement protocol](token-usage.md)
before claiming lower usage or better quality.
