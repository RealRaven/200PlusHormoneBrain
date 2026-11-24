"""
infrastructure.brainparts.midbrain.cerebral_peduncle.right
==========================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── cerebral_peduncle
        ├── left
        └── right                  <-- THIS MODULE (leaf)

**Primary synonym:** Right cerebral peduncle; **right crus cerebri**;
right basis pedunculi (when the substantia nigra is included — **not**
here). The **right** member of the paired crus cerebri.
**Cytoarchitectonic designation:** **Not a Brodmann area** and **not
a grey-matter nucleus** — the right cerebral peduncle is a
**white-matter fiber bundle** (a **conduction pathway**). It carries
**descending corticofugal axons**, not cell bodies. It has **no
neurons of its own**.
**Part of:** The **cerebral_peduncle** container — the **right**
member of the paired crus cerebri. The **cerebral_peduncle** is, in
turn, a child of the **midbrain** (mesencephalon) container, on the
**ventral** surface, **ventral to the substantia nigra** and the
**tegmentum**.
**Structural parent:** ``.../cerebral_peduncle/`` → **direct child**
of the cerebral peduncle container.
**Structural children:** **None.** This is a **leaf** module. The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are documented as **prose**, not as structural children.
**Boundary status (NOT the cerebral_peduncle container — a LEAF child
of the container):** **Boundary case — the right cerebral peduncle is
a LEAF child of the cerebral_peduncle container, not the container
itself.** The **container** (``.../cerebral_peduncle/``) holds the
**left** and **right** peduncles. The **right** leaf (here) is
**one** of the two. Consumers must **not** conflate the right
peduncle with the container, and must **not** resolve the left
peduncle through the right path.
**Boundary status (NOT the left cerebral peduncle — the SIDE
boundary):** **Boundary case — the right cerebral peduncle is NOT the
left cerebral peduncle.** The **left** leaf
(``.../cerebral_peduncle/left/``) is the **left** crus cerebri.
**They are DIFFERENT STRUCTURES** on **opposite sides** — each
carries **its own** descending axons, and each is the **contralateral
hemiplegia** substrate for a **ipsilateral** peduncular lesion.
Consumers must **not** conflate the two, and must **not** assume a
right-peduncle lesion produces right-sided hemiplegia — the
**corticospinal** fibers **decussate in the medulla**, **caudal** to
the peduncle, so a **right** peduncle lesion produces **left**
hemiplegia.
**Boundary status (NARROW DEFINITION — the leaf is the RIGHT CRUS
CEREBRI, NOT the whole right ventral midbrain):** **Boundary case —
the right cerebral peduncle is the RIGHT CRUS CEREBRI (narrow
definition), NOT the whole right ventral midbrain (broad
definition).** The **broad** classical definition (crus cerebri +
substantia nigra + tegmentum) is **rejected** — the **right
tegmentum** and **right substantia nigra** are **separate siblings**
under the midbrain. The **narrow definition** is the **only** one
consistent with the tree.
**Boundary status (NOT the right tegmentum — the right tegmentum is a
SIBLING under the midbrain):** **Boundary case — the right cerebral
peduncle is NOT the right tegmentum.** The **right tegmentum**
(``.../midbrain/tegmentum/right/``) contains the **right substantia
nigra**, the **right ventral tegmental area**, the **right red
nucleus**, the **right periaqueductal gray** (midline — shared),
the **right oculomotor nucleus** (CN III), the **right trochlear
nucleus** (CN IV), the **right Edinger-Westphal nucleus**, the
**right mesencephalic trigeminal nucleus** (CN V), and the **right
midbrain reticular formation**. The **right cerebral peduncle**
(here) is the **right crus cerebri** — the **descending fiber
bundle** on the **right ventral surface**. **They are DIFFERENT
STRUCTURES** — the **right tegmentum** is the **grey-matter +
intrinsic** midbrain; the **right cerebral peduncle** is the
**white-matter conduit**. Consumers must **not** conflate the two,
and must **not** resolve a right tegmentum structure (right
substantia nigra, right red nucleus, right CN III/IV nuclei) through
the right cerebral peduncle path.
**Boundary status (NOT the right substantia nigra — the right
substantia nigra is a TEGMENTUM structure):** **Boundary case — the
right cerebral peduncle is NOT the right substantia nigra.** The
**right substantia nigra**
(``.../midbrain/tegmentum/right/substantia_nigra/``) is the
**dopaminergic** nucleus **dorsal to the right crus cerebri** — it
is a **grey-matter** structure and a **tegmentum child**. The **right
cerebral peduncle** (here) is the **white-matter bundle ventral to
the right substantia nigra**. **They are DIFFERENT STRUCTURES** —
the **right substantia nigra** is **grey matter**; the **right
cerebral peduncle** is **white matter**. Consumers must **not**
conflate the two, and must **not** resolve the right substantia
nigra through the right cerebral peduncle path.
**Boundary status (NOT the right internal capsule — the internal
capsule is TELENCEPHALIC):** **Boundary case — the right cerebral
peduncle is NOT the right internal capsule.** The **right internal
capsule**
(``.../forebrain/telencephalon/.../internal_capsule/right/``) is the
**telencephalic segment** of the **same descending pathway** —
it carries the **same** right **corticospinal**, **corticobulbar**,
and **corticopontine** axons at a **more rostral** level. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **internal
capsule** is **telencephalic**; the **right cerebral peduncle** is
**mesencephalic**. Consumers must **not** conflate the two, and
must **not** resolve the right internal capsule through the midbrain
path.
**Boundary status (NOT the right basis pontis — the basis pontis is
RHOMBENCEPHALIC):** **Boundary case — the right cerebral peduncle is
NOT the right basis pontis.** The **right basis pontis**
(``.../hindbrain/metencephalon/pons/.../basis_pontis/right/``) is the
**pontine segment** of the **same descending pathway** — caudal to
the midbrain, across the **pontomesencephalic junction**. **They are
DIFFERENT STRUCTURES across a lobe boundary** — the **basis pontis**
is **rhombencephalic**; the **right cerebral peduncle** is
**mesencephalic**. Consumers must **not** conflate the two.
**Boundary status (NOT the right medullary pyramid — the pyramid is
MYELENCEPHALIC):** **Boundary case — the right cerebral peduncle is
NOT the right medullary pyramid.** The **right medullary pyramid**
(``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/right/``)
is the **medullary segment** of the **same descending pathway**.
**They are DIFFERENT STRUCTURES across a lobe boundary** — the
**pyramid** is **myelencephalic**; the **right cerebral peduncle** is
**mesencephalic**. Consumers must **not** conflate the two.
**Boundary status (NOT the right pyramidal decussation — the
decussation is MYELENCEPHALIC and CONTRALATERAL):** **Boundary
case — the right cerebral peduncle is NOT the right pyramidal
decussation.** The **pyramidal decussation**
(``.../hindbrain/myencephalon/medulla_oblongata/.../pyramidal_
decussation/``) is the **caudal medullary crossing** at which the
**right** corticospinal fibers cross to the **left** side of the
spinal cord. **The decussation is CAUDAL to the peduncle** — it is
the **reason** a **right** peduncle lesion produces **left**
hemiplegia. Consumers must **not** conflate the peduncle with the
decussation, and must **not** assume the right peduncle projects to
the right spinal cord — it projects to the **left** spinal cord.
**Boundary status (NOT the pyramidal tract as a whole — the peduncle
is ONE SEGMENT of the pyramidal tract):** **Boundary case — the
right cerebral peduncle is NOT the right pyramidal tract.** The
**pyramidal tract** (corticospinal tract) is the **whole pathway**
from the **right cerebral cortex** to the **left spinal cord** — it
includes the **corona radiata**, the **internal capsule**, the
**right cerebral peduncle**, the **right basis pontis**, the **right
medullary pyramid**, the **pyramidal decussation**, and the **left
corticospinal tracts** in the spinal cord. The **right cerebral
peduncle** (here) is **one segment** of that pathway. Consumers
must **not** conflate the peduncle with the whole pyramidal tract.
**Boundary status (NOT the right basal ganglia — the basal ganglia
are a PARALLEL motor system):** **Boundary case — the right
cerebral peduncle is NOT the right basal ganglia.** The **right basal
ganglia**
(``.../forebrain/telencephalon/.../basal_ganglia/right/``) are the
**telencephalic grey-matter nuclei** (right striatum, right globus
pallidus, right substantia nigra pars reticulata, etc.) — a
**parallel** motor-modulation system. The **right cerebral peduncle**
(here) is the **descending conduit** — it does **not** modulate;
it **carries**. Consumers must **not** conflate the two.
**Boundary status (NOT the right CN III nucleus or the right CN III
nerve — the CN III FASCICLES traverse the peduncle but do not
define it):** **Boundary case — the right cerebral peduncle is NOT
the right oculomotor (CN III) nucleus and NOT the right oculomotor
nerve.** The **right oculomotor nucleus**
(``.../midbrain/tegmentum/right/oculomotor_nucleus/``) is the
**CN III grey-matter nucleus** in the right tegmentum. The **right
oculomotor nerve** is the **peripheral** bundle wired elsewhere.
The **right CN III fascicles TRAVERSE the right cerebral peduncle**
(medially) **en route** to the interpeduncular fossa — but the
fascicles are **axons passing through**, not **structures of** the
peduncle. **They are DIFFERENT STRUCTURES** — the **CN III nucleus**
is grey matter; the **CN III nerve** is peripheral; the **CN III
fascicles** are fibers traversing the peduncle. Consumers must
**not** conflate the peduncle with the CN III nucleus or nerve,
**and** must **not** forget that the CN III fascicles are what make
**Weber syndrome** alternating.
**Boundary status (WHITE MATTER — NOT a grey-matter nucleus, NOT an
oscillator, NOT a premotor pool, NOT a sensor nucleus):** **Boundary
case — the right cerebral peduncle is a WHITE-MATTER CONDUCTION
PATHWAY.** It is **not** an oscillator (no intrinsic rhythm), **not**
a premotor pool (no cell bodies, no pattern shaping), **not** a
sensor nucleus (no transduction), and **not** a motoneuron pool (no
motor neurons). It is a **conduit** — it **carries** descending
axons **generated** in the **right cortex** and **destined** for the
**left spinal cord**, the **bilateral cranial nerve motor nuclei**,
or the **bilateral pontine nuclei**. **Structure-class taxonomy:**
**coupling warnings attach to oscillators — not to premotor pools,
not to sensor nuclei, and not to conduction pathways.** The **right
cerebral peduncle** is a **conduction pathway** — it carries **NO
coupling warning**, **NO SLEA warning**, **NO
amygdala-lateralization warning**, and **NO rhinencephalon-exclusion
flag**. It is a **strict mirror with NO warning**.
**Boundary status (NOT the fiber populations as structural children
— corticospinal, corticobulbar, corticopontine are PROSE):**
**Boundary case — the right cerebral peduncle is a SINGLE fiber
bundle, NOT a container of three structural children.** The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are **fiber types within the peduncle**, not
**sub-modules**. The tree wires **no** structural children under the
right leaf. Consumers must **not** resolve
``cerebral_peduncle.right.corticospinal`` — no such path exists.

Overview
--------
The right cerebral peduncle is the **right crus cerebri** — the
**ventral-most descending white-matter bundle** of the **right
midbrain**, the **right midbrain segment** of the **corticofugal**
pathways. It carries the **right corticospinal**, **right
corticobulbar**, and **right corticopontine** fiber populations on
the **right ventral midbrain surface**. It is a **leaf** under the
**cerebral_peduncle** container.

**The right cerebral peduncle is the RIGHT CRUS CEREBRI, NOT the
whole right ventral midbrain.** The **broad** classical definition
(crus cerebri + substantia nigra + tegmentum) is **rejected** — the
**right tegmentum** and **right substantia nigra** are **separate
siblings** under the midbrain.

**The right cerebral peduncle is a WHITE-MATTER CONDUCTION PATHWAY,
NOT a grey-matter nucleus.** It has **no neurons of its own** — it
**carries** descending axons **generated** in the **right cortex**.

**The right cerebral peduncle is a strictly independent conduit.** It
carries the **right** descending axons, which **decussate in the
medulla** to innervate the **left** spinal cord. There is **no
left–right peduncular coupling** — the two peduncles are
**independent conduction pathways**. It carries **NO coupling
warning** (it is a **conduction pathway**, not an oscillator). See
*Lateralization Notes*.

Fiber Populations (prose, not structural children)
--------------------------------------------------
The right cerebral peduncle carries **three descending fiber
populations** — documented as **prose**, not as structural children:

*   **Right corticospinal fibers** — **motor** axons from the
    **right primary motor cortex** (and right premotor areas) to
    the **left spinal cord** (via the **pyramidal decussation**).
    The principal **voluntary motor** pathway for the **left limbs
    and left trunk**.

*   **Right corticobulbar fibers** — **motor** axons from the
    **right motor cortex** to the **cranial nerve motor nuclei**
    (predominantly **bilateral** for CN V, VII, IX, X, XI, XII; the
    **lower facial** and **genioglossus** targets are
    **contralateral-dominant**). The **voluntary motor** pathway
    for the **head and neck** — **predominantly bilateral** at the
    level of the cranial nerve nuclei.

*   **Right corticopontine fibers** — axons from the **right
    cortex** to the **bilateral pontine nuclei** (predominantly
    **contralateral** — the right cortex projects predominantly to
    the **left** pontine nuclei, which project to the **left**
    cerebellar hemisphere). The **corticopontocerebellar** pathway.

**These fiber populations are prose, not structural children.** The
tree wires **no** structural children under the right leaf.
Consumers must **not** resolve
``cerebral_peduncle.right.corticospinal`` — no such path exists.

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
lateral"** — the **right** peduncle's **medial** fibers carry the
**left** face; the **lateral** fibers carry the **left** leg.

The Right Cerebral Peduncle / Right Tegmentum Boundary
-----------------------------------------------------
This is the **most consequential sibling** boundary — **narrow vs.
broad** definition on the **right side**:

*   **Right cerebral peduncle** (this module) — the **right crus
    cerebri** — **white matter**, **right ventral surface**.

*   **Right tegmentum** (``.../midbrain/tegmentum/right/``) — the
    **right grey-matter + intrinsic** midbrain — containing the
    **right red nucleus**, the **right CN III / IV nuclei**, the
    **right VTA**, the **right midbrain reticular formation**, and
    the **right periaqueductal gray** (midline-adjacent).

**They are SIBLINGS under the midbrain.** The **narrow definition**
excludes the right tegmentum from the right peduncle. **Consumers
must not conflate the two** — the **right peduncle** is the
**conduit**; the **right tegmentum** is the **processor**.

The Right Cerebral Peduncle / Right Substantia Nigra Boundary
------------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Right cerebral peduncle** (this module) — the **right crus
    cerebri** — **white matter**.

*   **Right substantia nigra**
    (``.../midbrain/tegmentum/right/substantia_nigra/``) — the
    **dopaminergic** nucleus — **grey matter**.

**The right substantia nigra is DORSAL to the right crus cerebri.**
It is a **tegmentum child**, **not** a peduncle child. Consumers
must **not** conflate the two, and must **not** resolve the right
substantia nigra through the right cerebral peduncle path.

The Right Cerebral Peduncle / Right Internal Capsule Boundary
------------------------------------------------------------
This is the **mesencephalic / telencephalic** boundary:

*   **Right cerebral peduncle** (this module) — the **right midbrain
    segment** of the descending pathway.

*   **Right internal capsule**
    (``.../forebrain/telencephalon/.../internal_capsule/right/``) —
    the **right telencephalic segment** of the **same descending
    pathway**.

**They carry the SAME right axons** — at **different rostrocaudal
levels**. Consumers must **not** conflate the two — the **internal
capsule** is **forebrain**; the **cerebral peduncle** is
**midbrain**.

The Right Cerebral Peduncle / Right Basis Pontis Boundary
--------------------------------------------------------
This is the **mesencephalic / rhombencephalic** boundary:

*   **Right cerebral peduncle** (this module) — the **right midbrain
    segment**.

*   **Right basis pontis**
    (``.../hindbrain/metencephalon/pons/.../basis_pontis/right/``) —
    the **right pontine segment**.

**They are across the pontomesencephalic junction.** Consumers must
**not** conflate the two — the **basis pontis** is **hindbrain**;
the **cerebral peduncle** is **midbrain**.

The Right Cerebral Peduncle / Right Medullary Pyramid Boundary
-------------------------------------------------------------
This is the **mesencephalic / myelencephalic** boundary:

*   **Right cerebral peduncle** (this module) — the **right midbrain
    segment**.

*   **Right medullary pyramid**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/right/``)
    — the **right medullary segment**.

**They are across the pontomedullary junction.** Consumers must
**not** conflate the two — the **medullary pyramid** is
**hindbrain**; the **cerebral peduncle** is **midbrain**.

The Right Cerebral Peduncle / Pyramidal Decussation Boundary
------------------------------------------------------------
This is the **decussation** boundary — the **reason** a right
peduncular lesion produces **left** hemiplegia:

*   **Right cerebral peduncle** (this module) — the **right midbrain
    segment** — **above** the decussation.

*   **Pyramidal decussation**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramidal_
    decussation/``) — the **caudal medullary crossing** — the
    **right** corticospinal fibers cross **here** to the **left**
    spinal cord.

**The decussation is CAUDAL to the peduncle** — a **right**
peduncular lesion produces **left** hemiplegia **because** the
fibers have **not yet crossed**. Consumers must **not** conflate the
peduncle with the decussation, and must **not** assume a right
peduncular lesion produces right-sided hemiplegia — it produces
**left** hemiplegia.

The Right Cerebral Peduncle / CN III Fascicles Boundary
-------------------------------------------------------
This is the **Weber-syndrome** boundary — **the peduncle is not the
nerve, but the fascicles traverse it**:

*   **Right cerebral peduncle** (this module) — the **right crus
    cerebri**.

*   **Right CN III fascicles** — the **axons** of the **right
    oculomotor nerve** traversing the **medial** aspect of the
    **right crus cerebri** **en route** to the **interpeduncular
    fossa**.

**The CN III fascicles are what make Weber syndrome alternating** —
a **right** peduncular lesion catches the **right CN III fascicles**
(→ **right CN III palsy**) **and** the **right corticospinal
fibers** (→ **left hemiplegia**). Consumers must **not** conflate
the peduncle with the **CN III nucleus** (right tegmentum) or the
**CN III nerve** (peripheral) — but must **not** forget the
fascicles.

The Right Cerebral Peduncle / Basal Ganglia Boundary
----------------------------------------------------
This is the **white-matter / grey-matter** boundary within the
forebrain:

*   **Right cerebral peduncle** (this module) — the **right midbrain
    descending fiber bundle**.

*   **Right basal ganglia**
    (``.../forebrain/telencephalon/.../basal_ganglia/right/``) — the
    **right telencephalic grey-matter nuclei** (right striatum,
    right globus pallidus, etc.).

**The right basal ganglia are NOT on the descending pathway carried
by the peduncle** — they are a **parallel** motor system.
Consumers must **not** conflate the two.

The Right Cerebral Peduncle / Left Cerebral Peduncle Boundary
-------------------------------------------------------------
This is the **side** boundary — the **strict-mirror, NO-warning**
relationship:

*   **Right cerebral peduncle** (this module) — the **right crus
    cerebri**.

*   **Left cerebral peduncle** (``.../cerebral_peduncle/left/``)
    — the **left crus cerebri**.

**They are STRICTLY SYMMETRIC CONDUCTION PATHWAYS** — each carries
**its own** descending axons, and the two are **not coupled**.
Consumers must **not** conflate the two, and must **not** assume a
right lesion and a left lesion produce mirror-image deficits —
**a right peduncular lesion produces RIGHT CN III palsy + LEFT
hemiplegia**, and a **left** peduncular lesion produces **LEFT
CN III palsy + RIGHT hemiplegia**. The **CN III palsy is
IPSILATERAL**; the **hemiplegia is CONTRALATERAL**.

Function in the Human Brain
---------------------------
The right cerebral peduncle's function is **descending motor and
corticopontine conduction on the right side** — **NOT** rhythm
generation, **NOT** motor programming, **NOT** sensory processing:

*   **Right Corticospinal Conduction (left voluntary motor):** The
    right peduncle **carries** the **right corticospinal** axons from
    the **right cortex** to the **left spinal cord** — the
    **voluntary motor** pathway for the **left limbs and left
    trunk**.

*   **Right Corticobulbar Conduction (predominantly bilateral
    cranial motor):** The right peduncle **carries** the **right
    corticobulbar** axons from the **right cortex** to the
    **bilateral cranial nerve motor nuclei** — predominantly
    **bilateral** innervation, with **contralateral dominance** for
    the **lower facial** and **genioglossus** targets.

*   **Right Corticopontine Conduction (contralateral cerebellar
    input):** The right peduncle **carries** the **right
    corticopontine** axons from the **right cortex** to the
    **bilateral pontine nuclei** (predominantly **left**
    pontine nuclei), providing the **left** cerebellar hemisphere
    with **right cortical input**.

*   **NOT a processor.** The right peduncle **carries** axons; it
    does **not** process them. It has **no neurons of its own**.

*   **NOT an oscillator.** The **oscillators** are the
    **pre-Bötzinger complex**, the **Bötzinger complex**, and the
    **pFRG** — **brainstem respiratory oscillators**. The right
    peduncle is a **conduction pathway** — it does **not** generate
    a rhythm.

*   **NOT the basal ganglia.** The right basal ganglia are the
    **telencephalic** motor-modulation system. The right peduncle is
    the **descending conduit** — it does **not** modulate; it
    **carries**.

**The unifying theme:** the right cerebral peduncle is the **right
midbrain segment of the descending corticofugal pathway** — a
**white-matter conduit** carrying the **right corticospinal**,
**right corticobulbar**, and **right corticopontine** axons. It is a
**conduction pathway**, **NOT** a processor (**right tegmentum**),
**NOT** a grey-matter nucleus (**right substantia nigra**), **NOT**
the whole pyramidal tract, and **NOT** the internal capsule / basis
pontis / medullary pyramid.

Associated Disorders
--------------------
The right cerebral peduncle has a **direct clinical association**
with **right-sided Weber syndrome** — its clinical relevance is
**direct**, via the **right crus cerebri** and the **right CN III
fascicles** that traverse it:

*   **Right Weber Syndrome (alternating oculomotor hemiplegia —
    RIGHT, DIRECT, via the right cerebral peduncle):** A **right
    ventral midbrain** lesion (**infarction** — most commonly
    **paramedian midbrain** from **basilar artery** perforators;
    **hemorrhage**; **tumor**; **tentorial herniation**) involving
    the **right cerebral peduncle** and the **right CN III
    fascicles** produces:
    *   **Ipsilateral (RIGHT) CN III palsy** — **right ptosis**,
        **right mydriasis**, **right "down and out" eye** — from
        the **right CN III fascicle** involvement.
    *   **Contralateral (LEFT) spastic hemiplegia** — from the
        **right corticospinal** fiber involvement in the **right
        crus cerebri**.
    **Weber syndrome lateralizes** — a **right** peduncular lesion
    produces **right CN III palsy + left hemiplegia**, and a
    **left** peduncular lesion produces **left CN III palsy +
    right hemiplegia**. **Right Weber syndrome is the named
    disorder of the right cerebral peduncle** — **direct**, not
    indirect.

*   **Wallerian Degeneration of the Right Cerebral Peduncle
    (DESCRIPTIVE):** Large **right cortical** or **right internal
    capsule** strokes produce **Wallerian degeneration** of the
    **ipsilateral (right) cerebral peduncle** — visible on **MRI**
    as **T2 hyperintensity** and **atrophy** of the **right crus
    cerebri**. This is **descriptive**, not a named syndrome — the
    **primary lesion** is **upstream**.

*   **Progressive Supranuclear Palsy (PSP — NOT the peduncle):** The
    "**hummingbird sign**" of PSP is a **midbrain tegmentum**
    measure — **not** a cerebral peduncle measure. **PSP belongs to
    the tegmentum**, not to this module.

*   **ALS (INDIRECT — via the right corticospinal tract, not the
    peduncle as a named site):** **ALS** affects the **right
    corticospinal tract** — including the fibers that pass through
    the **right cerebral peduncle** — but the **right cerebral
    peduncle is not a named site** of ALS pathology. This is
    **indirect**.

*   **No Named "Right Cerebral Peduncle Syndrome" (apart from right
    Weber):** The right cerebral peduncle is a **white-matter
    conduit** — its only named syndrome is **right Weber syndrome**
    (alternating oculomotor hemiplegia with right CN III palsy).
    Its clinical relevance is **direct**, via the **right crus
    cerebri** and the **right CN III fascicles**.

**What is NOT here:** The right cerebral peduncle is **not** the
substrate for **Benedikt syndrome** (right tegmentum — red nucleus +
right CN III), **Claude syndrome** (right tegmentum — red nucleus +
right CN III), **Parinaud syndrome** (dorsal midbrain — superior
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
This is the **right** cerebral_peduncle leaf. The right and left
cerebral peduncles are **bilaterally symmetric** and carry **NO
coupling warning of their own** — and they **inherit no warning
from any oscillator**:

*   **Bilateral Conduction Pathways:** Each hemisphere has its own
    cerebral peduncle — each is a **white-matter conduit** carrying
    **its own** (predominantly **ipsilateral** above the pyramidal
    decussation) descending axons.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **right cerebral peduncle** is a **conduction
    pathway** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. Its **right**
    and **left** sides are **independent conduits** — there is
    **no** peduncle–peduncle coupling. **This extends the
    propagatable rule:** **coupling warnings attach to oscillators —
    not to premotor pools, not to sensor nuclei, and not to
    conduction pathways.**

*   **NO SLEA Warning:** The right cerebral peduncle is **SLEA-free**
    — it is **not** an extended-amygdala component.

*   **NO Amygdala-Lateralization Warning:** The right cerebral
    peduncle is **not** part of the amygdala — it does **not**
    inherit the amygdala-lateralization warning.

*   **NO Rhinencephalon-Exclusion Flag:** The right cerebral
    peduncle is **not** a rhinencephalon structure — it carries
    **no** rhinencephalon-exclusion flag.

**A consumer that assumes "right cerebral_peduncle = left
cerebral_peduncle" will be structurally correct** — the two sides
are **symmetric** and **functionally independent as conduits**. The
right cerebral_peduncle is a **strict-mirror pair with NO warning**
— **no coupling warning**, **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-
exclusion flag**. Consumers must **not** assume the two sides
produce **mirror-image** deficits — **right** peduncular lesions
produce **right** CN III palsy + **left** hemiplegia, and **left**
peduncular lesions produce **left** CN III palsy + **right**
hemiplegia.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only — **no**
    import from ``.../left/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/tegmentum/``, ``.../midbrain/tectum/``, the
    **internal capsule**, the **basis pontis**, the **medullary
    pyramid**, the **pyramidal decussation**, the **basal ganglia**,
    or any other container. The right cerebral peduncle's
    relationships to the right tegmentum, the right substantia
    nigra, the right internal capsule, the right basis pontis, the
    right medullary pyramid, the pyramidal decussation, the right
    basal ganglia, and the right CN III fascicles are documented as
    **prose and boundary data**, not as structural parents or
    children.
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
*   **NARROW DEFINITION — the leaf is the RIGHT CRUS CEREBRI, NOT
    the whole right ventral midbrain.** The **right tegmentum** and
    **right substantia nigra** are **separate siblings** — they are
    **not** part of this module.
*   **WHITE-MATTER CONDUCTION PATHWAY — NOT a grey-matter nucleus,
    NOT an oscillator, NOT a premotor pool, NOT a sensor nucleus.**
    It carries descending axons — it does **not** process them.
*   **NOT the right tegmentum — the right tegmentum is a SIBLING.**
*   **NOT the right substantia nigra — the right substantia nigra
    is a TEGMENTUM structure.**
*   **NOT the right internal capsule or corona radiata — those are
    FOREBRAIN structures.**
*   **NOT the right basis pontis — that is a HINDBRAIN structure.**
*   **NOT the right medullary pyramid — that is a HINDBRAIN
    structure.**
*   **NOT the right pyramidal decussation — that is a CAUDAL
    MYELENCEPHALIC structure** — and it is **the reason** a right
    peduncular lesion produces **left** hemiplegia.
*   **NOT the right CN III nucleus or the right CN III nerve — the
    CN III FASCICLES traverse the peduncle but do not define it.**
    The CN III fascicles are **what make Weber syndrome
    alternating**.
*   **NO coupling warning — the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS.** The right cerebral
    peduncle is a **strict mirror with NO warning**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The right cerebral peduncle is a
    local leaf under the cerebral_peduncle container, not a
    cross-listed leaf.
*   **No nested cross-listing.** The right cerebral peduncle has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with the left cerebral peduncle — strict
    mirror with NO warning.** Right and left cerebral peduncle
    modules are **structurally identical** — same leaf status, same
    **crus cerebri** framing, same **conduction-pathway** framing,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.midbrain.cerebral_peduncle.right import crus_cerebri

Or by fully-qualified path string::

    path = "midbrain.cerebral_peduncle.right"

**Do not** assume the right cerebral peduncle is the **whole right
ventral midbrain** (the broad classical definition). It is the
**right crus cerebri** — **narrow definition** — because the **right
tegmentum** and **right substantia nigra** are **separate siblings**.

**Do not** assume the right cerebral peduncle is the **right
tegmentum** or the **right substantia nigra**. Those are **separate
structures** — the **right tegmentum** is the grey-matter +
intrinsic midbrain; the **right substantia nigra** is a **tegmentum
child**.

**Do not** assume the right cerebral peduncle is the **right internal
capsule** (telencephalic) or the **right basis pontis** (pontine) or
the **right medullary pyramid** (medullary). Those are **segments**
of the same descending pathway at **different rostrocaudal levels**.

**Do not** assume the right cerebral peduncle is the **right
pyramidal tract as a whole**. It is **one segment** — the **right
midbrain segment**.

**Do not** assume the right cerebral peduncle is the **right CN III
nucleus** or the **right CN III nerve**. The **right CN III
fascicles traverse** the peduncle medially, but they are **not**
the peduncle.

**Do not** assume a **right** peduncular lesion produces **right**
hemiplegia. The **right corticospinal** fibers **decussate in the
medulla** — a **right** peduncular lesion produces **left**
hemiplegia (and **right** CN III palsy — the "alternating" pattern).

**Do not** assume the right cerebral peduncle contains structural
**fiber-population children**. The **right corticospinal**,
**right corticobulbar**, and **right corticopontine** fibers are
**prose**, not modules. There is **no**
``cerebral_peduncle.right.corticospinal``.

**Do not** import the **oscillator coupling warning** into the
right cerebral peduncle. **It is a CONDUCTION PATHWAY** — it
carries **NO coupling warning**.

Iterating the right cerebral peduncle's (empty) children (recommended
consumer pattern)::

    CEREBRAL_PEDUNCLE_RIGHT_CHILDREN = ()
    # The right cerebral peduncle is a leaf. The right corticospinal,
    # right corticobulbar, and right corticopontine fiber populations
    # are prose, not modules.

Reaching the cerebral_peduncle container (recommended consumer
pattern — the CONTAINER, not a sibling)::

    # The cerebral_peduncle container holds the left and right
    # peduncles:
    #
    #   brainparts.midbrain.cerebral_peduncle
    #
    # The right peduncle is ONE OF TWO children of the container.

Reaching the left cerebral peduncle (recommended consumer pattern —
the SIDE sibling)::

    # The left cerebral peduncle is the LEFT CRUS CEREBRI:
    #
    #   brainparts.midbrain.cerebral_peduncle.left
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
    # The right cerebral peduncle is the WHITE-MATTER conduit; the
    # right tegmentum is the GREY-MATTER processor.

Reaching the right substantia nigra (recommended consumer pattern —
the tegmentum child, NOT a peduncle child)::

    # The right substantia nigra is a RIGHT TEGMENTUM child — the
    # dopaminergic nucleus DORSAL to the right crus cerebri:
    #
    #   brainparts.midbrain.tegmentum.right.substantia_nigra
    #
    # The right cerebral peduncle is the WHITE-MATTER bundle
    # VENTRAL to the right substantia nigra. The narrow definition
    # excludes the right substantia nigra from the peduncle.

Reaching the right internal capsule (recommended consumer pattern —
the TELENCEPHALIC segment)::

    # The right internal capsule is the RIGHT TELENCEPHALIC segment
    # of the descending pathway — the same right corticospinal /
    # corticobulbar / corticopontine axons at a more rostral level:
    #
    #   brainparts.forebrain.telencephalon...internal_capsule.right
    #
    # The right cerebral peduncle is the RIGHT MESENCEPHALIC segment.

Reaching the right basis pontis (recommended consumer pattern — the
RHOMBENCEPHALIC segment)::

    # The right basis pontis is the RIGHT PONTINE segment of the
    # descending pathway:
    #
    #   brainparts.hindbrain.metencephalon.pons...basis_pontis.right
    #
    # The right cerebral peduncle is the RIGHT MESENCEPHALIC segment.

Reaching the right medullary pyramid (recommended consumer pattern —
the MYELENCEPHALIC segment)::

    # The right medullary pyramid is the RIGHT MEDULLARY segment of
    # the descending pathway:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata...
    #   pyramid.right
    #
    # The right cerebral peduncle is the RIGHT MESENCEPHALIC segment.

Reaching the pyramidal decussation (recommended consumer pattern —
NOTE the decussation is CAUDAL to the peduncle)::

    # The pyramidal decussation is the CAUDAL MEDULLARY crossing
    # at which the RIGHT corticospinal fibers cross to the LEFT
    # spinal cord:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata...
    #   pyramidal_decussation
    #
    # The decussation is CAUDAL to the peduncle — this is the
    # REASON a RIGHT peduncular lesion produces LEFT hemiplegia.

Fiber-population-level detail (not wired — consult references)::

    # The right cerebral peduncle's fiber populations are prose,
    # not modules:
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
    # cerebral peduncle.

Bilateral iteration (recommended consumer pattern — NOTE the
conduction-pathway rule and the lateralization of Weber
syndrome)::

    for side in ("left", "right"):
        peduncle_path = (
            f"midbrain.cerebral_peduncle.{side}"
        )
        # resolve peduncle_path through the memory/recall layer
        #
        # NOTE: the two sides are CONDUCTION PATHWAYS — each
        # carries its own descending axons. There is NO coupling
        # warning here. The coupling warning attaches to the
        # OSCILLATORS (pre-Bötzinger complex, Bötzinger complex),
        # not to conduction pathways.
        #
        # NOTE: Weber syndrome lateralizes — a RIGHT peduncular
        # lesion produces RIGHT CN III palsy + LEFT hemiplegia,
        # and a LEFT peduncular lesion produces LEFT CN III
        # palsy + RIGHT hemiplegia. The CN III palsy is
        # IPSILATERAL; the hemiplegia is CONTRALATERAL.

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
    corticospinal and corticobulbar organization in the cerebral
    peduncle; the decussation at the medulla.)
*   **Corticopontine and corticopontocerebellar pathway:** Glickstein,
    M., May, J.G., Mercier, B.E. (1985). "Corticopontine projection
    in the macaque: the distribution of labelled cortical cells
    after multiple tracer injections." *Journal of Comparative
    Neurology* 235:343–359. (Corticopontine fibers in the cerebral
    peduncle and their projection to the pontine nuclei —
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
    syndrome of the cerebral peduncle.)
*   **Weber syndrome — modern review:** Bogousslavsky, J., Caplan,
    L.R. (2001). *Stroke Syndromes*, 2nd ed. (Weber syndrome and
    other ventral midbrain stroke syndromes — the clinical
    localization to the cerebral peduncle and CN III fascicles;
    the lateralization of the syndrome — ipsilateral CN III palsy,
    contralateral hemiplegia.)
*   **Benedikt syndrome (contrast — tegmentum, NOT peduncle):**
    Benedikt, M. (1889). "Krankenvorstellung." *Wiener Medicinische
    Presse* 30:1–4. (Benedikt syndrome — red nucleus + CN III —
    tegmentum, NOT the cerebral peduncle.)
*   **Claude syndrome (contrast — tegmentum, NOT peduncle):** Claude,
    H., Loyez, M. (1912). "Ramollissement du noyau rouge."
    *Revue Neurologique* 23:49–51. (Claude syndrome — red nucleus +
    CN III — tegmentum, NOT the cerebral peduncle.)
*   **Parinaud syndrome (contrast — dorsal midbrain, NOT
    peduncle):** Parinaud, H. (1883). "Paralysie des mouvements
    associés des yeux." *Annales d'Oculistique* 90:1–21. (Parinaud
    syndrome — superior colliculus / tectum — NOT the cerebral
    peduncle.)
*   **Progressive supranuclear palsy (contrast — midbrain
    tegmentum, NOT peduncle):** Steele, J.C., Richardson, J.C.,
    Olszewski, J. (1964). "Progressive supranuclear palsy."
    *Archives of Neurology* 10:333–359. (The "hummingbird sign" is
    a midbrain tegmentum measure — the cerebral peduncle is NOT the
    primary PSP substrate.)
*   **ALS (contrast — motor cortex and anterior horn, NOT the
    peduncle as a named site):** Rowland, L.P., Shneider, N.A.
    (2001). "Amyotrophic lateral sclerosis." *New England Journal
    of Medicine* 344:1688–1700. (ALS affects the corticospinal
    tract — including peduncle fibers — but the peduncle is NOT a
    named site of ALS pathology.)
*   **Internal capsule (contrast — telencephalic segment):** Emos,
    M.C., Agarwal, S. (2024). *Neuroanatomy, Internal Capsule*.
    StatPearls. (The internal capsule as the telencephalic segment
    of the descending motor pathway — contrast with the midbrain
    peduncle.)
*   **Basis pontis (contrast — rhombencephalic segment):** Brodal,
    P. (1972). "The corticopontine projection in the cat."
    *Journal of Comparative Neurology* 146:177–215. (The basis
    pontis and the pontine nuclei — the pontine segment of the
    descending pathway, contrast with the midbrain peduncle.)
*   **Medullary pyramids and pyramidal decussation (contrast —
    myelencephalic segments):** Lassek, A.M. (1942). "The human
    pyramidal tract. IV. A study of the mature, the old, and the
    newborn." *Journal of Nervous and Mental Disease* 95:271–280.
    (The medullary pyramids and the pyramidal decussation — the
    medullary segment of the descending pathway, contrast with the
    midbrain peduncle.)
*   **Basal ganglia (contrast — telencephalic grey matter):** Parent,
    A., Hazrati, L.N. (1995). "Functional anatomy of the basal
    ganglia. I. The cortico-basal ganglia-thalamo-cortical loop."
    *Brain Research Reviews* 20:91–127. (The basal ganglia as a
    parallel motor-modulation system — NOT on the descending pathway
    carried by the peduncle.)
*   **Dopaminergic phenotype (chemicals_hormones-layer fact —
    contrast):** Björklund, A., Dunnett, S.B. (2007). "Dopamine
    neuron systems in the brain: an update." *Trends in
    Neurosciences* 30:194–202. (The dopaminergic phenotype of the
    substantia nigra as a chemicals-layer fact — documented in the
    tegmentum leaf, never imported here.)
*   **SLEA (contrast — the right cerebral peduncle is not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the cerebral peduncle.)
*   NeuroNames — Cerebral peduncle (right); FMA — Cerebral peduncle
    (right crus cerebri).
"""