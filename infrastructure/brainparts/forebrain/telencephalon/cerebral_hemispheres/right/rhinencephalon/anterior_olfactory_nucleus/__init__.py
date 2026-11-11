"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon.anterior_olfactory_nucleus
=====================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── rhinencephalon
                └── anterior_olfactory_nucleus   <-- THIS MODULE

**Primary synonym:** Anterior olfactory nucleus (AON); anterior olfactory
cortex; nucleus olfactorius anterior.
**Cytoarchitectonic designation:** **Not a Brodmann area.** Sometimes
called the **anterior olfactory cortex** because of its cortical-like
layered structure[reference:0].
**Part of:** The **primary olfactory pathway** — the **first central
relay** beyond the olfactory bulb.
**Structural parent:** ``.../right/rhinencephalon/`` → **direct child** of
the rhinencephalon container.
**Structural children:** **None.** This is a **leaf** module. The four
classical subdivisions (pars externa, medialis, lateralis, ventralis)
are documented as **prose**, not as structural children.
**Boundary status:** **Boundary case — continuous with the olfactory
bulb caudally and embedded in the olfactory peduncle/tract.** Classical
and comparative anatomy treat the AON variously as (a) the **caudal
extension of the olfactory bulb**, (b) a **distinct nucleus** in the
olfactory peduncle, or (c) the **simplest olfactory cortex**
[reference:1]. The tree treats it as a **distinct leaf** — a sibling of
``olfactory_bulb`` and ``olfactory_tract``, not a subregion of either —
but consumers must not assume the anatomical boundaries are sharp. The
bulb–AON junction is **cytoarchitecturally continuous** in many species,
and the AON is **embedded within** the olfactory tract / peduncle rather
than sitting beside it.

Overview
--------
The anterior olfactory nucleus is the **first central relay** in the
olfactory pathway. It sits at the junction between the **olfactory
bulb** and the **olfactory tract**, receiving axons from the bulb's
**mitral and tufted cells** and projecting both **back to the bulb**
(reciprocal feedback) and **forward to the piriform cortex**
[reference:2]. It is the **only telencephalic structure that projects to
the contralateral olfactory bulb** — the anatomical basis of bilateral
olfactory integration[reference:3].

**The AON is small but structurally distinctive.** In humans it is a
thin sheet of cells embedded in the olfactory peduncle, less prominent
than in macrosmatic mammals but present and identifiable
[reference:4]. It is typically divided into **four subdivisions**:

*   **Pars externa** — the most distinctive subdivision. A thin layer
    of cells **within the lateral olfactory tract** that projects
    **to the contralateral olfactory bulb**. This is the AON's
    signature function: **cross-hemispheric olfactory integration**
    [reference:5].

*   **Pars medialis** — projects ipsilaterally to the bulb and to
    the **medial olfactory stria** targets (septal nuclei, diagonal
    band of Broca)[reference:6].

*   **Pars lateralis** — projects ipsilaterally to the bulb and to
    the **piriform cortex** and **periamygdaloid cortex**.

*   **Pars ventralis** (also called pars dorsalis in some species) —
    projects ipsilaterally to the bulb and to the **olfactory
    tubercle** and **hypothalamus**.

**These four subdivisions are documented as prose, not as structural
children.** The tree does not wire them as sub-modules; consumers that
need subdivision-level resolution should consult the references, not the
tree.

**The AON is not the olfactory bulb and not the piriform cortex.** It
is the **interposed relay** between them — a small but critical node
that (a) receives the bulb's first-order output, (b) modulates the bulb
via feedback, (c) coordinates the two bulbs via the pars externa, and
(d) forwards olfactory information to the primary olfactory cortex and
its limbic targets. Removing it does not abolish olfaction, but it
degrades **odor discrimination and bilateral integration**
[reference:7].

**"Anterior olfactory cortex" is a contested label.** Brunjes, Illig,
and Meyer (2005) argue that the AON's layered structure warrants the
term "cortex," making it arguably the **simplest cortical structure in
the brain**[reference:8]. This is a defensible but **minority**
position; most classical anatomy treats it as a **nucleus**. The tree
avoids the label by placing the AON as a **sibling of
``piriform_cortex``**, not as a cortex child — but consumers should be
aware that the "nucleus vs. cortex" debate is **unresolved** and that
some sources will call this structure the "anterior olfactory cortex."

