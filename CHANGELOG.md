# Changelog

## Unreleased

- Rework the README as a shorter project overview with CI/release/license badges,
  a quick start, a profile comparison, and links to task-specific documentation.
- Add a documentation index, installation/troubleshooting walkthrough, usage
  examples, contributor guidance, and focused GitHub issue/PR templates.
- Clarify update and manual-install instructions and record the published v0.4.0
  status without rewriting historical verification evidence. Runtime behavior,
  profile settings, shared skills, and CI configuration are unchanged.

## 0.4.0 — 2026-09-30

- Add Pro 100, Pro 200 and Pro 500 bundles with a GPT-6.1 Sol coordinator,
  Sol implementation/testing/review, Luna exploration and child caps of 2/3/4.
- Keep Plus coordination on Luna max, with Luna high children, a two-child cap,
  and Sol 6.1 independent review.
  Select Standard speed in every profile; reserve Astra for justified escalation.
- Add economy/normal/thorough routing guidance, cumulative delegation controls,
  and handling for unknown/stale quota evidence without an automatic quota reader.
- Update both installers and preserve legacy profile names and copy-ready paths.
  Legacy Pro names now select Pro 100; Plus max-2 selects Plus. Numeric choices
  3/4 now mean Pro 200/500; scripted callers should use explicit profile names.
- Keep permission defaults, managed-file replacement and rollback boundaries.
  Update profile/installer regressions and migration/measurement documentation.
- Clarify installer bundles versus native CLI profiles, actual launch and role
  invocation, custom-role precedence and live permission overrides. Document the
  official sources' quota-window discrepancy instead of assuming a fixed window.

Upgrade configuration, all roles, skill and managed instructions together, then
restart Codex. These presets are not benchmarked savings or account-access
claims. See the [migration guide](guides/migration.md#subscription-profile-upgrade)
and [verification checkpoint](docs/audit-remediation.md#documentation-review-and-v040-release--2026-09-30).

## 0.3.1 — 2026-09-26

- Stage managed-file replacements and roll back only installer-owned changes.
  Preserve external hardlinks and concurrent edits, with recovery copies for conflicts.
- Keep maintainer instructions out of fresh project installations and carry task
  authority explicitly through delegation briefs and role instructions.
- Show usage scan scope, malformed-input diagnostics, quota windows and distinct
  threads/rollout segments.
- Test Linux, macOS, PowerShell 7 and Windows PowerShell 5.1; enforce identical
  shared skill policy across profiles.
- Add audit/development documentation and clarify benchmark controls.
  Model routing and permission defaults remain unchanged.

### Upgrade

Update your checkout, rerun setup for project installations and approve the
configuration, skill and instruction updates, then restart Codex. For global
installations, follow the [migration guide](https://github.com/snaplyze/codex-orchestrator/blob/v0.3.1/guides/migration.md#manual-or-global-installations).
JSON consumers should use `thread_count` and `segment_count` and inspect
`scope` and `diagnostics`.

Validation: 56 tests pass in each of four native CI jobs.

## 0.3.0 — 2026-09-26

- Rename the project and repository to Codex Orchestrator at
  `snaplyze/codex-orchestrator`.
- Rename the skill to `codex-orchestrator` across all four profiles, installation
  paths, agent instructions, and usage examples.
- Migrate legacy managed instructions in place and archive the previous skill
  outside `skills`, preserving custom files and existing backups.
- Reject malformed or duplicate instruction blocks and restore component changes
  if installation fails.
- Retire the previous GitHub releases and tags. Preserve the project history and
  the existing model routing, permissions, and concurrency limits.

### Upgrade

Update your clone's `origin` to
`https://github.com/snaplyze/codex-orchestrator.git`, pull the release, and rerun
setup. Approve `.codex`, `.agents`, and managed `AGENTS.md` updates together before
starting a new Codex session. Replace custom `$astra-orchestrator` references with
`$codex-orchestrator`. Old references can refer to the retired skill.

For global installations, move the old skill outside discovered skill directories
and copy its renamed replacement. Update scripts pinned to `v0.1.0` or `v0.2.0`
to use `v0.3.0`. See the [migration guide](https://github.com/snaplyze/codex-orchestrator/blob/v0.3.0/guides/migration.md) for exact paths,
backup behavior, and partial-update recovery.

## 0.2.0 — 2026-09-22

- Migrate Plus roots and Luna subagents to GPT-6 Luna; use `high` for Luna
  subagents and retain `max` for Plus coordination.
- Route Pro implementation and testing to GPT-6 Sol at `medium`; retain Astra
  coordination/review and use Luna for exploration/research.
- Preserve all four profile names, five role names, permission defaults, and
  four/two-child concurrency limits.
- Consolidate duplicated orchestration rules into a shorter skill that reads
  effective settings, respects thread limits, and reports model fallbacks.
- Correct installer banners and document rollout, migration, optional Sol
  coordination, and model-specific reasoning choices with official sources.
- Add regression coverage for role models, reasoning, sandbox defaults,
  complete installation output, and upgrades preserving unrelated files.

Update the config, all role files, and the skill together, then start a new Codex
session. Account access depends on the model rollout. These presets have not been
benchmarked against the previous release; the historical token sample remains
unchanged. See [model selection and migration](guides/model-selection.md).

## 0.1.0 — 2026-09-18

- Sync upstream Pro/Plus profiles and add max-2 variants.
- Harden POSIX and PowerShell installers, managed instructions, and rollback.
- Improve token-usage parsing and add Ubuntu/Windows CI coverage.
