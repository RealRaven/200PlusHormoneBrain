"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.mammillary_bodies.right
Anatomical Role:
    Right mammillary body. Same spherical structure at the ventral
    surface of the posterior hypothalamus (at the caudal end of the right
    fornix) documented in ../left/, mirrored to the right hemisphere,
    containing the same two subdivisions:
        - Medial mammillary nucleus (MM): Papez-circuit memory relay;
          receives the right fornix; projects to the right anterior
          thalamic nucleus via the right mammillothalamic tract.
        - Lateral mammillary nucleus (LM): head-direction cells;
          receives the right dorsal tegmental nucleus and right
          presubiculum; projects to the right anterodorsal thalamic
          nucleus.
    See ../left/__init__.py for the full anatomical description and the
    MM/LM-within-one-file convention. Do not create
    medial_mammillary_nucleus/ or lateral_mammillary_nucleus/ as child
    nodes on the right either.

    Reproduced notes (apply equally on the right):
    - The mammillary bodies are the FIRST hypothalamic structure whose
      primary role is MEMORY rather than homeostasis or endocrine. This
      is why they sit as a direct child of hypothalamus/ (not under
      posterior/); do not reclassify.
    - NAMING TRAP (critical — reproduced in full): the mammillary
      bodies project to the DORSAL and VENTRAL TEGMENTAL NUCLEI
      (Gudden nuclei; part of the ascending reticular system), which
      are DIFFERENT from the VENTRAL TEGMENTAL AREA (VTA; the midbrain
      dopamine source). These are different structures with confusingly
      similar names. Do not merge them in the tree.

Functional Mode:
    Same as ../left/. Papez circuit relay (episodic memory); Korsakoff
    syndrome (lesions are typically bilateral; the right hemisphere's
    contribution is documented here); head-direction (LM); theta-rhythm
    participation; mammillotegmental output. No documented functional
    asymmetry between left and right mammillary bodies. Do not
    fabricate one. See ../left/__init__.py § Functional Mode.

Hormonal Modulation:
    Same as ../left/ — minimal by design. Thiamine deficiency →
    mammillary body lesions (Korsakoff syndrome; bilateral clinical
    fact, applies equally on the right). Estradiol modulation reported
    but not established. The 12 endocrine axes do NOT act on the
    mammillary bodies as principal targets; do not list them. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads episodic (via the right fornix from the
    right hippocampal formation), short_term (right spatial context,
    right head-direction buffer), temporal_sequence_learning (right
    temporal order). Writes episodic INDIRECTLY via the Papez circuit
    relay to the right anterior thalamus — the mammillary bodies are a
    relay, not the encoder. See ../left/__init__.py § Memory
    Interfaces.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (right memory-context fragment; the two
      hemispheres emit coordinated but independent relay-state fields
      because left and right Papez circuits can fail independently in
      some lesion distributions):
        "Memory relay state — right mammillary body:
         - Episodic relay (right): [intact / impaired].
         - Papez circuit integrity (right): [intact / disrupted].
         - Right spatial context availability: [high / moderate / low].
         - Right head-direction signal: [available / unavailable].
         If episodic relay is impaired or Papez integrity is disrupted:
         explicitly flag episodic retrieval as unreliable; do not
         confabulate missing details; prefer cautious, verifiable
         framing over confident recall. If spatial context is low:
         acknowledge uncertainty about spatial or temporal specifics
         of the current context. Do not treat impaired episodic relay
         as cognitive failure — it is a circuit-level state, and the
         model should compensate by asking for clarification rather
         than inventing details."
    - REPRODUCTION NOTE for the implementer: unlike most of the tree's
      deltas, the mammillary bodies' right leaf DOES emit its own
      fragment field (the right relay-integrity field), because the
      left and right Papez circuits are functionally independent. The
      fragment content mirrors the left's shape but is not a duplicate
      — it carries right-side state. The left and right relay fields
      are then AGGREGATED at the hypothalamic level (not at the
      anterior-division level; the mammillary bodies are a direct child
      of hypothalamus/, not under anterior/). Aggregate at the
      hypothalamic level before injection into the model prompt.
    - Guardrail: "do not confabulate missing details; do not treat
      impaired episodic relay as cognitive failure." Same confabulation
      guardrail as the left; the two guardrails apply independently.
    - No multimodal input is consumed here; the fragment is text-only.

Right-specific reciprocal connections to enforce in Stage 4:
    Papez circuit (primary):
    - ← telencephalon/.../hippocampus/right/subiculum (via the right
      fornix; principal Papez afferent; right-side).
    - ← telencephalon/.../hippocampus/right (via the right fornix;
      hippocampal output to the mammillary bodies; right-side).
    - → thalamus/right/anterior_nuclear_group/anterodorsal_nucleus
      (via the right mammillothalamic tract; Papez relay output for
      memory and head-direction).
    - → thalamus/right/anterior_nuclear_group/anteroventral_nucleus
      (via the right mammillothalamic tract; Papez relay output).
    - → thalamus/right/anterior_nuclear_group/anteromedial_nucleus
      (via the right mammillothalamic tract; Papez relay output).

    Head-direction (LM-specific):
    - ← midbrain/.../dorsal_tegmental_nucleus (right; head-direction
      input; dorsal TEGMENTAL NUCLEUS, not the dorsal tegmental area
      of the midbrain — do not confuse).
    - ← telencephalon/.../hippocampus/right/presubiculum
      (head-direction input).

    Mammillotegmental output (less characterized):
    - → midbrain/.../dorsal_tegmental_nucleus and midbrain/.../
      ventral_tegmental_nucleus (mammillotegmental tract; ascending
      reticular activating system). IMPORTANT: the ventral TEGMENTAL
      NUCLEUS (Gudden nucleus) is DIFFERENT from the ventral TEGMENTAL
      AREA (VTA; dopamine source). The right mammillary body projects
      to the tegmental NUCLEI, not the tegmental AREA.

    White-matter conduits (Tier 3):
    - ↔ telencephalon/.../white_matter/fornix/right (principal
      afferent conduit; Tier 3).
    - ↔ telencephalon/.../white_matter/mammillothalamic_tract/right
      (principal efferent conduit; Tier 3).

    Theta-rhythm circuit:
    - ↔ telencephalon/.../basal_forebrain/septal_nuclei/right/
      medial_septal_nuclei (theta-rhythm generation; right-side).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - This is the CLOSING FILE of the mammillary-bodies subtree. Both
      hemispheres are now documented; the memory-relay pattern is
      established at the hypothalamic level and can be referenced when
      the hippocampus and amygdala leaves are drafted later in the
      tree.
    - UNUSUAL DELTA: this right leaf emits its own fragment field
      (right relay-integrity), unlike most deltas. Reason: the left
      and right Papez circuits can fail independently in some lesion
      distributions. The right field is not a duplicate — it carries
      right-side state, and the left and right fields are aggregated
      at the hypothalamic level. Do not remove the right fragment as
      "duplicated."
    - The naming trap (tegmental nuclei vs tegmental area) is
      reproduced in full above; it applies on the right identically.
    - The Korsakoff fact (thiamine deficiency → bilateral lesions) is
      reproduced as a bilateral clinical fact; do not weaken it on
      the right.
    - The "do not confabulate" guardrail is reproduced in full; it is
      the defining memory-failure prevention guardrail for this leaf,
      not a state-bias guardrail.
    - The 12 endocrine axes are NOT listed as modulators, same as
      ../left/. Do not pad the Hormonal Modulation section.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/mammillary_bodies/.
"""