"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.white_matter
==========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── white_matter   <-- THIS MODULE (CONTAINER)

**Primary synonym:** White matter (right); right-hemisphere white
matter; cerebral white matter (right); **the white-matter container
of the right cerebral hemisphere**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container module** — the **white-matter compartment** of the
**right cerebral hemisphere**, containing **ten structural
children**:

*   ``centrum_semiovale`` — the **white-matter mass above the
    lateral ventricles**.
*   ``cingulum`` — the **cingulate-gyrus association bundle**.
*   ``corona_radiata`` — the **projection-fiber fan**.
*   ``external_capsule`` — the **capsule fibers lateral to the
    putamen**.
*   ``extreme_capsule`` — the **capsule fibers lateral to the
    claustrum**.
*   ``fasciculus_rectus`` — a **small white-matter bundle**.
*   ``fornix`` — the **hippocampal output tract**.
*   ``internal_capsule`` — the **deep, compact projection-fiber
    bundle**.
*   ``mammillothalamic_tract`` — the **mammillary-body →
    anterior-thalamic projection**.
*   ``medial_forebrain_bundle`` — a **brainstem-forebrain
    bundle**.

**Part of:** The **``.../right/`` (cerebral hemisphere) container**
— the **white-matter compartment** of the right cerebral hemisphere.
The **white_matter** container is the **parent of the ten
white-matter leaves** — **all of which are white matter**, **none of
which is grey matter**.
**Structural parent:** ``.../right/`` → **direct child** of the
cerebral hemisphere container.
**Structural children:** **YES — this is a CONTAINER module, not a
leaf.** Its **ten structural children** are:

*   ``.../white_matter/centrum_semiovale/`` — a **leaf**.
*   ``.../white_matter/cingulum/`` — a **leaf**.
*   ``.../white_matter/corona_radiata/`` — a **leaf**.
*   ``.../white_matter/external_capsule/`` — a **leaf**.
*   ``.../white_matter/extreme_capsule/`` — a **leaf**.
*   ``.../white_matter/fasciculus_rectus/`` — a **leaf**.
*   ``.../white_matter/fornix/`` — a **leaf**.
*   ``.../white_matter/internal_capsule/`` — a **leaf**.
*   ``.../white_matter/mammillothalamic_tract/`` — a **leaf**.
*   ``.../white_matter/medial_forebrain_bundle/`` — a **leaf**.

