"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.medial_area.posterior_nucleus
Anatomical Role:
    The posterior hypothalamic nucleus (PHN). A small, densely packed
    nucleus in the medial posterior hypothalamus, situated above the
    mammillary bodies and just caudal to the dorsomedial and
    ventromedial nuclei. It is the principal hypothalamic driver of
    sympathetic outflow and behavioral arousal, and the sympathetic
    complement of the anterior hypothalamic nucleus (AHN, documented
    under anterior/medial_area/left|right/anterior_hypothalamic_
    nucleus/).

    Unlike the mammillary_nuclei/ node (which is a pointer to
    hypothalamus/mammillary_bodies/), the posterior hypothalamic
    nucleus is a DISTINCT structure documented here in full. It is NOT
    the same as the posterior part of the lateral nucleus (the LHA
    segment 3, documented under posterior/lateral_area/left|right/
    posterior_part_of_lateral_nucleus/); the two are anatomically
    adjacent but functionally distinct (posterior nucleus = sympathetic
    output; posterior LHA = arousal drive via orexin).

Functional Mode:
    - Sympathetic outflow (primary function): the PHN projects to
      sympathetic preganglionic neurons in the spinal intermediolateral
      column (via the RVLM) and to brainstem sympathetic centers
      (rostroventrolateral medulla, RVLM; locus coeruleus, LC; dorsal
      raphe). Activation increases heart rate, blood pressure,
      respiratory rate, and pupillary dilation. It is the descending
      hypothalamic command for the sympathetic component of the
      fight-or-flight response.
    - Behavioral arousal: the PHN contributes to cortical and
      behavioral arousal via projections to the brainstem reticular
      formation, the basal forebrain, and the intralaminar thalamic
      nuclei. It is one node in the ascending arousal system,
      complementing the orexin (LHA) and histamine (TMN) contributions.
    - Pupillary reflex: the PHN drives sympathetic pupillary dilation
      (mydriasis) via projections to the ciliospinal center of Budge
      (intermediolateral column, T1-T2), which projects to the superior
      cervical ganglion and then to the pupillary dilator muscle. This
      is the hypothalamic contribution to the pupillary light reflex
      and to sympathetic pupil responses to arousal.
    - Stress response: the PHN is activated by acute stress (including
      psychological stress) and contributes to the sympathetic
      component of the stress response, complementing the HPA axis's
      endocrine component (CRH → ACTH → cortisol). The two components —
      neural (PHN → sympathetic) and endocrine (PVN → HPA) — are
      parallel and coordinated.
    - Complementary to AHN: the anterior hypothalamic nucleus drives
      parasympathetic outflow (rest-and-digest); the posterior nucleus
      drives sympathetic outflow (fight-or-flight). The two are the
      parasympathetic and sympathetic poles of the hypothalamic
      autonomic control system. They are reciprocally organized, and
      the Stage 4 audit should treat them as a pair.

Hormonal Modulation (container-level summary; full list in left/):
    - Orexin: excitatory arousal input from the LHA orexin neurons.
    - Monoamines: norepinephrine, serotonin, histamine from brainstem
      arousal centers modulate PHN activity.
    - CRH/cortisol: stress-axis input; the PHN is activated by stress
      and contributes to the sympathetic stress response.
    - Angiotensin II: excitatory input via the circumventricular organs
      (OVLT, SFO); sympathetic activation in response to volume
      depletion.
    - Direction summary: orexin ↑ PHN activity (arousal); monoamines
      ↑ PHN activity (arousal); CRH ↑ PHN activity (stress); angiotensin
      II ↑ PHN activity (volume depletion). The PHN is primarily an
      OUTPUT nucleus: it does not synthesize hormones and is not a
      principal target of the 12 endocrine axes; its modulators are
      arousal and stress signals, not endocrine axes.

