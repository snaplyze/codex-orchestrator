# Model Selection and Subscription Profiles

Official documentation checked on September 30, 2026. These are configuration
presets, not measured quality rankings or guarantees of account access. Model
availability and supported reasoning depend on the client, account, and workspace.

## Models and routing

OpenAI recommends `gpt-6.1-sol` for complex coding and agentic work when available,
and `gpt-6-luna` for focused, repeatable work. GPT-6.1 Sol offers near-Astra
performance at lower cost; keep Astra for the most demanding work.
[Official model guidance](https://learn.chatgpt.com/docs/models)

The exact new ID is `gpt-6.1-sol`. Its launch includes Plus, Pro, Business,
Enterprise, and Edu in supported clients, subject to rollout. Standard and Fast
are available; Sol 6.1 Ultrafast is not available at launch.
[Availability](https://learn.chatgpt.com/docs/models#gpt-6.1-sol)

| Profile | Root | Worker / tester | Reviewer | Child cap |
|---|---|---|---|---:|
| `plus` | Luna `max` | Luna `high` | Sol 6.1 `medium` | 2 |
| `pro-100` | Sol 6.1 `medium` | Sol 6.1 `medium` | Sol 6.1 `medium` | 2 |
| `pro-200` | Sol 6.1 `medium` | Sol 6.1 `medium` | Sol 6.1 `medium` | 3 |
| `pro-500` | Sol 6.1 `medium` | Sol 6.1 `medium` | Sol 6.1 `medium` | 4 |

Explorer, researcher, and generic children use Luna `high` in every profile.
The cap excludes the root and is a ceiling, not a target. All profiles select
Standard speed (`service_tier = "default"`). The three Pro profiles deliberately
share role quality: a higher subscription supports more independent work, not
an obligation to keep Astra running throughout every task.

Sol 6.1 `medium` is this repository's balanced starting preset. OpenAI recommends
starting with the client default for Sol 6.1, `high` for Luna, and `low` for Astra.
Increase reasoning for demonstrated difficulty. The Sol 6.1 API supports `low`,
`medium`, `high`, `xhigh`, and `max`; client Ultra is a separate orchestration
mode. Use only values
advertised by the active client/model.
[Subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[Sol 6.1 model specification](https://developers.openai.com/api/docs/models/gpt-6.1-sol)

Plus deliberately uses Luna `max` for the root to favor coordination depth;
its Luna children remain at `high`. This is a project preference, not OpenAI's
recommended starting effort or a demonstrated economy win. The optional
[routine preset](routine-coding.md) lowers root effort to `high`.

Independent review means a separate assessment of the actual diff and evidence;
it does not require a different model family. Use an Astra assessment for difficult
security, data-integrity, architecture, or unresolved reasoning issues. Named
roles remain pinned: changing the root or generic child default does not change
the reviewer. A fixed runtime role cannot be changed by writing another model
name in its task message. See [complex work](complex-repo-work.md).

## Subscription facts and limits

OpenAI offers Pro 100, Pro 200, and Pro 500 at $100, $200, and $500 USD/month.
New Pro 200 subscriptions have a lower included allowance than the previous
offer. Eligible existing subscribers keep their previous allowance through
October 29, 2026 while subscribed. Among Pro plans, only Pro 500 includes Astra
Ultrafast; buying credits on Pro 100/200 does not unlock it at launch.
[Official Pro conditions](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)

Codex and ChatGPT Work share usage. Model, reasoning, context, tool use, caching,
and other account activity affect consumption. Check `/status` or the usage
dashboard for the actual windows, remaining limits, and reset times of your
account. This repository does not encode an assumed 5x/10x/25x allowance, infer
your subscription from its price, or convert API prices into included tasks.
[Official pricing and usage](https://learn.chatgpt.com/docs/pricing)

The rollout documentation is not fully synchronized as of September 30: Pricing
says Pro has no five-hour limit, while the
[Help Center usage guide](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
still shows a five-hour table with older Pro 5x/20x labels. Do not turn either
table into fixed runtime assumptions; use the windows actually shown for the
account. The orchestration policy works with whichever limit windows are present.

Fast consumes included usage at 2.5x Standard; Astra Ultrafast at 8x. Purchased
credit multipliers differ. Keep Standard as the default even on Pro 500 and
choose acceleration explicitly when latency justifies its cost.
[Speed and billing](https://learn.chatgpt.com/docs/agent-configuration/speed)

## Work modes are separate from subscription

These are instructions to the orchestrator, not additional installer profiles
or new TOML keys. Say which mode you want in the task; the default is normal.

| Mode | Routing behavior |
|---|---|
| Economy | Root handles small tasks; start with one bounded delegate when useful, reuse its context, and avoid speculative parallel exploration. |
| Normal | Use configured roles and only the independent workstreams needed, within the cap. |
| Thorough | Add independent checks for material risk, raise reasoning or use Astra where justified; keep the cap and explicit speed choice. |

All modes preserve necessary tests, user-requested review, and completion criteria.
Economy changes overhead, not the definition of done. The skill follows available
quota evidence without inventing a remaining budget; no automatic quota reader,
model switcher, or billing controller is shipped. A concurrency cap alone does
not limit total agents or token use over the task.

## Upgrade and compatibility

1. Choose `pro-100`, `pro-200`, `pro-500`, or `plus` in either installer.
2. Update configuration, all five role files, the shared skill, and managed
   instructions together. Preserve unrelated user configuration.
3. Start a new session in the trusted target project. Check `/model` and the
   loaded roles; an already running session retains its runtime definitions.
4. Compare representative tasks with the [measurement protocol](token-usage.md).
   Static tests and a model listing do not establish quality or live account access.

The legacy names `pro` and `pro-max-2-subagents` map to `pro-100`;
`plus-max-2-subagents` maps to `plus`. Their copy-ready directories are retained
with identical contents to the canonical profiles. These names preserve paths,
not the old Astra routing or four-child Plus cap. Menu numbers 3 and 4 now select Pro 200
and Pro 500; automation should use explicit profile names.
See [migration](migration.md#subscription-profile-upgrade).

## Availability and fallback

If a model is rejected, report its ID and check the active picker and workspace
access. Metadata does not grant access. Use a confirmed available fallback within
the user's constraints, disclose it, and use an effort that fallback supports.
Do not silently downgrade roles or rewrite global settings. GPT-6 Sol can be a
temporary alternative to Sol 6.1 only where confirmed available; update every
affected pin, including the reviewer, when deliberately changing installed files.
