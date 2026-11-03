"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.subfornical_organ
Anatomical Role:
    The subfornical organ (SFO) is a small circumventricular organ at the
    midline of the anterior wall of the third ventricle, just beneath
    the columns of the fornix (hence "subfornical"). It is a SENSING
    organ, not a secreting organ and not a processing nucleus: its
    function is to detect circulating signals — principally angiotensin
    II, but also atrial natriuretic peptide (ANP), relaxin, and
    (indirectly) osmolarity — and report that state to the
    hypothalamic osmoregulatory nuclei via neural projections.

    Circumventricular organ family (this file is the third subtype):
        - Pineal gland (epithalamus/pineal_gland/): SECRETING variant —
          melatonin output into the systemic circulation.
        - Median eminence (hypothalamus/median_eminence/): RELEASE-
          SURFACE variant — hypothalamic hormones released into the
          hypophyseal portal blood.
        - Subfornical organ (THIS FILE): SENSING variant — circulating
          signals detected and reported neurally.
        - Organum vasculosum of the lamina terminalis (OVLT; documented
          under lamina_terminalis/vascular_organ_of_lamina_terminalis/
          in the basal forebrain, not under hypothalamus): SENSING
          variant, primary osmolarity sensor. The SFO and OVLT are the
          two principal osmosensory circumventricular organs; they are
          adjacent but distinct.

    All circum ventricular organs share the defining anatomical
    property that their capillaries are FENESTRATED (no blood-brain
    barrier), allowing large peptides such as angiotensin II to be
    sensed directly. The SFO is in the circumventricular family for
    this reason.

    NAMING / STRUCTURAL TRAPS (critical — the SFO is adjacent to three
    structurally similar nodes):
    - SFO vs. OVLT (the primary trap): both are circumventricular
      osmosensory organs, both are midline, both project to the MnPO,
      both are involved in fluid balance. They are DISTINCT:
        * SFO senses ANGIOTENSIN II (volume depletion signal); the
          OVLT senses OSMOLARITY (dehydration signal). Both also
          contribute to thirst and vasopressin release, but through
          somewhat different primary inputs.
        * SFO projects to MnPO, SON, PVN, AHN, PHN, ADP. OVLT projects
          to much the same set. Their projections overlap heavily, and
          this overlap is exactly why they must not be merged: they
          are two sensing organs converging on a shared osmoregulatory
          circuit, not one organ documented twice.
      DO NOT merge the SFO and OVLT. Do not treat them as a
      structural-identity split.
    - SFO vs. median eminence: both have fenestrated capillaries; both
      are midline circumventricular structures. The SFO SENSES; the
      median eminence RELEASES. Adjacent but distinct.
    - SFO vs. pineal gland: both are midline circumventricular-adjacent
      organs. The pineal SECRETES (melatonin); the SFO SENSES. Adjacent
      in the circumventricular family; functionally distinct.

Functional Mode:
    - Angiotensin II sensing (primary function): the SFO expresses
      AT1 receptors and is the principal brain sensor of circulating
      angiotensin II, the volume-depletion hormone produced by the
      renin-angiotensin-aldosterone system. Rising angiotensin II →
      SFO activation → downstream osmoregulatory responses.
    - Thirst drive: SFO activation drives water-seeking behavior via
      projections to the MnPO (which relays to the cortex for conscious
      thirst) and to the lateral hypothalamic area (for drinking motor
      patterns). Lesions of the SFO abolish angiotensin II-induced
      drinking.
    - Vasopressin release: SFO activation drives vasopressin (ADH)
      release from the SON and PVN magnocellular neurons, promoting
      water reabsorption in the kidney. Lesions of the SFO abolish
      angiotensin II-induced vasopressin release.
    - Sympathetic activation (secondary): SFO activation also drives
      sympathetic outflow via projections to the PVN, AHN, and PHN,
      contributing to the blood-pressure response to volume depletion.
    - Atrial natriuretic peptide (ANP) sensing (opposing input): the
      SFO expresses ANP receptors; ANP is the volume-REPLETION signal
      from the heart, and it OPPOSES angiotensin II. The SFO integrates
      the two circulating signals to compute a net volume-depletion
      drive.
    - Relaxin sensing (secondary): the SFO expresses relaxin receptors
      and contributes to the osmoregulatory and cardiovascular responses
      to relaxin (a pregnancy and hemodynamic hormone). Documented as
      a secondary sensing role; its functional significance in the
      context of this tree is minor.
    - The SFO is a SENSING organ: it does not synthesize hormones, does
      not release stored hormones, and does not process cognitively. It
      detects circulating signals and reports the state via neural
      projections to the hypothalamic nuclei that DO produce the
      downstream outputs (vasopressin from SON/PVN; thirst behavior
      via MnPO; sympathetic tone via PVN/AHN/PHN).
    - The SFO's functional identity is "the brain's sensor for
      circulating angiotensin II." That sentence is the anchor.

