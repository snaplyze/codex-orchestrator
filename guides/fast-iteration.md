# Fast Iteration

All [Pro profiles](full-orchestration.md) already use a Sol 6.1 coordinator at
`medium`. To use that coordinator with an existing Plus setup, merge:

```toml
model = "gpt-6.1-sol"
model_reasoning_effort = "medium"
service_tier = "default"
```

Named roles keep their installed settings. A Plus worker still runs Luna;
install a Pro bundle if Sol worker/tester are wanted by default too.
For narrow routine edits, see the [Luna preset](routine-coding.md).

Standard speed is the bundled default. If your task values latency enough to
spend more allowance and your account/model support Fast, use `/fast` in the CLI
or deliberately configure:

```toml
service_tier = "fast"

[features]
fast_mode = true
```

Merge into existing tables rather than creating duplicate `[features]` sections.
Fast consumes included subscription usage at 2.5x Standard; purchased credits at
2x. These are billing multipliers, not promises about task speed. To return to
Standard, turn Fast off in the client and restore `service_tier = "default"`.
Check effective runtime settings if a session overrides configuration.
[Official speed guidance](https://learn.chatgpt.com/docs/agent-configuration/speed)

Pro 500 includes Astra Ultrafast access, but no profile enables it automatically.
Sol 6.1 Ultrafast is not available at launch. See [model selection](model-selection.md).
