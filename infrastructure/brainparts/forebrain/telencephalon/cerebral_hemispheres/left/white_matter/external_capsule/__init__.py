"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter.external_capsule
=========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── white_matter
                └── external_capsule   <-- THIS MODULE

**Primary synonym:** External capsule (left); capsula externa;
**the capsular white-matter sheet between the putamen and the
claustrum**; **the capsule lateral to the putamen**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **capsular white-matter sheet**
between the **putamen** (medial) and the **claustrum** (lateral),
composed of **association fibers** (the **uncinate fasciculus**,
the **inferior fronto-occipital fasciculus**, and contributions
from the **superior longitudinal fasciculus** and the **inferior
longitudinal fasciculus**) and **corticostriatal** projection
fibers. It is a **specific named white-matter structure** — a
**capsular white-matter sheet**, **not** a region of passage,
**not** a projection-fiber fan, **not** a compact projection-fiber
bundle, **not** an association bundle, **not** a commissural
structure.
**Part of:** The **white_matter** container of the left cerebral
hemisphere — the **capsular white-matter sheet** that **carries**
the association fibers (uncinate fasciculus, inferior
fronto-occipital fasciculus, and contributions from the superior
and inferior longitudinal fasciculi) and the corticostriatal
projection fibers between the **putamen** and the **claustrum**.
**Structural parent:** ``.../left/white_matter/`` → **direct
child** of the white_matter container.
**Structural children:** **None.** This is a **leaf** module. The
**uncinate fasciculus**, the **inferior fronto-occipital
fasciculus**, the **superior longitudinal fasciculus
contribution**, the **inferior longitudinal fasciculus
contribution**, and the **corticostriatal** fibers that pass
through the external capsule are documented as **prose**, not as
structural children.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the external_capsule is WHITE MATTER, NOT a
grey-matter structure.** The **external capsule** (here) is the
**capsular white-matter sheet** between the **putamen** and the
**claustrum** — **myelinated axons** (association and projection
fibers). The **grey-matter structures** that the external capsule
sits **between** — the **putamen** (medial) and the **claustrum**
(lateral) — are **grey matter** and are wired under their own
containers (``.../left/subcortical/basal_ganglia/striatum/
dorsal_striatum/putamen/`` and
``.../left/subcortical/claustrum/``). **They are DIFFERENT
STRUCTURES** — the **external capsule** is the **capsular
white-matter sheet**; the **putamen** and the **claustrum** are
the **grey-matter structures** it **sits between**. Consumers
must **not** conflate the external capsule with any grey-matter
structure.
**Boundary status (CAPSULAR WHITE-MATTER SHEET — NOT a region of
passage, NOT a projection-fiber fan, NOT a compact
projection-fiber bundle, NOT an association bundle, NOT a
commissural structure):** **Boundary case — the external_capsule
is a CAPSULAR WHITE-MATTER SHEET, NOT a region of passage, NOT a
projection-fiber fan, NOT a compact projection-fiber bundle, NOT
an association bundle, NOT a commissural structure.** The
**external capsule** is a **specific capsular white-matter
sheet** — a **defined anatomical structure** whose **defining
bundles** are the **uncinate fasciculus** and the **inferior
fronto-occipital fasciculus** (with contributions from the
superior and inferior longitudinal fasciculi, plus corticostriatal
projection fibers). It is **not** a **region of passage** like
the **centrum semiovale**; it is **not** a **projection-fiber
fan** like the **corona radiata**; it is **not** a **compact
projection-fiber bundle** like the **internal capsule**; it is
**not** an **association bundle** like the **cingulum**; and it
is **not** a **commissural structure** like the **corpus
callosum**. Consumers must **not** treat the external capsule as
"another region of passage" or "another association bundle" — it
is a **capsular white-matter sheet** with its **own position** and
its **own defining bundles**.
**Boundary status (NOT the internal capsule — the internal capsule
is a SIBLING white-matter leaf, and it is a COMPACT
PROJECTION-FIBER BUNDLE medial to the putamen):** **Boundary case
— the external_capsule is NOT the internal capsule; the internal
capsule is a SIBLING white-matter leaf, and it is a COMPACT
PROJECTION-FIBER BUNDLE medial to the putamen.** The **internal
capsule** (``.../left/white_matter/internal_capsule/``) is the
**compact projection-fiber bundle** that passes **between** the
**caudate nucleus**, the **putamen**, the **globus pallidus**, and
the **thalamus** — **medial** to the putamen. The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum** — **lateral** to the
putamen. **They are SIBLINGS under the white_matter container,
and they are DIFFERENT STRUCTURES** — the **internal capsule** is
the **compact projection-fiber bundle** **medial** to the putamen;
the **external capsule** is the **capsular white-matter sheet**
**lateral** to the putamen. **They sit on OPPOSITE SIDES of the
putamen** — the internal capsule on the medial side, the external
capsule on the lateral side. Consumers must **not** conflate the
external capsule with the internal capsule — they are **different
structures on opposite sides of the putamen**.
**Boundary status (NOT the extreme capsule — the extreme capsule is
a SIBLING white-matter leaf, and it is the CAPSULAR WHITE-MATTER
SHEET lateral to the CLAUSTRUM):** **Boundary case — the
external_capsule is NOT the extreme capsule; the extreme capsule
is a SIBLING white-matter leaf, and it is the CAPSULAR
WHITE-MATTER SHEET lateral to the CLAUSTRUM.** The **extreme
capsule** (``.../left/white_matter/extreme_capsule/``) is the
**capsular white-matter sheet** **lateral** to the **claustrum**
— the **thin** white-matter sheet between the **claustrum** and
the **insular cortex**. The **external capsule** (here) is the
**capsular white-matter sheet** **medial** to the claustrum and
**lateral** to the putamen. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** — the
**external capsule** is the **capsular sheet between the putamen
and the claustrum**; the **extreme capsule** is the **capsular
sheet between the claustrum and the insular cortex**. **They are
SEPARATED by the CLAUSTRUM** — the external capsule is **medial**
to the claustrum, the extreme capsule is **lateral** to the
claustrum. Consumers must **not** conflate the external capsule
with the extreme capsule — they are **different capsular sheets
on opposite sides of the claustrum**.
**Boundary status (NOT the claustrum — the claustrum is the
GREY-MATTER structure the external capsule sits MEDIAL to):**
**Boundary case — the external_capsule is NOT the claustrum; the
claustrum is the GREY-MATTER structure the external capsule sits
MEDIAL to.** The **claustrum**
(``.../left/subcortical/claustrum/``) is the **thin grey-matter
sheet** between the **external capsule** (medial) and the
**extreme capsule** (lateral). The **external capsule** (here) is
the **capsular white-matter sheet** **medial** to the claustrum.
**They are DIFFERENT STRUCTURES** — the **claustrum** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately medial** to the
**claustrum**. Consumers must **not** conflate the external
capsule with the claustrum.
**Boundary status (NOT the putamen — the putamen is the GREY-MATTER
structure the external capsule sits LATERAL to):** **Boundary
case — the external_capsule is NOT the putamen; the putamen is the
GREY-MATTER structure the external capsule sits LATERAL to.** The
**putamen**
(``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
putamen/``) is the **grey-matter structure** of the **dorsal
striatum** — the **lateral** part of the **lentiform nucleus**
(with the globus pallidus). The **external capsule** (here) is the
**capsular white-matter sheet** **lateral** to the putamen.
**They are DIFFERENT STRUCTURES** — the **putamen** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately lateral** to the
**putamen**. Consumers must **not** conflate the external capsule
with the putamen.
**Boundary status (NOT the centrum semiovale — the centrum
semiovale is a SIBLING white-matter leaf, and it is a REGION OF
PASSAGE above the level of the lateral ventricles):** **Boundary
case — the external_capsule is NOT the centrum semiovale; the
centrum semiovale is a SIBLING white-matter leaf, and it is a
REGION OF PASSAGE above the level of the lateral ventricles.**
The **centrum semiovale**
(``.../left/white_matter/centrum_semiovale/``) is the
**white-matter mass above the lateral ventricles** — a **region
of passage** that **contains** the corona radiata, the
association fibers, and the callosal radiations as they pass
through it. The **external capsule** (here) is the **capsular
white-matter sheet** between the **putamen** and the
**claustrum** — **inferior** to the main mass of the centrum
semiovale. **They are SIBLINGS under the white_matter container,
and they are DIFFERENT STRUCTURES** — the **centrum semiovale**
is a **region of passage**; the **external capsule** is a
**capsular white-matter sheet**. Consumers must **not** conflate
the external capsule with the centrum semiovale.
**Boundary status (NOT the corona radiata — the corona radiata is
a SIBLING white-matter leaf, and it is a PROJECTION-FIBER FAN):**
**Boundary case — the external_capsule is NOT the corona radiata;
the corona radiata is a SIBLING white-matter leaf, and it is a
PROJECTION-FIBER FAN.** The **corona radiata**
(``.../left/white_matter/corona_radiata/``) is the
**projection-fiber fan** between the **internal capsule** and the
**cortex** — **projection fibers** (corticospinal,
corticobulbar, corticopontine, thalamocortical). The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum** — **association fibers**
(uncinate fasciculus, inferior fronto-occipital fasciculus) and
**corticostriatal** projection fibers. **They are SIBLINGS under
the white_matter container, and they are DIFFERENT STRUCTURES** —
the **corona radiata** is a **projection-fiber fan**; the
**external capsule** is a **capsular white-matter sheet**.
Consumers must **not** conflate the external capsule with the
corona radiata.
**Boundary status (NOT the cingulum — the cingulum is a SIBLING
white-matter leaf, and it is the ASSOCIATION bundle of the
cingulate gyrus):** **Boundary case — the external_capsule is NOT
the cingulum; the cingulum is a SIBLING white-matter leaf, and it
is the ASSOCIATION bundle of the cingulate gyrus.** The
**cingulum** (``.../left/white_matter/cingulum/``) is the
**specific association bundle** that runs **within the cingulate
gyrus** (around the corpus callosum). The **external capsule**
(here) is the **capsular white-matter sheet** between the
**putamen** and the **claustrum**. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** — the
**cingulum** is a **specific named association bundle** with a
**defined course**; the **external capsule** is a **capsular
white-matter sheet**. Consumers must **not** conflate the
external capsule with the cingulum.
**Boundary status (NOT the corpus callosum — the corpus callosum is
wired under ``commissures/``):** **Boundary case — the
external_capsule is NOT the corpus callosum; the corpus callosum
is wired under ``.../left/commissures/corpus_callosum/``.** The
**corpus callosum** (``.../left/commissures/corpus_callosum/``)
is the **commissural structure** — the **midline white-matter
commissure** that connects the two hemispheres. The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum** — **intrahemispheric**
fibers. **They are DIFFERENT STRUCTURES** — the **corpus
callosum** is a **commissural structure** (wired under
``commissures/``); the **external capsule** is an **intrahemispheric
capsular white-matter sheet** (wired under ``white_matter/``).
Consumers must **not** conflate the external capsule with the
corpus callosum.
**Boundary status (NOT the fornix — the fornix is a SIBLING
white-matter leaf, and it is a HIPPOCAMPAL OUTPUT tract):**
**Boundary case — the external_capsule is NOT the fornix; the
fornix is a SIBLING white-matter leaf, and it is a HIPPOCAMPAL
OUTPUT tract.** The **fornix** (``.../left/white_matter/fornix/``)
is the **major output tract** of the hippocampus. The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum**. **They are SIBLINGS under
the white_matter container, and they are DIFFERENT STRUCTURES** —
the **fornix** is a **hippocampal output tract**; the **external
capsule** is a **capsular white-matter sheet**. Consumers must
**not** conflate the external capsule with the fornix.
**Boundary status (NOT the fasciculus rectus, mammillothalamic
tract, or medial forebrain bundle — those are SIBLING
white-matter leaves):** **Boundary case — the external_capsule is
NOT the fasciculus rectus, mammillothalamic tract, or medial
forebrain bundle; those are SIBLING white-matter leaves.** Each
of those is a **specific named white-matter structure** — the
**fasciculus rectus** (a small bundle), the **mammillothalamic
tract** (the mammillary-body → anterior-thalamic projection), and
the **medial forebrain bundle** (a brainstem-forebrain bundle).
**None of them is part of the external capsule** — each is a
**separate leaf** under ``white_matter/``. Consumers must **not**
conflate the external capsule with any of those siblings.
**Boundary status (NOT the cortex — the cortex is the GREY-MATTER
structure at the SUPERFICIAL end of the external capsule):**
**Boundary case — the external_capsule is NOT the cortex; the
cortex is the GREY-MATTER structure at the SUPERFICIAL end of the
external capsule.** The **cortex** (``.../left/cortex/``) is the
**grey-matter sheet** that **caps** the cerebral hemisphere.
The **external capsule** (here) is the **capsular white-matter
sheet** between the **putamen** and the **claustrum** — the
**cortical** end of the **uncinate fasciculus** and the
**inferior fronto-occipital fasciculus** terminates in the
**cortex** (frontal, temporal, occipital). **They are DIFFERENT
STRUCTURES** — the **cortex** is **grey matter**; the **external
capsule** is **white matter**. Consumers must **not** conflate
the external capsule with the cortex.
**Boundary status (NOT the basal ganglia — the basal ganglia are
the GREY-MATTER structures the external capsule sits LATERAL to):**
**Boundary case — the external_capsule is NOT the basal ganglia;
the basal ganglia are the GREY-MATTER structures the external
capsule sits LATERAL to.** The **basal ganglia**
(``.../left/subcortical/basal_ganglia/``) — the **caudate
nucleus**, the **putamen**, the **globus pallidus**, and the
**ventral striatum** — are **grey-matter** structures. The
**external capsule** (here) is the **capsular white-matter
sheet** **lateral** to the **putamen** (one of the basal ganglia
structures). **They are DIFFERENT STRUCTURES** — the **basal
ganglia** are **grey matter**; the **external capsule** is
**white matter**. Consumers must **not** conflate the external
capsule with the basal ganglia.
**Boundary status (NOT the thalamus — the thalamus is a GREY-MATTER
structure MEDIAL to the putamen and the external capsule):**
**Boundary case — the external_capsule is NOT the thalamus; the
thalamus is a GREY-MATTER structure MEDIAL to the putamen and the
external capsule.** The **thalamus**
(``.../left/subcortical/diencephalon/thalamus/``) is a
**grey-matter** structure **medial** to the putamen (via the
internal capsule) — **farther medial** from the external capsule.
The **external capsule** (here) is the **capsular white-matter
sheet** between the **putamen** and the **claustrum**. **They are
DIFFERENT STRUCTURES** — the **thalamus** is **grey matter**;
the **external capsule** is **white matter**. Consumers must
**not** conflate the external capsule with the thalamus.
**Boundary status (NOT the lateral ventricles — the lateral
ventricles are the CSF spaces):** **Boundary case — the
external_capsule is NOT the lateral ventricles; the lateral
ventricles are the CSF spaces.** The **lateral ventricles**
(``.../left/lateral_ventricles/``) are the **CSF-filled spaces**
**medial** to the external capsule (the external capsule is
lateral, near the insular cortex). **They are DIFFERENT
STRUCTURES** — the **lateral ventricles** are **CSF spaces**;
the **external capsule** is **white matter**. Consumers must
**not** conflate the external capsule with the lateral ventricles.
**Boundary status (SLEA-FREE — the external capsule is NOT an
extended-amygdala component):** **Boundary case — the
external_capsule is SLEA-FREE.** The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **external capsule** is a
**capsular white-matter sheet** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the external
capsule — it is **SLEA-free**.
**Boundary status (WHITE-MATTER MODULE — a white-matter module in
the series):** **Boundary case — the external_capsule is a
WHITE-MATTER module in the series.** Every grey-matter module in
the medial_temporal_lobe subtree (amygdala, hippocampus, and their
children) is a **grey-matter** structure — a **nucleus**, a
**cortical region**, or a **CA field**. The **external capsule**
(here) is **white matter** — it is a **white-matter module in the
series**. Consumers must **not** treat the external capsule as
"another grey-matter structure" — it is **white matter**, and the
boundaries that anchored the grey-matter modules ("NOT the white
matter") are **reversed** here ("IS the white matter, NOT the
grey-matter structure").

Overview
--------
The external capsule is the **capsular white-matter sheet between
the putamen and the claustrum** — a **specific named white-matter
tract** whose **defining bundles** are the **uncinate fasciculus**
and the **inferior fronto-occipital fasciculus** (with
contributions from the superior and inferior longitudinal
fasciculi, plus corticostriatal projection fibers). It is a
**leaf** module under the white_matter container, the **sibling
of the centrum semiovale, the cingulum, the corona radiata, the
extreme capsule, the fasciculus rectus, the fornix, the internal
capsule, the mammillothalamic tract, and the medial forebrain
bundle**, and the **white-matter substrate** of the
**intrahemispheric association** between the **frontal**,
**temporal**, and **occipital** cortices.

**The external capsule is WHITE MATTER, NOT a grey-matter
structure.** It is the **capsular white-matter sheet** between the
**putamen** and the **claustrum** — **myelinated axons**
(association and projection fibers). The **grey-matter
structures** it sits **between** — the **putamen** (medial) and
the **claustrum** (lateral) — are **grey matter** and are wired
under their own containers.

**The external capsule is a CAPSULAR WHITE-MATTER SHEET, NOT a
region of passage, NOT a projection-fiber fan, NOT a compact
projection-fiber bundle, NOT an association bundle, NOT a
commissural structure.** It is a **specific capsular white-matter
sheet** whose **defining bundles** are the **uncinate
fasciculus** and the **inferior fronto-occipital fasciculus**
(with contributions from the superior and inferior longitudinal
fasciculi, plus corticostriatal projection fibers).

**The external capsule is NOT the internal capsule.** The
**internal capsule** (sibling) is the **compact projection-fiber
bundle** **medial** to the putamen. The **external capsule** is
the **capsular white-matter sheet** **lateral** to the putamen.
**They sit on OPPOSITE SIDES of the putamen** — **they are
SIBLINGS under the white_matter container**.

**The external capsule is NOT the extreme capsule.** The **extreme
capsule** (sibling) is the **capsular white-matter sheet**
**lateral** to the **claustrum** (between the claustrum and the
insular cortex). The **external capsule** is the **capsular
white-matter sheet** **medial** to the claustrum (between the
putamen and the claustrum). **They are SEPARATED by the
CLAUSTRUM** — **they are SIBLINGS under the white_matter
container**.

**The external capsule is NOT the claustrum.** The **claustrum**
(``.../left/subcortical/claustrum/``) is the **thin grey-matter
sheet** between the **external capsule** (medial) and the
**extreme capsule** (lateral). The **external capsule** sits
**immediately medial** to the **claustrum**.

**The external capsule is NOT the putamen.** The **putamen**
(``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
putamen/``) is the **grey-matter structure** of the **dorsal
striatum**. The **external capsule** sits **immediately lateral**
to the **putamen**.

**The external capsule is NOT the centrum semiovale.** The
**centrum semiovale** (sibling) is the **white-matter mass above
the lateral ventricles** — a **region of passage** that
**contains** the corona radiata, the association fibers, and the
callosal radiations as they pass through it. The **external
capsule** is **inferior** to the main mass of the centrum
semiovale. **They are SIBLINGS under the white_matter container.**

**The external capsule is NOT the corona radiata.** The **corona
radiata** (sibling) is a **projection-fiber fan** — the
corticospinal, corticobulbar, corticopontine, and thalamocortical
fibers. The **external capsule** is a **capsular white-matter
sheet** — the uncinate fasciculus, the inferior fronto-occipital
fasciculus, and corticostriatal projection fibers. **They are
SIBLINGS under the white_matter container.**

**The external capsule is NOT the cingulum.** The **cingulum**
(sibling) is the **specific association bundle** of the
cingulate gyrus — a **defined course** running within the
cingulate gyrus. The **external capsule** is a **capsular
white-matter sheet** between the putamen and the claustrum. **They
are SIBLINGS under the white_matter container.**

**The external capsule is NOT the corpus callosum.** The **corpus
callosum** is the **commissural structure** — wired under
``.../left/commissures/corpus_callosum/``. The **external
capsule** is an **intrahemispheric** capsular white-matter sheet
— wired under ``white_matter/``.

**The external capsule is NOT the fornix.** The **fornix**
(sibling) is the **hippocampal output tract** — the **major
output tract** of the hippocampus. The **external capsule** is a
**capsular white-matter sheet**. **They are SIBLINGS under the
white_matter container.**

**The external capsule is NOT the cortex, the basal ganglia, or
the thalamus.** Those are **grey-matter structures** — the
external capsule is the **capsular white-matter sheet** that
**connects** the cortex to the basal ganglia and carries
association fibers.

**The external capsule is NOT the lateral ventricles.** The
**lateral ventricles** are the **CSF-filled spaces** **medial**
to the external capsule.

**The external capsule is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere).

