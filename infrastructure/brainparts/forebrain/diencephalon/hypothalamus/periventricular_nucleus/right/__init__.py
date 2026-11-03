"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.periventricular_nucleus.right
Anatomical Role:
    Right hemisphere of the periventricular zone. Same four cell groups
    documented in ../left/, mirrored to the right hemisphere, documented
    WITHIN this file (not as further child nodes):
        - Anterior periventricular group: scattered kisspeptin
          neurons, scattered sleep-promoting neurons, scattered
          GnRH-adjacent interneurons — all SUPPLEMENTARY to the
          primary sources elsewhere.
        - Tuberal periventricular group: A14 dopaminergic cell group
          (supplementary; NOT the primary prolactin inhibitor);
          scattered somatostatin neurons (supplementary to PVN's
          somatostatin).
        - Posterior periventricular group: poorly characterized;
          documented factually.
        - Other periventricular cell groups not classified under a
          specific division's medial or lateral area.
    See ../left/__init__.py for the full anatomical description, the
    four-cell-group framing, and the honest documentation of the
    posterior periventricular group.

    Reproduced critical traps (all apply equally on the right):
    - PeN (periventricular preoptic nucleus): documented under
      lateral_area/right/periventricular_preoptic_nucleus/. THIS file's
      anterior periventricular kisspeptin is SCATTERED and SUPPLEMENTARY
      to the PeN. Do not merge; do not claim the periventricular zone's
      kisspeptin is "the" kisspeptin nucleus.
    - PVN (paraventricular nucleus): documented under
      medial_area/right/paraventricular_nucleus/. THIS file's tuberal
      somatostatin is SUPPLEMENTARY to the PVN's somatostatin. Do not
      merge; do not import PVN's five hormones into this file.
    - Arcuate nucleus (TIDA dopamine): documented under
      hypothalamus/tuberal/medial_area/right/arcuate_nucleus/ (when
      drafted). The arcuate's TIDA neurons are the PRIMARY prolactin
      inhibitor. THIS file's A14 dopaminergic group is a DIFFERENT
      tuberal dopaminergic population; its function is less established
      and it is NOT the primary prolactin inhibitor. Do not conflate.

    Reproduced SUPPLEMENTARY-NOT-PRIMARY discipline (applies on the
    right, same as on the left): every cell group in this file
    supplements a primary source documented elsewhere (PeN, AVPV, PVN,
    arcuate, LPO). The file is a catalogue of supplements, not a hub.

Functional Mode:
    Same as ../left/, one function per cell group, supplementary
    framing throughout:
    - A14 dopaminergic (tuberal): supplementary dopaminergic portal
      contribution; NOT the primary prolactin inhibitor. Function less
      established than arcuate TIDA.
    - Anterior periventricular kisspeptin: scattered, supplementary to
      the PeN and AVPV.
    - Anterior periventricular sleep-promoting: scattered, supplementary
      to the LPO/VLPO.
    - Tuberal somatostatin: scattered, supplementary to the PVN's
      somatostatin.
    - Posterior periventricular: poorly characterized; document
      factually without overclaiming.
    No documented functional asymmetry between left and right
    periventricular zone. Do not fabricate one. See ../left/__init__.py
    § Functional Mode.

