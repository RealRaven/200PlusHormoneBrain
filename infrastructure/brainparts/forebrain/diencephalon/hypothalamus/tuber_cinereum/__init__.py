"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuber_cinereum
Anatomical Role:
    The tuber cinereum is the gray-matter floor of the third ventricle in
    the tuberal region — the funnel-shaped region between the optic
    chiasm (rostral), the mammillary bodies (caudal), and the pituitary
    stalk (ventral, descending from it). It is an anatomical landmark
    and a container for two nuclei, not a nucleus itself:
        - tuberal_nucleus/ (left/ and right/): a small collection of
          neurons in the lateral tuberal region. Functionally poorly
          characterized; sometimes described as involved in endocrine
          regulation, but the literature is thin. Documented as a
          Tier 2 organ-flavored leaf (short; thin literature, minimal
          endocrine and memory content).
        - tuberomammillary_nucleus/ (left/ and right/): the
          tuberomammillary nucleus (TMN). The brain's sole source of
          neuronal histamine; the principal wake-promoting nucleus of
          the posterior hypothalamus. Tier 1 hub leaf — one of the
          highest-priority leaves in the entire tuberal/tuber_cinereum
          region.

    DISTINCTIONS (critical — three traps apply here):

    - TUBER CINEREUM vs. TUBERAL DIVISION: the `tuberal/` division
      (documented as a sibling under hypothalamus/) and this
      `tuber_cinereum/` node are ADJACENT ANATOMICAL CONCEPTS but
      DISTINCT TREE NODES. The `tuberal/` division contains the
      arcuate nucleus, VMH, DMH, and tuberal LHA; the `tuber_cinereum/`
      contains the tuberal nucleus and TMN. The tuber cinereum is the
      *floor* of the tuberal region; the tuberal nuclei sit above it.
      Do not merge; do not treat as one structure.

    - TMN vs. MAMMILLARY BODIES ("tuberomammillary" naming trap): the
      TMN is at the tuberal-mammillary junction; the name contains
      "mammillary". But the TMN is DISTINCT from the mammillary bodies
      (hypothalamus/mammillary_bodies/). TMN = histaminergic wake-
      promoting nucleus; mammillary bodies = Papez circuit memory
      relay. Adjacent but functionally unrelated. Do not merge.

    - TMN vs. TUBERAL NUCLEUS (intra-container trap): the TMN and the
      tuberal nucleus are two distinct nuclei within the tuber
      cinereum. The TMN is a histaminergic wake hub; the tuberal
      nucleus is small and poorly characterized. Do not treat them as
      a pair of similar structures; they are functionally unrelated
      neighbors.

