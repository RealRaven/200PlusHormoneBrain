"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.left.part_of_supraoptic_nucleus
Anatomical Role:
    The left lateral portion of the supraoptic nucleus (SON). The SON is a
    paired collection of magnocellular neurosecretory neurons situated
    dorsal to the optic tract, wrapping around it; the lateral portion
    documented here is the part of the SON that extends into the lateral
    anterior area. The medial portion is documented under
    hypothalamus/anterior/medial_area/left/supraoptic_nucleus/.

    STRUCTURAL IDENTITY (critical): this node and
    medial_area/left/supraoptic_nucleus/ are the SAME anatomical structure.
    The tree splits the SON across two compartments for anatomical
    mirroring of the lateral/medial zones, not because there are two
    nuclei. Stage 4 audit must treat them as ONE structure: the lateral
    portion (here) carries the perioptic magnocellular component
    (vasopressin-dominant, osmosensory), and the medial portion (there)
    carries the remaining magnocellular component. Do not merge the
    nodes into one leaf; do not re-describe the medial content here.
    Document the split, list the reciprocal edge, keep both files short.

    The neurons here are magnocellular: they project their axons to the
    posterior pituitary via the hypothalamo-hypophyseal tract and release
    vasopressin and oxytocin into the systemic circulation from axon
    terminals, not into the hypophyseal portal system. This is the
    distinction from the parvocellular neurosecretory neurons of the
    paraventricular nucleus.

Functional Mode:
    - Systemic neurosecretion: vasopressin (ADH) and oxytocin released
      from posterior pituitary terminals. The SON is one of the two
      magnocellular nuclei that produce these hormones (the other is the
      paraventricular nucleus, PVN).
    - Osmoregulation: osmosensory neurons in the SON (and in the
      organum vasculosum of the lamina terminalis, OVLT, and subfornical
      organ, SFO) detect plasma hypertonicity and drive vasopressin
      release, which increases water reabsorption in the kidney.
    - Volume regulation: baroreceptor inputs (via the solitary nucleus,
      NTS) modulate SON activity in response to blood pressure and blood
      volume changes. Hypovolemia → increased vasopressin.
    - Parturition reflex (oxytocin): uterine stretch → oxytocin release
      → uterine contraction (positive feedback loop, Ferguson reflex).
    - Milk ejection reflex (oxytocin): suckling → oxytocin pulsatile
      release → myoepithelial contraction in mammary glands.
    - Vasopressin is also a neuromodulator in the brain (social behavior,
      pair bonding, aggression, stress-axis modulation), but that role
      is largely PVN-and-extra-hypothalamic; document the SON's
      neurosecretory role here, not the central neuromodulator role.

Hormonal Modulation (input is plasma state; output is hormone release):
    - Plasma osmolarity ↑: vasopressin ↑ (primary osmoregulatory signal;
      the defining input-output relationship of the SON).
    - Angiotensin II ↑ (via OVLT/SFO): vasopressin ↑ (volume depletion,
      hypovolemia, hypotension signal).
    - Atrial natriuretic peptide (ANP) ↑ (volume repletion): vasopressin ↓
      (opposes vasopressin release under hypervolemia).
    - Baroreceptor unloading (hypotension/hypovolemia via NTS): vasopressin
      ↑; baroreceptor activation (volume expansion): vasopressin ↓.
    - Estradiol: modulates oxytocin release patterns; enhances oxytocin
      neuron excitability and parturition reflex sensitivity.
    - Suckling (somatosensory input, not a hormone): oxytocin pulsatile
      release.
    - Nausea, pain, stress: vasopressin ↑ via extrahypothalamic inputs.
    - The SON is a *source*, not a target of the 12 axes in the usual
      sense. Document it as an output organ for the fluid axis
      (chemicals_hormones/07_*); do not list modulators as if it were
      being modulated by the whole endocrine system.

