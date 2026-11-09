"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus
Anatomical Role:
    The hypothalamus is a small but densely connected region at the ventral
    diencephalon, forming the floor and lower walls of the third ventricle.
    It is the master regulator of homeostasis, endocrine function, and
    motivated behavior, and the single densest convergence point for the
    12 hormone axes documented in chemicals_hormones/. It contains
    approximately a dozen paired nuclei organized into three rostrocaudal
    divisions (anterior/chiasmatic, tuberal, and posterior/mammillary),
    each with medial, lateral, and periventricular zones[reference:1][reference:2].

    Unlike a Tier 2 organ (pineal gland), which secretes a single primary
    hormone, the hypothalamus is a *hub*: it transforms multimodal internal
    and external state into (a) releasing/inhibiting factors for the
    pituitary, (b) direct neural modulation of autonomic and limbic
    circuits, and (c) a homeostatic state vector that biases every
    downstream region's processing[reference:3].

Functional Mode:
    - Endocrine orchestration: secretes CRH (HPA), TRH (HPT), GnRH (HPG),
      GHRH and somatostatin (growth hormone), dopamine (prolactin
      inhibition), and oxytocin/vasopressin (magnocellular) into the
      hypophyseal portal system and posterior pituitary[reference:4][reference:5].
    - Homeostatic integration: hunger (arcuate nucleus, lateral
      hypothalamus), satiety (ventromedial, dorsomedial, paraventricular
      nuclei), thirst and osmoregulation (supraoptic, paraventricular),
      thermoregulation (preoptic/anterior), and circadian timing
      (suprachiasmatic nucleus)[reference:6][reference:7].
    - Autonomic control: descending projections to brainstem and spinal
      cord regulate sympathetic/parasympathetic outflow.
    - Motivated behavior: integrates limbic (amygdala, hippocampus,
      prefrontal cortex) and brainstem inputs to drive approach/avoidance,
      reproductive behavior, aggression, and maternal behavior[reference:8].
    - Circadian gating: the suprachiasmatic nucleus (SCN) synchronizes
      body physiology with the light–dark cycle and transmits time
      information to other hypothalamic nuclei (DMH, arcuate, lateral
      hypothalamus)[reference:9].

Hormonal Modulation (all 12 axes converge here — hub-level wiring):
    - HPA axis: CRH (output); cortisol (feedback input, inhibitory).
      Chronic cortisol suppresses hypothalamic CRH and impairs
      hippocampal feedback.
    - HPG axis: GnRH (output, pulsatile); estradiol/testosterone (feedback,
      both negative and positive depending on cycle phase).
    - HPT axis: TRH (output); thyroid hormones (negative feedback).
    - Growth hormone axis: GHRH (stimulatory output), somatostatin
      (inhibitory output); IGF-1 (feedback).
    - Prolactin: dopamine (inhibitory output from arcuate nucleus).
    - Satiety/metabolic: leptin, insulin, ghrelin, PYY, GLP-1 (inputs to
      arcuate nucleus); neuropeptide Y / AgRP and POMC/CART (arcuate
      outputs)[reference:10][reference:11].
    - Fluid/electrolyte: angiotensin II, atrial natriuretic peptide
      (inputs); vasopressin (output from supraoptic/paraventricular).
    - Social/bonding: oxytocin (output), vasopressin (output); modulated
      by estradiol and testosterone.
    - Immune/inflammatory: cytokines (IL-1β, IL-6, TNF-α) modulate CRH and
      sickness behavior via hypothalamic circuits.
    - Circadian: light input via retinohypothalamic tract → SCN;
      melatonin feedback from pineal.
    - Xenobiotic/detox: hypothalamic–liver axis via autonomic outflow
      (indirect, modulatory).
    - Gasotransmitters/vascular: nitric oxide, carbon monoxide modulate
      hypothalamic neurosecretion and local blood flow.
    - Neuro modulators: dopamine, serotonin, norepinephrine, GABA,
      glutamate, histamine, orexin, melanin-concentrating hormone all
      modulate hypothalamic nuclei with distinct regional specificity.