Consumers **may** import these children; the white_matter container
is the **structural parent** of the white-matter leaves, not a
leaf.
**Boundary status (CONTAINER — NOT a leaf and NOT a single tract):**
**Boundary case — the white_matter is a CONTAINER module with TEN
structural children, not a leaf and not a single tract.** The
**ten children** are **separate structural leaves** — consumers
must **not** assume the white_matter is a single tract (e.g., "the
white matter = the corpus callosum" or "the white matter = the
internal capsule"), and must **not** assume the white-matter leaves
are prose under a container. They are **wired children** with
their own modules.
**Boundary status (WHITE MATTER — NOT a grey-matter container):**
**Boundary case — the white_matter is WHITE MATTER, NOT a
grey-matter container.** The **white_matter** (here) is the
**compartment of myelinated axons** in the right cerebral
hemisphere. The **grey-matter structures** — the **cortex**
(``.../right/cortex/``), the **rhinencephalon**
(``.../right/rhinencephalon/``), and the **subcortical** structures
(``.../right/subcortical/``) — are **grey matter** and are wired
under their **own containers**. **They are DIFFERENT
COMPARTMENTS** — the **white_matter** is the **white-matter
compartment**; the **cortex**, **rhinencephalon**, and
**subcortical** are the **grey-matter compartments**. Consumers
must **not** conflate the white_matter container with any
grey-matter container.
**Boundary status (NOT the cortex — the cortex is the GREY-MATTER
sibling):** **Boundary case — the white_matter is NOT the cortex;
the cortex is the GREY-MATTER sibling.** The **cortex**
(``.../right/cortex/``) is the **grey-matter sheet** that **caps**
the hemisphere — **superficial** to the white matter. The
**white_matter** (here) is the **white-matter compartment**
**deep** to the cortex. **They are SIBLINGS under ``.../right/``,
and they are DIFFERENT COMPARTMENTS** — the **cortex** is **grey
matter**; the **white_matter** is **white matter**. Consumers
must **not** conflate the white_matter container with the cortex.
**Boundary status (NOT the rhinencephalon — the rhinencephalon is
the OLFACTORY-LOBE sibling):** **Boundary case — the white_matter
is NOT the rhinencephalon; the rhinencephalon is the
OLFACTORY-LOBE sibling.** The **rhinencephalon**
(``.../right/rhinencephalon/``) is the **cortical olfactory lobe**
— the olfactory bulb, olfactory tract, piriform cortex,
periamygdaloid cortex, anterior olfactory nucleus, and uncus. The
**white_matter** (here) is the **white-matter compartment**.
**They are SIBLINGS under ``.../right/``, and they are DIFFERENT
COMPARTMENTS** — the **rhinencephalon** is a **grey-matter /
olfactory structure**; the **white_matter** is **white matter**.
Consumers must **not** conflate the white_matter container with
the rhinencephalon.
**Boundary status (NOT the subcortical container — the subcortical
container holds the GREY-MATTER nuclei):** **Boundary case — the
white_matter is NOT the subcortical container; the subcortical
container holds the GREY-MATTER nuclei.** The **subcortical**
container (``.../right/subcortical/``) holds the **grey-matter
nuclei** — the **basal forebrain**, the **basal ganglia**, the
**extended amygdala**, the **medial temporal lobe** (amygdala and
hippocampus), and the **claustrum**. The **white_matter** (here)
is the **white-matter compartment**. **They are SIBLINGS under
``.../right/``, and they are DIFFERENT COMPARTMENTS** — the
**subcortical** container is the **grey-matter nuclei**; the
**white_matter** container is the **white-matter compartment**.
Consumers must **not** conflate the white_matter container with
the subcortical container.
**Boundary status (NOT the commissures — the corpus callosum and
the anterior commissure are wired under ``commissures/``):**
**Boundary case — the white_matter is NOT the commissures; the
corpus callosum and the anterior commissure are wired under
``.../right/commissures/``.** The **commissures** container
(``.../right/commissures/``) holds the **corpus callosum** and the
**anterior commissure** — the **midline white-matter commissures**
that connect the two hemispheres. The **white_matter** (here) is
the **ipsilateral white-matter compartment** of the right cerebral
hemisphere — the **commissural fibers** that **cross** the midline
are wired under ``commissures/``; the **ipsilateral white-matter
leaves** that the white_matter container holds are wired under
``white_matter/``. **They are SIBLINGS under ``.../right/``, and
they are DIFFERENT COMPARTMENTS** — the **commissures** container
is the **commissural white matter**; the **white_matter** container
is the **ipsilateral white matter**. Consumers must **not**
conflate the white_matter container with the commissures
container.
**Boundary status (NOT the lateral ventricles — the lateral
ventricles are the CSF spaces):** **Boundary case — the
white_matter is NOT the lateral ventricles; the lateral ventricles
are the CSF spaces.** The **lateral ventricles**
(``.../right/lateral_ventricles/``) are the **CSF-filled spaces**
**inside** the white-matter compartment. The **white_matter**
(here) is the **white-matter compartment** **around** the
ventricles. **They are SIBLINGS under ``.../right/``, and they are
DIFFERENT STRUCTURES** — the **lateral ventricles** are **CSF
spaces**; the **white_matter** is **white matter**. Consumers
must **not** conflate the white_matter container with the lateral
ventricles.
**Boundary status (NOT a single uniform compartment — MULTIPLE
leaves, MULTIPLE structures):** **Boundary case — the white_matter
is a HETEROGENEOUS compartment with MULTIPLE leaves and MULTIPLE
structures, not a single uniform compartment.** The **ten
children** are **functionally distinct** — the
**centrum_semiovale** is a **region of passage**; the **cingulum**
is an **association bundle**; the **corona_radiata** is a
**projection-fiber fan**; the **external_capsule** and
**extreme_capsule** are **capsular white-matter regions**; the
**fasciculus_rectus** is a **small bundle**; the **fornix** is a
**hippocampal output tract**; the **internal_capsule** is a
**deep, compact projection-fiber bundle**; the
**mammillothalamic_tract** is a **diencephalic projection**; and
the **medial_forebrain_bundle** is a **brainstem-forebrain
bundle**. **Each leaf is functionally distinct** — the tree wires
them as **separate structural children** of the white_matter
container, **not** as a single uniform white-matter mass.
Consumers must **not** treat the white_matter container as a
single uniform structure — it is a **compartment** of **ten
distinct white-matter structures**.
**Boundary status (SLEA-FREE — the white_matter is NOT an
extended-amygdala component):** **Boundary case — the white_matter
is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **white_matter** is a **white-matter compartment**
— it is **NOT** an extended-amygdala component, and it carries
**NO SLEA warning**. Consumers must **not** import the SLEA
warning into the white_matter — it is **SLEA-free**.
**Boundary status (NOT the grey-matter structures whose fibers pass
through it — those are the CORTEX, BASAL GANGLIA, and THALAMUS):**
**Boundary case — the white_matter is NOT the grey-matter
structures whose fibers pass through it.** The **cortex**
(``.../right/cortex/``), the **basal ganglia**
(``.../right/subcortical/basal_ganglia/``), and the **thalamus**
(``.../right/subcortical/diencephalon/thalamus/``) are the
**grey-matter structures** whose **axons** pass through the
white-matter compartment. The **white_matter** (here) is the
**compartment of myelinated axons**. **They are DIFFERENT
COMPARTMENTS** — the **cortex**, **basal ganglia**, and
**thalamus** are **grey matter**; the **white_matter** is
**white matter** that **carries their fibers**. Consumers must
**not** conflate the white_matter container with any of those
grey-matter structures.
**Boundary status (NOT the cerebral hemisphere container — the
white_matter is a CHILD of the ``.../right/`` container):**
**Boundary case — the white_matter is a CHILD of the ``.../right/``
container, not the container itself.** The **``.../right/``**
container contains the **cortex**, the **rhinencephalon**, the
**subcortical** structures, the **white_matter**, the
**commissures**, and the **lateral_ventricles** — the
**white_matter** is **one** of those six children. Consumers must
**not** conflate the white_matter container with the cerebral
hemisphere container.

Overview
--------
The white_matter container is the **white-matter compartment** of
the **right cerebral hemisphere** — the **parent of the ten
white-matter leaves** (centrum semiovale, cingulum, corona radiata,
external capsule, extreme capsule, fasciculus rectus, fornix,
internal capsule, mammillothalamic tract, medial forebrain bundle).
It is a **container** module under the ``.../right/`` container, the
**sibling of the cortex, the rhinencephalon, the subcortical
structures, the commissures, and the lateral ventricles**, and the
**white-matter substrate** of the **long-range connectivity** of
the right cerebral hemisphere.

**The white_matter is a CONTAINER, not a leaf.** Its **ten
structural children** are **wired modules**, not prose. Consumers
may import them.

**The white_matter is WHITE MATTER, NOT a grey-matter container.**
It is the **compartment of myelinated axons** in the right cerebral
hemisphere. The **grey-matter structures** — the **cortex**, the
**rhinencephalon**, and the **subcortical** structures — are
**grey matter** and are wired under their own containers.

**The white_matter is NOT the cortex, the rhinencephalon, or the
subcortical container.** Those are the **grey-matter siblings**
under ``.../right/``. **They are SIBLINGS under ``.../right/``, and
they are DIFFERENT COMPARTMENTS.**

**The white_matter is NOT the commissures.** The **corpus callosum**
and the **anterior commissure** are wired under
``.../right/commissures/``. The **white_matter** is the
**ipsilateral white-matter compartment** of the right cerebral
hemisphere; the **commissural white matter** is wired under
``commissures/``.

**The white_matter is NOT the lateral ventricles.** The **lateral
ventricles** are the **CSF-filled spaces** **inside** the
white-matter compartment. The **white_matter** is the
**white-matter compartment** **around** the ventricles.

**The white_matter is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The white_matter is the WHITE-MATTER COMPARTMENT, not the
grey-matter structures whose fibers pass through it.** The
**cortex**, the **basal ganglia**, and the **thalamus** are the
**grey-matter structures** whose **axons** pass through the
white-matter compartment. **They are DIFFERENT COMPARTMENTS.**

**The white_matter is a paired structure.** Each hemisphere has its
own white-matter container — the **left** white matter
(``.../left/white_matter/``) and the **right** white matter (here).
The two sides are **bilaterally symmetric** — the **gross anatomy**
of the white matter is **symmetric**. There is **no functional
lateralization** of the white-matter compartment per se — the
**functional lateralization** belongs to the **grey-matter
structures** whose fibers pass through it (see *Lateralization
Notes*).

Structural Children (wired — NOT prose)
---------------------------------------
This is a **container** module — its children are **wired
modules**, not prose:

*   ``.../white_matter/centrum_semiovale/`` — the **white-matter
    mass above the lateral ventricles**. A **leaf**. A **region
    of passage** — **contains** the corona radiata, the
    association fibers, and the callosal radiations as they pass
    through.

*   ``.../white_matter/cingulum/`` — the **cingulate-gyrus
    association bundle**. A **leaf**. An **association bundle**.

*   ``.../white_matter/corona_radiata/`` — the
    **projection-fiber fan**. A **leaf**. The **projection-fiber
    fan** that **radiates** from the internal capsule up to the
    cortex.

*   ``.../white_matter/external_capsule/`` — the **capsule fibers
    lateral to the putamen**. A **leaf**. A **capsular
    white-matter region**.

*   ``.../white_matter/extreme_capsule/`` — the **capsule fibers
    lateral to the claustrum**. A **leaf**. A **capsular
    white-matter region**.

*   ``.../white_matter/fasciculus_rectus/`` — a **small white-matter
    bundle**. A **leaf**. A **small bundle**.

*   ``.../white_matter/fornix/`` — the **hippocampal output
    tract**. A **leaf**. The **major output tract** of the
    hippocampus — carries the hippocampal output (via the
    subiculum) to the mammillary bodies and the anterior thalamic
    nuclei.

*   ``.../white_matter/internal_capsule/`` — the **deep, compact
    projection-fiber bundle**. A **leaf**. Passes **between** the
    basal ganglia, the thalamus, and the caudate nucleus.

*   ``.../white_matter/mammillothalamic_tract/`` — the
    **mammillary-body → anterior-thalamic projection**. A
    **leaf**. The **diencephalic projection** from the mammillary
    bodies to the anterior thalamic nuclei.

*   ``.../white_matter/medial_forebrain_bundle/`` — a
    **brainstem-forebrain bundle**. A **leaf**. A
    **brainstem-forebrain bundle** carrying ascending and
    descending fibers.

**These children are wired, not prose.** The tree wires them as
**structural children** of the white_matter container — they are
**not** prose under a container. Consumers that need
**tract-level** or **region-level** resolution should import them
directly.

The White Matter / Cortex Boundary
----------------------------------
This is the **white matter vs. grey matter** sibling boundary:

*   **White_matter** (this module) — the **white-matter
    compartment** of the right cerebral hemisphere.

*   **Cortex** (``.../right/cortex/``) — the **grey-matter sheet**
    that **caps** the hemisphere.

**They are SIBLINGS under ``.../right/``, and they are DIFFERENT
COMPARTMENTS** — the **cortex** is **grey matter**; the
**white_matter** is **white matter**. Consumers must **not**
conflate the white_matter container with the cortex.

The White Matter / Rhinencephalon Boundary
------------------------------------------
This is the **white matter vs. olfactory-lobe** sibling boundary:

*   **White_matter** (this module) — the **white-matter
    compartment**.

*   **Rhinencephalon** (``.../right/rhinencephalon/``) — the
    **cortical olfactory lobe**.

**They are SIBLINGS under ``.../right/``, and they are DIFFERENT
COMPARTMENTS** — the **rhinencephalon** is a **grey-matter /
olfactory structure**; the **white_matter** is **white matter**.
Consumers must **not** conflate the white_matter container with
the rhinencephalon.

The White Matter / Subcortical Boundary
---------------------------------------
This is the **white matter vs. grey-matter-nuclei** sibling
boundary:

*   **White_matter** (this module) — the **white-matter
    compartment**.

*   **Subcortical** (``.../right/subcortical/``) — the
    **grey-matter nuclei** (basal forebrain, basal ganglia,
    extended amygdala, medial temporal lobe, claustrum).

**They are SIBLINGS under ``.../right/``, and they are DIFFERENT
COMPARTMENTS** — the **subcortical** container is the
**grey-matter nuclei**; the **white_matter** container is the
**white-matter compartment**. Consumers must **not** conflate the
white_matter container with the subcortical container.

The White Matter / Commissures Boundary
---------------------------------------
This is the **ipsilateral white matter vs. commissural white
matter** sibling boundary:

*   **White_matter** (this module) — the **ipsilateral
    white-matter compartment** of the right cerebral hemisphere.

*   **Commissures** (``.../right/commissures/``) — the **commissural
    white matter** (corpus callosum, anterior commissure) — the
    **midline fibers** that **cross** to the left hemisphere.

**They are SIBLINGS under ``.../right/``, and they are DIFFERENT
COMPARTMENTS** — the **commissures** container is the
**commissural white matter**; the **white_matter** container is
the **ipsilateral white matter**. Consumers must **not** conflate
the white_matter container with the commissures container.

The White Matter / Lateral Ventricles Boundary
----------------------------------------------
This is the **white matter vs. CSF space** sibling boundary:

*   **White_matter** (this module) — the **white-matter
    compartment**.

*   **Lateral ventricles** (``.../right/lateral_ventricles/``) — the
    **CSF-filled spaces** **inside** the white-matter compartment.

**They are SIBLINGS under ``.../right/``, and they are DIFFERENT
STRUCTURES** — the **lateral ventricles** are **CSF spaces**; the
**white_matter** is **white matter**. Consumers must **not**
conflate the white_matter container with the lateral ventricles.

The White Matter / Cerebral Hemisphere Boundary
-----------------------------------------------
This is the **child vs. container** boundary:

*   **White_matter** (this module) — a **child** of the
    ``.../right/`` container.

*   **``.../right/``** — the **cerebral hemisphere container** that
    contains the **cortex**, the **rhinencephalon**, the
    **subcortical** structures, the **white_matter**, the
    **commissures**, and the **lateral_ventricles**.

**The white_matter is ONE of the six children of the cerebral
hemisphere container.** Consumers must **not** conflate the
white_matter container with the cerebral hemisphere container.

The White Matter / SLEA Boundary
--------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **White_matter** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The white_matter is NOT part of the SLEA continuum.** It is a
**white-matter compartment**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the
white_matter.

Function in the Human Brain
---------------------------
The white-matter compartment's functions are **long-range
connectivity** — **projection**, **association**, and
**commissural** conduction — **NOT a grey-matter function**:

*   **Projection-Fiber Conduction (Corona Radiata, Internal
    Capsule):** The **white_matter** compartment carries the
    **projection fibers** — the **corticospinal**,
    **corticobulbar**, and **corticopontine** descending fibers,
    and the **thalamocortical** ascending fibers — through the
    **corona radiata** and the **internal capsule**. This is the
    **projection** substrate of the white-matter compartment.

*   **Association-Fiber Conduction (Cingulum, Superior Longitudinal
    Fasciculus via the Centrum Semiovale):** The **white_matter**
    compartment carries the **association fibers** — the
    **intrahemispheric** bundles that connect **cortical areas**
    within the same hemisphere. This is the **association**
    substrate of the white-matter compartment.

*   **Commissural-Fiber Conduction (Callosal Radiations via the
    Centrum Semiovale):** The **white_matter** compartment carries
    the **commissural fibers** — the **callosal radiations** that
    **cross** the **corpus callosum** and **radiate** through the
    **centrum semiovale** to reach the **cortex**. This is the
    **commissural** substrate of the white-matter compartment.

*   **Limbic Output (Fornix, Mammillothalamic Tract):** The
    **white_matter** compartment carries the **limbic output
    tracts** — the **fornix** (the **hippocampal output** to the
    mammillary bodies and the anterior thalamic nuclei) and the
    **mammillothalamic tract** (the **mammillary-body → anterior
    thalamic** projection). This is the **limbic-output**
    substrate of the white-matter compartment.

*   **Brainstem-Forebrain Connectivity (Medial Forebrain
    Bundle):** The **white_matter** compartment carries the
    **medial forebrain bundle** — a **brainstem-forebrain
    bundle** carrying **ascending** (monoaminergic) and
    **descending** fibers. This is the **brainstem-forebrain**
    substrate of the white-matter compartment.

*   **NOT a neural processor in the classical sense.** The
    **white_matter** is a **white-matter compartment** — it
    **conducts** the **projection**, **association**,
    **commissural**, **limbic-output**, and **brainstem-forebrain**
    fibers, but it does **not** **process** information (that
    happens in the **grey-matter structures** — the cortex, the
    basal ganglia, the thalamus, and the amygdala/hippocampus).
    The **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the white_matter container is the
**white-matter compartment** of the **right cerebral hemisphere** —
the **parent of the ten white-matter leaves** that anchor the
**projection**, **association**, **commissural**,
**limbic-output**, and **brainstem-forebrain** connectivity of the
hemisphere. It is **SLEA-free**, **white-matter**, and **NOT a
grey-matter container** — the **grey-matter structures** are the
**cortex**, the **rhinencephalon**, the **subcortical** nuclei,
and the **amygdala/hippocampus** whose axons pass through it.

Associated Disorders
--------------------
The white-matter compartment has **no named "white-matter syndrome"**
in the narrow sense, but its clinical associations are
**well-documented** — primarily as a **white-matter imaging target**
and as a **white-matter disease category**:

*   **Leukoaraiosis and Small-Vessel Disease:** The **white-matter
    compartment** — especially the **centrum semiovale** and the
    **periventricular white matter** — is the **principal site**
    of **leukoaraiosis** — the **T2/FLAIR white-matter
    hyperintensities** that are the **radiological hallmark** of
    **small-vessel disease**, **aging**, and **vascular
    dementia**. The **white-matter** compartment is the
    **white-matter substrate** of **leukoaraiosis**.

*   **Multiple Sclerosis (White-Matter Plaques):** The
    **white-matter compartment** — especially the **centrum
    semiovale**, the **periventricular white matter**, and the
    **internal capsule** — is the **principal site** of **MS
    plaques** — the **demyelinating lesions** that are the
    **radiological hallmark** of **multiple sclerosis**. The
    **white-matter** compartment is the **white-matter substrate**
    of **MS lesions**.

*   **Leukodystrophies (White-Matter Genetic Diseases):** The
    **white-matter compartment** is the **principal site** of
    the **leukodystrophies** — a group of **genetic
    white-matter diseases** (e.g., **metachromatic
    leukodystrophy**, **adrenoleukodystrophy**, **Krabbe
    disease**) in which the **white-matter** compartment is
    **dysmyelinated** or **demyelinated**.

*   **Cerebral Amyloid Angiopathy (Centrum Semiovale Perivascular
    Spaces):** The **white-matter compartment** — especially the
    **centrum semiovale** — is a **principal site** of
    **enlarged perivascular spaces** — the **cribriform
    appearance** on MRI that is a **radiological marker** of
    **cerebral amyloid angiopathy** (CAA) and of **small-vessel
    disease**.

*   **Glioblastoma and White-Matter Tumors:** The **white-matter
    compartment** is a **common site** of **glioblastoma** and
    other **white-matter tumors** — the **infiltrative** tumor
    cells **spread** along the white-matter tracts. The
    **white-matter** compartment is the **white-matter substrate**
    of **tumor infiltration**.

*   **Stroke (White-Matter Stroke):** The **white-matter
    compartment** is a **common site** of **ischemic stroke** —
    the **lacunar infarcts** (small-vessel strokes in the
    **internal capsule**, the **corona radiata**, and the
    **centrum semiovale**) are **white-matter strokes**. The
    **white-matter** compartment is the **white-matter substrate**
    of **lacunar stroke**.

*   **No Named "White-Matter Syndrome":** The **white-matter
    compartment** is a **white-matter category**, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **direct** as a **white-matter
    imaging target** and a **white-matter disease category**
    (leukoaraiosis, MS, leukodystrophies, CAA, tumors, stroke).

**What is NOT here:** The **white-matter compartment** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as a **white-matter imaging target** and a
**white-matter disease category**.

Lateralization Notes
--------------------
This is the **right** white_matter container. The **white-matter
compartment** is **bilaterally symmetric** — and it carries **NO
warning**:

*   **Bilateral White-Matter Anatomy:** Each hemisphere has its own
    white-matter compartment. The two sides are **grossly
    symmetric** — the white_matter is a **white-matter
    compartment**, and its **gross anatomy** is **symmetric**.
    There is **no functional lateralization** of the white-matter
    compartment per se.

*   **NO Functional Lateralization of the White-Matter Compartment:**
    The **functional lateralization** belongs to the
    **grey-matter structures** whose fibers pass through the
    white-matter compartment (e.g., the **left-hemisphere
    language areas**, the **right-hemisphere spatial-attention
    areas**) — **not** to the white-matter compartment itself.
    Consumers must **not** assume the white-matter compartment
    carries a **functional lateralization** of its own.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The
    white_matter is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the white_matter.

*   **NO Amygdala-Lateralization Warning of their own (the
    white_matter is a WHITE-MATTER COMPARTMENT, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **white_matter** is a
    **white-matter compartment** — consumers must **not** conflate
    it with the **whole amygdala** or with the **central
    nucleus**.

**A consumer that assumes "left white matter = right white matter"
will be structurally correct** — the two sides are **symmetric**
(the white_matter is a **white-matter compartment**, and its
**gross anatomy** is **symmetric**). The **white_matter** is a
**strict-mirror pair with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    the ten white-matter leaves (the children are imported by
    consumers, not by the container), and it does **not** import
    from ``.../right/cortex/``,
    ``.../right/rhinencephalon/``,
    ``.../right/subcortical/``, ``.../right/commissures/``,
    ``.../right/lateral_ventricles/``,
    ``.../right/subcortical/basal_ganglia/``,
    ``.../right/subcortical/diencephalon/thalamus/``, or any other
    container. The white_matter's relationships to the cortex, the
    rhinencephalon, the subcortical structures, the commissures,
    the lateral ventricles, and the grey-matter structures whose
    fibers pass through the white-matter compartment are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **CONTAINER module — children EXIST.** The **ten structural
    children** — ``centrum_semiovale``, ``cingulum``,
    ``corona_radiata``, ``external_capsule``, ``extreme_capsule``,
    ``fasciculus_rectus``, ``fornix``, ``internal_capsule``,
    ``mammillothalamic_tract``, ``medial_forebrain_bundle`` — are
    **wired modules**, not prose. Consumers **may** import them.
    The white_matter is **not** a leaf.
*   **NOT a leaf — do not claim leaf status.** The white_matter has
    **ten structural children**; consumers must **not** assume it
    is a leaf and must **not** assume the ten white-matter
    structures are prose.
*   **NOT a single tract.** The white_matter is **not** "the
    corpus callosum", **not** "the internal capsule", and **not**
    any **one** of its children — it is the **container** of all
    ten children.
*   **WHITE MATTER — NOT a grey-matter container.** The
    **white_matter** is **white matter**; the **cortex**, the
    **rhinencephalon**, and the **subcortical** structures are
    **grey matter**. Consumers must **not** conflate the
    white_matter container with any grey-matter container.
*   **NOT the cortex — the cortex is the GREY-MATTER sibling.**
*   **NOT the rhinencephalon — the rhinencephalon is the
    OLFACTORY-LOBE sibling.**
*   **NOT the subcortical container — the subcortical container
    holds the GREY-MATTER nuclei.**
*   **NOT the commissures — the corpus callosum and the anterior
    commissure are wired under ``commissures/``.** The white_matter
    is the **ipsilateral white matter**; the commissural white
    matter is the **commissures**.
*   **NOT the lateral ventricles — the lateral ventricles are CSF
    spaces.**
*   **NOT the cerebral hemisphere container — the white_matter is a
    CHILD of the ``.../right/`` container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    white_matter is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; the **white_matter**
    is a **white-matter compartment**.
*   **NOT a single uniform compartment — MULTIPLE leaves, MULTIPLE
    structures.** The **ten children** are **functionally
    distinct** — consumers must **not** treat the white_matter
    container as a single uniform structure.
*   **No ``AREA_PATHS`` hop.** The white_matter is a local
    container under ``.../right/``, not a cross-listed structure.
*   **No nested cross-listing.** The white_matter has no nested
    dual-framing module. It is a single container.
*   **Structural parity with left white_matter — strict mirror
    with NO warning.** Left and right white-matter containers are
    **structurally identical** — same **container** status, same
    **ten structural children**, same **white-matter-compartment**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right import white_matter

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.white_matter"
    )

**Do not** assume the white_matter is a **leaf**. It has **ten
structural children** — ``centrum_semiovale``, ``cingulum``,
``corona_radiata``, ``external_capsule``, ``extreme_capsule``,
``fasciculus_rectus``, ``fornix``, ``internal_capsule``,
``mammillothalamic_tract``, ``medial_forebrain_bundle``.

**Do not** assume the white_matter is the **cortex**, the
**rhinencephalon**, or the **subcortical** container. Those are the
**grey-matter siblings** under ``.../right/``.

**Do not** assume the white_matter is the **commissures**. The
**corpus callosum** and the **anterior commissure** are wired
under ``.../right/commissures/``. The white_matter is the
**ipsilateral white matter**.

**Do not** assume the white_matter is the **lateral ventricles**.
The **lateral ventricles** are **CSF spaces**.

**Do not** assume the white_matter is the **cerebral hemisphere
container**. The **``.../right/``** container contains the
white_matter and the other five children — the white_matter is
**one** of those six children.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the white_matter. **The
white_matter is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the white_matter's structural children (recommended
consumer pattern — NOTE these are WIRED, not prose)::

    WHITE_MATTER_CHILDREN = (
        "centrum_semiovale",        # leaf
        "cingulum",                 # leaf
        "corona_radiata",           # leaf
        "external_capsule",         # leaf
        "extreme_capsule",          # leaf
        "fasciculus_rectus",        # leaf
        "fornix",                   # leaf
        "internal_capsule",         # leaf
        "mammillothalamic_tract",   # leaf
        "medial_forebrain_bundle",  # leaf
    )

