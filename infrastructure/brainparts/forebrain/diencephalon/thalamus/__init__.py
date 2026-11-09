"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus
Anatomical Role:
    The thalamus is the large, egg-shaped gray-matter mass on each side
    of the third ventricle, forming the dorsal part of the diencephalon.
    It is the brain's principal GATEWAY TO THE CORTEX: every ascending
    sensory pathway (except olfaction, which relays via the
    rhinencephalon → amygdala → cortex) synapses in a thalamic relay
    nucleus before reaching its cortical target, and every cortical
    area has a reciprocal thalamo-cortical loop.

    The thalamus is organized into SIX NUCLEAR GROUPS per hemisphere
    (documented as children, not within this container):

        - anterior_nuclear_group/  (part of the Papez circuit;
                                     anterodorsal, anteromedial,
                                     anteroventral). Target of the
                                     mammillothalamic tract; relays to
                                     the cingulate and retrosplenial
                                     cortex.
        - lateral_nuclear_group/   (higher-order association relay;
                                     lateral dorsal, lateral posterior,
                                     pulvinar). Pulvinar is the visual
                                     association relay.
        - medial_nuclear_group/    (limbic/executive/arousal relay;
                                     mediodorsal, intralaminar,
                                     midline, parafascicular,
                                     paratenial, reuniens, rhomboidal,
                                     central lateral, centromedian).
                                     Mediodorsal is the prefrontal
                                     relay.
        - ventral_nuclear_group/   (motor and somatosensory relay;
                                     ventral anterior, ventral lateral,
                                     ventral posterior [VPL and VPM]).
                                     VA/VL → motor cortex; VPL → body
                                     somatosensory cortex; VPM → face
                                     somatosensory cortex.
        - metathalamus/            (sensory relay; lateral geniculate
                                     body, medial geniculate body).
                                     LGN → primary visual cortex;
                                     MGN → primary auditory cortex.
        - reticular_nucleus/       (the thalamic reticular nucleus; the
                                     GABAergic inhibitory shell around
                                     the thalamus). NOT a relay: it
                                     gates the thalamo-cortical loop.

    The thalamus is therefore a HUB OF RELAYS: each nucleus receives its
    input from a specific subcortical or cortical source and projects to
    a specific cortical target. It is a set of relays, not a single
    functional unit.

    THE FIRST-ORDER vs. HIGHER-ORDER DISTINCTION (the organizing
    functional principle):
        - FIRST-ORDER RELAY NUCLEI: receive subcortical driver input
          (from the sensory periphery, the basal ganglia, the
          cerebellum, or the hypothalamus) and relay to a primary
          cortical area. Examples: LGN (vision), MGN (audition), VPL/
          VPM (somatosensation), VA/VL (basal ganglia → motor cortex).
          These are the primary thalamic relays.
        - HIGHER-ORDER RELAY NUCLEI: receive driver input primarily
          from CORTICAL layer 5 and relay back to a higher-order
          cortical area. Examples: pulvinar (visual association),
          mediodorsal (prefrontal), lateral posterior (parietal
          association). These support cortico-thalamo-cortical loops
          for higher cognition.
        - The RETICULAR NUCLEUS: neither first-order nor higher-order
          relay; it is the GABAergic INHIBITORY SHELL that gates the
          thalamo-cortical loop.

    NAMING TRAPS (critical — six confusions apply here; some have been
    flagged elsewhere in the tree already):

    - TRAP 1: THALAMIC PVT vs. HYPOTHALAMIC PVN (already flagged in
      posterior/lateral_area/.../posterior_part_of_lateral_nucleus/
      and tuberal/medial_area/.../arcuate_nucleus/). The THALAMIC
      PARAVENTRICULAR NUCLEUS (PVT) is documented under
      thalamus/left|right/medial_nuclear_group/paraventricular_nucleus/
      (in this tree, in the midline nuclear group — see the note
      below). The HYPOTHALAMIC PARAVENTRICULAR NUCLEUS (PVN) is
      documented under hypothalamus/anterior/medial_area/left|right/
      paraventricular_nucleus/. They are DIFFERENT STRUCTURES with
      confusingly similar names. The thalamic PVT is a limbic/arousal
      relay; the hypothalamic PVN is the CRH/TRH/oxytocin/vasopressin
      hub. Do not merge.

    - TRAP 2: PULVINAR vs. LATERAL POSTERIOR. Both are in the lateral
      nuclear group; both are higher-order association relays. The
      pulvinar is primarily visual association (connected to the
      visual cortex); the lateral posterior nucleus is primarily
      parietal association. Distinct nuclei; do not merge.

    - TRAP 3: VPL vs. VPM (ventral posterior lateral vs. ventral
      posterior medial). Both are in the ventral posterior nucleus;
      VPL relays BODY somatosensation (spinal cord, medial lemniscus,
      spinothalamic) and VPM relays FACE somatosensation
      (trigeminal). Different body maps; distinct nuclei; do not
      merge.

    - TRAP 4: LGN vs. MGN (lateral vs. medial geniculate body). Both
      are in the metathalamus; LGN is VISUAL (→ primary visual
      cortex), MGN is AUDITORY (→ primary auditory cortex). Different
      sensory modalities; distinct nuclei; do not merge.

    - TRAP 5: THALAMIC RETICULAR NUCLEUS vs. MIDBRAIN RETICULAR
      FORMATION. The thalamic reticular nucleus is a thin GABAergic
      shell AROUND the thalamus (a single continuous sheet); the
      midbrain reticular formation is a distributed arousal system in
      the brainstem. Distinct structures; different functions; do not
      merge. The thalamic reticular nucleus is under
      thalamus/left|right/reticular_nucleus/; the midbrain reticular
      formation is under midbrain/.../midbrain_reticular_formation/.

    - TRAP 6: ANTERIOR THALAMIC NUCLEI vs. ANTERIOR HYPOTHALAMIC
      NUCLEUS. Both are "anterior"; both are in the diencephalon.
      The anterior thalamic nuclei (anterodorsal, anteromedial,
      anteroventral) are the Papez circuit relay (hippocampus →
      mammillary bodies → anterior thalamus → cingulate cortex). The
      anterior hypothalamic nucleus is the parasympathetic/
      thermoregulatory hub. Different structures; do not merge.

    - ADDITIONAL SUB-TRAPS within the medial nuclear group: the
      intralaminar nuclear group (centrolateral, parafascicular,
      centromedian) vs. the midline nuclear group (paratenial,
      paraventricular [PVT], reuniens, rhomboidal) are DISTINCT
      groups with distinct functions. The intralaminar group is
      arousal/attention; the midline group is limbic/visceral.
      Distinct; do not merge.

