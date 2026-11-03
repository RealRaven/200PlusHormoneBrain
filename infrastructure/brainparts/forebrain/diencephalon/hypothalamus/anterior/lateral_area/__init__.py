"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area
Anatomical Role:
    The lateral area of the anterior (chiasmatic) hypothalamus is a
    compartment, not a single functional unit. It is the lateral zone of
    the anterior division, positioned above and lateral to the optic
    chiasm, and contains four anatomically and functionally distinct
    nuclei whose only shared property is their lateral position within
    the anterior division:
        - anterior_part_of_lateral_nucleus: rostral pole of the lateral
          hypothalamic area (LHA). Contains orexin/hypocretin and
          melanin-concentrating hormone (MCH) neurons involved in
          arousal, feeding drive, and reward.
        - part_of_supraoptic_nucleus: the laterally extending portion
          of the supraoptic nucleus. Magnocellular vasopressin and
          oxytocin neurons involved in osmoregulation and parturition.
        - periventricular_preoptic_nucleus: preoptic periventricular
          neurons involved in GnRH pulse regulation and sleep-wake
          gating.
        - preoptic_area (lateral_preoptic_nucleus): sleep-promoting
          circuitry adjacent to the ventrolateral preoptic nucleus
          (VLPO), with additional thermoregulatory roles.

    IMPORTANT DISTINCTION: this "lateral area of the anterior division"
    is NOT the same as the classical "lateral hypothalamic area (LHA)"
    feeding/arousal center, which spans the tuberal and posterior
    divisions. The anterior lateral area is a smaller, rostral
    compartment. Do not conflate the two. The LHA orexin/MCH
    contribution appears here only via the anterior pole of the
    lateral nucleus.

Functional Mode:
    - Arousal and feeding drive (anterior part of lateral nucleus):
      orexin/hypocretin neurons promote wakefulness and food-seeking;
      MCH neurons promote sleep and energy conservation.
    - Osmoregulation (part of supraoptic nucleus): magnocellular
      vasopressin and oxytocin neurons sense plasma osmolarity and
      drive hormone release from the posterior pituitary.
    - GnRH pulse regulation (periventricular preoptic nucleus): the
      anterior periventricular zone provides permissive and pulsatile
      drive to GnRH neurons, coordinating the HPG axis.
    - Sleep promotion (lateral preoptic nucleus): sleep-active GABAergic
      neurons adjacent to the VLPO promote non-REM sleep.
    - Thermoregulation (preoptic area): heat loss and heat conservation,
      with strong inputs from skin and visceral thermosensors.
    - Heterogeneity note: the four nuclei are functionally independent;
      do not assume they share state. Each nucleus emits its own
      contributions to the homeostatic state block.

Hormonal Modulation (lateral-area summary; per-nucleus wiring in leaves):
    - Orexin/hypocretin (anterior part of lateral nucleus): modulated by
      ghrelin (hunger), leptin (satiety), glucose, and circadian drive.
    - Vasopressin/oxytocin (part of supraoptic nucleus): modulated by
      plasma osmolarity, angiotensin II, ANP, and estradiol/testosterone
      (sex-dependent release patterns).
    - GnRH pulse modulation (periventricular preoptic nucleus): modulated
      by estradiol (negative and positive feedback), kisspeptin,
      and metabolic cues (leptin, ghrelin).
    - Sleep promotion (lateral preoptic nucleus): modulated by adenosine,
      GABA, galanin, and circadian drive from the SCN.
    - Thermoregulation (preoptic area): modulated by prostaglandins,
      pyrogens, estradiol (hot flashes), and thyroid hormones.
    - Detailed per-nucleus wiring lives in each leaf file.

