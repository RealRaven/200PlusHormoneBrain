"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain.lamina_terminalis
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_forebrain
                    └── lamina_terminalis   <-- THIS MODULE
                        └── vascular_organ_of_lamina_terminalis

**Primary synonym:** Lamina terminalis; terminal lamina; lamina
terminalis of the hypothalamus; anterior wall of the third ventricle.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A **thin
grey-matter membrane** — the **anterior wall of the third ventricle**.
**Part of:** The **basal forebrain** container — and, in classical
anatomy, the **anterior wall of the diencephalon** (see *Boundary
status*).
**Structural parent:** ``.../left/subcortical/basal_forebrain/`` →
**direct child** of the basal forebrain container.
**Structural children (one, closed set):**
``vascular_organ_of_lamina_terminalis`` (the **organum vasculosum of
the lamina terminalis**, OVLT — a **circumventricular organ**).
**Boundary status (container node):** **Boundary case — a container
with ONE child, but the container itself is also a structure.** The
lamina terminalis is both a **container** (it has the OVLT as a
child) and a **structure in its own right** (it is the thin grey-matter
membrane that forms the anterior wall of the third ventricle). Unlike
the basal forebrain container (which is a **pure structural
grouping** with no tissue identity of its own), the lamina terminalis
**is a membrane** and its one child sits **within** it. Consumers must
resolve both the **membrane** (this module) and the **OVLT** (its
child) — they are not the same structure.
**Boundary status (diencephalic-adjacent but telencephalic-wired):**
**Boundary case — the membrane is the anterior wall of the third
ventricle (diencephalic in classical anatomy) but is wired under the
basal forebrain (telencephalic).** The lamina terminalis is the
**rostral boundary of the hypothalamus** and the **anterior wall of
the third ventricle** — both **diencephalic** structures. The tree
places it under the **basal forebrain** because it is
**telencephalic-adjacent** (it abuts the septum pellucidum and fornix
rostrally) and because its **vascular organ is functionally part of
the forebrain circumventricular system**. This is a **deliberate
boundary choice**. Consumers that need **diencephalic
circumventricular organs** must resolve them under
``.../diencephalon/`` (see next flag); the **lamina terminalis and its
OVLT** are **here**, in the basal forebrain.
**Boundary status (the classical "lamina terminalis CVO group" is
split across the tree):** **Boundary case — the three CVOs classically
grouped with the lamina terminalis are split: the OVLT is HERE, the
subfornical organ and median eminence are under the hypothalamus.**
Classical anatomy groups **three circumventricular organs** with the
lamina terminalis region:
*   **Organum vasculosum of the lamina terminalis (OVLT)** — **HERE**
    (child of this module).
*   **Subfornical organ (SFO)** —
    ``.../diencephalon/hypothalamus/.../subfornical_organ/`` — **NOT
    here**.
*   **Median eminence** —
    ``.../diencephalon/hypothalamus/.../median_eminence/`` — **NOT
    here**.
Additionally, **two other CVOs** are diencephalic:
*   **Pineal gland** —
    ``.../diencephalon/epithalamus/pineal_gland/`` — **NOT here**.
*   **Subcommissural organ** —
    ``.../diencephalon/subcommissural_organ/`` — **NOT here**.
Consumers reconstructing the **classical lamina terminalis CVO group**
must **union** this module with the hypothalamus and epithalamus
modules. The lamina terminalis module provides only the **OVLT**; the
other **four CVOs** are documented in their own diencephalic modules.
**Boundary status (membrane, not a nucleus):** **Boundary case — a
thin grey-matter membrane, not a deep nucleus.** The lamina terminalis
is a **sheet of tissue** — thin enough to be transparent in some
preparations — that forms the **anterior wall of the third ventricle**.
It is **not** a deep nucleus (like the basal ganglia) and **not** a
cortical area (like the piriform cortex). It is a **surface** with a
**thin, heterogeneous cytoarchitecture** (ependymal lining on the
ventricular side, neuropil and scattered neurons on the
hypothalamic side). Consumers must not treat the lamina terminalis as
a uniform nucleus.
**Boundary status (midline, not paired):** **Boundary case — a
midline structure, not an anatomically paired one.** The lamina
terminalis is a **single midline membrane** at the **rostral end of
the third ventricle**; it is **not** a left-right pair like the
anterior perforated substance or the diagonal band. The tree wires it
under ``left/`` and ``right/`` as **structural duplicates** of the
same midline membrane. Consumers must **not** treat the left and
right modules as anatomically separate structures — they are the
**two halves of the same midline membrane**, or **conceptual
duplicates** for structural symmetry. See *Lateralization Notes*.