Reaching the cortex (recommended consumer pattern — the grey-matter
sibling)::

    # The cortex is the GREY-MATTER sibling under ``.../right/`` —
    # the grey-matter sheet that caps the hemisphere:
    #
    #   right.cortex
    #
    # The cortex is grey matter; the white_matter is white matter.

Reaching the rhinencephalon (recommended consumer pattern — the
olfactory-lobe sibling)::

    # The rhinencephalon is the OLFACTORY-LOBE sibling under
    # ``.../right/`` — the cortical olfactory lobe:
    #
    #   right.rhinencephalon
    #
    # The rhinencephalon is a grey-matter / olfactory structure;
    # the white_matter is white matter.

Reaching the subcortical container (recommended consumer pattern —
the grey-matter-nuclei sibling)::

    # The subcortical container holds the GREY-MATTER nuclei —
    # basal forebrain, basal ganglia, extended amygdala, medial
    # temporal lobe, claustrum:
    #
    #   right.subcortical
    #
    # The subcortical container is grey matter; the white_matter is
    # white matter.

Reaching the commissures (recommended consumer pattern — the
commissural white matter, NOT under white_matter/)::

    # The commissures (corpus callosum, anterior commissure) are
    # the COMMISSURAL WHITE MATTER — wired under ``commissures/``,
    # NOT under ``white_matter/``:
    #
    #   right.commissures
    #
    # The commissures are the commissural white matter; the
    # white_matter is the ipsilateral white matter.