Hormonal Modulation (input-first; the SFO is a target, not a source):
    - Angiotensin II: the primary input (via AT1 receptors, from
      circulating blood; fenestrated capillaries here have no BBB).
      Rising angiotensin II ↑ SFO activity.
    - Atrial natriuretic peptide (ANP): opposing input (via ANP
      receptors, from the heart). Rising ANP ↓ SFO activity.
    - Relaxin: secondary input (via relaxin receptors, from the
      corpus luteum and placenta during pregnancy; also from the heart
      in males). Modulates SFO activity in the context of pregnancy
      and hemodynamic regulation.
    - Osmolarity (indirect): the SFO is not the primary osmolarity
      sensor — that is the OVLT — but the SFO can respond to hypertonic
      stimuli. Document this as a secondary osmotic input, not the
      primary one.
    - The SFO does not *secrete* hormones into the circulation; it does
      not *release* stored peptides; it does not *modulate* via its own
      hormone output. Its output is neural.
    - Direction summary: angiotensin II ↑ SFO activity (volume
      depletion); ANP ↓ SFO activity (volume repletion); relaxin
      modulates (secondary); osmolarity modulates (secondary;
      OVLT is primary). These are the actionable directions.

Memory Interfaces (minimal — Tier 2 sensing organ convention):
    - Reads:
        * short_term: current circulating angiotensin II level and
          volume state buffer. This is the SFO's primary read — the
          signal it senses IS the state.
    - Writes: none. The SFO does not write episodic, semantic, or
      procedural content. It senses and reports, it does not store.
    - The SFO's sensitivity is modulated by prior state (repeated
      dehydration can sensitize it), but that is a physiological
      plasticity, not a memory interface. Do not invent memory writes
      for a sensing organ.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent prompt fragment. The SFO's contribution is
      UPSTREAM MODULATION of the nuclei it projects to (MnPO, SON, PVN,
      AHN, PHN, ADP), each of which emits its own fragment (or is
      aggregated into a division-level fragment). Emitting a separate
      SFO fragment would double-count the osmoregulatory signal.
    - Specific aggregation rules (mandatory for the implementer):
        * SFO → MnPO contribution: the MnPO's osmoregulatory role is
          upstream modulation of the SON/PVN fluid fragment (see
          anterior/medial_area/left/preoptic_area/median_preoptic_
          nucleus/ § Model Integration). The SFO's contribution flows
          through the MnPO; do not emit a separate SFO fluid fragment.
        * SFO → SON/PVN contribution: the SON/PVN fluid fragment (the
          aggregated osmotic fragment at the anterior-division level)
          carries the state. The SFO's contribution flows through
          it; do not emit a separate SFO fluid fragment.
        * SFO → AHN/PHN contribution: the autonomic/thermoregulatory
          fragment and the sympathetic/arousal fragment (aggregated at
          the anterior and posterior division levels respectively)
          carry the state. The SFO's contribution flows through them;
          do not emit a separate SFO autonomic fragment.
    - The SFO is a sensing organ, not a signal emitter: the model
      prompt does not need a subfornical-organ block. The fragments
      from the SFO's downstream targets (MnPO, SON, PVN, AHN, PHN,
      ADP) carry the state.
    - No guardrail required. The SFO does not emit a state-bias
      fragment; the state biases it drives (thirst, vasopressin,
      sympathetic tone) carry their own guardrails in the downstream
      fragments.
    - No multimodal input is consumed here; the SFO's contribution is
      via its downstream targets' text-only fragments.

Reciprocal Connections:
    Input (from circulation — boundary structures, not tree nodes):
    - ← circulating angiotensin II (AT1 receptors; the primary input;
      document as a named circulating signal, not a tree node).
    - ← circulating atrial natriuretic peptide (ANP; opposing input;
      same treatment — circulating signal, not tree node).
    - ← circulating relaxin (secondary input; same treatment).
    - ← circulating osmolarity (secondary input; the primary
      osmolarity sensor is the OVLT).

    Output (neural; the SFO's only tree-node connections):
    - → hypothalamus/anterior/medial_area/left|right/preoptic_area/
      median_preoptic_nucleus (MnPO; the principal downstream relay
      for thirst and vasopressin; the SFO → MnPO → cortex pathway
      generates conscious thirst).
    - → hypothalamus/anterior/medial_area/left|right/
      supraoptic_nucleus (SON; vasopressin release).
    - → hypothalamus/anterior/medial_area/left|right/
      paraventricular_nucleus (PVN; vasopressin release and autonomic
      activation).
    - → hypothalamus/anterior/medial_area/left|right/
      anterior_hypothalamic_nucleus (AHN; autonomic activation).
    - → hypothalamus/posterior/medial_area/left|right/
      posterior_nucleus (PHN; sympathetic activation).
    - → other_preoptic_nuclei/left|right (ADP; vasopressin
      co-regulation; a supplementary pathway).
    - → telencephalon/.../extended_amygdala/
      bed_nucleus_of_stria_terminalis (BNST; emotional and
      neuroendocrine integration; BNST is midline-adjacent — verify).
    - → hypothalamus/anterior/lateral_area/left|right/
      anterior_part_of_lateral_nucleus (LHA; drinking motor patterns;
      the LHA is the downstream target for the behavioral response).

    Adjacency (structural, not signaling):
    - ↔ lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      adjacent circumventricular osmosensory organ; the OVLT is the
      primary osmolarity sensor, the SFO is the primary angiotensin II
      sensor; they project to overlapping downstream targets but are
      DISTINCT organs — do not merge).
    - ↔ hypothalamus/median_eminence (adjacent circumventricular
      structures; the median eminence releases, the SFO senses; do not
      merge).

