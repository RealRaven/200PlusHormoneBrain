"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus
Anatomical Role:
    The subthalamus is a small region of the diencephalon situated
    ventral to the thalamus and dorsal to the midbrain tegmentum,
    between the hypothalamus (medial) and the internal capsule
    (lateral). It contains two nuclei:
        - subthalamic_nucleus/ (STN; left/ and right/): a lens-shaped
          glutamatergic nucleus. It is FUNCTIONALLY A BASAL GANGLIA
          NUCLEUS (part of the indirect pathway), not a thalamic one,
          despite its name. It is the most clinically important nucleus
          in the subthalamus (see clinical facts).
        - zona_incerta/ (ZI; left/ and right/): a broad, elongated band
          of cells between the STN and the thalamus. Historically
          described as a "zone of uncertainty" — its functions are
          heterogeneous and less characterized than the STN's.
          Contributes to arousal, nociception, visceral regulation, and
          motor gating.

    NAMING TRAPS (critical — four confusions apply here):

    - SUBTHALAMUS vs. THALAMUS: the name means "below the thalamus," but
      the subthalamus is a DISTINCT REGION, not part of the thalamus.
      The subthalamus is a diencephalon sibling of the thalamus, not a
      subdivision of it. Do not merge; do not move subthalamic
      structures under thalamus/.

    - SUBTHALAMIC NUCLEUS vs. SUBSTANTIA NIGRA: adjacent nuclei, both
      in the basal ganglia circuitry, but FUNCTIONALLY DISTINCT. The
      STN is glutamatergic (excitatory); the substantia nigra (SN) has
      two parts: pars compacta (dopaminergic; the SNc) and pars
      reticulata (GABAergic; the SNr). The STN and SNr are reciprocal
      partners in the indirect pathway but distinct nodes. Do not
      merge; do not treat the STN as "part of the substantia nigra."

    - SUBTHALAMIC NUCLEUS vs. THALAMUS: the STN is a basal ganglia
      nucleus, not a thalamic one. Its projections go to the globus
      pallidus (GPe, GPi) and the substantia nigra pars reticulata
      (SNr), not to the cerebral cortex via the thalamus. Do not draft
      it as a thalamic relay.

    - ZONA INCERTA vs. LHA / LATERAL HYPOTHALAMUS: the zona incerta
      sits adjacent to the lateral hypothalamic area (LHA). Some
      authors treat the zona incerta as a dorsal extension of the
      lateral hypothalamus; this tree places it under subthalamus/, not
      under hypothalamus/. Do not merge; do not move it. The two are
      anatomically adjacent but distinct tree nodes.