**The external capsule is a paired structure.** Each hemisphere
has its own external capsule, with **ipsilateral** connections to
the putamen, the claustrum, the insular cortex, and the frontal,
temporal, and occipital cortices. The two sides are **bilaterally
symmetric** — the external capsule is a **white-matter tract**,
and its **gross anatomy** is **symmetric**; there is **no
functional lateralization** of the external capsule per se. The
**functional lateralization** belongs to the **cortical
grey-matter structures** whose fibers pass through it (see
*Lateralization Notes*).

Fiber Composition (prose, not structural children)
--------------------------------------------------
The external capsule is a **capsular white-matter sheet** —
documented as **prose**, not as structural children:

*   **Uncinate fasciculus** — the **association bundle** that
    connects the **anterior temporal lobe** (uncus, parahippocampal
    gyrus, anterior temporal pole) to the **orbitofrontal** and
    **ventrolateral prefrontal** cortices. The **uncinate
    fasciculus** is one of the **defining bundles** of the
    external capsule — it **curves** around the **lateral
    sulcus** (the **limen insulae**) and passes through the
    **external capsule** on its way from the **temporal pole**
    to the **orbitofrontal** cortex.

*   **Inferior fronto-occipital fasciculus (IFOF)** — the
    **association bundle** that connects the **frontal lobe**
    (dorsolateral prefrontal, ventrolateral prefrontal,
    orbitofrontal) to the **occipital** and **posterior
    temporal** cortices. The **IFOF** is one of the **defining
    bundles** of the external capsule — it passes through the
    **external capsule** on its way from the **frontal** to the
    **occipital** cortex. The **IFOF** is the **ventral**
    association bundle that parallels the **superior
    longitudinal fasciculus** (dorsal).

*   **Superior longitudinal fasciculus (SLF) contribution** — the
    **superior longitudinal fasciculus** (SLF) is primarily a
    **dorsal** association bundle (the **arcuate fasciculus**
    is its **most posterior** component), but **some** of its
    fibers (especially the **SLF II** and **SLF III** components)
    pass through the **external capsule** **anteriorly** (near the
    **frontal operculum**).

*   **Inferior longitudinal fasciculus (ILF) contribution** — the
    **inferior longitudinal fasciculus** (ILF) is the **ventral**
    association bundle that connects the **occipital** to the
    **anterior temporal** lobe. **Some** of its fibers pass
    through the **posterior** part of the **external capsule**
    (near the **temporal** and **occipital** ends).

*   **Corticostriatal fibers** — the **projection fibers** that
    connect the **cerebral cortex** to the **striatum** (caudate
    nucleus, putamen). The **corticostriatal** fibers pass through
    the **external capsule** on their way from the cortex to
    the **striatum**. These are **projection fibers**, not
    association fibers.

**These fiber groups are prose, not structural children.** The
tree wires the **external capsule** as a **single leaf** under
``white_matter/`` — the **uncinate fasciculus**, the **inferior
fronto-occipital fasciculus**, the **SLF contribution**, the
**ILF contribution**, and the **corticostriatal** fibers are
**prose**, not structural children. Consumers that need
**fiber-level** resolution should consult the references, not the
tree.

The External Capsule / Internal Capsule Boundary
------------------------------------------------
This is the **most consequential sibling boundary** — the
**capsular white-matter sheet lateral to the putamen vs. the
compact projection-fiber bundle medial to the putamen** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the **putamen** (medial) and the
    **claustrum** (lateral).

*   **Internal_capsule**
    (``.../left/white_matter/internal_capsule/``) — the
    **compact projection-fiber bundle** that passes **between**
    the **caudate nucleus**, the **putamen**, the **globus
    pallidus**, and the **thalamus** — **medial** to the
    putamen.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **internal capsule** is the
**compact projection-fiber bundle** **medial** to the putamen;
the **external capsule** is the **capsular white-matter sheet**
**lateral** to the putamen. **They sit on OPPOSITE SIDES of the
putamen** — the internal capsule on the medial side, the external
capsule on the lateral side. Consumers must **not** conflate the
external capsule with the internal capsule — they are **different
structures on opposite sides of the putamen**.

The External Capsule / Extreme Capsule Boundary
-----------------------------------------------
This is the **second-most consequential sibling boundary** — the
**capsular sheet medial to the claustrum vs. capsular sheet
lateral to the claustrum** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **medial** to the **claustrum** (between
    the putamen and the claustrum).

*   **Extreme_capsule**
    (``.../left/white_matter/extreme_capsule/``) — the
    **capsular white-matter sheet** **lateral** to the
    **claustrum** (between the claustrum and the insular
    cortex).

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **external capsule** is the
**capsular sheet between the putamen and the claustrum**; the
**extreme capsule** is the **capsular sheet between the claustrum
and the insular cortex**. **They are SEPARATED by the CLAUSTRUM**
— the external capsule is **medial** to the claustrum, the
extreme capsule is **lateral** to the claustrum. Consumers must
**not** conflate the external capsule with the extreme capsule —
they are **different capsular sheets on opposite sides of the
claustrum**.

The External Capsule / Claustrum Boundary
-----------------------------------------
This is the **white matter vs. grey matter** boundary — the
claustrum is the **grey-matter sheet** the external capsule sits
**medial** to:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **medial** to the claustrum.

*   **Claustrum** (``.../left/subcortical/claustrum/``) — the
    **thin grey-matter sheet** between the **external capsule**
    (medial) and the **extreme capsule** (lateral).

**They are DIFFERENT STRUCTURES** — the **claustrum** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately medial** to the
**claustrum**. Consumers must **not** conflate the external
capsule with the claustrum.

The External Capsule / Putamen Boundary
---------------------------------------
This is the **white matter vs. grey matter** boundary — the
putamen is the **grey-matter structure** the external capsule sits
**lateral** to:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **lateral** to the putamen.

*   **Putamen**
    (``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
    putamen/``) — the **grey-matter structure** of the **dorsal
    striatum** — the **lateral** part of the **lentiform
    nucleus**.

**They are DIFFERENT STRUCTURES** — the **putamen** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately lateral** to the
**putamen**. Consumers must **not** conflate the external capsule
with the putamen.

The External Capsule / Centrum Semiovale Boundary
-------------------------------------------------
This is the **capsular white-matter sheet vs. region of passage**
boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Centrum_semiovale**
    (``.../left/white_matter/centrum_semiovale/``) — the
    **white-matter mass above the lateral ventricles** — a
    **region of passage** that **contains** the corona radiata,
    the association fibers, and the callosal radiations as they
    pass through it.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **centrum semiovale** is a **region
of passage**; the **external capsule** is a **capsular
white-matter sheet** **inferior** to the main mass of the centrum
semiovale. Consumers must **not** conflate the external capsule
with the centrum semiovale.

The External Capsule / Corona Radiata Boundary
----------------------------------------------
This is the **capsular white-matter sheet vs. projection-fiber
fan** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Corona_radiata**
    (``.../left/white_matter/corona_radiata/``) — the
    **projection-fiber fan** between the internal capsule and the
    cortex.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **corona radiata** is a
**projection-fiber fan**; the **external capsule** is a
**capsular white-matter sheet**. Consumers must **not** conflate
the external capsule with the corona radiata.

The External Capsule / Cingulum Boundary
----------------------------------------
This is the **capsular white-matter sheet vs. association bundle**
boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Cingulum** (``.../left/white_matter/cingulum/``) — the
    **specific association bundle** of the cingulate gyrus.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **cingulum** is a **specific named
association bundle** with a **defined course**; the **external
capsule** is a **capsular white-matter sheet**. Consumers must
**not** conflate the external capsule with the cingulum.

The External Capsule / Corpus Callosum Boundary
-----------------------------------------------
This is the **capsular white-matter sheet vs. commissural
structure** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Corpus_callosum**
    (``.../left/commissures/corpus_callosum/``) — the
    **commissural structure** that connects the two hemispheres —
    wired under ``commissures/``, **not** under
    ``white_matter/``.

**They are DIFFERENT STRUCTURES** — the **corpus callosum** is a
**commissural structure** (wired under ``commissures/``); the
**external capsule** is an **intrahemispheric capsular
white-matter sheet** (wired under ``white_matter/``). Consumers
must **not** conflate the external capsule with the corpus
callosum.