The Olfactory Peduncle Context
------------------------------
The AON is **embedded in the olfactory peduncle** — the stalk of tissue
connecting the olfactory bulb to the hemisphere. The tree separates the
**peduncle's three components** into three sibling leaves:

*   ``olfactory_bulb`` — the expanded rostral end.
*   ``olfactory_tract`` — the axonal bundle running caudally.
*   ``anterior_olfactory_nucleus`` — the grey-matter embedded within
    the tract/peduncle.

**These three are anatomically intermingled.** The AON's pars externa
is literally *inside* the lateral olfactory tract; the bulb–AON
junction is cytoarchitecturally continuous in many species; and the
"olfactory tract" proper is a mix of bulb efferents, AON efferents, and
AON dendrites. The tree's three-way split is a **useful abstraction**,
not a sharp anatomical boundary. A consumer that treats
``olfactory_bulb``, ``olfactory_tract``, and
``anterior_olfactory_nucleus`` as cleanly separable structures will
**misunderstand the peduncle** — they are better understood as
**regions of a continuous olfactory peduncle**.

Function in the Human Brain
---------------------------
The AON's functions are **modulatory and integrative**, not primary
sensory:

*   **First Central Relay (Primary Function):** The AON receives the
    **first synapse** of the olfactory pathway beyond the bulb —
    mitral and tufted cell axons terminate here before the signal
    reaches the piriform cortex[reference:9]. It is the **first site
    of central olfactory processing**.

*   **Feedback Modulation of the Olfactory Bulb:** The AON projects
    back to the bulb's **granule cells**, driving **reciprocal
    inhibition** that sharpens bulb output and contributes to
    **odor concentration coding** and **habituation**
    [reference:10].

*   **Bilateral Olfactory Integration (Pars Externa):** The pars
    externa is the **only telencephalic projection to the
    contralateral olfactory bulb**. It coordinates the two bulbs,
    supporting **bilateral odor localization** and **binaral-like
    odor comparison** — the olfactory analogue of sound localization
    [reference:11].

*   **Odor Discrimination and Learning:** Animal lesion studies show
    that AON lesions impair **fine odor discrimination** and
    **odor-reward learning** without abolishing basic detection
    [reference:12]. The AON is part of the circuit that **assigns
    significance** to odors.

*   **Relay to Limbic and Cortical Targets:** The AON projects to the
    **piriform cortex**, **periamygdaloid cortex**, **olfactory
    tubercle**, **amygdala**, **entorhinal cortex**, and
    **hypothalamus** — all documented under their own modules
    [reference:13]. The AON is a **distribution hub**, not a
    terminal processing stage.

**The unifying theme:** the AON is the **first central olfactory
relay** and the **bilateral integration node** of the olfactory system.
It is **not** a primary sensory cortex in the classical sense, **not**
a limbic structure in its own right, and **not** a motor area. It is a
**small, modulatory, integrative relay** between the bulb and the rest
of the olfactory brain.

Associated Disorders
--------------------
There is **no named "AON lesion syndrome."** Its clinical relevance is
**inferred** from olfactory-system pathology:

*   **Neurodegenerative Olfactory Dysfunction:** The AON is among the
    **earliest affected structures** in **Parkinson's disease** and
    **Alzheimer's disease**. Braak staging places AON pathology in
    the **earliest (stage 1–2)** phase of Parkinson's, before motor
    symptoms[reference:14]. AON involvement contributes to the
    **prodromal olfactory deficits** of both diseases.

*   **Post-Viral Anosmia (COVID-19 and Others):** Viral injury to the
    olfactory epithelium and bulb can extend to the AON, contributing
    to **persistent olfactory dysfunction** after infection
    [reference:15]. The AON's role in **odor discrimination** (not
    just detection) may explain why some post-viral patients recover
    detection but not discrimination.

