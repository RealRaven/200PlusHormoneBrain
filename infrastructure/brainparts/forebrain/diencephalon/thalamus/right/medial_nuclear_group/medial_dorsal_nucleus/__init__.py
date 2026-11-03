"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.medial_dorsal_nucleus
Anatomical Role:
    The right mediodorsal nucleus (MD). The LARGEST and most studied
    nucleus of the right medial nuclear group, situated in the
    dorsomedial thalamus, adjacent to the right midline nuclei and to
    the right internal medullary lamina. Same PREFRONTAL RELAY role as
    the left MD: driver input from the right prefrontal cortex, the
    right amygdala, the right substantia innominata, and the right
    ventral pallidum; output to the right prefrontal cortex (especially
    the dorsolateral and orbitofrontal PFC).

    See ../../../../left/medial_nuclear_group/medial_dorsal_nucleus/
    __init__.py for the full anatomical description, the three MD
    subdivisions (medial/magnocellular, central/parvicellular, lateral),
    the executive/limbic-prefrontal loop framing, the
    working-memory/decision-making/reward-based-learning/affective-
    regulation functional roles, and the three clinical facts.

    Reproduced THREE TRAPS (apply equally on the right):

    - MD vs. ANTERIOR NUCLEAR GROUP (the primary trap): the right MD
      is the PREFRONTAL relay (amygdala/PFC → MD → PFC). The right
      anterior nuclei (right/anterior_nuclear_group/) are the PAPEZ
      memory relays (hippocampus → mammillary bodies → anterior nuclei
      → cingulate). Different circuits; do not merge.

    - MD vs. MIDLINE FAMILY (intra-group sub-trap): the right MD is a
      DISCRETE prefrontal relay; the right midline nuclei
      (right/medial_nuclear_group/midline_nuclear_group/) are a
      DISTRIBUTED limbic/visceral family. Different families; do not
      merge.

    - MD vs. MEDIAL PULVINAR (cross-group sub-trap): both project to
      the right PFC, but the right MD is the PRINCIPAL prefrontal
      relay (first-order; amygdala/PFC driver) while the right medial
      pulvinar (right/lateral_nuclear_group/pulvinar/) is a
      MULTISENSORY association relay (higher-order; multimodal
      driver). Different relay types; do not merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/medial_dorsal_
    nucleus/: prefrontal relay (the anchor); working memory;
    decision-making and reward-based learning; affective regulation
    (medial/magnocellular subdivision); higher-order association
    (lateral subdivision). No documented functional asymmetry between
    left and right MD. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically, with the same
    established/investigational framing):
        (1) RIGHT MD LESION SYNDROME (executive-affective syndrome):
            working-memory impairment, decision-making deficits
            (especially reward-based and reversal learning), affective
            dysregulation, and sometimes apathy or personality change.
            Established; the MD's defining clinical anchor on the
            right as on the left.
        (2) TREATMENT-RESISTANT DEPRESSION AND RIGHT MD DBS: the right
            MD is a DBS target for treatment-resistant depression;
            right MD DBS is part of the same body of evidence as left
            MD DBS (investigational; active; case series + small
            trials).
        (3) SCHIZOPHRENIA AND RIGHT MD STRUCTURAL/CONNECTIVITY
            DEFICITS: reduced right MD volume and reduced right MD-PFC
            connectivity are reported in schizophrenia; the right MD
            is part of the bilateral MD pathophysiology finding
            (established structural finding).

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/medial_dorsal_
    nucleus/. Minimal; cholinergic, monoaminergic, and dopaminergic
    (right VTA) modulation of the MD-PFC loop. Not a principal target
    of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/medial_dorsal_
    nucleus/. Reads episodic, semantic, reinforcement_value_based_
    learning, and short_term (the thickest memory interface of any
    thalamic nucleus, reflecting the executive/limbic-prefrontal
    loop's use of all four stores). Writes nothing directly (relay,
    not encoder).

Model Integration (Gemma-4-E2B):
    No right MD fragment. The MD is a prefrontal relay; the model
    prompt does not need an MD block. The executive/limbic signals it
    relays are already represented in the upstream (right PFC, right
    amygdala, right ventral pallidum) and downstream (right PFC)
    fragments. The PFC carries the executive state; the amygdala
    carries the affective state.

