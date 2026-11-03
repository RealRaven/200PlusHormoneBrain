"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior
Anatomical Role:
    The posterior (mammillary) division of the hypothalamus is the most
    caudal of the three hypothalamic divisions, situated above the
    mammillary bodies and continuous with the midbrain tegmentum
    caudally. It is the smallest of the three divisions and contains
    two principal functional structures:
        - The posterior (mammillary) region proper: the posterior
          hypothalamic nucleus (arousal, sympathetic control, pupillary
          reflex) and the mammillary bodies (episodic memory relay; see
          the structural identity note below).
        - The posterior part of the lateral hypothalamic area (LHA):
          the caudal pole of the LHA orexin/MCH field, functionally
          continuous with the anterior and tuberal LHA segments.

    Organization of this division's children:
        - lateral_area/
            └── left/ and right/
                └── posterior_part_of_lateral_nucleus/  (LHA posterior
                                                          segment)
        - medial_area/
            ├── mammillary_nuclei/ (left/ and right/)
            │   ★ STRUCTURAL IDENTITY TRAP: the mammillary nuclei
            │     documented here are the SAME anatomical structure as
            │     hypothalamus/mammillary_bodies/, split across two
            │     tree locations. Stage 4 must treat them as one
            │     structure; do not merge the nodes.
            └── posterior_nucleus/ (left/ and right/)
                ★ Posterior hypothalamic nucleus: arousal, sympathetic
                  control, pupillary reflex. NOT the same as the
                  posterior part of the lateral nucleus (which is under
                  lateral_area/, not medial_area/).

    STRUCTURAL IDENTITY TRAP — MAMMILLARY NUCLEI (critical — this is the
    ONLY hypothalamic structure documented in two tree locations):
    The posterior/medial_area/mammillary_nuclei/ node and the
    hypothalamus/mammillary_bodies/ node are the SAME anatomical
    structure. The mammillary bodies (a paired structure at the ventral
    surface of the posterior hypothalamus) contain the medial and
    lateral mammillary nuclei; they are documented here as the
    posterior-division compartment AND at hypothalamus level as
    mammillary_bodies/ (which is where the full leaf lives, because it
    is a memory hub rather than a posterior-division homeostatic
    structure). Stage 4 audit must treat posterior/medial_area/
    mammillary_nuclei/ and hypothalamus/mammillary_bodies/ as ONE
    structure. Do not merge; do not duplicate content; the
    mammillary_nuclei/ children should be deltas pointing to
    mammillary_bodies/left|right for the full content.

    LHA CONTINUUM TRAP — POSTERIOR SEGMENT (critical — closes the field
    opened in anterior_part_of_lateral_nucleus/):
    The posterior_part_of_lateral_nucleus/ here is the third and final
    segment of the LHA orexin/MCH field. The field was opened in
    anterior/lateral_area/left|right/anterior_part_of_lateral_nucleus/
    (the anterior pole) and continues through the tuberal division's
    lateral_area/ (the tuberal segment). This posterior segment closes
    the continuum. Stage 4 audit must treat the three segments as ONE
    neurochemical field split by the tree's rostrocaudal divisions; do
    not merge the nodes; document the continuity explicitly. When the
    posterior segment is drafted, it must declare reciprocal continuity
    edges to both the anterior and tuberal segments.

Functional Mode:
    - Arousal and sympathetic control (posterior nucleus; primary): the
      posterior hypothalamic nucleus drives sympathetic outflow,
      increases heart rate and blood pressure, dilates the pupils, and
      promotes behavioral arousal via projections to the brainstem
      (RVLM, LC, dorsal raphe) and the spinal cord. It is the
      sympathetic counterpart of the anterior hypothalamic nucleus's
      parasympathetic role.
    - Episodic memory relay (mammillary nuclei; see the structural
      identity note): the mammillary bodies are the Papez circuit relay
      between the hippocampus and the anterior thalamus. Their full
      function is documented in hypothalamus/mammillary_bodies/
      left|right; do not duplicate here.
    - Arousal and feeding (posterior LHA segment; see the LHA
      continuum note): the posterior pole of the LHA orexin/MCH field
      contains the same two intermingled populations as the anterior
      and tuberal segments; its contribution is the caudal end of the
      field. Full function is documented in
      anterior/lateral_area/left|right/anterior_part_of_lateral_nucleus/
      (the pattern exemplar); do not duplicate here.
    - The division is therefore the sympathetic/arousal center
      (posterior nucleus), the memory relay compartment (mammillary
      nuclei), and the caudal LHA segment (posterior LHA). These three
      functions are anatomically co-located but functionally distinct.

