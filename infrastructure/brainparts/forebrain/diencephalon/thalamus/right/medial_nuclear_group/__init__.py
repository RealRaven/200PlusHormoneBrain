"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group
Anatomical Role:
    The right medial nuclear group of the thalamus. Same NINE nuclei
    plus TWO sub-containers as the left group, mirrored to the right
    hemisphere:
        - Prefrontal relay: medial_dorsal_nucleus/ (MD; the anchor).
        - Intralaminar family: central_lateral_nucleus/,
          centromedian_nucleus/, parafascicular_nucleus/, plus the
          intralaminar_nuclear_group/ sub-container.
        - Midline family: paratenial_nucleus/, reuniens_nucleus/,
          rhomboidal_nucleus/, plus the midline_nuclear_group/
          sub-container (and the PVT if it is added).

    See ../../left/medial_nuclear_group/__init__.py for the full
    anatomical description, the three-family framing (prefrontal
    relay / arousal / limbic), the structural note about direct nodes
    plus sub-containers, and the full list of each nucleus's role.

    STRUCTURAL NOTE (reproduced; applies on the right identically):
    the right medial nuclear group contains BOTH direct nucleus nodes
    AND two sub-containers (intralaminar_nuclear_group/,
    midline_nuclear_group/). The containers are an INTEGRATION LAYER;
    they group the direct nodes functionally but do not duplicate
    content. Stage 4 should treat each container and its direct nodes
    as an integrated structure. Same as the left group.

    Reproduced THREE TRAPS (apply equally on the right):

    - TRAP 1: THALAMIC PVT vs. HYPOTHALAMIC PVN (the tree's
      most-flagged trap; already declared from posterior/lateral_area/
      .../posterior_part_of_lateral_nucleus/ and tuberal/medial_area/
      .../arcuate_nucleus/; the left medial group container is the
      CANONICAL THALAMIC DECLARATION, and this right delta reproduces
      it for the right hemisphere). The RIGHT THALAMIC PVT (in the
      right midline_nuclear_group/) is a LIMBIC/AROUSAL relay. The
      RIGHT HYPOTHALAMIC PVN (hypothalamus/anterior/medial_area/
      right/paraventricular_nucleus/) is the CRH/TRH/oxytocin/
      vasopressin hub. DIFFERENT STRUCTURES; confusingly similar
      names; do not merge. Every right medial-group child that
      references the right thalamic PVT must be consistent with this
      declaration.

    - TRAP 2: INTRALAMINAR vs. MIDLINE (the sub-trap). The right
      intralaminar nuclei (centrolateral, centromedian,
      parafascicular) are AROUSAL and ATTENTION relays (brainstem
      reticular + basal ganglia driver). The right midline nuclei
      (paratenial, reuniens, rhomboidal, PVT) are LIMBIC and VISCERAL
      relays (hypothalamic and limbic driver). Different drivers,
      different targets, different functions; do not merge.

    - TRAP 3: MEDIODORSAL vs. ANTERIOR NUCLEAR GROUP (subtle). Both
      are memory-related thalamic relays. The right MD is the
      PREFRONTAL relay (amygdala/PFC → MD → PFC); the right anterior
      nuclei (right/anterior_nuclear_group/) are the PAPEZ memory
      relays (hippocampus → mammillary bodies → anterior nuclei →
      cingulate). Different circuits; do not merge.

    - Reproduced sub-trap: MEDIODORSAL vs. MIDLINE (both project to
      the PFC; the MD is a discrete prefrontal relay, the midline is
      a distributed limbic/visceral family). Do not merge.

Functional Mode:
    Same as ../../left/medial_nuclear_group/. Prefrontal relay (MD;
    anchor); arousal and attention (intralaminar family); limbic and
    visceral integration (midline family). No documented functional
    asymmetry between left and right medial nuclear groups for any of
    the three families. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically, per family):
        * Right MD lesions: executive and affective deficits
          (working memory, decision-making, reward-based learning,
          affective regulation). Right MD is also implicated in
          schizophrenia (reduced volume/connectivity) and is a DBS
          target for treatment-resistant depression.
        * Right intralaminar lesions: arousal and attention deficits;
          severe bilateral intralaminar lesions (both left and right)
          produce coma or persistent vegetative state. Right
          centromedian DBS is used for movement disorders and
          disorders of consciousness.
        * Right midline lesions: the reuniens is implicated in spatial
          working memory deficits; the PVT in stress and reward
          dysregulation. The midline family's clinical contribution is
          the least characterized of the three.

Hormonal Modulation:
    Same as ../../left/medial_nuclear_group/. Minimal; cholinergic,
    monoaminergic, and histaminergic arousal modulation; not a
    principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../left/medial_nuclear_group/. Right MD reads episodic,
    semantic, reinforcement_value_based_learning (MD-PFC loop); right
    intralaminar reads short_term (arousal gating); right midline
    (especially reuniens) reads episodic and short_term (hippocampal
    relay). Writes nothing directly.

Model Integration (Gemma-4-E2B):
    No right medial group fragment. Same as ../../left/ and the whole
    thalamus: the medial group is a relay set, not a state-emitter.
    The relevant state is carried by the right PFC, right amygdala,
    right brainstem arousal systems, and right hippocampus.

