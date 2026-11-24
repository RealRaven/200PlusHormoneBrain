"""
infrastructure.brainparts.midbrain.cerebral_peduncle.right.crus_cerebri
=======================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── cerebral_peduncle
        ├── left
        │   └── crus_cerebri
        └── right
            └── crus_cerebri    <-- THIS MODULE (leaf)

**Primary synonym:** Right crus cerebri; right cerebral peduncle
(narrow definition); right basis pedunculi (broad — when the
substantia nigra is included; **not** this module). The **right**
member of the paired crus cerebri.
**Cytoarchitectonic designation:** **Not a Brodmann area** and **not
a grey-matter nucleus** — the right crus cerebri is a **white-matter
fiber bundle** (a **conduction pathway**). It carries **descending
corticofugal axons**, not cell bodies. It has **no neurons of its
own**.
**Part of:** The **cerebral_peduncle** container → **right** side
container → **this leaf**. The **cerebral_peduncle** is a child of
the **midbrain** (mesencephalon) container, on the **ventral**
surface, **ventral to the substantia nigra** and the **tegmentum**.
**Structural parent:** ``.../cerebral_peduncle/right/`` → **direct
child** of the **right** side-scoped container of the cerebral
peduncle.
**Structural children:** **None.** This is a **leaf** module. The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are documented as **prose**, not as structural children.
**Boundary status (STRUCTURAL CLARIFICATION — the parent ``right/`` is
a SIDE CONTAINER, not the leaf):** **Boundary case — the right crus
cerebri is the LEAF; the ``right/`` module is the SIDE-SCOPED
CONTAINER that holds it.** The earlier ``right/__init__.py`` carried
substantive leaf-level prose **and** a Usage block resolving
``.../right.crus_cerebri`` — those framings disagreed. This module
resolves the disagreement in favor of the **tree structure**: the
``right/`` module is a **side-scoped namespace** (it holds exactly
one leaf, this one), and the **crus_cerebri** module (here) is the
**substantive leaf** that carries the white-matter-conduit prose.
Consumers that resolve ``.../cerebral_peduncle/right`` and expect a
leaf should go **one level deeper** to ``.../cerebral_peduncle/right/
crus_cerebri``. See *Design Contract* for the recommended
rebalancing of the ``right/__init__.py`` module.
**Boundary status (NOT the left crus cerebri — the SIDE
boundary):** **Boundary case — the right crus cerebri is NOT the
left crus cerebri.** The **left** leaf
(``.../cerebral_peduncle/left/crus_cerebri/``) is the **left**
crus cerebri. **They are DIFFERENT STRUCTURES** on **opposite
sides** — each carries **its own** descending axons, and each is the
**contralateral hemiplegia** substrate for an **ipsilateral**
peduncular lesion. Consumers must **not** conflate the two, and must
**not** assume a right-crus lesion produces right-sided hemiplegia —
the **corticospinal** fibers **decussate in the medulla**, **caudal**
to the crus cerebri, so a **right** crus lesion produces **left**
hemiplegia.
**Boundary status (NARROW DEFINITION — the leaf is the RIGHT CRUS
CEREBRI, NOT the whole right ventral midbrain):** **Boundary case —
the right crus cerebri is the RIGHT CRUS CEREBRI (narrow definition),
NOT the whole right ventral midbrain (broad definition).** The
**broad** classical definition (crus cerebri + substantia nigra +
tegmentum) is **rejected** — the **right tegmentum** and **right
substantia nigra** are **separate siblings** under the midbrain.
The **narrow definition** is the **only** one consistent with the
tree.
**Boundary status (NOT the right tegmentum — the right tegmentum is a
SIBLING under the midbrain):** **Boundary case — the right crus
cerebri is NOT the right tegmentum.** The **right tegmentum**
(``.../midbrain/tegmentum/right/``) contains the **right substantia
nigra**, the **right ventral tegmental area**, the **right red
nucleus**, the **right periaqueductal gray** (midline — shared), the
**right oculomotor nucleus** (CN III), the **right trochlear nucleus**
(CN IV), the **right Edinger-Westphal nucleus**, the **right
mesencephalic trigeminal nucleus** (CN V), and the **right midbrain
reticular formation**. The **right crus cerebri** (here) is the
**right descending fiber bundle** on the **right ventral surface**.
**They are DIFFERENT STRUCTURES** — the **right tegmentum** is the
**grey-matter + intrinsic** midbrain; the **right crus cerebri** is
the **white-matter conduit**. Consumers must **not** conflate the
two, and must **not** resolve a right tegmentum structure (right
substantia nigra, right red nucleus, right CN III/IV nuclei) through
the right crus cerebri path.
**Boundary status (NOT the right substantia nigra — the right
substantia nigra is a TEGMENTUM structure):** **Boundary case — the
right crus cerebri is NOT the right substantia nigra.** The **right
substantia nigra**
(``.../midbrain/tegmentum/right/substantia_nigra/``) is the
**dopaminergic** nucleus **dorsal to the right crus cerebri** — it
is a **grey-matter** structure and a **tegmentum child**. The **right
crus cerebri** (here) is the **white-matter bundle ventral to the
right substantia nigra**. **They are DIFFERENT STRUCTURES** — the
**right substantia nigra** is **grey matter**; the **right crus
cerebri** is **white matter**. Consumers must **not** conflate the
two, and must **not** resolve the right substantia nigra through the
right crus cerebri path.
**Boundary status (NOT the right internal capsule — the internal
capsule is TELENCEPHALIC):** **Boundary case — the right crus
cerebri is NOT the right internal capsule.** The **right internal
capsule**
(``.../forebrain/telencephalon/.../internal_capsule/right/``) is the
**telencephalic segment** of the **same descending pathway** — it
carries the **same** right **corticospinal**, **corticobulbar**, and
**corticopontine** axons at a **more rostral** level. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **internal
capsule** is **telencephalic**; the **right crus cerebri** is
**mesencephalic**. Consumers must **not** conflate the two, and must
**not** resolve the right internal capsule through the midbrain path.
**Boundary status (NOT the right basis pontis — the basis pontis is
RHOMBENCEPHALIC):** **Boundary case — the right crus cerebri is NOT
the right basis pontis.** The **right basis pontis**
(``.../hindbrain/metencephalon/pons/.../basis_pontis/right/``) is the
**pontine segment** of the **same descending pathway** — caudal to
the midbrain, across the **pontomesencephalic junction**. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **basis pontis**
is **rhombencephalic**; the **right crus cerebri** is
**mesencephalic**. Consumers must **not** conflate the two.
**Boundary status (NOT the right medullary pyramid — the pyramid is
MYELENCEPHALIC):** **Boundary case — the right crus cerebri is NOT
the right medullary pyramid.** The **right medullary pyramid**
(``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/right/``)
is the **medullary segment** of the **same descending pathway**.
**They are DIFFERENT STRUCTURES across a lobe boundary** — the
**pyramid** is **myelencephalic**; the **right crus cerebri** is
**mesencephalic**. Consumers must **not** conflate the two.
**Boundary status (NOT the right pyramidal decussation — the
decussation is MYELENCEPHALIC and CONTRALATERAL):** **Boundary
case — the right crus cerebri is NOT the right pyramidal decussation.**
The **pyramidal decussation**
(``.../hindbrain/myencephalon/medulla_oblongata/.../pyramidal_
decussation/``) is the **caudal medullary crossing** at which the
**right** corticospinal fibers cross to the **left** side of the
spinal cord. **The decussation is CAUDAL to the crus cerebri** — it
is the **reason** a **right** crus lesion produces **left**
hemiplegia. Consumers must **not** conflate the crus cerebri with
the decussation, and must **not** assume the right crus projects to
the right spinal cord — it projects to the **left** spinal cord.
**Boundary status (NOT the pyramidal tract as a whole — the crus is
ONE SEGMENT of the pyramidal tract):** **Boundary case — the right
crus cerebri is NOT the right pyramidal tract.** The **pyramidal
tract** (corticospinal tract) is the **whole pathway** from the
**right cerebral cortex** to the **left spinal cord** — it includes
the **corona radiata**, the **internal capsule**, the **right crus
cerebri**, the **right basis pontis**, the **right medullary
pyramid**, the **pyramidal decussation**, and the **left
corticospinal tracts** in the spinal cord. The **right crus
cerebri** (here) is **one segment** of that pathway. Consumers must
**not** conflate the crus cerebri with the whole pyramidal tract.
**Boundary status (NOT the right basal ganglia — the basal ganglia are
a PARALLEL motor system):** **Boundary case — the right crus cerebri
is NOT the right basal ganglia.** The **right basal ganglia**
(``.../forebrain/telencephalon/.../basal_ganglia/right/``) are the
**telencephalic grey-matter nuclei** (right striatum, right globus
pallidus, right substantia nigra pars reticulata, etc.) — a
**parallel** motor-modulation system. The **right crus cerebri**
(here) is the **descending conduit** — it does **not** modulate; it
**carries**. Consumers must **not** conflate the two.
**Boundary status (NOT the right CN III nucleus or the right CN III
nerve — the CN III FASCICLES traverse the crus but do not define
it):** **Boundary case — the right crus cerebri is NOT the right
oculomotor (CN III) nucleus and NOT the right oculomotor nerve.** The
**right oculomotor nucleus**
(``.../midbrain/tegmentum/right/oculomotor_nucleus/``) is the
**CN III grey-matter nucleus** in the right tegmentum. The **right
oculomotor nerve** is the **peripheral** bundle wired elsewhere.
The **right CN III fascicles TRAVERSE the right crus cerebri**
(medially) **en route** to the interpeduncular fossa — but the
fascicles are **axons passing through**, not **structures of** the
crus. **They are DIFFERENT STRUCTURES** — the **CN III nucleus** is
grey matter; the **CN III nerve** is peripheral; the **CN III
fascicles** are fibers traversing the crus. Consumers must **not**
conflate the crus with the CN III nucleus or nerve, **and** must
**not** forget that the CN III fascicles are what make **Weber
syndrome** alternating.
**Boundary status (WHITE MATTER — NOT a grey-matter nucleus, NOT an
oscillator, NOT a premotor pool, NOT a sensor nucleus):** **Boundary
case — the right crus cerebri is a WHITE-MATTER CONDUCTION PATHWAY.**
It is **not** an oscillator (no intrinsic rhythm), **not** a
premotor pool (no cell bodies, no pattern shaping), **not** a sensor
nucleus (no transduction), and **not** a motoneuron pool (no motor
neurons). It is a **conduit** — it **carries** descending axons
**generated** in the **right cortex** and **destined** for the
**left spinal cord**, the **bilateral cranial nerve motor nuclei**,
or the **bilateral pontine nuclei**. **Structure-class taxonomy:**
**coupling warnings attach to oscillators — not to premotor pools,
not to sensor nuclei, and not to conduction pathways.** The **right
crus cerebri** is a **conduction pathway** — it carries **NO
coupling warning**, **NO SLEA warning**, **NO
amygdala-lateralization warning**, and **NO rhinencephalon-exclusion
flag**. It is a **strict mirror with NO warning**.
**Boundary status (NOT the fiber populations as structural children
— corticospinal, corticobulbar, corticopontine are PROSE):**
**Boundary case — the right crus cerebri is a SINGLE fiber bundle,
NOT a container of three structural children.** The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are **fiber types within the crus**, not **sub-modules**.
The tree wires **no** structural children under this leaf.
Consumers must **not** resolve
``.../right/crus_cerebri/corticospinal`` — no such path exists.

Overview
--------
The right crus cerebri is the **right ventral-most descending
white-matter bundle** of the **right midbrain** — the **right midbrain
segment** of the **corticofugal** pathways. It carries the **right
corticospinal**, **right corticobulbar**, and **right corticopontine**
fiber populations on the **right ventral midbrain surface**. It is a
**leaf** under the **right** side-scoped container of the
**cerebral_peduncle** container.

**The right crus cerebri is the RIGHT CRUS CEREBRI, NOT the whole
right ventral midbrain.** The **broad** classical definition (crus
cerebri + substantia nigra + tegmentum) is **rejected** — the
**right tegmentum** and **right substantia nigra** are **separate
siblings** under the midbrain.

**The right crus cerebri is a WHITE-MATTER CONDUCTION PATHWAY, NOT a
grey-matter nucleus.** It has **no neurons of its own** — it
**carries** descending axons **generated** in the **right cortex**.

**The right crus cerebri is a strictly independent conduit.** It
carries the **right** descending axons, which **decussate in the
medulla** to innervate the **left** spinal cord. There is **no
left–right peduncular coupling** — the two crura are **independent
conduction pathways**. It carries **NO coupling warning** (it is a
**conduction pathway**, not an oscillator). See *Lateralization
Notes*.

**The right crus cerebri is the LEAF; the ``right/`` module is the
SIDE-SCOPED CONTAINER that holds it.** This is the **structural
clarification** this module makes retroactive: the ``right/`` module
was written with leaf-level prose *and* a Usage block that resolved
``.../right.crus_cerebri`` — those framings disagreed; this module
resolves the disagreement in favor of the **tree structure**. See
*Design Contract*.

Fiber Populations (prose, not structural children)
--------------------------------------------------
The right crus cerebri carries **three descending fiber
populations** — documented as **prose**, not as structural children:

*   **Right corticospinal fibers** — **motor** axons from the
    **right primary motor cortex** (and right premotor areas) to the
    **left spinal cord** (via the **pyramidal decussation**). The
    principal **voluntary motor** pathway for the **left limbs and
    left trunk**.

*   **Right corticobulbar fibers** — **motor** axons from the
    **right motor cortex** to the **cranial nerve motor nuclei**
    (predominantly **bilateral** for CN V, VII, IX, X, XI, XII; the
    **lower facial** and **genioglossus** targets are
    **contralateral-dominant**). The **voluntary motor** pathway
    for the **head and neck** — **predominantly bilateral** at the
    level of the cranial nerve nuclei.

*   **Right corticopontine fibers** — axons from the **right cortex**
    to the **bilateral pontine nuclei** (predominantly
    **contralateral** — the right cortex projects predominantly to
    the **left** pontine nuclei, which project to the **left**
    cerebellar hemisphere). The **corticopontocerebellar** pathway.

**These fiber populations are prose, not structural children.** The
tree wires **no** structural children under this leaf. Consumers
must **not** resolve
``.../right/crus_cerebri/corticospinal`` — no such path exists.

Somatotopy (prose — medial to lateral)
--------------------------------------
Within the **right** crus cerebri, the descending fibers are
**somatotopically organized**, **medial to lateral**:

1.  **Right corticobulbar** fibers — **most medial** (face, head,
    neck).
2.  **Right corticospinal arm** fibers — **middle-medial**
    (left arm).
3.  **Right corticospinal leg** fibers — **middle-lateral**
    (left leg).
4.  **Right corticopontine** fibers — **most lateral**.

**This somatotopy is clinically relevant** — a **medial** right-crus
lesion affects the **left face/arm** more than the **left leg**;
a **lateral** right-crus lesion affects the **left leg** more than
the **left face/arm**. The classic teaching is **"face medial, leg
lateral"** — the **right** crus's **medial** fibers carry the
**left** face; the **lateral** fibers carry the **left** leg.

The Right Crus Cerebri / Right Tegmentum Boundary
-------------------------------------------------
This is the **most consequential sibling** boundary — **narrow vs.
broad** definition on the **right side**:

*   **Right crus cerebri** (this module) — the **right descending
    fiber bundle** — **white matter**, **right ventral surface**.

*   **Right tegmentum** (``.../midbrain/tegmentum/right/``) — the
    **right grey-matter + intrinsic** midbrain — containing the
    **right red nucleus**, the **right CN III / IV nuclei**, the
    **right VTA**, the **right midbrain reticular formation**, and
    the **right periaqueductal gray** (midline-adjacent).

**They are SIBLINGS under the midbrain.** The **narrow definition**
excludes the right tegmentum from the right crus. **Consumers must
not conflate the two** — the **right crus** is the **conduit**; the
**right tegmentum** is the **processor**.

The Right Crus Cerebri / Right Substantia Nigra Boundary
--------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Right crus cerebri** (this module) — the **right descending
    fiber bundle** — **white matter**.

*   **Right substantia nigra**
    (``.../midbrain/tegmentum/right/substantia_nigra/``) — the
    **dopaminergic** nucleus — **grey matter**.

**The right substantia nigra is DORSAL to the right crus cerebri.**
It is a **tegmentum child**, **not** a crus child. Consumers must
**not** conflate the two, and must **not** resolve the right
substantia nigra through the right crus cerebri path.

The Right Crus Cerebri / Right Internal Capsule Boundary
--------------------------------------------------------
This is the **mesencephalic / telencephalic** boundary:

*   **Right crus cerebri** (this module) — the **right midbrain
    segment** of the descending pathway.

*   **Right internal capsule**
    (``.../forebrain/telencephalon/.../internal_capsule/right/``) —
    the **right telencephalic segment** of the **same descending
    pathway**.

**They carry the SAME right axons** — at **different rostrocaudal
levels**. Consumers must **not** conflate the two — the **internal
capsule** is **forebrain**; the **crus cerebri** is **midbrain**.

The Right Crus Cerebri / Right Basis Pontis Boundary
----------------------------------------------------
This is the **mesencephalic / rhombencephalic** boundary:

*   **Right crus cerebri** (this module) — the **right midbrain
    segment**.

*   **Right basis pontis**
    (``.../hindbrain/metencephalon/pons/.../basis_pontis/right/``) —
    the **right pontine segment**.

**They are across the pontomesencephalic junction.** Consumers must
**not** conflate the two — the **basis pontis** is **hindbrain**;
the **crus cerebri** is **midbrain**.

The Right Crus Cerebri / Right Medullary Pyramid Boundary
---------------------------------------------------------
This is the **mesencephalic / myelencephalic** boundary:

*   **Right crus cerebri** (this module) — the **right midbrain
    segment**.

*   **Right medullary pyramid**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/right/``)
    — the **right medullary segment**.

**They are across the pontomedullary junction.** Consumers must
**not** conflate the two — the **medullary pyramid** is
**hindbrain**; the **crus cerebri** is **midbrain**.

The Right Crus Cerebri / Pyramidal Decussation Boundary
-------------------------------------------------------
This is the **decussation** boundary — the **reason** a right crus
lesion produces **left** hemiplegia:

*   **Right crus cerebri** (this module) — the **right midbrain
    segment** — **above** the decussation.

*   **Pyramidal decussation**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramidal_
    decussation/``) — the **caudal medullary crossing** — the
    **right** corticospinal fibers cross **here** to the **left**
    spinal cord.

**The decussation is CAUDAL to the crus cerebri** — a **right** crus
lesion produces **left** hemiplegia **because** the fibers have
**not yet crossed**. Consumers must **not** conflate the crus with
the decussation, and must **not** assume a right crus lesion produces
right-sided hemiplegia — it produces **left** hemiplegia.

The Right Crus Cerebri / CN III Fascicles Boundary
--------------------------------------------------
This is the **Weber-syndrome** boundary — **the crus is not the
nerve, but the fascicles traverse it**:

*   **Right crus cerebri** (this module) — the **right descending
    fiber bundle**.

*   **Right CN III fascicles** — the **axons** of the **right
    oculomotor nerve** traversing the **medial** aspect of the
    **right crus cerebri** **en route** to the **interpeduncular
    fossa**.

**The CN III fascicles are what make Weber syndrome alternating** —
a **right** crus lesion catches the **right CN III fascicles** (→
**right CN III palsy**) **and** the **right corticospinal fibers**
(→ **left hemiplegia**). Consumers must **not** conflate the crus
with the **CN III nucleus** (right tegmentum) or the **CN III nerve**
(peripheral) — but must **not** forget the fascicles.

The Right Crus Cerebri / Basal Ganglia Boundary
-----------------------------------------------
This is the **white-matter / grey-matter** boundary within the
forebrain:

*   **Right crus cerebri** (this module) — the **right midbrain
    descending fiber bundle**.

*   **Right basal ganglia**
    (``.../forebrain/telencephalon/.../basal_ganglia/right/``) — the
    **right telencephalic grey-matter nuclei** (right striatum,
    right globus pallidus, etc.).

**The right basal ganglia are NOT on the descending pathway carried
by the crus** — they are a **parallel** motor system. Consumers
must **not** conflate the two.

The Right Crus Cerebri / Left Crus Cerebri Boundary
---------------------------------------------------
This is the **side** boundary — the **strict-mirror, NO-warning**
relationship:

*   **Right crus cerebri** (this module) — the **right** crus.

*   **Left crus cerebri**
    (``.../cerebral_peduncle/left/crus_cerebri/``) — the **left**
    crus.

**They are STRICTLY SYMMETRIC CONDUCTION PATHWAYS** — each carries
**its own** descending axons, and the two are **not coupled**.
Consumers must **not** conflate the two, and must **not** assume a
right lesion and a left lesion produce mirror-image deficits —
**a right crus lesion produces RIGHT CN III palsy + LEFT hemiplegia**,
and a **left** crus lesion produces **LEFT CN III palsy + RIGHT
hemiplegia**. The **CN III palsy is IPSILATERAL**; the **hemiplegia
is CONTRALATERAL**.

The Right Crus Cerebri / ``right/`` Side Container Boundary
-----------------------------------------------------------
This is the **leaf / container** boundary — **structural
clarification**:

*   **Right crus cerebri** (this module) — the **substantive leaf**.

*   **``right/`` module** (``.../cerebral_peduncle/right/``) — the
    **side-scoped namespace** that holds this leaf.

**The ``right/`` module is a SIDE CONTAINER, not a leaf.** The
earlier ``right/__init__.py`` was written with leaf-level prose *and*
a Usage block resolving ``.../right.crus_cerebri`` — this module
resolves the disagreement in favor of the **tree structure**.
Consumers that resolve ``.../cerebral_peduncle/right`` and expect a
leaf should go **one level deeper** to
``.../cerebral_peduncle/right/crus_cerebri``.

Function in the Human Brain
---------------------------
The right crus cerebri's function is **descending motor and
corticopontine conduction on the right side** — **NOT** rhythm
generation, **NOT** motor programming, **NOT** sensory processing:

*   **Right Corticospinal Conduction (left voluntary motor):** The
    right crus **carries** the **right corticospinal** axons from the
    **right cortex** to the **left spinal cord** — the **voluntary
    motor** pathway for the **left limbs and left trunk**.

*   **Right Corticobulbar Conduction (predominantly bilateral
    cranial motor):** The right crus **carries** the **right
    corticobulbar** axons from the **right cortex** to the
    **bilateral cranial nerve motor nuclei** — predominantly
    **bilateral** innervation, with **contralateral dominance** for
    the **lower facial** and **genioglossus** targets.

*   **Right Corticopontine Conduction (contralateral cerebellar
    input):** The right crus **carries** the **right corticopontine**
    axons from the **right cortex** to the **bilateral pontine
    nuclei** (predominantly **left** pontine nuclei), providing the
    **left** cerebellar hemisphere with **right cortical input**.

*   **NOT a processor.** The right crus **carries** axons; it does
    **not** process them. It has **no neurons of its own**.

*   **NOT an oscillator.** The **oscillators** are the
    **pre-Bötzinger complex**, the **Bötzinger complex**, and the
    **pFRG** — **brainstem respiratory oscillators**. The right crus
    is a **conduction pathway** — it does **not** generate a
    rhythm.

*   **NOT the basal ganglia.** The right basal ganglia are the
    **telencephalic** motor-modulation system. The right crus is the
    **descending conduit** — it does **not** modulate; it
    **carries**.

**The unifying theme:** the right crus cerebri is the **right midbrain
segment of the descending corticofugal pathway** — a **white-matter
conduit** carrying the **right corticospinal**, **right
corticobulbar**, and **right corticopontine** axons. It is a
**conduction pathway**, **NOT** a processor (**right tegmentum**),
**NOT** a grey-matter nucleus (**right substantia nigra**), **NOT**
the whole pyramidal tract, and **NOT** the internal capsule / basis
pontis / medullary pyramid.

Associated Disorders
--------------------
The right crus cerebri has a **direct clinical association** with
**right-sided Weber syndrome** — its clinical relevance is
**direct**, via the **right crus** and the **right CN III fascicles**
that traverse it:

*   **Right Weber Syndrome (alternating oculomotor hemiplegia —
    RIGHT, DIRECT, via the right crus cerebri):** A **right ventral
    midbrain** lesion (**infarction** — most commonly **paramedian
    midbrain** from **basilar artery** perforators; **hemorrhage**;
    **tumor**; **tentorial herniation**) involving the **right
    crus cerebri** and the **right CN III fascicles** produces:
    *   **Ipsilateral (RIGHT) CN III palsy** — **right ptosis**,
        **right mydriasis**, **right "down and out" eye** — from
        the **right CN III fascicle** involvement.
    *   **Contralateral (LEFT) spastic hemiplegia** — from the
        **right corticospinal** fiber involvement in the **right
        crus**.
    **Weber syndrome lateralizes** — a **right** crus lesion
    produces **right CN III palsy + left hemiplegia**, and a
    **left** crus lesion produces **left CN III palsy + right
    hemiplegia**. **Right Weber syndrome is the named disorder of
    the right crus cerebri** — **direct**, not indirect.

*   **Wallerian Degeneration of the Right Crus Cerebri
    (DESCRIPTIVE):** Large **right cortical** or **right internal
    capsule** strokes produce **Wallerian degeneration** of the
    **ipsilateral (right) crus cerebri** — visible on **MRI** as
    **T2 hyperintensity** and **atrophy** of the **right crus**.
    This is **descriptive**, not a named syndrome — the **primary
    lesion** is **upstream**.

*   **Progressive Supranuclear Palsy (PSP — NOT the crus):** The
    "**hummingbird sign**" of PSP is a **midbrain tegmentum**
    measure — **not** a crus cerebri measure. **PSP belongs to the
    tegmentum**, not to this module.

*   **ALS (INDIRECT — via the right corticospinal tract, not the crus
    as a named site):** **ALS** affects the **right corticospinal
    tract** — including the fibers that pass through the **right
    crus** — but the **right crus is not a named site** of ALS
    pathology. This is **indirect**.

*   **No Named "Right Crus Cerebri Syndrome" (apart from right
    Weber):** The right crus is a **white-matter conduit** — its
    only named syndrome is **right Weber syndrome** (alternating
    oculomotor hemiplegia with right CN III palsy). Its clinical
    relevance is **direct**, via the **right crus** and the **right
    CN III fascicles**.

**What is NOT here:** The right crus cerebri is **not** the substrate
for **Benedikt syndrome** (right tegmentum — red nucleus + right
CN III), **Claude syndrome** (right tegmentum — red nucleus + right
CN III), **Parinaud syndrome** (dorsal midbrain — superior
colliculus / tectum), **Nothnagel syndrome** (tectum / colliculi),
**Millard-Gubler syndrome** (pons), **Wallenberg syndrome** (lateral
medulla), **locked-in syndrome** (basis pontis), **CCHS** (RTN),
**OIRD** (pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger complex
+ arcuate nucleus), **essential hypertension / sympathetic
overactivity** (C1 group / RVLM), **Parkinson's disease** (right
substantia nigra — tegmentum), **Huntington's disease** (right
striatum — telencephalon), or **Kluver-Bucy syndrome** (amygdala).
Its clinical relevance is **direct**, via **right Weber syndrome**.
**Right Weber syndrome is the named disorder.**

Lateralization Notes
--------------------
This is the **right** crus cerebri leaf. The right and left crura are
**bilaterally symmetric** and carry **NO coupling warning of their
own** — and they **inherit no warning from any oscillator**:

*   **Bilateral Conduction Pathways:** Each hemisphere has its own
    crus cerebri — each is a **white-matter conduit** carrying **its
    own** (predominantly **ipsilateral** above the pyramidal
    decussation) descending axons.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **right crus cerebri** is a **conduction
    pathway** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. Its **right**
    and **left** sides are **independent conduits** — there is
    **no** crus–crus coupling. **This extends the propagatable
    rule:** **coupling warnings attach to oscillators — not to
    premotor pools, not to sensor nuclei, and not to conduction
    pathways.**

*   **NO SLEA Warning:** The right crus cerebri is **SLEA-free** — it
    is **not** an extended-amygdala component.

*   **NO Amygdala-Lateralization Warning:** The right crus cerebri is
    **not** part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **NO Rhinencephalon-Exclusion Flag:** The right crus cerebri is
    **not** a rhinencephalon structure — it carries **no**
    rhinencephalon-exclusion flag.

**A consumer that assumes "right crus cerebri = left crus cerebri"
will be structurally correct** — the two sides are **symmetric** and
**functionally independent as conduits**. The right crus cerebri is a
**strict-mirror pair with NO warning** — **no coupling warning**,
**no SLEA warning**, **no amygdala-lateralization warning**, and
**no rhinencephalon-exclusion flag**. Consumers must **not** assume
the two sides produce **mirror-image** deficits — **right** crus
lesions produce **right** CN III palsy + **left** hemiplegia, and
**left** crus lesions produce **left** CN III palsy + **right**
hemiplegia.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only — **no** import
    from ``.../left/crus_cerebri/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/tegmentum/``, ``.../midbrain/tectum/``, the
    **internal capsule**, the **basis pontis**, the **medullary
    pyramid**, the **pyramidal decussation**, the **basal ganglia**,
    or any other container. The right crus cerebri's relationships to
    the right tegmentum, the right substantia nigra, the right
    internal capsule, the right basis pontis, the right medullary
    pyramid, the pyramidal decussation, the right basal ganglia, and
    the right CN III fascicles are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **dopaminergic
    phenotype** of the right substantia nigra is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the tegmentum leaf, **not** here.
*   **Leaf module — no structural children.** The **right
    corticospinal**, **right corticobulbar**, and **right
    corticopontine** fiber populations are documented as **prose**,
    not as sub-modules. Consumers must not assume any exist as
    children; resolve **fiber-population-level** detail through the
    references.
*   **NARROW DEFINITION — the leaf is the RIGHT CRUS CEREBRI, NOT the
    whole right ventral midbrain.** The **right tegmentum** and
    **right substantia nigra** are **separate siblings** — they are
    **not** part of this module.
*   **WHITE-MATTER CONDUCTION PATHWAY — NOT a grey-matter nucleus,
    NOT an oscillator, NOT a premotor pool, NOT a sensor nucleus.**
    It carries descending axons — it does **not** process them.
*   **NOT the right tegmentum — the right tegmentum is a SIBLING.**
*   **NOT the right substantia nigra — the right substantia nigra is
    a TEGMENTUM structure.**
*   **NOT the right internal capsule or corona radiata — those are
    FOREBRAIN structures.**
*   **NOT the right basis pontis — that is a HINDBRAIN structure.**
*   **NOT the right medullary pyramid — that is a HINDBRAIN
    structure.**
*   **NOT the right pyramidal decussation — that is a CAUDAL
    MYELENCEPHALIC structure** — and it is **the reason** a right
    crus lesion produces **left** hemiplegia.
*   **NOT the right CN III nucleus or the right CN III nerve — the
    CN III FASCICLES traverse the crus but do not define it.** The
    CN III fascicles are **what make Weber syndrome alternating**.
*   **NO coupling warning — the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS.** The right crus
    cerebri is a **strict mirror with NO warning**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The right crus cerebri is a local leaf
    under the right side container of the cerebral peduncle, not a
    cross-listed leaf.
*   **No nested cross-listing.** The right crus cerebri has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with the left crus cerebri — strict mirror
    with NO warning.** Right and left crus cerebri modules are
    **structurally identical** — same leaf status, same **crus
    cerebri** framing, same **conduction-pathway** framing, same
    **no warning**.
*   **STRUCTURAL RECONCILIATION — the ``right/`` module should be
    reduced to a thin side container.** The earlier
    ``.../cerebral_peduncle/right/__init__.py`` carried substantive
    leaf-level prose **and** a Usage block resolving
    ``.../right.crus_cerebri``. This leaf resolves that disagreement:
    **this module carries the substantive leaf-level prose**; the
    ``right/__init__.py`` module **should be reduced** to a
    **side-scoped namespace** — a short container docstring pointing
    at this leaf, with the substantive content (fiber populations,
    somatotopy, boundary stack, Weber syndrome) **moving** here.
    Consumers should resolve the **leaf** (this module) for
    substantive content, and the **container** (``right/``) only for
    side-scoped enumeration.

Usage
-----
Resolve by path (the leaf — substantive content)::

    from infrastructure.brainparts.midbrain.cerebral_peduncle.right.crus_cerebri import (
        CEREBRAL_PEDUNCLE_RIGHT_CRUS_CEREBRI_CHILDREN,
    )

Or by fully-qualified path string::

    path = "midbrain.cerebral_peduncle.right.crus_cerebri"

**Do not** assume the right crus cerebri is the **whole right ventral
midbrain** (the broad classical definition). It is the **right crus
cerebri** — **narrow definition** — because the **right tegmentum**
and **right substantia nigra** are **separate siblings**.

**Do not** assume the right crus cerebri is the **right tegmentum** or
the **right substantia nigra**. Those are **separate structures** —
the **right tegmentum** is the grey-matter + intrinsic midbrain; the
**right substantia nigra** is a **tegmentum child**.

**Do not** assume the right crus cerebri is the **right internal
capsule** (telencephalic) or the **right basis pontis** (pontine) or
the **right medullary pyramid** (medullary). Those are **segments**
of the same descending pathway at **different rostrocaudal levels**.

**Do not** assume the right crus cerebri is the **right pyramidal
tract as a whole**. It is **one segment** — the **right midbrain
segment**.

**Do not** assume the right crus cerebri is the **right CN III
nucleus** or the **right CN III nerve**. The **right CN III
fascicles traverse** the crus medially, but they are **not** the
crus.

**Do not** assume a **right** crus lesion produces **right**
hemiplegia. The **right corticospinal** fibers **decussate in the
medulla** — a **right** crus lesion produces **left** hemiplegia
(and **right** CN III palsy — the "alternating" pattern).

**Do not** assume the right crus cerebri contains structural
**fiber-population children**. The **right corticospinal**,
**right corticobulbar**, and **right corticopontine** fibers are
**prose**, not modules. There is **no**
``.../right/crus_cerebri/corticospinal``.

**Do not** import the **oscillator coupling warning** into the right
crus cerebri. **It is a CONDUCTION PATHWAY** — it carries **NO
coupling warning**.

**Do not** resolve substantive content from the **``right/`` side
container**. The **leaf** (this module) carries the substantive
prose — the **container** (``right/``) is a **side-scoped
namespace**. If a consumer finds itself reading the ``right/`` module
for fiber populations, somatotopy, or Weber-syndrome detail, it has
resolved **one level too shallow** — go one level deeper to this
leaf.

Iterating the right crus cerebri's (empty) children (recommended
consumer pattern)::

    CEREBRAL_PEDUNCLE_RIGHT_CRUS_CEREBRI_CHILDREN = ()
    # The right crus cerebri is a leaf. The right corticospinal,
    # right corticobulbar, and right corticopontine fiber populations
    # are prose, not modules.

Reaching the right side container (recommended consumer pattern —
NOTE it is a CONTAINER, not a leaf)::

    # The right/ module is the SIDE-SCOPED CONTAINER that holds this
    # leaf:
    #
    #   brainparts.midbrain.cerebral_peduncle.right
    #
    # Do NOT resolve substantive content from right/ — the leaf
    # (this module) carries the fiber populations, somatotopy,
    # boundary stack, and Weber-syndrome detail.

Reaching the left crus cerebri (recommended consumer pattern — the
SIDE sibling)::

    # The left crus cerebri is the LEFT descending fiber bundle:
    #
    #   brainparts.midbrain.cerebral_peduncle.left.crus_cerebri
    #
    # The two sides are STRICTLY SYMMETRIC CONDUCTION PATHWAYS
    # — each carries its own descending axons. There is NO
    # coupling between them.

Reaching the right tegmentum (recommended consumer pattern — the
grey-matter sibling)::

    # The right tegmentum is the RIGHT GREY-MATTER + INTRINSIC
    # midbrain — right substantia nigra, right VTA, right red
    # nucleus, right PAG, right CN III/IV nuclei, right
    # Edinger-Westphal, right mesencephalic trigeminal, right
    # midbrain reticular formation:
    #
    #   brainparts.midbrain.tegmentum.right
    #
    # The right crus cerebri is the WHITE-MATTER conduit; the right
    # tegmentum is the GREY-MATTER processor.

Reaching the right substantia nigra (recommended consumer pattern —
the tegmentum child, NOT a crus child)::

    # The right substantia nigra is a RIGHT TEGMENTUM child — the
    # dopaminergic nucleus DORSAL to the right crus cerebri:
    #
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #
    # The right crus cerebri is the WHITE-MATTER bundle VENTRAL to
    # the right substantia nigra. The narrow definition excludes the
    # right substantia nigra from the crus.

Reaching the right internal capsule (recommended consumer pattern —
the TELENCEPHALIC segment)::

    # The right internal capsule is the RIGHT TELENCEPHALIC segment
    # of the descending pathway — the same right corticospinal /
    # corticobulbar / corticopontine axons at a more rostral level:
    #
    #   brainparts.forebrain.telencephalon...internal_capsule.right
    #
    # The right crus cerebri is the RIGHT MESENCEPHALIC segment.

Reaching the right basis pontis (recommended consumer pattern — the
RHOMBENCEPHALIC segment)::

    # The right basis pontis is the RIGHT PONTINE segment of the
    # descending pathway:
    #
    #   brainparts.hindbrain.metencephalon.pons...basis_pontis.right
    #
    # The right crus cerebri is the RIGHT MESENCEPHALIC segment.

Reaching the right medullary pyramid (recommended consumer pattern —
the MYELENCEPHALIC segment)::

    # The right medullary pyramid is the RIGHT MEDULLARY segment of
    # the descending pathway:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata...
    #   pyramid.right
    #
    # The right crus cerebri is the RIGHT MESENCEPHALIC segment.

Reaching the pyramidal decussation (recommended consumer pattern —
NOTE the decussation is CAUDAL to the crus)::

    # The pyramidal decussation is the CAUDAL MEDULLARY crossing
    # at which the RIGHT corticospinal fibers cross to the LEFT
    # spinal cord:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata...
    #   pyramidal_decussation
    #
    # The decussation is CAUDAL to the crus — this is the REASON a
    # RIGHT crus lesion produces LEFT hemiplegia.

Fiber-population-level detail (not wired — consult references)::

    # The right crus cerebri's fiber populations are prose, not
    # modules:
    #   right corticospinal  -> left voluntary motor (limbs, trunk)
    #                           somatotopy: left arm medial,
    #                           left leg lateral
    #   right corticobulbar  -> bilateral cranial motor
    #                           (predominantly bilateral;
    #                           left-dominant for lower face and
    #                           genioglossus) somatotopy: most
    #                           medial
    #   right corticopontine -> left cerebellar input
    #                           (predominantly contralateral)
    #                           somatotopy: most lateral
    #
    # Do not attempt to resolve these as sub-paths of the right
    # crus cerebri.

Bilateral iteration (recommended consumer pattern — NOTE the
conduction-pathway rule and the lateralization of Weber
syndrome)::

    for side in ("left", "right"):
        crus_path = (
            f"midbrain.cerebral_peduncle.{side}.crus_cerebri"
        )
        # resolve crus_path through the memory/recall layer
        #
        # NOTE: the two sides are CONDUCTION PATHWAYS — each
        # carries its own descending axons. There is NO coupling
        # warning here. The coupling warning attaches to the
        # OSCILLATORS (pre-Bötzinger complex, Bötzinger complex),
        # not to conduction pathways.
        #
        # NOTE: Weber syndrome lateralizes — a RIGHT crus lesion
        # produces RIGHT CN III palsy + LEFT hemiplegia, and a
        # LEFT crus lesion produces LEFT CN III palsy + RIGHT
        # hemiplegia. The CN III palsy is IPSILATERAL; the
        # hemiplegia is CONTRALATERAL.

References
----------
*   **Canonical midbrain anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (The midbrain
    subdivisions; the crus cerebri as the narrow cerebral peduncle;
    the descending fiber populations; the somatotopy of the crus.)
*   **Crus cerebri and descending pathways:** ten Donkelaar, H.J.,
    Lammens, M., Hori, A. (2003). *Clinical Neuroembryology:
    Development and Developmental Disorders of the Human Central
    Nervous System*. (Corticospinal and corticobulbar bundles in the
    crus cerebri; the descending motor pathway; the
    pontomesencephalic and pontomedullary junctions.)
*   **Corticospinal tract organization:** Lemon, R.N. (2008).
    "Descending pathways in motor control." *Annual Review of
    Neuroscience* 31:195–218. (The descending motor pathways —
    corticospinal and corticobulbar organization in the crus
    cerebri; the decussation at the medulla.)
*   **Corticopontine and corticopontocerebellar pathway:** Glickstein,
    M., May, J.G., Mercier, B.E. (1985). "Corticopontine projection
    in the macaque: the distribution of labelled cortical cells
    after multiple tracer injections." *Journal of Comparative
    Neurology* 235:343–359. (Corticopontine fibers in the crus
    cerebri and their projection to the pontine nuclei —
    predominantly contralateral.)
*   **Somatotopy in the crus cerebri:** Bertrand, G., Blundell, J.,
    Pelissier, P. (1973). "Somatotopic organization of the
    corticospinal tract in the human cerebral peduncle." *Surgical
    Neurology* 1:108–111. (The classical clinical somatotopy — face
    medial, leg lateral — within the human crus cerebri.)
*   **Corticobulbar dominance for lower face:** Kuypers, H.G.J.M.
    (1958). "Corticobular connexions to the pons and lower
    brain-stem in man: an anatomical study." *Brain* 81:364–388.
    (The bilateral-but-contralateral-dominant organization of the
    corticobulbar projection to the lower facial nucleus.)
*   **Weber syndrome (DIRECT disorder):** Weber, H.D. (1856).
    "A contribution to the pathology of the crura cerebri."
    *Medico-Chirurgical Transactions* 39:121–140. (The original
    description of alternating oculomotor hemiplegia — the named
    syndrome of the crus cerebri.)
*   **Weber syndrome — modern review:** Bogousslavsky, J., Caplan,
    L.R. (2001). *Stroke Syndromes*, 2nd ed. (Weber syndrome and
    other ventral midbrain stroke syndromes — the clinical
    localization to the crus cerebri and CN III fascicles; the
    lateralization of the syndrome — ipsilateral CN III palsy,
    contralateral hemiplegia.)
*   **Benedikt syndrome (contrast — tegmentum, NOT crus):** Benedikt,
    M. (1889). "Krankenvorstellung." *Wiener Medicinische Presse*
    30:1–4. (Benedikt syndrome — red nucleus + CN III — tegmentum,
    NOT the crus cerebri.)
*   **Claude syndrome (contrast — tegmentum, NOT crus):** Claude, H.,
    Loyez, M. (1912). "Ramollissement du noyau rouge." *Revue
    Neurologique* 23:49–51. (Claude syndrome — red nucleus + CN III
    — tegmentum, NOT the crus cerebri.)
*   **Parinaud syndrome (contrast — dorsal midbrain, NOT crus):**
    Parinaud, H. (1883). "Paralysie des mouvements associés des
    yeux." *Annales d'Oculistique* 90:1–21. (Parinaud syndrome —
    superior colliculus / tectum — NOT the crus cerebri.)
*   **Progressive supranuclear palsy (contrast — midbrain tegmentum,
    NOT crus):** Steele, J.C., Richardson, J.C., Olszewski, J.
    (1964). "Progressive supranuclear palsy." *Archives of
    Neurology* 10:333–359. (The "hummingbird sign" is a midbrain
    tegmentum measure — the crus cerebri is NOT the primary PSP
    substrate.)
*   **ALS (contrast — motor cortex and anterior horn, NOT the crus
    as a named site):** Rowland, L.P., Shneider, N.A. (2001).
    "Amyotrophic lateral sclerosis." *New England Journal of
    Medicine* 344:1688–1700. (ALS affects the corticospinal tract —
    including crus fibers — but the crus is NOT a named site of ALS
    pathology.)
*   **Internal capsule (contrast — telencephalic segment):** Emos,
    M.C., Agarwal, S. (2024). *Neuroanatomy, Internal Capsule*.
    StatPearls. (The internal capsule as the telencephalic segment
    of the descending motor pathway — contrast with the midbrain
    crus cerebri.)
*   **Basis pontis (contrast — rhombencephalic segment):** Brodal,
    P. (1972). "The corticopontine projection in the cat."
    *Journal of Comparative Neurology* 146:177–215. (The basis
    pontis and the pontine nuclei — the pontine segment of the
    descending pathway, contrast with the midbrain crus cerebri.)
*   **Medullary pyramids and pyramidal decussation (contrast —
    myelencephalic segments):** Lassek, A.M. (1942). "The human
    pyramidal tract. IV. A study of the mature, the old, and the
    newborn." *Journal of Nervous and Mental Disease* 95:271–280.
    (The medullary pyramids and the pyramidal decussation — the
    medullary segment of the descending pathway, contrast with the
    midbrain crus cerebri.)
*   **Basal ganglia (contrast — telencephalic grey matter):** Parent,
    A., Hazrati, L.N. (1995). "Functional anatomy of the basal
    ganglia. I. The cortico-basal ganglia-thalamo-cortical loop."
    *Brain Research Reviews* 20:91–127. (The basal ganglia as a
    parallel motor-modulation system — NOT on the descending pathway
    carried by the crus.)
*   **Dopaminergic phenotype (chemicals_hormones-layer fact —
    contrast):** Björklund, A., Dunnett, S.B. (2007). "Dopamine
    neuron systems in the brain: an update." *Trends in
    Neurosciences* 30:194–202. (The dopaminergic phenotype of the
    substantia nigra as a chemicals-layer fact — documented in the
    tegmentum leaf, never imported here.)
*   **SLEA (contrast — the right crus cerebri is not SLEA):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the crus cerebri.)
*   NeuroNames — Crus cerebri (right); FMA — Crus cerebri (right
    member).
"""