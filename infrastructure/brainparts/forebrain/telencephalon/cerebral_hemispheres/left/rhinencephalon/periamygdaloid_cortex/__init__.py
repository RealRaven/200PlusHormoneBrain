"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.rhinencephalon.periamygdaloid_cortex
==============================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── rhinencephalon
                └── periamygdaloid_cortex   <-- THIS MODULE

**Primary synonym:** Periamygdaloid cortex; periamygdaloid area;
cortex periamygdaloidea; "periamygdalar cortex."
**Cytoarchitectonic designation:** **Not a single Brodmann area.**
Classically overlaps **BA34** (dorsal entorhinal/periamygdaloid) and
**BA28** (ventral entorhinal) in some maps, but the tree wires
**BA34 separately** under ``cortex/temporal/brodmann_areas/brodmann_area_34/``.
This module is the **cortical surface region** overlying the amygdala,
**not** the Brodmann-area abstraction — see *Boundary status*.
**Part of:** The **primary olfactory cortex** — a direct target of the
**lateral olfactory stria (LOS)**.
**Structural parent:** ``.../left/rhinencephalon/`` → **direct child** of
the rhinencephalon container.
**Structural children:** **None.** This is a **leaf** module. The
classical subdivisions (pars lateralis, pars medialis, etc.) are
documented as **prose**, not as structural children.
**Boundary status (olfactory–limbic):** **Boundary case — a cortical
structure overlying the amygdala, not part of the amygdala proper.** The
periamygdaloid cortex is the **cortical mantle** of the uncus and
medial temporal surface that lies **over** the amygdala's nuclear
complex. It is **cortex** (receives LOS input, has cortical lamination),
not **amygdala** (which is a nuclear complex). The tree routes the
amygdala through
``subcortical/medial_temporal_lobe/amygdala/`` — its **own module** —
and routes the **cortical surface over it** through this module.
Consumers must **not** resolve periamygdaloid cortex as an amygdala
child, and must **not** resolve the amygdala's olfactory component
through this module.
**Boundary status (piriform vs. periamygdaloid):** **Boundary case —
sibling of piriform cortex, not a subregion.** Classical anatomy often
treats the periamygdaloid cortex as **part of the piriform cortex** (the
"periamygdaloid part of the piriform lobe"). The tree splits them into
**two sibling leaves**. This is **non-standard but deliberate** — the
tree preserves a finer granularity so that the olfactory–limbic
boundary can be documented **at the periamygdaloid cortex** rather than
folded into a larger piriform module.
**Boundary status (BA34):** **Boundary case — not Brodmann area 34.**
Brodmann's area 34 is sometimes called the "periamygdaloid area," and
the tree **does wire BA34 separately** under
``cortex/temporal/brodmann_areas/brodmann_area_34/``. **This module is
not BA34.** It is the **cortical surface region** over the amygdala,
which overlaps BA34 in some maps but is not identical to it. Consumers
that need Brodmann-area resolution should resolve
``brodmann_area_34``; consumers that need the cortical surface over
the amygdala should resolve this module. The two are **not
interchangeable**.

Overview
--------
The periamygdaloid cortex is the **cortical mantle overlying the
amygdala** on the medial temporal surface — the region of the **uncus**
and **anterior parahippocampal gyrus** that sits **between the piriform
cortex rostrally and the entorhinal cortex caudally**, and **over** the
amygdala's nuclear complex. It is a **primary olfactory cortical
area**: it receives direct input from the **lateral olfactory stria**
and is a **first-order cortical target** of the olfactory bulb.

**The periamygdaloid cortex is small, but it is the structural
interface between the olfactory and limbic systems.** Its **superficial
layers** are olfactory cortex (receiving LOS input); its **deep layers**
are continuous with the **amygdala's corticomedial nuclei** and project
into the amygdala. This is why the periamygdaloid cortex is the
anatomical substrate of the **olfactory–limbic interface** — the point
at which olfactory information first reaches the limbic system.

**The tree splits it from the piriform cortex deliberately.** In
classical anatomy, the periamygdaloid cortex is often treated as the
**"periamygdaloid part of the piriform cortex"** — a subregion of a
larger piriform lobe. The tree instead wires ``piriform_cortex`` and
``periamygdaloid_cortex`` as **two sibling leaves** under the
rhinencephalon. This finer granularity lets the **olfactory–limbic
boundary** be documented **at the periamygdaloid cortex** rather than
folded into a piriform module — but consumers should be aware that
**many sources will call this structure part of the piriform cortex**,
and the two modules should be read together when the piriform lobe is
the unit of interest.

