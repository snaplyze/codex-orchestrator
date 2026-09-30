# Complex Repository Work

Start with the selected [Pro profile](full-orchestration.md). Raise Sol 6.1
reasoning for demonstrated difficulty before treating every complex task as an
Astra task:

```toml
model = "gpt-6.1-sol"
model_reasoning_effort = "high"
service_tier = "default"
```

For especially difficult architecture, security, data-integrity, or sustained
reasoning work, deliberately select an available Astra root or bounded reviewer.
An initial root override is:

```toml
model = "gpt-6-astra"
model_reasoning_effort = "low"
service_tier = "default"
```

Raise Astra effort when the task needs it. Root overrides do not change the
named Sol 6.1 worker/tester/reviewer or the Luna explorer/researcher.

For one Astra assessment, the orchestrator must use a supported configurable
spawn role, explicitly selecting the model and effort and carrying the reviewer
instructions and read-only boundary. Use a supported read-only sandbox override
where available and preserve read-only instructions even if the client inherits
broader parent permissions. Fixed role definitions can override spawn
settings: do not claim that an Astra name in a task brief changes the model.
If the active tools cannot select the intended model, report that limitation.
For a persistent reviewer override, deliberately update its TOML model and effort
and restart; do not rewrite installed/global settings just to delegate one task.

Use thorough mode to add necessary independent validation, not a mandatory
pipeline. Keep the configured child cap and use Standard speed unless acceleration
was explicitly chosen. Ultra adds proactive delegation and is not enabled by
these presets. Compare [measured runs](token-usage.md) before claiming savings
or quality improvements.
