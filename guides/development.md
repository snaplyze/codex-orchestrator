# Development and verification

This repository distributes ready-to-copy Codex configuration, not a running
service. Profile TOML owns model/effort/permission settings; the identical skills
own shared delegation policy. Installers copy a selected bundle and manage only
their instruction block in the target project's AGENTS.md. Runtime overrides
remain authoritative for an already running Codex session.

The current work queue, evidence and acceptance criteria are in the
[audit remediation plan](../docs/audit-remediation.md). Read its latest checkpoint
before resuming work. Keep implementation claims separate from planned changes.

## Local checks

Use Python 3.12 or newer for the supported unittest matrix, a POSIX shell for
setup.sh, and PowerShell for setup.ps1. `tomllib` is in the standard library
since Python 3.11; the repository validates on 3.12. No Python packages are
required for the repository test suite.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -v
sh -n setup.sh
shellcheck setup.sh
```

Tests create temporary targets; never use a real user's project to reproduce a
destructive installer failure. Keep synthetic rollout logs separate from private
Codex sessions. Do not publish logs containing prompts, credentials or private
paths. Use targeted tests while editing, then the full suite before completion.

The workflow is configured for Python 3.12 on Linux/macOS with sh and on Windows
with separate pwsh and powershell jobs. It runs ShellCheck on Linux. The audit
remediation plan records which revision has actually passed this matrix; changing
the YAML does not establish a native-platform pass. A local Linux PowerShell pass
is not native Windows evidence.

Select an installed test engine explicitly with `CODEX_INSTALLER_TEST_ENGINE`
(`sh`, `pwsh` or `powershell`). `CODEX_INSTALLER_TEST_EXECUTABLE` can point to a
portable executable of that engine. A requested unavailable engine must fail
instead of silently skipping its suite.

The harness clears inherited `PSModulePath` only in PowerShell test children, so
each runtime loads its own built-in modules. Python launched from PowerShell 7
otherwise passes incompatible module paths to Windows PowerShell 5.1, as described
in [Microsoft's module-path guidance](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_psmodulepath#starting-windows-powershell-from-powershell-7).

For example, on a Linux host with portable PowerShell:

```bash
CODEX_INSTALLER_TEST_ENGINE=pwsh \
CODEX_INSTALLER_TEST_EXECUTABLE=/absolute/path/to/pwsh \
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_installers -v
```

Failure-injection fixtures execute temporary helpers. If the system temporary
directory is mounted `noexec`, create a private temporary directory on an
executable filesystem and set `TMPDIR` to it for the tests. Do not disable the
failure tests or change a system mount to obtain a pass.

## Codex integration smoke check

Static tests verify the bundled values; they do not establish account access.
For a supported-client update, record the CLI version, install each profile into
a disposable project, open it as trusted using the normal Codex trust flow, and
inspect the loaded root settings, five named roles and codex-orchestrator skill.
Use the client settings/picker to check advertised models; a paid model call is
not required for discovery. Restart after changing configuration. Record each
unverified platform/account separately; do not change global config for a test.

Historical validation covered CLI 0.155.1 and inspected 0.157.1 protocol sources.
For the subscription-profile update, use its separate checkpoint in the audit
record for current validation and explicit live-access limits. Neither TOML
parsing nor installer checks establish that an account can run the pinned models.

## Change boundaries

Keep the shared skill identical in all seven bundles. The canonical profiles are
Plus and Pro 100/200/500. Compatibility bundles `pro` and
`pro-max-2-subagents` must be byte identical to `pro-100`;
`plus-max-2-subagents` must be byte identical to `plus`. Canonical Pro profiles
share roles and differ in their child cap (2/3/4). These caps are presets, not
subscription entitlements. Do not replace the profile layout with a generator
without a concrete need. Preserve user instructions outside managed
markers and unrelated target files. Treat install rollback, file links and
concurrent user writes as data-integrity boundaries.

Historical changelog entries remain historical. Update user-facing behavior
docs when code lands; record current checks and remaining limits in the plan.
Publishing, production actions and model charges require applicable authority.