**The periamygdaloid cortex is not the amygdala.** This is the single
most important boundary caveat. The amygdala is a **nuclear complex**
(basolateral, corticomedial, central nuclei) with its **own module**
under ``subcortical/medial_temporal_lobe/amygdala/``. The
periamygdaloid cortex is the **cortical surface** that lies over it —
it is **cortex** (laminated, olfactory-recipient), not **nucleus**
(non-laminated, primarily limbic). The two are **anatomically
adjacent** and **functionally coupled** (the periamygdaloid cortex
projects into the amygdala), but they are **not the same structure** and
must not be conflated. A consumer that resolves the periamygdaloid
cortex and expects an amygdala structure will be **misled**; a consumer
that resolves the amygdala and expects the periamygdaloid cortex will be
**equally misled**.

**The periamygdaloid cortex is not BA34.** Brodmann's area 34 is
sometimes called the "periamygdaloid area," but the tree treats them as
**distinct**: BA34 is wired under ``cortex/temporal/brodmann_areas/``,
and the periamygdaloid cortex is wired here as a **rhinencephalon
leaf**. The two overlap in some atlases but are **not interchangeable**.
Consumers that need **Brodmann-area resolution** should resolve
``brodmann_area_34``; consumers that need the **cortical surface over
the amygdala** should resolve this module.

Subdivisions (prose, not structural children)
---------------------------------------------
The periamygdaloid cortex is classically divided into **subdivisions**
whose boundaries are **cytoarchitecturally subtle and inconsistently
named**. The most commonly described are:

*   **Pars lateralis** — the **lateral part**, adjacent to the
    piriform cortex rostrally and the entorhinal cortex caudally.
    Receives the **lateral olfactory stria** and projects to the
    **lateral amygdaloid nucleus**.

*   **Pars medialis** — the **medial part**, adjacent to the uncus
    surface and the **semilunar gyrus**. Receives LOS input and
    projects to the **medial amygdaloid nucleus** and the **bed
    nucleus of the stria terminalis**.

*   **Pars posterior** (some authors) — the **caudal part**, blending
    into the **entorhinal cortex**. Its boundary with the entorhinal
    cortex is **cytoarchitecturally gradual**, not sharp.

**These subdivisions are prose, not structural children.** The tree
does **not** wire them as sub-modules. Consumers that need
subdivision-level resolution should consult the references, not the
tree. The boundaries between subdivisions — and between the
periamygdaloid cortex and its neighbors (piriform rostrally,
entorhinal caudally, amygdala deeply) — are **graded**, not sharp.

Function in the Human Brain
---------------------------
The periamygdaloid cortex's functions are **olfactory–limbic
integration**:

*   **Primary Olfactory Reception (Primary Function):** The
    periamygdaloid cortex is a **direct cortical target** of the
    **lateral olfactory stria** — it receives first-order olfactory
    input from the bulb and AON. It is part of the **primary
    olfactory cortex** proper (alongside the piriform and entorhinal
    cortices).

*   **Olfactory–Limbic Relay (Defining Function):** The periamygdaloid
    cortex **projects into the amygdala** — to the **lateral**,
    **medial**, and **central** amygdaloid nuclei and to the **bed
    nucleus of the stria terminalis**. This projection is the
    **anatomical substrate** of the **olfactory–limbic interface**:
    the first point at which olfactory information reaches the
    limbic system and can be associated with **emotion, memory, and
    autonomic responses**.

*   **Odor–Emotion Association:** The periamygdaloid cortex
    contributes to the **emotional tagging of odors** — the
    association of smells with **fear, reward, disgust, and social
    signals** — via its amygdaloid projections. This function is
    **downstream** of the periamygdaloid cortex (the amygdala
    implements it), but the periamygdaloid cortex is the **cortical
    input stage**.

*   **Olfactory Auras in Epilepsy:** The periamygdaloid cortex is a
    **substrate for uncinate fits** — temporal lobe seizures with
    **olfactory and gustatory auras**. Seizures arising in the
    periamygdaloid cortex or the adjacent uncus produce the classic
    **"uncinate fit"** presentation.

*   **NOT the amygdala's emotional functions.** **Fear conditioning**,
    **Kluver-Bucy syndrome**, and **social-emotional processing** are
    properties of the **amygdala proper** (basolateral, central
    nuclei), documented under ``subcortical/medial_temporal_lobe/amygdala/``.
    The periamygdaloid cortex **feeds** the amygdala; it does not
    **implement** the amygdala's functions.

**The unifying theme:** the periamygdaloid cortex is the **cortical
olfactory–limbic interface** — a primary olfactory cortical area whose
defining role is to **relay olfactory information into the amygdala**.
It is **not** a limbic processor in its own right, **not** the
amygdala, and **not** a primary olfactory **identification** area
(that is the piriform cortex proper). It is the **cortical input stage**
of the olfactory–limbic system.

Associated Disorders
--------------------
Periamygdaloid cortex disorders are **olfactory and epileptic**, not
limbic-emotional:

