"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter.mammillothalamic_tract
==============================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── white_matter
                └── mammillothalamic_tract   <-- THIS MODULE

**Primary synonym:** Mammillothalamic tract (left); MTT;
mammillothalamic fasciculus; **the diencephalic projection from the
mammillary bodies to the anterior thalamic nuclei**; **the Vicq
d'Azyr bundle**; **the bundle of Vicq d'Azyr**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **diencephalic projection** that
**carries the Papez-circuit signal** from the **mammillary
bodies** (its **source**) to the **anterior thalamic nuclei**
(its **target**), running from the **mammillary bodies** in the
**posterior hypothalamus**, up through the **posterior
hypothalamus / anterior midbrain tegmentum**, to the **anterior
nucleus of the thalamus**. It is a **specific named white-matter
tract** — a **diencephalic projection**, **not** a region of
passage, **not** a projection-fiber fan, **not** a capsular
white-matter sheet, **not** an association bundle (long-course or
short), **not** a compact projection-fiber bundle, **not** a
hippocampal output tract, **not** a brainstem-forebrain bundle.
**Part of:** The **white_matter** container of the left cerebral
hemisphere — the **diencephalic projection** that **connects**
the **mammillary bodies** (in the **posterior hypothalamus**) to
the **anterior thalamic nuclei** (in the **anterior thalamus**).
The **mammillothalamic tract** is the **white-matter substrate**
of the **downstream limb** of the **Papez circuit**.
**Structural parent:** ``.../left/white_matter/`` → **direct
child** of the white_matter container.
**Structural children:** **None.** This is a **leaf** module. The
**mammillary-body origin** and the **anterior-thalamic-nucleus
termination** of the mammillothalamic tract are documented as
**prose**, not as structural children.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the mammillothalamic_tract is WHITE MATTER, NOT
a grey-matter structure.** The **mammillothalamic tract** (here)
is the **diencephalic projection** — **myelinated axons**
(projection fibers). The **grey-matter structures** that the
tract **connects** — the **mammillary bodies** (in the
**posterior hypothalamus**) and the **anterior thalamic nuclei**
(in the **anterior thalamus**) — are **grey matter** and are
wired under their own containers
(``.../left/subcortical/diencephalon/hypothalamus/
mammillary_bodies/`` and
``.../left/subcortical/diencephalon/thalamus/left/
anterior_nuclear_group/``). **They are DIFFERENT STRUCTURES** —
the **mammillothalamic tract** is the **diencephalic projection**;
the **mammillary bodies** and the **anterior thalamic nuclei**
are the **grey-matter structures** it **connects**. Consumers
must **not** conflate the mammillothalamic tract with any
grey-matter structure.
**Boundary status (DIENCEPHALIC PROJECTION — the ONLY
diencephalic projection in this container):** **Boundary case —
the mammillothalamic_tract is a DIENCEPHALIC PROJECTION, and it is
the ONLY diencephalic projection in this container.** Unlike
every other white-matter leaf in this container, the
mammillothalamic tract's **defining identity** is
**diencephalic-projection**: it carries the **Papez-circuit
signal** from the **mammillary bodies** (a **hypothalamic**
structure) to the **anterior thalamic nuclei** (a **thalamic**
structure) — **both** of its endpoints are **diencephalic**
structures. It is the **only white-matter tract in this container
whose source and target are both diencephalic**. Consumers must
**not** treat the mammillothalamic tract as "another cortical
projection tract" — it is the **diencephalic projection** of the
**downstream** Papez circuit.
**Boundary status (PROJECTION TRACT — NOT a region of passage, NOT
an association bundle, NOT a compact projection-fiber bundle,
NOT a hippocampal output tract, NOT a brainstem-forebrain
bundle):** **Boundary case — the mammillothalamic_tract is a
PROJECTION TRACT, NOT a region of passage, NOT an association
bundle, NOT a compact projection-fiber bundle, NOT a hippocampal
output tract, NOT a brainstem-forebrain bundle.** The
**mammillothalamic tract** is a **defined projection tract** —
it **carries** the **Papez-circuit signal** from the
**mammillary bodies** to the **anterior thalamic nuclei**. It is
**not** a **region of passage** like the **centrum semiovale**;
it is **not** an **association bundle** like the **cingulum** or
the **external / extreme capsules**; it is **not** a **compact
projection-fiber bundle** like the **internal capsule**; it is
**not** a **hippocampal output tract** like the **fornix**; and
it is **not** a **brainstem-forebrain bundle** like the
**medial forebrain bundle**. Consumers must **not** treat the
mammillothalamic tract as "another region of passage" or "another
association bundle" — it is a **projection tract** with a
**defined course** and **defined diencephalic endpoints**.
**Boundary status (DOWNSTREAM LIMB of the Papez circuit — the
fornix is the UPSTREAM LIMB):** **Boundary case — the
mammillothalamic_tract is the DOWNSTREAM LIMB of the Papez
circuit; the fornix is the UPSTREAM LIMB.** The **Papez circuit**
is **subiculum → mammillary bodies → anterior thalamic nuclei →
cingulate cortex** (and back to the subiculum via the cingulum
and the parahippocampal region). The **fornix**
(``.../left/white_matter/fornix/``) is the **upstream limb**
(subiculum → mammillary bodies). The **mammillothalamic tract**
(here) is the **downstream limb** (mammillary bodies → anterior
thalamic nuclei). **The two tracts are TANDEM components of the
Papez circuit** — the fornix carries the signal to the mammillary
bodies, and the mammillothalamic tract carries it from the
mammillary bodies to the anterior thalamic nuclei. Consumers must
**not** conflate the mammillothalamic tract with the fornix — the
two are **tandem components of the same circuit**, not the same
tract.
**Boundary status (NOT the fornix — the fornix is a SIBLING
white-matter leaf, and it is the UPSTREAM LIMB of the Papez
circuit):** **Boundary case — the mammillothalamic_tract is NOT
the fornix; the fornix is a SIBLING white-matter leaf, and it is
the UPSTREAM LIMB of the Papez circuit.** The **fornix**
(``.../left/white_matter/fornix/``) is the **hippocampal output
tract** — it carries the **subicular output** to the
**mammillary bodies**, the **septal nuclei**, and the
**hypothalamus**. The **mammillothalamic tract** (here) is the
**diencephalic projection** from the **mammillary bodies** to
the **anterior thalamic nuclei**. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** —
the **fornix** is the **upstream limb** (subiculum → mammillary
bodies); the **mammillothalamic tract** is the **downstream
limb** (mammillary bodies → anterior thalamic nuclei).
Consumers must **not** conflate the mammillothalamic tract with
the fornix.
**Boundary status (NOT the mammillary bodies — the mammillary
bodies are the GREY-MATTER SOURCE of the mammillothalamic
tract):** **Boundary case — the mammillothalamic_tract is NOT the
mammillary bodies; the mammillary bodies are the GREY-MATTER
SOURCE of the mammillothalamic tract.** The **mammillary bodies**
(``.../left/subcortical/diencephalon/hypothalamus/
mammillary_bodies/``) are the **grey-matter structures** on the
**inferior surface of the hypothalamus** — the **origin** of
the **mammillothalamic tract** and the **target** of the
**fornix**. The **mammillothalamic tract** (here) is the
**white-matter projection** that **projects from** the mammillary
bodies. **They are DIFFERENT STRUCTURES** — the **mammillary
bodies** are **grey matter**; the **mammillothalamic tract** is
**white matter**. Consumers must **not** conflate the
mammillothalamic tract with the mammillary bodies.
**Boundary status (NOT the anterior thalamic nuclei — the anterior
thalamic nuclei are the GREY-MATTER TARGET of the
mammillothalamic tract):** **Boundary case — the
mammillothalamic_tract is NOT the anterior thalamic nuclei; the
anterior thalamic nuclei are the GREY-MATTER TARGET of the
mammillothalamic tract.** The **anterior thalamic nuclei**
(``.../left/subcortical/diencephalon/thalamus/left/
anterior_nuclear_group/``) are the **grey-matter structures** of
the **anterior thalamus** — the **target** of the
**mammillothalamic tract** and the **Papez-circuit targets**
downstream of the mammillary bodies. The **mammillothalamic
tract** (here) is the **white-matter projection** that **projects
to** the anterior thalamic nuclei. **They are DIFFERENT
STRUCTURES** — the **anterior thalamic nuclei** are **grey
matter**; the **mammillothalamic tract** is **white matter**.
Consumers must **not** conflate the mammillothalamic tract with
the anterior thalamic nuclei.
**Boundary status (NOT the cingulate cortex — the cingulate cortex
is the downstream GREY-MATTER target of the Papez circuit, but it
is NOT the direct target of the mammillothalamic tract):**
**Boundary case — the mammillothalamic_tract is NOT the cingulate
cortex; the cingulate cortex is the downstream GREY-MATTER target
of the Papez circuit, but it is NOT the direct target of the
mammillothalamic tract.** The **cingulate cortex**
(``.../left/cortex/cingulate/``) is the **grey-matter cortex**
of the **cingulate gyrus** — the **downstream** Papez-circuit
target (after the anterior thalamic nuclei project to it via the
**anterior thalamic radiations** in the **anterior limb** of the
**internal capsule**). The **mammillothalamic tract** (here) is
the **white-matter projection** from the **mammillary bodies**
to the **anterior thalamic nuclei** — **not** to the cingulate
cortex. **They are DIFFERENT STRUCTURES** — the **cingulate
cortex** is **grey matter** (a **cortical** structure); the
**mammillothalamic tract** is **white matter** (a **diencephalic
projection**). Consumers must **not** conflate the
mammillothalamic tract with the cingulate cortex, and must **not**
assume the mammillothalamic tract projects to the cortex.
**Boundary status (NOT the hippocampus or the subiculum — those
are the UPSTREAM Papez-circuit structures, upstream of the
fornix, and far upstream of the mammillothalamic tract):**
**Boundary case — the mammillothalamic_tract is NOT the
hippocampus or the subiculum; those are the UPSTREAM Papez-circuit
structures, upstream of the fornix, and far upstream of the
mammillothalamic tract.** The **hippocampus**
(``.../left/subcortical/medial_temporal_lobe/hippocampus/``) and
the **subiculum**
(``.../left/subcortical/medial_temporal_lobe/hippocampus/
subiculum/``) are **grey-matter structures** — the **upstream**
Papez-circuit structures (subiculum → fornix → mammillary
bodies → mammillothalamic tract). The **mammillothalamic tract**
(here) is the **white-matter projection** downstream of the
**fornix** and the **mammillary bodies**. **They are DIFFERENT
STRUCTURES** — the **hippocampus** and the **subiculum** are
**grey matter** (upstream); the **mammillothalamic tract** is
**white matter** (downstream). Consumers must **not** conflate
the mammillothalamic tract with the hippocampus or the subiculum.
**Boundary status (NOT the centrum semiovale, corona radiata,
external capsule, extreme capsule, internal capsule, fasciculus
rectus, cingulum, medial forebrain bundle, or fornix — those are
SIBLING white-matter leaves):** **Boundary case — the
mammillothalamic_tract is NOT the centrum semiovale, corona
radiata, external capsule, extreme capsule, internal capsule,
fasciculus rectus, cingulum, medial forebrain bundle, or fornix;
those are SIBLING white-matter leaves.** Each of those is a
**different white-matter structure** — the **centrum semiovale**
(region of passage), the **corona radiata** (projection-fiber
fan), the **external capsule** and **extreme capsule** (capsular
sheets of the insular / claustral region), the **internal
capsule** (compact projection-fiber bundle between the basal
ganglia and the thalamus), the **fasciculus rectus** (small,
poorly characterized medial-frontal short association bundle),
the **cingulum** (long-course association bundle), the **medial
forebrain bundle** (brainstem-forebrain bundle), and the
**fornix** (hippocampal output tract — the **upstream limb** of
the Papez circuit). **None of them is part of the
mammillothalamic tract** — each is a **separate leaf** under
``white_matter/``. Consumers must **not** conflate the
mammillothalamic tract with any of those siblings.
**Boundary status (NOT the corpus callosum — the corpus callosum is
wired under ``commissures/``):** **Boundary case — the
mammillothalamic_tract is NOT the corpus callosum; the corpus
callosum is wired under ``.../left/commissures/corpus_callosum/``.**
The **corpus callosum** (``.../left/commissures/corpus_callosum/``)
is the **midline commissure** that connects the two hemispheres.
The **mammillothalamic tract** (here) is the **diencephalic
projection** between the **mammillary bodies** and the **anterior
thalamic nuclei** — **intrahemispheric** projection fibers.
**They are DIFFERENT STRUCTURES** — the **corpus callosum** is a
**commissural structure** (wired under ``commissures/``); the
**mammillothalamic tract** is an **intrahemispheric diencephalic
projection** (wired under ``white_matter/``). Consumers must
**not** conflate the mammillothalamic tract with the corpus
callosum.
**Boundary status (NOT the basal ganglia — the basal ganglia are
GREY-MATTER structures FAR from the mammillothalamic tract):**
**Boundary case — the mammillothalamic_tract is NOT the basal
ganglia; the basal ganglia are GREY-MATTER structures FAR from
the mammillothalamic tract.** The **basal ganglia**
(``.../left/subcortical/basal_ganglia/``) — the **caudate
nucleus**, the **putamen**, the **globus pallidus**, and the
**ventral striatum** — are **grey-matter** structures **far
anterior** and **far lateral** from the mammillothalamic tract.
The **mammillothalamic tract** (here) is the **white-matter
diencephalic projection** between the **mammillary bodies** and
the **anterior thalamic nuclei** — **far posterior** and
**medial**. **They are DIFFERENT STRUCTURES** — the **basal
ganglia** are **grey matter**; the **mammillothalamic tract** is
**white matter**. Consumers must **not** conflate the
mammillothalamic tract with the basal ganglia.
**Boundary status (NOT the thalamus as a whole — the thalamus is a
GREY-MATTER structure, and the mammillothalamic tract projects
only to the ANTERIOR thalamic nuclei):** **Boundary case — the
mammillothalamic_tract is NOT the thalamus as a whole; the thalamus
is a GREY-MATTER structure, and the mammillothalamic tract
projects only to the ANTERIOR thalamic nuclei.** The **thalamus**
(``.../left/subcortical/diencephalon/thalamus/``) is the
**grey-matter structure** of the **diencephalon** — the
**thalamic nuclei** (including the **anterior thalamic nuclei**
as one of its nuclear groups). The **mammillothalamic tract**
(here) is the **white-matter projection** that projects
**specifically to the anterior thalamic nuclei** — **not** to
the whole thalamus. **They are DIFFERENT STRUCTURES** — the
**thalamus** is **grey matter**; the **mammillothalamic tract**
is **white matter**. Consumers must **not** conflate the
mammillothalamic tract with the thalamus as a whole, and must
**not** assume the mammillothalamic tract projects to the whole
thalamus.
**Boundary status (NOT the hypothalamus as a whole — the
hypothalamus is a GREY-MATTER structure, and the
mammillothalamic tract originates ONLY from the mammillary
bodies):** **Boundary case — the mammillothalamic_tract is NOT
the hypothalamus as a whole; the hypothalamus is a GREY-MATTER
structure, and the mammillothalamic tract originates ONLY from
the mammillary bodies.** The **hypothalamus**
(``.../left/subcortical/diencephalon/hypothalamus/``) is the
**grey-matter structure** of the **diencephalon** — the
**hypothalamic nuclei** (including the **mammillary bodies** as
one of its nuclear groups). The **mammillothalamic tract** (here)
is the **white-matter projection** that **originates
specifically from the mammillary bodies** — **not** from the
whole hypothalamus. **They are DIFFERENT STRUCTURES** — the
**hypothalamus** is **grey matter**; the **mammillothalamic
tract** is **white matter**. Consumers must **not** conflate the
mammillothalamic tract with the hypothalamus as a whole.
**Boundary status (NOT the cortex — the cortex is NOT a target of
the mammillothalamic tract):** **Boundary case — the
mammillothalamic_tract is NOT the cortex, and the cortex is NOT a
target of the mammillothalamic tract.** The **cortex**
(``.../left/cortex/``) is the **grey-matter sheet** that **caps**
the cerebral hemisphere. The **mammillothalamic tract** (here) is
the **diencephalic projection** between the **mammillary bodies**
and the **anterior thalamic nuclei** — **both diencephalic
structures**, **not** the cortex. **They are DIFFERENT
STRUCTURES** — the **cortex** is **grey matter**; the
**mammillothalamic tract** is **white matter** — and the cortex
is **not** a direct target of the mammillothalamic tract. The
**cingulate cortex** is a **downstream** Papez-circuit target,
**not** a direct target of the mammillothalamic tract.
Consumers must **not** conflate the mammillothalamic tract with
the cortex, and must **not** assume the mammillothalamic tract
projects to the cortex.
**Boundary status (NOT the brainstem — the mammillothalamic tract
does not project to the brainstem):** **Boundary case — the
mammillothalamic_tract is NOT the brainstem, and the tract does
not project to the brainstem.** The **mammillothalamic tract**
runs from the **mammillary bodies** (in the **posterior
hypothalamus**) up through the **posterior hypothalamus /
anterior midbrain tegmentum** to the **anterior thalamic
nuclei** — its **endpoints are diencephalic**, **not**
brainstem. **They are DIFFERENT STRUCTURES** — the **mammillary
bodies** and the **anterior thalamic nuclei** are **diencephalic
grey matter**; the **mammillothalamic tract** is a **diencephalic
white-matter projection** — and it does **not** target the
brainstem. Consumers must **not** assume the mammillothalamic
tract projects to the brainstem.
**Boundary status (NOT the lateral ventricles — the lateral
ventricles are the CSF spaces):** **Boundary case — the
mammillothalamic_tract is NOT the lateral ventricles; the lateral
ventricles are the CSF spaces.** The **lateral ventricles**
(``.../left/lateral_ventricles/``) are the **CSF-filled spaces**
of the cerebral hemisphere — the mammillothalamic tract runs
**below** the **third ventricle** and **medial** to the
**thalamus**, but is **not** the ventricles. **They are
DIFFERENT STRUCTURES** — the **lateral ventricles** are **CSF
spaces**; the **mammillothalamic tract** is **white matter**.
Consumers must **not** conflate the mammillothalamic tract with
the lateral ventricles.
**Boundary status (SLEA-FREE — the mammillothalamic tract is NOT an
extended-amygdala component):** **Boundary case — the
mammillothalamic_tract is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in
the amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **mammillothalamic
tract** is a **diencephalic projection** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the
mammillothalamic tract — it is **SLEA-free**.
**Boundary status (WHITE-MATTER MODULE — a white-matter module in
the series):** **Boundary case — the mammillothalamic_tract is a
WHITE-MATTER module in the series.** Every grey-matter module in
the medial_temporal_lobe subtree (amygdala, hippocampus, and
their children) is a **grey-matter** structure — a **nucleus**, a
**cortical region**, or a **CA field**. The **mammillothalamic
tract** (here) is **white matter** — it is a **white-matter
module in the series**. Consumers must **not** treat the
mammillothalamic tract as "another grey-matter structure" — it is
**white matter**, and the boundaries that anchored the
grey-matter modules ("NOT the white matter") are **reversed**
here ("IS the white matter, NOT the grey-matter structure").

