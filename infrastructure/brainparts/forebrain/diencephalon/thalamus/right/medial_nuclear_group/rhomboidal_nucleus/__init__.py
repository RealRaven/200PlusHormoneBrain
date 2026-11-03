"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.rhomboidal_nucleus
Anatomical Role:
    The right rhomboidal nucleus (Rh). The smallest and least
    characterized of the three right midline thalamic nuclei, situated
    at the midline of the right thalamus, immediately adjacent to (and
    often considered a ventral continuation of) the right reuniens
    nucleus. Same LIMBIC-ADJACENT RELAY role as the left Rh: it
    receives hypothalamic and limbic inputs and projects to the right
    hippocampus, right amygdala, and right prefrontal cortex, with a
    projection profile that overlaps substantially with the right
    reuniens.

    See ../../../../left/medial_nuclear_group/rhomboidal_nucleus/
    __init__.py for the full anatomical description, the
    "reuniens-rhomboidal complex" framing, the honest "less well
    characterized" stance, the "no Rh-specific syndrome" honesty, and
    the full reciprocal edge list.

    Reproduced distinctions (apply equally on the right):
    - RH vs. REUNIENS (intra-family; primary): the right Rh is
      anatomically adjacent to and functionally overlapping with the
      right reuniens (right/medial_nuclear_group/reuniens_nucleus/);
      the reuniens is the HIPPOCAMPAL relay (well-studied; spatial
      working memory; the family anchor); the Rh is the less-studied
      limbic-adjacent neighbor. Often studied together as the
      "reuniens-rhomboidal complex"; document the complex framing but
      keep the two nuclei as distinct tree nodes; do not merge.
    - RH vs. PARATENIAL (intra-family): both are the family's
      "less-characterized" members; the right paratenial
      (right/medial_nuclear_group/paratenial_nucleus/) is
      dorsal-adjacent (olfactory-limbic emphasis); the right Rh is
      ventral-adjacent to the right reuniens (limbic-hippocampal
      emphasis). Distinct nuclei; do not merge.
    - RH vs. PVT (intra-family): the right PVT (if added) is the
      stress/reward relay; the right Rh is the limbic-adjacent relay.
      Different emphases; do not merge.
    - RH vs. INTRALAMINAR FAMILY (family-level): the right Rh is part
      of the midline family's LIMBIC/VISCERAL relay system; the right
      intralaminar family is AROUSAL/ATTENTION. Different families;
      do not merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/rhomboidal_nucleus/.
    Limbic-adjacent relay (the anchor; honestly "contributes to");
    hippocampal-adjacent modulation (secondary; poorly characterized;
    often conflated with the reuniens). No documented functional
    asymmetry between left and right Rh. Do not fabricate one.

    CLINICAL FACT (honest; applies on the right): the right Rh's
    clinical contribution is UNDOCUMENTED. Right Rh-specific lesions
    and syndromes are NOT established; the right Rh's clinical
    relevance is as part of the broader midline-family picture, often
    grouped with the right reuniens. Do not claim a right-Rh-specific
    syndrome.

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/rhomboidal_nucleus/.
    Minimal; hypothalamic inputs, limbic inputs (right amygdala, right
    hippocampus), and brainstem arousal inputs. Not a principal target
    of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/rhomboidal_nucleus/.
    Reads episodic (presumed; hippocampal-adjacent; often grouped with
    the right reuniens' episodic read) and short_term (presumed;
    limbic state). Writes nothing directly (relay, not encoder). Thin
    interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right Rh fragment. The Rh is a limbic-adjacent relay; the model
    prompt does not need a rhomboidal-nucleus block. The limbic
    signals it relays are already represented in the upstream (right
    hypothalamus, right hippocampus, right amygdala) and downstream
    (right hippocampus, right amygdala, right PFC) fragments. Same
    deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Limbic-adjacent relay (the anchor; honestly "presumed"/
    "contributes to"):
    - ← hypothalamus/*/right (hypothalamic limbic inputs; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (limbic-affective input; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (hippocampal-mnemonic input; right-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/
      hippocampus (right Rh → right hippocampus; presumed mnemonic
      modulation; right-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (right Rh → right amygdala; presumed affective modulation;
      right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/frontal/
      prefrontal_cortex (right Rh → right PFC; presumed
      limbic-prefrontal modulation; right-side).

    Reuniens-rhomboidal complex (the "complex" framing):
    - ↔ ../reuniens_nucleus/ (the right Rh and right reuniens are
      anatomically adjacent and functionally overlapping; often
      studied together as the "reuniens-rhomboidal complex"; the right
      reuniens is the well-studied anchor, the right Rh is the
      less-studied neighbor; do not merge; document the complex
      relationship).

    Intra-family:
    - ↔ ../paratenial_nucleus/ (right Pt; both are less-characterized
      limbic-adjacent relays; distinct nuclei; do not merge).
    - ↔ ../midline_nuclear_group/ (the sub-container's structural
      note applies: the right Rh and the sub-container are siblings,
      not parent-child; the sub-container integrates the family's
      collective role).

    - ↔ ../../../../left/medial_nuclear_group/rhomboidal_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      rhomboidal_nucleus/. Not a full leaf. Do not duplicate.
    - Tier 1 leaf delta, SHORT BY DESIGN (~50 lines): the Rh is the
      thinnest-literature member of the midline family. Same honest
      weight as the left leaf; do not inflate the delta to "catch up"
      with the reuniens.
    - THE REUNIENS-RHOMBOIDAL COMPLEX framing is reproduced: the two
      nuclei are often studied together; the right reuniens is the
      well-studied anchor; the right Rh is the less-studied neighbor.
      Document the complex relationship but keep the two nuclei as
      distinct tree nodes.
    - THE RH vs. REUNIENS and RH vs. PARATENIAL distinctions are
      reproduced in abbreviated form; the full text is in
      ../../../../left/medial_nuclear_group/rhomboidal_nucleus/ and
      ../../../__init__.py.
    - HONESTY DISCIPLINE: the right Rh's contribution is "contributes
      to" and "presumed contribution," not "is the" and "demonstrated
      role." Same as the left leaf.
    - CLINICAL FACT (honest): no right-Rh-specific syndrome. Do not
      invent one.
    - NO FRAGMENT: same as the whole thalamus. The right Rh is a
      relay, not a state-emitter.
    - THE PVT-vs-PVN TRAP does not apply directly to the Rh; the
      midline sub-container's trap declaration applies to the Rh's
      family context.
    - THE MEDIAL NUCLEAR GROUP IS NOW COMPLETE — BOTH HEMISPHERES:
      with this file, the entire medial nuclear group is fully
      documented:
        * Group container pair (2 files).
        * MD pair (2 files; the group's anchor).
        * Intralaminar family (8 files: CL pair, CM pair, Pf pair,
          sub-container pair).
        * Midline family (8 files: paratenial pair, reuniens pair,
          rhomboidal pair, sub-container pair).
      20 files total, all complete (assuming no separate PVT node).
      The medial nuclear group is the fourth fully-completed thalamic
      group after the anterior, lateral, and (as a family within it)
      intralaminar families.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right hypothalamus, right amygdala, right hippocampus, right
      PFC, right reuniens, right paratenial, right midline
      sub-container). Stage 4 should not confuse right-side edges with
      left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/rhomboidal_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""