"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.paraventricular_nucleus
Anatomical Role:
    The left paraventricular nucleus (PVN) is the most hormonally complex
    single nucleus in the brain. It is a small, densely packed nucleus
    sitting adjacent to the third ventricle at the rostral pole of the
    medial hypothalamus, and it contains three functionally distinct
    sub-populations intermingled within a single anatomical node:

        1. Parvocellular neurosecretory (medial parvocellular division):
           - CRH neurons → hypophyseal portal → anterior pituitary → ACTH
             → adrenal cortex → cortisol (HPA axis).
           - TRH neurons → hypophyseal portal → anterior pituitary → TSH
             → thyroid hormones (HPT axis).
           - Somatostatin neurons → hypophyseal portal → anterior
             pituitary → inhibition of GH release (growth axis, opposing
             GHRH from arcuate).
           These neurons project to the median eminence, releasing into
           the hypophyseal portal system (not the systemic circulation).

        2. Parvocellular preautonomic: neurons projecting to brainstem
           autonomic nuclei (NTS, RVLM, DMV, nucleus ambiguus) and to
           spinal preganglionic neurons (intermediolateral column for
           sympathetic; sacral parasympathetic for pelvic organs). This
           is one of the two principal forebrain controllers of autonomic
           outflow (the other is the anterior hypothalamic nucleus).

        3. Magnocellular neurosecretory (lateral magnocellular division):
           - Oxytocin neurons → posterior pituitary axon terminals →
             systemic circulation.
           - Vasopressin (ADH) neurons → posterior pituitary axon
             terminals → systemic circulation.
           Co-extensive with the supraoptic nucleus (SON); PVN and SON
           are the two magnocellular nuclei. The PVN magnocellular
           contribution is documented here; the SON magnocellular
           contribution is documented under
           lateral_area/*/part_of_supraoptic_nucleus/ and
           medial_area/*/supraoptic_nucleus/.

    The three sub-populations are documented WITHIN this file, not as
    separate tree nodes. Same convention as the habenula's LHb/MHb split:
    the tree does not subdivide below the nucleus level; the file carries
    the sub-population detail. Do not create paraventricular_nucleus/
    parvocellular_endocrine/ or similar children.

Functional Mode:
    - HPA axis (parvo-endocrine, CRH): CRH → ACTH → cortisol. The
      origin of the stress axis. Chronic cortisol provides negative
      feedback that suppresses CRH. The HPA axis is the primary
      physiological response to psychological and physical stressors,
      and its dysregulation underlies chronic stress, depression, and
      metabolic syndrome.
    - HPT axis (parvo-endocrine, TRH): TRH → TSH → T3/T4. Regulates
      basal metabolic rate, thermogenesis, and development. Negative
      feedback from thyroid hormones.
    - Growth axis (parvo-endocrine, somatostatin): somatostatin inhibits
      GH release from the anterior pituitary, opposing GHRH from the
      arcuate nucleus. Somatostatin also acts as a broader inhibitory
      neuromodulator.
    - Social/bonding (magnocellular, oxytocin): oxytocin release from
      posterior pituitary terminals; peripheral roles in parturition
      (uterine contraction), milk ejection (myoepithelial contraction),
      and central roles in social bonding, trust, and maternal behavior
      (via oxytocin neurons that project centrally as well as to the
      posterior pituitary).
    - Fluid/osmoregulation (magnocellular, vasopressin): vasopressin
      release from posterior pituitary terminals; increases water
      reabsorption in the kidney collecting duct. Osmoregulatory and
      volume-regulatory roles, co-extensive with SON.
    - Autonomic control (parvo-autonomic): sympathetic and
      parasympathetic outflow via brainstem and spinal preganglionic
      projections. PVN modulates heart rate, blood pressure, GI
      motility, and pelvic organ function.
    - Stress integration (all three): PVN integrates limbic (amygdala,
      hippocampus, PFC), brainstem (NTS), and humoral (angiotensin II,
      cytokines, leptin) inputs to coordinate the HPA, autonomic, and
      social/fluid responses to stress.