Overview
--------
The mammillothalamic tract is the **diencephalic projection** from
the **mammillary bodies** (in the **posterior hypothalamus**) to
the **anterior thalamic nuclei** (in the **anterior thalamus**) —
a **specific named white-matter tract** whose **defining
endpoints** are **both diencephalic**, and whose **defining role**
is the **downstream limb** of the **Papez circuit**. It is a
**leaf** module under the white_matter container, the **sibling
of the centrum semiovale, the cingulum, the corona radiata, the
external capsule, the extreme capsule, the fasciculus rectus,
the fornix, the internal capsule, and the medial forebrain
bundle**, and the **white-matter substrate** of the
**downstream** Papez circuit.

**The mammillothalamic tract is WHITE MATTER, NOT a grey-matter
structure.** It is the **diencephalic projection** —
**myelinated axons** (projection fibers). The **grey-matter
structures** it **connects** — the **mammillary bodies** (in the
**posterior hypothalamus**) and the **anterior thalamic nuclei**
(in the **anterior thalamus**) — are **grey matter** and are
wired under their own containers.

**The mammillothalamic tract is a DIENCEPHALIC PROJECTION — the
ONLY diencephalic projection in this container.** Its **source**
(the mammillary bodies) and its **target** (the anterior thalamic
nuclei) are **both diencephalic** structures. It is the **only
white-matter tract in this container whose source and target are
both diencephalic**.

