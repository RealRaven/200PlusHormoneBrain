"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left
Anatomical Role:
    Left hemisphere of the thalamus. Contains the SIX NUCLEAR GROUPS of
    the left thalamus, each documented as a child container with its
    own nuclei:
        - anterior_nuclear_group/   (Papez circuit relay; 3 nuclei)
        - lateral_nuclear_group/    (higher-order association; 3 nuclei)
        - medial_nuclear_group/     (limbic/executive/arousal; 9 nuclei
                                     + 2 sub-containers)
        - metathalamus/             (sensory relay; 2 nuclei)
        - reticular_nucleus/        (the GABAergic gatekeeper)
        - ventral_nuclear_group/    (motor and somatosensory; 3 nuclei
                                     + 2 sub-nuclei)

    See ../../__init__.py (the parent thalamus container) for the full
    anatomical description, the six-group taxonomy, the first-order vs.
    higher-order functional distinction, the six naming traps, and the
    "no fragment" discipline. This file is the left-hemisphere
    container; it does not re-describe the groups.

    The parent container's structural note about the medial nuclear
    group (direct nodes + intralaminar/midline sub-containers) applies
    to the left hemisphere identically: the direct nodes and the
    sub-containers are an INTEGRATED structure; the sub-containers
    group the direct nodes functionally but do not duplicate content.

Functional Mode:
    Same as the parent thalamus container. The left thalamus relays
    every sensory modality (except olfaction), relays basal ganglia and
    cerebellar motor commands, relays limbic and executive circuits,
    and gates the whole system via the left reticular nucleus. See
    ../../__init__.py § Functional Mode for the full description.
    No documented functional asymmetry between left and right thalamus
    for any of the six groups (the sensory and motor pathways are
    contralateral, but the thalamus itself is functionally symmetric).
    Do not fabricate one.

Hormonal Modulation:
    Same as the parent. The left thalamus is not a neuroendocrine
    structure; it is modulated by brainstem neuromodulators (NE,
    serotonin, ACh, dopamine, histamine, orexin), not by the 12
    endocrine axes. See ../../__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as the parent. The left thalamus relays memory signals but
    does not store them; some nuclei (anterior group, MD,
    intralaminar) read memory-adjacent stores. No thalamic nucleus
    writes memory directly. See ../../__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No thalamus-wide fragment. Same as the parent: the thalamus is a
    relay, not a state-emitter. The left hemisphere's relevant state
    fragments are emitted by the upstream sources (LC, raphe, LDT/PPN,
    VTA, TMN, orexin, sensory organs, basal ganglia, cerebellum,
    amygdala) and the cortical targets (PFC, V1, M1). See
    ../../__init__.py § Model Integration.

Children (six nuclear groups, each with its own nuclei; see parent for
full child lists; summarized here):
    - anterior_nuclear_group/    ★ Papez circuit relay. Contains:
        ├── anterodorsal_nucleus/        (head-direction; Papez)
        ├── anteromedial_nucleus/        (Papez)
        └── anteroventral_nucleus/       (Papez)
    - lateral_nuclear_group/     Higher-order association. Contains:
        ├── lateral_dorsal_nucleus/      (cingulate/association)
        ├── lateral_posterior_nucleus/   (parietal association)
        └── pulvinar/                    (visual association; V2–V5)
    - medial_nuclear_group/      Limbic/executive/arousal. Contains:
        ├── central_lateral_nucleus/     (intralaminar; arousal)
        ├── centromedian_nucleus/        (intralaminar; motor/arousal)
        ├── intralaminar_nuclear_group/  (sub-container; see parent note)
        ├── medial_dorsal_nucleus/       (prefrontal relay; ★)
        ├── midline_nuclear_group/       (sub-container; see parent note)
        ├── parafascicular_nucleus/      (intralaminar; arousal)
        ├── paratenial_nucleus/          (midline; limbic)
        ├── reuniens_nucleus/            (midline; hippocampal relay)
        └── rhomboidal_nucleus/          (midline; limbic)
    - metathalamus/              Sensory relay. Contains:
        ├── lateral_geniculate_body/     (vision; LGN → V1; ★)
        └── medial_geniculate_body/      (audition; MGN → A1; ★)
    - reticular_nucleus/         The GABAergic gatekeeper. The
                                 thalamic gate; not a relay.
    - ventral_nuclear_group/     Motor and somatosensory. Contains:
        ├── ventral_anterior_nucleus/    (basal ganglia motor; VA)
        ├── ventral_lateral_nucleus/     (cerebellar motor; VL)
        └── ventral_posterior_nucleus/   (somatosensory container)
            ├── ventral_posterior_lateral_nucleus/  (body; VPL)
            └── ventral_posterior_medial_nucleus/   (face; VPM)

