# Routine Coding

[Documentation](README.md) · [Getting started](getting-started.md) · [Usage](usage.md)

The [Plus profile](plus-plan.md) uses Luna `max` for coordination. For clear,
bounded work, deliberately lower the root to `high` with this optional preset:

```toml
model = "gpt-6-luna"
model_reasoning_effort = "high"
service_tier = "default"
```

Merge only these keys into your configuration. Installed named roles retain their
own models: changing the root does not move Pro worker/tester to Luna or change
the Sol 6.1 reviewer. The skill uses the effective settings.

Handle small edits in the root. For a bounded delegate, provide the needed paths,
constraints, and checks; return a short result instead of copying raw logs.
Economy mode reduces coordination overhead while preserving necessary validation.
Try lower reasoning only when representative checks show it is sufficient.

See [work modes](model-selection.md#work-modes-are-separate-from-subscription).
