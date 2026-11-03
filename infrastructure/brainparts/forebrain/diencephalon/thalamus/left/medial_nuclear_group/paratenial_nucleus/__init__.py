"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group.paratenial_nucleus
Anatomical Role:
    The left paratenial nucleus (Pt). One of the midline thalamic nuclei,
    situated along the midline of the left thalamus, adjacent to the
    left reuniens and rhomboidal nuclei. It is an OLFACTORY-LIMBIC
    RELAY: it receives olfactory and limbic inputs and projects to the
    amygdala, hippocampus, and prefrontal cortex.

    The Pt's honest characterization: the literature is THINNER than
    for the reuniens and PVT. The Pt is documented as a "contributes to
    olfactory-limbic integration" relay with the caveat that its
    specific contribution to limbic function is not well established.
    Same discipline as the LD, INAH-1/2, the tuberal nucleus, and the
    zona incerta — document honestly, do not invent.

    DISTINCTIONS (critical):

    - Pt vs. REUNIENS (intra-family; the primary distinction): the Pt
      is an OLFACTORY-LIMBIC relay (olfactory + limbic driver; the
      less-studied member); the reuniens
      (thalamus/left/medial_nuclear_group/reuniens_nucleus/) is a
      HIPPOCAMPAL relay (the well-studied member; spatial working
      memory). Different functional emphases; different
      characterization levels; do not merge.

    - Pt vs. RHOMBOIDAL (intra-family): both are less-characterized
      olfactory-limbic relays; the rhomboidal is adjacent to the
      reuniens and shares some inputs. The two are the midline
      family's "less characterized" pair; they are anatomically
      adjacent but distinct nuclei. Do not merge.

    - Pt vs. PVT (intra-family): the PVT (if added) is the family's
      stress/reward relay; the Pt is the olfactory-limbic relay.
      Different functional emphases; do not merge. (See the PVT-vs-PVN
      trap declared in the midline sub-container.)

    - Pt vs. MIDLINE FAMILY (family-level): the Pt is part of the
      midline family's LIMBIC/VISCERAL relay system; the intralaminar
      family is AROUSAL/ATTENTION. Different families; do not merge.

Functional Mode:
    - Olfactory-limbic integration (the Pt's anchor role; honestly
      "contributes to"):
        * The Pt receives olfactory inputs (from the olfactory bulb
          via the lateral olfactory tract-adjacent pathways, and from
          piriform/entorhinal cortices) and limbic inputs (from the
          amygdala and hippocampus), and projects to the amygdala,
          hippocampus, and prefrontal cortex.
        * The Pt CONTRIBUTES TO olfactory-limbic integration — the
          linking of olfactory information with limbic (affective,
          mnemonic) processing. Its specific contribution is LESS
          established than the reuniens' spatial working memory role
          or the PVT's stress/reward role.
        * Documented as "contributes to" and "presumed contribution,"
          not "is the" or "demonstrated role."
    - Limbic modulation (secondary; poorly characterized): the Pt's
      limbic projections suggest a modulatory role in affective and
      mnemonic processing, but the specific contribution is thin.
      Document as "presumed contribution."
    - The Pt is therefore the midline family's THIN-LITERATURE member
      alongside the rhomboidal: it has a real role (olfactory-limbic
      integration) but is less well characterized than the reuniens
      and PVT. Do not over-write.

    - CLINICAL FACT (honest): the Pt's clinical contribution is
      UNDOCUMENTED. Pt-specific lesions and Pt-specific syndromes are
      NOT established; the Pt's clinical relevance is as part of the
      broader midline-family picture. Do not claim a Pt-specific
      clinical syndrome that the literature does not establish. Same
      honest stance as the LD, the AM, the zona incerta, and the
      lateral tuberal nuclei.