**The mammillothalamic tract is the DOWNSTREAM LIMB of the Papez
circuit; the fornix is the UPSTREAM LIMB.** The **Papez circuit**
is **subiculum → mammillary bodies → anterior thalamic nuclei →
cingulate cortex** (and back to the subiculum via the cingulum
and the parahippocampal region). The **fornix** is the
**upstream limb** (subiculum → mammillary bodies). The
**mammillothalamic tract** is the **downstream limb** (mammillary
bodies → anterior thalamic nuclei). **The two tracts are TANDEM
components of the Papez circuit.**

**The mammillothalamic tract is a PROJECTION TRACT, NOT a region of
passage, NOT an association bundle, NOT a compact projection-fiber
bundle, NOT a hippocampal output tract, NOT a brainstem-forebrain
bundle.** It is a **defined projection tract** with a **defined
course** and **defined diencephalic endpoints**.

**The mammillothalamic tract is NOT the fornix.** The **fornix**
(sibling) is the **hippocampal output tract** — the **upstream
limb** of the Papez circuit. The **mammillothalamic tract** is
the **diencephalic projection** — the **downstream limb** of the
Papez circuit. **They are SIBLINGS under the white_matter
container** — **tandem components of the same circuit**.

**The mammillothalamic tract is NOT the mammillary bodies.** The
**mammillary bodies** are the **grey-matter source** of the
tract.

**The mammillothalamic tract is NOT the anterior thalamic nuclei.**
The **anterior thalamic nuclei** are the **grey-matter target**
of the tract.

**The mammillothalamic tract is NOT the cingulate cortex.** The
**cingulate cortex** is a **downstream** Papez-circuit target —
**not** the direct target of the mammillothalamic tract. The
**mammillothalamic tract** projects to the **anterior thalamic
nuclei**, which in turn project to the **cingulate cortex** via
the **anterior thalamic radiations** in the **anterior limb** of
the **internal capsule**.

**The mammillothalamic tract is NOT the hippocampus or the
subiculum.** Those are the **upstream** Papez-circuit structures
(upstream of the fornix, far upstream of the mammillothalamic
tract).

**The mammillothalamic tract is NOT the centrum semiovale, corona
radiata, external capsule, extreme capsule, internal capsule,
fasciculus rectus, cingulum, medial forebrain bundle, or fornix.**
Those are **sibling white-matter leaves** — **each a different
white-matter structure**. **None of them is part of the
mammillothalamic tract.**

**The mammillothalamic tract is NOT the corpus callosum.** The
**corpus callosum** is the **midline commissure** — wired under
``.../left/commissures/corpus_callosum/``.

**The mammillothalamic tract is NOT the basal ganglia.** The
**basal ganglia** are **grey-matter structures** **far anterior**
and **far lateral** from the mammillothalamic tract.

**The mammillothalamic tract is NOT the thalamus as a whole.** The
**thalamus** is a **grey-matter structure**; the
mammillothalamic tract projects **specifically to the anterior
thalamic nuclei**.

**The mammillothalamic tract is NOT the hypothalamus as a whole.**
The **hypothalamus** is a **grey-matter structure**; the
mammillothalamic tract originates **specifically from the
mammillary bodies**.

**The mammillothalamic tract is NOT the cortex.** The **cortex**
is **not a target** of the mammillothalamic tract — the tract
projects **specifically to the anterior thalamic nuclei**, **not**
to the cortex.

