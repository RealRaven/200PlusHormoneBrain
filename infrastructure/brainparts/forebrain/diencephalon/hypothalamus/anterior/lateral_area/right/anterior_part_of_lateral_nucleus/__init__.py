"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.right.anterior_part_of_lateral_nucleus
Anatomical Role:
    Right hemisphere of the anterior part of the lateral nucleus. Contains
    the same intermingled orexin/hypocretin and MCH populations as
    ../left/, mirrored to the right hemisphere. See ../left/__init__.py
    for the full anatomical description, the LHA-continuum discussion,
    and the two-mode framing.

    Reproduced critical warning (applies equally on the right):
    CRITICAL DISTINCTION FROM LHA — this node is the *anterior pole* of
    the right LHA orexin/MCH field, not the whole LHA. The LHA proper
    spans the tuberal and posterior divisions and is documented under
    hypothalamus/tuberal/lateral_area/right/. Stage 4 audit should treat
    the anterior and tuberal LHA orexin/MCH populations as a *continuum*,
    not as duplicate structures. Do not merge the nodes.

Functional Mode:
    Same as ../left/. Orexin drives arousal, feeding drive, and reward;
    MCH drives sleep, energy conservation, and reduced locomotor activity.
    The two populations are intermingled but antagonistic, operating as
    a two-mode nucleus (ORX-dominant vs. MCH-dominant). No documented
    functional asymmetry between left and right for this nucleus.
    Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Ghrelin ↑ ORX, leptin ↓ ORX, glucose ↓ ORX and
    ↑ MCH, estrogen ↓ MCH, NPY ↑ MCH. See ../left/__init__.py § Hormonal
    Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term, reinforcement_value_based_learning,
    temporal_sequence_learning, emotional_valence; writes no stored content
    directly. See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. The arousal/feeding fragment
    (ORX/MCH dominant mode, feeding motivation, guardrail against treating
    MCH-dominance as impairment) is emitted once at the left/ level and
    represents the bilateral nucleus. Emitting a separate right-hemisphere
    fragment would double-count the arousal signal. See
    ../left/__init__.py § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus
      (orexin → LC; excitatory; arousal; right-side target)
    - → midbrain/tegmentum/ventral_tegmental_area (orexin → VTA;
      excitatory; reward/motivation; VTA is midline-adjacent, not
      hemisphere-split — verify)
    - → midbrain/tegmentum/dorsal_raphe_nucleus (orexin → raphe;
      arousal; raphe is midline)
    - → telencephalon/cerebral_hemispheres/right/subcortical/
      basal_forebrain (orexin → basal forebrain; arousal; right-side
      target)
    - ↔ hypothalamus/tuberal/lateral_area/right/ (same ORX/MCH field;
      anterior-to-tuberal continuity; document as continuum, not
      duplicate)
    - ↔ hypothalamus/anterior/medial_area/right/arcuate_nucleus/ (NPY/
      AgRP → MCH; leptin/ghrelin → ORX)
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → LHA; circadian gating)
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed)

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - The LHA-continuum warning is reproduced above because it is a
      structural trap that applies on both hemispheres. The other
      content (two-mode framing, hormone directions, memory schema) is
      referenced rather than duplicated.
    - No hemisphere-specific model fragment: the left-side fragment is
      bilateral. This is the same convention as habenular_nuclei/right/.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/lateral_area/right/.
"""