Hormonal Modulation (minimal; the Pt is an olfactory-limbic relay):
    - The Pt is NOT a neuroendocrine structure.
    - Modulators: olfactory inputs (via piriform/entorhinal), limbic
      inputs (amygdala, hippocampus), and brainstem arousal inputs.
      Document as olfactory-limbic modulation, not endocrine
      modulation.
    - The Pt is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the Pt's hippocampal-adjacent projections suggest
          a presumed read of episodic/olfactory-mnemonic context
          (secondary; poorly characterized).
        * short_term: the current olfactory-limbic state buffer
          (presumed; poorly characterized).
    - Writes: none directly. The Pt is a RELAY: it transmits
      olfactory-limbic signals between the olfactory cortices and the
      amygdala/hippocampus/PFC; the memory content is stored in the
      cortex and hippocampus.
    - The Pt's memory interface is THIN (episodic presumed + short_term
      presumed). Do not pad with interfaces the literature does not
      support.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No Pt fragment. The Pt is an olfactory-limbic relay; the model
      prompt does not need a paratenial-nucleus block because the
      olfactory-limbic signals it relays are already represented in
      the upstream (olfactory cortices, amygdala, hippocampus) and
      downstream (amygdala, hippocampus, PFC) fragments. The
      emotional_valence and episodic state is carried by the upstream
      fragments.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The Pt's clinical contribution (undocumented) is noted for
      completeness, but is not a prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/medial_nuclear_group/paratenial_nucleus/):

    Olfactory-limbic integration (the anchor; honestly
    "presumed"/"contributes to"):
    - ← telencephalon/.../rhinencephalon/piriform_cortex and
      telencephalon/.../cortex/temporal/*/entorhinal_cortex
      (olfactory cortical inputs; the piriform cortex and entorhinal
      cortex are the primary olfactory cortical regions; the Pt is
      olfactory-limbic).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (limbic-affective input; the amygdala is the primary limbic
      input to the Pt).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (hippocampal-mnemonic input; the Pt's hippocampal
      input overlaps with the reuniens').
    - → telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (Pt → amygdala; the Pt's limbic output; presumed affective
      modulation).
    - → telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (Pt → hippocampus; presumed mnemonic modulation).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      prefrontal_cortex (Pt → PFC; presumed limbic-prefrontal
      modulation).

    Intra-family:
    - ↔ ../reuniens_nucleus/ (adjacent; reuniens is the hippocampal
      relay anchor; Pt is the olfactory-limbic relay; different
      emphases; do not merge).
    - ↔ ../rhomboidal_nucleus/ (adjacent; both are less-characterized
      olfactory-limbic relays; distinct nuclei; do not merge).
    - ↔ ../midline_nuclear_group/ (the sub-container's structural
      note applies: the Pt and the sub-container are siblings, not
      parent-child; the sub-container integrates the family's
      collective role).

Notes:
    - Tier 1 full leaf (left). The Pt is the midline family's
      THIN-LITERATURE member alongside the rhomboidal: real role
      (olfactory-limbic integration), less characterized than the
      reuniens and PVT. Do not over-write; ~60 lines matches the
      honest literature weight (the reuniens will be ~90; the
      rhomboidal ~55; the Pt is genuinely mid-thin).
    - THE Pt vs. REUNIENS distinction (the primary intra-family
      distinction) is reproduced: Pt is olfactory-limbic (less
      studied); reuniens is hippocampal (well studied). Do not merge.
    - THE Pt vs. RHOMBOIDAL distinction is reproduced: both are
      less-characterized olfactory-limbic relays; they are distinct
      nuclei despite sharing some inputs. Do not merge.
    - HONESTY DISCIPLINE: the Pt's contribution to olfactory-limbic
      integration is less established than the reuniens' spatial
      working memory or the PVT's stress/reward. Documented as
      "contributes to" and "presumed contribution," not "is the" and
      "demonstrated role." Same discipline as the zona incerta, the
      tuberal nucleus, INAH-1/2, and the lateral tuberal nuclei.
    - CLINICAL FACT (honest): Pt-specific lesions and syndromes are
      NOT established. The Pt's clinical relevance is as part of the
      broader midline-family picture. Do not invent a Pt-specific
      syndrome.
    - NO FRAGMENT: same as the whole thalamus. The Pt is a relay, not
      a state-emitter.
    - The Pt is NOT the reuniens (hippocampal relay anchor), NOT the
      rhomboidal (adjacent less-characterized nucleus), NOT the PVT
      (stress/reward relay). The distinctions make these explicit.
    - THE PVT-vs-PVN TRAP does not apply directly to the Pt (the Pt
      is not the PVT), but the midline sub-container's trap declaration
      applies to the Pt's family context. The Pt leaf does not
      re-declare the trap; it points to the family context.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, GABA,
      glutamate); memory/stores/ (episodic, short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/medial_nuclear_
      group/.
"""