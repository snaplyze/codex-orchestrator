# Documentation

[Repository overview](../README.md) · [Contributing](../CONTRIBUTING.md)

Codex Orchestrator provides orchestration profiles with specialized agents,
adaptive delegation, and project setup for focused and multi-agent coding
workflows. Start with installation and a first task; use the reference guides
for configuration and verification details.

## Start here

| Goal | Guide |
|---|---|
| Install into a project and verify discovery | [Getting started](getting-started.md) |
| Write a task, choose roles, and control delegation | [Using the orchestrator](usage.md) |
| Update an existing installation or old profile | [Migration](migration.md) |
| Diagnose setup, missing skills, or unchanged settings | [Troubleshooting](getting-started.md#troubleshooting) |
| Install manually at user scope | [Personal/global setup](getting-started.md#personalglobal-setup) |

## Profiles and tuning

| Question | Reference |
|---|---|
| Which models, efforts, and child caps are bundled? | [Model selection and subscription profiles](model-selection.md) |
| What is in the Pro bundles? | [Pro configuration](full-orchestration.md) |
| What is in the Plus bundle? | [Plus configuration](plus-plan.md) |
| How do I lower root effort for routine work? | [Routine coding](routine-coding.md) |
| When should I escalate difficult work? | [Complex repository work](complex-repo-work.md) |
| How do I make an explicit speed trade-off? | [Fast iteration](fast-iteration.md) |
| How do I measure a task without confusing tokens with billing? | [Token usage and measurement](token-usage.md) |

`plus` and `pro-*` are installer bundles. `Economy`, `Normal`, and `Thorough`
are instructions for a task. Neither is a native Codex `--profile` entry created
by this repository. See [the three configuration layers](usage.md#profiles-modes-and-runtime-settings).

## Maintain the distribution

[Contributing](../CONTRIBUTING.md) explains reports and pull requests.
[Development and verification](development.md) covers commands, invariants,
and native-platform versus live-account validation.

[Changelog](../CHANGELOG.md) records user-visible changes;
[GitHub releases](https://github.com/snaplyze/codex-orchestrator/releases) provide
published versions. The [audit record](../docs/audit-remediation.md) owns engineering
findings and dated verification checkpoints, not the first-time setup procedure.
Older checkpoints describe their own revision; they are not proof that a later
change passed the same checks.

## Sources of truth

| Subject | Authority |
|---|---|
| Bundled models, efforts, permissions, and caps | [`profiles/`](../profiles/) TOML files |
| Shared delegation behavior | [Bundled skill](../profiles/pro-100/agents/skills/codex-orchestrator/SKILL.md), identical in all seven bundles |
| Installation and update behavior | [`setup.sh`](../setup.sh), [`setup.ps1`](../setup.ps1), and installer regressions |
| An already running session | Its loaded configuration, role definitions, and client overrides |
| Model access and remaining allowance | The actual account/client, not an installer label or a benchmark sample |

Official client behavior is documented in OpenAI's
[subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents)
and [skill guide](https://learn.chatgpt.com/docs/build-skills).
Time-sensitive model and subscription references are kept in
[model selection](model-selection.md), with their verification date and caveats.
