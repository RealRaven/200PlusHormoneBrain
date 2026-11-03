"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.reticular_nucleus
Anatomical Role:
    The right thalamic reticular nucleus (TRN). A thin, GABAergic,
    sheet-like structure forming a shell around the LATERAL SURFACE of
    the right thalamus, between the right thalamus and the right
    internal capsule. Same structurally unique role as the left TRN:
        - NOT a relay: does not project to the cortex; projects only
          to the right thalamic relay nuclei.
        - The ONLY INHIBITORY COMPONENT of the right thalamus: all of
          its outputs are GABAergic.
        - TOPOGRAPHIC SECTORS (visual, auditory, somatosensory, motor,
          limbic, association) gate their corresponding right thalamic
          nuclei; each sector receives collaterals from the
          thalamo-cortical and cortico-thalamic axons of the nucleus it
          gates.
    The topographic sectors are documented WITHIN this leaf, not as
    child nodes (same convention as the left TRN).

    STRUCTURAL NOTE — GROUP-OF-ONE PATTERN (reproduced):
    reticular_nucleus/ is one of the six children of thalamus/right/
    (alongside the anterior, lateral, medial, metathalamus, and ventral
    groups). It contains a SINGLE nucleus — itself — so this file
    simultaneously serves as group-level framing AND nucleus-level
    content. Same "collapsed group" pattern as the left TRN. No
    duplication, no children, one authoritative document.

    See ../../left/reticular_nucleus/__init__.py for the full
    anatomical description, the attentional/state/spindle/absence
    functional framing, the sector organization, and the full clinical
    fact list.

    Reproduced THREE TRAPS (apply equally on the right):

    - TRN vs. MIDBRAIN RETICULAR FORMATION (primary): the right TRN is
      a thin GABAergic shell around the right thalamus (inhibitory;
      gates thalamo-cortical transmission). The midbrain reticular
      formation is a distributed brainstem arousal system (glutamatergic,
      cholinergic, monoaminergic; diffuse projections; arousal). Both
      are called "reticular"; different structures; do not merge.

    - TRN vs. "RETICULAR" NAME TRAP: "reticular" refers to the TRN's
      net-like (reticular) appearance as a thin cellular sheet, not to
      the brainstem reticular formation. The right TRN is a THALAMIC
      structure, not a brainstem structure. Do not move it out of
      thalamus/right/.

    - TRN vs. THALAMIC RELAY NUCLEI (gate-vs-relay): the right thalamic
      relay nuclei RELAY to the cortex; the right TRN GATES them
      (inhibitory; projects back to the thalamus). Do not draft the
      right TRN as a relay.

Functional Mode:
    Same as ../../left/reticular_nucleus/: attentional gating (the
    primary role); state gating — sleep-wake (the second role, including
    sleep spindle generation); absence epilepsy (the third role — the
    pathological variant of state gating); cortico-thalamic and
    thalamo-cortical coupling (the fourth role). No documented
    functional asymmetry between left and right TRN. Do not fabricate
    one.

    CLINICAL FACTS (apply on the right identically):
        * ABSENCE EPILEPSY: the right TRN-cortex-thalamus circuit
          contributes to absence seizures; ethosuximide suppresses right
          TRN T-type calcium currents. Established clinical anchor;
          bilateral involvement.
        * SLEEP SPINDLE DYSREGULATION: investigational.
        * TRN DBS FOR EPILEPSY: investigational.
        * ATTENTION/SCHIZOPHRENIA RESEARCH: preliminary.

