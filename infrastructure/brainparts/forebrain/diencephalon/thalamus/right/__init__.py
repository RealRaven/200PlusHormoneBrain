"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right
Anatomical Role:
    Right hemisphere of the thalamus. Contains the same SIX NUCLEAR
    GROUPS as ../left/, mirrored to the right hemisphere:
        - anterior_nuclear_group/   (Papez circuit relay; 3 nuclei)
        - lateral_nuclear_group/    (higher-order association; 3 nuclei)
        - medial_nuclear_group/     (limbic/executive/arousal; 9 nuclei
                                     + 2 sub-containers)
        - metathalamus/             (sensory relay; 2 nuclei)
        - reticular_nucleus/        (the GABAergic gatekeeper)
        - ventral_nuclear_group/    (motor and somatosensory; 3 nuclei
                                     + 2 sub-nuclei)

    See ../left/__init__.py for the full child map and the six-group
    taxonomy; see ../../__init__.py (the parent thalamus container) for
    the full anatomical description, the first-order vs. higher-order
    functional distinction, the six naming traps, and the "no fragment"
    discipline. This file is a hemisphere-container delta; it does not
    re-describe the groups.

    DELTA-OF-A-DELTA CHAIN NOTE: every right thalamic leaf (the ~40
    files under the six right groups) will ALSO be a delta of its left
    counterpart, following the established hemisphere-delta pattern.
    This file establishes that the chain extends across the entire
    thalamus subtree: six right group containers (each a delta of its
    left group container) + ~30 right leaf nuclei (each a delta of its
    left leaf). No full right-side leaves are needed; the left side
    carries the substantive content for both hemispheres because the
    thalamus is functionally symmetric.

Functional Mode:
    Same as ../left/ and the parent thalamus container. The right
    thalamus relays every sensory modality (except olfaction), relays
    basal ganglia and cerebellar motor commands, relays limbic and
    executive circuits, and gates the whole system via the right
    reticular nucleus. No documented functional asymmetry between left
    and right thalamus for any of the six groups. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. The right thalamus is not a neuroendocrine
    structure; it is modulated by brainstem neuromodulators (NE,
    serotonin, ACh, dopamine, histamine, orexin). See ../../__init__.py
    § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. The right thalamus relays memory signals but does
    not store them; some nuclei (anterior group, MD, intralaminar) read
    memory-adjacent stores. No thalamic nucleus writes memory directly.
    See ../../__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No thalamus-wide fragment. Same as ../left/ and the parent: the
    thalamus is a relay, not a state-emitter. The right hemisphere's
    relevant state fragments are emitted by the upstream sources and
    the cortical targets. See ../../__init__.py § Model Integration.

Reproduced six naming traps (apply equally on the right):
    - THALAMIC PVT vs. HYPOTHALAMIC PVN: the right thalamic
      paraventricular nucleus (PVT; right medial_nuclear_group/
      midline_nuclear_group/paraventricular_nucleus/) is DIFFERENT
      from the right hypothalamic paraventricular nucleus (PVN;
      hypothalamus/anterior/medial_area/right/paraventricular_nucleus/).
      The PVT is a limbic/arousal relay; the PVN is the
      CRH/TRH/oxytocin/vasopressin hub. Do not merge.
    - PULVINAR vs. LATERAL POSTERIOR: both higher-order; pulvinar =
      visual association, LP = parietal association. Do not merge.
    - VPL vs. VPM: both primary somatosensory; VPL = body, VPM = face.
      Somatotopic split, not functional split. Do not merge.
    - LGN vs. MGN: both metathalamus; LGN = visual, MGN = auditory.
      Do not merge.
    - THALAMIC RETICULAR vs. MIDBRAIN RETICULAR FORMATION: the right
      thalamic reticular nucleus is the thin GABAergic shell around
      the right thalamus; the midbrain reticular formation is the
      distributed brainstem arousal system. Do not merge.
    - ANTERIOR THALAMIC NUCLEI vs. ANTERIOR HYPOTHALAMIC NUCLEUS: both
      "anterior"; the anterior thalamic nuclei (right) are the Papez
      relay; the anterior hypothalamic nucleus (right) is the
      parasympathetic/thermoregulatory hub. Do not merge.

Children (six nuclear groups — all right-side deltas of their left
counterparts; see ../left/ for the child lists, and ../../ for the
functional descriptions):
    - anterior_nuclear_group/    ★ Delta of ../left/
                                   anterior_nuclear_group/. Papez
                                   circuit relay.
    - lateral_nuclear_group/     Delta of ../left/lateral_nuclear_group/.
                                   Higher-order association.
    - medial_nuclear_group/      Delta of ../left/medial_nuclear_group/.
                                   Limbic/executive/arousal. Includes
                                   the intralaminar_nuclear_group/ and
                                   midline_nuclear_group/
                                   sub-containers (also deltas).
    - metathalamus/              Delta of ../left/metathalamus/.
                                   Sensory relay.
    - reticular_nucleus/         Delta of ../left/reticular_nucleus/.
                                   The GABAergic gatekeeper.
    - ventral_nuclear_group/     Delta of ../left/ventral_nuclear_group/.
                                   Motor and somatosensory. Includes the
                                   ventral_posterior_nucleus/ container
                                   (also a delta) with its VPL and VPM
                                   sub-nuclei (also deltas).

