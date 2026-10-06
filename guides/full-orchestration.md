# Pro 100, Pro 200, and Pro 500

[Documentation](README.md) · [Getting started](getting-started.md) · [Usage](usage.md)

All three Pro profiles use GPT-6.1 Sol for coordination, implementation, testing,
and ordinary independent review. Luna handles exploration and research. Astra is
an escalation for difficult decisions, not a permanent coordinator.

| Installer choice / directory | Concurrent children |
|---|---:|
| Pro 100 / `profiles/pro-100` | 2 |
| Pro 200 / `profiles/pro-200` | 3 |
| Pro 500 / `profiles/pro-500` | 4 |

These are project presets, not OpenAI's account limits. A larger cap is useful
only for independent work; use fewer agents whenever the task permits.

For example, Pro 100 ships these root settings:

```toml
model = "gpt-6.1-sol"
model_reasoning_effort = "medium"
service_tier = "default"

approval_policy = "on-request"
sandbox_mode = "workspace-write"

[agents]
enabled = true
max_concurrent_threads_per_session = 2
default_subagent_model = "gpt-6-luna"
default_subagent_reasoning_effort = "high"
```

Pro 200 and Pro 500 change the child cap to 3 and 4. Copy all five role files
from the same profile too:

| Roles | Model | Effort | Sandbox |
|---|---|---|---|
| explorer, researcher | `gpt-6-luna` | `high` | read-only |
| worker, tester | `gpt-6.1-sol` | `medium` | workspace-write |
| reviewer | `gpt-6.1-sol` | `medium` | read-only |

Roles are available specialists, not a mandatory five-stage pipeline. A worker
can run its own tests. Use a separate reviewer when the change warrants another
assessment. Its model stays pinned even if you override generic child defaults.

Setup copies each bundle without rewriting configuration. For a manual install,
copy its `codex/` into project `.codex/`, its `agents/` into project `.agents/`,
and merge the managed instructions. For global use, merge root settings and copy
roles, skill, and managed instructions while preserving unrelated configuration.
See the [complete global setup](getting-started.md#personalglobal-setup).

The legacy `pro` and `pro-max-2-subagents` bundles now match Pro 100. See
[migration](migration.md#subscription-profile-upgrade) before upgrading an old
Astra-based setup. For work modes, subscription caveats, and escalation, see
[model selection](model-selection.md) and [complex work](complex-repo-work.md).
