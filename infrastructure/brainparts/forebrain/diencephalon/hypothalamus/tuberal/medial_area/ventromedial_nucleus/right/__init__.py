"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.ventromedial_nucleus.right
Anatomical Role:
    Right ventromedial nucleus of the hypothalamus (VMH). Same large,
    spherical nucleus in the right mediobasal tuberal hypothalamus
    documented in ../left/, with the same FOUR principal functional
    roles distributed across subdivisions (documented WITHIN this file,
    not as child nodes):
        - VMHc (central): satiety and meal termination.
        - VMHvl (ventrolateral): defensive aggression (male-typical) and
          female sexual behavior (female-typical); sexually dimorphic.
        - VMHdm (dorsomedial): thermogenic sympathetic drive.
        - VMH shell: surrounds the core subdivisions.
    See ../left/__init__.py for the full anatomical description, the
    four-role independence discipline, the complete per-role hormone
    directions, and the per-role memory interfaces.

    Reproduced FOUR TRAPS (apply equally on the right):
    - TRAP 4: VMH vs. DMH (adjacent-nuclei trap; VMH =
      satiety/aggression/thermoregulation/sexual behavior; DMH =
      circadian relay; do not merge).
    - TRAP 7a: VMH vs. AHN (thermoregulatory complementarity; VMH =
      thermogenic effector; AHN = parasympathetic thermoregulatory arm;
      part of the thermoregulatory triangle; complementary, not
      duplicate).
    - TRAP 7b: VMH vs. PHN (sympathetic complementarity; VMH =
      thermogenic sympathetic drive; PHN = whole-body sympathetic
      outflow; complementary, not duplicate).
    - VMH vs. ARCUATE (feeding complementarity; arcuate = first-order
      hunger/satiety; VMH = satiety center and meal termination;
      complementary, not duplicate).

Functional Mode:
    Same four independent roles as ../left/: satiety/meal termination
    (VMHc), defensive aggression (VMHvl), thermoregulation/thermogenesis
    (VMHdm), female sexual behavior (VMHvl). No documented functional
    asymmetry between left and right VMH. Do not fabricate one. See
    ../left/ § Functional Mode for the full four-role description and
    the ventromedial hypothalamic obesity clinical fact (VMH lesions →
    hyperphagia + obesity; the right VMH lesion produces the same
    syndrome as the left).

Hormonal Modulation:
    Same as ../left/, per role:
        * Satiety (VMHc): leptin ↑, insulin ↑, CCK/PYY/GLP-1 ↑,
          serotonin ↑, ghrelin ↓.
        * Aggression (VMHvl; male-typical): testosterone ↑, estrogen
          modulates, serotonin ↓.
        * Thermoregulation (VMHdm): PGE2 ↑, pyrogens ↑, estradiol
          modulates.
        * Female sexual behavior (VMHvl; female-typical): estradiol ↑,
          progesterone (after estradiol priming) ↑, oxytocin ↑;
          kisspeptin/GnRH modulate.
    See ../left/ § Hormonal Modulation for the full per-role detail.