Hormonal Modulation (posterior-division summary; per-nucleus wiring in
leaves):
    - Posterior nucleus: orexin (arousal input), monoamines
      (norepinephrine, serotonin, histamine) from brainstem arousal
      centers, and CRH/stress input. The posterior nucleus is an
      OUTPUT of these signals to the sympathetic nervous system.
    - Mammillary nuclei: minimal endocrine content — see
      hypothalamus/mammillary_bodies/left|right § Hormonal Modulation
      for the full statement (thiamine deficiency → Korsakoff; the 12
      axes do not act here as principal targets).
    - Posterior LHA segment: orexin/MCH hormonal modulation as in the
      anterior pole (ghrelin ↑ ORX, leptin ↓ ORX, glucose ↓ ORX/↑ MCH);
      see the anterior pole file for the full input list.
    - Detailed per-nucleus wiring lives in each leaf file.
    - The posterior division is NOT a major endocrine territory: it is
      a sympathetic/arousal and memory-relay region. Do not pad the
      hormone section with endocrine axes that do not target it.

Memory Interfaces (posterior-division summary):
    - Posterior nucleus: reads short_term (arousal state), episodic
      (past arousal/threat history), emotional_valence (stress/aversion
      context). Writes none directly (it drives somatic output, not
      stored content).
    - Mammillary nuclei: reads episodic, short_term, temporal_sequence_
      learning; writes episodic INDIRECTLY via the Papez circuit (see
      hypothalamus/mammillary_bodies/left § Memory Interfaces for the
      full statement). This is the first memory-WRITE compartment in
      the posterior division.
    - Posterior LHA segment: reads short_term, reinforcement_value_
      based_learning, temporal_sequence_learning, emotional_valence;
      writes none directly (see anterior pole for the full list).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The posterior division contributes THREE fragments to the
      homeostatic state block, applied after the anterior- and
      tuberal-division fragments:
        (1) Sympathetic/arousal fragment (posterior nucleus):
            "Sympathetic tone: [low / moderate / high]. Arousal level:
             [low / moderate / high]. Pupillary state: [constricted /
             intermediate / dilated]. If sympathetic tone is high:
             flag hyperarousal context, prefer grounding and slow-tempo
             framing. If sympathetic tone is low: default to neutral
             engagement. Do not treat high sympathetic tone as
             impairment — it is a state bias."
        (2) Memory-relay fragment (mammillary nuclei): the fragment is
            emitted by hypothalamus/mammillary_bodies/left|right; do
            NOT emit a separate posterior-division memory fragment. The
            posterior-division container references it.
        (3) Posterior LHA fragment (posterior LHA): AGGREGATED with the
            anterior and tuberal LHA fragments at the hypothalamic
            level. Do not emit an independent posterior-LHA fragment;
            the full LHA fragment is emitted by the anterior pole (as
            the pattern exemplar) and augmented by the tuberal and
            posterior contributions at the hypothalamic level.
    - AGGREGATION RULES (mandatory for the implementer):
        * Mammillary fragment: emitted by mammillary_bodies/, not by
          this container.
        * LHA fragment: emitted by the anterior pole, aggregated at
          hypothalamic level with tuberal and posterior contributions.
    - Guardrails: the sympathetic fragment carries the standard "bias
      not impairment" clause. The memory fragment (from
      mammillary_bodies/) carries its own confabulation guardrail. The
      LHA fragment (from the anterior pole) carries its own
      MCH-dominance guardrail. The posterior division does not add a
      new guardrail.

