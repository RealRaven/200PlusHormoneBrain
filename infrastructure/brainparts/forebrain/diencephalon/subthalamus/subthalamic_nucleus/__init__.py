"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus.subthalamic_nucleus
Anatomical Role:
    The subthalamic nucleus (STN) is a small, lens-shaped,
    glutamatergic nucleus in the dorsal subthalamus, situated between
    the internal capsule (lateral), the substantia nigra (caudal), the
    zona incerta (dorsal/medial), and the cerebral peduncle (ventral).
    It is the ONLY EXCITATORY node in the basal ganglia's indirect
    pathway — every other basal ganglia node is GABAergic/inhibitory.

    FUNCTIONAL IDENTITY: the STN is a BASAL GANGLIA NUCLEUS, not a
    thalamic one. Despite its name, its projections are to the globus
    pallidus (GPe, GPi), the substantia nigra pars reticulata (SNr),
    and (via collaterals) back to the GPe. It does NOT project to the
    thalamus or cortex. It is functionally embedded in the basal
    ganglia indirect pathway, and its clinical importance derives
    entirely from that role.

    SUBDIVISIONS (documented WITHIN each hemisphere's leaf, not as
    child nodes):
        - Motor subdivision (dorsolateral): receives motor cortical
          input; projects to the motor GPi; implicated in the motor
          symptoms of Parkinson's disease.
        - Associative subdivision (ventromedial): receives prefrontal
          and associative cortical input; projects to the associative
          GPi/SNr; implicated in cognitive and behavioral aspects.
        - Limbic subdivision (medial tip): receives limbic cortical
          and amygdala input; projects to the limbic GPi; implicated
          in emotional and motivational aspects.

    FOUR NAMING TRAPS (reproduced from the subthalamus/ container):

    - SUBTHALAMUS vs. THALAMUS: the STN is a subthalamic (not
      thalamic) nucleus. The subthalamus is a sibling of the thalamus,
      not a subdivision of it. Do not move STN under thalamus/.

    - SUBTHALAMIC NUCLEUS vs. SUBSTANTIA NIGRA: the STN and substantia
      nigra (SN) are ADJACENT nuclei in the basal ganglia circuitry,
      but FUNCTIONALLY DISTINCT. The STN is glutamatergic (excitatory);
      the SN has a dopaminergic part (SNc) and a GABAergic part (SNr).
      The STN and SNr are reciprocal partners in the indirect pathway
      but distinct nodes. Do not merge; do not treat the STN as "part
      of the substantia nigra."

    - SUBTHALAMIC NUCLEUS vs. THALAMUS: the STN projects to GPi and
      SNr, NOT to the thalamus or cortex. Do not draft it as a
      thalamic relay. The STN's "output" is to the basal ganglia
      output nuclei (GPi/SNr), which then project to the thalamus.

    - SUBTHALAMIC NUCLEUS vs. ZONA INCERTA: the zona incerta
      (subthalamus/zona_incerta/) is a distinct neighbor within the
      same subthalamus region. The STN is a well-studied basal ganglia
      hub; the zona incerta is a broad, poorly characterized
      modulatory hub. Do not merge; do not treat them as a pair of
      similar nuclei.