Hormonal Modulation:
    Same as ../../left/reticular_nucleus/. Minimal; cholinergic
    (brainstem, basal forebrain), monoaminergic (brainstem), and
    histaminergic (TMN) modulation of the right TRN's excitability and
    gating. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../left/reticular_nucleus/. Reads short_term (current
    arousal/attention state buffer). Writes nothing directly (gate, not
    relay). Thin interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right TRN fragment. The TRN is a thalamic gate; the model prompt
    does not need a TRN block because the attentional and state signals
    it gates are already represented in the upstream arousal fragments
    and downstream thalamic relay fragments. Same deliberate absence as
    on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Thalamo-cortical and cortico-thalamic collaterals (the TRN's
    inputs — the anatomically unique feature):
    - ← right thalamo-cortical axons (collaterals from EVERY right
      thalamic relay's axons as they pass through the right TRN en
      route to the cortex).
    - ← right cortico-thalamic axons (collaterals from cortical axons
      as they pass through the right TRN en route to the right
      thalamus).

    Inhibitory outputs to right thalamic relay nuclei (the TRN's
    gate-keeping outputs — topographic sectors):
    - → thalamus/right/lateral_nuclear_group/pulvinar (visual sector).
    - → thalamus/right/metathalamus/lateral_geniculate_body (visual
      sector).
    - → thalamus/right/metathalamus/medial_geniculate_body (auditory
      sector).
    - → thalamus/right/ventral_nuclear_group/ventral_posterior_nucleus
      (somatosensory sector).
    - → thalamus/right/ventral_nuclear_group/ventral_anterior_nucleus
      and ventral_lateral_nucleus (motor sector).
    - → thalamus/right/anterior_nuclear_group (limbic sector).
    - → thalamus/right/medial_nuclear_group (association/limbic
      sectors).

    Reciprocal thalamo-reticular connections:
    - ↔ every right thalamic relay nucleus (thalamo-reticular
      projections back to the right TRN; the reciprocal loop underlying
      spindle generation and attentional gating).

    - ↔ ../../left/reticular_nucleus/ (hemisphere counterpart; no
      functional asymmetry assumed; the right and left TRNs are
      independent sheets that gate their respective thalami; absence
      epilepsy requires bilateral involvement).

Notes:
    - Delta file of ../../left/reticular_nucleus/. Not a full leaf. Do
      not duplicate.
    - THE RETICULAR NUCLEUS PAIR IS NOW COMPLETE: with this file, the
      TRN is fully documented on both hemispheres, with the absence
      epilepsy clinical anchor and the sleep spindle generation
      function preserved across the pair.
    - ALL SIX THALAMIC SUBDIVISIONS ARE NOW CONTAINER-COMPLETE: the
      anterior group pair, lateral group pair, medial group pair,
      metathalamus pair, reticular nucleus pair, and the ventral group
      (still pending) will be complete once its container pair is
      drafted. The thalamus at the container level is now 5 of 6 done.
    - THE THREE TRAPS are reproduced in abbreviated form; the full text
      is in ../../left/reticular_nucleus/ and ../../__init__.py.
    - THE TOPOGRAPHIC SECTORS are documented WITHIN the left TRN leaf;
      do not create visual_sector/, auditory_sector/, etc. as child
      nodes on the right either.
    - SLEEP SPINDLES are generated by BOTH TRNs (each TRN's reciprocal
      loop with its thalamic relays generates spindles in its own
      hemisphere); the two hemispheres' spindles are typically
      coordinated but the mechanism is bilateral. The right TRN's
      spindle-generation role is independent of the left's.
    - THE ABSENCE EPILEPSY clinical anchor applies on the right; typical
      absence seizures involve BILATERAL TRN-cortex-thalamus circuits
      (the spike-and-wave discharge is bilaterally synchronous), so
      neither TRN alone is "the" absence epilepsy node — both
      contribute.
    - NO FRAGMENT: same as the whole thalamus. The right TRN is a gate,
      not a state-emitter.
    - The right TRN is NOT the midbrain reticular formation (different
      structure), NOT a thalamic relay nucleus (gate vs. relay), NOT a
      brainstem structure despite the name.
    - "Reticular" refers to appearance, not to the reticular formation.
      Do not move the right TRN out of thalamus/right/ or treat it as
      a brainstem structure.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/reticular_nucleus/ § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/.
"""