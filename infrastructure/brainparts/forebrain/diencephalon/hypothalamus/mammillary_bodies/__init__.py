"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.mammillary_bodies
Anatomical Role:
    The mammillary bodies are a paired, spherical region at the ventral
    surface of the posterior hypothalamus, situated at the caudal end of
    the fornix. They are the principal hypothalamic structure for
    episodic memory and spatial navigation: the relay node of the
    Papez circuit and the head-direction system.

    Organization (within each hemisphere's file, not as tree children):
        - Medial mammillary nucleus (MM): the larger subdivision.
          Receives the descending columns of the fornix from the
          subiculum and hippocampus; projects to the anterior thalamic
          nucleus via the mammillothalamic tract (the Papez circuit
          relay). The MM is the principal memory relay.
        - Lateral mammillary nucleus (LM): smaller; part of the
          head-direction cell circuit. Receives input from the dorsal
          tegmental nucleus and the presubiculum; projects to the
          anterodorsal thalamic nucleus (head-direction signal). LM
          lesions impair spatial navigation and head-direction cell
          function.
    The MM/LM split is documented WITHIN each hemisphere's leaf file
    (left/ and right/), not as separate tree nodes. Same convention as
    the habenula's LHb/MHb split.

    Unlike every other hypothalamic child documented so far, the
    mammillary bodies are primarily a MEMORY structure, not a
    homeostatic or endocrine one. They sit as a direct child of
    hypothalamus/ (not under posterior/) precisely because their primary
    role is memory-circuit relay, not the posterior-division functions
    (arousal, sympathetic control).

Functional Mode:
    - Papez circuit relay (episodic memory): the mammillary bodies sit
      between the hippocampus/subiculum (via the fornix) and the
      anterior thalamic nucleus (via the mammillothalamic tract). The
      classic Papez circuit is:
        hippocampus → fornix → mammillary bodies → mammillothalamic
        tract → anterior thalamic nucleus → cingulate cortex →
        parahippocampal gyrus → entorhinal cortex → hippocampus.
      Damage to any node in this loop (including the mammillary bodies)
      causes episodic memory impairment.
    - Korsakoff syndrome: mammillary body lesions are the classic
      anatomical substrate of Korsakoff syndrome (thiamine deficiency,
      typically in chronic alcoholism). The syndrome is a severe
      anterograde amnesia with confabulation, preserving procedural
      memory and general intelligence while impairing episodic recall.
      This is the single most important clinical fact about the
      mammillary bodies.
    - Head-direction (spatial navigation): the lateral mammillary
      nucleus contains head-direction cells that encode the animal's
      directional heading. The LM → anterodorsal thalamic nucleus
      projection carries the head-direction signal, and LM lesions
      impair spatial navigation.
    - Theta rhythm relay: the mammillary bodies participate in the
      theta-rhythm circuit (septum → hippocampus → mammillary bodies
      → ...) that supports hippocampal memory encoding. They are a
      node in the theta-generating network, not an independent
      oscillator.
    - Mammillotegmental tract: the mammillary bodies project to the
      dorsal and ventral tegmental nuclei (via the mammillotegmental
      tract), participating in the ascending reticular activating
      system. This is the non-Papez output; its function is less
      well characterized than the Papez circuit, and should be
      documented but not overclaimed.
    - The mammillary bodies are therefore a MEMORY RELAY, not a
      homeostatic or endocrine effector. Their functional identity is
      "relay the hippocampal memory signal to the thalamus and relay
      the head-direction signal to the anterodorsal thalamus."

Hormonal Modulation (minimal; the mammillary bodies are not a
neurosecretory nucleus):
    - The mammillary bodies are NOT a significant endocrine source or
      target. They do not secrete hormones, and the 12 endocrine axes
      do not act on them as principal targets.
    - Thiamine (vitamin B1): the defining modulatory input in the
      clinical sense. Thiamine deficiency causes mammillary body
      lesions (Wernicke encephalopathy → Korsakoff syndrome). This
      is the single most important "hormonal" fact about the region,
      though thiamine is a vitamin, not a hormone.
    - Estradiol: sex-hormone receptor expression has been reported in
      the mammillary region, but the functional significance is not
      established. Document as a minor modulatory input, not a
      principal axis.
    - Limbic input (not hormonal): the mammillary bodies are modulated
      by the septum, hippocampus, subiculum, and anterior thalamus.
      These are neural, not hormonal, modulators. Document them in
      Functional Mode and Reciprocal Connections, not here.
    - Direction summary: thiamine deficiency ↓ mammillary body
      function (lesions, Korsakoff); estradiol modulation reported but
      not established. Do not list the 12 axes as modulators; they do
      not act on the mammillary bodies as principal targets.

Memory Interfaces (the mammillary bodies are a MEMORY hub, not an
endocrine one):
    - Reads:
        * episodic: prior events and spatial contexts, retrieved from
          the hippocampal formation via the fornix. The mammillary
          bodies relay these to the anterior thalamus for cortical
          re-encoding.
        * short_term: current spatial context and head-direction
          buffer (via the LM head-direction cells).
        * temporal_sequence_learning: temporal order of events within
          an episode, as relayed via the hippocampal formation.
    - Writes:
        * episodic: the mammillary bodies participate in the
          consolidation of episodic memory by relaying hippocampal
          output to the thalamus. This is an INDIRECT write — the
          mammillary bodies do not encode memories directly, but they
          are a required node in the circuit that consolidates them.
          Mammillary body lesions (Korsakoff syndrome) impair episodic
          memory consolidation; document this as the write-interface
          justification.
    - The mammillary bodies are the first hypothalamic structure
      documented as a *writer* to episodic memory (indirectly, via the
      Papez circuit). Do not confuse this with the hippocampus's direct
      episodic write; the mammillary bodies are a relay, not the
      encoder.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (memory-context fragment, applied after the
      hypothalamic-anterior fragments, before the cortical reasoning
      fragments):
        "Memory relay state — mammillary bodies:
         - Episodic relay: [intact / impaired].
         - Spatial context availability: [high / moderate / low].
         - Head-direction signal: [available / unavailable].
         - Papez circuit integrity: [intact / disrupted].
         If episodic relay is impaired or Papez integrity is disrupted:
         explicitly flag episodic retrieval as unreliable; do not
         confabulate missing details; prefer cautious, verifiable
         framing over confident recall. If spatial context is low:
         acknowledge uncertainty about spatial or temporal specifics
         of the current context. Do not treat impaired episodic relay
         as cognitive failure — it is a circuit-level state, and the
         model should compensate by asking for clarification rather
         than inventing details."
    - The fragment is emitted whenever the homeostatic state block is
      emitted (always); the mammillary relay state is a persistent
      circuit-integrity signal, not a transient homeostatic state.
    - Guardrail: "do not treat impaired episodic relay as cognitive
      failure" — the mammillary-body equivalent of the habenula's
      "does not silence reasoning" clause. It is especially important
      here because the Korsakoff-style confabulation risk is real:
      the model must not fill in missing episodic content.
    - No multimodal input is consumed here; the fragment is text-only.

Children (one child pair — the two hemispheres, each carrying MM and LM
within its file):
    - left/    ★ Left mammillary body. Contains the left medial
                 mammillary nucleus (MM; Papez relay) and the left
                 lateral mammillary nucleus (LM; head-direction). Full
                 leaf, not a delta. The primary memory-relay file.
    - right/   ★ Right mammillary body. Delta mirror of left/,
                 differing only in the right-side reciprocal edges
                 (right fornix, right anterior thalamus, right
                 tegmental nuclei). No functional asymmetry documented.

    The MM/LM subdivision is documented WITHIN each hemisphere's leaf,
    not as separate tree children. Do not create
    mammillary_bodies/medial_mammillary_nucleus/ or similar nodes.

Notes:
    - Tier 1 hub container with a single child pair. Not a delta
      pattern — both left/ and right/ are full leaves, because the
      mammillary body has real functional content that cannot be
      reduced to "same as left."
    - The MM/LM split is documented within each hemisphere's leaf,
      not as child nodes. Same convention as habenula's LHb/MHb split.
    - The mammillary bodies are the FIRST hypothalamic structure whose
      primary role is MEMORY rather than homeostasis/endocrine. This
      is why they sit as a direct child of hypothalamus/ and not under
      posterior/. Do not move them or reclassify them.
    - Korsakoff syndrome is the defining clinical content of this
      file. It is what makes the mammillary bodies important, and it
      must be documented. Do not omit it.
    - The mammillary bodies are a MEMORY RELAY, not a memory encoder.
      The hippocampus is the encoder; the mammillary bodies relay
      hippocampal output to the thalamus. Do not conflate the two.
    - The mammillary bodies do not receive the 12 endocrine axes as
      principal targets. Do not list them as an endocrine target; do
      not list CRH, cortisol, etc. as modulators. The one significant
      "hormonal" fact is thiamine deficiency (a vitamin, not a
      hormone) → Korsakoff syndrome.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, minor); memory/stores/
      (episodic, short_term, temporal_sequence_learning); gateway/.
      Note: thiamine is documented here directly as a clinical
      modulator, not via the chemicals_hormones/ axes, because it is
      not one of the 12 axes.
    - Reciprocal connections to enforce in Stage 4:
        * mammillary_bodies/left|right ↔
          telencephalon/.../hippocampus/left|right (via the fornix;
          the principal Papez afferent; hippocampal output to
          mammillary bodies).
        * mammillary_bodies/left|right ↔
          telencephalon/.../hippocampus/left|right/subiculum (via the
          fornix; subicular output to the mammillary bodies is the
          principal Papez relay input).
        * mammillary_bodies/left|right → thalamus/left|right/
          anterior_nuclear_group/anterodorsal_nucleus (via the
          mammillothalamic tract; Papez relay output for memory and
          head-direction).
        * mammillary_bodies/left|right → thalamus/left|right/
          anterior_nuclear_group/anteroventral_nucleus (via the
          mammillothalamic tract; Papez relay output).
        * mammillary_bodies/left|right → midbrain/.../dorsal_tegmental_nucleus
          and ventral_tegmental_nucleus (mammillotegmental tract;
          ascending reticular activating system; these are DIFFERENT
          from the ventral_tegmental_area in the midbrain tegmentum —
          do not confuse dorsal/ventral tegmental NUCLEUS (mammillary
          targets) with ventral tegmental AREA (dopamine source);
          document the distinction explicitly).
        * mammillary_bodies/left|right ↔ telencephalon/.../
          white_matter/fornix (the fornix is the principal afferent
          white-matter tract; Tier 3 conduit).
        * mammillary_bodies/left|right ↔ telencephalon/.../
          white_matter/mammillothalamic_tract (the principal efferent
          white-matter tract; Tier 3 conduit).
    - Midline "verify" flags: not applicable — the mammillary bodies
      are a paired structure, and the left/right split is the natural
      tree structure. The anterior thalamic nuclei (targets) are paired
      and hemisphere-split; the fornix and mammillothalamic tract are
      also paired (or partly midline); document as hemisphere-specific
      in the left/right children.
    - Connects upward to hypothalamus/.
"""