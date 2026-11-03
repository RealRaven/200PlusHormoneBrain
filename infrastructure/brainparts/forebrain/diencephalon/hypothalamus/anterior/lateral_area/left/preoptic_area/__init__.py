"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.left.preoptic_area
Anatomical Role:
    The left lateral preoptic area (LPO). A sub-region of the preoptic
    area within the left anterior hypothalamus, positioned at the rostral
    pole of the third ventricle, adjacent to the diagonal band of Broca
    and the medial forebrain bundle. Contains sleep-promoting circuitry
    (including the ventrolateral preoptic nucleus, VLPO, which sits at
    the lateral edge of the LPO), thermoregulatory neurons, and
    osmoregulatory projections. Functionally, the LPO is a
    sleep-promoting region: lesions produce insomnia, and activation
    promotes sleep.

    PREOPTIC NAMING COLLISION (critical — applies here and must be
    reproduced wherever the preoptic area is referenced):
    This node is the LATERAL preoptic area, containing
    lateral_preoptic_nucleus/ (VLPO-adjacent sleep circuitry). It is
    distinct from:
        - medial_area/left/preoptic_area/ — the MEDIAL preoptic area,
          which contains medial_preoptic_nucleus/,
          median_preoptic_nucleus/, and inah_1–4 (GnRH-regulatory
          circuitry).
    These are anatomically and functionally distinct structures. Do not
    merge them. Do not move children across them.

Functional Mode:
    Sleep promotion, thermoregulation, and osmoregulatory projections
    are documented at the child leaf (lateral_preoptic_nucleus/) and the
    parent lateral_area/ (broader preoptic context). This sub-container
    does not restate them.

    Full description: see ../__init__.py (lateral_area parent) and
    ./lateral_preoptic_nucleus/__init__.py (child leaf).

Hormonal Modulation:
    Same as parent lateral_area/left/. See ../../__init__.py.
    The sleep-promoting nuclei (VLPO and adjacent LPO neurons) are
    modulated by adenosine (↑ with sleep pressure), GABA, galanin,
    prostaglandin D2, and circadian drive from the SCN. Details in the
    child leaf.

Memory Interfaces:
    Same as parent. See ../../__init__.py. The LPO reads short_term
    (sleep pressure), temporal_sequence_learning (circadian sleep
    window), and emotional_valence (stress-arousal context). No stored
    content writes.

Model Integration (Gemma-4-E2B):
    No sub-container-level prompt fragment. The sleep/thermoregulatory
    fragment is emitted by the child leaf
    (lateral_preoptic_nucleus/__init__.py) and aggregated into the
    anterior-division state block. This file does not emit a fragment.

Children (one child — a full leaf, not a delta):
    - lateral_preoptic_nucleus/   ★ Sleep-promoting sleep-active neurons
                                     (VLPO-adjacent); thermoregulation

Notes:
    - Sub-container file. Short by design. Do not duplicate the child's
      functional or hormonal wiring.
    - The PREOPTIC NAMING COLLISION warning is the most important content
      in this file. It is reproduced here (and in
      medial_area/left/preoptic_area/) because a contributor entering the
      tree at this level would not otherwise see the parent lateral_area/
      warning. The warning applies at every level where the preoptic area
      is referenced.
    - The left/ and right/ preoptic areas are anatomical mirrors with no
      documented functional asymmetry. The right/ sub-container is a
      delta of this file (preoptic collision warning reproduced, right
      edges listed, no functional content duplicated).
    - The LPO contains, but is not identical to, the VLPO. The VLPO is
      one nucleus within the broader preoptic area; the child leaf
      (lateral_preoptic_nucleus/) documents the sleep-active circuitry
      that is VLPO-adjacent.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (GABA, galanin, adenosine), 10_*
      (circadian, SCN), 07_* (fluid); memory/stores/; gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * preoptic_area/lateral_preoptic_nucleus/left ↔
          medial_area/left/preoptic_area/medial_preoptic_nucleus/
          (adjacent preoptic circuits; keep distinct)
        * preoptic_area/lateral_preoptic_nucleus/left ↔
          hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
          (SCN → VLPO; circadian sleep gating)
        * preoptic_area/lateral_preoptic_nucleus/left ↔
          hindbrain/.../tuberomammillary_nucleus (VLPO → TMN; inhibitory;
          sleep promotion)
    - Connects upward to hypothalamus/anterior/lateral_area/left/.
"""