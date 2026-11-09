"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.lateral_nuclear_group.lateral_dorsal_nucleus
Anatomical Role:
    The left lateral dorsal nucleus (LD). The SMALLEST and LEAST
    CHARACTERIZED of the three left lateral nuclear group nuclei,
    situated on the dorsolateral aspect of the left thalamus. It
    projects to the left cingulate cortex and left retrosplenial
    cortex — the same cortical targets as the left anterior thalamic
    nuclei (AD, AM, AV) — but via a DIFFERENT circuit: the LD is a
    HIGHER-ORDER ASSOCIATION RELAY (cortical layer 5 driver, cortical
    association output), not a Papez memory relay (hippocampal/
    mammillary driver).

    The LD's honest characterization: the literature is THINNER than
    for the pulvinar and lateral posterior nucleus. The LD is
    documented as a "higher-order limbic-adjacent association relay"
    with the caveat that its specific contribution to limbic-adjacent
    association is less established than its neighbors'. Same
    discipline as the zona incerta, the tuberal nucleus, INAH-1/2, and
    the lateral tuberal nuclei — document honestly, do not invent.

    DISTINCTIONS (critical):

    - LD vs. ANTERIOR NUCLEAR GROUP (the primary trap): the LD and the
      anterior thalamic nuclei (AD, AM, AV) both project to the
      cingulate and retrosplenial cortices. But the LD is a HIGHER-ORDER
      ASSOCIATION relay (cortical layer 5 driver), NOT a Papez memory
      relay (hippocampal/mammillary driver). Different circuits that
      converge on similar cortical regions. Do not merge the LD with
      AD/AM/AV; the convergence is anatomical, not functional.

    - LD vs. LATERAL POSTERIOR (intra-group): the LP is the PARIETAL
      association relay; the LD is the LIMBIC-ADJACENT association
      relay. Different cortical targets (posterior parietal vs.
      cingulate/retrosplenial); different association domains. Do not
      merge.

    - LD vs. PULVINAR (intra-group): the pulvinar is the VISUAL
      association relay; the LD is the limbic-adjacent association
      relay. Different cortical targets; different association
      domains. Do not merge.

    - LD vs. MEDIODORSAL NUCLEUS (MD; subtle): both project to
      cortical association regions (LD → cingulate; MD → prefrontal).
      Different association domains; different circuits. Do not merge.

Functional Mode:
    - Higher-order limbic-adjacent association (the LD's anchor role,
      with the honest "less characterized" caveat):
        * The LD receives cortical layer 5 input (from cingulate,
          retrosplenial, and adjacent limbic-adjacent cortices) and
          projects back to the cingulate cortex and retrosplenial
          cortex.
        * The LD contributes to limbic-adjacent association — spatial
          memory, contextual associations, and retrosplenial-adjacent
          processing — but its specific contribution is LESS
          established than the pulvinar's visual association or the
          LP's parietal association.
        * Documented as "contributes to limbic-adjacent association,"
          not "is the limbic-adjacent association hub." The honest
          framing is the correct framing.
    - Spatial memory (secondary): the LD's cingulate/retrosplenial
      projections suggest a contribution to spatial memory (the
      retrosplenial cortex is a spatial-orientation hub), but the
      literature is thinner than for the AD (head-direction) or the
      AV (memory). Document as a "presumed contribution," not a
      "demonstrated role."
    - The LD is therefore the lateral group's THIN-LITERATURE nucleus:
      it has a real role (limbic-adjacent association) but is less
      well characterized than the pulvinar and LP. Do not over-write
      it.

    - CLINICAL FACT (honest): the LD's clinical contribution is
      undocumented in isolation. LD-specific lesions and LD-specific
      syndromes are NOT established; the LD's clinical relevance is
      as part of the broader limbic-adjacent association picture. Do
      not claim an LD-specific clinical syndrome that the literature
      does not establish. Same honest stance as the AM's "no
      AM-specific syndrome" and the zona incerta's "exploratory" DBS.

