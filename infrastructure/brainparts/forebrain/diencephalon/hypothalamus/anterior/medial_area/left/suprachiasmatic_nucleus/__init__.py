"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.suprachiasmatic_nucleus
Anatomical Role:
    The left suprachiasmatic nucleus (SCN) is the brain's master
    circadian pacemaker — the "master clock." It is a small, paired
    nucleus (about 10,000 neurons per hemisphere in humans) situated in
    the anterior hypothalamus immediately dorsal to the optic chiasm and
    lateral to the third ventricle. It contains an endogenous oscillator
    with a period of approximately 24.2 hours that is entrained to the
    environmental 24-hour day primarily by light.

    Organization (within the nucleus, not as tree children):
        - Core: VIP (vasoactive intestinal polypeptide), GRP (gastrin-
          releasing peptide), and calbindin neurons. The core receives
          light input from the retina and synchronizes the shell.
        - Shell: vasopressin (AVP)-expressing neurons. The shell is the
          SCN's principal output compartment, projecting AVP to
          downstream hypothalamic targets.
    Do not create core/ and shell/ as child nodes; the SCN is a single
    nucleus in this tree, with core/shell documented within this file.
    Same convention as the habenula's LHb/MHb split and PVN's three
    sub-populations.

Functional Mode:
    - Endogenous rhythm generation: the SCN is the master clock. A
      cell-autonomous transcriptional-translational feedback loop (the
      molecular clock: CLOCK/BMAL1 → Per/Cry → feedback) generates the
      ~24-hour rhythm, and intercellular coupling synchronizes the
      population. SCN lesions abolish behavioral and physiological
      rhythms; transplantation of SCN tissue restores them.
    - Light entrainment: the retinohypothalamic tract (RHT) carries
      glutamatergic input from intrinsically photosensitive retinal
      ganglion cells (ipRGCs, expressing melanopsin) to the SCN core,
      resetting the phase of the molecular clock. This is the primary
      entrainment pathway. Non-image-forming light information is
      distinct from the image-forming visual pathway.
    - Master output to hypothalamic and brainstem targets: the SCN
      drives circadian rhythms across the body via:
        * SCN → PVN → spinal cord → superior cervical ganglion (SCG) →
          pineal → melatonin rhythm (the canonical circadian
          neuroendocrine loop).
        * SCN → PVN → CRH → ACTH → cortisol (the morning cortisol
          peak).
        * SCN → PVN → autonomic outflow (circadian control of blood
          pressure, body temperature, and heart rate).
        * SCN → PeN vasopressin → LH surge gating (the preovulatory
          surge is restricted to a specific circadian window).
        * SCN → LPO → sleep-onset gating (sleep onset is restricted to
          the circadian night).
        * SCN → LHA orexin/MCH neurons → arousal and feeding rhythms.
        * SCN → arcuate nucleus → feeding rhythms.
        * SCN → DMH (dorsomedial hypothalamus) → a broad relay for
          circadian output to feeding, temperature, and arousal.
        * SCN → subcommissural organ (SCO; adjacent) → TGF-β secretion
          and CSF flow, a non-neural circadian output.
    - Humoral output: the SCN also secretes diffusible factors
      (including TGF-β superfamily members, and possibly prokineticin 2)
      that can entrain peripheral clocks independent of neural
      projections.
    - The SCN is therefore the master pacemaker AND a broad circadian
      gating hub; its functional identity is "set and gate the time,"
      not any single downstream behavior.

