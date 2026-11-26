"""
infrastructure.brainparts.midbrain.tegmentum.ventral_tegmental_area
=====================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        └── ventral_tegmental_area   <-- THIS MODULE

**Primary synonym:** Ventral tegmental area; VTA; ventral tegmental
area of Tsai; A10 dopaminergic cell group; mesencephalic
dopaminergic complex; "the mesolimbic / mesocortical dopamine
source."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**midbrain tegmental nuclear complex** — the **A10 dopaminergic
cell group**, plus **minor GABAergic and glutamatergic**
populations. The **parabrachial pigmented nucleus (PBP)**, the
**paranigral nucleus (PN)**, the **interfascicular nucleus (IF)**,
the **rostral linear nucleus (RLi)**, and the **caudal linear
nucleus (CLi)** are documented as **prose**, not as structural
children.
**Part of:** The **tegmentum** container — the **ventral
tegmental** region of the **midbrain**, **medial** to the
**substantia nigra** and **ventral** to the **red nucleus**. The
VTA sits **immediately dorsal** to the **interpeduncular
nucleus** and **medial** to the **substantia nigra pars
compacta**.
**Structural parent:** ``.../tegmentum/`` → **direct child** of
the tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**PBP**, **PN**, **IF**, **RLi**, and **CLi** subnuclei, the
**GABAergic** and **glutamatergic** neuronal populations, and the
**medial vs. lateral** projection topography are documented as
**prose**, not as structural children.
**Boundary status (NOT the substantia nigra — the SN is the A9
nigrostriatal complex):** **Boundary case — the VTA is NOT the
substantia nigra.** The **substantia nigra**
(``.../tegmentum/substantia_nigra/``) is the **A9 dopaminergic
(pars compacta)** + **GABAergic (pars reticulata)** complex — it
projects to the **dorsal striatum** (nigrostriatal) and the
**thalamus / superior colliculus** (nigrothalamic / nigrotectal).
The **VTA** (here) is the **A10 dopaminergic** cell group — it
projects to the **ventral striatum (nucleus accumbens)**, the
**prefrontal cortex**, the **amygdala**, and the **hippocampus**
(mesolimbic / mesocortical). **They are DIFFERENT NUCLEI** with
**different projection targets** and **different clinical
associations** (SNc → Parkinson's disease; VTA → addiction /
schizophrenia / reward). Consumers must **not** conflate the two —
the **VTA is not the substantia nigra**, and **"A10" is not
"A9."**
**Boundary status (NOT the retrorubral area / A8 — the A8 group is
a separate dopaminergic cell group):** **Boundary case — the VTA
is NOT the retrorubral area (A8).** The **retrorubral area** is
the **A8 dopaminergic cell group** — it is **caudal and
dorsolateral** to the VTA (and the SNc), and it is **sometimes
grouped with the SN/VTA dopaminergic complex** in the literature.
In this tree it is a **separate structure** (wired elsewhere).
Consumers must **not** silently fold A8 into the VTA — it is a
**distinct dopaminergic cell group**.
**Boundary status (NOT the whole midbrain tegmentum — the
tegmentum contains many other nuclei):** **Boundary case — the VTA
is one nuclear complex within the midbrain tegmentum, not the
tegmentum itself.** The **tegmentum**
(``.../tegmentum/``) contains the **substantia nigra**, the **red
nucleus**, the **periaqueductal gray**, the **oculomotor and
trochlear nuclei**, the **interpeduncular nucleus**, the
**reticular formation**, and others. The VTA is **one** of them.
Consumers must **not** conflate the nucleus with its containing
region.
**Boundary status (NOT the nucleus accumbens — the accumbens is
the VTA's mesolimbic TARGET):** **Boundary case — the VTA is NOT
the nucleus accumbens.** The **nucleus accumbens**
(``.../basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/``)
is the **principal target** of the **mesolimbic dopaminergic
projection** from the VTA. The VTA **sends** dopamine to the
accumbens; the accumbens **receives** it. Consumers must **not**
conflate the **source** (VTA) with the **target** (nucleus
accumbens). **The nucleus accumbens is a SLEA component; the VTA
is NOT** — see the SLEA boundary below.
**Boundary status (NOT the prefrontal cortex — the PFC is the
VTA's mesocortical TARGET):** **Boundary case — the VTA is NOT
the prefrontal cortex.** The **prefrontal cortex**
(``.../cortex/frontal/cortex/prefrontal_cortex/``) is the
**principal target** of the **mesocortical dopaminergic
projection** from the VTA. The VTA **sends** dopamine to the
PFC; the PFC **receives** it and **projects back** to the VTA.
Consumers must **not** conflate the **source** (VTA) with the
**target** (prefrontal cortex).
**Boundary status (NOT the amygdala — the amygdala is a VTA
target):** **Boundary case — the VTA is NOT the amygdala.** The
**amygdala**
(``.../medial_temporal_lobe/amygdala/``) is a **target** of the
**mesolimbic dopaminergic projection** from the VTA. The VTA
**sends** dopamine to the amygdala; the amygdala **receives** it
and **projects back** to the VTA. Consumers must **not** conflate
the **source** (VTA) with the **target** (amygdala).
**Boundary status (NOT the hippocampus — the hippocampus is a VTA
target):** **Boundary case — the VTA is NOT the hippocampus.** The
**hippocampus**
(``.../medial_temporal_lobe/hippocampus/``) is a **target** of
the **mesolimbic dopaminergic projection** from the VTA. The VTA
**sends** dopamine to the hippocampus; the hippocampus
**receives** it and **projects back** to the VTA (via the
**fornix / subiculum**). Consumers must **not** conflate the
**source** (VTA) with the **target** (hippocampus).
**Boundary status (NOT the interpeduncular nucleus — the IPN is
the adjacent midline neighbor):** **Boundary case — the VTA is NOT
the interpeduncular nucleus.** The **interpeduncular nucleus**
(IPN, ``.../tegmentum/interpeduncular_nucleus/`` if wired) is the
**midline** nucleus **immediately ventral** to the VTA — it is a
**habenular-recipient** structure (the **habenulo-interpeduncular
tract**), functionally part of the **epithalamus → midbrain**
circuit. The VTA is the **dopaminergic** complex **dorsal** to
it. Consumers must **not** conflate the two — the **IPN** is a
**habenular relay**; the **VTA** is the **A10 dopaminergic
source**.
**Boundary status (NOT the dorsal raphe — the DR is the
serotonergic midline neighbor):** **Boundary case — the VTA is NOT
the dorsal raphe nucleus.** The **dorsal raphe nucleus**
(``.../midbrain/dorsal_raphe/`` if wired) is the **serotonergic**
midline nucleus of the **midbrain** — it is **dorsal and medial**
to the VTA. The VTA is **dopaminergic**. Consumers must **not**
conflate the two — the **dorsal raphe** is the **serotonergic**
midline source; the **VTA** is the **dopaminergic** ventral
tegmental source.
**Boundary status (NOT the periaqueductal gray — the PAG is the
dorsal midbrain defense / pain structure):** **Boundary case —
the VTA is NOT the periaqueductal gray.** The **periaqueductal
gray** (PAG, ``.../midbrain/periaqueductal_gray/`` if wired) is
the **dorsal midbrain** structure surrounding the **cerebral
aqueduct** — it is the **defense / pain-modulation / vocalization**
substrate. The VTA is **ventral** to it and **dopaminergic**.
Consumers must **not** conflate the two.
**Boundary status (NOT the red nucleus — the red nucleus is the
adjacent rubrospinal / rubro-olivary tegmentum neighbor):**
**Boundary case — the VTA is NOT the red nucleus.** The **red
nucleus** (``.../tegmentum/red_nucleus/``) is the **rubrospinal /
rubro-olivary** motor nucleus of the **midbrain tegmentum** — it
is **dorsal and lateral** to the VTA but **functionally
separate**. Consumers must **not** conflate the two — the **red
nucleus** is a **motor relay**; the **VTA** is the **A10
dopaminergic complex**.
**Boundary status (NOT the crus cerebri / cerebral peduncle — the
crus cerebri is the white-matter tract):** **Boundary case — the
VTA is NOT the crus cerebri.** The **crus cerebri** (cerebral
peduncle, ``.../midbrain/crus_cerebri/`` if wired) is the
**white-matter tract** — the **corticospinal, corticobulbar, and
corticopontine fibers** — that lies **ventral** to the midbrain
tegmentum. The VTA is **grey-matter nucleus** within the
tegmentum. Consumers must **not** conflate the **nucleus** with
the **fiber tract**.
**Boundary status (NOT a single uniform dopaminergic population —
MULTIPLE subnuclei and MULTIPLE neurotransmitters):** **Boundary
case — the VTA is HETEROGENEOUS, not a single uniform
dopaminergic population.** The VTA includes:
*   **Dopaminergic neurons** (the **A10** cell group — the
    dominant, defining population).
*   **GABAergic neurons** — a **significant minority** population
    with **local and long-range** projections; **not** a
    dopaminergic subtype.
*   **Glutamatergic neurons** — a **minor** population with
    **local and long-range** projections; **not** a dopaminergic
    subtype.
*   **Subnuclei** — **PBP**, **PN**, **IF**, **RLi**, **CLi** —
    with **different projection topographies** (medial → limbic;
    lateral → cortical).
**Each population and subnucleus is functionally distinct** — the
tree wires them as **prose** under the VTA leaf, not as structural
children. Consumers must **not** treat the VTA as a single uniform
dopaminergic population — it is a **heterogeneous
dopaminergic/GABAergic/glutamatergic complex** (Lammel et al.,
2014; Fields et al., 2007).
**Boundary status (NOT a SLEA component — the VTA is outside the
extended amygdala):** **Boundary case — the VTA is SLEA-FREE.**
The **SLEA continuum** includes the **central nucleus** (amygdala),
the **BNST**, the **ventral pallidum**, and the **nucleus
accumbens**. The VTA **projects to** the **nucleus accumbens**
(a SLEA component), but the **VTA itself** is **not** part of the
SLEA continuum, and it carries **no SLEA warning**. Consumers must
**not** import the SLEA warning into the VTA — **the VTA is
SLEA-FREE.**

Overview
--------
The ventral tegmental area is the **A10 dopaminergic cell group**
of the **midbrain tegmentum** — the **mesolimbic / mesocortical
dopamine source**, projecting to the **nucleus accumbens**
(ventral striatum), the **prefrontal cortex**, the **amygdala**,
and the **hippocampus**. It is a **leaf** module under the
tegmentum container, and it is the **canonical reward /
motivation / salience** dopaminergic substrate.

**The VTA is NOT the substantia nigra.** The **substantia nigra**
is the **A9 (pars compacta)** + **GABAergic (pars reticulata)**
complex — **nigrostriatal** (dorsal striatum) and
**nigrothalamic / nigrotectal**. The **VTA** is the **A10
dopaminergic** complex — **mesolimbic** (ventral striatum) and
**mesocortical** (prefrontal cortex). **They are DIFFERENT
NUCLEI** with **different projection targets** and **different
clinical associations** (SNc → Parkinson's disease; VTA →
addiction / schizophrenia / reward).

**The VTA is an UNPAIRED MIDLINE structure — there are NO left and
right VTA modules in this tree.** The VTA sits **on the midline**
of the midbrain tegmentum, **medial** to the paired substantia
nigra. Some **functional-imaging** studies describe "left VTA" and
"right VTA" activations, but these are **laterality-of-activation
claims within a single midline complex**, not structurally
separate left/right modules — and they are **contested and
task-dependent**. This module is the **single VTA**; consumers must
**not** look for ``.../ventral_tegmental_area/left/`` or
``.../ventral_tegmental_area/right/`` — they do not exist.

**The VTA is a HETEROGENEOUS complex, not a single uniform
dopaminergic population.** The **dopaminergic (A10)** neurons are
the **defining** population, but the VTA also contains significant
**GABAergic** and minor **glutamatergic** populations with **local
and long-range** projections. The **PBP / PN / IF / RLi / CLi**
subnuclei have **different projection topographies** (medial →
limbic; lateral → cortical). These are **prose**, not structural
children.

**The VTA is SLEA-FREE.** It **projects to** the **nucleus
accumbens** (a SLEA component), but the **VTA itself** is **not**
part of the SLEA continuum, and it carries **no SLEA warning**.

Subnuclear Composition (prose, not structural children)
-------------------------------------------------------
The VTA is a **heterogeneous dopaminergic/GABAergic/glutamatergic
complex** — documented as **prose**, not as structural children:

*   **Parabrachial pigmented nucleus (PBP)** — the **largest**
    VTA subnucleus; **dorsal / lateral** position. Projects
    predominantly to the **prefrontal cortex** and the
    **amygdala** (mesocortical / mesoamygdalar).

*   **Paranigral nucleus (PN)** — **ventral / medial** to the
    PBP. Projects predominantly to the **nucleus accumbens**
    (mesolimbic).

*   **Interfascicular nucleus (IF)** — the **most medial**
    subnucleus, embedded in the **fascicles of the oculomotor
    nerve**. Projects to the **ventral striatum** and the
    **medial prefrontal cortex**.

*   **Rostral linear nucleus (RLi)** — the **rostral-most**
    subnucleus, near the **midbrain-diencephalon junction**.
    Projects to the **medial prefrontal cortex** and the
    **extended amygdala**.

*   **Caudal linear nucleus (CLi)** — the **caudal-most**
    subnucleus. Projects to the **ventral striatum** and the
    **lateral habenula**.

*   **Dopaminergic neurons (A10)** — the **defining** population
    of the VTA. Project to the **nucleus accumbens**, **prefrontal
    cortex**, **amygdala**, and **hippocampus**.

*   **GABAergic neurons** — a **significant minority**
    population with **local and long-range** projections. **Not**
    a dopaminergic subtype — a **separate neurotransmitter
    population** (Cohen et al., 2012).

*   **Glutamatergic neurons** — a **minor** population with
    **local and long-range** projections. **Not** a dopaminergic
    subtype — a **separate neurotransmitter population** (Hnasko
    et al., 2012).

**These subnuclei and populations are prose, not structural
children.** The tree wires the **VTA** as a **single leaf** under
the tegmentum — the **PBP**, **PN**, **IF**, **RLi**, **CLi**,
**GABAergic**, and **glutamatergic** populations are **prose**,
not structural children. Consumers that need **subnucleus-level**
or **neurotransmitter-population-level** resolution should consult
the references (Sesack & Grace, 2010; Lammel et al., 2014), not
the tree.

Function in the Human Brain
---------------------------
The VTA's functions are **dopaminergic modulation of limbic and
cortical targets** — **NOT basal ganglia output, NOT
nigrostriatal motor**:

*   **Mesolimbic Dopamine (VTA → Nucleus Accumbens):** The VTA
    **projects** to the **nucleus accumbens** (ventral striatum)
    and **modulates** the **limbic-motor interface**. This is the
    **neural substrate** of **reward learning**, **motivation**,
    **incentive salience**, and **drug reinforcement** — the
    **canonical "reward pathway"** in the popular and scientific
    literature.

*   **Mesocortical Dopamine (VTA → Prefrontal Cortex):** The VTA
    **projects** to the **prefrontal cortex** (especially the
    **medial prefrontal cortex** and the **anterior cingulate**)
    and **modulates** **working memory**, **cognitive control**,
    **motivation**, and **affective regulation**. **Hypoactivity**
    of this projection is associated with **negative symptoms**
    and **cognitive deficits** in schizophrenia.

*   **Mesoamygdalar Dopamine (VTA → Amygdala):** The VTA
    **projects** to the **amygdala** and **modulates**
    **emotional salience**, **fear learning**, and **threat
    detection**.

*   **Mesohippocampal Dopamine (VTA → Hippocampus):** The VTA
    **projects** to the **hippocampus** and **modulates**
    **memory formation**, **novelty detection**, and
    **exploration**.

*   **Reward Prediction Error (the canonical framing — VTA is the
    primary source):** The **Schultz** framework attributes the
    **reward prediction error** signal primarily to **dopamine
    neurons** — and the **VTA** is the **more commonly cited**
    source than the **SNc** for **reward / motivation**. The
    **SNc vs. VTA division of labor** is **contested**, but the
    **VTA** is the **canonical reward** source in the modern
    literature.

*   **GABAergic and Glutamatergic Modulation:** The VTA's
    **GABAergic** and **glutamatergic** neurons provide
    **local** and **long-range** modulation of the **dopaminergic**
    and **target** circuits — the **GABAergic** neurons
    **inhibit** VTA dopamine neurons and project to the **nucleus
    accumbens** and **prefrontal cortex**; the **glutamatergic**
    neurons **excite** VTA dopamine neurons and project to the
    **nucleus accumbens** and **prefrontal cortex**. Consumers
    must **not** treat "VTA = dopamine" — the VTA is a
    **dopaminergic / GABAergic / glutamatergic** complex.

*   **NOT a basal ganglia output, NOT a motor nucleus.** The VTA
    is **dopaminergic modulation** of **limbic and cortical**
    targets — **NOT** the **basal ganglia output** (that is the
    **SNr / GPi**) and **NOT** the **nigrostriatal motor** system
    (that is the **SNc**).

**The unifying theme:** the VTA is the **mesolimbic / mesocortical
dopamine source** — the **A10** substrate of **reward, motivation,
salience, and cognitive-affective modulation**. It is
**SLEA-free**, **dopaminergic** (with **GABAergic** and
**glutamatergic** minorities), and **NOT the substantia nigra**.

Associated Disorders
--------------------
The VTA has **strong, named clinical associations** — the
**canonical** associations are **addiction**, **schizophrenia**,
and **depression**:

*   **Addiction (Mesolimbic Dopamine — the canonical
    association):** **Drugs of abuse** (cocaine, amphetamine,
    opioids, nicotine, alcohol) **increase** **mesolimbic
    dopamine** (VTA → nucleus accumbens) — the **final common
    pathway** of **drug reinforcement**. **Chronic** drug use
    produces **neuroadaptations** in the **VTA → accumbens**
    circuit — the **cellular basis** of **tolerance**,
    **dependence**, and **relapse**. This is the **most important
    clinical association** of the VTA.

*   **Schizophrenia (Dopamine Hypothesis — mesolimbic /
    mesocortical):** The **dopamine hypothesis** of
    schizophrenia centers on **mesolimbic** dopamine
    (**positive symptoms** — **hyperactivity** of the VTA →
    accumbens projection) and **mesocortical** dopamine
    (**negative symptoms / cognitive deficits** —
    **hypoactivity** of the VTA → prefrontal projection). The
    **VTA** is the **source** of both projections — the
    **canonical** dopamine-hypothesis substrate. Consumers must
    **not** attribute schizophrenia's **EPS** side-effects to
    the VTA — that is the **SNc / nigrostriatal** story.

*   **Depression (Mesocortical / Mesolimbic Dopamine):** **Reduced
    mesolimbic / mesocortical dopamine** is associated with
    **anhedonia**, **reduced motivation**, and **impaired reward
    learning** in **major depressive disorder**. The **VTA** is
    the **source** of the affected projections — documented, but
    **mechanistically contested** (the dopamine contribution is
    **one** of several; **serotonin** and **norepinephrine** are
    also involved).

*   **Parkinson's Disease (VTA Is SPARED Relative to the SNc):**
    **Parkinson's disease** degenerates the **SNc**
    **selectively** — the **VTA** is **relatively spared** in
    **early** PD, though **VTA involvement** is documented in
    **late** disease (contributing to **non-motor** symptoms —
    **depression**, **anxiety**, **cognitive impairment**).
    Consumers must **not** attribute **PD motor symptoms** to
    the VTA — the **SNc** is the **motor** substrate; the
    **VTA** is the **non-motor / limbic** substrate.

*   **Schizophrenia and Antipsychotic Action:** **Antipsychotic**
    drugs **block D2 receptors** in the **mesolimbic** circuit
    (VTA → accumbens) — **reducing positive symptoms** — and in
    the **mesocortical** circuit (VTA → prefrontal) — **not
    improving** (and possibly **worsening**) negative symptoms.
    **D2 blockade** in the **nigrostriatal** circuit (SNc →
    dorsal striatum) produces **EPS** — **not** a VTA effect.

*   **Stimulant Sensitization:** **Repeated stimulant** exposure
    produces **behavioral sensitization** mediated by the
    **VTA → accumbens** circuit — documented in animal models,
    **relevant to addiction liability**.

**What is NOT here:** The VTA is **not** the substrate for
**Parkinson's disease motor symptoms** (SNc), **Huntington's
disease** (striatum), **Kluver-Bucy syndrome** (amygdala),
**Alzheimer's disease** (hippocampus, nucleus basalis), or
**progressive supranuclear palsy** (SNr / STN). Its clinical
relevance is **mesolimbic / mesocortical** — **reward, addiction,
schizophrenia, and motivation** — with **addiction** as the
**canonical** association.

Laterality Notes
----------------
The VTA is an **UNPAIRED MIDLINE structure** — there are **NO left
and right VTA modules** in this tree:

*   **Midline, Unpaired:** The VTA sits **on the midline** of the
    **midbrain tegmentum**, **medial** to the paired **substantia
    nigra**. It is a **single complex**, not a **left/right
    pair** — consumers must **not** look for
    ``.../ventral_tegmental_area/left/`` or
    ``.../ventral_tegmental_area/right/``.

*   **"Left VTA" / "Right VTA" in Imaging (Contested):**
    **Functional-imaging** studies describe **"left VTA"** and
    **"right VTA"** **activations** — but these are
    **laterality-of-activation claims within a single midline
    complex**, **contested and task-dependent**. They are
    **NOT** structural left/right modules and **NOT** a warning
    at the module level. Consumers must **not** treat the VTA as
    a **paired structure** — it is **midline and unpaired**.

*   **NO Warning of their own:** The VTA is **UNPAIRED** with
    **NO warning** — **no SLEA warning**, **no
    extended-amygdala warning**, **no rhinencephalon-exclusion
    flag**, **no lateralization warning**. Consumers must **not**
    import any of those warnings into the VTA.

**A consumer that assumes "the VTA is a paired structure" will be
structurally wrong** — the VTA is **midline and unpaired**. The
**left/right laterality** in imaging is a **functional-activation**
note, not a **structural** fact, and it is **NOT a warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **UNPAIRED MIDLINE STRUCTURE — no left/right children.** The
    VTA is a **single complex**; there are **no
    ``.../ventral_tegmental_area/left/`` or
    ``.../ventral_tegmental_area/right/`` modules**. Consumers
    must **not** look for them.
*   **No cross-nucleus or cross-lobe imports.** This module does
    **not** import from ``.../tegmentum/substantia_nigra/``,
    ``.../tegmentum/red_nucleus/``, ``.../tegmentum/
    interpeduncular_nucleus/``, ``.../basal_ganglia/striatum/
    ventral_striatum/nucleus_accumbens/``, ``.../cortex/frontal/
    cortex/prefrontal_cortex/``, ``.../medial_temporal_lobe/
    amygdala/``, ``.../medial_temporal_lobe/hippocampus/``, or
    any other container. The VTA's relationships to the
    substantia nigra, retrorubral area, nucleus accumbens,
    prefrontal cortex, amygdala, hippocampus, interpeduncular
    nucleus, and dorsal raphe are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **PBP**, **PN**,
    **IF**, **RLi**, and **CLi** subnuclei, the **GABAergic** and
    **glutamatergic** populations, and the **medial vs. lateral**
    projection topography are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve subnucleus-level detail through the references
    (Sesack & Grace, 2010; Lammel et al., 2014).
*   **A10 — NOT A9.** The VTA is the **A10 dopaminergic** cell
    group; the **substantia nigra pars compacta** is the **A9**
    cell group. Consumers must **not** conflate the two.
*   **NOT the substantia nigra.** The SN is the **A9 (pars
    compacta)** + **GABAergic (pars reticulata)** complex —
    **nigrostriatal** and **nigrothalamic / nigrotectal**. The
    VTA is **A10** — **mesolimbic / mesocortical**.
*   **NOT the retrorubral area (A8).** The A8 group is **caudal
    and dorsolateral** — a **separate structure**.
*   **NOT the whole midbrain tegmentum.** The tegmentum contains
    many other nuclei.
*   **NOT the nucleus accumbens, prefrontal cortex, amygdala, or
    hippocampus.** These are the VTA's **targets**, not the VTA
    itself.
*   **NOT the interpeduncular nucleus.** The IPN is the
    **habenular-recipient midline neighbor**, **ventral** to the
    VTA.
*   **NOT the dorsal raphe.** The DR is the **serotonergic
    midline** nucleus, **dorsal** to the VTA.
*   **NOT the periaqueductal gray.** The PAG is the **dorsal
    midbrain** defense / pain structure.
*   **NOT the red nucleus.** The red nucleus is the **adjacent
    rubrospinal / rubro-olivary motor relay**.
*   **NOT the crus cerebri.** The crus cerebri is the
    **white-matter tract** ventral to the tegmentum; the VTA is
    the **grey-matter nucleus**.
*   **NOT a single uniform dopaminergic population — MULTIPLE
    subnuclei and MULTIPLE neurotransmitters.** The **PBP**,
    **PN**, **IF**, **RLi**, **CLi**, **GABAergic**, and
    **glutamatergic** populations are **prose**, not structural
    children.
*   **SLEA-FREE — no extended-amygdala relationship.** The VTA
    **projects to** the **nucleus accumbens** (a SLEA component),
    but the **VTA itself** is **not** part of the **SLEA
    continuum**, and it carries **no SLEA warning**.
*   **No ``AREA_PATHS`` hop.** The VTA is a **local leaf** under
    the tegmentum, not a cross-listed leaf.
*   **No nested cross-listing.** The VTA has no nested
    dual-framing module. It is a single leaf.
*   **NO lateralization warning.** The VTA is **unpaired and
    midline** — there is **no left/right module pair** and **no
    lateralization warning**. The "left VTA / right VTA"
    imaging laterality is a **functional-activation** note, not
    a structural fact.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.midbrain.tegmentum import ventral_tegmental_area

Or by fully-qualified path string::

    path = (
        "midbrain.tegmentum.ventral_tegmental_area"
    )

**Do not** assume the VTA is the **substantia nigra**. The VTA is
the **A10 dopaminergic** cell group (mesolimbic / mesocortical);
the **substantia nigra** is the **A9 (pars compacta)** +
**GABAergic (pars reticulata)** complex (nigrostriatal /
nigrothalamic / nigrotectal).

**Do not** assume the VTA is the **retrorubral area (A8)**. The
**A8** group is **caudal and dorsolateral** — a separate
dopaminergic cell group.

**Do not** assume the VTA is the **nucleus accumbens**, the
**prefrontal cortex**, the **amygdala**, or the **hippocampus**.
Those are the VTA's **targets**, not the VTA itself.

**Do not** assume the VTA is the **interpeduncular nucleus**, the
**dorsal raphe**, the **periaqueductal gray**, or the **red
nucleus**. Those are **adjacent midbrain nuclei** — **different
structures**.

**Do not** assume the VTA is a **paired structure**. The VTA is
**midline and unpaired** — there are **no left/right VTA
modules** in this tree.

**Do not** import the **SLEA warning** into the VTA. **The VTA is
SLEA-FREE** — it **projects to** the nucleus accumbens (a SLEA
component), but the **VTA itself** is **not** part of the SLEA
continuum.

Iterating the VTA's (empty) children (recommended consumer
pattern)::

    VENTRAL_TEGMENTAL_AREA_CHILDREN = ()
    # The VTA is a leaf. The PBP, PN, IF, RLi, and CLi subnuclei,
    # the GABAergic and glutamatergic populations, and the
    # medial vs. lateral projection topography are prose, not
    # modules.

Reaching the substantia nigra (recommended consumer pattern — the
adjacent dopaminergic sibling)::

    # The substantia nigra is the A9 (pars compacta) + GABAergic
    # (pars reticulata) complex — nigrostriatal / nigrothalamic
    # / nigrotectal, NOT mesolimbic / mesocortical:
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # The substantia nigra is PAIRED (left / right); the VTA is
    # UNPAIRED (midline).

Reaching the nucleus accumbens (recommended consumer pattern —
the mesolimbic target)::

    # The nucleus accumbens (ventral striatum) is the principal
    # TARGET of the mesolimbic dopaminergic projection from the
    # VTA:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left.
    #   subcortical.basal_ganglia.striatum.ventral_striatum.
    #   nucleus_accumbens
    #
    # The nucleus accumbens is a SLEA component; the VTA is NOT.

Reaching the prefrontal cortex (recommended consumer pattern —
the mesocortical target)::

    # The prefrontal cortex is the principal TARGET of the
    # mesocortical dopaminergic projection from the VTA:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left.
    #   cortex.frontal.cortex.prefrontal_cortex

Reaching the amygdala (recommended consumer pattern — the
mesoamygdalar target)::

    # The amygdala is a TARGET of the mesoamygdalar dopaminergic
    # projection from the VTA:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left.
    #   subcortical.medial_temporal_lobe.amygdala

Reaching the hippocampus (recommended consumer pattern — the
mesohippocampal target)::

    # The hippocampus is a TARGET of the mesohippocampal
    # dopaminergic projection from the VTA:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left.
    #   subcortical.medial_temporal_lobe.hippocampus

Reaching the SLEA components (recommended consumer pattern — NOTE
the VTA is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the VTA —
    # though the VTA PROJECTS TO the nucleus accumbens:
    #
    #   ...medial_temporal_lobe.amygdala.central_nucleus
    #   ...extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   ...basal_ganglia.globus_pallidus.ventral_pallidum
    #   ...basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The VTA is SLEA-FREE.

Subnucleus-level detail (not wired — consult references)::

    # The VTA's subnuclei are prose, not modules:
    #   PBP -> prefrontal cortex, amygdala (mesocortical / mesoamygdalar)
    #   PN  -> nucleus accumbens (mesolimbic)
    #   IF  -> ventral striatum, medial prefrontal cortex
    #   RLi -> medial prefrontal cortex, extended amygdala
    #   CLi -> ventral striatum, lateral habenula
    #   GABAergic neurons -> local + long-range inhibition
    #   glutamatergic neurons -> local + long-range excitation
    #
    # Do not attempt to resolve these as sub-paths of the VTA.

Reaching the VTA from the hemisphere loops (recommended consumer
pattern — NOTE the VTA is UNPAIRED)::

    # The VTA has NO left/right module — iterate it ONCE, not per
    # hemisphere:
    #
    vta_path = "midbrain.tegmentum.ventral_tegmental_area"
    # resolve vta_path through the memory/recall layer
    #
    # Do NOT write:
    #   for side in ("left", "right"):
    #       f"midbrain.tegmentum.ventral_tegmental_area.{side}"
    # That path does not exist.

References
----------
*   **VTA anatomy and connectivity:** Sesack, S.R., Grace, A.A.
    (2010). "Cortico-basal ganglia reward network: microcircuitry."
    *Neuropsychopharmacology* 35:27–47. (Definitive VTA
    microcircuitry; dopaminergic, GABAergic, and glutamatergic
    populations; PBP/PN/IF/RLi/CLi subnuclei.)
*   **VTA heterogeneity:** Lammel, S., Lim, B.K., Malenka, R.C.
    (2014). "Reward and aversion in a heterogeneous midbrain
    dopamine system." *Neuropharmacology* 76:351–359. (Medial vs.
    lateral VTA projection topography; reward vs. aversion
    subpopulations.)
*   **GABAergic VTA neurons:** Cohen, J.Y., et al. (2012).
    "Neuron-type-specific signals for reward and punishment in the
    ventral tegmental area." *Nature* 482:85–88. (GABAergic VTA
    neurons and reward / punishment signaling.)
*   **Glutamatergic VTA neurons:** Hnasko, T.S., et al. (2012).
    "Ventral tegmental area glutamate neurons: electrophysiological
    properties and projections." *Journal of Neuroscience*
    32:15076–15085. (Glutamatergic VTA neurons and their
    projections.)
*   **Reward prediction error:** Schultz, W. (1998). "Predictive
    reward signal of dopamine neurons." *Journal of
    Neurophysiology* 80:1–27. (Dopamine reward prediction error —
    VTA as the primary source; the SNc/VTA division of labor is
    contested.)
*   **Mesolimbic dopamine and addiction:** Nestler, E.J. (2005).
    "Is there a common molecular pathway for addiction?" *Nature
    Neuroscience* 8:1445–1449. (VTA → nucleus accumbens as the
    common pathway of drug reinforcement.)
*   **Dopamine and schizophrenia:** Howes, O.D., Kapur, S. (2009).
    "The dopamine hypothesis of schizophrenia: version III — the
    final common pathway." *Schizophrenia Bulletin* 35:549–562.
    (Mesolimbic hyperactivity / mesocortical hypoactivity;
    VTA as the source.)
*   **VTA and depression:** Nestler, E.J., Carlezon, W.A. (2006).
    "The mesolimbic dopamine reward circuit in depression."
    *Biological Psychiatry* 59:1151–1159. (VTA → accumbens and
    anhedonia; the dopamine contribution is contested.)
*   **VTA in Parkinson's disease:** Hirsch, E., Graybiel, A.M.,
    Agid, Y.A. (1988). "Melanized dopaminergic neurons are
    differentially susceptible to degeneration in Parkinson's
    disease." *Nature* 334:345–348. (VTA relative sparing in
    early PD; SNc selective vulnerability.)
*   **Dopaminergic cell groups (A8, A9, A10):** Dahlström, A.,
    Fuxe, K. (1964). "Evidence for the existence of monoamine-
    containing neurons in the central nervous system. I.
    Demonstration of monoamines in the cell bodies of brain stem
    neurons." *Acta Physiologica Scandinavica* 62 (Suppl. 232):
    1–55. (The A8/A9/A10 dopaminergic cell-group nomenclature.)
*   **Mesocortical dopamine and cognition:** Robbins, T.W.,
    Arnsten, A.F.T. (2009). "The neuropsychopharmacology of
    fronto-executive function: monoaminergic modulation." *Annual
    Review of Neuroscience* 32:267–287. (Mesocortical dopamine
    and working memory / cognitive control.)
*   **SLEA (contrast — the VTA is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    VTA, which projects TO the nucleus accumbens.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Ventral tegmental area in overview.)
*   NeuroNames — Ventral tegmental area; FMA — Ventral tegmental
    area.
"""