"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.lateral_nuclear_group
Anatomical Role:
    The left lateral nuclear group of the thalamus. A cluster of three
    nuclei situated on the lateral aspect of the left thalamus, forming
    the thalamus's HIGHER-ORDER ASSOCIATION RELAY GROUP. Unlike the
    anterior group (Papez memory relay) or the metathalamus (first-order
    sensory relay), the lateral group relays CORTICO-CORTICAL
    association signals: its driver input is primarily from cortical
    layer 5 (not from the sensory periphery or subcortical structures),
    and its output is to higher-order association cortices.

    The three nuclei:
        - lateral_dorsal_nucleus/ (LD): the smallest and least
          characterized of the three. Receives cingulate and
          limbic-adjacent inputs; projects to the cingulate cortex and
          the retrosplenial cortex. Contributes to spatial memory and
          limbic-adjacent association. Documented as a
          "higher-order limbic-adjacent relay" — the honest framing is
          that the LD is less well characterized than the pulvinar and
          LP.
        - lateral_posterior_nucleus/ (LP): a PARIETAL ASSOCIATION relay.
          Receives input from the parietal cortex (and from the
          pulvinar); projects to the posterior parietal cortex (areas
          5, 7, and adjacent). Contributes to spatial attention,
          visuomotor integration, and parietal association. The LP is
          one of the two principal higher-order association relays of
          the group (along with the pulvinar).
        - pulvinar/: the LARGEST nucleus of the group (and one of the
          largest in the thalamus). A VISUAL ASSOCIATION relay.
          Receives input from the visual cortices (V1–V5, MT) and
          projects back to visual association cortices (V2–V5, MT, IT)
          and to the parietal and temporal association cortices.
          Contributes to visual attention, visual salience, and
          visual-association integration. The pulvinar is the group's
          anchor nucleus.

    The lateral group is therefore the THALAMUS'S HIGHER-ORDER
    ASSOCIATION GROUP: it relays cortico-cortical association signals
    for visual, parietal, and limbic-adjacent association. It is the
    thalamic counterpart of the cortical association hierarchy.

    DISTINCTIONS (critical):

    - PULVINAR vs. LATERAL POSTERIOR (the group's signature trap): both
      are higher-order association relays; the PULVINAR is primarily
      VISUAL ASSOCIATION (V2–V5, MT, IT); the LP is primarily PARIETAL
      ASSOCIATION (posterior parietal cortex, areas 5/7). Different
      cortical targets; different association domains. Do not merge;
      do not treat them as interchangeable higher-order relays. The
      full trap is declared in the parent thalamus container; this
      group container reproduces it and the pulvinar/LP leaves
      enforce it.

    - LATERAL GROUP vs. ANTERIOR GROUP (both "higher-order"-adjacent
      but different circuits): the lateral group is the
      CORTICO-CORTICAL ASSOCIATION relay (cortical layer 5 driver →
      association cortex); the anterior group
      (thalamus/left/anterior_nuclear_group/) is the PAPEZ MEMORY
      relay (hippocampus → mammillary bodies → anterior thalamus →
      cingulate). Different circuits; different nuclei; do not merge.

    - LATERAL GROUP vs. VENTRAL GROUP (both thalamic but different
      relay types): the lateral group relays cortico-cortical
      association; the ventral group
      (thalamus/left/ventral_nuclear_group/) relays FIRST-ORDER
      sensory (VPL/VPM) and motor (VA/VL) signals. Different relay
      types; different nuclei; do not merge.

    - LATERAL DORSAL vs. ANTERIOR NUCLEAR GROUP (a subtle trap): the
      LD projects to the cingulate and retrosplenial cortices — the
      same cortical targets as the anterior thalamic nuclei. But the
      LD is a HIGHER-ORDER ASSOCIATION relay (cortical layer 5
      driver), not a Papez memory relay (hippocampal driver). The two
      are distinct circuits that happen to converge on similar
      cortical regions; do not merge the LD with the AD/AM/AV.

Functional Mode:
    - Visual association (pulvinar; the group's anchor role):
        * The pulvinar receives input from visual cortical areas
          (V1–V5, MT) and projects back to visual association areas
          (V2–V5, MT, IT). It is the thalamic relay for the visual
          association hierarchy.
        * The pulvinar contributes to visual attention (particularly
          the pulvinar's role in spatial attention and in filtering
          distractors), visual salience, and the integration of visual
          features across the visual hierarchy.
        * Two pulvinar subregions are recognized: the lateral
          pulvinar (visual), the medial pulvinar (multisensory,
          connected to parietal and temporal association cortices),
          and the inferior pulvinar (motion, MT-adjacent). The three
          subregions are documented WITHIN the pulvinar leaf, not as
          child nodes.
    - Parietal association (LP; the group's second role):
        * The LP receives input from the parietal cortex and projects
          back to the posterior parietal cortex (areas 5 and 7). It
          contributes to spatial attention and visuomotor integration.
        * The LP is a higher-order association relay, not a
          first-order sensory relay: it relays cortico-cortical
          association, not the primary somatosensory signal (that is
          the VPL/VPM's role in the ventral group).
    - Limbic-adjacent association (LD; the group's tertiary role):
        * The LD receives cingulate and limbic-adjacent inputs and
          projects to the cingulate cortex and retrosplenial cortex.
          It contributes to spatial memory and limbic-adjacent
          association.
        * The LD is the least well characterized of the three: the
          literature is thinner than for the pulvinar and LP. Document
          honestly; do not over-write the LD.
    - The lateral group is therefore the THALAMUS'S HIGHER-ORDER
      ASSOCIATION GROUP: its three nuclei relay cortico-cortical
      association for visual (pulvinar), parietal (LP), and
      limbic-adjacent (LD) domains. It is the thalamic counterpart of
      the cortical association hierarchy.

    - CLINICAL FACT (the group's clinical anchor; pulvinar-centered):
        * Pulvinar lesions can produce VISUAL ATTENTIONAL DEFICITS
          (spatial neglect-like symptoms, particularly for the
          contralateral hemifield) and VISUAL ASSOCIATION DEFICITS
          (integration and salience impairments). The pulvinar is one
          of the thalamic nuclei whose lesions produce a specific
          cortical-like syndrome.
        * LP lesions can produce PARIETAL-LIKE DEFICITS (spatial
          attention, visuomotor integration).
        * LD lesions are rare in isolation; the LD's clinical
          contribution is part of the broader limbic-adjacent
          association picture, not a distinct LD-specific syndrome.
      The group's clinical anchor is the pulvinar's visual attentional
      role; the LP and LD contribute secondary clinical pictures.

Hormonal Modulation (minimal; the lateral group is an association relay):
    - The lateral group is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) arousal inputs contribute to the attentional gating
      of the association relays. Document as arousal modulation, not
      endocrine modulators.
    - The lateral group is NOT a principal target of the 12 endocrine
      axes. Do not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the LD's limbic-adjacent role includes episodic
          spatial memory (cingulate/retrosplenial-adjacent).
        * semantic: the pulvinar and LP contribute to semantic
          association (visual and parietal object knowledge) via
          their cortical loops.
        * short_term: all three nuclei relay the current state of
          their cortical association loops (visual, parietal,
          limbic-adjacent).
    - Writes: none directly. The lateral group is a RELAY: it
      transmits association signals between cortical areas; the
      memory content is stored in the cortex, not the thalamus.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No lateral group fragment. The lateral group is an association
      relay; the model prompt does not need a lateral-group block
      because the association signals it relays are already
      represented in the upstream (visual cortex, parietal cortex,
      cingulate cortex) and downstream (visual association, parietal
      association, cingulate association) fragments. The cortex
      carries the association state.
    - AGGREGATION RULES: no fragments are emitted from this container
      or from the three nucleus leaves. Deliberate absence, same as
      the whole thalamus.
    - The lateral group's clinical facts (pulvinar visual attention;
      LP parietal; LD limbic-adjacent) are documented for
      completeness, but are not prompt fields.

Children (three children — three full leaves, no sub-containers):
    - lateral_dorsal_nucleus/    Tier 1 leaf. Limbic-adjacent
                                  association; LD → cingulate and
                                  retrosplenial. Least characterized
                                  of the three; document honestly.
    - lateral_posterior_nucleus/ Tier 1 leaf. Parietal association;
                                  LP → posterior parietal cortex. One
                                  of the two anchor nuclei of the
                                  group.
    - pulvinar/                  ★ Tier 1 leaf. Visual association;
                                  LGN-adjacent but HIGHER-ORDER (not
                                  first-order visual). The anchor
                                  nucleus of the group.

    All three are full leaves (not deltas of each other): LD, LP, and
    pulvinar are distinct nuclei with distinct cortical targets and
    distinct association domains. The left/right pairs follow the
    standard hemisphere-delta pattern.

Notes:
    - Group container. Names the three nuclei; defers functional
      content to the leaves (except for the container-level summary
      above).
    - THE PULVINAR vs. LP TRAP IS THE GROUP'S SIGNATURE: both
      higher-order; pulvinar = visual association, LP = parietal
      association. Reproduced in full above; the pulvinar and LP
      leaves must enforce it.
    - THE LD HONESTY: the lateral dorsal nucleus is the least
      characterized of the three. Document as "less well
      characterized" rather than inventing function. Same discipline
      as the zona incerta, the tuberal nucleus, and INAH-1/2.
    - THE LATERAL GROUP IS NOT A FIRST-ORDER SENSORY GROUP: it relays
      cortico-cortical association, not primary sensory input. The
      primary sensory relays are in the ventral group (VPL/VPM) and
      metathalamus (LGN/MGN). Do not draft the lateral group as if
      its nuclei were first-order sensory relays.
    - THE PULVINAR IS ANCHOR: it is the largest nucleus, the most
      studied, the most visually salient, and the group's clinical
      anchor. It is the natural first leaf to draft after this
      container.
    - THE LATERAL GROUP IS NOT THE ANTERIOR GROUP: both project to
      cingulate/retrosplenial (LD and the anterior nuclei), but the
      LD is a higher-order association relay (cortical layer 5
      driver) while the anterior nuclei are Papez memory relays
      (hippocampal/mammillary driver). Do not merge.
    - NO FRAGMENT: same as the whole thalamus. The lateral group is a
      relay, not a state-emitter.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (episodic, semantic, short_term); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * lateral_nuclear_group/left/lateral_dorsal_nucleus ↔
          telencephalon/.../cortex/cingulate/anterior_cingulate and
          telencephalon/.../cortex/cingulate/retrosplenial_cortex
          (LD → cingulate + retrosplenial; higher-order limbic-adjacent
          association).
        * lateral_nuclear_group/left/lateral_posterior_nucleus ↔
          telencephalon/.../cortex/parietal/posterior_parietal_cortex
          (LP ↔ posterior parietal cortex; parietal association).
        * lateral_nuclear_group/left/pulvinar ↔ telencephalon/.../
          cortex/occipital/* (V2–V5, MT) and telencephalon/.../
          cortex/temporal/* (IT) (pulvinar ↔ visual association
          cortices; visual association).
        * lateral_nuclear_group/left/pulvinar ↔ lateral_nuclear_group/
          left/lateral_posterior_nucleus (intra-group: pulvinar ↔ LP;
          the pulvinar projects to the LP as part of the parietal
          association circuit; distinct nuclei; do not merge).
    - Connects upward to diencephalon/thalamus/left/.
"""