Right-specific reciprocal connections to enforce in Stage 4:

    Executive/limbic-prefrontal loop (the anchor):
    - ← telencephalon/cerebral_hemispheres/right/cortex/frontal/
      prefrontal_cortex (the right MD's principal cortical input;
      the MD-PFC loop; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/frontal/
      prefrontal_cortex (the right MD's principal cortical output;
      the MD-PFC loop; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (right amygdala → right MD; limbic-affective input; right-side).
    - ← telencephalon/.../subcortical/basal_forebrain/substantia_
      innominata (right substantia innominata → right MD;
      basal-forebrain limbic input; right-side).
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      right (right ventral pallidum → right MD; basal-ganglia limbic
      input; right-side).

    Higher-order association (secondary; lateral MD subdivision):
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/frontal/*
      (right multimodal association PFC; right-side).

    Subcortical and brainstem (modulatory):
    - ← midbrain/tegmentum/ventral_tegmental_area (VTA dopamine →
      right MD; the mesocortical dopamine system's thalamic relay;
      VTA is midline-adjacent — verify).
    - ← brainstem/.../locus_coeruleus (noradrenergic modulation; LC
      is midline-adjacent — verify).
    - ← brainstem/.../dorsal_raphe_nucleus (serotonergic modulation;
      raphe is midline).
    - ← telencephalon/.../subcortical/basal_forebrain (cholinergic
      modulation; right-side).

    Intra-group:
    - ↔ ../intralaminar_nuclear_group/ (right intralaminar family is
      AROUSAL/ATTENTION; the right MD is the PREFRONTAL relay;
      different families; do not merge).
    - ↔ ../midline_nuclear_group/ (right midline family is LIMBIC/
      VISCERAL; the right MD is the PREFRONTAL relay; different
      families; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../../anterior_nuclear_group/ (right MD = PREFRONTAL relay;
      right anterior nuclei = PAPEZ memory relays; different
      circuits; do not merge).
    - ↔ ../../lateral_nuclear_group/pulvinar/ (right MD = discrete
      prefrontal relay; right medial pulvinar = multisensory
      association relay that also projects to the PFC; different
      relay types; do not merge).

    - ↔ ../../../../left/medial_nuclear_group/medial_dorsal_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      medial_dorsal_nucleus/. Not a full leaf. Do not duplicate.
    - THE MD PAIR IS NOW COMPLETE: with this file, the mediodorsal
      nucleus is fully documented on both hemispheres — the medial
      nuclear group's anchor is done. The three MD clinical facts
      (executive-affective syndrome; depression DBS; schizophrenia
      structural finding) are documented on both sides.
    - THE THREE TRAPS are reproduced in abbreviated form; the full
      text is in ../../../../left/medial_nuclear_group/medial_dorsal_
      nucleus/ and ../../../__init__.py. A contributor entering at
      the right MD must see them.
    - THE MD's THREE SUBDIVISIONS (medial/magnocellular,
      central/parvicellular, lateral) are documented WITHIN the left
      MD leaf, not as child nodes. Same convention applies on the
      right: do not create medial_md/, central_md/, or lateral_md/ as
      child nodes here either.
    - THE THREE CLINICAL FACTS apply on the right identically, with
      the same established/investigational framing:
        (1) Right MD lesion syndrome (executive-affective).
        (2) Right MD DBS for treatment-resistant depression
            (investigational; active).
        (3) Right MD structural/connectivity deficits in schizophrenia
            (established structural finding).
    - THE RIGHT MD'S MEMORY INTERFACE IS THE THICKEST OF ANY THALAMIC
      NUCLEUS ON THE RIGHT: reads episodic + semantic +
      reinforcement_value_based_learning + short_term, same as the
      left MD. The executive/limbic-prefrontal loop uses all four
      stores.
    - NO FRAGMENT: same as the whole thalamus. The right MD is a
      relay, not a state-emitter.
    - The right MD is NOT the right anterior group (Papez memory
      relay), NOT the right midline family (limbic/visceral), NOT the
      right medial pulvinar (multisensory association), NOT the right
      intralaminar family (arousal/attention). The traps make these
      distinctions explicit on the right.
    - Midline targets (VTA, LC, raphe) are flagged with "verify" so
      Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right PFC, right amygdala,
      right substantia innominata, right ventral pallidum, right
      basal forebrain, right multimodal PFC, right intralaminar
      family, right midline family, right anterior group, and right
      medial pulvinar are hemisphere-split and require right-side
      targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/medial_dorsal_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""