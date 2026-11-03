"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus.subthalamic_nucleus.left
Anatomical Role:
    The left subthalamic nucleus (STN). A small, lens-shaped,
    glutamatergic nucleus in the left dorsal subthalamus, situated
    between the left internal capsule (lateral), the left substantia
    nigra (caudal), the left zona incerta (dorsal/medial), and the
    left cerebral peduncle (ventral). It is the ONLY EXCITATORY node
    in the basal ganglia's indirect pathway — every other basal
    ganglia node is GABAergic/inhibitory.

    FUNCTIONAL IDENTITY: the left STN is a BASAL GANGLIA NUCLEUS, not
    a thalamic one. Its projections are to the left globus pallidus
    (GPe and GPi), the left substantia nigra pars reticulata (SNr),
    and (via collaterals) back to the left GPe. It does NOT project
    to the thalamus or cortex. It is functionally embedded in the
    basal ganglia indirect pathway, and its clinical importance
    derives entirely from that role.

    SUBDIVISIONS (documented WITHIN this file, not as child nodes):
        - Motor subdivision (dorsolateral): receives left motor and
          premotor cortical input; projects to the left motor GPi;
          implicated in the motor symptoms of Parkinson's disease.
          This is the DBS-targeted subdivision.
        - Associative subdivision (ventromedial): receives left
          prefrontal and associative cortical input; projects to the
          left associative GPi/SNr; implicated in cognitive and
          behavioral aspects (response inhibition, decision-making).
        - Limbic subdivision (medial tip): receives left limbic
          cortical and amygdala input; projects to the left limbic
          GPi; implicated in emotional and motivational aspects of
          action selection.

    FOUR NAMING TRAPS (reproduced from the subthalamus/ and
    subthalamic_nucleus/ containers):

    - SUBTHALAMUS vs. THALAMUS: the STN is a subthalamic (not
      thalamic) nucleus. The subthalamus is a sibling of the thalamus,
      not a subdivision of it. Do not move STN under thalamus/.

    - SUBTHALAMIC NUCLEUS vs. SUBSTANTIA NIGRA: the left STN and left
      substantia nigra (SN) are ADJACENT nuclei in the basal ganglia
      circuitry, but FUNCTIONALLY DISTINCT. The STN is glutamatergic;
      the SN has a dopaminergic part (SNc) and a GABAergic part
      (SNr). The STN and SNr are reciprocal partners in the indirect
      pathway but distinct nodes. Do not merge; do not treat the STN
      as "part of the substantia nigra."

    - SUBTHALAMIC NUCLEUS vs. THALAMUS: the STN projects to GPi and
      SNr, NOT to the thalamus or cortex. Do not draft it as a
      thalamic relay.

    - SUBTHALAMIC NUCLEUS vs. ZONA INCERTA: the left zona incerta
      (subthalamus/left/zona_incerta/) is a distinct neighbor within
      the same subthalamus region. The STN is a well-studied basal
      ganglia hub; the zona incerta is a broad, poorly characterized
      modulatory hub. Do not merge.

    NO STRUCTURAL-IDENTITY TRAP: the left STN is a single distinct
    nucleus. Its subdivisions are documented within this file; there
    is no split-structure or duplicate-location issue. Do not invent
    one.

