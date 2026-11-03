"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.medial_area.mammillary_nuclei
Anatomical Role:
    The posterior-division compartment of the mammillary bodies. This
    node EXISTS as a pointer, not as a content holder. It and
    hypothalamus/mammillary_bodies/left|right/ refer to the SAME
    anatomical structure, documented in two tree locations for two
    different purposes:

        - hypothalamus/mammillary_bodies/left|right/ — the FULL
          memory-hub leaf. Role, function, hormones (minimal; thiamine
          deficiency → Korsakoff), memory interfaces (indirect episodic
          write via the Papez circuit), model fragment (confabulation
          guardrail), all reciprocal connections (fornix, anterior
          thalamus, tegmental nuclei, hippocampus, subiculum,
          presubiculum, medial septal nuclei, mammillothalamic tract,
          mammillothalamic tract, medial forebrain bundle).
        - posterior/medial_area/mammillary_nuclei/left|right/ (THIS
          node and its children) — the posterior-division compartment.
          Pointers only. Records that the mammillary bodies sit in the
          posterior division of the hypothalamus (for tree
          completeness), but does NOT duplicate content.

    STRUCTURAL IDENTITY TRAP (reproduced from
    posterior/medial_area/__init__.py — the trap must be declared at
    every level where it appears):
    posterior/medial_area/mammillary_nuclei/left|right/ and
    hypothalamus/mammillary_bodies/left|right/ are the SAME anatomical
    structure. The mammillary bodies are a paired ventral-surface
    structure containing the medial and lateral mammillary nuclei. Stage
    4 audit MUST treat them as ONE structure. Do not flag as duplicates.
    Do not merge the nodes. Do not duplicate content. The children here
    are DELTAS pointing to mammillary_bodies/left|right/.

    The full content lives in mammillary_bodies/left|right/ — not here,
    not in the children. The children reproduce the trap declaration
    and record only the posterior-division compartmentalization.

Functional Mode:
    Same as hypothalamus/mammillary_bodies/left|right/ § Functional
    Mode. Do NOT restate:
    - Papez circuit relay (episodic memory).
    - Korsakoff syndrome (thiamine deficiency, bilateral lesions).
    - Head-direction (LM, via anterodorsal thalamic nucleus).
    - Theta-rhythm participation.
    - Mammillotegmental output (dorsal/ventral tegmental nuclei).
    The children point to mammillary_bodies/left|right/ for the full
    functional description; this container does not.

Hormonal Modulation:
    Same as hypothalamus/mammillary_bodies/left|right/ § Hormonal
    Modulation. Minimal by design (thiamine is the defining clinical
    modulator, though a vitamin; the 12 endocrine axes do not target
    the mammillary bodies as principal structures). DO NOT duplicate.

Memory Interfaces:
    Same as hypothalamus/mammillary_bodies/left|right/ § Memory
    Interfaces. Reads episodic, short_term, temporal_sequence_learning;
    writes episodic INDIRECTLY via the Papez circuit (the mammillary
    bodies are a relay, not the encoder). DO NOT duplicate.

Model Integration (Gemma-4-E2B):
    No fragment emitted here. The mammillary memory-relay fragment
    (with its confabulation guardrail) is emitted by
    hypothalamus/mammillary_bodies/left|right/, at the hypothalamic
    level, NOT by this container and NOT by the children. Do not emit
    a duplicate memory fragment from the posterior-division compartment;
    doing so would double-count the memory-relay signal.

Children (two children — both DELTAS, not full leaves):
    - left/    Delta of hypothalamus/mammillary_bodies/left/. Records
                 only the posterior-division compartmentalization
                 (this node sits in posterior/medial_area/, the full
                 leaf sits at hypothalamus/mammillary_bodies/). The
                 full content lives at the target.
    - right/   Delta of hypothalamus/mammillary_bodies/right/. Same
                 shape; right-side compartmentalization note.

    These children are NOT full leaves. If a future contributor writes
    them as full leaves, the content will duplicate mammillary_bodies/
    left|right/ and the Stage 4 audit will flag a duplicate. The
    trap declaration in this file (and in each child) is the specific
    mechanism preventing this.

Notes:
    - THIS CONTAINER EXISTS AS A POINTER. It has no content of its own
      beyond the trap declaration. Its left/ and right/ children are
      deltas of mammillary_bodies/left|right/, not full leaves.
    - STRUCTURAL IDENTITY TRAP declaration reproduced at container
      level. The trap was declared at posterior/medial_area/__init__.py
      (the parent), and must be reproduced here and in each delta child
      so a contributor entering at any level sees it.
    - DO NOT duplicate: functional mode, hormonal modulation, memory
      interfaces, model fragment, or any of the mammillary bodies'
      reciprocal connections. All live in mammillary_bodies/left|right/.
    - DO NOT write left/ and right/ as full leaves. They are deltas.
    - The Korsakoff clinical fact (thiamine deficiency → bilateral
      mammillary body lesions) applies on both sides; the delta
      children should reproduce the fact statement in abbreviated form
      (see their files when drafted) so a contributor reading only the
      posterior-division compartment still sees the clinical relevance.
      But the FULL Korsakoff description (Wernicke encephalopathy,
      anterograde amnesia, confabulation, preserved procedural memory)
      lives in mammillary_bodies/left/ and is NOT duplicated here.
    - The mammillary bodies' memory-write interface (indirect episodic
      via the Papez circuit) is the file's most important memory
      feature and must not be lost in the compartmentalization. The
      delta children must point to it explicitly in their Memory
      Interfaces sections.
    - This node and its children are the ONLY tree location where the
      "same structure, two tree locations" pattern appears. It has no
      equivalent elsewhere. Handle carefully.
    - The thalamic PVT vs. hypothalamic PVN trap does NOT apply here
      (that is a posterior/lateral_area/ and posterior_nucleus/ concern,
      not a mammillary-nuclei concern).
    - Vocabulary used above is defined in Stage 0 files; see
      hypothalamus/mammillary_bodies/left|right/ § Notes for the full
      list (thiamine is documented directly, not via the 12 axes).
    - Reciprocal connections to enforce in Stage 4:
        * posterior/medial_area/mammillary_nuclei/left ↔
          hypothalamus/mammillary_bodies/left (SAME STRUCTURE; Stage 4
          must treat as one; do not flag as duplicate).
        * posterior/medial_area/mammillary_nuclei/right ↔
          hypothalamus/mammillary_bodies/right (SAME STRUCTURE; same
          treatment).
        * All other mammillary bodies connections (fornix, anterior
          thalamus, tegmental nuclei, hippocampus, subiculum,
          presubiculum, medial septal nuclei, mammillothalamic tract,
          medial forebrain bundle) are declared in mammillary_bodies/
          left|right/, NOT here. Do not duplicate.
    - Connects upward to hypothalamus/posterior/medial_area/.
"""