*   **Uncinate Fits (Temporal Lobe Epilepsy):** The periamygdaloid
    cortex and the adjacent uncus are **classic epileptogenic
    substrates**. **Olfactory and gustatory auras** ("uncinate fits")
    arise from discharges in this region. The seizure itself
    propagates into the **amygdala** and **hippocampus** (documented
    under ``subcortical/``), but the **aura** is periamygdaloid/
    uncinate.

*   **Olfactory Dysfunction:** As a primary olfactory cortical area,
    the periamygdaloid cortex can be **affected** in **anosmia**,
    **hyposmia**, and **olfactory agnosia**. Its contribution is
    **secondary** to the piriform cortex and bulb — it is a
    **contributor**, not the primary substrate.

*   **Neurodegenerative Olfactory Pathology:** The periamygdaloid
    cortex can be **involved** in **Parkinson's disease** and
    **Alzheimer's disease** alongside the bulb, AON, and piriform
    cortex — contributing to **prodromal olfactory deficits**. Its
    pathology is **less well characterized** than the bulb's.

**What is NOT here:** The periamygdaloid cortex is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala proper),
**fear conditioning** (amygdala proper), **Urbach-Wiethe disease**
(amygdala proper), or **semantic dementia** (anterior temporal
neocortex). It is **not** the substrate for **temporal lobe epilepsy
proper** (hippocampus) — it contributes the **aura**, not the
**seizure**. Its clinical footprint is **olfactory and epileptic**, and
even there it is a **contributor**, not the primary substrate.

Lateralization Notes
--------------------
This is the **left** periamygdaloid cortex module. The periamygdaloid
cortex is **bilaterally symmetric** and **functionally
non-lateralized**:

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the periamygdaloid cortex has **no documented left-lateralized or
    right-lateralized function**.

*   **Ipsilateral Olfactory Projection:** Each periamygdaloid cortex
    receives **ipsilateral** LOS input from its own bulb. The two
    sides are **functionally symmetric** for olfactory reception.

*   **No Amygdala Lateralization Import:** The **right amygdala** is
    sometimes reported to be **more involved in emotional processing**
    (especially fear) than the left — but this is **amygdala proper**,
    not the periamygdaloid cortex. **Do not import amygdala
    lateralization claims into the periamygdaloid cortex.** The
    periamygdaloid cortex's lateralization is **not established**.

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the periamygdaloid cortex. Do not import them
    into the periamygdaloid cortex.

**A consumer that assumes "left periamygdaloid = right periamygdaloid"
will be structurally and functionally correct** — the two sides are
symmetric, and no lateralized function has been demonstrated. The
periamygdaloid cortex is **not** the amygdala, so **amygdala
lateralization does not apply**; and it is **not** orbitofrontal/
insular cortex, so **cortical-level asymmetries do not apply** either.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The
    periamygdaloid cortex's projections to the amygdala, entorhinal
    cortex, and bed nucleus of the stria terminalis are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The classical
    subdivisions (pars lateralis, pars medialis, pars posterior) are
    documented as **prose**, not as sub-modules. Consumers must not
    assume they exist as children; resolve subdivision-level detail
    through the references.
*   **Boundary case — cortical structure overlying the amygdala, not
    part of the amygdala proper.** The periamygdaloid cortex is
    **cortex** (laminated, LOS-recipient); the amygdala is a **nuclear
    complex**. They are **anatomically adjacent** and **functionally
    coupled**, but **not the same structure**. The tree routes the
    amygdala through
    ``subcortical/medial_temporal_lobe/amygdala/`` — its **own
    module**. Consumers must not resolve periamygdaloid cortex as an
    amygdala child, and must not resolve the amygdala's olfactory
    component through this module.
*   **Boundary case — sibling of ``piriform_cortex``, not a
    subregion.** Classical anatomy often treats the periamygdaloid
    cortex as part of the piriform cortex. The tree splits them into
    two sibling leaves. This is **non-standard but deliberate** —
    consumers that need the piriform lobe as a unit must **union**
    ``piriform_cortex`` and ``periamygdaloid_cortex``.
*   **Boundary case — not Brodmann area 34.** BA34 is wired
    separately under
    ``cortex/temporal/brodmann_areas/brodmann_area_34/``. This module
    is the **cortical surface over the amygdala**, not the
    Brodmann-area abstraction. The two overlap in some atlases but are
    **not interchangeable**.
*   **No ``AREA_PATHS`` hop.** The periamygdaloid cortex is a local
    leaf under the rhinencephalon, not a cross-listed leaf.
*   **No nested cross-listing.** The periamygdaloid cortex has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with right periamygdaloid cortex.** Left and
    right periamygdaloid cortex modules are **structurally identical**
    — same leaf status, same subdivisions documented as prose, same
    amygdala-boundary caveat, same BA34 distinction, same
    non-lateralized caveat.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.rhinencephalon import periamygdaloid_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.rhinencephalon."
        "periamygdaloid_cortex"
    )

