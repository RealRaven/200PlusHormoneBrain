"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.reticular_nucleus
Anatomical Role:
    The left thalamic reticular nucleus (TRN). A thin, GABAergic,
    sheet-like structure that forms a shell around the LATERAL SURFACE
    of the left thalamus, between the thalamus and the internal
    capsule. It is structurally unique in the thalamus:
        - It is NOT a relay: it does not project to the cortex; it
          projects ONLY to the thalamic relay nuclei (and the thalamic
          relay nuclei project back to it).
        - It is the ONLY INHIBITORY COMPONENT of the thalamus: all of
          its outputs are GABAergic.
        - It has a TOPOGRAPHIC ORGANIZATION into sectors that
          correspond to the thalamic nuclei it gates: the visual
          sector gates the LGN and pulvinar; the auditory sector gates
          the MGN; the somatosensory sector gates VPL/VPM; the motor
          sector gates VA/VL; the limbic/association sectors gate the
          anterior, medial, and lateral groups. Each sector receives
          collaterals from the thalamo-cortical and cortico-thalamic
          axons of the nucleus it gates.
    The topographic sectors are documented WITHIN this leaf, not as
    child nodes. Same convention as the habenula's LHb/MHb, the PVN's
    sub-populations, the pulvinar's three subregions, the MD's three
    subdivisions, and the LGN's layer-types.

    STRUCTURAL NOTE — GROUP-OF-ONE PATTERN:
    In the tree, reticular_nucleus/ is one of the six children of
    thalamus/left/ (alongside the anterior, lateral, medial,
    metathalamus, and ventral groups). It is a "group" in the sense
    that it is a thalamic subdivision, but it contains a SINGLE nucleus
    — itself. There are no sub-nuclei to defer to, so this file
    simultaneously serves as:
        - The group-level framing (the reticular nucleus is the
          thalamus's GABAergic gatekeeper).
        - The nucleus-level content (the TRN's anatomy, function,
          connections, and clinical facts).
    This is a new pattern in the tree: a "collapsed group" — the group
    and the leaf are the same file. Same discipline applies: no
    duplication, no children, one authoritative document.

    DISTINCTIONS (critical — three traps):

    - THALAMIC RETICULAR NUCLEUS vs. MIDBRAIN RETICULAR FORMATION (the
      primary trap; declared from the thalamus container and now
      canonically from the TRN side). The thalamic reticular nucleus
      is a thin GABAergic shell AROUND THE THALAMUS (a single
      continuous sheet; inhibitory; gates thalamo-cortical
      transmission). The midbrain reticular formation is a distributed
      AROUSAL SYSTEM in the BRAINSTEM (glutamatergic, cholinergic,
      monoaminergic; diffuse projections; arousal). Both are called
      "reticular," both modulate arousal, but they are entirely
      different structures with different mechanisms and different
      locations. Do not merge.

    - THALAMIC RETICULAR NUCLEUS vs. "RETICULAR NUCLEUS" (the
      misleading-name trap). The name "reticular" does not mean "part
      of the reticular activating system." The TRN is a THALAMIC
      structure (a subdivision of the thalamus), not a brainstem
      reticular structure. The "reticular" name refers to its
      net-like (reticular) appearance as a thin cellular sheet — not to
      the brainstem reticular formation. Do not move the TRN out of
      thalamus/ or treat it as a brainstem structure.

    - THALAMIC RETICULAR NUCLEUS vs. THALAMIC RELAY NUCLEI (the
      gate-vs-relay trap). The thalamic relay nuclei (LGN, MGN, VPL/
      VPM, VA/VL, MD, etc.) RELAY signals from subcortical or cortical
      sources to the cortex. The TRN is a GATE: it receives collaterals
      from those relays and INHIBITS them. The TRN does not project to
      the cortex; it projects back to the thalamus. Do not draft the
      TRN as "another thalamic relay"; it is the thalamus's gatekeeper,
      not a relay.

Functional Mode:
    - Attentional gating (the TRN's primary role):
        * The TRN gates the flow of information through the thalamus:
          it receives collaterals from thalamo-cortical axons (as they
          pass through the shell en route to the cortex) and from
          cortico-thalamic axons (as they pass through en route to
          the thalamus), integrates this information, and inhibits the
          thalamic relay nuclei accordingly.
        * The TRN's attentional role is to SELECT which thalamic
          channels are amplified (via reduced TRN inhibition) and
          which are suppressed (via increased TRN inhibition). It is
          the anatomical substrate of selective attention — the
          thalamic component of the brain's attentional filter.
        * The TRN's topographic sectors gate their corresponding
          nuclei: for example, the visual sector gates the LGN and
          pulvinar, selecting which visual information reaches V1 and
          the visual association cortices.
    - State gating — sleep-wake (the TRN's second role):
        * The TRN gates the transition between wakefulness and sleep
          via its inhibitory control of the thalamic relay nuclei. In
          sleep, increased TRN inhibition suppresses sensory throughput
          through the thalamus (the thalamus becomes the "closed gate"
          of sleep).
        * SLEEP SPINDLES: the TRN generates sleep spindles (11–15 Hz
          oscillatory bursts during NREM sleep) via its reciprocal
          inhibition of thalamic relay nuclei. The TRN-to-thalamus
          and thalamus-to-TRN loops are the anatomical basis of the
          spindle-generating circuit. Sleep spindles are a hallmark
          of NREM sleep and are thought to protect sleep from
          interruption by sensory input.
    - Absence epilepsy (the TRN's third role — the pathological
      variant of state gating):
        * The TRN's spindle-generating circuit is the anatomical
          substrate of ABSENCE SEIZURES: in absence epilepsy, the
          normal spindle oscillation is pathologically amplified into
          a 3-Hz spike-and-wave discharge, which causes a brief loss
          of consciousness. The TRN is a key node in the
          cortico-thalamo-cortical circuit that generates
          spike-and-wave discharges.
    - Cortico-thalamic and thalamo-cortical coupling (the TRN's fourth
      role):
        * The TRN is the mediator of cortico-thalamo-cortical
          coupling: it receives collaterals from BOTH the thalamo-
          cortical axons and the cortico-thalamic axons, and it
          inhibits the thalamic relay nuclei. The TRN is therefore
          positioned to modulate the entire thalamo-cortical loop,
          not just the sensory input.
    - The TRN is therefore the THALAMUS'S GATEKEEPER: it does not
      relay signals; it GATES them. Its functions (attentional
      selection, sleep-wake state gating, spindle generation, absence
      seizure generation) all derive from its inhibitory control of
      the thalamic relay nuclei.

    - CLINICAL FACTS (the TRN's defining clinical anchors):
        * ABSENCE EPILEPSY (the TRN's most established clinical
          anchor): the TRN-cortex-thalamus circuit is the anatomical
          substrate of absence seizures (3-Hz spike-and-wave
          discharges; brief loss of consciousness). The TRN is a
          principal node in the absence-seizure circuit and a target
          for anti-absence drugs (ethosuximide suppresses TRN
          T-type calcium currents).
        * SLEEP SPINDLE DYSREGULATION (investigational): altered TRN
          function has been implicated in insomnia and in sleep
          spindle abnormalities; the evidence is thinner than the
          absence-epilepsy finding.
        * TRN DBS FOR EPILEPSY (investigational): TRN DBS has been
          investigated as a treatment for medication-refractory
          epilepsy (particularly for absence and other generalized
          seizures); the evidence is preliminary.
        * ATTENTION AND THALAMIC GATING (research): the TRN is
          implicated in attention disorders and in thalamic gating
          dysfunction in schizophrenia, but the TRN-specific
          clinical evidence is preliminary. Document as research/
          investigational.
        * The TRN's clinical anchor is therefore ABSENCE EPILEPSY —
          a strong, established clinical fact comparable in scope to
          the LGN's contralateral homonymous hemianopia and the CM's
          DBS anchor.

Hormonal Modulation (minimal; the TRN is a thalamic gate):
    - The TRN is NOT a neuroendocrine structure.
    - Modulators: cholinergic (brainstem and basal forebrain),
      monoaminergic (brainstem), and histaminergic (TMN) inputs
      modulate TRN excitability and its gating of the thalamus.
      Document as arousal and state modulation, not endocrine
      modulation.
    - The TRN is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * short_term: the current arousal/attention state buffer (the
          TRN's gating is modulated by the current state).
    - Writes: none directly. The TRN is a GATE: it modulates the
      thalamic relay nuclei's throughput, not stored content.
    - The TRN's memory interface is THIN (short_term only): it does
      not read episodic, semantic, procedural, or reinforcement
      memory. It gates attention and state, not memory content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No TRN fragment. The TRN is a thalamic gate; the model prompt
      does not need a TRN block because the attentional and state
      signals it gates are already represented in the upstream
      arousal fragments (LPO, TMN, LC, raphe, orexin) and downstream
      (thalamic relay nuclei, cortex) fragments. The TRN's role is to
      GATE the thalamic relays, not to emit its own signal.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The TRN's clinical facts (absence epilepsy; spindle
      dysregulation; TRN DBS) are documented for completeness, but
      are not prompt fields.

Reciprocal Connections (left-side; the right side is in
../../right/reticular_nucleus/):

    Thalamo-cortical and cortico-thalamic collaterals (the TRN's
    inputs — the anatomically unique feature):
    - ← left thalamo-cortical axons (collaterals from EVERY left
      thalamic relay's axons as they pass through the TRN en route to
      the cortex; the TRN receives collaterals from every thalamic
      relay, not just one).
    - ← left cortico-thalamic axons (collaterals from cortical axons
      as they pass through the TRN en route to the thalamus; the TRN
      receives collaterals from every cortico-thalamic projection,
      not just one).
    - The collaterals are the TRN's defining anatomical feature: the
      TRN is a "coincidence detector" that receives information about
      every thalamo-cortical and cortico-thalamic signal, and it uses
      this information to gate the thalamic relays.

    Inhibitory outputs to thalamic relay nuclei (the TRN's
    gate-keeping outputs — topographic sectors):
    - → thalamus/left/lateral_nuclear_group/pulvinar (visual sector;
      GABAergic; the TRN gates the pulvinar).
    - → thalamus/left/metathalamus/lateral_geniculate_body (visual
      sector; GABAergic; the TRN gates the LGN).
    - → thalamus/left/metathalamus/medial_geniculate_body (auditory
      sector; GABAergic; the TRN gates the MGN).
    - → thalamus/left/ventral_nuclear_group/ventral_posterior_nucleus
      (somatosensory sector; GABAergic; the TRN gates VPL/VPM).
    - → thalamus/left/ventral_nuclear_group/ventral_anterior_nucleus
      and ventral_lateral_nucleus (motor sector; GABAergic; the TRN
      gates VA/VL).
    - → thalamus/left/anterior_nuclear_group (limbic sector;
      GABAergic; the TRN gates the anterior nuclei).
    - → thalamus/left/medial_nuclear_group (association/limbic
      sectors; GABAergic; the TRN gates the medial group).

    The TRN therefore projects to EVERY thalamic relay nucleus in the
    left thalamus, not to one specific nucleus. Its topographic
    sectors gate specific nuclei, but its overall role is to gate the
    WHOLE thalamus.

    Reciprocal thalamo-reticular connections:
    - ↔ every left thalamic relay nucleus (thalamo-reticular
      projections back to the TRN; the reciprocal loop that underlies
      spindle generation and attentional gating).

Notes:
    - Group-of-one leaf (left). Both group-level framing AND
      nucleus-level content are in this single file, since there are
      no sub-nuclei to defer to. The "collapsed group" pattern is new
      to the tree.
    - THE TRN IS THE THALAMUS'S GATE, NOT A RELAY: it does not project
      to the cortex; it projects only to the thalamic relay nuclei
      (inhibitory GABAergic). Do not draft it as "another thalamic
      relay."
    - THE TOPOGRAPHIC SECTORS (visual, auditory, somatosensory, motor,
      limbic, association) are documented WITHIN this leaf, not as
      child nodes. Same convention as the LGN's six layers, the MGN's
      three divisions, the pulvinar's three subregions, the MD's three
      subdivisions. Do not create visual_sector/, auditory_sector/,
      etc. as child nodes.
    - THE THREE TRAPS are reproduced in full:
        * Thalamic reticular nucleus vs. midbrain reticular formation
          (different structure, different mechanism).
        * Thalamic reticular nucleus vs. "reticular" name trap (the
          TRN is a thalamic structure, not a brainstem reticular
          structure).
        * Gate vs. relay trap (the TRN gates the thalamus, it doesn't
          relay to the cortex).
    - CLINICAL FACT: ABSENCE EPILEPSY is the TRN's defining clinical
      anchor — a strong, established clinical fact. The TRN-cortex-
      thalamus circuit generates spike-and-wave discharges; ethosuximide
      (anti-absence drug) suppresses TRN T-type calcium currents.
    - THE INVESTIGATIONAL FINDINGS (spindle dysregulation; TRN DBS for
      epilepsy; attention/schizophrenia research) are documented as
      "investigational" and "preliminary." Do not overclaim.
    - SLEEP SPINDLES are the TRN's most distinctive functional
      contribution: the TRN generates the 11–15 Hz spindle oscillations
      that hallmark NREM sleep. The TRN is therefore not just a "gate"
      in the sense of suppression — it also actively GENERATES sleep
      spindles via its reciprocal inhibition of the thalamic relays.
    - THE TRN PROJECTS TO EVERY THALAMIC RELAY, not one specific relay:
      its topographic sectors gate specific nuclei, but its overall
      role is to gate the WHOLE thalamus. This is why the TRN's
      reciprocal connection list is a list of "every left thalamic
      relay nucleus," not a single target.
    - NO FRAGMENT: same as the whole thalamus. The TRN is a gate, not
      a state-emitter. The arousal state is carried by the upstream
      arousal fragments.
    - THE "RETICULAR" NAME is misleading: it refers to the TRN's
      net-like appearance, not to the brainstem reticular formation.
      Do not move the TRN out of thalamus/ or treat it as a brainstem
      structure.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, histamine,
      GABA, glutamate); memory/stores/ (short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/.
"""