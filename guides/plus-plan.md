# Plus Profile

Plus uses GPT-6 Luna at `max` for the coordinator and `high` for bounded
execution, with a Sol 6.1 reviewer at `medium`. The child cap is two. The higher
root effort is this project's deliberate preference for coordination depth;
it may use more time and tokens than Luna `high`. These settings are starting
points for measurement, not a guarantee of subscription savings.

Select `plus` in either installer. For a manual installation, copy its `codex/`
to project `.codex/`, its `agents/` to project `.agents/`, and merge the managed
instructions from the repository's `AGENTS.md`.

For a global setup, merge these settings into your existing configuration:

```toml
model = "gpt-6-luna"
model_reasoning_effort = "max"
service_tier = "default"

[agents]
enabled = true
max_concurrent_threads_per_session = 2
default_subagent_model = "gpt-6-luna"
default_subagent_reasoning_effort = "high"
```

Copy all five role files to `~/.codex/agents/` and the skill to
`~/.agents/skills/codex-orchestrator/`. Preserve unrelated providers, plugins,
permissions, and user instructions. Start a fresh session after changing files.

Explorer, worker, tester, and researcher pin Luna `high`. Reviewer pins
`gpt-6.1-sol` `medium` with read-only defaults. Invoke it for material risk or
requested independent review; a simple edit does not need a second agent.

Use Sol 6.1 for complex work that exceeds Luna's capabilities, selecting the
model through supported runtime controls rather than merely naming it in a
brief. If you deliberately want Sol worker/tester by default too, install a Pro
bundle as a workload preset even on Plus, subject to account access and budget.
Profile names do not grant or restrict access.

`plus-max-2-subagents` is now a compatibility copy of `plus`.
See [migration](migration.md#subscription-profile-upgrade),
[work modes](model-selection.md#work-modes-are-separate-from-subscription), and
[measurement](token-usage.md).
