"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.metathalamus.lateral_geniculate_body
Anatomical Role:
    The left lateral geniculate body (LGN; also called the lateral
    geniculate nucleus). A six-layered, retinotopically organized
    nucleus at the left metathalamus, situated at the caudal pole of
    the left thalamus. It is the FIRST-ORDER VISUAL RELAY of the left
    hemisphere: the thalamic relay of the retinogeniculostriate visual
    pathway (retina → optic chiasm → optic tract → LGN → optic
    radiation → V1).

    The LGN's six layers (documented WITHIN this leaf, not as child
    nodes):
        - Magnocellular layers (1 and 2; ventral): large cells;
          process motion, low-contrast, and high-temporal-frequency
          information. The magnocellular pathway projects to V1's
          layer 4Cα and then to the dorsal ("where/how") visual
          stream (V5/MT, posterior parietal).
        - Parvocellular layers (3, 4, 5, and 6; dorsal): small cells;
          process color (red-green) and fine spatial detail. The
          parvocellular pathway projects to V1's layer 4Cβ and then
          to the ventral ("what") visual stream (V4, IT).
        - Koniocellular layers (between the magno and parvo layers):
          small, scattered cells; process blue-yellow color and some
          motion. The koniocellular pathway projects to V1's layer 2/3
          (cytochrome oxidase blobs) and to extrastriate areas.
    Same convention as the habenula's LHb/MHb, the PVN's
    sub-populations, the pulvinar's three subregions, and the MD's
    three subdivisions: the LGN's layers are documented within this
    leaf, not as tree children. Do not create magnocellular/,
    parvocellular/, or koniocellular/ as child nodes.

    Each LGN receives retinal input from BOTH eyes: the ipsilateral
    temporal retina and the contralateral nasal retina (crossed at
    the optic chiasm). The LGN layers alternate eye input (layers
    1, 4, 6 receive the contralateral eye; layers 2, 3, 5 receive the
    ipsilateral eye in primates), so each LGN represents the
    CONTRALATERAL visual hemifield in a retinotopic map. The LGN is
    therefore the first relay in the visual pathway where the
    contralateral hemifield representation is established.

    DISTINCTIONS (critical):

    - LGN vs. MGN (intra-metathalamus trap; reproduced from the
      metathalamus container): both are "geniculate bodies," both are
      in the metathalamus, both are first-order sensory relays. But
      the LGN is VISUAL (retina → LGN → V1) and the MGN is AUDITORY
      (cochlea → inferior colliculus → MGN → A1). Different
      modalities; different drivers; different cortical targets; do
      not merge.

    - LGN vs. PULVINAR (the canonical cross-group
      first-order-vs-higher-order trap; the pulvinar leaf and the
      metathalamus container are both canonical declarations; this
      leaf enforces it from the LGN side): the LGN is the FIRST-ORDER
      visual relay (retinal driver; V1 target); the pulvinar is the
      HIGHER-ORDER visual association relay (cortical layer 5 driver;
      V2–V5/MT/IT target). Both are thalamic visual relays, but of
      different ORDERS. Do not merge; do not treat them as
      interchangeable "visual thalamus."

    - LGN vs. SUPERIOR COLLICULUS (the subcortical-visual trap): the
      LGN is the THALAMIC-cortical visual relay (retina → LGN → V1;
      the geniculostriate pathway); the superior colliculus is the
      MIDBRAIN subcortical visual-motor structure (retina →
      superior colliculus → pulvinar/MT; the tectopulvinar pathway;
      orienting and saccades). Both receive retinal input, but through
      DIFFERENT pathways serving DIFFERENT functions (conscious
      visual perception vs. reflexive orienting). Do not merge.

    - LGN vs. RETINA (the "where does the relay start" trap): the
      retina is the SENSORY ORGAN (photoreceptors, retinal ganglion
      cells); the LGN is the first THALAMIC RELAY. The retina is NOT
      a tree node; document it as a named external relay. Do not
      confuse "retinal processing" (phototransduction, ganglion cell
      receptive fields) with "LGN processing" (first thalamic relay
      of the retinal output).

