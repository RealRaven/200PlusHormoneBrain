"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.preoptic_area
Anatomical Role:
    The right medial preoptic area (MPOA). Right-hemisphere mirror of
    ../left/preoptic_area/. Same anatomical position (along the third
    ventricle, medial to the lateral preoptic area), same two children
    (medial_preoptic_nucleus/ with inah_1–4/, and
    median_preoptic_nucleus/), same reproductive, maternal, and
    GnRH-regulatory roles. See ../left/__init__.py for the full
    anatomical description.

    Reproduced critical warnings (both apply equally on the right):
    - PREOPTIC NAMING COLLISION — this node is the MEDIAL preoptic area,
      containing medial_preoptic_nucleus/ (with inah_1–4/) and
      median_preoptic_nucleus/. It is distinct from
      lateral_area/right/preoptic_area/ — the LATERAL preoptic area,
      containing lateral_preoptic_nucleus/ (VLPO-adjacent sleep
      circuitry). Do not merge them. Do not move children across them.
    - MnPO DISAMBIGUATION — the "median preoptic nucleus" (MnPO)
      documented here is the medial preoptic median nucleus (GnRH
      regulation, osmoregulation, cardiovascular control). It is NOT
      the "MnPO" referenced in lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus/, where the same acronym is used for the
      ventrolateral sleep-active population of the LPO/VLPO complex.
      Two different structures share the acronym; distinguish by
      location. Do not merge.

Functional Mode:
    Same as ../left/. Maternal behavior, sexual behavior, GnRH
    regulation via medial_preoptic_nucleus/ (with the four INAH
    sub-nuclei); GnRH regulation, osmoregulation, and cardiovascular
    control via median_preoptic_nucleus/. No documented functional
    asymmetry between left and right MPOA for these roles. Do not
    fabricate one.

Hormonal Modulation:
    Same as ../left/. Estradiol (surge and maternal behavior),
    progesterone, prolactin (maternal behavior), testosterone (sexually
    dimorphic INAH volume), kisspeptin (GnRH regulation via PeN
    crosstalk). See ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (reproductive state), episodic
    (reproductive/maternal history), emotional_valence (stress
    suppression of reproductive behavior), temporal_sequence_learning
    (circadian timing of reproductive behavior). No stored content
    writes. See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No sub-container-level prompt fragment. The reproductive fragment
    is emitted by the child leaves (./medial_preoptic_nucleus/ and
    ./median_preoptic_nucleus/) and AGGREGATED with the right-side
    lateral-area PeN reproductive fragment
    (lateral_area/right/periventricular_preoptic_nucleus/) at the
    anterior-division level. See ../../../__init__.py § Model
    Integration for the mandatory aggregation rule. This file does not
    emit a fragment.

Children (two children — deltas of the left leaves):
    - medial_preoptic_nucleus/    ★ Delta of ../left/preoptic_area/
                                    medial_preoptic_nucleus/. Right
                                    hemisphere.
        ├── inah_1/               Deltas of the left INAH nuclei;
        ├── inah_2/               short leaves (Tier 2 organ-flavored
        ├── inah_3/               shape; primary role is sexually
        └── inah_4/               dimorphic volume).
    - median_preoptic_nucleus/    ★ Delta of ../left/preoptic_area/
                                    median_preoptic_nucleus/. Right
                                    hemisphere.

Right-specific reciprocal connections to enforce in Stage 4 (do not
duplicate the left-side edges in ../left/):
    - medial_preoptic_nucleus/ ↔ lateral_area/right/
      periventricular_preoptic_nucleus (GnRH-regulatory partners;
      continuity edge, not duplicate-structure warning; right-side).
    - medial_preoptic_nucleus/ ↔ telencephalon/cerebral_hemispheres/
      right/subcortical/medial_temporal_lobe/amygdala (reproductive/
      social context; stria terminalis and ventral amygdalofugal
      pathway; right-side).
    - medial_preoptic_nucleus/ ↔ midbrain/tegmentum/periaqueductal_gray
      (maternal/sexual behavior motor patterns; PAG is midline-adjacent
      — verify).
    - median_preoptic_nucleus/ ↔ lamina_terminalis/
      vascular_organ_of_lamina_terminalis and hypothalamus/subfornical_organ
      (osmoregulatory/cardiovascular control; both are midline).
    - median_preoptic_nucleus/ ↔ brainstem cardiovascular centers
      (NTS, RVLM; both are midline-adjacent — verify).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Sub-container delta of ../left/. Short by design. Do not duplicate
      the children's functional or hormonal wiring.
    - Both structural traps (preoptic collision and MnPO disambiguation)
      are reproduced above because they are structural traps that apply
      on both hemispheres. A contributor entering at
      right/preoptic_area/ would otherwise miss them.
    - The four INAH nuclei (inah_1–4) are very small; the right INAH
      deltas should be correspondingly short (Tier 2 organ-flavored).
    - No sub-container-level fragment: the reproductive fragment is
      emitted by the child leaves and aggregated at the anterior-division
      level. Same convention as ../left/preoptic_area/.
    - Midline targets (PAG, OVLT, SFO, NTS, RVLM) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/right/.
"""