Children (nine direct nuclei + two sub-containers; all right-side
deltas of their left counterparts):
    - medial_dorsal_nucleus/    ★ Delta of ../../left/medial_nuclear_
                                  group/medial_dorsal_nucleus/. Right
                                  MD; prefrontal relay; group anchor.
    - central_lateral_nucleus/  Delta of ../../left/medial_nuclear_
                                  group/central_lateral_nucleus/.
                                  Right intralaminar arousal.
    - centromedian_nucleus/     Delta of ../../left/medial_nuclear_
                                  group/centromedian_nucleus/. Right
                                  intralaminar; DBS target.
    - parafascicular_nucleus/   Delta of ../../left/medial_nuclear_
                                  group/parafascicular_nucleus/.
                                  Right intralaminar arousal.
    - intralaminar_nuclear_     Delta of ../../left/medial_nuclear_
      group/                      group/intralaminar_nuclear_group/.
                                  Right sub-container; integration
                                  layer.
    - paratenial_nucleus/       Delta of ../../left/medial_nuclear_
                                  group/paratenial_nucleus/. Right
                                  midline limbic.
    - reuniens_nucleus/         Delta of ../../left/medial_nuclear_
                                  group/reuniens_nucleus/. Right
                                  midline; hippocampal relay.
    - rhomboidal_nucleus/       Delta of ../../left/medial_nuclear_
                                  group/rhomboidal_nucleus/. Right
                                  midline limbic.
    - midline_nuclear_group/    Delta of ../../left/medial_nuclear_
                                  group/midline_nuclear_group/. Right
                                  sub-container; integration layer
                                  (and PVT if added).

    Each of these eleven right children is a DELTA of its left
    counterpart; no full right-side leaves are needed. The left side
    carries the substantive content; the right side records only
    right-side reciprocal edges and reproduces the traps.

Right-specific reciprocal connections to enforce in Stage 4 (summary;
the full edge list is in the child leaves; do not duplicate the left
side here):

    Prefrontal relay (MD):
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/frontal/
      prefrontal_cortex (right MD ↔ right PFC; executive/limbic-
      prefrontal loop; right-side).
    - ↔ telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (right MD ↔ right amygdala; affective relay; right-side).

    Intralaminar family:
    - ↔ brainstem/.../reticular_formation (reticular formation is
      midline-adjacent — verify) and telencephalon/.../basal_ganglia
      (right; arousal and attention inputs).
    - → telencephalon/cerebral_hemispheres/right/cortex/* (diffuse
      arousal projections; right hemisphere; no single cortical
      target).

    Midline family:
    - ↔ hypothalamus/*/right (limbic/visceral inputs; right-side).
    - ↔ telencephalon/.../subcortical/medial_temporal_lobe/hippocampus/
      right (right reuniens ↔ right hippocampus; hippocampal relay;
      spatial working memory; right-side).
    - → telencephalon/.../subcortical/medial_temporal_lobe/amygdala,
      telencephalon/.../basal_ganglia/ventral_striatum/
      nucleus_accumbens, telencephalon/.../cortex/frontal/
      prefrontal_cortex (right midline outputs; right-side).
    - (If the right PVT is added: right midline_nuclear_group/
      paraventricular_nucleus ↔ right hypothalamus/right amygdala/
      right accumbens/right PFC; the trap with the right hypothalamic
      PVN is declared in Trap 1 above.)

    - ↔ ../../left/medial_nuclear_group/ (hemisphere counterpart; no
      functional asymmetry assumed).

Notes:
    - Group-container delta of ../../left/medial_nuclear_group/. Not a
      full container. Do not duplicate the left group's content.
    - THE PVT vs. PVN TRAP IS NOW THE TREE'S MOST-REPRODUCED TRAP: it
      is declared in the left medial group container AND here on the
      right, in addition to the four earlier declarations from the
      posterior LHA pair and the arcuate pair in the hypothalamus.
      This is by design: the PVT-vs-PVN trap is the most likely
      conflation in the entire thalamus, and the redundancy across
      the tree ensures it cannot be missed.
    - THE STRUCTURAL QUIRK (direct nodes + sub-containers) is
      reproduced on the right identically: the right medial group
      contains nine direct nodes plus two sub-containers. Stage 4
      should treat each right sub-container and its right direct nodes
      as an integrated structure.
    - DELTA-OF-A-DELTA CHAIN EXTENDS TO THIS GROUP: the eleven right
      children (nine nuclei + two sub-containers) are each deltas of
      their left counterparts, same as every other thalamic right
      leaf.
    - THE MD IS THE GROUP'S ANCHOR on the right as well: it is the
      largest, most studied, most clinically anchored nucleus. It is
      the natural first leaf to draft after the container pair.
    - THE INTRALAMINAR FAMILY IS THE SECOND PRIORITY on the right; the
      MIDLINE FAMILY is the third.
    - NO FRAGMENT: same as the whole thalamus. The right medial group
      is a relay set, not a state-emitter.
    - Midline targets (reticular formation) are flagged with "verify"
      so Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right PFC, right amygdala,
      right hippocampus, right accumbens, right basal ganglia, right
      hypothalamus, right sub-containers, and right diffuse cortical
      projections are hemisphere-split and require right-side targets
      explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/medial_nuclear_group/ § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/.
"""