Memory Interfaces:
    Same as ../left/. Reads short_term (metabolic, thermal,
    arousal/aggression, reproductive-hormonal state), episodic (feeding,
    aggression, thermoregulatory, reproductive history),
    emotional_valence (stress/threat context). Writes no stored content
    directly. See ../left/ § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent VMH fragment. The VMH contributes TWO CONSTITUENT
    INPUTS to aggregates established elsewhere:
        (1) Feeding/satiety: aggregated with the right arcuate
            (arcuate = first-order hunger/satiety; VMH = satiety
            center/meal termination).
        (2) Autonomic/thermoregulatory: aggregated with the right AHN
            (parasympathetic arm) and the right PHN (whole-body
            sympathetic). The VMH contributes the thermogenic
            sympathetic drive.
    The aggression and female sexual behavior roles are documented in
    the leaf but do NOT emit separate fragments (behavioral/contextual
    roles, not state biases).
    AGGREGATION RULES (mandatory, applies identically on the right): the
    parent tuberal/medial_area/ container's rules apply. The right VMH's
    feeding contribution aggregates with the right arcuate's; its
    thermoregulatory contribution aggregates with the right AHN's and
    right PHN's. Do not emit a separate right VMH fragment.
    See ../left/ § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:

    Feeding complementarity (the anchor):
    - ↔ tuberal/medial_area/right/arcuate_nucleus (VMH = satiety
      center/meal termination vs. arcuate = first-order hunger/satiety;
      COMPLEMENTARY feeding roles, not duplicate; right-side; closes the
      arcuate leaf's feeding-complementarity note on the right).

    Thermoregulatory triangle (complementary pairs):
    - ↔ anterior/medial_area/right/anterior_hypothalamic_nucleus (VMH
      thermogenic effector vs. AHN parasympathetic thermoregulatory
      control; TRAP 7a; complementary pair, not duplicate; right-side).
    - ↔ posterior/medial_area/right/posterior_nucleus (VMH thermogenic
      sympathetic drive vs. PHN whole-body sympathetic outflow; TRAP
      7b; complementary pair, not duplicate; right-side).
    - ↔ anterior/medial_area/right/preoptic_area (thermoregulatory
      CONTROLLER; the preoptic is the controller, the VMH is the
      effector; complementary roles; right-side).

    Thermoregulatory effector output:
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic premotor output;
      RVLM is midline-adjacent — verify).
    - → spinal_cord/gray_matter/right/lateral_horn (sympathetic
      preganglionic output to BAT and vasculature; right-side).
    - → right brown adipose tissue (via the sympathetic chain;
      thermogenesis effector; pathway downstream of the IML — verify).

    Adjacent-but-distinct:
    - ↔ tuberal/medial_area/right/dorsomedial_hypothalamic_nucleus
      (VMH vs. DMH; TRAP 4; adjacent nuclei, distinct functions, do not
      merge; right-side).

    Aggression and defensive behavior:
    - → midbrain/tegmentum/periaqueductal_gray (defensive aggression
      motor patterns; PAG is midline-adjacent — verify).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (threat/aggression context; right-side).

    Feeding input (upstream):
    - ← tuberal/medial_area/right/arcuate_nucleus (arcuate NPY/AgRP and
      POMC → VMH; first-order feeding signals; right-side).
    - ← brainstem/.../solitary_nucleus (NTS; visceral satiety signals —
      CCK, PYY, GLP-1; NTS is midline-adjacent — verify).

    Female sexual behavior:
    - ← other_preoptic_nuclei/right (AVPV; estrogen-positive-feedback
      surge relay; kisspeptin/GnRH coordination with the VMHvl
      receptivity circuit; right-side).
    - ← anterior/medial_area/right/preoptic_area/medial_preoptic_nucleus
      (MPN; maternal/sexual behavior coordination; right-side).
    - ↔ anterior/medial_area/right/suprachiasmatic_nucleus (SCN;
      circadian gating of female sexual receptivity; SCN is
      midline-adjacent — verify).

    Cross-cutting:
    - ← anterior/medial_area/right/suprachiasmatic_nucleus (SCN;
      circadian gating of feeding, thermoregulation, and sexual behavior
      rhythms; midline-adjacent — verify).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - THIS IS THE FINAL SUBSTANTIVE FILE IN THE ENTIRE HYPOTHALAMUS
      SUBTREE. After this file, only the three container corrections
      (tuberal/lateral_area/ containers naming lateral_tuberal_nuclei/)
      remain, and the largest, most trap-dense region of the entire
      brain tree is complete.
    - ALL THREE DEFERRED COMPLEMENTARY-PAIR EDGE CLOSURES ARE NOW
      COMPLETE ON BOTH HEMISPHERES:
        (1) VMH ↔ AHN (thermoregulatory complementarity): closed on
            left and right.
        (2) VMH ↔ PHN (sympathetic complementarity): closed on left and
            right.
        (3) VMH ↔ arcuate (feeding complementarity): closed on left and
            right.
      The three complementary pairs were each declared from the other
      side earlier; this pair of VMH leaves closes them.
    - All four traps (VMH vs. DMH; VMH vs. AHN; VMH vs. PHN; VMH vs.
      arcuate) are reproduced in abbreviated form above. Trap 4 is
      adjacent-but-distinct; Traps 7a/7b and the arcuate pair are
      complementary-pair relationships. None is a split-structure
      warning.
    - SEX DIFFERENCES: the VMHvl circuit is functionally dimorphic
      (female-typical receptivity vs. male-typical aggression). The same
      subregion carries different functions by sex. Document factually;
      do not overclaim beyond what the literature establishes. Applies
      on the right identically.
    - The ventromedial hypothalamic obesity clinical fact (VMH lesions →
      hyperphagia + obesity) applies bilaterally; the right VMH lesion
      produces the same syndrome as the left. Reproduced in abbreviated
      form above; the full clinical description lives in ../left/ and is
      NOT duplicated here.
    - The subdivisions (VMHc, VMHvl, VMHdm, shell) are documented WITHIN
      this file, not as child nodes. Same convention as ../left/ and as
      the habenula's LHb/MHb and PVN's sub-populations. Do not create
      vmhc/, vmhvl/, vmhdm/, or shell/ as child nodes on the right
      either.
    - The VMH's aggression and female sexual behavior roles do NOT emit
      separate fragments. Same as ../left/.
    - No independent fragment: two constituent inputs to the feeding and
      autonomic/thermoregulatory aggregates. Same aggregation rules as
      ../left/.
    - The VMH is NOT the arcuate (first-order vs. integrated satiety);
      NOT the DMH (satiety/aggression/thermoregulation/sexual vs.
      circadian relay); NOT the AHN (thermogenic effector vs.
      parasympathetic thermoregulatory); NOT the PHN (thermogenic
      sympathetic vs. whole-body sympathetic). The four traps make these
      distinctions explicit on the right.
    - Midline targets (RVLM, PAG, NTS, SCN) are flagged with "verify" so
      Stage 4 does not force a hemisphere split on structures that are
      not hemisphere-split in the tree. Right arcuate, right DMH, right
      AHN, right PHN, right preoptic area, right MPN, right AVPV, right
      amygdala, right lateral horn, and right brown adipose sympathetic
      circuit are hemisphere-split and require right-side targets
      explicitly.
    - Vocabulary used above is defined in Stage 0 files; see ../left/
      § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/medial_area/
      ventromedial_nucleus/.
"""