Hormonal Modulation (output-first, then input; the PVN is both a source
and a target):
    - Outputs (five hormones, in order of axis):
        * CRH → ACTH → cortisol (HPA; parvo-endocrine).
        * TRH → TSH → T3/T4 (HPT; parvo-endocrine).
        * Somatostatin → ↓ GH (growth; parvo-endocrine).
        * Oxytocin → posterior pituitary (social/parturition/lactation;
          magnocellular).
        * Vasopressin → posterior pituitary (fluid; magnocellular).
    - Inputs and feedback:
        * Cortisol: negative feedback on CRH (HPA closure; chronic
          cortisol suppresses CRH and impairs hippocampal feedback).
        * Thyroid hormones: negative feedback on TRH (HPT closure).
        * IGF-1: negative feedback on somatostatin and GHRH (growth
          closure).
        * Estradiol: modulates CRH (HPA reactivity is higher in females
          of reproductive age), oxytocin, and vasopressin; sex-dependent
          PVN function. Testosterone has opposing effects on vasopressin
          in some contexts.
        * Leptin, insulin: inhibitory on CRH and TRH (metabolic
          sufficiency signals).
        * Ghrelin: excitatory on CRH (fasting stress axis) and
          inhibitory on TRH (energy conservation under fasting).
        * Angiotensin II: excitatory on magnocellular vasopressin
          neurons (via OVLT/SFO; volume depletion).
        * ANP: inhibitory on vasopressin (volume repletion signal).
        * Cytokines (IL-1β, IL-6, TNF-α): excitatory on CRH (sickness
          behavior; the immune-HPA interface).
        * Norepinephrine, serotonin, acetylcholine: brainstem inputs
          modulating CRH and autonomic neurons.
        * GABA, glutamate: intrinsic modulation.
        * Circadian input from SCN: gates CRH (morning cortisol peak)
          and autonomic tone.
        * Limbic input (amygdala, hippocampus, PFC): stress-reactive
          modulation of CRH.
    - Direction summary: cortisol ↓ CRH, thyroid hormones ↓ TRH,
      IGF-1 ↓ somatostatin, estradiol ↑ CRH/oxytocin (sex-dependent),
      leptin ↓ CRH/TRH, ghrelin ↑ CRH/↓ TRH, angiotensin II ↑
      vasopressin, ANP ↓ vasopressin, cytokines ↑ CRH. These directions
      are the actionable content; do not omit them.