Functional Mode:
    - Indirect pathway of the basal ganglia (the anchor role): the STN
      is a glutamatergic, excitatory nucleus. The classic indirect
      pathway:
        Cortex → striatum (indirect medium spiny neurons, iMSNs) →
        GPe (external globus pallidus) → STN → GPi (internal globus
        pallidus) and SNr (substantia nigra pars reticulata) →
        thalamus → cortex.
      The STN EXCITES the GPi and SNr, which then INHIBIT the
      thalamus. The indirect pathway therefore SUPPRESSES movement;
      STN activation tends to inhibit movement, and STN silencing/
      lesion disinhibits movement.
    - Movement suppression and action selection (the functional
      consequence): the STN's net effect in the indirect pathway is to
      suppress competing motor programs and select the intended
      action. It is a "brake" on unwanted movements, not a "movement
      generator."
    - Hyperdirect pathway (the fast route): a direct
      cortex → STN pathway (bypassing the striatum) provides fast
      cortical control of the STN. The hyperdirect pathway is the
      substrate for rapid action cancellation and is the anatomical
      basis of the "braking" function of the STN.
    - Subdivision-specific functions:
        * Motor (dorsolateral): motor suppression, action selection.
        * Associative (ventromedial): cognitive control, response
          inhibition.
        * Limbic (medial tip): emotional/motivational aspects of
          action selection; implicated in impulsivity and
          motivation.
    - THE THREE DEFINING CLINICAL FACTS (the file's substantive
      contribution):
        (1) HEMIBALLISMUS (the STN's defining clinical syndrome):
            a lesion of the STN (typically ischemic stroke) produces
            violent, involuntary, flinging movements of the
            contralateral limbs (hemiballismus). Mechanism: STN lesion
            → loss of STN excitation of GPi/SNr → GPi/SNr hypoactivity
            → thalamic disinhibition → excessive movement. The STN's
            normal role is to SUPPRESS unwanted movement; its loss
            allows them through. Hemiballismus is the STN's clinical
            signature and is the anatomical proof of the STN's role
            in movement suppression.
        (2) DEEP BRAIN STIMULATION (DBS) for Parkinson's disease (the
            STN's modern clinical use): the STN is a principal DBS
            target for advanced Parkinson's. High-frequency DBS of
            the STN reduces tremor, rigidity, and bradykinesia by
            modulating the STN's pathological hyperactivity in the
            parkinsonian indirect pathway. The STN is one of the two
            most-used DBS targets (along with the GPi); it is the
            single most-used DBS target in many centers.
        (3) STN involvement in other movement disorders: STN
            involvement is implicated in dystonia, essential tremor,
            and other hyperkinetic disorders; its role in these is
            under active investigation, and DBS of the STN (or of
            adjacent targets like the zona incerta) is explored for
            these indications.
    - The STN is therefore the subthalamus's clinical anchor: a small
      nucleus with outsized clinical importance because of its role
      in the indirect pathway and its use as a DBS target.

Hormonal Modulation (STN-specific; dopamine is the key modulator):
    - Dopamine (from the substantia nigra pars compacta, SNc): the STN
      is under dopaminergic modulation via the indirect pathway. In
      Parkinson's disease, loss of dopamine → pathological STN
      hyperactivity → the therapeutic rationale for STN DBS.
      Dopamine's net effect is inhibitory on STN activity (via
      striatal modulation of the GPe → STN pathway); loss → STN
      hyperactivity.
    - Glutamate: intrinsic transmitter of STN neurons (the STN is
      glutamatergic); not a "modulator" in the usual sense — it is the
      STN's output.
    - GABA (from GPe): the STN is inhibited by GABAergic input from
      the external globus pallidus (GPe). This is the direct inhibition
      in the indirect pathway.
    - Direction summary: dopamine ↓ STN activity (indirect pathway);
      GPe GABA ↓ STN activity; STN glutamate output ↑ GPi/SNr
      activity. These are the actionable directions.
    - The STN is NOT a neuroendocrine nucleus: it is not a principal
      target of the 12 endocrine axes. Its modulators are the basal
      ganglia transmitters (dopamine, GABA, glutamate), not the
      endocrine axes. Do not pad the section with the 12 axes.

Memory Interfaces:
    - Reads:
        * reinforcement_value_based_learning: the STN's role in action
          selection depends on learned action-outcome associations;
          suppressing "competing programs" requires knowing what they
          are (learned through reinforcement).
        * procedural: motor skill programs; the STN's motor
          suppression is tuned to the currently active motor program.
        * short_term: current motor state and arousal buffer.
    - Writes: none directly. The STN drives motor output via the
      basal ganglia output nuclei; it does not write stored content.
    - The STN is therefore a procedural/reinforcement-adjacent node:
      it reads learned motor and value information but does not store
      it. Do not draft it as a memory write site.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No STN fragment. The STN is a motor action selection nucleus;
      the model prompt does not need a subthalamic block because the
      model is not executing motor actions.
    - The STN's basal ganglia context is documented FUNCTIONALLY, not
      as a state fragment. The model does not need to represent
      "current STN activity" as a prompt field.
    - AGGREGATION RULES: no fragments are emitted from this container
      or from the STN leaves. This is a deliberate absence, not an
      oversight: motor action selection is a functional/anatomical
      fact, not a state signal for the language model.
    - The Parkinson's / DBS / hemiballismus clinical context is
      documented in the leaves for completeness, but is not a prompt
      field.

