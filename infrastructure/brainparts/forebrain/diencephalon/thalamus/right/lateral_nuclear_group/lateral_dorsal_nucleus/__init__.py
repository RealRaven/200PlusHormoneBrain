"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.lateral_nuclear_group.lateral_dorsal_nucleus
Anatomical Role:
    The right lateral dorsal nucleus (LD). The SMALLEST and LEAST
    CHARACTERIZED of the three right lateral nuclear group nuclei,
    situated on the dorsolateral aspect of the right thalamus. Same
    higher-order limbic-adjacent association role as the left LD: it
    receives right cortical layer 5 input and projects to the right
    cingulate cortex and right retrosplenial cortex — the same
    cortical targets as the right anterior thalamic nuclei (AD, AM,
    AV), but via a different circuit (association relay, not Papez
    memory relay).

    See ../../../../left/lateral_nuclear_group/lateral_dorsal_
    nucleus/__init__.py for the full anatomical description, the
    honest "less well characterized" framing, and the thin-literature
    discipline.

    Reproduced distinctions (apply equally on the right):
    - LD vs. ANTERIOR NUCLEAR GROUP (the primary trap): the right LD
      and the right anterior nuclei both project to the right
      cingulate and retrosplenial cortices. But the right LD is a
      HIGHER-ORDER ASSOCIATION relay (cortical layer 5 driver), NOT a
      Papez memory relay (hippocampal/mammillary driver). Different
      circuits converging on similar cortical targets. Do not merge
      the right LD with the right AD/AM/AV.
    - LD vs. LATERAL POSTERIOR: the right LP is the parietal
      association relay; the right LD is the limbic-adjacent
      association relay. Different domains; do not merge.
    - LD vs. PULVINAR: the right pulvinar is the visual association
      relay; the right LD is the limbic-adjacent association relay.
      Different domains; do not merge.
    - LD vs. MEDIODORSAL NUCLEUS: the right LD projects to cingulate;
      the right MD (right/medial_nuclear_group/medial_dorsal_nucleus/)
      projects to prefrontal. Different association domains; do not
      merge.

Functional Mode:
    Same as ../../../../left/lateral_nuclear_group/lateral_dorsal_
    nucleus/. Higher-order limbic-adjacent association (the anchor,
    with the "less characterized" caveat); spatial memory (secondary;
    "presumed contribution," not "demonstrated role"). No documented
    functional asymmetry between left and right LD. Do not fabricate
    one.

    CLINICAL FACT (honest): the right LD's clinical contribution is
    undocumented in isolation. LD-specific lesions and syndromes are
    NOT established; the right LD's clinical relevance is as part of
    the broader limbic-adjacent association picture. Do not claim a
    right-LD-specific syndrome that the literature does not establish.

Hormonal Modulation:
    Same as ../../../../left/lateral_nuclear_group/lateral_dorsal_
    nucleus/. Minimal; cholinergic and monoaminergic arousal
    modulation; not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/lateral_nuclear_group/lateral_dorsal_
    nucleus/. Reads episodic (limbic-adjacent role), short_term
    (cortical association loop). Writes nothing directly (relay, not
    encoder). No distinct semantic interface documented; do not pad.

Model Integration (Gemma-4-E2B):
    No right LD fragment. The LD is a higher-order association relay;
    the model prompt does not need an LD block. The association state
    is carried by the right cingulate and retrosplenial cortex. Same
    deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Higher-order limbic-adjacent association (the anchor):
    - ← telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate and telencephalon/.../cortex/cingulate/
      retrosplenial_cortex (cortical layer 5 input; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate and telencephalon/.../cortex/cingulate/
      retrosplenial_cortex (LD output to right cingulate and
      retrosplenial; the higher-order association loop; right-side).

    Intra-group:
    - ↔ ../lateral_posterior_nucleus/ (right LP; parietal association;
      different domain; do not merge).
    - ↔ ../pulvinar/ (right pulvinar; visual association; different
      domain; do not merge).

    - ↔ ../../../../left/lateral_nuclear_group/lateral_dorsal_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/lateral_nuclear_group/
      lateral_dorsal_nucleus/. Not a full leaf. Do not duplicate.
    - Tier 1 leaf delta, SHORT BY DESIGN (~50 lines): the LD is the
      thin-literature nucleus of the lateral group. Same honest weight
      as the left leaf; do not inflate the delta to "catch up" with
      the pulvinar or LP.
    - THE LD vs. ANTERIOR NUCLEAR GROUP TRAP is reproduced in
      abbreviated form; the full text is in
      ../../../../left/lateral_nuclear_group/lateral_dorsal_nucleus/
      and ../../../__init__.py. A contributor entering at the right
      LD must see it.
    - LD vs. LP and LD vs. pulvinar distinctions reproduced: right LD
      is the limbic-adjacent association relay; right LP is parietal;
      right pulvinar is visual. Different domains.
    - HONESTY DISCIPLINE: the right LD's contribution is "contributes
      to" and "presumed contribution," not "is the" and "demonstrated
      role." Same as the left leaf.
    - CLINICAL FACT (honest): no right-LD-specific syndrome. Do not
      invent one.
    - NO FRAGMENT: same as the whole thalamus. The right LD is a
      relay, not a state-emitter.
    - THE LATERAL GROUP IS NOT A FIRST-ORDER SENSORY GROUP: same on
      the right. The right LD relays cortico-cortical association,
      not primary sensory input.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/lateral_nuclear_group/lateral_dorsal_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/lateral_nuclear_
      group/.
"""