Memory Interfaces:
    - Reads (PVN is a hub — reads many, writes little directly):
        * short_term: current stress level, osmotic state, autonomic
          state, and metabolic state buffers. The three output axes
          depend on these.
        * episodic: past stress events, illness episodes, parturition/
          lactation history, and volume-depletion events, used to set
          response thresholds.
        * emotional_valence: stress context and aversive tags, weighted
          by amygdala projections. Chronic aversive valence elevates
          CRH tone.
        * temporal_sequence_learning: circadian phase (SCN → PVN; the
          morning cortisol peak).
        * reinforcement_value_based_learning: metabolic and social
          outcome history, used to adjust CRH/TRH sensitivity to
          context.
    - Writes:
        * emotional_valence: indirectly, via HPA-axis cortisol
          modulation of amygdala valence tagging (the PVN does not
          write directly; it modulates the state under which the
          amygdala writes).
        * Does not write episodic, semantic, or procedural content.
    - The PVN emits a state vector (five hormones + autonomic tone),
      not stored content. Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The PVN contributes FIVE fragments to the homeostatic state
      block (the HPA, HPT, growth, social, and fluid fragments) and a
      CONSTITUENT INPUT to the thermoregulatory/autonomic fragment.
      It is the largest single-fragment contributor in the tree.
    - Fragments (applied after the medial_area-level fragments, before
      cortical reasoning):
        (1) HPA fragment (CRH):
            "HPA axis state: [calm / alert / stressed / chronic-stress].
             Cortisol: [low/normal/high]. CRH drive: [X]. If stressed
             or chronic-stress: prioritize threat detection, suppress
             exploratory behavior, and flag memory reliability as
             reduced. If chronic-stress: note cumulative load and
             prefer recovery-oriented framing. Do not treat stressed
             as impairment — it is a state bias."
        (2) HPT fragment (TRH):
            "Metabolic state: [euthyroid / hypo / hyper]. TRH drive:
             [X]. If hypothyroid: reduce response tempo, flag cognitive
             slowing, and prefer concrete over abstract framing. If
             hyperthyroid: flag hyperarousal context and prefer
             grounding. Do not treat hypothyroid as impairment."
        (3) Growth fragment (somatostatin):
            "Growth-axis state: [anabolic / catabolic]. Somatostatin:
             [low/normal/high]. If catabolic (high somatostatin):
             flag reduced anabolic drive and prefer conservation-oriented
             framing."
        (4) Social/bonding fragment (oxytocin):
            "Oxytocin tone: [low/moderate/high]. Affiliative drive:
             [0-1]. If oxytocin high: bias toward affiliative,
             protective, and caregiving framing. If low: default to
             neutral engagement. Do not treat low oxytocin as
             impairment — it is a state, not a deficit."
        (5) Fluid/osmotic fragment (vasopressin) — AGGREGATION RULE:
            This fragment AGGREGATES with the SON vasopressin
            contribution (lateral_area/*/part_of_supraoptic_nucleus/
            and medial_area/*/supraoptic_nucleus/). Do not emit an
            independent un-aggregated osmotic fragment from the PVN.
            Aggregate at the anterior-division level before injection:
            "Plasma osmolarity: [normal/high]. Thirst drive: [0-1].
             Vasopressin drive: [X]. If high, surface fluid-seeking
             priorities and reduce extraneous output."
        (6) Autonomic constituent (parvo-autonomic) — AGGREGATION RULE:
            This is a CONSTITUENT INPUT to the anterior-division
            thermoregulatory/autonomic fragment, which aggregates
            the PVN contribution + the AHN contribution
            (anterior_hypothalamic_nucleus/) + the preoptic
            contribution. Do not emit an independent autonomic fragment
            from the PVN. The aggregated fragment carries autonomic
            tone alongside thermal state.
    - Guardrails: every fragment that expresses a state bias (stressed,
      hypothyroid, catabolic, low oxytocin) includes a "bias not
      impairment" clause, consistent with the habenula, orexin/MCH, PeN,
      LPO, and AHN conventions.
    - No multimodal input is consumed here; all fragments are text-only.