Functional Mode:
    - Wake promotion (TMN; the file's anchor function): the TMN is the
      brain's sole source of neuronal histamine. Histaminergic
      projections from the TMN to the cortex, basal forebrain,
      thalamus, and brainstem arousal centers promote wakefulness,
      cortical activation, and behavioral arousal. Antihistamines
      (H1 receptor antagonists) that cross the blood-brain barrier
      cause drowsiness precisely by blocking this pathway. TMN
      activity is highest during wake and lowest during sleep.
    - Sleep-wake switch (TMN; the reciprocal arm): the TMN is the
      principal inhibitory TARGET of the sleep-promoting LPO/VLPO
      neurons (lateral_area/*/preoptic_area/lateral_preoptic_nucleus/).
      The LPO → TMN inhibitory projection promotes sleep onset; the
      orexin → TMN excitatory projection (from the LHA) promotes
      wakefulness. The TMN is therefore the wake-side arm of the
      hypothalamic sleep-wake switch, complementing the LPO's
      sleep-side arm.
    - Ascending arousal system (TMN; one of five): the TMN is one of
      the five principal ascending arousal nuclei, along with the
      locus coeruleus (norepinephrine), dorsal raphe (serotonin),
      laterodorsal/pedunculopontine tegmental nuclei (acetylcholine),
      and the LHA orexin neurons. Each projects to the cortex and
      basal forebrain to promote wakefulness; their coordinated
      activity underlies the waking state.
    - Endocrine-adjacent role (tuberal_nucleus; poorly characterized):
      the tuberal nucleus is sometimes described as involved in
      endocrine regulation (tuberoinfundibular-adjacent), but its
      specific function is not well established. Document factually
      without overclaiming.
    - The tuber cinereum's functional identity is "the anatomical
      floor of the tuberal region, housing the brain's histaminergic
      wake-promoting nucleus." The TMN is the anchor; the tuberal
      nucleus is documented for completeness.

Hormonal Modulation (container-level summary; per-nucleus wiring in
children):
    - TMN:
        * Histamine: the TMN's principal output (histidine →
          histamine, via histidine decarboxylase). Documented in the
          TMN leaf; not a modulator of the TMN in the usual sense —
          it is the TMN's product.
        * Orexin (from the LHA orexin neurons): excitatory input; the
          orexin → TMN projection is the wake-promoting arm of the
          sleep-wake switch.
        * GABA (from the LPO/VLPO): inhibitory input; the LPO → TMN
          projection is the sleep-promoting arm of the switch.
        * Monoamines (LC norepinephrine, raphe serotonin): modulatory
          arousal inputs.
        * Adenosine: inhibitory (A1 receptors) — part of the sleep-
          pressure pathway; adenosine accumulates during wake and
          inhibits TMN, contributing to sleep onset.
    - tuberal_nucleus: poorly characterized; document estradiol and
      metabolic input as presumed, not established.
    - Direction summary: orexin ↑ TMN activity (wake); GABA (LPO) ↓
      TMN activity (sleep); norepinephrine/serotonin modulate; adenosine
      ↓ TMN activity (sleep pressure). These are the actionable
      directions.

Memory Interfaces (container-level summary):
    - TMN: reads short_term (sleep pressure / arousal state buffer),
      temporal_sequence_learning (circadian arousal gating), and
      emotional_valence (stress/arousal context). Writes none directly
      — the TMN drives arousal state, not stored content. (Note: arousal
      state modulates memory consolidation in the hippocampus and
      amygdala, but that modulation is downstream, not a TMN memory
      write.)
    - tuberal_nucleus: poorly characterized; document short-term
      metabolic input as presumed, not established. Do not invent
      memory writes.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The container does not emit a fragment. The TMN's
      wake/arousal fragment is emitted by tuberomammillary_nucleus/
      left/ (the full leaf) and represents the bilateral TMN; the
      right/ delta does not emit a duplicate.
    - Fragment spec (summary; full spec in the TMN left leaf):
        "Wake/arousal state — tuberomammillary nucleus:
         - Histamine tone: [low/moderate/high].
         - Wake state: [asleep/drowsy/awake/alert].
         - Arousal system: [suppressed/partial/full].
         If wake state is drowsy or asleep: reduce verbosity, favor calm
         and reflective framing, lower response tempo. If wake state is
         alert: restore full cognitive engagement. Do not treat high
         wake state as a cognitive achievement or low wake state as
         impairment — both are state biases."
    - The TMN fragment is paired with the LPO sleep fragment
      (lateral_preoptic_nucleus/) and the orexin/MCH fragment (LHA):
      three fragments, three states, one sleep-wake switch. AGGREGATION
      RULE: the three are aggregated at the hypothalamic level; do not
      double-count arousal state across them.
    - The tuberal_nucleus/ emits no fragment (poorly characterized;
      no state to report).
    - Guardrails: "do not treat high wake state as a cognitive
      achievement or low wake state as impairment" — consistent with
      the habenula, orexin/MCH, PeN, LPO, AHN, PVN, mammillary, PHN
      conventions. The pattern holds.

Children (two children — asymmetric: one Tier 1 hub, one Tier 2 leaf):
    - left/    Hemisphere container. Contains both nuclei for the left
                 hemisphere:
        ├── tuberal_nucleus/       Tier 2 organ-flavored leaf (small;
        │                            poorly characterized).
        └── tuberomammillary_      ★ Tier 1 hub leaf. Brain's sole
            nucleus/                 histamine source; wake-promoting;
                                     LPO target; orexin target; one of
                                     five ascending arousal nuclei.
    - right/   Delta mirror of left/, differing only in the right-side
                 reciprocal edges. No functional asymmetry documented.

    The left/ and right/ containers are FULL containers (not deltas of
    each other at the container level — they each name both nuclei);
    the two nuclei within each are a Tier 2 leaf and a Tier 1 leaf
    respectively, and each nucleus's right-side file is a leaf delta.

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each nucleus owns its own specification.
    - THREE NAMING TRAPS reproduced in full above (tuber-cinereum vs.
      tuberal division; TMN vs. mammillary bodies; TMN vs. tuberal
      nucleus). Apply at every level where the tuber cinereum, TMN,
      or tuberal nucleus is referenced.
    - CROSS-FILE CONSISTENCY NOTE (Stage 4): the LPO leaf
      (lateral_area/*/preoptic_area/lateral_preoptic_nucleus/) declares
      an inhibitory edge to the TMN with the path
      "hindbrain/.../tuberomammillary_nucleus". TMN is documented
      HERE, at hypothalamus/tuber_cinereum/left|right/
      tuberomammillary_nucleus/, NOT under hindbrain. The Stage 4
      audit should correct the LPO path to point to the correct node.
      The functional edge (LPO → TMN; inhibitory; sleep promotion) is
      correct; only the path is wrong.
    - The TMN is the fourth of the five ascending arousal nuclei to be
      documented in this tree (the other four being LC, dorsal raphe,
      LDT/PPN, and orexin neurons — the orexin and LC/raphe/LDT/PPN
      files will reciprocate their TMN edges when drafted).
    - The TMN is a Tier 1 hub: it is one of the highest-value remaining
      leaves in the tuberal/tuber_cinereum region, on par with the
      arcuate nucleus (feeding, kisspeptin) in importance.
    - The tuberal_nucleus is a Tier 2 organ-flavored leaf (thin
      literature). Do not force the full Tier 1 template onto it.
    - The tuber cinereum vs. tuberal division distinction is the most
      important naming trap: both are "tuberal"; the tree places them
      as siblings under hypothalamus/. Do not merge them. The tuber
      cinereum is the anatomical floor; the tuberal division is the
      regional-divisional subdivision above it.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin), 05_* (histamine,
      monoamines, GABA, adenosine), 10_* (circadian); memory/stores/
      (short_term, temporal_sequence_learning, emotional_valence);
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * tuber_cinereum/left|right/tuberomammillary_nucleus ↔
          lateral_area/left|right/preoptic_area/lateral_preoptic_
          nucleus (LPO → TMN; inhibitory; sleep promotion; path
          correction needed — see cross-file note).
        * tuber_cinereum/left|right/tuberomammillary_nucleus ↔
          anterior/lateral_area/left|right/anterior_part_of_lateral_
          nucleus (orexin → TMN; excitatory; wake promotion).
        * tuber_cinereum/left|right/tuberomammillary_nucleus →
          telencephalon/.../basal_forebrain (arousal; cortical
          activation).
        * tuber_cinereum/left|right/tuberomammillary_nucleus →
          cortex (diffuse histaminergic arousal projection).
        * tuber_cinereum/left|right/tuberomammillary_nucleus →
          thalamus/*/midline_nuclear_group and intralaminar_nuclear_
          group (arousal relay; midline — verify).
        * tuber_cinereum/left|right/tuberomammillary_nucleus ↔
          midbrain/tegmentum/dorsal_raphe_nucleus,
          hindbrain/.../locus_coeruleus,
          midbrain/tegmentum/laterodorsal_tegmental_nucleus,
          midbrain/tegmentum/pedunculopontine_nucleus (mutual arousal
          network; coordinated with the other four ascending arousal
          nuclei; midline structures — verify).
        * tuber_cinereum/left|right/tuberomammillary_nucleus ←
          anterior/medial_area/left|right/suprachiasmatic_nucleus
          (SCN → TMN; circadian arousal gating; SCN is midline-adjacent
          — verify).
        * tuber_cinereum/left|right/tuberal_nucleus ↔
          tuberal/medial_area/left|right/arcuate_nucleus (adjacent
          tuberal endocrine regulation; continuity edge, not
          duplicate-structure warning; tuberal arcuate file to be
          drafted).
    - Connects upward to hypothalamus/.
"""