*   **Olfactory Learning and Discrimination Deficits (Animal Models):**
    Experimental AON lesions in rodents impair **fine odor
    discrimination** and **social odor recognition** without
    abolishing detection[reference:16]. These are **animal-model
    findings**, not established human syndromes.

*   **No Named Syndrome:** The literature does **not** describe an
    "AON syndrome." The AON is discussed as a **component of the
    olfactory pathway**, not as a standalone clinical node. Consumers
    should treat it as a **contributor** to olfactory dysfunction,
    not as a primary syndrome substrate.

**What is NOT here:** The AON is **not** the substrate for **temporal
lobe epilepsy** (that is hippocampal/amygdalar), **Kluver-Bucy
syndrome** (amygdala), **semantic dementia** (anterior temporal
neocortex), or **Wernicke's aphasia** (BA22). Its clinical footprint is
**olfactory**, and even there it is a **contributor**, not the primary
substrate (which is the bulb and piriform cortex).

Lateralization Notes
--------------------
This is the **right** AON module. The AON is the **most
cross-hemispherically integrated structure in the olfactory system**,
and its lateralization is therefore **structurally special**:

*   **Pars Externa Crosses (the defining feature):** The **right**
    AON's pars externa projects to the **left** olfactory bulb, and
    the **left** AON's pars externa projects to the **right**
    olfactory bulb. **Each side does its own half of the
    cross-hemispheric work** — the two AONs are **structurally
    symmetric** and **functionally complementary**, not redundant.

*   **No Lateralized Syndrome:** The AON has **no documented
    left-lateralized or right-lateralized function**. Unlike BA22
    (left Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left
    semantic / right social), the AON is **bilaterally organized**
    and its function is **integration across the two sides**, not
    specialization within one side.

*   **Cortical-Level Asymmetries Do Not Apply:** The subtle
    left-verbal / right-emotional asymmetries reported for
    **orbitofrontal** and **insular** odor processing are
    **cortical-level** phenomena **downstream** of the AON. Do not
    import them into the AON. The AON itself is **functionally
    symmetric**.

**A consumer that assumes "right AON = left AON" will be structurally
and functionally correct** — the two sides are symmetric, and the
AON's function is **explicitly cross-hemispheric**. This is a stronger
form of left/right equivalence than most structures: the AON's *job*
is to connect the two sides, so structural parity is **functional**,
not just convenient.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The AON's
    projections to the piriform cortex, amygdala, entorhinal cortex,
    olfactory tubercle, and hypothalamus are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The four classical
    subdivisions (pars externa, medialis, lateralis, ventralis) are
    documented as **prose**, not as sub-modules. Consumers must not
    assume they exist as children; resolve subdivision-level detail
    through the references.
*   **Boundary case — continuous with the olfactory bulb and embedded
    in the olfactory tract.** The tree treats the AON as a distinct
    leaf, but the bulb–AON junction is **cytoarchitecturally
    continuous** in many species and the AON is **embedded within**
    the olfactory peduncle, not beside it. Consumers must not assume
    sharp anatomical boundaries among ``olfactory_bulb``,
    ``olfactory_tract``, and ``anterior_olfactory_nucleus``.
*   **"Nucleus" vs. "cortex" is unresolved.** Some sources (notably
    Brunjes et al., 2005) call this structure the **anterior
    olfactory cortex**. The tree avoids the label by placing the AON
    as a **sibling of ``piriform_cortex``**, but consumers should
    expect the alternate name in the literature.
*   **Pars externa crosses — documented, not wired.** The
    cross-hemispheric projection is a **functional** fact, not a
    structural parent. The tree does **not** import from the left
    AON. The projection is documented as prose only.
*   **No ``AREA_PATHS`` hop.** The AON is a local leaf under the
    rhinencephalon, not a cross-listed leaf.
*   **No nested cross-listing.** The AON has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with left AON.** Right and left AON modules
    are **structurally identical** — same leaf status, same four
    subdivisions documented as prose, same continuous-with-bulb
    caveat, same cross-hemispheric pars externa note.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon import anterior_olfactory_nucleus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.rhinencephalon."
        "anterior_olfactory_nucleus"
    )