Functional Mode:
    - Sensory relay (first-order; the thalamus's primary role):
        * Vision: retina → optic nerve → optic chiasm → optic tract →
          LGN → primary visual cortex (V1).
        * Audition: cochlea → brainstem auditory nuclei → inferior
          colliculus → MGN → primary auditory cortex (A1).
        * Somatosensation (body): dorsal column/medial lemniscus and
          spinothalamic → VPL → primary somatosensory cortex (S1).
        * Somatosensation (face): trigeminothalamic → VPM → S1.
        * Taste: nucleus of the solitary tract → parabrachial →
          VPM (parvicellular part) → gustatory cortex (anterior
          insula).
        * Vestibular: vestibular nuclei → VPM (or VPL in some
          species) → vestibular cortex.
        * (Olfaction does NOT relay through the thalamus; it projects
          directly to the piriform cortex and amygdala.)
    - Motor relay (first-order):
        * Basal ganglia: GPi/SNr → VA/VL → motor cortex (M1, premotor,
          supplementary motor). The thalamus's motor relay is the
          final common pathway of the basal ganglia's influence on
          the cortex.
        * Cerebellum: cerebellar dentate nucleus → VL (especially
          VLc/VLps) → motor cortex. The thalamus's cerebellar relay
          is the final common pathway of the cerebellum's influence
          on the cortex.
    - Limbic relay (first-order and higher-order):
        * Papez circuit: hippocampus → fornix → mammillary bodies →
          mammillothalamic tract → anterior thalamic nuclei (AV, AM,
          AD) → cingulate cortex and retrosplenial cortex. The
          anterior thalamus is the Papez circuit's thalamic relay.
        * Prefrontal/executive: amygdala, substantia innominata,
          ventral pallidum, and prefrontal cortex → mediodorsal
          nucleus (MD) → prefrontal cortex. MD is the prefrontal
          relay.
        * Visceral/limbic: hypothalamic and brainstem inputs →
          midline nuclei (PVT, reuniens, rhomboid) → hippocampal
          formation, amygdala, nucleus accumbens, prefrontal cortex.
    - Higher-order association relay (higher-order):
        * Visual association: pulvinar → visual association cortex
          (V2–V5, MT, IT). The pulvinar is the visual association
          relay.
        * Parietal association: lateral posterior nucleus →
          posterior parietal cortex. The lateral posterior is the
          parietal association relay.
        * Prefrontal association: MD → prefrontal cortex. MD is the
          higher-order executive relay.
    - Arousal and attention (intralaminar and reticular):
        * Intralaminar nuclei (centrolateral, parafascicular,
          centromedian): receive brainstem reticular and basal ganglia
          inputs; project diffusely to the cortex; contribute to
          arousal, attention, and the cortical activation that
          underlies consciousness.
        * Thalamic reticular nucleus: the GABAergic shell around the
          thalamus; receives collaterals from thalamo-cortical and
          cortico-thalamic axons; INHIBITS the thalamic relay nuclei;
          gates attention and state (sleep-wake). The reticular
          nucleus is the "gatekeeper" of the thalamic gateway.
    - The thalamus is therefore the CORTICAL GATEWAY and the
      CORTICAL-ACTIVATION HUB: it relays every sensory modality
      (except olfaction), relays the basal ganglia and cerebellar
      motor commands, relays the limbic and executive circuits, and
      gates the whole system via the reticular nucleus.

Hormonal Modulation (thalamus-wide summary; per-nucleus wiring in the
child leaves):
    - The thalamus is NOT a neuroendocrine structure: it is not a
      principal source or target of the 12 endocrine axes.
    - Modulators are neuromodulators from the brainstem:
        * Norepinephrine (from the LC): diffuse ascending arousal
          modulation of the thalamus.
        * Serotonin (from the raphe): diffuse ascending modulation.
        * Acetylcholine (from the LDT/PPN and the basal forebrain):
          diffuse ascending modulation.
        * Dopamine (from the VTA): modulates the limbic and motor
          thalamic nuclei (MD, VA/VL).
        * Histamine (from the TMN): diffuse ascending modulation.
        * Orexin (from the LHA): diffuse arousal modulation.
    - These are NOT endocrine hormones; they are ascending
      neuromodulators of the arousal system. The thalamus is their
      target, not a source.
    - Direction summary: norepinephrine, serotonin, acetylcholine,
      dopamine, histamine, and orexin all modulate thalamic activity
      (arousal and attentional gating). These are the actionable
      directions.
    - The thalamus is NOT a principal target of the 12 endocrine axes.
      Do not pad the section with CRH, cortisol, etc.

Memory Interfaces (thalamus-wide summary; per-nucleus wiring in the
child leaves):
    - The thalamus is NOT a memory hub: it relays memory signals but
      does not store them.
    - Some thalamic nuclei READ memory-adjacent stores:
        * Anterior thalamic nuclei READ episodic (the Papez circuit's
          hippocampal episodic signal is relayed through the mammillary
          bodies to the anterior thalamus, which then relays it to the
          cingulate cortex — where episodic re-encoding happens).
        * MD READS episodic, semantic, and reinforcement_value_based_
          learning (the prefrontal cortex is the primary site of
          executive memory use; MD relays the prefrontal loops that
          use these stores).
        * Intralaminar nuclei READ short_term (the arousal state that
          gates attention).
    - The thalamus WRITES NO memory directly. Same discipline as the
      STN and zona incerta: motor/arousal relay does not store
      content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No thalamus-wide fragment. The thalamus is a RELAY, not a
      state-emitter: it does not generate a state that the language
      model should be conditioned on. The relevant state fragments
      (arousal, attention, sensory, motor, limbic) are emitted by the
      upstream sources (LC, raphe, LDT/PPN, VTA, TMN, orexin, sensory
      organs, basal ganglia, cerebellum, amygdala) and by the cortical
      targets (PFC, visual cortex, motor cortex).
    - The thalamic reticular nucleus's gating role is a FUNCTIONAL
      fact (it gates attention and state), not a state fragment; the
      upstream arousal fragments carry the model-relevant state.
    - AGGREGATION RULES: no fragments are emitted from this container
      or from any thalamic child leaf. This is a deliberate absence,
      not an oversight.
    - The thalamus's clinical context (thalamic stroke syndromes;
      thalamic pain; central pain; DBS targets like the VIM for
      tremor) is documented in the leaves for completeness, but is
      not a prompt field.