**The mammillothalamic tract is NOT the brainstem.** The tract's
**endpoints are diencephalic** — it does **not** project to the
brainstem.

**The mammillothalamic tract is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere).

**The mammillothalamic tract is a paired structure.** Each
hemisphere has its own mammillothalamic tract, with
**ipsilateral** projections from the **mammillary bodies** to the
**anterior thalamic nuclei**. The two sides are **bilaterally
symmetric** — the tract is a **white-matter tract**, and its
**gross anatomy** is **symmetric**; there is **no functional
lateralization** of the mammillothalamic tract per se. The
**functional lateralization** belongs to the **grey-matter
structures** whose fibers pass through it (see *Lateralization
Notes*).

Course and Fiber Composition (prose, not structural children)
--------------------------------------------------------------
The mammillothalamic tract is a **diencephalic projection** —
documented as **prose**, not as structural children:

*   **Origin (mammillary bodies)** — the **mammillary bodies** (in
    the **posterior hypothalamus**) are the **grey-matter
    source** of the mammillothalamic tract. The **principal
    neurons** of the **medial mammillary nucleus** give rise to
    the **mammillothalamic tract fibers**.

*   **Course (posterior hypothalamus → anterior midbrain
    tegmentum → anterior thalamus)** — the tract **ascends**
    from the **mammillary bodies** through the **posterior
    hypothalamus**, into the **anterior midbrain tegmentum**,
    and then **anteriorly and superiorly** to the **anterior
    thalamic nuclei**.

*   **Termination (anterior thalamic nuclei)** — the **anterior
    thalamic nuclei** (especially the **anteroventral** and
    **anteromedial** nuclei) are the **grey-matter target** of
    the mammillothalamic tract. The tract fibers **synapse** on
    the **principal neurons** of the **anterior thalamic
    nuclei**.

*   **Fiber group (mammillothalamic fibers)** — the **principal
    fibers** of the mammillothalamic tract are the **projection
    fibers** from the **medial mammillary nucleus** to the
    **anterior thalamic nuclei**. This is the **defining fiber
    group** of the mammillothalamic tract.

*   **Downstream (anterior thalamic radiations)** — the
    **anterior thalamic nuclei** in turn project to the
    **cingulate cortex** (and other cortical targets) via the
    **anterior thalamic radiations** in the **anterior limb** of
    the **internal capsule**. The **mammillothalamic tract** is
    **upstream** of the **anterior thalamic radiations** in the
    Papez circuit.

**These course and fiber details are prose, not structural
children.** The tree wires the **mammillothalamic tract** as a
**single leaf** under ``white_matter/`` — the **origin**, the
**course**, the **termination**, and the **fiber groups** are
**prose**, not structural children. Consumers that need
**course-level** or **fiber-level** resolution should consult the
references, not the tree.

The Mammillothalamic Tract / Fornix Boundary
--------------------------------------------
This is the **most consequential sibling boundary** — the
**downstream limb vs. upstream limb of the Papez circuit**
boundary:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection** — carries the **Papez-circuit signal** from the
    **mammillary bodies** (source) to the **anterior thalamic
    nuclei** (target). **Downstream** limb of the Papez circuit.

*   **Fornix** (``.../left/white_matter/fornix/``) — the
    **hippocampal output tract** — carries the **Papez-circuit
    signal** from the **subiculum** (source) to the **mammillary
    bodies** (target). **Upstream** limb of the Papez circuit.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **fornix** is the **hippocampal
output tract** (subiculum → mammillary bodies); the
**mammillothalamic tract** is the **diencephalic projection**
(mammillary bodies → anterior thalamic nuclei). **The two tracts
are TANDEM components of the Papez circuit** — the fornix is the
**upstream** limb, the mammillothalamic tract is the **downstream**
limb. Consumers must **not** conflate the mammillothalamic tract
with the fornix.

The Mammillothalamic Tract / Mammillary Bodies Boundary
-------------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
**source** of the mammillothalamic tract fibers:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection**.

*   **Mammillary bodies**
    (``.../left/subcortical/diencephalon/hypothalamus/
    mammillary_bodies/``) — the **grey-matter source** of the
    tract (the **origin** of the mammillothalamic fibers).

**They are DIFFERENT STRUCTURES** — the **mammillary bodies** are
**grey matter**; the **mammillothalamic tract** is **white
matter**. The **mammillary bodies** are the **origin** of the
tract. Consumers must **not** conflate the mammillothalamic tract
with the mammillary bodies.

The Mammillothalamic Tract / Anterior Thalamic Nuclei Boundary
--------------------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
**target** of the mammillothalamic tract fibers:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection**.

*   **Anterior thalamic nuclei**
    (``.../left/subcortical/diencephalon/thalamus/left/
    anterior_nuclear_group/``) — the **grey-matter target** of
    the tract (the **termination** of the mammillothalamic
    fibers).

**They are DIFFERENT STRUCTURES** — the **anterior thalamic
nuclei** are **grey matter**; the **mammillothalamic tract** is
**white matter**. The **anterior thalamic nuclei** are the
**target** of the tract. Consumers must **not** conflate the
mammillothalamic tract with the anterior thalamic nuclei.

The Mammillothalamic Tract / Cingulate Cortex Boundary
------------------------------------------------------
This is the **white matter vs. grey matter** boundary — a
**downstream** Papez-circuit target (not a direct target of the
mammillothalamic tract):

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection** (mammillary bodies → anterior thalamic nuclei).

*   **Cingulate cortex** (``.../left/cortex/cingulate/``) — the
    **grey-matter cortex** of the **cingulate gyrus** — the
    **downstream** Papez-circuit target (after the anterior
    thalamic nuclei project to it via the anterior thalamic
    radiations).

**They are DIFFERENT STRUCTURES** — the **cingulate cortex** is
**grey matter** (a **cortical** structure); the
**mammillothalamic tract** is **white matter** (a **diencephalic
projection**). The **mammillothalamic tract** projects to the
**anterior thalamic nuclei**, **not** to the cingulate cortex —
the **cingulate cortex** is a **downstream** target of the Papez
circuit. Consumers must **not** conflate the mammillothalamic
tract with the cingulate cortex, and must **not** assume the
mammillothalamic tract projects to the cortex.

The Mammillothalamic Tract / Hippocampus and Subiculum Boundary
---------------------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
**upstream** Papez-circuit structures:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection** (downstream of the mammillary bodies).

*   **Hippocampus**
    (``.../left/subcortical/medial_temporal_lobe/hippocampus/``)
    and **subiculum**
    (``.../left/subcortical/medial_temporal_lobe/hippocampus/
    subiculum/``) — the **upstream** Papez-circuit structures
    (upstream of the fornix, far upstream of the mammillothalamic
    tract).

**They are DIFFERENT STRUCTURES** — the **hippocampus** and the
**subiculum** are **grey matter** (upstream); the
**mammillothalamic tract** is **white matter** (downstream).
Consumers must **not** conflate the mammillothalamic tract with
the hippocampus or the subiculum.

The Mammillothalamic Tract / Other White-Matter Leaves Boundary
--------------------------------------------------------------
This is the **diencephalic projection vs. other named white-matter
structures** boundary:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection**.

*   **Centrum semiovale**, **corona radiata**, **external
    capsule**, **extreme capsule**, **internal capsule**,
    **fasciculus rectus**, **cingulum**, **medial forebrain
    bundle** — the **other named white-matter leaves** under
    ``white_matter/``.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — each of those is a **different
white-matter structure**; the **mammillothalamic tract** is a
**diencephalic projection**. **None of those is part of the
mammillothalamic tract** — each is a **separate leaf** under
``white_matter/``. Consumers must **not** conflate the
mammillothalamic tract with any of those siblings.

The Mammillothalamic Tract / Corpus Callosum Boundary
-----------------------------------------------------
This is the **diencephalic projection vs. commissural structure**
boundary:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection**.

