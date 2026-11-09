"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.arcuate_nucleus.right
Anatomical Role:
    Right arcuate nucleus (ARC; infundibular nucleus). Same small,
    arc-shaped nucleus at the base of the right mediobasal hypothalamus
    documented in ../left/, containing the same FOUR intermingled
    functional populations:
        1. Kisspeptin KNDy neurons (GnRH pulse generator; estradiol
           negative feedback).
        2. Tuberoinfundibular dopaminergic (TIDA) neurons (PRIMARY
           prolactin inhibitor).
        3. GHRH neurons (stimulatory arm of the growth axis).
        4. Feeding populations (NPY/AgRP hunger; POMC/CART satiety).
    See ../left/__init__.py for the full anatomical description, the
    four-role independence discipline, the complete hormone directions
    per population, and the complete memory interfaces per population.
    This file is a delta; it does not restate that content.

    Reproduced FOUR TRAPS (apply equally on the right; each resolves a
    specific conflation risk):
    - TRAP 1: right arcuate TIDA (primary prolactin inhibitor) vs.
      right periventricular A14 (supplementary; function less
      established). Do not conflate.
    - TRAP 2: right arcuate KNDy (pulse generator) vs. right AVPV
      (surge relay; other_preoptic_nuclei/right/). Complementary
      kisspeptin populations, not duplicates.
    - TRAP 3: right arcuate GHRH (stimulatory) vs. right PVN
      somatostatin (inhibitory;
      anterior/medial_area/right/paraventricular_nucleus/).
      Complementary growth-axis arms, not duplicates.
    - TRAP 4: right arcuate → right tuberal LHA segment 2
      (tuberal/lateral_area/right/tuberal_part_of_lateral_nucleus/;
      EFFERENT PROJECTION, not continuity). The arcuate is NOT part of
      the LHA field; it is a source that projects onto segment 2.

Functional Mode:
    Same four independent roles as ../left/: reproductive pulse (KNDy),
    prolactin inhibition (TIDA), growth stimulation (GHRH), feeding
    (NPY/AgRP + POMC/CART). No documented functional asymmetry between
    left and right arcuate. Do not fabricate one. See ../left/
    § Functional Mode for the full four-role description.

Hormonal Modulation:
    Same as ../left/, per population:
        * KNDy: estradiol ↓ (negative feedback); NKB ↑ firing;
          dynorphin ↓ firing.
        * TIDA: dopamine output; prolactin ↑ TIDA (short-loop
          feedback); suckling ↓ TIDA.
        * GHRH: IGF-1 ↓ GHRH; ghrelin ↑ GHRH.
        * NPY/AgRP: ghrelin ↑; leptin ↓; insulin/glucose/PYY/GLP-1/
          CCK ↓.
        * POMC/CART: leptin ↑; ghrelin ↓; insulin/glucose/PYY/GLP-1/
          CCK ↑.
    See ../left/ § Hormonal Modulation for the full per-population
    detail.

