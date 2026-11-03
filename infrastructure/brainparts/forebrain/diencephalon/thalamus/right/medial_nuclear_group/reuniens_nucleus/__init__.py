"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.reuniens_nucleus
Anatomical Role:
    The right reuniens nucleus (Re). The most studied of the three
    midline thalamic nuclei, situated at the midline of the right
    thalamus, adjacent to the right paratenial and rhomboidal nuclei
    and to the third ventricle. Same HIPPOCAMPAL-PREFRONTAL RELAY role
    as the left reuniens: it is reciprocally connected with the right
    hippocampus (especially CA1 and subiculum) and the right medial
    prefrontal cortex (mPFC), and it is the principal thalamic hub of
    the right hippocampal-prefrontal communication system.

    See ../../../../left/medial_nuclear_group/reuniens_nucleus/
    __init__.py for the full anatomical description, the
    hippocampal-prefrontal loop framing, the spatial working memory
    role, the "reuniens as midline family anchor" framing, and the
    full clinical fact list.

    Reproduced distinctions (apply equally on the right):
    - REUNIENS vs. ANTERIOR NUCLEAR GROUP (primary
      hippocampal-adjacent trap): both are hippocampal-adjacent
      thalamic relays, but via DIFFERENT circuits — the right anterior
      nuclei via the Papez circuit (hippocampus → fornix → mammillary
      bodies → mammillothalamic tract → anterior nuclei → cingulate),
      the right reuniens via direct hippocampal connections
      (hippocampus CA1/subiculum → reuniens → mPFC). Different memory
      systems; do not merge.
    - REUNIENS vs. MEDIAL DORSAL NUCLEUS (PFC-projecting sub-trap):
      both project to the right PFC, but the right reuniens is
      hippocampus-driven (spatial working memory) while the right MD
      (right/medial_nuclear_group/medial_dorsal_nucleus/) is
      amygdala/PFC-driven (executive/limbic integration). Different
      circuits; do not merge.
    - REUNIENS vs. PARATENIAL and RHOMBOIDAL (intra-family): the right
      reuniens is the hippocampal relay (well-studied; spatial
      working memory); the right paratenial
      (right/medial_nuclear_group/paratenial_nucleus/) and right
      rhomboidal (right/medial_nuclear_group/rhomboidal_nucleus/) are
      the olfactory-limbic relays (less characterized). Different
      emphases; do not merge.
    - REUNIENS vs. PVT (intra-family): the right reuniens is the
      hippocampal relay; the right PVT (if added) is the
      stress/reward relay. Different emphases; do not merge.
    - REUNIENS vs. INTRALAMINAR FAMILY (family-level): the right
      reuniens is part of the midline family's LIMBIC/VISCERAL relay
      system; the right intralaminar family is AROUSAL/ATTENTION.
      Different families; do not merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/reuniens_nucleus/.
    Hippocampal-prefrontal relay (the anchor); spatial working memory
    (the most studied function); executive-adjacent modulation
    (secondary). No documented functional asymmetry between left and
    right reuniens. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically, with the same
    established/investigational framing):
        * RIGHT REUNIENS LESIONS: spatial working memory deficits in
          animal lesion studies (delayed alternation, spatial delayed
          non-matching to sample) while sparing reference memory. This
          is ESTABLISHED; the right reuniens' defining clinical
          anchor.
        * STRESS-RELATED MEMORY IMPAIRMENT (investigational): the
          right reuniens as a node in the stress-memory interaction;
          evidence thinner than the spatial working memory finding.
        * PSYCHIATRIC CONDITIONS (preliminary): schizophrenia and
          depression (both involve hippocampal-prefrontal dysfunction)
          have been associated with reuniens-adjacent structural
          findings; evidence is preliminary.
        * REUNIENS DBS is NOT an established clinical target on the
          right either; the reuniens is a research target for its role
          in hippocampal-prefrontal function.

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/reuniens_nucleus/.
    Minimal; hippocampal (glutamatergic) inputs, right mPFC
    (glutamatergic) inputs, and brainstem arousal inputs. Not a
    principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/reuniens_nucleus/.
    Reads episodic (right hippocampal episodic via right CA1/subiculum;
    distinct from the mammillary-mediated episodic read of the right
    anterior nuclei), short_term (right spatial working-memory buffer),
    temporal_sequence_learning (the right reuniens' role in delayed
    alternation requires temporal-order information). Writes nothing
    directly (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right reuniens fragment. The reuniens is a hippocampal-prefrontal
    relay; the model prompt does not need a reuniens-nucleus block
    because the hippocampal and mPFC signals it relays are already
    represented in the upstream (right hippocampus) and downstream
    (right mPFC) fragments. Same deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Hippocampal-prefrontal relay (the anchor):
    - ← telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus/right/ca1 (the right reuniens' primary hippocampal
      input; CA1 → reuniens; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus/right/subiculum (subicular input to the right
      reuniens; right-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus/right (the right reuniens' reciprocal projection
      back to the right hippocampus; the reuniens-hippocampal
      reciprocal loop; right-side).
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/frontal/
      prefrontal_cortex/medial (the right reuniens ↔ right medial PFC
      reciprocal connection; right-side).

    Hippocampal-prefrontal loop (the functional circuit):
    - The right reuniens bridges the two structures:
        right hippocampus (CA1, subiculum) → right reuniens →
        right medial PFC, and right medial PFC → right reuniens →
        right hippocampus.

    Intra-family:
    - ↔ ../paratenial_nucleus/ (right Pt; olfactory-limbic relay;
      different emphasis; do not merge).
    - ↔ ../rhomboidal_nucleus/ (right Rh; olfactory-limbic relay;
      different emphasis; do not merge).
    - ↔ ../midline_nuclear_group/ (the sub-container's structural
      note applies: the right reuniens and the sub-container are
      siblings, not parent-child; the sub-container integrates the
      family's collective role; the right reuniens is the family's
      anchor).

    Distinction (not signaling; structural note):
    - ↔ ../../anterior_nuclear_group/ (the right anterior nuclei are
      the PAPEZ episodic-memory relays; the right reuniens is the
      HIPPOCAMPAL-PREFRONTAL spatial-working-memory relay; different
      circuits converging on the right hippocampus but through
      different pathways; do not merge).
    - ↔ ../medial_dorsal_nucleus/ (the right MD is the
      executive/limbic-prefrontal relay; the right reuniens is the
      hippocampal-prefrontal relay; different circuits; do not
      merge).

    - ↔ ../../../../left/medial_nuclear_group/reuniens_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      reuniens_nucleus/. Not a full leaf. Do not duplicate.
    - THE REUNIENS PAIR IS NOW COMPLETE: with this file, the reuniens
      nucleus is fully documented on both hemispheres — the midline
      family's anchor is done. The spatial working memory clinical
      anchor is documented on both sides.
    - THE TWO TRAPS are reproduced in abbreviated form; the full text
      is in ../../../../left/medial_nuclear_group/reuniens_nucleus/
      and ../../../__init__.py. A contributor entering at the right
      reuniens must see them.
    - THE REUNIENS' DISTINCTIVE EPISODIC READ is reproduced: the right
      reuniens reads right hippocampal episodic (CA1/subiculum) while
      the right anterior nuclei read mammillary episodic
      (mammillothalamic tract). Different circuits; the trap makes
      this explicit on the right too.
    - THE CLINICAL FACT (spatial working memory deficits, ESTABLISHED)
      applies on the right identically. The investigational findings
      (stress, psychiatric) are reproduced with the same honesty
      framing.
    - NO FRAGMENT: same as the whole thalamus. The right reuniens is a
      relay, not a state-emitter. The episodic and working-memory
      state is carried by the right hippocampus and the right mPFC.
    - The right reuniens is NOT the right anterior group (Papez
      episodic relay), NOT the right MD (amygdala/limbic-prefrontal),
      NOT the right paratenial or rhomboidal (olfactory-limbic). The
      traps make these distinctions explicit on the right.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right CA1, right subiculum, right hippocampus, right mPFC,
      right paratenial, right rhomboidal, right midline sub-container).
      Stage 4 should not confuse right-side edges with left-side
      edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/reuniens_nucleus/ § Notes
      for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""