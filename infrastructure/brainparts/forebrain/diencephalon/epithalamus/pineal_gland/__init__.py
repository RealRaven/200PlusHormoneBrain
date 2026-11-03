"""
Package: infrastructure.brainparts.forebrain.diencephalon.epithalamus.pineal_gland
Anatomical Role:
    The pineal gland is a small, unpaired midline endocrine organ attached
    to the dorsal diencephalon via the pineal stalk. It is the brain's
    primary source of circulating melatonin, synthesized from tryptophan
    via serotonin: tryptophan → 5-hydroxytryptophan → serotonin →
    N-acetylserotonin → melatonin[reference:0][reference:1]. Melatonin is
    secreted predominantly at night, inhibited by light, and is the
    principal hormonal output of the gland[reference:2][reference:3].

    Unlike most brain regions, the pineal gland is an *effector* rather
    than a processor: it converts neural circadian signals into a
    hormonal state that broadcasts globally. It does not compute, store,
    or relay information in the way a nucleus does.

Functional Mode:
    - Melatonin secretion: night-time output of melatonin, gated by light
      and driven by the central circadian clock.
    - Circadian transduction: converts SCN neural rhythm into a humoral
      signal. The pathway is multisynaptic: SCN → paraventricular nucleus
      (PVN) → sympathetic preganglionic neurons in the spinal cord →
      superior cervical ganglion (SCG) → noradrenergic fibers → pineal
      [reference:4].
    - Photoperiodic encoding: melatonin duration encodes night length,
      providing seasonal timing information.
    - Circadian gating of downstream physiology: melatonin modulates
      sleep/wake architecture, immune function, and reproductive timing.
    - Temporal integration (supporting role): some literature links
      melatonin to spatio-temporal binding and circadian context
      maintenance[reference:6], but this is a modulatory contribution, not
      a memory-storage role.

Hormonal Modulation (Tier 2 organ — output is primary):
    - Melatonin: primary output. High at night, low during day. Read
      this as the gland's *state variable*.
    - Serotonin: immediate precursor, not a modulatory input in the
      usual sense. Pineal serotonin is consumed to make melatonin
      [reference:7].
    - Norepinephrine: the *input* signal. Noradrenergic fibers from the
      SCG release NE at night, activating aralkylamine N-acetyltransferase
      (AANAT) and driving melatonin synthesis[reference:8].
    - Light: inhibitory input, relayed via the SCN pathway. Light
      suppresses melatonin; darkness permits it.
    - The gland does not *receive* modulation from the wider hormone
      axes in the way a hub does; it is a downstream effector of the
      circadian axis. Document it as a source, not a target.

Memory Interfaces (minimal — Tier 2 organ convention):
    - Reads:
        * temporal_sequence_learning: time-of-day context, used to
          anchor the current circadian phase. This is the only memory
          read.
    - Writes: none. The pineal gland does not store episodic, semantic,
      emotional, or procedural content. It modulates *timing*, not
      content.
    - This read-only, write-nothing pattern is the Tier 2 organ
      convention. Do not invent memory writes for secretory organs.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (applied after the epithalamus-level fragments,
      before the habenular aversive fragment):
        "Circadian state — pineal gland:
         - Circadian phase: [night / day].
         - Melatonin level: [low / moderate / high].
         - Photoperiod context: [short night / long night / neutral].
         If melatonin is high: reduce verbosity, favor reflective or
         sleep-adjacent framing, slow response tempo, and avoid
         high-arousal language. If melatonin is low: restore full
         cognitive engagement and default response tempo. Do not treat
         high melatonin as impairment — it is a state bias, not a
         degradation."
    - The fragment is emitted whenever the pineal channel is active
      (always, since circadian phase is always defined). Unlike the
      habenula fragment, this one is *not* omitted on neutral input;
      circadian state is always present.
    - No multimodal input is consumed here. The model is any-to-any
      (text, image, audio input → text output)[reference:9], but the pineal
      fragment is text-only and modality-agnostic.

Reciprocal Connections (enforce in Stage 4 audit):
    - ← hypothalamus/anterior/medial_area/left|right/
      suprachiasmatic_nucleus (SCN → PVN → spinal cord → SCG → pineal;
      indirect, multisynaptic; the primary circadian driver)
      [reference:10].
    - ← hindbrain/.../superior_cervical_ganglion (not a brain node in
      this tree; document as an external relay if the tree is extended;
      otherwise note the SCG as a named relay in this file only).
    - → systemic circulation (melatonin broadcast; not a brain-region
      edge; no reciprocal node in the tree).
    - ↔ epithalamus/habenular_nuclei/left|right (anatomical neighbors,
      no direct functional projection; document as structural adjacency,
      not a signaling edge).

Notes:
    - Tier 2 organ exemplar: full template, but with the hormone section
      expanded and the memory section reduced to read-only. This is the
      shape for other secretory organs (pituitary_gland/, and the
      circumventricular organs if they are later added). Do not copy the
      Tier 1 hub shape (habenular_nuclei/left/) onto an organ.
    - The "input is norepinephrine, output is melatonin" framing is the
      key distinction from a hub. A hub *transforms* a state; an organ
      *secretes* one. Keep this distinction in every Tier 2 file.
    - The pineal gland is unpaired and midline. There is no left/ or
      right/ delta file for this node. Do not create hemisphere children.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/10_* (circadian, melatonin), chemicals_hormones/
      05_* (serotonin, norepinephrine), memory/stores/
      (temporal_sequence_learning), and gateway/.
    - Connects upward to epithalamus/.
"""