Overview
--------
The lamina terminalis is a **thin grey-matter membrane** forming the
**anterior wall of the third ventricle** — the rostral boundary of
the hypothalamus and the rostral-most extent of the diencephalon. It
extends from the **optic chiasm** (inferiorly) to the **rostrum of the
corpus callosum** (superiorly), and it is bounded caudally by the
**anterior commissure** and the **preoptic area** of the hypothalamus.

**The lamina terminalis is the "front wall" of the third ventricle.**
It is a **membrane**, not a nucleus, and it is the **structural
boundary** between the **telencephalon** (rostrally — septum
pellucidum, fornix) and the **diencephalon** (caudally —
hypothalamus). It is the **only midline membrane** in the basal
forebrain container, and its one child — the **OVLT** — is the
**only circumventricular organ** in the telencephalic-wired portion of
the forebrain.

**The lamina terminalis contains the OVLT in its mid-portion.** The
**organum vasculosum of the lamina terminalis (OVLT)** is a
**circumventricular organ** embedded in the lamina terminalis
mid-portion. It is a **fenestrated capillary bed** with **neurosecretory
neurons** that sense **plasma osmolality** and **circulating
angiotensin II**, driving **thirst** and **vasopressin release**. It
is the **functional core** of the lamina terminalis — the membrane
houses it, and the OVLT is the membrane's **only child**.

**The lamina terminalis is NOT the OVLT.** The membrane is the
**container**; the OVLT is the **circumventricular organ within it**.
Consumers that need the **membrane** resolve this module; consumers
that need the **osmoregulatory organ** resolve the **child module**.
They are **not** the same structure, and the membrane has few
functions of its own beyond **housing the OVLT** and **forming the
anterior wall of the third ventricle**.

**The classical "lamina terminalis CVO group" is split across the
tree.** Classical anatomy groups **three CVOs** with the lamina
terminalis region — the **OVLT** (here), the **subfornical organ**
(under hypothalamus), and the **median eminence** (under
hypothalamus). The tree separates them: the OVLT is the lamina
terminalis's **only child**, and the SFO and ME are **hypothalamic
children**. Additionally, the **pineal** (under epithalamus) and the
**subcommissural organ** (under diencephalon) are **diencephalic
CVOs** — not part of the lamina terminalis group at all. Consumers
reconstructing the **classical CVO group** must **union** this module
with the hypothalamus and epithalamus modules.

Container Contents (one child, closed set)
------------------------------------------
The lamina terminalis has **exactly one child**:

*   **``vascular_organ_of_lamina_terminalis``** — the **organum
    vasculosum of the lamina terminalis (OVLT)**, a **circumventricular
    organ** embedded in the lamina terminalis mid-portion.
    **Fenestrated capillary bed** with **neurosecretory neurons** that
    sense **plasma osmolality** and **circulating angiotensin II**,
    driving **thirst** and **vasopressin release**. **Depth: leaf (no
    children).** The OVLT is **one of the three classical lamina
    terminalis CVOs**; the other two (SFO, ME) are **under the
    hypothalamus**.

**Not children (deliberately excluded):**
*   **Subfornical organ (SFO)** →
    ``.../diencephalon/hypothalamus/.../subfornical_organ/`` — **not**
    here, despite its classical grouping with the lamina terminalis.
*   **Median eminence** →
    ``.../diencephalon/hypothalamus/.../median_eminence/`` — **not**
    here, despite its classical grouping with the lamina terminalis.
*   **Pineal gland** → ``.../diencephalon/epithalamus/pineal_gland/``
    — **not** here.
*   **Subcommissural organ** →
    ``.../diencephalon/subcommissural_organ/`` — **not** here.
