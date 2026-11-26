"""
infrastructure.brainparts.midbrain.tegmentum.substantia_nigra.right
=====================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        └── substantia_nigra
            └── right   <-- THIS MODULE

**Primary synonym:** Right substantia nigra; right SN; right nigra;
right neuromelanin-containing nuclear complex; right A9 dopaminergic
cell group (pars compacta component).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**midbrain nuclear complex** with **two principal parts** —
**pars compacta** (dopaminergic, A9 cell group, neuromelanin-
containing) and **pars reticulata** (GABAergic, basal ganglia
output). A small **pars lateralis** is documented as prose.
**Part of:** The **substantia_nigra** container — the **paired
midbrain dopaminergic/GABAergic nuclear complex** of the
**tegmentum**. The **substantia nigra** sits in the **midbrain
tegmentum**, dorsal to the **crus cerebri** (cerebral peduncle).
**Structural parent:** ``.../substantia_nigra/`` → **direct child**
of the substantia_nigra container.
**Structural children:** **pars_compacta** and **pars_reticulata**
(two) — the **dopaminergic** and **GABAergic** components. The
**pars_lateralis** is documented as **prose**, not as a structural
child.
**Boundary status (NOT the left substantia nigra — strict mirror):**
**Boundary case — the right substantia nigra is the RIGHT member of
a strict-mirror pair.** The **left substantia nigra**
(``.../substantia_nigra/left/``) is the **left** member. The two
sides are **structurally identical** — same nuclear composition,
same **SNc/SNr** division, same **no-warning** status. Consumers
must **not** treat the left and right modules as functionally
distinct unless explicitly documented in the substantia_nigra
container — the lateralization is **subtle, contested, and
clinical-onset-level** (see *Lateralization Notes*).
**Boundary status (NOT the ventral tegmental area — the VTA is the
A10 cell group):** **Boundary case — the substantia nigra is NOT
the ventral tegmental area (VTA).** The **VTA**
(``.../tegmentum/ventral_tegmental_area/``) is the **A10
dopaminergic cell group** — it projects to the **ventral striatum
(nucleus accumbens)**, the **prefrontal cortex**, and the
**amygdala** (mesolimbic / mesocortical pathways). The
**substantia nigra** (here) is the **A9 dopaminergic cell group**
(pars compacta) plus the **GABAergic pars reticulata** — it
projects to the **dorsal striatum** (nigrostriatal pathway) and the
**thalamus / superior colliculus** (SNr output). **They are
DIFFERENT NUCLEI** with **different projection targets** and
**different clinical associations** (SNc → Parkinson's disease;
VTA → reward / addiction / schizophrenia). Consumers must **not**
conflate the two.
**Boundary status (NOT the subthalamic nucleus — the STN is the
indirect-pathway glutamatergic node):** **Boundary case — the
substantia nigra is NOT the subthalamic nucleus.** The
**subthalamic nucleus** (``.../subthalamus/subthalamic_nucleus/``)
is the **glutamatergic** node of the **indirect pathway** — it
**excites** the **SNr/GPi** output. The **substantia nigra**
(here) is the **dopaminergic (SNc)** and **GABAergic (SNr)**
complex. The STN is **upstream** of the SNr (it drives it); the
SNc **modulates** the whole striatal circuit. Consumers must
**not** conflate the two — the **STN** is the **indirect-pathway
driver**; the **SN** is the **dopaminergic modulator (SNc)** and
the **basal ganglia output (SNr)**.
**Boundary status (NOT the globus pallidus — GPi is the other basal
ganglia output):** **Boundary case — the SNr is functionally
analogous to, but distinct from, the internal globus pallidus
(GPi).** The **GPi**
(``.../basal_ganglia/globus_pallidus/``) is the **other** basal
ganglia output nucleus — it projects to the **thalamus (VA/VL)**
via the **ans lenticularis / thalamic fasciculus**. The **SNr**
(here, as part of the substantia nigra) projects to the
**thalamus (VA/VL, mediodorsal)** and to the **superior colliculus**
(saccades). The two are **functionally parallel** but
**anatomically distinct** — same output role, different nucleus,
different projection fascicles. Consumers must **not** conflate the
SNr with the GPi — they are **parallel outputs**, not the same
structure.
**Boundary status (NOT the red nucleus — the red nucleus is the
adjacent rubrospinal / rubro-olivary tegmentum neighbor):**
**Boundary case — the substantia nigra is NOT the red nucleus.**
The **red nucleus** (``.../tegmentum/red_nucleus/``) is the
**rubrospinal / rubro-olivary** motor nucleus of the **midbrain
tegmentum** — it is **adjacent** to the substantia nigra but
**functionally separate**. Consumers must **not** conflate the two
— the **red nucleus** is a **motor relay**; the **substantia
nigra** is the **dopaminergic/GABAergic basal ganglia complex**.
**Boundary status (NOT the crus cerebri / cerebral peduncle — the
crus cerebri is the white-matter tract ventral to the SN):**
**Boundary case — the substantia nigra is NOT the crus cerebri.**
The **crus cerebri** (cerebral peduncle, ``.../midbrain/crus_cerebri/``
if wired) is the **white-matter tract** — the **corticospinal,
corticobulbar, and corticopontine fibers** — that lies **ventral**
to the substantia nigra. The substantia nigra is the **grey-matter
nucleus** dorsal to it. Consumers must **not** conflate the
**nucleus** with the **fiber tract** that forms its ventral
boundary.
**Boundary status (NOT the retrorubral area / A8 — the A8 group is
a separate dopaminergic cell group):** **Boundary case — the
substantia nigra is NOT the retrorubral area (A8).** The
**retrorubral area** is the **A8 dopaminergic cell group** — it is
**caudal and dorsolateral** to the SNc and is **sometimes grouped
with the SN/VTA dopaminergic complex** in the literature. In this
tree it is a **separate structure** (wired elsewhere). Consumers
must **not** silently fold A8 into the substantia nigra.
**Boundary status (NOT the whole midbrain tegmentum — the
tegmentum contains many other nuclei):** **Boundary case — the
substantia nigra is one nuclear complex within the midbrain
tegmentum, not the tegmentum itself.** The **tegmentum**
(``.../midbrain/tegmentum/``) contains the **red nucleus**, the
**VTA**, the **periaqueductal gray**, the **oculomotor and
trochlear nuclei**, the **reticular formation**, and others. The
substantia nigra is **one** of them. Consumers must **not**
conflate the nucleus with its containing region.
**Boundary status (NOT the dorsal striatum — the striatum is the
SNc's target):** **Boundary case — the substantia nigra is NOT the
dorsal striatum.** The **dorsal striatum** (caudate + putamen,
``.../basal_ganglia/striatum/dorsal_striatum/``) is the **target**
of the **nigrostriatal dopaminergic projection** from the SNc. The
SNc **sends** dopamine to the striatum; the striatum **receives**
it. Consumers must **not** conflate the **source** (SNc) with the
**target** (dorsal striatum).
**Boundary status (NOT a SLEA component — the substantia nigra is
outside the extended amygdala):** **Boundary case — the
substantia nigra is SLEA-FREE.** The **SLEA continuum** includes
the **central nucleus** (amygdala), the **BNST**, the **ventral
pallidum**, and the **nucleus accumbens**. The substantia nigra is
**not** part of it, and it carries **no SLEA warning**. Consumers
must **not** import the SLEA warning into the substantia nigra.

Overview
--------
The right substantia nigra is the **right member of the paired
midbrain substantia nigra** — a **dopaminergic (pars compacta,
A9)** and **GABAergic (pars reticulata)** nuclear complex in the
**midbrain tegmentum**, dorsal to the **crus cerebri**. It is the
**nigrostriatal dopaminergic source** (SNc → dorsal striatum) and
the **basal ganglia output nucleus** functionally parallel to the
GPi (SNr → thalamus / superior colliculus).

**The substantia nigra is a paired structure.** Each hemisphere has
its own substantia nigra, with **ipsilateral** projections. The
two sides are **bilaterally symmetric** and, for structural
purposes, **functionally symmetric** — the lateralization is
**subtle and clinical-onset-level** (see *Lateralization Notes*).

**The substantia nigra is a two-part complex, not a single uniform
nucleus.** The **pars compacta** (dopaminergic, neuromelanin-
containing) and the **pars reticulata** (GABAergic, output) are
**functionally distinct** — wired here as **structural children**
(pars_compacta, pars_reticulata). The **pars lateralis** is
**prose**, not a structural child. Consumers must **not** treat
the substantia nigra as a single uniform dopaminergic nucleus —
the **GABAergic pars reticulata** is functionally as important as
the **dopaminergic pars compacta**.

**The substantia nigra is SLEA-FREE and NOT the VTA.** It is a
**midbrain basal ganglia nucleus** — not an extended-amygdala
component, and not the **A10 ventral tegmental area**.

Nuclear Composition
-------------------
The right substantia nigra contains **two principal structural
children** plus prose-level detail:

*   **pars_compacta** (``.../substantia_nigra/right/pars_compacta/``)
    — the **dopaminergic** component. **A9 cell group.**
    **Neuromelanin-containing** (the dark pigment that gives the
    substantia nigra its name — "black substance"). Projects to
    the **dorsal striatum** (caudate + putamen) via the
    **nigrostriatal pathway**. The **canonical Parkinson's
    disease** substrate.

*   **pars_reticulata** (``.../substantia_nigra/right/pars_reticulata/``)
    — the **GABAergic** component. **Basal ganglia output
    nucleus**, functionally **parallel to the GPi**. Projects to
    the **thalamus (VA/VL, mediodorsal)** and to the **superior
    colliculus** (saccadic eye movements). Receives **striatal**
    and **subthalamic** input. **Not** neuromelanin-containing.

*   **pars_lateralis** — **prose**, not a structural child. A
    small **dopaminergic** subdivision, sometimes distinguished
    from the SNc proper.

*   **Dopaminergic neurons embedded in the SNr** — **prose**. A
    small population of **dopaminergic** neurons is found within
    the SNr; this is documented as prose, not as a separate
    structural child.

Function in the Human Brain
---------------------------
The substantia nigra's functions are **dopaminergic modulation**
(SNc) and **basal ganglia output** (SNr):

*   **Nigrostriatal Dopamine (SNc → Dorsal Striatum):** The **SNc**
    **projects** to the **dorsal striatum** (caudate + putamen) and
    **modulates** the **corticostriatal** input via **D1**
    (direct-pathway, facilitatory) and **D2** (indirect-pathway,
    inhibitory) receptors. This is the **neural substrate** of
    **action selection**, **habit learning**, **motor vigor**, and
    (in the influential but contested **Schultz** framing) the
    **reward prediction error** signal — though the **VTA** is the
    more commonly cited reward/learning source, and the
    **SNc/VTA division of labor** is **contested**.

*   **Basal Ganglia Output (SNr → Thalamus):** The **SNr** is a
    **tonically active GABAergic output nucleus** — it **inhibits**
    the **thalamus (VA/VL)** and is **inhibited** by the
    **direct-pathway striatum** and **excited** by the
    **indirect-pathway subthalamic nucleus**. It is the **SNr
    analogue of the GPi** — **parallel basal ganglia output**.

*   **Saccadic Eye Movements (SNr → Superior Colliculus):** The
    **SNr** **inhibits** the **superior colliculus** — releasing
    it to generate **saccades**. This is the **basal ganglia
    control of orienting eye movements** (Hikosaka).

*   **Motor Vigor and Action Selection:** Via the **nigrostriatal**
    projection to the **dorsal striatum**, the SNc **modulates
    movement vigor, action initiation, and action selection** —
    the **motor** functions classically lost in **Parkinson's
    disease**.

*   **NOT a cortical processor, NOT a limbic reward nucleus in the
    narrow sense.** The substantia nigra is a **midbrain basal
    ganglia nucleus** — its functions are **motor / action
    selection (SNc → dorsal striatum; SNr → thalamus/SC)**. The
    **reward / limbic** functions are primarily the **VTA's**
    (mesolimbic / mesocortical); the SNc's role in reward is
    **contested and secondary**.

Associated Disorders
--------------------
The substantia nigra has **strong, named clinical associations** —
unlike the cortical-region modules, this is a **canonical disease
substrate**:

*   **Parkinson's Disease (SNc Dopamine Neuron Loss — the
    canonical association):** **Selective degeneration** of the
    **SNc dopaminergic neurons** (especially the **ventrolateral
    tier** projecting to the **putamen**) is the **defining
    neuropathology** of **Parkinson's disease**. **Neuromelanin**
    loss on **MRI** (neuromelanin-sensitive imaging) is used as an
    **in vivo biomarker**. **Lewy bodies** (α-synuclein) form in
    the surviving SNc neurons (Braak staging). This is the
    **most important clinical association** of the substantia
    nigra.

*   **Parkinson-Plus Syndromes (SNc + SNr + beyond):** **Progressive
    supranuclear palsy (PSP)** involves **SNc and SNr** degeneration
    (tauopathy) — with **SNr** involvement contributing to the
    **supranuclear gaze palsy**. **Multiple system atrophy (MSA)**
    and **corticobasal degeneration (CBD)** also involve the
    substantia nigra. Consumers must **not** attribute all
    parkinsonism to **SNc alone** — the **SNr** and the **wider
    basal ganglia** are involved in the plus syndromes.

*   **MPTP Toxicity (SNc-Selective Toxin):** **MPTP** (via its
    metabolite **MPP+**) is **selectively toxic** to **SNc
    dopaminergic neurons** — it produces an **acute parkinsonian
    syndrome** and is the **canonical experimental model** of
    Parkinson's disease. It is **SNc-selective**, which is part of
    why the SNc is the **Parkinson's substrate**.

*   **Schizophrenia (Dopamine Hypothesis — mostly VTA/Ventral
    Striatum):** The **dopamine hypothesis** of schizophrenia
    centers on **mesolimbic / mesocortical** dopamine (VTA
    projections) — but **SNc / nigrostriatal** dopamine is
    **implicated** in **antipsychotic-induced extrapyramidal
    symptoms** (D2 blockade in the **dorsal striatum**). Consumers
    must **not** attribute schizophrenia's **positive symptoms**
    to the SNc — that is the **VTA / ventral striatum** story;
    the SNc is the **EPS / motor side-effect** story.

*   **Restless Legs Syndrome (Iron / Neuromelanin):** **Iron
    deficiency** in the substantia nigra (and **neuromelanin**
    changes) is associated with **restless legs syndrome** —
    documented, but **mechanistically contested**.

*   **Wilson's Disease and Manganese Toxicity:** **Copper**
    (Wilson's) and **manganese** (welding, hepatic
    encephalopathy) accumulate in the **basal ganglia**, including
    the substantia nigra — producing **parkinsonism** and **MRI
    T1 hyperintensity**. Documented, but **not SNc-selective** in
    the way Parkinson's is.

**What is NOT here:** The substantia nigra is **not** the substrate
for **Huntington's disease** (striatum — caudate/putamen),
**Kluver-Bucy syndrome** (amygdala), **Alzheimer's disease**
(hippocampus, nucleus basalis), or **addiction** (VTA / nucleus
accumbens). Its clinical relevance is **nigrostriatal /
nigrothalamic / nigrotectal** — **motor, action selection, and
saccades** — with **Parkinson's disease** as the **canonical**
association.

Lateralization Notes
--------------------
This is the **right** substantia nigra module. The substantia nigra
is **bilaterally symmetric** — and it carries **NO warning**:

*   **Bilateral Symmetry:** Each hemisphere has its own substantia
    nigra, with **ipsilateral** projections. The two sides are
    **structurally identical** — same **SNc/SNr** composition,
    same **nigrostriatal / nigrothalamic / nigrotectal** targets.

*   **Clinical Asymmetry (PD Onset — contested at the structural
    level):** **Parkinson's disease** often presents with
    **asymmetric motor symptoms** (one side first) — but this is
    **clinical-onset asymmetry**, and the **structural
    lateralization** of the SNc is **subtle and contested**. It is
    documented in the **substantia_nigra container**, not at the
    **right** module level, and it is **NOT a warning**.

*   **NO Warning of their own:** The right substantia nigra is a
    **strict-mirror pair with NO warning** — **no SLEA warning**,
    **no extended-amygdala warning**, **no rhinencephalon-
    exclusion flag**. Consumers must **not** import any of those
    warnings into the substantia nigra.

**A consumer that assumes "right substantia nigra = left substantia
nigra" will be structurally correct** — the two sides are
**symmetric**. The clinical-onset asymmetry in Parkinson's is a
**container-level / clinical** note, not a **module-level**
warning.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../substantia_nigra/left/``, ``.../tegmentum/
    ventral_tegmental_area/``, ``.../tegmentum/red_nucleus/``,
    ``.../subthalamus/subthalamic_nucleus/``, ``.../basal_ganglia/
    globus_pallidus/``, ``.../basal_ganglia/striatum/
    dorsal_striatum/``, or any other container. The substantia
    nigra's relationships to the VTA, STN, GPi, dorsal striatum,
    red nucleus, and crus cerebri are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are** ``pars_compacta``
    and ``pars_reticulata``. The **pars_lateralis** and the
    **dopaminergic neurons embedded in the SNr** are **prose**, not
    sub-modules.
*   **TWO-PART COMPLEX — NOT a single uniform nucleus.** The **SNc**
    (dopaminergic) and the **SNr** (GABAergic) are **functionally
    distinct**; consumers must **not** treat the substantia nigra
    as a single dopaminergic nucleus.
*   **NOT the VTA.** The VTA is the **A10** cell group; the
    substantia nigra is the **A9** (SNc) + **GABAergic** (SNr)
    complex.
*   **NOT the subthalamic nucleus.** The STN is the
    **indirect-pathway glutamatergic** driver; the SN is the
    **dopaminergic modulator (SNc)** and **output (SNr)**.
*   **NOT the globus pallidus.** The **SNr** is **functionally
    parallel to the GPi**, not the same structure.
*   **NOT the crus cerebri.** The crus cerebri is the
    **white-matter tract** ventral to the SN; the SN is the
    **grey-matter nucleus**.
*   **NOT the red nucleus.** The red nucleus is the **adjacent
    rubrospinal / rubro-olivary motor relay**.
*   **NOT the retrorubral area (A8).** The A8 group is **caudal
    and dorsolateral** — a **separate structure**.
*   **NOT the whole midbrain tegmentum.** The tegmentum contains
    many other nuclei.
*   **NOT the dorsal striatum.** The striatum is the **SNc's
    target**, not the SN itself.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    substantia nigra is **not** an extended-amygdala component.
*   **Structural parity with left substantia nigra — strict mirror
    with NO warning.** Right and left substantia nigra modules are
    **structurally identical** — same **container** status, same
    **SNc/SNr** children, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.midbrain.tegmentum.substantia_nigra import right

Or by fully-qualified path string::

    path = (
        "midbrain.tegmentum.substantia_nigra.right"
    )

**Do not** assume the substantia nigra is the **ventral tegmental
area**. The **VTA** is the **A10** cell group (mesolimbic /
mesocortical); the **substantia nigra** is the **A9 (SNc)** +
**GABAergic (SNr)** complex (nigrostriatal / nigrothalamic /
nigrotectal).

**Do not** assume the substantia nigra is the **subthalamic
nucleus**. The **STN** is the **indirect-pathway glutamatergic**
driver; the **SN** is the **dopaminergic modulator (SNc)** and
**basal ganglia output (SNr)**.

**Do not** assume the **SNr** is the **GPi**. They are
**functionally parallel** basal ganglia outputs — **different
nuclei, different projection fascicles**.

**Do not** assume the substantia nigra is the **crus cerebri** or
the **red nucleus**. The **crus cerebri** is the **white-matter
tract** ventral to the SN; the **red nucleus** is the **adjacent
rubrospinal / rubro-olivary motor relay**.

**Do not** import the **SLEA warning** into the substantia nigra.
**The substantia nigra is SLEA-FREE** — it is **not** an
extended-amygdala component.

Iterating the substantia nigra's structural children (recommended
consumer pattern)::

    SUBSTANTIA_NIGRA_RIGHT_CHILDREN = (
        "pars_compacta",
        "pars_reticulata",
    )
    # pars_lateralis and the dopaminergic neurons embedded in the
    # SNr are prose, not modules.

Reaching the pars compacta (recommended consumer pattern — the
dopaminergic component)::

    # The pars compacta is the DOPAMINERGIC / A9 component —
    # neuromelanin-containing, projecting to the dorsal striatum:
    #
    #   midbrain.tegmentum.substantia_nigra.right.pars_compacta
    #
    # The canonical Parkinson's disease substrate.

Reaching the pars reticulata (recommended consumer pattern — the
GABAergic output)::

    # The pars reticulata is the GABAERGIC OUTPUT component —
    # functionally parallel to the GPi, projecting to the thalamus
    # and superior colliculus:
    #
    #   midbrain.tegmentum.substantia_nigra.right.pars_reticulata

Reaching the VTA (recommended consumer pattern — the adjacent
dopaminergic sibling)::

    # The VTA is the A10 dopaminergic cell group — mesolimbic /
    # mesocortical, NOT nigrostriatal:
    #
    #   midbrain.tegmentum.ventral_tegmental_area
    #
    # Do not fold the VTA into the substantia nigra.

Reaching the subthalamic nucleus (recommended consumer pattern —
the indirect-pathway driver)::

    # The STN is the glutamatergic indirect-pathway node that
    # drives the SNr/GPi output:
    #
    #   forebrain.diencephalon.subthalamus.subthalamic_nucleus

Reaching the globus pallidus (recommended consumer pattern — the
parallel output)::

    # The GPi is the other basal ganglia output — functionally
    # parallel to the SNr:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.right.
    #   subcortical.basal_ganglia.globus_pallidus

Reaching the dorsal striatum (recommended consumer pattern — the
SNc's target)::

    # The dorsal striatum is the TARGET of the nigrostriatal
    # dopaminergic projection:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.right.
    #   subcortical.basal_ganglia.striatum.dorsal_striatum

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        sn_path = (
            f"midbrain.tegmentum.substantia_nigra.{side}"
        )
        # resolve sn_path through the memory/recall layer

References
----------
*   **Basal ganglia circuits:** Alexander, G.E., Crutcher, M.D.
    (1990). "Functional architecture of basal ganglia circuits:
    neural substrates of parallel processing." *Trends in
    Neurosciences* 13:266–271. (Direct / indirect / hyperdirect
    pathways; SNr as output.)
*   **Basal ganglia anatomy:** Parent, A., Hazrati, L.N. (1995).
    "Functional anatomy of the basal ganglia. I. The cortico-basal
    ganglia-thalamo-cortical loop." *Brain Research Reviews*
    20:91–127. (SNc/SNr composition; striatal and pallidal
    connections.)
*   **Dopamine and the basal ganglia:** Haber, S.N. (2014). "The
    place of dopamine in the cortico-basal ganglia circuit."
    *Neuroscience* 282:248–257. (Nigrostriatal dopamine and
    corticostriatal modulation.)
*   **Reward prediction error:** Schultz, W. (1998). "Predictive
    reward signal of dopamine neurons." *Journal of
    Neurophysiology* 80:1–27. (Dopamine reward prediction error —
    SNc/VTA; the SNc/VTA division of labor is contested.)
*   **Human substantia nigra anatomy:** Damier, P., Hirsch, E.C.,
    Agid, Y., Graybiel, A.M. (1999). "The substantia nigra of the
    human brain: I. Nigrosomes and the nigral matrix, a
    compartmental organization based on calbindin D28K
    immunohistochemistry." *Brain* 122:1421–1436. (SNc/SNr
    compartments; neuromelanin.)
*   **Parkinson's disease and SNc selectivity:** Fearnley, J.M.,
    Lees, A.J. (1991). "Ageing and Parkinson's disease:
    substantia nigra regional selectivity." *Brain*
    114:2283–2301. (Ventrolateral SNc / putamen-projecting neurons
    are selectively vulnerable.)
*   **Parkinson's disease staging:** Braak, H., et al. (2003).
    "Staging of brain pathology related to sporadic Parkinson's
    disease." *Neurobiology of Aging* 24:197–211. (Lewy body
    pathology and SNc involvement.)
*   **Neuromelanin:** Zecca, L., et al. (2004). "Neuromelanin of
    the substantia nigra and locus coeruleus: a key to
    Parkinson's disease." *Trends in Neurosciences* 27:397–402.
    (Neuromelanin as the dark pigment and PD biomarker.)
*   **Nigrostriatal system in PD:** Kordower, J.H., et al. (2013).
    "Disease duration and the integrity of the nigrostriatal
    system in Parkinson's disease." *Brain* 136:2419–2431.
    (Nigrostriatal degeneration timeline.)
*   **Saccades and the SNr:** Hikosaka, O., et al. (2000). "Role of
    the basal ganglia in the control of purposive saccadic eye
    movements." *Physiological Reviews* 80:953–978. (SNr →
    superior colliculus and saccade control.)
*   **Subthalamic nucleus:** Joel, D., Weiner, I. (1997). "The
    connections of the primate subthalamic nucleus: indirect
    pathways and the open-interconnected scheme of basal ganglia-
    thalamo-cortical circuitry." *Brain Research Reviews*
    23:62–78. (STN as indirect-pathway driver of SNr/GPi.)
*   **Habit and goal-directed control:** Redgrave, P., et al.
    (2010). "Goal-directed and habitual control in the basal
    ganglia: implications for Parkinson's disease." *Nature
    Reviews Neuroscience* 11:760–772. (SNc/dorsal striatum and
    action control.)
*   **SLEA (contrast — the substantia nigra is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the substantia nigra.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Substantia nigra in overview.)
*   NeuroNames — Substantia nigra (right); FMA — Substantia nigra
    (right member).
"""