Functional Mode:
    - First-order visual relay (the LGN's anchor role):
        * The LGN receives retinal ganglion cell axons via the optic
          tract (from the contralateral nasal retina and the
          ipsilateral temporal retina), preserves the retinotopic
          map, and projects to V1 via the optic radiation
          (geniculocalcarine tract).
        * The LGN is the SOLE thalamic relay to V1: all visually
          guided behavior that depends on V1 passes through the LGN
          (except for the subcortical tectopulvinar pathway, which
          reaches MT via the superior colliculus and pulvinar).
        * The LGN is a RELAY, not a passive wire: it performs
          thalamic-level processing including gain control, temporal
          filtering, and corticothalamic feedback modulation (V1
          projects back to the LGN and modulates its relay gain).
    - Magnocellular, parvocellular, and koniocellular pathways (the
      LGN's parallel-channel architecture):
        * The magnocellular pathway (layers 1–2) carries motion and
          low-contrast information to V1's 4Cα → dorsal stream (V5/MT
          → posterior parietal). The dorsal stream is the
          "where/how" pathway for motion and spatial vision.
        * The parvocellular pathway (layers 3–6) carries color and
          fine detail to V1's 4Cβ → ventral stream (V4 → IT). The
          ventral stream is the "what" pathway for object recognition.
        * The koniocellular pathway (between layers) carries
          blue-yellow color and some motion to V1's layer 2/3 blobs
          and to extrastriate areas.
    - Retinotopic organization and visual field representation:
        * The LGN maintains the retina's retinotopic map: neighboring
          retinal locations project to neighboring LGN locations.
        * Each LGN represents the CONTRALATERAL visual hemifield
          (because each LGN receives crossed nasal fibers from the
          contralateral eye and uncrossed temporal fibers from the
          ipsilateral eye). The left LGN represents the RIGHT visual
          hemifield; the right LGN represents the LEFT visual
          hemifield.
        * This contralateral representation is the anatomical basis
          of the LGN's clinical anchor (contralateral homonymous
          hemianopia; see clinical fact).
    - The LGN is therefore the THALAMUS'S FIRST-ORDER VISUAL RELAY: it
      is the anatomical substrate of conscious visual perception via
      V1, and the pattern exemplar for all first-order sensory relays
      in the thalamus (VPL/VPM will follow).

    - CLINICAL FACTS (the LGN's defining clinical anchor;
      contralateral):
        * CONTRALATERAL HOMONYMOUS HEMIANOPIA: a left LGN lesion
          produces a RIGHT homonymous hemianopia (loss of the right
          visual hemifield in both eyes), because the left LGN
          represents the right hemifield. This is the LGN's defining
          clinical anchor and the anatomical proof that each LGN
          carries the contralateral visual hemifield.
        * OPTIC NEUROPATHY AND TRANS-SYNAPTIC DEGENERATION: when the
          left optic nerve or left retina is damaged, the left LGN
          undergoes trans-synaptic degeneration (the LGN's
          retinal-target neurons lose their input and atrophy). This
          is an important clinical correlate of optic nerve disease
          and glaucoma.
        * THALAMIC STROKE: the LGN is supplied by the posterior
          cerebral artery (PCA) territory; PCA territory infarcts can
          involve the LGN and produce the corresponding hemianopia,
          often in conjunction with other PCA-territory deficits
          (e.g., hemianesthesia from VPL involvement, or memory
          deficits from hippocampal involvement).
        * LGN-SPECIFIC SYNDROMES are rare in isolation because the
          LGN is rarely affected alone; the clinical picture is
          usually part of a broader optic nerve, thalamic, or PCA
          syndrome. The LGN's clinical anchor is the contralateral
          homonymous hemianopia (established); the other facts are
          additional clinical context.

Hormonal Modulation (minimal; the LGN is a first-order sensory relay):
    - The LGN is NOT a neuroendocrine structure.
    - Modulators: cholinergic (brainstem and basal forebrain) and
      monoaminergic (brainstem) arousal inputs modulate LGN relay
      gain; V1 corticothalamic feedback modulates LGN gain
      (attention-dependent). Document as arousal and attentional
      modulation, not endocrine modulators.
    - The LGN is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * short_term: the current visual sensory buffer being
          relayed. The LGN is a sensory relay, not a memory
          structure; the visual memory itself is stored in the
          visual cortex.
    - Writes: none directly. The LGN relays visual signals to V1;
      the visual perceptual memory is stored in V1 and downstream
      visual areas.
    - The LGN has the THINNEST memory interface of any thalamic
      nucleus: it reads only short_term (sensory buffer) and writes
      nothing. Sensory relays do not have higher memory interfaces.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No LGN fragment. The LGN is a first-order visual relay; the
      model prompt does not need an LGN block because the visual
      signals it relays are already represented in the upstream
      (retina, optic tract) and downstream (V1, visual cortex)
      fragments. The visual cortical state is carried by V1 and the
      visual association areas.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The LGN's clinical facts (contralateral homonymous hemianopia;
      trans-synaptic degeneration; PCA stroke) are documented for
      completeness, but are not prompt fields.

