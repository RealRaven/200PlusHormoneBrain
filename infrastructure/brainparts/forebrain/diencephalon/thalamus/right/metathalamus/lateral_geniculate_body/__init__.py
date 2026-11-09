"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.metathalamus.lateral_geniculate_body
Anatomical Role:
    The right lateral geniculate body (LGN). A six-layered,
    retinotopically organized nucleus at the right metathalamus, at the
    caudal pole of the right thalamus. Same FIRST-ORDER VISUAL RELAY
    role as the left LGN: the thalamic relay of the right
    retinogeniculostriate visual pathway (right retina → optic chiasm →
    right optic tract → right LGN → right optic radiation → right V1).

    The six-layer structure (magnocellular, parvocellular,
    koniocellular) is documented WITHIN the leaf, not as child nodes.
    Same convention as the left LGN, the habenula's LHb/MHb, the PVN's
    sub-populations, the pulvinar's three subregions, and the MD's
    three subdivisions. Do not create magnocellular/, parvocellular/,
    or koniocellular/ as child nodes here either.

    Each LGN receives input from BOTH eyes (ipsilateral temporal retina
    and contralateral nasal retina). The right LGN represents the
    CONTRALATERAL (LEFT) visual hemifield; the left LGN represents the
    RIGHT visual hemifield. See
    ../../../../left/metathalamus/lateral_geniculate_body/__init__.py
    for the full anatomical description, the parallel-channel
    architecture, and the retinotopic organization.

    Reproduced FOUR TRAPS (apply equally on the right):
    - LGN vs. MGN (intra-metathalamus): the right LGN is VISUAL; the
      right MGN (right/metathalamus/medial_geniculate_body/) is
      AUDITORY. Both are "geniculate bodies"; different modalities; do
      not merge.
    - LGN vs. PULVINAR (canonical first-order-vs-higher-order trap):
      the right LGN is the FIRST-ORDER visual relay (retinal driver;
      right V1 target); the right pulvinar
      (right/lateral_nuclear_group/pulvinar/) is the HIGHER-ORDER
      visual association relay (cortical layer 5 driver; right
      V2–V5/MT/IT target). Different relay types; do not merge.
    - LGN vs. SUPERIOR COLLICULUS: both receive right retinal input,
      but the right LGN is the THALAMOCORTICAL visual relay (conscious
      perception via right V1) while the right superior colliculus is
      the MIDBRAIN subcortical visual-motor structure (reflexive
      orienting). Distinct pathways; do not merge.
    - LGN vs. RETINA: the right retina is the SENSORY ORGAN (a named
      external relay, not a tree node); the right LGN is the first
      THALAMIC RELAY. Different levels of the visual pathway; do not
      merge.

Functional Mode:
    Same as ../../../../left/metathalamus/lateral_geniculate_body/.
    First-order visual relay (the anchor); magnocellular / parvocellular
    / koniocellular parallel channels; retinotopic organization with
    contralateral (left) hemifield representation. No documented
    functional asymmetry between left and right LGN. Do not fabricate
    one.

    CLINICAL FACTS (apply on the right identically, with
    CONTRALATERAL specification):
        * RIGHT LGN LESIONS: produce CONTRALATERAL HOMONYMOUS
          HEMIANOPIA — a RIGHT LGN lesion produces a LEFT homonymous
          hemianopia (loss of the LEFT visual hemifield in both eyes),
          because the right LGN represents the LEFT visual hemifield.
          The LEFT LGN leaf documents the reverse: a LEFT LGN lesion
          produces a RIGHT homonymous hemianopia. The two leaves
          together document the full contralateral pattern with the
          correct direction on each side. This is the fifth
          contralateral-clinical pair in the tree (after the STN, LP,
          pulvinar, and (pending) the LGN pair itself).
        * RIGHT OPTIC NEUROPATHY AND TRANS-SYNAPTIC DEGENERATION: right
          optic nerve or right retinal damage produces trans-synaptic
          degeneration of the right LGN (same clinical correlate as on
          the left).
        * RIGHT THALAMIC STROKE (PCA territory): right PCA territory
          infarcts can involve the right LGN and produce the
          corresponding left homonymous hemianopia, often with other
          PCA-territory deficits.
        * LGN-SPECIFIC SYNDROMES are rare in isolation on the right
          either; the clinical picture is usually part of a broader
          optic nerve, thalamic, or PCA syndrome.