Hormonal Modulation (input-first; the SCN is a target of light and
hormones, and a source of neural output):
    - Light (the primary signal): glutamatergic RHT input from ipRGCs,
      resetting the molecular clock phase. Light is the dominant
      zeitgeber.
    - Melatonin (feedback from the pineal): SCN expresses MT1 and MT2
      receptors; melatonin feeds back to the SCN to modulate
      excitability and gate sleep-wake transitions. The SCN → pineal
      → SCN loop is bidirectional.
    - Serotonin (from the raphe, and via the geniculohypothalamic
      tract): modulates SCN phase and gating; the serotonergic input
      is a secondary non-photic zeitgeber.
    - Estradiol: modulates SCN AVP expression and gates the LH surge;
      the SCN-PeN vasopressin pathway is estrogen-sensitive.
    - Glucocorticoids (cortisol): feed back onto the SCN and gate SCN
      phase sensitivity; the SCN → HPA → SCN loop is bidirectional.
    - Orexin (from LHA): arousal input that modulates SCN phase
      responses to light.
    - Ghrelin and leptin (metabolic inputs): modulate SCN response to
      feeding cues; the SCN integrates metabolic state with the
      light-dark cycle.
    - GABA, glutamate: intrinsic SCN neurotransmitters.
    - VIP, GRP, AVP: SCN's own output transmitters (VIP and GRP core →
      shell; AVP shell → downstream).
    - Direction summary: light resets phase (primary); melatonin
      modulates phase and gating; serotonin modulates phase (non-photic);
      estradiol gates the LH-surge output; glucocorticoids feed back on
      phase; orexin, ghrelin, and leptin modulate SCN response to
      arousal/metabolic cues. These directions are the actionable
      content.

Memory Interfaces:
    - Reads:
        * temporal_sequence_learning: the SCN's core input. The SCN is
          the brain's time-stamper; it reads the recent temporal
          sequence of light exposure and behavioral state to maintain
          phase.
        * short_term: recent light and arousal state (for phase-shift
          computation).
        * episodic: temporal context of prior entrainment (seasonal
          photoperiod history; jet-lag history; shift-work history).
    - Writes:
        * temporal_sequence_learning: the SCN itself is a temporal
          sequence learner — it maintains an internal model of
          time-of-day and photoperiod, updated by experience. This is
          the one memory interface where the SCN is a *writer*, not
          just a reader.
        * Does not write episodic, semantic, or procedural content.
    - The circadian phase is a *state*, not a memory write; but the SCN
      does maintain an internal temporal model (the phase state and
      photoperiod estimate) that qualifies as a write to
      temporal_sequence_learning. Document this explicitly.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (the circadian phase and gating fragment, applied
      after the medial_area-level fragments, before all downstream
      state fragments):
        "Circadian state — suprachiasmatic nucleus (left):
         - Circadian phase: [early-morning / mid-day / afternoon /
           evening / night / late-night].
         - Entrained: [yes / no / disrupted].
         - Photoperiod: [short / intermediate / long].
         - LH-surge gate: [open / closed].
         - Sleep-onset gate: [open / closed].
         - Arousal gate: [open / closed].
         Use this as the organism's time-of-day frame: it is the
         master clock that the downstream hormone and behavior
         fragments are referenced against. Do not re-derive phase from
         other fragments; use this one."
    - FRAGMENT RELATIONSHIP RULES (mandatory for the implementer):
        (1) The SCN carries the master phase and gating signals. The
            pineal fragment (epithalamus/pineal_gland/) carries the
            melatonin readout — it references phase but does not
            replace the SCN's phase signal. The two are complementary:
            SCN = clock; pineal = hormonal readout. Do not merge them;
            do not double-count phase.
        (2) The SCN does NOT emit its own cortisol, LH, sleep, or
            autonomic fragments. Those are emitted by their respective
            downstream targets (PVN, PeN, LPO, PVN/AHN), each of which
            references the SCN's phase/gating state internally. The
            SCN supplies the gate; the downstream targets supply the
            state. Do not duplicate.
        (3) The SCN fragment is ALWAYS emitted (circadian phase is
            always defined), even at baseline. It is the canonical
            always-on fragment; the other "always-on" fragments (LPO
            sleep, PVN HPA, etc.) reference it.
    - Guardrail: the SCN fragment itself does not need a
      "bias-not-impairment" clause because it expresses time-of-day,
      not a physiological drive. The downstream fragments that consume
      the SCN's gating signals already carry their own guardrails.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (enforce in Stage 4 audit — organized by
