"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.medial_area.posterior_nucleus.left
Anatomical Role:
    The left posterior hypothalamic nucleus (PHN). A small, densely
    packed nucleus in the left medial posterior hypothalamus, situated
    above the left mammillary body and just caudal to the left
    dorsomedial and ventromedial nuclei. It is the principal hypothalamic
    driver of sympathetic outflow and behavioral arousal, and the
    sympathetic complement of the left anterior hypothalamic nucleus
    (AHN).

    The PHN is DISTINCT from three neighboring structures:
        - The posterior part of the lateral nucleus (posterior LHA
          segment 3, documented under
          posterior/lateral_area/left/posterior_part_of_lateral_
          nucleus/): adjacent but functionally distinct. PHN = sympathetic
          output; posterior LHA = arousal drive via orexin.
        - The left anterior hypothalamic nucleus (AHN, documented under
          anterior/medial_area/left/anterior_hypothalamic_nucleus/):
          the sympathetic complement of the AHN's parasympathetic role
          — a complementary pair, not duplicates.
        - The left mammillary body (documented under
          hypothalamus/mammillary_bodies/left/; also referenced via
          the pointer at posterior/medial_area/mammillary_nuclei/
          left/): the PHN is a separate structure.

    The PHN has NO structural-identity trap and NO naming collision.
    Do not invent one. It is a single, unambiguously named nucleus.

Functional Mode:
    - Sympathetic outflow (primary function): the PHN projects to
      sympathetic preganglionic neurons in the spinal intermediolateral
      column (IML) via the rostroventrolateral medulla (RVLM), and to
      brainstem sympathetic centers (RVLM; locus coeruleus, LC; dorsal
      raphe). Activation increases heart rate, blood pressure,
      respiratory rate, and pupillary dilation. It is the descending
      hypothalamic command for the sympathetic component of the
      fight-or-flight response.
    - Behavioral arousal: the PHN contributes to cortical and
      behavioral arousal via projections to the brainstem reticular
      formation, the basal forebrain, and the intralaminar thalamic
      nuclei. It is one node in the ascending arousal system,
      complementing the orexin (LHA) and histamine (TMN) contributions.
    - Pupillary reflex: the PHN drives sympathetic pupillary dilation
      (mydriasis) via projections to the ciliospinal center of Budge
      (intermediolateral column, T1–T2), which projects to the
      superior cervical ganglion and then to the pupillary dilator
      muscle. This is the hypothalamic contribution to the pupillary
      light reflex and to sympathetic pupil responses to arousal. Note:
      the pupillary LIGHT reflex pathway (retina → pretectum →
      Edinger-Westphal → ciliary ganglion → pupillary constrictor) is
      distinct from this sympathetic pupillary dilation pathway; the
      two systems act in opposition, and the PHN drives the dilatory
      (sympathetic) side.
    - Stress response: the PHN is activated by acute stress (including
      psychological stress) and contributes to the sympathetic
      component of the stress response, complementing the HPA axis's
      endocrine component (CRH → ACTH → cortisol). The two components —
      neural (PHN → sympathetic) and endocrine (PVN → HPA) — are
      parallel and coordinated.
    - Complementary to the AHN: the left AHN drives parasympathetic
      outflow (rest-and-digest); the left PHN drives sympathetic
      outflow (fight-or-flight). The two are the parasympathetic and
      sympathetic poles of the left-hemisphere hypothalamic autonomic
      control system. They are reciprocally organized, and the Stage 4
      audit should treat them as a pair.

Hormonal Modulation:
    - Orexin (from the LHA orexin neurons): excitatory arousal input.
    - Monoamines (from brainstem arousal centers):
        * Norepinephrine (LC): excitatory arousal input.
        * Serotonin (dorsal raphe): modulatory.
        * Histamine (TMN): excitatory arousal input.
    - CRH / cortisol (stress-axis input): the PHN is activated by
      stress; CRH contributes to the sympathetic stress response.
    - Angiotensin II (via OVLT and SFO): excitatory input; sympathetic
      activation in response to volume depletion.
    - Direction summary: orexin ↑ PHN activity (arousal); norepinephrine
      ↑ PHN activity (arousal); histamine ↑ PHN activity (arousal);
      CRH ↑ PHN activity (stress); angiotensin II ↑ PHN activity
      (volume depletion). These are the actionable directions.
    - The PHN is primarily an OUTPUT nucleus: it does not synthesize
      hormones and is NOT a principal target of the 12 endocrine axes.
      Its modulators are arousal and stress signals (orexin,
      monoamines, CRH, angiotensin II), not the endocrine axes
      themselves. Do not pad with endocrine "modulators" that do not
      target it.