Left-specific reciprocal connections to enforce in Stage 4 (the full
edge list is in the child leaves; this is a summary of the left-side
edges; do not duplicate the right side here — those belong in
right/__init__.py):

    Sensory relays (first-order):
    - left anterior_nuclear_group ↔ hypothalamus/mammillary_bodies/
      left (mammillothalamic tract; Papez relay; the mammillary leaf
      declares this edge from its side) and ↔ telencephalon/.../
      cortex/cingulate (Papez cortical target).
    - left metathalamus/lateral_geniculate_body ↔ left retina (via
      optic tract) and ↔ telencephalon/.../occipital/primary_visual_
      cortex (V1).
    - left metathalamus/medial_geniculate_body ↔ midbrain/.../
      inferior_colliculus and ↔ telencephalon/.../temporal/
      primary_auditory_cortex (A1).
    - left ventral_nuclear_group/ventral_posterior_lateral_nucleus ↔
      spinal cord + brainstem (body somatosensory input) and →
      telencephalon/.../parietal/primary_somatosensory_cortex (S1).
    - left ventral_nuclear_group/ventral_posterior_medial_nucleus ↔
      brainstem trigeminal (face somatosensory input) and →
      telencephalon/.../parietal/primary_somatosensory_cortex (S1).

    Motor relays (first-order):
    - left ventral_nuclear_group/ventral_anterior_nucleus ↔
      telencephalon/.../basal_ganglia (basal ganglia motor input) and
      → telencephalon/.../cortex/frontal/primary_motor_cortex (M1).
    - left ventral_nuclear_group/ventral_lateral_nucleus ↔ cerebellum
      (cerebellar motor input) and → telencephalon/.../cortex/frontal/
      primary_motor_cortex and premotor_cortex.

    Limbic and higher-order relays:
    - left medial_nuclear_group/medial_dorsal_nucleus ↔
      telencephalon/.../cortex/frontal/prefrontal_cortex (PFC).
    - left lateral_nuclear_group/pulvinar ↔ telencephalon/.../cortex/
      occipital/* and temporal/* (visual association).
    - left lateral_nuclear_group/lateral_posterior_nucleus ↔
      telencephalon/.../cortex/parietal/posterior_parietal_cortex.

    Gate:
    - left reticular_nucleus ↔ left thalamo-cortical and
      cortico-thalamic axons (the GABAergic gate; no single cortical
      target; gates the whole left thalamus).

    Arousal:
    - left medial_nuclear_group/intralaminar group ↔
      brainstem/.../reticular_formation and telencephalon/.../
      basal_ganglia (arousal and attention; diffuse cortical
      projections).

Notes:
    - Left-hemisphere container. Not a delta of the parent — it is the
      authoritative left-hemisphere container. right/ is a delta of
      this file (the thalamus/right/ container is a delta mirror of
      this file; each thalamic leaf on the right is a delta of its
      left counterpart).
    - SIX NAMING TRAPS reproduced from the parent container in
      abbreviated form above (see the Children and Functional Mode
      sections). The full text is in ../../__init__.py. A contributor
      entering at left/ must see them.
    - THE PVT vs. PVN TRAP IS THE MOST IMPORTANT: the thalamic
      paraventricular nucleus (PVT; in the left medial_nuclear_group/
      midline_nuclear_group/paraventricular_nucleus/) is DIFFERENT from
      the hypothalamic paraventricular nucleus (PVN; in
      hypothalamus/anterior/medial_area/left/paraventricular_nucleus/).
      The PVT is a limbic/arousal relay; the PVN is the
      CRH/TRH/oxytocin/vasopressin hub. Do not merge.
    - NO FRAGMENT: same as the parent. The thalamus is a relay, not a
      state-emitter.
    - The six nuclear groups are all left-side children; do not create
      left/ sub-children under them (the left/ hemisphere is the
      container; the groups are the children).
    - The medial_nuclear_group/ sub-containers (intralaminar,
      midline) are an integration layer, not separate functional
      entities. See parent container's structural note.
    - The anterior_nuclear_group/ is the natural first group to draft
      because it closes the mammillary bodies → anterior thalamus edge
      declared from the hypothalamus work.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py § Notes for the full list.
    - Connects upward to diencephalon/thalamus/.
"""