# 200PlusHormoneBrain

An LLM that runs on a live neuroendocrine simulation — 215 chemicals, a
full brain-region tree, and a memory system whose recall shifts with the
model's hormonal state. Built on Gemma 4 E2B IT, served with vLLM,
trained with Unsloth.

> **Status: early development.** The structure is in place, the base
> model is published, the loop and UI are the next milestone. See
> [Status](#status) below for what works and what doesn't yet.

---

## What this is

Most "AI emotion" projects are one of three things: sentiment
classification, prompt engineering, or a single mood float that scales
temperature. This one is different. It's an actual attempt to give an
LLM a *state* — a vector of 215 chemicals with half-lives, synthesis
pathways, receptor affinities, and interaction networks — and to make
that state change what the model thinks, recalls, and says.

The simulation is composed of four pieces:

- **A brain.** ~500 regions across forebrain, midbrain, hindbrain, and
  spinal cord. Not all are implemented; the ones that are, drive the
  hormone loop.
- **A chemistry.** 215 hormones, neurotransmitters, enzymes, and
  structural anchors in a YAML registry. Each has real clinical
  metadata: half-life, receptor targets, precursors, reference ranges.
- **A memory.** Four stores (episodic, semantic, procedural, working)
  with state-dependent recall — memories formed under a given hormone
  state are preferentially retrieved when that state recurs.
- **A model.** Gemma 4 E2B IT, abliterated with Heretic, fine-tuned
  with Unsloth for dual-output generation: an *internal monologue* that
  reflects the raw state, and a *spoken response* that reflects judgment.

## The three-panel view

The project's UI is a single screen with three panels:

| Panel | What it shows |
|---|---|
| **Left** | Brain state — regions light up with current hormone activity |
| **Middle** | What the model is thinking — raw internal monologue, hot temperature |
| **Right** | What the model says — composed response, cool temperature |

The middle and right panels come from the **same model, same call, same
hormone state**. What changes is the system prompt. This means the
difference between thought and speech is a real generation difference,
not a post-hoc rationalization.

Say "I got into a fight with my boss." The left panel shows cortisol
and noradrenaline spike. The middle panel shows the model's own
thinking trace — narrowing focus, threat response, hedged language.
The right panel shows a measured, professional response. Say "tell me
about my childhood dog" with low salience — cortisol stays low, the
middle panel shifts to something calmer, and the memory retrieved is
different because the hormone-state match is different.

## Why state-dependent recall matters

This is the project's novel claim, and the one thing that would be
publishable if it works:

**A memory formed under high cortisol is preferentially retrieved when
cortisol is high again, independent of semantic similarity.**

This maps to mood-congruent memory in cognitive psychology (Bower's
associative network theory). It's been observed in humans for decades.
It has not, to our knowledge, been implemented as a retrieval
mechanism in an LLM.

The mechanism:

1. When a memory is stored, the current hormone snapshot is frozen
   into its metadata (215 floats, one per chemical).
2. When a memory is recalled, the query is scored against four signals:
   semantic similarity, **hormone state similarity**, recency, and
   importance.
3. The hormone similarity term — a weighted cosine over the state
   vector — is what makes recall state-dependent.

The A/B test is simple: for the same query, run recall with the
hormone term enabled and disabled, and compare the top-k results.
`memory/analytics.py` produces that report. If the ranking doesn't
change with state, the whole project's premise doesn't hold and we
say so.

## Quick start

```bash
git clone https://github.com/<your-username>/200PlusHormoneBrain.git
cd 200PlusHormoneBrain
cp .env.example .env    # fill in HF_TOKEN and VLLM_REVISION
make up
```

Then open:

- **UI:** http://localhost:8501
- **API:** http://localhost:8000/docs
- **vLLM:** http://localhost:8001/v1/models

First run pulls the model from Hugging Face (~11 GB) — takes a few
minutes. After that, `make up` is ~30 seconds to a running system.

Requires Docker with the NVIDIA Container Toolkit, and a GPU with at
least 16 GB VRAM.

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│  ui/  Streamlit three-panel                                 │
│  ┌─────────────┬──────────────────┬────────────────────┐   │
│  │ brain viz   │ internal state   │ spoken response    │   │
│  └─────────────┴──────────────────┴────────────────────┘   │
└───────────────────────────┬────────────────────────────────┘
                            │ HTTP / SSE
┌───────────────────────────▼────────────────────────────────┐
│  gateway/  FastAPI + Uvicorn                                │
│  /chat      hormone tick → memory recall → prompt → vLLM    │
│  /state     current snapshot (for brain viz)                │
└────────────┬───────────────────────────────┬───────────────┘
             │                               │
             │ OpenAI-compatible             │ Chroma
┌────────────▼──────────────┐    ┌───────────▼───────────────┐
│  vLLM                     │    │  memory/                   │
│  TrueRealRaven/gemma-4-   │    │  episodic · semantic       │
│  E2B-it-heretic-v1        │    │  procedural · working      │
│  port 8001                │    │  state-dependent recall    │
└───────────────────────────┘    └────────────────────────────┘
```

The gateway owns the brain loop. For every user message:

1. Tick the hormone state — decay toward baseline, apply
   input-driven release to cortisol, noradrenaline, and adrenaline.
2. Snapshot the state (215 floats).
3. Recall memories, ranked by (semantic, hormone-match, recency,
   importance).
4. Assemble two prompts — one for the internal monologue, one for the
   spoken response — both containing the hormone snapshot, only the
   internal one containing the memory trace.
5. Send one call with thinking enabled. Split the output into
   `internal` and `spoken`.
6. Return both plus the snapshot to the UI.

## Project structure

```
200PlusHormoneBrain/
├── Makefile                     # make up / down / seed / train / abliterate
├── docker-compose.yml           # vLLM + gateway + UI + Chroma volume
├── config/
│   ├── models.yaml              # HF repo + revision (pinned)
│   ├── recall_weights.yaml      # tuning weights for memory system
│   └── memory_types.yaml        # taxonomy (implemented + unimplemented)
├── gateway/
│   ├── main.py                  # FastAPI routes
│   ├── brain_loop.py            # the tick + prompt assembly
│   └── state.py                 # HormoneState wrapper
├── infrastructure/
│   ├── brainparts/              # ~500 region folders (snake_case, symmetric)
│   ├── chemicals_hormones/      # 215 chemicals in 12 categories of YAML
│   └── memory/
│       ├── base.py              # MemoryItem, MemoryQuery, Recall
│       ├── vector.py            # HormoneVector — weighted cosine
│       ├── system.py            # MemorySystem — composes stores
│       ├── forgetting.py        # DecayPolicy, run_decay
│       ├── analytics.py         # state_relevance_report (the A/B test)
│       ├── backends/            # chroma, in_memory
│       └── stores/              # 5 implemented stores
├── ui/
│   └── app.py                   # Streamlit three-panel
├── training/
│   ├── sft_hormone_state.py     # Unsloth SFT
│   └── dpo_hormone_state.py     # Unsloth DPO
└── scripts/
    ├── check_symmetry.py        # brainparts left/right validator
    ├── forget.py                # scheduled decay CLI
    └── seed_memory.py           # populate Chroma for first run
```

## The model

The base is
[`TrueRealRaven/gemma-4-E2B-it-heretic-v1`](https://huggingface.co/TrueRealRaven/gemma-4-E2B-it-heretic-v1),
an abliterated variant of `google/gemma-4-E2B-it` produced with
[Heretic](https://github.com/p-e-w/heretic).

**Why abliterate.** The internal-monologue panel needs a model that
will express stress, fear, and dark thought without a safety layer
overriding the hormone state. The unmodified base hedges on exactly
those prompts. Heretic orthogonalizes the refusal direction while
minimizing KL divergence from the base — the Pareto point is chosen so
that refusal drops to near-zero without destroying coherence.

**Why E2B.** Gemma 4 E2B is "effective 2B" — 2.3B active parameters,
5.1B total including embeddings — multimodal (text, image, audio in),
128K context, Apache 2.0. It fits in 16 GB alongside Chroma and the
gateway, and its native thinking mode collapses the internal-monologue
and spoken-response panels into a single model call.

**Self-learning.** The base is the *starting point*. Each running
instance fine-tunes itself locally on its own conversation history,
using ORPO (single-stage preference optimization, no reference model,
fits alongside the served model on the same GPU). The fine-tuned
weights are **never published** — they stay on the user's disk,
versioned in `checkpoints/adapters/` and promoted only when they beat
the previous adapter on a held-out eval set. The published artifact is
the base; everything above it is personal.

The base is pinned by commit hash in `config/models.yaml`. The gateway
loads it once and swaps LoRA adapters as they're trained, so the model
is only reloaded when the *base* changes — never for a routine
training round.

## Self-learning

The project's model adapts to *one user*, on *their* hardware, on
*their* data. Nothing is sent to a server.

**Training loop.** Every conversation is logged with the hormone
snapshot at each turn. Every N turns (configurable), the system:

1. **Builds preference pairs** from the log — via rejection sampling
   (generate multiple responses, score them, pair best/worst), explicit
   user ratings, and optionally brain-state consistency (a response
   whose internal monologue contradicts the current hormone state is
   scored lower).
2. **Runs ORPO** — a single-stage LoRA fine-tune that combines SFT and
   preference optimization. No reference model means it fits alongside
   vLLM on the same GPU.
3. **Gates the result** — the new adapter must beat the current adapter
   on a held-out eval set before it's promoted. If it doesn't, the
   previous adapter stays active and the training log is kept for
   inspection.
4. **Hot-swaps the adapter** — vLLM's LoRA serving means the base model
   stays loaded; only the ~100 MB adapter file changes.

**Stability.** Iterative ORPO on user data drifts the model over time.
Three controls:

- **Adapter versioning** — every training round produces a timestamped
  checkpoint. Rollback is `cp checkpoints/adapters/{prev}/* checkpoints/adapters/current/`.
- **Eval gate** — no adapter is promoted without passing held-out
  validation. The gate is the only thing between the training loop and
  the served model.
- **Periodic reset** — every ~10 rounds, retrain from the published
  base rather than from the current adapter, to prevent accumulated
  drift.

**What this is *not*.** It's not continual online learning — training
happens in batches, not per-turn. It's not reinforcement learning —
ORPO is preference optimization, not reward maximization. The model
improves on *your* data, in *your* style, with *your* hormone-state
patterns. It doesn't get universally smarter.

**Forgetting.** The memory stores (Chroma) decay over time — see
`scripts/forget.py` and `memory/forgetting.py`. The *weights* do not
decay. An adapter can only be rolled back to a previous version, not
"forgotten." Two lifecycles, two mechanisms, by design.

## Status

What works today:

- [x] Brain region tree — 500 folders, snake_case, symmetric
- [x] Chemical registry — 215 records across 12 categories, schema
      and loader, cross-reference validation
- [x] Base model — abliterated, published, pinned
- [x] Memory schema — `MemoryItem`, `MemoryQuery`, `Recall`, `HormoneVector`
- [x] Memory system — `MemorySystem` with composition and merging
- [x] Backends — Chroma + in-memory, swappable

What's in progress:

- [ ] Gateway — FastAPI app, brain loop, dual-output split
- [ ] UI — three-panel Streamlit
- [ ] Chroma stores — migrate legacy `facts_memory/`, fix known bugs
- [ ] `state_relevance_report` — the A/B test that proves recall changes with state
- [ ] Docker Compose — end-to-end `make up` from fresh clone

What's planned:

- [ ] SFT/DPO fine-tune on hormone-state pairs
- [ ] Procedural memory — skill registry backed by LoRA adapters
- [ ] Forgetting CLI — scheduled decay
- [ ] Brain visualization — real region graph, not placeholder
- [ ] Audio input — Gemma 4 E2B accepts it natively

## What this project is not

- **Not a medical device.** Nothing here is clinically validated. No
  output from this project should inform any health decision.
- **Not a consciousness claim.** The model has a state. It does not
  have experience, qualia, or self-awareness. The word "thinks" in this
  README is shorthand for "generates a reasoning trace," not a claim
  about phenomenology.
- **Not a safety-aligned assistant.** The underlying model has had its
  refusal direction removed. It will express content that a standard
  model would decline. That's the point of the internal-monologue panel,
  but it means the model is not suitable for general deployment.
- **Not finished.** See [Status](#status). Read this as a project in
  progress with a working foundation, not a shipped product.

## Contributing

Issues and PRs welcome, especially on:

- The state-dependent recall A/B test — the evaluation methodology
  matters more than the implementation
- Cross-references in `chemicals_hormones/` — many records still have
  missing `precursors` / `interacts_with` links
- Brain region symmetry — see `scripts/check_symmetry.py`

Before contributing, run:

```bash
make test       # schema validation, symmetry check, smoke tests
make lint       # ruff, mypy
```

## License

**Project code: MIT** — see [LICENSE](LICENSE).

**Model weights: Apache 2.0** — inherited from Gemma 4 (Google), per
their [license terms](https://ai.google.dev/gemma/terms). The
abliterated model card on Hugging Face states this explicitly.

All upstream dependencies are compatible: Heretic (MIT), Unsloth
(Apache 2.0), vLLM (Apache 2.0), Chroma (Apache 2.0).

## Acknowledgments

- **Google** for Gemma 4 and for shipping a small, multimodal, Apache-2.0
  model that runs on consumer hardware
- **p-e-w** for [Heretic](https://github.com/p-e-w/heretic) — the
  cleanest abliteration tool available
- **Unsloth** for making fine-tuning possible on a single GPU
- **vLLM** for making inference fast enough to feel like a conversation

## Citation

If you use this project or its models:

```bibtex
@misc{200plushormonebrain2026,
  title  = {200PlusHormoneBrain: an LLM on a neuroendocrine simulation},
  author = {<your-name>},
  year   = {2026},
  url    = {https://github.com/<your-username>/200PlusHormoneBrain}
}
```

For the base model specifically:

```bibtex
@misc{gemma4e2bheretic2026,
  title  = {Gemma 4 E2B IT — Heretic v1},
  author = {<your-name>},
  year   = {2026},
  url    = {https://huggingface.co/TrueRealRaven/gemma-4-E2B-it-heretic-v1}
}
```