Reaching the lateral ventricles (recommended consumer pattern — the
CSF spaces)::

    # The lateral ventricles are the CSF-FILLED SPACES inside the
    # white-matter compartment:
    #
    #   right.lateral_ventricles
    #
    # The lateral ventricles are CSF spaces; the white_matter is
    # white matter.

Reaching the cerebral hemisphere (recommended consumer pattern —
the container)::

    # The cerebral hemisphere (``.../right/``) is the CONTAINER
    # that contains the white_matter and the other five children:
    #
    #   right
    #
    # The white_matter is ONE of the six children of the cerebral
    # hemisphere container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the white_matter is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # white_matter:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The white_matter is SLEA-FREE.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        wm_path = (
            f"telencephalon.cerebral_hemispheres.{side}."
            f"white_matter"
        )
        # resolve wm_path through the memory/recall layer

References
----------
*   **Canonical white-matter anatomy:** Wakana, S., Jiang, H.,
    Nagae, L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter
    atlas of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the ten white-matter structures.)
*   **White-matter anatomy (review):** Schmahmann, J.D., Pandya,
    D.N. (2006). *Fiber Pathways of the Brain*. Oxford University
    Press, New York. (Definitive white-matter anatomy; the ten
    white-matter structures; association, projection, and
    commissural fibers.)
