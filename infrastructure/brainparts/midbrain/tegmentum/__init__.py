"""
infrastructure.brainparts.midbrain.tegmentum
============================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── tectum
    ├── tegmentum                  <-- THIS MODULE (region container)
    │   ├── left
    │   │   ├── oculomotor_nucleus            (cross-listed with
    │   │   │                                  cranial_nerve_nuclei)
    │   │   ├── trochlear_nucleus             (cross-listed)
    │   │   ├── edinger_westphal_nucleus      (cross-listed)
    │   │   ├── mesencephalic_trigeminal_nucleus  (cross-listed)
    │   │   ├── red_nucleus
    │   │   ├── substantia_nigra
    │   │   │   ├── pars_compacta
    │   │   │   └── pars_reticulata
    │   │   ├── ventral_tegmental_area
    │   │   ├── riMLF
    │   │   ├── interstitial_nucleus_of_cajal
    │   │   ├── periaqueductal_gray
    │   │   └── midbrain_reticular_formation
    │   └── right
    │       └── ... (mirror)
    ├── pretectum
    ├── cerebral_aqueduct
    ├── cerebral_peduncle
    └── cranial_nerve_nuclei

**Primary synonym:** Midbrain tegmentum; mesencephalic tegmentum;
tegmentum mesencephali; **the tegmentum**; **the ventral midbrain**
(a functional synonym — the tegmentum is the portion of the midbrain
**ventral** to the cerebral aqueduct and the tectum).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). The tegmentum is a **region** of the **ventral
midbrain** — it is the **"covering" (tegmentum)** of the midbrain,
**ventral** to the **cerebral aqueduct** and **dorsal** to the
**cerebral peduncle** (the crus cerebri). It contains a **diverse
set of nuclei and regions** — the **oculomotor nucleus** (CN III),
the **Edinger-Westphal nucleus** (CN IIIp), the **trochlear
nucleus** (CN IV), the **mesencephalic trigeminal nucleus** (CN Vm),
the **red nucleus**, the **substantia nigra** (pars compacta and
pars reticulata), the **ventral tegmental area** (VTA), the
**periaqueductal gray** (PAG), the **rostral interstitial nucleus
of the MLF** (riMLF), the **interstitial nucleus of Cajal**, and
the **midbrain reticular formation**. It is the **largest and most
functionally diverse** compartment of the midbrain.
**Container status:** **This module is a REGION CONTAINER, not a
leaf.** It holds the **tegmentum nuclei and regions** — **paired**
where the structure is paired (the red nucleus, the substantia
nigra, the VTA, the riMLF, the interstitial nucleus of Cajal, the
PAG, the midbrain reticular formation, and the four **CN nuclei**
that are **cross-listed** with ``cranial_nerve_nuclei/``). The
container imposes **aggregation rules** on the tegmentum's children
— but does **not** itself carry a single anatomical function. Every
functional claim belongs to a **child**. See *Expected Structural
Children* and *Aggregation Rules*.
**Developmental designation:** **Mesencephalic** — the tegmentum is
**unambiguously mesencephalic**. It is the **ventral** mesencephalic
compartment — **not** the diencephalon (the thalamus, the
hypothalamus, the pretectum at the junction), **not** the hindbrain
(the pons, the medulla oblongata), **not** the telencephalon (the
cortex, the basal ganglia). **The CN nuclei it hosts** are
**mesencephalic** — **not** pontine (CN V main, VI, VII, VIII) and
**not** medullary (CN IX, X, XI, XII).
**Structural parent:** ``.../midbrain/`` → **direct child** of the
midbrain container, as a **region container** peer to ``tectum/``,
``pretectum/``, ``cerebral_aqueduct/``, ``cerebral_peduncle/``, and
``cranial_nerve_nuclei/``.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left tegmentum** — a side-scoped container
    holding the left-side tegmentum nuclei and regions.
*   ``right/`` — the **right tegmentum** — a side-scoped container
    holding the right-side tegmentum nuclei and regions.
Each of the two side containers is expected to hold:
*   **``oculomotor_nucleus/``** — **CN III somatic motor** —
    **cross-listed** with
    ``.../cranial_nerve_nuclei/left/oculomotor_nucleus/`` (and the
    right counterpart). **The tegmentum side container is the
    TOPOGRAPHIC HOME** in the tree; the ``cranial_nerve_nuclei/``
    path is the **functional grouping**. **Both paths resolve to
    the same leaf.** See *Cross-Listing Statement*.
*   **``trochlear_nucleus/``** — **CN IV somatic motor** —
    **cross-listed** with
    ``.../cranial_nerve_nuclei/left/trochlear_nucleus/`` (and the
    right counterpart).
*   **``edinger_westphal_nucleus/``** — **CN III preganglionic
    parasympathetic** — **cross-listed** with
    ``.../cranial_nerve_nuclei/left/edinger_westphal_nucleus/``
    (and the right counterpart).
*   **``mesencephalic_trigeminal_nucleus/``** — **CN V mesencephalic
    — primary sensory (proprioceptive)** — **cross-listed** with
    ``.../cranial_nerve_nuclei/left/mesencephalic_trigeminal_nucleus/``
    (and the right counterpart).
*   **``red_nucleus/``** — **the rubrospinal motor relay** — a
    **premotor motor relay** — the **rubrospinal tract** — involved
    in **motor coordination** and **gait**. **Paired** (left/right).
*   **``substantia_nigra/``** — **the substantia nigra** — a
    **container** for its two functionally distinct **pars**:
    *   **``pars_compacta/``** — the **dopaminergic** subdivision —
        projects to the **striatum** (the **nigrostriatal**
        pathway) — the **dopaminergic input** to the **basal
        ganglia**. **Parkinson's disease** substrate. **Paired**.
    *   **``pars_reticulata/``** — the **GABAergic** subdivision —
        the **inhibitory output** of the **basal ganglia** — the
        **tonic inhibitory gate** on the **superior colliculus**
        (via the **nigrotectal** pathway). **Saccade gating**
        substrate. **Paired**.
*   **``ventral_tegmental_area/``** — **the VTA** — the
    **dopaminergic** neuromodulatory nucleus — projects to the
    **nucleus accumbens**, the **prefrontal cortex**, and the
    **amygdala** (the **mesolimbic** and **mesocortical**
    pathways) — the **reward/motivation** substrate. **Paired**.
*   **``riMLF/``** — the **rostral interstitial nucleus of the
    MLF** — the **vertical saccade generator** — a **premotor
    saccade generator** — projects to the **CN III/IV nuclei** for
    **vertical saccades**. **Paired**.
*   **``interstitial_nucleus_of_cajal/``** — the **interstitial
    nucleus of Cajal** — a **vertical gaze center** — involved in
    **vertical gaze holding** and **vertical saccade integration**.
    **Paired**.
*   **``periaqueductal_gray/``** — the **PAG** — the
    **pain-modulation** and **defensive-behavior** region —
    surrounds the **cerebral aqueduct** — a **modulatory region**
    — projects to the **rostral ventromedial medulla** (RVM) for
    **descending pain modulation**, and to the **hypothalamus**,
    the **amygdala**, and the **brainstem autonomic centers** for
    **defensive behaviors** and **autonomic control**. **Paired**
    (left/right — though midline-adjacent, it is treated as
    paired in the tree).
*   **``midbrain_reticular_formation/``** — the **midbrain
    reticular formation** — a **diffuse arousal/locomotion
    region** — involved in **arousal**, **locomotion** (via the
    **mesencephalic locomotor region** — MLR), and **sensorimotor
    integration**. **Paired** (left/right — or single midline, per
    the on-disk tree).

**These are the expected children — the on-disk tree is the
authoritative source.** The container imposes the **cross-listing**
and **aggregation rules** below; the leaves impose the leaf-level
contract (boundary stacks, function, disorders, lateralization,
references) documented in the existing leaf modules.

**Boundary status (TOPOGRAPHIC HOME — the tegmentum is the
TOPOGRAPHIC PARENT of the four midbrain CN nuclei, CROSS-LISTED with
``cranial_nerve_nuclei/``):** **Boundary case — the tegmentum is the
TOPOGRAPHIC HOME of the four midbrain CN nuclei (the
**oculomotor nucleus**, the **trochlear nucleus**, the
**Edinger-Westphal nucleus**, and the **mesencephalic trigeminal
nucleus**), AND the four CN nuclei are ALSO children of
``.../cranial_nerve_nuclei/`` — **both paths resolve to the same
leaf**.** This is the **container-level completion** of the
**cross-listing** that the four CN nuclei leaves declared when they
named ``.../tegmentum/<side>/<nucleus>/`` as their **topographic
home** and ``.../cranial_nerve_nuclei/<side>/<nucleus>/`` as their
**functional home**. **The tegmentum side container is the
topographic home; the ``cranial_nerve_nuclei/`` side container is
the functional grouping.** **Both paths reach the same leaf.**
Consumers should resolve by **one** path per lookup — enumerating
**both** paths yields **duplicates** for the four CN nuclei. See
*Cross-Listing Statement*.
**Boundary status (NOT the tectum — the tectum is the DORSAL
midbrain, ABOVE the cerebral aqueduct):** **Boundary case — the
tegmentum is NOT the tectum.** The **tectum**
(``.../midbrain/tectum/``) is the **dorsal midbrain** — the
**"roof"** — **dorsal** to the **cerebral aqueduct** — containing
the **superior colliculus** and the **inferior colliculus**. The
**tegmentum** (here) is the **ventral midbrain** — the
**"covering"** — **ventral** to the **cerebral aqueduct** —
containing the **substantia nigra**, the **VTA**, the **red
nucleus**, the **PAG**, the **CN nuclei**, the **riMLF**, the
**interstitial nucleus of Cajal**, and the **midbrain reticular
formation**. **They are DIFFERENT COMPARTMENTS of the midbrain** —
the **tectum** is **dorsal**; the **tegmentum** is **ventral** —
separated by the **cerebral aqueduct**. Consumers must **not**
conflate the tegmentum with the tectum, and must **not** resolve a
tectum structure (the colliculi) through the tegmentum path (or
vice versa).
**Boundary status (NOT the pretectum — the pretectum is a SEPARATE
REGION at the DIENCEPHALON-MIDBRAIN JUNCTION):** **Boundary case —
the tegmentum is NOT the pretectum.** The **pretectum**
(``.../midbrain/pretectum/``) is a **separate region** at the
**diencephalon-midbrain junction** — **rostral** to the superior
colliculus — containing the **olivary pretectal nucleus**, the
**nucleus of the optic tract**, and the **anterior, posterior, and
medial pretectal nuclei**. **The pretectum is PUPILLARY AND
OPTOKINETIC; the tegmentum is the GENERAL VENTRAL MIDBRAIN.** They
are **different regions in different functional systems**.
Consumers must **not** conflate the tegmentum with the pretectum.
**Boundary status (NOT the cerebral peduncle — the peduncle is the
VENTRAL SURFACE, the CRUS CEREBRI, VENTRAL to the substantia
nigra):** **Boundary case — the tegmentum is NOT the cerebral
peduncle.** The **cerebral peduncle**
(``.../midbrain/cerebral_peduncle/``) is the **ventral-most
descending fiber bundle** of the midbrain — the **crus cerebri** —
**white matter** — **ventral** to the **substantia nigra**. **The
tegmentum is the GREY-MATTER + INTRINSIC midbrain** — **dorsal**
to the **substantia nigra**, **ventral** to the **cerebral
aqueduct**. **They are DIFFERENT COMPARTMENTS** — the
**tegmentum** is **grey-matter + intrinsic**; the **cerebral
peduncle** is **white-matter conduit**. The **substantia nigra**
sits **between** them — **dorsal** to the **crus cerebri**,
**ventral** to the **tegmentum proper**. **The narrow definition
of the cerebral peduncle (crus cerebri) EXCLUDES the substantia
nigra** — the substantia nigra is a **tegmentum** structure. See
``.../midbrain/cerebral_peduncle/`` for the narrow-definition
reconciliation. Consumers must **not** conflate the tegmentum with
the cerebral peduncle, and must **not** resolve a tegmentum
structure (the substantia nigra, the red nucleus, the VTA, the
PAG) through the cerebral-peduncle path.
**Boundary status (NOT the cerebral aqueduct — the aqueduct is the
MIDLINE CSF CONDUIT, DORSAL to the tegmentum):** **Boundary case —
the tegmentum is NOT the cerebral aqueduct.** The **cerebral
aqueduct** (``.../midbrain/cerebral_aqueduct/``) is the **midline
CSF conduit** — the **mesencephalic aqueduct** — connecting the
**third ventricle** (diencephalon) to the **fourth ventricle**
(hindbrain). It is a **fluid-filled space** — **NOT a neural
structure**. **The tegmentum is the NEURAL TISSUE** — **ventral**
to the **aqueduct**. The **PAG surrounds the aqueduct** — but the
**PAG is a tegmentum structure**; the **aqueduct is not**. Consumers
must **not** conflate the tegmentum with the cerebral aqueduct.
**Boundary status (NOT the cranial_nerve_nuclei FUNCTIONAL
GROUPING — the tegmentum is the TOPOGRAPHIC HOME):** **Boundary
case — the tegmentum is NOT the ``cranial_nerve_nuclei/`` functional
grouping container.** The **``cranial_nerve_nuclei/`` container**
(``.../midbrain/cranial_nerve_nuclei/``) is a **functional grouping**
— it holds the four midbrain CN nuclei **grouped by
cranial-nerve identity**. The **tegmentum** (here) is the
**topographic container** — it holds the four CN nuclei **plus**
the **substantia nigra**, the **VTA**, the **red nucleus**, the
**PAG**, the **riMLF**, the **interstitial nucleus of Cajal**, and
the **midbrain reticular formation**. **They are DIFFERENT KINDS of
container** — the **tegmentum** is **topographic**; the
**``cranial_nerve_nuclei/``** is **functional**. **Both hold the
four CN nuclei** — **cross-listed**. Consumers must **not**
conflate the tegmentum with the ``cranial_nerve_nuclei/``
container. See *Cross-Listing Statement*.
**Boundary status (NOT the whole midbrain — the tegmentum is a
SUB-REGION):** **Boundary case — the tegmentum is NOT the whole
midbrain.** The **midbrain** (``.../midbrain/``) contains the
**tectum** (dorsal), the **pretectum** (junction region), the
**cerebral_aqueduct** (midline CSF conduit), the
**cerebral_peduncle** (ventral descending fiber bundle), the
**cranial_nerve_nuclei** (functional grouping), **and** the
**tegmentum** (ventral neural tissue). **The tegmentum is one
sub-region** of the midbrain — the **ventral neural tissue**.
Consumers must **not** conflate the tegmentum with the whole
midbrain.
**Boundary status (NOT the hindbrain — the pons and the medulla
are RHOMBENCEPHALIC):** **Boundary case — the tegmentum is NOT the
hindbrain.** The **pons**
(``.../hindbrain/metencephalon/pons/``) and the **medulla oblongata**
(``.../hindbrain/myencephalon/medulla_oblongata/``) are
**rhombencephalic** — **caudal** to the midbrain, across the
**pontomesencephalic junction**. **The tegmentum is mesencephalic**
— **rostral** to the pons. Consumers must **not** conflate the
tegmentum with the pontine tegmentum (the **pons** has its **own
tegmentum** — the **pontine tegmentum** — but that is a **pontine**
structure, not a **midbrain** structure) or with the medulla.
**Boundary status (NOT the forebrain — the thalamus and the basal
ganglia are PROSENCEPHALIC):** **Boundary case — the tegmentum is
NOT the forebrain.** The **thalamus** and the **hypothalamus**
(``.../forebrain/diencephalon/``) and the **basal ganglia**
(``.../forebrain/telencephalon/.../basal_ganglia/``) are
**prosencephalic** — **rostral** to the midbrain, across the
**diencephalon-midbrain junction**. **The tegmentum is
mesencephalic**. The **substantia nigra** **projects to** the
**striatum** (the **nigrostriatal** pathway) and **receives** the
**striatal input** (the **striatonigral** pathway) — but the
**substantia nigra is midbrain**, and the **striatum is
telencephalic**. Consumers must **not** conflate the tegmentum with
the forebrain, and must **not** resolve the striatum or the
thalamus through the tegmentum path.
**Boundary status (CROSS-LISTING — the four CN nuclei are ALSO
children of ``cranial_nerve_nuclei/``):** **Boundary case — the
four midbrain CN nuclei under this container are ALSO children of
``.../cranial_nerve_nuclei/``.** The **left oculomotor nucleus**,
the **left trochlear nucleus**, the **left Edinger-Westphal
nucleus**, and the **left mesencephalic trigeminal nucleus** (and
their **right** counterparts) are reachable by **two paths**:
*   **Topographic path (this container)** —
    ``.../tegmentum/<side>/<nucleus>/``
*   **Functional path** —
    ``.../cranial_nerve_nuclei/<side>/<nucleus>/``
**Both paths resolve to the SAME leaf.** **The topographic path is
the structural home** (the tegmentum is where the CN nuclei
physically sit); the **functional path** is a **grouping by
cranial-nerve identity**. Consumers should resolve by **one** path
per lookup — enumerating **both** paths yields **duplicates** for
the four CN nuclei. See *Cross-Listing Statement*.
**Boundary status (STRUCTURE-CLASS TAXONOMY — the tegmentum holds
multiple structure classes, and NONE carries a coupling warning):**
**Boundary case — the tegmentum holds MULTIPLE structure classes**,
and **none carries a coupling warning**. The tegmentum's children
fall into several **functional classes**:
*   **CN nuclei (cross-listed)** — **somatic motor** (CN III, CN
    IV), **preganglionic parasympathetic** (EW), and **primary
    sensory** (mesV) — **no coupling warning**, same rule as the
    ``cranial_nerve_nuclei/`` leaves.
*   **Grey-matter processing nuclei** — the **substantia nigra
    pars reticulata** (the **inhibitory output** of the basal
    ganglia; the **nigrotectal** saccade gate) — **no coupling
    warning**.
*   **Dopaminergic neuromodulatory nuclei** — the **substantia
    nigra pars compacta** (the **nigrostriatal** dopaminergic
    input to the basal ganglia) and the **VTA** (the
    **mesolimbic** / **mesocortical** dopaminergic reward
    pathways) — **no coupling warning**. *(The **dopaminergic
    phenotype** is a ``chemicals_hormones``-layer fact — see
    *Design Contract*: no hormone imports.)*
*   **Premotor motor relay** — the **red nucleus** (the
    **rubrospinal** motor coordination relay) — **no coupling
    warning**.
*   **Modulatory region** — the **PAG** (pain modulation, defensive
    behavior, autonomic control) — **no coupling warning**.
*   **Premotor saccade generators** — the **riMLF** and the
    **interstitial nucleus of Cajal** (vertical saccade generation
    and integration) — **no coupling warning**.
*   **Arousal/locomotion region** — the **midbrain reticular
    formation** (arousal, the mesencephalic locomotor region, and
    sensorimotor integration) — **no coupling warning**.
**None of these classes carries a coupling warning** — the
**coupling warning attaches to OSCILLATORS** (the pre-Bötzinger
complex, the Bötzinger complex, the pFRG), and the tegmentum holds
**no oscillators**. Consumers must **not** import a coupling
warning into any tegmentum leaf. See *Lateralization Notes* and
*Design Contract*.

Overview
--------
The midbrain tegmentum is the **ventral midbrain** — the
**"covering" (tegmentum)** — **ventral** to the **cerebral
aqueduct** and **dorsal** to the **cerebral peduncle** (the crus
cerebri). It is the **largest and most functionally diverse**
compartment of the midbrain — it contains the four midbrain **CN
nuclei** (the **oculomotor nucleus**, the **trochlear nucleus**,
the **Edinger-Westphal nucleus**, and the **mesencephalic
trigeminal nucleus** — **cross-listed** with
``cranial_nerve_nuclei/``), the **red nucleus** (the rubrospinal
motor relay), the **substantia nigra** (pars compacta and pars
reticulata — the dopaminergic nigrostriatal input and the
GABAergic nigrotectal output), the **ventral tegmental area** (the
mesolimbic / mesocortical dopaminergic reward nucleus), the
**periaqueductal gray** (pain modulation and defensive behavior),
the **riMLF** and the **interstitial nucleus of Cajal** (vertical
saccade generators), and the **midbrain reticular formation**
(arousal and locomotion). The tegmentum is a **region container**
under the midbrain — its children are the **tegmentum nuclei and
regions**, paired where the structure is paired, with the four
**CN nuclei cross-listed** between ``cranial_nerve_nuclei/`` and
``tegmentum/``.

**The tegmentum is the TOPOGRAPHIC HOME of the four midbrain CN
nuclei.** The four CN nuclei are reachable by **both** the
**topographic path** (``.../tegmentum/<side>/<nucleus>/``) **and**
the **functional path**
(``.../cranial_nerve_nuclei/<side>/<nucleus>/``). **The
topographic path is the structural home** (the CN nuclei physically
sit in the tegmentum); the **functional path** is a grouping by
cranial-nerve identity. **Both paths reach the same leaf.** See
*Cross-Listing Statement*.

**The tegmentum is the CONTAINER, NOT a functional leaf.** Every
functional claim belongs to a **child** — the **substantia nigra**
for the nigrostriatal dopaminergic input and the nigrotectal
inhibitory gate; the **VTA** for the mesolimbic / mesocortical
dopaminergic reward pathways; the **red nucleus** for the
rubrospinal motor relay; the **PAG** for pain modulation and
defensive behavior; the **riMLF** and the **interstitial nucleus of
Cajal** for vertical saccade generation; the **midbrain reticular
formation** for arousal and locomotion; and the four **CN nuclei**
for their respective CN functions. Consumers must resolve the
**child** that carries the function.

**The tegmentum is a PAIRED-STRUCTURE region.** Every tegmentum
nucleus is **paired** (a `left/` leaf and a `right/` leaf) — with
the **exception** of the **midbrain reticular formation**, which
may be a **midline region** spanning both sides in some atlas
conventions. The **PAG** is a **midline-adjacent region** but is
treated as **paired** in the tree (it surrounds the aqueduct on
both sides). **The on-disk tree is authoritative** for which
structures are paired.

**The tegmentum holds NO OSCILLATORS.** Every tegmentum leaf is
**no coupling warning** — the **CN nuclei** (somatic motor,
preganglionic parasympathetic, primary sensory), the **red
nucleus** (premotor motor relay), the **substantia nigra** (pars
compacta = dopaminergic neuromodulatory; pars reticulata =
GABAergic inhibitory gate), the **VTA** (dopaminergic
neuromodulatory), the **PAG** (modulatory region), the **riMLF**
and the **interstitial nucleus of Cajal** (premotor saccade
generators), and the **midbrain reticular formation**
(arousal/locomotion). **None is an oscillator** — the coupling
warning attaches to the **pre-Bötzinger complex**, the **Bötzinger
complex**, and the **pFRG** in the medulla, **not** to any
tegmentum structure.

Cross-Listing Statement
-----------------------
The **four midbrain CN nuclei** are **cross-listed** between
``.../tegmentum/<side>/`` and
``.../cranial_nerve_nuclei/<side>/`` — the same leaf is reachable
by **two** side-scoped paths:

*   **Topographic path (structural home)** —
    ``.../tegmentum/<side>/<nucleus>/``
*   **Functional path (cranial-nerve grouping)** —
    ``.../cranial_nerve_nuclei/<side>/<nucleus>/``

**Both paths resolve to the SAME leaf.** **The topographic path is
the structural home** — the four CN nuclei **physically sit** in the
**tegmentum**. **The functional path** — the
``cranial_nerve_nuclei/`` container — is a **grouping by
cranial-nerve identity**, the way a clinician frames them.

**Consumers should resolve the CN nuclei by ONE path** — not by
both. Enumerating **both** paths yields **duplicates** for the four
CN nuclei. **This is the same cross-listing mechanism** used
between ``tectum/left/`` and ``tectum/corpora_quadrigemina/left/``
(for the two colliculi). The **tegmentum is the SUPERSET of the
``cranial_nerve_nuclei/`` container's four CN nuclei** — the
``cranial_nerve_nuclei/`` container is a **functional subset** of
the tegmentum's **substantive** leaves.

**The six earlier midbrain leaves** (left/right ×
`oculomotor_nucleus`, `edinger_westphal_nucleus`,
`mesencephalic_trigeminal_nucleus`, `trochlear_nucleus`) were
written naming **both** parents (`cranial_nerve_nuclei/<side>/` and
`tegmentum/<side>/`) — this container **confirms those paths as its
children**, and **completes the cross-listing** from the container
side.

**The tegmentum is the TOPOGRAPHIC HOME; the
``cranial_nerve_nuclei/`` is the FUNCTIONAL GROUPING.** Both are
**valid paths** to the same leaf — the distinction is **framing**,
not **structure**.

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
The tegmentum container is expected to hold **two side containers**
(``left/`` and ``right/``), each holding the **tegmentum nuclei and
regions**:

**Cross-listed CN nuclei** (topographic home; functional grouping
in ``cranial_nerve_nuclei/``):
*   ``oculomotor_nucleus/`` — CN III somatic motor.
*   ``trochlear_nucleus/`` — CN IV somatic motor.
*   ``edinger_westphal_nucleus/`` — CN III preganglionic
    parasympathetic.
*   ``mesencephalic_trigeminal_nucleus/`` — CN V mesencephalic
    primary sensory (proprioceptive).

**Tegmentum's own substantive leaves:**
*   ``red_nucleus/`` — the **rubrospinal motor relay** — the
    **rubrospinal tract** — motor coordination and gait.
*   ``substantia_nigra/`` — the **substantia nigra** —
    **container** with two **pars**:
    *   ``pars_compacta/`` — **dopaminergic** — nigrostriatal
        input to the basal ganglia.
    *   ``pars_reticulata/`` — **GABAergic** — nigrotectal
        inhibitory gate on the superior colliculus; saccade
        gating.
*   ``ventral_tegmental_area/`` — the **VTA** — **dopaminergic**
    — mesolimbic / mesocortical reward pathways.
*   ``riMLF/`` — the **rostral interstitial nucleus of the MLF** —
    vertical saccade generator.
*   ``interstitial_nucleus_of_cajal/`` — the **interstitial nucleus
    of Cajal** — vertical gaze center.
*   ``periaqueductal_gray/`` — the **PAG** — pain modulation,
    defensive behavior, autonomic control.
*   ``midbrain_reticular_formation/`` — the **midbrain reticular
    formation** — arousal, the **mesencephalic locomotor region**
    (MLR), sensorimotor integration.

**These are the expected children — the on-disk tree is the
authoritative source.** The container imposes the **cross-listing**
and **aggregation rules** below; the leaves impose the leaf-level
contract documented in the existing leaf modules.

Aggregation Rules (the container's contract on its children)
------------------------------------------------------------
The tegmentum container **imposes the following rules** on every
leaf under it. These are **inherited** from the midbrain container
and are **specialized** for the tegmentum's role as a **topographic
parent** with **cross-listed CN nuclei** and **multiple structure
classes**:

*   **TOPOGRAPHIC-CONTAINER DISCIPLINE.** The tegmentum is a
    **topographic** container — it holds the **nuclei and regions**
    that **physically sit** in the **ventral midbrain**. It is
    **NOT a functional grouping** — that is the
    ``cranial_nerve_nuclei/`` container's role. Consumers should
    resolve the tegmentum by **topographic identity** (where does
    this structure sit?), not by **function** (what does it do?).
*   **CROSS-LISTING DISCIPLINE.** The **four CN nuclei** are
    **cross-listed** between ``.../tegmentum/<side>/`` and
    ``.../cranial_nerve_nuclei/<side>/``. **Both paths resolve to
    the SAME leaf.** Consumers should resolve by **one** path per
    lookup — enumerating **both** paths yields **duplicates** for
    the four CN nuclei.
*   **NO DUPLICATE LEAVES.** The four CN nuclei under the tegmentum
    are the **same four leaves** as under the
    ``cranial_nerve_nuclei/`` container — **not** duplicate
    structures. The **tegmentum is the SUPERSET** of the
    ``cranial_nerve_nuclei/`` container's leaves — it holds the
    four CN nuclei **plus** the red nucleus, the substantia nigra,
    the VTA, the PAG, the riMLF, the interstitial nucleus of Cajal,
    and the midbrain reticular formation.
*   **MULTI-CLASS DISCIPLINE.** The tegmentum holds **multiple
    structure classes** — the **CN nuclei** (somatic motor,
    preganglionic parasympathetic, primary sensory), the **grey-
    matter processing nuclei** (substantia nigra pars reticulata),
    the **dopaminergic neuromodulatory nuclei** (substantia nigra
    pars compacta, VTA), the **premotor motor relay** (red
    nucleus), the **modulatory region** (PAG), the **premotor
    saccade generators** (riMLF, interstitial nucleus of Cajal),
    and the **arousal/locomotion region** (midbrain reticular
    formation). **Every class carries NO coupling warning** —
    same rule as the CN nuclei and every non-oscillator class.
*   **CHEMICALS-LAYER DISCIPLINE.** The **dopaminergic phenotype**
    of the **substantia nigra pars compacta** and the **VTA** is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the leaves, **never imported**. Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **SUBSTANTIA NIGRA PARS DISCIPLINE.** The **substantia nigra**
    is a **container** with two **pars** —
    ``pars_compacta/`` (the **dopaminergic** subdivision) and
    ``pars_reticulata/`` (the **GABAergic** subdivision). Consumers
    must **not** treat the substantia nigra as a **single
    undifferentiated** structure — the two pars have **distinct
    connectomes**, **distinct functions**, and **distinct
    transmitters** (dopamine vs. GABA). Consumers resolving the
    substantia nigra must go **one level deeper** to the specific
    **pars**.
*   **NO COUPLING WARNING.** No tegmentum leaf carries a
    **coupling warning** — the coupling warning attaches to
    **oscillators** (the pre-Bötzinger complex, the Bötzinger
    complex, the pFRG), and the tegmentum holds **no oscillators**.
    Consumers must **not** import a coupling warning into any
    tegmentum leaf.
*   **PAIRED-LEAF DISCIPLINE.** Each tegmentum nucleus is a **paired
    structure** (a `left/` leaf and a `right/` leaf) — with the
    **possible exception** of the midbrain reticular formation
    (which may be a single midline region). The **PAG** is
    **midline-adjacent** but is **paired** in the tree. The
    **on-disk tree is authoritative** for which structures are
    paired.
*   **ROSTROCAUDAL-ANCHOR DISCIPLINE.** The tegmentum spans the
    **whole midbrain rostrocaudally** — the four CN nuclei and the
    red nucleus are at the **superior colliculus level**
    (except the trochlear, at the inferior colliculus level); the
    substantia nigra, the VTA, the PAG, the riMLF, the interstitial
    nucleus of Cajal, and the midbrain reticular formation are
    distributed across both levels. **The collicular levels are the
    anchors** (the superior colliculus for the CN III/EW/mesV
    group and the red nucleus; the inferior colliculus for the
    trochlear nucleus).
*   **CONSISTENT with the midbrain, cranial_nerve_nuclei, tectum,
    pretectum, and cerebral_peduncle container child lists.**
    Consumers reading any of those container docstrings should
    find the tegmentum's child list **consistent** with theirs.
*   **The on-disk tree is authoritative.** The expected children
    listed above are the **standard tegmentum nuclei and regions**;
    the actual children are **whatever exists on disk**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-lobe imports.** The tegmentum container does **not**
    import from ``../forebrain/`` or ``../hindbrain/``. The
    tegmentum's relationships to the **tectum**, the **pretectum**,
    the **cerebral peduncle**, the **cerebral aqueduct**, the
    **cranial_nerve_nuclei** functional grouping, the **pons**, the
    **medulla oblongata**, the **thalamus**, the **hypothalamus**,
    the **basal ganglia**, the **superior colliculus**, the
    **inferior colliculus**, the **PPRF**, the **CN III/IV/VI
    nuclei**, the **pulvinar**, the **LGN**, the **SNr**, the
    **striatum**, the **nucleus accumbens**, the **prefrontal
    cortex**, the **amygdala**, the **RVM**, the **hypothalamus**,
    and the **brainstem autonomic centers** are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **dopaminergic phenotype** of the substantia nigra pars
    compacta and the VTA is a ``chemicals_hormones``-layer fact —
    documented as **prose** in the leaves, **never imported**.
*   **REGION CONTAINER — not a leaf.** The tegmentum is a **region
    container** — it has **no anatomical function of its own**;
    every functional claim belongs to a **child**.
*   **CROSS-LISTING via ``AREA_PATHS``.** The four CN nuclei are
    cross-listed between ``.../tegmentum/<side>/`` and
    ``.../cranial_nerve_nuclei/<side>/``. **The tegmentum is the
    SUPERSET**; the ``cranial_nerve_nuclei/`` container is a
    **functional subset** of the tegmentum's substantive leaves.
*   **CONSISTENT with the ``midbrain``, ``cranial_nerve_nuclei``,
    ``tectum``, ``pretectum``, and ``cerebral_peduncle`` container
    child lists.** All these containers place the four CN nuclei
    under BOTH ``tegmentum/`` and ``cranial_nerve_nuclei/`` — the
    tegmentum is the **topographic home** and
    ``cranial_nerve_nuclei/`` is the **functional grouping**.
*   **CN NUCLEI — TOPOGRAPHIC HOME.** The four midbrain CN nuclei
    **physically sit** in the tegmentum; the tegmentum is the
    **topographic home** in the tree.
*   **TEGMENTUM'S OWN SUBSTANTIVE LEAVES.** The red nucleus, the
    substantia nigra (pars compacta and pars reticulata), the VTA,
    the riMLF, the interstitial nucleus of Cajal, the PAG, and the
    midbrain reticular formation are the **tegmentum's own
    substantive leaves** — **not** cross-listed with any other
    container.
*   **SUBSTANTIA NIGRA — container with two pars.** The
    substantia nigra has a **pars compacta** (dopaminergic) and a
    **pars reticulata** (GABAergic) — **distinct connectomes,
    distinct functions, distinct transmitters**.
*   **MULTI-CLASS DISCIPLINE.** The tegmentum holds **multiple
    structure classes** — **all carry NO coupling warning**.
*   **NO coupling warning.** The tegmentum holds **no oscillators**
    — consumers must **not** import a coupling warning into any
    tegmentum leaf.
*   **CHEMICALS-LAYER DISCIPLINE.** The **dopaminergic phenotype**
    of the substantia nigra pars compacta and the VTA is a
    ``chemicals_hormones``-layer fact — documented as **prose**,
    **never imported**.
*   **NOT the tectum — the tectum is the DORSAL midbrain.**
*   **NOT the pretectum — the pretectum is a SEPARATE REGION at the
    junction.**
*   **NOT the cerebral peduncle — the peduncle is the VENTRAL
    SURFACE, the crus cerebri.**
*   **NOT the cerebral aqueduct — the aqueduct is the MIDLINE CSF
    CONDUIT.**
*   **NOT the cranial_nerve_nuclei functional grouping — the
    tegmentum is the TOPOGRAPHIC HOME.**
*   **NOT the whole midbrain — a SUB-REGION.**
*   **NOT the hindbrain — the pons and the medulla are
    RHOMBENCEPHALIC.** The pons has its **own** tegmentum (the
    pontine tegmentum) — but that is a **pontine** structure.
*   **NOT the forebrain — the thalamus and the basal ganglia are
    PROSENCEPHALIC.**
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/<side>`` ↔
    ``cranial_nerve_nuclei/<side>``) — not into the forebrain,
    hindbrain, or periphery.
*   **No nested cross-listing.** The tegmentum is a **single region
    container**. Its children are the **tegmentum nuclei and
    regions** — with the four CN nuclei cross-listed at the leaf
    level (not at the container level).
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts.midbrain import tegmentum

Resolve a tegmentum leaf by path::

    from infrastructure.brainparts.midbrain.tegmentum.left import red_nucleus
    from infrastructure.brainparts.midbrain.tegmentum.left.substantia_nigra import pars_reticulata
    from infrastructure.brainparts.midbrain.tegmentum.left import ventral_tegmental_area

Resolve a cross-listed CN nucleus by **either** path (they are
equivalent)::

    # Topographic path (structural home — the tegmentum):
    from infrastructure.brainparts.midbrain.tegmentum.left import oculomotor_nucleus

    # Functional path (the cranial_nerve_nuclei grouping):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left import oculomotor_nucleus

    # Both resolve to the SAME leaf.

Or by fully-qualified path string::

    tegmentum_oculomotor_path = (
        "midbrain.tegmentum.left.oculomotor_nucleus"
    )
    cnn_oculomotor_path = (
        "midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus"
    )
    # Both resolve to the SAME leaf.

**Do not** assume the tegmentum is the **tectum**. The **tectum**
is the **dorsal midbrain** — the **colliculi** — **dorsal** to the
cerebral aqueduct. The **tegmentum** is the **ventral midbrain** —
**ventral** to the cerebral aqueduct. **Different compartments,
different structures.**

**Do not** assume the tegmentum is the **pretectum**. The
**pretectum** is a **separate region** at the diencephalon-midbrain
junction. **Different regions, different functional systems.**

**Do not** assume the tegmentum is the **cerebral peduncle**. The
**cerebral peduncle** is the **ventral-most descending fiber
bundle** of the midbrain — the **crus cerebri** — **white matter**.
The **tegmentum** is the **grey-matter + intrinsic midbrain** —
**dorsal** to the **substantia nigra**. **Different compartments,
different structures.**

**Do not** assume the tegmentum is the **cerebral aqueduct**. The
**cerebral aqueduct** is the **midline CSF conduit** — a
**fluid-filled space**. The **tegmentum** is the **neural tissue**
— **ventral** to the aqueduct. **Different structures, different
kinds of structure.**

**Do not** assume the tegmentum is the **cranial_nerve_nuclei
functional grouping**. The **tegmentum** is the **topographic
home** of the four midbrain CN nuclei; the
**``cranial_nerve_nuclei/``** is a **functional grouping** — a
**different path** to the **same four leaves**. **Both are valid —
the distinction is framing.**

**Do not** assume the tegmentum is the **whole midbrain**. It is a
**sub-region** — the **ventral neural tissue**.

**Do not** assume the tegmentum is the **hindbrain**. The **pons**
and the **medulla oblongata** are **rhombencephalic**. The pons has
its **own** tegmentum (the pontine tegmentum) — but that is a
**pontine** structure, not the **midbrain** tegmentum.

**Do not** assume the tegmentum is the **forebrain**. The
**thalamus**, the **hypothalamus**, and the **basal ganglia** are
**prosencephalic**. The **substantia nigra** **projects to** the
**striatum** — but the **substantia nigra is midbrain** and the
**striatum is telencephalic**.

**Do not** resolve the four midbrain CN nuclei by **both** paths in
a single lookup. Use **one** path — the **topographic path**
(``tegmentum/<side>/<nucleus>``) or the **functional path**
(``cranial_nerve_nuclei/<side>/<nucleus>``). Enumerating **both**
paths yields **duplicates**.

**Do not** treat the **substantia nigra** as a **single
undifferentiated** structure. It has **two pars** — the
**pars_compacta** (dopaminergic; the nigrostriatal dopaminergic
input to the basal ganglia) and the **pars_reticulata** (GABAergic;
the nigrotectal inhibitory gate on the superior colliculus).
**Distinct connectomes, distinct functions, distinct transmitters.**
Go **one level deeper** to the specific **pars**.

**Do not** import the **dopaminergic phenotype** of the substantia
nigra pars compacta or the VTA into the midbrain structural layer.
The **dopaminergic phenotype** is a
**``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into any tegmentum leaf.
The tegmentum holds **no oscillators** — every tegmentum leaf is
**no coupling warning** — same rule as every non-oscillator class.
The **coupling warning attaches to the pre-Bötzinger complex, the
Bötzinger complex, and the pFRG** in the medulla, **not** to any
tegmentum structure.

Iterating the tegmentum's children (recommended consumer pattern —
NOTE cross-listing and the substantia nigra container)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tegmentum as tegmentum_pkg

    TEGMENTUM_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(tegmentum_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("left", "right")
    #
    # Each side container holds the tegmentum nuclei and regions:
    # cross-listed CN nuclei: oculomotor_nucleus, trochlear_nucleus,
    #                         edinger_westphal_nucleus,
    #                         mesencephalic_trigeminal_nucleus
    # tegmentum's own leaves: red_nucleus, substantia_nigra
    #                         (container — pars_compacta,
    #                         pars_reticulata), ventral_tegmental_area,
    #                         riMLF, interstitial_nucleus_of_cajal,
    #                         periaqueductal_gray,
    #                         midbrain_reticular_formation
    #
    # The four CN nuclei are ALSO children of
    # .../cranial_nerve_nuclei/<side>/. Enumerating BOTH paths yields
    # DUPLICATES. Use ONE path per lookup.

Reaching the ``cranial_nerve_nuclei/`` functional grouping
(recommended consumer pattern — the FUNCTIONAL sibling)::

    # The cranial_nerve_nuclei/ container holds the four midbrain CN
    # nuclei GROUPED BY CRANIAL-NERVE IDENTITY:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei
    #
    # The tegmentum/ is the TOPOGRAPHIC HOME of the same four CN
    # nuclei. Both paths resolve to the SAME leaves.

Reaching the tectum (recommended consumer pattern — the DORSAL
sibling)::

    # The tectum is the DORSAL MIDBRAIN — the colliculi — dorsal to
    # the cerebral aqueduct:
    #
    #   brainparts.midbrain.tectum
    #
    # The tegmentum is the VENTRAL midbrain — ventral to the
    # cerebral aqueduct. Different compartments.

Reaching the pretectum (recommended consumer pattern — the
JUNCTION sibling)::

    # The pretectum is a SEPARATE REGION at the diencephalon-
    # midbrain junction — ROSTRAL to the superior colliculus:
    #
    #   brainparts.midbrain.pretectum
    #
    # The pretectum is PUPILLARY AND OPTOKINETIC; the tegmentum is
    # the GENERAL VENTRAL MIDBRAIN. Different regions.

Reaching the cerebral peduncle (recommended consumer pattern — the
VENTRAL SURFACE sibling)::

    # The cerebral peduncle is the VENTRAL-MOST descending fiber
    # bundle — the crus cerebri — white matter — ventral to the
    # substantia nigra:
    #
    #   brainparts.midbrain.cerebral_peduncle
    #
    # The tegmentum is the GREY-MATTER + INTRINSIC midbrain — dorsal
    # to the substantia nigra. Different compartments.

Reaching the cerebral aqueduct (recommended consumer pattern — the
MIDLINE CSF conduit)::

    # The cerebral aqueduct is the MIDLINE CSF CONDUIT — a
    # fluid-filled space — dorsal to the tegmentum:
    #
    #   brainparts.midbrain.cerebral_aqueduct
    #
    # The tegmentum is the NEURAL TISSUE — ventral to the aqueduct.
    # The PAG surrounds the aqueduct, but the aqueduct is NOT
    # tegmentum.

Reaching the substantia nigra pars (recommended consumer pattern —
the TWO PARS of the substantia nigra)::

    # The substantia nigra has TWO PARS — distinct connectomes,
    # distinct functions, distinct transmitters:
    #
    #   brainparts.midbrain.tegmentum.left.substantia_nigra.pars_compacta
    #   brainparts.midbrain.tegmentum.left.substantia_nigra.pars_reticulata
    #
    # The pars_compacta is the DOPAMINERGIC subdivision — the
    # nigrostriatal input to the basal ganglia. Parkinson's disease
    # substrate.
    #
    # The pars_reticulata is the GABAERGIC subdivision — the
    # inhibitory output of the basal ganglia — the tonic inhibitory
    # gate on the superior colliculus (nigrotectal pathway).
    #
    # Do not conflate the two pars.

Reaching the superior colliculus (recommended consumer pattern —
the DORSAL neighbor, the SACCADE COMMAND LEVEL)::

    # The superior colliculus is the DORSAL neighbor — the SACCADE
    # COMMAND GENERATOR:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   OR: brainparts.midbrain.tectum.corpora_quadrigemina.left.superior_colliculus
    #
    # The substantia nigra pars reticulata PROJECTS TO the superior
    # colliculus (nigrotectal pathway) as the inhibitory gate on
    # saccade generation.

Reaching the pons and the medulla oblongata (recommended consumer
pattern — the CAUDAL siblings, the HINDBRAIN)::

    # The pons and the medulla oblongata are HINDBRAIN — rhombencephalic:
    #
    #   brainparts.hindbrain.metencephalon.pons
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata
    #
    # The pons has its OWN tegmentum (the pontine tegmentum) — but
    # that is a PONTINE structure, not the MIDBRAIN tegmentum.

Reaching the thalamus and the basal ganglia (recommended consumer
pattern — the ROSTRAL siblings, the FOREBRAIN)::

    # The thalamus and the basal ganglia are FOREBRAIN —
    # prosencephalic:
    #
    #   brainparts.forebrain.diencephalon.thalamus
    #   brainparts.forebrain.telencephalon...basal_ganglia
    #
    # The substantia nigra PROJECTS TO the striatum (nigrostriatal
    # pathway) — but the substantia nigra is MIDBRAIN and the
    # striatum is TELENCEPHALIC.

Bilateral iteration (recommended consumer pattern — NOTE the
cross-listing and the no-coupling-warning rule)::

    for side in ("left", "right"):
        for nucleus in (
            "oculomotor_nucleus",
            "trochlear_nucleus",
            "edinger_westphal_nucleus",
            "mesencephalic_trigeminal_nucleus",
            "red_nucleus",
            "ventral_tegmental_area",
            "riMLF",
            "interstitial_nucleus_of_cajal",
            "periaqueductal_gray",
            "midbrain_reticular_formation",
        ):
            # For the four CN nuclei, either path resolves to the
            # same leaf — use ONE:
            tegmentum_path = (
                f"midbrain.tegmentum.{side}.{nucleus}"
            )
            # OR for the four CN nuclei:
            # cnn_path = f"midbrain.cranial_nerve_nuclei.{side}.{nucleus}"
            #
            # For the tegmentum's OWN leaves, only the tegmentum
            # path exists:
            #
            # resolve path through the memory/recall layer
            #
            # NOTE: the tegmentum holds NO OSCILLATORS — every leaf
            # is NO coupling warning. The dopaminergic phenotype of
            # the substantia nigra pars compacta and the VTA is a
            # chemicals_hormones-layer fact — documented as prose,
            # never imported.

Substantia-nigra-pars detail (not wired — consult references)::

    # The substantia nigra has TWO PARS:
    #
    #   pars_compacta    -> DOPAMINERGIC (A9 dopaminergic cell
    #                       group) — projects to the STRIATUM
    #                       (nigrostriatal pathway) — the
    #                       dopaminergic input to the basal ganglia
    #                       — PARKINSON'S DISEASE substrate
    #   pars_reticulata  -> GABAERGIC — the INHIBITORY OUTPUT of
    #                       the basal ganglia — the TONIC INHIBITORY
    #                       GATE on the SUPERIOR COLLICULUS
    #                       (nigrotectal pathway) — SACCADE GATING
    #                       substrate
    #
    # The two pars have DISTINCT connectomes, DISTINCT functions,
    # DISTINCT transmitters. Do not conflate them. The DOPAMINERGIC
    # phenotype of the pars compacta is a chemicals_hormones-layer
    # fact — documented in the pars_compacta leaf, never imported
    # into the midbrain structural layer.

Structure-class detail (not wired — consult references)::

    # The tegmentum holds MULTIPLE STRUCTURE CLASSES:
    #
    #   CN nuclei (cross-listed)       -> somatic motor (III, IV),
    #                                     preganglionic
    #                                     parasympathetic (EW),
    #                                     primary sensory (mesV) —
    #                                     no coupling warning
    #   grey-matter processing nucleus -> substantia nigra
    #                                     pars reticulata — GABAergic
    #                                     inhibitory gate — no
    #                                     coupling warning
    #   dopaminergic neuromodulatory   -> substantia nigra
    #     nuclei                          pars compacta, VTA — no
    #                                     coupling warning (chemicals-
    #                                     layer phenotypes)
    #   premotor motor relay           -> red nucleus — rubrospinal
    #                                     tract — no coupling warning
    #   modulatory region              -> PAG — pain modulation,
    #                                     defensive behavior,
    #                                     autonomic control — no
    #                                     coupling warning
    #   premotor saccade generators    -> riMLF, interstitial nucleus
    #                                     of Cajal — vertical
    #                                     saccades — no coupling
    #                                     warning
    #   arousal/locomotion region      -> midbrain reticular
    #                                     formation — mesencephalic
    #                                     locomotor region (MLR) — no
    #                                     coupling warning
    #
    # NONE of these classes carries a coupling warning. The
    # coupling warning attaches to OSCILLATORS (the pre-Bötzinger
    # complex, the Bötzinger complex, the pFRG in the medulla) —
    # NOT to any tegmentum structure.

Rostrocaudal-anchor detail (not wired — consult references)::

    # The tegmentum spans the WHOLE MIDBRAIN rostrocaudally, with
    # the collicular levels as anchors:
    #
    #   SUPERIOR COLLICULUS level (rostral):
    #     - oculomotor nucleus (CN III) (tegmentum)
    #     - Edinger-Westphal nucleus (CN IIIp) (tegmentum)
    #     - mesencephalic trigeminal nucleus (CN Vm) (tegmentum)
    #     - red nucleus (tegmentum)
    #     - substantia nigra (tegmentum) — spanning both levels
    #     - VTA (tegmentum)
    #     - riMLF (tegmentum) — vertical saccade generator
    #     - interstitial nucleus of Cajal (tegmentum) — vertical
    #       gaze center
    #     - PAG (tegmentum) — spanning both levels
    #     - midbrain reticular formation (tegmentum) — spanning
    #       both levels
    #
    #   INFERIOR COLLICULUS level (caudal):
    #     - trochlear nucleus (CN IV) (tegmentum)
    #     - decussation of the trochlear nerve (superior medullary
    #       velum — just caudal)
    #     - decussation of the superior cerebellar peduncle (just
    #       caudal)
    #     - caudal end of the PAG
    #     - caudal end of the substantia nigra
    #     - caudal end of the midbrain reticular formation
    #
    # Do not attempt to resolve these as sub-paths of the
    # tegmentum container beyond their named children.

References
----------
*   **Canonical midbrain tegmentum anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (The midbrain tegmentum — its nuclei and regions (the red
    nucleus, the substantia nigra, the VTA, the PAG, the riMLF,
    the interstitial nucleus of Cajal, the midbrain reticular
    formation, and the four CN nuclei); the rostrocaudal
    organization; the boundaries against the tectum, the pretectum,
    and the cerebral peduncle.)
*   **Substantia nigra:** Parent, A., Hazrati, L.N. (1995).
    "Functional anatomy of the basal ganglia. I. The cortico-basal
    ganglia-thalamo-cortical loop." *Brain Research Reviews*
    20:91–127. (The substantia nigra — the pars compacta
    dopaminergic input to the striatum; the pars reticulata
    GABAergic inhibitory output; the nigrotectal pathway as the
    inhibitory gate on the superior colliculus.)
*   **Substantia nigra pars reticulata and saccade gating:**
    Hikosaka, O., Wurtz, R.H. (1983). "Visual and oculomotor
    functions of monkey substantia nigra pars reticulata. I.
    Relation of visual and auditory responses to saccades."
    *Journal of Neurophysiology* 49:1230–1253. (The substantia
    nigra pars reticulata as the inhibitory gate on the superior
    colliculus — the nigrotectal pathway.)
*   **Ventral tegmental area:** Fields, H.L., Hjelmstad, G.O.,
    Margolis, E.B., Nicola, S.M. (2007). "Ventral tegmental area
    neurons in learned appetitive behavior and positive
    reinforcement." *Annual Review of Neuroscience* 30:289–316.
    (The VTA — the dopaminergic mesolimbic and mesocortical reward
    pathways.)
*   **Red nucleus:** ten Donkelaar, H.J. (1988). "Evolution of the
    red nucleus and rubrospinal tract." *Behavioural Brain
    Research* 28:9–20. (The red nucleus — the rubrospinal motor
    relay — motor coordination and gait.)
*   **Periaqueductal gray:** Behbehani, M.M. (1995). "Functional
    characteristics of the midbrain periaqueductal gray."
    *Progress in Neurobiology* 46:575–605. (The PAG — pain
    modulation, defensive behavior, autonomic control.)
*   **riMLF and vertical saccades:** Büttner-Ennever, J.A.,
    Büttner, U. (1988). "The reticular formation." In
    *Neuroanatomy of the Oculomotor System* (Büttner-Ennever, ed.).
    (The riMLF and the interstitial nucleus of Cajal as vertical
    gaze centers — premotor saccade generators.)
*   **Midbrain reticular formation:** Shik, M.L., Orlovsky, G.N.
    (1976). "Neurophysiology of locomotor automatism."
    *Physiological Reviews* 56:465–501. (The midbrain reticular
    formation — the mesencephalic locomotor region — locomotion
    and arousal.)
*   **Cross-listing and structure-class taxonomy:** See the
    individual tegmentum leaf modules (``oculomotor_nucleus/``,
    ``trochlear_nucleus/``, ``edinger_westphal_nucleus/``,
    ``mesencephalic_trigeminal_nucleus/``, ``red_nucleus/``,
    ``substantia_nigra/``, ``ventral_tegmental_area/``, ``riMLF/``,
    ``interstitial_nucleus_of_cajal/``, ``periaqueductal_gray/``,
    ``midbrain_reticular_formation/``) for the substantive
    laterality-specific references.
*   **SLEA (contrast — the tegmentum is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the midbrain tegmentum.)
*   NeuroNames — Midbrain tegmentum; FMA — Midbrain tegmentum.
"""