Functional Mode:
    - Indirect pathway of the basal ganglia (the anchor role):
        * The left STN is a glutamatergic, excitatory nucleus. The
          classic indirect pathway:
            Cortex → striatum (indirect medium spiny neurons, iMSNs) →
            GPe (external globus pallidus) → STN → GPi (internal
            globus pallidus) and SNr (substantia nigra pars
            reticulata) → thalamus → cortex.
        * The STN EXCITES the GPi and SNr, which then INHIBIT the
          thalamus. The indirect pathway therefore SUPPRESSES movement;
          STN activation tends to inhibit movement, and STN silencing/
          lesion disinhibits movement.
    - Movement suppression and action selection: the STN's net effect
      in the indirect pathway is to suppress competing motor programs
      and select the intended action. It is a "brake" on unwanted
      movements, not a "movement generator." Action selection
      involves:
        * Suppressing competing programs (via the indirect pathway's
          net inhibition of the thalamus).
        * Selecting the intended program (releasing it from inhibition
          via cortical drive to the direct pathway).
        * Braking runaway movements (the hyperdirect pathway's fast
          cortical cancellation signal).
    - Hyperdirect pathway (the fast route):
        * A direct cortex → STN pathway (bypassing the striatum)
          provides fast cortical control of the STN.
        * The hyperdirect pathway is the substrate for rapid action
          cancellation and is the anatomical basis of the "braking"
          function of the STN. It responds faster than the indirect
          pathway (fewer synapses) and is particularly active during
          stop-signal tasks and error detection.
    - Subdivision-specific functions:
        * Motor (dorsolateral): motor suppression, action selection;
          the DBS-targeted subdivision in Parkinson's disease.
        * Associative (ventromedial): cognitive control, response
          inhibition, decision-making under conflict.
        * Limbic (medial tip): emotional/motivational aspects of
          action selection; implicated in impulsivity and motivation.
    - THE THREE DEFINING CLINICAL FACTS (the file's substantive
      contribution):
        (1) HEMIBALLISMUS (the STN's defining clinical syndrome):
            a lesion of the left STN (typically ischemic stroke)
            produces violent, involuntary, flinging movements of the
            RIGHT contralateral limbs (hemiballismus).
            Mechanism: STN lesion → loss of STN excitation of GPi/SNr
            → GPi/SNr hypoactivity → thalamic disinhibition →
            excessive movement. The STN's normal role is to SUPPRESS
            unwanted movement; its loss allows them through.
            Hemiballismus is the STN's clinical signature and is the
            anatomical proof of the STN's role in movement
            suppression.
        (2) DEEP BRAIN STIMULATION (DBS) for Parkinson's disease (the
            STN's modern clinical use): the left STN (specifically the
            motor dorsolateral subdivision) is a principal DBS target
            for advanced Parkinson's. High-frequency DBS of the STN
            reduces tremor, rigidity, and bradykinesia by modulating
            the STN's pathological hyperactivity in the parkinsonian
            indirect pathway. The STN is one of the two most-used DBS
            targets (along with the GPi); it is the single most-used
            DBS target in many centers.
        (3) STN involvement in other movement disorders: STN
            involvement is implicated in dystonia, essential tremor,
            and other hyperkinetic disorders; its role in these is
            under active investigation, and DBS of the STN (or of
            adjacent targets like the zona incerta) is explored for
            these indications.
    - The left STN is therefore the subthalamus's clinical anchor: a
      small nucleus with outsized clinical importance because of its
      role in the indirect pathway and its use as a DBS target.

