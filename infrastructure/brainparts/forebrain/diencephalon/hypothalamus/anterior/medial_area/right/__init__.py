"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right
Anatomical Role:
    Delta mirror of ../left/. Right hemisphere of the medial area of the
    anterior hypothalamus. Contains the same five nuclei, mirrored to the
    right hemisphere:
        - anterior_hypothalamic_nucleus/
        - paraventricular_nucleus/          ★★
        - preoptic_area/                    (sub-container)
            ├── medial_preoptic_nucleus/    ★
            │   ├── inah_1/
            │   ├── inah_2/
            │   ├── inah_3/
            │   └── inah_4/
            └── median_preoptic_nucleus/    ★
        - suprachiasmatic_nucleus/          ★★
        - supraoptic_nucleus/

    See ../left/__init__.py for the full anatomical description and the
    tree diagram. See ../../__init__.py for the per-nucleus functional
    descriptions and the seven model fragments.

Functional Mode:
    Same as ../left/ and ../../__init__.py. No documented functional
    asymmetry between left and right medial area for these five nuclei.
    Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. See ../../__init__.py.

Memory Interfaces:
    Same as ../left/. See ../../__init__.py.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. The seven fragments (HPA,
    HPT/growth, social, fluid/osmotic, circadian, thermoregulatory/
    autonomic, reproductive) are emitted by the parent medial_area/
    container and by the five leaf files, and aggregate with their
    lateral-area counterparts at the anterior-division level. See
    ../../__init__.py § Model Integration for the two mandatory
    AGGREGATION RULES (osmotic fragment aggregated with lateral_area;
    reproductive fragment aggregated with lateral_area PeN). Those rules
    apply identically on the right.

Reproduced critical warnings (both apply to specific children in this
compartment, same as on the left):
    - PREOPTIC NAMING COLLISION (applies to preoptic_area/ below): the
      preoptic_area/ under THIS file is the MEDIAL preoptic area,
      containing medial_preoptic_nucleus/, median_preoptic_nucleus/, and
      inah_1–4. It is distinct from
      lateral_area/right/preoptic_area/ (LATERAL preoptic area,
      containing lateral_preoptic_nucleus/). Do not merge. Do not move
      children between the two preoptic areas.
    - SON STRUCTURAL IDENTITY (applies to supraoptic_nucleus/ below):
      supraoptic_nucleus/ here and
      lateral_area/right/part_of_supraoptic_nucleus/ are the SAME
      anatomical structure, split across two compartments for anatomical
      mirroring of the medial/lateral zones. Stage 4 audit must treat
      them as ONE structure. Do not merge the nodes.

Children (right-hemisphere deltas of the left leaves):
    - anterior_hypothalamic_nucleus/   (delta of ../left/...)
    - paraventricular_nucleus/         (delta of ../left/...)
    - preoptic_area/                   (sub-container delta of ../left/...)
      ├── medial_preoptic_nucleus/       (delta of ../left/...)
      │   ├── inah_1/
      │   ├── inah_2/
      │   ├── inah_3/
      │   └── inah_4/
      └── median_preoptic_nucleus/     (delta of ../left/...)
    - suprachiasmatic_nucleus/         (delta of ../left/...)
    - supraoptic_nucleus/              (delta of ../left/...)

Right-specific reciprocal connections to enforce in Stage 4 (do not
duplicate the left-side edges listed in ../left/):
    - paraventricular_nucleus/ ↔ pituitary_gland/anterior (CRH, TRH,
      somatostatin via hypophyseal portal; right-side projection)
    - paraventricular_nucleus/ ↔ pituitary_gland/posterior (oxytocin,
      vasopressin via magnocellular axon terminals)
    - paraventricular_nucleus/ ↔ brainstem autonomic nuclei (NTS, RVLM;
      both are midline-adjacent — verify)
    - paraventricular_nucleus/ ↔ lateral_area/right/
      part_of_supraoptic_nucleus (magnocellular co-regulation; right-side)
    - suprachiasmatic_nucleus/ ↔ epithalamus/pineal_gland (SCN → PVN →
      spinal cord → SCG → pineal; canonical circadian loop; SCN and pineal
      are midline/adjacent — verify)
    - suprachiasmatic_nucleus/ ↔ lateral_area/right/
      periventricular_preoptic_nucleus (SCN → PeN vasopressin; circadian
      gating of LH surge; right-side)
    - suprachiasmatic_nucleus/ ↔ lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus (SCN → LPO; circadian sleep gating;
      right-side)
    - supraoptic_nucleus/ ↔ lateral_area/right/
      part_of_supraoptic_nucleus (SAME STRUCTURE, split across
      compartments; treat as one)
    - supraoptic_nucleus/ ↔ pituitary_gland/neurohypophysis (vasopressin,
      oxytocin release; right-side projection)
    - anterior_hypothalamic_nucleus/ ↔ brainstem parasympathetic nuclei
      (dorsal motor vagus, nucleus ambiguus; both are midline-adjacent —
      verify)
    - preoptic_area/right/medial_preoptic_nucleus/ ↔ lateral_area/right/
      preoptic_area (adjacent preoptic circuits; keep distinct; right-side)
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed)

Notes:
    - Container delta of ../left/. Inherits everything structural and
      functional from ../left/. Do not duplicate.
    - Both structural traps are reproduced above because they are
      structural traps that apply on both hemispheres. The full
      anatomical, functional, hormonal, and memory content is referenced
      rather than duplicated.
    - The left-specific reciprocal connections live in ../left/__init__.py
      § Notes. The right-specific ones live here. Both lists are needed
      for the Stage 4 audit to reach closure.
    - ★★ priority markers on PVN and SCN are inherited from ../left/ and
      ../../__init__.py. Right-side PVN and SCN should be drafted after
      their left-side counterparts, not before.
    - Midline targets (NTS, RVLM, pineal, dorsal motor vagus, nucleus
      ambiguus) are flagged with "verify" so Stage 4 does not force a
      hemisphere split on structures that are not hemisphere-split in
      the tree.
    - "other_preoptic_nuclei" and "periventricular_nucleus" are children
      of hypothalamus/, NOT of medial_area/. Do not add them here (same
      as ../left/).
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/.
"""