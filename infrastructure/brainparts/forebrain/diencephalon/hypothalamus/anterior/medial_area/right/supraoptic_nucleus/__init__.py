"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.supraoptic_nucleus
Anatomical Role:
    Right hemisphere of the medial portion of the supraoptic nucleus
    (SON). The same magnocellular neurosecretory neurons documented in
    ../left/, mirrored to the right hemisphere: situated adjacent to the
    periventricular zone, projecting to the posterior pituitary, and
    secreting vasopressin and oxytocin. The lateral portion is documented
    under lateral_area/right/part_of_supraoptic_nucleus/.

    STRUCTURAL IDENTITY (critical — reproduced; both directions apply):
    this node and lateral_area/right/part_of_supraoptic_nucleus/ are the
    SAME anatomical structure, split across two compartments for
    anatomical mirroring of the medial/lateral zones, not because there
    are two nuclei. Stage 4 audit must treat them as ONE structure. Do
    not merge the nodes; do not re-describe the lateral content here.
    Document the split, list the reciprocal edge, keep both files short.

    See ../../../left/supraoptic_nucleus/__init__.py (and, via it,
    ../../../lateral_area/left/part_of_supraoptic_nucleus/__init__.py)
    for the full anatomical description, the magnocellular-vs-
    parvocellular distinction, the input-output direction list, and the
    AGGREGATION RULE for the osmotic fragment.

Functional Mode:
    Same as ../left/. Systemic neurosecretion of vasopressin (ADH) and
    oxytocin from posterior pituitary axon terminals; osmoregulation,
    volume regulation, parturition, and milk ejection reflexes. The
    lateral/medial split is anatomical mirroring, not functional
    subdivision. No documented functional asymmetry between left and
    right SON, and no documented functional difference between the
    perioptic (lateral) and medial components. Do not fabricate either.

Hormonal Modulation:
    Same as ../left/. See ../../../left/supraoptic_nucleus/__init__.py
    § Hormonal Modulation for the input-output list and directions
    (plasma osmolarity ↑, angiotensin II ↑, ANP ↓, baroreceptor
    unloading ↑, estradiol modulates oxytocin, suckling → oxytocin
    pulse). The SON is a source, not a target.

Memory Interfaces:
    Same as ../left/. Reads short_term (osmolarity, volume), episodic
    (dehydration/hemorrhage/parturition history), emotional_valence
    (stress context); writes nothing (Tier 2 organ convention). See
    ../../../left/supraoptic_nucleus/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The osmotic fragment emitted by the
    lateral half represents the bilateral SON and is aggregated at the
    anterior-division level (together with the right PVN vasopressin
    contribution). See the lateral file § Model Integration for the
    AGGREGATION RULE. This file does not emit a fragment, and the
    implementer must not add one — the bilateral SON is a single
    osmotic signal, not four (two hemispheres × two halves).

Right-specific reciprocal connections to enforce in Stage 4:
    - ↔ lateral_area/right/part_of_supraoptic_nucleus (SAME STRUCTURE,
      split across compartments; Stage 4 must treat as one structure
      and must not flag as duplicate).
    - → pituitary_gland/neurohypophysis (posterior pituitary axon
      terminals; vasopressin and oxytocin release; the right medial SON
      contribution to the magnocellular output).
    - ↔ hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (magnocellular co-regulation; PVN and SON are the two
      magnocellular nuclei; right-side).
    - ← hypothalamus/anterior/medial_area/right/preoptic_area/
      median_preoptic_nucleus (MnPO osmoregulatory modulation via
      OVLT/SFO signals; right-side).
    - ← brainstem/solitary_nucleus (NTS; baroreceptor and volume
      inputs; NTS is midline-adjacent — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmosensory input; OVLT is midline).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - Short delta by design. The full content lives in the lateral and
      medial left files; this file points there and records only the
      right-side edges. Same discipline as the other short deltas.
    - This is the FINAL file in the entire hypothalamus/anterior/
      division. After this file, the anterior division is complete on
      both hemispheres: every structural trap closed, every circadian
      loop resolved, every fragment aggregated.
    - The STRUCTURAL IDENTITY paragraph runs in both directions: this
      node ↔ right lateral half, and (mirror) left medial half ↔ left
      lateral half. Both files of each pair declare the identity, so
      the Stage 4 audit can resolve the one-structure pair from either
      side without flagging a duplicate.
    - "Anatomical mirroring, not functional subdivision" is restated
      because a contributor entering at the right medial half must not
      invent a lateral-vs-medial or left-vs-right functional
      asymmetry. The SON has no documented functional asymmetry on
      either axis.
    - No independent fragment: the bilateral SON osmotic signal is
      aggregated at the anterior-division level. The implementer must
      not add a right-side or medial-side osmotic fragment.
    - The MnPO → SON edge is the osmoregulatory integrator-to-effector
      pathway. Both this file and
      ../../../right/preoptic_area/median_preoptic_nucleus/ declare it.
    - Midline targets (NTS, OVLT) are flagged with "verify" so Stage 4
      does not force a hemisphere split on structures that are not
      hemisphere-split in the tree. The right pituitary is
      midline-adjacent — verify on the pituitary side.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../left/supraoptic_nucleus/__init__.py § Notes for the full
      list.
    - Connects upward to hypothalamus/anterior/medial_area/right/.
"""