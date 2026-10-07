# Research implementation and evidence

This repository supplies the runtime metadata gate. The companion
[rajesamp/sentinel-tpd-research](https://github.com/rajesamp/sentinel-tpd-research)
supplies the manuscript, evaluation harness, authored fixtures, source acquisition
pins, raw observations and derived tables. A reference to a paper or a proposed
equation does not mean its algorithm is implemented in this library.

## Exact baseline and current alignment

The manuscript's immutable baseline is
[`5ce5d56e57a0acd092435fca5d89b78d0b39ee7b`](https://github.com/rajesamp/sentinel-tpd/tree/5ce5d56e57a0acd092435fca5d89b78d0b39ee7b),
package version 2026.8.0. On 2026-10-07 the current main revision was this exact
commit, and all 12 files in the research
[vendor manifest](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/vendor/manifest.json)
matched SHA-256 values. This update corrects README scope and adds research links;
it does not change runtime modules or tests and does not constitute a new experiment.
The original 11 non-README files and derived runtime-module inventory are checked
by `python3 tools/check_research_alignment.py` in CI. Added or changed runtime
modules fail this alignment check. A failure calls for a new review and study
revision where necessary; changing a hash alone is not scientific re-evaluation.

The complete
[alignment record](https://github.com/rajesamp/sentinel-tpd-research/blob/codex/sentinel-tpd-paper/research/upstream-alignment.json)
separates the checked pre-update revision, documentation revision and unchanged
runtime-file hashes. Future behavior changes require a new comparison and new
scored evidence before claiming that this paper evaluates them. Original frozen
observations must not be overwritten.

## Where each paper material is stored

| Material | Reference under `rajesamp` |
|---|---|
| Author and anonymous papers, editable sources and reviewer package | [Version 0.1.1 release](https://github.com/rajesamp/sentinel-tpd-research/releases/tag/v0.1.1) |
| Every figure, table, equation, section and all 34 reference keys | [Paper evidence index](https://github.com/rajesamp/sentinel-tpd-research/blob/codex/sentinel-tpd-paper/research/paper-evidence-index.md) |
| Exact evidence paths, revisions and hashes | [Machine-readable manifest](https://github.com/rajesamp/sentinel-tpd-research/blob/codex/sentinel-tpd-paper/research/paper-evidence-manifest.json) |
| Ten signals, scanner, registry and audit | [Pinned runtime modules](https://github.com/rajesamp/sentinel-tpd/tree/5ce5d56e57a0acd092435fca5d89b78d0b39ee7b/sentinel_tpd) |
| 70 authored cases and 15 lifecycle traces | [Public data](https://github.com/rajesamp/sentinel-tpd-research/tree/d62ccf1707713b31829a1a480c54fb789ec75c15/data) |
| 47 external source templates and declared projections | [Source manifest](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/data/source-manifest.json) and [provenance](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/research/corpus-provenance.md) |
| Raw case/lifecycle/timing observations, two sessions | [Session 1](https://github.com/rajesamp/sentinel-tpd-research/tree/d62ccf1707713b31829a1a480c54fb789ec75c15/results/frozen-001) and [session 2](https://github.com/rajesamp/sentinel-tpd-research/tree/d62ccf1707713b31829a1a480c54fb789ec75c15/results/frozen-002) |
| Protocol, five original workload levels and cost boundary | [Measurement protocol](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/research/measurement-protocol.md) |
| Original patterns, studies and unverified historical numbers | [Original coverage crosswalk](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/research/original-coverage.md) |
| Bibliography and verification limits of third-party sources | [References](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/manuscript/references.bib), [audit](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/research/reference-audit.md), [source dossier](https://github.com/rajesamp/sentinel-tpd-research/blob/d62ccf1707713b31829a1a480c54fb789ec75c15/research/sources.json) |
| Replay and traceability verification | [Reproduction instructions](https://github.com/rajesamp/sentinel-tpd-research#reproduce) and [traceability verifier](https://github.com/rajesamp/sentinel-tpd-research/blob/codex/sentinel-tpd-paper/tools/audit_traceability.py) |

Third-party publications remain attributed primary-source links, with bibliographic
metadata and review scope in the research repository. External payloads are not
redistributed: the pinned acquisition procedure verifies them locally. The original
uploaded similarity/manuscript PDF is not republished; the derived coverage ledger
preserves its research questions and flags unsupported original numbers.

## What is implemented

Ten lexical rules produce maximum severity; the default M3 threshold controls
admission. The scanner reads selected name/description/schema text fields.
Invocation checks compare the name/description/input-schema projection and enforce
registry quarantine. Audit records are hash-linked and tamper-evident relative to
the retained chain. The host must honor decisions and supply authorization,
provider binding, execution isolation and other runtime controls.

No weighted semantic risk, name-distance detector, model-based classifier, complete
request authorization, general server-behavior observer or OS sandbox is implemented
by adding these research references. The paper's proposed equations remain explicitly
unimplemented. The separate dispatch-conformance artifact studies a different
contract and its results are not pooled into this paper.
