"""
infrastructure.brainparts.midbrain.tegmentum.substantia_nigra
=============================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        ├── caudal_linear_nucleus        (midline leaf — anomalous)
        ├── dorsal_raphe_nucleus         (midline leaf — anomalous)
        ├── interpeduncular_nucleus      (midline leaf — anomalous)
        ├── midbrain_reticular_formation (diffuse bilateral leaf — anomalous)
        ├── periaqueductal_gray          (diffuse bilateral leaf — CLEAN)
        ├── red_nucleus                  (structure container — CLEAN)
        ├── rostral_interstitial_nucleus_mlf (structure container — CLEAN)
        ├── rostral_linear_nucleus_raphe (midline leaf — anomalous)
        └── substantia_nigra             <-- THIS MODULE
            ├── pars_compacta            (MULTI-PART STRUCTURE
            │   ├── left                 CONTAINER — paired —
            │   └── right                holds the TWO PARS as
            └── pars_reticulata          children — each pars
                ├── left                 itself paired)
                └── right

**Primary synonym:** Substantia nigra; **SN**; **substantia nigra
of the midbrain tegmentum**; **the black substance**; **substantia
nigra (pars compacta + pars reticulata)**; **locus niger** (older
Latin); **Soemmering's substance** (older term — after Samuel
Thomas von Soemmerring).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). The substantia nigra is a **multi-part structure** of
the **ventral midbrain tegmentum** — at the level of the **superior
colliculus**, **dorsal to the cerebral peduncle (crus cerebri)** and
**ventral to the tegmentum proper** — **paired** (a left substantia
nigra and a right substantia nigra). **It has TWO
cytoarchitectonically, neurochemically, and functionally distinct
pars:**
*   **Pars compacta (SNc)** — the **dorsal** subdivision —
    **dopaminergic** (tyrosine hydroxylase-positive,
    neuromelanin-containing, **A9** dopaminergic cell group) —
    the **principal dopaminergic input to the striatum**
    (the **nigrostriatal** pathway) — the **motor-modulation**
    substructure — **Parkinson's disease** substrate.
*   **Pars reticulata (SNr)** — the **ventral** subdivision —
    **GABAergic** (GABA-synthesizing, **GABAergic inhibitory**)
    — the **principal inhibitory output of the basal ganglia**
    to the thalamus, the superior colliculus, and the brainstem
    — the **inhibitory gate** on saccades, posture, and movement
    — **PSP** co-substrate (with the **riMLF**).
**The "black" color** comes from **neuromelanin** — the dark
pigment that accumulates in the **dopaminergic neurons of the pars
compacta** as a byproduct of dopamine metabolism. **It is the
largest neuromelanin-containing structure in the human brain** —
the reason for the name "substantia nigra" ("black substance").
**The pars reticulata has no neuromelanin** — the pigmentation is a
pars compacta feature, not a substantia nigra feature.
**Container status:** **This module is a MULTI-PART STRUCTURE
CONTAINER, not a leaf.** It holds the **pars_compacta** and the
**pars_reticulata** as **children** — each is **itself a structure
container** (a paired structure with `left/` and `right/` leaves).
**The substantia nigra is the FIRST multi-part structure container
in the family** — it establishes the **multi-part
structure-container pattern** — a **structure that has two or more
functionally distinct subdivisions, each of which is itself a
structure**. **The structure-container pattern applies
RECURSIVELY** — the **substantia nigra container** holds the
**two pars containers**, and **each pars container** holds the
**left and right substantive leaves**. See *The Multi-Part
Structure-Container Pattern* and *Design Contract — Live amendment
to the tegmentum container*.
**Part of:** The **tegmentum** region container — as a **multi-part
structure container** for a **paired multi-part structure**. **The
substantia nigra is NOT a cranial nerve nucleus** and is **NOT
cross-listed** with ``cranial_nerve_nuclei/``.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — as a **multi-part structure
container**.
**Structural children (expected — the tree is authoritative):**
*   ``pars_compacta/`` — the **pars compacta** — a **structure
    container** for the **paired pars compacta** — holding
    ``left/`` (the **left pars compacta**) and ``right/`` (the
    **right pars compacta**) as **substantive paired leaves**.
    **The pars compacta is the dopaminergic, motor-modulation
    substructure** — the **nigrostriatal** pathway — the
    **Parkinson's disease** substrate.
*   ``pars_reticulata/`` — the **pars reticulata** — a **structure
    container** for the **paired pars reticulata** — holding
    ``left/`` (the **left pars reticulata**) and ``right/`` (the
    **right pars reticulata**) as **substantive paired leaves**.
    **The pars reticulata is the GABAergic, inhibitory-gate
    substructure** — the **inhibitory output of the basal
    ganglia** to the thalamus, the superior colliculus, and the
    brainstem — the **saccade-gating** substrate — the **PSP**
    co-substrate (with the **riMLF**).
**Boundary status (MULTI-PART STRUCTURE CONTAINER — the FIRST
multi-part structure container in the family):** **Boundary case —
the substantia nigra is a MULTI-PART STRUCTURE CONTAINER.** It
holds the **pars_compacta** and the **pars_reticulata** as
**children** — each is **itself a structure container** (a paired
structure with `left/` and `right/` leaves). **The substantia
nigra is the FIRST multi-part structure container in the family**
— it establishes the **multi-part structure-container pattern** —
a **structure that has two or more functionally distinct
subdivisions, each of which is itself a structure**. **The
structure-container pattern applies RECURSIVELY** — the
**substantia nigra container** holds the **two pars containers**,
and **each pars container** holds the **left and right substantive
leaves**. See *The Multi-Part Structure-Container Pattern* and
*Design Contract — Live amendment to the tegmentum container*.
**Boundary status (THE MULTI-PART STRUCTURE-CONTAINER PATTERN —
the substantia nigra is the first instance — the red nucleus and the
riMLF are the single-part structure containers):** **Boundary case
— the substantia nigra establishes the MULTI-PART
STRUCTURE-CONTAINER PATTERN.** The pattern is:
*   **A SINGLE-PART PAIRED structure** (the **red nucleus**, the
    **riMLF**) — a **structure container** at
    ``tegmentum/<structure>/`` — holding ``left/`` and ``right/``
    as **substantive paired leaves** — the **anatomy is in the
    two leaves**.
*   **A MULTI-PART PAIRED structure** (the **substantia nigra**)
    — a **multi-part structure container** at
    ``tegmentum/<structure>/`` — holding the **pars** as
    **children** (``<pars>/``) — each pars being **itself a
    single-part structure container** at
    ``tegmentum/<structure>/<pars>/`` — holding **its own**
    ``left/`` and ``right/`` as **substantive paired leaves**.
    **The anatomy is in the two leaves of each pars.**
**The multi-part structure-container pattern is the RECURSIVE
version of the single-part structure-container pattern.** **The
substantia nigra is the first instance** — its two pars are
**distinct structures** — **not just subdivisions of a single
structure**, but **functionally and neurochemically distinct
nuclei**: the **pars compacta** is a **dopaminergic
neuromodulatory nucleus**; the **pars reticulata** is a
**GABAergic inhibitory nucleus**. **They have different
connectomes, different transmitters, different functions, and
different clinical associations.** **The multi-part structure
container declares this split** — **the two pars are separate
structures within the substantia nigra container**. See *The
Multi-Part Structure-Container Pattern*.
**Boundary status (TWO FUNCTIONALLY DISTINCT PARS — the pars
compacta and the pars reticulata are DIFFERENT structures):**
**Boundary case — the substantia nigra's two pars are FUNCTIONALLY
AND NEUROCHEMICALLY DISTINCT structures.** They are **not**
interchangeable subdivisions — they are **two different nuclei
that share a container**:
*   **Pars compacta** — **dopaminergic** (tyrosine
    hydroxylase-positive, neuromelanin-containing, **A9** group)
    — the **principal dopaminergic input to the striatum** (the
    **nigrostriatal** pathway) — the **motor-modulation**
    substructure — **Parkinson's disease** substrate — a
    **neuromodulatory nucleus** (like the VTA, the DR, the
    CLi) — **NOT** an inhibitory nucleus.
*   **Pars reticulata** — **GABAergic** (GABA-synthesizing,
    **inhibitory**) — the **principal inhibitory output of the
    basal ganglia** to the thalamus, the superior colliculus,
    and the brainstem — the **inhibitory gate** on saccades,
    posture, and movement — a **GABAergic inhibitory nucleus**
    (like the globus pallidus internus, the substantia nigra
    pars reticulata's homologue) — **NOT** a dopaminergic
    nucleus.
**They have DIFFERENT connectomes** (the pars compacta receives
from the striatum and projects to the striatum; the pars
reticulata receives from the striatum and projects to the
thalamus, the superior colliculus, and the brainstem), **DIFFERENT
transmitters** (dopamine vs. GABA), **DIFFERENT functions**
(motor modulation vs. inhibitory gating), and **DIFFERENT clinical
associations** (**Parkinson's disease** vs. **saccade disorders**
and **PSP**). **Consumers must not treat the substantia nigra as a
single undifferentiated structure** — the two pars are **different
structures** — **go one level deeper to the specific pars**.
**Boundary status (PAIRED STRUCTURE — the substantia nigra is
BILATERALLY SYMMETRIC, each pars paired):** **Boundary case — the
substantia nigra is a PAIRED structure.** Each hemisphere has its
**own** substantia nigra — a **left substantia nigra** (with a
**left pars compacta** and a **left pars reticulata**) and a
**right substantia nigra** (with a **right pars compacta** and a
**right pars reticulata**). **The two sides are bilaterally
symmetric** — same two pars, same connectomes, same functions.
**Each pars is itself paired** — the **pars compacta container**
holds the **left pars compacta** and the **right pars compacta**
as substantive paired leaves; the **pars reticulata container**
holds the **left pars reticulata** and the **right pars
reticulata** as substantive paired leaves. **The multi-part
structure-container pattern applies recursively** — the
**substantia nigra container** holds the **two pars containers**,
and **each pars container** holds the **two side leaves**.
**Boundary status (NOT the VTA — the VTA is a SEPARATE dopaminergic
nucleus):** **Boundary case — the substantia nigra is NOT the
ventral tegmental area (VTA).** The **VTA**
(``.../tegmentum/left/ventral_tegmental_area/`` and the right
counterpart) is a **separate dopaminergic nucleus** — **paired** —
the **mesolimbic / mesocortical** reward pathways. **The pars
compacta of the substantia nigra** is a **different dopaminergic
nucleus** — the **nigrostriatal** motor pathway. **They are
DIFFERENT STRUCTURES** — **different dopaminergic cell groups**
(the **A9** group for the pars compacta, the **A10** group for
the VTA), **different projections** (the **striatum** vs. the
**nucleus accumbens, prefrontal cortex, and amygdala**), and
**different clinical associations** (**Parkinson's disease** vs.
**addiction and reward processing**). Consumers must **not**
conflate the substantia nigra with the VTA — **even though both
are dopaminergic and both are in the ventral midbrain**.
**Boundary status (NOT the red nucleus — the red nucleus is the
LIMB-MOTOR premotor relay, DORSOMEDIAL to the substantia nigra):**
**Boundary case — the substantia nigra is NOT the red nucleus.**
The **red nucleus** (``.../tegmentum/red_nucleus/``) is the
**limb-motor premotor relay** — the **rubrospinal motor
coordination** — **dorsomedial** to the substantia nigra.
**They are DIFFERENT STRUCTURES** — the **red nucleus** is a
**premotor motor relay**; the **substantia nigra** is a
**dopaminergic neuromodulatory nucleus** (pars compacta) **plus**
a **GABAergic inhibitory nucleus** (pars reticulata). **Different
structure classes, different functional subsystems.** Consumers
must **not** conflate the substantia nigra with the red nucleus.
**Boundary status (NOT the cerebral peduncle — the peduncle is
VENTRAL to the substantia nigra):** **Boundary case — the
substantia nigra is NOT the cerebral peduncle.** The **cerebral
peduncle** (``.../midbrain/cerebral_peduncle/``) is the
**ventral-most descending fiber bundle** — the **crus cerebri** —
**white matter** — **ventral** to the substantia nigra. **The
substantia nigra sits DORSAL to the crus cerebri** and **VENTRAL
to the tegmentum proper**. **They are DIFFERENT STRUCTURES** —
the **peduncle** is a **conduction pathway**; the **substantia
nigra** is a **grey-matter structure** (dopaminergic pars
compacta + GABAergic pars reticulata). Consumers must **not**
conflate the substantia nigra with the cerebral peduncle.
**Boundary status (NOT the globus pallidus — the globus pallidus is
TELENCEPHALIC):** **Boundary case — the substantia nigra is NOT
the globus pallidus.** The **globus pallidus**
(``.../forebrain/telencephalon/subcortical/basal_ganglia/globus_
pallidus/``) is a **telencephalic** basal ganglia structure — the
**GABAergic output of the basal ganglia** to the thalamus — the
**external (GPe)** and **internal (GPi)** segments. **The
substantia nigra pars reticulata** is the **midbrain** homologue
of the **globus pallidus internus** — **similar GABAergic
inhibitory function, different location** (midbrain vs.
telencephalon). **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **globus pallidus** is **telencephalic**; the
**substantia nigra** is **mesencephalic**. Consumers must **not**
conflate the substantia nigra with the globus pallidus — **even
though the pars reticulata and the GPi are functional analogues**.
**Boundary status (NOT the striatum — the striatum is the UPSTREAM
INPUT):** **Boundary case — the substantia nigra is NOT the
striatum.** The **striatum**
(``.../forebrain/telencephalon/subcortical/basal_ganglia/striatum/``)
is a **telencephalic** basal ganglia structure — the **caudate
nucleus** and the **putamen** — the **input structure** of the
basal ganglia. **The substantia nigra** (pars compacta +
pars reticulata) **receives from** the striatum (the
**striatonigral** pathway) and **projects to** the striatum
(the **nigrostriatal** pathway). **The substantia nigra is
DOWNSTREAM of the striatum** in the direct pathway, **and
UPSTREAM of the striatum** in the nigrostriatal dopaminergic
modulation. **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **striatum** is **telencephalic**; the
**substantia nigra** is **mesencephalic**. Consumers must **not**
conflate the substantia nigra with the striatum.
**Boundary status (NOT the subthalamic nucleus — the subthalamic
nucleus is DIENCEPHALIC):** **Boundary case — the substantia
nigra is NOT the subthalamic nucleus (STN).** The **subthalamic
nucleus** (``.../forebrain/diencephalon/subthalamus/subthalamic_
nucleus/``) is a **diencephalic** basal ganglia structure — the
**glutamatergic** excitatory input to the **globus pallidus
internus** and the **substantia nigra pars reticulata** — the
**indirect pathway** node. **The substantia nigra** (pars
reticulata) **receives from** the subthalamic nucleus. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **subthalamic
nucleus** is **diencephalic**; the **substantia nigra** is
**mesencephalic**. Consumers must **not** conflate the
substantia nigra with the subthalamic nucleus — **even though
they are both basal ganglia structures and both project to the
same targets**.
**Boundary status (NOT the periaqueductal gray, the MRF, the CLi,
the DR, the IPN, the RLi, or the riMLF — different structures):**
**Boundary case — the substantia nigra is NOT the periaqueductal
gray, the midbrain reticular formation, the caudal linear
nucleus, the dorsal raphe, the interpeduncular nucleus, the
rostral linear nucleus of the raphe, or the riMLF.** Those are
**different tegmentum structures** — the **PAG** (diffuse
bilateral — pain modulation and defensive behavior), the **MRF**
(diffuse bilateral — arousal and locomotion), the **CLi**, the
**DR**, the **RLi** (midline — serotonergic /
serotonergic-dopaminergic), the **IPN** (midline — GABAergic
limbic relay), and the **riMLF** (paired — vertical saccade
generator). **The substantia nigra is a multi-part paired
structure** — **dopaminergic pars compacta + GABAergic pars
reticulata**. **Different structure class, different functional
subsystem.** Consumers must **not** conflate the substantia
nigra with any of these.
**Boundary status (DOPAMINERGIC (pars compacta) AND GABAergic (pars
reticulata) — the phenotypes are ``chemicals_hormones``-layer
facts):** **Boundary case — the substantia nigra's two pars carry
DIFFERENT transmitter phenotypes — both ``chemicals_hormones``-
layer facts.** The **pars compacta** is **dopaminergic** —
**tyrosine hydroxylase (TH), dopamine synthesis, dopamine
transporters, dopamine receptors, and neuromelanin** (a
byproduct of dopamine metabolism). The **pars reticulata** is
**GABAergic** — **glutamic acid decarboxylase (GAD), GABA
synthesis, GABA transporters, and GABA-A / GABA-B receptors**.
**Both phenotypes are ``chemicals_hormones``-layer facts** —
documented as **prose** in the **pars leaves**, **never
imported** into the midbrain structural layer. Dependency DAG
unchanged: ``chemicals_hormones → memory → brainparts``.
**The "black" color** (neuromelanin) is a **dopamine-metabolism
byproduct** — a **``chemicals_hormones``-layer fact** specific to
the **pars compacta**. Consumers must **not** import either
phenotype into the midbrain structural layer. See
*Chemicals-Layer Discipline* and *Design Contract*.
**Boundary status (NO COUPLING WARNING — the substantia nigra is
NEITHER an oscillator NOR a coupled pair):** **Boundary case —
the substantia nigra carries NO coupling warning.** The
**coupling warning** attaches to **OSCILLATORS** (the
pre-Bötzinger complex, the Bötzinger complex, the pFRG) — and
**neither the pars compacta nor the pars reticulata is an
oscillator**. The **pars compacta** is a **dopaminergic
neuromodulatory nucleus** — it **modulates** the striatum via
volume transmission of dopamine — **not** an oscillator. The
**pars reticulata** is a **GABAergic inhibitory nucleus** — it
**provides tonic inhibition** to its targets — **not** an
oscillator. **The two pars are DIFFERENT structure classes** —
**both carry NO coupling warning** — same rule as every
non-oscillator class. **The left and right substantia nigra are
coordinated** via their **bilateral projections** (the
**striatonigral** and **nigrostriatal** pathways are bilateral,
and the **pars reticulata** projects to bilateral targets) —
**not via intrinsic left-right coupling**. **The substantia
nigra pair is a strict mirror with NO warning.**

Overview
--------
The substantia nigra is the **largest neuromelanin-containing
structure in the human brain** — a **multi-part paired structure**
of the **ventral midbrain tegmentum**, at the level of the
**superior colliculus** — **dorsal to the cerebral peduncle (crus
cerebri)** and **ventral to the tegmentum proper**. It has **two
cytoarchitectonically, neurochemically, and functionally distinct
pars** — the **dorsal pars compacta** (dopaminergic, A9 group, the
nigrostriatal pathway, the motor-modulation substructure,
Parkinson's disease substrate) and the **ventral pars reticulata**
(GABAergic, the inhibitory output of the basal ganglia, the
inhibitory gate on saccades, posture, and movement, the PSP
co-substrate with the riMLF). The **"black" color** comes from
**neuromelanin** — a dopamine-metabolism byproduct that accumulates
in the **pars compacta** — **not in the pars reticulata**. **The
substantia nigra is the FIRST multi-part structure container in the
family** — it establishes the **multi-part structure-container
pattern** — a **structure that has two or more functionally
distinct subdivisions, each of which is itself a structure**.

**The substantia nigra has TWO PARS — the pars compacta and the
pars reticulata — and they are FUNCTIONALLY AND NEUROCHEMICALLY
DISTINCT structures.** **The pars compacta** is a **dopaminergic
neuromodulatory nucleus** — the **principal dopaminergic input to
the striatum** (the **nigrostriatal** pathway) — **Parkinson's
disease** substrate. **The pars reticulata** is a **GABAergic
inhibitory nucleus** — the **principal inhibitory output of the
basal ganglia** to the thalamus, the superior colliculus, and the
brainstem — the **inhibitory gate** on saccades, posture, and
movement — **PSP** co-substrate (with the **riMLF**).
**They have different connectomes, different transmitters,
different functions, and different clinical associations.**
Consumers must **not** treat the substantia nigra as a single
undifferentiated structure — **go one level deeper to the specific
pars**.

**The substantia nigra is a MULTI-PART STRUCTURE CONTAINER.** It
holds the **pars_compacta** and the **pars_reticulata** as
**children** — each is **itself a structure container** (a paired
structure with `left/` and `right/` leaves). **The structure-
container pattern applies RECURSIVELY** — the **substantia nigra
container** holds the **two pars containers**, and **each pars
container** holds the **left and right substantive leaves**.

**The substantia nigra is a PAIRED structure.** Each hemisphere has
its **own** substantia nigra — a **left substantia nigra** (with a
**left pars compacta** and a **left pars reticulata**) and a
**right substantia nigra** (with a **right pars compacta** and a
**right pars reticulata**). **The two sides are bilaterally
symmetric.**

**The substantia nigra carries NO coupling warning** — **neither
the pars compacta (dopaminergic neuromodulatory) nor the pars
reticulata (GABAergic inhibitory) is an oscillator** — same rule
as every non-oscillator class.

**The substantia nigra is NOT a CN nucleus.** It is **not**
cross-listed with ``cranial_nerve_nuclei/`` — it has **one path
only**: ``.../tegmentum/substantia_nigra/`` (as a multi-part
structure container) with **pars_compacta/** and
**pars_reticulata/** children.

The Multi-Part Structure-Container Pattern
------------------------------------------
**The substantia nigra is the FIRST multi-part structure container in
the family** — it establishes the **multi-part structure-container
pattern** — a **structure that has two or more functionally
distinct subdivisions, each of which is itself a structure**.

**The pattern is:**
*   **A SINGLE-PART PAIRED structure** (the **red nucleus**, the
    **riMLF**) — a **structure container** at
    ``tegmentum/<structure>/`` — holding ``left/`` and ``right/``
    as **substantive paired leaves** — the **anatomy is in the
    two leaves**.
*   **A MULTI-PART PAIRED structure** (the **substantia nigra**)
    — a **multi-part structure container** at
    ``tegmentum/<structure>/`` — holding the **pars** as
    **children** (``<pars>/``) — each pars being **itself a
    single-part structure container** at
    ``tegmentum/<structure>/<pars>/`` — holding **its own**
    ``left/`` and ``right/`` as **substantive paired leaves**.
    **The anatomy is in the two leaves of each pars.**

**The multi-part structure-container pattern is the RECURSIVE version
of the single-part structure-container pattern.** The **red nucleus**
and the **riMLF** are **single-part structure containers** (one
structure with two sides). The **substantia nigra** is a
**multi-part structure container** (two structures — the two pars —
each with two sides).

**The recursion is the structural expression of the two-pars
split.** The **two pars are distinct structures** — **not just
subdivisions of a single structure, but functionally and
neurochemically distinct nuclei**: the **pars compacta** is a
**dopaminergic neuromodulatory nucleus**; the **pars reticulata**
is a **GABAergic inhibitory nucleus**. **They have different
connectomes, different transmitters, different functions, and
different clinical associations.** **The multi-part structure
container declares this split** — **the two pars are separate
structures within the substantia nigra container**.

**The tegmentum container amendment must acknowledge the multi-part
structure-container pattern** — **in addition to** the
**single-part structure-container pattern** (the red nucleus, the
riMLF), the **midline leaf pattern** (the RLi — the **actual
clean case**; the CLi, DR, IPN — **anomalous, pending joint
Resolution B**), and the **diffuse bilateral leaf pattern** (the
**PAG** — the actual clean case; the **MRF** — anomalous). **The
amendment now has FOUR patterns to acknowledge** — **paired
single-part structure containers**, **paired multi-part structure
containers**, **midline leaves**, and **diffuse bilateral
leaves**.

Function in the Human Brain
---------------------------
**See the pars leaf modules** — the **`pars_compacta/left`**,
**`pars_compacta/right`**, **`pars_reticulata/left`**, and
**`pars_reticulata/right`** — for the substantive functions of the
two pars. **This multi-part structure container has no function of
its own** — it **holds the two pars containers** and **declares
their distinction**. Every functional claim belongs to a **pars
leaf**.

Associated Disorders
--------------------
**See the pars leaf modules** — the **`pars_compacta/left`**,
**`pars_compacta/right`**, **`pars_reticulata/left`**, and
**`pars_reticulata/right`** — for the substantive clinical
associations of the two pars. **This multi-part structure container
has no clinical associations of its own** — it **holds the two
pars containers** and **declares their distinction**.

**The two pars have DIFFERENT clinical associations:**

*   **Pars compacta** — **Parkinson's disease** (DIRECT — the
    primary substrate) — the **loss of the nigrostriatal
    dopaminergic neurons** produces the **motor symptoms** of
    Parkinson's disease (resting tremor, rigidity, bradykinesia,
    postural instability).
*   **Pars reticulata** — **saccade disorders** (DIRECT — the
    inhibitory gate on the superior colliculus) — **PSP** (with
    the **riMLF** — the vertical gaze palsy and the loss of
    saccade inhibition) — **slow saccades**, **saccade
    hypometria**.

**The two pars' clinical associations are DISTINCT** — **not
interchangeable** — **which is why the two pars are separate
structures, not interchangeable subdivisions**.

Lateralization Notes
--------------------
This is the **substantia_nigra** multi-part structure container —
its structural children are the **pars_compacta** (container with
`left/` and `right/` leaves) and the **pars_reticulata** (container
with `left/` and `right/` leaves). **The left and right substantia
nigra are BILATERALLY SYMMETRIC paired structures** — each has the
same two pars, same connectomes, same functions. **The two sides
are coordinated via their bilateral projections** — the
**striatonigral** and **nigrostriatal** pathways are bilateral, and
the **pars reticulata** projects to bilateral targets — **not via
intrinsic left-right coupling**.

*   **Paired Structure — Two Independent Substantia Nigra:** Each
    side is an **independent substantia nigra** — the **left
    substantia nigra** (with the **left pars compacta** and the
    **left pars reticulata**) and the **right substantia nigra**
    (with the **right pars compacta** and the **right pars
    reticulata**). **The two sides are structurally symmetric** —
    same two pars, same connectomes, same functions.

*   **NO Coupling Warning — neither pars is an oscillator.** The
    **pre-Bötzinger complex** carries a **coupling warning**
    because it is an **oscillator** whose two sides must
    synchronize to produce a single rhythm. **Neither the pars
    compacta (dopaminergic neuromodulatory) nor the pars
    reticulata (GABAergic inhibitory) is an oscillator** — they
    do **not** generate a rhythm. **The left and right
    substantia nigra are coordinated** via their **bilateral
    projections** — **not via intrinsic left-right coupling**.
    **NO coupling warning** — same rule as every non-oscillator
    class.

*   **No SLEA Warning:** The substantia nigra is **SLEA-free** —
    it is **not** an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The substantia nigra
    is **not** part of the amygdala — it does **not** inherit
    the amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The substantia nigra is
    **not** a rhinencephalon structure.

**The substantia nigra is a strict mirror pair with the left and
right sides structurally identical** — the **two pars are
distinct** within each side, but the **left and right sides are
symmetric**. **The pars leaves** (the `pars_compacta/left`,
`pars_compacta/right`, `pars_reticulata/left`,
`pars_reticulata/right`) are the substantive anatomical leaves —
**each pars container holds its own left and right leaves** — **the
multi-part structure-container pattern is the recursive version of
the single-part structure-container pattern**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** This multi-part structure
    container does **not** import from ``.../pars_compacta/`` or
    ``.../pars_reticulata/`` at the container level — the
    container's `__init__.py` is **namespace only**. The **pars
    containers** are children; the **pars leaves** are
    grandchildren. **Each leaf carries its own cross-hemisphere
    rules** (the left leaf does not import from the right, and
    vice versa).
*   **No cross-lobe imports.** This module does **not** import
    from the **striatum**, the **globus pallidus**, the
    **subthalamic nucleus**, the **thalamus**, the **superior
    colliculus**, the **VTA**, the **red nucleus**, the
    **cerebral peduncle**, the **tegmentum proper**, the **CN
    nuclei**, the **basal ganglia**, or any other container. The
    substantia nigra's relationships to these structures are
    documented as **prose and boundary data** in the **pars
    leaves** — not re-stated here.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **pars
    compacta's dopaminergic phenotype** (TH, dopamine synthesis,
    dopamine transporters, dopamine receptors, neuromelanin) and
    the **pars reticulata's GABAergic phenotype** (GAD, GABA
    synthesis, GABA transporters, GABA-A / GABA-B receptors) are
    **``chemicals_hormones``-layer facts** — documented as
    **prose** in the pars leaves, **never imported**.
*   **MULTI-PART STRUCTURE CONTAINER — the FIRST multi-part
    structure container in the family.** The substantia nigra
    holds the **pars_compacta** and the **pars_reticulata** as
    **children** — each is **itself a structure container** (a
    paired structure with `left/` and `right/` leaves). **The
    multi-part structure-container pattern is the recursive
    version of the single-part structure-container pattern.**
*   **THE MULTI-PART STRUCTURE-CONTAINER PATTERN.** A **multi-part
    paired structure** (the substantia nigra) — a **multi-part
    structure container** at ``tegmentum/<structure>/`` —
    holding the **pars** as **children** — each pars being
    **itself a single-part structure container** at
    ``tegmentum/<structure>/<pars>/`` — holding **its own**
    ``left/`` and ``right/`` as **substantive paired leaves**.
    **The anatomy is in the two leaves of each pars.**
*   **TWO FUNCTIONALLY DISTINCT PARS — the pars compacta and the
    pars reticulata are DIFFERENT structures.** **The pars
    compacta** is a **dopaminergic neuromodulatory nucleus** —
    the **nigrostriatal** pathway — **Parkinson's disease**
    substrate. **The pars reticulata** is a **GABAergic
    inhibitory nucleus** — the **inhibitory gate** on saccades,
    posture, and movement — the **PSP** co-substrate (with the
    **riMLF**). **Different connectomes, different transmitters,
    different functions, different clinical associations.**
    Consumers must **not** treat the substantia nigra as a single
    undifferentiated structure — **go one level deeper to the
    specific pars**.
*   **PAIRED STRUCTURE — each pars is paired.** The substantia
    nigra is a **paired structure**, and **each pars is itself
    paired** — the **pars compacta container** holds the **left
    pars compacta** and the **right pars compacta**; the **pars
    reticulata container** holds the **left pars reticulata** and
    the **right pars reticulata**.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER.** The tegmentum
    container's **paired-leaf rule** — *"each tegmentum nucleus
    is a paired structure (a ``left/`` leaf and a ``right/``
    leaf)"* — should be **AMENDED** to acknowledge **FOUR
    patterns**:
    *   **Paired single-part structure containers** — the **red
        nucleus**, the **riMLF** (substantive paired leaves).
    *   **Paired multi-part structure containers** — the
        **substantia nigra** (pars children, each pars itself
        paired).
    *   **Midline leaves** — the **RLi** (the **actual clean
        on-disk example**; the **CLi**, **DR**, **IPN** —
        **pending the joint Resolution B**).
    *   **Diffuse bilateral leaves** — the **PAG** (the
        **actual clean on-disk example**; the **MRF** —
        **pending Resolution B**).
    **The amendment's evidence base is now MORE FULLY
    EVIDENCED** — **the paired single-part structure containers**
    (red nucleus, riMLF), the **paired multi-part structure
    container** (substantia nigra — this module), the **midline
    leaves** (the RLi — **the actual clean on-disk example**;
    the CLi, DR, IPN — anomalous, pending the joint
    Resolution B), and the **diffuse bilateral leaves** (the
    PAG — the actual clean on-disk example; the MRF —
    anomalous). **The substantia nigra provides the clean on-disk
    example for the multi-part structure-container pattern.**
*   **NOT the VTA — the VTA is a SEPARATE dopaminergic nucleus.**
    Different dopaminergic cell groups (A9 vs. A10), different
    projections (striatum vs. nucleus accumbens / prefrontal
    cortex / amygdala), different clinical associations
    (Parkinson's disease vs. addiction and reward processing).
*   **NOT the red nucleus — the red nucleus is the LIMB-MOTOR
    premotor relay.**
*   **NOT the cerebral peduncle — the peduncle is VENTRAL to the
    substantia nigra (white matter, not grey matter).**
*   **NOT the globus pallidus — the globus pallidus is
    TELENCEPHALIC.** The **pars reticulata** is the **midbrain**
    homologue of the **globus pallidus internus**.
*   **NOT the striatum — the striatum is the UPSTREAM INPUT.** The
    substantia nigra receives from the striatum (striatonigral)
    and projects to the striatum (nigrostriatal).
*   **NOT the subthalamic nucleus — the subthalamic nucleus is
    DIENCEPHALIC.** The substantia nigra pars reticulata receives
    from the subthalamic nucleus.
*   **NOT the PAG, the MRF, the CLi, the DR, the IPN, the RLi, or
    the riMLF — different tegmentum structures.**
*   **DOPAMINERGIC (pars compacta) AND GABAergic (pars reticulata)
    — the phenotypes are ``chemicals_hormones``-layer facts.**
    Documented as **prose** in the pars leaves, **never
    imported**. The **"black" color** (neuromelanin) is a
    **dopamine-metabolism byproduct** specific to the **pars
    compacta** — a **``chemicals_hormones``-layer fact**.
*   **NO COUPLING WARNING — neither pars is an oscillator.**
    **The substantia nigra pair is a strict mirror with NO
    warning.**
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The substantia
    nigra is a **local multi-part structure container** under
    the tegmentum — no cross-listing.
*   **No nested cross-listing** at the container level. The
    substantia nigra container's **structural children are the
    pars_compacta and the pars_reticulata** — each is **itself
    a structure container** with its own leaves.
*   **The on-disk tree is authoritative.** If the tree has
    ``.../tegmentum/substantia_nigra/pars_compacta/left/``,
    ``.../tegmentum/substantia_nigra/pars_compacta/right/``,
    ``.../tegmentum/substantia_nigra/pars_reticulata/left/``,
    and ``.../tegmentum/substantia_nigra/pars_reticulata/right/``,
    the **multi-part structure-container** representation is
    authoritative.

Usage
-----
Resolve the multi-part structure container by path::

    from infrastructure.brainparts.midbrain.tegmentum import substantia_nigra

Resolve a pars container by path::

    from infrastructure.brainparts.midbrain.tegmentum.substantia_nigra import pars_compacta
    from infrastructure.brainparts.midbrain.tegmentum.substantia_nigra import pars_reticulata

Resolve a pars leaf by path::

    from infrastructure.brainparts.midbrain.tegmentum.substantia_nigra.pars_compacta.left import (
        PARS_COMPACTA_LEFT_CHILDREN,
    )
    # (and similarly for the other three leaves)

Or by fully-qualified path string (leaves, not the container)::

    snc_left_path = (
        "midbrain.tegmentum.substantia_nigra.pars_compacta.left"
    )
    snc_right_path = (
        "midbrain.tegmentum.substantia_nigra.pars_compacta.right"
    )
    snr_left_path = (
        "midbrain.tegmentum.substantia_nigra.pars_reticulata.left"
    )
    snr_right_path = (
        "midbrain.tegmentum.substantia_nigra.pars_reticulata.right"
    )

**Do not** assume the substantia nigra is a **single
undifferentiated structure** — it is a **multi-part structure
container** — the **two pars are FUNCTIONALLY AND NEUROCHEMICALLY
DISTINCT structures** (dopaminergic pars compacta vs. GABAergic
pars reticulata). **Go one level deeper to the specific pars**.

**Do not** assume the substantia nigra is a **midline nucleus** or
a **diffuse bilateral region** — it is a **paired multi-part
structure** — **each pars is paired** — **the multi-part
structure-container pattern applies recursively**.

**Do not** assume the substantia nigra is a **cranial nerve
nucleus** — it is **not** and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the substantia nigra is the **VTA** — the VTA is
a **separate dopaminergic nucleus** (A10 vs. A9), **different
projections** (nucleus accumbens / prefrontal cortex / amygdala
vs. striatum), **different clinical associations** (addiction and
reward processing vs. Parkinson's disease).

**Do not** assume the substantia nigra is the **red nucleus** —
the red nucleus is the **limb-motor premotor relay**.

**Do not** assume the substantia nigra is the **cerebral
peduncle** — the peduncle is **ventral** to the substantia nigra
(white matter, not grey matter).

**Do not** assume the substantia nigra is the **globus pallidus** —
the globus pallidus is **telencephalic**; the **pars reticulata**
is the **midbrain** homologue of the **globus pallidus
internus**.

**Do not** assume the substantia nigra is the **striatum** — the
striatum is the **upstream input**.

**Do not** assume the substantia nigra is the **subthalamic
nucleus** — the subthalamic nucleus is **diencephalic**.

**Do not** import the **dopaminergic phenotype** (pars compacta) or
the **GABAergic phenotype** (pars reticulata) into the midbrain
structural layer. Both are **``chemicals_hormones``-layer facts**.
**The "black" color** (neuromelanin) is a **dopamine-metabolism
byproduct** specific to the **pars compacta** — a
**``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the substantia
nigra — **neither pars is an oscillator** — same rule as every
non-oscillator class.

Iterating the substantia nigra's children (recommended consumer
pattern)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tegmentum.substantia_nigra as sn_pkg

    SUBSTANTIA_NIGRA_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(sn_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("pars_compacta", "pars_reticulata")
    #
    # Each pars is itself a structure container — the pars_compacta
    # container holds the left and right pars compacta leaves; the
    # pars_reticulata container holds the left and right pars
    # reticulata leaves.

Reaching the pars compacta container (recommended consumer pattern
— the DOPAMINERGIC pars)::

    # The pars compacta container holds the left and right pars
    # compacta — the dopaminergic nigrostriatal pathway — the
    # Parkinson's disease substrate:
    #
    #   brainparts.midbrain.tegmentum.substantia_nigra.pars_compacta
    #
    # The pars compacta is the DOPAMINERGIC pars (A9 group); the
    # pars reticulata is the GABAergic pars.

Reaching the pars reticulata container (recommended consumer pattern
— the GABAergic pars)::

    # The pars reticulata container holds the left and right pars
    # reticulata — the GABAergic inhibitory gate on the superior
    # colliculus and the thalamus — the PSP co-substrate with the
    # riMLF:
    #
    #   brainparts.midbrain.tegmentum.substantia_nigra.pars_reticulata
    #
    # The pars reticulata is the GABAergic pars; the pars compacta
    # is the dopaminergic pars.

Reaching the left/right pars compacta leaves (recommended consumer
pattern — the SUBSTANTIVE dopaminergic leaves)::

    # The left and right pars compacta leaves are the substantive
    # anatomy of the dopaminergic nigrostriatal pathway:
    #
    #   brainparts.midbrain.tegmentum.substantia_nigra.pars_compacta.left
    #   brainparts.midbrain.tegmentum.substantia_nigra.pars_compacta.right
    #
    # The pars compacta is the Parkinson's disease substrate; the
    # VTA (a separate dopaminergic nucleus) is the reward
    # substrate — different structures, different clinical
    # associations.

Reaching the left/right pars reticulata leaves (recommended consumer
pattern — the SUBSTANTIVE GABAergic leaves)::

    # The left and right pars reticulata leaves are the substantive
    # anatomy of the GABAergic inhibitory gate — the inhibitory
    # gate on the superior colliculus (saccade gating) and the
    # thalamus (posture and movement):
    #
    #   brainparts.midbrain.tegmentum.substantia_nigra.pars_reticulata.left
    #   brainparts.midbrain.tegmentum.substantia_nigra.pars_reticulata.right
    #
    # The pars reticulata is the PSP co-substrate (with the
    # riMLF); the pars compacta is the Parkinson's disease
    # substrate — different structures, different clinical
    # associations.

Reaching the VTA (recommended consumer pattern — the SEPARATE
dopaminergic nucleus)::

    # The ventral tegmental area (VTA) is a SEPARATE dopaminergic
    # nucleus — the A10 group — the mesolimbic / mesocortical
    # reward pathways:
    #
    #   brainparts.midbrain.tegmentum.left.ventral_tegmental_area
    #   brainparts.midbrain.tegmentum.right.ventral_tegmental_area
    #
    # The VTA is the REWARD substrate; the pars compacta is the
    # PARKINSON'S DISEASE substrate — different dopaminergic
    # nuclei, different clinical associations.

Reaching the red nucleus (recommended consumer pattern — the
LIMB-MOTOR premotor relay)::

    # The red nucleus is the LIMB-MOTOR premotor relay — the
    # rubrospinal motor coordination:
    #
    #   brainparts.midbrain.tegmentum.red_nucleus
    #
    # The red nucleus is a single-part structure container
    # (structure container with paired substantive leaves); the
    # substantia nigra is a MULTI-PART structure container
    # (multi-part structure container with two pars children,
    # each pars itself paired).

Reaching the cerebral peduncle (recommended consumer pattern — the
VENTRAL neighbor)::

    # The cerebral peduncle (crus cerebri) is the ventral-most
    # descending fiber bundle — VENTRAL to the substantia nigra:
    #
    #   brainparts.midbrain.cerebral_peduncle
    #
    # The substantia nigra sits DORSAL to the crus cerebri and
    # VENTRAL to the tegmentum proper.

Reaching the striatum (recommended consumer pattern — the UPSTREAM
INPUT)::

    # The striatum is the upstream input to the substantia nigra
    # (striatonigral) and the downstream target of the pars
    # compacta (nigrostriatal):
    #
    #   brainparts.forebrain.telencephalon.subcortical.basal_ganglia.striatum
    #
    # The striatum is TELENCEPHALIC; the substantia nigra is
    # MESENCEPHALIC — different structures across a lobe boundary.

The multi-part structure-container pattern — detail (not wired —
structural note)::

    # The substantia nigra is the FIRST MULTI-PART STRUCTURE
    # CONTAINER in the family:
    #
    #   tegmentum/substantia_nigra/          (MULTI-PART STRUCTURE
    #     ├── pars_compacta/                  CONTAINER — the two
    #     │   ├── left/                       PARS as children)
    #     │   └── right/
    #     └── pars_reticulata/
    #         ├── left/
    #         └── right/
    #
    # The pattern is the RECURSIVE version of the single-part
    # structure-container pattern:
    #   - SINGLE-PART paired structure (red nucleus, riMLF) —
    #     structure container with left/ and right/ as substantive
    #     paired leaves.
    #   - MULTI-PART paired structure (substantia nigra) —
    #     multi-part structure container with pars children, each
    #     pars being itself a single-part structure container with
    #     left/ and right/ substantive paired leaves.
    #
    # The recursion is the structural expression of the two-pars
    # split — the two pars are DISTINCT STRUCTURES (dopaminergic
    # pars compacta vs. GABAergic pars reticulata), not just
    # subdivisions. The multi-part structure container declares
    # this distinction.
    #
    # Do not attempt to resolve the two pars as sub-paths of the
    # substantia nigra beyond their named children — the two pars
    # are the structure-container's children; their anatomy is in
    # their own left and right leaves.

Clinical-pattern detail (not wired — consult references)::

    # The two pars have DIFFERENT clinical associations:
    #
    #   PARS COMPACTA              -> PARKINSON'S DISEASE (DIRECT
    #     (dopaminergic — A9           — the primary substrate) —
    #      group)                      the loss of the
    #                                  nigrostriatal dopaminergic
    #                                  neurons produces the motor
    #                                  symptoms (resting tremor,
    #                                  rigidity, bradykinesia,
    #                                  postural instability).
    #   PARS RETICULATA            -> SACCADE DISORDERS (DIRECT —
    #     (GABAergic — the             the inhibitory gate on the
    #      inhibitory gate)            superior colliculus) — PSP
    #                                  (with the riMLF — the
    #                                  vertical gaze palsy and the
    #                                  loss of saccade inhibition) —
    #                                  slow saccades, saccade
    #                                  hypometria.
    #
    # The two pars' clinical associations are DISTINCT — not
    # interchangeable — which is why the two pars are separate
    # structures, not interchangeable subdivisions.
    #
    # Do not conflate the two pars — the pars compacta is the
    # Parkinson's disease substrate; the pars reticulata is the
    # saccade-gating and PSP co-substrate.

References
----------
*   **Canonical substantia nigra anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (The substantia nigra — its two pars (pars compacta and
    pars reticulata), its location in the ventral midbrain
    tegmentum, its connections to the striatum, the thalamus,
    and the superior colliculus.)
*   **Substantia nigra — comprehensive review:** Parent, A.,
    Hazrati, L.N. (1995). "Functional anatomy of the basal
    ganglia. I. The cortico-basal ganglia-thalamo-cortical
    loop." *Brain Research Reviews* 20:91–127. (The substantia
    nigra — the pars compacta dopaminergic input to the
    striatum; the pars reticulata GABAergic inhibitory output;
    the nigrotectal and nigrothalamic pathways.)
*   **Pars compacta — dopaminergic:** Dahlstroem, A., Fuxe, K.
    (1964). "Evidence for the existence of monoamine-containing
    neurons in the central nervous system. I. Demonstration of
    monoamines in the cell bodies of brain stem neurons." *Acta
    Physiologica Scandinavica* 62 (Suppl. 232):1–55. (The A9
    dopaminergic cell group — the pars compacta — the
    nigrostriatal pathway.)
*   **Pars reticulata — GABAergic:** Hikosaka, O., Wurtz, R.H.
    (1983). "Visual and oculomotor functions of monkey
    substantia nigra pars reticulata. I. Relation of visual and
    auditory responses to saccades." *Journal of
    Neurophysiology* 49:1230–1253. (The pars reticulata as the
    GABAergic inhibitory gate on the superior colliculus — the
    nigrotectal pathway.)
*   **Parkinson's disease — pars compacta:** Braak, H., Del
    Tredici, K., Rüb, U., de Vos, R.A.I., Jansen Steur, E.N.H.,
    Braak, E. (2003). "Staging of brain pathology related to
    sporadic Parkinson's disease." *Neurobiology of Aging*
    24:197–211. (The pars compacta dopaminergic neuron loss in
    Parkinson's disease — the primary substrate of the motor
    symptoms.)
*   **PSP — pars reticulata and riMLF:** Steele, J.C., Richardson,
    J.C., Olszewski, J. (1964). "Progressive supranuclear
    palsy." *Archives of Neurology* 10:333–359. (PSP — the
    pars reticulata and the riMLF as the two primary substrates
    for the vertical gaze palsy and the loss of saccade
    inhibition.)
*   **Substantia nigra — iron and neuromelanin:** Morris, C.M.,
    Candy, J.M., Oakley, A.E., Bloxham, C.A., Edwardson, J.A.
    (1992). "Histochemical distribution of non-haem iron in the
    human brain." *Acta Neuropathologica* 84:225–230. (The
    neuromelanin content of the pars compacta — the "black"
    color — and its relationship to iron and dopamine
    metabolism.)
*   **Substantia nigra — the basal ganglia:** Bolam, J.P.,
    Hanley, J.J., Booth, P.A.C., Bevan, M.D. (2000). "Synaptic
    organisation of the basal ganglia." *Journal of Anatomy*
    196:527–542. (The substantia nigra as part of the basal
    ganglia — the striatonigral and nigrostriatal pathways.)
*   **VTA — contrast:** Fields, H.L., Hjelmstad, G.O., Margolis,
    E.B., Nicola, S.M. (2007). "Ventral tegmental area neurons
    in learned appetitive behavior and positive
    reinforcement." *Annual Review of Neuroscience*
    30:289–316. (The VTA — the separate A10 dopaminergic
    nucleus — the mesolimbic and mesocortical reward pathways —
    contrast with the pars compacta.)
*   **Globus pallidus — contrast (the pars reticulata is the
    midbrain homologue of the GPi):** Parent, A., Hazrati, L.N.
    (1995). "Functional anatomy of the basal ganglia. II. The
    place of subthalamic nucleus and external pallidum in basal
    ganglia circuitry." *Brain Research Reviews* 20:128–154.
    (The globus pallidus internus and externus — the pars
    reticulata as the midbrain homologue of the GPi.)
*   **Subthalamic nucleus — contrast:** Hamani, C., Saint-Cyr,
    J.A., Fraser, J., Kaplitt, M., Lozano, A.M. (2007). "The
    subthalamic nucleus in the context of movement disorders."
    *Brain* 127:4–20. (The subthalamic nucleus — the
    diencephalic glutamatergic input to the pars reticulata
    and the GPi — contrast with the substantia nigra.)
*   **SLEA (contrast — the substantia nigra is not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in
    basal forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39.
    (SLEA continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; **NOT** the substantia nigra.)
*   NeuroNames — Substantia nigra; FMA — Substantia nigra.
    **The substantia nigra is a paired multi-part structure —
    each pars is paired. This container holds the pars_compacta
    and the pars_reticulata as children; each pars container
    holds the left and right leaves.**
"""