Children (one child pair — full leaf + delta):
    - left/    ★★ FULL TIER 1 LEAF. The complete STN content:
                 indirect pathway role, hyperdirect pathway role,
                 subdivisions (motor/associative/limbic), the three
                 clinical facts (hemiballismus; DBS for Parkinson's;
                 other movement disorders), all reciprocal
                 connections (GPe, GPi, SNr, SNc, cortex via the
                 hyperdirect pathway), and all memory interfaces.
    - right/   Delta mirror of left/, differing only in the right-side
                 reciprocal edges. No functional asymmetry documented.

Notes:
    - Tier 1 hub container. The full leaf lives in left/; right/ is a
      delta.
    - FOUR TRAPS reproduced above (subthalamus vs. thalamus; STN vs.
      substantia nigra; STN vs. thalamus; STN vs. zona incerta). All
      apply to the STN specifically. Do not omit any of them.
    - THE STN IS A BASAL GANGLIA NUCLEUS, NOT A THALAMIC ONE. This is
      the most important structural fact about the STN and must be
      declared at every level. Its name ("subthalamic") is misleading;
      its connections are to GPe, GPi, and SNr, not to the thalamus or
      cortex. The Stage 4 audit should treat STN → GPi and STN → SNr
      as basal ganglia edges, not thalamic ones.
    - THE THREE DEFINING CLINICAL FACTS are the STN's substantive
      contribution:
        (1) Hemiballismus from STN lesion.
        (2) STN DBS for Parkinson's disease.
        (3) STN involvement in other movement disorders (dystonia,
            essential tremor; investigational).
      Document all three in the leaf; do not omit.
    - The STN's subdivisions (motor, associative, limbic) are
      documented WITHIN each hemisphere's leaf, not as child nodes.
      Same convention as habenula's LHb/MHb and PVN's sub-populations.
    - The STN has NO fragment. This is deliberate: motor action
      selection is not a state signal for the language model.
    - The STN's dopaminergic modulation (via SNc) is the key
      modulator; the STN's glutamatergic output is its product. Do
      not confuse the two.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, GABA, glutamate);
      memory/stores/ (reinforcement_value_based_learning, procedural,
      short_term); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * subthalamic_nucleus/left|right → telencephalon/.../
          basal_ganglia/globus_pallidus/left|right (STN → GPi;
          excitatory; indirect pathway output; and STN → GPe;
          excitatory; the GPe then inhibits the STN via GABA — the
          reciprocal pair within the indirect pathway).
        * subthalamic_nucleus/left|right → midbrain/.../
          substantia_nigra/left|right/pars_reticulata (STN → SNr;
          excitatory; indirect pathway output; SNr reciprocates when
          drafted).
        * subthalamic_nucleus/left|right ← midbrain/.../
          substantia_nigra/left|right/pars_compacta (SNc dopamine;
          the STN's dopaminergic modulation via the indirect pathway).
        * subthalamic_nucleus/left|right ← telencephalon/.../cortex/
          frontal/primary_motor_cortex and premotor_cortex (the
          hyperdirect pathway: cortex → STN; a direct, fast route
          that bypasses the striatum).
        * subthalamic_nucleus/left|right ↔ subthalamus/left|right/
          zona_incerta (adjacent nuclei; distinct functions; do not
          merge; the zona incerta is the broad modulatory hub, the
          STN is the basal ganglia hub).
    - Connects upward to diencephalon/subthalamus/.
"""