*   **Corpus_callosum**
    (``.../left/commissures/corpus_callosum/``) — the **midline
    commissure** that connects the two hemispheres — wired under
    ``commissures/``, **not** under ``white_matter/``.

**They are DIFFERENT STRUCTURES** — the **corpus callosum** is a
**commissural structure** (wired under ``commissures/``); the
**mammillothalamic tract** is an **intrahemispheric diencephalic
projection** (wired under ``white_matter/``). Consumers must
**not** conflate the mammillothalamic tract with the corpus
callosum.

The Mammillothalamic Tract / Basal Ganglia Boundary
---------------------------------------------------
This is the **white matter vs. grey matter** boundary — the basal
ganglia are **far anterior / far lateral** from the
mammillothalamic tract:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection**.

*   **Basal ganglia** (``.../left/subcortical/basal_ganglia/``) —
    the **grey-matter structures** (caudate nucleus, putamen,
    globus pallidus, ventral striatum) **far anterior** and **far
    lateral** from the mammillothalamic tract.

**They are DIFFERENT STRUCTURES** — the **basal ganglia** are
**grey matter**; the **mammillothalamic tract** is **white
matter**. Consumers must **not** conflate the mammillothalamic
tract with the basal ganglia.

The Mammillothalamic Tract / Thalamus and Hypothalamus Boundary
---------------------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
thalamus and hypothalamus are the **grey-matter containers** of
the **tract's endpoints**:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection** (mammillary bodies → anterior thalamic nuclei).

