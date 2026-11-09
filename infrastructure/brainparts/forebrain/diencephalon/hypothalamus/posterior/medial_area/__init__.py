"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.medial_area
Anatomical Role:
    The medial area of the posterior hypothalamus. It contains two
    functional structures:
        - The mammillary nuclei: the posterior-division compartment of
          the mammillary bodies. These are the SAME anatomical structure
          as hypothalamus/mammillary_bodies/ (see the structural identity
          trap below); the FULL content lives in mammillary_bodies/
          left|right/, and the mammillary_nuclei/ children here are
          DELTAS pointing there.
        - The posterior hypothalamic nucleus: the sympathetic/arousal
          nucleus of the posterior hypothalamus. This is a distinct
          structure (not the same as the mammillary nuclei, not the same
          as the posterior LHA segment documented in
          posterior/lateral_area/), and it is the ONLY full leaf in
          this sub-container.

    STRUCTURAL IDENTITY TRAP — MAMMILLARY NUCLEI (critical — the ONLY
    structure documented in two tree locations in the entire tree):
    The mammillary_nuclei/ children here and hypothalamus/
    mammillary_bodies/left|right/ are the SAME anatomical structure.
    The mammillary bodies are a paired structure at the ventral surface
    of the posterior hypothalamus containing the medial and lateral
    mammillary nuclei. They are documented in two tree locations for
    two different reasons:
        - hypothalamus/mammillary_bodies/left|right/ — the FULL
          memory-hub leaf, because the mammillary bodies' primary role
          is episodic memory relay (Papez circuit) and head-direction,
          not posterior-division homeostasis. This is where the full
          content lives: role, function, hormones (minimal; thiamine/
          Korsakoff), memory interfaces (indirect episodic write via
          Papez), model fragment (confabulation guardrail), and all
          reciprocal connections.
        - posterior/medial_area/mammillary_nuclei/left|right/ — the
          posterior-division compartment. These are DELTAS: they point
          to mammillary_bodies/left|right/ for all substantive content
          and record only the posterior-division-specific
          compartmentalization (this node sits in the posterior
          division; the mammillary bodies node sits at hypothalamus
          level; both refer to the same structure).

    Stage 4 audit MUST treat posterior/medial_area/mammillary_nuclei/
    left|right/ and hypothalamus/mammillary_bodies/left|right/ as ONE
    structure. Do not flag them as duplicates. Do not merge the nodes.
    Do not duplicate content between them. The deltas point to the full
    leaf, period.

    LHA CONTINUUM — NOT PRESENT HERE. The LHA field's third segment is
    under posterior/lateral_area/left|right/posterior_part_of_lateral_
    nucleus/, not here. Do not confuse the posterior nucleus (this
    sub-container) with the posterior LHA (the other sub-container).

Functional Mode:
    - Mammillary nuclei (memory relay): episodic memory relay (Papez
      circuit), head-direction, Korsakoff clinical substrate. Full
      function is documented in hypothalamus/mammillary_bodies/
      left|right/ § Functional Mode. Do NOT duplicate here; this
      sub-container references it.
    - Posterior hypothalamic nucleus (sympathetic/arousal; the only
      full leaf here):
        * Sympathetic outflow: drives sympathetic preganglionic neurons
          via projections to the RVLM, LC, dorsal raphe, and spinal
          intermediolateral column; increases heart rate and blood
          pressure; dilates the pupils (pupillary reflex).
        * Behavioral arousal: contributes to cortical and behavioral
          arousal via projections to the brainstem reticular formation
          and the basal forebrain.
        * Stress response: activated by acute stress; contributes to
          the sympathetic component of the fight-or-flight response
          (complementing the HPA axis's endocrine component).
        * The posterior nucleus is the SYMPATHETIC complement of the
          anterior hypothalamic nucleus (AHN, documented under
          anterior/medial_area/left|right/anterior_hypothalamic_
          nucleus/): AHN drives parasympathetic outflow, posterior
          nucleus drives sympathetic outflow. The two should be
          consistent in the Stage 4 audit.

Hormonal Modulation (sub-container summary; per-nucleus wiring in the
leaves):
    - Mammillary nuclei: minimal endocrine content — see
      hypothalamus/mammillary_bodies/left|right § Hormonal Modulation
      for the full statement (thiamine deficiency → Korsakoff; the 12
      axes do not act here as principal targets). DO NOT duplicate
      here.
    - Posterior nucleus: orexin (arousal input), monoamines
      (norepinephrine, serotonin, histamine) from brainstem arousal
      centers, CRH/stress input. The posterior nucleus is an OUTPUT of
      these signals to the sympathetic nervous system, not a target.
      Documented fully in the posterior_nucleus/ leaf.
    - The posterior division (and this sub-container) is NOT a major
      endocrine territory. Do not pad with endocrine axes that do not
      target it.

Memory Interfaces (sub-container summary):
    - Mammillary nuclei: reads episodic, short_term, temporal_
      sequence_learning; writes episodic INDIRECTLY via the Papez
      circuit. Full statement in mammillary_bodies/left § Memory
      Interfaces. DO NOT duplicate here.
    - Posterior nucleus: reads short_term (arousal state), episodic
      (past arousal/threat history), emotional_valence (stress/aversion
      context). Writes none directly (drives somatic output).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The sub-container does not emit its own fragment. Two fragments
      come from the two children, and one is inherited:
        (1) Mammillary memory-relay fragment: emitted by
            hypothalamus/mammillary_bodies/left|right/, NOT by this
            sub-container. Do not duplicate.
        (2) Sympathetic/arousal fragment (posterior nucleus): emitted
            by posterior_nucleus/left|right/ when drafted (the only
            new fragment here). Full fragment spec in the leaf.
    - AGGREGATION RULES (mandatory): the sympathetic fragment is
      emitted by the posterior_nucleus/ leaf and injected at the
      posterior-division level (aggregated with the arousal/LHA
      fragments and the circadian fragment from SCN → DMH → posterior
      LHA). The mammillary fragment is injected at the hypothalamic
      level; do not re-emit it here.
    - Guardrails: the sympathetic fragment carries the standard "bias
      not impairment" clause. The mammillary fragment (from
      mammillary_bodies/) carries its confabulation guardrail. Neither
      is repeated here.