**Do not** assume the periamygdaloid cortex is part of the **amygdala**.
It is a **cortex** leaf under the rhinencephalon; the amygdala is a
**nuclear complex** under
``subcortical/medial_temporal_lobe/amygdala/``. A consumer that
iterates the amygdala and expects to find the periamygdaloid cortex
there will **miss it**; a consumer that iterates the rhinencephalon
and expects to find the amygdala there will **equally miss it**.

**Do not** assume the periamygdaloid cortex is a **subregion of
``piriform_cortex``**. It is a **sibling leaf**. Classical anatomy
often groups them; the tree does not. If the piriform lobe is the
unit of interest, **union** the two leaves.

**Do not** assume the periamygdaloid cortex is **Brodmann area 34**.
BA34 is wired separately. The two overlap in some atlases but are
**not interchangeable**.

**Do not** assume the periamygdaloid cortex has structural children.
It is a **leaf**. The classical subdivisions (pars lateralis, pars
medialis, pars posterior) are **prose only** — they are not wired as
modules.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pac_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon."
            f"periamygdaloid_cortex"
        )
        # resolve pac_path through the memory/recall layer

Reaching the periamygdaloid cortex's downstream targets (recommended
consumer pattern)::

    # The periamygdaloid cortex projects to structures documented
    # elsewhere in the tree. Resolve them at their own paths:
    #
    #   subcortical.medial_temporal_lobe.amygdala.lateral_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.medial_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.basal_forebrain.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   cortex.temporal.gyri.entorhinal_cortex
    #
    # These are NOT periamygdaloid cortex children. They are
    # downstream targets.

Reaching the amygdala's own olfactory component (recommended
consumer pattern)::

    # The amygdala's main olfactory system is a child of the amygdala
    # module, NOT of the periamygdaloid cortex:
    #
    #   subcortical.medial_temporal_lobe.amygdala.main_olfactory_system
    #
    # The periamygdaloid cortex is the CORTICAL surface over the
    # amygdala; the amygdala's main_olfactory_system is the NUCLEAR
    # olfactory component. They are distinct.

Piriform-lobe-level iteration (recommended consumer pattern)::

    # If the piriform lobe is the unit of interest, union the two
    # sibling leaves:
    PIRIFORM_LOBE_LEAVES = (
        "piriform_cortex",
        "periamygdaloid_cortex",
    )
    # Classical anatomy often treats periamygdaloid as part of
    # piriform; the tree splits them for finer granularity.

References
----------
*   **Canonical anatomy:** Amaral, D.G., Insausti, R. (1990). "The
    hippocampal formation." In *The Human Nervous System*
    (Paxinos, G., ed.). (Periamygdaloid cortex as part of the
    piriform lobe; relationship to the amygdala.)
*   **Olfactory cortex:** Price, J.L. (1990). "Olfactory system." In
    *The Human Nervous System* (Paxinos, G., ed.). (Periamygdaloid
    cortex as a primary olfactory cortical area; LOS input;
    amygdaloid projections.)
*   **Amygdala anatomy:** Amaral, D.G., Price, J.L., Pitkänen, A.,
    Carmichael, S.T. (1992). "Anatomical organization of the primate
    amygdaloid complex." In *The Amygdala* (Aggleton, J.P., ed.).
    (Corticomedial nuclei; periamygdaloid cortex as cortical input
    stage.)
*   **Olfactory–limbic interface:** Carmichael, S.T., Clugnet, M.C.,
    Price, J.L. (1994). "Central olfactory connections in the
    macaque monkey." *Journal of Comparative Neurology* 346:403–434.
    (Periamygdaloid cortex projections to amygdala.)
*   **Uncinate fits:** Gloor, P. (1997). *The Temporal Lobe and
    Limbic System*. (Olfactory auras and uncinate seizures;
    periamygdaloid/uncinate substrate.)
*   **Brodmann area 34:** Brodmann, K. (1909). *Vergleichende
    Lokalisationslehre der Grosshirnrinde*. (BA34 as dorsal
    entorhinal/periamygdaloid; note the tree wires BA34 separately.)
*   **Human olfactory cortex:** Doty, R.L. (2015). *Handbook of
    Olfaction and Gustation*, 3rd ed. (Primary olfactory cortical
    areas including periamygdaloid.)
*   **Parkinson's disease:** Braak, H., et al. (2003). "Staging of
    brain pathology related to sporadic Parkinson's disease."
    *Neurobiology of Aging* 24:197–211. (Olfactory cortical
    involvement, including periamygdaloid region.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Periamygdaloid cortex in the olfactory
    pathway.)
*   NeuroNames — Periamygdaloid cortex (left); FMA — Periamygdaloid
    cortex (left member).
"""