*   **Optic chiasm** → ``.../diencephalon/hypothalamus/optic_chiasm/``
    — **not** here, despite its **inferior boundary** role for the
    lamina terminalis.
*   **Anterior commissure** → ``.../telencephalon/commissures/anterior_commissure/``
    — **not** here, despite its **caudal boundary** role.
*   **Septum pellucidum** → ``.../telencephalon/.../septum_pellucidum/``
    (not shown in visible tree dump) — **not** here, despite its
    **rostral adjacency**.
*   **Preoptic area** →
    ``.../diencephalon/hypothalamus/anterior/preoptic_area/`` —
    **not** here.

The Lamina Terminalis / Diencephalon Boundary
---------------------------------------------
This is the **most consequential boundary** in the lamina terminalis
module:

*   **Lamina terminalis + OVLT** — **here**, under the **basal
    forebrain** (telencephalic-wired).

*   **SFO, ME, pineal, subcommissural organ** — **diencephalic**,
    under ``.../diencephalon/``.

**The classical "lamina terminalis CVO group" is split across the
tree.** Consumers reconstructing it must **union** the two:

    CLASSICAL_LAMINA_TERMINALIS_CVO_GROUP = {
        "telencephalon.left.subcortical.basal_forebrain.lamina_terminalis": (
            "vascular_organ_of_lamina_terminalis",   # OVLT
        ),
        "forebrain.diencephalon.hypothalamus": (
            "subfornical_organ",   # SFO
            "median_eminence",     # ME
        ),
    }