The External Capsule / Fornix Boundary
--------------------------------------
This is the **capsular white-matter sheet vs. hippocampal output
tract** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Fornix** (``.../left/white_matter/fornix/``) — the **major
    output tract** of the hippocampus.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **fornix** is a **hippocampal output
tract**; the **external capsule** is a **capsular white-matter
sheet**. Consumers must **not** conflate the external capsule with
the fornix.

The External Capsule / Other White-Matter Leaves Boundary
--------------------------------------------------------
This is the **capsular white-matter sheet vs. other named
white-matter structures** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Fasciculus rectus**, **mammillothalamic tract**, **medial
    forebrain bundle** — the **other named white-matter leaves**
    under ``white_matter/``.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — each of those is a **specific named
white-matter structure**; the **external capsule** is a
**capsular white-matter sheet**. **None of those is part of the
external capsule** — each is a **separate leaf** under
``white_matter/``. Consumers must **not** conflate the external
capsule with any of those siblings.

The External Capsule / Cortex Boundary
--------------------------------------
This is the **white matter vs. grey matter** boundary at the
superficial end of the external capsule:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Cortex** (``.../left/cortex/``) — the **grey-matter sheet**
    that **caps** the cerebral hemisphere.

**They are DIFFERENT STRUCTURES** — the **cortex** is **grey
matter**; the **external capsule** is **white matter** — the
**association fibers** (uncinate fasciculus, inferior
fronto-occipital fasciculus) **terminate** in the **cortex**.
Consumers must **not** conflate the external capsule with the
cortex.

The External Capsule / Basal Ganglia Boundary
---------------------------------------------
This is the **white matter vs. grey matter** boundary — the
external capsule sits **lateral** to the putamen:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **lateral** to the putamen.

*   **Basal ganglia** (``.../left/subcortical/basal_ganglia/``) —
    the **grey-matter structures** (caudate nucleus, putamen,
    globus pallidus, ventral striatum).

**They are DIFFERENT STRUCTURES** — the **basal ganglia** are
**grey matter**; the **external capsule** is **white matter**.
Consumers must **not** conflate the external capsule with the
basal ganglia.

The External Capsule / Thalamus Boundary
----------------------------------------
This is the **white matter vs. grey matter** boundary — the
thalamus is **medial** to the putamen (farther medial from the
external capsule):

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **lateral** to the putamen.

*   **Thalamus** (``.../left/subcortical/diencephalon/thalamus/``)
    — the **grey-matter structure** **medial** to the putamen.

**They are DIFFERENT STRUCTURES** — the **thalamus** is **grey
matter**; the **external capsule** is **white matter**. Consumers
must **not** conflate the external capsule with the thalamus.

The External Capsule / Lateral Ventricles Boundary
--------------------------------------------------
This is the **white matter vs. CSF space** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum
    (lateral, near the insular cortex).

*   **Lateral ventricles** (``.../left/lateral_ventricles/``) — the
    **CSF-filled spaces** **medial** to the external capsule.

**They are DIFFERENT STRUCTURES** — the **lateral ventricles** are
**CSF spaces**; the **external capsule** is **white matter**.
Consumers must **not** conflate the external capsule with the
lateral ventricles.

The External Capsule / White Matter Container Boundary
------------------------------------------------------
This is the **child vs. container** boundary:

*   **External_capsule** (this module) — a **child** of the
    white_matter container.

*   **White_matter** (``.../left/white_matter/``) — the
    **container** that contains the **centrum semiovale**, the
    **cingulum**, the **corona radiata**, the **external
    capsule**, the **extreme capsule**, the **fasciculus rectus**,
    the **fornix**, the **internal capsule**, the
    **mammillothalamic tract**, and the **medial forebrain
    bundle**.

**The external capsule is ONE of the ten children of the
white_matter container.** Consumers must **not** conflate the
external capsule with the white_matter container.

The External Capsule / Cerebral Hemisphere Boundary
---------------------------------------------------
This is the **grandchild vs. container** boundary:

*   **External_capsule** (this module) — a **grandchild** of the
    ``.../left/`` (cerebral hemisphere) container.

*   **``.../left/``** — the **cerebral hemisphere container** that
    contains the **cortex**, the **rhinencephalon**, the
    **subcortical** structures, the **white_matter**, the
    **commissures**, and the **lateral_ventricles**.

**The external capsule is a grandchild of the cerebral hemisphere**
(child of the white_matter container). Consumers must **not**
conflate the external capsule with the cerebral hemisphere
container.

The External Capsule / SLEA Boundary
------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **External_capsule** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The external capsule is NOT part of the SLEA continuum.** It is a
**capsular white-matter sheet**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
external capsule.

Function in the Human Brain
---------------------------
The external capsule's functions are **intrahemispheric
association** and **corticostriatal projection** — **NOT a
grey-matter function**:

*   **Uncinate Fasciculus (Temporal → Frontal Association):** The
    **external capsule** carries the **uncinate fasciculus** —
    the association bundle that connects the **anterior temporal
    lobe** to the **orbitofrontal** and **ventrolateral
    prefrontal** cortices. This is the **temporal-prefrontal
    association** substrate of the external capsule — a
    **limbic / paralimbic** association bundle implicated in
    **emotion regulation**, **social cognition**, and
    **episodic memory retrieval**.

*   **Inferior Fronto-Occipital Fasciculus (Frontal → Occipital
    Association):** The **external capsule** carries the
    **inferior fronto-occipital fasciculus** — the association
    bundle that connects the **frontal lobe** to the
    **occipital** and **posterior temporal** cortices. This is
    the **frontal-occipital association** substrate of the
    external capsule — a **ventral** association bundle
    implicated in **semantic processing**, **visual
    recognition**, and **reading**.

*   **Superior Longitudinal Fasciculus Contribution (Frontal →
    Parietal / Temporal):** The **external capsule** carries a
    contribution from the **superior longitudinal fasciculus**
    — the dorsal association bundle (the **arcuate fasciculus**
    is its most posterior component). This is the
    **frontal-parietal / temporal association** substrate of
    the external capsule.

*   **Inferior Longitudinal Fasciculus Contribution (Occipital →
    Temporal):** The **external capsule** carries a contribution
    from the **inferior longitudinal fasciculus** — the ventral
    association bundle that connects the **occipital** to the
    **anterior temporal** lobe. This is the **occipital-temporal
    association** substrate of the external capsule.

*   **Corticostriatal Projection (Cortex → Striatum):** The
    **external capsule** carries the **corticostriatal** fibers
    — the projection fibers from the **cerebral cortex** to the
    **striatum** (caudate nucleus, putamen). This is the
    **corticostriatal** substrate of the external capsule.

*   **NOT a neural processor in the classical sense.** The
    **external capsule** is a **capsular white-matter sheet** —
    it **conducts** the **association fibers** and the
    **corticostriatal projection fibers**, but it does **not**
    **process** information (that happens in the **grey-matter
    structures** — the cortex, the putamen, the claustrum). The
    **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the external capsule is the **capsular
white-matter sheet** of the **cerebral hemisphere** — the
**specific named white-matter tract** that anchors the
**intrahemispheric association** (uncinate fasciculus, inferior
fronto-occipital fasciculus) and the **corticostriatal
projection**. It is **SLEA-free**, **white-matter**, and **NOT a
grey-matter structure** — the **grey-matter structures** are the
**putamen**, the **claustrum**, and the **cortex** whose fibers
pass through it.

Associated Disorders
--------------------
The external capsule has **no named "external capsule syndrome"**
in the narrow sense, but its clinical associations are
**well-documented** — primarily as a **white-matter imaging
target** and as an **association-tract** structure:

*   **Multiple Sclerosis (External Capsule Plaques):** The
    **external capsule** is a **site** of **MS plaques** — the
    **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**. The **external capsule**
    is the **white-matter substrate** of **MS lesions**.

*   **White-Matter Hyperintensities (Leukoaraiosis / Small-Vessel
    Disease):** The **external capsule** is a **site** of
    **white-matter hyperintensities** — the **T2/FLAIR
    hyperintensities** that are the **radiological hallmark** of
    **small-vessel disease**, **aging**, and **vascular
    dementia**.

*   **Uncinate Fasciculus Disconnection (Emotion Regulation /
    Social Cognition):** The **uncinate fasciculus** —
    the **defining bundle** of the **anterior external
    capsule** — is implicated in **emotion regulation** and
    **social cognition**. **Uncinate fasciculus DTI
    abnormalities** are reported in **psychopathy**,
    **antisocial personality disorder**, and **frontotemporal
    dementia**.

*   **Inferior Fronto-Occipital Fasciculus Disconnection (Semantic
    Processing / Reading):** The **inferior fronto-occipital
    fasciculus** — the **defining bundle** of the **posterior
    external capsule** — is implicated in **semantic processing**
    and **reading**. **IFOF DTI abnormalities** are reported in
    **semantic dementia** and in **developmental dyslexia**.

*   **Glioblastoma and White-Matter Tumor Infiltration:** The
    **external capsule** is a **common site** of **glioblastoma**
    and other **white-matter tumors** — the **infiltrative**
    tumor cells **spread** along the association fibers of the
    external capsule.

*   **No Named "External Capsule Syndrome":** The **external
    capsule** is a **capsular white-matter sheet**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** as a
    **white-matter imaging target** (MS, leukoaraiosis,
    glioblastoma), and **indirect** for the **association
    bundles** it carries (uncinate fasciculus, inferior
    fronto-occipital fasciculus).

**What is NOT here:** The **external capsule** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as a **white-matter imaging target**, and **indirect**
for the **association bundles** it carries.

Lateralization Notes
--------------------
This is the **left** external_capsule module. The **external
capsule** is **bilaterally symmetric** — and it carries **NO
warning**:

*   **Bilateral White-Matter Anatomy:** Each hemisphere has its
    own external capsule. The two sides are **grossly symmetric**
    — the external capsule is a **white-matter tract**, and its
    **gross anatomy** is **symmetric**. There is **no functional
    lateralization** of the external capsule per se.

*   **NO Functional Lateralization of the White-Matter Tract:**
    The **functional lateralization** belongs to the **cortical
    grey-matter structures** whose fibers pass through the
    external capsule (e.g., the **left-hemisphere language areas**
    via the **uncinate fasciculus** and the **inferior
    fronto-occipital fasciculus**, the **right-hemisphere
    emotion-regulation areas** via the **uncinate fasciculus**)
    — **not** to the external capsule itself. Consumers must
    **not** assume the external capsule carries a **functional
    lateralization** of its own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    external_capsule is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the external capsule.

*   **NO Amygdala-Lateralization Warning of their own (the
    external capsule is a CAPSULAR WHITE-MATTER SHEET, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **external capsule** is a
    **capsular white-matter sheet** — consumers must **not**
    conflate it with the **whole amygdala** or with the
    **central nucleus**.

**A consumer that assumes "left external capsule = right external
capsule" will be structurally correct** — the two sides are
**symmetric** (the external capsule is a **white-matter tract**,
and its **gross anatomy** is **symmetric**). The **external
capsule** is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no amygdala-lateralization warning of their own**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../left/white_matter/centrum_semiovale/``,
    ``.../left/white_matter/cingulum/``,
    ``.../left/white_matter/corona_radiata/``,
    ``.../left/white_matter/extreme_capsule/``,
    ``.../left/white_matter/fasciculus_rectus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/white_matter/internal_capsule/``,
    ``.../left/white_matter/mammillothalamic_tract/``,
    ``.../left/white_matter/medial_forebrain_bundle/``,
    ``.../left/cortex/``, ``.../left/commissures/``,
    ``.../left/subcortical/basal_ganglia/``,
    ``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
    putamen/``, ``.../left/subcortical/claustrum/``,
    ``.../left/subcortical/diencephalon/thalamus/``,
    ``.../left/lateral_ventricles/``, or any other container. The
    **external capsule**'s relationships to the other white-matter
    leaves, the cortex, the corpus callosum, the basal ganglia,
    the putamen, the claustrum, the thalamus, and the lateral
    ventricles are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **uncinate
    fasciculus**, the **inferior fronto-occipital fasciculus**,
    the **superior longitudinal fasciculus contribution**, the
    **inferior longitudinal fasciculus contribution**, and the
    **corticostriatal** fibers are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve fiber-level detail through the references.
*   **WHITE MATTER — NOT a grey-matter structure.** The **external
    capsule** is **white matter**; the **putamen**, the
    **claustrum**, the **cortex**, the **basal ganglia**, and the
    **thalamus** are **grey matter**. Consumers must **not**
    conflate the external capsule with any grey-matter structure.
*   **CAPSULAR WHITE-MATTER SHEET — NOT a region of passage, NOT a
    projection-fiber fan, NOT a compact projection-fiber bundle,
    NOT an association bundle, NOT a commissural structure.** The
    **external capsule** is a **capsular white-matter sheet**
    whose **defining bundles** are the **uncinate fasciculus**
    and the **inferior fronto-occipital fasciculus**.
*   **NOT the internal capsule — the internal capsule is a SIBLING
    white-matter leaf, and it is a COMPACT PROJECTION-FIBER
    BUNDLE MEDIAL to the putamen.** The **external capsule** is
    the **capsular white-matter sheet LATERAL to the putamen**.
    They are **on opposite sides of the putamen** — not the same
    structure.
*   **NOT the extreme capsule — the extreme capsule is a SIBLING
    white-matter leaf, and it is the CAPSULAR WHITE-MATTER SHEET
    LATERAL to the CLAUSTRUM.** The **external capsule** is the
    **capsular white-matter sheet MEDIAL to the claustrum**. They
    are **separated by the claustrum** — not the same structure.
*   **NOT the claustrum — the claustrum is the GREY-MATTER
    structure the external capsule sits MEDIAL to.**
*   **NOT the putamen — the putamen is the GREY-MATTER structure
    the external capsule sits LATERAL to.**
*   **NOT the centrum semiovale — the centrum semiovale is a
    SIBLING white-matter leaf, and it is a REGION OF PASSAGE above
    the level of the lateral ventricles.** Consumers must **not**
    conflate the external capsule with the centrum semiovale.
*   **NOT the corona radiata — the corona radiata is a SIBLING
    white-matter leaf, and it is a PROJECTION-FIBER FAN.**
*   **NOT the cingulum — the cingulum is a SIBLING white-matter
    leaf, and it is the ASSOCIATION bundle of the cingulate
    gyrus.**
*   **NOT the corpus callosum — the corpus callosum is wired under
    ``commissures/``.**
*   **NOT the fornix — the fornix is a SIBLING white-matter leaf,
    and it is a HIPPOCAMPAL OUTPUT tract.**
*   **NOT the fasciculus rectus, mammillothalamic tract, or medial
    forebrain bundle — those are SIBLING white-matter leaves.**
*   **NOT the cortex, basal ganglia, or thalamus — those are
    GREY-MATTER structures.**
*   **NOT the lateral ventricles — the lateral ventricles are CSF
    spaces.**
*   **NOT the white_matter container — the external capsule is a
    CHILD of the white_matter container.**
*   **NOT the cerebral hemisphere container — the external capsule
    is a GRANDCHILD of the ``.../left/`` container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The external
    capsule is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **external capsule** is a **capsular white-matter sheet**.
*   **No ``AREA_PATHS`` hop.** The **external capsule** is a local
    leaf under ``white_matter/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **external capsule** has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with right external capsule — strict
    mirror with NO warning.** Left and right external capsule
    modules are **structurally identical** — same **leaf** status,
    same **capsular-white-matter-sheet** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter import external_capsule

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.white_matter."
        "external_capsule"
    )

