"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group.rhomboidal_nucleus
Anatomical Role:
    The left rhomboidal nucleus (Rh). The smallest and least
    characterized of the three left midline thalamic nuclei, situated
    at the midline of the left thalamus, immediately adjacent to (and
    often considered a ventral continuation of) the left reuniens
    nucleus. It is a LIMBIC-ADJACENT RELAY: it receives hypothalamic
    and limbic inputs and projects to the hippocampus, amygdala, and
    prefrontal cortex, with a projection profile that overlaps
    substantially with the reuniens.

    The Rh's honest characterization: the literature is THIN, thinner
    even than the paratenial's. The Rh is documented as a "contributes
    to limbic-adjacent relay" nucleus with the caveat that its
    specific contribution is not well established and is often
    studied in conjunction with the reuniens rather than in
    isolation. Same discipline as the paratenial, the LD, INAH-1/2,
    the tuberal nucleus, the zona incerta, and the lateral tuberal
    nuclei — document honestly, do not invent.

    DISTINCTIONS (critical):

    - RH vs. REUNIENS (intra-family; the primary distinction): the
      Rh is anatomically adjacent to and functionally overlapping
      with the reuniens
      (thalamus/left/medial_nuclear_group/reuniens_nucleus/), but the
      reuniens is the HIPPOCAMPAL relay (well-studied; spatial working
      memory; the family's anchor) while the Rh is the less-studied
      limbic-adjacent neighbor. The Rh's contributions are often
      attributed to the "reuniens-rhomboidal complex" in the
      literature; document the complex framing but keep the two
      nuclei as distinct tree nodes.

    - RH vs. PARATENIAL (intra-family): both are the family's
      "less-characterized" members; the paratenial
      (thalamus/left/medial_nuclear_group/paratenial_nucleus/) is
      dorsal-adjacent (olfactory-limbic emphasis), the Rh is
      ventral-adjacent to the reuniens (limbic-hippocampal emphasis).
      Different emphases; anatomically adjacent but distinct nuclei;
      do not merge.

    - RH vs. PVT (intra-family): the PVT (if added) is the family's
      stress/reward relay; the Rh is the limbic-adjacent relay.
      Different emphases; do not merge.

    - RH vs. INTRALAMINAR FAMILY (family-level): the Rh is part of the
      midline family's LIMBIC/VISCERAL relay system; the intralaminar
      family is AROUSAL/ATTENTION. Different families; do not merge.

Functional Mode:
    - Limbic-adjacent relay (the Rh's anchor role; honestly
      "contributes to"):
        * The Rh receives hypothalamic and limbic inputs and projects
          to the hippocampus, amygdala, and prefrontal cortex. Its
          projection profile overlaps substantially with the
          reuniens; the two nuclei are often studied together as the
          "reuniens-rhomboidal complex."
        * The Rh CONTRIBUTES TO limbic-adjacent relay — the
          modulation of hippocampal, amygdalar, and prefrontal
          activity — but its specific contribution is LESS
          established than the reuniens' spatial working memory role.
        * Documented as "contributes to" and "presumed contribution,"
          not "is the" or "demonstrated role."
    - Hippocampal-adjacent modulation (secondary; poorly
      characterized): the Rh's hippocampal projections suggest a
      modulatory role in hippocampal processing, but the specific
      contribution is thin and often conflated with the reuniens'.
      Document as "presumed contribution."
    - The Rh is therefore the midline family's THIN-LITERATURE member
      alongside the paratenial: it has a real role (limbic-adjacent
      relay) but is less well characterized than the reuniens and
      PVT. Do not over-write.

    - CLINICAL FACT (honest): the Rh's clinical contribution is
      UNDOCUMENTED. Rh-specific lesions and Rh-specific syndromes are
      NOT established; the Rh's clinical relevance is as part of the
      broader midline-family picture, often grouped with the
      reuniens. Do not claim an Rh-specific clinical syndrome that
      the literature does not establish. Same honest stance as the
      paratenial, the LD, the AM, the zona incerta, and the lateral
      tuberal nuclei.

Hormonal Modulation (minimal; the Rh is a limbic-adjacent relay):
    - The Rh is NOT a neuroendocrine structure.
    - Modulators: hypothalamic inputs, limbic inputs (amygdala,
      hippocampus), and brainstem arousal inputs. Document as
      limbic modulation, not endocrine modulation.
    - The Rh is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the Rh's hippocampal-adjacent projections suggest
          a presumed read of episodic/contextual state (secondary;
          poorly characterized; often grouped with the reuniens'
          episodic read).
        * short_term: the current limbic state buffer (presumed;
          poorly characterized).
    - Writes: none directly. The Rh is a RELAY: it transmits
      limbic-adjacent signals between the hypothalamus and the
      hippocampus/amygdala/PFC; the memory content is stored in the
      cortex and hippocampus.
    - The Rh's memory interface is THIN (episodic presumed +
      short_term presumed), same as the paratenial's. Do not pad with
      interfaces the literature does not support.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No Rh fragment. The Rh is a limbic-adjacent relay; the model
      prompt does not need a rhomboidal-nucleus block because the
      limbic signals it relays are already represented in the
      upstream (hypothalamus, hippocampus, amygdala) and downstream
      (hippocampus, amygdala, PFC) fragments. The emotional_valence
      and episodic state is carried by the upstream fragments.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The Rh's clinical contribution (undocumented) is noted for
      completeness, but is not a prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/medial_nuclear_group/rhomboidal_nucleus/):

    Limbic-adjacent relay (the anchor; honestly "presumed"/
    "contributes to"):
    - ← hypothalamus/*/left (hypothalamic limbic inputs; the Rh is a
      midline nucleus that receives hypothalamic input).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (limbic-affective input; left-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (hippocampal-mnemonic input; the Rh's hippocampal
      input overlaps with the reuniens'; left-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (Rh → hippocampus; presumed mnemonic modulation;
      left-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (Rh → amygdala; presumed affective modulation; left-side).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      prefrontal_cortex (Rh → PFC; presumed limbic-prefrontal
      modulation; left-side).

    Reuniens-rhomboidal complex (the "complex" framing):
    - ↔ ../reuniens_nucleus/ (the Rh and the reuniens are
      anatomically adjacent and functionally overlapping; often
      studied together as the "reuniens-rhomboidal complex"; the
      reuniens is the well-studied anchor, the Rh is the less-studied
      neighbor; do not merge; document the complex relationship).

    Intra-family:
    - ↔ ../paratenial_nucleus/ (adjacent; both are less-characterized
      limbic-adjacent relays; distinct nuclei; do not merge).
    - ↔ ../midline_nuclear_group/ (the sub-container's structural
      note applies: the Rh and the sub-container are siblings, not
      parent-child; the sub-container integrates the family's
      collective role).

Notes:
    - Tier 1 full leaf (left). The Rh is the midline family's
      THIN-LITERATURE member alongside the paratenial: real role
      (limbic-adjacent relay), less characterized than the reuniens
      and PVT. Do not over-write; ~55 lines matches the honest
      literature weight (the paratenial was ~60, the reuniens ~90;
      the Rh is genuinely the thinnest of the three).
    - THE REUNIENS-RHOMBOIDAL COMPLEX framing is documented: the two
      nuclei are anatomically adjacent and functionally overlapping,
      often studied together. The Rh leaf documents the complex
      framing but keeps the two nuclei as distinct tree nodes; do not
      merge them.
    - THE RH vs. REUNIENS distinction is reproduced: reuniens =
      hippocampal relay anchor (well studied); Rh = less-studied
      limbic-adjacent neighbor. Do not merge.
    - THE RH vs. PARATENIAL distinction is reproduced: both are the
      family's "less-characterized" members; dorsal-adjacent (Pt)
      vs. ventral-adjacent to reuniens (Rh). Distinct nuclei.
    - HONESTY DISCIPLINE: the Rh's contribution to limbic-adjacent
      relay is less established than the reuniens' spatial working
      memory. Documented as "contributes to" and "presumed
      contribution." Same discipline as the paratenial, the zona
      incerta, the tuberal nucleus, INAH-1/2, and the lateral tuberal
      nuclei.
    - CLINICAL FACT (honest): Rh-specific lesions and syndromes are
      NOT established. The Rh's clinical relevance is as part of the
      broader midline-family picture, often grouped with the
      reuniens. Do not invent an Rh-specific syndrome.
    - NO FRAGMENT: same as the whole thalamus. The Rh is a relay, not
      a state-emitter.
    - The Rh is NOT the reuniens (hippocampal relay anchor), NOT the
      paratenial (dorsal-adjacent olfactory-limbic), NOT the PVT
      (stress/reward relay). The distinctions make these explicit.
    - THE PVT-vs-PVN TRAP does not apply directly to the Rh; the
      midline sub-container's trap declaration applies to the Rh's
      family context. The Rh leaf does not re-declare the trap.
    - THE RHOMBOIDAL PAIR WILL COMPLETE THE MEDIAL NUCLEAR GROUP: with
      this leaf and its right delta, the medial nuclear group is
      complete (20 files: 2 group containers + 6 intralaminar family
      files + 6 midline family files + the MD pair = 20 files,
      assuming no separate PVT node).
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, GABA,
      glutamate); memory/stores/ (episodic, short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/medial_nuclear_
      group/.
"""