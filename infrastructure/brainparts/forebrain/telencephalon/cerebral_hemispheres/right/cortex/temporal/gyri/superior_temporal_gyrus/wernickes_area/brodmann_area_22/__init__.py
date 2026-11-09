"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22
=====================================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── gyri
                        └── superior_temporal_gyrus
                            └── wernickes_area
                                └── brodmann_area_22   <-- THIS MODULE

**Primary synonym:** Brodmann Area 22 (BA22), nested "Wernicke's-area"
framing on the RIGHT; Right posterior superior temporal auditory/prosodic
cortex (leaf level).
**Cytoarchitectonic designation:** Area 22 of Brodmann (1909). **This is
the same cortical territory as the top-level leaf
``.../temporal/brodmann_areas/brodmann_area_22`` — not a separate field.**
**Part of:** The nested "Wernicke's-area" module
(``.../wernickes_area``), which is in turn a child of the
**superior temporal gyrus** (``.../superior_temporal_gyrus``).
**Location:** The **posterior superior temporal gyrus (STG)** of the
**right** hemisphere — the **right bank of the posterior Sylvian
fissure** — on the lateral temporal surface, extending onto the
**superior temporal plane**.
**Structural parent:** ``.../wernickes_area`` (nested functionally named
region).
**Structural grandparent:** ``.../superior_temporal_gyrus`` (structural
convolution).
**Sibling (dual-framing) module:** ``.../temporal/brodmann_areas/brodmann_area_22``
(top-level cytoarchitectonic framing; structurally identical).
**Cytoarchitectonic type:** **Neocortical (parakoniocortical /
dysgranular)** — BA22 is a **higher-order auditory association cortex**
with a **less prominent layer IV** than the koniocortical A1 and a
**more developed layer III** for cortico-cortical output.

**⚠ CRITICAL NAMING WARNING:** The "Wernicke's area" name on the right
is **INHERITED STRUCTURALLY**, not functionally accurate. The right
nested BA22 leaf is the **right superior temporal auditory/prosodic
cortex** — **NOT** the speech-comprehension hub. Right nested BA22
lesions produce **aprosodia**, **NOT Wernicke's aphasia**.

Overview
--------
This module is the **deepest level** of the **first three-level
structural hierarchy** in the entire brainparts tree, and it is the
**functional framing** of Brodmann Area 22 (BA22) in the **right**
hemisphere. It represents the **same cortical territory** as the
top-level leaf ``.../temporal/brodmann_areas/brodmann_area_22``, but it
accesses that territory **through the "Wernicke's-area" nested path**
and documents the territory with a **functional framing** — with
**right-lateralized prosodic content** rather than the left's
speech-comprehension content.

**This is the first module in the tree whose identity is defined entirely
by its *position in a hierarchy* rather than by a novel cortical
territory.** The territory itself — Brodmann area 22 on the posterior
**right** superior temporal gyrus — has already been documented at the
top-level Brodmann leaf. This module documents the **same territory
through the nested "Wernicke's-area" path**, so that consumers who need
**functionally framed** access to right BA22 (rather than
cytoarchitectonically framed access) have a first-class module to query
— with the **prosodic functional framing** that is the right hemisphere's
actual functional content.