**The pineal and subcommissural organ are NOT part of the classical
lamina terminalis group** — they are **separate diencephalic CVOs**
with different functions (pineal: melatonin; subcommissural organ:
Reissner's fiber/glycoprotein secretion). Consumers must not include
them in a "lamina terminalis" registry.

The Lamina Terminalis / Basal Forebrain Boundary
------------------------------------------------
The lamina terminalis is one of the **six basal forebrain children**,
but it is **structurally unlike** the other five:

*   **``anterior_perforated_substance``** — a **ventral surface patch**
    (paired, one per side).
*   **``diagonal_band_of_broca``** — a **grey-matter band** (paired,
    one per side).
*   **``septal_nuclei``** — deep **grey-matter nuclei** (paired).
*   **``nucleus_basalis``** — a deep **grey-matter nucleus** (paired).
*   **``substantia_innominata``** — a **transition zone** (paired).
*   **``lamina_terminalis``** (this module) — a **thin midline
    membrane** (single midline structure, structurally duplicated as
    left/right).

**The lamina terminalis is the only midline container in the basal
forebrain**, and the only one whose **left/right modules are structural
duplicates of a single midline structure** (see *Lateralization
Notes*). It is also the only one whose **primary clinical role is
circumventricular (osmoregulation) rather than striatal, cholinergic,
or olfactory** — the five other children's clinical associations are
Alzheimer's (nucleus basalis), basal forebrain amnesia (septum/DBB),
putaminal hemorrhage (APS), striatal (substantia innominata), and
limbic (septum). The lamina terminalis's clinical association is
**osmoregulatory** — adipsia, hypernatremia, thirst disorders,
fever — a **distinct category**.

Function in the Human Brain
---------------------------
The lamina terminalis has **membrane functions** (housing the OVLT,
forming the wall of the third ventricle) and **OVLT functions**
(osmoregulation, thirst, vasopressin, fever). The container-level
summary:

*   **Anterior wall of the third ventricle (Membrane Function):** The
    lamina terminalis **closes the third ventricle anteriorly** — it
    is the **structural boundary** between the telencephalon and the
    diencephalon at the midline, and it **contains the third
    ventricle's CSF** rostrally. It is a **thin, fenestrated
    membrane** that allows **CSF-vascular exchange** at the OVLT.

*   **Housing the OVLT (Structural Function):** The lamina terminalis
    is the **structural base** for the OVLT — the OVLT is **embedded
    in its mid-portion** and uses the **membrane's fenestrated
    capillaries** to sense plasma composition. The membrane itself is
    the **OVLT's housing**; the OVLT is the **functional core**.

*   **Osmoregulation (OVLT Function):** The OVLT **senses plasma
    osmolality** and **circulating angiotensin II** — the two major
    signals for **thirst** and **vasopressin (ADH) release**. It
    projects to the **median preoptic nucleus** and the
    **paraventricular and supraoptic nuclei** of the hypothalamus,
    driving **water intake** and **antidiuresis**.

*   **Fever Generation (OVLT Function):** The OVLT is a **site of
    prostaglandin E2 action** — circulating pyrogens (e.g., IL-1,
    LPS) act on the OVLT to produce **fever**. The OVLT's fenestrated
    capillaries allow **circulating pyrogens to access** the brain
    at this site.

*   **Neurosecretion (OVLT Function):** The OVLT contains
    **neurosecretory neurons** that release peptides into its
    fenestrated capillaries — it is a **neurohemal organ**, like the
    median eminence and the posterior pituitary, though its secretory
    products are less well characterized than those of the median
    eminence.

*   **NOT a neural processor in the classical sense.** The lamina
    terminalis (the membrane) is **not a neural processing
    structure** — it is a **membrane** and an **OVLT housing**. The
    OVLT (the child) is a **sensory circumventricular organ**, not a
    processor — it **senses** plasma composition and **drives**
    hypothalamic responses, but it does **not** process neural
    information in the way a cortical area does.

**The unifying theme:** the lamina terminalis is the **anterior wall
of the third ventricle** and the **housing for the OVLT**. It is a
**membrane with a circumventricular organ**, not a neural processor.
Its most famous function is **osmoregulation** (via the OVLT); its
most famous clinical association is **osmoregulatory disorder**
(adipsia, hypernatremia).

Associated Disorders
--------------------
Lamina terminalis and OVLT disorders are **osmoregulatory and
circumventricular**:

*   **Adipsia and Essential Hypernatremia — the signature
    disorder:** **OVLT lesions** (from **craniopharyngioma**,
    **anterior communicating artery aneurysm**, **subarachnoid
    hemorrhage**, **hydrocephalus**, or **surgery** in the region)
    disrupt **osmoregulation** and produce **adipsia** (absence of
    thirst) with **hypernatremia** — the **classic
    osmoregulatory disorder** of the lamina terminalis region. Patients
    do **not feel thirsty** despite high plasma osmolality, and they
    may develop **hypernatremia** without adequate water intake.
    **This is the lamina terminalis's signature clinical
    association.**

*   **SIADH-Like Syndromes (Contrast):** In **contrast** to adipsia,
    lesions that **spare the OVLT but disrupt hypothalamic
    osmoregulation** (e.g., some hypothalamic tumors) can produce
    **SIADH** (syndrome of inappropriate antidiuretic hormone) — but
    the **OVLT itself** is more often associated with **adipsia** and
    **hypernatremia** than with SIADH. The **OVLT drives water
    intake**; hypothalamic lesions drive **ADH release**. The
    distinction matters clinically.

*   **Fever of Unknown Origin / Central Fever:** The OVLT is a
    **site of prostaglandin E2 action** for fever. **Central fever**
    (fever from CNS injury) can arise from OVLT involvement in
    **subarachnoid hemorrhage**, **traumatic brain injury**, or
    **hypothalamic surgery**. **Antipyretics** (which inhibit
    prostaglandin synthesis) work partly through the OVLT.

*   **Craniopharyngioma — Lamina Terminalis Compression:** The
    **lamina terminalis** is adjacent to the **suprasellar region**,
    where **craniopharyngiomas** arise. These tumors can **compress
    the lamina terminalis** and the **OVLT**, producing **adipsia**,
    **hypernatremia**, and **obesity** (from hypothalamic
    involvement). **Craniopharyngioma** is a **classic clinical
    context** for lamina terminalis/OVLT dysfunction.

*   **Subarachnoid Hemorrhage — OVLT Dysfunction:** **Aneurysmal
    subarachnoid hemorrhage** (especially from **ACoA aneurysms**) can
    **damage the OVLT** and the **lamina terminalis**, contributing
    to **hyponatremia** (from **cerebral salt wasting** or
    **SIADH** — the mechanism is debated), **thirst disorders**, and
    **fever**. The **OVLT** is a **recognized site of secondary
    injury** in SAH.

*   **Lamina Terminalis Cysts:** **Rare cystic lesions** of the
    lamina terminalis have been reported — usually **asymptomatic**,
    but occasionally producing **hydrocephalus** (from third
    ventricle obstruction) or **osmoregulatory symptoms** (from OVLT
    compression).

*   **Lamina Terminalis Fenestration (Neurosurgical):** **Surgical
    fenestration of the lamina terminalis** is a **deliberate
    neurosurgical procedure** used in **aneurysm clipping** (to
    improve CSF flow and reduce hydrocephalus risk) and in
    **third ventriculostomy**. It is a **therapeutic disruption**,
    not a disorder, but it is worth documenting because it shows the
    lamina terminalis's **surgical relevance**.

**What is NOT here:** The lamina terminalis is **not** the substrate
for **Alzheimer's disease** (nucleus basalis), **basal forebrain
amnesia** (septum/DBB), **putaminal hemorrhage** (APS), **Kluver-Bucy
syndrome** (amygdala), or **temporal lobe epilepsy** (hippocampus).
Its clinical footprint is **osmoregulatory** (adipsia, hypernatremia),
**circumventricular** (fever, neurosecretion), and **surgical**
(fenestration) — a **distinct category** from the other basal
forebrain children.

Lateralization Notes
--------------------
This is the **left** lamina terminalis module. The lamina terminalis
is **midline**, and its lateralization status is **unique** in the
rhinencephalon/basal-forebrain region:

*   **Midline structure, not a paired one:** The lamina terminalis is
    a **single midline membrane** at the **rostral end of the third
    ventricle**. It is **not** a left-right pair like the
    **anterior perforated substance** (paired), the **diagonal band**
    (paired), the **septal nuclei** (paired), the **nucleus basalis**
    (paired), or the **substantia innominata** (paired). The tree
    wires it under ``left/`` and ``right/`` as **structural
    duplicates** — the two modules describe the **same midline
    membrane**, split for structural symmetry.

*   **The OVLT is also midline:** The **OVLT** is a **single midline
    organ** embedded in the lamina terminalis mid-portion. Its
    "left OVLT" and "right OVLT" modules describe the **same midline
    organ**.

*   **No Lateralized Function:** The lamina terminalis and OVLT have
    **no documented left-lateralized or right-lateralized function**.
    **Osmoregulation**, **thirst**, **vasopressin release**, and
    **fever** are **midline functions** — they are not lateralized.

*   **No Lateralized Syndrome:** Adipsia, hypernatremia, SIADH-like
    syndromes, and central fever are **midline disorders**, not
    lateralized ones. The **left and right modules** describe the
    **same clinical entity**.

**A consumer that assumes "left lamina terminalis = right lamina
terminalis" will be structurally and functionally correct — but for
a different reason than other structures.** Most structures in the
basal forebrain are **paired** (one per side), and the left/right
modules describe **two anatomical entities**. The lamina terminalis
is **midline**, and the left/right modules describe **one anatomical
entity** (the single midline membrane) duplicated for structural
symmetry. Consumers must **not** assume the left and right modules
describe **anatomically separate structures** — they describe the
**same midline structure**, wired as a left/right pair for the tree's
structural convention.

**This is the first midline structure in the telencephalon documented
so far**, and the **only midline container** in the basal forebrain.
The **pineal gland** (under epithalamus) and the **subfornical organ**
(under hypothalamus) are also midline, but they are **diencephalic**.
The lamina terminalis is the **only midline basal forebrain
structure**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only. But note that
    the **left module describes a midline structure** — the right
    module is a **structural duplicate**, not an anatomically
    separate structure.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../diencephalon/`` or from any other partition. The lamina
    terminalis's relationships to the hypothalamus, SFO, ME, pineal,
    and subcommissural organ are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — one child, closed set.** The lamina terminalis
    has exactly one child: ``vascular_organ_of_lamina_terminalis``
    (the OVLT). Consumers may resolve it, but should not assume any
    other children exist.
*   **Container IS a structure.** The lamina terminalis is both a
    **container** (it has the OVLT as a child) and a **structure** (it
    is the thin grey-matter membrane). Consumers must resolve both —
    the **membrane** (this module) and the **OVLT** (its child) — as
    distinct structures.
*   **Diencephalic-adjacent but telencephalic-wired.** The membrane is
    the **anterior wall of the third ventricle** (diencephalic in
    classical anatomy) but is **wired under the basal forebrain**
    (telencephalic). This is a **deliberate boundary choice**.
    Consumers that need **diencephalic CVOs** (SFO, ME, pineal,
    subcommissural organ) must resolve them under ``.../diencephalon/``.
*   **The classical "lamina terminalis CVO group" is split.** Only
    the **OVLT** is here; the **SFO** and **ME** are under the
    **hypothalamus**. Consumers reconstructing the classical group
    must **union** the two.
*   **Midline structure, not paired.** The left and right modules are
    **structural duplicates** of the **same midline membrane**, not
    anatomically separate structures. Consumers must not treat them
    as separate anatomical entities.
*   **Membrane, not a nucleus.** The lamina terminalis is a **thin
    grey-matter sheet**, not a deep nucleus. Consumers must not treat
    it as a uniform nucleus.
*   **No ``AREA_PATHS`` hop.** The lamina terminalis is a local
    container under the basal forebrain, not a cross-listed leaf.
*   **No nested cross-listing.** The lamina terminalis has no nested
    dual-framing module. It is a single container.
*   **Structural parity with right lamina terminalis.** Left and
    right lamina terminalis modules are **structurally identical** —
    same one-child closed set, same midline-structure caveat, same
    diencephalic-CVO redirects, same osmoregulatory associations.
    **The structural parity is stronger than for paired structures**,
    because the left and right modules describe the **same midline
    structure** — they are **duplicates**, not mirrors.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_forebrain import lamina_terminalis

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_forebrain.lamina_terminalis"
    )

