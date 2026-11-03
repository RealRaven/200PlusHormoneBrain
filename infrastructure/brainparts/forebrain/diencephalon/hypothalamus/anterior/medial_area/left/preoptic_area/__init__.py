"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.preoptic_area
Anatomical Role:
    The left medial preoptic area (MPOA). A sub-region of the preoptic
    area within the left anterior hypothalamus, positioned along the
    third ventricle (periventricular zone) and medial to the lateral
    preoptic area. It is the principal hypothalamic region for
    reproductive behavior, maternal behavior, and GnRH regulation,
    containing:
        - medial_preoptic_nucleus/ (MPN): the medial preoptic nucleus,
          a sexually dimorphic nucleus central to maternal behavior,
          sexual behavior, and GnRH regulation. Contains four INAH
          sub-nuclei (inah_1/ through inah_4/), the interstitial nuclei
          of the anterior hypothalamus, which are the sexually
          dimorphic components.
        - median_preoptic_nucleus/ (MnPO, medial preoptic variant):
          the median preoptic nucleus of the medial preoptic area,
          contributing to GnRH regulation and to osmoregulatory and
          cardiovascular control (reciprocal with the SFO and OVLT).

    This is the MEDIAL preoptic area. It is distinct from the LATERAL
    preoptic area documented under
    lateral_area/left/preoptic_area/ (which contains
    lateral_preoptic_nucleus/, the VLPO-adjacent sleep-promoting
    nucleus).

PREOPTIC NAMING COLLISION (critical — this is the MEDIAL half of the
collision; reproduced here because a contributor entering at this level
must see it):
    This node is the MEDIAL preoptic area, containing
    medial_preoptic_nucleus/ (with inah_1–4/) and
    median_preoptic_nucleus/. It is distinct from
    lateral_area/left/preoptic_area/ — the LATERAL preoptic area,
    containing lateral_preoptic_nucleus/ (VLPO-adjacent sleep circuitry).
    Do not merge them. Do not move children across them. The two
    preoptic areas share thermoregulatory and adjacent-circuit functions
    but are anatomically and functionally distinct nodes.

MnPO DISAMBIGUATION (critical — reproduced from the lateral side):
    The "median preoptic nucleus" (MnPO) documented HERE is the medial
    preoptic median nucleus, involved in GnRH regulation, osmoregulation,
    and cardiovascular control. It is NOT the "MnPO" referenced in the
    lateral side's lateral_preoptic_nucleus/ file, where the same
    acronym is used for the ventrolateral sleep-active population that
    is part of the LPO/VLPO complex. Two different structures share the
    acronym; the tree distinguishes them by location. Do not merge.

Functional Mode:
    The functional content is documented at the child leaves:
        - medial_preoptic_nucleus/__init__.py: maternal behavior,
          sexual behavior, GnRH regulation, the INAH sub-nuclei and
          their sexually dimorphic role.
        - median_preoptic_nucleus/__init__.py: GnRH regulation,
          osmoregulatory/cardiovascular control (reciprocal with
          SFO/OVLT).
    This sub-container does not restate them. Full description: see
    ../../../__init__.py (medial_area parent) and the two child leaves.

Hormonal Modulation:
    Same as parent medial_area/left/. See ../../../__init__.py.
    The medial preoptic area's principal hormonal modulators are
    estradiol (surge and maternal behavior), progesterone, prolactin
    (maternal behavior), testosterone (sexually dimorphic INAH volume),
    and kisspeptin (GnRH regulation, via PeN crosstalk). Details in the
    child leaves.

Memory Interfaces:
    Same as parent. See ../../../__init__.py. The medial preoptic area
    reads short_term (reproductive state), episodic (reproductive/
    maternal history), emotional_valence (stress suppression of
    reproductive behavior), and temporal_sequence_learning (circadian
    timing of reproductive behavior). No stored content writes.

Model Integration (Gemma-4-E2B):
    No sub-container-level prompt fragment. The reproductive fragment
    is emitted by the child leaves (medial_preoptic_nucleus/ and
    median_preoptic_nucleus/) and AGGREGATED with the lateral-area PeN
    reproductive fragment at the anterior-division level. See
    ../../../__init__.py § Model Integration for the mandatory
    aggregation rule (reproductive fragment aggregated with
    lateral_area/*/periventricular_preoptic_nucleus). This file does not
    emit a fragment.

Children (two children — both full leaves, not deltas):
    - medial_preoptic_nucleus/    ★ Maternal behavior; sexual behavior;
                                    GnRH regulation; sexually dimorphic
                                    (parent of four INAH sub-nuclei).
        ├── inah_1/               Very small INAH nuclei; document as
        ├── inah_2/               short leaves (Tier 2 organ-flavored
        ├── inah_3/               shape; primary role is sexually
        └── inah_4/               dimorphic volume; minimal endocrine
                                    and memory content).
    - median_preoptic_nucleus/    ★ GnRH regulation; osmoregulatory and
                                    cardiovascular control; reciprocal
                                    with SFO/OVLT.

Notes:
    - Sub-container file. Short by design. Do not duplicate the
      children's functional or hormonal wiring.
    - Both structural traps (preoptic collision and MnPO disambiguation)
      are reproduced above because they are structural traps that apply
      at this level. A contributor entering at left/preoptic_area/ would
      otherwise miss the parent medial_area/ warning (collision) or the
      lateral-side warning (MnPO).
    - The four INAH nuclei (inah_1–4) are very small. Document them as
      Tier 2 organ-flavored leaves (short; primary role is sexually
      dimorphic volume and hormonal modulation; minimal endocrine and
      memory content). They do NOT need the full Tier 1 template.
    - The medial and lateral preoptic areas are anatomical mirrors with
      no documented functional asymmetry for the roles documented here.
      The right/ sub-container is a delta of this file (both warnings
      reproduced, right edges listed, no functional content duplicated).
    - DISTINCTION FROM PeN: the periventricular preoptic nucleus
      (lateral_area/*/periventricular_preoptic_nucleus/) is a distinct
      GnRH-regulatory nucleus in the lateral area. The medial preoptic
      area's GnRH-regulatory circuitry (MPN, INAH, MnPO) interacts with
      PeN but is anatomically separate. The reciprocal edge is a
      continuity edge, not a duplicate-structure warning.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, progesterone,
      testosterone), 06_* (social, prolactin, oxytocin), 07_* (fluid,
      angiotensin II — MnPO osmoregulatory role); memory/stores/;
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * medial_preoptic_nucleus/ ↔
          lateral_area/left/periventricular_preoptic_nucleus (GnRH-
          regulatory partners; continuity edge, not duplicate-structure
          warning)
        * medial_preoptic_nucleus/ ↔ amygdala (reproductive/social
          context; stria terminalis and ventral amygdalofugal pathway)
        * medial_preoptic_nucleus/ ↔ brainstem periaqueductal gray
          (maternal/sexual behavior motor patterns)
        * median_preoptic_nucleus/ ↔ lamina_terminalis/OVLT and
          subfornical_organ (osmoregulatory/cardiovascular control;
          reciprocal with circumventricular organs)
        * median_preoptic_nucleus/ ↔ brainstem cardiovascular centers
          (NTS, RVLM; cardiovascular control)
    - Connects upward to hypothalamus/anterior/medial_area/left/.
"""