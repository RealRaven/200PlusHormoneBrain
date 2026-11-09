"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.left
Anatomical Role:
    Left hemisphere of the anterior lateral area of the hypothalamus.
    Contains four nuclei, all in the left hemisphere. See
    ../../__init__.py (the lateral_area container) for the full
    anatomical description of each nucleus and for the important
    distinction from the lateral hypothalamic area (LHA). This file is
    the hemisphere-specific container; it does not re-describe the
    nuclei.

Functional Mode:
    Same as parent lateral_area/. See ../../__init__.py for the full
    functional description of each nucleus (orexin/MCH arousal, vasopressin
    osmoregulation, GnRH pulse regulation, sleep promotion).
    No documented functional asymmetry exists between the left and right
    anterior lateral area for these four nuclei. Do not fabricate one.

Hormonal Modulation:
    Same as parent. See ../../__init__.py.

Memory Interfaces:
    Same as parent. See ../../__init__.py.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. The three fragments
    (arousal/feeding, osmotic, sleep/GnRH) are emitted by the
    lateral_area/ container and by the four leaf files, not by this
    container. See ../../__init__.py § Model Integration.

Children (left-hemisphere nuclei — each is a full leaf, not a delta):
    - anterior_part_of_lateral_nucleus/   ★ Orexin/MCH arousal and
                                             feeding drive; reward
    - part_of_supraoptic_nucleus/         ★ Magnocellular vasopressin/
                                             oxytocin; osmoregulation
    - periventricular_preoptic_nucleus/   ★ GnRH pulse regulation;
                                             sleep-wake gating
    - preoptic_area/                      ★ Sub-container for
        └── lateral_preoptic_nucleus/       sleep-promoting circuitry

Notes:
    - Left-side container. Not a delta of the parent — it is the
      authoritative left-hemisphere container. right/ is a delta of
      this file (habenular_nuclei/right/ convention).
    - PREOPTIC NAMING COLLISION: the preoptic_area/ under THIS file is
      the *lateral* preoptic area. It is distinct from
      hypothalamus/anterior/medial_area/left/preoptic_area/ (medial
      preoptic area), which contains different children
      (medial_preoptic_nucleus, median_preoptic_nucleus, inah_1-4).
      Do not merge.
    - SUPRAOPTIC IDENTITY: part_of_supraoptic_nucleus/ here and
      supraoptic_nucleus/ in medial_area/left/ are the SAME anatomical
      structure, split across two compartments for tree reasons. The
      Stage 4 audit should treat them as one structure — the lateral
      portion is documented here (osmoregulatory magnocellular
      component), and the medial portion is documented in the medial
      compartment. Reciprocal edge below.
    - Left-specific reciprocal connections to enforce in Stage 4:
        * part_of_supraoptic_nucleus/ ↔
          hypothalamus/anterior/medial_area/left/supraoptic_nucleus/
          (same structure, split across compartments)
        * periventricular_preoptic_nucleus/ ↔
          hypothalamus/anterior/medial_area/left/preoptic_area/
          medial_preoptic_nucleus/ (GnRH regulation partners, both
          left-side)
        * preoptic_area/lateral_preoptic_nucleus/ ↔
          hypothalamus/anterior/medial_area/left/preoptic_area/
          (adjacent sleep circuitry, both left-side)
        * anterior_part_of_lateral_nucleus/ ↔
          hypothalamus/tuberal/lateral_area/left/ (orexin/MCH span
          across divisions; document the connectivity, do not merge
          the compartments)
    - The hemisphere-mirror reciprocal connections (to right-side
      counterparts) belong in right/__init__.py (delta). Do not list
      them here.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py for the full list.
    - Connects upward to hypothalamus/anterior/lateral_area/.
"""