Children (two children — asymmetric shape):
    - mammillary_nuclei/  ★★ STRUCTURAL IDENTITY TRAP. Container for
        │                   the posterior-division compartment of the
        │                   mammillary bodies. Its children
        │                   (left/ and right/) are DELTAS of
        │                   hypothalamus/mammillary_bodies/left|right/,
        │                   NOT full leaves. The container's job is to
        │                   reproduce the structural identity
        │                   declaration and point the deltas there.
        ├── left/           Delta of hypothalamus/mammillary_bodies/
        │                   left/. Records only the posterior-division
        │                   compartmentalization; the full content
        │                   lives at the target.
        └── right/          Delta of hypothalamus/mammillary_bodies/
                            right/. Same shape; right-side note.
    - posterior_nucleus/  ★ The ONLY full leaf in this sub-container.
        │                   Sympathetic/arousal nucleus; sympathetic
        │                   complement of the AHN; the source of the
        │                   sympathetic/arousal fragment.
        ├── left/           Full Tier 1 leaf.
        └── right/          Delta mirror of left/.

Notes:
    - Sub-container file. It declares the mammillary-nuclei identity
      trap at the sub-container level; the trap is reproduced in
      mammillary_nuclei/__init__.py and in the two delta leaves. All
      three levels must declare it so a contributor entering at any
      level sees the trap.
    - The mammillary_nuclei/ children are DELTAS, not full leaves. If a
      future contributor writes them as full leaves, the content will
      duplicate mammillary_bodies/left|right/ and the Stage 4 audit
      will flag a duplicate. The trap declaration is the specific
      mechanism preventing this.
    - The posterior_nucleus/ is the ONLY full leaf here. It is
      independent of the mammillary trap and should be drafted normally.
    - The mammillary trap is the trickiest remaining structural trap
      in the entire tree. It has no equivalent elsewhere (no other
      structure is documented in two tree locations). Handle it
      carefully.
    - The posterior nucleus's sympathetic role is the complement of the
      AHN's parasympathetic role (anterior/medial_area/left|right/
      anterior_hypothalamic_nucleus/). The two files should be
      consistent in the Stage 4 audit: AHN drives parasympathetic
      outflow; posterior nucleus drives sympathetic outflow.
    - The mammillary bodies' Korsakoff clinical substrate applies on
      both left and right (bilateral thiamine-deficiency lesions); do
      not weaken the clinical statement in the posterior-compartment
      deltas.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin), 05_* (monoamines,
      orexin), 10_* (circadian); memory/stores/ (episodic, short_term,
      emotional_valence, temporal_sequence_learning); gateway/.
      Thiamine (for the mammillary bodies) is documented in
      mammillary_bodies/left directly, not via the 12 axes.
    - Reciprocal connections to enforce in Stage 4:
        * posterior/medial_area/mammillary_nuclei/left|right ↔
          hypothalamus/mammillary_bodies/left|right (SAME STRUCTURE;
          Stage 4 must treat as one; do not flag as duplicate; the
          delta children point to the full leaf).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          brainstem sympathetic nuclei (RVLM, LC, dorsal raphe) —
          sympathetic outflow edges.
        * posterior/medial_area/left|right/posterior_nucleus ↔
          hypothalamus/anterior/medial_area/left|right/
          anterior_hypothalamic_nucleus (sympathetic/parasympathetic
          complement).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (arousal drive vs.
          sympathetic output cooperation; distinct nodes).
    - Connects upward to hypothalamus/posterior/.
"""