"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.paratenial_nucleus
Anatomical Role:
    The right paratenial nucleus (Pt). One of the midline thalamic
    nuclei, situated along the midline of the right thalamus, adjacent
    to the right reuniens and rhomboidal nuclei. Same OLFACTORY-LIMBIC
    RELAY role as the left Pt: it receives olfactory and limbic inputs
    and projects to the right amygdala, right hippocampus, and right
    prefrontal cortex.

    See ../../../../left/medial_nuclear_group/paratenial_nucleus/
    __init__.py for the full anatomical description, the honest
    "less well characterized" framing, the "contributes to
    olfactory-limbic integration" role, and the "no Pt-specific
    syndrome" honesty.

    Reproduced distinctions (apply equally on the right):
    - Pt vs. REUNIENS (intra-family; primary): the right Pt is the
      OLFACTORY-LIMBIC relay (less studied); the right reuniens
      (right/medial_nuclear_group/reuniens_nucleus/) is the
      HIPPOCAMPAL relay (well studied; spatial working memory).
      Different emphases; do not merge.
    - Pt vs. RHOMBOIDAL (intra-family): both are less-characterized
      olfactory-limbic relays; anatomically adjacent but distinct
      nuclei; do not merge.
    - Pt vs. PVT (intra-family): the right PVT (if added) is the
      family's stress/reward relay; the right Pt is the
      olfactory-limbic relay. Different emphases; do not merge.
    - Pt vs. INTRALAMINAR FAMILY (family-level): the right Pt is part
      of the midline family's LIMBIC/VISCERAL relay system; the right
      intralaminar family
      (right/medial_nuclear_group/intralaminar_nuclear_group/) is
      AROUSAL/ATTENTION. Different families; do not merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/paratenial_nucleus/.
    Olfactory-limbic integration (the anchor; honestly "contributes
    to"); limbic modulation (secondary; poorly characterized). No
    documented functional asymmetry between left and right Pt. Do not
    fabricate one.

    CLINICAL FACT (honest; applies on the right): the right Pt's
    clinical contribution is UNDOCUMENTED. Right Pt-specific lesions
    and syndromes are NOT established; the right Pt's clinical
    relevance is as part of the broader midline-family picture. Do not
    claim a right-Pt-specific syndrome.

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/paratenial_nucleus/.
    Minimal; olfactory inputs (right piriform/entorhinal), limbic
    inputs (right amygdala, right hippocampus), and brainstem arousal
    inputs. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/paratenial_nucleus/.
    Reads episodic (presumed; hippocampal-adjacent) and short_term
    (presumed; olfactory-limbic state). Writes nothing directly (relay,
    not encoder). Thin interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right Pt fragment. The Pt is an olfactory-limbic relay; the
    model prompt does not need a paratenial-nucleus block. The
    olfactory-limbic signals it relays are already represented in the
    upstream (right olfactory cortices, right amygdala, right
    hippocampus) and downstream (right amygdala, right hippocampus,
    right PFC) fragments. Same deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Olfactory-limbic integration (the anchor; honestly "presumed"/
    "contributes to"):
    - ← telencephalon/.../rhinencephalon/piriform_cortex and
      telencephalon/.../cortex/temporal/*/entorhinal_cortex
      (olfactory cortical inputs; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (limbic-affective input; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (hippocampal-mnemonic input; right-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (right Pt → right amygdala; presumed affective modulation;
      right-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (right Pt → right hippocampus; presumed mnemonic
      modulation; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/frontal/
      prefrontal_cortex (right Pt → right PFC; presumed
      limbic-prefrontal modulation; right-side).

    Intra-family:
    - ↔ ../reuniens_nucleus/ (right reuniens; hippocampal relay
      anchor; different emphasis; do not merge).
    - ↔ ../rhomboidal_nucleus/ (right rhomboidal; both are
      less-characterized olfactory-limbic relays; distinct nuclei; do
      not merge).
    - ↔ ../midline_nuclear_group/ (the sub-container's structural
      note applies: the right Pt and the sub-container are siblings,
      not parent-child; the sub-container integrates the family's
      collective role).

    - ↔ ../../../../left/medial_nuclear_group/paratenial_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      paratenial_nucleus/. Not a full leaf. Do not duplicate.
    - Tier 1 leaf delta, SHORT BY DESIGN (~50 lines): the Pt is the
      thin-literature member of the midline family. Same honest weight
      as the left leaf; do not inflate the delta to "catch up" with
      the reuniens.
    - THE Pt vs. REUNIENS distinction is reproduced: right Pt is
      olfactory-limbic (less studied); right reuniens is hippocampal
      (well studied). Do not merge.
    - THE Pt vs. RHOMBOIDAL distinction is reproduced: both are
      less-characterized olfactory-limbic relays; distinct nuclei.
    - HONESTY DISCIPLINE: the right Pt's contribution is "contributes
      to" and "presumed contribution," not "is the" and "demonstrated
      role." Same as the left leaf.
    - CLINICAL FACT (honest): no right-Pt-specific syndrome. Do not
      invent one.
    - NO FRAGMENT: same as the whole thalamus. The right Pt is a
      relay, not a state-emitter.
    - THE PVT-vs-PVN TRAP does not apply directly to the Pt; the
      midline sub-container's trap declaration applies to the Pt's
      family context. The Pt leaf does not re-declare the trap.
    - THE PARATENIAL PAIR IS NOW COMPLETE: with this file, the
      paratenial nucleus is fully documented on both hemispheres.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right piriform, right entorhinal, right amygdala, right
      hippocampus, right PFC). Stage 4 should not confuse right-side
      edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/paratenial_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""