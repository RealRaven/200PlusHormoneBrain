"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.preoptic_area.medial_preoptic_nucleus
Anatomical Role:
    Right hemisphere of the medial preoptic nucleus (MPN). Same
    reproductive-behavior hub documented in ../left/ (maternal behavior,
    female and male sexual behavior, parental behavior, GnRH-regulation
    contribution), mirrored to the right hemisphere, and containing the
    same four interstitial nuclei of the anterior hypothalamus (INAH 1–4)
    as components:
        - inah_1/   Interstitial nucleus of the anterior hypothalamus 1.
        - inah_2/   Interstitial nucleus of the anterior hypothalamus 2.
        - inah_3/   Interstitial nucleus of the anterior hypothalamus 3
                    (human homologue of the rodent SDN-POA).
        - inah_4/   Interstitial nucleus of the anterior hypothalamus 4.

    See ../left/__init__.py for the full anatomical description, the
    three behavior domains, and the sex-difference framing. The four INAH
    are components of the MPN, not separate anatomical structures; do not
    flatten them into siblings of the MPN, and do not merge them into the
    MPN's main file.

    Reproduced critical distinctions (apply equally on the right):
    - DISTINCT FROM PeN: the periventricular preoptic nucleus
      (lateral_area/right/periventricular_preoptic_nucleus/) is a
      separate GnRH-regulatory nucleus. Continuity edge, not
      duplicate-structure warning.
    - DISTINCT FROM MnPO: median_preoptic_nucleus/ (the right-side
      sibling under ../) is a separate preoptic node (GnRH regulation,
      osmoregulation, cardiovascular control). Do not merge.
    - PREOPTIC COLLISION: this node is inside the MEDIAL preoptic area,
      distinct from lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus/ (VLPO-adjacent sleep nucleus). Do not
      merge.
    - MnPO DISAMBIGUATION: the "MnPO" acronym refers to the medial
      sibling median_preoptic_nucleus/, not to the ventrolateral
      sleep-active population of the LPO. Do not confuse the two.

Functional Mode:
    Same as ../left/. Maternal behavior, female sexual behavior, male
    sexual behavior, parental behavior, GnRH-regulation contribution, and
    a minor thermoregulatory/cardiovascular contribution. No documented
    functional asymmetry between left and right MPN for these roles. Do
    not fabricate one.

Hormonal Modulation:
    Same as ../left/. Estradiol ↑ MPN activity (maternal, sexual, GnRH
    surge contribution); progesterone withdrawal ↑ maternal onset;
    prolactin ↑ maternal onset; testosterone (aromatized to estradiol)
    ↑ male sexual behavior; oxytocin ↑ maternal behavior; kisspeptin
    modulates GnRH-regulatory output; CRH/cortisol ↓ MPN reproductive
    behavior. See ../left/__init__.py § Hormonal Modulation for the full
    list and directions.

Memory Interfaces:
    Same as ../left/. Reads short_term (reproductive-hormonal state,
    social context), episodic (reproductive/maternal history),
    emotional_valence (stress suppression of reproductive behavior),
    reinforcement_value_based_learning (reproductive/parental outcomes),
    temporal_sequence_learning (circadian timing of reproductive
    behavior). Writes reinforcement_value_based_learning indirectly
    (reproductive and parental outcomes feed back into value learning).
    See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The reproductive/parental fragment
    emitted by ../left/ represents the bilateral MPN and is aggregated
    with the right-side PeN
    (lateral_area/right/periventricular_preoptic_nucleus/) and the
    right-side MnPO (../median_preoptic_nucleus/) contributions at the
    anterior-division level. Emitting a separate right-side fragment
    would double-count the reproductive signal. See ../left/__init__.py
    § Model Integration (AGGREGATION RULE).

