"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.mammillary_bodies.left
Anatomical Role:
    The left mammillary body. A spherical structure at the ventral
    surface of the posterior hypothalamus, at the caudal end of the left
    fornix, containing two subdivisions:
        - Medial mammillary nucleus (MM): the larger subdivision.
          Receives the descending columns of the fornix from the left
          subiculum and hippocampus; projects to the left anterior
          thalamic nucleus via the left mammillothalamic tract. The MM
          is the principal Papez-circuit memory relay.
        - Lateral mammillary nucleus (LM): the smaller subdivision.
          Contains head-direction cells that encode the animal's
          directional heading. Receives input from the left dorsal
          tegmental nucleus and left presubiculum; projects to the left
          anterodorsal thalamic nucleus via the mammillothalamic tract.
          LM lesions impair spatial navigation and head-direction cell
          function.
    The MM/LM split is documented WITHIN this file, not as separate tree
    children. Same convention as the habenula's LHb/MHb split and the
    PVN's three sub-populations. Do not create medial_mammillary_nucleus/
    or lateral_mammillary_nucleus/ as child nodes.

    The mammillary bodies are the FIRST hypothalamic structure whose
    primary role is MEMORY rather than homeostasis or endocrine. This is
    why they sit as a direct child of hypothalamus/ (not under
    posterior/); do not reclassify.

Functional Mode:
    - Papez circuit relay (episodic memory; the primary function): the
      left mammillary bodies sit between the left hippocampal formation
      (via the left fornix) and the left anterior thalamic nucleus (via
      the left mammillothalamic tract). The classic Papez circuit is:
        hippocampus → fornix → mammillary bodies → mammillothalamic
        tract → anterior thalamic nucleus → cingulate cortex →
        parahippocampal gyrus → entorhinal cortex → hippocampus.
      Damage to any node in this loop causes episodic memory impairment.
      The mammillary bodies are a required relay, not the encoder.
    - Korsakoff syndrome (the defining clinical fact): left mammillary
      body lesions are the classic anatomical substrate of Korsakoff
      syndrome (thiamine deficiency, typically in chronic alcoholism).
      The syndrome is a severe anterograde amnesia with confabulation,
      preserving procedural memory and general intelligence while
      impairing episodic recall. The lesion is typically bilateral, but
      the left hemisphere's contribution is documented here. Do not
      omit Korsakoff: it is what makes the mammillary bodies
      clinically important.
    - Head-direction (spatial navigation; LM): the left lateral
      mammillary nucleus contains head-direction cells that encode the
      animal's directional heading. The LM → left anterodorsal thalamic
      nucleus projection carries the head-direction signal, and LM
      lesions impair spatial navigation.
    - Theta-rhythm participation: the left mammillary bodies
      participate in the septo-hippocampal theta circuit
      (septum → hippocampus → mammillary bodies → ...), which supports
      hippocampal memory encoding. They are a node in the
      theta-generating network, not an independent oscillator.
    - Mammillotegmental output (less well characterized): the left
      mammillary bodies project to the left dorsal and ventral
      tegmental nuclei (via the mammillotegmental tract), participating
      in the ascending reticular activating system. This is the
      non-Papez output; its function is less well characterized than
      the Papez circuit, and should be documented but not overclaimed.
    - The mammillary bodies are a MEMORY RELAY, not a memory encoder,
      and not a homeostatic or endocrine effector. The hippocampus is
      the encoder; the mammillary bodies relay hippocampal output to
      the thalamus.

Hormonal Modulation (minimal by design — the mammillary bodies are NOT
a neurosecretory nucleus and are NOT a principal target of the 12
endocrine axes):
    - Thiamine (vitamin B1): the defining clinical modulator, though a
      vitamin, not a hormone. Thiamine deficiency causes mammillary
      body lesions (Wernicke encephalopathy → Korsakoff syndrome).
      This is the single most important "modulatory" fact about the
      region and must be documented.
    - Estradiol: sex-hormone receptor expression has been reported in
      the mammillary region, but the functional significance is not
      established. Document as a minor modulatory input, not a
      principal axis.
    - The 12 endocrine axes (CRH, cortisol, HPT, HPG, satiety,
      monoamines, social, fluid, immune, circadian, xenobiotic,
      gasotransmitters) do NOT act on the mammillary bodies as
      principal targets. Do not list them here. The mammillary bodies
      are a memory structure, not a homeostatic one.
    - Limbic neural input (not hormonal): the mammillary bodies are
      modulated by the septum, hippocampus, subiculum, and anterior
      thalamus. These are neural, not hormonal, modulators. Documented
      in Functional Mode and Reciprocal Connections, not here.
    - Direction summary: thiamine deficiency ↓ mammillary body function
      (lesions, Korsakoff); estradiol modulation reported but not
      established. Do not list the 12 axes as modulators.

