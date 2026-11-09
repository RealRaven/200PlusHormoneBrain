"""
Package: infrastructure.brainparts.forebrain.diencephalon.subthalamus.subthalamic_nucleus.right
Anatomical Role:
    The right subthalamic nucleus (STN). Same small, lens-shaped,
    glutamatergic nucleus in the right dorsal subthalamus documented in
    ../left/: the ONLY EXCITATORY node in the basal ganglia's indirect
    pathway, situated between the right internal capsule (lateral),
    right substantia nigra (caudal), right zona incerta (dorsal/
    medial), and right cerebral peduncle (ventral). Functionally a
    BASAL GANGLIA NUCLEUS, not a thalamic one.

    See ../left/__init__.py for the full anatomical description, the
    four-role subdivision framing (motor, associative, limbic), the
    complete circuit architecture (indirect pathway + hyperdirect
    pathway), the complete hormone directions, and the complete
    memory interfaces.

    Reproduced FOUR TRAPS (apply equally on the right):
    - SUBTHALAMUS vs. THALAMUS: the right STN is a subthalamic nucleus;
      the subthalamus is a sibling of the thalamus.
    - SUBTHALAMIC NUCLEUS vs. SUBSTANTIA NIGRA: the right STN and
      right SN are adjacent but distinct; STN glutamatergic, SN
      dopaminergic (SNc) + GABAergic (SNr); reciprocal partners, not
      the same structure.
    - SUBTHALAMIC NUCLEUS vs. THALAMUS: the right STN projects to
      right GPi/SNr, not to the thalamus or cortex; basal ganglia
      nucleus, not a thalamic relay.
    - SUBTHALAMIC NUCLEUS vs. ZONA INCERTA: the right zona incerta is
      a distinct neighbor; STN = basal ganglia hub, zona incerta =
      broad modulatory hub.

    NO STRUCTURAL-IDENTITY TRAP: the right STN is a single distinct
    nucleus; same as ../left/. Do not invent one.

Functional Mode:
    Same as ../left/. Indirect pathway role; hyperdirect pathway;
    movement suppression and action selection; three subdivisions
    (motor, associative, limbic). The same three clinical facts apply
    on the right, with one CONTRALATERAL specification:

    CONTRALATERAL SPECIFICATION (critical — the left/right distinction
    here is anatomically meaningful, unlike most deltas):
    - HEMIBALLISMUS is CONTRALATERAL. A RIGHT STN lesion produces
      LEFT-sided hemiballismus. (Compare: a LEFT STN lesion produces
      RIGHT-sided hemiballismus, documented in ../left/.) This is the
      standard basal ganglia circuit rule — the descending motor
      pathways decussate — and the right STN leaf must state the
      left-sided hemiballismus explicitly, not just "hemiballismus."
    - DBS for Parkinson's is ipsilateral in the sense that the DBS
      lead is placed in the right STN, but the motor benefit is
      contralateral; the right STN DBS treats predominantly the LEFT
      side's motor symptoms in asymmetric Parkinson's, and both sides
      in bilateral DBS.
    - Other movement disorders: same as left; the right STN's role is
      symmetric to the left's.

    See ../left/ § Functional Mode for the full four-role description
    and the clinical fact details (mechanism, DBS rationale).

Hormonal Modulation:
    Same as ../left/. Dopamine (from right SNc) ↓ STN activity
    (indirect pathway; loss → STN hyperactivity in Parkinson's);
    GABA (from right GPe) ↓ STN activity; glutamate (STN output) ↑
    GPi/SNr activity. The STN is not a neuroendocrine nucleus. See
    ../left/ § Hormonal Modulation for the full per-modulator detail.

Memory Interfaces:
    Same as ../left/. Reads reinforcement_value_based_learning
    (action-outcome associations for action selection), procedural
    (motor skill programs), short_term (current motor state, arousal).
    Writes none directly. See ../left/ § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No STN fragment. Same as ../left/: motor action selection is a
    functional fact, not a state signal for the language model. This
    is a deliberate absence, not an oversight. See ../left/ § Model
    Integration.

Right-specific reciprocal connections to enforce in Stage 4 (the
left-side edges are in ../left/):

    Indirect pathway (the anchor circuit):
    - → telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      right (STN → GPi; EXCITATORY; indirect pathway output; right-side).
    - → telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      right (STN → GPe; EXCITATORY; the STN's collateral projection;
      reciprocal pair with GPe GABA; right-side).
    - → midbrain/tegmentum/substantia_nigra/right/pars_reticulata
      (STN → SNr; EXCITATORY; indirect pathway output; right-side).
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      right (GPe → STN; INHIBITORY; GABAergic; right-side).
    - ← midbrain/tegmentum/substantia_nigra/right/pars_compacta
      (SNc dopamine; the STN's dopaminergic modulation via the
      indirect pathway; right-side).

    Hyperdirect pathway (the fast route):
    - ← telencephalon/cerebral_hemispheres/right/cortex/frontal/
      primary_motor_cortex (hyperdirect pathway; EXCITATORY;
      right-side).
    - ← telencephalon/cerebral_hemispheres/right/cortex/frontal/
      premotor_cortex and supplementary_motor_cortex (hyperdirect
      pathway; right-side).

    Adjacency (not signaling):
    - ↔ subthalamus/right/zona_incerta (adjacent nuclei; distinct
      functions; do not merge; right-side).
    - ↔ midbrain/tegmentum/substantia_nigra/right (anatomical
      adjacency to the SN; distinct nuclei; do not merge; right-side).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed; but the CONTRALATERAL hemiballismus specification is
      anatomically required, as noted in Functional Mode).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - FOUR TRAPS reproduced in abbreviated form above; the full text
      is in ../left/ and in the parent subthalamus/ and
      subthalamic_nucleus/ containers. A contributor entering at the
      right STN must see them.
    - THE STN IS A BASAL GANGLIA NUCLEUS, NOT A THALAMIC ONE. Same as
      ../left/. The name ("subthalamic") is misleading; its
      connections are to GPe, GPi, and SNr, not to the thalamus or
      cortex. Stage 4 should treat right STN → right GPi, right STN →
      right GPe, and right STN → right SNr as BASAL GANGLIA edges,
      not thalamic ones.
    - THE THREE DEFINING CLINICAL FACTS apply on the right with the
      CONTRALATERAL hemiballismus specification:
        (1) Right STN lesion → LEFT-sided hemiballismus (contralateral;
            compare with the left STN's right-sided hemiballismus).
        (2) Right STN DBS for Parkinson's (contralateral motor benefit
            predominant; bilateral in bilateral DBS).
        (3) Right STN involvement in other movement disorders
            (dystonia, essential tremor; investigational).
      The contralateral specification is the ONE place in the entire
      delta library where the left and right versions differ
      substantively (most deltas say "no functional asymmetry
      assumed"; this one says the hemiballismus is anatomically
      contralateral, so the right and left differ in the clinical
      specifier). Do not flatten this to "hemiballismus."
    - The STN's subdivisions (motor, associative, limbic) are
      documented WITHIN ../left/, not as child nodes. Same convention
      applies on the right (do not create motor/, associative/, or
      limbic/ as child nodes here either).
    - NO FRAGMENT: same as ../left/. Motor action selection is not a
      state signal for the language model. Do not add a fragment on
      the right either.
    - The hyperdirect pathway (cortex → STN) is distinct from the
      indirect pathway (cortex → striatum → GPe → STN). Both are STN
      inputs; they serve different functions. Same on the right.
    - The right STN ↔ right zona incerta adjacency is ADJACENCY, not
      signaling. Same as ../left/.
    - Midline targets: none in this file's specific edges; all
      targets are hemisphere-split and require right-side targets
      explicitly (right GPi, right GPe, right SNr, right SNc, right
      motor/premotor/supplementary motor cortex, right zona incerta,
      right SN). The Stage 4 audit should not confuse right-side
      edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see ../left/
      § Notes for the full list.
    - Connects upward to diencephalon/subthalamus/subthalamic_nucleus/.
"""