*   **White-matter atlas (human):** Mori, S., Wakana, S., van Zijl,
    P.C.M. (2005). *MRI Atlas of Human White Matter*. Elsevier,
    Amsterdam. (Human white-matter tract anatomy; the ten
    white-matter structures.)
*   **White-matter hyperintensities (leukoaraiosis):** Fazekas, F.,
    Chawluk, J.B., Alavi, A., Hurtig, H.I., Zimmerman, R.A.
    (1987). "MR signal abnormalities at 1.5 T in Alzheimer's
    dementia and normal aging." *American Journal of
    Roentgenology* 149:351–356. (The Fazekas scale for white-matter
    hyperintensities — the radiological hallmark of small-vessel
    disease.)
*   **Leukoaraiosis (review):** Pantoni, L., Garcia, J.H. (1997).
    "Pathogenesis of leukoaraiosis: a review." *Stroke*
    28:652–659. (Leukoaraiosis in the white-matter compartment —
    small-vessel disease.)
*   **Multiple sclerosis and white-matter plaques:** Polman, C.H.,
    et al. (2011). "Diagnostic criteria for multiple sclerosis:
    2010 revisions to the McDonald criteria." *Annals of
    Neurology* 69:292–302. (MS plaques in the white-matter
    compartment.)
*   **Leukodystrophies (review):** van der Knaap, M.S., Bugiani,
    M. (2017). "Leukodystrophies: a proposed classification
    system based on pathological changes and current
    pathophysiological insights." *Acta Neuropathologica*
    134:351–382. (The leukodystrophies — genetic white-matter
    diseases of the white-matter compartment.)
*   **Centrum semiovale perivascular spaces and cerebral amyloid
    angiopathy:** Charidimou, A., et al. (2017). "White matter
    perivascular spaces in cerebral amyloid angiopathy and
    hypertensive arteriopathy." *Neurology* 88:1157–1164. (White
    matter perivascular spaces — cribriform appearance as a
    marker of CAA.)
*   **Lacunar stroke:** Fisher, C.M. (1982). "Lacunar strokes and
    infarcts: a review." *Neurology* 32:871–876. (Lacunar
    infarcts — small-vessel strokes in the white-matter
    compartment: internal capsule, corona radiata, centrum
    semiovale.)
*   **Glioblastoma and white-matter tumor infiltration:** Louis,
    D.N., et al. (2016). "The 2016 World Health Organization
    classification of tumors of the central nervous system: a
    summary." *Acta Neuropathologica* 131:803–820. (Glioblastoma
    and white-matter tumor infiltration.)
*   **Amygdala (contrast — the white_matter is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the white-matter compartment.)
*   **SLEA (contrast — the white_matter is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    white-matter compartment.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (White matter in overview.)
*   NeuroNames — White matter (right); FMA — White matter (right
    member).
"""