Memory Interfaces (the mammillary bodies are a MEMORY hub; this is the
most important section of this file):
    - Reads:
        * episodic: prior events and spatial contexts, retrieved from
          the left hippocampal formation via the left fornix. The
          mammillary bodies relay these to the left anterior thalamus
          for cortical re-encoding.
        * short_term: current spatial context and head-direction
          buffer (via the LM head-direction cells).
        * temporal_sequence_learning: temporal order of events within
          an episode, as relayed via the left hippocampal formation.
    - Writes:
        * episodic: the left mammillary bodies participate in the
          consolidation of episodic memory by relaying hippocampal
          output to the left anterior thalamus. This is an INDIRECT
          write — the mammillary bodies do not encode memories
          directly, but they are a required node in the circuit that
          consolidates them. Mammillary body lesions (Korsakoff
          syndrome) impair episodic memory consolidation; this is the
          write-interface justification. Do not confuse this with the
          hippocampus's direct episodic write; the mammillary bodies
          are a relay, not the encoder.
    - The mammillary bodies are the FIRST hypothalamic structure
      documented as a *writer* to episodic memory. The hippocampus
      (elsewhere in the tree) is the direct encoder; the mammillary
      bodies are the indirect relay/consolidator. This distinction is
      the defining memory-interface property of this leaf.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (memory-context fragment, applied after the
      anterior-division fragments, before the cortical reasoning
      fragments):
        "Memory relay state — left mammillary body:
         - Episodic relay (left): [intact / impaired].
         - Papez circuit integrity (left): [intact / disrupted].
         - Left spatial context availability: [high / moderate / low].
         - Left head-direction signal: [available / unavailable].
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
      emitted (always); mammillary relay state is a persistent
      circuit-integrity signal, not a transient homeostatic state.
    - Guardrail: "do not confabulate missing details; do not treat
      impaired episodic relay as cognitive failure." This is a NEW
      guardrail type: it prevents a specific failure mode
      (confabulation) rather than a state-bias overreach. The
      habenula/LPO/orientation guardrails prevent over-suppression of
      reasoning; this one prevents over-confident recall. Both are
      "bias not failure" framings, but at different ends of the
      behavior spectrum.
    - The two hemispheres emit a coordinated bilateral relay signal:
      the right mammillary body (in right/) contributes the right-side
      relay state. The implementer aggregates the left and right
      relay-integrity signals at the hypothalamic level, but the
      memory fragment content itself is per-hemisphere (left and right
      Papez circuits can fail independently in some lesion
      distributions).
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (left-side; the right side is in right/):
    Papez circuit (primary):
    - ← telencephalon/.../hippocampus/left/subiculum (via the left
      fornix; the principal Papez afferent — subicular output to the
      mammillary bodies is the main relay input).
    - ← telencephalon/.../hippocampus/left (via the left fornix;
      hippocampal output to the mammillary bodies).
    - → thalamus/left/anterior_nuclear_group/anterodorsal_nucleus
      (via the left mammillothalamic tract; Papez relay output for
      memory and head-direction).
    - → thalamus/left/anterior_nuclear_group/anteroventral_nucleus
      (via the left mammillothalamic tract; Papez relay output).
    - → thalamus/left/anterior_nuclear_group/anteromedial_nucleus
      (via the left mammillothalamic tract; Papez relay output).

    Head-direction (LM-specific):
    - ← midbrain/.../dorsal_tegmental_nucleus (left; head-direction
      input; IMPORTANT: this is the dorsal TEGMENTAL NUCLEUS (part of
      the Gudden tegmental nuclei), NOT the dorsal tegmental area of
      the midbrain — do not confuse).
    - ← telencephalon/.../hippocampus/left/presubiculum (head-direction
      input).

    Mammillotegmental output (less characterized):
    - → midbrain/.../dorsal_tegmental_nucleus and midbrain/.../
      ventral_tegmental_nucleus (mammillotegmental tract; ascending
      reticular activating system). IMPORTANT: the ventral TEGMENTAL
      NUCLEUS (a Gudden nucleus) is DIFFERENT from the ventral
      TEGMENTAL AREA (dopamine source). Do not confuse. The mammillary
      bodies project to the tegmental NUCLEI, not the tegmental AREA.

    White-matter conduits (Tier 3):
    - ↔ telencephalon/.../white_matter/fornix/left (principal afferent
      conduit; Tier 3).
    - ↔ telencephalon/.../white_matter/mammillothalamic_tract/left
      (principal efferent conduit; Tier 3).

    Theta-rhythm circuit:
    - ↔ telencephalon/.../basal_forebrain/septal_nuclei/left/medial_septal_nuclei
      (theta-rhythm generation; septum → hippocampus → mammillary
      bodies loop).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - The FIRST memory-write leaf in the tree. The episodic write is
      INDIRECT — via the Papez circuit relay to the anterior thalamus.
      Do not conflate with the hippocampus's direct episodic write.
    - The MM/LM split is documented WITHIN this file, not as child
      nodes. Same convention as habenula's LHb/MHb and PVN's
      sub-populations.
    - HORMONAL MODULATION IS MINIMAL BY DESIGN. This is the first leaf
      where the hormone section is deliberately thin: the mammillary
      bodies are not a neurosecretory nucleus and are not a principal
      target of the 12 axes. Thiamine is documented as the defining
      clinical modulator even though it is a vitamin, not a hormone.
      Do not pad the section with the 12 axes to match other leaves.
    - Korsakoff syndrome is the defining clinical content and must
      remain in the file. It is the single fact that explains why the
      mammillary bodies matter.
    - NAMING TRAP (critical): the mammillary bodies project to the
      DORSAL and VENTRAL TEGMENTAL NUCLEI (Gudden nuclei; part of the
      ascending reticular system), which are DIFFERENT from the
      VENTRAL TEGMENTAL AREA (VTA; the midbrain dopamine source).
      These are different structures with confusingly similar names.
      Document the distinction explicitly; do not merge them in the
      tree.
    - The "do not confabulate" guardrail is a new type in the tree:
      previous guardrails prevent state-bias overreach (over-suppression
      of reasoning, over-claiming impairment); this one prevents memory
      over-confidence. Both are "bias not failure" framings, but at
      opposite ends of the failure-mode spectrum. Do not remove it.
    - Estradiol is documented as a minor modulatory input; its
      functional significance in the mammillary bodies is not
      established. Do not overclaim.
    - Vocabulary used above is defined in Stage 0 files:
      memory/stores/ (episodic, short_term, temporal_sequence_learning);
      gateway/. Thiamine is documented here directly (not via the 12
      axes) because it is not one of the 12 axes.
    - Connects upward to hypothalamus/mammillary_bodies/.
"""