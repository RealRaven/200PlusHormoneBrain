"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.metathalamus.medial_geniculate_body
Anatomical Role:
    The right medial geniculate body (MGN). A three-division,
    tonotopically organized nucleus at the right metathalamus, at the
    caudal pole of the right thalamus, medial to the right LGN and
    lateral to the right pulvinar. Same FIRST-ORDER AUDITORY RELAY role
    as the left MGN: the thalamic relay of the right ascending auditory
    pathway (cochlea → brainstem auditory nuclei → right inferior
    colliculus → right brachium of the inferior colliculus → right MGN
    → right acoustic radiation → right A1).

    The three divisions are documented WITHIN this leaf, not as child
    nodes (same convention as the left MGN, the LGN's six layers, the
    habenula's LHb/MHb, the PVN's sub-populations, the pulvinar's three
    subregions, and the MD's three subdivisions):
        - Ventral MGN: the PRIMARY, TONOTOPIC division; the canonical
          FIRST-ORDER auditory relay to right A1.
        - Medial MGN: a MULTISENSORY-ADJACENT higher-order division.
        - Dorsal MGN: a HIGHER-ORDER auditory association division.
    Do not create ventral_mgn/, medial_mgn/, or dorsal_mgn/ as child
    nodes on the right either.

    See ../../../../left/metathalamus/medial_geniculate_body/
    __init__.py for the full anatomical description, the intra-MGN
    first-order/higher-order split framing, the bilateral
    representation framing, and the auditory processing deficit
    clinical anchor.

    Reproduced distinctions (apply equally on the right):

    - MGN vs. LGN (intra-metathalamus trap): the right MGN is
      AUDITORY; the right LGN
      (right/metathalamus/lateral_geniculate_body/) is VISUAL. Both are
      "geniculate bodies"; different modalities; do not merge.

    - MGN vs. HIGHER-ORDER AUDITORY CORTEX (intra-MGN
      first-order-vs-higher-order trap): the VENTRAL MGN is the
      canonical first-order auditory relay (tonotopic; right A1
      target); the MEDIAL and DORSAL MGN divisions are higher-order
      auditory association. Do not treat all right MGN output as
      "primary auditory."

    - MGN vs. INFERIOR COLLICULUS (midbrain-vs-thalamic trap): the
      right inferior colliculus is the MIDBRAIN auditory relay
      (ascending auditory input → right MGN); the right MGN is the
      THALAMIC auditory relay (→ right A1). Different levels; do not
      merge.

    - MGN vs. COCHLEAR NUCLEI and SUPERIOR OLIVE (brainstem-vs-
      thalamic trap): the right cochlear nuclei and superior olive are
      BRAINSTEM auditory nuclei; the right MGN is the first THALAMIC
      relay. Do not confuse brainstem auditory processing with
      thalamic auditory relay.

    - MGN vs. PULVINAR (cross-modal association trap): the right MGN
      is the AUDITORY relay (primarily first-order; medial/dorsal
      divisions higher-order); the right pulvinar
      (right/lateral_nuclear_group/pulvinar/) is the VISUAL and
      MULTISENSORY association relay (higher-order). Different
      modalities; different relay orders; do not merge.

Functional Mode:
    Same as ../../../../left/metathalamus/medial_geniculate_body/.
    First-order auditory relay (ventral MGN; the anchor); higher-order
    auditory association (medial and dorsal MGN; secondary roles);
    bilateral representation (each MGN receives input from both ears
    via the bilateral ascending auditory pathway). No documented
    functional asymmetry between left and right MGN. Do not fabricate
    one.

    CLINICAL FACTS (apply on the right identically; with the
    BILATERAL-REPRESENTATION caveat):
        * RIGHT MGN LESIONS: produce AUDITORY PROCESSING DEFICITS —
          typically SUBTLE because the ascending auditory pathway is
          BILATERAL above the cochlear nuclei. Unilateral right MGN
          lesions may produce:
            - Mild difficulty with right-side sound localization
              (using interaural time and level differences).
            - Subtle deficits in complex sound processing
              (speech-in-noise; pattern recognition).
            - Generally NO complete unilateral deafness in the left
              ear.
        * MGN LESIONS ARE RARE IN ISOLATION: the right MGN is affected
          mainly by right thalamic stroke (right PCA territory),
          infiltrative disease, or surgical injury.
        * AUDITORY PROCESSING DISORDER (APD) is a related but distinct
          clinical entity (broader than MGN-specific syndromes); do not
          conflate APD with a right-MGN-specific syndrome.
        * The right MGN's clinical anchor is therefore the AUDITORY
          PROCESSING DEFICITS (subtle; rare in isolation) — same subtle
          anchor as the left MGN, contrasted with the right LGN's
          strong contralateral hemianopia.

Hormonal Modulation:
    Same as ../../../../left/metathalamus/medial_geniculate_body/.
    Minimal; cholinergic and monoaminergic arousal modulation of the
    MGN's relay gain; right auditory cortex corticothalamic feedback
    modulates the right MGN's gain. Not a principal target of the 12
    endocrine axes.

Memory Interfaces:
    Same as ../../../../left/metathalamus/medial_geniculate_body/.
    Reads short_term (auditory sensory buffer). Writes nothing directly
    (sensory relay, not memory structure). The thinnest memory
    interface of any thalamic nucleus (same as the LGN); do not pad.

Model Integration (Gemma-4-E2B):
    No right MGN fragment. The MGN is a first-order auditory relay; the
    model prompt does not need an MGN block. The auditory cortical
    state is carried by right A1 and the right auditory association
    areas. Same deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Ascending auditory pathway (the anchor):
    - ← midbrain/.../inferior_colliculus (via the right brachium of
      the inferior colliculus; the inferior colliculus is
      midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/temporal/
      primary_auditory_cortex (right A1; via the right acoustic
      radiation; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/temporal/*
      (right secondary auditory and association areas; the right
      MGN's medial and dorsal divisions; right-side).
    - ← telencephalon/cerebral_hemispheres/right/cortex/temporal/*
      (right auditory cortex corticothalamic feedback to right MGN;
      right-side).

    Intra-metathalamus:
    - ↔ ../lateral_geniculate_body/ (right LGN; anatomically adjacent
      within the right metathalamus; different modalities; distinct
      nuclei; do not merge; the MGN-vs-LGN trap).

    Cross-group:
    - ↔ ../../lateral_nuclear_group/pulvinar/ (right pulvinar; visual
      and multisensory association; distinct modality and relay order;
      do not merge).

    - ↔ ../../../../left/metathalamus/medial_geniculate_body/
      (hemisphere counterpart; no functional asymmetry assumed; both
      MGNs share the bilateral-representation feature — unilateral
      lesions produce subtle auditory deficits on either side).

Notes:
    - Delta file of ../../../../left/metathalamus/medial_geniculate_body/.
      Not a full leaf. Do not duplicate.
    - THE MGN PAIR IS NOW COMPLETE: with this file, the MGN is fully
      documented on both hemispheres, with the auditory processing
      deficit clinical anchor and the intra-MGN first-order/higher-order
      split preserved across the pair.
    - THE METATHALAMUS IS NOW COMPLETE — BOTH HEMISPHERES: with this
      file, the entire metathalamus group is fully documented:
        * Container pair (left group container + right group-container
          delta).
        * LGN pair (left leaf + right delta).
        * MGN pair (left leaf + right delta; this file).
      6 files, all complete.
    - THE INTRA-MGN FIRST-ORDER/HIGHER-ORDER SPLIT is reproduced:
      ventral MGN = first-order (tonotopic; A1); medial and dorsal MGN
      = higher-order association. Do not flatten the MGN into a single
      "first-order" role on the right either.
    - ALL FOUR TRAPS are reproduced in abbreviated form; the full text
      is in ../../../../left/metathalamus/medial_geniculate_body/ and
      ../../../__init__.py.
    - THE BILATERAL-REPRESENTATION FEATURE is preserved: each right MGN
      receives input from both ears via the bilateral ascending
      auditory pathway. Unilateral right MGN lesions produce subtle
      auditory deficits (not unilateral deafness). Same on the left.
    - THE CLINICAL ANCHOR IS SUBTLE (same as on the left): auditory
      processing deficits; rare in isolation; APD distinction. Do not
      overclaim an LGN-like strong clinical anchor.
    - NO FRAGMENT: same as the whole thalamus. The right MGN is a
      relay, not a state-emitter.
    - The right MGN is NOT the right LGN (visual), NOT the right
      inferior colliculus (midbrain), NOT the right cochlear nuclei or
      superior olive (brainstem), NOT the right pulvinar (visual/
      multisensory association). The traps make these distinctions
      explicit on the right.
    - Midline targets (inferior colliculus) are flagged with "verify"
      so Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right A1, right secondary
      auditory areas, right auditory cortex corticothalamic feedback,
      right LGN, and right pulvinar are hemisphere-split and require
      right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/metathalamus/medial_geniculate_body/ § Notes
      for the full list.
    - Connects upward to diencephalon/thalamus/right/metathalamus/.
"""