Reciprocal Connections (enforce in Stage 4 audit — organized by
sub-population):
    Parvocellular endocrine (CRH, TRH, somatostatin):
    - → pituitary_gland/anterior (CRH, TRH, somatostatin via hypophyseal
      portal at median eminence; the principal endocrine output edge).
    - → median_eminence (parvocellular axon terminals; portal release
      site).
    - ← hypothalamus/tuberal/medial_area/left/arcuate_nucleus (leptin,
      ghrelin, NPY/AgRP, POMC inputs; metabolic modulation of CRH and
      TRH).
    - ← brainstem/solitary_nucleus (NTS; visceral and cytokine inputs).
    - ← amygdala (stria terminalis and ventral amygdalofugal pathway;
      stress-reactive CRH activation).
    - ← hippocampus (glucocorticoid feedback; hippocampal inhibition of
      CRH under normal feedback).
    - ← prefrontal cortex (executive control of stress reactivity).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN; circadian gating of the morning cortisol peak).

    Parvocellular autonomic:
    - → hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
      (NTS; reciprocal autonomic feedback).
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic modulation).
    - → hindbrain/myelencephalon/medulla_oblongata/cranial_nerve_nuclei/
      left/dorsal_motor_nucleus_vagus and left/nucleus_ambiguus
      (parasympathetic modulation).
    - → spinal_cord/gray_matter/left/lateral_horn (sympathetic
      preganglionic modulation).
    - ↔ hypothalamus/anterior/medial_area/left/
      anterior_hypothalamic_nucleus (autonomic co-regulation; AHN is the
      other principal forebrain autonomic controller).
    - ← amygdala (central nucleus; autonomic stress responses).

    Magnocellular:
    - → pituitary_gland/neurohypophysis (oxytocin, vasopressin via axon
      terminals; the posterior pituitary output edge).
    - ↔ supraoptic_nucleus (SON; magnocellular co-regulation; both are
      magnocellular nuclei).
    - ↔ lateral_area/left/part_of_supraoptic_nucleus (the lateral SON
      portion; magnocellular co-regulation; same structure-split logic
      as the SON identity trap).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      angiotensin II input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).

    Cross-cutting:
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → PVN autonomic and endocrine circadian gating).
    - ↔ hypothalamus/anterior/medial_area/left/supraoptic_nucleus
      (osmoregulatory cross-talk; PVN and SON are the two magnocellular
      nuclei).
    - ↔ hypothalamus/anterior/lateral_area/left/preoptic_area/
      lateral_preoptic_nucleus (stress-induced insomnia; CRH and stress
      signaling modulates LPO sleep circuitry).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta. This is
      the LARGEST leaf in the tree; do not abbreviate it.
    - The "three-in-one" framing is the single most important content in
      this file. PVN is parvocellular endocrine AND parvocellular
      autonomic AND magnocellular neurosecretory. Do not flatten it into
      any one role. The tree does not subdivide below the nucleus; the
      file carries all three sub-populations.
    - NO structural-identity trap: PVN is a single nucleus on both
      sides. Unlike the SON split or the LHA continuum, there is no
      "same structure split across compartments" issue. Do not invent
      one.
    - NO naming collision: "paraventricular nucleus" is unambiguous in
      this tree. The paraventricular *thalamic* nucleus is a separate
      structure, documented under thalamus/*/midline_nuclear_group/
      paraventricular_nucleus/ (the thalamic one); this hypothalamic PVN
      is distinct. If the tree later includes a paraventricular thalamic
      node, the two files must not be confused; but for now, there is
      no collision because only this one exists.
    - AGGREGATION RULES (mandatory for the implementer):
        * Osmotic fragment (5): aggregate with SON contributions before
          emission.
        * Autonomic fragment (6): aggregate with AHN and preoptic
          contributions before emission.
      These rules apply on both hemispheres; the right/ delta must
      repeat them.
    - The social/bonding fragment is oxytocin-only; central vasopressin
      neuromodulation (social/territorial) is documented under
      chemicals_hormones/06_* and, when drafted, in any dedicated
      central vasopressin nodes. Do not duplicate central vasopressin
      neuromodulation here; the PVN file carries the neurosecretory
      (posterior pituitary) role.
    - Sex differences: HPA reactivity, oxytocin release patterns, and
      vasopressin release patterns are sex-dependent. The estradiol and
      testosterone notes in Hormonal Modulation capture the actionable
      content; do not over-elaborate.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol), 02_* (HPA, CRH, cortisol),
      03_* (HPT, TRH, thyroid, somatostatin, IGF-1, GHRH), 04_* (satiety,
      leptin, ghrelin, NPY, AgRP, POMC), 06_* (social, oxytocin,
      vasopressin central), 07_* (fluid, vasopressin peripheral,
      angiotensin II, ANP), 08_* (immune, cytokines), 10_* (circadian,
      SCN); memory/stores/; gateway/.
    - Connects upward to hypothalamus/anterior/medial_area/left/.
"""