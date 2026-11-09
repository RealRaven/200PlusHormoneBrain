"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.preoptic_area.median_preoptic_nucleus
Anatomical Role:
    The left median preoptic nucleus (MnPO) is a periventricular structure
    of the medial preoptic area, positioned along the lamina terminalis at
    the anterior wall of the third ventricle. It is the neural integrator
    of the medial preoptic area: it receives osmotic and angiotensin
    signals from the circumventricular organs (OVLT, SFO), integrates them
    with hormonal and visceral input, and modulates downstream nuclei
    (SON, PVN, GnRH neurons, brainstem cardiovascular centers). It is not
    a primary output nucleus — its state flows through the nuclei it
    modulates.

    DISTINCTIONS (critical — the MnPO acronym is used for multiple
    structures in this tree):
    - DISTINCT FROM THE LATERAL-AREA "MnPO": the "median preoptic
      nucleus" referenced in lateral_area/*/preoptic_area/
      lateral_preoptic_nucleus/ is the ventrolateral sleep-active
      population of the LPO/VLPO complex. THIS file's MnPO is the
      osmoregulatory/GnRH/cardiovascular population of the medial
      preoptic area. Two different structures share the acronym; the
      tree distinguishes them by location. Do not merge.
    - DISTINCT FROM MPN (sibling): the medial preoptic nucleus (MPN,
      ../medial_preoptic_nucleus/) is the maternal/sexual-behavior hub
      and the parent of the four INAH nuclei. THIS file's MnPO is the
      osmoregulatory/GnRH/cardiovascular integrator. They are siblings,
      not the same structure; they interact but are distinct nodes.
    - PREOPTIC COLLISION: this node is inside the MEDIAL preoptic area,
      distinct from lateral_area/*/preoptic_area/lateral_preoptic_nucleus/
      (the VLPO-adjacent sleep nucleus). Do not merge.

Functional Mode:
    - Osmoregulation and thirst (the primary function): MnPO is the
      principal neural integrator of osmotic and volume signals from
      the OVLT (osmotic) and SFO (angiotensin II, volume), projecting
      to the SON and PVN to modulate vasopressin release, and driving
      thirst behavior via projections to the cortex and downstream
      hypothalamic circuits. MnPO lesions impair drinking responses to
      hypertonicity and hypovolemia.
    - Cardiovascular control: MnPO projects to the NTS and the RVLM and
      modulates sympathetic and parasympathetic outflow, contributing to
      blood-pressure and heart-rate responses to volume changes.
    - GnRH regulation (permissive/modulatory): MnPO contributes to
      GnRH pulsatility via kisspeptin input (from the arcuate KNDy
      population and PeN) and direct projections to GnRH neurons. Its
      contribution is permissive/modulatory; the principal pulse
      generator is the arcuate KNDy population and the principal surge
      generator is the PeN. Do not overstate the MnPO's GnRH role.
    - Thermoregulation (minor, shared): MnPO shares preoptic
      thermoregulatory circuitry with the preoptic area broadly; document
      as a supporting role, not an anchor.
    - The nucleus is therefore an INTEGRATOR, not a primary output
      nucleus: it does not secrete hormones itself, and its state flows
      through the nuclei it modulates (SON, PVN, GnRH neurons, brainstem
      cardiovascular centers). This is the defining framing for the
      model integration section.

Hormonal Modulation (input-first; the MnPO is a target, not a source):
    - Angiotensin II: excitatory input via the SFO; the principal
      volume-depletion signal driving thirst and vasopressin release.
    - Plasma osmolarity: excitatory input via the OVLT; the principal
      osmotic signal.
    - Atrial natriuretic peptide (ANP): inhibitory input; volume
      repletion signal opposing angiotensin II.
    - Estradiol: modulates MnPO GnRH-regulatory output; sex-dependent.
    - Kisspeptin (from the arcuate KNDy population and PeN):
      permissive/modulatory input to GnRH regulation.
    - Norepinephrine, serotonin: brainstem inputs modulating MnPO
      osmoregulatory and cardiovascular output.
    - GABA, glutamate: intrinsic modulatory transmitters.
    - Direction summary: angiotensin II ↑ MnPO activity (volume
      depletion, thirst); osmolarity ↑ MnPO activity (osmotic thirst);
      ANP ↓ MnPO activity; estradiol ↑ MnPO GnRH-regulatory output;
      kisspeptin ↑ GnRH-regulatory output. These directions are the
      actionable content; do not omit them.

Memory Interfaces:
    - Reads:
        * short_term: current plasma osmolarity, volume state, and
          reproductive-hormonal state buffers. The osmoregulatory and
          GnRH-regulatory outputs depend on these.
        * episodic: past dehydration and volume-depletion events, and
          reproductive-cycle history, used to set response thresholds.
        * emotional_valence: stress context; stress suppresses
          GnRH-regulatory output and modulates thirst.
        * temporal_sequence_learning: circadian timing (SCN → MnPO);
          drinking and reproductive behavior have circadian components.
    - Writes: none directly. The MnPO is an integrator; it emits
      constituent signals to downstream nuclei, not stored content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The MnPO is a neural INTEGRATOR, not a primary output nucleus.
      Its state contributions flow through the nuclei it modulates.
      Specifically:
        (1) Reproductive contribution (permissive/modulatory): the MnPO
            emits a CONSTITUENT INPUT to the anterior-division
            reproductive fragment, aggregated with the MPN
            (../medial_preoptic_nucleus/) and the PeN
            (lateral_area/left/periventricular_preoptic_nucleus/)
            contributions. Do not emit an independent reproductive
            fragment from the MnPO; aggregate at the anterior-division
            level.
        (2) Fluid/osmotic contribution: the MnPO's osmoregulatory role
            is documented as UPSTREAM MODULATION of the SON and PVN. The
            anterior-division fluid/osmotic fragment (emitted by the
            SON/PVN aggregate) carries the state; the MnPO does not emit
            a separate fluid fragment. Do not double-count.
        (3) Cardiovascular/autonomic contribution: the MnPO's
            cardiovascular role is documented as UPSTREAM MODULATION of
            the PVN and the anterior hypothalamic nucleus. The
            anterior-division autonomic/thermoregulatory fragment
            aggregates the PVN + AHN + preoptic contributions; the MnPO
            does not emit a separate autonomic fragment. Do not
            double-count.
    - The MnPO's contribution to the model is therefore indirect:
      it modulates the fragments emitted by SON, PVN, MPN, PeN, and AHN.
      The file does not emit its own fragments; the implementer must
      not add them.
    - Guardrail (inherited, not restated): where the MnPO's downstream
      targets emit state-bias fragments, those fragments carry the
      standard "bias not impairment" guardrail. The MnPO does not add
      a separate guardrail.
    - No multimodal input is consumed here; the MnPO's contribution is
      through its downstream targets' text-only fragments.

Reciprocal Connections (organized by functional domain):
    Osmoregulatory:
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmotic input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).
    - → hypothalamus/anterior/medial_area/left/supraoptic_nucleus
      (modulation of vasopressin/oxytocin release; medial SON).
    - → hypothalamus/anterior/lateral_area/left/
      part_of_supraoptic_nucleus (modulation of vasopressin release;
      lateral SON).
    - → hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (modulation of vasopressin release and autonomic outflow).

    Cardiovascular:
    - → hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
      (NTS; feedback; NTS is midline-adjacent — verify).
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic modulation;
      RVLM is midline-adjacent — verify).
    - ↔ hypothalamus/anterior/medial_area/left/
      anterior_hypothalamic_nucleus (cardiovascular co-regulation).

    Reproductive (permissive/modulatory):
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area/
      medial_preoptic_nucleus (MPN; sibling; shared GnRH regulation;
      continuity edge, not duplicate-structure warning).
    - ↔ lateral_area/left/periventricular_preoptic_nucleus (PeN;
      shared GnRH regulation; continuity edge, not duplicate-structure
      warning).
    - ← hypothalamus/tuberal/medial_area/left/arcuate_nucleus (kisspeptin
      KNDy input; permissive on GnRH regulation).

    Cross-cutting:
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN; circadian gating; SCN is midline-adjacent — verify).
    - ↔ telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/amygdala (emotional/stress context;
      left-side).
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area (sibling
      preoptic sub-container; adjacent preoptic circuits; keep
      distinct).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - The MnPO is an INTEGRATOR, not a primary output nucleus. Its
      model contribution is through the nuclei it modulates, not as
      independent fragments. This is the defining framing; do not
      draft the MnPO as if it emitted its own fragments.
    - The MnPO acronym trap is the single most important content in
      this file: the "MnPO" here is the osmoregulatory/GnRH/
      cardiovascular MnPO; the "MnPO" in
      lateral_area/*/preoptic_area/lateral_preoptic_nucleus/ is the
      ventrolateral sleep-active population. Two different structures;
      do not merge. Reproduce this warning wherever MnPO is referenced.
    - The MPN distinction (sibling, distinct node) and the preoptic
      collision (medial vs. lateral preoptic area) are also reproduced
      above. Do not remove.
    - Continuity edges (not duplicate-structure warnings):
        * MnPO ↔ MPN (siblings; both GnRH-regulatory; distinct nodes).
        * MnPO ↔ PeN (both GnRH-regulatory; distinct nodes).
      The audit should not flag these as duplicates.
    - The MnPO does NOT emit independent fragments. Its reproductive
      contribution aggregates with MPN + PeN; its fluid role is
      upstream modulation of SON/PVN; its cardiovascular role is
      upstream modulation of PVN + AHN. Three aggregation points, zero
      independent fragments. State this explicitly for the implementer.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin), 05_*
      (GABA, glutamate, monoamines), 07_* (fluid, angiotensin II,
      ANP, vasopressin); memory/stores/; gateway/.
    - Connects upward to hypothalamus/anterior/medial_area/left/
      preoptic_area/.
"""