**Do not** assume the external capsule is the **internal capsule**.
The **internal capsule** is a **sibling** white-matter leaf — the
**compact projection-fiber bundle** **medial** to the putamen.
The **external capsule** is the **capsular white-matter sheet**
**lateral** to the putamen. **They sit on opposite sides of the
putamen.**

**Do not** assume the external capsule is the **extreme capsule**.
The **extreme capsule** is a **sibling** white-matter leaf — the
**capsular white-matter sheet** **lateral** to the **claustrum**
(between the claustrum and the insular cortex). The **external
capsule** is the **capsular white-matter sheet** **medial** to the
claustrum. **They are separated by the claustrum.**

**Do not** assume the external capsule is the **claustrum**. The
**claustrum** is the **grey-matter sheet** the external capsule
sits **medial** to.

**Do not** assume the external capsule is the **putamen**. The
**putamen** is the **grey-matter structure** the external capsule
sits **lateral** to.

**Do not** assume the external capsule is the **centrum
semiovale**. The **centrum semiovale** is a **sibling**
white-matter leaf — a **region of passage** above the level of
the lateral ventricles.

**Do not** assume the external capsule is the **corona radiata**.
The **corona radiata** is a **sibling** white-matter leaf — a
**projection-fiber fan**.

**Do not** assume the external capsule is the **cingulum**. The
**cingulum** is a **sibling** white-matter leaf — the
**association bundle** of the cingulate gyrus.

**Do not** assume the external capsule is the **corpus callosum**.
The **corpus callosum** is wired under ``commissures/`` — the
**commissural structure**.

**Do not** assume the external capsule is the **fornix**. The
**fornix** is a **sibling** white-matter leaf — the **hippocampal
output tract**.

**Do not** assume the external capsule is **any** of the other
white-matter siblings — the **fasciculus rectus**, the
**mammillothalamic tract**, or the **medial forebrain bundle**.
Those are **separate leaves** under ``white_matter/``.

**Do not** assume the external capsule is the **cortex**, the
**basal ganglia**, or the **thalamus**. Those are **grey-matter
structures** — the external capsule is the **capsular
white-matter sheet** that **connects** them.

**Do not** assume the external capsule is the **lateral
ventricles**. The **lateral ventricles** are **CSF spaces** —
the external capsule is **lateral**, near the insular cortex.

**Do not** assume the external capsule is the **white_matter
container**. The **white_matter** container contains the
**external capsule** and the other nine white-matter leaves — the
**external capsule** is **one** of those ten children.

**Do not** assume the external capsule is the **cerebral
hemisphere container**. The **external capsule** is a
**grandchild** of the ``.../left/`` container (child of the
white_matter container).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the external capsule.
**The external capsule is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the external capsule's (empty) children (recommended
consumer pattern)::

    EXTERNAL_CAPSULE_CHILDREN = ()
    # The external capsule is a leaf. The uncinate fasciculus, the
    # inferior fronto-occipital fasciculus, the superior
    # longitudinal fasciculus contribution, the inferior
    # longitudinal fasciculus contribution, and the corticostriatal
    # fibers are prose, not modules.

Reaching the internal capsule sibling (recommended consumer
pattern — the compact projection-fiber bundle medial to the
putamen)::

    # The internal capsule is the COMPACT PROJECTION-FIBER BUNDLE
    # MEDIAL to the putamen — the SIBLING of the external capsule
    # under the white_matter container:
    #
    #   white_matter.internal_capsule
    #
    # The internal capsule is medial to the putamen; the external
    # capsule is lateral to the putamen. They are on opposite sides
    # of the putamen.

Reaching the extreme capsule sibling (recommended consumer pattern
— the capsular white-matter sheet lateral to the claustrum)::

    # The extreme capsule is the CAPSULAR WHITE-MATTER SHEET LATERAL
    # to the CLAUSTRUM — the SIBLING of the external capsule under
    # the white_matter container:
    #
    #   white_matter.extreme_capsule
    #
    # The external capsule is medial to the claustrum; the extreme
    # capsule is lateral to the claustrum. They are separated by
    # the claustrum.

Reaching the claustrum (recommended consumer pattern — the
grey-matter sheet between the external and extreme capsules)::

    # The claustrum is the GREY-MATTER SHEET between the external
    # capsule (medial) and the extreme capsule (lateral):
    #
    #   left.subcortical.claustrum
    #
    # The claustrum is grey matter; the external capsule is white
    # matter — the external capsule sits immediately medial to the
    # claustrum.

Reaching the putamen (recommended consumer pattern — the
grey-matter structure medial to the external capsule)::

    # The putamen is the GREY-MATTER STRUCTURE of the DORSAL
    # STRIATUM, MEDIAL to the external capsule:
    #
    #   left.subcortical.basal_ganglia.striatum.dorsal_striatum.putamen
    #
    # The putamen is grey matter; the external capsule is white
    # matter — the external capsule sits immediately lateral to the
    # putamen.

Reaching the centrum semiovale sibling (recommended consumer
pattern — the region of passage)::

    # The centrum semiovale is the WHITE-MATTER MASS ABOVE THE
    # LATERAL VENTRICLES — the SIBLING of the external capsule under
    # the white_matter container:
    #
    #   white_matter.centrum_semiovale
    #
    # The centrum semiovale is a region of passage; the external
    # capsule is a capsular white-matter sheet.

Reaching the corona radiata sibling (recommended consumer pattern —
the projection-fiber fan)::

    # The corona radiata is the PROJECTION-FIBER FAN — the SIBLING
    # of the external capsule under the white_matter container:
    #
    #   white_matter.corona_radiata
    #
    # The corona radiata is a projection-fiber fan; the external
    # capsule is a capsular white-matter sheet.

Reaching the cingulum sibling (recommended consumer pattern — the
association bundle of the cingulate gyrus)::

    # The cingulum is the ASSOCIATION BUNDLE of the CINGULATE GYRUS
    # — the SIBLING of the external capsule under the white_matter
    # container:
    #
    #   white_matter.cingulum
    #
    # The cingulum is a specific named association bundle with a
    # defined course; the external capsule is a capsular white-
    # matter sheet.

Reaching the fornix sibling (recommended consumer pattern — the
hippocampal output tract)::

    # The fornix is the HIPPOCAMPAL OUTPUT TRACT — the SIBLING of
    # the external capsule under the white_matter container:
    #
    #   white_matter.fornix
    #
    # The fornix is a hippocampal output tract; the external capsule
    # is a capsular white-matter sheet.

Reaching the corpus callosum (recommended consumer pattern — the
commissural structure, NOT under white_matter/)::

    # The corpus callosum is the COMMISSURAL STRUCTURE — wired
    # under ``commissures/``, NOT under ``white_matter/``:
    #
    #   left.commissures.corpus_callosum
    #
    # The corpus callosum is a commissural structure; the external
    # capsule is an intrahemispheric capsular white-matter sheet.

Reaching the cortex (recommended consumer pattern — the grey-matter
sheet at the superficial end of the external capsule)::

    # The cortex is the GREY-MATTER SHEET that caps the hemisphere —
    # the structure the external capsule's association fibers
    # terminate in:
    #
    #   left.cortex
    #
    # The cortex is grey matter; the external capsule is white
    # matter — the association fibers (uncinate fasciculus,
    # inferior fronto-occipital fasciculus) terminate in the
    # cortex.

Reaching the white_matter container (recommended consumer pattern —
the container)::

    # The white_matter container contains the external capsule and
    # the other nine white-matter leaves:
    #
    #   left.white_matter
    #
    # The external capsule is ONE of the ten children of the
    # white_matter container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the external capsule is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the external
    # capsule:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The external capsule is SLEA-FREE.

Fiber-level detail (not wired — consult references)::

    # The external capsule's fiber groups are prose, not modules:
    #   uncinate fasciculus                   -> anterior temporal
    #                                             lobe to the
    #                                             orbitofrontal and
    #                                             ventrolateral
    #                                             prefrontal
    #                                             cortices
    #   inferior fronto-occipital fasciculus  -> frontal lobe to
    #                                             the occipital and
    #                                             posterior temporal
    #                                             cortices
    #   superior longitudinal fasciculus
    #     contribution                        -> frontal-parietal /
    #                                             temporal (anterior
    #                                             contribution,
    #                                             especially SLF II
    #                                             and SLF III)
    #   inferior longitudinal fasciculus
    #     contribution                        -> occipital to
    #                                             anterior temporal
    #                                             (posterior
    #                                             contribution)
    #   corticostriatal fibers                -> cerebral cortex
    #                                             to the striatum
    #                                             (caudate nucleus,
    #                                             putamen)
    #
    # Do not attempt to resolve these as sub-paths of the external
    # capsule.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ec_path = (
            f"telencephalon.cerebral_hemispheres.{side}.white_matter."
            f"external_capsule"
        )
        # resolve ec_path through the memory/recall layer

References
----------
*   **Canonical white-matter anatomy:** Wakana, S., Jiang, H.,
    Nagae, L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter
    atlas of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the external capsule and its association fibers.)
*   **External capsule anatomy (review):** Schmahmann, J.D.,
    Pandya, D.N. (2006). *Fiber Pathways of the Brain*. Oxford
    University Press, New York. (Definitive white-matter anatomy;
    the external capsule — the uncinate fasciculus, the inferior
    fronto-occipital fasciculus, and the relationship to the
    internal and extreme capsules.)
*   **External capsule in the human connectome:** Catani, M.,
    Thiebaut de Schotten, M. (2012). *Atlas of Human Brain
    Connections*. Oxford University Press, Oxford. (The external
    capsule in the human connectome — the uncinate fasciculus
    and the inferior fronto-occipital fasciculus.)
*   **Uncinate fasciculus (review):** Von Der Heide, R.J.,
    Skipper, L.M., Klobusicky, E., Olson, I.R. (2013).
    "Dissecting the uncinate fasciculus: disorders, controversies
    and a hypothesis." *Brain* 136:1692–1707. (Definitive review
    of the uncinate fasciculus — the defining anterior bundle of
    the external capsule.)
*   **Inferior fronto-occipital fasciculus (review):** Martino,
    J., Brogna, C., Robles, S.G., Vergani, F., Duffau, H. (2010).
    "Anatomical study of the inferior fronto-occipital fasciculus
    using postmortem fiber dissection." *Neurosurgical Focus*
    28:E5. (Definitive review of the inferior fronto-occipital
    fasciculus — the defining posterior bundle of the external
    capsule.)
*   **DTI tractography atlas:** Catani, M., Thiebaut de Schotten,
    M. (2008). "A diffusion tensor imaging tractography atlas for
    virtual in vivo dissections." *Cortex* 44:1105–1132. (The
    external capsule in DTI tractography.)
*   **Multiple sclerosis and white-matter plaques:** Polman, C.H.,
    et al. (2011). "Diagnostic criteria for multiple sclerosis:
    2010 revisions to the McDonald criteria." *Annals of
    Neurology* 69:292–302. (MS plaques in the external capsule —
    the radiological hallmark of MS.)
*   **White-matter hyperintensities (leukoaraiosis):** Fazekas, F.,
    Chawluk, J.B., Alavi, A., Hurtig, H.I., Zimmerman, R.A.
    (1987). "MR signal abnormalities at 1.5 T in Alzheimer's
    dementia and normal aging." *American Journal of
    Roentgenology* 149:351–356. (The Fazekas scale for
    white-matter hyperintensities — the radiological hallmark of
    small-vessel disease.)
*   **Uncinate fasciculus and psychopathy:** Craig, M.C., Catani,
    M., Deeley, Q., Latham, R., Daly, E., Kanaan, R., Picchioni,
    M., McGuire, P.K., Fahy, T., Murphy, D.G.M. (2009). "Altered
    connections on the road to psychopathy." *Molecular
    Psychiatry* 14:946–953. (Uncinate fasciculus DTI abnormalities
    in psychopathy.)
*   **Uncinate fasciculus and frontotemporal dementia:** Galantucci,
    S., et al. (2011). "White matter damage in frontotemporal
    lobar degeneration spectrum." *Cerebral Cortex* 21:2709–2717.
    (Uncinate fasciculus damage in frontotemporal dementia.)
*   **IFOF and semantic dementia:** Agosta, F., et al. (2010).
    "Language networks in semantic dementia." *Brain*
    133:286–299. (Inferior fronto-occipital fasciculus damage in
    semantic dementia.)
*   **IFOF and reading:** Vandermosten, M., Boets, B., Wouters, J.,
    Ghesquière, P. (2012). "A qualitative and quantitative review
    of diffusion tensor imaging studies in reading and dyslexia."
    *Neuroscience & Biobehavioral Reviews* 36:1532–1552. (IFOF
    and reading — developmental dyslexia.)
*   **Glioblastoma and white-matter tumor infiltration:** Louis,
    D.N., et al. (2016). "The 2016 World Health Organization
    classification of tumors of the central nervous system: a
    summary." *Acta Neuropathologica* 131:803–820. (Glioblastoma
    and white-matter tumor infiltration — the external capsule as
    a common site of infiltration.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    external capsule is not the amnesia substrate):** Scoville,
    W.B., Milner, B. (1957). "Loss of recent memory after
    bilateral hippocampal lesions." *Journal of Neurology,
    Neurosurgery, and Psychiatry* 20:11–21. (Bilateral
    hippocampal damage and anterograde amnesia — distinct from
    the external capsule.)
*   **Amygdala (contrast — the external capsule is NOT the
    amygdala):** LeDoux, J.E. (2000). "Emotion circuits in the
    brain." *Annual Review of Neuroscience* 23:155–184.
    (Amygdala fear circuit — distinct from the external capsule.)
