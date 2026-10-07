# SENTINEL-TPD

**Content-level trust gate for MCP tool metadata.**

Access-control layers (mTLS, ACLs, gateways) answer *who may call which tool*.
SENTINEL-TPD answers a different question: **can the tool's own description be
trusted to steer the agent?** A tool's description and schema enter the model's
context verbatim — they are instructions to the model wearing the costume of
documentation. This library treats them as **untrusted input** (instruction-
hierarchy Layer 4) from the moment they are registered.

Grounded in the MCP threat-modeling literature: tool poisoning scores
**DREAD 46.5/50**, the highest-severity client-side MCP threat (Huang et al.,
arXiv:2603.22489).

## What it does

Two enforcement points, both fail-closed, both audit-logged:

1. **`TOOL_REGISTERED` gate** — the tool's name, description, and nested
   input-schema `description`/`title` strings are scanned against a deterministic
   signal catalog. The verdict is maximum matched severity. At the default
   threshold, severity ≥ M3 ⇒ deny. The integrating host must honor that verdict
   before exposing metadata to the model or dispatching a call.
2. **Call-time decision-path check** — admitted metadata is fingerprinted
   (SHA-256 over canonical JSON). At invocation, the current metadata is
   re-fingerprinted and diffed. A covered-field mutation (**rug pull**) ⇒ deny +
   quarantine until a clean re-scan on the next `tools/list` refresh.
   Unknown tool ⇒ **default-deny**.

Every allow/deny/mutation event lands in a **hash-chained audit log**: each
entry embeds the SHA-256 of the previous one, so editing any record breaks
every downstream hash.

## Signal catalog (v2026.8)

| Signal | Sev | Tactic |
|---|---|---|
| `TPD-IMPERATIVE-TAG` | M4 | `<IMPORTANT>`/`<system>`-style markup addressing the model |
| `TPD-CONCEALMENT` | M4 | "do not tell the user" — secrecy from the operator |
| `TPD-EXFIL-DEST` | M4 | send/post/forward + embedded URL or email |
| `TPD-DIRECT-MODEL-ADDRESS` | M3 | "you must…", "ignore previous…" |
| `TPD-PRIORITY-CLAIM` | M3 | "takes precedence over all other instructions" |
| `TPD-SENSITIVE-PATH` | M3 | `~/.ssh`, `id_rsa`, `.env`, API keys, seed phrases |
| `TPD-CROSS-TOOL-STEER` | M3 | shadowing: modifies how *other* tools are used |
| `TPD-PARAM-SMUGGLE` | M3 | "include the entire conversation in this field" |
| `TPD-ENCODED-BLOB` | M2 | long base64-like payloads in metadata |
| `TPD-URGENCY` | M1 | pressure framing aimed at the model |

Default-deny threshold: **M3**. Configurable per registry.

## Quickstart

```python
from sentinel_tpd import ToolRegistry

reg = ToolRegistry()

verdict = reg.register(tool_dict)          # TOOL_REGISTERED gate
if verdict.allowed:
    decision = reg.check_invocation(tool_dict)   # call-time diff
    if decision.allowed:
        ...  # metadata gate passed; host authorization and execution controls still apply

reg.rescan_on_refresh(new_tools_list)      # on tools/list change

ok, detail = reg.audit.verify()            # audit chain integrity
```

Zero runtime dependencies — Python 3.11+ stdlib only. Run tests with either:

```bash
python -m unittest discover -s tests
pytest
```

## Design decisions

- **Deterministic classifier, no LLM in the loop.** A model inside the trust
  boundary you are defending is a recursion, not a defense. Regex/heuristic
  signals are auditable, testable, and explainable per-deny.
- **Fail-closed registry decisions for its defined checks.** Missing/invalid
  names, unknown tools, quarantine and covered metadata mutation deny. Complete
  input-schema validation is not implemented; a null schema can pass. M1/M2
  matches may allow at the default M3 threshold. See the research probes below.
- **Framework-agnostic.** Takes plain dicts, returns verdicts. No MCP client
  dependency; wire it into any client at the two enforcement points.

## Honest limitations

- The signal catalog is a **first-line, precision-biased filter** — it will
  not catch novel phrasings, non-English payloads, or semantic attacks that
  avoid the listed patterns. Recall is intentionally traded for explainable
  denies. Pair with runtime egress controls and least-privilege tool scopes.
- The audit chain is **tamper-evident, not tamper-proof**: an attacker with
  write access to the log can rewrite the whole chain. Real WORM guarantees
  require append-only storage with retention lock (e.g. GCS bucket retention
  policy) — that's a deployment concern this library deliberately leaves to
  the deployment.
- Fingerprinting covers `name`, `description`, and `inputSchema`. Server
  behavior changes that don't touch metadata are out of scope here.
- Top-level `title`, `annotations`, `outputSchema`, tool responses and provider
  identity are outside this fingerprint projection. There is no semantic
  name-similarity or provider-authentication detector. A clean refresh can recover
  quarantine; direct registration does not clear it.

## Research paper and reproducible evidence

The research companion is
[rajesamp/sentinel-tpd-research](https://github.com/rajesamp/sentinel-tpd-research).
[Research alignment and evidence links](docs/research.md) explains the separation
between this implementation and the paper's assay, fixtures and recorded results.

The paper evaluates exact revision
[`5ce5d56e57a0acd092435fca5d89b78d0b39ee7b`](https://github.com/rajesamp/sentinel-tpd/tree/5ce5d56e57a0acd092435fca5d89b78d0b39ee7b).
The live repository matched all 12 pinned files on 2026-10-07 before this
documentation-only update. Runtime modules, package version and upstream tests
remain unchanged. The
[paper evidence index](https://github.com/rajesamp/sentinel-tpd-research/blob/codex/sentinel-tpd-paper/research/paper-evidence-index.md)
maps every figure, table, equation and all 34 bibliography entries to GitHub
evidence and attributed primary sources.

The study records local inert enqueues: source attack-label prevention 17/27 and
benign enqueues 20/20; authored challenge prevention 4/26 and benign enqueues
37/44. All three source shadowing templates are missed. These are bounded
metadata outcomes, not real-agent attack success or safe remote execution.
Weighted semantic risk, behavior monitoring and process isolation remain
unimplemented proposals or external host responsibilities. See the manuscript's
projection, labeling and validity limits before interpreting the counts.

## Relation to the SENTINEL family

SENTINEL-TPD extends the author's broader agent-runtime-security posture
(instruction hierarchy, M0–M4 severity tiers, default-deny on missing
contract, fail-closed on ambiguity) to the client-side MCP tool-metadata
trust gap.

## License

MIT — see [LICENSE](LICENSE).

## Author

Rajeshkumar Sampathrajan · [github.com/rajesamp](https://github.com/rajesamp)
