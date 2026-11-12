"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.white_matter.cingulum
==================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── white_matter
                └── cingulum   <-- THIS MODULE

**Primary synonym:** Cingulum (right); cingulum bundle; cingulum
gyri; **the association bundle of the cingulate gyrus**; **the
limbic association bundle**; **the cingulum of the cingulate
gyrus**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **specific named association bundle**
that runs **within the cingulate gyrus** (around the corpus
callosum), from the **subcallosal area / paraterminal gyrus** and
the **cingulate cortex** (anterior), through the **cingulate
gyrus** (middle), to the **parahippocampal gyrus** and the
**entorhinal cortex** (posterior). It is a **specific named
association bundle**, **not** a region of passage, **not** a
projection-fiber fan, **not** a commissural structure.
**Part of:** The **white_matter** container of the right cerebral
hemisphere — the **limbic association bundle** that connects the
**cingulate cortex** and the **parahippocampal / entorhinal
cortex**. The **cingulum** is the **white-matter substrate** of
the **limbic association circuit**.
**Structural parent:** ``.../right/white_matter/`` → **direct
child** of the white_matter container.
**Structural children:** **None.** This is a **leaf** module. The
**subgenual (anterior) cingulum**, the **dorsal (middle)
cingulum**, and the **posterior / parahippocampal cingulum** are
documented as **prose**, not as structural children.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the cingulum is WHITE MATTER, NOT a grey-matter
structure.** The **cingulum** (here) is the **white-matter
bundle** within the cingulate gyrus — **myelinated axons**
(association fibers). The **grey-matter structures** that the
cingulum **connects** — the **cingulate cortex**, the
**parahippocampal gyrus**, and the **entorhinal cortex** — are
**grey matter** and are wired under ``.../right/cortex/``. **They
are DIFFERENT STRUCTURES** — the **cingulum** is the
**white-matter bundle**; the **cingulate cortex**, the
**parahippocampal gyrus**, and the **entorhinal cortex** are the
**grey-matter structures** it **connects**. Consumers must
**not** conflate the cingulum with any grey-matter structure.
**Boundary status (SPECIFIC NAMED ASSOCIATION BUNDLE — NOT a
region of passage):** **Boundary case — the cingulum is a
SPECIFIC NAMED ASSOCIATION BUNDLE, NOT a region of passage.** The
**cingulum** is a **defined white-matter tract** — it has a
**defined course** (within the **cingulate gyrus**), a **defined
origin** (the **subcallosal area / paraterminal gyrus** and the
**cingulate cortex**), and a **defined terminus** (the
**parahippocampal gyrus** and the **entorhinal cortex**). It is
**not** a **region of passage** like the **centrum semiovale**
(``.../right/white_matter/centrum_semiovale/``) — the **centrum
semiovale** is the **white-matter mass** that **contains** the
association fibers (including some of the cingulum's neighbors),
but the **centrum semiovale does NOT contain the cingulum** — the
**cingulum** runs **inferior** to the main mass of the centrum
semiovale. Consumers must **not** treat the cingulum as "part of
the centrum semiovale" — it is a **specific named bundle** with
its **own course**.
**Boundary status (NOT the centrum semiovale — the centrum
semiovale is a SIBLING white-matter leaf, and it does NOT contain
the cingulum):** **Boundary case — the cingulum is NOT the centrum
semiovale; the centrum semiovale is a SIBLING white-matter leaf,
and it does NOT contain the cingulum.** The **centrum semiovale**
(``.../right/white_matter/centrum_semiovale/``) is the
**white-matter mass above the lateral ventricles** — a **region
of passage** that **contains** the **corona radiata**, the
**association fibers** (superior longitudinal fasciculus, arcuate
fasciculus, inferior longitudinal fasciculus, uncinate
fasciculus), and the **callosal radiations** as they pass through
it. The **cingulum** (here) is the **specific association bundle
of the cingulate gyrus** — it runs **inferior** to the main mass
of the centrum semiovale. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** — the
**centrum semiovale** is a **region of passage**; the **cingulum**
is a **specific named association bundle**. Consumers must **not**
conflate the cingulum with the centrum semiovale.
**Boundary status (NOT the corona radiata — the corona radiata is a
SIBLING white-matter leaf, and it is a PROJECTION-fiber fan):**
**Boundary case — the cingulum is NOT the corona radiata; the
corona radiata is a SIBLING white-matter leaf, and it is a
PROJECTION-fiber fan.** The **corona radiata**
(``.../right/white_matter/corona_radiata/``) is the
**projection-fiber fan** that **radiates** from the internal
capsule up to the cortex — **projection fibers**, not
**association fibers**. The **cingulum** (here) is the
**association bundle** of the cingulate gyrus. **They are
SIBLINGS under the white_matter container, and they are DIFFERENT
STRUCTURES** — the **corona radiata** is a **projection-fiber
fan**; the **cingulum** is a **specific named association
bundle**. Consumers must **not** conflate the cingulum with the
corona radiata.
**Boundary status (NOT the internal capsule — the internal capsule
is a SIBLING white-matter leaf, and it is a PROJECTION-fiber
bundle):** **Boundary case — the cingulum is NOT the internal
capsule; the internal capsule is a SIBLING white-matter leaf, and
it is a PROJECTION-fiber bundle.** The **internal capsule**
(``.../right/white_matter/internal_capsule/``) is the
**compact projection-fiber bundle** that passes **between** the
basal ganglia, the thalamus, and the caudate nucleus. The
**cingulum** (here) is the **association bundle** of the
cingulate gyrus. **They are SIBLINGS under the white_matter
container, and they are DIFFERENT STRUCTURES** — the **internal
capsule** is a **projection-fiber bundle**; the **cingulum** is a
**specific named association bundle**. Consumers must **not**
conflate the cingulum with the internal capsule.
**Boundary status (NOT the corpus callosum — the corpus callosum is
wired under ``commissures/``):** **Boundary case — the cingulum is
NOT the corpus callosum; the corpus callosum is wired under
``.../right/commissures/corpus_callosum/``.** The **corpus
callosum** (``.../right/commissures/corpus_callosum/``) is the
**commissural structure** — the **midline white-matter
commissure** that connects the two hemispheres (the **left**
hemisphere, from this hemisphere's perspective). The **cingulum**
(here) is the **association bundle** that runs **around** the
corpus callosum (in the cingulate gyrus) but is **not** the
corpus callosum. **They are DIFFERENT STRUCTURES** — the **corpus
callosum** is the **commissural structure** (wired under
``commissures/``); the **cingulum** is the **association bundle**
(wired under ``white_matter/``). **The cingulum runs AROUND the
corpus callosum, but it is NOT the corpus callosum.** Consumers
must **not** conflate the cingulum with the corpus callosum.
**Boundary status (NOT the fornix — the fornix is a SIBLING
white-matter leaf, and it is a HIPPOCAMPAL OUTPUT tract):**
**Boundary case — the cingulum is NOT the fornix; the fornix is a
SIBLING white-matter leaf, and it is a HIPPOCAMPAL OUTPUT tract.**
The **fornix** (``.../right/white_matter/fornix/``) is the
**major output tract** of the hippocampus — it carries the
**hippocampal output** (via the subiculum) to the **mammillary
bodies** and the **anterior thalamic nuclei**. The **cingulum**
(here) is the **association bundle** of the cingulate gyrus — it
**connects the cingulate cortex** to the **parahippocampal gyrus**
and the **entorhinal cortex**. **They are SIBLINGS under the
white_matter container, and they are DIFFERENT STRUCTURES** — the
**fornix** is a **hippocampal output tract** (projection fibers
to the diencephalon); the **cingulum** is a **specific named
association bundle** (association fibers within the hemisphere).
Consumers must **not** conflate the cingulum with the fornix.
**Boundary status (NOT the external capsule, extreme capsule,
fasciculus rectus, mammillothalamic tract, or medial forebrain
bundle — those are SIBLING white-matter leaves):** **Boundary
case — the cingulum is NOT the external capsule, extreme capsule,
fasciculus rectus, mammillothalamic tract, or medial forebrain
bundle; those are SIBLING white-matter leaves.** Each of those is
a **specific named white-matter structure** — the **external
capsule** and **extreme capsule** (capsule fibers lateral to the
putamen and claustrum), the **fasciculus rectus** (a small
bundle), the **mammillothalamic tract** (the mammillary-body →
anterior-thalamic projection), and the **medial forebrain
bundle** (a brainstem-forebrain bundle). **None of them is part
of the cingulum** — each is a **separate leaf** under
``white_matter/``. Consumers must **not** conflate the cingulum
with any of those siblings.
**Boundary status (NOT the cingulate cortex — the cingulate cortex
is the GREY-MATTER structure the cingulum runs WITHIN):**
**Boundary case — the cingulum is NOT the cingulate cortex; the
cingulate cortex is the GREY-MATTER structure the cingulum runs
WITHIN.** The **cingulate cortex**
(``.../right/cortex/cingulate/``) is the **grey-matter sheet** of
the **cingulate gyrus** — the **anterior cingulate**, the
**posterior cingulate**, the **retrosplenial cortex**, the
**subgenual area 25**, and the **indusium griseum**. The
**cingulum** (here) is the **white-matter bundle** that runs
**within** the cingulate gyrus. **They are DIFFERENT STRUCTURES**
— the **cingulate cortex** is **grey matter**; the **cingulum**
is **white matter** — the myelinated axons that run within the
cingulate gyrus. Consumers must **not** conflate the cingulum
with the cingulate cortex.
**Boundary status (NOT the parahippocampal gyrus or the entorhinal
cortex — those are the GREY-MATTER targets at the posterior end
of the cingulum):** **Boundary case — the cingulum is NOT the
parahippocampal gyrus or the entorhinal cortex; those are the
GREY-MATTER targets at the posterior end of the cingulum.** The
**parahippocampal gyrus**
(``.../right/cortex/temporal/gyri/parahippocampal_gyrus/``) and
the **entorhinal cortex**
(``.../right/cortex/temporal/gyri/entorhinal_cortex/``) are the
**grey-matter structures** that the **cingulum** **connects to**
at its posterior end. **They are DIFFERENT STRUCTURES** — the
**parahippocampal gyrus** and the **entorhinal cortex** are
**grey matter**; the **cingulum** is **white matter** — the
**association bundle** that connects them to the cingulate
cortex. Consumers must **not** conflate the cingulum with the
parahippocampal gyrus or the entorhinal cortex.
**Boundary status (NOT the hippocampus, subiculum, or amygdala —
those are GREY-MATTER structures that the cingulum interacts with
INDIRECTLY via the parahippocampal gyrus):** **Boundary case —
the cingulum is NOT the hippocampus, the subiculum, or the
amygdala; those are GREY-MATTER structures that the cingulum
interacts with INDIRECTLY via the parahippocampal gyrus.** The
**hippocampus** (``.../right/subcortical/medial_temporal_lobe/
hippocampus/``), the **subiculum**
(``.../right/subcortical/medial_temporal_lobe/hippocampus/
subiculum/``), and the **amygdala**
(``.../right/subcortical/medial_temporal_lobe/amygdala/``) are
**grey-matter structures**. The **cingulum** (here) is the
**white-matter association bundle** of the cingulate gyrus —
it **connects** the **cingulate cortex** to the
**parahippocampal gyrus** and the **entorhinal cortex**, which
**in turn** are **cortical** (and the entorhinal cortex feeds the
hippocampus via the **perforant path**). The **cingulum** does
**not** directly project to the hippocampus, the subiculum, or
the amygdala — its relationship to those structures is
**indirect**, via the parahippocampal / entorhinal cortical
relay. Consumers must **not** conflate the cingulum with the
hippocampus, the subiculum, or the amygdala.
**Boundary status (NOT the lateral ventricles — the lateral
ventricles are the CSF spaces):** **Boundary case — the cingulum
is NOT the lateral ventricles; the lateral ventricles are the
CSF spaces.** The **lateral ventricles**
(``.../right/lateral_ventricles/``) are the **CSF-filled spaces**
**inferior** to the cingulum (the cingulum runs **above** the
lateral ventricles, in the cingulate gyrus, around the corpus
callosum). **They are DIFFERENT STRUCTURES** — the **lateral
ventricles** are **CSF spaces**; the **cingulum** is **white
matter**. Consumers must **not** conflate the cingulum with the
lateral ventricles.
**Boundary status (SLEA-FREE — the cingulum is NOT an
extended-amygdala component):** **Boundary case — the cingulum is
SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **cingulum** is a **white-matter association
bundle** — it is **NOT** an extended-amygdala component, and it
carries **NO SLEA warning**. Consumers must **not** import the
SLEA warning into the cingulum — it is **SLEA-free**.
**Boundary status (WHITE-MATTER MODULE — a white-matter module in
the series):** **Boundary case — the cingulum is a WHITE-MATTER
module in the series.** Every grey-matter module in the
medial_temporal_lobe subtree (amygdala, hippocampus, and their
children) is a **grey-matter** structure — a **nucleus**, a
**cortical region**, or a **CA field**. The **cingulum** (here)
is **white matter** — it is a **white-matter module in the
series**. Consumers must **not** treat the cingulum as "another
grey-matter structure" — it is **white matter**, and the
boundaries that anchored the grey-matter modules ("NOT the white
matter") are **reversed** here ("IS the white matter, NOT the
grey-matter structure").

Overview
--------
The cingulum is the **association bundle of the cingulate gyrus** —
a **specific named white-matter tract** that runs **within the
cingulate gyrus** (around the corpus callosum), from the
**subcallosal area / paraterminal gyrus** and the **cingulate
cortex** (anterior), through the **cingulate gyrus** (middle), to
the **parahippocampal gyrus** and the **entorhinal cortex**
(posterior). It is a **leaf** module under the white_matter
container, the **sibling of the centrum semiovale, the corona
radiata, the external capsule, the extreme capsule, the
fasciculus rectus, the fornix, the internal capsule, the
mammillothalamic tract, and the medial forebrain bundle**, and the
**white-matter substrate** of the **limbic association circuit**.

**The cingulum is WHITE MATTER, NOT a grey-matter structure.** It
is the **white-matter bundle** within the cingulate gyrus —
**myelinated axons** (association fibers). The **grey-matter
structures** that the cingulum **connects** — the **cingulate
cortex**, the **parahippocampal gyrus**, and the **entorhinal
cortex** — are **grey matter** and are wired under
``.../right/cortex/``.

**The cingulum is a SPECIFIC NAMED ASSOCIATION BUNDLE, NOT a region
of passage.** It has a **defined course** (within the **cingulate
gyrus**), a **defined origin** (the **subcallosal area /
paraterminal gyrus** and the **cingulate cortex**), and a
**defined terminus** (the **parahippocampal gyrus** and the
**entorhinal cortex**). It is **not** a **region of passage**
like the **centrum semiovale**.

**The cingulum is NOT the centrum semiovale.** The **centrum
semiovale** (sibling) is the **white-matter mass above the lateral
ventricles** — a **region of passage** that **contains** the
corona radiata, the association fibers, and the callosal
radiations as they pass through. The **cingulum** runs
**inferior** to the main mass of the centrum semiovale. **The
centrum semiovale does NOT contain the cingulum.** **They are
SIBLINGS under the white_matter container.**

**The cingulum is NOT the corona radiata or the internal capsule.**
Those are **projection-fiber** structures (the corona radiata is
a **projection-fiber fan**; the internal capsule is a **compact
projection-fiber bundle**). The **cingulum** is an **association
bundle** — **association fibers**, not projection fibers. **They
are SIBLINGS under the white_matter container.**

**The cingulum is NOT the corpus callosum.** The **corpus
callosum** is the **commissural structure** — wired under
``.../right/commissures/corpus_callosum/``. The **cingulum** runs
**around** the corpus callosum (in the cingulate gyrus) but is
**not** the corpus callosum. **They are DIFFERENT STRUCTURES** —
the **corpus callosum** is a **commissural structure** (wired
under ``commissures/``); the **cingulum** is an **association
bundle** (wired under ``white_matter/``).

**The cingulum is NOT the fornix.** The **fornix** (sibling) is the
**major output tract** of the hippocampus — a **hippocampal
output tract** (projection fibers to the diencephalon). The
**cingulum** is an **association bundle** (association fibers
within the hemisphere). **They are SIBLINGS under the white_matter
container.**

**The cingulum is NOT the cingulate cortex.** The **cingulate
cortex** (``.../right/cortex/cingulate/``) is the **grey-matter
sheet** of the **cingulate gyrus** — the **anterior cingulate**,
the **posterior cingulate**, the **retrosplenial cortex**, the
**subgenual area 25**, and the **indusium griseum**. The
**cingulum** is the **white-matter bundle** that runs **within**
the cingulate gyrus.

**The cingulum is NOT the parahippocampal gyrus or the entorhinal
cortex.** Those are the **grey-matter structures** that the
**cingulum** **connects to** at its posterior end. **They are
DIFFERENT STRUCTURES** — the **parahippocampal gyrus** and the
**entorhinal cortex** are **grey matter**; the **cingulum** is
**white matter**.

**The cingulum is NOT the hippocampus, the subiculum, or the
amygdala.** Those are **grey-matter structures** that the
cingulum interacts with **indirectly** via the parahippocampal
gyrus and the entorhinal cortex. The **cingulum** does **not**
directly project to the hippocampus, the subiculum, or the
amygdala.

**The cingulum is NOT the lateral ventricles.** The **lateral
ventricles** are the **CSF-filled spaces** **inferior** to the
cingulum. The **cingulum** runs **above** the lateral ventricles,
in the cingulate gyrus, around the corpus callosum.

**The cingulum is SLEA-FREE.** It is **not** an extended-amygdala
component, and it carries **no SLEA warning**. The **SLEA
overlap** belongs to the **central nucleus** (the **only SLEA
component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The cingulum is a paired structure.** Each hemisphere has its own
cingulum, with **ipsilateral** and **bilateral** connections to
the cingulate cortex, the parahippocampal gyrus, the entorhinal
cortex, and the contralateral cingulum (some crossing fibers).
The two sides are **bilaterally symmetric** — the cingulum is a
**white-matter tract**, and its **gross anatomy** is
**symmetric**; there is **no functional lateralization** of the
cingulum per se. The **functional lateralization** belongs to the
**cingulate cortex** and the **parahippocampal / entorhinal
cortex** whose fibers pass through it (see *Lateralization
Notes*).

Course and Subdivisions (prose, not structural children)
--------------------------------------------------------
The cingulum is a **specific named association bundle** —
documented as **prose**, not as structural children. It is
conventionally divided into three parts (some schemes use two):

*   **Subgenual (anterior) cingulum** — the **anterior** part,
    connecting the **subcallosal area / paraterminal gyrus** and
    the **subgenual anterior cingulate** to the rest of the
    cingulum. This part is the **white-matter substrate** of the
    **subgenual anterior cingulate** (area 25) and is the
    **deep-brain-stimulation target** for **treatment-resistant
    depression** (Mayberg et al., 2005).

*   **Dorsal (middle) cingulum** — the **middle** part, running
    **within the cingulate gyrus** (around the corpus callosum).
    This part is the **core cingulum bundle** — it connects the
    **anterior cingulate** and the **posterior cingulate** and
    **retrosplenial cortex**.

*   **Posterior / parahippocampal cingulum** — the **posterior**
    part, connecting the **posterior cingulate** and the
    **retrosplenial cortex** to the **parahippocampal gyrus** and
    the **entorhinal cortex**. This part is the **white-matter
    substrate** of the **posterior cingulate / retrosplenial —
    parahippocampal / entorhinal** connection.

**These subdivisions are prose, not structural children.** The
tree wires the **cingulum** as a **single leaf** under
``white_matter/`` — the **subgenual**, **dorsal**, and
**posterior / parahippocampal** subdivisions are **prose**, not
structural children. Consumers that need **subdivision-level**
resolution should consult the references, not the tree.

The Cingulum / Centrum Semiovale Boundary
-----------------------------------------
This is the **most consequential sibling boundary** — the
**specific association bundle vs. region of passage** boundary:

*   **Cingulum** (this module) — the **specific named association
    bundle** of the **cingulate gyrus** — it runs **within the
    cingulate gyrus**, from the **subcallosal area / paraterminal
    gyrus** and the **cingulate cortex** to the **parahippocampal
    gyrus** and the **entorhinal cortex**.

*   **Centrum_semiovale**
    (``.../right/white_matter/centrum_semiovale/``) — the
    **white-matter mass above the lateral ventricles** — a
    **region of passage** that **contains** the corona radiata,
    the association fibers (superior longitudinal fasciculus,
    arcuate fasciculus, inferior longitudinal fasciculus,
    uncinate fasciculus), and the callosal radiations as they
    pass through.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **centrum semiovale** is a **region
of passage**; the **cingulum** is a **specific named association
bundle**. **The centrum semiovale does NOT contain the cingulum**
— the **cingulum** runs **inferior** to the main mass of the
centrum semiovale. Consumers must **not** conflate the cingulum
with the centrum semiovale.

The Cingulum / Corona Radiata Boundary
--------------------------------------
This is the **association bundle vs. projection-fiber fan**
boundary:

*   **Cingulum** (this module) — the **association bundle** of the
    cingulate gyrus.

*   **Corona_radiata**
    (``.../right/white_matter/corona_radiata/``) — the
    **projection-fiber fan** that radiates from the internal
    capsule up to the cortex.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **corona radiata** is a
**projection-fiber fan**; the **cingulum** is a **specific named
association bundle**. Consumers must **not** conflate the cingulum
with the corona radiata.

The Cingulum / Internal Capsule Boundary
----------------------------------------
This is the **association bundle vs. projection-fiber bundle**
boundary:

*   **Cingulum** (this module) — the **association bundle** of the
    cingulate gyrus.

*   **Internal_capsule**
    (``.../right/white_matter/internal_capsule/``) — the
    **compact projection-fiber bundle** that passes between the
    basal ganglia, the thalamus, and the caudate nucleus.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **internal capsule** is a
**projection-fiber bundle**; the **cingulum** is a **specific
named association bundle**. Consumers must **not** conflate the
cingulum with the internal capsule.

The Cingulum / Corpus Callosum Boundary
---------------------------------------
This is the **association bundle vs. commissural structure**
boundary:

*   **Cingulum** (this module) — the **association bundle** that
    runs **around** the corpus callosum (in the cingulate gyrus).

*   **Corpus_callosum**
    (``.../right/commissures/corpus_callosum/``) — the
    **commissural structure** that connects the two hemispheres
    (the **left** hemisphere, from this hemisphere's perspective)
    — wired under ``commissures/``, **not** under
    ``white_matter/``.

**They are DIFFERENT STRUCTURES** — the **corpus callosum** is the
**commissural structure** (wired under ``commissures/``); the
**cingulum** is an **association bundle** (wired under
``white_matter/``). **The cingulum runs AROUND the corpus
callosum, but it is NOT the corpus callosum.** Consumers must
**not** conflate the cingulum with the corpus callosum.

The Cingulum / Fornix Boundary
------------------------------
This is the **association bundle vs. hippocampal output tract**
boundary:

*   **Cingulum** (this module) — the **association bundle** of the
    cingulate gyrus.

*   **Fornix** (``.../right/white_matter/fornix/``) — the **major
    output tract** of the hippocampus — a **hippocampal output
    tract** (projection fibers to the diencephalon).

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **fornix** is a **hippocampal output
tract** (projection fibers to the diencephalon); the **cingulum**
is a **specific named association bundle** (association fibers
within the hemisphere). Consumers must **not** conflate the
cingulum with the fornix.

The Cingulum / Other White-Matter Leaves Boundary
------------------------------------------------
This is the **association bundle vs. other named white-matter
structures** boundary:

*   **Cingulum** (this module) — the **association bundle** of the
    cingulate gyrus.

*   **External capsule**, **extreme capsule**, **fasciculus
    rectus**, **mammillothalamic tract**, **medial forebrain
    bundle** — the **other named white-matter leaves** under
    ``white_matter/``.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — each of those is a **specific named
white-matter structure**; the **cingulum** is a **specific named
association bundle**. **None of those is part of the cingulum** —
each is a **separate leaf** under ``white_matter/``. Consumers
must **not** conflate the cingulum with any of those siblings.

The Cingulum / Cingulate Cortex Boundary
----------------------------------------
This is the **white matter vs. grey matter** boundary:

*   **Cingulum** (this module) — the **white-matter bundle** that
    runs **within** the cingulate gyrus.

*   **Cingulate cortex** (``.../right/cortex/cingulate/``) — the
    **grey-matter sheet** of the **cingulate gyrus** — the
    **anterior cingulate**, the **posterior cingulate**, the
    **retrosplenial cortex**, the **subgenual area 25**, and the
    **indusium griseum**.

**They are DIFFERENT STRUCTURES** — the **cingulate cortex** is
**grey matter**; the **cingulum** is **white matter** — the
myelinated axons that run **within** the cingulate gyrus.
Consumers must **not** conflate the cingulum with the cingulate
cortex.

The Cingulum / Parahippocampal Gyrus and Entorhinal Cortex Boundary
-------------------------------------------------------------------
This is the **white matter vs. grey matter** boundary at the
posterior end of the cingulum:

*   **Cingulum** (this module) — the **white-matter bundle** that
    **connects** the **cingulate cortex** to the
    **parahippocampal gyrus** and the **entorhinal cortex**.

*   **Parahippocampal gyrus**
    (``.../right/cortex/temporal/gyri/parahippocampal_gyrus/``)
    and **entorhinal cortex**
    (``.../right/cortex/temporal/gyri/entorhinal_cortex/``) — the
    **grey-matter structures** at the **posterior end** of the
    cingulum.

**They are DIFFERENT STRUCTURES** — the **parahippocampal gyrus**
and the **entorhinal cortex** are **grey matter**; the
**cingulum** is **white matter** — the **association bundle**
that connects them to the cingulate cortex. Consumers must **not**
conflate the cingulum with the parahippocampal gyrus or the
entorhinal cortex.

The Cingulum / Hippocampus, Subiculum, and Amygdala Boundary
------------------------------------------------------------
This is the **white matter vs. grey matter** boundary — an
**indirect** relationship:

*   **Cingulum** (this module) — the **white-matter association
    bundle** of the cingulate gyrus.

*   **Hippocampus** (``.../right/subcortical/medial_temporal_lobe/
    hippocampus/``), **subiculum**
    (``.../right/subcortical/medial_temporal_lobe/hippocampus/
    subiculum/``), and **amygdala**
    (``.../right/subcortical/medial_temporal_lobe/amygdala/``) —
    the **grey-matter structures**.

**They are DIFFERENT STRUCTURES** — the **hippocampus**, the
**subiculum**, and the **amygdala** are **grey matter**; the
**cingulum** is **white matter**. The **cingulum** interacts with
the hippocampus, the subiculum, and the amygdala **indirectly**
via the **parahippocampal gyrus** and the **entorhinal cortex**
(the entorhinal cortex feeds the hippocampus via the **perforant
path**). The **cingulum** does **not** directly project to the
hippocampus, the subiculum, or the amygdala. Consumers must **not**
conflate the cingulum with the hippocampus, the subiculum, or the
amygdala.

The Cingulum / Lateral Ventricles Boundary
------------------------------------------
This is the **white matter vs. CSF space** boundary:

*   **Cingulum** (this module) — the **white-matter bundle** that
    runs **above** the lateral ventricles, in the cingulate gyrus,
    around the corpus callosum.

*   **Lateral ventricles** (``.../right/lateral_ventricles/``) — the
    **CSF-filled spaces** **inferior** to the cingulum.

**They are DIFFERENT STRUCTURES** — the **lateral ventricles** are
**CSF spaces**; the **cingulum** is **white matter**. Consumers
must **not** conflate the cingulum with the lateral ventricles.

The Cingulum / White Matter Container Boundary
----------------------------------------------
This is the **child vs. container** boundary:

*   **Cingulum** (this module) — a **child** of the white_matter
    container.

*   **White_matter** (``.../right/white_matter/``) — the
    **container** that contains the **centrum semiovale**, the
    **cingulum**, the **corona radiata**, the **external
    capsule**, the **extreme capsule**, the **fasciculus rectus**,
    the **fornix**, the **internal capsule**, the
    **mammillothalamic tract**, and the **medial forebrain
    bundle**.

**The cingulum is ONE of the ten children of the white_matter
container.** Consumers must **not** conflate the cingulum with the
white_matter container.

The Cingulum / Cerebral Hemisphere Boundary
-------------------------------------------
This is the **grandchild vs. container** boundary:

*   **Cingulum** (this module) — a **grandchild** of the
    ``.../right/`` (cerebral hemisphere) container.

*   **``.../right/``** — the **cerebral hemisphere container** that
    contains the **cortex**, the **rhinencephalon**, the
    **subcortical** structures, the **white_matter**, the
    **commissures**, and the **lateral_ventricles**.

**The cingulum is a grandchild of the cerebral hemisphere** (child
of the white_matter container). Consumers must **not** conflate
the cingulum with the cerebral hemisphere container.

The Cingulum / SLEA Boundary
----------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cingulum** (this module) — **SLEA-FREE**. No extended-amygdala
    relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The cingulum is NOT part of the SLEA continuum.** It is a
**white-matter association bundle**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
cingulum.

Function in the Human Brain
---------------------------
The cingulum's functions are **limbic association** —
**cingulate-to-parahippocampal** and
**cingulate-to-entorhinal** conduction — **NOT a grey-matter
function**:

*   **Limbic Association (Cingulate Cortex → Parahippocampal Gyrus
    → Entorhinal Cortex):** The **cingulum** connects the
    **cingulate cortex** (anterior cingulate, posterior
    cingulate, retrosplenial cortex, subgenual area 25) to the
    **parahippocampal gyrus** and the **entorhinal cortex** — the
    **limbic association circuit**. This is the **limbic
    association** substrate of the cingulum.

*   **Default-Mode Network (Posterior Cingulate / Retrosplenial —
    Parahippocampal):** The **posterior cingulum** is the
    **white-matter substrate** of the **default-mode network** —
    the **posterior cingulate / retrosplenial cortex** —
    **parahippocampal gyrus / entorhinal cortex** connection that
    is a core component of the default-mode network.

*   **Emotion Regulation (Subgenual Cingulum):** The **subgenual
    cingulum** is the **white-matter substrate** of the
    **subgenual anterior cingulate** (area 25) — the
    **emotion-regulation** node that is the
    **deep-brain-stimulation target** for **treatment-resistant
    depression**.

*   **Pain Processing (Anterior Cingulate):** The **anterior
    cingulum** is the **white-matter substrate** of the
    **anterior cingulate** — the **pain-affective** processing
    node.

*   **Episodic Memory (Posterior Cingulate — Parahippocampal /
    Entorhinal):** The **posterior cingulum** is the
    **white-matter substrate** of the **posterior cingulate —
    parahippocampal / entorhinal** connection that supports
    **episodic memory** and **spatial navigation**.

*   **NOT a neural processor in the classical sense.** The
    **cingulum** is a **white-matter association bundle** — it
    **conducts** the **association fibers** between the
    **cingulate cortex** and the **parahippocampal / entorhinal
    cortex**, but it does **not** **process** information (that
    happens in the **grey-matter structures** — the cingulate
    cortex, the parahippocampal gyrus, and the entorhinal cortex).
    The **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the cingulum is the **association bundle**
of the **cingulate gyrus** — the **specific named white-matter
tract** that anchors the **limbic association circuit**. It is
**SLEA-free**, **white-matter**, and **NOT a grey-matter
structure** — the **grey-matter structures** are the **cingulate
cortex**, the **parahippocampal gyrus**, and the **entorhinal
cortex** whose fibers pass through it.

Associated Disorders
--------------------
The cingulum has **no named "cingulum syndrome"** in the narrow
sense, but its clinical associations are **well-documented** —
primarily as a **white-matter imaging target** and as a **limbic
association tract**:

*   **Alzheimer's Disease (Cingulum Bundle Degeneration):** The
    **cingulum** — especially the **posterior / parahippocampal
    cingulum** — is one of the **earliest** affected white-matter
    tracts in **Alzheimer's disease**. **Cingulum bundle
    degeneration** (on **DTI**) is an **early** white-matter
    marker of Alzheimer's disease — **often preceding** the
    **hippocampal atrophy** that is the classic imaging
    hallmark. The **cingulum** is the **white-matter substrate**
    of the **limbic association** deficit in Alzheimer's disease.

*   **Mild Cognitive Impairment (Cingulum Bundle Changes):** The
    **cingulum** shows **DTI changes** in **mild cognitive
    impairment** — the **cingulum** is a **sensitive** DTI
    marker of the **transition** from normal aging to
    **Alzheimer's disease**.

*   **Depression (Subgenual Cingulum — DBS Target):** The
    **subgenual cingulum** is the **white-matter substrate** of
    the **subgenual anterior cingulate** (area 25) — the
    **deep-brain-stimulation target** for **treatment-resistant
    depression** (Mayberg et al., 2005). **Subgenual cingulum
    changes** are reported in **major depressive disorder**.

*   **Schizophrenia (Cingulum Bundle Abnormalities — Contested):**
    The **cingulum** shows **DTI abnormalities** in
    **schizophrenia** — **reduced fractional anisotropy** in the
    **cingulum bundle** is reported. This is **contested** — the
    findings are **not** uniformly replicated.

*   **Traumatic Brain Injury (Cingulum Bundle Vulnerability):** The
    **cingulum** is **vulnerable** to **traumatic brain injury**
    (TBI) — **cingulum bundle damage** (on DTI) is reported after
    **TBI**, contributing to **post-traumatic cognitive and
    affective** deficits.

*   **Multiple Sclerosis (Cingulum Bundle Plaques):** The
    **cingulum** is a **site** of **MS plaques** — the
    **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**.

*   **Vascular Dementia / Small-Vessel Disease (Cingulum Bundle
    Changes):** The **cingulum** shows **DTI changes** in
    **vascular dementia** and **small-vessel disease** — the
    **cingulum** is a **sensitive** DTI marker of **white-matter
    disease** in the **limbic association circuit**.

*   **No Named "Cingulum Syndrome":** The **cingulum** is a
    **white-matter association bundle**, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **direct** as a **white-matter
    imaging target** (Alzheimer's disease, mild cognitive
    impairment, depression, TBI, multiple sclerosis, vascular
    dementia).

**What is NOT here:** The **cingulum** is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as a **white-matter imaging target** (Alzheimer's
disease, mild cognitive impairment, depression, TBI, MS, vascular
dementia).

Lateralization Notes
--------------------
This is the **right** cingulum module. The **cingulum** is
**bilaterally symmetric** — and it carries **NO warning**:

*   **Bilateral White-Matter Anatomy:** Each hemisphere has its own
    cingulum. The two sides are **grossly symmetric** — the
    cingulum is a **white-matter tract**, and its **gross
    anatomy** is **symmetric**. There is **no functional
    lateralization** of the cingulum per se.

*   **NO Functional Lateralization of the White-Matter Tract:**
    The **functional lateralization** belongs to the
    **cingulate cortex** and the **parahippocampal / entorhinal
    cortex** whose fibers pass through the cingulum (e.g., the
    **left-hemisphere language areas** via the
    **parahippocampal / entorhinal** connection, the
    **right-hemisphere spatial-attention areas**) — **not** to
    the cingulum itself. Consumers must **not** assume the
    cingulum carries a **functional lateralization** of its own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    cingulum is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the cingulum.

*   **NO Amygdala-Lateralization Warning of their own (the
    cingulum is a WHITE-MATTER ASSOCIATION BUNDLE, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **cingulum** is a
    **white-matter association bundle** — consumers must **not**
    conflate it with the **whole amygdala** or with the
    **central nucleus**.

**A consumer that assumes "left cingulum = right cingulum" will be
structurally correct** — the two sides are **symmetric** (the
cingulum is a **white-matter tract**, and its **gross anatomy**
is **symmetric**). The **cingulum** is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../right/white_matter/centrum_semiovale/``,
    ``.../right/white_matter/corona_radiata/``,
    ``.../right/white_matter/external_capsule/``,
    ``.../right/white_matter/extreme_capsule/``,
    ``.../right/white_matter/fasciculus_rectus/``,
    ``.../right/white_matter/fornix/``,
    ``.../right/white_matter/internal_capsule/``,
    ``.../right/white_matter/mammillothalamic_tract/``,
    ``.../right/white_matter/medial_forebrain_bundle/``,
    ``.../right/cortex/cingulate/``,
    ``.../right/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../right/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../right/commissures/corpus_callosum/``,
    ``.../right/subcortical/medial_temporal_lobe/hippocampus/``,
    ``.../right/subcortical/medial_temporal_lobe/hippocampus/
    subiculum/``,
    ``.../right/subcortical/medial_temporal_lobe/amygdala/``,
    ``.../right/lateral_ventricles/``, or any other container. The
    **cingulum**'s relationships to the other white-matter leaves,
    the cingulate cortex, the parahippocampal gyrus, the
    entorhinal cortex, the corpus callosum, the hippocampus, the
    subiculum, the amygdala, and the lateral ventricles are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **subgenual
    cingulum**, the **dorsal cingulum**, and the **posterior /
    parahippocampal cingulum** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve subdivision-level detail through the references.
*   **WHITE MATTER — NOT a grey-matter structure.** The
    **cingulum** is **white matter**; the **cingulate cortex**,
    the **parahippocampal gyrus**, and the **entorhinal cortex**
    are **grey matter**. Consumers must **not** conflate the
    cingulum with any grey-matter structure.
*   **SPECIFIC NAMED ASSOCIATION BUNDLE — NOT a region of
    passage.** The **cingulum** is a **specific named association
    bundle** with a **defined course** and **defined endpoints**.
    Consumers must **not** treat it as a region of passage like
    the centrum semiovale.
*   **NOT the centrum semiovale — the centrum semiovale is a
    SIBLING white-matter leaf, and it does NOT contain the
    cingulum.** The **centrum semiovale** is a **region of
    passage**; the **cingulum** is a **specific association
    bundle** that runs **inferior** to the main mass of the
    centrum semiovale. Consumers must **not** conflate the two.
*   **NOT the corona radiata — the corona radiata is a SIBLING
    white-matter leaf, and it is a PROJECTION-fiber fan.**
    Consumers must **not** conflate the cingulum with the corona
    radiata.
*   **NOT the internal capsule — the internal capsule is a SIBLING
    white-matter leaf, and it is a PROJECTION-fiber bundle.**
    Consumers must **not** conflate the cingulum with the internal
    capsule.
*   **NOT the corpus callosum — the corpus callosum is wired under
    ``commissures/``.** The **cingulum** runs **around** the
    corpus callosum but is **not** the corpus callosum.
*   **NOT the fornix — the fornix is a SIBLING white-matter leaf,
    and it is a HIPPOCAMPAL OUTPUT tract.** Consumers must **not**
    conflate the cingulum with the fornix.
*   **NOT the external capsule, extreme capsule, fasciculus rectus,
    mammillothalamic tract, or medial forebrain bundle — those
    are SIBLING white-matter leaves.** None of them is part of
    the cingulum.
*   **NOT the cingulate cortex — the cingulate cortex is the
    GREY-MATTER structure the cingulum runs WITHIN.** Consumers
    must **not** conflate the cingulum with the cingulate cortex.
*   **NOT the parahippocampal gyrus or the entorhinal cortex —
    those are the GREY-MATTER targets at the posterior end of the
    cingulum.**
*   **NOT the hippocampus, the subiculum, or the amygdala — those
    are GREY-MATTER structures that the cingulum interacts with
    INDIRECTLY via the parahippocampal gyrus.**
*   **NOT the lateral ventricles — the lateral ventricles are CSF
    spaces.**
*   **NOT the white_matter container — the cingulum is a CHILD of
    the white_matter container.**
*   **NOT the cerebral hemisphere container — the cingulum is a
    GRANDCHILD of the ``.../right/`` container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    cingulum is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **cingulum** is a **white-matter association bundle**.
*   **No ``AREA_PATHS`` hop.** The **cingulum** is a local leaf
    under ``white_matter/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **cingulum** has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left cingulum — strict mirror with
    NO warning.** Left and right cingulum modules are
    **structurally identical** — same **leaf** status, same
    **specific-association-bundle** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.white_matter import cingulum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.white_matter."
        "cingulum"
    )

**Do not** assume the cingulum is the **centrum semiovale**. The
**centrum semiovale** is a **sibling** white-matter leaf — a
**region of passage**. The **cingulum** is a **specific named
association bundle** that runs **inferior** to the main mass of
the centrum semiovale. **The centrum semiovale does NOT contain
the cingulum.**

**Do not** assume the cingulum is the **corona radiata** or the
**internal capsule**. Those are **sibling** white-matter leaves —
**projection-fiber** structures. The **cingulum** is an
**association bundle**.

**Do not** assume the cingulum is the **corpus callosum**. The
**corpus callosum** is wired under ``commissures/`` — the
**commissural structure** that connects the two hemispheres (the
**left** hemisphere, from this hemisphere's perspective). The
**cingulum** runs **around** the corpus callosum (in the cingulate
gyrus), but it is **not** the corpus callosum.

**Do not** assume the cingulum is the **fornix**. The **fornix** is
a **sibling** white-matter leaf — the **hippocampal output
tract**. The **cingulum** is an **association bundle**.

**Do not** assume the cingulum is **any** of the other white-matter
siblings — the **external capsule**, the **extreme capsule**, the
**fasciculus rectus**, the **mammillothalamic tract**, or the
**medial forebrain bundle**. Those are **separate leaves** under
``white_matter/``.

**Do not** assume the cingulum is the **cingulate cortex**. The
**cingulate cortex** is the **grey-matter sheet** of the
**cingulate gyrus** — the **cingulum** is the **white-matter
bundle** that runs **within** the cingulate gyrus.

**Do not** assume the cingulum is the **parahippocampal gyrus** or
the **entorhinal cortex**. Those are the **grey-matter
structures** that the cingulum **connects to** at its posterior
end.

**Do not** assume the cingulum is the **hippocampus**, the
**subiculum**, or the **amygdala**. Those are **grey-matter
structures** that the cingulum interacts with **indirectly** via
the parahippocampal gyrus and the entorhinal cortex.

**Do not** assume the cingulum is the **lateral ventricles**. The
**lateral ventricles** are **CSF spaces** — the cingulum runs
**above** the lateral ventricles, in the cingulate gyrus, around
the corpus callosum.

**Do not** assume the cingulum is the **white_matter container**.
The **white_matter** container contains the **cingulum** and the
other nine white-matter leaves — the **cingulum** is **one** of
those ten children.

**Do not** assume the cingulum is the **cerebral hemisphere
container**. The **cingulum** is a **grandchild** of the
``.../right/`` container (child of the white_matter container).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cingulum. **The
cingulum is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the cingulum's (empty) children (recommended consumer
pattern)::

    CINGULUM_CHILDREN = ()
    # The cingulum is a leaf. The subgenual (anterior) cingulum,
    # the dorsal (middle) cingulum, and the posterior /
    # parahippocampal cingulum are prose, not modules.

Reaching the centrum semiovale sibling (recommended consumer
pattern — the region of passage)::

    # The centrum semiovale is the WHITE-MATTER MASS ABOVE THE
    # LATERAL VENTRICLES — the SIBLING of the cingulum under the
    # white_matter container:
    #
    #   white_matter.centrum_semiovale
    #
    # The centrum semiovale is a REGION OF PASSAGE; the cingulum is
    # a SPECIFIC NAMED ASSOCIATION BUNDLE that runs inferior to the
    # main mass of the centrum semiovale. The centrum semiovale does
    # NOT contain the cingulum.

Reaching the corona radiata sibling (recommended consumer pattern —
the projection-fiber fan)::

    # The corona radiata is the PROJECTION-FIBER FAN — the SIBLING
    # of the cingulum under the white_matter container:
    #
    #   white_matter.corona_radiata
    #
    # The corona radiata is a projection-fiber fan; the cingulum is
    # a specific named association bundle.

Reaching the internal capsule sibling (recommended consumer
pattern — the deep compact projection-fiber bundle)::

    # The internal capsule is the DEEP, COMPACT PROJECTION-FIBER
    # BUNDLE — the SIBLING of the cingulum under the white_matter
    # container:
    #
    #   white_matter.internal_capsule
    #
    # The internal capsule is a projection-fiber bundle; the
    # cingulum is a specific named association bundle.

Reaching the fornix sibling (recommended consumer pattern — the
hippocampal output tract)::

    # The fornix is the HIPPOCAMPAL OUTPUT TRACT — the SIBLING of
    # the cingulum under the white_matter container:
    #
    #   white_matter.fornix
    #
    # The fornix is a hippocampal output tract (projection fibers to
    # the diencephalon); the cingulum is a specific named
    # association bundle.

Reaching the corpus callosum (recommended consumer pattern — the
commissural structure, NOT under white_matter/)::

    # The corpus callosum is the COMMISSURAL STRUCTURE — wired
    # under ``commissures/``, NOT under ``white_matter/``:
    #
    #   right.commissures.corpus_callosum
    #
    # The cingulum runs AROUND the corpus callosum (in the
    # cingulate gyrus), but the corpus callosum itself is a
    # separate commissural structure that connects the two
    # hemispheres (the left hemisphere, from this hemisphere's
    # perspective).

Reaching the cingulate cortex (recommended consumer pattern — the
grey-matter sheet the cingulum runs within)::

    # The cingulate cortex is the GREY-MATTER SHEET of the
    # cingulate gyrus — the structure the cingulum runs WITHIN:
    #
    #   right.cortex.cingulate
    #
    # The cingulate cortex is grey matter; the cingulum is white
    # matter — the myelinated axons that run within the cingulate
    # gyrus.

Reaching the parahippocampal gyrus and the entorhinal cortex
(recommended consumer pattern — the grey-matter targets at the
posterior end of the cingulum)::

    # The parahippocampal gyrus and the entorhinal cortex are the
    # GREY-MATTER structures at the posterior end of the cingulum:
    #
    #   right.cortex.temporal.gyri.parahippocampal_gyrus
    #   right.cortex.temporal.gyri.entorhinal_cortex
    #
    # The parahippocampal gyrus and the entorhinal cortex are grey
    # matter; the cingulum is white matter — the association bundle
    # that connects them to the cingulate cortex.

Reaching the hippocampus, the subiculum, or the amygdala
(recommended consumer pattern — the grey-matter structures the
cingulum interacts with INDIRECTLY)::

    # The hippocampus, the subiculum, and the amygdala are the
    # GREY-MATTER structures that the cingulum interacts with
    # INDIRECTLY via the parahippocampal gyrus and the entorhinal
    # cortex:
    #
    #   right.subcortical.medial_temporal_lobe.hippocampus
    #   right.subcortical.medial_temporal_lobe.hippocampus.subiculum
    #   right.subcortical.medial_temporal_lobe.amygdala
    #
    # The cingulum does NOT directly project to the hippocampus,
    # the subiculum, or the amygdala — its relationship to those
    # structures is indirect, via the parahippocampal / entorhinal
    # cortical relay.

Reaching the white_matter container (recommended consumer pattern —
the container)::

    # The white_matter container contains the cingulum and the other
    # nine white-matter leaves:
    #
    #   right.white_matter
    #
    # The cingulum is ONE of the ten children of the white_matter
    # container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the cingulum is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # cingulum:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The cingulum is SLEA-FREE.

Course-level detail (not wired — consult references)::

    # The cingulum's subdivisions are prose, not modules:
    #   subgenual (anterior) cingulum   -> subcallosal area /
    #                                       paraterminal gyrus;
    #                                       subgenual anterior
    #                                       cingulate (area 25) —
    #                                       DBS target for
    #                                       treatment-resistant
    #                                       depression
    #   dorsal (middle) cingulum        -> cingulate gyrus —
    #                                       core cingulum bundle
    #   posterior / parahippocampal
    #     cingulum                      -> posterior cingulate /
    #                                       retrosplenial cortex —
    #                                       parahippocampal gyrus /
    #                                       entorhinal cortex
    #
    # Do not attempt to resolve these as sub-paths of the
    # cingulum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.white_matter."
            f"cingulum"
        )
        # resolve cg_path through the memory/recall layer

References
----------
*   **Canonical cingulum anatomy:** Schmahmann, J.D., Pandya, D.N.
    (2006). *Fiber Pathways of the Brain*. Oxford University
    Press, New York. (Definitive white-matter anatomy; the
    cingulum as the association bundle of the cingulate gyrus.)
*   **Cingulum bundle anatomy (review):** Bubb, E.J.,
    Metzler-Baddeley, C., Aggleton, J.P. (2018). "The cingulum
    bundle: anatomy, function, and dysfunction." *Neuroscience &
    Biobehavioral Reviews* 92:104–127. (Comprehensive review of
    the cingulum bundle — anatomy, function, and clinical
    associations.)
*   **White-matter atlas (human):** Wakana, S., Jiang, H., Nagae,
    L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter atlas
    of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the cingulum in DTI.)
*   **DTI tractography atlas:** Catani, M., Thiebaut de Schotten,
    M. (2008). "A diffusion tensor imaging tractography atlas for
    virtual in vivo dissections." *Cortex* 44:1105–1132. (The
    cingulum in DTI tractography.)
*   **Cingulum bundle (human connections):** Catani, M., Thiebaut
    de Schotten, M. (2012). *Atlas of Human Brain Connections*.
    Oxford University Press, Oxford. (The cingulum in the human
    connectome.)
*   **Subgenual cingulum DBS for depression:** Mayberg, H.S.,
    Lozano, A.M., Voon, V., McNeely, H.E., Seminowicz, D.,
    Hamani, C., Schwalb, J.M., Kennedy, S.H. (2005). "Deep brain
    stimulation for treatment-resistant depression." *Neuron*
    45:651–660. (The subgenual cingulum as a DBS target for
    treatment-resistant depression.)
*   **Depression and subgenual cingulate:** Mayberg, H.S. (2003).
    "Modulating dysfunctional limbic-cortical circuits in
    depression: towards development of brain-based algorithms for
    diagnosis and optimised treatment." *British Medical
    Bulletin* 65:193–207. (The subgenual anterior cingulate —
    area 25 — in depression.)
*   **Alzheimer's disease and the cingulum bundle:** Bozzali, M.,
    et al. (2012). "The contribution of white matter damage to
    the cognitive profile of Alzheimer's disease." *Journal of
    Alzheimer's Disease* 30:413–423. (Cingulum bundle
    degeneration in Alzheimer's disease — an early DTI marker.)
*   **Mild cognitive impairment and the cingulum bundle:**
    Fellgiebel, A., et al. (2004). "Ultrastructural hippocampal
    and white matter changes in mild cognitive impairment: a
    diffusion tensor imaging study." *Neurobiology of Aging*
    25:641–648. (Cingulum bundle DTI changes in MCI.)
*   **Schizophrenia and the cingulum bundle (contested):**
    Kubicki, M., et al. (2003). "A review of diffusion tensor
    imaging studies in schizophrenia." *Journal of Psychiatric
    Research* 37:15–30. (Cingulum bundle DTI abnormalities in
    schizophrenia — contested.)
*   **Traumatic brain injury and the cingulum bundle:** Kraus,
    M.F., et al. (2007). "White matter integrity and cognition in
    chronic traumatic brain injury." *Brain* 130:289–303.
    (Cingulum bundle damage after TBI.)
*   **Multiple sclerosis and the cingulum bundle:** Roosendaal,
    S.D., et al. (2010). "Structural and functional hippocampal
    changes in multiple sclerosis." *Radiology* 256:848–856.
    (Cingulum bundle and hippocampal changes in MS.)
*   **Vascular dementia and the cingulum bundle:** O'Sullivan, M.,
    et al. (2004). "Diffusion tensor MRI correlates with
    executive dysfunction in patients with ischaemic
    leukoaraiosis." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 75:441–447. (Cingulum bundle DTI changes in
    vascular dementia / small-vessel disease.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    cingulum is not the amnesia substrate):** Scoville, W.B.,
    Milner, B. (1957). "Loss of recent memory after bilateral
    hippocampal lesions." *Journal of Neurology, Neurosurgery,
    and Psychiatry* 20:11–21. (Bilateral hippocampal damage and
    anterograde amnesia — distinct from the cingulum.)
*   **Amygdala (contrast — the cingulum is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the cingulum.)
*   **SLEA (contrast — the cingulum is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    cingulum.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Cingulum in overview.)
*   NeuroNames — Cingulum (right); FMA — Cingulum (right member).
"""