Children (four INAH — delta mirrors of the left INAH leaves):
    - inah_1/   Delta of ../../../../left/preoptic_area/
                 medial_preoptic_nucleus/inah_1/. Right hemisphere.
    - inah_2/   Delta of ../../../../left/preoptic_area/
                 medial_preoptic_nucleus/inah_2/. Right hemisphere.
    - inah_3/   Delta of ../../../../left/preoptic_area/
                 medial_preoptic_nucleus/inah_3/. Right hemisphere.
                 Slightly longer than the other INAH deltas because
                 INAH-3 carries the SDN-POA homologue role; but still
                 Tier 2 organ-flavored.
    - inah_4/   Delta of ../../../../left/preoptic_area/
                 medial_preoptic_nucleus/inah_4/. Right hemisphere.

    The INAH right deltas are short Tier 2 organ-flavored shapes (same as
    their left counterparts). Do not force the full Tier 1 template onto
    them.

Right-specific reciprocal connections to enforce in Stage 4:
    - ↔ lateral_area/right/periventricular_preoptic_nucleus (PeN;
      GnRH-regulatory partners; continuity edge, not
      duplicate-structure warning; right-side).
    - ↔ lateral_area/right/preoptic_area/lateral_preoptic_nucleus (LPO;
      adjacent preoptic sleep circuitry; reciprocal stress-arousal
      cross-talk; keep distinct; right-side).
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area/
      median_preoptic_nucleus (MnPO; adjacent preoptic nodes; distinct
      functions; right-side).
    - → midbrain/tegmentum/periaqueductal_gray (maternal/sexual
      behavior motor patterns; PAG is midline-adjacent — verify).
    - → midbrain/tegmentum/ventral_tegmental_area (reproductive
      motivation and reward; VTA is midline-adjacent — verify).
    - ↔ telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/amygdala (reproductive and social context;
      stria terminalis and ventral amygdalofugal pathway; right-side).
    - ↔ telencephalon/.../subcortical/extended_amygdala/
      bed_nucleus_of_stria_terminalis (BNST; reproductive and stress
      context integration; BNST is midline-adjacent — verify).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → MPN; circadian timing of reproductive behavior; SCN is
      midline-adjacent — verify).
    - ← hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (PVN CRH; stress suppression of reproductive behavior; right-side).
    - ← hypothalamus/tuberal/medial_area/right/arcuate_nucleus
      (kisspeptin KNDy input; GnRH regulation; right-side).
    - ← brainstem/.../locus_coeruleus (noradrenergic input; arousal
      context for sexual behavior; LC is midline-adjacent — verify).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - Unusual for a leaf: this file has four INAH child deltas. They are
      components of the MPN (not separate structures), so they follow
      the delta pattern rather than being full leaves. Do not treat them
      as equivalent to the MPN delta in scope.
    - NO structural-identity trap: MPN is a single nucleus on both
      sides; the INAH are components, not a split-structure issue. The
      "Reproduced critical distinctions" block above is about
      distinguishing the MPN from *other* nodes (PeN, MnPO, LPO), not
      about a same-structure split. Do not invent a structural-identity
      warning.
    - Continuity edges (not duplicate-structure warnings) reproduced
      from ../left/ because they apply on the right:
        * MPN ↔ right PeN (GnRH-regulatory partners).
        * MPN ↔ right MnPO (adjacent preoptic nodes).
      The audit should not flag these as duplicates.
    - The preoptic collision and MnPO disambiguation are reproduced in
      abbreviated form above. The full text is in ../left/__init__.py
      and in the parent preoptic_area/right/__init__.py; the abbreviated
      version here is sufficient to prevent the two traps from
      re-emerging at the right MPN.
    - Sex differences: MPN and INAH volume and receptor density are
      sex-dependent on both hemispheres. Document factually and without
      over-claiming functional consequences, same as ../left/.
    - The INAH right deltas should be correspondingly short (Tier 2
      organ-flavored). Their primary content is the right-side volume
      and the reciprocal edge back to the right MPN.
    - Midline targets (PAG, VTA, BNST, SCN, LC) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/right/
      preoptic_area/.
"""