**Do not** assume the lamina terminalis is a **midline structure
paired left-right**. It is a **single midline membrane**; the left
and right modules are **structural duplicates**. Consumers that
iterate both sides and expect **two anatomically separate structures**
will be **misled**.

**Do not** assume the lamina terminalis **contains** the subfornical
organ, median eminence, pineal gland, or subcommissural organ. Those
are **diencephalic** and under ``.../diencephalon/``. The lamina
terminalis's **only child** is the **OVLT**.

**Do not** assume the lamina terminalis is a **deep nucleus** or a
**cortical area**. It is a **thin grey-matter membrane** — the
**anterior wall of the third ventricle**.

**Do not** assume the lamina terminalis is **diencephalic** just
because it is the anterior wall of the third ventricle. The tree
places it under the **basal forebrain** — a deliberate boundary
choice.

Iterating the lamina terminalis's child (recommended consumer
pattern)::

    LAMINA_TERMINALIS_CHILDREN = (
        "vascular_organ_of_lamina_terminalis",   # OVLT
    )
    # Closed set. Do not assume additional children.

Reaching the classical lamina terminalis CVO group (recommended
consumer pattern)::

    # The classical "lamina terminalis CVO group" is split across
    # the tree. Union it:
    CLASSICAL_LAMINA_TERMINALIS_CVO_GROUP = {
        "telencephalon.left.subcortical.basal_forebrain.lamina_terminalis": (
            "vascular_organ_of_lamina_terminalis",   # OVLT
        ),
        "forebrain.diencephalon.hypothalamus": (
            "subfornical_organ",   # SFO
            "median_eminence",     # ME
        ),
    }
    # The pineal and subcommissural organ are NOT part of this group.