Hormonal Modulation (minimal; the LD is a higher-order association relay):
    - The LD is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) arousal inputs contribute to the attentional gating
      of the association relay. Document as arousal modulation, not
      endocrine modulators.
    - The LD is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the LD's limbic-adjacent role includes episodic
          spatial memory (cingulate/retrosplenial-adjacent).
        * short_term: the current state of the LD's cortical
          association loop.
    - Writes: none directly. The LD is a RELAY: it transmits
      association signals between cortical areas; the memory content
      is stored in the cortex, not the thalamus.
    - The LD's memory interfaces are THINNER than the pulvinar's
      (semantic) and LP's (semantic + parietal): the LD reads episodic
      and short_term, with no distinct semantic interface documented.
      Do not pad with interfaces the literature does not support.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No LD fragment. The LD is a higher-order association relay; the
      model prompt does not need an LD block because the association
      signals it relays are already represented in the upstream
      (cingulate, retrosplenial) and downstream (cingulate,
      retrosplenial) fragments. The cortex carries the association
      state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The LD's clinical contribution (undocumented in isolation) is
      noted for completeness, but is not a prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/lateral_nuclear_group/lateral_dorsal_nucleus/):

    Higher-order limbic-adjacent association (the anchor):
    - ← telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      anterior_cingulate and telencephalon/.../cortex/cingulate/
      retrosplenial_cortex (cortical layer 5 input; the LD's driver
      input from cingulate and retrosplenial cortices).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      anterior_cingulate and telencephalon/.../cortex/cingulate/
      retrosplenial_cortex (LD output to the same cortical targets;
      the higher-order association loop).

    Intra-group:
    - ↔ ../lateral_posterior_nucleus/ (adjacent; LP is the parietal
      association relay; LD is the limbic-adjacent association relay;
      different domains; do not merge).
    - ↔ ../pulvinar/ (adjacent; pulvinar is the visual association
      relay; LD is the limbic-adjacent association relay; different
      domains; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../../anterior_nuclear_group/ (the LD and the anterior nuclei
      both project to the cingulate and retrosplenial cortices;
      DIFFERENT circuits converging on similar cortical regions; the
      LD is a cortical-layer-5-driven association relay, the anterior
      nuclei are hippocampal/mammillary-driven Papez memory relays;
      do not merge; this structural note is not a signaling edge).

Notes:
    - Tier 1 full leaf (left). The LD is the THIN-LITERATURE nucleus
      of the lateral group: real role (limbic-adjacent association),
      less characterized than the pulvinar and LP. Do not over-write;
      ~70 lines matches the honest literature weight (the pulvinar is
      ~110, the LP is ~85; the LD is genuinely thinner).
    - THE LD vs. ANTERIOR NUCLEAR GROUP TRAP reproduced in full: the
      LD and the anterior nuclei both project to cingulate/
      retrosplenial, but via different circuits (association vs.
      Papez memory). Same convergence, different function. Do not
      merge.
    - LD vs. LP and LD vs. pulvinar distinctions reproduced: the LD is
      the LIMBIC-ADJACENT association relay; the LP is parietal; the
      pulvinar is visual. Different domains; different cortical
      targets.
    - HONESTY DISCIPLINE: the LD's contribution to limbic-adjacent
      association is less established than the pulvinar's visual
      association or the LP's parietal association. Documented as
      "contributes to" and "presumed contribution," not "is the" and
      "demonstrated role." Same discipline as the zona incerta, the
      tuberal nucleus, INAH-1/2, and the lateral tuberal nuclei.
    - CLINICAL FACT (honest): LD-specific lesions and syndromes are
      NOT established. The LD's clinical relevance is as part of the
      broader limbic-adjacent association picture. Do not invent an
      LD-specific syndrome.
    - NO FRAGMENT: same as the whole thalamus. The LD is a relay, not
      a state-emitter.
    - The LD is NOT the AD (head-direction), NOT the AM/AV (Papez
      memory), NOT the LP (parietal association), NOT the pulvinar
      (visual association). The traps make these distinctions
      explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (episodic, short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/lateral_nuclear_
      group/.
"""