*   **SLEA (contrast — the external capsule is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the external capsule.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (External capsule in overview.)
*   NeuroNames — External capsule (left); FMA — External capsule
    (left member).
""""""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter.external_capsule
=========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── white_matter
                └── external_capsule   <-- THIS MODULE

**Primary synonym:** External capsule (left); capsula externa;
**the capsular white-matter sheet between the putamen and the
claustrum**; **the capsule lateral to the putamen**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **capsular white-matter sheet**
between the **putamen** (medial) and the **claustrum** (lateral),
composed of **association fibers** (the **uncinate fasciculus**,
the **inferior fronto-occipital fasciculus**, and contributions
from the **superior longitudinal fasciculus** and the **inferior
longitudinal fasciculus**) and **corticostriatal** projection
fibers. It is a **specific named white-matter structure** — a
**capsular white-matter sheet**, **not** a region of passage,
**not** a projection-fiber fan, **not** a compact projection-fiber
bundle, **not** an association bundle, **not** a commissural
structure.
**Part of:** The **white_matter** container of the left cerebral
hemisphere — the **capsular white-matter sheet** that **carries**
the association fibers (uncinate fasciculus, inferior
fronto-occipital fasciculus, and contributions from the superior
and inferior longitudinal fasciculi) and the corticostriatal
projection fibers between the **putamen** and the **claustrum**.
**Structural parent:** ``.../left/white_matter/`` → **direct
child** of the white_matter container.
**Structural children:** **None.** This is a **leaf** module. The
**uncinate fasciculus**, the **inferior fronto-occipital
fasciculus**, the **superior longitudinal fasciculus
contribution**, the **inferior longitudinal fasciculus
contribution**, and the **corticostriatal** fibers that pass
through the external capsule are documented as **prose**, not as
structural children.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the external_capsule is WHITE MATTER, NOT a
grey-matter structure.** The **external capsule** (here) is the
**capsular white-matter sheet** between the **putamen** and the
**claustrum** — **myelinated axons** (association and projection
fibers). The **grey-matter structures** that the external capsule
sits **between** — the **putamen** (medial) and the **claustrum**
(lateral) — are **grey matter** and are wired under their own
containers (``.../left/subcortical/basal_ganglia/striatum/
dorsal_striatum/putamen/`` and
``.../left/subcortical/claustrum/``). **They are DIFFERENT
STRUCTURES** — the **external capsule** is the **capsular
white-matter sheet**; the **putamen** and the **claustrum** are
the **grey-matter structures** it **sits between**. Consumers
must **not** conflate the external capsule with any grey-matter
structure.
**Boundary status (CAPSULAR WHITE-MATTER SHEET — NOT a region of
passage, NOT a projection-fiber fan, NOT a compact
projection-fiber bundle, NOT an association bundle, NOT a
commissural structure):** **Boundary case — the external_capsule
is a CAPSULAR WHITE-MATTER SHEET, NOT a region of passage, NOT a
projection-fiber fan, NOT a compact projection-fiber bundle, NOT
an association bundle, NOT a commissural structure.** The
**external capsule** is a **specific capsular white-matter
sheet** — a **defined anatomical structure** whose **defining
bundles** are the **uncinate fasciculus** and the **inferior
fronto-occipital fasciculus** (with contributions from the
superior and inferior longitudinal fasciculi, plus corticostriatal
projection fibers). It is **not** a **region of passage** like
the **centrum semiovale**; it is **not** a **projection-fiber
fan** like the **corona radiata**; it is **not** a **compact
projection-fiber bundle** like the **internal capsule**; it is
**not** an **association bundle** like the **cingulum**; and it
is **not** a **commissural structure** like the **corpus
callosum**. Consumers must **not** treat the external capsule as
"another region of passage" or "another association bundle" — it
is a **capsular white-matter sheet** with its **own position** and
its **own defining bundles**.
**Boundary status (NOT the internal capsule — the internal capsule
is a SIBLING white-matter leaf, and it is a COMPACT
PROJECTION-FIBER BUNDLE medial to the putamen):** **Boundary case
— the external_capsule is NOT the internal capsule; the internal
capsule is a SIBLING white-matter leaf, and it is a COMPACT
PROJECTION-FIBER BUNDLE medial to the putamen.** The **internal
capsule** (``.../left/white_matter/internal_capsule/``) is the
**compact projection-fiber bundle** that passes **between** the
**caudate nucleus**, the **putamen**, the **globus pallidus**, and
the **thalamus** — **medial** to the putamen. The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum** — **lateral** to the
putamen. **They are SIBLINGS under the white_matter container,
and they are DIFFERENT STRUCTURES** — the **internal capsule** is
the **compact projection-fiber bundle** **medial** to the putamen;
the **external capsule** is the **capsular white-matter sheet**
**lateral** to the putamen. **They sit on OPPOSITE SIDES of the
putamen** — the internal capsule on the medial side, the external
capsule on the lateral side. Consumers must **not** conflate the
external capsule with the internal capsule — they are **different
structures on opposite sides of the putamen**.
**Boundary status (NOT the extreme capsule — the extreme capsule is
a SIBLING white-matter leaf, and it is the CAPSULAR WHITE-MATTER
SHEET lateral to the CLAUSTRUM):** **Boundary case — the
external_capsule is NOT the extreme capsule; the extreme capsule
is a SIBLING white-matter leaf, and it is the CAPSULAR
WHITE-MATTER SHEET lateral to the CLAUSTRUM.** The **extreme
capsule** (``.../left/white_matter/extreme_capsule/``) is the
**capsular white-matter sheet** **lateral** to the **claustrum**
— the **thin** white-matter sheet between the **claustrum** and
the **insular cortex**. The **external capsule** (here) is the
**capsular white-matter sheet** **medial** to the claustrum and
**lateral** to the putamen. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** — the
**external capsule** is the **capsular sheet between the putamen
and the claustrum**; the **extreme capsule** is the **capsular
sheet between the claustrum and the insular cortex**. **They are
SEPARATED by the CLAUSTRUM** — the external capsule is **medial**
to the claustrum, the extreme capsule is **lateral** to the
claustrum. Consumers must **not** conflate the external capsule
with the extreme capsule — they are **different capsular sheets
on opposite sides of the claustrum**.
**Boundary status (NOT the claustrum — the claustrum is the
GREY-MATTER structure the external capsule sits MEDIAL to):**
**Boundary case — the external_capsule is NOT the claustrum; the
claustrum is the GREY-MATTER structure the external capsule sits
MEDIAL to.** The **claustrum**
(``.../left/subcortical/claustrum/``) is the **thin grey-matter
sheet** between the **external capsule** (medial) and the
**extreme capsule** (lateral). The **external capsule** (here) is
the **capsular white-matter sheet** **medial** to the claustrum.
**They are DIFFERENT STRUCTURES** — the **claustrum** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately medial** to the
**claustrum**. Consumers must **not** conflate the external
capsule with the claustrum.
**Boundary status (NOT the putamen — the putamen is the GREY-MATTER
structure the external capsule sits LATERAL to):** **Boundary
case — the external_capsule is NOT the putamen; the putamen is the
GREY-MATTER structure the external capsule sits LATERAL to.** The
**putamen**
(``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
putamen/``) is the **grey-matter structure** of the **dorsal
striatum** — the **lateral** part of the **lentiform nucleus**
(with the globus pallidus). The **external capsule** (here) is the
**capsular white-matter sheet** **lateral** to the putamen.
**They are DIFFERENT STRUCTURES** — the **putamen** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately lateral** to the
**putamen**. Consumers must **not** conflate the external capsule
with the putamen.
**Boundary status (NOT the centrum semiovale — the centrum
semiovale is a SIBLING white-matter leaf, and it is a REGION OF
PASSAGE above the level of the lateral ventricles):** **Boundary
case — the external_capsule is NOT the centrum semiovale; the
centrum semiovale is a SIBLING white-matter leaf, and it is a
REGION OF PASSAGE above the level of the lateral ventricles.**
The **centrum semiovale**
(``.../left/white_matter/centrum_semiovale/``) is the
**white-matter mass above the lateral ventricles** — a **region
of passage** that **contains** the corona radiata, the
association fibers, and the callosal radiations as they pass
through it. The **external capsule** (here) is the **capsular
white-matter sheet** between the **putamen** and the
**claustrum** — **inferior** to the main mass of the centrum
semiovale. **They are SIBLINGS under the white_matter container,
and they are DIFFERENT STRUCTURES** — the **centrum semiovale**
is a **region of passage**; the **external capsule** is a
**capsular white-matter sheet**. Consumers must **not** conflate
the external capsule with the centrum semiovale.
**Boundary status (NOT the corona radiata — the corona radiata is
a SIBLING white-matter leaf, and it is a PROJECTION-FIBER FAN):**
**Boundary case — the external_capsule is NOT the corona radiata;
the corona radiata is a SIBLING white-matter leaf, and it is a
PROJECTION-FIBER FAN.** The **corona radiata**
(``.../left/white_matter/corona_radiata/``) is the
**projection-fiber fan** between the **internal capsule** and the
**cortex** — **projection fibers** (corticospinal,
corticobulbar, corticopontine, thalamocortical). The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum** — **association fibers**
(uncinate fasciculus, inferior fronto-occipital fasciculus) and
**corticostriatal** projection fibers. **They are SIBLINGS under
the white_matter container, and they are DIFFERENT STRUCTURES** —
the **corona radiata** is a **projection-fiber fan**; the
**external capsule** is a **capsular white-matter sheet**.
Consumers must **not** conflate the external capsule with the
corona radiata.
**Boundary status (NOT the cingulum — the cingulum is a SIBLING
white-matter leaf, and it is the ASSOCIATION bundle of the
cingulate gyrus):** **Boundary case — the external_capsule is NOT
the cingulum; the cingulum is a SIBLING white-matter leaf, and it
is the ASSOCIATION bundle of the cingulate gyrus.** The
**cingulum** (``.../left/white_matter/cingulum/``) is the
**specific association bundle** that runs **within the cingulate
gyrus** (around the corpus callosum). The **external capsule**
(here) is the **capsular white-matter sheet** between the
**putamen** and the **claustrum**. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** — the
**cingulum** is a **specific named association bundle** with a
**defined course**; the **external capsule** is a **capsular
white-matter sheet**. Consumers must **not** conflate the
external capsule with the cingulum.
**Boundary status (NOT the corpus callosum — the corpus callosum is
wired under ``commissures/``):** **Boundary case — the
external_capsule is NOT the corpus callosum; the corpus callosum
is wired under ``.../left/commissures/corpus_callosum/``.** The
**corpus callosum** (``.../left/commissures/corpus_callosum/``)
is the **commissural structure** — the **midline white-matter
commissure** that connects the two hemispheres. The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum** — **intrahemispheric**
fibers. **They are DIFFERENT STRUCTURES** — the **corpus
callosum** is a **commissural structure** (wired under
``commissures/``); the **external capsule** is an **intrahemispheric
capsular white-matter sheet** (wired under ``white_matter/``).
Consumers must **not** conflate the external capsule with the
corpus callosum.
**Boundary status (NOT the fornix — the fornix is a SIBLING
white-matter leaf, and it is a HIPPOCAMPAL OUTPUT tract):**
**Boundary case — the external_capsule is NOT the fornix; the
fornix is a SIBLING white-matter leaf, and it is a HIPPOCAMPAL
OUTPUT tract.** The **fornix** (``.../left/white_matter/fornix/``)
is the **major output tract** of the hippocampus. The **external
capsule** (here) is the **capsular white-matter sheet** between
the **putamen** and the **claustrum**. **They are SIBLINGS under
the white_matter container, and they are DIFFERENT STRUCTURES** —
the **fornix** is a **hippocampal output tract**; the **external
capsule** is a **capsular white-matter sheet**. Consumers must
**not** conflate the external capsule with the fornix.
**Boundary status (NOT the fasciculus rectus, mammillothalamic
tract, or medial forebrain bundle — those are SIBLING
white-matter leaves):** **Boundary case — the external_capsule is
NOT the fasciculus rectus, mammillothalamic tract, or medial
forebrain bundle; those are SIBLING white-matter leaves.** Each
of those is a **specific named white-matter structure** — the
**fasciculus rectus** (a small bundle), the **mammillothalamic
tract** (the mammillary-body → anterior-thalamic projection), and
the **medial forebrain bundle** (a brainstem-forebrain bundle).
**None of them is part of the external capsule** — each is a
**separate leaf** under ``white_matter/``. Consumers must **not**
conflate the external capsule with any of those siblings.
**Boundary status (NOT the cortex — the cortex is the GREY-MATTER
structure at the SUPERFICIAL end of the external capsule):**
**Boundary case — the external_capsule is NOT the cortex; the
cortex is the GREY-MATTER structure at the SUPERFICIAL end of the
external capsule.** The **cortex** (``.../left/cortex/``) is the
**grey-matter sheet** that **caps** the cerebral hemisphere.
The **external capsule** (here) is the **capsular white-matter
sheet** between the **putamen** and the **claustrum** — the
**cortical** end of the **uncinate fasciculus** and the
**inferior fronto-occipital fasciculus** terminates in the
**cortex** (frontal, temporal, occipital). **They are DIFFERENT
STRUCTURES** — the **cortex** is **grey matter**; the **external
capsule** is **white matter**. Consumers must **not** conflate
the external capsule with the cortex.
**Boundary status (NOT the basal ganglia — the basal ganglia are
the GREY-MATTER structures the external capsule sits LATERAL to):**
**Boundary case — the external_capsule is NOT the basal ganglia;
the basal ganglia are the GREY-MATTER structures the external
capsule sits LATERAL to.** The **basal ganglia**
(``.../left/subcortical/basal_ganglia/``) — the **caudate
nucleus**, the **putamen**, the **globus pallidus**, and the
**ventral striatum** — are **grey-matter** structures. The
**external capsule** (here) is the **capsular white-matter
sheet** **lateral** to the **putamen** (one of the basal ganglia
structures). **They are DIFFERENT STRUCTURES** — the **basal
ganglia** are **grey matter**; the **external capsule** is
**white matter**. Consumers must **not** conflate the external
capsule with the basal ganglia.
**Boundary status (NOT the thalamus — the thalamus is a GREY-MATTER
structure MEDIAL to the putamen and the external capsule):**
**Boundary case — the external_capsule is NOT the thalamus; the
thalamus is a GREY-MATTER structure MEDIAL to the putamen and the
external capsule.** The **thalamus**
(``.../left/subcortical/diencephalon/thalamus/``) is a
**grey-matter** structure **medial** to the putamen (via the
internal capsule) — **farther medial** from the external capsule.
The **external capsule** (here) is the **capsular white-matter
sheet** between the **putamen** and the **claustrum**. **They are
DIFFERENT STRUCTURES** — the **thalamus** is **grey matter**;
the **external capsule** is **white matter**. Consumers must
**not** conflate the external capsule with the thalamus.
**Boundary status (NOT the lateral ventricles — the lateral
ventricles are the CSF spaces):** **Boundary case — the
external_capsule is NOT the lateral ventricles; the lateral
ventricles are the CSF spaces.** The **lateral ventricles**
(``.../left/lateral_ventricles/``) are the **CSF-filled spaces**
**medial** to the external capsule (the external capsule is
lateral, near the insular cortex). **They are DIFFERENT
STRUCTURES** — the **lateral ventricles** are **CSF spaces**;
the **external capsule** is **white matter**. Consumers must
**not** conflate the external capsule with the lateral ventricles.
**Boundary status (SLEA-FREE — the external capsule is NOT an
extended-amygdala component):** **Boundary case — the
external_capsule is SLEA-FREE.** The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **external capsule** is a
**capsular white-matter sheet** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the external
capsule — it is **SLEA-free**.
**Boundary status (WHITE-MATTER MODULE — a white-matter module in
the series):** **Boundary case — the external_capsule is a
WHITE-MATTER module in the series.** Every grey-matter module in
the medial_temporal_lobe subtree (amygdala, hippocampus, and their
children) is a **grey-matter** structure — a **nucleus**, a
**cortical region**, or a **CA field**. The **external capsule**
(here) is **white matter** — it is a **white-matter module in the
series**. Consumers must **not** treat the external capsule as
"another grey-matter structure" — it is **white matter**, and the
boundaries that anchored the grey-matter modules ("NOT the white
matter") are **reversed** here ("IS the white matter, NOT the
grey-matter structure").

Overview
--------
The external capsule is the **capsular white-matter sheet between
the putamen and the claustrum** — a **specific named white-matter
tract** whose **defining bundles** are the **uncinate fasciculus**
and the **inferior fronto-occipital fasciculus** (with
contributions from the superior and inferior longitudinal
fasciculi, plus corticostriatal projection fibers). It is a
**leaf** module under the white_matter container, the **sibling
of the centrum semiovale, the cingulum, the corona radiata, the
extreme capsule, the fasciculus rectus, the fornix, the internal
capsule, the mammillothalamic tract, and the medial forebrain
bundle**, and the **white-matter substrate** of the
**intrahemispheric association** between the **frontal**,
**temporal**, and **occipital** cortices.

**The external capsule is WHITE MATTER, NOT a grey-matter
structure.** It is the **capsular white-matter sheet** between the
**putamen** and the **claustrum** — **myelinated axons**
(association and projection fibers). The **grey-matter
structures** it sits **between** — the **putamen** (medial) and
the **claustrum** (lateral) — are **grey matter** and are wired
under their own containers.

**The external capsule is a CAPSULAR WHITE-MATTER SHEET, NOT a
region of passage, NOT a projection-fiber fan, NOT a compact
projection-fiber bundle, NOT an association bundle, NOT a
commissural structure.** It is a **specific capsular white-matter
sheet** whose **defining bundles** are the **uncinate
fasciculus** and the **inferior fronto-occipital fasciculus**
(with contributions from the superior and inferior longitudinal
fasciculi, plus corticostriatal projection fibers).

**The external capsule is NOT the internal capsule.** The
**internal capsule** (sibling) is the **compact projection-fiber
bundle** **medial** to the putamen. The **external capsule** is
the **capsular white-matter sheet** **lateral** to the putamen.
**They sit on OPPOSITE SIDES of the putamen** — **they are
SIBLINGS under the white_matter container**.

**The external capsule is NOT the extreme capsule.** The **extreme
capsule** (sibling) is the **capsular white-matter sheet**
**lateral** to the **claustrum** (between the claustrum and the
insular cortex). The **external capsule** is the **capsular
white-matter sheet** **medial** to the claustrum (between the
putamen and the claustrum). **They are SEPARATED by the
CLAUSTRUM** — **they are SIBLINGS under the white_matter
container**.

**The external capsule is NOT the claustrum.** The **claustrum**
(``.../left/subcortical/claustrum/``) is the **thin grey-matter
sheet** between the **external capsule** (medial) and the
**extreme capsule** (lateral). The **external capsule** sits
**immediately medial** to the **claustrum**.

**The external capsule is NOT the putamen.** The **putamen**
(``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
putamen/``) is the **grey-matter structure** of the **dorsal
striatum**. The **external capsule** sits **immediately lateral**
to the **putamen**.

**The external capsule is NOT the centrum semiovale.** The
**centrum semiovale** (sibling) is the **white-matter mass above
the lateral ventricles** — a **region of passage** that
**contains** the corona radiata, the association fibers, and the
callosal radiations as they pass through it. The **external
capsule** is **inferior** to the main mass of the centrum
semiovale. **They are SIBLINGS under the white_matter container.**

**The external capsule is NOT the corona radiata.** The **corona
radiata** (sibling) is a **projection-fiber fan** — the
corticospinal, corticobulbar, corticopontine, and thalamocortical
fibers. The **external capsule** is a **capsular white-matter
sheet** — the uncinate fasciculus, the inferior fronto-occipital
fasciculus, and corticostriatal projection fibers. **They are
SIBLINGS under the white_matter container.**

**The external capsule is NOT the cingulum.** The **cingulum**
(sibling) is the **specific association bundle** of the
cingulate gyrus — a **defined course** running within the
cingulate gyrus. The **external capsule** is a **capsular
white-matter sheet** between the putamen and the claustrum. **They
are SIBLINGS under the white_matter container.**

**The external capsule is NOT the corpus callosum.** The **corpus
callosum** is the **commissural structure** — wired under
``.../left/commissures/corpus_callosum/``. The **external
capsule** is an **intrahemispheric** capsular white-matter sheet
— wired under ``white_matter/``.

**The external capsule is NOT the fornix.** The **fornix**
(sibling) is the **hippocampal output tract** — the **major
output tract** of the hippocampus. The **external capsule** is a
**capsular white-matter sheet**. **They are SIBLINGS under the
white_matter container.**

**The external capsule is NOT the cortex, the basal ganglia, or
the thalamus.** Those are **grey-matter structures** — the
external capsule is the **capsular white-matter sheet** that
**connects** the cortex to the basal ganglia and carries
association fibers.

**The external capsule is NOT the lateral ventricles.** The
**lateral ventricles** are the **CSF-filled spaces** **medial**
to the external capsule.

**The external capsule is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere).

**The external capsule is a paired structure.** Each hemisphere
has its own external capsule, with **ipsilateral** connections to
the putamen, the claustrum, the insular cortex, and the frontal,
temporal, and occipital cortices. The two sides are **bilaterally
symmetric** — the external capsule is a **white-matter tract**,
and its **gross anatomy** is **symmetric**; there is **no
functional lateralization** of the external capsule per se. The
**functional lateralization** belongs to the **cortical
grey-matter structures** whose fibers pass through it (see
*Lateralization Notes*).

Fiber Composition (prose, not structural children)
--------------------------------------------------
The external capsule is a **capsular white-matter sheet** —
documented as **prose**, not as structural children:

*   **Uncinate fasciculus** — the **association bundle** that
    connects the **anterior temporal lobe** (uncus, parahippocampal
    gyrus, anterior temporal pole) to the **orbitofrontal** and
    **ventrolateral prefrontal** cortices. The **uncinate
    fasciculus** is one of the **defining bundles** of the
    external capsule — it **curves** around the **lateral
    sulcus** (the **limen insulae**) and passes through the
    **external capsule** on its way from the **temporal pole**
    to the **orbitofrontal** cortex.

*   **Inferior fronto-occipital fasciculus (IFOF)** — the
    **association bundle** that connects the **frontal lobe**
    (dorsolateral prefrontal, ventrolateral prefrontal,
    orbitofrontal) to the **occipital** and **posterior
    temporal** cortices. The **IFOF** is one of the **defining
    bundles** of the external capsule — it passes through the
    **external capsule** on its way from the **frontal** to the
    **occipital** cortex. The **IFOF** is the **ventral**
    association bundle that parallels the **superior
    longitudinal fasciculus** (dorsal).

*   **Superior longitudinal fasciculus (SLF) contribution** — the
    **superior longitudinal fasciculus** (SLF) is primarily a
    **dorsal** association bundle (the **arcuate fasciculus**
    is its **most posterior** component), but **some** of its
    fibers (especially the **SLF II** and **SLF III** components)
    pass through the **external capsule** **anteriorly** (near the
    **frontal operculum**).

*   **Inferior longitudinal fasciculus (ILF) contribution** — the
    **inferior longitudinal fasciculus** (ILF) is the **ventral**
    association bundle that connects the **occipital** to the
    **anterior temporal** lobe. **Some** of its fibers pass
    through the **posterior** part of the **external capsule**
    (near the **temporal** and **occipital** ends).

*   **Corticostriatal fibers** — the **projection fibers** that
    connect the **cerebral cortex** to the **striatum** (caudate
    nucleus, putamen). The **corticostriatal** fibers pass through
    the **external capsule** on their way from the cortex to
    the **striatum**. These are **projection fibers**, not
    association fibers.

**These fiber groups are prose, not structural children.** The
tree wires the **external capsule** as a **single leaf** under
``white_matter/`` — the **uncinate fasciculus**, the **inferior
fronto-occipital fasciculus**, the **SLF contribution**, the
**ILF contribution**, and the **corticostriatal** fibers are
**prose**, not structural children. Consumers that need
**fiber-level** resolution should consult the references, not the
tree.

The External Capsule / Internal Capsule Boundary
------------------------------------------------
This is the **most consequential sibling boundary** — the
**capsular white-matter sheet lateral to the putamen vs. the
compact projection-fiber bundle medial to the putamen** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the **putamen** (medial) and the
    **claustrum** (lateral).

*   **Internal_capsule**
    (``.../left/white_matter/internal_capsule/``) — the
    **compact projection-fiber bundle** that passes **between**
    the **caudate nucleus**, the **putamen**, the **globus
    pallidus**, and the **thalamus** — **medial** to the
    putamen.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **internal capsule** is the
**compact projection-fiber bundle** **medial** to the putamen;
the **external capsule** is the **capsular white-matter sheet**
**lateral** to the putamen. **They sit on OPPOSITE SIDES of the
putamen** — the internal capsule on the medial side, the external
capsule on the lateral side. Consumers must **not** conflate the
external capsule with the internal capsule — they are **different
structures on opposite sides of the putamen**.

The External Capsule / Extreme Capsule Boundary
-----------------------------------------------
This is the **second-most consequential sibling boundary** — the
**capsular sheet medial to the claustrum vs. capsular sheet
lateral to the claustrum** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **medial** to the **claustrum** (between
    the putamen and the claustrum).

*   **Extreme_capsule**
    (``.../left/white_matter/extreme_capsule/``) — the
    **capsular white-matter sheet** **lateral** to the
    **claustrum** (between the claustrum and the insular
    cortex).

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **external capsule** is the
**capsular sheet between the putamen and the claustrum**; the
**extreme capsule** is the **capsular sheet between the claustrum
and the insular cortex**. **They are SEPARATED by the CLAUSTRUM**
— the external capsule is **medial** to the claustrum, the
extreme capsule is **lateral** to the claustrum. Consumers must
**not** conflate the external capsule with the extreme capsule —
they are **different capsular sheets on opposite sides of the
claustrum**.

The External Capsule / Claustrum Boundary
-----------------------------------------
This is the **white matter vs. grey matter** boundary — the
claustrum is the **grey-matter sheet** the external capsule sits
**medial** to:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **medial** to the claustrum.

*   **Claustrum** (``.../left/subcortical/claustrum/``) — the
    **thin grey-matter sheet** between the **external capsule**
    (medial) and the **extreme capsule** (lateral).

**They are DIFFERENT STRUCTURES** — the **claustrum** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately medial** to the
**claustrum**. Consumers must **not** conflate the external
capsule with the claustrum.

The External Capsule / Putamen Boundary
---------------------------------------
This is the **white matter vs. grey matter** boundary — the
putamen is the **grey-matter structure** the external capsule sits
**lateral** to:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **lateral** to the putamen.

*   **Putamen**
    (``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
    putamen/``) — the **grey-matter structure** of the **dorsal
    striatum** — the **lateral** part of the **lentiform
    nucleus**.

**They are DIFFERENT STRUCTURES** — the **putamen** is **grey
matter**; the **external capsule** is **white matter**. The
**external capsule** sits **immediately lateral** to the
**putamen**. Consumers must **not** conflate the external capsule
with the putamen.

The External Capsule / Centrum Semiovale Boundary
-------------------------------------------------
This is the **capsular white-matter sheet vs. region of passage**
boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Centrum_semiovale**
    (``.../left/white_matter/centrum_semiovale/``) — the
    **white-matter mass above the lateral ventricles** — a
    **region of passage** that **contains** the corona radiata,
    the association fibers, and the callosal radiations as they
    pass through it.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **centrum semiovale** is a **region
of passage**; the **external capsule** is a **capsular
white-matter sheet** **inferior** to the main mass of the centrum
semiovale. Consumers must **not** conflate the external capsule
with the centrum semiovale.

The External Capsule / Corona Radiata Boundary
----------------------------------------------
This is the **capsular white-matter sheet vs. projection-fiber
fan** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Corona_radiata**
    (``.../left/white_matter/corona_radiata/``) — the
    **projection-fiber fan** between the internal capsule and the
    cortex.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **corona radiata** is a
**projection-fiber fan**; the **external capsule** is a
**capsular white-matter sheet**. Consumers must **not** conflate
the external capsule with the corona radiata.

The External Capsule / Cingulum Boundary
----------------------------------------
This is the **capsular white-matter sheet vs. association bundle**
boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Cingulum** (``.../left/white_matter/cingulum/``) — the
    **specific association bundle** of the cingulate gyrus.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **cingulum** is a **specific named
association bundle** with a **defined course**; the **external
capsule** is a **capsular white-matter sheet**. Consumers must
**not** conflate the external capsule with the cingulum.

The External Capsule / Corpus Callosum Boundary
-----------------------------------------------
This is the **capsular white-matter sheet vs. commissural
structure** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Corpus_callosum**
    (``.../left/commissures/corpus_callosum/``) — the
    **commissural structure** that connects the two hemispheres —
    wired under ``commissures/``, **not** under
    ``white_matter/``.

**They are DIFFERENT STRUCTURES** — the **corpus callosum** is a
**commissural structure** (wired under ``commissures/``); the
**external capsule** is an **intrahemispheric capsular
white-matter sheet** (wired under ``white_matter/``). Consumers
must **not** conflate the external capsule with the corpus
callosum.

The External Capsule / Fornix Boundary
--------------------------------------
This is the **capsular white-matter sheet vs. hippocampal output
tract** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Fornix** (``.../left/white_matter/fornix/``) — the **major
    output tract** of the hippocampus.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **fornix** is a **hippocampal output
tract**; the **external capsule** is a **capsular white-matter
sheet**. Consumers must **not** conflate the external capsule with
the fornix.

The External Capsule / Other White-Matter Leaves Boundary
--------------------------------------------------------
This is the **capsular white-matter sheet vs. other named
white-matter structures** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Fasciculus rectus**, **mammillothalamic tract**, **medial
    forebrain bundle** — the **other named white-matter leaves**
    under ``white_matter/``.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — each of those is a **specific named
white-matter structure**; the **external capsule** is a
**capsular white-matter sheet**. **None of those is part of the
external capsule** — each is a **separate leaf** under
``white_matter/``. Consumers must **not** conflate the external
capsule with any of those siblings.

The External Capsule / Cortex Boundary
--------------------------------------
This is the **white matter vs. grey matter** boundary at the
superficial end of the external capsule:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum.

*   **Cortex** (``.../left/cortex/``) — the **grey-matter sheet**
    that **caps** the cerebral hemisphere.

**They are DIFFERENT STRUCTURES** — the **cortex** is **grey
matter**; the **external capsule** is **white matter** — the
**association fibers** (uncinate fasciculus, inferior
fronto-occipital fasciculus) **terminate** in the **cortex**.
Consumers must **not** conflate the external capsule with the
cortex.

The External Capsule / Basal Ganglia Boundary
---------------------------------------------
This is the **white matter vs. grey matter** boundary — the
external capsule sits **lateral** to the putamen:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **lateral** to the putamen.

*   **Basal ganglia** (``.../left/subcortical/basal_ganglia/``) —
    the **grey-matter structures** (caudate nucleus, putamen,
    globus pallidus, ventral striatum).

**They are DIFFERENT STRUCTURES** — the **basal ganglia** are
**grey matter**; the **external capsule** is **white matter**.
Consumers must **not** conflate the external capsule with the
basal ganglia.

The External Capsule / Thalamus Boundary
----------------------------------------
This is the **white matter vs. grey matter** boundary — the
thalamus is **medial** to the putamen (farther medial from the
external capsule):

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** **lateral** to the putamen.

*   **Thalamus** (``.../left/subcortical/diencephalon/thalamus/``)
    — the **grey-matter structure** **medial** to the putamen.

**They are DIFFERENT STRUCTURES** — the **thalamus** is **grey
matter**; the **external capsule** is **white matter**. Consumers
must **not** conflate the external capsule with the thalamus.

The External Capsule / Lateral Ventricles Boundary
--------------------------------------------------
This is the **white matter vs. CSF space** boundary:

*   **External_capsule** (this module) — the **capsular
    white-matter sheet** between the putamen and the claustrum
    (lateral, near the insular cortex).

*   **Lateral ventricles** (``.../left/lateral_ventricles/``) — the
    **CSF-filled spaces** **medial** to the external capsule.

**They are DIFFERENT STRUCTURES** — the **lateral ventricles** are
**CSF spaces**; the **external capsule** is **white matter**.
Consumers must **not** conflate the external capsule with the
lateral ventricles.

The External Capsule / White Matter Container Boundary
------------------------------------------------------
This is the **child vs. container** boundary:

*   **External_capsule** (this module) — a **child** of the
    white_matter container.

*   **White_matter** (``.../left/white_matter/``) — the
    **container** that contains the **centrum semiovale**, the
    **cingulum**, the **corona radiata**, the **external
    capsule**, the **extreme capsule**, the **fasciculus rectus**,
    the **fornix**, the **internal capsule**, the
    **mammillothalamic tract**, and the **medial forebrain
    bundle**.

**The external capsule is ONE of the ten children of the
white_matter container.** Consumers must **not** conflate the
external capsule with the white_matter container.

The External Capsule / Cerebral Hemisphere Boundary
---------------------------------------------------
This is the **grandchild vs. container** boundary:

*   **External_capsule** (this module) — a **grandchild** of the
    ``.../left/`` (cerebral hemisphere) container.

*   **``.../left/``** — the **cerebral hemisphere container** that
    contains the **cortex**, the **rhinencephalon**, the
    **subcortical** structures, the **white_matter**, the
    **commissures**, and the **lateral_ventricles**.

**The external capsule is a grandchild of the cerebral hemisphere**
(child of the white_matter container). Consumers must **not**
conflate the external capsule with the cerebral hemisphere
container.

The External Capsule / SLEA Boundary
------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **External_capsule** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The external capsule is NOT part of the SLEA continuum.** It is a
**capsular white-matter sheet**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
external capsule.

Function in the Human Brain
---------------------------
The external capsule's functions are **intrahemispheric
association** and **corticostriatal projection** — **NOT a
grey-matter function**:

*   **Uncinate Fasciculus (Temporal → Frontal Association):** The
    **external capsule** carries the **uncinate fasciculus** —
    the association bundle that connects the **anterior temporal
    lobe** to the **orbitofrontal** and **ventrolateral
    prefrontal** cortices. This is the **temporal-prefrontal
    association** substrate of the external capsule — a
    **limbic / paralimbic** association bundle implicated in
    **emotion regulation**, **social cognition**, and
    **episodic memory retrieval**.

*   **Inferior Fronto-Occipital Fasciculus (Frontal → Occipital
    Association):** The **external capsule** carries the
    **inferior fronto-occipital fasciculus** — the association
    bundle that connects the **frontal lobe** to the
    **occipital** and **posterior temporal** cortices. This is
    the **frontal-occipital association** substrate of the
    external capsule — a **ventral** association bundle
    implicated in **semantic processing**, **visual
    recognition**, and **reading**.

*   **Superior Longitudinal Fasciculus Contribution (Frontal →
    Parietal / Temporal):** The **external capsule** carries a
    contribution from the **superior longitudinal fasciculus**
    — the dorsal association bundle (the **arcuate fasciculus**
    is its most posterior component). This is the
    **frontal-parietal / temporal association** substrate of
    the external capsule.

*   **Inferior Longitudinal Fasciculus Contribution (Occipital →
    Temporal):** The **external capsule** carries a contribution
    from the **inferior longitudinal fasciculus** — the ventral
    association bundle that connects the **occipital** to the
    **anterior temporal** lobe. This is the **occipital-temporal
    association** substrate of the external capsule.

*   **Corticostriatal Projection (Cortex → Striatum):** The
    **external capsule** carries the **corticostriatal** fibers
    — the projection fibers from the **cerebral cortex** to the
    **striatum** (caudate nucleus, putamen). This is the
    **corticostriatal** substrate of the external capsule.

*   **NOT a neural processor in the classical sense.** The
    **external capsule** is a **capsular white-matter sheet** —
    it **conducts** the **association fibers** and the
    **corticostriatal projection fibers**, but it does **not**
    **process** information (that happens in the **grey-matter
    structures** — the cortex, the putamen, the claustrum). The
    **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the external capsule is the **capsular
white-matter sheet** of the **cerebral hemisphere** — the
**specific named white-matter tract** that anchors the
**intrahemispheric association** (uncinate fasciculus, inferior
fronto-occipital fasciculus) and the **corticostriatal
projection**. It is **SLEA-free**, **white-matter**, and **NOT a
grey-matter structure** — the **grey-matter structures** are the
**putamen**, the **claustrum**, and the **cortex** whose fibers
pass through it.

Associated Disorders
--------------------
The external capsule has **no named "external capsule syndrome"**
in the narrow sense, but its clinical associations are
**well-documented** — primarily as a **white-matter imaging
target** and as an **association-tract** structure:

*   **Multiple Sclerosis (External Capsule Plaques):** The
    **external capsule** is a **site** of **MS plaques** — the
    **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**. The **external capsule**
    is the **white-matter substrate** of **MS lesions**.

*   **White-Matter Hyperintensities (Leukoaraiosis / Small-Vessel
    Disease):** The **external capsule** is a **site** of
    **white-matter hyperintensities** — the **T2/FLAIR
    hyperintensities** that are the **radiological hallmark** of
    **small-vessel disease**, **aging**, and **vascular
    dementia**.

*   **Uncinate Fasciculus Disconnection (Emotion Regulation /
    Social Cognition):** The **uncinate fasciculus** —
    the **defining bundle** of the **anterior external
    capsule** — is implicated in **emotion regulation** and
    **social cognition**. **Uncinate fasciculus DTI
    abnormalities** are reported in **psychopathy**,
    **antisocial personality disorder**, and **frontotemporal
    dementia**.

*   **Inferior Fronto-Occipital Fasciculus Disconnection (Semantic
    Processing / Reading):** The **inferior fronto-occipital
    fasciculus** — the **defining bundle** of the **posterior
    external capsule** — is implicated in **semantic processing**
    and **reading**. **IFOF DTI abnormalities** are reported in
    **semantic dementia** and in **developmental dyslexia**.

*   **Glioblastoma and White-Matter Tumor Infiltration:** The
    **external capsule** is a **common site** of **glioblastoma**
    and other **white-matter tumors** — the **infiltrative**
    tumor cells **spread** along the association fibers of the
    external capsule.

*   **No Named "External Capsule Syndrome":** The **external
    capsule** is a **capsular white-matter sheet**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** as a
    **white-matter imaging target** (MS, leukoaraiosis,
    glioblastoma), and **indirect** for the **association
    bundles** it carries (uncinate fasciculus, inferior
    fronto-occipital fasciculus).

**What is NOT here:** The **external capsule** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as a **white-matter imaging target**, and **indirect**
for the **association bundles** it carries.

Lateralization Notes
--------------------
This is the **left** external_capsule module. The **external
capsule** is **bilaterally symmetric** — and it carries **NO
warning**:

*   **Bilateral White-Matter Anatomy:** Each hemisphere has its
    own external capsule. The two sides are **grossly symmetric**
    — the external capsule is a **white-matter tract**, and its
    **gross anatomy** is **symmetric**. There is **no functional
    lateralization** of the external capsule per se.

*   **NO Functional Lateralization of the White-Matter Tract:**
    The **functional lateralization** belongs to the **cortical
    grey-matter structures** whose fibers pass through the
    external capsule (e.g., the **left-hemisphere language areas**
    via the **uncinate fasciculus** and the **inferior
    fronto-occipital fasciculus**, the **right-hemisphere
    emotion-regulation areas** via the **uncinate fasciculus**)
    — **not** to the external capsule itself. Consumers must
    **not** assume the external capsule carries a **functional
    lateralization** of its own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    external_capsule is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the external capsule.

*   **NO Amygdala-Lateralization Warning of their own (the
    external capsule is a CAPSULAR WHITE-MATTER SHEET, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **external capsule** is a
    **capsular white-matter sheet** — consumers must **not**
    conflate it with the **whole amygdala** or with the
    **central nucleus**.

**A consumer that assumes "left external capsule = right external
capsule" will be structurally correct** — the two sides are
**symmetric** (the external capsule is a **white-matter tract**,
and its **gross anatomy** is **symmetric**). The **external
capsule** is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no amygdala-lateralization warning of their own**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../left/white_matter/centrum_semiovale/``,
    ``.../left/white_matter/cingulum/``,
    ``.../left/white_matter/corona_radiata/``,
    ``.../left/white_matter/extreme_capsule/``,
    ``.../left/white_matter/fasciculus_rectus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/white_matter/internal_capsule/``,
    ``.../left/white_matter/mammillothalamic_tract/``,
    ``.../left/white_matter/medial_forebrain_bundle/``,
    ``.../left/cortex/``, ``.../left/commissures/``,
    ``.../left/subcortical/basal_ganglia/``,
    ``.../left/subcortical/basal_ganglia/striatum/dorsal_striatum/
    putamen/``, ``.../left/subcortical/claustrum/``,
    ``.../left/subcortical/diencephalon/thalamus/``,
    ``.../left/lateral_ventricles/``, or any other container. The
    **external capsule**'s relationships to the other white-matter
    leaves, the cortex, the corpus callosum, the basal ganglia,
    the putamen, the claustrum, the thalamus, and the lateral
    ventricles are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **uncinate
    fasciculus**, the **inferior fronto-occipital fasciculus**,
    the **superior longitudinal fasciculus contribution**, the
    **inferior longitudinal fasciculus contribution**, and the
    **corticostriatal** fibers are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve fiber-level detail through the references.
*   **WHITE MATTER — NOT a grey-matter structure.** The **external
    capsule** is **white matter**; the **putamen**, the
    **claustrum**, the **cortex**, the **basal ganglia**, and the
    **thalamus** are **grey matter**. Consumers must **not**
    conflate the external capsule with any grey-matter structure.
*   **CAPSULAR WHITE-MATTER SHEET — NOT a region of passage, NOT a
    projection-fiber fan, NOT a compact projection-fiber bundle,
    NOT an association bundle, NOT a commissural structure.** The
    **external capsule** is a **capsular white-matter sheet**
    whose **defining bundles** are the **uncinate fasciculus**
    and the **inferior fronto-occipital fasciculus**.
*   **NOT the internal capsule — the internal capsule is a SIBLING
    white-matter leaf, and it is a COMPACT PROJECTION-FIBER
    BUNDLE MEDIAL to the putamen.** The **external capsule** is
    the **capsular white-matter sheet LATERAL to the putamen**.
    They are **on opposite sides of the putamen** — not the same
    structure.
*   **NOT the extreme capsule — the extreme capsule is a SIBLING
    white-matter leaf, and it is the CAPSULAR WHITE-MATTER SHEET
    LATERAL to the CLAUSTRUM.** The **external capsule** is the
    **capsular white-matter sheet MEDIAL to the claustrum**. They
    are **separated by the claustrum** — not the same structure.
*   **NOT the claustrum — the claustrum is the GREY-MATTER
    structure the external capsule sits MEDIAL to.**
*   **NOT the putamen — the putamen is the GREY-MATTER structure
    the external capsule sits LATERAL to.**
*   **NOT the centrum semiovale — the centrum semiovale is a
    SIBLING white-matter leaf, and it is a REGION OF PASSAGE above
    the level of the lateral ventricles.** Consumers must **not**
    conflate the external capsule with the centrum semiovale.
*   **NOT the corona radiata — the corona radiata is a SIBLING
    white-matter leaf, and it is a PROJECTION-FIBER FAN.**
*   **NOT the cingulum — the cingulum is a SIBLING white-matter
    leaf, and it is the ASSOCIATION bundle of the cingulate
    gyrus.**
*   **NOT the corpus callosum — the corpus callosum is wired under
    ``commissures/``.**
*   **NOT the fornix — the fornix is a SIBLING white-matter leaf,
    and it is a HIPPOCAMPAL OUTPUT tract.**
*   **NOT the fasciculus rectus, mammillothalamic tract, or medial
    forebrain bundle — those are SIBLING white-matter leaves.**
*   **NOT the cortex, basal ganglia, or thalamus — those are
    GREY-MATTER structures.**
*   **NOT the lateral ventricles — the lateral ventricles are CSF
    spaces.**
*   **NOT the white_matter container — the external capsule is a
    CHILD of the white_matter container.**
*   **NOT the cerebral hemisphere container — the external capsule
    is a GRANDCHILD of the ``.../left/`` container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The external
    capsule is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **external capsule** is a **capsular white-matter sheet**.
*   **No ``AREA_PATHS`` hop.** The **external capsule** is a local
    leaf under ``white_matter/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **external capsule** has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with right external capsule — strict
    mirror with NO warning.** Left and right external capsule
    modules are **structurally identical** — same **leaf** status,
    same **capsular-white-matter-sheet** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter import external_capsule

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.white_matter."
        "external_capsule"
    )

**Do not** assume the external capsule is the **internal capsule**.
The **internal capsule** is a **sibling** white-matter leaf — the
**compact projection-fiber bundle** **medial** to the putamen.
The **external capsule** is the **capsular white-matter sheet**
**lateral** to the putamen. **They sit on opposite sides of the
putamen.**

**Do not** assume the external capsule is the **extreme capsule**.
The **extreme capsule** is a **sibling** white-matter leaf — the
**capsular white-matter sheet** **lateral** to the **claustrum**
(between the claustrum and the insular cortex). The **external
capsule** is the **capsular white-matter sheet** **medial** to the
claustrum. **They are separated by the claustrum.**

**Do not** assume the external capsule is the **claustrum**. The
**claustrum** is the **grey-matter sheet** the external capsule
sits **medial** to.

**Do not** assume the external capsule is the **putamen**. The
**putamen** is the **grey-matter structure** the external capsule
sits **lateral** to.

**Do not** assume the external capsule is the **centrum
semiovale**. The **centrum semiovale** is a **sibling**
white-matter leaf — a **region of passage** above the level of
the lateral ventricles.

**Do not** assume the external capsule is the **corona radiata**.
The **corona radiata** is a **sibling** white-matter leaf — a
**projection-fiber fan**.

**Do not** assume the external capsule is the **cingulum**. The
**cingulum** is a **sibling** white-matter leaf — the
**association bundle** of the cingulate gyrus.

**Do not** assume the external capsule is the **corpus callosum**.
The **corpus callosum** is wired under ``commissures/`` — the
**commissural structure**.

**Do not** assume the external capsule is the **fornix**. The
**fornix** is a **sibling** white-matter leaf — the **hippocampal
output tract**.

**Do not** assume the external capsule is **any** of the other
white-matter siblings — the **fasciculus rectus**, the
**mammillothalamic tract**, or the **medial forebrain bundle**.
Those are **separate leaves** under ``white_matter/``.

**Do not** assume the external capsule is the **cortex**, the
**basal ganglia**, or the **thalamus**. Those are **grey-matter
structures** — the external capsule is the **capsular
white-matter sheet** that **connects** them.

**Do not** assume the external capsule is the **lateral
ventricles**. The **lateral ventricles** are **CSF spaces** —
the external capsule is **lateral**, near the insular cortex.

**Do not** assume the external capsule is the **white_matter
container**. The **white_matter** container contains the
**external capsule** and the other nine white-matter leaves — the
**external capsule** is **one** of those ten children.

**Do not** assume the external capsule is the **cerebral
hemisphere container**. The **external capsule** is a
**grandchild** of the ``.../left/`` container (child of the
white_matter container).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the external capsule.
**The external capsule is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the external capsule's (empty) children (recommended
consumer pattern)::

    EXTERNAL_CAPSULE_CHILDREN = ()
    # The external capsule is a leaf. The uncinate fasciculus, the
    # inferior fronto-occipital fasciculus, the superior
    # longitudinal fasciculus contribution, the inferior
    # longitudinal fasciculus contribution, and the corticostriatal
    # fibers are prose, not modules.