Reaching the other diencephalic CVOs (recommended consumer pattern)::

    # The diencephalic CVOs are NOT lamina terminalis children. Resolve
    # them at their own paths:
    #
    #   .../diencephalon/hypothalamus/.../subfornical_organ/
    #   .../diencephalon/hypothalamus/.../median_eminence/
    #   .../diencephalon/epithalamus/pineal_gland/
    #   .../diencephalon/subcommissural_organ/
    #
    # These are SEPARATE MODULES under diencephalon/.

Reaching the OVLT (recommended consumer pattern)::

    # The OVLT is the lamina terminalis's ONLY child. Resolve it:
    #
    #   subcortical.basal_forebrain.lamina_terminalis.vascular_organ_of_lamina_terminalis
    #
    # The lamina terminalis (this module) is the MEMBRANE; the OVLT
    # is the CIRCUMVENTRICULAR ORGAN. They are distinct structures.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        lt_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.lamina_terminalis"
        )
        # resolve lt_path through the memory/recall layer
        # NOTE: the two paths describe the SAME midline structure,
        # duplicated for structural symmetry.

References
----------
*   **Canonical lamina terminalis anatomy:** McKinley, M.J., et al.
    (2003). "The sensory circumventricular organs of the mammalian
    brain." *Advances in Anatomy, Embryology and Cell Biology*
    172:1–122. (Definitive review; lamina terminalis; OVLT; SFO;
    osmoregulation; thirst.)