Right-specific reciprocal connections to enforce in Stage 4 (summary;
the full edge list is in the child leaves; do not duplicate the left
side here):

    Sensory relays (first-order):
    - right anterior_nuclear_group ↔ hypothalamus/mammillary_bodies/
      right (mammillothalamic tract; Papez relay; the right mammillary
      leaf declares this edge from its side) and ↔ telencephalon/.../
      cortex/cingulate (Papez cortical target).
    - right metathalamus/lateral_geniculate_body ↔ right retina (via
      right optic tract) and ↔ telencephalon/.../occipital/
      primary_visual_cortex (V1).
    - right metathalamus/medial_geniculate_body ↔ midbrain/.../
      inferior_colliculus (inferior colliculus is midline-adjacent —
      verify) and ↔ telencephalon/.../temporal/primary_auditory_cortex
      (A1).
    - right ventral_nuclear_group/ventral_posterior_lateral_nucleus ↔
      spinal cord + brainstem (body somatosensory input) and →
      telencephalon/.../parietal/primary_somatosensory_cortex (S1).
    - right ventral_nuclear_group/ventral_posterior_medial_nucleus ↔
      brainstem trigeminal (face somatosensory input) and →
      telencephalon/.../parietal/primary_somatosensory_cortex (S1).

    Motor relays (first-order):
    - right ventral_nuclear_group/ventral_anterior_nucleus ↔
      telencephalon/.../basal_ganglia (basal ganglia motor input) and
      → telencephalon/.../cortex/frontal/primary_motor_cortex (M1).
    - right ventral_nuclear_group/ventral_lateral_nucleus ↔ cerebellum
      (cerebellar motor input; the right cerebellar hemisphere) and →
      telencephalon/.../cortex/frontal/primary_motor_cortex and
      premotor_cortex.

    Limbic and higher-order relays:
    - right medial_nuclear_group/medial_dorsal_nucleus ↔
      telencephalon/.../cortex/frontal/prefrontal_cortex (PFC).
    - right lateral_nuclear_group/pulvinar ↔ telencephalon/.../cortex/
      occipital/* and temporal/* (visual association).
    - right lateral_nuclear_group/lateral_posterior_nucleus ↔
      telencephalon/.../cortex/parietal/posterior_parietal_cortex.

    Gate:
    - right reticular_nucleus ↔ right thalamo-cortical and
      cortico-thalamic axons (the GABAergic gate; no single cortical
      target; gates the whole right thalamus).

    Arousal:
    - right medial_nuclear_group/intralaminar group ↔
      brainstem/.../reticular_formation (reticular formation is
      midline-adjacent — verify) and telencephalon/.../basal_ganglia
      (arousal and attention; diffuse cortical projections).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Hemisphere-container delta of ../left/. Inherits everything
      structural and functional from ../left/ and ../../. Do not
      duplicate the parent or left-container content.
    - DELTA-OF-A-DELTA CHAIN EXTENDED TO THE THALAMUS: every right
      thalamic leaf (~40 files across the six groups and their
      sub-containers) will be a delta of its left counterpart. This
      file establishes that the chain extends across the entire
      thalamus subtree, with the same discipline as the LHA segments
      and the STN/VMH right leaves. The left side carries the
      substantive content; the right side records only right-side
      reciprocal edges and reproduces structural traps.
    - SIX TRAPS reproduced in abbreviated form above. The PVT vs. PVN
      trap is the most important and has been flagged from other files
      (posterior LHA, arcuate) — this is the canonical declaration for
      the right hemisphere, matching ../left/.
    - NO FRAGMENT: same as ../left/ and the parent. The thalamus is a
      relay, not a state-emitter. Do not add a fragment on the right
      either.
    - The six nuclear groups are all right-side children; do not
      create right/ sub-children under them (the right/ hemisphere is
      the container; the groups are the children).
    - The medial_nuclear_group/ sub-containers (intralaminar, midline)
      are integration layers on the right, same as on the left. See
      ../left/ § Notes.
    - The anterior_nuclear_group/ is the natural first group to draft
      on the right because it closes the mammillary bodies → anterior
      thalamus edge (the right mammillary bodies leaf declares the
      right side of this edge).
    - Midline targets (inferior colliculus, reticular formation) are
      flagged with "verify" so Stage 4 does not force a hemisphere
      split on structures that are not hemisphere-split in the tree.
      Right retina, right cingulate, right V1, right A1, right S1,
      right PFC, right visual association cortex, right posterior
      parietal cortex, right M1, right premotor cortex, right basal
      ganglia, right cerebellum, right mammillary bodies, right
      thalamo-cortical and cortico-thalamic axons, and right
      intralaminar-to-cortex projections are hemisphere-split and
      require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../__init__.py § Notes for the full list.
    - Connects upward to diencephalon/thalamus/.
"""