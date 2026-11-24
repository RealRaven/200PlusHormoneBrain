"""
infrastructure.brainparts.midbrain.cerebral_peduncle
====================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── tectum
    ├── tegmentum
    ├── cerebral_aqueduct
    └── cerebral_peduncle          <-- THIS MODULE (paired container)
        ├── left
        │   └── (crus cerebri)     <-- leaf
        └── right
            └── (crus cerebri)     <-- leaf

**Primary synonym:** Cerebral peduncle; **crus cerebri** (the
narrow-definition term — the structure this module is wired to be);
basis pedunculi (when the substantia nigra is included — **not** here).
**Cytoarchitectonic designation:** **Not a Brodmann area** and **not
a grey-matter nucleus** — the cerebral peduncle is a **white-matter
fiber bundle** (a **conduction pathway**). It carries **descending
corticofugal axons**, not cell bodies. It has **no neurons of its own**.
**Part of:** The **midbrain** (mesencephalon) container — specifically,
the **ventral** surface of the midbrain, **ventral to the substantia
nigra** and the **tegmentum**.
**Structural parent:** ``.../midbrain/`` → **direct child** of the
midbrain container.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left cerebral peduncle** (left crus cerebri);
    a **leaf**.
*   ``right/`` — the **right cerebral peduncle** (right crus cerebri);
    a **leaf**.
**Boundary status (NARROW DEFINITION — the peduncle is the CRUS
CEREBRI, NOT the whole ventral midbrain):** **Boundary case — the
cerebral_peduncle is the CRUS CEREBRI (narrow definition), NOT the
whole ventral midbrain (broad definition).** Classical neuroanatomy
uses "cerebral peduncle" **broadly** to mean the whole midbrain
ventral to the tectum — the **crus cerebri + substantia nigra +
tegmentum**. Modern clinical anatomy (and this tree) uses
"cerebral peduncle" **narrowly** to mean **the crus cerebri** — the
ventral descending fiber bundle. **The tree wires the tegmentum and
the substantia nigra as separate siblings**, so this module takes
the **narrow definition**. Consumers must **not** assume the
cerebral_peduncle includes the tegmentum or the substantia nigra —
it does **not**.
**Boundary status (NOT the tegmentum — the tegmentum is a SIBLING
under the midbrain):** **Boundary case — the cerebral_peduncle is NOT
the tegmentum.** The **tegmentum** (``.../midbrain/tegmentum/``) is
the **ventral midbrain** in the **modern** sense — it contains the
**substantia nigra**, the **ventral tegmental area**, the **red
nucleus**, the **periaqueductal gray**, the **oculomotor nucleus**
(CN III), the **trochlear nucleus** (CN IV), the **Edinger-Westphal
nucleus**, the **mesencephalic trigeminal nucleus** (CN V), and the
**midbrain reticular formation**. The **cerebral_peduncle** (here) is
the **crus cerebri** — the **descending fiber bundle** on the
**ventral surface**. **They are DIFFERENT STRUCTURES** — the
**tegmentum** is the **grey-matter + intrinsic** midbrain; the
**cerebral_peduncle** is the **white-matter conduit**. Consumers
must **not** conflate the two, and must **not** resolve a
tegmentum structure (substantia nigra, red nucleus, PAG, CN III/IV
nuclei) through the cerebral_peduncle path.
**Boundary status (NOT the substantia nigra — the substantia nigra
is a TEGMENTUM structure):** **Boundary case — the cerebral_peduncle
is NOT the substantia nigra.** The **substantia nigra**
(``.../midbrain/tegmentum/substantia_nigra/``) is the
**dopaminergic** nucleus **dorsal to the crus cerebri** and
**ventral to the tegmentum proper** — it is a **grey-matter
nucleus**, and it is a **tegmentum child**. The **cerebral_peduncle**
(here) is the **white-matter bundle ventral to the substantia
nigra**. **They are DIFFERENT STRUCTURES** — the **substantia
nigra** is **grey matter**; the **cerebral_peduncle** is **white
matter**. The **substantia nigra** is **excluded** from the
**broad** "basis pedunculi" — and this module takes the **narrow**
definition, which **also** excludes it. Consumers must **not**
conflate the two, and must **not** resolve the substantia nigra
through the cerebral_peduncle path.
**Boundary status (NOT the internal capsule or corona radiata — those
are FOREBRAIN structures):** **Boundary case — the
cerebral_peduncle is NOT the internal capsule, and NOT the corona
radiata.** The **internal capsule**
(``.../forebrain/telencephalon/.../internal_capsule/``) and the
**corona radiata** are **telencephalic** white-matter structures —
they carry the **same descending axons** (corticospinal,
corticobulbar, corticopontine) **before** they enter the midbrain.
The **cerebral_peduncle** (here) is the **midbrain segment** of that
descending pathway. **They are DIFFERENT STRUCTURES across a lobe
boundary** — the **internal capsule** is **telencephalic**; the
**cerebral peduncle** is **mesencephalic**. Consumers must **not**
conflate the two, and must **not** resolve the internal capsule
through the midbrain path.
**Boundary status (NOT the pyramidal tract as a whole — the peduncle
is ONE SEGMENT of the pyramidal tract):** **Boundary case — the
cerebral_peduncle is NOT the pyramidal tract.** The **pyramidal
tract** (corticospinal tract) is the **whole pathway** from the
**cerebral cortex** to the **spinal cord** — it includes the
**corona radiata**, the **internal capsule**, the **cerebral
peduncle**, the **basis pontis**, the **medullary pyramids**, and the
**pyramidal decussation** (and the **corticospinal tracts** in the
spinal cord). The **cerebral_peduncle** (here) is **one segment** of
that pathway — the **midbrain segment**. Consumers must **not**
conflate the peduncle with the whole pyramidal tract, and must
**not** resolve pontine or medullary structures through the
cerebral_peduncle path.
**Boundary status (NOT the pons or the basis pontis — those are
HINDBRAIN structures):** **Boundary case — the cerebral_peduncle is
NOT the pons, and NOT the basis pontis.** The **pons**
(``.../hindbrain/metencephalon/pons/``) and the **basis pontis**
(the ventral pontine fiber bundle) are **rhombencephalic** —
**caudal to the midbrain**, across the **pontomesencephalic
junction**. The **cerebral_peduncle** (here) is **mesencephalic**.
**They are DIFFERENT STRUCTURES across a lobe boundary.** Consumers
must **not** conflate the peduncle with the basis pontis, and must
**not** resolve pontine structures through the midbrain path.
**Boundary status (NOT the medullary pyramids or the pyramidal
decussation — those are HINDBRAIN structures):** **Boundary case —
the cerebral_peduncle is NOT the medullary pyramids, and NOT the
pyramidal decussation.** The **medullary pyramids**
(``.../hindbrain/myelencephalon/medulla_oblongata/.../pyramid/``)
and the **pyramidal decussation** (the caudal medullary crossing)
are **rhombencephalic** — **caudal to the pons**. The
**cerebral_peduncle** (here) is **mesencephalic**. **They are
DIFFERENT STRUCTURES.** Consumers must **not** conflate the
peduncle with the medullary pyramids.
**Boundary status (NOT the fiber populations as structural children —
the corticospinal, corticobulbar, and corticopontine fibers are
PROSE):** **Boundary case — the cerebral_peduncle is a SINGLE fiber
bundle, NOT a container of three structural children.** The
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations are **fiber types within the peduncle**, not
**sub-modules**. The tree wires the **left** and **right** peduncles
as the only structural children (the **paired** structure); the
**fiber populations** are documented as **prose** in the leaf
modules. Consumers must **not** resolve
``cerebral_peduncle.left.corticospinal`` — no such path exists.
**Boundary status (WHITE MATTER — NOT a grey-matter nucleus, NOT an
oscillator, NOT a premotor pool, NOT a sensor nucleus):** **Boundary
case — the cerebral_peduncle is a WHITE-MATTER CONDUCTION
PATHWAY.** It is **not** an oscillator (no intrinsic rhythm), **not**
a premotor pool (no cell bodies, no pattern shaping), **not** a
sensor nucleus (no transduction), and **not** a motoneuron pool (no
motor neurons). It is a **conduit** — it **carries** descending
axons **generated** in the cortex. **Structure-class taxonomy:** in
the VRG modules, the rule is **coupling warnings attach to
oscillators — not to premotor pools, not to sensor nuclei**. The
**cerebral_peduncle** is a **conduction pathway** — a **fourth
class** — and it carries **NO coupling warning**, **NO SLEA
warning**, **NO amygdala-lateralization warning**, and **NO
rhinencephalon-exclusion flag**. It is a **strict mirror with NO
warning**.
**Boundary status (PAIRED STRUCTURE — a container for left/right, NOT
a single midline leaf):** **Boundary case — the cerebral_peduncle is
a PAIRED structure, wired as a CONTAINER.** The **left** and
**right** peduncles are **structural children** of this container.
Consumers must **not** resolve the peduncle as a single midline
leaf — the left and right sides are the **leaves**.
**Boundary status (NOT the midbrain as a whole — a SUB-REGION of the
midbrain):** **Boundary case — the cerebral_peduncle is a LEAF-level
container under the midbrain, not the midbrain itself.** The
**midbrain** (``.../midbrain/``) contains the **tectum**, the
**tegmentum**, the **cerebral_aqueduct**, and the
**cerebral_peduncle**. Consumers must **not** conflate the peduncle
with the midbrain, and must **not** resolve tectum or tegmentum
structures through the cerebral_peduncle path.

Overview
--------
The cerebral peduncle is the **ventral-most descending white-matter
bundle** of the **midbrain** — the **midbrain segment** of the
**corticofugal** (cortex-descending) pathways. In the **narrow
definition** used by this tree, it is the **crus cerebri**: the
**corticospinal**, **corticobulbar**, and **corticopontine** fiber
populations on each side of the ventral midbrain surface. It is a
**paired container** — its structural children are the **left** and
**right** peduncles, each a **leaf** representing one side's crus
cerebri.

**The cerebral_peduncle is the CRUS CEREBRI, NOT the whole ventral
midbrain.** The **broad** classical definition (crus cerebri +
substantia nigra + tegmentum) is **rejected** here because the
**tegmentum** and **substantia nigra** are **separate siblings**
under the midbrain. The **narrow** definition is the **only** one
consistent with the tree.

**The cerebral_peduncle is a WHITE-MATTER CONDUCTION PATHWAY, NOT a
grey-matter nucleus.** It has **no neurons of its own** — it
**carries** descending axons **generated** in the cortex. It is a
**conduit**, not a processor.

**The cerebral_peduncle is a PAIRED STRUCTURE.** The **left** and
**right** peduncles are its **structural children** (leaves). The two
sides are **bilaterally symmetric** and **functionally independent
conduits** — each carries its own side's descending axons. They
carry **NO coupling warning** (they are **conduction pathways**, not
oscillators). See *Lateralization Notes*.

Narrow vs. Broad Definition (the module's central structural call)
------------------------------------------------------------------
**Narrow (this module):** The cerebral peduncle = **the crus cerebri**
— the ventral descending fiber bundle, **ventral to the substantia
nigra**. This is the **modern clinical** definition — the one used in
**Weber syndrome** ("lesion of the cerebral peduncle") and in
**modern neuroimaging** (the "cerebral peduncle" sign in
**progressive supranuclear palsy** is a **crus cerebri** measure, not
a whole-ventral-midbrain measure).

**Broad (NOT this module):** The cerebral peduncle = **everything
ventral to the tectum** — crus cerebri + substantia nigra +
tegmentum. This is the **classical** definition. It is **rejected**
here because the tree wires the **tegmentum** and **substantia
nigra** as **separate siblings**.

**Consumers must use the NARROW definition.** A consumer that
resolves `cerebral_peduncle` and expects to find the **red nucleus**
or the **substantia nigra** will be **wrong** — those are **tegmentum**
children.

Fiber Populations (prose, not structural children)
--------------------------------------------------
The cerebral peduncle carries **three descending fiber populations** —
documented as **prose**, not as structural children:

*   **Corticospinal fibers** — **motor** axons from the **primary
    motor cortex** (and premotor areas) to the **spinal cord**
    (**lateral** and **anterior corticospinal tracts**). Somatotopy
    within the crus: **arm** medial, **leg** lateral.

*   **Corticobulbar fibers** — **motor** axons from the **motor
    cortex** to the **cranial nerve motor nuclei** (CN V, VII, IX, X,
    XI, XII). Somatotopy: **most medial** of the three populations.

*   **Corticopontine fibers** — axons from the **cortex** to the
    **pontine nuclei** (the **corticopontocerebellar** pathway).
    Somatotopy: **most lateral** of the three populations.

**These fiber populations are prose, not structural children.** The
tree wires the **left** and **right** peduncles as the **only**
structural children. Consumers must **not** resolve
``cerebral_peduncle.left.corticospinal`` — no such path exists.

Somatotopy (prose — medial to lateral)
--------------------------------------
Within each crus cerebri, the descending fibers are **somatotopically
organized**, **medial to lateral**:

1.  **Corticobulbar** fibers — **most medial** (face, head, neck).
2.  **Corticospinal arm** fibers — **middle-medial**.
3.  **Corticospinal leg** fibers — **middle-lateral**.
4.  **Corticopontine** fibers — **most lateral**.

**This somatotopy is clinically relevant** — a **medial** crus lesion
affects the **face/arm** more than the **leg**; a **lateral** crus
lesion affects the **leg** more than the **face/arm**. The classic
teaching is **"face medial, leg lateral"** — a useful shorthand, but
the **corticopontine** fibers are **also** lateral, so the full
pattern is **corticobulbar → arm → leg → corticopontine**.

The Cerebral Peduncle / Tegmentum Boundary
------------------------------------------
This is the **most consequential sibling** boundary — **narrow vs.
broad** definition:

*   **Cerebral_peduncle** (this module) — the **crus cerebri** —
    **white matter**, **ventral surface**.

*   **Tegmentum** (``.../midbrain/tegmentum/``) — the **grey-matter
    + intrinsic** midbrain — **dorsal to the substantia nigra**,
    containing the **red nucleus**, the **PAG**, the **CN III / IV
    nuclei**, the **VTA**, and the **midbrain reticular formation**.

**They are SIBLINGS under the midbrain.** The **narrow definition**
excludes the tegmentum from the peduncle. **Consumers must not
conflate the two** — the **peduncle** is the **conduit**; the
**tegmentum** is the **processor**.

The Cerebral Peduncle / Substantia Nigra Boundary
-------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Cerebral_peduncle** (this module) — the **crus cerebri** —
    **white matter**.

*   **Substantia nigra**
    (``.../midbrain/tegmentum/substantia_nigra/``) — the
    **dopaminergic** nucleus — **grey matter**.

**The substantia nigra is DORSAL to the crus cerebri and VENTRAL to
the tegmentum proper.** It is a **tegmentum child**, **not** a
peduncle child. The **broad** "basis pedunculi" includes it — this
module's **narrow** definition **excludes** it. Consumers must
**not** conflate the two, and must **not** resolve the substantia
nigra through the cerebral_peduncle path.

The Cerebral Peduncle / Internal Capsule Boundary
-------------------------------------------------
This is the **mesencephalic / telencephalic** boundary:

*   **Cerebral_peduncle** (this module) — the **midbrain segment**
    of the descending pathway.

*   **Internal capsule**
    (``.../forebrain/telencephalon/.../internal_capsule/``) — the
    **telencephalic segment** of the same descending pathway.

**They carry the SAME axons** — but at **different rostrocaudal
levels**. **Consumers must not conflate the two** — the **internal
capsule** is **forebrain**; the **cerebral peduncle** is **midbrain**.

The Cerebral Peduncle / Basis Pontis Boundary
---------------------------------------------
This is the **mesencephalic / rhombencephalic** boundary:

*   **Cerebral_peduncle** (this module) — the **midbrain segment**.

*   **Basis pontis**
    (``.../hindbrain/metencephalon/pons/.../basis_pontis/``) — the
    **pontine segment**.

**They are across the pontomesencephalic junction.** Consumers must
**not** conflate the two — the **basis pontis** is **hindbrain**;
the **cerebral peduncle** is **midbrain**.

The Cerebral Peduncle / Medullary Pyramids Boundary
---------------------------------------------------
This is the **midbrain / medulla** boundary:

*   **Cerebral_peduncle** (this module) — the **midbrain segment**.

*   **Medullary pyramids**
    (``.../hindbrain/myencephalon/medulla_oblongata/.../pyramid/``)
    — the **medullary segment**.

**They are across the pontomedullary junction.** Consumers must
**not** conflate the two — the **medullary pyramids** are
**hindbrain**; the **cerebral peduncle** is **midbrain**.

The Cerebral Peduncle / Basal Ganglia Boundary
----------------------------------------------
This is the **white-matter / grey-matter** boundary within the
forebrain:

*   **Cerebral_peduncle** (this module) — the **midbrain descending
    fiber bundle**.

*   **Basal ganglia**
    (``.../forebrain/telencephalon/.../basal_ganglia/``) — the
    **telencephalic grey-matter nuclei** (striatum, globus pallidus,
    etc.).

**The basal ganglia are NOT on the descending pathway carried by
the peduncle** — they are a **parallel** motor system. Consumers
must **not** conflate the peduncle with the basal ganglia.

Function in the Human Brain
---------------------------
The cerebral peduncle's function is **descending motor and
corticopontine conduction** — **NOT** rhythm generation, **NOT**
motor programming, **NOT** sensory processing:

*   **Corticospinal Conduction (voluntary motor):** The peduncle
    **carries** the **corticospinal** axons from the cortex to the
    spinal cord — the **voluntary motor** pathway for the **limbs
    and trunk**. The peduncle is the **midbrain conduit** for this
    pathway.

*   **Corticobulbar Conduction (cranial motor):** The peduncle
    **carries** the **corticobulbar** axons from the cortex to the
    **cranial nerve motor nuclei** — the **voluntary motor**
    pathway for the **face, head, and neck**.

*   **Corticopontine Conduction (cerebellar input):** The peduncle
    **carries** the **corticopontine** axons from the cortex to the
    **pontine nuclei** — the **corticopontocerebellar** pathway
    that provides the cerebellum with **cortical input**.

*   **NOT a processor.** The peduncle **carries** axons; it does
    **not** process them. It has **no neurons of its own** — the
    axons are **generated** in the **cortex** and **terminate** in
    the **spinal cord**, the **cranial nerve nuclei**, or the
    **pontine nuclei**.

*   **NOT an oscillator.** The **oscillators** are the
    **pre-Bötzinger complex**, the **Bötzinger complex**, and the
    **pFRG** — **brainstem respiratory oscillators**. The peduncle is
    a **conduction pathway** — it does **not** generate a rhythm.

*   **NOT the basal ganglia.** The basal ganglia are the
    **telencephalic** motor-modulation system. The peduncle is the
    **descending conduit** — it does **not** modulate; it
    **carries**.

**The unifying theme:** the cerebral peduncle is the **midbrain
segment of the descending corticofugal pathway** — a **white-matter
conduit** carrying the **corticospinal**, **corticobulbar**, and
**corticopontine** axons. It is a **conduction pathway**, **NOT** a
processor (**tegmentum**), **NOT** a grey-matter nucleus
(**substantia nigra**), **NOT** the whole pyramidal tract, and
**NOT** the internal capsule / basis pontis / medullary pyramids.

Associated Disorders
--------------------
The cerebral peduncle has a **direct clinical association** with
**Weber syndrome** — its clinical relevance is **direct**, via the
**crus cerebri** and the **CN III fascicles** that traverse it:

*   **Weber Syndrome (alternating oculomotor hemiplegia — DIRECT,
    via the cerebral peduncle):** A **ventral midbrain** lesion
    (**infarction**, **hemorrhage**, **tumor**, **tentorial
    herniation**) involving the **cerebral peduncle** and the
    **CN III fascicles** produces:
    *   **Ipsilateral CN III palsy** — **ptosis**, **mydriasis**,
        **"down and out" eye** — from the **CN III fascicle**
        involvement.
    *   **Contralateral spastic hemiplegia** — from the
        **corticospinal** fiber involvement in the **crus cerebri**.
    **Weber syndrome is the named disorder of the cerebral
    peduncle** — **direct**, not indirect.

*   **Wallerian Degeneration of the Cerebral Peduncle (DESCRIPTIVE):**
    Large **cortical** or **internal capsule** strokes produce
    **Wallerian degeneration** of the **ipsilateral cerebral
    peduncle** — visible on **MRI** as **T2 hyperintensity** and
    **atrophy**. This is **descriptive**, not a named syndrome —
    the **primary lesion** is **upstream**.

*   **Progressive Supranuclear Palsy (PSP — NOT the peduncle):** The
    "**hummingbird sign**" of PSP is a **midbrain tegmentum**
    measure (the **superior profile** of the midbrain), **not** a
    cerebral peduncle measure. The **cerebral peduncle** is
    **not** the primary PSP substrate. **PSP belongs to the
    tegmentum**, not to this module.

*   **ALS (INDIRECT — via the corticospinal tract, not the peduncle
    as a named site):** **Amyotrophic lateral sclerosis** affects
    the **corticospinal tract** — including the fibers that pass
    through the cerebral peduncle — but the **cerebral peduncle is
    not a named site** of ALS pathology. The **primary** pathology
    is in the **motor cortex** and **anterior horn cells**. This is
    **indirect**.

*   **No Named "Cerebral Peduncle Syndrome" (apart from Weber):** The
    cerebral peduncle is a **white-matter conduit** — its only
    named syndrome is **Weber syndrome** (alternating oculomotor
    hemiplegia). Its clinical relevance is **direct**, via the
    **crus cerebri** and the **CN III fascicles**.

**What is NOT here:** The cerebral peduncle is **not** the substrate
for **Benedikt syndrome** (tegmentum — red nucleus + CN III),
**Claude syndrome** (tegmentum — red nucleus + CN III), **Parinaud
syndrome** (dorsal midbrain — superior colliculus / tectum),
**Nothnagel syndrome** (tectum / colliculi), **Millard-Gubler
syndrome** (pons), **Wallenberg syndrome** (lateral medulla),
**locked-in syndrome** (basis pontis), **CCHS** (RTN), **OIRD**
(pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger complex
+ arcuate nucleus), **essential hypertension / sympathetic
overactivity** (C1 group / RVLM), **Parkinson's disease**
(substantia nigra — tegmentum), **Huntington's disease**
(striatum — telencephalon), or **Kluver-Bucy syndrome** (amygdala).
Its clinical relevance is **direct**, via **Weber syndrome**.
**Weber syndrome is the named disorder.**

Lateralization Notes
--------------------
This is the **cerebral_peduncle** container — its structural children
are the **left** and **right** peduncles. The two sides are
**bilaterally symmetric** and carry **NO coupling warning of their
own** — and they **inherit no warning from any oscillator**:

*   **Bilateral Conduction Pathways:** Each hemisphere has its own
    cerebral peduncle — each is a **white-matter conduit** carrying
    **its own** (predominantly **ipsilateral** above the pyramidal
    decussation) descending axons.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **cerebral peduncle** is a **conduction
    pathway** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. Its **left**
    and **right** sides are **independent conduits** — there is
    **no** peduncle–peduncle coupling. **This extends the
    propagatable rule:** **coupling warnings attach to oscillators —
    not to premotor pools, not to sensor nuclei, and not to
    conduction pathways.**

*   **NO SLEA Warning:** The cerebral peduncle is **SLEA-free** — it
    is **not** an extended-amygdala component.

*   **NO Amygdala-Lateralization Warning:** The cerebral peduncle is
    **not** part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **NO Rhinencephalon-Exclusion Flag:** The cerebral peduncle is
    **not** a rhinencephalon structure — it carries **no**
    rhinencephalon-exclusion flag.

**A consumer that assumes "left cerebral_peduncle = right
cerebral_peduncle" will be structurally correct** — the two sides
are **symmetric** and **functionally independent as conduits**. The
cerebral_peduncle is a **strict-mirror pair with NO warning** —
**no coupling warning**, **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container does **not**
    import from the left or right leaves at module load — the
    container's `__init__.py` is **namespace only** (see Usage for
    the recommended re-export pattern).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/tegmentum/``, ``.../midbrain/tectum/``, the
    **internal capsule**, the **basis pontis**, the **medullary
    pyramids**, the **basal ganglia**, or any other container. The
    cerebral peduncle's relationships to the tegmentum, the
    substantia nigra, the internal capsule, the basis pontis, the
    medullary pyramids, and the basal ganglia are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **dopaminergic
    phenotype** of the substantia nigra is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the tegmentum leaf, **not** here.
*   **Container — the paired peduncle.** The left and right
    peduncles are the **structural children**. The **fiber
    populations** (corticospinal, corticobulbar, corticopontine) are
    **prose**, not structural children.
*   **NARROW DEFINITION — the peduncle is the CRUS CEREBRI, NOT the
    whole ventral midbrain.** The **tegmentum** and **substantia
    nigra** are **separate siblings** — they are **not** part of
    this module.
*   **WHITE-MATTER CONDUCTION PATHWAY — NOT a grey-matter nucleus,
    NOT an oscillator, NOT a premotor pool, NOT a sensor nucleus.**
    It carries descending axons — it does **not** process them.
*   **NOT the tegmentum — the tegmentum is a SIBLING.** The
    tegmentum is the grey-matter + intrinsic midbrain.
*   **NOT the substantia nigra — the substantia nigra is a TEGMENTUM
    structure.** It is grey matter, dorsal to the crus cerebri.
*   **NOT the internal capsule or corona radiata — those are
    FOREBRAIN structures.** They carry the **same axons** at a
    **more rostral** level.
*   **NOT the pyramidal tract as a whole — the peduncle is ONE
    SEGMENT of the pyramidal tract.**
*   **NOT the pons or basis pontis — those are HINDBRAIN
    structures.**
*   **NOT the medullary pyramids or the pyramidal decussation —
    those are HINDBRAIN structures.**
*   **NO coupling warning — the coupling warning attaches to
    OSCILLATORS, not to CONDUCTION PATHWAYS.** The cerebral
    peduncle is a **strict mirror with NO warning**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The cerebral_peduncle is a local
    container under the midbrain, not a cross-listed package.
*   **No nested cross-listing.** The cerebral_peduncle has no
    nested dual-framing module. It is a single paired container.
*   **Structural parity with the VRG family's conduction-pathway
    analog.** The **amygdala_cortex_pathways** (from the original
    template) is a **fiber-pathway** module — the
    **cerebral_peduncle** follows the same **conduction-pathway**
    contract: **white matter, prose fiber populations, no coupling
    warning**.

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts.midbrain import cerebral_peduncle

Resolve a leaf by path (the function belongs to the leaf)::

    from infrastructure.brainparts.midbrain.cerebral_peduncle.left import crus_cerebri

Or by fully-qualified path string (leaves, not the container)::

    left_path = "midbrain.cerebral_peduncle.left"
    right_path = "midbrain.cerebral_peduncle.right"

**Do not** assume the cerebral_peduncle is the **whole ventral
midbrain** (the broad classical definition). It is the **crus
cerebri** — **narrow definition** — because the **tegmentum** and
**substantia nigra** are **separate siblings**.

**Do not** assume the cerebral_peduncle is the **tegmentum** or the
**substantia nigra**. Those are **separate structures** — the
**tegmentum** is the grey-matter + intrinsic midbrain; the
**substantia nigra** is a **tegmentum child**.

**Do not** assume the cerebral_peduncle is the **internal capsule**
or the **corona radiata**. Those are **telencephalic** segments of
the **same descending pathway**.

**Do not** assume the cerebral_peduncle is the **basis pontis** or
the **medullary pyramids**. Those are **hindbrain** segments of the
same descending pathway.

**Do not** assume the cerebral_peduncle is the **pyramidal tract as
a whole**. It is **one segment** — the **midbrain segment**.

**Do not** assume the cerebral_peduncle contains structural
**fiber-population children**. The **corticospinal**,
**corticobulbar**, and **corticopontine** fibers are **prose**, not
modules. There is **no** ``cerebral_peduncle.left.corticospinal``.

**Do not** import the **oscillator coupling warning** into the
cerebral_peduncle. **It is a CONDUCTION PATHWAY** — it carries
**NO coupling warning**.

Iterating the cerebral_peduncle's children (recommended consumer
pattern)::

    CEREBRAL_PEDUNCLE_CHILDREN = ("left", "right")
    # The two sides are the structural children. The fiber
    # populations (corticospinal, corticobulbar, corticopontine)
    # are prose, not modules.

Reaching the tegmentum (recommended consumer pattern — the
grey-matter sibling)::

    # The tegmentum is the GREY-MATTER + INTRINSIC midbrain —
    # substantia nigra, VTA, red nucleus, PAG, CN III/IV nuclei,
    # Edinger-Westphal, mesencephalic trigeminal, midbrain
    # reticular formation:
    #
    #   brainparts.midbrain.tegmentum
    #
    # The cerebral peduncle is the WHITE-MATTER conduit; the
    # tegmentum is the GREY-MATTER processor. They are SIBLINGS
    # under the midbrain.

Reaching the substantia nigra (recommended consumer pattern — the
tegmentum child, NOT a peduncle child)::

    # The substantia nigra is a TEGMENTUM child — the dopaminergic
    # nucleus DORSAL to the crus cerebri:
    #
    #   brainparts.midbrain.tegmentum.substantia_nigra
    #
    # The cerebral peduncle is the WHITE-MATTER bundle VENTRAL to
    # the substantia nigra. The narrow definition excludes the
    # substantia nigra from the peduncle.

Reaching the internal capsule (recommended consumer pattern — the
TELENCEPHALIC segment)::

    # The internal capsule is the TELENCEPHALIC segment of the
    # descending pathway — it carries the same corticospinal /
    # corticobulbar / corticopontine axons at a more rostral level:
    #
    #   brainparts.forebrain.telencephalon...internal_capsule
    #
    # The cerebral peduncle is the MESENCEPHALIC segment. They are
    # DIFFERENT STRUCTURES across a lobe boundary.

Reaching the basis pontis (recommended consumer pattern — the
RHOMBENCEPHALIC segment)::

    # The basis pontis is the PONTINE segment of the descending
    # pathway — it carries the same axons at a more caudal level:
    #
    #   brainparts.hindbrain.metencephalon.pons...basis_pontis
    #
    # The cerebral peduncle is the MESENCEPHALIC segment. They are
    # DIFFERENT STRUCTURES across a lobe boundary.

Reaching the medullary pyramids (recommended consumer pattern — the
MYELENCEPHALIC segment)::

    # The medullary pyramids are the MEDULLARY segment of the
    # descending pathway:
    #
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata...pyramid
    #
    # The cerebral peduncle is the MESENCEPHALIC segment. They are
    # DIFFERENT STRUCTURES across a lobe boundary.

Bilateral iteration (recommended consumer pattern — NOTE the
conduction-pathway rule)::

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

Fiber-population detail (not wired — consult references)::

    # The cerebral peduncle's fiber populations are prose, not
    # modules:
    #   corticospinal  -> voluntary motor (limbs, trunk)
    #                     somatotopy: arm medial, leg lateral
    #   corticobulbar  -> voluntary motor (face, head, neck)
    #                     somatotopy: most medial
    #   corticopontine -> cerebellar input (corticopontocerebellar)
    #                     somatotopy: most lateral
    #
    # Do not attempt to resolve these as sub-paths of the
    # cerebral_peduncle.

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
    crus cerebri; the descending motor pathway.)
*   **Corticospinal tract organization:** Lemon, R.N. (2008).
    "Descending pathways in motor control." *Annual Review of
    Neuroscience* 31:195–218. (The descending motor pathways —
    corticospinal and corticobulbar organization in the cerebral
    peduncle.)
*   **Corticopontine and corticopontocerebellar pathway:** Glickstein,
    M., May, J.G., Mercier, B.E. (1985). "Corticopontine projection
    in the macaque: the distribution of labelled cortical cells
    after multiple tracer injections." *Journal of Comparative
    Neurology* 235:343–359. (Corticopontine fibers in the cerebral
    peduncle and their projection to the pontine nuclei.)
*   **Somatotopy in the crus cerebri:** Bertrand, G., Blundell, J.,
    Pelissier, P. (1973). "Somatotopic organization of the
    corticospinal tract in the human cerebral peduncle." *Surgical
    Neurology* 1:108–111. (The classical clinical somatotopy — face
    medial, leg lateral — within the human crus cerebri.)
*   **Weber syndrome (DIRECT disorder):** Weber, H.D. (1856).
    "A contribution to the pathology of the crura cerebri."
    *Medico-Chirurgical Transactions* 39:121–140. (The original
    description of alternating oculomotor hemiplegia — the named
    syndrome of the cerebral peduncle.)
*   **Weber syndrome — modern review:** Bogousslavsky, J., Caplan,
    L.R. (2001). *Stroke Syndromes*, 2nd ed. (Weber syndrome and
    other ventral midbrain stroke syndromes — the clinical
    localization to the cerebral peduncle and CN III fascicles.)
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
*   **Medullary pyramids (contrast — myelencephalic segment):**
    Lassek, A.M. (1942). "The human pyramidal tract. IV. A study of
    the mature, the old, and the newborn." *Journal of Nervous and
    Mental Disease* 95:271–280. (The medullary pyramids and the
    pyramidal decussation — the medullary segment of the descending
    pathway, contrast with the midbrain peduncle.)
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
*   **SLEA (contrast — the cerebral peduncle is not SLEA):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the cerebral peduncle.)
*   NeuroNames — Cerebral peduncle; FMA — Cerebral peduncle
    (crus cerebri).
"""