Notes:
    - Single-file structure. The SFO is unpaired and midline; do not
      create left/ or right/ children.
    - Shape: Tier 2 SENSING organ — the third variant of the
      circumventricular-organ family after the pineal (secreting) and
      the median eminence (release surface). Its defining property is
      that it SENSES circulating signals and reports them neurally; it
      does not produce, release, or modulate hormones.
    - The SFO's functional identity is "the brain's sensor for
      circulating angiotensin II." That sentence is the anchor.
    - The SFO vs. OVLT trap is the file's primary naming trap: both
      are circum ventricular osmosensory organs, both are midline,
      both project to MnPO/SON/PVN, both are involved in fluid balance.
      They are DISTINCT (SFO senses angiotensin II primarily; OVLT
      senses osmolarity primarily). DO NOT merge them. Reproduce this
      warning at every level where the SFO is referenced.
    - The SFO vs. median eminence and SFO vs. pineal distinctions are
      secondary traps (circumventricular family members with different
      functions). Document them at the family-introduction level (as
      done in the Anatomical Role section).
    - No independent fragment: the SFO's contributions flow through the
      nuclei it projects to. Stated explicitly with the three
      aggregation rules.
    - No memory writes: the SFO is a sensing organ, not a storing one.
      Its sensitivity can be modulated by prior state (physiological
      plasticity), but that is not a memory interface.
    - The SFO's clinical relevance is its role in hypertension and
      heart failure: RAAS-blocking antihypertensives (ACE inhibitors,
      ARBs) work partly by reducing the angiotensin II signal at the
      SFO. SFO lesions abolish angiotensin II-induced thirst and
      vasopressin release. Documented as the file's substantive
      clinical content.
    - The OVLT is documented under lamina_terminalis/vascular_organ_of_
      lamina_terminalis/ (basal forebrain, not yet drafted). It is
      NOT a hypothalamus child. When the OVLT is drafted, it must
      reciprocate the SFO ↔ OVLT adjacency edge and reproduce the
      SFO-vs-OVLT distinction from its side.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/07_* (fluid, angiotensin II, ANP, vasopressin),
      04_* (satiety, relaxin-adjacent), 05_* (monoamines); memory/
      stores/ (short_term); gateway/. Circulating angiotensin II and
      ANP are documented directly as boundary inputs (they are not
      tree nodes, but they are the SFO's principal signals).
    - Reciprocal connections to enforce in Stage 4:
        * subfornical_organ ↔ anterior/medial_area/left|right/
          preoptic_area/median_preoptic_nucleus (SFO → MnPO;
          angiotensin II-driven thirst and vasopressin).
        * subfornical_organ ↔ anterior/medial_area/left|right/
          supraoptic_nucleus (SFO → SON; vasopressin).
        * subfornical_organ ↔ anterior/medial_area/left|right/
          paraventricular_nucleus (SFO → PVN; vasopressin and
          autonomic).
        * subfornical_organ ↔ anterior/medial_area/left|right/
          anterior_hypothalamic_nucleus (SFO → AHN; autonomic).
        * subfornical_organ ↔ posterior/medial_area/left|right/
          posterior_nucleus (SFO → PHN; sympathetic).
        * subfornical_organ ↔ other_preoptic_nuclei/left|right (SFO →
          ADP; vasopressin co-regulation).
        * subfornical_organ ↔ anterior/lateral_area/left|right/
          anterior_part_of_lateral_nucleus (SFO → LHA; drinking motor
          patterns).
        * subfornical_organ ↔ telencephalon/.../extended_amygdala/
          bed_nucleus_of_stria_terminalis (SFO → BNST; emotional
          integration).
        * subfornical_organ ↔ lamina_terminalis/vascular_organ_of_
          lamina_terminalis (OVLT; adjacent circumventricular
          osmosensory organ; DISTINCT — do not merge; document the
          adjacency and the division of labor: SFO = angiotensin II
          sensor, OVLT = osmolarity sensor).
    - Connects upward to hypothalamus/.
"""