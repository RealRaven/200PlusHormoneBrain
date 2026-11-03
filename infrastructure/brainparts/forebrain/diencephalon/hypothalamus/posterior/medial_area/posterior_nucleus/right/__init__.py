"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.medial_area.posterior_nucleus.right
Anatomical Role:
    Right posterior hypothalamic nucleus (PHN). Same small, densely
    packed nucleus documented in ../left/, mirrored to the right
    hemisphere. Principal hypothalamic driver of sympathetic outflow
    and behavioral arousal; sympathetic complement of the right
    anterior hypothalamic nucleus (AHN). See ../left/__init__.py for the
    full anatomical description and the three distinct-neighbor
    distinctions (posterior LHA, AHN, mammillary body).

    Reproduced notes (apply equally on the right):
    - NO structural-identity trap and NO naming collision: the PHN is a
      single, unambiguously named nucleus. Do not invent a trap.
    - The PHN is DISTINCT from the posterior LHA segment 3 (arousal
      drive via orexin), the AHN (parasympathetic complement), and the
      mammillary body (memory relay). All three are adjacent; do not
      merge.

Functional Mode:
    Same as ../left/. Sympathetic outflow, behavioral arousal,
    sympathetic pupillary dilation, stress response; complementary to
    the AHN. No documented functional asymmetry between left and right
    PHN. Do not fabricate one. See ../left/__init__.py § Functional
    Mode.

Hormonal Modulation:
    Same as ../left/. Orexin ↑ PHN activity (arousal); norepinephrine
    ↑ PHN activity; histamine ↑ PHN activity; CRH ↑ PHN activity
    (stress); angiotensin II ↑ PHN activity (volume depletion). The
    PHN is primarily an output nucleus; the 12 endocrine axes are not
    its principal targets. See ../left/__init__.py § Hormonal
    Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (arousal state), episodic
    (arousal/threat history), emotional_valence (stress/aversion
    context), temporal_sequence_learning (circadian arousal gating).
    Writes no stored content directly. See ../left/__init__.py
    § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The sympathetic/arousal fragment
    (sympathetic tone, arousal level, pupillary state, stress response,
    and the "do not treat high sympathetic tone or high arousal as
    impairment" guardrail) is emitted once at the left/ level and
    represents the bilateral nucleus. Emitting a separate right-side
    fragment would double-count the sympathetic/arousal signal. See
    ../left/__init__.py § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:

    Sympathetic outflow (primary):
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic premotor output;
      RVLM is midline-adjacent — verify).
    - → spinal_cord/gray_matter/right/lateral_horn (sympathetic
      preganglionic output via the intermediolateral column; right-side).
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus (LC;
      noradrenergic arousal and sympathetic co-activation; LC is
      midline-adjacent — verify).
    - → midbrain/tegmentum/dorsal_raphe_nucleus (dorsal raphe;
      serotonergic arousal co-activation; raphe is midline).

    Behavioral arousal:
    - → telencephalon/cerebral_hemispheres/right/subcortical/
      basal_forebrain (arousal; right-side).
    - → thalamus/right/midline_nuclear_group (intralaminar arousal
      relay; the midline/intralaminar nuclei are midline — verify).

    Complementary pair:
    - ↔ hypothalamus/anterior/medial_area/right/
      anterior_hypothalamic_nucleus (AHN; parasympathetic complement;
      complementary pair, NOT duplicate; right-side).
    - ↔ hypothalamus/posterior/lateral_area/right/
      posterior_part_of_lateral_nucleus (posterior LHA segment 3;
      arousal drive cooperating with PHN's sympathetic output;
      distinct nodes; right-side).

    Input:
    - ← hypothalamus/anterior/lateral_area/right/
      anterior_part_of_lateral_nucleus (orexin arousal input from the
      LHA; distinct edge, not the LHA continuum; right-side).
    - ← hypothalamus/anterior/medial_area/right/
      suprachiasmatic_nucleus (SCN → PHN; circadian autonomic gating;
      SCN is midline-adjacent — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      angiotensin II input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).
    - ← brainstem/.../solitary_nucleus (NTS; visceral and stress input;
      NTS is midline-adjacent — verify).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - This is the FINAL FILE IN THE POSTERIOR DIVISION. With this file,
      the posterior division is fully documented on both hemispheres:
      - posterior/lateral_area/ (5 files, complete)
      - posterior/medial_area/mammillary_nuclei/ (3 files, complete;
        pointer deltas to mammillary_bodies/)
      - posterior/medial_area/posterior_nucleus/ (3 files; this file
        completes it)
    - The PHN ↔ AHN complementary pair is reproduced above because it
      is a structural relationship that applies on both hemispheres.
      The two fragments (AHN's parasympathetic, PHN's sympathetic) use
      consistent "bias not impairment" guardrails; keep them consistent
      in the Stage 4 audit.
    - The pupillary light reflex vs. sympathetic pupillary dilation
      distinction is reproduced below in abbreviated form (the full
      distinction is in ../left/): the light reflex is pretectum →
      Edinger-Westphal → ciliary ganglion → constrictor
      (parasympathetic); the sympathetic dilation is PHN → ciliospinal
      center → superior cervical ganglion → dilator. The right PHN
      drives the right-side dilatory pathway; do not conflate the two.
    - No structural-identity trap, no naming collision to reproduce.
      The PHN is a single unambiguously named nucleus on both sides.
      The "no trap" note is reproduced because a contributor entering
      at right/ should not pattern-match from other posterior files
      and invent one.
    - No independent fragment: the sympathetic/arousal fragment is
      bilateral. Same convention as habenular_nuclei/right/ and the
      other deltas in the tree.
    - Midline targets (RVLM, LC, raphe, intralaminar nuclei, SCN, OVLT,
      SFO, NTS) are flagged with "verify" so Stage 4 does not force a
      hemisphere split on structures that are not hemisphere-split in
      the tree. Right spinal lateral horn, right AHN, right posterior
      LHA, and right basal forebrain are hemisphere-split and require
      right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/posterior/medial_area/
      posterior_nucleus/.
"""