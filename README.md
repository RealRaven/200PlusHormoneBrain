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
200PlusHormoneBrain
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── config
│   ├── memory_types.yaml
│   └── recall_weights.yaml
├── docker-compose.yml
├── infrastructure
│   ├── __init__.py
│   ├── brainparts
│   │   ├── __init__.py
│   │   ├── forebrain
│   │   │   ├── __init__.py
│   │   │   ├── diencephalon
│   │   │   │   ├── __init__.py
│   │   │   │   ├── epithalamus
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── habenular_nuclei
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       └── __init__.py
│   │   │   │   │   ├── pineal_gland
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── stria_medullaris
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       └── __init__.py
│   │   │   │   │   └── taenia_thalami
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── left
│   │   │   │   │       │   └── __init__.py
│   │   │   │   │       └── right
│   │   │   │   │           └── __init__.py
│   │   │   │   ├── hypothalamus
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── anterior
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── lateral_area
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── anterior_part_of_lateral_nucleus
│   │   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   │   ├── part_of_supraoptic_nucleus
│   │   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   │   ├── periventricular_preoptic_nucleus
│   │   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   │   └── preoptic_area
│   │   │   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │   │   │       └── lateral_preoptic_nucleus
│   │   │   │   │   │   │   │           └── __init__.py
│   │   │   │   │   │   │   └── right
│   │   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │   │       ├── anterior_part_of_lateral_nucleus
│   │   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │   │       ├── part_of_supraoptic_nucleus
│   │   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │   │       ├── periventricular_preoptic_nucleus
│   │   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │   │       └── preoptic_area
│   │   │   │   │   │   │           ├── __init__.py
│   │   │   │   │   │   │           └── lateral_preoptic_nucleus
│   │   │   │   │   │   │               └── __init__.py
│   │   │   │   │   │   └── medial_area
│   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │       ├── left
│   │   │   │   │   │       │   ├── __init__.py
│   │   │   │   │   │       │   ├── anterior_hypothalamic_nucleus
│   │   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │   │       │   ├── paraventricular_nucleus
│   │   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │   │       │   ├── preoptic_area
│   │   │   │   │   │       │   │   ├── __init__.py
│   │   │   │   │   │       │   │   ├── medial_preoptic_nucleus
│   │   │   │   │   │       │   │   │   ├── __init__.py
│   │   │   │   │   │       │   │   │   ├── inah_1
│   │   │   │   │   │       │   │   │   │   └── __init__.py
│   │   │   │   │   │       │   │   │   ├── inah_2
│   │   │   │   │   │       │   │   │   │   └── __init__.py
│   │   │   │   │   │       │   │   │   ├── inah_3
│   │   │   │   │   │       │   │   │   │   └── __init__.py
│   │   │   │   │   │       │   │   │   └── inah_4
│   │   │   │   │   │       │   │   │       └── __init__.py
│   │   │   │   │   │       │   │   └── median_preoptic_nucleus
│   │   │   │   │   │       │   │       └── __init__.py
│   │   │   │   │   │       │   ├── suprachiasmatic_nucleus
│   │   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │   │       │   └── supraoptic_nucleus
│   │   │   │   │   │       │       └── __init__.py
│   │   │   │   │   │       └── right
│   │   │   │   │   │           ├── __init__.py
│   │   │   │   │   │           ├── anterior_hypothalamic_nucleus
│   │   │   │   │   │           │   └── __init__.py
│   │   │   │   │   │           ├── paraventricular_nucleus
│   │   │   │   │   │           │   └── __init__.py
│   │   │   │   │   │           ├── preoptic_area
│   │   │   │   │   │           │   ├── __init__.py
│   │   │   │   │   │           │   ├── medial_preoptic_nucleus
│   │   │   │   │   │           │   │   ├── __init__.py
│   │   │   │   │   │           │   │   ├── inah_1
│   │   │   │   │   │           │   │   │   └── __init__.py
│   │   │   │   │   │           │   │   ├── inah_2
│   │   │   │   │   │           │   │   │   └── __init__.py
│   │   │   │   │   │           │   │   ├── inah_3
│   │   │   │   │   │           │   │   │   └── __init__.py
│   │   │   │   │   │           │   │   └── inah_4
│   │   │   │   │   │           │   │       └── __init__.py
│   │   │   │   │   │           │   └── median_preoptic_nucleus
│   │   │   │   │   │           │       └── __init__.py
│   │   │   │   │   │           ├── suprachiasmatic_nucleus
│   │   │   │   │   │           │   └── __init__.py
│   │   │   │   │   │           └── supraoptic_nucleus
│   │   │   │   │   │               └── __init__.py
│   │   │   │   │   ├── mammillary_bodies
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       └── __init__.py
│   │   │   │   │   ├── median_eminence
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── optic_chiasm
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── other_preoptic_nuclei
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       └── __init__.py
│   │   │   │   │   ├── periventricular_nucleus
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       └── __init__.py
│   │   │   │   │   ├── pituitary_stalk
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── posterior
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── lateral_area
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   └── posterior_part_of_lateral_nucleus
│   │   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   │   └── right
│   │   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │   │       └── posterior_part_of_lateral_nucleus
│   │   │   │   │   │   │           └── __init__.py
│   │   │   │   │   │   └── medial_area
│   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │       ├── mammillary_nuclei
│   │   │   │   │   │       │   ├── __init__.py
│   │   │   │   │   │       │   ├── left
│   │   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │   │       │   └── right
│   │   │   │   │   │       │       └── __init__.py
│   │   │   │   │   │       └── posterior_nucleus
│   │   │   │   │   │           ├── __init__.py
│   │   │   │   │   │           ├── left
│   │   │   │   │   │           │   └── __init__.py
│   │   │   │   │   │           └── right
│   │   │   │   │   │               └── __init__.py
│   │   │   │   │   ├── subfornical_organ
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── tuber_cinereum
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── tuberal_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── tuberomammillary_nucleus
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │       ├── tuberal_nucleus
│   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │       └── tuberomammillary_nucleus
│   │   │   │   │   │           └── __init__.py
│   │   │   │   │   └── tuberal
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── lateral_area
│   │   │   │   │       │   ├── __init__.py
│   │   │   │   │       │   ├── left
│   │   │   │   │       │   │   ├── __init__.py
│   │   │   │   │       │   │   ├── lateral_tuberal_nuclei
│   │   │   │   │       │   │   │   └── __init__.py
│   │   │   │   │       │   │   └── tuberal_part_of_lateral_nucleus
│   │   │   │   │       │   │       └── __init__.py
│   │   │   │   │       │   └── right
│   │   │   │   │       │       ├── __init__.py
│   │   │   │   │       │       ├── lateral_tuberal_nuclei
│   │   │   │   │       │       │   └── __init__.py
│   │   │   │   │       │       └── tuberal_part_of_lateral_nucleus
│   │   │   │   │       │           └── __init__.py
│   │   │   │   │       └── medial_area
│   │   │   │   │           ├── __init__.py
│   │   │   │   │           ├── arcuate_nucleus
│   │   │   │   │           │   ├── __init__.py
│   │   │   │   │           │   ├── left
│   │   │   │   │           │   │   └── __init__.py
│   │   │   │   │           │   └── right
│   │   │   │   │           │       └── __init__.py
│   │   │   │   │           ├── dorsomedial_hypothalamic_nucleus
│   │   │   │   │           │   ├── __init__.py
│   │   │   │   │           │   ├── left
│   │   │   │   │           │   │   └── __init__.py
│   │   │   │   │           │   └── right
│   │   │   │   │           │       └── __init__.py
│   │   │   │   │           └── ventromedial_nucleus
│   │   │   │   │               ├── __init__.py
│   │   │   │   │               ├── left
│   │   │   │   │               │   └── __init__.py
│   │   │   │   │               └── right
│   │   │   │   │                   └── __init__.py
│   │   │   │   ├── pituitary_gland
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── adenohypophysis
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── neurohypophysis
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── pars_intermedia
│   │   │   │   │       └── __init__.py
│   │   │   │   ├── subcommissural_organ
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── subthalamus
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── subthalamic_nucleus
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       └── __init__.py
│   │   │   │   │   └── zona_incerta
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── left
│   │   │   │   │       │   └── __init__.py
│   │   │   │   │       └── right
│   │   │   │   │           └── __init__.py
│   │   │   │   ├── thalamus
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── left
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── anterior_nuclear_group
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── anterodorsal_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── anteromedial_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── anteroventral_nucleus
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   ├── lateral_nuclear_group
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── lateral_dorsal_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── lateral_posterior_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── pulvinar
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   ├── medial_nuclear_group
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── central_lateral_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── centromedian_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── intralaminar_nuclear_group
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── medial_dorsal_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── midline_nuclear_group
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── parafascicular_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── paratenial_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── reuniens_nucleus
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── rhomboidal_nucleus
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   ├── metathalamus
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── lateral_geniculate_body
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── medial_geniculate_body
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   ├── reticular_nucleus
│   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   └── ventral_nuclear_group
│   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │       ├── ventral_anterior_nucleus
│   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │       ├── ventral_lateral_nucleus
│   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │       └── ventral_posterior_nucleus
│   │   │   │   │   │           ├── __init__.py
│   │   │   │   │   │           ├── ventral_posterior_lateral_nucleus
│   │   │   │   │   │           │   └── __init__.py
│   │   │   │   │   │           └── ventral_posterior_medial_nucleus
│   │   │   │   │   │               └── __init__.py
│   │   │   │   │   └── right
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── anterior_nuclear_group
│   │   │   │   │       │   ├── __init__.py
│   │   │   │   │       │   ├── anterodorsal_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── anteromedial_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   └── anteroventral_nucleus
│   │   │   │   │       │       └── __init__.py
│   │   │   │   │       ├── lateral_nuclear_group
│   │   │   │   │       │   ├── __init__.py
│   │   │   │   │       │   ├── lateral_dorsal_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── lateral_posterior_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   └── pulvinar
│   │   │   │   │       │       └── __init__.py
│   │   │   │   │       ├── medial_nuclear_group
│   │   │   │   │       │   ├── __init__.py
│   │   │   │   │       │   ├── central_lateral_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── centromedian_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── intralaminar_nuclear_group
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── medial_dorsal_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── midline_nuclear_group
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── parafascicular_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── paratenial_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   ├── reuniens_nucleus
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   └── rhomboidal_nucleus
│   │   │   │   │       │       └── __init__.py
│   │   │   │   │       ├── metathalamus
│   │   │   │   │       │   ├── __init__.py
│   │   │   │   │       │   ├── lateral_geniculate_body
│   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │       │   └── medial_geniculate_body
│   │   │   │   │       │       └── __init__.py
│   │   │   │   │       ├── reticular_nucleus
│   │   │   │   │       │   └── __init__.py
│   │   │   │   │       └── ventral_nuclear_group
│   │   │   │   │           ├── __init__.py
│   │   │   │   │           ├── ventral_anterior_nucleus
│   │   │   │   │           │   └── __init__.py
│   │   │   │   │           ├── ventral_lateral_nucleus
│   │   │   │   │           │   └── __init__.py
│   │   │   │   │           └── ventral_posterior_nucleus
│   │   │   │   │               ├── __init__.py
│   │   │   │   │               ├── ventral_posterior_lateral_nucleus
│   │   │   │   │               │   └── __init__.py
│   │   │   │   │               └── ventral_posterior_medial_nucleus
│   │   │   │   │                   └── __init__.py
│   │   │   │   └── third_ventricle
│   │   │   │       └── __init__.py
│   │   │   └── telencephalon
│   │   │       ├── __init__.py
│   │   │       ├── cerebral_hemispheres
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   ├── __init__.py
│   │   │       │   │   ├── cortex
│   │   │       │   │   │   ├── __init__.py
│   │   │       │   │   │   ├── cingulate
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── anterior_cingulate
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── brodmann_areas
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_23
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_24
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_26_retrosplenial
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_29_retrosplenial
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_30_retrosplenial
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_31
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── brodmann_area_32
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── indusium_griseum
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── posterior_cingulate
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── retrosplenial_cortex
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   └── subgenual_area_25
│   │   │       │   │   │   │       └── __init__.py
│   │   │       │   │   │   ├── frontal
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── brodmann_areas
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── brocas_area
│   │   │       │   │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   │   ├── brodmann_area_44
│   │   │       │   │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   │   └── brodmann_area_45
│   │   │       │   │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_10
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_11
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_12
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_25
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_33
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_4
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_46
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_47
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_6
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_8
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── brodmann_area_9
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── cortex
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── prefrontal_cortex
│   │   │       │   │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   │   ├── dorsolateral_prefrontal_cortex
│   │   │       │   │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   │   ├── dorsomedial_prefrontal_cortex
│   │   │       │   │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   │   ├── orbitofrontal_cortex
│   │   │       │   │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   │   ├── ventrolateral_prefrontal_cortex
│   │   │       │   │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   │   └── ventromedial_prefrontal_cortex
│   │   │       │   │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   │   ├── premotor_cortex
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── primary_motor_cortex
│   │   │       │   │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   │   └── precentral_gyrus
│   │   │       │   │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   │   └── supplementary_motor_cortex
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── gyri
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── inferior_frontal_gyrus
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── middle_frontal_gyrus
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── superior_frontal_gyrus
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   └── sulci
│   │   │       │   │   │   │       ├── __init__.py
│   │   │       │   │   │   │       ├── inferior_frontal_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       ├── olfactory_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       ├── orbital_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       ├── paracentral_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       ├── precentral_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       └── superior_frontal_sulcus
│   │   │       │   │   │   │           └── __init__.py
│   │   │       │   │   │   ├── insular
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── brodmann_areas
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_13_middle_insula
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_14
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_16
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_41_posterior_insula
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_42_posterior_insula
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── brodmann_area_43_anterior_insula
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   └── primary_gustatory_cortex
│   │   │       │   │   │   │       └── __init__.py
│   │   │       │   │   │   ├── occipital
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── brodmann_areas
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_17_primary_visual
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_18
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── brodmann_area_19
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── cortex
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── primary_visual_cortex
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── v2
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── v3
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── v4
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── cuneus
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── gyri
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   └── lateral_occipital_gyrus
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   └── sulci
│   │   │       │   │   │   │       ├── __init__.py
│   │   │       │   │   │   │       ├── calcarine_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       ├── lunate_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       └── transverse_occipital_sulcus
│   │   │       │   │   │   │           └── __init__.py
│   │   │       │   │   │   ├── parietal
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── brodmann_areas
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_1
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_2
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_26
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_39
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_40
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── brodmann_area_5
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── brodmann_area_7
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── cortex
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── posterior_parietal_cortex
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   ├── primary_somatosensory_cortex
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── secondary_somatosensory_cortex
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── gyri
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   ├── paracentral_lobule
│   │   │       │   │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   │   └── postcentral_gyrus
│   │   │       │   │   │   │   │       ├── __init__.py
│   │   │       │   │   │   │   │       └── brodmann_area_3
│   │   │       │   │   │   │   │           └── __init__.py
│   │   │       │   │   │   │   ├── precuneus
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   └── sulci
│   │   │       │   │   │   │       ├── __init__.py
│   │   │       │   │   │   │       ├── intraparietal_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       ├── marginal_sulcus
│   │   │       │   │   │   │       │   └── __init__.py
│   │   │       │   │   │   │       └── postcentral_sulcus
│   │   │       │   │   │   │           └── __init__.py
│   │   │       │   │   │   └── temporal
│   │   │       │   │   │       ├── __init__.py
│   │   │       │   │   │       ├── brodmann_areas
│   │   │       │   │   │       │   ├── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_15
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_20
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_21
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_22
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_27
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_28
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_34
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_35
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_36
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_37
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── brodmann_area_38
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   └── brodmann_area_48_retrosubicular
│   │   │       │   │   │       │       └── __init__.py
│   │   │       │   │   │       ├── cortex
│   │   │       │   │   │       │   ├── __init__.py
│   │   │       │   │   │       │   ├── anterior_temporal_lobe
│   │   │       │   │   │       │   │   ├── __init__.py
│   │   │       │   │   │       │   │   └── olfactory_cortex
│   │   │       │   │   │       │   │       └── __init__.py
│   │   │       │   │   │       │   ├── inferior_temporal_cortex
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── mt
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── posterior_inferior_temporal_cortex
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── primary_auditory_cortex
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   └── secondary_auditory_cortex
│   │   │       │   │   │       │       └── __init__.py
│   │   │       │   │   │       ├── gyri
│   │   │       │   │   │       │   ├── __init__.py
│   │   │       │   │   │       │   ├── entorhinal_cortex
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── fusiform_gyrus
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── inferior_temporal_gyrus
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── middle_temporal_gyrus
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── parahippocampal_gyrus
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── perirhinal_cortex
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   └── superior_temporal_gyrus
│   │   │       │   │   │       │       ├── __init__.py
│   │   │       │   │   │       │       └── wernickes_area
│   │   │       │   │   │       │           ├── __init__.py
│   │   │       │   │   │       │           └── brodmann_area_22
│   │   │       │   │   │       │               └── __init__.py
│   │   │       │   │   │       ├── medial_superior_temporal_area
│   │   │       │   │   │       │   └── __init__.py
│   │   │       │   │   │       └── sulci
│   │   │       │   │   │           ├── __init__.py
│   │   │       │   │   │           ├── inferior_temporal_sulcus
│   │   │       │   │   │           │   └── __init__.py
│   │   │       │   │   │           └── superior_temporal_sulcus
│   │   │       │   │   │               └── __init__.py
│   │   │       │   │   ├── rhinencephalon
│   │   │       │   │   │   ├── __init__.py
│   │   │       │   │   │   ├── anterior_olfactory_nucleus
│   │   │       │   │   │   │   └── __init__.py
│   │   │       │   │   │   ├── olfactory_bulb
│   │   │       │   │   │   │   └── __init__.py
│   │   │       │   │   │   ├── olfactory_tract
│   │   │       │   │   │   │   └── __init__.py
│   │   │       │   │   │   ├── periamygdaloid_cortex
│   │   │       │   │   │   │   └── __init__.py
│   │   │       │   │   │   ├── piriform_cortex
│   │   │       │   │   │   │   └── __init__.py
│   │   │       │   │   │   └── uncus
│   │   │       │   │   │       └── __init__.py
│   │   │       │   │   ├── subcortical
│   │   │       │   │   │   ├── __init__.py
│   │   │       │   │   │   ├── basal_forebrain
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── anterior_perforated_substance
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── diagonal_band_of_broca
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── lamina_terminalis
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   └── vascular_organ_of_lamina_terminalis
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   ├── nucleus_basalis
│   │   │       │   │   │   │   │   └── __init__.py
│   │   │       │   │   │   │   ├── septal_nuclei
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   └── medial_septal_nuclei
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   └── substantia_innominata
│   │   │       │   │   │   │       └── __init__.py
│   │   │       │   │   │   ├── basal_ganglia
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   ├── globus_pallidus
│   │   │       │   │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   │   └── ventral_pallidum
│   │   │       │   │   │   │   │       └── __init__.py
│   │   │       │   │   │   │   └── striatum
│   │   │       │   │   │   │       ├── __init__.py
│   │   │       │   │   │   │       ├── dorsal_striatum
│   │   │       │   │   │   │       │   ├── __init__.py
│   │   │       │   │   │   │       │   ├── caudate_nucleus
│   │   │       │   │   │   │       │   │   └── __init__.py
│   │   │       │   │   │   │       │   └── putamen
│   │   │       │   │   │   │       │       └── __init__.py
│   │   │       │   │   │   │       └── ventral_striatum
│   │   │       │   │   │   │           ├── __init__.py
│   │   │       │   │   │   │           ├── nucleus_accumbens
│   │   │       │   │   │   │           │   └── __init__.py
│   │   │       │   │   │   │           └── olfactory_tubercle
│   │   │       │   │   │   │               └── __init__.py
│   │   │       │   │   │   ├── claustrum
│   │   │       │   │   │   │   └── __init__.py
│   │   │       │   │   │   ├── extended_amygdala
│   │   │       │   │   │   │   ├── __init__.py
│   │   │       │   │   │   │   └── stria_terminalis
│   │   │       │   │   │   │       ├── __init__.py
│   │   │       │   │   │   │       └── bed_nucleus_of_stria_terminalis
│   │   │       │   │   │   │           └── __init__.py
│   │   │       │   │   │   └── medial_temporal_lobe
│   │   │       │   │   │       ├── __init__.py
│   │   │       │   │   │       ├── amygdala
│   │   │       │   │   │       │   ├── __init__.py
│   │   │       │   │   │       │   ├── accessory_olfactory_system
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── amygdala_cortex_pathways
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── autonomic_nervous_system
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── basolateral_nuclei
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── basomedial_nuclei
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── central_nucleus
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── frontotemporal_cortical_system
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── lateral_nucleus
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   ├── main_olfactory_system
│   │   │       │   │   │       │   │   └── __init__.py
│   │   │       │   │   │       │   └── medial_nucleus
│   │   │       │   │   │       │       └── __init__.py
│   │   │       │   │   │       └── hippocampus
│   │   │       │   │   │           ├── __init__.py
│   │   │       │   │   │           ├── cornu_ammonis
│   │   │       │   │   │           │   ├── __init__.py
│   │   │       │   │   │           │   ├── ca1
│   │   │       │   │   │           │   │   └── __init__.py
│   │   │       │   │   │           │   ├── ca2
│   │   │       │   │   │           │   │   └── __init__.py
│   │   │       │   │   │           │   ├── ca3
│   │   │       │   │   │           │   │   └── __init__.py
│   │   │       │   │   │           │   └── ca4
│   │   │       │   │   │           │       └── __init__.py
│   │   │       │   │   │           ├── dentate_gyrus
│   │   │       │   │   │           │   └── __init__.py
│   │   │       │   │   │           ├── parasubiculum
│   │   │       │   │   │           │   └── __init__.py
│   │   │       │   │   │           ├── presubiculum
│   │   │       │   │   │           │   └── __init__.py
│   │   │       │   │   │           └── subiculum
│   │   │       │   │   │               └── __init__.py
│   │   │       │   │   └── white_matter
│   │   │       │   │       ├── __init__.py
│   │   │       │   │       ├── centrum_semiovale
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── cingulum
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── corona_radiata
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── external_capsule
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── extreme_capsule
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── fasciculus_rectus
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── fornix
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── internal_capsule
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       ├── mammillothalamic_tract
│   │   │       │   │       │   └── __init__.py
│   │   │       │   │       └── medial_forebrain_bundle
│   │   │       │   │           └── __init__.py
│   │   │       │   └── right
│   │   │       │       ├── __init__.py
│   │   │       │       ├── cortex
│   │   │       │       │   ├── __init__.py
│   │   │       │       │   ├── cingulate
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── anterior_cingulate
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── brodmann_areas
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_23
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_24
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_26_retrosplenial
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_29_retrosplenial
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_30_retrosplenial
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_31
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── brodmann_area_32
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── indusium_griseum
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── posterior_cingulate
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── retrosplenial_cortex
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   └── subgenual_area_25
│   │   │       │       │   │       └── __init__.py
│   │   │       │       │   ├── frontal
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── brodmann_areas
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── brocas_area
│   │   │       │       │   │   │   │   ├── __init__.py
│   │   │       │       │   │   │   │   ├── brodmann_area_44
│   │   │       │       │   │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   │   └── brodmann_area_45
│   │   │       │       │   │   │   │       └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_10
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_11
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_12
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_25
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_33
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_4
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_46
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_47
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_6
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_8
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── brodmann_area_9
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── cortex
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── prefrontal_cortex
│   │   │       │       │   │   │   │   ├── __init__.py
│   │   │       │       │   │   │   │   ├── dorsolateral_prefrontal_cortex
│   │   │       │       │   │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   │   ├── dorsomedial_prefrontal_cortex
│   │   │       │       │   │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   │   ├── orbitofrontal_cortex
│   │   │       │       │   │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   │   ├── ventrolateral_prefrontal_cortex
│   │   │       │       │   │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   │   └── ventromedial_prefrontal_cortex
│   │   │       │       │   │   │   │       └── __init__.py
│   │   │       │       │   │   │   ├── premotor_cortex
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── primary_motor_cortex
│   │   │       │       │   │   │   │   ├── __init__.py
│   │   │       │       │   │   │   │   └── precentral_gyrus
│   │   │       │       │   │   │   │       └── __init__.py
│   │   │       │       │   │   │   └── supplementary_motor_cortex
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── gyri
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── inferior_frontal_gyrus
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── middle_frontal_gyrus
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── superior_frontal_gyrus
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   └── sulci
│   │   │       │       │   │       ├── __init__.py
│   │   │       │       │   │       ├── inferior_frontal_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       ├── olfactory_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       ├── orbital_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       ├── paracentral_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       ├── precentral_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       └── superior_frontal_sulcus
│   │   │       │       │   │           └── __init__.py
│   │   │       │       │   ├── insular
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── brodmann_areas
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_13_middle_insula
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_14
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_16
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_41_posterior_insula
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_42_posterior_insula
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── brodmann_area_43_anterior_insula
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   └── primary_gustatory_cortex
│   │   │       │       │   │       └── __init__.py
│   │   │       │       │   ├── occipital
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── brodmann_areas
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_17_primary_visual
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_18
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── brodmann_area_19
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── cortex
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── primary_visual_cortex
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── v2
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── v3
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── v4
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── cuneus
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── gyri
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   └── lateral_occipital_gyrus
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   └── sulci
│   │   │       │       │   │       ├── __init__.py
│   │   │       │       │   │       ├── calcarine_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       ├── lunate_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       └── transverse_occipital_sulcus
│   │   │       │       │   │           └── __init__.py
│   │   │       │       │   ├── parietal
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── brodmann_areas
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_1
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_2
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_26
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_39
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_40
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── brodmann_area_5
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── brodmann_area_7
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── cortex
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── posterior_parietal_cortex
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   ├── primary_somatosensory_cortex
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── secondary_somatosensory_cortex
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── gyri
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   ├── paracentral_lobule
│   │   │       │       │   │   │   │   └── __init__.py
│   │   │       │       │   │   │   └── postcentral_gyrus
│   │   │       │       │   │   │       ├── __init__.py
│   │   │       │       │   │   │       └── brodmann_area_3
│   │   │       │       │   │   │           └── __init__.py
│   │   │       │       │   │   ├── precuneus
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   └── sulci
│   │   │       │       │   │       ├── __init__.py
│   │   │       │       │   │       ├── intraparietal_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       ├── marginal_sulcus
│   │   │       │       │   │       │   └── __init__.py
│   │   │       │       │   │       └── postcentral_sulcus
│   │   │       │       │   │           └── __init__.py
│   │   │       │       │   └── temporal
│   │   │       │       │       ├── __init__.py
│   │   │       │       │       ├── brodmann_areas
│   │   │       │       │       │   ├── __init__.py
│   │   │       │       │       │   ├── brodmann_area_15
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_20
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_21
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_22
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_27
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_28
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_34
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_35
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_36
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_37
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── brodmann_area_38
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   └── brodmann_area_48_retrosubicular
│   │   │       │       │       │       └── __init__.py
│   │   │       │       │       ├── cortex
│   │   │       │       │       │   ├── __init__.py
│   │   │       │       │       │   ├── anterior_temporal_lobe
│   │   │       │       │       │   │   ├── __init__.py
│   │   │       │       │       │   │   └── olfactory_cortex
│   │   │       │       │       │   │       └── __init__.py
│   │   │       │       │       │   ├── inferior_temporal_cortex
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── mt
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── posterior_inferior_temporal_cortex
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── primary_auditory_cortex
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   └── secondary_auditory_cortex
│   │   │       │       │       │       └── __init__.py
│   │   │       │       │       ├── gyri
│   │   │       │       │       │   ├── __init__.py
│   │   │       │       │       │   ├── entorhinal_cortex
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── fusiform_gyrus
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── inferior_temporal_gyrus
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── middle_temporal_gyrus
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── parahippocampal_gyrus
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── perirhinal_cortex
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   └── superior_temporal_gyrus
│   │   │       │       │       │       ├── __init__.py
│   │   │       │       │       │       └── wernickes_area
│   │   │       │       │       │           ├── __init__.py
│   │   │       │       │       │           └── brodmann_area_22
│   │   │       │       │       │               └── __init__.py
│   │   │       │       │       ├── medial_superior_temporal_area
│   │   │       │       │       │   └── __init__.py
│   │   │       │       │       └── sulci
│   │   │       │       │           ├── __init__.py
│   │   │       │       │           ├── inferior_temporal_sulcus
│   │   │       │       │           │   └── __init__.py
│   │   │       │       │           └── superior_temporal_sulcus
│   │   │       │       │               └── __init__.py
│   │   │       │       ├── rhinencephalon
│   │   │       │       │   ├── __init__.py
│   │   │       │       │   ├── anterior_olfactory_nucleus
│   │   │       │       │   │   └── __init__.py
│   │   │       │       │   ├── olfactory_bulb
│   │   │       │       │   │   └── __init__.py
│   │   │       │       │   ├── olfactory_tract
│   │   │       │       │   │   └── __init__.py
│   │   │       │       │   ├── periamygdaloid_cortex
│   │   │       │       │   │   └── __init__.py
│   │   │       │       │   ├── piriform_cortex
│   │   │       │       │   │   └── __init__.py
│   │   │       │       │   └── uncus
│   │   │       │       │       └── __init__.py
│   │   │       │       ├── subcortical
│   │   │       │       │   ├── __init__.py
│   │   │       │       │   ├── basal_forebrain
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── anterior_perforated_substance
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── diagonal_band_of_broca
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── lamina_terminalis
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   └── vascular_organ_of_lamina_terminalis
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   ├── nucleus_basalis
│   │   │       │       │   │   │   └── __init__.py
│   │   │       │       │   │   ├── septal_nuclei
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   └── medial_septal_nuclei
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   └── substantia_innominata
│   │   │       │       │   │       └── __init__.py
│   │   │       │       │   ├── basal_ganglia
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   ├── globus_pallidus
│   │   │       │       │   │   │   ├── __init__.py
│   │   │       │       │   │   │   └── ventral_pallidum
│   │   │       │       │   │   │       └── __init__.py
│   │   │       │       │   │   └── striatum
│   │   │       │       │   │       ├── __init__.py
│   │   │       │       │   │       ├── dorsal_striatum
│   │   │       │       │   │       │   ├── __init__.py
│   │   │       │       │   │       │   ├── caudate_nucleus
│   │   │       │       │   │       │   │   └── __init__.py
│   │   │       │       │   │       │   └── putamen
│   │   │       │       │   │       │       └── __init__.py
│   │   │       │       │   │       └── ventral_striatum
│   │   │       │       │   │           ├── __init__.py
│   │   │       │       │   │           ├── nucleus_accumbens
│   │   │       │       │   │           │   └── __init__.py
│   │   │       │       │   │           └── olfactory_tubercle
│   │   │       │       │   │               └── __init__.py
│   │   │       │       │   ├── claustrum
│   │   │       │       │   │   └── __init__.py
│   │   │       │       │   ├── extended_amygdala
│   │   │       │       │   │   ├── __init__.py
│   │   │       │       │   │   └── stria_terminalis
│   │   │       │       │   │       ├── __init__.py
│   │   │       │       │   │       └── bed_nucleus_of_stria_terminalis
│   │   │       │       │   │           └── __init__.py
│   │   │       │       │   └── medial_temporal_lobe
│   │   │       │       │       ├── __init__.py
│   │   │       │       │       ├── amygdala
│   │   │       │       │       │   ├── __init__.py
│   │   │       │       │       │   ├── accessory_olfactory_system
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── amygdala_cortex_pathways
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── autonomic_nervous_system
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── basolateral_nuclei
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── basomedial_nuclei
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── central_nucleus
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── frontotemporal_cortical_system
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── lateral_nucleus
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   ├── main_olfactory_system
│   │   │       │       │       │   │   └── __init__.py
│   │   │       │       │       │   └── medial_nucleus
│   │   │       │       │       │       └── __init__.py
│   │   │       │       │       └── hippocampus
│   │   │       │       │           ├── __init__.py
│   │   │       │       │           ├── cornu_ammonis
│   │   │       │       │           │   ├── __init__.py
│   │   │       │       │           │   ├── ca1
│   │   │       │       │           │   │   └── __init__.py
│   │   │       │       │           │   ├── ca2
│   │   │       │       │           │   │   └── __init__.py
│   │   │       │       │           │   ├── ca3
│   │   │       │       │           │   │   └── __init__.py
│   │   │       │       │           │   └── ca4
│   │   │       │       │           │       └── __init__.py
│   │   │       │       │           ├── dentate_gyrus
│   │   │       │       │           │   └── __init__.py
│   │   │       │       │           ├── parasubiculum
│   │   │       │       │           │   └── __init__.py
│   │   │       │       │           ├── presubiculum
│   │   │       │       │           │   └── __init__.py
│   │   │       │       │           └── subiculum
│   │   │       │       │               └── __init__.py
│   │   │       │       └── white_matter
│   │   │       │           ├── __init__.py
│   │   │       │           ├── centrum_semiovale
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── cingulum
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── corona_radiata
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── external_capsule
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── extreme_capsule
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── fasciculus_rectus
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── fornix
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── internal_capsule
│   │   │       │           │   └── __init__.py
│   │   │       │           ├── mammillothalamic_tract
│   │   │       │           │   └── __init__.py
│   │   │       │           └── medial_forebrain_bundle
│   │   │       │               └── __init__.py
│   │   │       ├── commissures
│   │   │       │   ├── __init__.py
│   │   │       │   ├── anterior_commissure
│   │   │       │   │   └── __init__.py
│   │   │       │   └── corpus_callosum
│   │   │       │       └── __init__.py
│   │   │       └── lateral_ventricles
│   │   │           ├── __init__.py
│   │   │           ├── left
│   │   │           │   └── __init__.py
│   │   │           └── right
│   │   │               └── __init__.py
│   │   ├── hindbrain
│   │   │   ├── __init__.py
│   │   │   ├── metencephalon
│   │   │   │   ├── __init__.py
│   │   │   │   ├── cerebellum
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── deep_white_matter
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── hemispheres
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── anterior_lobe
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   ├── flocculonodular_lobe
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── posterior_lobe
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   └── right
│   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │       ├── anterior_lobe
│   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │       ├── flocculonodular_lobe
│   │   │   │   │   │       │   └── __init__.py
│   │   │   │   │   │       └── posterior_lobe
│   │   │   │   │   │           └── __init__.py
│   │   │   │   │   ├── nuclei
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── dentate_nucleus
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── right
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   ├── fastigial_nucleus
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── left
│   │   │   │   │   │   │   │   └── __init__.py
│   │   │   │   │   │   │   └── right
│   │   │   │   │   │   │       └── __init__.py
│   │   │   │   │   │   └── interposed_nucleus
│   │   │   │   │   │       ├── __init__.py
│   │   │   │   │   │       ├── emboliform_nucleus
│   │   │   │   │   │       │   ├── __init__.py
│   │   │   │   │   │       │   ├── left
│   │   │   │   │   │       │   │   └── __init__.py
│   │   │   │   │   │       │   └── right
│   │   │   │   │   │       │       └── __init__.py
│   │   │   │   │   │       └── globose_nucleus
│   │   │   │   │   │           ├── __init__.py
│   │   │   │   │   │           ├── left
│   │   │   │   │   │           │   └── __init__.py
│   │   │   │   │   │           └── right
│   │   │   │   │   │               └── __init__.py
│   │   │   │   │   └── vermis
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── anterior_lobe
│   │   │   │   │       │   └── __init__.py
│   │   │   │   │       ├── flocculonodular_lobe
│   │   │   │   │       │   └── __init__.py
│   │   │   │   │       └── posterior_lobe
│   │   │   │   │           └── __init__.py
│   │   │   │   ├── fourth_ventricle
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── median_aperture
│   │   │   │   │       └── __init__.py
│   │   │   │   └── pons
│   │   │   │       ├── __init__.py
│   │   │   │       ├── caudal_pontine_reticular_nucleus
│   │   │   │       │   └── __init__.py
│   │   │   │       ├── cerebellar_peduncles
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── inferior_cerebellar_peduncle
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   ├── middle_cerebellar_peduncle
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   └── superior_cerebellar_peduncle
│   │   │   │       │       └── __init__.py
│   │   │   │       ├── cranial_nerve_nuclei
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── left
│   │   │   │       │   │   ├── __init__.py
│   │   │   │       │   │   ├── abducens_nucleus
│   │   │   │       │   │   │   └── __init__.py
│   │   │   │       │   │   ├── chief_sensory_trigeminal_nucleus
│   │   │   │       │   │   │   └── __init__.py
│   │   │   │       │   │   ├── facial_nerve_nucleus
│   │   │   │       │   │   │   └── __init__.py
│   │   │   │       │   │   ├── motor_trigeminal_nucleus
│   │   │   │       │   │   │   └── __init__.py
│   │   │   │       │   │   ├── superior_salivatory_nucleus
│   │   │   │       │   │   │   └── __init__.py
│   │   │   │       │   │   └── vestibulocochlear_nuclei
│   │   │   │       │   │       ├── __init__.py
│   │   │   │       │   │       ├── cochlear_nuclei
│   │   │   │       │   │       │   └── __init__.py
│   │   │   │       │   │       └── vestibular_nuclei
│   │   │   │       │   │           └── __init__.py
│   │   │   │       │   └── right
│   │   │   │       │       ├── __init__.py
│   │   │   │       │       ├── abducens_nucleus
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       ├── chief_sensory_trigeminal_nucleus
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       ├── facial_nerve_nucleus
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       ├── motor_trigeminal_nucleus
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       ├── superior_salivatory_nucleus
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       └── vestibulocochlear_nuclei
│   │   │   │       │           ├── __init__.py
│   │   │   │       │           ├── cochlear_nuclei
│   │   │   │       │           │   └── __init__.py
│   │   │   │       │           └── vestibular_nuclei
│   │   │   │       │               └── __init__.py
│   │   │   │       ├── parabrachial_area
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── lateral_parabrachial_nucleus
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   ├── medial_parabrachial_nucleus
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   └── subparabrachial_nucleus
│   │   │   │       │       ├── __init__.py
│   │   │   │       │       ├── kolliker_fuse_nucleus
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       └── pontine_respiratory_group
│   │   │   │       │           └── __init__.py
│   │   │   │       ├── paramedian_pontine_reticular_formation
│   │   │   │       │   └── __init__.py
│   │   │   │       ├── parvocellular_reticular_nucleus
│   │   │   │       │   └── __init__.py
│   │   │   │       ├── pontine_nuclei
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── left
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   └── right
│   │   │   │       │       └── __init__.py
│   │   │   │       ├── superior_olivary_complex
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── lateral_superior_olive
│   │   │   │       │   │   ├── __init__.py
│   │   │   │       │   │   ├── left
│   │   │   │       │   │   │   └── __init__.py
│   │   │   │       │   │   └── right
│   │   │   │       │   │       └── __init__.py
│   │   │   │       │   ├── medial_nucleus_of_trapezoid_body
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   └── medial_superior_olive
│   │   │   │       │       ├── __init__.py
│   │   │   │       │       ├── left
│   │   │   │       │       │   └── __init__.py
│   │   │   │       │       └── right
│   │   │   │       │           └── __init__.py
│   │   │   │       └── tegmentum
│   │   │   │           ├── __init__.py
│   │   │   │           ├── laterodorsal_tegmental_nucleus
│   │   │   │           │   └── __init__.py
│   │   │   │           ├── locus_coeruleus
│   │   │   │           │   └── __init__.py
│   │   │   │           ├── nucleus_incertus
│   │   │   │           │   └── __init__.py
│   │   │   │           ├── pedunculopontine_nucleus
│   │   │   │           │   └── __init__.py
│   │   │   │           ├── pontine_micturition_center
│   │   │   │           │   └── __init__.py
│   │   │   │           └── tegmental_pontine_reticular_nucleus
│   │   │   │               └── __init__.py
│   │   │   └── myelencephalon
│   │   │       ├── __init__.py
│   │   │       └── medulla_oblongata
│   │   │           ├── __init__.py
│   │   │           ├── arcuate_nucleus
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           ├── caudal_ventrolateral_medulla
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           ├── cranial_nerve_nuclei
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── dorsal_motor_nucleus_vagus
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   ├── hypoglossal_nucleus
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   ├── inferior_salivatory_nucleus
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── nucleus_ambiguus
│   │   │           │   │       └── __init__.py
│   │   │           │   └── right
│   │   │           │       ├── __init__.py
│   │   │           │       ├── dorsal_motor_nucleus_vagus
│   │   │           │       │   └── __init__.py
│   │   │           │       ├── hypoglossal_nucleus
│   │   │           │       │   └── __init__.py
│   │   │           │       ├── inferior_salivatory_nucleus
│   │   │           │       │   └── __init__.py
│   │   │           │       └── nucleus_ambiguus
│   │   │           │           └── __init__.py
│   │   │           ├── medullary_pyramid
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           ├── olivary_body
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   └── inferior_olivary_nucleus
│   │   │           │   │       └── __init__.py
│   │   │           │   └── right
│   │   │           │       ├── __init__.py
│   │   │           │       └── inferior_olivary_nucleus
│   │   │           │           └── __init__.py
│   │   │           ├── parafacial_zone
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           ├── paramedian_reticular_nucleus
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           ├── perihypoglossal_nuclei
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── intercalated_nucleus
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── prepositus_nucleus
│   │   │           │   │       └── __init__.py
│   │   │           │   └── right
│   │   │           │       ├── __init__.py
│   │   │           │       ├── intercalated_nucleus
│   │   │           │       │   └── __init__.py
│   │   │           │       └── prepositus_nucleus
│   │   │           │           └── __init__.py
│   │   │           ├── respiratory_center
│   │   │           │   ├── __init__.py
│   │   │           │   ├── area_postrema
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── left
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── right
│   │   │           │   │       └── __init__.py
│   │   │           │   ├── chemoreceptor_trigger_zone
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── left
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── right
│   │   │           │   │       └── __init__.py
│   │   │           │   ├── cuneate_nucleus
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── left
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── right
│   │   │           │   │       └── __init__.py
│   │   │           │   ├── dorsal_respiratory_group
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── left
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── right
│   │   │           │   │       └── __init__.py
│   │   │           │   ├── gigantocellular_reticular_nucleus
│   │   │           │   │   ├── __init__.py
│   │   │           │   │   ├── left
│   │   │           │   │   │   └── __init__.py
│   │   │           │   │   └── right
│   │   │           │   │       └── __init__.py
│   │   │           │   └── gracile_nucleus
│   │   │           │       ├── __init__.py
│   │   │           │       ├── left
│   │   │           │       │   └── __init__.py
│   │   │           │       └── right
│   │   │           │           └── __init__.py
│   │   │           ├── rostral_ventrolateral_medulla
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           ├── solitary_nucleus
│   │   │           │   ├── __init__.py
│   │   │           │   ├── left
│   │   │           │   │   └── __init__.py
│   │   │           │   └── right
│   │   │           │       └── __init__.py
│   │   │           └── ventral_respiratory_group
│   │   │               ├── __init__.py
│   │   │               ├── left
│   │   │               │   ├── __init__.py
│   │   │               │   ├── botzinger_complex
│   │   │               │   │   └── __init__.py
│   │   │               │   ├── nucleus_para_ambiguus
│   │   │               │   │   └── __init__.py
│   │   │               │   ├── nucleus_retroambiguus
│   │   │               │   │   └── __init__.py
│   │   │               │   ├── nucleus_retrofacialis
│   │   │               │   │   └── __init__.py
│   │   │               │   ├── pre_botzinger_complex
│   │   │               │   │   └── __init__.py
│   │   │               │   └── retrotrapezoid_nucleus
│   │   │               │       └── __init__.py
│   │   │               └── right
│   │   │                   ├── __init__.py
│   │   │                   ├── botzinger_complex
│   │   │                   │   └── __init__.py
│   │   │                   ├── nucleus_para_ambiguus
│   │   │                   │   └── __init__.py
│   │   │                   ├── nucleus_retroambiguus
│   │   │                   │   └── __init__.py
│   │   │                   ├── nucleus_retrofacialis
│   │   │                   │   └── __init__.py
│   │   │                   ├── pre_botzinger_complex
│   │   │                   │   └── __init__.py
│   │   │                   └── retrotrapezoid_nucleus
│   │   │                       └── __init__.py
│   │   ├── midbrain
│   │   │   ├── __init__.py
│   │   │   ├── cerebral_peduncle
│   │   │   │   ├── __init__.py
│   │   │   │   ├── left
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── crus_cerebri
│   │   │   │   │       └── __init__.py
│   │   │   │   └── right
│   │   │   │       ├── __init__.py
│   │   │   │       └── crus_cerebri
│   │   │   │           └── __init__.py
│   │   │   ├── cranial_nerve_nuclei
│   │   │   │   ├── __init__.py
│   │   │   │   ├── left
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── edinger_westphal_nucleus
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── mesencephalic_trigeminal_nucleus
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   ├── oculomotor_nucleus
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── trochlear_nucleus
│   │   │   │   │       └── __init__.py
│   │   │   │   └── right
│   │   │   │       ├── __init__.py
│   │   │   │       ├── edinger_westphal_nucleus
│   │   │   │       │   └── __init__.py
│   │   │   │       ├── mesencephalic_trigeminal_nucleus
│   │   │   │       │   └── __init__.py
│   │   │   │       ├── oculomotor_nucleus
│   │   │   │       │   └── __init__.py
│   │   │   │       └── trochlear_nucleus
│   │   │   │           └── __init__.py
│   │   │   ├── mesencephalic_aqueduct
│   │   │   │   └── __init__.py
│   │   │   ├── pretectum
│   │   │   │   └── __init__.py
│   │   │   ├── tectum
│   │   │   │   ├── __init__.py
│   │   │   │   └── corpora_quadrigemina
│   │   │   │       ├── __init__.py
│   │   │   │       ├── left
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── inferior_colliculus
│   │   │   │       │   │   └── __init__.py
│   │   │   │       │   └── superior_colliculus
│   │   │   │       │       └── __init__.py
│   │   │   │       └── right
│   │   │   │           ├── __init__.py
│   │   │   │           ├── inferior_colliculus
│   │   │   │           │   └── __init__.py
│   │   │   │           └── superior_colliculus
│   │   │   │               └── __init__.py
│   │   │   └── tegmentum
│   │   │       ├── __init__.py
│   │   │       ├── caudal_linear_nucleus
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── dorsal_raphe_nucleus
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── interpeduncular_nucleus
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── midbrain_reticular_formation
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── periaqueductal_gray
│   │   │       │   └── __init__.py
│   │   │       ├── red_nucleus
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── rostral_interstitial_nucleus_mlf
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── rostral_linear_nucleus_raphe
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   └── __init__.py
│   │   │       │   └── right
│   │   │       │       └── __init__.py
│   │   │       ├── substantia_nigra
│   │   │       │   ├── __init__.py
│   │   │       │   ├── left
│   │   │       │   │   ├── __init__.py
│   │   │       │   │   ├── pars_compacta
│   │   │       │   │   │   └── __init__.py
│   │   │       │   │   └── pars_reticulata
│   │   │       │   │       └── __init__.py
│   │   │       │   └── right
│   │   │       │       ├── __init__.py
│   │   │       │       ├── pars_compacta
│   │   │       │       │   └── __init__.py
│   │   │       │       └── pars_reticulata
│   │   │       │           └── __init__.py
│   │   │       └── ventral_tegmental_area
│   │   │           ├── __init__.py
│   │   │           ├── left
│   │   │           │   ├── __init__.py
│   │   │           │   ├── parabrachial_pigmented_nucleus
│   │   │           │   │   └── __init__.py
│   │   │           │   ├── paranigral_nucleus
│   │   │           │   │   └── __init__.py
│   │   │           │   └── rostromedial_tegmental_nucleus
│   │   │           │       └── __init__.py
│   │   │           └── right
│   │   │               ├── __init__.py
│   │   │               ├── parabrachial_pigmented_nucleus
│   │   │               │   └── __init__.py
│   │   │               ├── paranigral_nucleus
│   │   │               │   └── __init__.py
│   │   │               └── rostromedial_tegmental_nucleus
│   │   │                   └── __init__.py
│   │   └── spinal_cord
│   │       ├── __init__.py
│   │       ├── gray_matter
│   │       │   ├── __init__.py
│   │       │   ├── left
│   │       │   │   ├── __init__.py
│   │       │   │   ├── dorsal_horn
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── lateral_horn
│   │       │   │   │   └── __init__.py
│   │       │   │   └── ventral_horn
│   │       │   │       └── __init__.py
│   │       │   └── right
│   │       │       ├── __init__.py
│   │       │       ├── dorsal_horn
│   │       │       │   └── __init__.py
│   │       │       ├── lateral_horn
│   │       │       │   └── __init__.py
│   │       │       └── ventral_horn
│   │       │           └── __init__.py
│   │       └── white_matter
│   │           ├── __init__.py
│   │           ├── left
│   │           │   ├── __init__.py
│   │           │   ├── corticospinal_tract
│   │           │   │   └── __init__.py
│   │           │   ├── dorsal_columns
│   │           │   │   └── __init__.py
│   │           │   └── spinothalamic_tract
│   │           │       └── __init__.py
│   │           └── right
│   │               ├── __init__.py
│   │               ├── corticospinal_tract
│   │               │   └── __init__.py
│   │               ├── dorsal_columns
│   │               │   └── __init__.py
│   │               └── spinothalamic_tract
│   │                   └── __init__.py
│   ├── chemicals_hormones
│   │   ├── 01_hpg_axis_androgens_reproduction
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 02_hpa_axis_stress_survival
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 03_metabolic_thyroid_growth
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 04_satiety_gut_energy_signaling
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 05_neuro_modulators_mood
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 06_social_territorial_bonding
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 07_fluid_electrolyte_structural
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 08_immune_inflammation_defense
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 09_structural_anchors_transporters_catalysts
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 10_circadian_gating_epigenetic_clocks
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   ├── 11_xenobiotic_defense_phase_i_iii_detox
│   │   │   ├── __init__.py
│   │   │   └── hormones.yaml
│   │   └── 12_gasotransmitters_vascular_dynamics
│   │       ├── __init__.py
│   │       └── hormones.yaml
│   └── memory
│       ├── analytics.py
│       ├── backends
│       │   ├── __init__.py
│       │   ├── chroma.py
│       │   └── in_memory.py
│       ├── base.py
│       ├── forgetting.py
│       ├── stores
│       │   ├── __init__.py
│       │   ├── long_term
│       │   │   ├── __init__.py
│       │   │   ├── explicit
│       │   │   │   ├── __init__.py
│       │   │   │   ├── episodic
│       │   │   │   │   └── __init__.py
│       │   │   │   └── semantic
│       │   │   │       └── __init__.py
│       │   │   └── implicit
│       │   │       ├── __init__.py
│       │   │       ├── classical_associative_conditioning
│       │   │       │   └── __init__.py
│       │   │       ├── emotional_valence
│       │   │       │   └── __init__.py
│       │   │       ├── implicit_social_cognitive
│       │   │       │   └── __init__.py
│       │   │       ├── motor_sensorimotor_adaptation
│       │   │       │   └── __init__.py
│       │   │       ├── non_sociative_learning
│       │   │       │   └── __init__.py
│       │   │       ├── priming
│       │   │       │   └── __init__.py
│       │   │       ├── procedural
│       │   │       │   └── __init__.py
│       │   │       ├── reinforcement_value_based_learning
│       │   │       │   └── __init__.py
│       │   │       ├── stimulus_response_s_r_learning
│       │   │       │   └── __init__.py
│       │   │       └── temporal_sequence_learning
│       │   │           └── __init__.py
│       │   └── short_term
│       │       └── __init__.py
│       ├── system.py
│       └── vector.py
├── scripts
│   └── __init__.py
└── ui
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