*   **Thalamus**
    (``.../left/subcortical/diencephalon/thalamus/``) — the
    **grey-matter container** of the **anterior thalamic nuclei**
    (the **tract's target**). The **tract projects specifically
    to the anterior thalamic nuclei**, **not** to the whole
    thalamus.

*   **Hypothalamus**
    (``.../left/subcortical/diencephalon/hypothalamus/``) — the
    **grey-matter container** of the **mammillary bodies** (the
    **tract's source**). The **tract originates specifically from
    the mammillary bodies**, **not** from the whole hypothalamus.

**They are DIFFERENT STRUCTURES** — the **thalamus** and the
**hypothalamus** are **grey matter**; the **mammillothalamic
tract** is **white matter**. Consumers must **not** conflate the
mammillothalamic tract with the thalamus or the hypothalamus as a
whole, and must **not** assume the tract projects to (or
originates from) the whole thalamus or hypothalamus.

The Mammillothalamic Tract / Cortex and Brainstem Boundary
---------------------------------------------------------
This is the **white matter vs. grey matter / other structures**
boundary — the cortex and the brainstem are **NOT tract
endpoints**:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection** between the mammillary bodies and the anterior
    thalamic nuclei.

*   **Cortex** (``.../left/cortex/``) — the **grey-matter sheet**
    that **caps** the cerebral hemisphere — **NOT** a direct
    target of the mammillothalamic tract.

*   **Brainstem** (the brainstem, in the
    ``.../left/subcortical/`` region and further caudal) — the
    **grey-matter / white-matter structures** of the brainstem —
    **NOT** a target of the mammillothalamic tract.

**They are DIFFERENT STRUCTURES** — the **cortex** is **grey
matter**; the **brainstem** contains **grey and white matter**;
the **mammillothalamic tract** is **white matter**. The **cortex**
and the **brainstem** are **not** direct targets of the
mammillothalamic tract — the tract's **endpoints are
diencephalic**. Consumers must **not** assume the
mammillothalamic tract projects to the cortex or to the brainstem.

The Mammillothalamic Tract / Lateral Ventricles Boundary
-------------------------------------------------------
This is the **white matter vs. CSF space** boundary:

*   **Mammillothalamic_tract** (this module) — the **diencephalic
    projection** that runs **below** the **third ventricle** and
    **medial** to the **thalamus**.

*   **Lateral ventricles** (``.../left/lateral_ventricles/``) — the
    **CSF-filled spaces** of the cerebral hemisphere.

**They are DIFFERENT STRUCTURES** — the **lateral ventricles** are
**CSF spaces**; the **mammillothalamic tract** is **white matter**.
Consumers must **not** conflate the mammillothalamic tract with the
lateral ventricles.

The Mammillothalamic Tract / White Matter Container Boundary
------------------------------------------------------------
This is the **child vs. container** boundary:

*   **Mammillothalamic_tract** (this module) — a **child** of the
    white_matter container.

*   **White_matter** (``.../left/white_matter/``) — the
    **container** that contains the **centrum semiovale**, the
    **cingulum**, the **corona radiata**, the **external
    capsule**, the **extreme capsule**, the **fasciculus rectus**,
    the **fornix**, the **internal capsule**, the
    **mammillothalamic tract**, and the **medial forebrain
    bundle**.

**The mammillothalamic tract is ONE of the ten children of the
white_matter container.** Consumers must **not** conflate the
mammillothalamic tract with the white_matter container.

The Mammillothalamic Tract / Cerebral Hemisphere Boundary
--------------------------------------------------------
This is the **grandchild vs. container** boundary:

*   **Mammillothalamic_tract** (this module) — a **grandchild** of
    the ``.../left/`` (cerebral hemisphere) container.

*   **``.../left/``** — the **cerebral hemisphere container** that
    contains the **cortex**, the **rhinencephalon**, the
    **subcortical** structures, the **white_matter**, the
    **commissures**, and the **lateral_ventricles**.

**The mammillothalamic tract is a grandchild of the cerebral
hemisphere** (child of the white_matter container). Consumers
must **not** conflate the mammillothalamic tract with the cerebral
hemisphere container.

The Mammillothalamic Tract / SLEA Boundary
------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Mammillothalamic_tract** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The mammillothalamic tract is NOT part of the SLEA continuum.**
It is a **diencephalic projection**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
mammillothalamic tract.

Function in the Human Brain
---------------------------
The mammillothalamic tract's function is **diencephalic
projection** — **downstream Papez-circuit relay** — **NOT a
grey-matter function**:

*   **Papez-Circuit Relay (Mammillary Bodies → Anterior Thalamic
    Nuclei):** The **mammillothalamic tract** is the
    **downstream limb** of the **Papez circuit** — it carries the
    **Papez-circuit signal** from the **mammillary bodies** to
    the **anterior thalamic nuclei**. This is the
    **Papez-circuit** substrate of the mammillothalamic tract —
    the **limbic circuit** historically associated with **emotion
    and episodic memory**.

*   **Anterior Thalamic Activation (Limbic Modulation):** The
    **mammillothalamic tract** **activates** the **anterior
    thalamic nuclei** — which in turn project to the
    **cingulate cortex** (and other cortical targets) via the
    **anterior thalamic radiations** in the **anterior limb** of
    the **internal capsule**. The **anterior thalamic nuclei**
    are a **critical node** in the **Papez circuit** for
    **episodic memory** — their **activation by the
    mammillothalamic tract** is **necessary** for **normal
    episodic memory**.

*   **Spatial and Episodic Memory Contribution:** The **Papez
    circuit** (including the mammillothalamic tract) is
    **necessary** for **normal spatial and episodic memory** —
    **lesions of the mammillothalamic tract** produce
    **anterograde amnesia** in humans (especially for **episodic
    memory**), similar to **lesions of the mammillary bodies**
    or the **anterior thalamic nuclei**.

*   **Head-Direction Signal Relay (Contested):** The **anterior
    thalamic nuclei** (the **target** of the mammillothalamic
    tract) contain **head-direction cells** — the
    **mammillothalamic tract** may **relay** part of the
    **head-direction** signal from the **mammillary bodies** to
    the **anterior thalamic nuclei**. This is **contested** and
    is documented in the references.

*   **NOT a neural processor in the classical sense.** The
    **mammillothalamic tract** is a **diencephalic projection** —
    it **conducts** the **Papez-circuit signal** from the
    **mammillary bodies** to the **anterior thalamic nuclei**,
    but it does **not** **process** information (that happens in
    the **grey-matter structures** — the **mammillary bodies**
    and the **anterior thalamic nuclei**). The **fear-output** is
    the **central nucleus**; the **fear-learning** structures are
    the **basolateral nuclei**.

**The unifying theme:** the mammillothalamic tract is the
**diencephalic projection** of the **cerebral hemisphere** — the
**specific named white-matter tract** that anchors the
**downstream limb** of the **Papez circuit**. It is **SLEA-free**,
**white-matter**, and **NOT a grey-matter structure** — the
**grey-matter structures** are the **mammillary bodies** and the
**anterior thalamic nuclei** whose fibers pass through it.

Associated Disorders
--------------------
The mammillothalamic tract has **no named "mammillothalamic tract
syndrome"** in the narrow sense, but its clinical associations are
**well-documented** — primarily as a **Papez-circuit imaging
target** and as a **diencephalic amnesia** structure:

*   **Wernicke-Korsakoff Syndrome (Mammillothalamic Tract /
    Mammillary-Body Involvement):** The **mammillothalamic tract**
    — together with the **mammillary bodies** — is **involved** in
    **Wernicke-Korsakoff syndrome** (thiamine deficiency) — the
    **Papez-circuit** disruption contributes to the
    **anterograde amnesia** of the syndrome. The
    **mammillothalamic tract** is the **white-matter substrate**
    of the **downstream-Papez-circuit** component of the
    syndrome.

*   **Diencephalic Amnesia (Bilateral Mammillothalamic Tract
    Lesions):** **Bilateral lesions** of the **mammillothalamic
    tract** produce **diencephalic amnesia** — a
    **Papez-circuit** amnesia characterized by **anterograde
    episodic memory** impairment, with **preserved** short-term
    memory and **preserved** procedural memory. The
    **mammillothalamic tract** is the **white-matter substrate**
    of diencephalic amnesia.

*   **Anterior Thalamic Infarction (Papez-Circuit Disruption):**
    Infarction of the **anterior thalamic nuclei** (the
    **mammillothalamic tract's target**) produces
    **Papez-circuit** memory impairment — the
    **mammillothalamic tract** is the **white-matter projection**
    whose interruption (upstream of the anterior thalamic
    nuclei) produces **similar** memory impairment.

*   **Colloid Cyst and Mammillothalamic Tract Compression:** A
    **colloid cyst** of the **third ventricle** can **compress**
    the **mammillothalamic tract** (as well as the fornix) — the
    **tract compression** contributes to **memory** deficits in
    patients with **colloid cysts**.

*   **Schizophrenia (Mammillothalamic Tract Abnormalities —
    Contested):** The **mammillothalamic tract** shows **DTI
    abnormalities** in **schizophrenia** — **reduced fractional
    anisotropy** in the **Papez-circuit tracts** (including the
    mammillothalamic tract) is reported. This is **contested** —
    the findings are **not** uniformly replicated.

*   **Multiple Sclerosis (Mammillothalamic Tract Plaques):** The
    **mammillothalamic tract** is a **site** of **MS plaques** —
    the **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**. **Mammillothalamic
    tract DTI changes** are reported in **MS**.

*   **No Named "Mammillothalamic Tract Syndrome":** The
    **mammillothalamic tract** is a **diencephalic projection**,
    not a **single functional system** — it has **no named
    clinical syndrome**. Its clinical relevance is **direct** as a
    **Papez-circuit imaging target** (Wernicke-Korsakoff,
    diencephalic amnesia, anterior thalamic infarction, colloid
    cyst, MS), and **contested** for **schizophrenia**.

**What is NOT here:** The **mammillothalamic tract** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as a **Papez-circuit imaging target**, and **contested**
for **schizophrenia**.

Lateralization Notes
--------------------
This is the **left** mammillothalamic_tract module. The
**mammillothalamic tract** is **bilaterally symmetric** — and it
carries **NO warning**:

*   **Bilateral White-Matter Anatomy:** Each hemisphere has its own
    mammillothalamic tract, with **ipsilateral** projections from
    the mammillary bodies to the anterior thalamic nuclei. The
    two sides are **grossly symmetric** — the mammillothalamic
    tract is a **white-matter tract**, and its **gross anatomy**
    is **symmetric**. There is **no functional lateralization** of
    the mammillothalamic tract per se.

*   **NO Functional Lateralization of the White-Matter Tract:**
    The **functional lateralization** belongs to the **grey-matter
    structures** whose fibers pass through the mammillothalamic
    tract (the **mammillary bodies** and the **anterior thalamic
    nuclei** — and, downstream, the **cingulate cortex**) —
    **not** to the mammillothalamic tract itself. Consumers must
    **not** assume the mammillothalamic tract carries a
    **functional lateralization** of its own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    mammillothalamic_tract is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the mammillothalamic tract.

*   **NO Amygdala-Lateralization Warning of their own (the
    mammillothalamic tract is a DIENCEPHALIC PROJECTION, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **mammillothalamic tract** is a
    **diencephalic projection** — consumers must **not** conflate
    it with the **whole amygdala** or with the **central
    nucleus**.

**A consumer that assumes "left mammillothalamic tract = right
mammillothalamic tract" will be structurally correct** — the two
sides are **symmetric** (the mammillothalamic tract is a
**white-matter tract**, and its **gross anatomy** is
**symmetric**). The **mammillothalamic tract** is a
**strict-mirror pair with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../left/white_matter/centrum_semiovale/``,
    ``.../left/white_matter/cingulum/``,
    ``.../left/white_matter/corona_radiata/``,
    ``.../left/white_matter/external_capsule/``,
    ``.../left/white_matter/extreme_capsule/``,
    ``.../left/white_matter/fasciculus_rectus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/white_matter/internal_capsule/``,
    ``.../left/white_matter/medial_forebrain_bundle/``,
    ``.../left/commissures/``,
    ``.../left/subcortical/diencephalon/hypothalamus/
    mammillary_bodies/``,
    ``.../left/subcortical/diencephalon/thalamus/left/
    anterior_nuclear_group/``,
    ``.../left/subcortical/diencephalon/thalamus/``,
    ``.../left/subcortical/diencephalon/hypothalamus/``,
    ``.../left/subcortical/basal_ganglia/``,
    ``.../left/subcortical/medial_temporal_lobe/hippocampus/``,
    ``.../left/subcortical/medial_temporal_lobe/hippocampus/
    subiculum/``,
    ``.../left/cortex/``, ``.../left/cortex/cingulate/``,
    ``.../left/lateral_ventricles/``, or any other container. The
    **mammillothalamic tract**'s relationships to the fornix, the
    mammillary bodies, the anterior thalamic nuclei, the cingulate
    cortex, the hippocampus, the subiculum, the corpus callosum,
    the basal ganglia, the thalamus, the hypothalamus, the cortex,
    the brainstem, the lateral ventricles, and the other
    white-matter leaves are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **mammillary-body
    origin** and the **anterior-thalamic-nucleus termination** of
    the mammillothalamic tract are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve course-level detail through the references.
*   **WHITE MATTER — NOT a grey-matter structure.** The
    **mammillothalamic tract** is **white matter**; the
    **mammillary bodies**, the **anterior thalamic nuclei**, the
    **cingulate cortex**, the **thalamus** (as a whole), and the
    **hypothalamus** (as a whole) are **grey matter**. Consumers
    must **not** conflate the mammillothalamic tract with any
    grey-matter structure.
*   **DIENCEPHALIC PROJECTION — the ONLY diencephalic projection in
    this container.** The **mammillothalamic tract**'s **source**
    (the mammillary bodies) and **target** (the anterior thalamic
    nuclei) are **both diencephalic** structures. Consumers must
    **not** treat the mammillothalamic tract as "another cortical
    projection tract" — it is the **diencephalic projection** of
    the **downstream** Papez circuit.
*   **PROJECTION TRACT — NOT a region of passage, NOT an
    association bundle, NOT a compact projection-fiber bundle,
    NOT a hippocampal output tract, NOT a brainstem-forebrain
    bundle.** The **mammillothalamic tract** is a **projection
    tract**.
*   **DOWNSTREAM LIMB of the Papez circuit — the fornix is the
    UPSTREAM LIMB.** The **mammillothalamic tract** (downstream,
    mammillary bodies → anterior thalamic nuclei) and the
    **fornix** (upstream, subiculum → mammillary bodies) are
    **TANDEM components of the Papez circuit**. Consumers must
    **not** conflate the two, and must **not** treat them as the
    same tract.
*   **NOT the fornix — the fornix is a SIBLING white-matter leaf,
    and it is the UPSTREAM LIMB of the Papez circuit.**
*   **NOT the mammillary bodies — the mammillary bodies are the
    GREY-MATTER SOURCE of the mammillothalamic tract.**
*   **NOT the anterior thalamic nuclei — the anterior thalamic
    nuclei are the GREY-MATTER TARGET of the mammillothalamic
    tract.**
*   **NOT the cingulate cortex — the cingulate cortex is the
    downstream GREY-MATTER target of the Papez circuit, but it is
    NOT the direct target of the mammillothalamic tract.**
*   **NOT the hippocampus or the subiculum — those are the UPSTREAM
    Papez-circuit structures, upstream of the fornix, and far
    upstream of the mammillothalamic tract.**
*   **NOT the centrum semiovale, corona radiata, external capsule,
    extreme capsule, internal capsule, fasciculus rectus,
    cingulum, medial forebrain bundle, or fornix — those are
    SIBLING white-matter leaves.** None of them is part of the
    mammillothalamic tract.
*   **NOT the corpus callosum — the corpus callosum is wired under
    ``commissures/``.**
*   **NOT the basal ganglia — the basal ganglia are GREY-MATTER
    structures FAR anterior and FAR lateral from the
    mammillothalamic tract.**
*   **NOT the thalamus as a whole — the mammillothalamic tract
    projects specifically to the ANTERIOR thalamic nuclei.**
*   **NOT the hypothalamus as a whole — the mammillothalamic tract
    originates specifically from the MAMMILLARY BODIES.**
*   **NOT the cortex — the cortex is NOT a target of the
    mammillothalamic tract.**
*   **NOT the brainstem — the tract does not project to the
    brainstem.**
*   **NOT the lateral ventricles — the lateral ventricles are CSF
    spaces.**
*   **NOT the white_matter container — the mammillothalamic tract is
    a CHILD of the white_matter container.**
*   **NOT the cerebral hemisphere container — the mammillothalamic
    tract is a GRANDCHILD of the ``.../left/`` container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    mammillothalamic tract is **not** an extended-amygdala
    component, and it carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **mammillothalamic tract** is a **diencephalic projection**.
*   **No ``AREA_PATHS`` hop.** The **mammillothalamic tract** is a
    local leaf under ``white_matter/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **mammillothalamic tract** has
    no nested dual-framing module. It is a single leaf.
*   **Structural parity with right mammillothalamic tract — strict
    mirror with NO warning.** Left and right mammillothalamic
    tract modules are **structurally identical** — same **leaf**
    status, same **diencephalic-projection** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter import mammillothalamic_tract

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.white_matter."
        "mammillothalamic_tract"
    )

**Do not** assume the mammillothalamic tract is the **fornix**. The
**fornix** is a **sibling** white-matter leaf — the **upstream
limb** of the Papez circuit (subiculum → mammillary bodies). The
**mammillothalamic tract** is the **downstream limb** (mammillary
bodies → anterior thalamic nuclei). **They are tandem components
of the Papez circuit.**

**Do not** assume the mammillothalamic tract is the **mammillary
bodies**. The **mammillary bodies** are the **grey-matter
source** of the tract.

**Do not** assume the mammillothalamic tract is the **anterior
thalamic nuclei**. The **anterior thalamic nuclei** are the
**grey-matter target** of the tract.

**Do not** assume the mammillothalamic tract is the **cingulate
cortex**. The **cingulate cortex** is a **downstream**
Papez-circuit target — **not** the direct target of the
mammillothalamic tract.

**Do not** assume the mammillothalamic tract is the **hippocampus**
or the **subiculum**. Those are the **upstream** Papez-circuit
structures (upstream of the fornix, far upstream of the
mammillothalamic tract).

**Do not** assume the mammillothalamic tract is **any** of the
other white-matter siblings — the **centrum semiovale**, the
**corona radiata**, the **external capsule**, the **extreme
capsule**, the **internal capsule**, the **fasciculus rectus**,
the **cingulum**, or the **medial forebrain bundle**. Those are
**separate leaves** under ``white_matter/``.

**Do not** assume the mammillothalamic tract is the **corpus
callosum**. The **corpus callosum** is wired under
``commissures/`` — the **commissural structure**.

**Do not** assume the mammillothalamic tract is the **basal
ganglia**. The **basal ganglia** are **grey-matter structures**
**far anterior** and **far lateral** from the mammillothalamic
tract.

**Do not** assume the mammillothalamic tract is the **thalamus** or
the **hypothalamus** as a whole. The **thalamus** and the
**hypothalamus** are **grey-matter structures**; the
mammillothalamic tract projects **specifically to the anterior
thalamic nuclei** and originates **specifically from the
mammillary bodies**.

**Do not** assume the mammillothalamic tract is the **cortex** or
the **brainstem**. The **cortex** and the **brainstem** are
**not** direct targets of the mammillothalamic tract — the
tract's **endpoints are diencephalic**.

**Do not** assume the mammillothalamic tract is the **lateral
ventricles**. The **lateral ventricles** are **CSF spaces** —
the tract runs **below** the third ventricle and **medial** to
the thalamus.

**Do not** assume the mammillothalamic tract is the **white_matter
container**. The **white_matter** container contains the
**mammillothalamic tract** and the other nine white-matter leaves
— the **mammillothalamic tract** is **one** of those ten
children.

**Do not** assume the mammillothalamic tract is the **cerebral
hemisphere container**. The **mammillothalamic tract** is a
**grandchild** of the ``.../left/`` container (child of the
white_matter container).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the mammillothalamic
tract. **The mammillothalamic tract is SLEA-FREE** — it is **not**
an extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the mammillothalamic tract's (empty) children
(recommended consumer pattern)::

    MAMMILLOTHALAMIC_TRACT_CHILDREN = ()
    # The mammillothalamic tract is a leaf. The mammillary-body
    # origin and the anterior-thalamic-nucleus termination are
    # prose, not modules.

Reaching the fornix sibling (recommended consumer pattern — the
UPSTREAM limb of the Papez circuit)::

    # The fornix is the HIPPOCAMPAL OUTPUT TRACT — the SIBLING of
    # the mammillothalamic tract under the white_matter container,
    # and the UPSTREAM limb of the Papez circuit:
    #
    #   white_matter.fornix
    #
    # The fornix is the UPSTREAM limb (subiculum → mammillary
    # bodies); the mammillothalamic tract is the DOWNSTREAM limb
    # (mammillary bodies → anterior thalamic nuclei). The two
    # tracts are TANDEM components of the Papez circuit.

Reaching the mammillary bodies (recommended consumer pattern — the
grey-matter source of the mammillothalamic tract)::

    # The mammillary bodies are the GREY-MATTER SOURCE of the
    # mammillothalamic tract:
    #
    #   left.subcortical.diencephalon.hypothalamus.mammillary_bodies
    #
    # The mammillary bodies are grey matter; the mammillothalamic
    # tract is white matter — the diencephalic projection that
    # originates from the mammillary bodies.

Reaching the anterior thalamic nuclei (recommended consumer pattern
— the grey-matter target of the mammillothalamic tract)::

    # The anterior thalamic nuclei are the GREY-MATTER TARGET of
    # the mammillothalamic tract:
    #
    #   left.subcortical.diencephalon.thalamus.left.anterior_nuclear_group
    #
    # The anterior thalamic nuclei are grey matter; the
    # mammillothalamic tract is white matter — the diencephalic
    # projection that terminates in the anterior thalamic nuclei.

Reaching the cingulate cortex (recommended consumer pattern — the
downstream Papez-circuit cortical target)::

    # The cingulate cortex is the DOWNSTREAM Papez-circuit cortical
    # target — NOT the direct target of the mammillothalamic tract:
    #
    #   left.cortex.cingulate
    #
    # The mammillothalamic tract projects to the anterior thalamic
    # nuclei; the anterior thalamic nuclei project to the cingulate
    # cortex via the anterior thalamic radiations in the anterior
    # limb of the internal capsule.

Reaching the hippocampus and subiculum (recommended consumer
pattern — the upstream Papez-circuit structures)::

    # The hippocampus and the subiculum are the UPSTREAM
    # Papez-circuit structures — upstream of the fornix, far
    # upstream of the mammillothalamic tract:
    #
    #   left.subcortical.medial_temporal_lobe.hippocampus
    #   left.subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # The subiculum is the principal source of the fornix fibers
    # (the upstream limb of the Papez circuit); the
    # mammillothalamic tract is the downstream limb.

Reaching the corpus callosum (recommended consumer pattern — the
commissural structure, NOT under white_matter/)::

    # The corpus callosum is the COMMISSURAL STRUCTURE — wired
    # under ``commissures/``, NOT under ``white_matter/``:
    #
    #   left.commissures.corpus_callosum
    #
    # The corpus callosum is a commissural structure; the
    # mammillothalamic tract is an intrahemispheric diencephalic
    # projection.

Reaching the white_matter container (recommended consumer pattern —
the container)::

    # The white_matter container contains the mammillothalamic tract
    # and the other nine white-matter leaves:
    #
    #   left.white_matter
    #
    # The mammillothalamic tract is ONE of the ten children of the
    # white_matter container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the mammillothalamic tract is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # mammillothalamic tract:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The mammillothalamic tract is SLEA-FREE.

Course-level detail (not wired — consult references)::

    # The mammillothalamic tract's course is prose, not a module:
    #   origin        -> mammillary bodies (posterior hypothalamus)
    #   course        -> ascending through the posterior
    #                    hypothalamus, into the anterior midbrain
    #                    tegmentum, then anteriorly and superiorly
    #                    to the anterior thalamic nuclei
    #   termination   -> anterior thalamic nuclei (anterior
    #                    thalamus)
    #
    # Do not attempt to resolve these as sub-paths of the
    # mammillothalamic tract.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mtt_path = (
            f"telencephalon.cerebral_hemispheres.{side}.white_matter."
            f"mammillothalamic_tract"
        )
        # resolve mtt_path through the memory/recall layer

References
----------
*   **Canonical mammillothalamic tract anatomy:** Swanson, L.W.,
    Cowan, W.M. (1977). "An autoradiographic study of the
    organization of the efferent connections of the hippocampal
    formation in the rat." *Journal of Comparative Neurology*
    172:49–84. (Definitive mammillothalamic tract anatomy — the
    mammillary bodies → anterior thalamic nuclei projection.)
*   **Mammillothalamic tract anatomy (review):** Aggleton, J.P.,
    Saunders, R.C. (2007). "The origin and course of the
    fornix." In: *The Fornix*, Nova Science Publishers, New York.
    (Review of the fornix and its downstream continuation via the
    mammillothalamic tract.)
*   **Papez circuit (review):** Aggleton, J.P., et al. (2010).
    "Hippocampal-anterior thalamic pathways for memory: uncovering
    a network of direct and indirect actions." *European Journal
    of Neuroscience* 31:2292–2307. (The Papez circuit — the
    fornix, mammillary bodies, mammillothalamic tract, anterior
    thalamic nuclei, cingulate cortex.)
*   **Papez circuit (origin):** Papez, J.W. (1937). "A proposed
    mechanism of emotion." *Archives of Neurology and Psychiatry*
    38:725–743. (The original Papez-circuit description.)
*   **Mammillothalamic tract (review — anatomy, function, and
    clinical associations):** Bubb, E.J., Kinnavane, L.,
    Aggleton, J.P. (2017). "Hippocampal-diencephalic-cingulate
    networks for memory: anatomical, functional and clinical
    commentary." *Brain and Neuroscience Advances* 1:1–25.
    (Review of the mammillothalamic tract and the extended Papez
    circuit.)
*   **Diencephalic amnesia (review):** Aggleton, J.P., Brown,
    M.W. (1999). "Episodic memory, amnesia, and the
    hippocampal-anterior thalamic axis." *Behavioral and Brain
    Sciences* 22:425–444. (The hippocampal-anterior thalamic
    axis — the mammillothalamic tract in diencephalic amnesia.)
*   **Mammillothalamic tract in Wernicke-Korsakoff syndrome:**
    Kril, J.J., Harper, C.G. (2012). "Neuroanatomical
    signs in the brains of chronic alcoholics — a review."
    *Alcohol and Alcoholism* 47:115–122. (Wernicke-Korsakoff
    syndrome — the involvement of the mammillothalamic tract and
    mammillary bodies.)
*   **Mammillary body and anterior thalamic pathology:** Harding,
    A., Halliday, G., Caine, D., Kril, J. (2000). "Degeneration
    of anterior thalamic nuclei differentiates alcoholics with
    amnesia." *Brain* 123:141–154. (Anterior thalamic nuclei
    degeneration in alcoholics with amnesia — the
    mammillothalamic tract target.)
*   **Colloid cyst and mammillothalamic tract compression:**
    Pollock, B.E., Schreiner, S.A., Huston, J. (2000). "Colloid
    cysts of the third ventricle: a review of the literature."
    *Neurology* 55:12–15. (Colloid cysts — mammillothalamic tract
    compression and memory deficits.)
*   **Schizophrenia and the mammillothalamic tract (contested):**
    Fitzsimmons, J., Kubicki, M., Shenton, M.E. (2013). "Review
    of functional and anatomical brain connectivity findings in
    schizophrenia." *Current Opinion in Psychiatry* 26:172–187.
    (Mammillothalamic tract DTI abnormalities in schizophrenia —
    contested.)
*   **Multiple sclerosis and the mammillothalamic tract:**
    Roosendaal, S.D., et al. (2010). "Structural and functional
    hippocampal changes in multiple sclerosis." *Radiology*
    256:848–856. (Mammillothalamic tract / hippocampal changes in
    MS.)
*   **Head-direction signal (review):** Taube, J.S. (2007). "The
    head direction signal: origins and sensory-motor
    integration." *Annual Review of Neuroscience* 30:181–207.
    (The head-direction signal — the anterior thalamic nuclei as
    head-direction nodes; the mammillothalamic tract as a possible
    relay.)
*   **White-matter atlas (human):** Wakana, S., Jiang, H., Nagae,
    L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter atlas
    of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the mammillothalamic tract in DTI.)
