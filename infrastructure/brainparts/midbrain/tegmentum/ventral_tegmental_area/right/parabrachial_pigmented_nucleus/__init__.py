"""
infrastructure.brainparts.midbrain.tegmentum.ventral_tegmental_area.right.parabrachial_pigmented_nucleus
========================================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        └── ventral_tegmental_area
            └── right
                └── parabrachial_pigmented_nucleus   <-- THIS MODULE

**Primary synonym:** Parabrachial pigmented nucleus; PBP; right PBP;
right parabrachial pigmented nucleus of the VTA; the **dorsolateral**
A10 dopaminergic subnucleus; "the pigmented shoulder of the VTA."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**dopaminergic VTA subnucleus** — the **A10 cell group's largest
and most dorsolateral** component. **Neuromelanin-containing** in
humans (the **pigment** that gives the PBP its name — "parabrachial
pigmented"). The **PBP / SNc boundary is cytoarchitecturally
fuzzy** — the two nuclei are **adjacent** and **share
neuromelanin-containing dopaminergic neurons**, which is why the
PBP is the **most conflatable** VTA subnucleus with the
**substantia nigra pars compacta** (Halliday & Törk, 1989; Fu et
al., 2016).
**Part of:** The **ventral_tegmental_area** container —
specifically, the **right** VTA, and one of the **right VTA
subnuclei** (**with PN, IF, RLi, and CLi as its subnuclear
siblings**). The VTA sits in the **midbrain tegmentum**, **medial**
to the **substantia nigra** and **ventral** to the **red
nucleus**.
**Structural parent:** ``.../ventral_tegmental_area/right/`` →
**direct child** of the right VTA.
**Structural children:** **None.** This is a **leaf** module. The
**dorsal vs. ventral** tier, the **medial vs. lateral** projection
topography, the **neuromelanin-containing vs. non-containing**
subpopulations, and the **dopamine-glutamate co-transmission**
subpopulation are documented as **prose**, not as structural
children.
**Boundary status (NOT the VTA container — the PBP is a
COMPONENT):** **Boundary case — the PBP is a SUBNUCLEUS of the
VTA, not the VTA itself.** The **ventral_tegmental_area**
container holds the **left** and **right** VTA, each of which
holds the **PBP**, **PN**, **IF**, **RLi**, and **CLi**
subnuclei. Consumers must **not** treat "VTA" and "PBP" as
synonyms — the PBP is **one** of the VTA subnuclei, not the whole
complex.
**Boundary status (NOT the other VTA subnuclei — PN, IF, RLi,
CLi are SIBLINGS):** **Boundary case — the PBP is NOT the
paranigral nucleus (PN), the interfascicular nucleus (IF), the
rostral linear nucleus (RLi), or the caudal linear nucleus
(CLi).** Those are the **other VTA subnuclei** —
**medial / ventral** to the PBP, with **different projection
topographies** (PN / IF → predominantly **nucleus accumbens**;
RLi / CLi → predominantly **medial prefrontal cortex** and
**extended amygdala**). The **PBP** (here) is the **dorsolateral**
subnucleus — predominantly **prefrontal cortex** and **amygdala**
(mesocortical / mesoamygdalar). Consumers must **not** conflate
the PBP with its subnuclear siblings — each is a **distinct
subnucleus** with a **distinct projection target**.
**Boundary status (NOT the substantia nigra pars compacta — the
most consequential boundary):** **Boundary case — the PBP is NOT
the substantia nigra pars compacta (SNc).** The **SNc**
(``.../tegmentum/substantia_nigra/right/pars_compacta/``) is the
**A9 dopaminergic** cell group — it projects to the **dorsal
striatum** (nigrostriatal) and is the **canonical Parkinson's
disease** substrate. The **PBP** (here) is the **A10 dopaminergic**
subnucleus — it projects to the **prefrontal cortex** and
**amygdala** (mesocortical / mesoamygdalar) and is **not** the
canonical PD substrate. **The PBP abuts the SNc and shares
neuromelanin-containing neurons with it** — the **cytoarchitectural
boundary is fuzzy** — but they are **DIFFERENT NUCLEI** with
**different projection targets** (SNc → dorsal striatum; PBP →
prefrontal cortex / amygdala) and **different clinical
associations** (SNc → Parkinson's disease; PBP → addiction /
schizophrenia / affective disorders). Consumers must **not**
conflate the two — **"A10 PBP" is not "A9 SNc"**, and the
**shared neuromelanin** does **not** make them the same structure.
**Boundary status (NOT the substantia nigra pars reticulata — the
SNr is the GABAergic output):** **Boundary case — the PBP is NOT
the substantia nigra pars reticulata.** The **SNr**
(``.../tegmentum/substantia_nigra/right/pars_reticulata/``) is the
**GABAergic** basal ganglia output nucleus — functionally parallel
to the GPi, projecting to the **thalamus** and **superior
colliculus**. The **PBP** is **dopaminergic** and projects to the
**prefrontal cortex** and **amygdala**. **They are DIFFERENT
NUCLEI** with **different neurotransmitters** and **different
projection targets**. Consumers must **not** conflate the two.
**Boundary status (NOT the retrorubral area / A8 — the A8 group is
a separate dopaminergic cell group):** **Boundary case — the PBP
is NOT the retrorubral area (A8).** The **retrorubral area** is
the **A8 dopaminergic cell group** — it is **caudal and
dorsolateral** to the VTA (and the SNc), and it is **sometimes
grouped with the SN/VTA dopaminergic complex** in the literature.
In this tree it is a **separate structure** (wired elsewhere).
Consumers must **not** silently fold A8 into the PBP — it is a
**distinct dopaminergic cell group**.
**Boundary status (NOT the prefrontal cortex, amygdala, nucleus
accumbens, or hippocampus — those are the PBP's TARGETS):**
**Boundary case — the PBP is NOT any of its projection targets.**
The **prefrontal cortex**
(``.../cortex/frontal/cortex/prefrontal_cortex/``), the **amygdala**
(``.../medial_temporal_lobe/amygdala/``), the **nucleus accumbens**
(``.../basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/``),
and the **hippocampus** (``.../medial_temporal_lobe/hippocampus/``)
are **targets** of the **PBP's dopaminergic projections**. The PBP
**sends** dopamine; those structures **receive** it. Consumers
must **not** conflate the **source** (PBP) with any **target**.
**Boundary status (NOT the interpeduncular nucleus, dorsal raphe,
or periaqueductal gray — those are ADJACENT midline nuclei):**
**Boundary case — the PBP is NOT the interpeduncular nucleus
(IPN), the dorsal raphe (DR), or the periaqueductal gray (PAG).**
Those are **distinct midbrain nuclei** — the **IPN** (habenular
relay, ventral to the VTA), the **DR** (serotonergic, dorsal to
the VTA), and the **PAG** (defense / pain, dorsal midbrain).
The PBP is the **dorsolateral A10 dopaminergic** subnucleus.
Consumers must **not** conflate the PBP with any of them.
**Boundary status (NOT the red nucleus or the crus cerebri — the
red nucleus is the adjacent rubrospinal motor relay; the crus
cerebri is the ventral white-matter tract):** **Boundary case —
the PBP is NOT the red nucleus and NOT the crus cerebri.** The
**red nucleus** (``.../tegmentum/red_nucleus/``) is the
**rubrospinal / rubro-olivary** motor relay — **dorsal and
lateral** to the VTA. The **crus cerebri**
(``.../midbrain/crus_cerebri/`` if wired) is the **white-matter
tract** — **ventral** to the midbrain tegmentum. The PBP is
**grey-matter nucleus** within the tegmentum. Consumers must
**not** conflate the PBP with either.
**Boundary status (NOT a single uniform dopaminergic population —
MULTIPLE intra-PBP subpopulations):** **Boundary case — the PBP
is HETEROGENEOUS, not a single uniform dopaminergic population.**
The PBP includes:
*   **Neuromelanin-containing** dopaminergic neurons — the
    **pigmented** component (shared with the SNc).
*   **Neuromelanin-poor / non-containing** dopaminergic neurons
    — the **non-pigmented** component.
*   **Dorsal vs. ventral** tiers — different projection
    topographies (dorsal → prefrontal cortex; ventral → amygdala
    / ventral striatum).
*   **Dopamine-glutamate co-transmitting** neurons — a
    **contested** subpopulation (some VTA dopaminergic neurons
    co-release glutamate; the PBP is one of the sites where this
    is documented).
*   **Non-dopaminergic (GABAergic, glutamatergic)** neurons —
    intermingled with the dopaminergic population.
**Each subpopulation is functionally distinct** — the tree wires
them as **prose** under the PBP leaf, not as structural children.
Consumers must **not** treat the PBP as a single uniform
dopaminergic population.
**Boundary status (NOT a SLEA component — the PBP is outside the
extended amygdala):** **Boundary case — the PBP is SLEA-FREE.**
The **SLEA continuum** includes the **central nucleus**
(amygdala), the **BNST**, the **ventral pallidum**, and the
**nucleus accumbens**. The PBP **projects to** the **nucleus
accumbens** (a SLEA component), but the **PBP itself** is **not**
part of the SLEA continuum, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the PBP.

Overview
--------
The right parabrachial pigmented nucleus is the **largest and most
dorsolateral** subnucleus of the **right ventral tegmental area** —
the **A10 dopaminergic** component that projects predominantly to
the **prefrontal cortex** (mesocortical) and the **amygdala**
(mesoamygdalar). It is a **leaf** module under the right VTA, and
it is the **dorsolateral A10 dopaminergic substrate** of
**cognitive-affective** dopamine modulation.

**The PBP is NOT the substantia nigra pars compacta.** The **SNc**
is the **A9** dopaminergic cell group — **nigrostriatal** (dorsal
striatum), **Parkinson's disease** substrate. The **PBP** is the
**A10** dopaminergic subnucleus — **mesocortical / mesoamygdalar**
(prefrontal cortex, amygdala), **addiction / schizophrenia /
affective** substrate. **The two abut, share neuromelanin, and
have a fuzzy cytoarchitectural boundary — but they are DIFFERENT
NUCLEI with DIFFERENT projection targets and DIFFERENT clinical
associations.** This is the **most consequential boundary** for
the PBP — consumers must **not** conflate the two.

**The PBP is a SUBNUCLEUS of the VTA, not the VTA itself.** The
VTA container holds the **PBP**, **PN**, **IF**, **RLi**, and
**CLi** subnuclei (per side) — the PBP is **one** of them, the
**dorsolateral** one, with a **predominantly cortical / amygdalar
projection**. Consumers must **not** treat "VTA" and "PBP" as
synonyms.

**The PBP is a paired structure.** Each hemisphere has its own
PBP, with **ipsilateral** projections. The two sides are
**structurally identical** and **bilaterally symmetric** — the
lateralization is **subtle and functional-imaging-level** (see
*Lateralization Notes*).

**The PBP is a HETEROGENEOUS dopaminergic subnucleus, not a single
uniform population.** The **neuromelanin-containing** vs.
**non-containing** dopaminergic populations, the **dorsal vs.
ventral** tiers, the **dopamine-glutamate co-transmitting**
subpopulation, and the **intermingled GABAergic / glutamatergic**
neurons are **functionally distinct** — wired as **prose**, not
structural children.

**The PBP is SLEA-FREE.** It **projects to** the **nucleus
accumbens** (a SLEA component), but the **PBP itself** is **not**
part of the SLEA continuum, and it carries **no SLEA warning**.

Intra-PBP Composition (prose, not structural children)
------------------------------------------------------
The PBP is a **heterogeneous dopaminergic subnucleus** —
documented as **prose**, not as structural children:

*   **Neuromelanin-containing dopaminergic neurons** — the
    **pigmented** component (the **"pigmented"** in "parabrachial
    pigmented"). Shared with the **SNc** — the cytoarchitectural
    **basis** of the fuzzy PBP / SNc boundary.

*   **Neuromelanin-poor / non-containing dopaminergic neurons** —
    the **non-pigmented** component. More **ventral / medial**
    within the PBP.

*   **Dorsal tier** — projects predominantly to the
    **prefrontal cortex** (mesocortical).

*   **Ventral tier** — projects predominantly to the **amygdala**
    and the **ventral striatum** (mesoamygdalar / mesolimbic).

*   **Dopamine-glutamate co-transmitting neurons** — a
    **contested** subpopulation; some VTA dopaminergic neurons
    **co-release glutamate** (the PBP is one documented site;
    the functional significance is **debated**).

*   **Non-dopaminergic (GABAergic, glutamatergic) neurons** —
    **intermingled** with the dopaminergic population; the VTA
    is **not** exclusively dopaminergic.

**These subpopulations are prose, not structural children.** The
tree wires the **PBP** as a **single leaf** under the right VTA —
the **neuromelanin** subpopulations, the **dorsal / ventral**
tiers, the **co-transmitting** neurons, and the **GABAergic /
glutamatergic** interneurons are **prose**, not structural
children. Consumers that need **subpopulation-level** resolution
should consult the references (Sesack & Grace, 2010; Lammel et
al., 2014; Fu et al., 2016), not the tree.

Function in the Human Brain
---------------------------
The PBP's functions are **dopaminergic modulation of cortical and
amygdalar targets** — **NOT nigrostriatal motor**, **NOT basal
ganglia output**:

*   **Mesocortical Dopamine (PBP → Prefrontal Cortex):** The PBP
    **projects** to the **prefrontal cortex** — especially the
    **medial prefrontal cortex** and the **anterior cingulate**.
    **Modulates** **working memory**, **cognitive control**,
    **motivation**, and **affective regulation**. **Hypoactivity**
    of this projection is associated with **negative symptoms**
    and **cognitive deficits** in **schizophrenia**.

*   **Mesoamygdalar Dopamine (PBP → Amygdala):** The PBP
    **projects** to the **amygdala** and **modulates** **emotional
    salience**, **fear learning**, and **threat detection** —
    **affective** dopamine modulation.

*   **Mesolimbic Contribution (PBP → Ventral Striatum):** The PBP
    **contributes** to the **mesolimbic** projection to the
    **nucleus accumbens** (ventral striatum) — though the
    **PN / IF** are the **dominant** mesolimbic subnuclei. The
    PBP's mesolimbic contribution is **secondary** relative to its
    mesocortical / mesoamygdalar projections.

*   **Reward Prediction Error (VTA-wide — the PBP contributes):**
    The **Schultz** framing attributes the **reward prediction
    error** signal primarily to **dopamine neurons** — the PBP is
    **one** of the contributing VTA subnuclei. Consumers must
    **not** attribute the **whole** reward prediction error to
    the PBP — it is a **subnucleus** of a **larger dopaminergic
    complex**.

*   **NOT a basal ganglia output, NOT a nigrostriatal motor
    nucleus.** The PBP is **dopaminergic modulation** of
    **cortical and amygdalar** targets — **NOT** the **basal
    ganglia output** (that is the **SNr / GPi**) and **NOT** the
    **nigrostriatal motor** system (that is the **SNc**). This is
    the **central boundary** between the PBP and the SNc.

**The unifying theme:** the PBP is the **dorsolateral A10
dopaminergic subnucleus** — the **mesocortical / mesoamygdalar**
substrate of **cognitive-affective** dopamine modulation. It is
**SLEA-free**, **dopaminergic**, and **NOT the A9 SNc** — the
**shared neuromelanin** does **not** make them the same structure.

Associated Disorders
--------------------
The PBP has **no named clinical syndrome of its own** — its
clinical associations are **indirect**, via the **VTA-wide
dopaminergic circuits** it contributes to:

*   **Addiction (Mesolimbic / Mesocortical Dopamine — VTA-wide):**
    **Drugs of abuse** increase **mesolimbic / mesocortical
    dopamine** — the **VTA-wide** reinforcement pathway. The
    **PBP** **contributes** to this via its **prefrontal** and
    **amygdalar** projections — but the **canonical** mesolimbic
    substrate is the **PN / IF → nucleus accumbens** projection.
    Consumers must **not** attribute the **whole** addiction
    substrate to the PBP — the **VTA-wide** circuit is the
    substrate; the **PBP** is a **contributing subnucleus**.

*   **Schizophrenia (Mesocortical Dopamine — VTA-wide):** The
    **dopamine hypothesis** of schizophrenia centers on
    **mesolimbic hyperactivity** (positive symptoms) and
    **mesocortical hypoactivity** (negative / cognitive
    symptoms). The **PBP** is a **principal mesocortical**
    contributor — its **prefrontal** projection is the
    **canonical** hypoactive substrate for **negative symptoms**.
    Consumers must **not** attribute the **whole** schizophrenia
    dopamine story to the PBP — the **mesolimbic** side is
    **PN / IF**, and the **EPS** side is **SNc**.

*   **Depression (Mesocortical / Mesoamygdalar Dopamine —
    indirect):** **Reduced mesocortical / mesoamygdalar
    dopamine** is associated with **anhedonia**, **reduced
    motivation**, and **impaired affective regulation** in
    **major depressive disorder**. The **PBP** contributes to
    this — documented, but **mechanistically contested** (the
    dopamine contribution is **one** of several; **serotonin**
    and **norepinephrine** are also involved).

*   **Anxiety Disorders (Mesoamygdalar Dopamine — indirect):**
    The **PBP → amygdala** projection modulates **threat
    detection** and **emotional salience** — a **contested**
    contribution to **anxiety** pathophysiology. Documented, but
    **indirect**.

*   **Parkinson's Disease (PBP Relatively Spared — a CONTESTED
    Gradient):** The **SNc** is the **selective** PD
    degeneration substrate — the **VTA** (including the PBP) is
    **relatively spared** in **early** PD. **Some** PBP
    involvement is documented in **late** disease, and the
    **SNc / VTA vulnerability gradient** is a **continuum** — the
    PBP is **closer to the SNc** cytoarchitecturally and may be
    **more vulnerable** than other VTA subnuclei. Consumers must
    **not** attribute **PD motor symptoms** to the PBP — the
    **SNc** is the **motor** substrate; the PBP is the
    **non-motor / limbic** substrate.

**What is NOT here:** The PBP is **not** the substrate for
**Parkinson's disease motor symptoms** (SNc), **progressive
supranuclear palsy** (SNr / STN), **hemiballismus** (STN),
**Huntington's disease** (striatum), or **Kluver-Bucy syndrome**
(amygdala). Its clinical relevance is **mesocortical /
mesoamygdalar** — **affective, cognitive, and addiction**
circuits — with **no named PBP-specific syndrome**.

Lateralization Notes
--------------------
This is the **right** PBP module. The PBP is **bilaterally
symmetric** — and it carries **NO warning**:

*   **Bilateral Symmetry:** Each hemisphere has its own PBP, with
    **ipsilateral** projections. The two sides are **structurally
    identical** — same **neuromelanin** composition, same
    **dorsal / ventral** tiers, same **prefrontal / amygdalar**
    targets.

*   **Functional-Imaging Laterality (Contested):**
    **Functional-imaging** studies describe **"left PBP"** and
    **"right PBP"** **activations** — but these are
    **laterality-of-activation claims within a paired
    subnucleus**, **contested and task-dependent**. They are
    **NOT** a lateralization warning at the module level.
    Consumers must **not** import a lateralization warning into
    the PBP.

*   **NO Warning of their own:** The right PBP is a **strict-mirror
    pair with NO warning** — **no SLEA warning**, **no
    extended-amygdala warning**, **no rhinencephalon-exclusion
    flag**, **no lateralization warning**. Consumers must **not**
    import any of those warnings into the PBP.

**A consumer that assumes "right PBP = left PBP" will be
structurally correct** — the two sides are **symmetric**. The
**functional-imaging laterality** is a **task-dependent** note,
not a **module-level** warning.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-nucleus or cross-lobe imports.** This module does
    **not** import from ``.../ventral_tegmental_area/right/
    paranigral_nucleus/``, ``.../ventral_tegmental_area/right/
    interfascicular_nucleus/``, ``.../ventral_tegmental_area/
    right/rostral_linear_nucleus/``, ``.../ventral_tegmental_area/
    right/caudal_linear_nucleus/``, ``.../tegmentum/
    substantia_nigra/``, ``.../tegmentum/red_nucleus/``,
    ``.../cortex/frontal/cortex/prefrontal_cortex/``,
    ``.../medial_temporal_lobe/amygdala/``, ``.../basal_ganglia/
    striatum/ventral_striatum/nucleus_accumbens/``, or any other
    container. The PBP's relationships to the SNc, SNr, A8, its
    VTA subnuclear siblings, and its projection targets are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The
    **neuromelanin-containing vs. non-containing**
    subpopulations, the **dorsal / ventral** tiers, the
    **dopamine-glutamate co-transmitting** subpopulation, and the
    **GABAergic / glutamatergic** interneurons are documented as
    **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve subpopulation-level detail through
    the references (Sesack & Grace, 2010; Lammel et al., 2014;
    Fu et al., 2016).
*   **A SUBNUCLEUS of the VTA — NOT the VTA itself.** The PBP is
    **one** of the VTA subnuclei (with PN, IF, RLi, CLi as
    siblings). Consumers must **not** treat "VTA" and "PBP" as
    synonyms.
*   **NOT the substantia nigra pars compacta — the most
    consequential boundary.** The **SNc** is the **A9** cell
    group (nigrostriatal, Parkinson's disease); the **PBP** is
    the **A10** subnucleus (mesocortical / mesoamygdalar,
    addiction / schizophrenia / affective disorders). The shared
    **neuromelanin** and the **fuzzy cytoarchitectural boundary**
    do **not** make them the same structure.
*   **NOT the substantia nigra pars reticulata.** The SNr is the
    **GABAergic basal ganglia output**; the PBP is the
    **dopaminergic A10 subnucleus**.
*   **NOT the retrorubral area (A8).** The A8 group is **caudal
    and dorsolateral** — a **separate dopaminergic cell group**.
*   **NOT the PFC, amygdala, nucleus accumbens, or hippocampus.**
    Those are the PBP's **targets**, not the PBP itself.
*   **NOT the IPN, DR, PAG, red nucleus, or crus cerebri.**
    Those are **adjacent midbrain structures** — different
    nuclei / tracts.
*   **NOT a single uniform dopaminergic population — MULTIPLE
    intra-PBP subpopulations.** The **neuromelanin** tiers, the
    **dorsal / ventral** tiers, and the **co-transmitting**
    neurons are **prose**, not structural children.
*   **SLEA-FREE — no extended-amygdala relationship.** The PBP
    **projects to** the **nucleus accumbens** (a SLEA component),
    but the **PBP itself** is **not** part of the **SLEA
    continuum**, and it carries **no SLEA warning**.
*   **No ``AREA_PATHS`` hop.** The PBP is a **local leaf** under
    the right VTA, not a cross-listed leaf.
*   **No nested cross-listing.** The PBP has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left PBP — strict mirror with NO
    warning.** Right and left PBP modules are **structurally
    identical** — same **leaf** status, same **dorsolateral A10**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.midbrain.tegmentum.ventral_tegmental_area.right import parabrachial_pigmented_nucleus

Or by fully-qualified path string::

    path = (
        "midbrain.tegmentum.ventral_tegmental_area.right."
        "parabrachial_pigmented_nucleus"
    )

**Do not** assume the PBP is the **ventral tegmental area**. The
PBP is **one subnucleus** of the VTA — the VTA also contains
**PN**, **IF**, **RLi**, and **CLi**.

**Do not** assume the PBP is the **substantia nigra pars
compacta**. The **SNc** is the **A9** dopaminergic cell group
(nigrostriatal, Parkinson's disease); the **PBP** is the **A10**
subnucleus (mesocortical / mesoamygdalar, addiction /
schizophrenia / affective disorders). The shared **neuromelanin**
and the **fuzzy cytoarchitectural boundary** do **not** make them
the same structure.

**Do not** assume the PBP is the **substantia nigra pars
reticulata**. The **SNr** is the **GABAergic basal ganglia
output**; the PBP is the **dopaminergic A10 subnucleus**.

**Do not** assume the PBP is the **retrorubral area (A8)**. The
**A8** group is **caudal and dorsolateral** — a separate
dopaminergic cell group.

**Do not** assume the PBP is the **prefrontal cortex**, the
**amygdala**, the **nucleus accumbens**, or the **hippocampus**.
Those are the PBP's **targets**, not the PBP itself.

**Do not** import the **SLEA warning** into the PBP. **The PBP is
SLEA-FREE** — it **projects to** the nucleus accumbens (a SLEA
component), but the **PBP itself** is **not** part of the SLEA
continuum.

Iterating the PBP's (empty) children (recommended consumer
pattern)::

    PARABRACHIAL_PIGMENTED_NUCLEUS_RIGHT_CHILDREN = ()
    # The PBP is a leaf. The neuromelanin-containing vs.
    # non-containing subpopulations, the dorsal / ventral tiers,
    # the dopamine-glutamate co-transmitting neurons, and the
    # GABAergic / glutamatergic interneurons are prose, not
    # modules.

Reaching the other VTA subnuclei (recommended consumer pattern —
the subnuclear siblings)::

    # The other VTA subnuclei are SIBLINGS of the PBP — medial /
    # ventral to it, with different projection topographies:
    #
    #   midbrain.tegmentum.ventral_tegmental_area.right.paranigral_nucleus
    #   midbrain.tegmentum.ventral_tegmental_area.right.interfascicular_nucleus
    #   midbrain.tegmentum.ventral_tegmental_area.right.rostral_linear_nucleus
    #   midbrain.tegmentum.ventral_tegmental_area.right.caudal_linear_nucleus
    #
    # The PBP is the DORSOLATERAL subnucleus (mesocortical /
    # mesoamygdalar); PN and IF are the MEDIAL / VENTRAL subnuclei
    # (mesolimbic, dominant accumbens projection).

Reaching the substantia nigra pars compacta (recommended consumer
pattern — the adjacent dopaminergic sibling)::

    # The SNc is the A9 dopaminergic cell group — nigrostriatal,
    # Parkinson's disease substrate. The PBP abuts the SNc and
    # shares neuromelanin-containing neurons with it — but they
    # are DIFFERENT NUCLEI with different projection targets:
    #
    #   midbrain.tegmentum.substantia_nigra.right.pars_compacta

Reaching the prefrontal cortex (recommended consumer pattern —
the principal mesocortical target)::

    # The prefrontal cortex is the principal TARGET of the PBP's
    # mesocortical dopaminergic projection:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.right.
    #   cortex.frontal.cortex.prefrontal_cortex

Reaching the amygdala (recommended consumer pattern — the
mesoamygdalar target)::

    # The amygdala is a TARGET of the PBP's mesoamygdalar
    # dopaminergic projection:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.right.
    #   subcortical.medial_temporal_lobe.amygdala

Reaching the SLEA components (recommended consumer pattern — NOTE
the PBP is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the PBP —
    # though the PBP PROJECTS TO the nucleus accumbens:
    #
    #   ...medial_temporal_lobe.amygdala.central_nucleus
    #   ...extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   ...basal_ganglia.globus_pallidus.ventral_pallidum
    #   ...basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The PBP is SLEA-FREE.

Subpopulation-level detail (not wired — consult references)::

    # The PBP's subpopulations are prose, not modules:
    #   neuromelanin-containing -> pigmented, shared with the SNc
    #   neuromelanin-poor       -> non-pigmented
    #   dorsal tier             -> prefrontal cortex (mesocortical)
    #   ventral tier            -> amygdala / ventral striatum
    #   dopamine-glutamate      -> co-transmitting (contested)
    #   GABAergic / glutamatergic -> intermingled non-dopaminergic
    #
    # Do not attempt to resolve these as sub-paths of the PBP.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pbp_path = (
            f"midbrain.tegmentum.ventral_tegmental_area.{side}."
            f"parabrachial_pigmented_nucleus"
        )
        # resolve pbp_path through the memory/recall layer

References
----------
*   **VTA anatomy and connectivity:** Sesack, S.R., Grace, A.A.
    (2010). "Cortico-basal ganglia reward network: microcircuitry."
    *Neuropsychopharmacology* 35:27–47. (Definitive VTA
    microcircuitry; the PBP / PN / IF / RLi / CLi subnuclei;
    dopaminergic, GABAergic, and glutamatergic populations.)
*   **VTA subnuclei — human neuroanatomy:** Halliday, G.M.,
    Törk, I. (1989). "Serotonin-like immunoreactive cells in the
    substantia nigra and ventral tegmental area of the rat."
    *Journal of Comparative Neurology* 289:154–164. (The PBP /
    PN / IF / RLi / CLi subnuclear nomenclature — the standard
    reference for the fuzzy PBP / SNc boundary.)
*   **PBP / SNc boundary and neuromelanin:** Fu, Y., et al.
    (2016). "A cytoarchitectonic and chemoarchitectonic analysis
    of the human ventral tegmental area." *Brain Structure and
    Function* 221:3263–3284. (Cytoarchitectural criteria for the
    human PBP / SNc boundary; the shared neuromelanin-containing
    dopaminergic neurons.)
*   **VTA heterogeneity — medial vs. lateral:** Lammel, S., Lim,
    B.K., Malenka, R.C. (2014). "Reward and aversion in a
    heterogeneous midbrain dopamine system."
    *Neuropharmacology* 76:351–359. (Medial vs. lateral VTA
    projection topography; reward vs. aversion subpopulations;
    the dorsolateral PBP in the cortical-projecting pole.)
*   **Dopamine-glutamate co-transmission:** Hnasko, T.S., et al.
    (2012). "Ventral tegmental area glutamate neurons:
    electrophysiological properties and projections." *Journal of
    Neuroscience* 32:15076–15085. (The co-transmitting
    subpopulation — contested functional significance.)
*   **Reward prediction error:** Schultz, W. (1998). "Predictive
    reward signal of dopamine neurons." *Journal of
    Neurophysiology* 80:1–27. (Dopamine reward prediction error —
    VTA-wide; the PBP is a contributing subnucleus.)
*   **Mesocortical dopamine and cognition:** Robbins, T.W.,
    Arnsten, A.F.T. (2009). "The neuropsychopharmacology of
    fronto-executive function: monoaminergic modulation." *Annual
    Review of Neuroscience* 32:267–287. (Mesocortical dopamine
    — the PBP's prefrontal projection and working memory /
    cognitive control.)
*   **Dopamine and schizophrenia:** Howes, O.D., Kapur, S. (2009).
    "The dopamine hypothesis of schizophrenia: version III — the
    final common pathway." *Schizophrenia Bulletin* 35:549–562.
    (Mesocortical hypoactivity — the PBP's prefrontal projection
    as a negative-symptom substrate.)
*   **Mesolimbic dopamine and addiction:** Nestler, E.J. (2005).
    "Is there a common molecular pathway for addiction?" *Nature
    Neuroscience* 8:1445–1449. (VTA → nucleus accumbens as the
    common pathway — the PBP's mesolimbic contribution is
    secondary to PN / IF.)
*   **VTA in Parkinson's disease:** Hirsch, E., Graybiel, A.M.,
    Agid, Y.A. (1988). "Melanized dopaminergic neurons are
    differentially susceptible to degeneration in Parkinson's
    disease." *Nature* 334:345–348. (VTA relative sparing in
    early PD; the SNc / VTA vulnerability gradient; the PBP as
    an intermediate point on the continuum.)
*   **Dopaminergic cell groups (A8, A9, A10):** Dahlström, A.,
    Fuxe, K. (1964). "Evidence for the existence of monoamine-
    containing neurons in the central nervous system. I.
    Demonstration of monoamines in the cell bodies of brain stem
    neurons." *Acta Physiologica Scandinavica* 62 (Suppl. 232):
    1–55. (The A8/A9/A10 dopaminergic cell-group nomenclature.)
*   **SLEA (contrast — the PBP is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    PBP, which projects TO the nucleus accumbens.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Ventral tegmental area and subnuclei in
    overview.)
*   NeuroNames — Parabrachial pigmented nucleus (right); FMA —
    Parabrachial pigmented nucleus (right member).
"""