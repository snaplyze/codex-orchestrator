# Contributing

[Documentation](guides/README.md) · [Development and verification](guides/development.md)

This repository distributes Codex configuration, role instructions, a shared
skill, interactive installers, and a read-only usage report. Keep changes focused
and distinguish shipped behavior from proposed improvements.

## Report a problem

Search [existing issues](https://github.com/snaplyze/codex-orchestrator/issues)
before opening a report. Use the bug or documentation form and include the
revision or release, affected file/command, expected result, actual result, and
a minimal reproduction. Installer reports should identify the OS, shell engine,
selected bundle, and whether the target was new or already configured.

Share only sanitized excerpts. Do not publish credentials, private configuration,
raw rollout logs, prompts, or identifiable project paths. Reproduce installer
failures in disposable targets, not a real user's project. A model-access error
or stale quota snapshot is not, by itself, a defect in the distribution.

## Make a change

Read [AGENTS.md](AGENTS.md), the [development guide](guides/development.md), and
any relevant [audit checkpoint](docs/audit-remediation.md) before editing.
Preserve user changes and keep the diff limited to the agreed scope.

Use `main` as the pull request base. Describe the problem, approach, changed
behavior, verification evidence, and anything not tested. For a larger behavior
or topology change, establish scope in an issue first. A typo correction does not
need a separate planning document or mandatory issue.

Models, reasoning, permissions, and caps belong in profile TOML. Shared delegation
policy belongs in the identical bundled skills; source-maintainer instructions
stay outside the distributed `AGENTS.md` block. Do not change those settings as a
side effect of a documentation cleanup.

## Verify the result

For implementation or profile changes, run the focused regressions and applicable
full checks from the distribution root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -v
sh -n setup.sh
shellcheck setup.sh
```

See [development](guides/development.md#local-checks) for Python requirements,
PowerShell engine selection, temporary targets, and platform boundaries.
An unavailable tool or platform is **not run**, not a pass. Do not change global
settings or disable a test to obtain green output.

For documentation-only changes, check relative links and heading anchors, render
Markdown, and compare every command, profile table, and behavioral claim with the
implementation. Parse changed TOML examples or issue-form YAML when applicable.
Keep existing CI checks enabled and report the result for the actual revision.
Do not infer account/model access from static checks or spend model credits merely
to validate wording.

## Keep documentation maintainable

The [documentation index](guides/README.md) is the entry point; link task-specific
detail rather than growing the root README. Preserve existing file paths and
heading anchors when possible, and update inbound links when moving material.
Keep historical releases and verification results historical. Add user-visible
changes under **Unreleased** in [CHANGELOG.md](CHANGELOG.md); only a published
release receives a release version and date.

Do not commit local settings, generated reports, screenshots used only for review,
caches, temporary test targets, or raw execution logs. Keep planning and audit
evidence in the existing record instead of creating competing roadmaps.