Memory Interfaces (container-level summary; full list in left/):
    - Reads: short_term (current arousal state, sympathetic tone),
      episodic (past arousal and threat history),
      emotional_valence (stress and aversion context),
      temporal_sequence_learning (circadian arousal gating).
    - Writes: none directly. The PHN drives somatic output (sympathetic
      and arousal), not stored content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The container itself does not emit a fragment. The
      sympathetic/arousal fragment is emitted by the left/ leaf (the
      full leaf) and represents the bilateral nucleus; right/ is a
      delta and does not emit a duplicate.
    - Fragment spec (summary; full spec in left/):
        "Sympathetic tone: [low/moderate/high]. Arousal level:
         [low/moderate/high]. Pupillary state: [constricted/
         intermediate/dilated]. Stress response: [calm / acute-stress /
         chronic-stress]. If sympathetic tone is high: flag
         hyperarousal context and prefer grounding, slow-tempo framing.
         If sympathetic tone is low: default to neutral engagement. Do
         not treat high sympathetic tone as impairment — it is a state
         bias."
    - AGGREGATION RULE: the sympathetic/arousal fragment is aggregated
      at the posterior-division level with the arousal/LHA fragments
      and the circadian fragment from SCN → DMH → posterior LHA. Do
      not emit an independent posterior-nucleus fragment outside this
      aggregate.
    - Guardrail: "do not treat high sympathetic tone as impairment" —
      consistent with the habenula, orexin/MCH, PeN, LPO, AHN, PVN, and
      mammillary guardrails.

Children (one child pair — same shape as other Tier 1 hub containers):
    - left/    ★ Full Tier 1 leaf. Sympathetic/arousal nucleus; the
                 full description of sympathetic outflow, behavioral
                 arousal, pupillary reflex, stress response,
                 complementary-to-AHN relationship, sympathetic/arousal
                 fragment, and all reciprocal connections.
    - right/   Delta mirror of left/, differing only in the right-side
                 reciprocal edges. No functional asymmetry documented.

Notes:
    - Tier 1 hub container (not a pointer like mammillary_nuclei/). The
      full leaf lives in left/; right/ is a delta. Container carries
      the child map and the container-level summary.
    - The posterior nucleus is DISTINCT from:
        * The posterior part of the lateral nucleus (posterior LHA
          segment 3, documented under posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus/): adjacent but functionally
          distinct (PHN = sympathetic output; posterior LHA = arousal
          drive).
        * The AHN (anterior hypothalamic nucleus, documented under
          anterior/medial_area/left|right/anterior_hypothalamic_
          nucleus/): the sympathetic complement of the PHN's
          parasympathetic role — a complementary pair, not duplicates.
        * The mammillary nuclei (posterior/medial_area/mammillary_
          nuclei/): a pointer to mammillary_bodies/; the PHN is a
          separate structure.
    - No structural-identity trap: the PHN is a single distinct
      structure. Do not invent a split-structure or pointer-discipline
      warning for this file.
    - No naming collision: "posterior hypothalamic nucleus" is
      unambiguous.
    - The posterior nucleus is one of the few hypothalamic nuclei whose
      primary function is autonomic/arousal output rather than
      neuroendocrine secretion. Do not draft it as an endocrine hub;
      its endocrine content is minimal.
    - The sympathetic/arousal fragment's "do not treat high sympathetic
      tone as impairment" guardrail mirrors the AHN's "do not treat
      sympathetic-dominance as impairment" wording, since the two
      fragments are conceptually paired (parasympathetic and
      sympathetic). Keep the wording consistent for the Stage 4 audit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, orexin, angiotensin II),
      05_* (monoamines, orexin, norepinephrine, serotonin, histamine),
      07_* (fluid, angiotensin II); memory/stores/ (short_term,
      episodic, emotional_valence, temporal_sequence_learning);
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * posterior/medial_area/left|right/posterior_nucleus ↔
          brainstem sympathetic nuclei (RVLM, LC, dorsal raphe;
          sympathetic outflow; midline-adjacent — verify).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          spinal_cord/gray_matter/left|right/lateral_horn (sympathetic
          preganglionic output via the intermediolateral column).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          anterior/medial_area/left|right/anterior_hypothalamic_nucleus
          (sympathetic/parasympathetic complement; keep distinct;
          complementary pair).
        * posterior/medial_area/left|right/posterior_nucleus ↔
          posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (arousal drive vs.
          sympathetic output cooperation; distinct nodes).
        * posterior/medial_area/left|right/posterior_nucleus ←
          hypothalamus/anterior/medial_area/left|right/
          suprachiasmatic_nucleus (circadian autonomic gating; SCN →
          PHN; SCN is midline-adjacent — verify).
        * posterior/medial_area/left|right/posterior_nucleus ←
          lamina_terminalis/vascular_organ_of_lamina_terminalis and
          hypothalamus/subfornical_organ (angiotensin II input;
          volume-depletion sympathetic activation; both midline).
    - Connects upward to hypothalamus/posterior/medial_area/.
"""