Memory Interfaces:
    - Reads:
        * short_term: current arousal state (sympathetic tone, pupillary
          state) and stress level buffers.
        * episodic: past arousal and threat history; the PHN's
          sensitivity to stress is shaped by prior experience.
        * emotional_valence: stress and aversion context; chronic
          aversive valence elevates PHN baseline sympathetic tone.
        * temporal_sequence_learning: circadian arousal gating (SCN →
          PHN); sympathetic tone has a circadian component (higher
          during the active phase).
    - Writes: none directly. The PHN drives somatic output (sympathetic
      and arousal), not stored content. It modulates the state under
      which other regions read and write memory, but does not itself
      write.
    - The arousal/sympathetic state is a *state*, not a memory write.
      Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (sympathetic/arousal fragment; applied after the
      posterior-division-level fragments, before the cortical reasoning
      fragments):
        "Sympathetic state — posterior hypothalamic nucleus (left):
         - Sympathetic tone: [low / moderate / high].
         - Arousal level: [low / moderate / high].
         - Pupillary state: [constricted / intermediate / dilated].
         - Stress response: [calm / acute-stress / chronic-stress].
         If sympathetic tone is high or arousal level is high:
         flag hyperarousal context and prefer grounding, slow-tempo
         framing. If stress response is acute-stress: acknowledge the
         stress context and prefer calm, structured responses. If
         chronic-stress: note cumulative load and prefer
         recovery-oriented framing. Do not treat high sympathetic tone
         or high arousal as impairment — these are state biases, not
         degradations of reasoning capacity."
    - The fragment is emitted whenever the posterior-division state block
      is emitted (always); sympathetic tone and arousal level are
      persistent state signals, not transient homeostatic states.
    - Guardrail: "do not treat high sympathetic tone or high arousal as
      impairment" — the PHN equivalent of the habenula's "does not
      silence reasoning" clause, and consistent with the AHN's
      parasympathetic counterpart wording. The pattern is now firmly
      established across nine guardrails in the tree (habenula, orexin/
      MCH, PeN, LPO, AHN, PVN, mammillary confabulation, SCN (none
      needed), PHN).
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (left-side; the right side is in ../right/):
    Sympathetic outflow (primary):
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic premotor output;
      the principal relay to spinal preganglionic neurons; RVLM is
      midline-adjacent — verify).
    - → spinal_cord/gray_matter/left/lateral_horn (sympathetic
      preganglionic output via the intermediolateral column; direct
      hypothalamic projection).
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus (LC;
      noradrenergic arousal and sympathetic co-activation; LC is
      midline-adjacent — verify).
    - → midbrain/tegmentum/dorsal_raphe_nucleus (dorsal raphe;
      serotonergic arousal co-activation; raphe is midline).

    Behavioral arousal:
    - → telencephalon/cerebral_hemispheres/left/subcortical/
      basal_forebrain (arousal; cortical activation via the basal
      forebrain cholinergic system).
    - → thalamus/left/midline_nuclear_group (intralaminar arousal
      relay; the midline/intralaminar nuclei are midline — verify;
      these arousal projections complement the posterior LHA's
      arousal projections to the thalamic PVT).

    Complementary pair:
    - ↔ hypothalamus/anterior/medial_area/left/
      anterior_hypothalamic_nucleus (AHN; parasympathetic complement;
      the two nuclei are the sympathetic and parasympathetic poles of
      the hypothalamic autonomic system; complementary pair, NOT
      duplicates; keep distinct).
    - ↔ hypothalamus/posterior/lateral_area/left/
      posterior_part_of_lateral_nucleus (posterior LHA segment 3;
      arousal drive via orexin cooperating with the PHN's sympathetic
      output; distinct nodes; document the cooperation).

    Input:
    - ← hypothalamus/anterior/lateral_area/left/
      anterior_part_of_lateral_nucleus (orexin arousal input from the
      LHA; the orexin neurons that excite the PHN; continuity edge is
      NOT applicable here — the LHA → PHN arousal input is a distinct
      edge, not the LHA continuum).
    - ← hypothalamus/anterior/medial_area/left/
      suprachiasmatic_nucleus (SCN → PHN; circadian autonomic gating;
      SCN is midline-adjacent — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      angiotensin II input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input;
      SFO is midline).
    - ← brainstem/.../solitary_nucleus (NTS; visceral and stress
      input; NTS is midline-adjacent — verify).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - The PHN is the LAST full leaf in the posterior division. After
      its right delta, the posterior division is complete.
    - The PHN is the SYMPATHETIC complement of the AHN
      (anterior/medial_area/left/anterior_hypothalamic_nucleus/). The
      two fragments use consistent "bias not impairment" guardrails;
      the AHN's is "do not treat sympathetic-dominance as impairment"
      (from the parasympathetic perspective); the PHN's is "do not
      treat high sympathetic tone or high arousal as impairment" (from
      the sympathetic perspective). The pair should be consistent in
      the Stage 4 audit.
    - The pupillary LIGHT reflex (pretectum → Edinger-Westphal →
      ciliary ganglion → constrictor) is DISTINCT from the sympathetic
      pupillary DILATION pathway (PHN → ciliospinal center →
      superior cervical ganglion → dilator). The two pathways act in
      opposition. The PHN drives the dilatory (sympathetic) side; the
      Edinger-Westphal nucleus (midbrain) drives the constrictor
      (parasympathetic) side. Do not conflate.
    - The PHN's endocrine content is minimal: it is an output nucleus
      (sympathetic command), not a neuroendocrine hub. Do not draft it
      as one.
    - NO structural-identity trap, NO naming collision: PHN is a single
      unambiguously named nucleus. Do not invent a trap.
    - The PHN ↔ AHN edge is a complementary pair, not a duplicate.
      Document it as such; do not flag as duplicate.
    - The PHN ↔ posterior LHA edge is arousal drive (LHA) vs.
      sympathetic output (PHN); document as cooperative, not
      duplicate.
    - The orexin → PHN arousal input (from the LHA) is a DISTINCT
      edge from the LHA continuity relationship (LHA segments 1/2/3).
      The PHN is not part of the LHA field; the orexin → PHN input is
      an efferent from the field to the PHN, not a continuity edge.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin, angiotensin II),
      05_* (monoamines, orexin, norepinephrine, serotonin, histamine),
      07_* (fluid, angiotensin II), 02_* (HPA, CRH); memory/stores/
      (short_term, episodic, emotional_valence, temporal_sequence_
      learning); gateway/.
    - Connects upward to hypothalamus/posterior/medial_area/
      posterior_nucleus/.
"""