Reaching the internal capsule sibling (recommended consumer
pattern — the compact projection-fiber bundle medial to the
putamen)::

    # The internal capsule is the COMPACT PROJECTION-FIBER BUNDLE
    # MEDIAL to the putamen — the SIBLING of the external capsule
    # under the white_matter container:
    #
    #   white_matter.internal_capsule
    #
    # The internal capsule is medial to the putamen; the external
    # capsule is lateral to the putamen. They are on opposite sides
    # of the putamen.

Reaching the extreme capsule sibling (recommended consumer pattern
— the capsular white-matter sheet lateral to the claustrum)::

    # The extreme capsule is the CAPSULAR WHITE-MATTER SHEET LATERAL
    # to the CLAUSTRUM — the SIBLING of the external capsule under
    # the white_matter container:
    #
    #   white_matter.extreme_capsule
    #
    # The external capsule is medial to the claustrum; the extreme
    # capsule is lateral to the claustrum. They are separated by
    # the claustrum.

Reaching the claustrum (recommended consumer pattern — the
grey-matter sheet between the external and extreme capsules)::

    # The claustrum is the GREY-MATTER SHEET between the external
    # capsule (medial) and the extreme capsule (lateral):
    #
    #   left.subcortical.claustrum
    #
    # The claustrum is grey matter; the external capsule is white
    # matter — the external capsule sits immediately medial to the
    # claustrum.