Children (per-hemisphere structure; the container splits into left/
and right/ first, then the six nuclear groups within each):
    - left/    ★ Hemisphere container. Names the six nuclear groups
                 for the left hemisphere; defers functional content
                 to them.
        ├── anterior_nuclear_group/         (Papez relay)
        │   ├── anterodorsal_nucleus/
        │   ├── anteromedial_nucleus/
        │   └── anteroventral_nucleus/
        ├── lateral_nuclear_group/          (higher-order association)
        │   ├── lateral_dorsal_nucleus/
        │   ├── lateral_posterior_nucleus/
        │   └── pulvinar/
        ├── medial_nuclear_group/           (limbic/executive/arousal)
        │   ├── central_lateral_nucleus/    (intralaminar)
        │   ├── centromedian_nucleus/       (intralaminar)
        │   ├── intralaminar_nuclear_group/ (container; see note)
        │   ├── medial_dorsal_nucleus/      (prefrontal relay)
        │   ├── midline_nuclear_group/      (container; PVT et al.)
        │   ├── parafascicular_nucleus/     (intralaminar)
        │   ├── paratenial_nucleus/         (midline)
        │   ├── reuniens_nucleus/           (midline)
        │   └── rhomboidal_nucleus/         (midline)
        ├── metathalamus/                   (sensory relay)
        │   ├── lateral_geniculate_body/    (LGN; vision)
        │   └── medial_geniculate_body/     (MGN; audition)
        ├── reticular_nucleus/              (the GABAergic gatekeeper)
        └── ventral_nuclear_group/          (motor and somatosensory)
            ├── ventral_anterior_nucleus/   (basal ganglia motor)
            ├── ventral_lateral_nucleus/    (cerebellar motor)
            └── ventral_posterior_nucleus/  (container; VPL + VPM)
                ├── ventral_posterior_lateral_nucleus/  (body)
                └── ventral_posterior_medial_nucleus/   (face)
    - right/   ★ Hemisphere container delta mirror of left/, differing
                 only in the right-side reciprocal edges.

    STRUCTURAL NOTE: the tree contains BOTH direct nucleus nodes AND
    sub-containers within the medial nuclear group. Specifically:
        * Intralaminar group: central_lateral_nucleus/,
          centromedian_nucleus/, parafascicular_nucleus/ are documented
          as DIRECT nodes under medial_nuclear_group/, AND there is
          also an intralaminar_nuclear_group/ container node. The
          Stage 4 audit should treat the direct nodes and the container
          as an INTEGRATED structure (the container is a grouping
          convenience, not a separate functional entity).
        * Midline group: paratenial_nucleus/, reuniens_nucleus/,
          rhomboidal_nucleus/ (and the paraventricular thalamic nucleus
          if it is added) are documented as DIRECT nodes under
          medial_nuclear_group/, AND there is also a
          midline_nuclear_group/ container node. Same integration note.
    This is a structural feature of the tree as it stands; the
    containers group the direct nodes functionally, but do not create
    duplicate content. Document the grouping; do not duplicate.