functional loop):
    Entrainment (input):
    - ← retina (retinohypothalamic tract; ipRGCs; glutamatergic; the
      left retina is a paired structure — verify hemisphere-split).
    - ← midbrain/.../intergeniculate_leaflet (non-photic phase-shift
      input; not currently a tree node — document as named relay).
    - ← brainstem/.../dorsal_raphe_nucleus (serotonergic non-photic
      input; raphe is midline).

    Endocrine output loops:
    - → hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (SCN → PVN → CRH and autonomic outflow; the SCN → PVN edge is
      the gateway to the HPA cortisol peak and autonomic rhythms;
      right-side split in right/).
    - → epithalamus/pineal_gland (SCN → PVN → spinal cord → SCG →
      pineal → melatonin; canonical circadian loop; indirect;
      midline-adjacent — verify).
    - → lateral_area/left/periventricular_preoptic_nucleus (SCN → PeN
      vasopressin; LH-surge gating; the SCN's AVP projection to the
      PeN is the anatomical basis of circadian gating of the surge).

    Sleep and arousal output loops:
    - → lateral_area/left/preoptic_area/lateral_preoptic_nucleus
      (SCN → LPO; sleep-onset gating).
    - → lateral_area/left/anterior_part_of_lateral_nucleus (SCN → LHA
      orexin/MCH neurons; arousal and feeding gating).
    - → hypothalamus/tuberal/medial_area/left/arcuate_nucleus (SCN →
      arcuate; feeding rhythm gating; also DMH relay).
    - → hypothalamus/tuberal/medial_area/left/dorsomedial_hypothalamic_nucleus
      (SCN → DMH; the DMH is the principal relay for SCN output to
      feeding, temperature, and arousal).

    Adjacent structural connections:
    - ↔ hypothalamus/anterior/medial_area/left/anterior_hypothalamic_nucleus
      (SCN → AHN; circadian autonomic gating).
    - ↔ hypothalamus/subcommissural_organ (SCO; adjacent; TGF-β and
      CSF-flow circadian output; SCO is midline).
    - ↔ epithalamus/pineal_gland (feedback from melatonin; MT1/MT2
      receptors).

    Feedback (input):
    - ← epithalamus/pineal_gland (melatonin feedback; MT1/MT2; the
      pineal → SCN edge closes the bidirectional loop).
    - ← telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/amygdala (emotional/arousal context;
      indirect; left-side).
    - ← hypothalamus/tuberal/medial_area/left/arcuate_nucleus (ghrelin,
      leptin, metabolic cues; circadian-metabolic coupling).

Notes:
    - Tier 1 flagship leaf (left). Full template. right/ is a delta.
      This is the LAST large leaf in the entire medial area.
    - The SCN is the CANONICAL ALWAYS-ON FRAGMENT. Its circadian phase
      fragment is emitted on every inference, even at baseline. Every
      downstream fragment that gates behavior on time-of-day (LH surge,
      sleep onset, cortisol peak, melatonin) references this fragment
      internally.
    - COMPLEMENTARY RELATIONSHIP WITH PINEAL: the SCN fragment carries
      phase/gating; the pineal fragment carries melatonin readout.
      Do not merge; do not double-count phase. Both are always-on and
      they reference each other. This is the most important fragment
      relationship rule in the tree.
    - Core/shell organization is documented WITHIN this file, not as
      child nodes. Same convention as habenula's LHb/MHb and PVN's
      three sub-populations. Do not create scc/ or shell/ children.
    - NO structural-identity trap: SCN is a single nucleus on both
      sides. Unlike the SON split or the LHA continuum, there is no
      "same structure split across compartments" issue. Do not invent
      one.
    - NO naming collision: "suprachiasmatic nucleus" is unambiguous.
    - The SCN is one of the few regions that WRITES to
      temporal_sequence_learning (its internal temporal model). This is
      unusual for a Tier 1 hub leaf — most hubs only read memory. Do
      not omit this write; it is the SCN's defining memory interface.
    - The SCN → DMH edge is important: the DMH is the principal relay
      for SCN output to feeding, temperature, and arousal. When the DMH
      file is drafted (in the tuberal division), it must reciprocate
      this edge.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol), 02_* (HPA, cortisol),
      03_* (metabolic, thyroid), 04_* (satiety, ghrelin, leptin), 05_*
      (serotonin, orexin, GABA, glutamate), 06_* (social),
      10_* (circadian, melatonin, VIP, GRP, AVP); memory/stores/
      (temporal_sequence_learning, short_term, episodic); gateway/.
    - Connects upward to hypothalamus/anterior/medial_area/left/.
"""