Reaching the putamen (recommended consumer pattern — the
grey-matter structure medial to the external capsule)::

    # The putamen is the GREY-MATTER STRUCTURE of the DORSAL
    # STRIATUM, MEDIAL to the external capsule:
    #
    #   left.subcortical.basal_ganglia.striatum.dorsal_striatum.putamen
    #
    # The putamen is grey matter; the external capsule is white
    # matter — the external capsule sits immediately lateral to the
    # putamen.

Reaching the centrum semiovale sibling (recommended consumer
pattern — the region of passage)::

    # The centrum semiovale is the WHITE-MATTER MASS ABOVE THE
    # LATERAL VENTRICLES — the SIBLING of the external capsule under
    # the white_matter container:
    #
    #   white_matter.centrum_semiovale
    #
    # The centrum semiovale is a region of passage; the external
    # capsule is a capsular white-matter sheet.

Reaching the corona radiata sibling (recommended consumer pattern —
the projection-fiber fan)::

    # The corona radiata is the PROJECTION-FIBER FAN — the SIBLING
    # of the external capsule under the white_matter container:
    #
    #   white_matter.corona_radiata
    #
    # The corona radiata is a projection-fiber fan; the external
    # capsule is a capsular white-matter sheet.

Reaching the cingulum sibling (recommended consumer pattern — the
association bundle of the cingulate gyrus)::

    # The cingulum is the ASSOCIATION BUNDLE of the CINGULATE GYRUS
    # — the SIBLING of the external capsule under the white_matter
    # container:
    #
    #   white_matter.cingulum
    #
    # The cingulum is a specific named association bundle with a
    # defined course; the external capsule is a capsular white-
    # matter sheet.