*   **OVLT and osmoregulation:** Johnson, A.K., Gross, P.M. (1993).
    "Sensory circumventricular organs and brain homeostatic
    pathways." *FASEB Journal* 7:678–686. (OVLT, SFO, and area
    postrema as sensory CVOs; osmoregulation.)
*   **OVLT and angiotensin II:** Simpson, J.B. (1981). "The
    circumventricular organs and the central actions of
    angiotensin II." *Neuroendocrinology* 32:248–256. (OVLT as a
    central site of angiotensin II action for thirst.)
*   **OVLT and fever:** Stitt, J.T. (1985). "Evidence for the
    involvement of the organum vasculosum laminae terminalis in the
    febrile responses of rabbits and rats." *Journal of Physiology*
    368:501–511. (OVLT as a site of prostaglandin E2 action for
    fever.)
*   **Adipsia and hypernatremia:** Robertson, G.L. (1987). "Physiology
    of ADH secretion and thirst." In *Clinical Neuroendocrinology*
    (Martin, J.B., Reichlin, S., Bick, K.L., eds.). (Osmoregulatory
    disorders; adipsia; hypernatremia.)
*   **Craniopharyngioma and osmoregulatory dysfunction:** Sklar, C.A.
    (1994). "Craniopharyngioma: endocrine sequelae of treatment."
    *Pediatric Neurosurgery* 21:120–123. (Adipsia and hypernatremia
    after craniopharyngioma treatment.)
*   **SAH and OVLT:** Diringer, M.N. (2003). "Management of sodium
    abnormalities following subarachnoid hemorrhage."
    *Neurosurgery Clinics of North America* 14:427–438.
    (Hyponatremia after SAH; OVLT and hypothalamic involvement.)
*   **Lamina terminalis fenestration:** Komotar, R.J., et al. (2008).
    "The role of lamina terminalis fenestration in reducing shunt-
    dependent hydrocephalus following aneurysmal subarachnoid
    hemorrhage." *Journal of Neurosurgery* 108:1001–1007. (Surgical
    fenestration of the lamina terminalis.)
*   **Lamina terminalis cysts:** Binitie, O., et al. (2004). "Lamina
    terminalis cysts." *Journal of Clinical Neuroscience*
    11:559–561. (Rare cystic lesions of the lamina terminalis.)
*   **Circumventricular organs overview:** Ganong, W.F. (2000).
    "Circumventricular organs: definition and role in the regulation
    of endocrine and autonomic function." *Clinical and Experimental
    Pharmacology and Physiology* 27:422–427. (Overview of the CVO
    group including OVLT, SFO, ME, pineal, subcommissural organ,
    area postrema.)
*   **Diencephalic anatomy:** Nieuwenhuys, R., Voogd, J., van
    Huijzen, C. (2008). *The Human Central Nervous System*, 4th ed.
    (Lamina terminalis as the anterior wall of the third ventricle;
    its relation to the hypothalamus.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Lamina terminalis and OVLT in overview.)
*   NeuroNames — Lamina terminalis (left); FMA — Lamina terminalis
    (left member). Note: the lamina terminalis is a **midline
    structure**, and the FMA "left member" designation is a
    structural convention, not an anatomical pairing.
"""