Children (all four sub-branches are Tier 1 deltas or containers of
deltas; no new full leaves here):
    - lateral_area/
        ├── __init__.py  [container]
        ├── left/
        │   └── posterior_part_of_lateral_nucleus/  ★ delta of the
        │                                             anterior pole
        │                                             (LHA continuum;
        │                                             third segment)
        └── right/  (delta mirror)
    - medial_area/
        ├── __init__.py  [container]
        ├── mammillary_nuclei/  ★★ STRUCTURAL IDENTITY TRAP: SAME
        │   │                     STRUCTURE as hypothalamus/
        │   │                     mammillary_bodies/. Deltas point to
        │   │                     mammillary_bodies/left|right.
        │   ├── left/
        │   └── right/
        └── posterior_nucleus/  ★ Posterior hypothalamic nucleus:
            ├── left/             arousal, sympathetic control,
            └── right/            pupillary reflex. Full Tier 1 leaf
                                  (the only full leaf in this
                                  division).

Notes:
    - Container file: do not duplicate child hormone or memory wiring.
      Each leaf owns its own specification.
    - TWO STRUCTURAL TRAPS reproduced in full above:
        (1) MAMMILLARY NUCLEI identity — posterior/medial_area/
            mammillary_nuclei/ and hypothalamus/mammillary_bodies/ are
            the SAME STRUCTURE, split across two tree locations. This is
            the ONLY hypothalamic structure documented twice. The full
            content lives in mammillary_bodies/ (memory hub); the
            posterior/medial_area/mammillary_nuclei/ files should be
            DELTAS pointing there.
        (2) LHA CONTINUUM — posterior_part_of_lateral_nucleus/ is the
            THIRD and FINAL segment of the LHA field (anterior →
            tuberal → posterior). Closes the trap opened in
            anterior_part_of_lateral_nucleus/. The full content lives in
            the anterior pole (pattern exemplar); the tuberal and
            posterior segments are deltas that declare continuity edges.
    - The posterior nucleus is the ONLY full Tier 1 leaf in this
      division. All other children are deltas.
    - The division is small: 8 total files (this container, two
      sub-containers, five deltas). Do not pad.
    - The posterior nucleus's arousal function is the sympathetic
      complement of the anterior hypothalamic nucleus's parasympathetic
      role; the two should be consistent in the Stage 4 audit.
    - The posterior LHA segment's continuity to the anterior pole and
      the tuberal segment must be declared in the segment's delta file,
      not here; this container only declares that the field continues.
    - The mammillary nuclei's identity with mammillary_bodies/ must be
      reproduced in the posterior/medial_area/mammillary_nuclei/
      container file and in each left/right delta; this container's
      declaration is the highest level where the trap appears, and the
      children must reproduce it.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin, MCH, ghrelin, leptin),
      05_* (monoamines, orexin, histamine), 10_* (circadian); memory/
      stores/ (episodic, short_term, emotional_valence,
      temporal_sequence_learning, reinforcement_value_based_learning);
      gateway/. Thiamine (for the mammillary bodies) is documented in
      mammillary_bodies/left directly, not via the 12 axes.
    - Reciprocal connections to enforce in Stage 4:
        * posterior/medial_area/mammillary_nuclei/left|right ↔
          hypothalamus/mammillary_bodies/left|right (SAME STRUCTURE;
          Stage 4 must treat as one; do not flag as duplicate).
        * posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus ↔
          anterior/lateral_area/left|right/
          anterior_part_of_lateral_nucleus and
          tuberal/lateral_area/left|right/ (LHA continuum; three
          segments, one field).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          brainstem sympathetic nuclei (RVLM, LC, dorsal raphe).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          hypothalamus/anterior/medial_area/left|right/
          anterior_hypothalamic_nucleus (sympathetic/parasympathetic
          complement).
    - Connects upward to hypothalamus/.
"""