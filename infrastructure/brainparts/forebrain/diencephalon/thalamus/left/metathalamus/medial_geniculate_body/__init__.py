"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.metathalamus.medial_geniculate_body
Anatomical Role:
    The left medial geniculate body (MGN; also called the medial
    geniculate nucleus). A three-division, tonotopically organized
    nucleus at the left metathalamus, situated at the caudal pole of
    the left thalamus, medial to the left LGN and lateral to the left
    pulvinar. It is the FIRST-ORDER AUDITORY RELAY of the left
    hemisphere: the thalamic relay of the ascending auditory pathway
    (cochlea → brainstem auditory nuclei → left inferior colliculus →
    left MGN → left acoustic radiation → left A1).

    The MGN's three divisions (documented WITHIN this leaf, not as
    child nodes):
        - Ventral MGN (MGNv): the PRIMARY, TONOTOPIC division.
          Receives the principal ascending auditory input from the
          inferior colliculus (via the brachium of the inferior
          colliculus); preserves a tonotopic (frequency) map; projects
          to A1 (primary auditory cortex). This is the canonical
          FIRST-ORDER auditory relay.
        - Medial MGN (MGNm): a MULTISENSORY-ADJACENT division.
          Receives input from the inferior colliculus's external
          cortex and from auditory-adjacent structures; projects to
          secondary auditory areas and to auditory-adjacent
          association regions. Contributes to higher-order auditory
          and multisensory association (auditory-visual integration,
          orientation to sound).
        - Dorsal MGN (MGNd): a HIGHER-ORDER AUDITORY ASSOCIATION
          division. Receives more complex auditory inputs (including
          some corticothalamic feedback); projects to secondary
          auditory and association cortical areas. Contributes to
          higher-order auditory processing (pattern recognition,
          auditory memory).
    Same convention as the habenula's LHb/MHb, the PVN's
    sub-populations, the pulvinar's three subregions, the MD's three
    subdivisions, and the LGN's three layer-types: the MGN divisions
    are documented within this leaf, not as tree children. Do not
    create ventral_mgn/, medial_mgn/, or dorsal_mgn/ as child nodes.

    IMPORTANT: the MGN's VENTRAL division is the FIRST-ORDER relay
    (tonotopic; A1 target). The MEDIAL and DORSAL divisions are
    HIGHER-ORDER ASSOCIATION divisions (secondary auditory areas;
    auditory association). Do not draft the entire MGN as "first-order
    auditory" — only the ventral division is the canonical first-order
    relay; the medial and dorsal divisions are higher-order
    association.

    DISTINCTIONS (critical):

    - MGN vs. LGN (intra-metathalamus trap; reproduced from the
      metathalamus container): both are "geniculate bodies," both are
      in the metathalamus, both are first-order sensory relays (at
      least for the ventral MGN division). But the MGN is AUDITORY
      (cochlea → inferior colliculus → MGN → A1) and the LGN is
      VISUAL (retina → LGN → V1). Different modalities; different
      drivers; different cortical targets; do not merge.

    - MGN vs. HIGHER-ORDER AUDITORY CORTEX (the intra-MGN
      first-order-vs-higher-order trap): the VENTRAL MGN is the
      canonical first-order auditory relay (tonotopic; A1 target); the
      MEDIAL and DORSAL MGN divisions are higher-order auditory
      association (secondary auditory areas; auditory association).
      Do not treat all MGN output as "primary auditory"; the ventral
      MGN is the primary; the medial and dorsal divisions contribute
      higher-order auditory and multisensory association.

    - MGN vs. INFERIOR COLLICULUS (the midbrain-vs-thalamic auditory
      relay trap): the inferior colliculus is the MIDBRAIN auditory
      relay (receives ascending auditory input from the cochlear
      nuclei and superior olive; projects to the MGN via the brachium
      of the inferior colliculus); the MGN is the THALAMIC auditory
      relay (projects to A1). Both are auditory relays in the
      ascending pathway, but at different levels (midbrain vs.
      thalamus). Do not merge.

    - MGN vs. SUPERIOR OLIVE and COCHLEAR NUCLEI (the "where does the
      relay start" trap): the cochlear nuclei and superior olive are
      BRAINSTEM auditory nuclei (first-order and second-order auditory
      processing); the MGN is the first THALAMIC relay. Do not confuse
      brainstem auditory processing with thalamic auditory relay.

    - MGN vs. PULVINAR (the cross-modal association trap): the MGN is
      the AUDITORY relay (first-order, primarily); the pulvinar is the
      VISUAL and MULTISENSORY association relay (higher-order). Both
      are thalamic relays involved in sensory processing, but for
      different modalities and at different relay orders. Do not
      merge.

Functional Mode:
    - First-order auditory relay (ventral MGN; the anchor role):
        * The MGN receives ascending auditory input from the left
          inferior colliculus (via the left brachium of the inferior
          colliculus) and projects to the left primary auditory
          cortex (A1) via the left acoustic radiation.
        * The MGN is the thalamic relay of the ascending auditory
          pathway: all auditory information reaching A1 passes through
          the MGN (the auditory pathway is more complex than the
          visual pathway — there are multiple brainstem auditory
          nuclei — but the MGN is the obligatory thalamic relay to
          A1).
        * The MGN preserves a tonotopic (frequency) map: neighboring
          frequencies project to neighboring MGN locations. The
          tonotopic map is the auditory counterpart to the LGN's
          retinotopic map.
    - Higher-order auditory association (medial and dorsal MGN; the
      secondary roles):
        * The medial MGN contributes to multisensory-adjacent auditory
          processing (auditory-visual integration, orientation to
          sound) via its projections to secondary auditory and
          association cortical areas.
        * The dorsal MGN contributes to higher-order auditory
          processing (pattern recognition, auditory memory) via its
          projections to secondary auditory and association cortical
          areas.
        * The medial and dorsal MGN divisions are the MGN's
          higher-order association components; they are distinct from
          the ventral MGN's first-order role. Document the distinction;
          do not flatten the MGN into a single "first-order" role.
    - Bilateral representation (the MGN's distinctive feature):
        * Unlike the visual pathway (where each LGN represents the
          contralateral hemifield), the auditory pathway is BILATERAL
          above the cochlear nuclei: each MGN receives input from
          both ears (via the superior olive and the ascending auditory
          brainstem nuclei), with some ipsilateral dominance. This
          bilateral representation is why unilateral MGN lesions
          produce SUBTLE auditory deficits (rather than complete
          deafness in one ear).
    - The MGN is therefore the THALAMUS'S FIRST-ORDER AUDITORY RELAY
      (with a higher-order association component in its medial and
      dorsal divisions). It is the auditory counterpart to the LGN,
      but with a distinctive bilateral representation and a
      three-division first-order/higher-order split.

    - CLINICAL FACTS (the MGN's clinical anchor; bilateral):
        * AUDITORY PROCESSING DEFICITS from MGN lesions: typically
          SUBTLE because the ascending auditory pathway is BILATERAL
          above the cochlear nuclei. Unilateral MGN lesions may
          produce:
            - Mild difficulty with sound localization (using
              interaural time and level differences).
            - Subtle deficits in complex sound processing (pattern
              recognition, speech-in-noise).
            - Generally NO complete unilateral deafness (contrast with
              the LGN, where unilateral lesions produce complete
              contralateral hemianopia).
        * MGN LESIONS ARE RARE IN ISOLATION: the MGN is affected
          mainly by thalamic stroke (the MGN is supplied by the
          posterior cerebral artery territory, like the LGN),
          infiltrative disease, or surgical injury. MGN-specific
          syndromes are not well described.
        * AUDITORY PROCESSING DISORDER (APD) is a related but distinct
          clinical entity: APD is a deficit in central auditory
          processing that can involve the MGN and other auditory
          pathway structures, but it is not an MGN-specific syndrome.
          Document the distinction; do not conflate APD with MGN
          lesion syndromes.
        * The MGN's clinical anchor is therefore the AUDITORY
          PROCESSING DEFICITS (typically subtle; rare in isolation) —
          a subtler clinical anchor than the LGN's contralateral
          homonymous hemianopia. This reflects the MGN's bilateral
          representation and the auditory pathway's redundancy.

Hormonal Modulation (minimal; the MGN is a first-order auditory
relay):
    - The MGN is NOT a neuroendocrine structure.
    - Modulators: cholinergic (brainstem and basal forebrain) and
      monoaminergic (brainstem) arousal inputs modulate MGN relay
      gain; A1 corticothalamic feedback modulates MGN gain
      (attention-dependent). Document as arousal and attentional
      modulation, not endocrine modulators.
    - The MGN is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * short_term: the current auditory sensory buffer being
          relayed. The MGN is a sensory relay, not a memory
          structure; the auditory perceptual memory itself is stored
          in the auditory cortex and association areas.
    - Writes: none directly. The MGN relays auditory signals to A1
      and secondary auditory areas; the auditory perceptual memory is
      stored in the cortex.
    - The MGN has the THINNEST memory interface of any thalamic
      nucleus (same as the LGN): reads only short_term (sensory
      buffer); writes nothing.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No MGN fragment. The MGN is a first-order auditory relay; the
      model prompt does not need an MGN block because the auditory
      signals it relays are already represented in the upstream
      (inferior colliculus) and downstream (A1, auditory cortex)
      fragments. The auditory cortical state is carried by A1 and the
      auditory association areas.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The MGN's clinical facts (auditory processing deficits; rare in
      isolation) are documented for completeness, but are not prompt
      fields.

Reciprocal Connections (left-side; the right side is in
../../../../right/metathalamus/medial_geniculate_body/):

    Ascending auditory pathway (the anchor):
    - ← midbrain/.../inferior_colliculus (via the left brachium of
      the inferior colliculus; the left IC → left MGN; the inferior
      colliculus is midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/left/cortex/temporal/
      primary_auditory_cortex (left A1; via the left acoustic
      radiation; the MGN's principal cortical output to primary
      auditory cortex).
    - → telencephalon/cerebral_hemispheres/left/cortex/temporal/*
      (secondary auditory areas; the MGN's medial and dorsal divisions
      project to secondary auditory and association areas; the MGN's
      higher-order auditory output).
    - ← telencephalon/cerebral_hemispheres/left/cortex/temporal/*
      (corticothalamic feedback from auditory cortex to MGN; the
      auditory cortex modulates MGN relay gain; the corticothalamic
      edge that makes the MGN a modulator as well as a relay).

    Brainstem auditory pathway (distinction, not direct LGN-like
    input):
    - The ascending auditory pathway reaches the MGN via the inferior
      colliculus (which itself receives input from the cochlear nuclei,
      superior olive, and lateral lemniscus). The MGN does NOT receive
      direct cochlear input; the inferior colliculus is the midbrain
      relay between the brainstem and the MGN.

    Intra-metathalamus:
    - ↔ ../lateral_geniculate_body/ (left LGN; anatomically adjacent
      within the left metathalamus; different modalities; distinct
      nuclei; do not merge; the MGN-vs-LGN trap).

    Cross-group:
    - ↔ ../../lateral_nuclear_group/pulvinar/ (left pulvinar; the
      pulvinar is a visual and multisensory association relay; the MGN
      is the auditory first-order relay with a higher-order association
      component in its medial/dorsal divisions; distinct modalities
      and relay orders; do not merge).

Notes:
    - Tier 1 full leaf (left). The AUDITORY COUNTERPART to the LGN;
      the second first-order sensory relay in the metathalamus. Its
      leaf is slightly shorter than the LGN's (~85 lines vs. ~95)
      because the MGN's anatomical structure (three divisions) is
      simpler than the LGN's six layers, and the clinical anchor is
      subtler.
    - THE MGN'S THREE DIVISIONS (ventral/medial/dorsal) are documented
      WITHIN this leaf, not as child nodes. Same convention as the
      habenula's LHb/MHb, the PVN's sub-populations, the pulvinar's
      three subregions, the MD's three subdivisions, and the LGN's
      three layer-types. Do not create ventral_mgn/, medial_mgn/, or
      dorsal_mgn/ as child nodes.
    - THE VENTRAL MGN vs. MEDIAL/DORSAL MGN distinction is the
      intra-MGN first-order-vs-higher-order trap: the ventral MGN is
      the canonical first-order auditory relay (tonotopic; A1 target);
      the medial and dorsal MGN are higher-order auditory association
      divisions. Do not flatten the MGN into a single "first-order"
      role.
    - THE MGN vs. LGN TRAP is reproduced in full: both are geniculate
      bodies; different modalities; do not merge.
    - THE MGN vs. INFERIOR COLLICULUS TRAP is a NEW trap declared in
      this leaf: the inferior colliculus is the midbrain auditory relay
      (brainstem → MGN); the MGN is the thalamic auditory relay (→
      A1). Different levels of the auditory pathway; do not merge.
    - THE MGN vs. COCHLEAR NUCLEI/SUPERIOR OLIVE TRAP is a NEW trap:
      the brainstem auditory nuclei are the first-stage auditory
      processing; the MGN is the first thalamic relay. Do not confuse
      brainstem auditory processing with thalamic auditory relay.
    - THE MGN vs. PULVINAR TRAP: cross-modal (auditory vs.
      visual-multisensory); different relay orders; do not merge.
    - THE MGN'S BILATERAL REPRESENTATION is its distinctive feature
      (contrast with the LGN's contralateral hemifield
      representation). This is the anatomical basis of the MGN's
      subtler clinical anchor: unilateral MGN lesions produce
      AUDITORY PROCESSING DEFICITS (typically subtle), NOT unilateral
      deafness. Document this; do not overclaim an LGN-like clinical
      anchor.
    - THE MGN'S CLINICAL ANCHOR IS SUBTLER THAN THE LGN'S: the MGN's
      clinical facts (auditory processing deficits; rare in isolation;
      APD distinction) are documented honestly, without overclaiming.
      This reflects the auditory pathway's redundancy and the MGN's
      bilateral representation.
    - NO FRAGMENT: same as the whole thalamus. The MGN is a relay, not
      a state-emitter.
    - The MGN is NOT the LGN (visual), NOT the inferior colliculus
      (midbrain auditory relay), NOT the cochlear nuclei/superior
      olive (brainstem auditory nuclei), NOT the pulvinar (visual/
      multisensory association). The traps make these distinctions
      explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines); memory/
      stores/ (short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/metathalamus/.
"""