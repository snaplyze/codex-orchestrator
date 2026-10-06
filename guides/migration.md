# Migrate to Codex Orchestrator

[Documentation](README.md) · [Getting started](getting-started.md) · [Model selection](model-selection.md)

Use this guide for an existing installation. For a new target, start with
[getting started](getting-started.md). Update configuration, all five role files,
the shared skill, and managed instructions together, then start a new session.

The subscription-profile changes below were introduced in **v0.4.0**. The later
sections also cover the **v0.3.0** repository/skill rename; that rename itself
preserved the then-current model routing and limits.

## Subscription-profile upgrade

The canonical bundle names are `pro-100`, `pro-200`, `pro-500`, and `plus`.
Moving from pre-v0.4.0 bundles changes models and reasoning, not just labels:

| Previous selection | Compatible selection | Change from the older bundle |
|---|---|---|
| `pro` | `pro-100` | Astra root becomes Sol 6.1; child cap 4 becomes 2 |
| `pro-max-2-subagents` | `pro-100` | Astra root becomes Sol 6.1; child cap remains 2 |
| `plus` | `plus` | Luna root stays `max`; child cap 4 becomes 2 |
| `plus-max-2-subagents` | `plus` | Luna root stays `max`; child cap remains 2 |

Pro worker/tester pins move from Sol to Sol 6.1. Every reviewer moves from Astra
`low` to Sol 6.1 `medium`. All profiles select Standard speed; existing runtime
overrides still take precedence. Permission defaults are unchanged.

Legacy textual names are still accepted with a notice, and their directories
remain complete copies of the corresponding canonical bundle. They preserve
path compatibility, not the previous model behavior.

> **Menu choices 3 and 4 now select Pro 200 and Pro 500**, not the former max-2
> variants. Choice 1/default selects Pro 100. Use explicit canonical names in
> scripted input rather than relying on the old menu positions.

Choose `pro-200` or `pro-500` explicitly for three or four concurrent children
with the same Sol/Luna roles. The installer does not detect your subscription.
These caps are project presets, not account entitlements.