Reaching the fornix sibling (recommended consumer pattern — the
hippocampal output tract)::

    # The fornix is the HIPPOCAMPAL OUTPUT TRACT — the SIBLING of
    # the external capsule under the white_matter container:
    #
    #   white_matter.fornix
    #
    # The fornix is a hippocampal output tract; the external capsule
    # is a capsular white-matter sheet.

Reaching the corpus callosum (recommended consumer pattern — the
commissural structure, NOT under white_matter/)::

    # The corpus callosum is the COMMISSURAL STRUCTURE — wired
    # under ``commissures/``, NOT under ``white_matter/``:
    #
    #   left.commissures.corpus_callosum
    #
    # The corpus callosum is a commissural structure; the external
    # capsule is an intrahemispheric capsular white-matter sheet.

Reaching the cortex (recommended consumer pattern — the grey-matter
sheet at the superficial end of the external capsule)::

    # The cortex is the GREY-MATTER SHEET that caps the hemisphere —
    # the structure the external capsule's association fibers
    # terminate in:
    #
    #   left.cortex
    #
    # The cortex is grey matter; the external capsule is white
    # matter — the association fibers (uncinate fasciculus,
    # inferior fronto-occipital fasciculus) terminate in the
    # cortex.

Reaching the white_matter container (recommended consumer pattern —
the container)::

    # The white_matter container contains the external capsule and
    # the other nine white-matter leaves:
    #
    #   left.white_matter
    #
    # The external capsule is ONE of the ten children of the
    # white_matter container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the external capsule is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the external
    # capsule:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The external capsule is SLEA-FREE.

Fiber-level detail (not wired — consult references)::

    # The external capsule's fiber groups are prose, not modules:
    #   uncinate fasciculus                   -> anterior temporal
    #                                             lobe to the
    #                                             orbitofrontal and
    #                                             ventrolateral
    #                                             prefrontal
    #                                             cortices
    #   inferior fronto-occipital fasciculus  -> frontal lobe to
    #                                             the occipital and
    #                                             posterior temporal
    #                                             cortices
    #   superior longitudinal fasciculus
    #     contribution                        -> frontal-parietal /
    #                                             temporal (anterior
    #                                             contribution,
    #                                             especially SLF II
    #                                             and SLF III)
    #   inferior longitudinal fasciculus
    #     contribution                        -> occipital to
    #                                             anterior temporal
    #                                             (posterior
    #                                             contribution)
    #   corticostriatal fibers                -> cerebral cortex
    #                                             to the striatum
    #                                             (caudate nucleus,
    #                                             putamen)
    #
    # Do not attempt to resolve these as sub-paths of the external
    # capsule.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ec_path = (
            f"telencephalon.cerebral_hemispheres.{side}.white_matter."
            f"external_capsule"
        )
        # resolve ec_path through the memory/recall layer

References
----------
*   **Canonical white-matter anatomy:** Wakana, S., Jiang, H.,
    Nagae, L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter
    atlas of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the external capsule and its association fibers.)
*   **External capsule anatomy (review):** Schmahmann, J.D.,
    Pandya, D.N. (2006). *Fiber Pathways of the Brain*. Oxford
    University Press, New York. (Definitive white-matter anatomy;
    the external capsule — the uncinate fasciculus, the inferior
    fronto-occipital fasciculus, and the relationship to the
    internal and extreme capsules.)
*   **External capsule in the human connectome:** Catani, M.,
    Thiebaut de Schotten, M. (2012). *Atlas of Human Brain
    Connections*. Oxford University Press, Oxford. (The external
    capsule in the human connectome — the uncinate fasciculus
    and the inferior fronto-occipital fasciculus.)
*   **Uncinate fasciculus (review):** Von Der Heide, R.J.,
    Skipper, L.M., Klobusicky, E., Olson, I.R. (2013).
    "Dissecting the uncinate fasciculus: disorders, controversies
    and a hypothesis." *Brain* 136:1692–1707. (Definitive review
    of the uncinate fasciculus — the defining anterior bundle of
    the external capsule.)
*   **Inferior fronto-occipital fasciculus (review):** Martino,
    J., Brogna, C., Robles, S.G., Vergani, F., Duffau, H. (2010).
    "Anatomical study of the inferior fronto-occipital fasciculus
    using postmortem fiber dissection." *Neurosurgical Focus*
    28:E5. (Definitive review of the inferior fronto-occipital
    fasciculus — the defining posterior bundle of the external
    capsule.)
*   **DTI tractography atlas:** Catani, M., Thiebaut de Schotten,
    M. (2008). "A diffusion tensor imaging tractography atlas for
    virtual in vivo dissections." *Cortex* 44:1105–1132. (The
    external capsule in DTI tractography.)
*   **Multiple sclerosis and white-matter plaques:** Polman, C.H.,
    et al. (2011). "Diagnostic criteria for multiple sclerosis:
    2010 revisions to the McDonald criteria." *Annals of
    Neurology* 69:292–302. (MS plaques in the external capsule —
    the radiological hallmark of MS.)
*   **White-matter hyperintensities (leukoaraiosis):** Fazekas, F.,
    Chawluk, J.B., Alavi, A., Hurtig, H.I., Zimmerman, R.A.
    (1987). "MR signal abnormalities at 1.5 T in Alzheimer's
    dementia and normal aging." *American Journal of
    Roentgenology* 149:351–356. (The Fazekas scale for
    white-matter hyperintensities — the radiological hallmark of
    small-vessel disease.)
*   **Uncinate fasciculus and psychopathy:** Craig, M.C., Catani,
    M., Deeley, Q., Latham, R., Daly, E., Kanaan, R., Picchioni,
    M., McGuire, P.K., Fahy, T., Murphy, D.G.M. (2009). "Altered
    connections on the road to psychopathy." *Molecular
    Psychiatry* 14:946–953. (Uncinate fasciculus DTI abnormalities
    in psychopathy.)
*   **Uncinate fasciculus and frontotemporal dementia:** Galantucci,
    S., et al. (2011). "White matter damage in frontotemporal
    lobar degeneration spectrum." *Cerebral Cortex* 21:2709–2717.
    (Uncinate fasciculus damage in frontotemporal dementia.)
*   **IFOF and semantic dementia:** Agosta, F., et al. (2010).
    "Language networks in semantic dementia." *Brain*
    133:286–299. (Inferior fronto-occipital fasciculus damage in
    semantic dementia.)
*   **IFOF and reading:** Vandermosten, M., Boets, B., Wouters, J.,
    Ghesquière, P. (2012). "A qualitative and quantitative review
    of diffusion tensor imaging studies in reading and dyslexia."
    *Neuroscience & Biobehavioral Reviews* 36:1532–1552. (IFOF
    and reading — developmental dyslexia.)
*   **Glioblastoma and white-matter tumor infiltration:** Louis,
    D.N., et al. (2016). "The 2016 World Health Organization
    classification of tumors of the central nervous system: a
    summary." *Acta Neuropathologica* 131:803–820. (Glioblastoma
    and white-matter tumor infiltration — the external capsule as
    a common site of infiltration.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    external capsule is not the amnesia substrate):** Scoville,
    W.B., Milner, B. (1957). "Loss of recent memory after
    bilateral hippocampal lesions." *Journal of Neurology,
    Neurosurgery, and Psychiatry* 20:11–21. (Bilateral
    hippocampal damage and anterograde amnesia — distinct from
    the external capsule.)
*   **Amygdala (contrast — the external capsule is NOT the
    amygdala):** LeDoux, J.E. (2000). "Emotion circuits in the
    brain." *Annual Review of Neuroscience* 23:155–184.
    (Amygdala fear circuit — distinct from the external capsule.)
*   **SLEA (contrast — the external capsule is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the external capsule.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (External capsule in overview.)
*   NeuroNames — External capsule (left); FMA — External capsule
    (left member).
"""