Memory Interfaces (Tier 2 organ convention — read-only):
    - Reads:
        * short_term: current plasma osmolarity and volume state buffers.
          The osmoregulatory reflex depends on these.
        * episodic: past dehydration, hemorrhage, and parturition events,
          used to set sensitivity thresholds.
        * emotional_valence: stress context, which modulates vasopressin
          release via limbic inputs.
    - Writes: none directly. Like the pineal gland, the SON emits
      hormones, not stored content. It contributes to the homeostatic
      state vector via vasopressin and oxytocin output.
    - This read-only, write-nothing pattern is the Tier 2 organ
      convention. Do not invent memory writes for a secretory nucleus.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (osmotic/fluid constituent input):
        "Osmotic state — left supraoptic (lateral part):
         - Plasma osmolarity: [normal / high].
         - Volume state: [euvolemic / hypovolemic / hypervolemic].
         - Vasopressin drive: [X].
         - Oxytocin reflex state: [quiescent / parturition / lactation].
         If vasopressin drive is high (hypertonic or hypovolemic):
         surface fluid-seeking priorities, reduce extraneous output, and
         prefer conservative framing. If oxytocin reflex is active:
         bias toward affiliative, protective, or caregiving framing
         where context permits."
    - AGGREGATION RULE (must be respected by the implementer): this
      fragment is a *constituent input* to the anterior-division osmotic
      fragment, which also aggregates the medial supraoptic contribution
      (medial_area/left/supraoptic_nucleus/). Do not emit this fragment
      as an independent, un-aggregated state block — that would
      double-count the osmotic signal. Aggregate at the
      anterior-division level before injection.
    - The fragment is otherwise emitted whenever the anterior-division
      osmotic fragment is emitted.
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (enforce in Stage 4 audit):
    - ↔ hypothalamus/anterior/medial_area/left/supraoptic_nucleus
      (SAME STRUCTURE, split across compartments; Stage 4 must treat as
      one structure and must not flag as duplicate).
    - → pituitary_gland/neurohypophysis (posterior pituitary axon
      terminals; vasopressin and oxytocin release; the SON's principal
      output edge).
    - ← hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (parvocellular-to-magnocellular modulation and vasopressin/
      oxytocin co-regulation; PVN and SON are the two magnocellular
      nuclei).
    - ← brainstem solitary nucleus (NTS; baroreceptor and volume inputs
      via the ascending pathway).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmosensory input; the SFO is documented separately under
      hypothalamus/subfornical_organ/).
    - ← median_eminence (permissive modulation of neurohypophyseal
      release, though the primary portal role is for the anterior
      pituitary).

Notes:
    - Tier 2 organ-flavored leaf (left). Full template, but with hormone
      output primary and memory read-only. right/ is a delta.
    - The STRUCTURAL IDENTITY warning with medial supraoptic is the most
      important content in this file. It is the structural counterpart
      of the LHA distinction in the anterior pole leaf: two tree nodes,
      one anatomical structure, documented as a split with a reciprocal
      edge, not merged.
    - The lateral/medial split of the SON in this tree is *anatomical
      mirroring*, not functional subdivision. There is no compelling
      evidence for a functional difference between the perioptic
      (lateral) and the more medial components of the SON beyond what
      the reciprocal edge documents. Do not invent a functional
      asymmetry.
    - The paraventricular nucleus also releases vasopressin and oxytocin
      from magnocellular neurons. This file documents the SON component;
      the PVN component is documented under
      medial_area/left/paraventricular_nucleus/. Keep the descriptions
      consistent when that file is drafted.
    - Vasopressin as a central neuromodulator (social behavior, pair
      bonding, aggression) is a PVN-and-extrahypothalamic function;
      do not duplicate it here. Keep the SON file neurosecretory.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/06_* (social, oxytocin, vasopressin as
      neuromodulators), 07_* (fluid, vasopressin, angiotensin II, ANP),
      01_* (estradiol); memory/stores/ (short_term, episodic,
      emotional_valence); gateway/.
    - Connects upward to hypothalamus/anterior/lateral_area/left/.
"""