Hormonal Modulation:
    Same as ../../../../left/metathalamus/lateral_geniculate_body/.
    Minimal; cholinergic and monoaminergic arousal modulation of the
    LGN's relay gain; right V1 corticothalamic feedback modulates the
    right LGN's gain. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/metathalamus/lateral_geniculate_body/.
    Reads short_term (visual sensory buffer). Writes nothing directly
    (sensory relay, not memory structure). The thinnest memory
    interface of any thalamic nucleus; do not pad.

Model Integration (Gemma-4-E2B):
    No right LGN fragment. The LGN is a first-order visual relay; the
    model prompt does not need an LGN block. The visual cortical state
    is carried by right V1 and the right visual association areas. Same
    deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Retinogeniculostriate pathway (the anchor):
    - ← right retina (via the right optic tract; the ipsilateral
      temporal retina and the contralateral nasal retina both project
      to the right LGN; the retina is NOT a tree node — document as a
      named external relay).
    - → telencephalon/cerebral_hemispheres/right/cortex/occipital/
      primary_visual_cortex (right V1; via the right optic radiation /
      geniculocalcarine tract; right-side).
    - ← telencephalon/cerebral_hemispheres/right/cortex/occipital/
      primary_visual_cortex (right V1 → right LGN; corticothalamic
      feedback; right-side).

    Subcortical visual-motor pathways (distinction, not signaling
    from LGN):
    - ↔ midbrain/.../superior_colliculus (distinct right retinal
      targets; the right superior colliculus is the subcortical
      visual-motor structure; distinct pathways; do not merge; the
      superior colliculus is midline-adjacent — verify).

    Intra-metathalamus:
    - ↔ ../medial_geniculate_body/ (right MGN; anatomically adjacent
      within the right metathalamus; different modalities; distinct
      nuclei; do not merge; the LGN-vs-MGN trap).

    Cross-group:
    - ↔ ../../lateral_nuclear_group/pulvinar/ (right pulvinar;
      adjacent right thalamic visual relays; LGN = first-order;
      pulvinar = higher-order; distinct relay types; do not merge; the
      canonical first-order-vs-higher-order trap).

    - ↔ ../../../../left/metathalamus/lateral_geniculate_body/
      (hemisphere counterpart; no functional asymmetry assumed; but
      see the CONTRALATERAL clinical fact — left and right LGN lesions
      produce opposite-side hemianopias, which is a real directional
      fact, not a functional asymmetry of the nuclei themselves).

Notes:
    - Delta file of ../../../../left/metathalamus/
      lateral_geniculate_body/. Not a full leaf. Do not duplicate.
    - THE LGN PAIR IS NOW COMPLETE: with this file, the LGN is fully
      documented on both hemispheres, with the contralateral
      homonymous hemianopia clinical fact correctly specified for each
      side (left LGN → right hemianopia; right LGN → left hemianopia).
    - THE FOUR TRAPS are reproduced in abbreviated form; the full text
      is in ../../../../left/metathalamus/lateral_geniculate_body/
      and ../../../__init__.py. A contributor entering at the right
      LGN must see them.
    - THE SIX-LAYER STRUCTURE is documented within the left LGN leaf,
      not as child nodes. Do not create magnocellular/, parvocellular/,
      or koniocellular/ as child nodes on the right either.
    - THE CONTRALATERAL CLINICAL FACT IS REVERSED ON THE RIGHT: right
      LGN lesion → LEFT homonymous hemianopia (left LGN lesion →
      RIGHT homonymous hemianopia). This is the ONLY substantive
      content difference between the left and right LGN leaves; the
      contralateral direction is documented explicitly.
    - THE LGN's MEMORY INTERFACE IS THE THINNEST OF ANY THALAMIC
      NUCLEUS (short_term only; writes nothing), same as on the left.
      Do not pad.
    - NO FRAGMENT: same as the whole thalamus. The right LGN is a
      relay, not a state-emitter.
    - The right LGN is NOT the right MGN (auditory), NOT the right
      pulvinar (higher-order visual), NOT the right superior colliculus
      (subcortical visual-motor), NOT the right retina (sensory
      organ). The traps make these distinctions explicit on the right.
    - Midline targets (superior colliculus) are flagged with "verify"
      so Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right retina, right V1,
      right optic radiation, right MGN, and right pulvinar are
      hemisphere-split and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/metathalamus/lateral_geniculate_body/ § Notes
      for the full list.
    - Connects upward to diencephalon/thalamus/right/metathalamus/.
"""