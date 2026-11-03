"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left
Anatomical Role:
    Left hemisphere of the medial area of the anterior hypothalamus.
    Contains five nuclei, all in the left hemisphere. See
    ../../__init__.py (the medial_area container) for the full anatomical
    description of each nucleus, the ★★ priority marking for PVN and SCN,
    and the two structural traps that apply to specific children.

    The five left-hemisphere nuclei:
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

Functional Mode:
    Same as parent medial_area/. See ../../__init__.py for the full
    functional description of each nucleus (HPA/HPT/growth, social,
    fluid, circadian, parasympathetic/thermoregulatory, autonomic, and
    medial preoptic reproductive circuits).
    No documented functional asymmetry exists between the left and right
    medial area for these five nuclei. Do not fabricate one.

Hormonal Modulation:
    Same as parent. See ../../__init__.py.

Memory Interfaces:
    Same as parent. See ../../__init__.py.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. The seven fragments (HPA,
    HPT/growth, social, fluid/osmotic, circadian, thermoregulatory/
    autonomic, reproductive) are emitted by the parent medial_area/
    container and by the five leaf files, not by this container. See
    ../../__init__.py § Model Integration for the full fragment set and
    the two mandatory AGGREGATION RULES (osmotic fragment aggregated
    with lateral_area; reproductive fragment aggregated with lateral_area
    PeN).

Reproduced critical warnings (both apply to specific children in this
compartment, same as on the right):
    - PREOPTIC NAMING COLLISION (applies to preoptic_area/ below): the
      preoptic_area/ under THIS file is the MEDIAL preoptic area,
      containing medial_preoptic_nucleus/, median_preoptic_nucleus/, and
      inah_1–4. It is distinct from
      lateral_area/left/preoptic_area/ (LATERAL preoptic area,
      containing lateral_preoptic_nucleus/). Do not merge. Do not move
      children between the two preoptic areas.
    - SON STRUCTURAL IDENTITY (applies to supraoptic_nucleus/ below):
      supraoptic_nucleus/ here and
      lateral_area/left/part_of_supraoptic_nucleus/ are the SAME
      anatomical structure, split across two compartments for anatomical
      mirroring of the medial/lateral zones. Stage 4 audit must treat
      them as ONE structure. Do not merge the nodes.

Children (left-hemisphere nuclei — each is a full leaf or sub-container,
not a delta):
    - anterior_hypothalamic_nucleus/   ★ Parasympathetic outflow;
                                         thermoregulation; cardiovascular
                                         control.
    - paraventricular_nucleus/         ★★ Most hormonally complex nucleus
                                         in the brain: CRH, TRH,
                                         somatostatin (parvocellular
                                         endocrine); oxytocin, vasopressin
                                         (magnocellular); autonomic
                                         control. Draft first within the
                                         medial area.
    - preoptic_area/                   Sub-container (MEDIAL preoptic
      ├── medial_preoptic_nucleus/       area; distinct from lateral).
      │   ├── inah_1/                  ★ Maternal/sexual behavior; GnRH
      │   ├── inah_2/                    regulation.
      │   ├── inah_3/
      │   └── inah_4/
      └── median_preoptic_nucleus/     ★ GnRH regulation.
    - suprachiasmatic_nucleus/         ★★ Master circadian pacemaker;
                                         closes the SCN → pineal loop.
    - supraoptic_nucleus/              ★ Medial portion of the SON.
                                         Same structure as
                                         lateral_area/left/
                                         part_of_supraoptic_nucleus.
                                         Vasopressin, oxytocin
                                         (magnocellular).

Left-specific reciprocal connections to enforce in Stage 4 (do not list
right-side or mirror edges here — those belong in right/__init__.py):
    - paraventricular_nucleus/ ↔ pituitary_gland/anterior (CRH, TRH,
      somatostatin via hypophyseal portal; left-side projection)
    - paraventricular_nucleus/ ↔ pituitary_gland/posterior (oxytocin,
      vasopressin via magnocellular axon terminals)
    - paraventricular_nucleus/ ↔ brainstem autonomic nuclei (NTS, RVLM;
      sympathetic/parasympathetic outflow)
    - paraventricular_nucleus/ ↔ lateral_area/left/
      part_of_supraoptic_nucleus (magnocellular co-regulation; both are
      magnocellular nuclei)
    - suprachiasmatic_nucleus/ ↔ epithalamus/pineal_gland (SCN → PVN →
      spinal cord → SCG → pineal; canonical circadian loop)
    - suprachiasmatic_nucleus/ ↔ lateral_area/left/
      periventricular_preoptic_nucleus (SCN → PeN vasopressin; circadian
      gating of LH surge)
    - suprachiasmatic_nucleus/ ↔ lateral_area/left/preoptic_area/
      lateral_preoptic_nucleus (SCN → LPO; circadian sleep gating)
    - supraoptic_nucleus/ ↔ lateral_area/left/
      part_of_supraoptic_nucleus (SAME STRUCTURE, split across
      compartments; treat as one)
    - supraoptic_nucleus/ ↔ pituitary_gland/neurohypophysis (vasopressin,
      oxytocin release)
    - anterior_hypothalamic_nucleus/ ↔ brainstem parasympathetic nuclei
      (dorsal motor vagus, nucleus ambiguus)
    - preoptic_area/left/medial_preoptic_nucleus/ ↔ lateral_area/left/
      preoptic_area (adjacent preoptic circuits; keep distinct)

Notes:
    - Left-side container. Not a delta of the parent — it is the
      authoritative left-hemisphere container. right/ is a delta of this
      file (lateral_area/right/ convention).
    - Both structural traps are reproduced above because they apply to
      specific children within THIS compartment (preoptic collision →
      preoptic_area/; SON identity → supraoptic_nucleus/). A contributor
      entering at this level would otherwise miss them.
    - The ★★ marking on PVN and SCN is inherited from the parent and
      restated here: draft these two first within the left compartment.
    - "other_preoptic_nuclei" and "periventricular_nucleus" are children
      of hypothalamus/, NOT of medial_area/. Do not add them here.
    - The five children are all lateralized (left/ and right/). The
      right-side files are delta mirrors; none is a full duplicate.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/.
"""