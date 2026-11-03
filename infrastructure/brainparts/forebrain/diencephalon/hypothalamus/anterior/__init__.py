"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior
Anatomical Role:
    The anterior (chiasmatic) division of the hypothalamus is the rostral
    third of the hypothalamus, situated above and around the optic chiasm
    and bordered rostrally by the lamina terminalis. It contains the
    brain's master circadian pacemaker (suprachiasmatic nucleus), the
    magnocellular neurosecretory neurons (supraoptic and paraventricular
    nuclei), the primary thermoregulatory and sleep-promoting region
    (preoptic area), and the anterior hypothalamic nucleus
    (parasympathetic/thermoregulatory control).

    Structurally, the anterior division is organized into a **lateral
    area** and a **medial area**, each of which is **bilateral**
    (left/right). The nuclei of functional interest sit at the leaves of
    this hierarchy, not as direct children of anterior/.

Functional Mode:
    - Circadian timing: suprachiasmatic nucleus (SCN) is the master
      pacemaker; entrains to light via the retinohypothalamic tract and
      drives circadian rhythms across the body.
    - Magnocellular neurosecretion: supraoptic and paraventricular nuclei
      produce vasopressin (ADH) and oxytocin, transported to the posterior
      pituitary for release.
    - Parvocellular neurosecretion: paraventricular nucleus produces CRH,
      TRH, and somatostatin for the hypophyseal portal system (HPA, HPT,
      growth axes).
    - Thermoregulation: preoptic area is the primary thermoregulatory
      center (heat loss and heat conservation).
    - Sleep promotion: preoptic area (especially the ventrolateral
      preoptic nucleus, VLPO) promotes non-REM sleep.
    - Parasympathetic control: anterior hypothalamic nucleus.
    - Osmoregulation: supraoptic and paraventricular nuclei sense plasma
      osmolarity and drive vasopressin release.

Hormonal Modulation (anterior-division summary; per-nucleus wiring in
leaves):
    - HPA: CRH (PVN output); cortisol (feedback).
    - HPT: TRH (PVN output); thyroid hormones (feedback).
    - Growth: somatostatin (PVN and periventricular output); GHRH
      (arcuate, in tuberal division, not here); IGF-1 feedback.
    - Fluid: vasopressin (SON, PVN outputs); angiotensin II and ANP
      (inputs).
    - Social: oxytocin (PVN, SON outputs).
    - Circadian: light (retinohypothalamic → SCN); melatonin (pineal
      feedback → SCN).
    - Thermoregulation: prostaglandins, pyrogens modulate preoptic area.
    - Neuro modulators: norepinephrine, serotonin, acetylcholine,
      histamine, orexin modulate SCN and preoptic circuits.
    - Detailed per-nucleus wiring lives in each leaf file.

Memory Interfaces (anterior-division summary):
    - Reads: episodic (homeostatic and stress history), emotional_valence
      (stress/aversive tags), temporal_sequence_learning (circadian
      context), short_term (current osmotic/thermal/sleep drive).
    - Writes: none directly. The anterior division emits state signals
      (hormones and neural), not stored content. It contributes to the
      homeostatic state vector via hormone outputs.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The anterior division contributes three distinct fragments to the
      homeostatic state block assembled by hypothalamus/, applied after
      the hypothalamus preamble:
        (1) Circadian fragment (SCN):
            "Circadian phase: [day/night]. Entrained: [yes/no]. If
             night, bias toward reduced arousal and reflective framing."
        (2) Osmotic/fluid fragment (SON/PVN):
            "Plasma osmolarity: [normal/high]. Thirst drive: [0-1].
             If high, surface fluid-seeking priorities and reduce
             extraneous output."
        (3) Thermoregulatory/sleep fragment (preoptic area):
            "Thermal state: [comfortable/cold/hot]. Sleep drive: [0-1].
             If high sleep drive, reduce verbosity and favor calm tone."
    - The PVN's CRH/TRH/somatostatin outputs feed the HPA/HPT/growth
      fragments documented in hypothalamus/; they do not emit their own
      fragment (avoid double-counting).
    - Fragments are emitted whenever the parent homeostatic state block
      is emitted (always), even at baseline values.

Children (actual hierarchy — two levels of containers before the nuclei):
    - lateral_area/
        ├── left/
        │   ├── anterior_part_of_lateral_nucleus/  (hypocretin/orexin
        │   │                                         input; arousal)
        │   ├── part_of_supraoptic_nucleus/         (osmosensory)
        │   ├── periventricular_preoptic_nucleus/   (GnRH regulation;
        │   │                                         sleep)
        │   └── preoptic_area/
        │       └── lateral_preoptic_nucleus/       (sleep-promoting,
        │                                             VLPO-adjacent)
        └── right/  (mirror)
    - medial_area/
        ├── left/
        │   ├── anterior_hypothalamic_nucleus/      (parasympathetic;
        │   │                                         thermoregulation)
        │   ├── paraventricular_nucleus/            ★ CRH, TRH,
        │   │                                         somatostatin, oxytocin,
        │   │                                         vasopressin; autonomic
        │   │                                         control
        │   ├── preoptic_area/
        │   │   ├── medial_preoptic_nucleus/
        │   │   │   ├── inah_1/  (GnRH pulse modulation)
        │   │   │   ├── inah_2/  (GnRH pulse modulation)
        │   │   │   ├── inah_3/  (GnRH pulse modulation)
        │   │   │   └── inah_4/  (GnRH pulse modulation)
        │   │   └── median_preoptic_nucleus/        (GnRH regulation)
        │   ├── suprachiasmatic_nucleus/            ★ Master circadian
        │   │                                         pacemaker
        │   └── supraoptic_nucleus/                 ★ Vasopressin,
        │                                             oxytocin (magnocellular)
        └── right/  (mirror)

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each leaf owns its own specification.
    - The tree nests nuclei two levels below anterior/ (via
      lateral_area|medial_area → left|right → nucleus). Do not create
      direct children of anterior/ — the hierarchy is authoritative.
    - The preoptic_area name appears in BOTH lateral_area/ and
      medial_area/, with different children in each. Do not merge them;
      they are anatomically distinct (lateral preoptic vs medial preoptic
      regions).
    - Twelve right-hemisphere files (lateral_area/right/*, medial_area/
      right/*) are delta mirrors of their left counterparts. Use the
      habenular_nuclei/right/ delta convention.
    - The four INAH nuclei (inah_1–4) are very small; consider documenting
      them as short leaf files (like Tier 2 organs — hormone role is
      primary, memory minimal).
    - This file is a sub-container of the hypothalamus hub. The hub
      (hypothalamus/__init__.py) named these nuclei; this file maps
      the actual hierarchy.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/02_* (HPA), 01_* (HPG), 03_* (HPT, growth),
      05_* (monoamines), 06_* (social), 07_* (fluid), 10_* (circadian);
      memory/stores/; gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * suprachiasmatic_nucleus/left|right ↔ pineal_gland (via SCN →
          PVN → spinal cord → SCG → pineal; canonical circadian loop)
        * supraoptic_nucleus/left|right ↔ pituitary_gland/posterior
          (vasopressin, oxytocin)
        * paraventricular_nucleus/left|right ↔ pituitary_gland/anterior
          (CRH, TRH, somatostatin) and posterior (oxytocin, vasopressin)
        * paraventricular_nucleus/left|right ↔ brainstem autonomic
          nuclei (sympathetic/parasympathetic outflow)
        * preoptic_area/* ↔ amygdala and brainstem (thermoregulatory,
          sleep circuits)
    - Connects upward to hypothalamus/.
"""