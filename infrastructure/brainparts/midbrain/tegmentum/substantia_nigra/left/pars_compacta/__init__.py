"""
infrastructure.brainparts.midbrain.tegmentum.substantia_nigra.left.pars_compacta
=================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        └── substantia_nigra
            └── left
                └── pars_compacta   <-- THIS MODULE

**Primary synonym:** Pars compacta of the left substantia nigra;
left SNc; left substantia nigra pars compacta; left A9 dopaminergic
cell group; left neuromelanin-containing nigral component; "the
black substance's dark component."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**dopaminergic nuclear subdivision** — the **A9 cell group** of the
midbrain tegmentum. **Neuromelanin-containing** (the dark pigment
that gives the substantia nigra its name). The **calbindin-rich
matrix** and the **calbindin-poor nigrosomes** are documented as
**prose**, not as structural children.
**Part of:** The **substantia_nigra** container — specifically, the
**dopaminergic** component (**with the pars_reticulata as its
GABAergic sibling**). The **substantia nigra** sits in the
**midbrain tegmentum**, dorsal to the **crus cerebri**.
**Structural parent:** ``.../substantia_nigra/left/`` → **direct
child** of the left substantia nigra.
**Structural children:** **None.** This is a **leaf** module. The
**calbindin-rich matrix**, the **calbindin-poor nigrosomes**
(including **nigrosome-1**, the ventrolateral tier most vulnerable
in Parkinson's disease), and the **dorsal vs. ventral tier**
subdivisions are documented as **prose**, not as structural
children.
**Boundary status (NOT the pars reticulata — that is the GABAergic
sibling):** **Boundary case — the pars compacta is NOT the pars
reticulata.** The **pars reticulata**
(``.../substantia_nigra/left/pars_reticulata/``) is the
**GABAergic** component — the **basal ganglia output nucleus**,
functionally parallel to the GPi, projecting to the **thalamus**
and **superior colliculus**. The **pars compacta** (here) is the
**dopaminergic** component — the **A9 cell group**, projecting to
the **dorsal striatum**. **They are DIFFERENT SUBDIVISIONS** with
**different neurotransmitters**, **different projection targets**,
and **different clinical associations** (SNc → Parkinson's
disease; SNr → saccadic / parkinsonism-plus gaze palsy).
Consumers must **not** conflate the two — the **pars compacta** is
the **dopaminergic input modulator**; the **pars reticulata** is
the **GABAergic output**.
**Boundary status (NOT the ventral tegmental area — the VTA is the
A10 cell group):** **Boundary case — the pars compacta is NOT the
ventral tegmental area (VTA).** The **VTA**
(``.../tegmentum/ventral_tegmental_area/``) is the **A10
dopaminergic cell group** — it projects to the **ventral striatum
(nucleus accumbens)**, the **prefrontal cortex**, and the
**amygdala** (mesolimbic / mesocortical pathways). The **pars
compacta** (here) is the **A9 dopaminergic cell group** — it
projects to the **dorsal striatum** (nigrostriatal pathway).
**They are DIFFERENT NUCLEI** with **different projection
targets** and **different clinical associations** (SNc →
Parkinson's disease; VTA → reward / addiction / schizophrenia).
Consumers must **not** conflate the two.
**Boundary status (NOT the retrorubral area / A8 — the A8 group is
a separate dopaminergic cell group):** **Boundary case — the pars
compacta is NOT the retrorubral area (A8).** The **retrorubral
area** is the **A8 dopaminergic cell group** — it is **caudal and
dorsolateral** to the SNc and is **sometimes grouped with the
SN/VTA dopaminergic complex** in the literature. In this tree it is
a **separate structure** (wired elsewhere). Consumers must **not**
silently fold A8 into the pars compacta.
**Boundary status (NOT the whole substantia nigra — the pars
reticulata is the other component):** **Boundary case — the pars
compacta is a COMPONENT of the substantia nigra, not the whole
substantia nigra.** The **substantia nigra**
(``.../substantia_nigra/left/``) container holds **both**
**pars_compacta** (here, dopaminergic) and **pars_reticulata**
(GABAergic). Consumers must **not** treat "substantia nigra" and
"pars compacta" as synonyms — the pars compacta is the
**dopaminergic** component; the substantia nigra also contains the
**GABAergic** component.
**Boundary status (NOT the dorsal striatum — the striatum is the
pars compacta's target):** **Boundary case — the pars compacta is
NOT the dorsal striatum.** The **dorsal striatum** (caudate +
putamen, ``.../basal_ganglia/striatum/dorsal_striatum/``) is the
**target** of the **nigrostriatal dopaminergic projection** from
the pars compacta. The pars compacta **sends** dopamine to the
striatum; the striatum **receives** it. Consumers must **not**
conflate the **source** (pars compacta) with the **target**
(dorsal striatum).
**Boundary status (NOT the subthalamic nucleus — the STN is the
indirect-pathway glutamatergic node):** **Boundary case — the pars
compacta is NOT the subthalamic nucleus.** The **subthalamic
nucleus** (``.../subthalamus/subthalamic_nucleus/``) is the
**glutamatergic** node of the **indirect pathway** — it **excites**
the **SNr/GPi** output. The **pars compacta** (here) is the
**dopaminergic modulator** of the **whole striatal circuit** — it
is **upstream** of both direct and indirect pathways. Consumers
must **not** conflate the two — the **STN** is the
**indirect-pathway driver**; the **pars compacta** is the
**dopaminergic modulator**.
**Boundary status (NOT the globus pallidus — GPi is the other basal
ganglia output):** **Boundary case — the pars compacta is NOT the
globus pallidus.** The **globus pallidus**
(``.../basal_ganglia/globus_pallidus/``) is a **basal ganglia
output nucleus** (GPi — functionally parallel to the **pars
reticulata**, not the pars compacta) and a **GABAergic relay**
(GPe). The **pars compacta** (here) is the **dopaminergic input
modulator** — it does **not** project to the thalamus as an output
nucleus. Consumers must **not** conflate the pars compacta with
the pallidum — the **pallidum** is **output / relay**; the **pars
compacta** is **dopaminergic modulation**.
**Boundary status (NOT the red nucleus — the red nucleus is the
adjacent rubrospinal / rubro-olivary tegmentum neighbor):**
**Boundary case — the pars compacta is NOT the red nucleus.** The
**red nucleus** (``.../tegmentum/red_nucleus/``) is the
**rubrospinal / rubro-olivary** motor nucleus of the **midbrain
tegmentum** — it is **adjacent** to the substantia nigra but
**functionally separate**. Consumers must **not** conflate the two
— the **red nucleus** is a **motor relay**; the **pars compacta**
is the **dopaminergic modulatory** component.
**Boundary status (NOT the crus cerebri / cerebral peduncle — the
crus cerebri is the white-matter tract ventral to the SN):**
**Boundary case — the pars compacta is NOT the crus cerebri.** The
**crus cerebri** (cerebral peduncle, ``.../midbrain/crus_cerebri/``
if wired) is the **white-matter tract** — the **corticospinal,
corticobulbar, and corticopontine fibers** — that lies **ventral**
to the substantia nigra. The pars compacta is **grey-matter
nucleus** dorsal to it. Consumers must **not** conflate the
**nucleus** with the **fiber tract** that forms its ventral
boundary.
**Boundary status (NOT the dopaminergic neurons embedded in the
pars reticulata — those are pars reticulata prose):** **Boundary
case — the pars compacta is NOT the dopaminergic neurons embedded
in the pars reticulata.** A small population of **dopaminergic**
neurons is found **within the pars reticulata** — these are
documented as **pars reticulata prose**, not as part of the pars
compacta. Consumers must **not** fold the **SNr-embedded
dopaminergic** neurons into the pars compacta — they are a
**distinct, prose-level** population.
**Boundary status (NOT a single uniform dopaminergic population —
MULTIPLE subpopulations with DIFFERENT functions and
vulnerabilities):** **Boundary case — the pars compacta is
HETEROGENEOUS, not a single uniform dopaminergic population.** The
pars compacta includes:
*   **Calbindin-rich matrix** — the **dorsal tier**; relatively
    **spared** in Parkinson's disease.
*   **Calbindin-poor nigrosomes** (including **nigrosome-1**) —
    the **ventrolateral tier**; **selectively vulnerable** in
    Parkinson's disease.
*   **Dorsal vs. ventral tier** — different projection targets
    (matrix → **striatal matrix** / sensorimotor; nigrosomes →
    **striosomes** / limbic-associative).
**Each subpopulation is functionally distinct** — the tree wires
them as **prose** under the pars_compacta leaf, not as structural
children. Consumers must **not** treat the pars compacta as a
single uniform dopaminergic population — it is a **compartmental
dopaminergic complex** (Damier / Graybiel).
**Boundary status (NOT a SLEA component — the pars compacta is
outside the extended amygdala):** **Boundary case — the pars
compacta is SLEA-FREE.** The **SLEA continuum** includes the
**central nucleus** (amygdala), the **BNST**, the **ventral
pallidum**, and the **nucleus accumbens**. The pars compacta is
**not** part of it, and it carries **no SLEA warning**. Consumers
must **not** import the SLEA warning into the pars compacta.

Overview
--------
The left pars compacta is the **dopaminergic component** of the
**left substantia nigra** — the **A9 cell group**, **neuromelanin-
containing**, projecting to the **dorsal striatum** via the
**nigrostriatal pathway**. It is a **leaf** module under the left
substantia nigra, and it is the **canonical Parkinson's disease**
substrate.

**The pars compacta is the DOPAMINERGIC component, NOT the
GABAergic pars reticulata.** The **pars reticulata**
(``.../substantia_nigra/left/pars_reticulata/``) is the **GABAergic
output** — the basal ganglia output nucleus functionally parallel
to the GPi. The **pars compacta** (here) is the **dopaminergic
modulator** — the A9 cell group projecting to the dorsal striatum.
**They are DIFFERENT SUBDIVISIONS** with **different
neurotransmitters** and **different projection targets**.

**The pars compacta is NOT the ventral tegmental area (VTA).** The
**VTA** is the **A10** cell group — mesolimbic / mesocortical,
projecting to the **ventral striatum**, **prefrontal cortex**, and
**amygdala**. The **pars compacta** is the **A9** cell group —
**nigrostriatal**, projecting to the **dorsal striatum**. The two
are **different dopaminergic cell groups** with **different
clinical associations** (SNc → Parkinson's disease; VTA →
reward / addiction / schizophrenia).

**The pars compacta is a HETEROGENEOUS dopaminergic complex, not a
single uniform population.** The **calbindin-rich matrix**
(dorsal tier, relatively spared in PD) and the **calbindin-poor
nigrosomes** (ventrolateral tier, selectively vulnerable in PD)
are **functionally distinct** subpopulations — wired as **prose**,
not structural children. Consumers must **not** treat the pars
compacta as a single uniform dopaminergic population.

**The pars compacta is a paired structure.** Each hemisphere has
its own pars compacta, with **ipsilateral** projections. The two
sides are **bilaterally symmetric** — the lateralization is
**subtle and clinical-onset-level** (see *Lateralization Notes*).

**The pars compacta is SLEA-FREE.** It is a **midbrain dopaminergic
nucleus** — not an extended-amygdala component, and not a limbic
reward nucleus in the narrow sense (that is primarily the **VTA**).

Compartmental Composition (prose, not structural children)
----------------------------------------------------------
The pars compacta is a **compartmental dopaminergic complex** —
documented as **prose**, not as structural children:

*   **Calbindin-rich matrix** — the **dorsal tier**. Relatively
    **spared** in Parkinson's disease. Projects primarily to the
    **striatal matrix** (sensorimotor territories). **Higher
    calbindin** content confers **relative resistance** to
    degeneration.

*   **Calbindin-poor nigrosomes** (including **nigrosome-1**) —
    the **ventrolateral tier**. **Selectively vulnerable** in
    Parkinson's disease — this is the **earliest-degenerating**
    subpopulation. Projects primarily to the **striosomes**
    (limbic-associative territories). **Low calbindin** and
    **high neuromelanin** content confer **relative
    vulnerability**.

*   **Dorsal tier** — the **calbindin-rich matrix** component.
    **Relatively spared** in PD.

*   **Ventral tier** — the **calbindin-poor nigrosome** component.
    **Selectively vulnerable** in PD.

*   **Neuromelanin-containing neurons** — the **dark pigment**
    (from **dopamine oxidation**) that gives the substantia nigra
    its name. **Not** a structural subdivision — a **histochemical
    property** of most pars compacta neurons.

**These compartments are prose, not structural children.** The
tree wires the **pars_compacta** as a **single leaf** under the
left substantia nigra — the **calbindin-rich matrix**, the
**calbindin-poor nigrosomes**, and the **dorsal / ventral tier**
subdivisions are **prose**, not structural children. Consumers
that need **compartment-level** resolution should consult the
references (Damier et al., 1999), not the tree.

Function in the Human Brain
---------------------------
The pars compacta's functions are **dopaminergic modulation** —
**NOT basal ganglia output, NOT limbic reward**:

*   **Nigrostriatal Dopamine (SNc → Dorsal Striatum):** The **pars
    compacta** **projects** to the **dorsal striatum** (caudate +
    putamen) and **modulates** the **corticostriatal** input via
    **D1** (direct-pathway, facilitatory) and **D2**
    (indirect-pathway, inhibitory) receptors. This is the **neural
    substrate** of **action selection**, **habit learning**,
    **motor vigor**, and **reinforcement learning**.

*   **Reward Prediction Error (Contested — predominantly VTA in the
    modern literature):** The **Schultz** framing attributes the
    **reward prediction error** signal primarily to **dopamine
    neurons** — but the **SNc vs. VTA division of labor** is
    **contested**. The **VTA** is more commonly cited for
    **reward / motivation**; the **SNc** is more commonly cited for
    **movement vigor / action selection**. Consumers must **not**
    over-attribute the **reward prediction error** to the pars
    compacta — the **SNc/VTA division** is **contested**, and the
    **VTA** is the **canonical** reward source.

*   **Motor Vigor and Action Selection:** Via the **nigrostriatal**
    projection to the **dorsal striatum**, the pars compacta
    **modulates** movement vigor, action initiation, and action
    selection — the **motor** functions classically lost in
    **Parkinson's disease**.

*   **Habit Learning:** The **nigrostriatal** projection to the
    **dorsal striatum** is the substrate of **habit learning** —
    the **stimulus-response** learning that underlies
    **procedural / automatic** behavior (Redgrave et al., 2010).

*   **Neuromelanin as a Byproduct (not a function):** The
    **neuromelanin** pigment is a **byproduct** of **dopamine
    oxidation** — it is **not** a neurotransmitter and **not** a
    function. It is a **histochemical marker** of the pars
    compacta and a **clinical biomarker** (neuromelanin-sensitive
    MRI).

*   **NOT a cortical processor, NOT a limbic reward nucleus in the
    narrow sense.** The pars compacta is a **midbrain dopaminergic
    nucleus** — its functions are **motor / action selection /
    habit (nigrostriatal)**. The **reward / limbic** functions are
    primarily the **VTA's** (mesolimbic / mesocortical); the
    **pars compacta's role in reward** is **contested and
    secondary**.

**The unifying theme:** the pars compacta is the **dopaminergic
modulator** of the **dorsal striatum** — the **nigrostriatal**
substrate of **action selection**, **motor vigor**, and **habit
learning**. It is **SLEA-free**, **dopaminergic**, and **NOT the
GABAergic output** — the **output** is the **pars reticulata**.

Associated Disorders
--------------------
The pars compacta has **strong, named clinical associations** —
this is a **canonical disease substrate**:

*   **Parkinson's Disease (Pars Compacta Dopamine Neuron Loss —
    the canonical association):** **Selective degeneration** of
    the **pars compacta dopaminergic neurons** — specifically the
    **calbindin-poor nigrosomes** of the **ventrolateral tier**
    projecting to the **putamen** — is the **defining
    neuropathology** of **Parkinson's disease**. **Neuromelanin**
    loss on **MRI** (neuromelanin-sensitive imaging,
    **nigrosome-1** signal loss) is used as an **in vivo
    biomarker**. **Lewy bodies** (α-synuclein) form in the
    surviving pars compacta neurons (Braak staging). This is the
    **most important clinical association** of the pars compacta.

*   **MPTP Toxicity (Pars Compacta-Selective Toxin):** **MPTP**
    (via its metabolite **MPP+**) is **selectively toxic** to
    **pars compacta dopaminergic neurons** — it produces an
    **acute parkinsonian syndrome** and is the **canonical
    experimental model** of Parkinson's disease. It is **pars
    compacta-selective**, which is part of why the pars compacta
    is the **Parkinson's substrate**.

*   **Parkinson-Plus Syndromes (Pars Compacta + Pars Reticulata +
    beyond):** **Progressive supranuclear palsy (PSP)** involves
    **pars compacta and pars reticulata** degeneration
    (tauopathy) — with **pars reticulata** involvement
    contributing to the **supranuclear gaze palsy**. **Multiple
    system atrophy (MSA)** and **corticobasal degeneration
    (CBD)** also involve the pars compacta. Consumers must **not**
    attribute all parkinsonism to the **pars compacta alone** —
    the **pars reticulata** and the **wider basal ganglia** are
    involved in the plus syndromes.

*   **Restless Legs Syndrome (Iron / Neuromelanin):** **Iron
    deficiency** in the substantia nigra (and **neuromelanin**
    changes) is associated with **restless legs syndrome** —
    documented, but **mechanistically contested**.

*   **Wilson's Disease and Manganese Toxicity:** **Copper**
    (Wilson's) and **manganese** (welding, hepatic
    encephalopathy) accumulate in the **basal ganglia**, including
    the substantia nigra — producing **parkinsonism** and **MRI
    T1 hyperintensity**. Documented, but **not pars compacta-
    selective** in the way Parkinson's is.

*   **Schizophrenia (Dopamine Hypothesis — mostly VTA/Ventral
    Striatum):** The **dopamine hypothesis** of schizophrenia
    centers on **mesolimbic / mesocortical** dopamine (VTA
    projections) — but **pars compacta / nigrostriatal** dopamine
    is **implicated** in **antipsychotic-induced extrapyramidal
    symptoms** (D2 blockade in the **dorsal striatum**). Consumers
    must **not** attribute schizophrenia's **positive symptoms**
    to the pars compacta — that is the **VTA / ventral striatum**
    story; the pars compacta is the **EPS / motor side-effect**
    story.

**What is NOT here:** The pars compacta is **not** the substrate
for **Huntington's disease** (striatum — caudate/putamen),
**Kluver-Bucy syndrome** (amygdala), **Alzheimer's disease**
(hippocampus, nucleus basalis), or **addiction** (VTA / nucleus
accumbens). Its clinical relevance is **nigrostriatal** —
**motor, action selection, and habit** — with **Parkinson's
disease** as the **canonical** association.

Lateralization Notes
--------------------
This is the **left** pars compacta module. The pars compacta is
**bilaterally symmetric** — and it carries **NO warning**:

*   **Bilateral Symmetry:** Each hemisphere has its own pars
    compacta, with **ipsilateral** projections. The two sides are
    **structurally identical** — same **matrix / nigrosome**
    composition, same **nigrostriatal** targets.

*   **Clinical Asymmetry (PD Onset — contested at the structural
    level):** **Parkinson's disease** often presents with
    **asymmetric motor symptoms** (one side first) — but this is
    **clinical-onset asymmetry**, and the **structural
    lateralization** of the pars compacta is **subtle and
    contested**. It is documented in the **substantia_nigra
    container**, not at the **left** module level, and it is
    **NOT a warning**.

*   **NO Warning of their own:** The left pars compacta is a
    **strict-mirror pair with NO warning** — **no SLEA warning**,
    **no extended-amygdala warning**, **no rhinencephalon-
    exclusion flag**. Consumers must **not** import any of those
    warnings into the pars compacta.

**A consumer that assumes "left pars compacta = right pars
compacta" will be structurally correct** — the two sides are
**symmetric**. The clinical-onset asymmetry in Parkinson's is a
**container-level / clinical** note, not a **module-level**
warning.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-nucleus or cross-lobe imports.** This module does
    **not** import from ``.../substantia_nigra/left/
    pars_reticulata/``, ``.../tegmentum/ventral_tegmental_area/``,
    ``.../tegmentum/red_nucleus/``, ``.../subthalamus/
    subthalamic_nucleus/``, ``.../basal_ganglia/globus_pallidus/``,
    ``.../basal_ganglia/striatum/dorsal_striatum/``, or any other
    container. The pars compacta's relationships to the pars
    reticulata, VTA, STN, GPi, dorsal striatum, red nucleus, and
    crus cerebri are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **calbindin-rich
    matrix**, the **calbindin-poor nigrosomes** (including
    **nigrosome-1**), and the **dorsal / ventral tier**
    subdivisions are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    compartment-level detail through the references (Damier et
    al., 1999).
*   **DOPAMINERGIC — NOT the GABAergic pars reticulata.** The pars
    compacta is the **A9 dopaminergic** component; the **pars
    reticulata** is the **GABAergic output**. Consumers must
    **not** conflate the two.
*   **NOT the VTA.** The VTA is the **A10** cell group; the pars
    compacta is the **A9** cell group.
*   **NOT the retrorubral area (A8).** The A8 group is **caudal
    and dorsolateral** — a **separate structure**.
*   **NOT the whole substantia nigra.** The pars compacta is a
    **component** of the substantia nigra; the **pars reticulata**
    is the other component.
*   **NOT the dorsal striatum.** The striatum is the **pars
    compacta's target**, not the pars compacta itself.
*   **NOT the subthalamic nucleus.** The STN is the
    **indirect-pathway glutamatergic** driver; the pars compacta
    is the **dopaminergic modulator**.
*   **NOT the globus pallidus.** The pallidum is **output /
    relay**; the pars compacta is **dopaminergic modulation**.
*   **NOT the crus cerebri.** The crus cerebri is the
    **white-matter tract** ventral to the SN; the pars compacta
    is the **grey-matter nucleus**.
*   **NOT the red nucleus.** The red nucleus is the **adjacent
    rubrospinal / rubro-olivary motor relay**.
*   **NOT the dopaminergic neurons embedded in the pars reticulata.**
    Those are **pars reticulata prose**, not pars compacta.
*   **NOT a single uniform dopaminergic population — MULTIPLE
    subpopulations.** The **calbindin-rich matrix** and the
    **calbindin-poor nigrosomes** are **prose**, not structural
    children.
*   **SLEA-FREE — no extended-amygdala relationship.** The pars
    compacta is **not** an extended-amygdala component.
*   **No ``AREA_PATHS`` hop.** The pars compacta is a **local
    leaf** under the left substantia nigra, not a cross-listed
    leaf (unlike Brodmann areas).
*   **No nested cross-listing.** The pars compacta has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right pars compacta — strict mirror
    with NO warning.** Left and right pars compacta modules are
    **structurally identical** — same **leaf** status, same
    **dopaminergic** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.midbrain.tegmentum.substantia_nigra.left import pars_compacta

Or by fully-qualified path string::

    path = (
        "midbrain.tegmentum.substantia_nigra.left.pars_compacta"
    )

**Do not** assume the pars compacta is the **pars reticulata**.
The **pars reticulata** is the **GABAergic output**; the pars
compacta is the **dopaminergic modulator**.

**Do not** assume the pars compacta is the **ventral tegmental
area**. The **VTA** is the **A10** cell group; the pars compacta
is the **A9** cell group.

**Do not** assume the pars compacta is the **whole substantia
nigra**. The **pars reticulata** is the other component.

**Do not** assume the pars compacta is the **dorsal striatum**.
The striatum is the **target**, not the pars compacta.

**Do not** assume the pars compacta is the **subthalamic nucleus**
or the **globus pallidus**. The **STN** is the
**indirect-pathway driver**; the **pallidum** is **output /
relay**; the pars compacta is the **dopaminergic modulator**.

**Do not** import the **SLEA warning** into the pars compacta.
**The pars compacta is SLEA-FREE** — it is **not** an
extended-amygdala component.

Iterating the pars compacta's (empty) children (recommended
consumer pattern)::

    PARS_COMPACTA_LEFT_CHILDREN = ()
    # The pars compacta is a leaf. The calbindin-rich matrix, the
    # calbindin-poor nigrosomes (including nigrosome-1), and the
    # dorsal / ventral tier subdivisions are prose, not modules.

Reaching the pars reticulata (recommended consumer pattern — the
GABAergic sibling)::

    # The pars reticulata is the GABAERGIC OUTPUT component of the
    # left substantia nigra — functionally parallel to the GPi:
    #
    #   midbrain.tegmentum.substantia_nigra.left.pars_reticulata
    #
    # The pars compacta is the DOPAMINERGIC component; the pars
    # reticulata is the GABAERGIC output.

Reaching the VTA (recommended consumer pattern — the adjacent
dopaminergic sibling)::

    # The VTA is the A10 dopaminergic cell group — mesolimbic /
    # mesocortical, NOT nigrostriatal:
    #
    #   midbrain.tegmentum.ventral_tegmental_area
    #
    # Do not fold the VTA into the pars compacta.

Reaching the dorsal striatum (recommended consumer pattern — the
pars compacta's target)::

    # The dorsal striatum is the TARGET of the nigrostriatal
    # dopaminergic projection from the pars compacta:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left.
    #   subcortical.basal_ganglia.striatum.dorsal_striatum

Reaching the subthalamic nucleus (recommended consumer pattern —
the indirect-pathway driver)::

    # The STN is the glutamatergic indirect-pathway node that
    # drives the SNr/GPi output:
    #
    #   forebrain.diencephalon.subthalamus.subthalamic_nucleus

Reaching the globus pallidus (recommended consumer pattern — the
parallel output)::

    # The GPi is the other basal ganglia output — functionally
    # parallel to the pars reticulata, NOT the pars compacta:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left.
    #   subcortical.basal_ganglia.globus_pallidus

Reaching the SLEA components (recommended consumer pattern — NOTE
the pars compacta is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the pars
    # compacta:
    #
    #   ...medial_temporal_lobe.amygdala.central_nucleus
    #   ...extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   ...basal_ganglia.globus_pallidus.ventral_pallidum
    #   ...basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The pars compacta is SLEA-FREE.

Compartment-level detail (not wired — consult references)::

    # The pars compacta's compartments are prose, not modules:
    #   calbindin-rich matrix   -> dorsal tier, spared in PD
    #   calbindin-poor nigrosomes -> ventrolateral tier, vulnerable in PD
    #   nigrosome-1             -> the most vulnerable nigrosome
    #   dorsal tier             -> matrix component
    #   ventral tier            -> nigrosome component
    #
    # Do not attempt to resolve these as sub-paths of the
    # pars compacta.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        snc_path = (
            f"midbrain.tegmentum.substantia_nigra.{side}."
            f"pars_compacta"
        )
        # resolve snc_path through the memory/recall layer

References
----------
*   **Human substantia nigra anatomy — nigrosomes and matrix:**
    Damier, P., Hirsch, E.C., Agid, Y., Graybiel, A.M. (1999).
    "The substantia nigra of the human brain: I. Nigrosomes and
    the nigral matrix, a compartmental organization based on
    calbindin D28K immunohistochemistry." *Brain* 122:1421–1436.
    (Definitive calbindin-rich matrix vs. calbindin-poor
    nigrosome compartments; nigrosome-1 as the ventrolateral,
    PD-vulnerable subpopulation.)
*   **Parkinson's disease and SNc selectivity:** Fearnley, J.M.,
    Lees, A.J. (1991). "Ageing and Parkinson's disease:
    substantia nigra regional selectivity." *Brain*
    114:2283–2301. (Ventrolateral SNc / putamen-projecting
    neurons are selectively vulnerable.)
*   **Parkinson's disease staging:** Braak, H., et al. (2003).
    "Staging of brain pathology related to sporadic Parkinson's
    disease." *Neurobiology of Aging* 24:197–211. (Lewy body
    pathology and SNc involvement.)
*   **Nigrosome-1 imaging:** Schwarz, S.T., et al. (2014). "The
    'swallow tail' appearance of the healthy nigrosome — a new
    accurate test for Parkinson's disease." *PLoS ONE*
    9:e93814. (Nigrosome-1 signal loss on neuromelanin-sensitive
    MRI as a PD biomarker.)
*   **Neuromelanin:** Zecca, L., et al. (2004). "Neuromelanin of
    the substantia nigra and locus coeruleus: a key to
    Parkinson's disease." *Trends in Neurosciences* 27:397–402.
    (Neuromelanin as the dark pigment and PD biomarker.)
*   **Nigrostriatal system in PD:** Kordower, J.H., et al. (2013).
    "Disease duration and the integrity of the nigrostriatal
    system in Parkinson's disease." *Brain* 136:2419–2431.
    (Nigrostriatal degeneration timeline.)
*   **Dopamine and the basal ganglia:** Haber, S.N. (2014). "The
    place of dopamine in the cortico-basal ganglia circuit."
    *Neuroscience* 282:248–257. (Nigrostriatal dopamine and
    corticostriatal modulation.)
*   **Reward prediction error:** Schultz, W. (1998). "Predictive
    reward signal of dopamine neurons." *Journal of
    Neurophysiology* 80:1–27. (Dopamine reward prediction error —
    SNc/VTA; the SNc/VTA division of labor is contested.)
*   **Dopaminergic cell groups (A8, A9, A10):** Dahlström, A.,
    Fuxe, K. (1964). "Evidence for the existence of monoamine-
    containing neurons in the central nervous system. I.
    Demonstration of monoamines in the cell bodies of brain stem
    neurons." *Acta Physiologica Scandinavica* 62 (Suppl. 232):
    1–55. (The A8/A9/A10 dopaminergic cell-group nomenclature.)
*   **Habit and goal-directed control:** Redgrave, P., et al.
    (2010). "Goal-directed and habitual control in the basal
    ganglia: implications for Parkinson's disease." *Nature
    Reviews Neuroscience* 11:760–772. (SNc/dorsal striatum and
    action control.)
*   **MPTP and the SNc:** Langston, J.W., et al. (1983). "Chronic
    Parkinsonism in humans due to a product of meperidine-analog
    synthesis." *Science* 219:979–980. (MPTP as the
    SNc-selective parkinsonian toxin.)
*   **SLEA (contrast — the pars compacta is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the pars compacta.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Substantia nigra pars compacta in
    overview.)
*   NeuroNames — Substantia nigra pars compacta (left); FMA —
    Substantia nigra pars compacta (left member).
"""