Notes:
    - LARGEST CONTAINER IN THE ENTIRE TREE (~40+ files). The thalamus is
      the most consequential remaining block in the diencephalon.
    - SIX NAMING TRAPS reproduced in full above (thalamic PVT vs.
      hypothalamic PVN; pulvinar vs. lateral posterior; VPL vs. VPM;
      LGN vs. MGN; thalamic reticular nucleus vs. midbrain reticular
      formation; anterior thalamic nuclei vs. anterior hypothalamic
      nucleus). Plus the medial-nuclear-group sub-traps (intralaminar
      vs. midline). Some of these have been flagged from other files
      earlier (e.g., PVT vs. PVN from the posterior LHA and arcuate
      leaves); this container is the CANONICAL declaration and every
      child should be consistent with it.
    - NO FRAGMENT: the thalamus is a relay, not a state-emitter. The
      model prompt does not need a thalamus block.
    - FIRST-ORDER vs. HIGHER-ORDER is the organizing functional
      principle. Each child should be identified as first-order relay,
      higher-order relay, or reticular gate.
    - The RETICULAR NUCLEUS is the thalamic gateway's gatekeeper: it
      is the ONLY inhibitory component of the thalamus, and it gates
      attention and state. Do not draft it as a relay; it is the gate.
    - THE ANTERIOR THALAMIC NUCLEI are the Papez circuit's thalamic
      relay. When the mammillary bodies' leaf (hypothalamus/
      mammillary_bodies/) declared the mammillothalamic tract edge to
      the anterior thalamic nuclei, it was declaring this edge from
      the mammillary side. The anterior thalamic nuclei leaves will
      close it. Same for the hippocampal formation's subiculum →
      fornix → mammillary bodies → mammillothalamic tract → anterior
      thalamus → cingulate circuit.
    - THE MEDIODORSAL NUCLEUS is the prefrontal relay: it is the
      thalamic hub for the executive and limbic loops with the
      prefrontal cortex. Its role is executive/limbic relay, not
      primary sensory.
    - THE VPL/VPM SUBDIVISION is a SOMATOTOPIC split (body vs. face),
      not a functional split. VPL and VPM are both primary
      somatosensory relays; their separation is anatomical (body map
      vs. face map). The VPL/VPM leaf pair should document this
      honestly.
    - THE PULVINAR is the visual association relay (V2–V5, MT, IT);
      the LATERAL POSTERIOR is the parietal association relay; both
      are higher-order. Do not merge them.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (monoamines, acetylcholine);
      memory/stores/ (episodic, semantic, reinforcement_value_based_
      learning, short_term); gateway/.
    - Reciprocal connections to enforce in Stage 4 (summary;
      per-nucleus wiring in the child leaves):
        * thalamus/left|right/anterior_nuclear_group ↔ hypothalamus/
          mammillary_bodies/left|right (mammillothalamic tract; the
          Papez circuit relay; the mammillary leaves declare this edge
          from their side).
        * thalamus/left|right/anterior_nuclear_group ↔ telencephalon/
          .../cortex/cingulate and retrosplenial (Papez circuit
          cortical targets).
        * thalamus/left|right/metathalamus/lateral_geniculate_body ↔
          retina → optic tract (visual input) and → telencephalon/
          .../occipital/primary_visual_cortex (V1; the visual relay).
        * thalamus/left|right/metathalamus/medial_geniculate_body ↔
          midbrain/.../inferior_colliculus (auditory input) and →
          telencephalon/.../temporal/primary_auditory_cortex (A1; the
          auditory relay).
        * thalamus/left|right/ventral_nuclear_group/ventral_posterior_
          lateral_nucleus ↔ spinal cord + brainstem (somatosensory
          body input) and → telencephalon/.../parietal/
          primary_somatosensory_cortex (S1; body map).
        * thalamus/left|right/ventral_nuclear_group/ventral_posterior_
          medial_nucleus ↔ brainstem trigeminal (somatosensory face
          input) and → telencephalon/.../parietal/
          primary_somatosensory_cortex (S1; face map).
        * thalamus/left|right/ventral_nuclear_group/
          ventral_anterior_nucleus and ventral_lateral_nucleus ↔
          telencephalon/.../basal_ganglia (VA; basal ganglia motor
          relay) and cerebellum (VL; cerebellar motor relay), and →
          telencephalon/.../cortex/frontal/primary_motor_cortex and
          premotor_cortex (motor relay).
        * thalamus/left|right/medial_nuclear_group/medial_dorsal_
          nucleus ↔ telencephalon/.../cortex/frontal/prefrontal_cortex
          (prefrontal relay; executive loop).
        * thalamus/left|right/lateral_nuclear_group/pulvinar ↔
          telencephalon/.../cortex/occipital/* and temporal/*
          (visual association relay).
        * thalamus/left|right/lateral_nuclear_group/lateral_posterior_
          nucleus ↔ telencephalon/.../cortex/parietal/
          posterior_parietal_cortex (parietal association relay).
        * thalamus/left|right/reticular_nucleus ↔ thalamo-cortical and
          cortico-thalamic axons (the GABAergic gate; no single
          cortical target; the gatekeeper of the whole thalamus).
        * thalamus/left|right/medial_nuclear_group/intralaminar group ↔
          brainstem/.../reticular_formation and basal ganglia
          (arousal and attention relay; diffuse cortical projections).
    - Connects upward to diencephalon/.
"""