For a project upgrade, follow [project installations](#project-installations).
For user-wide settings, follow [manual/global installations](#manual-or-global-installations).
Review custom root/role values before approving replacements. Installer bundles
are not native Codex `--profile` entries. See [model selection](model-selection.md)
for account access, work modes, and explicit fallback guidance.

## Existing clones

Inspect the checkout and remote before updating. For a clean checkout already
on `main` and tracking the intended repository:

```bash
git status --short
git remote -v
git pull --ff-only
```

Stop and preserve local work if the checkout is dirty, detached, or on a different
branch; do not reset or switch it merely to make these commands succeed.
For a checkout still using the previous upstream URL, update `origin` only after
confirming that it should point to this distribution rather than your own fork:

```bash
git remote set-url origin https://github.com/snaplyze/codex-orchestrator.git
```

The checkout directory may keep its current name. Renaming a local folder is
optional and should be done with tools using it closed.
GitHub redirects a renamed repository, but reusing its previous name replaces the
redirect; see [GitHub's rename documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository).

## Project installations

1. Run `sh ./setup.sh` or `pwsh -File ./setup.ps1` from the updated distribution.
2. Select the existing target project and an explicit bundle name.
3. Review and approve the `.codex`, `.agents`, and managed `AGENTS.md` updates.
4. For an old skill installation, replace custom `$astra-orchestrator` references
   with `$codex-orchestrator`.
5. Start a new trusted Codex session in the target and verify the root, roles,
   and skill using the [post-install checks](getting-started.md#5-verify-a-fresh-session).

For Windows PowerShell 5.1, use the command in
[Windows setup](getting-started.md#windows).
Setup adds missing files and replaces only the paths listed at confirmation;
it does not merge custom TOML values within a replaced file.

Setup recognizes the previous `codex-astra-luna-orchestrator:managed` markers
and replaces their block with `codex-orchestrator:managed` markers. Instructions
outside that block are preserved. Malformed or duplicate blocks stop the update
and trigger rollback.

When the legacy `.agents/skills/astra-orchestrator` directory exists and the
`.agents` update is approved, setup moves it to
`.agents/migration-backups/astra-orchestrator`, using a numbered suffix if needed.
This existing installer behavior keeps previous customizations outside skill
discovery. Review and merge any needed customizations into the new
`.agents/skills/codex-orchestrator/SKILL.md`.

Declining a component leaves it unchanged and can leave the upgrade incomplete.
For example, installing the renamed skill while retaining old instruction
references can break invocation. Rerun setup and review the remaining component
updates before starting a new task.

## Failed updates and recovery

Setup journals each managed file and replaces its directory entry with a staged
file. Existing hardlinks therefore keep their original external contents.
On a normal failure or cancellation, rollback restores a file only while it still
matches the installer's recorded state. Concurrent user edits, deletions, and
unrelated new files are preserved. Symbolic links and Windows reparse points are
rechecked before managed writes and rollback. Created directories are removed
only when empty; a legacy archive is not moved over an occupied path.

A conflict or failed restoration prints the retained transaction directory.
Its `entry-N` directories contain `before` (when the target existed) and `after`
copies; `manifest.txt` identifies the target's relative path. Compare the affected
files and merge intended content manually. Do not restore a whole component over
newer work. The warning identifies a retained legacy archive separately.
These copies can contain private configuration; do not commit or publish them.

These safeguards handle normal failures and detected concurrent changes. They
are not recovery after a forced process kill or power loss, nor a guarantee
against a hostile process racing filesystem operations. Avoid editing managed
paths during setup. Verification boundaries are recorded in the
[audit record](../docs/audit-remediation.md).

## Manual or global installations

The project installer does not change global configuration. For a manual global
update, inspect the existing files and use one selected bundle throughout:

1. Compare the bundle's `codex/config.toml` with the active user configuration.
   Merge intended root settings in place; preserve unrelated providers, plugins,
   permissions, MCP servers, and other user settings.
2. Update all five role files in the active user agents directory from the same
   bundle, preserving unrelated roles and reviewing custom changes.
3. Update the skill from `profiles/<bundle>/agents/skills/codex-orchestrator/`.
   With default user paths, its destination is
   `~/.agents/skills/codex-orchestrator/`.
4. If `~/.agents/skills/astra-orchestrator/` still exists, retire it from skill
   discovery after carrying forward required customizations. Keep any retained
   legacy directory outside all discovered `skills` directories.
5. Merge the managed instruction block into `~/.codex/AGENTS.md` using only the
   managed block from this repository's `AGENTS.md`, not its source-maintainer
   section. Preserve user instructions and replace old skill references where
   applicable. Check for an active `AGENTS.override.md` and avoid duplicating
   the block in global and project instructions.
6. Review the resulting diff and syntax, then start a new session and invoke
   `$codex-orchestrator`.

Default user configuration and role paths are `~/.codex/config.toml` and
`~/.codex/agents/`; respect customized active client paths. See the
[global path mapping](getting-started.md#personalglobal-setup).
For a manual project installation, use project `.codex/`, `.agents/`, and
`AGENTS.md` instead. Copying only the new skill leaves old skills and role pins
unchanged; verify the complete configuration rather than treating a copied file
as a completed migration.

## Releases and old tags

`v0.3.0` started the release series under the new repository name. The previous
GitHub releases/tags `v0.1.0` and `v0.2.0` were retired; their changes remain in
Git history and the [changelog](../CHANGELOG.md).

[v0.4.0](https://github.com/snaplyze/codex-orchestrator/releases/tag/v0.4.0) was
published on September 30, 2026. An example of fetching that known release pin is:

```bash
git fetch origin tag v0.4.0
```

Fetching the tag does not switch the checkout or update an installed target.
Choose the intended revision deliberately, preserve local work, and rerun the
installer afterward. Use the documentation at the selected tag for a pinned
installation; consult [Releases](https://github.com/snaplyze/codex-orchestrator/releases)
for later versions. There is no need to delete local historical tags as part of
an ordinary configuration upgrade.