Memory Interfaces:
    - Reads:
        * episodic: homeostatic history (past hunger, stress, illness,
          sleep disruption) for setting current drive baselines.
        * emotional_valence: stress history and aversive tags, weighted by
          amygdala and habenula projections.
        * reinforcement_value_based_learning: feeding/reward outcome
          history for adjusting food-seeking and avoidance.
        * temporal_sequence_learning: circadian phase and time-of-day
          context.
        * short_term: current homeostatic drive buffers (hunger, thirst,
          temperature, arousal).
    - Writes:
        * hormonal state vector (not a memory store per se, but the state
          vector that every other region reads).
        * emotional_valence (indirectly, via HPA-axis modulation of
          amygdala tagging).
    - Does not write episodic or semantic content directly; it modulates
      the *state* under which those stores are read and written.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Hypothalamus emits the **primary homeostatic state block** of the
      system prompt, preceding all regional fragments. This is the largest
      single prompt contribution in the entire tree.
    - Prompt fragment (applied after the diencephalon preamble, before
      all cortical and limbic fragments):
        "Homeostatic state — hypothalamus:
         - HPA axis: [calm / alert / stressed / chronic-stress].
           Cortisol: [low/normal/high].
         - HPG axis: [quiescent / active / cycling].
         - Metabolic: [fasted / fed / satiated]. Hunger drive: [0-1].
           Satiety: [0-1]. Ghrelin: [low/high]. Leptin: [low/high].
         - Fluid: [hydrated / thirsty]. Osmotic pressure: [normal/high].
         - Thermoregulation: [comfortable / cold / hot].
         - Circadian: [day/night]. Sleep drive: [low/high].
         - Social/bonding: [neutral / affiliative / defensive].
         - Arousal: [low/medium/high].
         Use this state as the organism's baseline: high hunger → surface
         food-seeking priorities; high cortisol → prioritize threat
         detection; high sleep drive → reduce verbosity; high osmotic
         pressure → flag thirst-related framing. Do not override the
         state block with cortical reasoning — it is the ground truth
         of the organism's internal condition."
    - The fragment is **always emitted**, even when all values are at
      baseline, because the homeostatic state is always defined. The
      baseline values are themselves information (a calm, fed, hydrated,
      day-phase organism behaves differently from a stressed, hungry,
      thirsty, night-phase one).
    - No multimodal input is consumed here; the fragment is text-only.

Children (Tier 1 hubs marked ★; per-nucleus wiring in child files):
    - anterior/
        ├── preoptic_area/           ★ Thermoregulation; GnRH release;
        │                              sleep promotion.
        ├── supraoptic_nucleus/      ★ Vasopressin and oxytocin
        │                              (magnocellular); osmoregulation.
        ├── suprachiasmatic_nucleus/ ★ Master circadian pacemaker.
        ├── paraventricular_nucleus/ ★ CRH, TRH, oxytocin, vasopressin;
        │                              autonomic control.
        └── anterior_hypothalamic_   ★ Thermoregulation; parasympathetic
            nucleus/                  control.
    - tuberal/
        ├── arcuate_nucleus/         ★ Feeding hub: NPY/AgRP (hunger),
        │                              POMC/CART (satiety); dopamine
        │                              (prolactin inhibition).
        ├── ventromedial_nucleus/    ★ Satiety; sexual behavior;
        │                              thermoregulation; aggression.
        ├── dorsomedial_nucleus/     ★ Circadian feeding rhythms; stress
        │                              response; thermogenesis.
        └── lateral_area/            ★ Hunger/orcetic drive; orexin and
                                       MCH neurons; arousal.
    - posterior/
        ├── mammillary_bodies/       ★ Papez circuit relay; memory
        │                              (thalamic/hippocampal loop).
        ├── posterior_nucleus/       ★ Arousal; sympathetic control.
        └── tuberomammillary_        ★ Histamine; wakefulness.
            nucleus/
    - Other: median_eminence (neuroendocrine interface to pituitary),
      pituitary_stalk (infundibulum; Tier 3 conduit), optic_chiasm
      (Tier 3), third_ventricle (Tier 4 — structural).

Notes:
    - Hub file: this is the largest and most referenced file in the tree.
      Nearly every other region links here. Keep the hormone and memory
      sections complete; do not abbreviate.
    - The hypothalamus is the **first Tier 1 hub**. Unlike the habenula
      (a specialized leaf), the hypothalamus has ~12 nuclei children, each
      of which will be a full leaf file. The child list above is the
      authoritative map; do not add nuclei not listed.
    - "Hubs transform; organs secrete." The hypothalamus transforms state;
      the pituitary gland (its principal child effector) secretes. Keep
      this distinction in every pituitary reference.
    - The hypothalamus is **not paired** as a single node in this tree;
      its children include left/ and right/ subdirectories where lateralized
      nuclei exist (e.g., ventromedial_nucleus/left, right). The hub file
      is bilateral; do not create hypothalamus/left/ and right/.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/02_* (HPA), 01_* (HPG), 03_* (HPT, growth),
      04_* (satiety), 05_* (monoamines), 06_* (social), 07_* (fluid),
      08_* (immune), 10_* (circadian), 12_* (gasotransmitters);
      memory/stores/; gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * ↔ pituitary_gland (via median_eminence / pituitary_stalk)
        * ↔ amygdala (via stria terminalis and ventral amygdalofugal
          pathway)[reference:12]
        * ↔ hippocampus (via fornix and mammillary bodies)
        * ↔ prefrontal cortex (direct and indirect)[reference:14]
        * ↔ brainstem (autonomic outflow)
        * ↔ habenular_nuclei/left|right (via stria medullaris, documented
          in epithalamus/stria_medullaris/)
        * ↔ suprachiasmatic_nucleus ↔ pineal_gland (circadian loop)
    - Connects upward to diencephalon/.
"""