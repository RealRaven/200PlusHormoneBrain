"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.preoptic_area.median_preoptic_nucleus
Anatomical Role:
    Right hemisphere of the median preoptic nucleus (MnPO). Same
    periventricular integrator of the medial preoptic area documented in
    ../left/ (positioned along the lamina terminalis, integrating OVLT
    and SFO signals and modulating SON, PVN, GnRH neurons, and brainstem
    cardiovascular centers), mirrored to the right hemisphere. See
    ../left/__init__.py for the full anatomical description and the
    "integrator, not output nucleus" framing.

    Reproduced critical distinctions (all apply equally on the right):
    - MnPO ACRONYM TRAP (the most important content in this file): the
      "median preoptic nucleus" documented HERE is the osmoregulatory/
      GnRH/cardiovascular population of the medial preoptic area. The
      "MnPO" referenced in lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus/ is the ventrolateral sleep-active
      population of the LPO/VLPO complex. Two different structures
      share the acronym; the tree distinguishes them by location. Do
      not merge.
    - DISTINCT FROM MPN (sibling): the medial preoptic nucleus (MPN,
      ../medial_preoptic_nucleus/) is the maternal/sexual-behavior hub
      and the parent of the four INAH nuclei. THIS file's MnPO is the
      osmoregulatory/GnRH/cardiovascular integrator. Siblings, not the
      same structure; they interact but are distinct nodes.
    - PREOPTIC COLLISION: this node is inside the MEDIAL preoptic area,
      distinct from lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus/. Do not merge.

Functional Mode:
    Same as ../left/. Osmoregulation and thirst (primary function);
    cardiovascular control; GnRH regulation (permissive/modulatory);
    thermoregulation (minor, shared). The MnPO is an INTEGRATOR, not a
    primary output nucleus: its state flows through the nuclei it
    modulates (SON, PVN, GnRH neurons, brainstem cardiovascular
    centers). No documented functional asymmetry between left and right
    MnPO. Do not fabricate one. See ../left/__init__.py § Functional
    Mode.

Hormonal Modulation:
    Same as ../left/. Angiotensin II ↑ MnPO activity (via SFO);
    plasma osmolarity ↑ MnPO activity (via OVLT); ANP ↓ MnPO activity;
    estradiol ↑ MnPO GnRH-regulatory output; kisspeptin (from arcuate
    KNDy and PeN) ↑ GnRH-regulatory output; monoamines and GABA/
    glutamate modulate. See ../left/__init__.py § Hormonal Modulation
    for the full list and directions.

Memory Interfaces:
    Same as ../left/. Reads short_term (osmolarity, volume,
    reproductive-hormonal state), episodic (dehydration/volume-depletion
    history, reproductive-cycle history), emotional_valence (stress
    context), temporal_sequence_learning (circadian timing). Writes no
    stored content directly. See ../left/__init__.py § Memory
    Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragments. The MnPO is an INTEGRATOR; its
    model contribution is through the nuclei it modulates. The three
    aggregation points documented in ../left/ apply identically on the
    right:
        (1) Reproductive: emits a CONSTITUENT INPUT to the
            anterior-division reproductive fragment, aggregated with the
            right MPN (../medial_preoptic_nucleus/) and the right PeN
            (lateral_area/right/periventricular_preoptic_nucleus/)
            contributions. Do not emit an independent reproductive
            fragment from the right MnPO.
        (2) Fluid/osmotic: UPSTREAM MODULATION of the right SON and
            PVN. The anterior-division fluid/osmotic fragment (emitted
            by the SON/PVN aggregate) carries the state; the right MnPO
            does not emit a separate fluid fragment. Do not
            double-count.
        (3) Cardiovascular/autonomic: UPSTREAM MODULATION of the right
            PVN and the right AHN. The anterior-division autonomic/
            thermoregulatory fragment aggregates the PVN + AHN +
            preoptic contributions; the right MnPO does not emit a
            separate autonomic fragment. Do not double-count.
    - IMPLEMENTER NOTE (mandatory, repeated because the rule is
      unusual): zero independent fragments, three aggregation points,
      all on the right. Do not add right-side MnPO fragments.
    - No multimodal input is consumed here; the MnPO's contribution is
      through its downstream targets' text-only fragments.

Right-specific reciprocal connections to enforce in Stage 4 (organized
by functional domain; do not duplicate the left-side edges in ../left/):

    Osmoregulatory:
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmotic input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).
    - → hypothalamus/anterior/medial_area/right/supraoptic_nucleus
      (modulation of vasopressin/oxytocin release; right medial SON;
      right-side).
    - → hypothalamus/anterior/lateral_area/right/
      part_of_supraoptic_nucleus (modulation of vasopressin release;
      right lateral SON portion; right-side).
    - → hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (modulation of vasopressin release and autonomic outflow;
      right-side).

    Cardiovascular:
    - → hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
      (NTS; feedback; NTS is midline-adjacent — verify).
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic modulation; RVLM
      is midline-adjacent — verify).
    - ↔ hypothalamus/anterior/medial_area/right/
      anterior_hypothalamic_nucleus (cardiovascular co-regulation;
      right-side).

    Reproductive (permissive/modulatory):
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area/
      medial_preoptic_nucleus (MPN; sibling; shared GnRH regulation;
      continuity edge, not duplicate-structure warning; right-side).
    - ↔ lateral_area/right/periventricular_preoptic_nucleus (PeN;
      shared GnRH regulation; continuity edge, not duplicate-structure
      warning; right-side).
    - ← hypothalamus/tuberal/medial_area/right/arcuate_nucleus
      (kisspeptin KNDy input; permissive on GnRH regulation;
      right-side).

    Cross-cutting:
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN; circadian gating; SCN is midline-adjacent — verify).
    - ↔ telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/amygdala (emotional/stress context;
      right-side).
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area (sibling
      preoptic sub-container; adjacent preoptic circuits; keep
      distinct).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - The MnPO ACRONYM TRAP is the most important content in this delta,
      same as in ../left/. Reproduced in full above because a
      contributor entering at the right/ level must not confuse the
      right MnPO (osmoregulatory/GnRH/cardiovascular) with the right
      LPO sleep-active "MnPO" (in lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus/). Two different structures; do not
      merge.
    - The MPN sibling distinction and the preoptic collision are also
      reproduced. Three traps total, all present on the right.
    - ZERO INDEPENDENT FRAGMENTS: the MnPO does not emit any of its own
      fragments on the right, same as on the left. The three
      aggregation points are listed above; do not add right-side MnPO
      fragments. This is the unusual pattern in the tree (integrator
      leaf, indirect model contribution).
    - Continuity edges (not duplicate-structure warnings) reproduced
      from ../left/ because they apply on the right:
        * right MnPO ↔ right MPN (siblings; distinct nodes).
        * right MnPO ↔ right PeN (both GnRH-regulatory; distinct nodes).
      The audit should not flag these as duplicates.
    - Midline targets (OVLT, SFO, NTS, RVLM, SCN) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree. Right SON
      (medial and lateral), right PVN, right AHN, right MPN, right PeN,
      right arcuate, and right amygdala are hemisphere-split and
      therefore require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/right/
      preoptic_area/.
"""