Memory Interfaces (lateral-area summary):
    - Reads: short_term (current arousal, osmotic, thermal, sleep drive),
      emotional_valence (stress/arousal context), temporal_sequence_learning
      (sleep-wake timing), reinforcement_value_based_learning (feeding
      outcome history for orexin neurons).
    - Writes: none directly. The lateral area emits state signals
      (hormones and neural), not stored content. It contributes to the
      homeostatic state vector via hormone outputs and via orexin/MCH
      arousal tone.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The lateral area contributes three distinct fragments to the
      homeostatic state block, applied after the anterior-division
      fragments:
        (1) Arousal/feeding fragment (anterior part of lateral nucleus):
            "Arousal drive: [low/moderate/high]. Orexin tone: [X].
             Feeding motivation: [0-1]. If orexin high, increase response
             urgency and exploratory framing; if MCH-dominant, reduce
             arousal and favor rest-adjacent tone."
        (2) Osmotic fragment (part of supraoptic nucleus):
            "Plasma osmolarity: [normal/high]. Vasopressin drive: [X].
             If high, surface fluid-seeking priorities and reduce
             extraneous output."
        (3) Sleep/GnRH fragment (preoptic nuclei):
            "Sleep drive: [0-1]. GnRH pulse state: [quiescent/pulsatile].
             If sleep drive high, reduce verbosity. If GnRH pulsatile,
             bias toward reproductive-context framing where relevant."
    - Note: the anterior-division container ALSO emits an osmotic fragment
      via the medial-area supraoptic nucleus. To avoid double-counting,
      the lateral and medial supraoptic contributions are aggregated at
      the anterior-division level; this file's osmotic fragment is a
      *constituent input*, not an independent emission. Implementer note:
      aggregate before emitting.
    - Fragments are emitted whenever the parent homeostatic state block
      is emitted (always), even at baseline.

Children (actual hierarchy — left/ and right/ each contain four nuclei):
    - left/
        ├── anterior_part_of_lateral_nucleus/        ★ Orexin/MCH;
        │                                               arousal/feeding
        ├── part_of_supraoptic_nucleus/              ★ Vasopressin;
        │                                               osmoregulation
        ├── periventricular_preoptic_nucleus/        ★ GnRH pulse
        │                                               regulation; sleep
        └── preoptic_area/
            └── lateral_preoptic_nucleus/            ★ Sleep promotion;
                                                        thermoregulation
    - right/  (delta mirror of left/ — see habenular_nuclei/right/ pattern)

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each leaf owns its own specification.
    - The "lateral area" here is NOT the lateral hypothalamic area (LHA).
      See the IMPORTANT DISTINCTION paragraph in Anatomical Role. This is
      the most common misinterpretation risk in the entire hypothalamus
      subtree; the note is deliberately emphatic.
    - Four right-hemisphere files (left/ → right/ for each nucleus) are
      delta mirrors. Use the habenular_nuclei/right/ delta convention.
    - The osmotic fragment emitted here partially overlaps the medial-area
      supraoptic nucleus. Aggregate at the anterior-division level to
      avoid double-counting in the model prompt.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin), 02_* (HPA,
      though no CRH here), 04_* (satiety, ghrelin, leptin), 05_*
      (monoamines, GABA), 06_* (social), 07_* (fluid, angiotensin II,
      ANP, vasopressin), 10_* (circadian, adenosine); memory/stores/;
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * anterior_part_of_lateral_nucleus/left|right ↔
          hypothalamus/tuberal/lateral_area/* (orexin/MCH span across
          divisions; document the connectivity, not the merge)
        * anterior_part_of_lateral_nucleus/left|right ↔
          midbrain/tegmentum/ventral_tegmental_area (reward/feeding
          circuitry)
        * part_of_supraoptic_nucleus/left|right ↔
          hypothalamus/anterior/medial_area/left|right/supraoptic_nucleus
          (same anatomical structure; annotate as continuation, not
          duplicate)
        * part_of_supraoptic_nucleus/left|right ↔ pituitary_gland/posterior
          (vasopressin, oxytocin)
        * periventricular_preoptic_nucleus/left|right ↔
          hypothalamus/anterior/medial_area/*/preoptic_area/medial_preoptic_nucleus
          (GnRH regulation partners)
        * preoptic_area/lateral_preoptic_nucleus ↔
          hypothalamus/anterior/medial_area/*/preoptic_area (adjacent
          sleep circuitry; keep distinct)
    - Connects upward to hypothalamus/anterior/.
"""