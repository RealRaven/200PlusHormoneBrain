"""
infrastructure.brainparts.midbrain.cerebral_peduncle.left.crus_cerebri
======================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── cerebral_peduncle
        ├── left
        │   └── crus_cerebri     <-- THIS MODULE (leaf)
        └── right
            └── crus_cerebri

**Primary synonym:** Left crus cerebri; left cerebral peduncle (narrow
definition); left basis pedunculi (broad — when the substantia nigra
is included; **not** this module). The **left** member of the paired
crus cerebri.
**Cytoarchitectonic designation:** **Not a Brodmann area** and **not
a grey-matter nucleus** — the left crus cerebri is a **white-matter
fiber bundle** (a **conduction pathway**). It carries **descending
corticofugal axons**, not cell bodies. It has **no neurons of its
own**.
**Part of:** The **cerebral_peduncle** container → **left** side
container → **this leaf**. The **cerebral_peduncle** is a child of
the **midbrain** (mesencephalon) container, on the **ventral**
surface, **ventral to the substantia nigra** and the **tegmentum**.
**Structural parent:** ``.../cerebral_peduncle/left/`` → **direct
child** of the **left** side-scoped container of the cerebral
peduncle.
**Structural children:** **None.** This is a **leaf** module. The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are documented as **prose**, not as structural children.
**Boundary status (STRUCTURAL CLARIFICATION — the parent ``left/`` is
a SIDE CONTAINER, not the leaf):** **Boundary case — the left crus
cerebri is the LEAF; the ``left/`` module is the SIDE-SCOPED
CONTAINER that holds it.** The earlier ``left/__init__.py`` carried
substantive leaf-level prose **and** a Usage block resolving
``.../left.crus_cerebri`` — those framings disagreed. This module
resolves the disagreement in favor of the **tree structure**: the
``left/`` module is a **side-scoped namespace** (it holds exactly one
leaf, this one), and the **crus_cerebri** module (here) is the
**substantive leaf** that carries the white-matter-conduit prose.
Consumers that resolve ``.../cerebral_peduncle/left`` and expect a
leaf should go **one level deeper** to ``.../cerebral_peduncle/left/
crus_cerebri``. See *Design Contract* for the recommended
rebalancing of the ``left/__init__.py`` module.
**Boundary status (NOT the right crus cerebri — the SIDE
boundary):** **Boundary case — the left crus cerebri is NOT the
right crus cerebri.** The **right** leaf
(``.../cerebral_peduncle/right/crus_cerebri/``) is the **right**
crus cerebri. **They are DIFFERENT STRUCTURES** on **opposite
sides** — each carries **its own** descending axons, and each is the
**contralateral hemiplegia** substrate for an **ipsilateral**
peduncular lesion. Consumers must **not** conflate the two, and must
**not** assume a left-crus lesion produces left-sided hemiplegia —
the **corticospinal** fibers **decussate in the medulla**, **caudal**
to the crus cerebri, so a **left** crus lesion produces **right**
hemiplegia.
**Boundary status (NARROW DEFINITION — the leaf is the LEFT CRUS
CEREBRI, NOT the whole left ventral midbrain):** **Boundary case —
the left crus cerebri is the LEFT CRUS CEREBRI (narrow definition),
NOT the whole left ventral midbrain (broad definition).** The
**broad** classical definition (crus cerebri + substantia nigra +
tegmentum) is **rejected** — the **left tegmentum** and **left
substantia nigra** are **separate siblings** under the midbrain.
The **narrow definition** is the **only** one consistent with the
tree.
**Boundary status (NOT the left tegmentum — the left tegmentum is a
SIBLING under the midbrain):** **Boundary case — the left crus
cerebri is NOT the left tegmentum.** The **left tegmentum**
(``.../midbrain/tegmentum/left/``) contains the **left substantia
nigra**, the **left ventral tegmental area**, the **left red
nucleus**, the **left periaqueductal gray** (midline — shared), the
**left oculomotor nucleus** (CN III), the **left trochlear nucleus**
(CN IV), the **left Edinger-Westphal nucleus**, the **left
mesencephalic trigeminal nucleus** (CN V), and the **left midbrain
reticular formation**. The **left crus cerebri** (here) is the
**left descending fiber bundle** on the **left ventral surface**.
**They are DIFFERENT STRUCTURES** — the **left tegmentum** is the
**grey-matter + intrinsic** midbrain; the **left crus cerebri** is
the **white-matter conduit**. Consumers must **not** conflate the
two, and must **not** resolve a left tegmentum structure (left
substantia nigra, left red nucleus, left CN III/IV nuclei) through
the left crus cerebri path.
**Boundary status (NOT the left substantia nigra — the left
substantia nigra is a TEGMENTUM structure):** **Boundary case — the
left crus cerebri is NOT the left substantia nigra.** The **left
substantia nigra**
(``.../midbrain/tegmentum/left/substantia_nigra/``) is the
**dopaminergic** nucleus **dorsal to the left crus cerebri** — it
is a **grey-matter** structure and a **tegmentum child**. The **left
crus cerebri** (here) is the **white-matter bundle ventral to the
left substantia nigra**. **They are DIFFERENT STRUCTURES** — the
**left substantia nigra** is **grey matter**; the **left crus
cerebri** is **white matter**. Consumers must **not** conflate the
two, and must **not** resolve the left substantia nigra through the
left crus cerebri path.
**Boundary status (NOT the left internal capsule — the internal
capsule is TELENCEPHALIC):** **Boundary case — the left crus
cerebri is NOT the left internal capsule.** The **left internal
capsule**
(``.../forebrain/telencephalon/.../internal_capsule/left/``) is the
**telencephalic segment** of the **same descending pathway** — it
carries the **same** left **corticospinal**, **corticobulbar**, and
**corticopontine** axons at a **more rostral** level. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **internal
capsule** is **telencephalic**; the **left crus cerebri** is
**mesencephalic**. Consumers must **not** conflate the two, and must
**not** resolve the left internal capsule through the midbrain path.
**Boundary status (NOT the left basis pontis — the basis pontis is
RHOMBENCEPHALIC):** **Boundary case — the left crus cerebri is NOT
the left basis pontis.** The **left basis pontis**
(``.../hindbrain/metencephalon/pons/.../basis_pontis/left/``) is the
**pontine segment** of the **same descending pathway** — caudal to
the midbrain, across the **pontomesencephalic junction**. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **basis pontis**
is **rhombencephalic**; the **left crus cerebri** is
**mesencephalic**. Consumers must **not** conflate the two.
**Boundary status (NOT the left medullary pyramid — the pyramid is
MYELENCEPHALIC):** **Boundary case — the left crus cerebri is NOT
the left medullary pyramid.** The **left medullary pyramid**
(``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/left/``)
is the **medullary segment** of the **same descending pathway**.
**They are DIFFERENT STRUCTURES across a lobe boundary** — the
**pyramid** is **myelencephalic**; the **left crus cerebri** is
**mesencephalic**. Consumers must **not** conflate the two.
**Boundary status (NOT the left pyramidal decussation — the
decussation is MYELENCEPHALIC and CONTRALATERAL):** **Boundary
case — the left crus cerebri is NOT the left pyramidal decussation.**
The **pyramidal decussation**
(``.../hindbrain/myencephalon/medulla_oblongata/.../pyramidal_
decussation/``) is the **caudal medullary crossing** at which the
**left** corticospinal fibers cross to the **right** side of the
spinal cord. **The decussation is CAUDAL to the crus cerebri** — it
is the **reason** a **left** crus lesion produces **right**
hemiplegia. Consumers must **not** conflate the crus cerebri with
the decussation, and must **not** assume the left crus projects to
the left spinal cord — it projects to the **right** spinal cord.
**Boundary status (NOT the pyramidal tract as a whole — the crus is
ONE SEGMENT of the pyramidal tract):** **Boundary case — the left
crus cerebri is NOT the left pyramidal tract.** The **pyramidal
tract** (corticospinal tract) is the **whole pathway** from the
**left cerebral cortex** to the **right spinal cord** — it includes
the **corona radiata**, the **internal capsule**, the **left crus
cerebri**, the **left basis pontis**, the **left medullary
pyramid**, the **pyramidal decussation**, and the **right
corticospinal tracts** in the spinal cord. The **left crus
cerebri** (here) is **one segment** of that pathway. Consumers must
**not** conflate the crus cerebri with the whole pyramidal tract.
**Boundary status (NOT the left basal ganglia — the basal ganglia are
a PARALLEL motor system):** **Boundary case — the left crus cerebri
is NOT the left basal ganglia.** The **left basal ganglia**
(``.../forebrain/telencephalon/.../basal_ganglia/left/``) are the
**telencephalic grey-matter nuclei** (left striatum, left globus
pallidus, left substantia nigra pars reticulata, etc.) — a
**parallel** motor-modulation system. The **left crus cerebri**
(here) is the **descending conduit** — it does **not** modulate; it
**carries**. Consumers must **not** conflate the two.
**Boundary status (NOT the left CN III nucleus or the left CN III
nerve — the CN III FASCICLES traverse the crus but do not define
it):** **Boundary case — the left crus cerebri is NOT the left
oculomotor (CN III) nucleus and NOT the left oculomotor nerve.** The
**left oculomotor nucleus**
(``.../midbrain/tegmentum/left/oculomotor_nucleus/``) is the
**CN III grey-matter nucleus** in the left tegmentum. The **left
oculomotor nerve** is the **peripheral** bundle wired elsewhere.
The **left CN III fascicles TRAVERSE the left crus cerebri**
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
case — the left crus cerebri is a WHITE-MATTER CONDUCTION PATHWAY.**
It is **not** an oscillator (no intrinsic rhythm), **not** a
premotor pool (no cell bodies, no pattern shaping), **not** a sensor
nucleus (no transduction), and **not** a motoneuron pool (no motor
neurons). It is a **conduit** — it **carries** descending axons
**generated** in the **left cortex** and **destined** for the
**right spinal cord**, the **bilateral cranial nerve motor nuclei**,
or the **bilateral pontine nuclei**. **Structure-class taxonomy:**
**coupling warnings attach to oscillators — not to premotor pools,
not to sensor nuclei, and not to conduction pathways.** The **left
crus cerebri** is a **conduction pathway** — it carries **NO
coupling warning**, **NO SLEA warning**, **NO
amygdala-lateralization warning**, and **NO rhinencephalon-exclusion
flag**. It is a **strict mirror with NO warning**.
**Boundary status (NOT the fiber populations as structural children
— corticospinal, corticobulbar, corticopontine are PROSE):**
**Boundary case — the left crus cerebri is a SINGLE fiber bundle,
NOT a container of three structural children.** The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are **fiber types within the crus**, not **sub-modules**.
The tree wires **no** structural children under this leaf.
Consumers must **not** resolve
``.../left/crus_cerebri/corticospinal`` — no such path exists.

Overview
--------
The left crus cerebri is the **left ventral-most descending
white-matter bundle** of the **left midbrain** — the **left midbrain
segment** of the **corticofugal** pathways. It carries the **left
corticospinal**, **left corticobulbar**, and **left corticopontine**
fiber populations on the **left ventral midbrain surface**. It is a
**leaf** under the **left** side-scoped container of the
**cerebral_peduncle** container.

**The left crus cerebri is the LEFT CRUS CEREBRI, NOT the whole left
ventral midbrain.** The **broad** classical definition (crus cerebri
+ substantia nigra + tegmentum) is **rejected** — the **left
tegmentum** and **left substantia nigra** are **separate siblings**
under the midbrain.

**The left crus cerebri is a WHITE-MATTER CONDUCTION PATHWAY, NOT a
grey-matter nucleus.** It has **no neurons of its own** — it
**carries** descending axons **generated** in the **left cortex**.

**The left crus cerebri is a strictly independent conduit.** It
carries the **left** descending axons, which **decussate in the
medulla** to innervate the **right** spinal cord. There is **no
left–right peduncular coupling** — the two crura are **independent
conduction pathways**. It carries **NO coupling warning** (it is a
**conduction pathway**, not an oscillator). See *Lateralization
Notes*.

**The left crus cerebri is the LEAF; the ``left/`` module is the
SIDE-SCOPED CONTAINER that holds it.** This is the **structural
clarification** this module makes retroactive: the ``left/`` module
was written with leaf-level prose *and* a Usage block that resolved
``.../left.crus_cerebri`` — those framings disagreed; this module
resolves the disagreement in favor of the **tree structure**. See
*Design Contract*.

Fiber Populations (prose, not structural children)
--------------------------------------------------
The left crus cerebri carries **three descending fiber
populations** — documented as **prose**, not as structural children:

*   **Left corticospinal fibers** — **motor** axons from the
    **left primary motor cortex** (and left premotor areas) to the
    **right spinal cord** (via the **pyramidal decussation**). The
    principal **voluntary motor** pathway for the **right limbs and
    right trunk**.

*   **Left corticobulbar fibers** — **motor** axons from the
    **left motor cortex** to the **cranial nerve motor nuclei**
    (predominantly **bilateral** for CN V, VII, IX, X, XI, XII; the
    **lower facial** and **genioglossus** targets are
    **contralateral-dominant**). The **voluntary motor** pathway
    for the **head and neck** — **predominantly bilateral** at the
    level of the cranial nerve nuclei.

*   **Left corticopontine fibers** — axons from the **left cortex**
    to the **bilateral pontine nuclei** (predominantly
    **contralateral** — the left cortex projects predominantly to
    the **right** pontine nuclei, which project to the **right**
    cerebellar hemisphere). The **corticopontocerebellar** pathway.

**These fiber populations are prose, not structural children.** The
tree wires **no** structural children under this leaf. Consumers
must **not** resolve
``.../left/crus_cerebri/corticospinal`` — no such path exists.

Somatotopy (prose — medial to lateral)
--------------------------------------
Within the **left** crus cerebri, the descending fibers are
**somatotopically organized**, **medial to lateral**:

1.  **Left corticobulbar** fibers — **most medial** (face, head,
    neck).
2.  **Left corticospinal arm** fibers — **middle-medial**
    (right arm).
3.  **Left corticospinal leg** fibers — **middle-lateral**
    (right leg).
4.  **Left corticopontine** fibers — **most lateral**.

**This somatotopy is clinically relevant** — a **medial** left-crus
lesion affects the **right face/arm** more than the **right leg**;
a **lateral** left-crus lesion affects the **right leg** more than
the **right face/arm**. The classic teaching is **"face medial, leg
lateral"** — the **left** crus's **medial** fibers carry the
**right** face; the **lateral** fibers carry the **right** leg.

The Left Crus Cerebri / Left Tegmentum Boundary
-----------------------------------------------
This is the **most consequential sibling** boundary — **narrow vs.
broad** definition on the **left side**:

*   **Left crus cerebri** (this module) — the **left descending
    fiber bundle** — **white matter**, **left ventral surface**.

*   **Left tegmentum** (``.../midbrain/tegmentum/left/``) — the
    **left grey-matter + intrinsic** midbrain — containing the
    **left red nucleus**, the **left CN III / IV nuclei**, the
    **left VTA**, the **left midbrain reticular formation**, and
    the **left periaqueductal gray** (midline-adjacent).

**They are SIBLINGS under the midbrain.** The **narrow definition**
excludes the left tegmentum from the left crus. **Consumers must
not conflate the two** — the **left crus** is the **conduit**; the
**left tegmentum** is the **processor**.

The Left Crus Cerebri / Left Substantia Nigra Boundary
------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Left crus cerebri** (this module) — the **left descending
    fiber bundle** — **white matter**.

*   **Left substantia nigra**
    (``.../midbrain/tegmentum/left/substantia_nigra/``) — the
    **dopaminergic** nucleus — **grey matter**.

**The left substantia nigra is DORSAL to the left crus cerebri.**
It is a **tegmentum child**, **not** a crus child. Consumers must
**not** conflate the two, and must **not** resolve the left
substantia nigra through the left crus cerebri path.

The Left Crus Cerebri / Left Internal Capsule Boundary
------------------------------------------------------
This is the **mesencephalic / telencephalic** boundary:

*   **Left crus cerebri** (this module) — the **left midbrain
    segment** of the descending pathway.

*   **Left internal capsule**
    (``.../forebrain/telencephalon/.../internal_capsule/left/``) —
    the **left telencephalic segment** of the **same descending
    pathway**.

**They carry the SAME left axons** — at **different rostrocaudal
levels**. Consumers must **not** conflate the two — the **internal
capsule** is **forebrain**; the **crus cerebri** is **midbrain**.

The Left Crus Cerebri / Left Basis Pontis Boundary
--------------------------------------------------
This is the **mesencephalic / rhombencephalic** boundary:

*   **Left crus cerebri** (this module) — the **left midbrain
    segment**.

*   **Left basis pontis**
    (``.../hindbrain/metencephalon/pons/.../basis_pontis/left/``) —
    the **left pontine segment**.

**They are across the pontomesencephalic junction.** Consumers must
**not** conflate the two — the **basis pontis** is **hindbrain**;
the **crus cerebri** is **midbrain**.

The Left Crus Cerebri / Left Medullary Pyramid Boundary
-------------------------------------------------------
This is the **mesencephalic / myelencephalic** boundary:

*   **Left crus cerebri** (this module) — the **left midbrain
    segment**.

*   **Left medullary pyramid**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/left/``)
    — the **left medullary segment**.

**They are across the pontomedullary junction.** Consumers must
**not** conflate the two — the **medullary pyramid** is
**hindbrain**; the **crus cerebri** is **midbrain**.

The Left Crus Cerebri / Pyramidal Decussation Boundary
------------------------------------------------------
This is the **decussation** boundary — the **reason** a left crus
lesion produces **right** hemiplegia:

*   **Left crus cerebri** (this module) — the **left midbrain
    segment** — **above** the decussation.

*   **Pyramidal decussation**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramidal_
    decussation/``) — the **caudal medullary crossing** — the
    **left** corticospinal fibers cross **here** to the **right**
    spinal cord.

**The decussation is CAUDAL to the crus cerebri** — a **left** crus
lesion produces **right** hemiplegia **because** the fibers have
**not yet crossed**. Consumers must **not** conflate the crus with
the decussation, and must **not** assume a left crus lesion produces
left-sided hemiplegia — it produces **right** hemiplegia.

The Left Crus Cerebri / CN III Fascicles Boundary
-------------------------------------------------
This is the **Weber-syndrome** boundary — **the crus is not the
nerve, but the fascicles traverse it**:

*   **Left crus cerebri** (this module) — the **left descending
    fiber bundle**.

*   **Left CN III fascicles** — the **axons** of the **left
    oculomotor nerve** traversing the **medial** aspect of the
    **left crus cerebri** **en route** to the **interpeduncular
    fossa**.

**The CN III fascicles are what make Weber syndrome alternating** —
a **left** crus lesion catches the **left CN III fascicles** (→
**left CN III palsy**) **and** the **left corticospinal fibers** (→
**right hemiplegia**). Consumers must **not** conflate the crus with
the **CN III nucleus** (left tegmentum) or the **CN III nerve**
(peripheral) — but must **not** forget the fascicles.

The Left Crus Cerebri / Basal Ganglia Boundary
----------------------------------------------
This is the **white-matter / grey-matter** boundary within the
forebrain:

*   **Left crus cerebri** (this module) — the **left midbrain
    descending fiber bundle**.

*   **Left basal ganglia**
    (``.../forebrain/telencephalon/.../basal_ganglia/left/``) — the
    **left telencephalic grey-matter nuclei** (left striatum, left
    globus pallidus, etc.).

**The left basal ganglia are NOT on the descending pathway carried
by the crus** — they are a **parallel** motor system. Consumers
must **not** conflate the two.

The Left Crus Cerebri / Right Crus Cerebri Boundary
---------------------------------------------------
This is the **side** boundary — the **strict-mirror, NO-warning**
relationship:

*   **Left crus cerebri** (this module) — the **left** crus.

*   **Right crus cerebri**
    (``.../cerebral_peduncle/right/crus_cerebri/``) — the **right**
    crus.

**They are STRICTLY SYMMETRIC CONDUCTION PATHWAYS** — each carries
**its own** descending axons, and the two are **not coupled**.
Consumers must **not** conflate the two, and must **not** assume a
left lesion and a right lesion produce mirror-image deficits —
**a left crus lesion produces LEFT CN III palsy + RIGHT hemiplegia**,
and a **right** crus lesion produces **RIGHT CN III palsy + LEFT
hemiplegia**. The **CN III palsy is IPSILATERAL**; the **hemiplegia
is CONTRALATERAL**.

The Left Crus Cerebri / ``left/`` Side Container Boundary
---------------------------------------------------------
This is the **leaf / container** boundary — **structural
clarification**:

*   **Left crus cerebri** (this module) — the **substantive leaf**.

*   **``left/`` module** (``.../cerebral_peduncle/left/``) — the
    **side-scoped namespace** that holds this leaf.

**The ``left/`` module is a SIDE CONTAINER, not a leaf.** The
earlier ``left/__init__.py`` was written with leaf-level prose *and*
a Usage block resolving ``.../left.crus_cerebri`` — this module
resolves the disagreement in favor of the **tree structure**.
Consumers that resolve ``.../cerebral_peduncle/left`` and expect a
leaf should go **one level deeper** to
``.../cerebral_peduncle/left/crus_cerebri``.

Function in the Human Brain
---------------------------
The left crus cerebri's function is **descending motor and
corticopontine conduction on the left side** — **NOT** rhythm
generation, **NOT** motor programming, **NOT** sensory processing:

*   **Left Corticospinal Conduction (right voluntary motor):** The
    left crus **carries** the **left corticospinal** axons from the
    **left cortex** to the **right spinal cord** — the **voluntary
    motor** pathway for the **right limbs and right trunk**.

*   **Left Corticobulbar Conduction (predominantly bilateral
    cranial motor):** The left crus **carries** the **left
    corticobulbar** axons from the **left cortex** to the
    **bilateral cranial nerve motor nuclei** — predominantly
    **bilateral** innervation, with **contralateral dominance** for
    the **lower facial** and **genioglossus** targets.

*   **Left Corticopontine Conduction (contralateral cerebellar
    input):** The left crus **carries** the **left corticopontine**
    axons from the **left cortex** to the **bilateral pontine
    nuclei** (predominantly **right** pontine nuclei), providing the
    **right** cerebellar hemisphere with **left cortical input**.

*   **NOT a processor.** The left crus **carries** axons; it does
    **not** process them. It has **no neurons of its own**.

*   **NOT an oscillator.** The **oscillators** are the
    **pre-Bötzinger complex**, the **Bötzinger complex**, and the
    **pFRG** — **brainstem respiratory oscillators**. The left crus
    is a **conduction pathway** — it does **not** generate a
    rhythm.

*   **NOT the basal ganglia.** The left basal ganglia are the
    **telencephalic** motor-modulation system. The left crus is the
    **descending conduit** — it does **not** modulate; it
    **carries**.

**The unifying theme:** the left crus cerebri is the **left midbrain
segment of the descending corticofugal pathway** — a **white-matter
conduit** carrying the **left corticospinal**, **left
corticobulbar**, and **left corticopontine** axons. It is a
**conduction pathway**, **NOT** a processor (**left tegmentum**),
**NOT** a grey-matter nucleus (**left substantia nigra**), **NOT**
the whole pyramidal tract, and **NOT** the internal capsule / basis
pontis / medullary pyramid.

Associated Disorders
--------------------
The left crus cerebri has a **direct clinical association** with
**left-sided Weber syndrome** — its clinical relevance is
**direct**, via the **left crus** and the **left CN III fascicles**
that traverse it:

*   **Left Weber Syndrome (alternating oculomotor hemiplegia — LEFT,
    DIRECT, via the left crus cerebri):** A **left ventral midbrain**
    lesion (**infarction** — most commonly **paramedian midbrain**
    from **basilar artery** perforators; **hemorrhage**; **tumor**;
    **tentorial herniation**) involving the **left crus cerebri**
    and the **left CN III fascicles** produces:
    *   **Ipsilateral (LEFT) CN III palsy** — **left ptosis**,
        **left mydriasis**, **left "down and out" eye** — from the
        **left CN III fascicle** involvement.
    *   **Contralateral (RIGHT) spastic hemiplegia** — from the
        **left corticospinal** fiber involvement in the **left
        crus**.
    **Weber syndrome lateralizes** — a **left** crus lesion
    produces **left CN III palsy + right hemiplegia**, and a
    **right** crus lesion produces **right CN III palsy + left
    hemiplegia**. **Left Weber syndrome is the named disorder of
    the left crus cerebri** — **direct**, not indirect.

*   **Wallerian Degeneration of the Left Crus Cerebri
    (DESCRIPTIVE):** Large **left cortical** or **left internal
    capsule** strokes produce **Wallerian degeneration** of the
    **ipsilateral (left) crus cerebri** — visible on **MRI** as
    **T2 hyperintensity** and **atrophy** of the **left crus**.
    This is **descriptive**, not a named syndrome — the **primary
    lesion** is **upstream**.

*   **Progressive Supranuclear Palsy (PSP — NOT the crus):** The
    "**hummingbird sign**" of PSP is a **midbrain tegmentum**
    measure — **not** a crus cerebri measure. **PSP belongs to the
    tegmentum**, not to this module.

*   **ALS (INDIRECT — via the left corticospinal tract, not the crus
    as a named site):** **ALS** affects the **left corticospinal
    tract** — including the fibers that pass through the **left
    crus** — but the **left crus is not a named site** of ALS
    pathology. This is **indirect**.

*   **No Named "Left Crus Cerebri Syndrome" (apart from left
    Weber):** The left crus is a **white-matter conduit** — its
    only named syndrome is **left Weber syndrome** (alternating
    oculomotor hemiplegia with left CN III palsy). Its clinical
    relevance is **direct**, via the **left crus** and the **left
    CN III fascicles**.

**What is NOT here:** The left crus cerebri is **not** the substrate
for **Benedikt syndrome** (left tegmentum — red nucleus + left
CN III), **Claude syndrome** (left tegmentum — red nucleus + left
CN III), **Parinaud syndrome** (dorsal midbrain — superior
colliculus / tectum), **Nothnagel syndrome** (tectum / colliculi),
**Millard-Gubler syndrome** (pons), **Wallenberg syndrome** (lateral
medulla), **locked-in syndrome** (basis pontis), **CCHS** (RTN),
**OIRD** (pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger complex
+ arcuate nucleus), **essential hypertension / sympathetic
overactivity** (C1 group / RVLM), **Parkinson's disease** (left
substantia nigra — tegmentum), **Huntington's disease** (left
striatum — telencephalon), or **Kluver-Bucy syndrome** (amygdala).
Its clinical relevance is **direct**, via **left Weber syndrome**.
**Left Weber syndrome is the named disorder.**

Lateralization Notes
--------------------
This is the **left** crus cerebri leaf. The left and right crura are
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
    single rhythm. The **left crus cerebri** is a **conduction
    pathway** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. Its **left**
    and **right** sides are **independent conduits** — there is
    **no** crus–crus coupling. **This extends the propagatable
    rule:** **coupling warnings attach to oscillators — not to
    premotor pools, not to sensor nuclei, and not to conduction
    pathways.**

*   **NO SLEA Warning:** The left crus cerebri is **SLEA-free** — it
    is **not** an extended-amygdala component.

*   **NO Amygdala-Lateralization Warning:** The left crus cerebri is
    **not** part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **NO Rhinencephalon-Exclusion Flag:** The left crus cerebri is
    **not** a rhinencephalon structure — it carries **no**
    rhinencephalon-exclusion flag.

**A consumer that assumes "left crus cerebri = right crus cerebri"
will be structurally correct** — the two sides are **symmetric** and
**functionally independent as conduits**. The left crus cerebri is a
**strict-mirror pair with NO warning** — **no coupling warning**,
**no SLEA warning**, **no amygdala-lateralization warning**, and
**no rhinencephalon-exclusion flag**. Consumers must **not** assume
the two sides produce **mirror-image** deficits — **left** crus
lesions produce **left** CN III palsy + **right** hemiplegia, and
**right** crus lesions produce **right** CN III palsy + **left**
hemiplegia.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — **no** import
    from ``.../right/crus_cerebri/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/tegmentum/``, ``.../midbrain/tectum/``, the
    **internal capsule**, the **basis pontis**, the **medullary
    pyramid**, the **pyramidal decussation**, the **basal ganglia**,
    or any other container. The left crus cerebri's relationships to
    the left tegmentum, the left substantia nigra, the left internal
    capsule, the left basis pontis, the left medullary pyramid, the
    pyramidal decussation, the left basal ganglia, and the left
    CN III fascicles are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **dopaminergic
    phenotype** of the left substantia nigra is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the tegmentum leaf, **not** here.
*   **Leaf module — no structural children.** The **left
    corticospinal**, **left corticobulbar**, and **left
    corticopontine** fiber populations are documented as **prose**,
    not as sub-modules. Consumers must not assume any exist as
    children; resolve **fiber-population-level** detail through the
    references.
*   **NARROW DEFINITION — the leaf is the LEFT CRUS CEREBRI, NOT the
    whole left ventral midbrain.** The **left tegmentum** and
    **left substantia nigra** are **separate siblings** — they are
    **not** part of this module.
*   **WHITE-MATTER CONDUCTION PATHWAY — NOT a grey-matter nucleus,
    NOT an oscillator, NOT a premotor pool, NOT a sensor nucleus.**
    It carries descending axons — it does **not** process them.
*   **NOT the left tegmentum — the left tegmentum is a SIBLING.**
*   **NOT the left substantia nigra — the left substantia nigra is a
    TEGMENTUM structure.**
*   **NOT the left internal capsule or corona radiata — those are
    FOREBRAIN structures.**
*   **NOT the left basis pontis — that is a HINDBRAIN structure.**
*   **NOT the left medullary pyramid — that is a HINDBRAIN
    structure.**
*   **NOT the left pyramidal decussation — that is a CAUDAL
    MYELENCEPHALIC structure** — and it is **the reason** a left
    crus lesion produces **right** hemiplegia.
*   **NOT the left CN III nucleus or the left CN III nerve — the
    CN III FASCICLES traverse the crus but do not define it.** The
    CN III fascicles are **what make Weber syndrome alternating**.
*   **NO coupling warning — the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS.** The left crus
    cerebri is a **strict mirror with NO warning**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The left crus cerebri is a local leaf
    under the left side container of the cerebral peduncle, not a
    cross-listed leaf.
*   **No nested cross-listing.** The left crus cerebri has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with the right crus cerebri — strict mirror
    with NO warning.** Left and right crus cerebri modules are
    **structurally identical** — same leaf status, same **crus
    cerebri** framing, same **conduction-pathway** framing, same
    **no warning**.
*   **STRUCTURAL RECONCILIATION — the ``left/`` module should be
    reduced to a thin side container.** The earlier
    ``.../cerebral_peduncle/left/__init__.py`` carried substantive
    leaf-level prose **and** a Usage block resolving
    ``.../left.crus_cerebri``. This leaf resolves that disagreement:
    **this module carries the substantive leaf-level prose**; the
    ``left/__init__.py`` module **should be reduced** to a
    **side-scoped namespace** — a short container docstring pointing
    at this leaf, with the substantive content (fiber populations,
    somatotopy, boundary stack, Weber syndrome) **moving** here.
    Consumers should resolve the **leaf** (this module) for
    substantive content, and the **container** (``left/``) only for
    side-scoped enumeration.

Usage
-----
Resolve by path (the leaf — substantive content)::

    from infrastructure.brainparts.midbrain.cerebral_peduncle.left.crus_cerebri import (
        CEREBRAL_PEDUNCLE_LEFT_CRUS_CEREBRI_CHILDREN,
    )

Or by fully-qualified path string::

    path = "midbrain.cerebral_peduncle.left.crus_cerebri"

**Do not** assume the left crus cerebri is the **whole left ventral
midbrain** (the broad classical definition). It is the **left crus
cerebri** — **narrow definition** — because the **left tegmentum**
and **left substantia nigra** are **separate siblings**.

**Do not** assume the left crus cerebri is the **left tegmentum** or
the **left substantia nigra**. Those are **separate structures** —
the **left tegmentum** is the grey-matter + intrinsic midbrain; the
**left substantia nigra** is a **tegmentum child**.

**Do not** assume the left crus cerebri is the **left internal
capsule** (telencephalic) or the **left basis pontis** (pontine) or
the **left medullary pyramid** (medullary). Those are **segments**
of the same descending pathway at **different rostrocaudal levels**.

**Do not** assume the left crus cerebri is the **left pyramidal
tract as a whole**. It is **one segment** — the **left midbrain
segment**.

**Do not** assume the left crus cerebri is the **left CN III nucleus**
or the **left CN III nerve**. The **left CN III fascicles traverse**
the crus medially, but they are **not** the crus.

**Do not** assume a **left** crus lesion produces **left**
hemiplegia. The **left corticospinal** fibers **decussate in the
medulla** — a **left** crus lesion produces **right** hemiplegia
(and **left** CN III palsy — the "alternating" pattern).

**Do not** assume the left crus cerebri contains structural
**fiber-population children**. The **left corticospinal**,
**left corticobulbar**, and **left corticopontine** fibers are
**prose**, not modules. There is **no**
``.../left/crus_cerebri/corticospinal``.

**Do not** import the **oscillator coupling warning** into the left
crus cerebri. **It is a CONDUCTION PATHWAY** — it carries **NO
coupling warning**.

**Do not** resolve substantive content from the **``left/`` side
container**. The **leaf** (this module) carries the substantive
prose — the **container** (``left/``) is a **side-scoped
namespace**. If a consumer finds itself reading the ``left/`` module
for fiber populations, somatotopy, or Weber-syndrome detail, it has
resolved **one level too shallow** — go one level deeper to this
leaf.

Iterating the left crus cerebri's (empty) children (recommended
consumer pattern)::

    CEREBRAL_PEDUNCLE_LEFT_CRUS_CEREBRI_CHILDREN = ()
    # The left crus cerebri is a leaf. The left corticospinal,
    # left corticobulbar, and left corticopontine fiber populations
    # are prose, not modules.

Reaching the left side container (recommended consumer pattern —
NOTE it is a CONTAINER, not a leaf)::

    # The left/ module is the SIDE-SCOPED CONTAINER that holds this
    # leaf:
    #
    #   brainparts.midbrain.cerebral_peduncle.left
    #
    # Do NOT resolve substantive content from left/ — the leaf
    # (this module) carries the fiber populations, somatotopy,
    # boundary stack, and Weber-syndrome detail.

Reaching the right crus cerebri (recommended consumer pattern — the
SIDE sibling)::

    # The right crus cerebri is the RIGHT descending fiber bundle:
    #
    #   brainparts.midbrain.cerebral_peduncle.right.crus_cerebri
    #
    # The two sides are STRICTLY SYMMETRIC CONDUCTION PATHWAYS
    # — each carries its own descending axons. There is NO
    # coupling between them.

Reaching the left tegmentum (recommended consumer pattern — the
grey-matter sibling)::

    # The left tegmentum is the LEFT GREY-MATTER + INTRINSIC
    # midbrain — left substantia nigra, left VTA, left red
    # nucleus, left PAG, left CN III/IV nuclei, left
    # Edinger-Westphal, left mesencephalic trigeminal, left
    # midbrain reticular formation:
    #
    #   brainparts.midbrain.tegmentum.left
    #
    # The left crus cerebri is the WHITE-MATTER conduit; the left
    # tegmentum is the GREY-MATTER processor.

Reaching the left substantia nigra (recommended consumer pattern —
the tegmentum child, NOT a crus child)::

    # The left substantia nigra is a LEFT TEGMENTUM child — the
    # dopaminergic nucleus DORSAL to the left crus cerebri:
    #
    #   brainparts.midbrain.tegmentum.left.substantia_nigra
    #
    # The left crus cerebri is the WHITE-MATTER bundle VENTRAL to
    # the left substantia nigra. The narrow definition excludes the
    # left substantia nigra from the crus.

Reaching the left internal capsule (recommended consumer pattern —
the TELENCEPHALIC segment)::

    # The left internal capsule is the LEFT TELENCEPHALIC segment
    # of the descending pathway — the same left corticospinal /
    # corticobulbar / corticopontine axons at a more rostral level:
    #
    #   brainparts.forebrain.telencephalon...internal_capsule.left
    #
    # The left crus cerebri is the LEFT MESENCEPHALIC segment.

Reaching the left basis pontis (recommended consumer pattern — the
RHOMBENCEPHALIC segment)::

    # The left basis pontis is the LEFT PONTINE segment of the
    # descending pathway:
    #
    #   brainparts.hindbrain.metencephalon.pons...basis_pontis.left
    #
    # The left crus cerebri is the LEFT MESENCEPHALIC segment.

Reaching the left medullary pyramid (recommended consumer pattern —
the MYELENCEPHALIC segment)::

    # The left medullary pyramid is the LEFT MEDULLARY segment of
    # the descending pathway:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata...
    #   pyramid.left
    #
    # The left crus cerebri is the LEFT MESENCEPHALIC segment.

Reaching the pyramidal decussation (recommended consumer pattern —
NOTE the decussation is CAUDAL to the crus)::

    # The pyramidal decussation is the CAUDAL MEDULLARY crossing
    # at which the LEFT corticospinal fibers cross to the RIGHT
    # spinal cord:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata...
    #   pyramidal_decussation
    #
    # The decussation is CAUDAL to the crus — this is the REASON a
    # LEFT crus lesion produces RIGHT hemiplegia.

Fiber-population-level detail (not wired — consult references)::

    # The left crus cerebri's fiber populations are prose, not
    # modules:
    #   left corticospinal  -> right voluntary motor (limbs, trunk)
    #                          somatotopy: right arm medial,
    #                          right leg lateral
    #   left corticobulbar  -> bilateral cranial motor
    #                          (predominantly bilateral;
    #                          right-dominant for lower face and
    #                          genioglossus) somatotopy: most
    #                          medial
    #   left corticopontine -> right cerebellar input
    #                          (predominantly contralateral)
    #                          somatotopy: most lateral
    #
    # Do not attempt to resolve these as sub-paths of the left
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
        # NOTE: Weber syndrome lateralizes — a LEFT crus lesion
        # produces LEFT CN III palsy + RIGHT hemiplegia, and a
        # RIGHT crus lesion produces RIGHT CN III palsy + LEFT
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
*   **SLEA (contrast — the left crus cerebri is not SLEA):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the crus cerebri.)
*   NeuroNames — Crus cerebri (left); FMA — Crus cerebri (left
    member).
"""