Functional Mode:
    The subthalamus is NOT a single functional unit: its two nuclei
    have distinct functions and distinct clinical importance.

    - SUBTHALAMIC NUCLEUS (STN; the file's anchor):
        * Indirect pathway of the basal ganglia (the anchor role): the
          STN is a glutamatergic, excitatory nucleus. In the classic
          basal ganglia indirect pathway:
            Cortex → striatum (indirect medium spiny neurons) →
            GPe (external globus pallidus) → STN → GPi (internal
            globus pallidus) and SNr (substantia nigra pars
            reticulata) → thalamus → cortex.
          The STN EXCITES the GPi and SNr, which then INHIBIT the
          thalamus. The indirect pathway therefore SUPPRESSES
          movement; STN activation tends to inhibit movement, and STN
          silencing/lesion disinhibits movement (see hemiballismus
          below).
        * Movement suppression and action selection: the STN's net
          effect in the indirect pathway is to suppress competing
          motor programs and select the intended action. It is not a
          simple "movement generator" but a "movement selector" /
          "brake" on unwanted movements.
        * Subdivisions: motor (dorsolateral), associative (ventromedial),
          and limbic (medial tip). Each has distinct cortical inputs
          and distinct functional roles.
        * Clinical fact — HEMIBALLISMUS (the STN's defining clinical
          syndrome): a lesion of the STN (typically ischemic stroke)
          disinhibits the GPi/SNr → disinhibits the thalamus → produces
          violent, involuntary, flinging movements of the contralateral
          limbs (hemiballismus). The STN's normal role is to SUPPRESS
          unwanted movement; its loss allows them through.
        * Clinical fact — DEEP BRAIN STIMULATION (DBS) for Parkinson's
          disease: the STN is a principal DBS target for advanced
          Parkinson's. High-frequency DBS of the STN reduces tremor,
          rigidity, and bradykinesia by modulating the STN's
          pathological hyperactivity in the parkinsonian indirect
          pathway. The STN is one of the two most-used DBS targets
          (along with the GPi).
        * Clinical fact — STN in other movement disorders: STN
          involvement is implicated in dystonia, essential tremor, and
          other hyperkinetic disorders; its role is under active
          investigation.
        * The STN is therefore the subthalamus's clinical anchor. It is
          a small nucleus with outsized clinical importance because of
          its role in the indirect pathway and its use as a DBS target.

    - ZONA INCERTA (ZI; the secondary content):
        * Broad modulatory hub (poorly characterized): the zona incerta
          is a long, thin band of cells that receives inputs from many
          brainstem and hypothalamic structures and projects broadly.
          Its functional roles overlap with several systems:
          arousal (through connections with the reticular activating
          system), nociception (through spinothalamic-adjacent
          projections), visceral regulation (through hypothalamic
          connections), and motor gating (through basal ganglia
          connections).
        * "Zone of uncertainty" (the honest historical framing): the
          zona incerta was named for the difficulty of assigning it a
          clear function. Modern work is narrowing its roles, but it
          remains less characterized than the STN. Document as
          "heterogeneous; roles overlap with multiple systems; not a
          single functional unit."
        * DBS target (secondary clinical fact): the zona incerta has
          been explored as an alternative DBS target for Parkinson's
          disease and tremor; its use is less established than the
          STN's.
        * The zona incerta's functional identity is "broad modulatory
          hub"; it is NOT a single hub like the STN.

Hormonal Modulation (subthalamus-wide summary):
    - STN:
        * Dopamine (from the substantia nigra pars compacta, SNc): the
          STN is under dopaminergic modulation via the indirect
          pathway. Loss of dopamine in Parkinson's disease →
          pathological STN hyperactivity → the therapeutic rationale
          for STN DBS. Document as the key modulator.
        * Glutamate: intrinsic transmitter of STN neurons (the STN is
          glutamatergic); not a "modulator" in the usual sense.
        * GABA (from GPe): the STN is inhibited by GABAergic input
          from the external globus pallidus (GPe). This is the direct
          inhibition in the indirect pathway.
        * Direction: dopamine ↓ STN activity (via indirect pathway;
          loss → STN hyperactivity in Parkinson's); GPe GABA ↓ STN
          activity.
    - Zona incerta:
        * Heterogeneous modulation: the zona incerta receives inputs
          from the reticular activating system, hypothalamic nuclei,
          and the basal ganglia. Its modulators are therefore
          diverse: norepinephrine, dopamine, GABA, and several
          hypothalamic peptides. Document as "heterogeneous
          modulatory inputs, poorly characterized."
    - Direction summary: dopamine ↓ STN activity (indirect pathway);
      GPe GABA ↓ STN activity; zona incerta receives heterogeneous
      modulatory inputs (poorly characterized). These are the
      actionable directions.

Memory Interfaces (subthalamus-wide summary):
    - STN: reads reinforcement_value_based_learning (action selection
      uses learned action-outcome associations; the STN's role in
      suppressing competing motor programs depends on learning what
      the "competing programs" are) and procedural (motor skill
      programs). Reads short_term (current motor state and arousal).
      Writes none directly (drives motor output, not stored content).
    - Zona incerta: reads short_term (arousal, nociceptive state,
      visceral state). No documented higher memory interface. Writes
      none directly.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The container does not emit fragments itself. Both nuclei are
      primarily motor/arousal/integrative nodes, not state-emitting
      nodes for the model prompt:
        (1) STN: does NOT emit a prompt fragment. Its role is motor
            action selection through the indirect pathway; the model
            prompt does not need an STN block because the model is not
            executing motor actions. The STN's basal ganglia context
            is documented functionally, not as a state fragment.
        (2) Zona incerta: does NOT emit a prompt fragment. Its roles
            (arousal, nociception, visceral, motor gating) are
            contextual and heterogeneous; the model prompt does not
            need a zona incerta block.
    - AGGREGATION RULES (mandatory): no fragments are emitted from the
      subthalamus. The basal ganglia's indirect-pathway context is a
      functional/anatomical fact, not a state signal for the model.
    - Guardrails: no guardrails are needed because no fragments are
      emitted. The subthalamus does not feed the "bias not impairment"
      pattern.

Children (two children — asymmetric shapes):
    - subthalamic_nucleus/   ★★ TIER 1 HUB. The subthalamus's clinical
        ├── left/                anchor. Indirect pathway; hemiballismus;
        └── right/               DBS target for Parkinson's. The most
                                 important nucleus in this container.
    - zona_incerta/          Tier 2 organ-flavored leaf (broad
        ├── left/                modulatory hub; poorly characterized;
        └── right/               heterogeneous functions; not a single
                                 functional unit).

    The asymmetric child discipline applies: the STN is a well-studied
    hub (Tier 1); the zona incerta is a broad modulatory hub (Tier 2
    organ-flavored). Do not force the same template onto both.

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each child owns its own specification.
    - FOUR NAMING TRAPS reproduced in full above (subthalamus vs.
      thalamus; STN vs. substantia nigra; STN vs. thalamus; zona incerta
      vs. LHA). Apply at every level where the subthalamus is referenced.
    - THE STN IS FUNCTIONALLY A BASAL GANGLIA NUCLEUS, NOT A THALAMIC
      ONE. Its name is misleading; its connections are to the GPe,
      GPi, and SNr, not to the thalamus or cortex. Do not draft it as
      a thalamic relay. The Stage 4 audit should treat STN → GPi and
      STN → SNr as basal ganglia edges, not thalamic ones.
    - THE STN IS THE SUBTHALAMUS'S CLINICAL ANCHOR. The three defining
      clinical facts are:
        (1) Hemiballismus from STN lesion.
        (2) STN DBS for Parkinson's disease.
        (3) STN involvement in other movement disorders (dystonia,
            essential tremor).
      Document all three in the STN leaf; do not omit.
    - The zona incerta is a broad modulatory hub, not a single
      functional unit. Do not draft it as "the zona incerta =
      arousal" or "the zona incerta = nociception"; it overlaps with
      multiple systems and its functions are less characterized than
      the STN's.
    - The zona incerta vs. LHA adjacency is a genuine anatomical
      relationship, but the two are distinct tree nodes (zona incerta
      under subthalamus/, LHA under hypothalamus/). Some authors treat
      the zona incerta as a dorsal LHA extension; this tree does not.
      Do not merge.
    - The STN's reciprocal connections (STN ↔ GPe; STN ↔ GPi; STN ↔
      SNr; STN ↔ motor cortex via the hyperdirect pathway) will be
      declared in the STN leaf and reciprocated by the GPi/GPe/SNr
      leaves (documented under telencephalon/subcortical/basal_ganglia
      and midbrain/tegmentum/substantia_nigra, when drafted).
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, GABA, glutamate);
      memory/stores/ (reinforcement_value_based_learning, procedural,
      short_term); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * subthalamus/left|right/subthalamic_nucleus ↔
          telencephalon/.../basal_ganglia/globus_pallidus/left|right
          (STN → GPi; excitatory; indirect pathway output; STN ↔ GPe
          reciprocal; the STN's principal basal ganglia connections).
        * subthalamus/left|right/subthalamic_nucleus ↔
          midbrain/tegmentum/substantia_nigra/left|right/pars_reticulata
          (STN → SNr; excitatory; indirect pathway output; SNr
          reciprocates when drafted).
        * subthalamus/left|right/subthalamic_nucleus ←
          midbrain/tegmentum/substantia_nigra/left|right/pars_compacta
          (SNc dopamine; the STN's dopaminergic modulation via the
          indirect pathway).
        * subthalamus/left|right/subthalamic_nucleus ↔
          telencephalon/.../cortex/frontal/primary_motor_cortex and
          premotor_cortex (the hyperdirect pathway: cortex → STN; a
          direct, fast route from cortex to the STN that bypasses the
          striatum).
        * subthalamus/left|right/zona_incerta ↔
          hypothalamus/.../lateral_area (adjacency; distinct tree
          nodes; do not merge).
        * subthalamus/left|right/zona_incerta ↔
          brainstem/.../reticular_formation (arousal; heterogeneous
          modulatory inputs).
    - Connects upward to diencephalon/.
"""