**Do not** assume the AON is a subregion of ``olfactory_bulb`` or
``olfactory_tract``. It is a **sibling leaf** of both. A consumer
that iterates ``olfactory_bulb`` submodules and expects to find the
AON there will **miss it**.

**Do not** assume the AON has structural children. It is a **leaf**.
The four classical subdivisions (pars externa, medialis, lateralis,
ventralis) are **prose only** — they are not wired as modules.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        aon_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon."
            f"anterior_olfactory_nucleus"
        )
        # resolve aon_path through the memory/recall layer

Reaching the AON's downstream targets (recommended consumer
pattern)::

    # The AON projects to structures documented elsewhere in the tree.
    # Resolve them at their own paths:
    #
    #   cortex.temporal.gyri.entorhinal_cortex
    #   rhinencephalon.piriform_cortex
    #   rhinencephalon.periamygdaloid_cortex
    #   subcortical.basal_forebrain.striatum.ventral_striatum.olfactory_tubercle
    #   subcortical.medial_temporal_lobe.amygdala
    #   diencephalon.hypothalamus
    #
    # These are NOT AON children. They are downstream targets.

Subdivision-level detail (not wired — consult references)::

    # The AON's four classical subdivisions are prose, not modules:
    #   pars externa    -> contralateral bulb (cross-hemispheric)
    #   pars medialis   -> ipsilateral bulb, septal nuclei, diagonal band
    #   pars lateralis  -> ipsilateral bulb, piriform, periamygdaloid
    #   pars ventralis  -> ipsilateral bulb, olfactory tubercle, hypothalamus
    #
    # Do not attempt to resolve these as sub-paths of the AON module.

References
----------
*   **Canonical review:** Brunjes, P.C., Illig, K.R., Meyer, E.A.
    (2005). "A field guide to the anterior olfactory nucleus
    (cortex)." *Brain Research Reviews* 50:305–335. (The definitive
    review; argues for the "anterior olfactory cortex" label;
    documents the four subdivisions and their projections.)
*   **Comparative anatomy:** Crosby, E.C., Humphrey, T. (1941).
    "Studies of the vertebrate telencephalon. II. The nuclear pattern
    of the anterior olfactory nucleus, tuberculum olfactorium and the
    amygdaloid complex in adult man." *Journal of Comparative
    Neurology* 74:309–352. (Classical human AON anatomy.)
*   **Olfactory pathway:** Doty, R.L. (2015). *Handbook of Olfaction
    and Gustation*, 3rd ed. (AON as first central relay; human
    olfactory anatomy.)
*   **Cross-hemispheric projection:** Schoenfeld, T.A., Macrides, F.
    (1984). "Topographic organization of connections between the main
    olfactory bulb and pars externa of the anterior olfactory nucleus
    in the hamster." *Journal of Comparative Neurology* 227:121–135.
    (Pars externa's contralateral bulb projection.)
*   **Feedback modulation:** Shipley, M.T., Ennis, M. (1996).
    "Functional organization of olfactory system." *Journal of
    Neurobiology* 30:123–176. (AON feedback to bulb granule cells.)
*   **Lesion studies:** Ferry, B., et al. (1995). "Olfactory
    discrimination learning in rats with lesions of the anterior
    olfactory nucleus." *Behavioral Neuroscience* 109:1093–1101.
    (AON lesions impair fine discrimination.)
*   **Braak staging:** Braak, H., et al. (2003). "Staging of brain
    pathology related to sporadic Parkinson's disease."
    *Neurobiology of Aging* 24:197–211. (AON involvement in early
    Parkinson's.)
*   **COVID-19 olfactory pathway:** Netland, J., et al. (2008).
    "Severe acute respiratory syndrome coronavirus infection causes
    neuronal death in the absence of encephalitis in mice transgenic
    for human ACE2." *Journal of Virology* 82:7264–7275. (Olfactory
    pathway involvement, including AON.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (AON in the olfactory pathway.)
*   NeuroNames — Anterior olfactory nucleus (right); FMA — Anterior
    olfactory nucleus (right member).
"""