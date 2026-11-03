"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.right.preoptic_area
Anatomical Role:
    The right lateral preoptic area (LPO). Right-hemisphere mirror of
    ../left/preoptic_area/. Same anatomical position (rostral pole of the
    third ventricle, adjacent to the diagonal band of Broca and medial
    forebrain bundle), same sleep-promoting circuitry (VLPO-adjacent),
    same thermoregulatory and osmoregulatory projections. See
    ../left/__init__.py for the full anatomical description.

    Reproduced critical warning (applies equally on the right):
    PREOPTIC NAMING COLLISION — this node is the LATERAL preoptic area,
    containing lateral_preoptic_nucleus/ (VLPO-adjacent sleep circuitry).
    It is distinct from medial_area/right/preoptic_area/ — the MEDIAL
    preoptic area, which contains medial_preoptic_nucleus/,
    median_preoptic_nucleus/, and inah_1–4 (GnRH-regulatory circuitry).
    These are anatomically and functionally distinct structures. Do not
    merge them. Do not move children across them.

Functional Mode:
    Same as ../left/. Sleep promotion, thermoregulation, and osmoregulatory
    projections, documented at the child leaf
    (./lateral_preoptic_nucleus/) and the parent lateral_area/right/.
    No documented functional asymmetry between left and right LPO.
    Do not fabricate one.

Hormonal Modulation:
    Same as ../left/ and ../../__init__.py. Sleep-promoting nuclei are
    modulated by adenosine (↑ with sleep pressure), GABA, galanin,
    prostaglandin D2, and circadian drive from the SCN. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (sleep pressure),
    temporal_sequence_learning (circadian sleep window), emotional_valence
    (stress-arousal context). No stored content writes. See
    ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No sub-container-level prompt fragment. The sleep/thermoregulatory
    fragment is emitted by the child leaf
    (./lateral_preoptic_nucleus/) and aggregated into the
    anterior-division state block. This file does not emit a fragment.

Children (one child — a delta of the left leaf):
    - lateral_preoptic_nucleus/   ★ Sleep-promoting sleep-active neurons
                                     (VLPO-adjacent); right hemisphere

Right-specific reciprocal connections to enforce in Stage 4:
    - lateral_preoptic_nucleus/ ↔
      medial_area/right/preoptic_area/medial_preoptic_nucleus/
      (adjacent preoptic circuits; keep distinct)
    - lateral_preoptic_nucleus/ ↔
      hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → VLPO; circadian sleep gating; SCN is midline-adjacent —
      verify)
    - lateral_preoptic_nucleus/ ↔
      hindbrain/.../tuberomammillary_nucleus (VLPO → TMN; inhibitory;
      sleep promotion; TMN is midline-adjacent — verify)
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed)

Notes:
    - Sub-container delta of ../left/. Short by design. Do not duplicate
      the child's functional or hormonal wiring.
    - The PREOPTIC NAMING COLLISION warning is reproduced above because
      it is a structural trap that applies on both hemispheres. A
      contributor entering the tree at right/preoptic_area/ would
      otherwise miss the parent lateral_area/ warning.
    - No sub-container-level fragment: sleep/thermoregulatory fragments
      are emitted by the child leaf. Same convention as
      ../left/preoptic_area/.
    - Midline targets (SCN, TMN) are flagged with "verify" so Stage 4
      does not force a hemisphere split on structures that are not
      hemisphere-split in the tree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/lateral_area/right/.
"""