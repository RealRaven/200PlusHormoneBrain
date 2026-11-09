"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.other_preoptic_nuclei.left
Anatomical Role:
    The left "other preoptic nuclei" group. Contains the named preoptic
    nuclei that are not classified under the lateral_area or medial_area
    preoptic sub-trees, all in the left hemisphere, documented WITHIN
    this file (not as further child nodes):
        - Anteroventral periventricular nucleus (AVPV): a kisspeptin-
          expressing, sexually dimorphic periventricular nucleus. Female-
          larger, kisspeptin-dense; the principal estrogen-positive-
          feedback relay to GnRH neurons.
        - Anterodorsal preoptic nucleus (ADP): a small vasopressin-
          expressing nucleus adjacent to the AVPV; minor fluid-balance
          and social-behavior contributor.
        - Striohypothalamic nucleus: a small preoptic nucleus receiving
          striatal and limbic inputs; functionally poorly characterized.
        - Ventral preoptic area: the non-nucleated preoptic region
          adjacent to the lateral preoptic area; anatomically distinct
          from lateral_area/*/preoptic_area/ (which contains
          lateral_preoptic_nucleus/). Poorly characterized.
        - Other small preoptic cell groups: any preoptic nuclei not
          named above and not classified under lateral_area or
          medial_area. Documented as "poorly characterized" unless the
          literature establishes otherwise.

    The AVPV is the file's anchor. The other structures are documented
    for completeness but are secondary or poorly characterized. Do not
    flatten the file into a single coherent hub; it is a catalogue with
    an AVPV anchor.

    DISTINCTIONS (critical — preoptic collision and AVPV/PeN apply):
    - This file is NOT lateral_area/left/preoptic_area/ (the lateral
      preoptic area) and NOT medial_area/left/preoptic_area/ (the
      medial preoptic area). It is the "other" group.
    - AVPV ↔ PeN: the AVPV is DISTINCT from the periventricular preoptic
      nucleus (PeN, lateral_area/left/periventricular_preoptic_nucleus/)
      but they are adjacent kisspeptin populations that function as a
      continuum. The edge is a CONTINUITY EDGE, not a
      duplicate-structure warning. Do not merge.
    - AVPV's sexual dimorphism is the OPPOSITE of INAH-3's: AVPV is
      larger in females (estrogen-positive-feedback substrate); INAH-3
      is larger in males (SDN-POA homologue). They are different
      dimorphisms in adjacent regions. Do not conflate.

Functional Mode:
    - Estrogen positive feedback (AVPV; primary function): the AVPV
      kisspeptin neurons are the principal anatomical substrate for the
      estradiol positive feedback that triggers the preovulatory GnRH/LH
      surge. Rising estradiol in the late follicular phase activates
      AVPV kisspeptin neurons, which project to GnRH neurons and drive
      the surge. This is the female-specific complement to the PeN's
      tonic drive.
    - Sexual dimorphism (AVPV): the AVPV is larger and more kisspeptin-
      dense in females; its dimorphism is the anatomical substrate for
      the female-specific capacity to generate a GnRH surge. Distinct
      from the INAH-3 dimorphism (male-larger); do not conflate.
    - Vasopressin and fluid balance (ADP; secondary function): the ADP
      expresses vasopressin and contributes to water-balance regulation
      via projections to the SON/PVN axis. Minor compared with the SON/
      PVN contribution.
    - Social behavior (ADP; minor): vasopressinergic projections to
      limbic circuits contribute to social recognition and affiliative
      behavior. Minor; not the file's anchor.
    - Striohypothalamic and ventral preoptic (poorly characterized):
      these regions receive striatal and limbic inputs, but their
      specific functions are not well established. Document them
      factually without overclaiming.
    - The AVPV is therefore the file's functional anchor; the other
      nuclei are documented for completeness but should not be over-
      written.

Hormonal Modulation:
    - AVPV (the primary content):
        * Estradiol: the defining modulator. Rising estradiol (late
          follicular phase) ACTIVATES AVPV kisspeptin neurons → GnRH/LH
          surge. This is the positive-feedback direction (opposite to
          the arcuate's negative feedback).
        * SCN vasopressin: gates AVPV kisspeptin activity to the
          circadian window of the LH surge (SCN → AVPV, time-locked).
        * Progesterone: facilitates the surge after estradiol priming;
          modulatory.
        * Kisspeptin (intrinsic to AVPV; also from arcuate KNDy):
          amplifies the estradiol signal.
        * GABA, glutamate: intrinsic modulatory transmitters.
    - ADP (secondary content):
        * Vasopressin (output): the ADP releases vasopressin; it is a
          minor contributor compared with SON/PVN.
        * Estradiol: modulates ADP vasopressin expression.
        * Osmotic input via OVLT/SFO (indirect): modulates ADP activity.
    - Striohypothalamic and ventral preoptic: poorly characterized;
      document estradiol and limbic input as presumed, not established.
    - Direction summary: estradiol ↑ AVPV kisspeptin (surge); SCN
      vasopressin ↑ AVPV gating (circadian window); ADP outputs
      vasopressin. These are the actionable directions; do not omit.

Memory Interfaces:
    - AVPV reads:
        * short_term: current estradiol level, circadian phase (from
          SCN), and reproductive-state buffer.
        * episodic: past reproductive-cycle events (surge history).
        * emotional_valence: stress context; chronic stress suppresses
          the surge.
        * temporal_sequence_learning: circadian timing (SCN-gated) of
          the surge.
    - AVPV writes: none directly. It emits a state signal (kisspeptin
      activity), not stored content.
    - ADP reads:
        * short_term: current osmotic state.
    - ADP writes: none directly.
    - Striohypothalamic and ventral preoptic: no documented memory
      interfaces; do not invent.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent prompt fragment. The AVPV's contribution is a
      CONSTITUENT INPUT to the anterior-division reproductive fragment,
      aggregated with the PeN (lateral_area/left/periventricular_
      preoptic_nucleus/), MPN (medial_area/left/preoptic_area/
      medial_preoptic_nucleus/), and MnPO (medial_area/left/preoptic_
      area/median_preoptic_nucleus/) contributions. Do not emit a
      separate AVPV fragment; aggregate at the anterior-division level.
    - The ADP's vasopressin role is upstream of the SON/PVN fluid
      fragment (aggregated at the anterior-division level); the ADP
      does not emit a separate fluid fragment. Do not double-count.
    - The reproductive fragment (carried by MPN/PeN/MnPO) carries the
      standard "bias not impairment" guardrail; the AVPV does not add
      a new guardrail.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (left-side; the right side is in right/):
    AVPV (primary):
    - ↔ lateral_area/left/periventricular_preoptic_nucleus (PeN;
      AVPV/PeN CONTINUITY EDGE — kisspeptin continuum; not a
      duplicate-structure warning; this edge closes the deferred
      continuity).
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area/
      medial_preoptic_nucleus (MPN; adjacent preoptic GnRH-regulatory
      nodes).
    - ← hypothalamus/anterior/medial_area/left/suprachiasmatic_nucleus
      (SCN → AVPV; circadian gating of the LH surge; SCN is midline-
      adjacent — verify).
    - ↔ hypothalamus/tuberal/medial_area/left/arcuate_nucleus
      (kisspeptin KNDy input; the arcuate-to-AVPV kisspeptin network;
      the reciprocal of the arcuate's AVPV edge).
    - → preoptic GnRH neuron population (kisspeptin → GnRH neurons;
      the principal reproductive output edge).
    - ↔ telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (reproductive/social context; left-side).

    ADP (secondary):
    - ↔ hypothalamus/anterior/medial_area/left/supraoptic_nucleus
      and paraventricular_nucleus (vasopressin co-regulation).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmotic input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input;
      SFO is midline).

    Striohypothalamic and ventral preoptic:
    - ↔ telencephalon/.../subcortical/basal_ganglia/striatum (striatal
      input; left-side; poorly characterized function).
    - ↔ lateral_area/left/preoptic_area/lateral_preoptic_nucleus
      (anatomical adjacency; the LPO file's lateral edge; keep distinct
      — different structures).

    Cross-cutting:
    - ↔ hypothalamus/anterior/medial_area/left/preoptic_area (sibling
      preoptic sub-container; adjacent preoptic circuits).
    - ↔ hypothalamus/anterior/lateral_area/left/preoptic_area (sibling
      preoptic sub-container; adjacent preoptic circuits).

Notes:
    - Tier 1 hub leaf (left). Full template. right/ is a delta.
    - This is the AVPV CLOSER: the AVPV/PeN continuity edge was declared
      in lateral_area/left/periventricular_preoptic_nucleus/__init__.py
      and deferred to "when the AVPV is drafted." This file drafts the
      AVPV and declares the reciprocal edge. The continuity edge is now
      CLOSED on the left side; the right/ delta will close it on the
      right.
    - The AVPV's function is distinct from the PeN's: AVPV = estrogen
      POSITIVE feedback / surge; PeN = tonic drive / pulse frequency.
      Both are kisspeptin; both are periventricular; both are sexually
      dimorphic — but in OPPOSITE directions and with DIFFERENT
      functional specializations. Document the distinction; do not
      flatten them into "the kisspeptin nucleus."
    - The AVPV dimorphism (female-larger) is the OPPOSITE of the INAH-3
      dimorphism (male-larger). Do not conflate. The dimorphism
      literatures are separate; document each factually in its own file.
    - The striohypothalamic and ventral preoptic regions are poorly
      characterized. Document them factually as "presumed" or "not
      established"; do not invent functional roles to fill space.
    - The preoptic collision applies here: this file is the "other"
      preoptic group, distinct from lateral_area/left/preoptic_area/
      and medial_area/left/preoptic_area/. Reproduced in Anatomical
      Role; do not remove.
    - No independent fragment: AVPV → aggregated reproductive; ADP →
      upstream fluid. Same aggregation rules as the parent container.
    - Do not create AVPV/, ADP/, striohypothalamic_nucleus/, or
      ventral_preoptic_area/ as child nodes. They are documented WITHIN
      this file. Same convention as mammillary_bodies/left/ carrying
      MM and LM.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, progesterone),
      05_* (GABA, glutamate), 07_* (fluid, vasopressin, angiotensin II,
      ANP), 10_* (circadian, SCN); memory/stores/; gateway/.
    - Connects upward to hypothalamus/other_preoptic_nuclei/.
"""