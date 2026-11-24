"""
infrastructure.brainparts.midbrain.pretectum
============================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── tectum
    ├── tegmentum
    ├── cerebral_aqueduct
    ├── cerebral_peduncle
    ├── cranial_nerve_nuclei
    └── pretectum                   <-- THIS MODULE (region container)
        ├── left
        │   ├── olivary_pretectal_nucleus
        │   ├── nucleus_of_the_optic_tract
        │   ├── anterior_pretectal_nucleus
        │   ├── posterior_pretectal_nucleus
        │   └── medial_pretectal_nucleus
        └── right
            ├── olivary_pretectal_nucleus
            ├── nucleus_of_the_optic_tract
            ├── anterior_pretectal_nucleus
            ├── posterior_pretectal_nucleus
            └── medial_pretectal_nucleus

**Primary synonym:** Pretectum; pretectal region; pretectal area;
pretectal nuclei; area pretectalis; nucleus pretectalis.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). The pretectum is a **region** of the **diencephalon-
midbrain junction** — a **cluster of small nuclei** (the **olivary
pretectal nucleus**, the **nucleus of the optic tract**, the
**anterior pretectal nucleus**, the **posterior pretectal
nucleus**, and the **medial pretectal nucleus**) positioned
**caudal to the thalamus** and **rostral to the superior
colliculus**, at the **diencephalon-midbrain junction**.
**Container status:** **This module is a REGION CONTAINER, not a
leaf.** It holds the **pretectal nuclei** as its children. Each is
**paired** (a `left/` leaf and a `right/` leaf). The container
imposes **aggregation rules** on the nuclei but does **not** itself
carry a single anatomical function — every functional claim belongs
to a **child** (the olivary pretectal nucleus for the pupillary
light reflex, the nucleus of the optic tract for optokinetic
nystagmus, the anterior pretectal nucleus for nociception and
somatosensation, etc.). See *Expected Structural Children*.
**Developmental designation:** **Contested — the pretectum is at the
diencephalon-midbrain junction, and its allocation to one vesicle
or the other is a matter of atlas convention rather than
development.** See *Contested Placement and Reconciliation*.
**Structural parent:** ``.../midbrain/`` → **direct child** of the
midbrain container, as a **region container** peer to ``tectum/``,
``tegmentum/``, ``cerebral_aqueduct/``, ``cerebral_peduncle/``, and
``cranial_nerve_nuclei/``.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left pretectal nuclei** — a side-scoped
    container holding the five left-side pretectal nuclei.
*   ``right/`` — the **right pretectal nuclei** — a side-scoped
    container holding the five right-side pretectal nuclei.
Each of the two side containers is expected to hold:
*   ``olivary_pretectal_nucleus/`` — the **pupillary light reflex
    relay** — projects **bilaterally** to the **Edinger-Westphal
    nucleus** — the **afferent limb** of the direct and consensual
    pupillary light reflex. **The key pretectal nucleus for
    pupillary clinical signs.**
*   ``nucleus_of_the_optic_tract/`` — a **direction-selective**
    pretectal nucleus — implicated in the **optokinetic
    nystagmus** circuit and in **horizontal optokinetic
    responses**.
*   ``anterior_pretectal_nucleus/`` — a **nociceptive and
    somatosensory relay** — implicated in **pain modulation** and
    **defensive behaviors** via projections to the **periaqueductal
    gray** and **intralaminar thalamus**.
*   ``posterior_pretectal_nucleus/`` — a **visual relay** — less
    well characterized than the olivary pretectal nucleus.
*   ``medial_pretectal_nucleus/`` — the **least characterized** of
    the pretectal nuclei — its functional role is **not well
    established** in humans.
**Boundary status (CONTESTED PLACEMENT — the pretectum is at the
DIENCEPHALON-MIDBRAIN JUNCTION, and its allocation to one vesicle or
the other is a matter of ATLAS CONVENTION):** **Boundary case —
the pretectum is at the DIENCEPHALON-MIDBRAIN JUNCTION, and its
allocation to the midbrain or to the diencephalon is CONTESTED.** In
the **modern comparative and Paxinos-style atlas tradition**, the
pretectum is placed in the **diencephalon** — as the **pretectal
region** of the **thalamus** (caudal to the main thalamus, rostral
to the superior colliculus). In the **older comparative anatomy
and some brainstem atlases**, the pretectum is placed in the
**midbrain** — as the **pretectal area** of the **midbrain
tegmentum**. **Both placements describe the same nuclei at the
same physical location.** The **on-disk tree places the pretectum
under ``midbrain/``** — **that is the AUTHORITATIVE placement for
this tree**, and consumers resolving the pretectum should use the
**midbrain path**. **This module explicitly reconciles the
disagreement** with the earlier leaves that called the pretectal
nuclei "diencephalon" — see *Contested Placement and
Reconciliation* below.
**Boundary status (RECONCILIATION — the earlier leaves that called
the pretectal nuclei "DIENCEPHALON" must be AMENDED):** **Boundary
case — the earlier leaves (the left and right **oculomotor
nucleus**, **Edinger-Westphal nucleus**, and **mesencephalic
trigeminal nucleus** leaves) were written stating that the
**pretectal nuclei are DIENCEPHALON** and that consumers should
**not** resolve the pretectal nucleus through the midbrain path.
The on-disk tree now places the pretectum **under ``midbrain/``**,
which **contradicts** those statements.** **The tree is
authoritative** — and the reconciliation is: **the pretectal nuclei
are at the diencephalon-midbrain junction**, and the tree resolves
them **under ``midbrain/pretectum/``** (and, **if a
``forebrain/diencephalon/pretectum/`` node is also present, under
that path as a cross-listed region** — the same cross-listing
mechanism the tree already uses between ``cranial_nerve_nuclei/``
and ``tegmentum/``). **The earlier six leaves (left/right
oculomotor, left/right EW, left/right mesV) should be amended** to
replace *"pretectal nuclei are DIENCEPHALON; do not resolve through
the midbrain path"* with *"pretectal nuclei are at the
diencephalon-midbrain junction; resolve them under
``midbrain/pretectum/`` (and, if present,
``forebrain/diencephalon/pretectum/``) — the two paths reach the
same nuclei"*. **This is a live structural contradiction in the
tree that this module resolves** — but the reconciliation is only
complete when the earlier six leaves are amended. See *Cross-
Listing Statement*.
**Boundary status (REGION CONTAINER — NOT a leaf, NOT a single
nucleus):** **Boundary case — the pretectum is a REGION CONTAINER,
not a single nucleus.** It holds the **pretectal nuclei** as its
children (five nuclei per side). It has **no anatomical function of
its own** — every functional claim belongs to a **child** (the
olivary pretectal nucleus for the pupillary light reflex; the
nucleus of the optic tract for optokinetic nystagmus; the anterior
pretectal nucleus for nociception; the posterior and medial
pretectal nuclei for less-characterized visual and integrative
functions). Consumers must **not** resolve a pretectal function by
resolving this container — they must resolve the **child** that
carries it.
**Boundary status (NOT the tectum — the tectum is the COLLICULI, and
they are DIFFERENT midbrain compartments):** **Boundary case — the
pretectum is NOT the tectum.** The **tectum**
(``.../midbrain/tectum/``) is the **dorsal midbrain** — it contains
the **superior colliculus** (visual/oculomotor orienting; saccade
generation) and the **inferior colliculus** (auditory relay). The
**pretectum** is a **separate region** at the diencephalon-midbrain
junction, **rostral to the superior colliculus**. **They are
DIFFERENT STRUCTURES in DIFFERENT midbrain compartments** — the
**tectum** is the **saccadic and auditory midbrain**; the
**pretectum** is the **pupillary and optokinetic region**. The
**superior colliculus** drives **saccades** via the **tectobulbar
tract** to the **CN III nuclei**; the **pretectum** drives the
**pupillary light reflex** via the **EW nucleus**. **These are
DIFFERENT functional systems.** Consumers must **not** conflate the
pretectum with the tectum, and must **not** resolve the colliculi
through the pretectum path.
**Boundary status (NOT the thalamus — the thalamus is
DIENCEPHALON, and the pretectum is at its CAUDAL border):**
**Boundary case — the pretectum is NOT the thalamus.** The
**thalamus** (``.../forebrain/diencephalon/thalamus/``) is the
**diencephalic relay** — it contains the **lateral geniculate body**
(visual relay), the **medial geniculate body** (auditory relay),
the **pulvinar** (visual attention), the **ventral posterior
nucleus** (somatosensory relay), the **ventral lateral nucleus**
(motor relay), the **mediodorsal nucleus** (prefrontal relay), and
the **intralaminar nuclei** (arousal). The **pretectum** is
**caudal to the main thalamus**, at the **diencephalon-midbrain
junction**. **They are DIFFERENT STRUCTURES** — the **thalamus** is
the **main diencephalic relay**; the **pretectum** is a **small
region at its caudal border** with **pupillary and optokinetic
functions**. Some atlases group the pretectum **with** the
thalamus (as the "pretectal region of the thalamus") — but the
**functions are distinct**, and consumers must **not** resolve the
thalamus through the pretectum path (or vice versa).
**Boundary status (NOT a cranial nerve nucleus — the pretectal
nuclei are RELAY nuclei, and the EW nucleus they project to IS a
CN nucleus):** **Boundary case — the pretectum is NOT a cranial
nerve nucleus.** The **pretectal nuclei** are **relay nuclei** —
they receive **retinal input** via the **optic tract** and project
to the **Edinger-Westphal nucleus**. The **EW nucleus**
(``.../cranial_nerve_nuclei/left/edinger_westphal_nucleus/`` and
``.../cranial_nerve_nuclei/right/edinger_westphal_nucleus/``) is
the **CN III preganglionic parasympathetic** nucleus — it is
**downstream** of the pretectum. **The pretectum is UPSTREAM of
the EW nucleus** in the **pupillary light reflex arc**. Consumers
must **not** conflate the pretectum with the EW nucleus, and must
**not** resolve the EW nucleus through the pretectum path. **The
pupillary light reflex spans the pretectum (diencephalon-midbrain
junction) → EW nucleus (midbrain) → ciliary ganglion (peripheral).**
**Boundary status (NOT the superior colliculus — the superior
colliculus DRIVES saccades, and the pretectum DRIVES the pupillary
light reflex):** **Boundary case — the pretectum is NOT the
superior colliculus.** The **superior colliculus**
(``.../tectum/left/superior_colliculus/`` and
``.../tectum/right/superior_colliculus/``) is the
**visual/oculomotor orienting** structure — it **drives saccades**
via the **tectobulbar tract** to the **CN III nuclei**. The
**pretectum** (here) **drives the pupillary light reflex** via the
**EW nucleus**. **They are DIFFERENT STRUCTURES in DIFFERENT
functional systems** — the **superior colliculus** is **saccadic**;
the **pretectum** is **pupillary/optokinetic**. Consumers must
**not** conflate the pretectum with the superior colliculus.
**Boundary status (NOT the lateral geniculate body — the LGN is the
THALAMIC VISUAL RELAY):** **Boundary case — the pretectum is NOT
the lateral geniculate body.** The **lateral geniculate body**
(``.../forebrain/diencephalon/thalamus/lateral_geniculate_body/``)
is the **thalamic visual relay** — it projects to the **primary
visual cortex (V1)** for **conscious visual perception**. The
**pretectum** (here) is the **pupillary and optokinetic relay** —
it does **not** project to the visual cortex, and it does **not**
mediate **conscious vision**. **They are DIFFERENT STRUCTURES in
DIFFERENT functional systems** — the **LGN** is **visual
perception**; the **pretectum** is **pupillary/optokinetic
reflexes**. Consumers must **not** conflate the pretectum with the
LGN.
**Boundary status (STRUCTURE-CLASS TAXONOMY — the pretectal nuclei
are RELAY nuclei, and carry NO coupling warning):** **Boundary
case — the pretectal nuclei are RELAY nuclei.** In the family's
**structure-class taxonomy**, they are **sensory relay nuclei** —
similar in class to the **mesencephalic trigeminal nucleus**
(sensory nucleus — no coupling warning) and the **retrotrapezoid
nucleus** (sensor/driver — no coupling warning). **Relay nuclei
carry NO coupling warning** — same rule as motor nuclei, premotor
pools, sensor nuclei, and conduction pathways. Their coordination
with the **contralateral pretectum** is via the **bilateral
projection** from each pretectal nucleus to the **EW nuclei** on
**both sides** (for the consensual pupillary light reflex) — **not**
via intrinsic nucleus-to-nucleus coupling. **Relay nuclei carry
NO coupling warning.** See *Lateralization Notes* and *Design
Contract*.
**Boundary status (BILATERAL PROJECTION — the CONTRALATERAL
projection to the EW nuclei is what makes the pupillary light
reflex CONSENSUAL):** **Boundary case — the pretectum projects
BILATERALLY to the EW nuclei on BOTH sides.** The **olivary
pretectal nucleus** — the principal pupillary light reflex relay —
**projects to BOTH the left and right EW nuclei**, **not just the
ipsilateral one**. **This bilateral projection is what makes the
pupillary light reflex CONSENSUAL** — light in one eye produces
pupil constriction in **both** eyes. **The two pretectal nuclei
(left and right) are NOT directly coupled** — each is an
**independent relay** whose **bilateral output** to the EW nuclei
on both sides is what makes the reflex **consensual**. **The
pretectal bilateral projection is the upstream mechanism of the
consensual reflex.** Consumers must **not** assume the consensual
reflex is produced by **EW-EW coupling** — it is produced by the
**pretectal bilateral projection** to both EW nuclei. See *The
Pupillary Light Reflex Arc* below.

Overview
--------
The pretectum is a **region** of the **diencephalon-midbrain
junction** — a **cluster of small nuclei** (the **olivary pretectal
nucleus**, the **nucleus of the optic tract**, the **anterior
pretectal nucleus**, the **posterior pretectal nucleus**, and the
**medial pretectal nucleus**) positioned **caudal to the thalamus**
and **rostral to the superior colliculus**. It is the **afferent
relay of the pupillary light reflex** — receiving **retinal input**
via the **optic tract** and projecting **bilaterally** to the
**Edinger-Westphal nuclei** to drive the **direct and consensual
pupillary light responses**. It also participates in **optokinetic
nystagmus** (via the nucleus of the optic tract) and in
**nociception and defensive behaviors** (via the anterior pretectal
nucleus). It is a **region container** under the midbrain — its
children are the **five paired pretectal nuclei**.

**The pretectum is at the DIENCEPHALON-MIDBRAIN JUNCTION, and its
allocation to one vesicle or the other is a matter of atlas
convention.** Modern atlases place it in the **diencephalon**;
older comparative and brainstem atlases place it in the
**midbrain**. **Both describe the same nuclei at the same
physical location.** The **on-disk tree places the pretectum under
``midbrain/``** — that is the **authoritative** placement for this
tree. See *Contested Placement and Reconciliation*.

**The pretectum is the CONTAINER, NOT a functional leaf.** Every
functional claim belongs to a **child** — the **olivary pretectal
nucleus** for the pupillary light reflex; the **nucleus of the
optic tract** for optokinetic nystagmus; the **anterior pretectal
nucleus** for nociception and defensive behaviors; the **posterior
and medial pretectal nuclei** for less-characterized visual and
integrative functions. Consumers must resolve the **child** that
carries the function.

**The pretectum is a PAIRED-STRUCTURE region.** Each of the five
pretectal nuclei is **paired** (a `left/` leaf and a `right/`
leaf). **The bilateral projection to the EW nuclei** (from each
pretectal nucleus to **both** EW nuclei) is what makes the
pupillary light reflex **consensual** — **not** EW-EW coupling.

**The pretectum is the upstream of the CONSENSUAL pupillary light
reflex.** The reflex arc is: **retina → optic nerve → pretectum
(bilateral projection) → EW nuclei (both sides) → ciliary ganglia
(both sides) → sphincter pupillae (both sides)**. **The pretectum's
bilateral projection is the mechanism** — and this is the **key
fact** the earlier oculomotor and EW leaves already state.

Contested Placement and Reconciliation
-------------------------------------
**The pretectum is at the diencephalon-midbrain junction.** Modern
comparative and Paxinos-style atlases place it in the
**diencephalon** (as the **pretectal region** of the **thalamus**).
Older comparative anatomy and some brainstem atlases place it in
the **midbrain** (as the **pretectal area** of the **midbrain
tegmentum**). **Both describe the same nuclei at the same physical
location** — the disagreement is **naming and allocation**, not
**anatomy**.

**The on-disk tree places the pretectum under ``midbrain/``.** That
is the **authoritative** placement for this tree — and it
**reconciles the disagreement** by giving the pretectum a **definite
home in the tree**. Consumers resolving the pretectum should use
the **midbrain path** (`midbrain.pretectum.<nucleus>.<side>`).

**If the tree also has a ``forebrain/diencephalon/pretectum/`` node**
— that is the **same region**, cross-listed under the diencephalon
path. **The two paths reach the same nuclei** — this is the **same
cross-listing mechanism** used between `cranial_nerve_nuclei/` and
`tegmentum/`. Consumers should resolve by **one** path, not both, for
a single lookup — enumerating **both** paths will yield
**duplicates** for the pretectal nuclei.

**The earlier leaves (left/right oculomotor, left/right EW,
left/right mesV) were written stating that the pretectal nuclei are
DIENCEPHALON and that consumers should not resolve the pretectal
nucleus through the midbrain path. Those statements are now
inconsistent with the on-disk tree** — the tree places the pretectum
under `midbrain/`. **The earlier six leaves should be amended** to
replace their diencephalon-only framing with a **junction framing**:
*"the pretectal nuclei are at the diencephalon-midbrain junction;
resolve them under `midbrain/pretectum/` (and, if present,
`forebrain/diencephalon/pretectum/`) — the two paths reach the same
nuclei."* **This module is the reconciliation — but the
reconciliation is complete only when the earlier six leaves are
amended.**

The Pupillary Light Reflex Arc (the pretectum's primary function)
---------------------------------------------------------------
The **pupillary light reflex** is the pretectum's **principal
function**. The arc:

*   **Afferent limb** — light → retina → optic nerve → optic chiasm
    → optic tract → **pretectum** (specifically, the **olivary
    pretectal nucleus**, and the **nucleus of the optic tract**).
*   **Pretectal relay** — the pretectum projects **BILATERALLY** to
    the **EW nuclei** on **both sides**.
*   **Efferent limb** — each **EW nucleus** → **ipsilateral ciliary
    ganglion** → **ipsilateral sphincter pupillae** → **pupil
    constriction**.

**Direct response:** light in the **left** eye → left retina → left
optic nerve → **left pretectum** → **bilateral** projection to
**both** EW nuclei → **both** pupils constrict.

**Consensual response:** light in the **right** eye → right retina
→ right optic nerve → **right pretectum** → **bilateral**
projection to **both** EW nuclei → **both** pupils constrict.

**The bilateral pretectal projection is the mechanism of the
consensual response.** The **two EW nuclei are NOT directly coupled**
— the coordination is **upstream**, at the pretectal level.

**The pretectum's bilateral projection is the upstream half of the
arc; the EW nucleus's efferent projection is the downstream half;
the ciliary ganglion's postganglionic projection is the peripheral
half.** The **pretectum** is the **midbrain-level afferent relay**.

**Light-Near Dissociation (the pretectal clinical signature):** The
**near response** (accommodation and miosis during near vision)
uses a **different pathway** — cortical projections to the EW
nucleus that **bypass the pretectum** (or use a different pretectal
route). **A pretectal lesion** disrupts the **light reflex** (the
afferent limb fails to reach EW) but **spares the near response**
(the cortical pathway is intact) — producing **light-near
dissociation** — the **pupil does not react to light but DOES
constrict during the near response**. **This is the diagnostic
signature of a pretectal lesion** — and it is one of the **components
of Parinaud syndrome** (dorsal midbrain syndrome).

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
The pretectum container is expected to hold **two side containers**
(``left/`` and ``right/``), each holding **five pretectal nuclei**:

*   **``olivary_pretectal_nucleus/``** — the **pupillary light reflex
    relay** — the **principal** pretectal nucleus for the direct and
    consensual pupillary light responses. Receives **retinal
    input** via the **optic tract**; projects **bilaterally** to
    the **EW nuclei** on both sides. **The key pretectal nucleus for
    pupillary clinical signs.** **Paired** (left/right).

*   **``nucleus_of_the_optic_tract/``** — a **direction-selective**
    pretectal nucleus — implicated in the **optokinetic nystagmus**
    circuit and in **horizontal optokinetic responses**. Receives
    **retinal input** via the **optic tract**; projects to the
    **inferior olive** and the **vestibular nuclei** (via the
    **climbing fiber** and **vestibulo-optokinetic** pathways).
    **Paired** (left/right).

*   **``anterior_pretectal_nucleus/``** — a **nociceptive and
    somatosensory relay** — implicated in **pain modulation** and
    **defensive behaviors** via projections to the **periaqueductal
    gray** (PAG) and the **intralaminar thalamus**. **Paired**
    (left/right).

*   **``posterior_pretectal_nucleus/``** — a **visual relay** — less
    well characterized than the olivary pretectal nucleus;
    implicated in **visually guided behaviors**. **Paired**
    (left/right).

*   **``medial_pretectal_nucleus/``** — the **least characterized**
    of the pretectal nuclei — its functional role is **not well
    established** in humans. **Paired** (left/right).

**These are the expected children — the on-disk tree is the
authoritative source.** The container imposes the **cross-listing**
and **aggregation rules** below; the leaves impose the leaf-level
contract (boundary stacks, function, disorders, lateralization,
references) documented in the existing leaf modules.

Aggregation Rules (the container's contract on its children)
------------------------------------------------------------
The pretectum container **imposes the following rules** on every
leaf under it. These are **inherited** from the midbrain container
and **specialized** for the pretectum's role as a **junction
region**:

*   **PAIRED-LEAF DISCIPLINE.** Each pretectal nucleus is a **paired
    structure** — a `left/` leaf and a `right/` leaf. There is **no
    midline pretectal nucleus**.
*   **RELAY-NUCLEUS DISCIPLINE — NO COUPLING WARNING.** The pretectal
    nuclei are **relay nuclei** (sensory relay, nociceptive relay,
    optokinetic relay). **Relay nuclei carry NO coupling warning**
    — same rule as motor nuclei, premotor pools, sensor nuclei, and
    conduction pathways. Coordination with the **contralateral
    pretectum** is via the **bilateral projection** to the EW nuclei
    — **not** via intrinsic pretectal-to-pretectal coupling.
*   **BILATERAL-PROJECTION DISCIPLINE.** The **olivary pretectal
    nucleus** (and the **nucleus of the optic tract**) project
    **bilaterally** to the **EW nuclei** on **both sides** — this is
    the mechanism of the **consensual pupillary light reflex**.
    **The pretectal bilateral projection is upstream of EW** — **not**
    EW-EW coupling. Consumers must **not** attribute the consensual
    reflex to **EW-EW coupling** — the coordination is
    **pretectal**.
*   **CHEMICALS-LAYER DISCIPLINE.** The **transmitter phenotypes** of
    the pretectal nuclei (glutamatergic, GABAergic, cholinergic
    subpopulations) are **``chemicals_hormones``-layer facts** —
    documented as **prose** in the leaves, **never imported**.
    Dependency DAG unchanged: ``chemicals_hormones → memory →
    brainparts``.
*   **CROSS-LISTING WITH THE DIENCEPHALON (IF PRESENT).** If the tree
    has a ``forebrain/diencephalon/pretectum/`` node, the pretectal
    nuclei are **cross-listed** between that path and
    ``midbrain/pretectum/`` — the same mechanism used between
    ``cranial_nerve_nuclei/`` and ``tegmentum/``. Consumers resolve
    by **one** path per lookup.
*   **JUNCTION REGION — NOT A SINGLE VESICLE.** The pretectum is at
    the **diencephalon-midbrain junction**; its allocation to the
    midbrain in this tree is **convention**, not a developmental
    claim. Consumers must **not** treat "pretectum under midbrain" as
    a claim that the pretectum is **developmentally** midbrain — it
    is at the **junction**.
*   **NOT A CRANIAL NERVE NUCLEUS — NOT A TECTUM STRUCTURE — NOT A
    THALAMIC NUCLEUS.** The pretectal nuclei are **relay nuclei**
    upstream of the **EW nucleus**; they are **not** CN nuclei,
    **not** tectum structures (colliculi), **not** thalamic nuclei
    (LGN, pulvinar, etc.). The boundary stack above spells out each
    exclusion.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-lobe imports.** The pretectum container does **not**
    import from ``../forebrain/diencephalon/`` or
    ``../hindbrain/``. The pretectum's relationships to the
    **thalamus**, the **lateral geniculate body**, the **EW
    nucleus**, the **superior colliculus**, the **PAG**, the
    **ciliary ganglion**, and the **retina** are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **transmitter
    phenotypes** of the pretectal nuclei (glutamatergic, GABAergic,
    cholinergic subpopulations) are **``chemicals_hormones``-layer
    facts** — documented as **prose**, **never imported**.
*   **CONTAINER — paired pretectal nuclei.** The left and right
    pretectal nuclei are the **structural children**. The **five
    pretectal nuclei per side** are **sub-container children**
    (`left/<nucleus>/` and `right/<nucleus>/`).
*   **CONTESTED PLACEMENT — RECONCILED VIA THE TREE.** The pretectum
    is at the diencephalon-midbrain junction; its allocation to the
    midbrain in this tree is **convention**. **The on-disk tree is
    authoritative** — resolve the pretectum under
    ``midbrain/pretectum/``. **The earlier six leaves (left/right
    oculomotor, left/right EW, left/right mesV) should be amended**
    to replace their "pretectal = diencephalon only" framing with a
    "junction" framing — otherwise the tree has a **live
    contradiction**.
*   **CROSS-LISTING (IF PRESENT).** If a
    ``forebrain/diencephalon/pretectum/`` node exists, the pretectal
    nuclei are **cross-listed** between that path and
    ``midbrain/pretectum/``. Consumers resolve by **one** path per
    lookup.
*   **REGION CONTAINER — NOT A LEAF.** The pretectum is a **region
    container** — it has **no anatomical function of its own**;
    every functional claim belongs to a **child**.
*   **RELAY NUCLEI — NO COUPLING WARNING.** The pretectal nuclei are
    **relay nuclei** — **no coupling warning**, same rule as motor
    nuclei, premotor pools, sensor nuclei, and conduction pathways.
    The **bilateral projection to the EW nuclei** is the mechanism
    of the consensual reflex — **not** intrinsic pretectal-to-
    pretectal coupling.
*   **BILATERAL PROJECTION — NOT EW-EW COUPLING.** The consensual
    pupillary light reflex is mediated by the **pretectal bilateral
    projection** to both EW nuclei — **not** by EW-EW coupling.
*   **NOT the tectum — NOT the colliculi.** The pretectum is a
    **separate region** rostral to the superior colliculus.
*   **NOT the thalamus — NOT the LGN.** The pretectum is at the
    **caudal border** of the thalamus; it is **not** the thalamus,
    and it is **not** the LGN (the thalamic visual relay to V1).
*   **NOT a cranial nerve nucleus — the EW nucleus it projects to IS
    a CN nucleus.** The pretectum is **upstream** of EW.
*   **NOT the superior colliculus — the colliculus DRIVES saccades;
    the pretectum DRIVES the pupillary light reflex.**
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing
    (if present) is **within the diencephalon-midbrain junction**
    (``forebrain/diencephalon/pretectum`` ↔
    ``midbrain/pretectum``) — the same mechanism used for the CN
    nuclei cross-listing.
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts.midbrain import pretectum

Resolve a pretectal leaf by path::

    from infrastructure.brainparts.midbrain.pretectum.left import olivary_pretectal_nucleus
    from infrastructure.brainparts.midbrain.pretectum.right import olivary_pretectal_nucleus

Or by fully-qualified path string (leaves, not the container)::

    left_olivary_path = (
        "midbrain.pretectum.left.olivary_pretectal_nucleus"
    )
    right_olivary_path = (
        "midbrain.pretectum.right.olivary_pretectal_nucleus"
    )

**Do not** assume the pretectum is the **tectum**. The **tectum** is
the **dorsal midbrain** — the **colliculi** (superior colliculus,
inferior colliculus). The **pretectum** is a **separate region**
rostral to the superior colliculus. **They are DIFFERENT
STRUCTURES in DIFFERENT functional systems** — the **tectum** is
**saccadic and auditory**; the **pretectum** is **pupillary and
optokinetic**.

**Do not** assume the pretectum is the **thalamus**. The **thalamus**
is the **main diencephalic relay**; the **pretectum** is a **small
region at its caudal border**. **They are DIFFERENT STRUCTURES** —
the **thalamus** is the **sensory and motor relay to cortex**; the
**pretectum** is a **small pupillary and optokinetic region**.

**Do not** assume the pretectum is the **lateral geniculate body**.
The **LGN** is the **thalamic visual relay to V1** — **conscious
vision**. The **pretectum** is the **pupillary and optokinetic
relay** — **reflexive**. **They are DIFFERENT STRUCTURES in
DIFFERENT functional systems.**

**Do not** assume the pretectum is the **Edinger-Westphal nucleus**.
The **EW nucleus** is a **CN III preganglionic parasympathetic
nucleus** — **downstream** of the pretectum. The **pretectum** is
**upstream** of EW. **They are DIFFERENT STRUCTURES** — the
**pretectum** is the **relay**; the **EW** is the **efferent
nucleus**.

**Do not** assume the pretectum is the **superior colliculus**. The
**superior colliculus** **drives saccades**; the **pretectum**
**drives the pupillary light reflex**. **Different structures in
different functional systems.**

**Do not** assume the pretectum is a **cranial nerve nucleus**.
The **pretectal nuclei** are **relay nuclei**; the **EW nucleus**
they project to **is** a CN nucleus. **The pretectum is upstream
of the CN nuclei.**

**Do not** resolve the pretectum as **DIENCEPHALON ONLY** — the
earlier leaves did, but the **on-disk tree** places it under
``midbrain/pretectum/``. **The tree is authoritative** — resolve
the pretectum under the midbrain path. **If a
``forebrain/diencephalon/pretectum/`` node also exists, the two
paths reach the same nuclei** — resolve by **one** path per
lookup.

**Do not** assume the consensual pupillary light reflex is produced
by **EW-EW coupling**. The **consensual reflex** is produced by the
**pretectal bilateral projection** to both EW nuclei. **The two
pretectal nuclei are NOT directly coupled** — each is an
**independent relay** whose **bilateral output** to the EW nuclei
is what makes the reflex **consensual**.

**Do not** attribute **conscious vision** to the pretectum. The
**LGN and visual cortex** mediate **conscious vision**; the
**pretectum** mediates **pupillary and optokinetic reflexes**.

**Do not** attribute **saccade generation** to the pretectum. The
**superior colliculus** and the **PPRF/riMLF** mediate **saccades**;
the **pretectum** mediates **pupillary and optokinetic reflexes**.

**Do not** import the **transmitter phenotypes** of the pretectal
nuclei into the midbrain structural layer. Those are
**``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the pretectum. **Relay
nuclei carry NO coupling warning** — same rule as motor nuclei,
premotor pools, sensor nuclei, and conduction pathways.

Iterating the pretectum's children (recommended consumer pattern)::

    import pkgutil
    import infrastructure.brainparts.midbrain.pretectum as pretectum_pkg

    PRETECTUM_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(pretectum_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("left", "right")
    #
    # Each side container holds the five pretectal nuclei:
    # ("olivary_pretectal_nucleus", "nucleus_of_the_optic_tract",
    #  "anterior_pretectal_nucleus", "posterior_pretectal_nucleus",
    #  "medial_pretectal_nucleus")

Reaching the superior colliculus (recommended consumer pattern —
NOTE the pretectum is ROSTRAL to the superior colliculus, and the
two are DIFFERENT functional systems)::

    # The superior colliculus is a TECTUM structure — the
    # visual/oculomotor orienting structure that drives SACCADES
    # via the tectobulbar tract to the CN III nuclei:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   brainparts.midbrain.tectum.right.superior_colliculus
    #
    # The superior colliculus DRIVES saccades; the pretectum DRIVES
    # the pupillary light reflex. DIFFERENT functional systems.

Reaching the Edinger-Westphal nucleus (recommended consumer pattern —
NOTE the EW nucleus is DOWNSTREAM of the pretectum)::

    # The Edinger-Westphal nucleus is the CN III PREGANGLIONIC
    # PARASYMPATHETIC nucleus — the EFFERENT limb of the pupillary
    # light reflex:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.edinger_westphal_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.edinger_westphal_nucleus
    #
    # The pretectum PROJECTS BILATERALLY to the EW nuclei on BOTH
    # sides — this is the mechanism of the CONSENSUAL pupillary
    # light reflex. The pretectum is UPSTREAM of the EW nucleus;
    # the EW nucleus is DOWNSTREAM.

Reaching the thalamus (recommended consumer pattern — NOTE the
pretectum is at the CAUDAL BORDER of the thalamus, not the
thalamus itself)::

    # The thalamus is the DIENCEPHALIC relay — the LGN (visual),
    # MGN (auditory), pulvinar (visual attention), VPL (somatosensory),
    # VL (motor), MD (prefrontal), intralaminar (arousal):
    #
    #   brainparts.forebrain.diencephalon.thalamus
    #
    # The pretectum is at the CAUDAL BORDER of the thalamus — it is
    # NOT the thalamus, and it is NOT the LGN (the thalamic visual
    # relay to V1).

Reaching the lateral geniculate body (recommended consumer pattern —
NOTE the LGN is the VISUAL PERCEPTION relay, the pretectum is the
PUPILLARY REFLEX relay)::

    # The lateral geniculate body (LGN) is the THALAMIC VISUAL
    # RELAY to V1 — CONSCIOUS VISION:
    #
    #   brainparts.forebrain.diencephalon.thalamus.lateral_geniculate_body
    #
    # The pretectum is the PUPILLARY REFLEX RELAY — REFLEXIVE. They
    # are DIFFERENT STRUCTURES in DIFFERENT functional systems.

Reaching the periaqueductal gray (recommended consumer pattern —
NOTE the PAG is a TEgmentum structure, and the anterior pretectal
nucleus projects to it)::

    # The periaqueductal gray (PAG) is a TEgmentum structure —
    # the pain-modulation and defensive-behavior region:
    #
    #   brainparts.midbrain.tegmentum.left.periaqueductal_gray
    #   brainparts.midbrain.tegmentum.right.periaqueductal_gray
    #
    # The ANTERIOR PRETECTAL NUCLEUS projects to the PAG — but the
    # PAG is NOT the pretectum. Different structures in different
    # functional systems (PAG: pain modulation / defensive behavior;
    # anterior pretectal: nociceptive relay).

Reaching the ciliary ganglion (recommended consumer pattern — the
PERIPHERAL postganglionic relay, DOWNSTREAM of the EW nucleus)::

    # The ciliary ganglion is PERIPHERAL — the POSTGANGLIONIC
    # parasympathetic relay from EW to the sphincter pupillae:
    #
    #   peripheral.ciliary_ganglion
    #
    # The ciliary ganglion is DOWNSTREAM of EW; EW is DOWNSTREAM of
    # the pretectum. The full arc: retina -> pretectum -> EW ->
    # ciliary ganglion -> sphincter pupillae.

Reaching the retina (recommended consumer pattern — the AFFERENT
origin of the pupillary light reflex)::

    # The retina is the AFFERENT origin of the pupillary light
    # reflex — the retinal ganglion cells project via the optic
    # nerve and optic tract to the PRETECTUM:
    #
    #   peripheral.retina
    #
    # The retina is UPSTREAM of the pretectum; the pretectum is the
    # first central relay of the pupillary light reflex.

Bilateral iteration (recommended consumer pattern — NOTE the
relay-nucleus rule and the PRETECTAL bilateral projection)::

    for side in ("left", "right"):
        for nucleus in (
            "olivary_pretectal_nucleus",
            "nucleus_of_the_optic_tract",
            "anterior_pretectal_nucleus",
            "posterior_pretectal_nucleus",
            "medial_pretectal_nucleus",
        ):
            path = (
                f"midbrain.pretectum.{side}.{nucleus}"
            )
            # resolve path through the memory/recall layer
            #
            # NOTE: the pretectal nuclei are RELAY nuclei — NO
            # coupling warning. The CONSENSUAL pupillary light
            # reflex is produced by the PRETECTAL BILATERAL
            # PROJECTION to the EW nuclei on BOTH sides — not by
            # intrinsic pretectal-to-pretectal coupling.

The Pupillary Light Reflex Arc — detail (not wired — consult
references)::

    # The pupillary light reflex arc — the pretectum is the FIRST
    # CENTRAL RELAY:
    #
    #   light -> retina -> optic nerve -> optic chiasm -> optic
    #   tract -> PRETECTUM (diencephalon-midbrain junction) —
    #   OLIVARY PRETECTAL NUCLEUS — BILATERAL projection to LEFT
    #   and RIGHT EW NUCLEI (midbrain) -> LEFT and RIGHT ciliary
    #   ganglia (peripheral) -> LEFT and RIGHT sphincter pupillae
    #   (peripheral) -> both pupils constrict
    #
    # The BILATERAL projection from the olivary pretectal nucleus
    # to BOTH EW nuclei is the mechanism of the CONSENSUAL reflex.
    # The two pretectal nuclei are NOT directly coupled — the
    # coordination is upstream, at the pretectal level.
    #
    # Do not attempt to resolve the retina, the EW nucleus, the
    # ciliary ganglion, or the sphincter pupillae as sub-paths of
    # the pretectum — they are DIFFERENT structures at DIFFERENT
    # levels of the arc.

Clinical-pattern detail (not wired — consult references)::

    # The pretectum is the FIRST CENTRAL RELAY of the pupillary
    # light reflex. The CLINICAL PATTERNS of the related lesions
    # are DISTINCT:
    #
    #   LEFT pretectal lesion     -> LEFT light reflex lost, LEFT
    #                                consensual PRESERVED (via the
    #                                RIGHT pretectum -> both EWs);
    #                                LIGHT-NEAR DISSOCIATION (near
    #                                response preserved because it
    #                                uses a cortical -> EW pathway
    #                                that BYPASSES the pretectum)
    #   Parinaud syndrome         -> dorsal midbrain syndrome:
    #     (dorsal midbrain lesion)      upgaze palsy, convergence-
    #                                   retraction nystagmus,
    #                                   LIGHT-NEAR DISSOCIATION,
    #                                   eyelid retraction (Collier
    #                                   sign) — the pretectum is ONE
    #                                   COMPONENT of this syndrome
    #   Argyll Robertson pupil    -> DEBATED — pretectal OR
    #     (tabes dorsalis, MS,          postganglionic OR ciliary
    #      diabetes)                    ganglion involvement; NOT a
    #                                   pure pretectal lesion
    #   Optokinetic nystagmus     -> nucleus of the optic tract
    #     (OKN) deficits                involvement
    #   Nociception / defensive   -> anterior pretectal nucleus
    #     behaviors                     involvement (less clinical)
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # PRETECTAL NUCLEI (or to the pretectum as a whole, for the
    # light-near dissociation).

References
----------
*   **Canonical pretectum anatomy:** Büttner-Ennever, J.A. (2006).
    *Neuroanatomy of the Oculomotor System*. (The pretectum — its
    location at the diencephalon-midbrain junction, its nuclei
    (olivary pretectal, nucleus of the optic tract, anterior,
    posterior, medial), and its projections to the EW nucleus.)
*   **Pretectum — comparative and Paxinos-style diencephalon
    placement:** Paxinos, G., Franklin, K.B.J. (2019). *Paxinos
    and Franklin's the Mouse Brain in Stereotaxic Coordinates*,
    5th ed. (The pretectum as part of the diencephalon / thalamic
    region — a common modern placement.)
*   **Pretectum — older brainstem placement:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (The pretectal area as a region at the diencephalon-midbrain
    junction — a common older placement.)
*   **The pupillary light reflex — modern review:** Wilhelm, H.
    (2011). "Disorders of the pupil." *Handbook of Clinical
    Neurology* 102:427–466. (The pupillary light reflex arc —
    retina → optic nerve → pretectum → EW → ciliary ganglion →
    sphincter pupillae; the clinical syndromes.)
*   **The pretectum and the pupillary light reflex:** Gamlin,
    P.D.R. (2002). "The pupillary light reflex and its brainstem
    pathways." In *Neuro-Ophthalmology* (Miller et al., eds.).
    (The olivary pretectal nucleus as the principal pupillary
    light reflex relay; its bilateral projection to both EW
    nuclei.)
*   **Olivary pretectal nucleus:** Klooster, J., Vrensen,
    G.F.J.M. (1997). "The pretectal complex of the rabbit: a
    cytoarchitectonic and hodological study." *Neuroscience*
    76:1233–1254. (The pretectal nuclei — their cytoarchitecture
    and projections; the olivary pretectal nucleus as the
    pupillary relay.)
*   **Nucleus of the optic tract and optokinetic nystagmus:**
    Mustari, M.J., Fuchs, A.F. (1990). "Response properties of
    neurons in the nucleus of the optic tract in the alert
    monkey." *Journal of Neurophysiology* 63:234–246. (The
    nucleus of the optic tract — direction-selective cells
    implicated in optokinetic nystagmus.)
*   **Anterior pretectal nucleus and nociception:** Rees, H.,
    Roberts, M.H.T. (1993). "The anterior pretectal nucleus: a
    proposed role in somatosensory nociceptive processing."
    *Neuroscience* 53:943–957. (The anterior pretectal nucleus as
    a nociceptive and somatosensory relay; its projections to the
    PAG and intralaminar thalamus.)
*   **Parinaud syndrome:** Parinaud, H. (1883). "Paralysie des
    mouvements associés des yeux." *Annales d'Oculistique* 90:1–21.
    (Parinaud syndrome — the dorsal midbrain syndrome; the
    pretectum is one component of the light-near dissociation.)
*   **Argyll Robertson pupil:** Thompson, H.S., Pilley, S.F.J.
    (1998). "Unequal pupils. A flow chart for sorting out the
    anisocorias." *Survey of Ophthalmology* 43:263–269. (The
    light-near dissociation of the Argyll Robertson pupil — the
    historical lesion debate, and the modern view that it is not
    a pure pretectal lesion.)
*   **Light-near dissociation — modern review:** Cox, T.A. (2003).
    "Pupillary light reflex and near response." *Ophthalmology
    Clinics of North America* 16:1–9. (The dissociated light and
    near pathways to the EW nucleus; the pretectal lesion as the
    most common cause of light-near dissociation.)
*   **Edinger-Westphal nucleus (downstream — CN IIIp):** Kozicz,
    T., Bittencourt, J.C., May, P.J., Reiner, A., Gamlin, P.D.R.,
    Palkovits, M., Horn, A.K.E. (2011). "The Edinger-Westphal
    nucleus: a historical, structural, and functional appraisal
    of the urocortin-1 containing centrally projecting neuron
    population, and its comparison to the parasympathetic and
    preganglionic neurons of the oculomotor nucleus." *Brain
    Structure and Function* 216:1–19. (The EWpg / EWcp
    distinction; the EWpg is the preganglionic parasympathetic
    nucleus that the pretectum projects to.)
*   **Superior colliculus (contrast — tectum):** Sparks, D.L.
    (2002). "The brainstem control of saccadic eye movements."
    *Nature Reviews Neuroscience* 3:952–964. (The superior
    colliculus — saccade generation — contrast with the pretectum
    (pupillary and optokinetic reflexes).)
*   **Lateral geniculate body (contrast — thalamic visual relay):**
    Casagrande, V.A., Xu, X. (2004). "The lateral geniculate
    nucleus." In *The Visual Neurosciences* (Chalupa & Werner,
    eds.). (The LGN as the thalamic visual relay to V1 —
    contrast with the pretectum (pupillary and optokinetic
    reflexes).)
*   **Periaqueductal gray (contrast — tegmentum, downstream of the
    anterior pretectal nucleus):** Behbehani, M.M. (1995).
    "Functional characteristics of the midbrain periaqueductal
    gray." *Progress in Neurobiology* 46:575–605. (The PAG as the
    pain-modulation and defensive-behavior structure — a
    downstream target of the anterior pretectal nucleus.)
*   **SLEA (contrast — the pretectum is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the pretectum.)
*   NeuroNames — Pretectal region; FMA — Pretectal region.
"""