Memory Interfaces:
    Same as ../left/, per population. KNDy reads short_term (estradiol),
    temporal_sequence_learning (cycle phase), episodic (cycle history),
    emotional_valence (stress). TIDA reads short_term (prolactin,
    suckling), episodic (lactation history). GHRH reads short_term
    (metabolic), episodic (growth history). NPY/AgRP + POMC/CART reads
    short_term (metabolic), episodic (feeding history),
    reinforcement_value_based_learning (feeding outcomes),
    emotional_valence (stress), temporal_sequence_learning (circadian
    feeding rhythm). Writes reinforcement_value_based_learning
    indirectly. See ../left/ § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent arcuate fragment. The four roles contribute
    CONSTITUENT INPUTS to the same four aggregates documented in
    ../left/:
        (1) Feeding/satiety → aggregated with right VMH.
        (2) Prolactin-adjacent → right TIDA (primary) + right PeV A14
            (supplementary).
        (3) Growth → right GHRH (stimulatory) + right PVN somatostatin
            (inhibitory).
        (4) Reproductive pulse → right KNDy (pulse) + right PeN/MPN/
            MnPO/AVPV (surge).
    The parent tuberal/medial_area/ and tuberal/ containers' AGGREGATION
    RULES apply identically on the right. The four guardrails inherited
    from the aggregates apply identically (feeding "hunger"; reproductive
    "periovulatory"; growth "catabolic"; prolactin "elevated"). See
    ../left/ § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4 (organized
by role; the left-side edges are in ../left/):

    Reproductive pulse (KNDy):
    - ↔ other_preoptic_nuclei/right (AVPV; pulse vs. surge;
      TRAP 2; complementary pair, not duplicate; right-side).
    - ↔ anterior/medial_area/right/preoptic_area (MPN + MnPO + PeN;
      reproductive axis partners; right-side).
    - → preoptic GnRH neuron population (KNDy kisspeptin → GnRH
      terminals; right-side reproductive output edge).

    Prolactin inhibition (TIDA):
    - → median_eminence (TIDA dopamine terminals; midline — verify;
      the prolactin inhibition output edge).
    - ↔ hypothalamus/periventricular_nucleus/right (PeV A14; TIDA
      primary vs. A14 supplementary; TRAP 1; right-side).

    Growth (GHRH):
    - → median_eminence (GHRH terminals; midline — verify; the growth
      stimulation output edge).
    - ↔ anterior/medial_area/right/paraventricular_nucleus (PVN
      somatostatin inhibitory vs. arcuate GHRH stimulatory; TRAP 3;
      complementary pair; right-side).
    - ↔ anterior/medial_area/right/paraventricular_nucleus (NPY/AgRP
      → PVN feeding circuit; and POMC α-MSH → PVN MC4R satiety
      circuit; right-side).

    Feeding (NPY/AgRP + POMC/CART):
    - ↔ tuberal/lateral_area/right/tuberal_part_of_lateral_nucleus
      (arcuate NPY/AgRP → tuberal MCH; arcuate-adjacent leptin/ghrelin
      → tuberal ORX; EFFERENT PROJECTION, not continuity; TRAP 4; the
      deferred closure of the right LHA segment 2's distinctive input;
      right-side).
    - ↔ tuberal/medial_area/right/ventromedial_nucleus (adjacent
      feeding nuclei; complementary feeding roles; right-side; VMH
      reciprocates when drafted).
    - ↔ anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (arcuate → LHA orexin/MCH; right-side).

    Cross-cutting:
    - ← brainstem/.../solitary_nucleus (NTS; visceral satiety signals
      — CCK, GLP-1, PYY; midline-adjacent — verify).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (emotional/stress context; right-side).
    - ↔ tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus
      (adjacent tuberal feeding/circadian cross-talk; right-side; DMH
      reciprocates when drafted).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN; circadian gating; midline-adjacent — verify).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - FOUR TRAPS reproduced in abbreviated form above; the full text is
      in ../left/ and in the parent tuberal/medial_area/ container. A
      contributor entering at the right arcuate must see them.
    - The four roles are independent on the right, same as the left:
      each has its own population, downstream targets, aggregation
      rule, and memory interfaces. Do not flatten.
    - THREE DEFERRED EDGE CLOSURES — RIGHT SIDE: this delta closes the
      right arcuate ends of the three edges declared from the other
      side earlier:
        (1) Arcuate → tuberal LHA segment 2 (feeding projection;
            declared in tuberal/lateral_area/right/
            tuberal_part_of_lateral_nucleus/; TRAP 4; efferent
            projection, not continuity).
        (2) Arcuate ↔ PeV A14 (TIDA primary vs. A14 supplementary;
            declared in periventricular_nucleus/right/; TRAP 1).
        (3) Arcuate ↔ AVPV (pulse vs. surge; declared in
            other_preoptic_nuclei/right/; TRAP 2).
      With this file, all three deferred edges are now closed on BOTH
      hemispheres.
    - ARCUATE PAIR NOW COMPLETE: with this file, the ★★ tuberal
      flagship is fully documented on both hemispheres — the most
      functionally dense nucleus in the entire hypothalamus is done.
    - The arcuate is NOT the AVPV (pulse vs. surge), NOT the PeV A14
      (primary vs. supplementary), NOT the tuberal LHA (efferent source
      vs. field segment), NOT the PVN somatostatin (stimulatory vs.
      inhibitory growth arm). Same distinctions as ../left/; the four
      traps make them explicit on the right.
    - No independent fragment: four constituent inputs to the same
      four aggregates documented in ../left/.
    - Midline targets (median eminence, NTS, SCN) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree. Right
      AVPV, right PeV A14, right PeN/MPN/MnPO, right PVN, right VMH,
      right DMH, right tuberal LHA, right amygdala, right anterior
      LHA, and right preoptic GnRH neurons are hemisphere-split and
      require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see ../left/
      § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/medial_area/
      arcuate_nucleus/.
"""