Reciprocal Connections (left-side; the right side is in
../../../../right/metathalamus/lateral_geniculate_body/):

    Retinogeniculostriate pathway (the anchor):
    - ← left retina (via the left optic tract; the ipsilateral
      temporal retina and the contralateral nasal retina both project
      to the left LGN; the retina is NOT a tree node — document as a
      named external relay).
    - → telencephalon/cerebral_hemispheres/left/cortex/occipital/
      primary_visual_cortex (left V1; via the left optic radiation /
      geniculocalcarine tract; the LGN's principal cortical output).
    - ← telencephalon/cerebral_hemispheres/left/cortex/occipital/
      primary_visual_cortex (V1 → LGN; corticothalamic feedback; the
      visual cortex modulates LGN relay gain; the corticothalamic
      edge that makes the LGN a modulator as well as a relay).

    Subcortical visual-motor pathways (distinction, not signaling
    from LGN):
    - ↔ midbrain/.../superior_colliculus (the LGN and superior
      colliculus are two distinct retinal targets; the superior
      colliculus is the subcortical visual-motor structure; the LGN
      is the thalamocortical visual relay; distinct pathways; do not
      merge; the superior colliculus is midline-adjacent — verify).

    Intra-metathalamus:
    - ↔ ../medial_geniculate_body/ (left MGN; anatomically adjacent
      within the left metathalamus; different modalities; distinct
      nuclei; do not merge; the LGN-vs-MGN trap).

    Cross-group:
    - ↔ ../../lateral_nuclear_group/pulvinar/ (left pulvinar; adjacent
      left thalamic visual relays; LGN = first-order; pulvinar =
      higher-order; distinct relay types; do not merge; the
      canonical first-order-vs-higher-order trap).

Notes:
    - Tier 1 full leaf (left). The CLEANEST first-order sensory
      relay in the entire thalamus — the pattern exemplar for
      first-order sensory relay documentation (the VPL/VPM in the
      ventral group will follow this shape).
    - THE LGN's SIX-LAYER STRUCTURE (magnocellular, parvocellular,
      koniocellular) is documented WITHIN this leaf, not as child
      nodes. Same convention as the habenula's LHb/MHb, the PVN's
      sub-populations, the pulvinar's three subregions, and the MD's
      three subdivisions. Do not create magnocellular/,
      parvocellular/, or koniocellular/ as child nodes.
    - THE LGN vs. MGN TRAP is reproduced in full: both are geniculate
      bodies; different modalities; do not merge.
    - THE LGN vs. PULVINAR TRAP is the canonical
      first-order-vs-higher-order trap; reproduced in full; the LGN
      leaf enforces it from the LGN side (the pulvinar leaf and the
      metathalamus container enforce it from their sides).
    - THE LGN vs. SUPERIOR COLLICULUS TRAP is a NEW trap declared in
      this leaf: both receive retinal input, but the LGN is the
      thalamocortical visual relay (conscious perception via V1) while
      the superior colliculus is the subcortical visual-motor structure
      (reflexive orienting). Distinct pathways; do not merge.
    - THE LGN vs. RETINA TRAP is a NEW trap declared in this leaf: the
      retina is the SENSORY ORGAN; the LGN is the first THALAMIC RELAY.
      The retina is a named external relay, not a tree node.
    - THE CONTRALATERAL CLINICAL FACT: a LEFT LGN lesion produces a
      RIGHT homonymous hemianopia (the left LGN represents the right
      visual hemifield). The right LGN leaf will document the reverse:
      a RIGHT LGN lesion produces a LEFT homonymous hemianopia. The
      contralateral direction is stated explicitly; the right delta
      will state the reverse explicitly. This is the same pattern as
      the LP pair, the pulvinar pair, and the STN pair.
    - THE LGN's MEMORY INTERFACE IS THE THINNEST OF ANY THALAMIC
      NUCLEUS: reads short_term only; writes nothing. Sensory relays
      do not have higher memory interfaces. This is the correct
      epistemic stance; do not pad with interfaces the literature
      does not support.
    - NO FRAGMENT: same as the whole thalamus. The LGN is a relay,
      not a state-emitter.
    - The LGN is NOT the MGN (auditory first-order relay), NOT the
      pulvinar (higher-order visual association), NOT the superior
      colliculus (subcortical visual-motor), NOT the retina (sensory
      organ). The traps make these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines); memory/
      stores/ (short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/metathalamus/.
"""