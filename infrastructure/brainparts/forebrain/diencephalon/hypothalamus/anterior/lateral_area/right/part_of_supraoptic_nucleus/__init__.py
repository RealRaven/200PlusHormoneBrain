"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.right.part_of_supraoptic_nucleus
Anatomical Role:
    Right hemisphere of the lateral portion of the supraoptic nucleus (SON).
    The same perioptic magnocellular component documented in ../left/,
    mirrored to the right hemisphere. See ../left/__init__.py for the full
    anatomical description, the magnocellular-vs-parvocellular distinction,
    and the neurosecretory role.

    Reproduced critical warning (applies equally on the right):
    STRUCTURAL IDENTITY — this node and
    hypothalamus/anterior/medial_area/right/supraoptic_nucleus/ are the
    SAME anatomical structure, split across two compartments for
    anatomical mirroring of the lateral/medial zones, not because there
    are two nuclei. Stage 4 audit must treat them as ONE structure. Do
    not merge the nodes; do not re-describe the medial content here.

Functional Mode:
    Same as ../left/. Systemic neurosecretion of vasopressin (ADH) and
    oxytocin from posterior pituitary axon terminals; osmoregulation,
    volume regulation, parturition, and milk ejection reflexes. No
    documented functional asymmetry between left and right SON for these
    roles. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Plasma osmolarity ↑ → vasopressin ↑; angiotensin II
    ↑ → vasopressin ↑; ANP ↑ → vasopressin ↓; baroreceptor unloading →
    vasopressin ↑; estradiol modulates oxytocin release patterns; suckling
    → oxytocin pulsatile release. The SON is a source, not a target. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (osmolarity, volume), episodic
    (past dehydration/hemorrhage/parturition), emotional_valence (stress
    context); writes nothing (Tier 2 organ convention). See
    ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The osmotic fragment emitted by
    ../left/ represents the bilateral SON and is aggregated at the
    anterior-division level together with the medial supraoptic
    contribution. Emitting a separate right-side osmotic fragment would
    double-count the signal. See ../left/__init__.py § Model Integration
    (AGGREGATION RULE).

Right-specific reciprocal connections to enforce in Stage 4:
    - ↔ hypothalamus/anterior/medial_area/right/supraoptic_nucleus
      (SAME STRUCTURE, split across compartments; Stage 4 must treat as
      one structure and must not flag as duplicate).
    - → pituitary_gland/neurohypophysis (posterior pituitary axon
      terminals; vasopressin and oxytocin release; right-side
      projection).
    - ← hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (parvocellular-to-magnocellular modulation; PVN and SON are the
      two magnocellular nuclei; right-side co-regulation).
    - ← brainstem solitary nucleus (NTS; baroreceptor and volume inputs;
      NTS is midline-adjacent, not hemisphere-split — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmosensory input; OVLT is midline, not hemisphere-split —
      verify).
    - ← median_eminence (permissive modulation of neurohypophyseal
      release; median eminence is midline).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - The STRUCTURAL IDENTITY warning with medial supraoptic is
      reproduced above because it is a structural trap that applies on
      both hemispheres. The full anatomical, hormonal, and memory
      content is referenced rather than duplicated.
    - No hemisphere-specific osmotic fragment: the left-side fragment
      is bilateral and aggregated at the anterior-division level. Same
      convention as habenular_nuclei/right/ and
      anterior_part_of_lateral_nucleus/right/.
    - Midline targets (NTS, OVLT, median eminence) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/lateral_area/right/.
"""