"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.supraoptic_nucleus
Anatomical Role:
    The left medial portion of the supraoptic nucleus (SON). The SON is a
    paired collection of magnocellular neurosecretory neurons situated
    dorsal to the optic tract; the medial portion documented here is the
    part of the SON that sits adjacent to the periventricular zone. The
    lateral portion is documented under
    lateral_area/left/part_of_supraoptic_nucleus/.

    STRUCTURAL IDENTITY (critical — this is the OTHER half of the
    warning first declared in the lateral file): this node and
    lateral_area/left/part_of_supraoptic_nucleus/ are the SAME
    anatomical structure. The tree splits the SON across two
    compartments for anatomical mirroring of the lateral/medial zones,
    not because there are two nuclei. Stage 4 audit must treat them as
    ONE structure. Do not merge the nodes; do not re-describe the
    lateral content here. Document the split, list the reciprocal
    edge, keep both files short.

    See ../lateral_area/left/part_of_supraoptic_nucleus/__init__.py for
    the full anatomical description, the magnocellular-vs-parvocellular
    distinction, the neurosecretory role, the input-output direction
    list (plasma osmolarity, angiotensin II, ANP, baroreceptor,
    estradiol, suckling, stress → vasopressin or oxytocin), and the
    AGGREGATION RULE for the osmotic fragment.

Functional Mode:
    Same as the lateral half. Systemic neurosecretion of vasopressin
    (ADH) and oxytocin from posterior pituitary axon terminals;
    osmoregulation, volume regulation, parturition, and milk ejection
    reflexes. The medial portion carries the same functional role; the
    lateral/medial split is anatomical mirroring, not functional
    subdivision. There is no compelling evidence for a functional
    difference between the perioptic (lateral) and medial components of
    the SON beyond what the reciprocal edge documents. Do not invent a
    functional asymmetry.

Hormonal Modulation:
    Same as the lateral half. See
    ../../../lateral_area/left/part_of_supraoptic_nucleus/__init__.py
    § Hormonal Modulation for the full input-output list and
    directions. The SON is a source, not a target.

Memory Interfaces:
    Same as the lateral half. Reads short_term (osmolarity, volume),
    episodic (dehydration/hemorrhage/parturition history),
    emotional_valence (stress context); writes nothing (Tier 2 organ
    convention). See the lateral file § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The osmotic fragment emitted by the
    lateral half represents the bilateral SON and is aggregated at the
    anterior-division level (together with the PVN vasopressin
    contribution). See the lateral file § Model Integration for the
    AGGREGATION RULE. This file does not emit a fragment, and the
    implementer must not add one — the bilateral SON is a single
    osmotic signal, not two.

Reciprocal Connections (medial-side only; the lateral-side edges are
in the lateral file):
    - ↔ lateral_area/left/part_of_supraoptic_nucleus (SAME STRUCTURE,
      split across compartments; Stage 4 must treat as one structure
      and must not flag as duplicate).
    - → pituitary_gland/neurohypophysis (posterior pituitary axon
      terminals; vasopressin and oxytocin release; the medial SON
      contribution to the magnocellular output).
    - ↔ hypothalamus/anterior/medial_area/left/paraventricular_nucleus
      (magnocellular co-regulation; PVN and SON are the two magnocellular
      nuclei).
    - ← hypothalamus/anterior/medial_area/left/preoptic_area/
      median_preoptic_nucleus (MnPO osmoregulatory modulation via OVLT/
      SFO signals).
    - ← brainstem/solitary_nucleus (NTS; baroreceptor and volume inputs;
      NTS is midline-adjacent — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmosensory input; OVLT is midline).

Notes:
    - Short leaf by design. The full content lives in the lateral half;
      do not duplicate. This is the closing half of the SON structural
      trap declared in lateral_area/left/part_of_supraoptic_nucleus/.
    - The STRUCTURAL IDENTITY paragraph runs in the opposite direction
      from the lateral file: the lateral file said "this node and the
      medial supraoptic are one structure"; this file says the same,
      pointing back. Both declarations are required for the Stage 4
      audit to treat the two nodes as one structure without flagging
      them as duplicates.
    - "Anatomical mirroring, not functional subdivision" is restated
      from the lateral file because a contributor entering at the
      medial half must not invent a lateral-vs-medial functional
      asymmetry.
    - No independent fragment: the bilateral SON osmotic signal is
      aggregated at the anterior-division level. Same AGGREGATION RULE
      as the lateral half.
    - The MnPO → SON edge is the osmoregulatory integrator-to-effector
      pathway: the MnPO (in the preoptic area) receives OVLT/SFO input
      and modulates SON activity. Both this file and the MnPO file
      declare the edge.
    - Vocabulary used above is defined in Stage 0 files; see the
      lateral file § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/left/.
"""