"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.right
Anatomical Role:
    Delta mirror of ../left/. Right hemisphere of the anterior lateral
    area of the hypothalamus. Contains the same four nuclei, mirrored to
    the right hemisphere:
        - anterior_part_of_lateral_nucleus/
        - part_of_supraoptic_nucleus/
        - periventricular_preoptic_nucleus/
        - preoptic_area/lateral_preoptic_nucleus/

    See ../left/__init__.py for the full anatomical description and for
    both critical warnings. This file is a delta and does not restate them
    in full — but see the reproduced warnings below, because both apply
    equally on the right.

Functional Mode:
    Same as ../left/ and ../../__init__.py. No documented functional
    asymmetry between left and right anterior lateral area for these four
    nuclei. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. See ../../__init__.py.

Memory Interfaces:
    Same as ../left/. See ../../__init__.py.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. See ../left/ and
    ../../__init__.py for the fragment emission rules (including the
    osmotic double-counting aggregation rule at the anterior-division
    level, which applies identically on the right).

Reproduced critical warnings (both apply on the right, same as on the left):
    - PREOPTIC NAMING COLLISION: preoptic_area/ under THIS file is the
      *lateral* preoptic area, distinct from
      hypothalamus/anterior/medial_area/right/preoptic_area/ (medial
      preoptic area). Do not merge.
    - SUPRAOPTIC IDENTITY: part_of_supraoptic_nucleus/ here and
      supraoptic_nucleus/ in medial_area/right/ are the SAME anatomical
      structure, split across compartments. Stage 4 audit should treat
      them as one structure — the lateral portion documented here, the
      medial portion documented in the medial compartment.

Children (right-hemisphere deltas of the left leaves):
    - anterior_part_of_lateral_nucleus/   (delta of ../left/...)
    - part_of_supraoptic_nucleus/         (delta of ../left/...)
    - periventricular_preoptic_nucleus/   (delta of ../left/...)
    - preoptic_area/                      (delta of ../left/...)
        └── lateral_preoptic_nucleus/       (delta of ../left/...)

Right-specific reciprocal connections to enforce in Stage 4:
    - part_of_supraoptic_nucleus/ ↔
      hypothalamus/anterior/medial_area/right/supraoptic_nucleus/
      (same structure, split across compartments; right-side)
    - periventricular_preoptic_nucleus/ ↔
      hypothalamus/anterior/medial_area/right/preoptic_area/
      medial_preoptic_nucleus/ (GnRH regulation partners, right-side)
    - preoptic_area/lateral_preoptic_nucleus/ ↔
      hypothalamus/anterior/medial_area/right/preoptic_area/
      (adjacent sleep circuitry, right-side)
    - anterior_part_of_lateral_nucleus/ ↔
      hypothalamus/tuberal/lateral_area/right/ (orexin/MCH span across
      divisions; right-side)
    - ↔ ../left/ (hemisphere counterpart; no strong functional
      lateralization assumed)

Notes:
    - Delta file. Inherits everything structural and functional from
      ../left/. Do not duplicate.
    - The left-specific reciprocal connections live in ../left/__init__.py
      § Notes. The right-specific ones live here. Both lists are needed
      for the Stage 4 audit to reach closure.
    - This file is the DELTA-PATTERN EXEMPLAR for hemisphere-mirror
      *containers* (as distinct from the leaf delta exemplar
      habenular_nuclei/right/). Copy this shape for other hemisphere-
      mirror containers whose parent already carries the warnings:
      reproduce the warnings, point to left for everything else, list
      only hemisphere-specific edges.
    - Connects upward to hypothalamus/anterior/lateral_area/.
"""