Hormonal Modulation (STN-specific; dopamine is the key modulator):
    - Dopamine (from the left substantia nigra pars compacta, SNc):
        * The STN is under dopaminergic modulation via the indirect
          pathway. Dopamine acts on D1 and D2 receptors in the
          striatum to modulate the direct and indirect pathways;
          dopaminergic input to the STN itself is modest, but the
          STN's activity is strongly shaped by the downstream
          striatal modulation.
        * In Parkinson's disease, loss of dopamine → pathological STN
          hyperactivity → the therapeutic rationale for STN DBS.
        * Direction: dopamine loss ↑ STN activity (pathological
          hyperactivity in Parkinson's).
    - Glutamate: intrinsic transmitter of STN neurons (the STN is
      glutamatergic); its OUTPUT, not a modulator in the usual sense.
    - GABA (from the left GPe): the STN is inhibited by GABAergic
      input from the external globus pallidus (GPe). This is the
      direct inhibition in the indirect pathway.
    - Direction summary: dopamine ↓ STN activity (indirect pathway;
      loss → STN hyperactivity in Parkinson's); GPe GABA ↓ STN
      activity; STN glutamate output ↑ GPi/SNr activity. These are
      the actionable directions.
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
    - Writes: none directly. The STN drives motor output via the basal
      ganglia output nuclei (GPi, SNr); it does not write stored
      content.
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
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      This is a deliberate absence, not an oversight: motor action
      selection is a functional/anatomical fact, not a state signal
      for the language model.
    - The Parkinson's / DBS / hemiballismus clinical context is
      documented here for completeness, but is not a prompt field.
    - No multimodal input is consumed here; no fragments are emitted.

Reciprocal Connections (left-side; the right side is in ../right/):

    Indirect pathway (the anchor circuit):
    - → telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      left/ventral_pallidum and left/... (STN → GPi; EXCITATORY;
      indirect pathway output; GPi is the internal segment; the
      STN's principal basal ganglia output to GPi).
    - → telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      left (STN → GPe; EXCITATORY; the STN's collateral projection to
      GPe; GPe then inhibits the STN via GABA — the reciprocal pair
      within the indirect pathway).
    - → midbrain/tegmentum/substantia_nigra/left/pars_reticulata
      (STN → SNr; EXCITATORY; indirect pathway output to SNr; the
      SNr reciprocates when drafted).
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      left (GPe → STN; INHIBITORY; GABAergic; the GPe's inhibition
      of the STN).
    - ← midbrain/tegmentum/substantia_nigra/left/pars_compacta (SNc
      dopamine; the STN's dopaminergic modulation via the indirect
      pathway; SNc reciprocates when drafted).

    Hyperdirect pathway (the fast route):
    - ← telencephalon/cerebral_hemispheres/left/cortex/frontal/
      primary_motor_cortex (hyperdirect pathway: cortex → STN;
      EXCITATORY; glutamatergic; the fast route that bypasses the
      striatum).
    - ← telencephalon/cerebral_hemispheres/left/cortex/frontal/
      premotor_cortex and supplementary_motor_cortex (hyperdirect
      pathway; action preparation and cancellation).

    Adjacency (not signaling):
    - ↔ subthalamus/left/zona_incerta (adjacent nuclei within the
      left subthalamus; distinct functions; do not merge; the zona
      incerta is the broad modulatory hub, the STN is the basal
      ganglia hub; no documented signaling edge between them beyond
      adjacency).
    - ↔ midbrain/tegmentum/substantia_nigra/left (anatomical
      adjacency to the SN; distinct nuclei; do not merge; the STN
      and SN are reciprocal partners but distinct nodes).

Notes:
    - Tier 1 full leaf (left). THE SUBTHALAMUS'S CLINICAL ANCHOR.
      right/ is a delta.
    - FOUR TRAPS reproduced in full above (subthalamus vs. thalamus;
      STN vs. substantia nigra; STN vs. thalamus; STN vs. zona
      incerta). All apply to the STN specifically. Do not omit any of
      them.
    - THE STN IS A BASAL GANGLIA NUCLEUS, NOT A THALAMIC ONE. Its
      name ("subthalamic") is misleading; its connections are to GPe,
      GPi, and SNr, not to the thalamus or cortex. The Stage 4 audit
      should treat STN → GPi, STN → GPe, and STN → SNr as BASAL
      GANGLIA edges, not thalamic ones.
    - THE THREE DEFINING CLINICAL FACTS are the STN's substantive
      contribution:
        (1) Hemiballismus from STN lesion (left lesion → RIGHT
            contralateral hemiballismus; the contralateral relationship
            is important).
        (2) STN DBS for Parkinson's disease.
        (3) STN involvement in other movement disorders (dystonia,
            essential tremor; investigational).
      Document all three; do not omit.
    - The STN's subdivisions (motor, associative, limbic) are
      documented WITHIN this file, not as child nodes. Same convention
      as habenula's LHb/MHb and PVN's sub-populations. Do not create
      motor/, associative/, or limbic/ as child nodes.
    - The STN has NO fragment. This is deliberate: motor action
      selection is not a state signal for the language model. Do not
      add a fragment because "every hub should have one" — the STN's
      role is functional, not state-level.
    - The STN's dopaminergic modulation (via SNc) is the key
      modulator; the STN's glutamatergic output is its product. Do
      not confuse the two.
    - The hyperdirect pathway (cortex → STN) is DISTINCT from the
      indirect pathway (cortex → striatum → GPe → STN). Both are STN
      inputs; they serve different functions (fast cancellation vs.
      slow contextual suppression).
    - The STN ↔ zona incerta adjacency is ADJACENCY, not signaling:
      the two structures share the subthalamus region but are
      anatomically and functionally distinct. Stage 4 should not
      expect a signaling edge between them.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, GABA, glutamate); memory/
      stores/ (reinforcement_value_based_learning, procedural,
      short_term); gateway/.
    - Connects upward to diencephalon/subthalamus/subthalamic_nucleus/.
"""