**The "Wernicke's area" framing is a functional inheritance — and on the
right, it is a misnomer.** The "Wernicke's area" name travels down the
path ``superior_temporal_gyrus → wernickes_area → brodmann_area_22`` —
the gyrus is **structural**, the intermediate region is **functionally
named** (with an inherited name), and the leaf is **cytoarchitectonic**.
This module combines both framings: the **cytoarchitectonic identity** of
BA22 (from the leaf name) with the **inherited functional identity** of
"Wernicke's area" (from the parent's name) — but the inherited name does
**not** reflect the right hemisphere's actual function.

**The right nested BA22 leaf is the prosodic mirror of the left.** The
tree provides **two complete access paths** to the same cortical
territory, **on both hemispheres**:

::

    Path A (cytoarchitectonic framing)       Path B (functional framing)
    ─────────────────────────────────        ──────────────────────────────
    temporal/brodmann_areas/                 temporal/gyri/superior_temporal_gyrus/
    └── brodmann_area_22                     └── wernickes_area/
        (top-level leaf)                         └── brodmann_area_22
                                                     (nested leaf; THIS MODULE)

**Both paths return the same cortical territory.** The top-level path
answers *"which cytoarchitectonic field is this?"* — the leaf's
**laminar organization, cell density, and thalamic input** are the
primary constants. The nested path answers *"which functionally named
region is this?"* — but on the **right**, the answer is **prosodic, not
speech-comprehension**. The nested path's **functional content is the
right superior temporal auditory/prosodic cortex**, not the
speech-comprehension hub.

**The parent `wernickes_area` module carries the same right-specific
prosodic warning.** This module **inherits** that warning and preserves
it, so that a consumer querying the nested BA22 leaf directly (rather
than through the parent) still sees the inherited-name caveat.

The Nested Dual-Framing Context
-------------------------------
This module is the **deepest level** of the three-level structural
hierarchy, which is **bilaterally instantiated** across the tree:

::

    Three-level structural hierarchy (right hemisphere)
    ───────────────────────────────────────────────────
    Level 1: superior_temporal_gyrus    (structural convolution)
    Level 2: wernickes_area              (nested functionally named region;
                                          INHERITED NAME on right)
    Level 3: brodmann_area_22            (nested Brodmann leaf; THIS MODULE;
                                          PROSODIC functional content)

    Dual-framing counterpart (top-level)
    ────────────────────────────────────
    temporal/brodmann_areas/brodmann_area_22
    (cytoarchitectonic framing; same cortical territory)

**The two right BA22 modules are structurally identical in their
cytoarchitectonic constants.** They represent the **same cortical
territory** with the **same laminar organization, cell density, and
thalamic input**. **Only the framing differs:**

*   **Top-level BA22** (`.../temporal/brodmann_areas/brodmann_area_22`)
    — **cytoarchitectonic framing**: right BA22 as a **Brodmann field**,
    documented primarily by its **laminar organization, cell density,
    boundaries, and thalamic input**.
*   **Nested BA22** (this module) — **functional framing**: right BA22
    as the **right posterior superior temporal auditory/prosodic
    cortex**, documented primarily by its **prosodic comprehension
    functions, aprosodia syndrome, and prosodic-network participation**
    — with the inherited "Wernicke's-area" name flagged as a **structural
    inheritance, not a functional claim**.

**Consumers must not assume that the top-level and nested right BA22
modules are different cortical territories.** They are the **same
territory** with **two framings**. The `DUAL_FRAMING` constant below
makes this explicit and greppable, **and** the `INHERITED_NAME_WARNING`
constant flags the prosodic-asymmetry caveat.

Cytoarchitecture
----------------
The nested right BA22 leaf shares **all cytoarchitectonic constants**
with the top-level right BA22 leaf, and with the **left** nested BA22
leaf. The cytoarchitecture is **summarized here for reference**;
consumers that need **detailed cytoarchitectonic constants** should
query the top-level leaf (``.../temporal/brodmann_areas/brodmann_area_22``):

*   **Parakoniocortical / dysgranular** — BA22 is a **higher-order
    auditory association cortex**, with a **less prominent layer IV**
    than the koniocortical A1 (BA41/BA42) and a **more developed layer
    III** for cortico-cortical output.

*   **Laminar profile** — a **granular layer IV** is present but
    **thinner and less sharply delineated** than in A1. **Layer III**
    contains **large pyramidal cells** — the **principal output neurons**
    to the arcuate fasciculus (on the left) or the right-hemisphere
    prosodic network (on the right).

*   **Hemispheric asymmetry** — BA22 exhibits **interhemispheric
    microcircuitry differences** that accompany its **functional
    lateralization** (speech on the left, prosody on the right). The
    cytoarchitectonic constants are **structurally identical** between
    the left and right nested BA22 leaves; only the **functional
    framing** differs.

**This cytoarchitectonic profile is inherited from the top-level BA22
leaf** and is documented here only at the level of summary. Consumers
that need **detailed laminar constants** should query the top-level
leaf — and they should note that the **right** cytoarchitectonic
constants are **structurally identical** to the left's.

Function in the Human Brain
---------------------------
The nested right BA22 leaf is the **leaf-level functional framing of the
right prosodic cortex**. Its best-supported functions cluster into six
domains — **the right-lateralized mirror of the left nested BA22 leaf's
speech-comprehension functions**:

*   **Emotional Prosody Comprehension (the defining function):** The
    right nested BA22 leaf is the **leaf-level substrate for the
    comprehension of emotional prosody** — the melodic, rhythmic, and
    affective dimensions of speech. **Emotional prosodies activate the
    right STG (BA22)**, and the **contrast of emotional vs. neutral
    prosodies shows rightward lateralization**.

*   **Affective Intonation and Speech Melody:** The right nested BA22
    leaf is **more sensitive to the overall intonational pattern** of
    speech — the **fundamental frequency (F0)** and its variation. This
    is the **right-hemisphere complement** to the left Wernicke's
    area's phonological-semantic processing.

*   **Discrimination of Emotional vs. Neutral Prosody:** The right
    nested BA22 leaf is **primarily responsible** for the discrimination
    of emotional vs. neutral prosodies. This is the **functional
    signature** of the right nested BA22 leaf — a **selective** prosodic
    function with no left-hemisphere analogue.

*   **Prosodic Input Region for Affective Comprehension:** Dynamic causal
    modeling shows that the **right posterior STG (BA22) is the input
    region** for affective-prosody comprehension, with information
    transferred to the frontal lobes via parallel pathways.

*   **Sensory Aprosodia Substrate:** The right nested BA22 leaf is the
    **leaf-level substrate for sensory aprosodia** — the **inability to
    comprehend prosodic changes in speech**. This is the **right-
    hemisphere analogue of Wernicke's aphasia** — the same structural
    lesion site, the mirrored functional deficit.

*   **Music-Adjacent Prosodic Processing:** Consistent with its prosodic
    function, the right nested BA22 leaf contributes to **music-adjacent
    prosodic processing** — the analysis of pitch contour and melodic
    structure in speech and song.

**These functions are the leaf-level instantiation of the parent
`wernickes_area` module's right-lateralized prosodic functions.** No new
functional content is introduced here — the module's role is to provide
**leaf-level access** to those functions via the nested
"Wernicke's-area" path, with the **inherited-name caveat explicitly
documented**.

Associated Disorders
--------------------
Damage to or dysfunction of the nested right BA22 leaf is associated with
the **same disorders as the parent `wernickes_area` module on the
right**:

*   **Sensory Aprosodia (the signature syndrome):** **Sensory aprosodia**
    — the **inability to comprehend prosodic changes in voice and body
    language** — follows **right posterior STG (BA22) damage**. This is
    the **right-hemisphere analogue of Wernicke's aphasia**.

*   **Affective Prosody Deficits:** Impaired **comprehension of
    emotional vs. neutral prosodies** — the right posterior STG's
    selective function.

*   **Impaired Prosodic Comprehension in Speech:** Difficulty
    **interpreting the melodic and intonational pattern** of speech — a
    prosodic analogue of receptive language impairment.

*   **Findings Reported in Autism and Right-Hemisphere Lesion
    Populations:** The right STG/BA22 has been implicated in autism
    (reduced prosodic processing in the right STG/STS) and in
    right-hemisphere lesion syndromes (aprosodia spectrum). These are
    **findings reported** rather than established syndrome attributions.

**What is NOT here:** **Wernicke's aphasia**, **pure word deafness**,
**lexical-semantic deficits**, and **phonological processing deficits**
are **left nested BA22** functions. They are **absent** from right
nested BA22 lesions. They are documented in the left nested BA22 leaf
and are **explicitly not claimed here**. The right nested BA22 leaf is
the **prosody pole**; the left nested BA22 leaf is the
**speech-comprehension** pole.

**CRITICAL WARNING:** The right nested BA22 leaf **shares the name**
with the left nested BA22 leaf — inherited from the parent
`wernickes_area` module — but **NOT the function**. A consumer that
assumes the right nested BA22 leaf is the speech-comprehension hub will
be **clinically wrong**. Right nested BA22 lesions produce **aprosodia**,
not **Wernicke's aphasia**.

Lateralization Notes
--------------------
This is the **right** nested BA22 leaf. The lateralization landscape is
**strongly right-loaded for prosody** — the mirror image of the left
nested BA22 leaf's left-loaded speech profile:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Emotional prosody comprehension** — the melodic and affective
      dimensions of speech.
    - **Affective intonation and speech melody** — F0 tracking.
    - **Discrimination of emotional vs. neutral prosody**.
    - **Prosodic input region for affective comprehension**.
    - **Sensory aprosodia substrate** — the signature syndrome.

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Speech comprehension** — the left nested BA22 hub.
    - **Lexical-semantic processing** — linking spoken words to meanings.
    - **Phonological processing** — analysis of speech sounds.
    - **Naming and word retrieval**.
    - **Auditory short-term memory and repetition**.
    - **Reading and writing**.
    - **Wernicke's aphasia substrate** — the left nested BA22 signature
      syndrome.

*   **Symmetric Functions (bilateral properties of BA22):**
    - **Auditory processing** of complex sounds (with right dominance for
      prosody, left dominance for speech).
    - **Basic acoustic feature analysis** (shared with BA41/42).
    - **Auditory memory** (bilateral component).

**This is the "right-loaded" pattern at its most extreme — the mirror
image of the left-loaded speech hub.** The left nested BA22 leaf is the
**speech-comprehension hub**; the right nested BA22 leaf is the
**prosodic and emotional-intonation cortex**. The asymmetry is
**maximal** — the two hemispheres carry **functionally distinct,
non-overlapping named syndromes** (Wernicke's aphasia vs. aprosodia).

**A consumer that assumes "right nested BA22 = left nested BA22" will
be wrong for the entire speech-comprehension domain.** The left is the
**speech hub**; the right is the **prosodic hub**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    right frontal operculum (BA47) or the right parietal lobe. Those are
    **downstream targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Nested-leaf status — flagged in data.** This module is the
    **deepest level** of the three-level structural hierarchy
    (STG → wernickes_area → BA22). The ``NESTED_LEVEL`` constant is
    **"brodmann_leaf"**.
*   **Dual-framing — flagged in data.** The top-level Brodmann leaf
    ``.../temporal/brodmann_areas/brodmann_area_22`` and this nested
    leaf represent the **same cortical territory** with **different
    framings**. The ``DUAL_FRAMING`` constant documents this.
*   **No novel cytoarchitectonic or functional content.** This module
    inherits its cytoarchitectonic and functional constants from the
    top-level BA22 leaf and the parent `wernickes_area` module. It
    exists to provide **leaf-level access via the nested
    "Wernicke's-area" path** — with **prosodic** functional content.
*   **Inherited-name warning — flagged in data.** The "Wernicke's area"
    name on the right is **inherited structurally, not functionally
    accurate**. The ``INHERITED_NAME_WARNING`` constant makes this
    explicit and greppable.
*   **Right-lateralized prosodic functions — flagged in data.** The
    ``RIGHT_LATERALIZED`` constant documents the right-lateralized
    prosodic functions.
*   **Left-lateralized speech functions explicitly DENIED — flagged in
    data.** The ``DENIED_LEFT_LATERALIZED`` constant documents the
    left-lateralized functions that are **not claimed** here.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri.superior_temporal_gyrus.wernickes_area import brodmann_area_22

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.gyri.superior_temporal_gyrus."
        "wernickes_area.brodmann_area_22"
    )

**⚠ WARNING:** The right nested BA22 leaf is **prosodic**, NOT
speech-comprehension. Use the `INHERITED_NAME_WARNING` constant to
check::

    from ...brodmann_area_22 import INHERITED_NAME_WARNING
    # INHERITED_NAME_WARNING = True

**This is the nested (functional) framing of right BA22.** For the
top-level (cytoarchitectonic) framing of the **same cortical
territory**::

    from ...temporal.brodmann_areas import brodmann_area_22

For the dual-framing::

    from ...wernickes_area.brodmann_area_22 import DUAL_FRAMING
    # DUAL_FRAMING = {
    #     "top_level": "temporal.brodmann_areas.brodmann_area_22",
    #     "nested": "temporal.gyri.superior_temporal_gyrus."
    #               "wernickes_area.brodmann_area_22",
    #     "structurally_identical": True,
    # }

For the nested level::

    from ...wernickes_area.brodmann_area_22 import NESTED_LEVEL
    # NESTED_LEVEL = "brodmann_leaf"

For the right-lateralized functions::

    from ...wernickes_area.brodmann_area_22 import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("emotional_prosody_comprehension",
    #                      "affective_intonation_speech_melody",
    #                      "emotional_vs_neutral_prosody_discrimination",
    #                      "prosodic_input_affective_comprehension",
    #                      "sensory_aprosodia_substrate")

For the left-lateralized functions explicitly denied here::

    from ...wernickes_area.brodmann_area_22 import DENIED_LEFT_LATERALIZED
    # DENIED_LEFT_LATERALIZED = ("speech_comprehension",
    #                            "lexical_semantic_processing",
    #                            "phonological_processing",
    #                            "naming_and_word_retrieval",
    #                            "auditory_short_term_memory_and_repetition",
    #                            "reading_and_writing",
    #                            "wernickes_aphasia_substrate")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba22_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.superior_temporal_gyrus."
            f"wernickes_area.brodmann_area_22"
        )
        # resolve ba22_path through the memory/recall layer

References
----------
*   **Right STG and emotional prosody:** Mitchell, R.L.C., et al. (2003).
    "The neural response to emotional prosody, as revealed by functional
    magnetic resonance imaging." *Neuropsychologia*, 41(10), 1410–1421.
    Passive listening to emotional prosody activates the lateral
    temporal lobe (STG/MTG) with **relative right-lateralisation**;
    attention to emotional prosody induces **right-lateralised activity**
    including the STG.
*   **Right posterior STG and emotional vs. neutral prosody:** *Speech
    Prosodies of Different Emotional Categories Activate Different Brain
    Regions in Adult Cortex: an fNIRS Study* (2018), *Sci Rep*, 8, 607.
    **Emotional prosodies activated the right STG (BA22) and right
    primary/secondary AC (BA42)**; the **contrast of emotional vs.
    neutral prosodies showed rightward lateralization**.
*   **Right posterior STG as prosodic input region:** *Cerebral pathways
    in processing of affective prosody: A dynamic causal modeling study*
    (2005), *NeuroImage*. The **right posterior STG (BA22) is the input
    region** for affective-prosody comprehension, with information
    transferred to the frontal lobes via parallel pathways.
*   **Right-hemisphere prosodic network:** Wildgruber, D., et al. (2005).
    "Identification of emotional intonation evaluated by fMRI."
    *NeuroImage*, 24(4), 1233–1241. Comprehension of affective prosody
    is bound to a **right-hemisphere pattern** including posterior STS
    (BA22), dorsolateral (BA44/45), and orbitobasal (BA47) areas.
*   **Sensory aprosodia and right BA22:** *Brodmann Area 22 — Superior
    Temporal Gyrus* (Neurofeedback Academy). **Prosody and emotional
    speech processing (right)**; **sensory aprosodia (right)**; right
    BA22 aids in the interpretation of prosody, and damage causes
    sensory aprosodia.
*   **Aprosodia (right-hemisphere analogue of aphasia):** Ross, E.D.
    (1981). "The aprosodias: functional-anatomic organization of the
    affective components of language in the right hemisphere." *Arch
    Neurol*, 38(9), 561–569. Right posterior STG damage produces
    **aprosodia**, not aphasia.
*   **Dual-framing (nested + top-level BA22):** *Wernicke's area — a
    review* (2018), *Brain Struct Funct*. The nested "Wernicke's area"
    framing on the right represents the **same cortical territory** as
    the left, but the **functional content is prosodic** — the name is
    a **structural inheritance, not a functional claim**.
*   **Cytoarchitecture (BA22):** *Interhemispheric Asymmetries of the
    Modular Structure in Human Temporal Cortex* (2000), *Science*.
    Language-relevant processing of auditory signals is lateralized and
    involves the **posterior part of Brodmann area 22**; functional
    lateralization is accompanied by **interhemispheric differences in
    intrinsic microcircuitry**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Lateral temporal and superior temporal plane
    anatomy.)
*   NeuroNames — Brodmann area 22 (right, nested Wernicke's-area
    framing); FMA — right posterior superior temporal gyrus.
"""