*   **Mammillothalamic tract in DTI tractography:** Catani, M.,
    Thiebaut de Schotten, M. (2008). "A diffusion tensor imaging
    tractography atlas for virtual in vivo dissections." *Cortex*
    44:1105–1132. (The mammillothalamic tract in DTI
    tractography.)
*   **Mammillothalamic tract in the human connectome:** Catani,
    M., Thiebaut de Schotten, M. (2012). *Atlas of Human Brain
    Connections*. Oxford University Press, Oxford. (The
    mammillothalamic tract in the human connectome.)
*   **Fiber pathways (review):** Schmahmann, J.D., Pandya, D.N.
    (2006). *Fiber Pathways of the Brain*. Oxford University
    Press, New York. (Definitive white-matter anatomy; the
    mammillothalamic tract as a diencephalic projection.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    mammillothalamic tract is not the medial-temporal-lobe
    amnesia substrate):** Scoville, W.B., Milner, B. (1957).
    "Loss of recent memory after bilateral hippocampal
    lesions." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 20:11–21. (Bilateral hippocampal damage and
    anterograde amnesia.)
*   **Amygdala (contrast — the mammillothalamic tract is NOT the
    amygdala):** LeDoux, J.E. (2000). "Emotion circuits in the
    brain." *Annual Review of Neuroscience* 23:155–184.
    (Amygdala fear circuit — distinct from the mammillothalamic
    tract.)
*   **SLEA (contrast — the mammillothalamic tract is not
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral
    pallidum, nucleus accumbens; NOT the mammillothalamic tract.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Mammillothalamic tract in overview.)
*   NeuroNames — Mammillothalamic tract (left); FMA —
    Mammillothalamic tract (left member).
"""