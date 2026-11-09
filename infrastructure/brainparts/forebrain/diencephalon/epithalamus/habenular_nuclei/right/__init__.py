"""
Package: infrastructure.brainparts.forebrain.diencephalon.epithalamus.habenular_nuclei.right
Anatomical Role:
    Right habenular complex — anatomical mirror of left/, containing the
    same two subdivisions (lateral habenula, medial habenula) with the
    same transmitter identities and projection targets in the right
    hemisphere. See ../left/__init__.py for the full anatomical, functional,
    hormonal, and memory documentation. This file records only the deltas.

    DELTA DISCIPLINE: This is a delta file, not a duplicate. For structural
    mirrors (right hemisphere of a laterally paired nucleus), the parent
    recommends documenting the left fully and recording only what differs
    on the right. This convention applies to every right-hemisphere
    counterpart in the tree (~180 files). Do not copy-paste the left
    file's hormone or memory sections here.

Functional Mode:
    Same as left/ with one honest caveat on lateralization (below).
    - Negative reward prediction error, reward downshift, aversive salience,
      anti-reward feedback loop, nicotine withdrawal (MHb-IPN axis), limbic-
      to-midbrain relay — all as documented in ../left/.
    - The one functional asymmetry some literature suggests (but does not
      reliably establish): right-LHb may be more strongly associated with
      sustained negative affect and depression-adjacent states, while left-
      LHb may be more involved in reward downshift and positive prediction
      error signaling. This is contested. This project does NOT bake this
      asymmetry into the model; it is noted for future reference only.

Hormonal Modulation:
    Same as left/. Do not duplicate. See ../left/__init__.py § Hormonal
    Modulation.

Memory Interfaces:
    Same as left/. Do not duplicate. See ../left/__init__.py § Memory
    Interfaces.

Model Integration (Gemma-4-E2B):
    - No hemisphere-specific prompt fragment. The parent-level fragment
      (habenular_nuclei/__init__.py § Model Integration) covers both
      hemispheres as a single aversive salience channel. Emitting a
      separate right-hemisphere fragment would double-count the aversion
      signal and bias the model more strongly than the literature
      warrants.
    - This is a deliberate design decision: the right habenula contributes
      to the parent's aversive channel but does not add its own fragment.
    - Absence of a fragment here is not an omission — it is the convention
      for hemisphere mirrors unless a specific, defensible asymmetry is
      being modeled.

Reciprocal Connections (enforce in Stage 4 audit — right-side targets only):
    - → midbrain/tegmentum/ventral_tegmental_area (via right fasciculus
      retroflexus → interpeduncular nucleus → VTA; indirect; primarily
      inhibitory). Note: VTA itself is a midline-adjacent structure; the
      right habenula's projection is functionally right-sided but the
      VTA node is not hemisphere-split in this tree. Verify in Stage 4.
    - → midbrain/tegmentum/substantia_nigra/right/pars_compacta
      (inhibitory; right-side target).
    - → hindbrain/metencephalon/pons/tegmentum/dorsal_raphe_nucleus
      (habenulo-raphe; inhibitory; raphe is midline, not hemisphere-split).
    - → midbrain/tegmentum/interpeduncular_nucleus (MHb projection;
      direct; midline structure, not hemisphere-split).
    - ← epithalamus/stria_medullaris/right (primary afferent conduit from
      septal, preoptic, and hypothalamic regions; Tier 3 fiber tract).
    - ↔ left/ (hemisphere counterpart; no strong functional lateralization
      assumed, see Functional Mode above).

Notes:
    - Delta file: NOT a full leaf template. Do not duplicate ../left/.
      The sections above record only what differs (right-side targets,
      lateralization caveat, no-hemisphere-fragment decision).
    - This file is the DELTA-PATTERN EXEMPLAR for the ~180 right-hemisphere
      mirrors in the tree. Copy this shape for: thalamus/right, amygdala
      (if split), hippocampus (if split), substantia_nigra/right, VTA/right
      (if split), basal ganglia right-side structures, etc. The discipline
      is: point to left/, record the deltas, do not restate.
    - Vocabulary used above is defined in Stage 0 files; see ../left/ Notes
      for the full list.
    - Connects upward to habenular_nuclei/.
"""