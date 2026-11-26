"""
infrastructure.brainparts.midbrain.tegmentum.substantia_nigra.right.pars_reticulata
=====================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        └── substantia_nigra
            └── right
                └── pars_reticulata   <-- THIS MODULE

**Primary synonym:** Pars reticulata of the right substantia nigra;
right SNr; right substantia nigra pars reticulata; right nigrothalamic /
nigrotectal output nucleus; right basal ganglia output component;
"the substantia nigra's pale output component."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**GABAergic nuclear subdivision** — the **basal ganglia output
nucleus** of the midbrain tegmentum, **functionally parallel to the
internal globus pallidus (GPi)**. **Not neuromelanin-containing**
(the SNr is **pale** — the dark pigment belongs to the pars
compacta). The **dorsal vs. ventral** and **medial vs. lateral**
subdivisions, and the **nigrothalamic vs. nigrotectal** output
populations, are documented as **prose**, not as structural
children.
**Part of:** The **substantia_nigra** container — specifically, the
**GABAergic** component (**with the pars_compacta as its
dopaminergic sibling**). The **substantia nigra** sits in the
**midbrain tegmentum**, dorsal to the **crus cerebri**.
**Structural parent:** ``.../substantia_nigra/right/`` → **direct
child** of the right substantia nigra.
**Structural children:** **None.** This is a **leaf** module. The
**dorsal vs. ventral** tier, the **medial vs. lateral** division,
the **nigrothalamic** (medial/dorsal) and **nigrotectal**
(lateral/ventral) output populations, and the **parvalbumin-
containing** GABAergic neurons are documented as **prose**, not as
structural children.
**Boundary status (NOT the pars compacta — that is the dopaminergic
sibling):** **Boundary case — the pars reticulata is NOT the pars
compacta.** The **pars compacta**
(``.../substantia_nigra/right/pars_compacta/``) is the
**dopaminergic** component — the **A9 cell group**,
**neuromelanin-containing**, projecting to the **dorsal striatum**
via the **nigrostriatal pathway**. The **pars reticulata** (here)
is the **GABAergic** component — the **basal ganglia output
nucleus**, functionally parallel to the **GPi**, projecting to the
**thalamus** and **superior colliculus**. **They are DIFFERENT
SUBDIVISIONS** with **different neurotransmitters**, **different
projection targets**, and **different clinical associations**
(SNc → Parkinson's disease; SNr → progressive supranuclear palsy /
saccadic control). Consumers must **not** conflate the two — the
**pars reticulata** is the **GABAergic output**; the **pars
compacta** is the **dopaminergic modulator**.
**Boundary status (NOT the globus pallidus — GPi is the functionally
parallel output):** **Boundary case — the pars reticulata is
functionally analogous to, but distinct from, the internal globus
pallidus (GPi).** The **GPi**
(``.../basal_ganglia/globus_pallidus/``) is the **other** basal
ganglia output nucleus — it projects to the **thalamus (VA/VL)**
via the **ans lenticularis / thalamic fasciculus**. The **SNr**
(here) projects to the **thalamus (VA/VL, mediodorsal)** and to the
**superior colliculus** (saccades) via the **nigrothalamic** and
**nigrotectal** tracts. The two are **functionally parallel** but
**anatomically distinct** — same output role, different nucleus,
different projection fascicles, different embryological origin
(SNr is **midbrain**; GPi is **telencephalic**). Consumers must
**not** conflate the SNr with the GPi — they are **parallel
outputs**, not the same structure.
**Boundary status (NOT the subthalamic nucleus — the STN is the
indirect-pathway glutamatergic INPUT to the SNr):** **Boundary
case — the pars reticulata is NOT the subthalamic nucleus.** The
**subthalamic nucleus** (``.../subthalamus/subthalamic_nucleus/``)
is the **glutamatergic** node of the **indirect pathway** — it
**excites** the **SNr/GPi** output. The **pars reticulata** (here)
is the **GABAergic output nucleus** that the STN **drives**. The
STN is **upstream** of the SNr (it excites it); the SNr is
**downstream** (it inhibits the thalamus / SC). Consumers must
**not** conflate the two — the **STN** is the **indirect-pathway
driver**; the **SNr** is the **basal ganglia output**.
**Boundary status (NOT the ventral tegmental area — the VTA is the
A10 dopaminergic cell group):** **Boundary case — the pars
reticulata is NOT the ventral tegmental area (VTA).** The **VTA**
(``.../tegmentum/ventral_tegmental_area/``) is the **A10
dopaminergic cell group** — it projects to the **ventral striatum
(nucleus accumbens)**, the **prefrontal cortex**, and the
**amygdala** (mesolimbic / mesocortical pathways). The **pars
reticulata** (here) is the **GABAergic output** — it projects to
the **thalamus** and **superior colliculus**. **They are
DIFFERENT NUCLEI** with **different neurotransmitters** and
**different projection targets** (VTA → limbic / cortical
dopamine; SNr → thalamic / tectal GABA). Consumers must **not**
conflate the two.
**Boundary status (NOT the retrorubral area / A8 — the A8 group is
a separate dopaminergic cell group):** **Boundary case — the pars
reticulata is NOT the retrorubral area (A8).** The **retrorubral
area** is the **A8 dopaminergic cell group** — it is **caudal and
dorsolateral** to the SNc and is **sometimes grouped with the
SN/VTA dopaminergic complex** in the literature. It is
**dopaminergic**, not GABAergic, and it is a **separate
structure** (wired elsewhere). Consumers must **not** silently
fold A8 into the pars reticulata.
**Boundary status (NOT the whole substantia nigra — the pars
compacta is the other component):** **Boundary case — the pars
reticulata is a COMPONENT of the substantia nigra, not the whole
substantia nigra.** The **substantia nigra**
(``.../substantia_nigra/right/``) container holds **both**
**pars_compacta** (dopaminergic) and **pars_reticulata** (here,
GABAergic). Consumers must **not** treat "substantia nigra" and
"pars reticulata" as synonyms — the pars reticulata is the
**GABAergic output**; the substantia nigra also contains the
**dopaminergic modulator**.
**Boundary status (NOT the dorsal striatum — the striatum is the
SNr's INPUT source):** **Boundary case — the pars reticulata is
NOT the dorsal striatum.** The **dorsal striatum** (caudate +
putamen, ``.../basal_ganglia/striatum/dorsal_striatum/``) is the
**primary input** to the SNr — the **direct-pathway** striatal
MSNs (D1) **inhibit** the SNr. The SNr **receives** striatal
inhibition and **sends** GABAergic inhibition to the thalamus /
SC. Consumers must **not** conflate the **input** (dorsal
striatum) with the **output** (SNr) — they are **opposite ends**
of the basal ganglia circuit.
**Boundary status (NOT the thalamus — the thalamus is the SNr's
OUTPUT target):** **Boundary case — the pars reticulata is NOT the
thalamus.** The **thalamus** (``.../diencephalon/thalamus/``) is
the **primary output target** of the **nigrothalamic** projection
— the SNr **inhibits** the **VA/VL** and **mediodorsal** thalamic
nuclei. The SNr is the **source**; the thalamus is the **target**.
Consumers must **not** conflate the **source** (SNr) with the
**target** (thalamus).
**Boundary status (NOT the superior colliculus — the SC is the
SNr's tectal OUTPUT target):** **Boundary case — the pars
reticulata is NOT the superior colliculus.** The **superior
colliculus** (``.../midbrain/tectum/superior_colliculus/``) is the
**tectal output target** of the **nigrotectal** projection — the
SNr **inhibits** the SC to **gate saccadic eye movements**. The
SNr is the **source**; the SC is the **target**. Consumers must
**not** conflate the **source** (SNr) with the **target** (SC).
**Boundary status (NOT the red nucleus — the red nucleus is the
adjacent rubrospinal / rubro-olivary tegmentum neighbor):**
**Boundary case — the pars reticulata is NOT the red nucleus.**
The **red nucleus** (``.../tegmentum/red_nucleus/``) is the
**rubrospinal / rubro-olivary** motor nucleus of the **midbrain
tegmentum** — it is **adjacent** to the substantia nigra but
**functionally separate**. Consumers must **not** conflate the two
— the **red nucleus** is a **motor relay**; the **pars
reticulata** is the **basal ganglia GABAergic output**.
**Boundary status (NOT the crus cerebri / cerebral peduncle — the
crus cerebri is the white-matter tract ventral to the SN):**
**Boundary case — the pars reticulata is NOT the crus cerebri.**
The **crus cerebri** (cerebral peduncle, ``.../midbrain/
crus_cerebri/`` if wired) is the **white-matter tract** — the
**corticospinal, corticobulbar, and corticopontine fibers** — that
lies **ventral** to the substantia nigra. The pars reticulata is
**grey-matter nucleus** dorsal to it. Consumers must **not**
conflate the **nucleus** with the **fiber tract** that forms its
ventral boundary.
**Boundary status (NOT the pars lateralis — that is a prose
subdivision of the substantia nigra):** **Boundary case — the
pars reticulata is NOT the pars lateralis.** The **pars
lateralis** is a **small dopaminergic subdivision** of the
substantia nigra, documented as **prose** under the
substantia_nigra container (not as a structural child of either
pars_compacta or pars_reticulata). Consumers must **not** fold the
pars lateralis into the pars reticulata — it is a **separate
prose-level** subdivision.
**Boundary status (NOT the dopaminergic neurons embedded in the
pars reticulata — those are PROSE, not the pars compacta):**
**Boundary case — the pars reticulata is NOT the dopaminergic
neurons embedded within it.** A small population of
**dopaminergic** neurons is found **within the pars reticulata** —
these are documented as **pars reticulata prose**, not as part of
the **pars compacta**. Consumers must **not** fold the
**SNr-embedded dopaminergic** neurons into the pars compacta —
they are a **distinct, prose-level** population. Conversely,
consumers must **not** treat the pars reticulata as **purely
GABAergic** — it is **predominantly GABAergic** with a **minor
dopaminergic** component documented as prose.
**Boundary status (NOT a single uniform GABAergic population —
MULTIPLE output populations with DIFFERENT targets):** **Boundary
case — the pars reticulata is HETEROGENEOUS, not a single uniform
GABAergic population.** The pars reticulata includes:
*   **Nigrothalamic neurons** (medial / dorsal) — projecting to
    the **VA/VL** and **mediodorsal** thalamus; the
    **skeletomotor / associative** output.
*   **Nigrotectal neurons** (lateral / ventral) — projecting to
    the **superior colliculus**; the **saccadic** output.
*   **Nigroreticular neurons** — projecting to the **brainstem
    reticular formation**; the **orienting / postural** output.
**Each output population is functionally distinct** — the tree
wires them as **prose** under the pars_reticulata leaf, not as
structural children. Consumers must **not** treat the pars
reticulata as a single uniform output nucleus — it is a
**heterogeneous GABAergic output complex** with **segregated
output channels**.
**Boundary status (NOT a SLEA component — the pars reticulata is
outside the extended amygdala):** **Boundary case — the pars
reticulata is SLEA-FREE.** The **SLEA continuum** includes the
**central nucleus** (amygdala), the **BNST**, the **ventral
pallidum**, and the **nucleus accumbens**. The pars reticulata is
**not** part of it, and it carries **no SLEA warning**. Consumers
must **not** import the SLEA warning into the pars reticulata.

Overview
--------
The right pars reticulata is the **GABAergic output component** of
the **right substantia nigra** — the **basal ganglia output
nucleus** functionally parallel to the **GPi**, projecting to the
**thalamus (VA/VL, mediodorsal)** and the **superior colliculus**.
It is a **leaf** module under the right substantia nigra, and it is
the **midbrain output substrate** of **basal ganglia gating** of
**movement** and **saccades**.

**The pars reticulata is the GABAERGIC component, NOT the
dopaminergic pars compacta.** The **pars compacta**
(``.../substantia_nigra/right/pars_compacta/``) is the
**dopaminergic modulator** — the A9 cell group projecting to the
dorsal striatum. The **pars reticulata** (here) is the **GABAergic
output** — the basal ganglia output nucleus functionally parallel
to the GPi. **They are DIFFERENT SUBDIVISIONS** with **different
neurotransmitters** and **different projection targets**.

**The pars reticulata is functionally parallel to, but distinct
from, the GPi.** The **GPi** is the **telencephalic** basal
ganglia output; the **SNr** is the **midbrain** basal ganglia
output. They share **output targets** (thalamus VA/VL) and
**input logic** (direct-pathway striatal inhibition, indirect-
pathway STN excitation), but they are **anatomically distinct**
nuclei with **different embryological origins** and **different
projection fascicles**. Consumers must **not** treat the SNr and
GPi as the same structure — they are **parallel outputs**.

**The pars reticulata is NOT the ventral tegmental area.** The
**VTA** is the **A10 dopaminergic** cell group — mesolimbic /
mesocortical. The **pars reticulata** is the **GABAergic output**
— nigrothalamic / nigrotectal. The two are **different nuclei**
with **different neurotransmitters** and **different clinical
associations**.

**The pars reticulata is a HETEROGENEOUS GABAergic output complex,
not a single uniform population.** The **nigrothalamic**
(medial/dorsal), **nigrotectal** (lateral/ventral), and
**nigroreticular** output populations are **functionally
distinct** subpopulations — wired as **prose**, not structural
children. Consumers must **not** treat the pars reticulata as a
single uniform output nucleus.

**The pars reticulata is a paired structure.** Each hemisphere has
its own pars reticulata, with **ipsilateral** projections. The two
sides are **bilaterally symmetric** — the lateralization is
**subtle and clinical-onset-level** (see *Lateralization Notes*).

**The pars reticulata is SLEA-FREE.** It is a **midbrain
GABAergic output nucleus** — not an extended-amygdala component,
and not a limbic reward nucleus. It is the **basal ganglia
output** — a **motor / saccadic / orienting** structure.

Subregional Composition (prose, not structural children)
--------------------------------------------------------
The pars reticulata is a **heterogeneous GABAergic output complex**
— documented as **prose**, not as structural children:

*   **Nigrothalamic neurons** — the **medial / dorsal**
    subpopulation. Project to the **VA/VL** and **mediodorsal**
    thalamus. Subserve the **skeletomotor / associative** output
    — the **basal ganglia gating** of **movement** and
    **cognitive-motor** behavior.

*   **Nigrotectal neurons** — the **lateral / ventral**
    subpopulation. Project to the **superior colliculus**.
    Subserve the **saccadic** output — the **basal ganglia gating**
    of **orienting eye movements** (Hikosaka).

*   **Nigroreticular neurons** — project to the **brainstem
    reticular formation**. Subserve the **orienting / postural**
    output.

*   **Parvalbumin-containing GABAergic neurons** — the **dominant
    neurochemical marker** of the SNr (parvalbumin-positive
    GABAergic neurons). **Not** a structural subdivision — a
    **histochemical property** of most pars reticulata neurons.

*   **Dopaminergic neurons embedded in the SNr** — a small
    **dopaminergic** population **within the pars reticulata**.
    Documented as **prose**, **not** as part of the pars
    compacta.

*   **Dorsal vs. ventral tier** — a **prose-level** subdivision
    sometimes distinguished for the **nigrothalamic** vs.
    **nigrotectal** projection topography (dorsal → thalamus;
    ventral → tectum).

**These subregions are prose, not structural children.** The tree
wires the **pars_reticulata** as a **single leaf** under the right
substantia nigra — the **nigrothalamic**, **nigrotectal**,
**nigroreticular** populations, the **parvalbumin** marker, and
the **dorsal / ventral** tiers are **prose**, not structural
children. Consumers that need **output-channel-level** resolution
should consult the references (Hikosaka et al., 2000; Parent &
Hazrati, 1995), not the tree.

Function in the Human Brain
---------------------------
The pars reticulata's functions are **GABAergic basal ganglia
output** — **NOT dopaminergic modulation, NOT limbic reward**:

*   **Nigrothalamic Output (SNr → VA/VL, MD Thalamus):** The
    **SNr** is a **tonically active GABAergic output nucleus** —
    it **inhibits** the **VA/VL** and **mediodorsal** thalamus.
    It is **inhibited** by the **direct-pathway striatum** (D1
    MSNs) and **excited** by the **indirect-pathway subthalamic
    nucleus**. This is the **SNr analogue of the GPi** — the
    **basal ganglia gating** of **movement** and
    **cognitive-motor** behavior.

*   **Nigrotectal Output (SNr → Superior Colliculus):** The
    **SNr** **inhibits** the **superior colliculus** — the
    **tonic GABAergic brake** on **saccadic eye movements**.
    **Release of SNr inhibition** (via striatal inhibition of the
    SNr) **permits** the SC to generate **saccades**. This is the
    **basal ganglia control of orienting eye movements**
    (Hikosaka et al., 2000).

*   **Nigroreticular Output (SNr → Brainstem Reticular
    Formation):** The **SNr** **inhibits** the **brainstem
    reticular formation** — contributing to the **orienting /
    postural** output of the basal ganglia.

*   **Basal Ganglia Gating (SNr as the "brake"):** The **SNr** is
    one of the two **basal ganglia output nuclei** (with the GPi)
    — the **tonic GABAergic brake** that **inhibits** the
    thalamus and SC. **Movement and saccades** are **released**
    by **transient inhibition of the SNr** (via the direct
    pathway). This is the **basal ganglia gating** function.

*   **NOT a dopaminergic modulator, NOT a limbic reward nucleus.**
    The pars reticulata is the **GABAergic output** — its
    functions are **movement gating / saccade gating / orienting**.
    The **dopaminergic modulation** is the **pars compacta's**
    (A9); the **limbic reward** functions are primarily the
    **VTA's** (A10). Consumers must **not** attribute
    **dopaminergic modulation** to the pars reticulata — it is
    **GABAergic output**.

*   **NOT a neural processor in the classical sense.** The **pars
    reticulata** is a **basal ganglia output nucleus** — it
    **inhibits** its targets (thalamus, SC, reticular formation)
    and **is inhibited** by the striatum. The **processing**
    happens in the **striatum** (input integration) and the
    **cortex** (action selection); the **SNr** is the **output
    gate**.

**The unifying theme:** the pars reticulata is the **GABAergic
basal ganglia output** — the **midbrain counterpart of the GPi** —
gating **movement** (via the thalamus) and **saccades** (via the
superior colliculus). It is **SLEA-free**, **GABAergic**, and
**NOT the dopaminergic pars compacta**.

Associated Disorders
--------------------
The pars reticulata has **clinical associations** — but the
**canonical** association is **PSP**, **not Parkinson's disease**:

*   **Progressive Supranuclear Palsy (PSP — the canonical
    association):** **Tauopathy** involving the **SNr** (and the
    **STN**, **midbrain**, and **wider basal ganglia**) —
    contributing to the **supranuclear gaze palsy** (vertical >
    horizontal) that is the **hallmark** of **PSP**. The **SNr
    degeneration** impairs the **nigrotectal** control of
    **saccades**, producing the **supranuclear** gaze deficit.
    This is the **most important clinical association** of the
    pars reticulata. Consumers must **not** attribute PSP to the
    **pars compacta alone** — the **SNr** is the **gaze-palsy**
    substrate.

*   **Parkinson's Disease (SNr Is Involved in the CIRCUIT, Not the
    DEGENERATION):** The **pars reticulata** is **functionally
    involved** in the **Parkinson's disease circuit** — loss of
    **SNc dopamine** disinhibits the **indirect pathway**,
    **increasing STN excitation of the SNr**, **increasing SNr
    output**, and **inhibiting the thalamus** (contributing to
    **hypokinesia**). **But the SNr is NOT the degenerating
    structure** in PD — the **pars compacta** is. Consumers must
    **not** attribute the **PD degeneration** to the SNr — the
    SNr is **downstream** of the SNc degeneration. **Deep brain
    stimulation (DBS)** of the **STN** (the standard PD target)
    works in part by **modulating STN → SNr** drive.

*   **Saccadic Disorders (SNr / Nigrotectal Dysfunction):** **SNr
    lesions** produce **irrepressible saccades** and **impaired
    saccade suppression** — the **SC is released** from the
    **tonic SNr brake**. Documented in **primate lesion
    studies** (Hikosaka) and consistent with the **PSP** gaze
    palsy.

*   **Deep Brain Stimulation (STN DBS — SNr Circuit):** **STN
    DBS** for Parkinson's disease **modulates** the **STN → SNr**
    projection — part of the **therapeutic mechanism** is
    **reduced SNr output** and **disinhibited thalamus**.
    Documented, but **mechanistically contested** (the DBS
    mechanism is not fully understood).

*   **Hemiballismus (STN — NOT the SNr):** **Hemiballismus** is a
    **subthalamic nucleus** lesion — **not** an SNr lesion. The
    STN lesion **reduces SNr excitation**, **reducing SNr
    output**, and **disinhibiting the thalamus** (producing
    **ballism**). Consumers must **not** attribute hemiballismus
    to the **SNr** — the **lesion** is in the **STN**; the SNr
    is **downstream**.

*   **Wilson's Disease and Manganese Toxicity:** **Copper**
    (Wilson's) and **manganese** (welding, hepatic
    encephalopathy) accumulate in the **basal ganglia**, including
    the substantia nigra — producing **parkinsonism** and **MRI
    T1 hyperintensity**. Documented, but **not SNr-selective** in
    the way PSP is.

**What is NOT here:** The pars reticulata is **not** the substrate
for **Parkinson's disease degeneration** (pars compacta),
**Huntington's disease** (striatum — caudate/putamen),
**Kluver-Bucy syndrome** (amygdala), **Alzheimer's disease**
(hippocampus, nucleus basalis), **addiction** (VTA / nucleus
accumbens), or **hemiballismus** (STN). Its clinical relevance is
**nigrothalamic / nigrotectal** — **movement gating and saccade
gating** — with **progressive supranuclear palsy** as the
**canonical** association.

Lateralization Notes
--------------------
This is the **right** pars reticulata module. The pars reticulata is
**bilaterally symmetric** — and it carries **NO warning**:

*   **Bilateral Symmetry:** Each hemisphere has its own pars
    reticulata, with **ipsilateral** projections. The two sides
    are **structurally identical** — same **nigrothalamic /
    nigrotectal** composition, same **thalamic and tectal**
    targets.

*   **Clinical Asymmetry (PSP Onset — contested at the structural
    level):** **PSP** typically presents with **symmetric**
    **supranuclear gaze palsy** — but **asymmetric onset** is
    documented, and the **structural lateralization** of the SNr
    is **subtle and contested**. It is documented in the
    **substantia_nigra container**, not at the **right** module
    level, and it is **NOT a warning**.

*   **NO Warning of their own:** The right pars reticulata is a
    **strict-mirror pair with NO warning** — **no SLEA warning**,
    **no extended-amygdala warning**, **no rhinencephalon-
    exclusion flag**. Consumers must **not** import any of those
    warnings into the pars reticulata.

**A consumer that assumes "right pars reticulata = left pars
reticulata" will be structurally correct** — the two sides are
**symmetric**. The clinical-onset asymmetry in PSP is a
**container-level / clinical** note, not a **module-level**
warning.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-nucleus or cross-lobe imports.** This module does
    **not** import from ``.../substantia_nigra/right/
    pars_compacta/``, ``.../tegmentum/ventral_tegmental_area/``,
    ``.../tegmentum/red_nucleus/``, ``.../subthalamus/
    subthalamic_nucleus/``, ``.../basal_ganglia/globus_pallidus/``,
    ``.../basal_ganglia/striatum/dorsal_striatum/``,
    ``.../diencephalon/thalamus/``, ``.../midbrain/tectum/
    superior_colliculus/``, or any other container. The pars
    reticulata's relationships to the pars compacta, GPi, STN,
    VTA, dorsal striatum, thalamus, superior colliculus, red
    nucleus, and crus cerebri are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **nigrothalamic**,
    **nigrotectal**, and **nigroreticular** output populations,
    the **parvalbumin** marker, the **dorsal / ventral** tiers,
    and the **SNr-embedded dopaminergic** neurons are documented
    as **prose**, not as sub-modules. Consumers must not assume
    any exist as children; resolve output-channel-level detail
    through the references (Hikosaka et al., 2000; Parent &
    Hazrati, 1995).
*   **GABAERGIC — NOT the dopaminergic pars compacta.** The pars
    reticulata is the **GABAergic output**; the **pars compacta**
    is the **dopaminergic modulator**. Consumers must **not**
    conflate the two.
*   **NOT the VTA.** The VTA is the **A10 dopaminergic** cell
    group; the pars reticulata is the **GABAergic output**.
*   **NOT the retrorubral area (A8).** The A8 group is **caudal
    and dorsolateral** — a **separate structure**.
*   **NOT the whole substantia nigra.** The pars reticulata is a
    **component** of the substantia nigra; the **pars compacta**
    is the other component.
*   **NOT the GPi.** The **SNr** is **functionally parallel to**
    the GPi — **different nucleus, different embryological
    origin, different projection fascicles**.
*   **NOT the subthalamic nucleus.** The STN is the
    **indirect-pathway glutamatergic** driver; the SNr is the
    **GABAergic output** that the STN **excites**.
*   **NOT the dorsal striatum.** The striatum is the **SNr's
    input source** (direct-pathway inhibition).
*   **NOT the thalamus.** The thalamus is the **SNr's output
    target** (nigrothalamic).
*   **NOT the superior colliculus.** The SC is the **SNr's output
    target** (nigrotectal).
*   **NOT the crus cerebri.** The crus cerebri is the
    **white-matter tract** ventral to the SN; the pars reticulata
    is the **grey-matter nucleus**.
*   **NOT the red nucleus.** The red nucleus is the **adjacent
    rubrospinal / rubro-olivary motor relay**.
*   **NOT the pars lateralis.** The pars lateralis is a **prose
    subdivision** of the substantia nigra, not the pars
    reticulata.
*   **NOT the dopaminergic neurons embedded in the pars reticulata.**
    Those are **pars reticulata prose**, not the pars compacta.
*   **NOT a single uniform GABAergic population — MULTIPLE output
    populations.** The **nigrothalamic**, **nigrotectal**, and
    **nigroreticular** populations are **prose**, not structural
    children.
*   **SLEA-FREE — no extended-amygdala relationship.** The pars
    reticulata is **not** an extended-amygdala component.
*   **No ``AREA_PATHS`` hop.** The pars reticulata is a **local
    leaf** under the right substantia nigra, not a cross-listed
    leaf (unlike Brodmann areas).
*   **No nested cross-listing.** The pars reticulata has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left pars reticulata — strict
    mirror with NO warning.** Right and left pars reticulata
    modules are **structurally identical** — same **leaf**
    status, same **GABAergic** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.midbrain.tegmentum.substantia_nigra.right import pars_reticulata

Or by fully-qualified path string::

    path = (
        "midbrain.tegmentum.substantia_nigra.right.pars_reticulata"
    )

**Do not** assume the pars reticulata is the **pars compacta**.
The **pars compacta** is the **dopaminergic modulator**; the pars
reticulata is the **GABAergic output**.

**Do not** assume the pars reticulata is the **ventral tegmental
area**. The **VTA** is the **A10 dopaminergic** cell group; the
pars reticulata is the **GABAergic output**.

**Do not** assume the pars reticulata is the **whole substantia
nigra**. The **pars compacta** is the other component.

**Do not** assume the pars reticulata is the **GPi**. The **SNr**
is **functionally parallel to** the GPi — **different nucleus,
different projection fascicles**.

**Do not** assume the pars reticulata is the **subthalamic
nucleus**. The **STN** is the **indirect-pathway driver** that
**excites** the SNr; the pars reticulata is the **GABAergic
output**.

**Do not** assume the pars reticulata is the **dorsal striatum**,
the **thalamus**, or the **superior colliculus**. The striatum is
the **input source**; the thalamus and SC are the **output
targets**.

**Do not** import the **SLEA warning** into the pars reticulata.
**The pars reticulata is SLEA-FREE** — it is **not** an
extended-amygdala component.

Iterating the pars reticulata's (empty) children (recommended
consumer pattern)::

    PARS_RETICULATA_RIGHT_CHILDREN = ()
    # The pars reticulata is a leaf. The nigrothalamic,
    # nigrotectal, and nigroreticular output populations, the
    # parvalbumin marker, the dorsal / ventral tiers, and the
    # SNr-embedded dopaminergic neurons are prose, not modules.

Reaching the pars compacta (recommended consumer pattern — the
dopaminergic sibling)::

    # The pars compacta is the DOPAMINERGIC component of the right
    # substantia nigra — the A9 cell group projecting to the
    # dorsal striatum:
    #
    #   midbrain.tegmentum.substantia_nigra.right.pars_compacta
    #
    # The pars reticulata is the GABAERGIC output; the pars
    # compacta is the DOPAMINERGIC modulator.

Reaching the globus pallidus (recommended consumer pattern — the
parallel output)::

    # The GPi is the other basal ganglia output — functionally
    # parallel to the SNr, NOT the same structure:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.right.
    #   subcortical.basal_ganglia.globus_pallidus

Reaching the subthalamic nucleus (recommended consumer pattern —
the indirect-pathway driver)::

    # The STN is the glutamatergic indirect-pathway node that
    # EXCITES the SNr (and the GPi):
    #
    #   forebrain.diencephalon.subthalamus.subthalamic_nucleus

Reaching the dorsal striatum (recommended consumer pattern — the
SNr's input source)::

    # The dorsal striatum is the INPUT SOURCE of the SNr — the
    # direct-pathway striatal MSNs INHIBIT the SNr:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.right.
    #   subcortical.basal_ganglia.striatum.dorsal_striatum

Reaching the thalamus (recommended consumer pattern — the
nigrothalamic target)::

    # The thalamus (VA/VL, mediodorsal) is the OUTPUT TARGET of
    # the nigrothalamic projection:
    #
    #   forebrain.diencephalon.thalamus

Reaching the superior colliculus (recommended consumer pattern —
the nigrotectal target)::

    # The superior colliculus is the OUTPUT TARGET of the
    # nigrotectal projection — the SNr gates saccadic eye
    # movements via the SC:
    #
    #   midbrain.tectum.superior_colliculus

Reaching the SLEA components (recommended consumer pattern — NOTE
the pars reticulata is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the pars
    # reticulata:
    #
    #   ...medial_temporal_lobe.amygdala.central_nucleus
    #   ...extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   ...basal_ganglia.globus_pallidus.ventral_pallidum
    #   ...basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The pars reticulata is SLEA-FREE.

Output-channel-level detail (not wired — consult references)::

    # The pars reticulata's output populations are prose, not
    # modules:
    #   nigrothalamic      -> VA/VL, MD thalamus (skeletomotor / associative)
    #   nigrotectal        -> superior colliculus (saccadic)
    #   nigroreticular     -> brainstem reticular formation (orienting / postural)
    #   parvalbumin+       -> dominant neurochemical marker of the SNr
    #   dorsal tier        -> nigrothalamic
    #   ventral tier       -> nigrotectal
    #
    # Do not attempt to resolve these as sub-paths of the
    # pars reticulata.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        snr_path = (
            f"midbrain.tegmentum.substantia_nigra.{side}."
            f"pars_reticulata"
        )
        # resolve snr_path through the memory/recall layer

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
    connections; SNr as output parallel to GPi.)
*   **Saccades and the SNr:** Hikosaka, O., et al. (2000). "Role of
    the basal ganglia in the control of purposive saccadic eye
    movements." *Physiological Reviews* 80:953–978. (SNr →
    superior colliculus; the tonic GABAergic brake on saccades.)
*   **Nigrotectal projection:** Takada, M., et al. (1994). "Nigral
    innervation of the superior colliculus in the macaque
    monkey." *Journal of Comparative Neurology* 340:395–406.
    (Nigrotectal neurons and saccade gating.)
*   **GABAergic SNr neurons:** Smith, Y., Bolam, J.P. (1990). "The
    output neurones and the dopaminergic neurones of the
    substantia nigra receive a GABA-containing input from the
    globus pallidus in the rat." *Journal of Comparative
    Neurology* 296:47–64. (SNr GABAergic output neurons;
    pallidal and striatal input.)
*   **Parvalbumin in the SNr:** Rajakumar, N., et al. (1994).
    "Parvalbumin-containing GABAergic neurons in the basal
    ganglia of the rat." *Journal of Comparative Neurology*
    340:395–406. (Parvalbumin as the SNr neurochemical marker.)
*   **PSP and SNr degeneration:** Dickson, D.W., et al. (2010).
    "Neuropathology of variants of progressive supranuclear
    palsy." *Current Opinion in Neurology* 23:394–400.
    (Tauopathy involving the SNr; the supranuclear gaze palsy
    substrate.)
*   **PSP and saccades:** Chen, A.L., et al. (2010). "Saccadic
    eye movement abnormalities in progressive supranuclear
    palsy." *Movement Disorders* 25:2363–2371. (Saccadic deficits
    in PSP and the SNr / SC circuit.)
*   **Parkinson's disease and the SNr circuit:** Wichmann, T.,
    DeLong, M.R. (1996). "Functional and pathophysiological
    models of the basal ganglia." *Current Opinion in
    Neurobiology* 6:751–758. (The SNr is downstream of the SNc
    degeneration; increased SNr output in PD.)
*   **STN DBS and the SNr:** Benabid, A.L., et al. (2009).
    "Deep brain stimulation of the subthalamic nucleus for the
    treatment of Parkinson's disease." *Lancet Neurology*
    8:67–81. (STN DBS mechanism and the STN → SNr projection.)
*   **Dopaminergic cell groups (A8, A9, A10):** Dahlström, A.,
    Fuxe, K. (1964). "Evidence for the existence of monoamine-
    containing neurons in the central nervous system. I.
    Demonstration of monoamines in the cell bodies of brain stem
    neurons." *Acta Physiologica Scandinavica* 62 (Suppl. 232):
    1–55. (The A8/A9/A10 dopaminergic cell-group nomenclature —
    relevant for the SNr-embedded dopaminergic neurons.)
*   **SLEA (contrast — the pars reticulata is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the pars reticulata.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Substantia nigra pars reticulata in
    overview.)
*   NeuroNames — Substantia nigra pars reticulata (right); FMA —
    Substantia nigra pars reticulata (right member).
"""