Hormonal Modulation:
    Same as ../left/. A14: dopamine output, estradiol and prolactin
    feedback. Anterior kisspeptin: estradiol modulatory, kisspeptin
    intrinsic, SCN gating. Anterior sleep: adenosine, GABA, galanin,
    SCN. Tuberal somatostatin: thyroid hormones and IGF-1 feedback.
    Posterior: not established; do not list. See ../left/__init__.py
    § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. A14: short_term (reproductive-hormonal),
    episodic (cycle history). Anterior kisspeptin: short_term,
    temporal_sequence_learning. Anterior sleep: short_term (sleep
    pressure), temporal_sequence_learning. Tuberal somatostatin:
    short_term (metabolic), episodic (growth-axis). Posterior: not
    established. No stored content writes. See ../left/__init__.py
    § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The four contributions aggregate
    into the appropriate division-level aggregates, identically on the
    right (mandatory AGGREGATION RULES):
        (1) A14 dopaminergic → prolactin-adjacent aggregate (currently
            carried by the arcuate's fragment when drafted; the A14
            contribution is supplementary).
        (2) Anterior periventricular kisspeptin → right reproductive
            aggregate (aggregated with right PeN + right MPN + right
            MnPO + right AVPV).
        (3) Anterior periventricular sleep-promoting → right sleep
            aggregate (aggregated with right LPO).
        (4) Tuberal somatostatin → right growth aggregate (aggregated
            with right PVN).
    SUPPLEMENTARY discipline: do not emit right-side periventricular
    fragments directly. Aggregate at the appropriate division level
    before injection. See ../left/__init__.py § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4
(organized by cell group; do not duplicate the left-side edges in
../left/):

    A14 dopaminergic (tuberal):
    - ↔ hypothalamus/tuberal/medial_area/right/arcuate_nucleus
      (adjacent tuberal dopaminergic populations; different functions;
      arcuate TIDA is primary, A14 is supplementary; document as
      supplementation, NOT duplicate; right-side).
    - → hypothalamus/median_eminence (supplementary dopaminergic portal
      contribution).

    Anterior periventricular kisspeptin:
    - ↔ lateral_area/right/periventricular_preoptic_nucleus (PeN;
      adjacent periventricular kisspeptin populations; PeN is dense
      and primary, periventricular is scattered and supplementary;
      document as supplementation, NOT duplicate; right-side).
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area/
      median_preoptic_nucleus (MnPO; periventricular GnRH-regulatory
      neighbors; right-side).
    - ↔ other_preoptic_nuclei/right (AVPV; adjacent kisspeptin
      populations; supplementary periventricular contribution;
      right-side).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → periventricular kisspeptin; circadian gating; SCN is
      midline-adjacent — verify).

    Anterior periventricular sleep-promoting:
    - ↔ lateral_area/right/preoptic_area/lateral_preoptic_nucleus
      (LPO; adjacent sleep circuitry; LPO is primary, periventricular
      is supplementary; document as supplementation, NOT duplicate;
      right-side).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → periventricular sleep neurons; circadian sleep gating;
      SCN is midline-adjacent — verify).

    Tuberal somatostatin:
    - ↔ hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (PVN; somatostatin co-contribution; PVN is primary, periventricular
      is supplementary; document as supplementation, NOT duplicate;
      right-side).
    - → hypothalamus/median_eminence (supplementary somatostatin portal
      contribution).

    Cross-cutting:
    - ↔ hypothalamus/median_eminence (anatomically adjacent; the portal
      pathway is shared; supplementary contributions feed it).
    - ↔ hypothalamus/pituitary_stalk (periventricular contributions
      travel through the stalk to the anterior pituitary).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - All three naming traps (PeN, PVN, arcuate-TIDA-vs-A14) are
      reproduced above because they are structural/naming traps that
      apply on both hemispheres. The full content is referenced.
    - SUPPLEMENTARY-NOT-PRIMARY discipline is reproduced above: every
      cell group on the right supplements a primary source documented
      elsewhere. Do not draft the right periventricular zone as a hub.
    - No independent fragment: all four contributions aggregate at the
      appropriate division level. Same AGGREGATION RULES as ../left/.
    - Do not create A14_group/, anterior_periventricular_kisspeptin/,
      sleep_promoting_periventricular/, etc. as child nodes on the
      right either. Same convention as ../left/.
    - The posterior periventricular group is poorly characterized.
      Same honest stance as ../left/: document factually, do not invent
      functional roles.
    - Midline targets (SCN, median eminence) are flagged with "verify"
      so Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right PeN, right MPN, right
      MnPO, right AVPV, right arcuate, right LPO, right PVN, and right
      preoptic sub-containers are hemisphere-split and require
      right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/periventricular_nucleus/.
"""