"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area.lateral_parabrachial_nucleus
==================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parabrachial_area
                ├── lateral_parabrachial_nucleus   <-- THIS MODULE
                ├── medial_parabrachial_nucleus
                └── subparabrachial_nucleus
                    ├── kolliker_fuse_nucleus
                    └── pontine_respiratory_group

**Primary synonym:** Lateral parabrachial nucleus; lateral parabrachial
subnucleus; LPB; LPBN; "the pontine visceral-sensory and pain/aversion
relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — a **viscerotopically and
somatotopically organized neuron cluster** in the **dorsolateral
parabrachial area**, flanking the **dorsolateral superior cerebellar
peduncle** in the **dorsal pons**, beneath the **floor of the fourth
ventricle**. It is the **principal pontine relay** for **visceral
sensation**, **taste**, **pain**, **temperature**, **aversion**, and
**food intake suppression**.
**Part of:** The **parabrachial_area** container — specifically, the
**visceral-sensory and pain/aversion** component. The **parabrachial
area** is the **dorsal tegmental visceral-sensory and respiratory-relay
complex** of the **pons**.
**Structural parent:** ``.../parabrachial_area/`` → **direct child** of
the parabrachial_area container.
**Structural children:** **None.** This is a **leaf** module. The **CGRP-
expressing**, **PDYN-expressing**, **FoxP2-expressing**, and other
**molecularly defined neuron populations** — and the **viscerotopic
subnuclei** (the **external lateral**, **dorsal lateral**, **central
lateral**, **ventral lateral**, and **superior lateral** subnuclei) — are
documented as **prose**, not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
lateral parabrachial nucleus is a LEAF, not a container.** It has **no
structural children**. The **CGRP-expressing**, **PDYN-expressing**,
**FoxP2-expressing**, and other **molecularly defined neuron
populations** — and the **viscerotopic subnuclei** — are **prose
populations and sub-regions**, not structural children. Consumers must
**not** treat the lateral parabrachial nucleus as a container, and must
**not** assume the molecular populations or viscerotopic subnuclei exist
as sub-modules.
**Boundary status (NOT the medial parabrachial nucleus — that is a
SIBLING):** **Boundary case — the lateral parabrachial nucleus is NOT
the medial parabrachial nucleus; the medial parabrachial nucleus is a
SIBLING under the parabrachial_area container.** The **medial
parabrachial nucleus**
(``.../parabrachial_area/medial_parabrachial_nucleus/``) is the
**respiratory and autonomic relay**. The **lateral parabrachial
nucleus** (here) is the **visceral-sensory and pain/aversion relay**.
They are **DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory/autonomic), different
downstream targets (amygdala/BNST/insula/hypothalamus/VPMpc/PAG vs.
VRG/Kölliker-Fuse). They are **anatomically adjacent** (both are in the
dorsal parabrachial area) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the lateral parabrachial
nucleus with the medial parabrachial nucleus.
**Boundary status (NOT the subparabrachial nucleus — that is a
SIBLING):** **Boundary case — the lateral parabrachial nucleus is NOT
the subparabrachial nucleus; the subparabrachial nucleus is a SIBLING
under the parabrachial_area container.** The **subparabrachial nucleus**
(``.../parabrachial_area/subparabrachial_nucleus/``) is the **pontine
respiratory center** — it contains the **Kölliker-Fuse nucleus** and the
**pontine respiratory group**. The **lateral parabrachial nucleus**
(here) is the **visceral-sensory and pain/aversion relay**. They are
**DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory rhythm), different
downstream targets. Consumers must **not** conflate the lateral
parabrachial nucleus with the subparabrachial nucleus.
**Boundary status (NOT the Kölliker-Fuse nucleus or the pontine
respiratory group — those are STRUCTURAL NEPHEWS):** **Boundary case —
the lateral parabrachial nucleus is NOT the Kölliker-Fuse nucleus or the
pontine respiratory group; those are STRUCTURAL NEPHEWS (children of the
subparabrachial nucleus, which is a sibling of the lateral parabrachial
nucleus).** The **Kölliker-Fuse nucleus** and the **pontine respiratory
group** are children of the **subparabrachial_nucleus** — a **sibling**
of the lateral parabrachial nucleus. They are **structural nephews** of
the lateral parabrachial nucleus, not the lateral parabrachial nucleus
itself. Consumers must **not** conflate the lateral parabrachial nucleus
with the Kölliker-Fuse nucleus or the pontine respiratory group.
**Boundary status (NOT the superior cerebellar peduncle — that is the
WHITE-MATTER TRACT the nucleus FLANKS):** **Boundary case — the lateral
parabrachial nucleus is the GREY-MATTER NUCLEUS, NOT the superior
cerebellar peduncle.** The **superior cerebellar peduncle** (the
"brachium conjunctivum") is the **white-matter tract** that carries
**cerebellar efferents** from the **dentate nucleus** and the
**interposed nucleus** to the **red nucleus** and the **thalamus**. The
**lateral parabrachial nucleus** (here) is the **grey-matter neuron
cluster** that **flanks** the **dorsolateral superior cerebellar
peduncle** — hence the name "para-brachial" (alongside the brachium).
They are **DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**peduncle** is white matter. **This distinction is the etymological
origin of the name and is a classic source of confusion** — consumers
must **not** conflate the lateral parabrachial nucleus with the
superior cerebellar peduncle. The nucleus **flanks** the peduncle; it is
**not** the peduncle.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the lateral parabrachial
nucleus is NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain — it
is in the **pontine tegmentum**, **ventromedial** to the lateral
parabrachial nucleus. The **lateral parabrachial nucleus** (here) is the
**visceral-sensory and pain/aversion relay**. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (glutamate, CGRP, PDYN, etc.
vs. norepinephrine), different functional systems
(visceral-sensory/pain/aversion vs. noradrenergic arousal). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the lateral parabrachial
nucleus with the locus coeruleus.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
UPSTREAM SOURCE):** **Boundary case — the lateral parabrachial nucleus
is NOT the solitary nucleus.** The **solitary nucleus** (nucleus tractus
solitarius, ``.../medulla_oblongata/solitary_nucleus/left/`` and
``.../right/``) is the **medullary visceral-afferent hub** for **CN VII,
IX, and X** — **taste**, **visceral sensation**, **baroreception**,
**respiratory chemoreception**, and **gastrointestinal** afferents. The
**solitary nucleus** is the **upstream source** — it **projects to** the
**lateral parabrachial nucleus** via the **central tegmental tract**. The
**lateral parabrachial nucleus** (here) is the **pontine relay** that
**receives** the solitary nucleus projections and **projects** them to
the **amygdala**, **BNST**, **insula**, **hypothalamus**, **VPMpc
thalamus**, and **PAG**. They are **DIFFERENT STRUCTURES** — the
**solitary nucleus** is **medullary** and **upstream**; the **lateral
parabrachial nucleus** is **pontine** and **downstream**. **This
distinction is clinically load-bearing** — a **solitary nucleus** lesion
causes **impaired visceral afferent integration** (loss of taste,
visceral sensation, baroreception, respiratory chemoreception); a
**lateral parabrachial nucleus** lesion causes **impaired relay** of
those signals to the forebrain (blunted visceral sensation, blunted
taste, blunted pain/aversion). Consumers must **not** conflate the
lateral parabrachial nucleus with the solitary nucleus.
**Boundary status (NOT the spinoparabrachial tract — that is the
WHITE-MATTER AFFERENT TRACT):** **Boundary case — the lateral
parabrachial nucleus is NOT the spinoparabrachial tract.** The
**spinoparabrachial tract** is the **white-matter ascending tract** that
**carries** the **lamina I pain and temperature afferents** from the
**spinal cord dorsal horn** to the **contralateral lateral parabrachial
nucleus**. The **lateral parabrachial nucleus** (here) is the
**grey-matter neuron cluster** that **receives** those axons. They are
**DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the **tract**
is white matter. **This distinction is clinically load-bearing** — the
**spinoparabrachial tract** is the **pain and temperature afferent
pathway**; the **lateral parabrachial nucleus** is the **central relay**
that **projects** pain and temperature signals to the **amygdala**
(emotional/autonomic aspects of pain), the **hypothalamus**, and the
**PAG** (descending pain modulation). Consumers must **not** conflate
the lateral parabrachial nucleus with the spinoparabrachial tract.
**Boundary status (NOT the central tegmental tract — that is the
WHITE-MATTER AFFERENT TRACT):** **Boundary case — the lateral
parabrachial nucleus is NOT the central tegmental tract.** The **central
tegmental tract** is the **white-matter ascending tract** that **carries**
the **solitary nucleus visceral afferents** (taste, visceral sensation,
baroreception, respiratory chemoreception) to the **ipsilateral lateral
parabrachial nucleus**. The **lateral parabrachial nucleus** (here) is
the **grey-matter neuron cluster** that **receives** those axons. They
are **DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**tract** is white matter. Consumers must **not** conflate the lateral
parabrachial nucleus with the central tegmental tract.
**Boundary status (NOT the central nucleus of the amygdala — that is a
DOWNSTREAM TARGET):** **Boundary case — the lateral parabrachial nucleus
is NOT the central nucleus of the amygdala.** The **central nucleus of
the amygdala** (``.../amygdala/central_nucleus/``) is the **fear-output
structure** — it **receives** the **lateral parabrachial nucleus
projections** (for **visceral sensation**, **pain**, **aversion**,
**food intake suppression**) and **drives** the **autonomic and
behavioral fear responses**. The **lateral parabrachial nucleus** (here)
is the **pontine visceral-sensory and pain/aversion relay** — it is the
**upstream source**. They are **DIFFERENT STRUCTURES** — the **lateral
parabrachial nucleus** is **pontine** and **upstream**; the **central
nucleus** is **forebrain** (amygdala) and **downstream**. **This
distinction is clinically load-bearing** — the **central nucleus** is a
**fear-output structure** (SLEA component); the **lateral parabrachial
nucleus** is a **visceral/pain relay** (not an SLEA component, but it
**projects to** the SLEA). Consumers must **not** conflate the lateral
parabrachial nucleus with the central nucleus of the amygdala.
**Boundary status (NOT the BNST — that is a DOWNSTREAM TARGET):**
**Boundary case — the lateral parabrachial nucleus is NOT the BNST.** The
**bed nucleus of the stria terminalis (BNST)**
(``.../extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/``)
is the **SLEA component** — it **receives** the **lateral parabrachial
nucleus projections** (for **visceral sensation**, **pain**, **aversion**,
**food intake suppression**) and **drives** the **sustained autonomic
and behavioral stress responses**. The **lateral parabrachial nucleus**
(here) is the **pontine visceral-sensory and pain/aversion relay** — it
is the **upstream source**. They are **DIFFERENT STRUCTURES** — the
**lateral parabrachial nucleus** is **pontine** and **upstream**; the
**BNST** is **forebrain** and **downstream**. **This distinction is
clinically load-bearing** — the **BNST** is an **SLEA component**; the
**lateral parabrachial nucleus** is a **visceral/pain relay** (not an
SLEA component, but it **projects to** the SLEA). Consumers must **not**
conflate the lateral parabrachial nucleus with the BNST.
**Boundary status (NOT the insula — that is a DOWNSTREAM CORTICAL
TARGET):** **Boundary case — the lateral parabrachial nucleus is NOT the
insula.** The **insula**
(``.../cerebral_hemispheres/left/cortex/insular/`` and ``.../right/``)
is a **cortical target** of the lateral parabrachial nucleus — it
**receives** the **visceral** and **taste** projections and **mediates**
the **conscious perception** of **visceral sensation** and **taste**.
The **lateral parabrachial nucleus** (here) is the **pontine
visceral-sensory relay** — it is the **upstream source**. They are
**DIFFERENT STRUCTURES** — the **lateral parabrachial nucleus** is
**pontine** and **upstream**; the **insula** is **cortical** and
**downstream**. Consumers must **not** conflate the lateral parabrachial
nucleus with the insula.
**Boundary status (NOT the hypothalamus — that is a DOWNSTREAM TARGET):**
**Boundary case — the lateral parabrachial nucleus is NOT the
hypothalamus.** The **hypothalamus**
(``.../diencephalon/hypothalamus/``) is a **diencephalic target** of the
lateral parabrachial nucleus — it **receives** the **visceral**,
**taste**, **pain**, and **thermoregulatory** projections and **mediates**
the **autonomic** and **neuroendocrine** responses. The **lateral
parabrachial nucleus** (here) is the **pontine visceral-sensory relay**
— it is the **upstream source**. They are **DIFFERENT STRUCTURES** — the
**lateral parabrachial nucleus** is **pontine** and **upstream**; the
**hypothalamus** is **diencephalic** and **downstream**. Consumers must
**not** conflate the lateral parabrachial nucleus with the
hypothalamus.
**Boundary status (NOT the VPMpc thalamus — that is a DOWNSTREAM
THALAMIC RELAY):** **Boundary case — the lateral parabrachial nucleus is
NOT the VPMpc thalamus.** The **ventral posteromedial nucleus,
parvicellular part (VPMpc)**
(``.../diencephalon/thalamus/left/ventral_nuclear_group/ventral_posterior_nucleus/ventral_posterior_medial_nucleus/``)
is the **thalamic relay** that **receives** the **lateral parabrachial
nucleus taste projections** and **relays** them to the **primary
gustatory cortex** (in the insula). The **lateral parabrachial nucleus**
(here) is the **pontine visceral-sensory relay** — it is the **upstream
source**. They are **DIFFERENT STRUCTURES** — the **lateral parabrachial
nucleus** is **pontine** and **upstream**; the **VPMpc thalamus** is
**diencephalic** and **downstream**. Consumers must **not** conflate the
lateral parabrachial nucleus with the VPMpc thalamus.
**Boundary status (NOT the periaqueductal gray — that is a DOWNSTREAM
MIDBRAIN TARGET):** **Boundary case — the lateral parabrachial nucleus is
NOT the periaqueductal gray (PAG).** The **PAG**
(``.../midbrain/tegmentum/periaqueductal_gray/``) is the **midbrain
pain-modulation and defensive-behavior center** — it **receives** the
**lateral parabrachial nucleus pain projections** and **projects** to the
**rostral ventromedial medulla** and the **spinal cord** for
**descending pain modulation**. The **lateral parabrachial nucleus**
(here) is the **pontine visceral-sensory and pain relay** — it is the
**upstream source**. They are **DIFFERENT STRUCTURES** — different
brainstem levels (pons vs. midbrain), different functional roles
(ascending relay vs. descending modulation). Consumers must **not**
conflate the lateral parabrachial nucleus with the PAG.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
molecularly defined populations):** **Boundary case — the lateral
parabrachial nucleus is NOT a single uniform neuron population; it
contains MULTIPLE molecularly defined populations that serve different
functions.** The **CGRP-expressing neurons** (in the **external lateral
subnucleus**) mediate **learned taste aversion** and **food intake
suppression** — they **project to** the **central nucleus of the
amygdala** and the **BNST**. The **PDYN-expressing neurons** (in the
**dorsal lateral subnucleus**) mediate **thermal sensation** and
**pain** — they **project to** the **PAG** and the **hypothalamus**.
The **FoxP2-expressing neurons** mediate **visceral sensation** — they
**project to** the **insula** and the **VPMpc thalamus**. **These
molecular populations are prose, not structural children.** Consumers
must **not** treat the lateral parabrachial nucleus as a single uniform
population — it is a **molecularly heterogeneous complex** with
**functionally distinct** sub-circuits.
**Boundary status (SLEA-FREE — but it PROJECTS TO the SLEA):** **Boundary
case — the lateral parabrachial nucleus is SLEA-FREE, but it PROJECTS TO
the SLEA.** The **lateral parabrachial nucleus** is **NOT** an
extended-amygdala component — it carries **NO SLEA warning**. **However**,
the lateral parabrachial nucleus **projects to** the **central nucleus of
the amygdala** and the **BNST** — these are **SLEA components** and are
**downstream targets** of the lateral parabrachial nucleus. The
**lateral parabrachial nucleus** is **upstream** of the SLEA, not part of
it. Consumers must **not** conflate the lateral parabrachial nucleus with
the SLEA continuum — the lateral parabrachial nucleus is **upstream** of
the SLEA.

Overview
--------
The lateral parabrachial nucleus is the **visceral-sensory and
pain/aversion relay** of the **parabrachial area** — a **molecularly
heterogeneous** and **viscerotopically organized** grey-matter nucleus in
the **dorsolateral parabrachial area**, flanking the **dorsolateral
superior cerebellar peduncle** in the **dorsal pons**. It is a **leaf**
module under the parabrachial_area container, and it is the **principal
pontine relay** for **visceral sensation**, **taste**, **pain**,
**temperature**, **aversion**, and **food intake suppression**.

**The lateral parabrachial nucleus is a LEAF, not a container.** It has
**no structural children**. The **CGRP-expressing**, **PDYN-expressing**,
**FoxP2-expressing**, and other **molecularly defined neuron
populations** — and the **viscerotopic subnuclei** (external lateral,
dorsal lateral, central lateral, ventral lateral, superior lateral) —
are **prose populations and sub-regions**, not structural children.

**The lateral parabrachial nucleus is GREY-MATTER, NOT the superior
cerebellar peduncle.** The **superior cerebellar peduncle** (brachium
conjunctivum) is the **white-matter tract** that the lateral parabrachial
nucleus **flanks** — hence the name "para-brachial" (alongside the
brachium). They are **DIFFERENT STRUCTURES** — the **nucleus** is grey
matter; the **peduncle** is white matter. **This distinction is the
etymological origin of the name and is a classic source of confusion.**

**The lateral parabrachial nucleus is NOT the medial parabrachial nucleus
or the subparabrachial nucleus.** Those are **siblings** under the
parabrachial_area container — the **medial parabrachial nucleus** is the
**respiratory and autonomic relay**; the **subparabrachial nucleus** is
the **pontine respiratory center** (containing the Kölliker-Fuse nucleus
and the pontine respiratory group). They are **DIFFERENT STRUCTURES** —
different functional systems, different downstream targets.

**The lateral parabrachial nucleus is NOT the solitary nucleus.** The
**solitary nucleus** is the **medullary visceral-afferent hub** that
**projects to** the lateral parabrachial nucleus. The lateral parabrachial
nucleus is the **pontine downstream relay**.

**The lateral parabrachial nucleus is NOT the locus coeruleus.** The
**locus coeruleus** is the **noradrenergic nucleus** — it is
**anatomically adjacent** to the lateral parabrachial nucleus, but it is
a **different structure**.

**The lateral parabrachial nucleus is MOLECULARLY HETEROGENEOUS.** The
**CGRP**, **PDYN**, **FoxP2**, and other **molecular populations** serve
different functions — **CGRP** (aversion and food intake), **PDYN**
(thermal sensation and pain), **FoxP2** (visceral sensation). They are
**prose populations**, not structural children.

**The lateral parabrachial nucleus is SLEA-FREE but PROJECTS TO the
SLEA.** It is **not** an extended-amygdala component, but it **projects
to** the **central nucleus of the amygdala** and the **BNST** — which are
**SLEA components** and **downstream targets**. The lateral parabrachial
nucleus is **upstream** of the SLEA, not part of it.

Prose Population Composition (prose, not structural children)
--------------------------------------------------------------
The lateral parabrachial nucleus contains **multiple molecularly defined
neuron populations** and **viscerotopic subnuclei** — documented as
**prose**, not as structural children:

*   **CGRP-expressing neurons (external lateral subnucleus)** — the
    **calcitonin gene-related peptide (CGRP)** neurons in the **external
    lateral subnucleus**. They **receive** visceral malaise signals from
    the **solitary nucleus** (e.g. from **gastrointestinal** irritation,
    **toxin** detection) and **project to** the **central nucleus of the
    amygdala** (the **capsular** part) and the **BNST** — they **mediate
    learned taste aversion** (the association between a novel taste and
    visceral illness) and **food intake suppression**. **Aversion and
    food intake suppression are the functional systems** subserved
    primarily by the CGRP-expressing neurons.

*   **PDYN-expressing neurons (dorsal lateral subnucleus)** — the
    **prodynorphin (PDYN)** neurons in the **dorsal lateral subnucleus**.
    They **receive** pain and temperature signals from the **spinal cord
    dorsal horn** (lamina I, via the **spinoparabrachial tract**) and
    **project to** the **periaqueductal gray (PAG)** and the
    **hypothalamus** — they **mediate thermal sensation**, **pain**, and
    **descending pain modulation**. **Thermal sensation and pain
    modulation are the functional systems** subserved primarily by the
    PDYN-expressing neurons.

*   **FoxP2-expressing neurons (central lateral, ventral lateral, superior
    lateral subnuclei)** — the **forkhead box P2 (FoxP2)** neurons in the
    **central lateral**, **ventral lateral**, and **superior lateral**
    subnuclei. They **receive** visceral and taste signals from the
    **solitary nucleus** and **project to** the **insula** (via the
    **VPMpc thalamus**) and the **hypothalamus** — they **mediate
    visceral sensation** and **taste**. **Visceral sensation and taste
    are the functional systems** subserved primarily by the
    FoxP2-expressing neurons.

**These populations are prose, not structural children.** The tree wires
the **lateral parabrachial nucleus** as a **single leaf** under the
parabrachial_area container — the **CGRP**, **PDYN**, **FoxP2**, and other
molecular populations — and the **viscerotopic subnuclei** (external
lateral, dorsal lateral, central lateral, ventral lateral, superior
lateral) — are **prose**, not structural children. Consumers that need
**molecular-population-level** or **viscerotopic-subnucleus-level**
resolution should consult the references, not the tree.

The Lateral Parabrachial Nucleus / Medial Parabrachial Nucleus Boundary
----------------------------------------------------------------------
This is the **sibling** boundary — **visceral-sensory/pain/aversion vs.
respiratory/autonomic**:

*   **Lateral parabrachial nucleus** (this module) — the
    **visceral-sensory and pain/aversion relay**.

*   **Medial parabrachial nucleus**
    (``.../parabrachial_area/medial_parabrachial_nucleus/``) — the
    **respiratory and autonomic relay**.

**They are DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory/autonomic), different
downstream targets. They are **anatomically adjacent** (both are in the
dorsal parabrachial area) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the lateral parabrachial
nucleus with the medial parabrachial nucleus.

The Lateral Parabrachial Nucleus / Subparabrachial Nucleus Boundary
-------------------------------------------------------------------
This is the **sibling** boundary — **visceral-sensory/pain/aversion vs.
respiratory rhythm**:

*   **Lateral parabrachial nucleus** (this module) — the
    **visceral-sensory and pain/aversion relay**.

*   **Subparabrachial nucleus**
    (``.../parabrachial_area/subparabrachial_nucleus/``) — the **pontine
    respiratory center** (containing the **Kölliker-Fuse nucleus** and
    the **pontine respiratory group**).

**They are DIFFERENT STRUCTURES** — different functional systems
(visceral-sensory/pain/aversion vs. respiratory rhythm), different
downstream targets. Consumers must **not** conflate the lateral
parabrachial nucleus with the subparabrachial nucleus.

The Lateral Parabrachial Nucleus / Kölliker-Fuse Nucleus and Pontine Respiratory Group Boundary
---------------------------------------------------------------------------------------------
This is the **structural nephew** boundary:

*   **Lateral parabrachial nucleus** (this module) — the
    **visceral-sensory and pain/aversion relay**.

*   **Kölliker-Fuse nucleus** and **pontine respiratory group** —
    **children** of the **subparabrachial_nucleus**, which is a
    **sibling** of the lateral parabrachial nucleus.

**They are DIFFERENT STRUCTURES** — the **Kölliker-Fuse nucleus** and the
**pontine respiratory group** are **structural nephews** (siblings' own
children) of the lateral parabrachial nucleus, not the lateral
parabrachial nucleus itself. Consumers must **not** conflate the lateral
parabrachial nucleus with the Kölliker-Fuse nucleus or the pontine
respiratory group.

The Lateral Parabrachial Nucleus / Superior Cerebellar Peduncle Boundary
-----------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **etymological
origin of the name**:

*   **Lateral parabrachial nucleus** (this module) — the **grey-matter
    neuron cluster** flanking the dorsolateral superior cerebellar
    peduncle.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES.** The **nucleus** is grey matter; the
**peduncle** is white matter. The nucleus **flanks** the peduncle; it is
**not** the peduncle. **This distinction is the etymological origin of
the name "parabrachial"** ("para-" = alongside, "brachium" = the superior
cerebellar peduncle) — and it is a **classic source of confusion**.
Consumers must **not** conflate the lateral parabrachial nucleus with the
superior cerebellar peduncle.

The Lateral Parabrachial Nucleus / Locus Coeruleus Boundary
-----------------------------------------------------------
This is the **anatomically adjacent** boundary — **visceral/pain/aversion
relay vs. noradrenergic nucleus**:

*   **Lateral parabrachial nucleus** (this module) — the
    **visceral-sensory and pain/aversion relay**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of norepinephrine**
    in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, CGRP, PDYN, etc. vs. norepinephrine), different functional
systems (visceral-sensory/pain/aversion vs. noradrenergic arousal). They
are **anatomically adjacent** (both are in the dorsal pons near the
floor of the fourth ventricle) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the lateral parabrachial
nucleus with the locus coeruleus.

The Lateral Parabrachial Nucleus / Solitary Nucleus Boundary
------------------------------------------------------------
This is the **upstream source vs. pontine relay** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory and pain/aversion relay**.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** — it **projects to** the
lateral parabrachial nucleus via the **central tegmental tract**. The
**lateral parabrachial nucleus** (here) is the **pontine relay** that
**receives** the solitary nucleus projections and **projects** them to
the forebrain. They are **DIFFERENT STRUCTURES** — the **solitary
nucleus** is **medullary** and **upstream**; the **lateral parabrachial
nucleus** is **pontine** and **downstream**. **This distinction is
clinically load-bearing** — a **solitary nucleus** lesion causes
**impaired visceral afferent integration** (loss of taste, visceral
sensation, baroreception, respiratory chemoreception); a **lateral
parabrachial nucleus** lesion causes **impaired relay** of those signals
to the forebrain (blunted visceral sensation, blunted taste, blunted
pain/aversion). Consumers must **not** conflate the lateral parabrachial
nucleus with the solitary nucleus.

The Lateral Parabrachial Nucleus / Spinoparabrachial Tract Boundary
-------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **pain and
temperature afferent tract**:

*   **Lateral parabrachial nucleus** (this module) — the **grey-matter
    neuron cluster** that **receives** the spinoparabrachial axons.

*   **Spinoparabrachial tract** — the **white-matter ascending tract**
    that carries the **lamina I pain and temperature afferents** from
    the spinal cord dorsal horn to the **contralateral lateral
    parabrachial nucleus**.

**They are DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**tract** is white matter. **This distinction is clinically
load-bearing** — the **spinoparabrachial tract** is the **pain and
temperature afferent pathway**; the **lateral parabrachial nucleus** is
the **central relay** that **projects** pain and temperature signals to
the **amygdala** (emotional/autonomic aspects of pain), the
**hypothalamus**, and the **PAG** (descending pain modulation). Consumers
must **not** conflate the lateral parabrachial nucleus with the
spinoparabrachial tract.

The Lateral Parabrachial Nucleus / Central Tegmental Tract Boundary
-------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **visceral
afferent tract**:

*   **Lateral parabrachial nucleus** (this module) — the **grey-matter
    neuron cluster** that **receives** the central tegmental tract axons.

*   **Central tegmental tract** — the **white-matter ascending tract**
    that carries the **solitary nucleus visceral afferents** (taste,
    visceral sensation, baroreception, respiratory chemoreception) to
    the **ipsilateral lateral parabrachial nucleus**.

**They are DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**tract** is white matter. Consumers must **not** conflate the lateral
parabrachial nucleus with the central tegmental tract.

The Lateral Parabrachial Nucleus / Central Nucleus of the Amygdala Boundary
---------------------------------------------------------------------------
This is the **upstream relay vs. downstream SLEA target** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory and pain/aversion relay** — **upstream**.

*   **Central nucleus of the amygdala** (``.../amygdala/central_nucleus/``)
    — the **fear-output structure** — **downstream SLEA target**.

**They are DIFFERENT STRUCTURES** — the **lateral parabrachial nucleus**
is **pontine** and **upstream**; the **central nucleus** is **forebrain**
(amygdala) and **downstream**. **This distinction is clinically
load-bearing** — the **central nucleus** is a **fear-output structure**
(SLEA component); the **lateral parabrachial nucleus** is a
**visceral/pain relay** (not an SLEA component, but it **projects to**
the SLEA). Consumers must **not** conflate the lateral parabrachial
nucleus with the central nucleus of the amygdala.

The Lateral Parabrachial Nucleus / BNST Boundary
------------------------------------------------
This is the **upstream relay vs. downstream SLEA target** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory and pain/aversion relay** — **upstream**.

*   **BNST**
    (``.../extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/``)
    — the **SLEA component** — **downstream SLEA target**.

**They are DIFFERENT STRUCTURES** — the **lateral parabrachial nucleus**
is **pontine** and **upstream**; the **BNST** is **forebrain** and
**downstream**. **This distinction is clinically load-bearing** — the
**BNST** is an **SLEA component**; the **lateral parabrachial nucleus**
is a **visceral/pain relay** (not an SLEA component, but it **projects
to** the SLEA). Consumers must **not** conflate the lateral parabrachial
nucleus with the BNST.

The Lateral Parabrachial Nucleus / Insula Boundary
--------------------------------------------------
This is the **pontine relay vs. cortical target** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory relay** — **upstream**.

*   **Insula** (``.../cerebral_hemispheres/left/cortex/insular/`` and
    ``.../right/``) — the **cortical target** for **visceral sensation**
    and **taste** — **downstream**.

**They are DIFFERENT STRUCTURES** — the **lateral parabrachial nucleus**
is **pontine** and **upstream**; the **insula** is **cortical** and
**downstream**. The lateral parabrachial nucleus **projects to** the
insula (via the **VPMpc thalamus** for taste; via **direct** and
**indirect** pathways for visceral sensation). Consumers must **not**
conflate the lateral parabrachial nucleus with the insula.

The Lateral Parabrachial Nucleus / Hypothalamus Boundary
--------------------------------------------------------
This is the **pontine relay vs. diencephalic target** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory and pain/aversion relay** — **upstream**.

*   **Hypothalamus** (``.../diencephalon/hypothalamus/``) — the
    **diencephalic target** for **autonomic**, **neuroendocrine**, and
    **thermoregulatory** responses — **downstream**.

**They are DIFFERENT STRUCTURES** — the **lateral parabrachial nucleus**
is **pontine** and **upstream**; the **hypothalamus** is
**diencephalic** and **downstream**. The lateral parabrachial nucleus
**projects to** the hypothalamus. Consumers must **not** conflate the
lateral parabrachial nucleus with the hypothalamus.

The Lateral Parabrachial Nucleus / VPMpc Thalamus Boundary
----------------------------------------------------------
This is the **pontine relay vs. thalamic relay** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory relay** — **upstream**.

*   **VPMpc thalamus**
    (``.../diencephalon/thalamus/left/ventral_nuclear_group/ventral_posterior_nucleus/ventral_posterior_medial_nucleus/``)
    — the **thalamic relay** for **taste** — **downstream**.

**They are DIFFERENT STRUCTURES** — the **lateral parabrachial nucleus**
is **pontine** and **upstream**; the **VPMpc thalamus** is
**diencephalic** and **downstream**. The lateral parabrachial nucleus
**projects to** the VPMpc thalamus. Consumers must **not** conflate the
lateral parabrachial nucleus with the VPMpc thalamus.

The Lateral Parabrachial Nucleus / Periaqueductal Gray Boundary
---------------------------------------------------------------
This is the **ascending relay vs. descending modulation** boundary:

*   **Lateral parabrachial nucleus** (this module) — the **pontine
    visceral-sensory and pain relay** — **upstream**.

*   **Periaqueductal gray (PAG)**
    (``.../midbrain/tegmentum/periaqueductal_gray/``) — the **midbrain
    pain-modulation and defensive-behavior center** — **downstream**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
midbrain), different functional roles (ascending relay vs. descending
modulation). The lateral parabrachial nucleus **projects to** the PAG.
Consumers must **not** conflate the lateral parabrachial nucleus with
the PAG.

The Lateral Parabrachial Nucleus / SLEA Boundary
------------------------------------------------
This is the **SLEA** boundary — **NOT an SLEA component, but UPSTREAM of
the SLEA**:

*   **Lateral parabrachial nucleus** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The lateral parabrachial nucleus is NOT part of the SLEA continuum.**
It is a **pontine visceral-sensory and pain/aversion relay**, and it
carries **no SLEA warning**. **However**, the lateral parabrachial
nucleus **projects to** the **central nucleus of the amygdala** and the
**BNST** — these are **downstream SLEA targets**, not components of the
lateral parabrachial nucleus. The **lateral parabrachial nucleus** is
**upstream** of the SLEA, not part of it. Consumers must **not** conflate
the lateral parabrachial nucleus with the SLEA continuum — the lateral
parabrachial nucleus is **upstream** of the SLEA.

Function in the Human Brain
---------------------------
The lateral parabrachial nucleus's functions are **the pontine relay for
visceral sensation, taste, pain, temperature, aversion, and food intake
suppression** — **NOT a single unified function**:

*   **Visceral Sensation (FoxP2-expressing neurons):** The **FoxP2-
    expressing neurons** in the **central lateral**, **ventral lateral**,
    and **superior lateral** subnuclei **receive** the **visceral
    afferents** from the **solitary nucleus** (gastrointestinal,
    cardiovascular, respiratory) and **project to** the **insula** (via
    the **VPMpc thalamus** for some modalities, directly for others) and
    the **hypothalamus**. They **mediate** the **conscious perception**
    of **visceral sensation** and the **autonomic** and
    **neuroendocrine** responses to visceral afferent input.

*   **Taste (FoxP2-expressing neurons):** The **FoxP2-expressing
    neurons** in the **central lateral** and **ventral lateral**
    subnuclei **receive** the **taste afferents** from the **solitary
    nucleus** (via the **central tegmental tract**) and **project to**
    the **VPMpc thalamus** and then to the **primary gustatory cortex**
    (in the **insula**). They **mediate** the **conscious perception**
    of **taste** — **sweet**, **salty**, **sour**, **bitter**, and
    **umami**.

*   **Pain and Temperature (PDYN-expressing neurons):** The
    **PDYN-expressing neurons** in the **dorsal lateral subnucleus**
    **receive** the **pain and temperature afferents** from the **spinal
    cord dorsal horn** (lamina I, via the **spinoparabrachial tract**)
    and **project to** the **PAG** and the **hypothalamus**. They
    **mediate** the **thermal sensation**, the **affective** and
    **autonomic** aspects of **pain**, and the **descending pain
    modulation** via the **PAG**.

*   **Aversion (CGRP-expressing neurons):** The **CGRP-expressing
    neurons** in the **external lateral subnucleus** **receive**
    **visceral malaise signals** from the **solitary nucleus** (toxin
    detection, gastrointestinal irritation) and **project to** the
    **central nucleus of the amygdala** (the **capsular** part) and the
    **BNST**. They **mediate** **learned taste aversion** — the
    association between a novel taste and visceral illness — and the
    **suppression of food intake** in response to visceral malaise.

*   **Food Intake Suppression (CGRP-expressing neurons):** The
    **CGRP-expressing neurons** also **mediate** the **suppression of
    food intake** in response to **visceral satiety signals** and
    **visceral malaise** — they are the **neural substrate** of the
    **anorectic** response to **visceral illness** and to **satiety
    hormones** (e.g. **CCK**, **GLP-1**) that act via the **solitary
    nucleus** and the **lateral parabrachial nucleus**.

*   **NOT a neural processor in the classical sense.** The lateral
    parabrachial nucleus is a **relay complex** — it **receives**
    ascending visceral, taste, pain, and temperature afferents and
    **projects** them to the forebrain. The **processing** of these
    signals happens in the **solitary nucleus** (visceral afferent
    integration), the **lateral parabrachial nucleus** (pontine relay),
    and the **forebrain targets** (conscious perception, emotional
    responses, autonomic regulation).

**The unifying theme:** the lateral parabrachial nucleus is the **pontine
visceral-sensory and pain/aversion relay** — the **principal pontine
relay** for **visceral sensation**, **taste**, **pain**, **temperature**,
**aversion**, and **food intake suppression**. It is **molecularly
heterogeneous** (CGRP, PDYN, FoxP2, and other populations), **SLEA-FREE**
(but **upstream** of the SLEA — it **projects to** the central nucleus
and BNST), and **NOT the superior cerebellar peduncle** — the **peduncle**
is the white-matter tract that the nucleus **flanks**.

Associated Disorders
--------------------
The lateral parabrachial nucleus has **no named "lateral parabrachial
nucleus syndrome"** — its clinical associations are **molecular-population-
specific**:

*   **CGRP-expressing Neuron Dysfunction — Impaired Learned Taste
    Aversion and Food Intake Regulation:** A lesion or dysfunction of the
    **CGRP-expressing neurons** in the **lateral parabrachial nucleus**
    causes **impaired learned taste aversion** (the ability to associate
    a novel taste with visceral illness is lost) and **impaired food
    intake suppression** (the anorectic response to visceral malaise and
    satiety signals is lost). **This is a critical clinical entity** —
    the **CGRP-expressing neurons** are the **neural substrate** of
    **learned taste aversion** and **food intake suppression**, and
    their dysfunction is implicated in **eating disorders** and
    **obesity**.

*   **PDYN-expressing Neuron Dysfunction — Impaired Thermal Sensation
    and Pain Modulation:** A lesion or dysfunction of the **PDYN-
    expressing neurons** in the **lateral parabrachial nucleus** causes
    **impaired thermal sensation** (blunted temperature perception) and
    **impaired pain modulation** (blunted affective/autonomic aspects of
    pain, impaired descending pain modulation). **This is a critical
    clinical entity** — the **PDYN-expressing neurons** are the **neural
    substrate** of **thermal sensation** and **pain modulation**, and
    their dysfunction is implicated in **chronic pain syndromes** and
    **thermoregulatory disorders**.

*   **FoxP2-expressing Neuron Dysfunction — Impaired Visceral Sensation
    and Taste:** A lesion or dysfunction of the **FoxP2-expressing
    neurons** in the **lateral parabrachial nucleus** causes **impaired
    visceral sensation** (blunted visceral perception) and **impaired
    taste** (blunted taste perception). **This is a critical clinical
    entity** — the **FoxP2-expressing neurons** are the **neural
    substrate** of **visceral sensation** and **taste**, and their
    dysfunction is implicated in **visceral sensory disorders** and
    **taste disorders**.

*   **Lateral Parabrachial Nucleus Lesion — Pan-Modal Visceral-Sensory
    and Pain/Aversion Deficits:** A lesion of the **lateral parabrachial
    nucleus** (e.g. **pontine stroke**, **tumor**, **demyelination**)
    causes **pan-modal deficits** — **impaired visceral sensation**,
    **impaired taste**, **impaired pain and temperature sensation** on
    the **contralateral body** (because the spinoparabrachial tract
    crosses), **impaired learned taste aversion**, and **impaired food
    intake suppression**. **The pan-modal pattern** is the **substrate**
    of the **visceral-sensory and pain/aversion** functions of the
    lateral parabrachial nucleus.

*   **Central Post-Stroke Pain (Thalamic Pain Syndrome) — Lateral
    Parabrachial Nucleus Involvement:** **Central post-stroke pain** is
    a **neuropathic pain syndrome** that occurs after a **stroke**
    affecting the **spinothalamic** and **spinoparabrachial** pathways
    (e.g. **thalamic stroke**, **lateral medullary stroke**). The
    **lateral parabrachial nucleus** is **one of the central relays**
    for the **spinoparabrachial** pathway — its **dysfunction** (or
    **disinhibition**) after stroke may **contribute** to the **central
    pain** phenotype.

*   **Opioid Withdrawal — Lateral Parabrachial Nucleus Involvement:**
    The **lateral parabrachial nucleus** (especially the **CGRP-
    expressing neurons**) is **activated** during **opioid withdrawal**
    — it **mediates** the **aversive** and **autonomic** symptoms of
    **naloxone-precipitated withdrawal** (jumping, diarrhea, ptosis,
    etc.) in **animal models**. The **lateral parabrachial nucleus** is
    **one of the neural substrates** of **opioid withdrawal aversion**.

*   **Chronic Pain — Lateral Parabrachial Nucleus Sensitization:** The
    **lateral parabrachial nucleus** (especially the **PDYN-expressing
    neurons**) is **sensitized** in **chronic pain states** — it
    **contributes** to the **affective** and **autonomic** components of
    **chronic pain**, and to **descending pain modulation** via the
    **PAG**.

*   **Thermoregulatory Disorders — Lateral Parabrachial Nucleus
    Involvement:** The **lateral parabrachial nucleus** (especially the
    **PDYN-expressing neurons** projecting to the **hypothalamus**)
    **mediates** **thermoregulatory** responses to **skin temperature**
    and **core temperature** changes. Its **dysfunction** may
    **contribute** to **thermoregulatory disorders**.

*   **No Named "Lateral Parabrachial Nucleus Syndrome":** The lateral
    parabrachial nucleus is a **molecularly heterogeneous complex** — it
    has **no named clinical syndrome**. Its clinical relevance is
    **molecular-population-specific** — **CGRP** (aversion, food
    intake), **PDYN** (thermal sensation, pain), **FoxP2** (visceral
    sensation, taste).

**What is NOT here:** The lateral parabrachial nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), or **trigeminal neuralgia** (trigeminal nerve root). Its
clinical relevance is **visceral-sensory-pain-aversion-specific**, via
the **CGRP**, **PDYN**, **FoxP2**, and other molecular populations it
subserves. **No named lateral parabrachial nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **single** lateral parabrachial nucleus module. The lateral
parabrachial nuclei are **bilateral in real anatomy** (left and right
flanking the left and right superior cerebellar peduncles), but the tree
wires them as a **single module** — and the module carries **NO warning
at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **lateral_parabrachial_nucleus** module (here) is a **single
    module** that represents the **bilateral lateral parabrachial
    nuclei** (left and right flanking the left and right superior
    cerebellar peduncles). The tree does **not** split them into
    left/right. Consumers must **not** assume a left/right split exists
    at the tree level — the module is a **single, bilateral-container
    representation**.

*   **Ipsilateral Visceral Input (Structural Fact, NOT a Lateralization
    Warning):** The **central tegmental tract** from the **solitary
    nucleus** to the **lateral parabrachial nucleus** is **largely
    ipsilateral** — the **left lateral parabrachial nucleus** receives
    **left solitary nucleus** visceral afferents; the **right lateral
    parabrachial nucleus** receives **right solitary nucleus** visceral
    afferents. This **ipsilateral input** is a **structural fact** of
    the **visceral afferent system** — it is **not** a functional
    lateralization. It is the **neural substrate** of **ipsilateral
    visceral sensation** in **solitary nucleus** and **lateral
    parabrachial nucleus** lesions.

*   **Contralateral Pain and Temperature Input (Structural Fact, NOT a
    Lateralization Warning):** The **spinoparabrachial tract** from the
    **spinal cord dorsal horn** to the **lateral parabrachial nucleus**
    is **crossed** — the **left lateral parabrachial nucleus** receives
    **right spinal cord** pain and temperature afferents; the **right
    lateral parabrachial nucleus** receives **left spinal cord** pain
    and temperature afferents. This **crossed input** is a **structural
    fact** of the **spinoparabrachial system** — it is **not** a
    functional lateralization. It is the **neural substrate** of
    **contralateral pain and temperature sensation** in **lateral
    parabrachial nucleus** lesions.

*   **Bilateral Projections to Forebrain Targets (Structural Fact, NOT a
    Lateralization Warning):** The **lateral parabrachial nucleus**
    **projects** to the **central nucleus of the amygdala**, the
    **BNST**, the **insula**, the **hypothalamus**, the **VPMpc
    thalamus**, and the **PAG** — **bilaterally** (from both left and
    right lateral parabrachial nuclei). This **bilateral projection** is
    a **structural fact** of the **visceral-sensory and pain/aversion
    system** — it is **not** a functional lateralization. It is the
    **neural substrate** of the **bilateral forebrain representation**
    of **visceral sensation**, **taste**, **pain**, and **aversion**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The lateral
    parabrachial nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the lateral
    parabrachial nucleus. **However**, the lateral parabrachial nucleus
    **projects to** the **central nucleus of the amygdala** and the
    **BNST** — these are **downstream SLEA targets**, not components of
    the lateral parabrachial nucleus. The **lateral parabrachial
    nucleus** is **upstream** of the SLEA, not part of it.

*   **NO Amygdala-Lateralization Warning of their own (the lateral
    parabrachial nucleus is VISCERAL/PAIN/AVERSION, not the
    fear-output):** The **right-amygdala fear association** belongs to
    the **amygdala module** — specifically the **central nucleus**
    (fear-output) and the **basolateral nuclei** (fear-learning). The
    lateral parabrachial nucleus is a **pontine visceral-sensory and
    pain/aversion relay** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**. **Note**: the lateral
    parabrachial nucleus **projects to** the central nucleus (a
    fear-output structure), but the lateral parabrachial nucleus itself
    is **not** part of the fear circuit — it is an **upstream
    visceral/pain relay**.

**A consumer that sees "lateral_parabrachial_nucleus" must understand
that the module is a SINGLE, BILATERAL-CONTAINER representation** — it
is **not** a left/right split at the tree level. The **ipsilateral
visceral input** and the **contralateral pain/temperature input** are
**structural facts**, not lateralizations. The lateral parabrachial
nucleus is a **strict-single module with NO warning at the module
level** — **no SLEA warning**, **no amygdala-lateralization warning**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** lateral parabrachial nuclei as a **single module** —
    it does **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../parabrachial_area/medial_parabrachial_nucleus/``,
    ``.../parabrachial_area/subparabrachial_nucleus/``,
    ``.../pons/tegmentum/``, ``.../medulla_oblongata/``,
    ``.../midbrain/``, ``.../diencephalon/``, ``.../cortex/``, or any
    other container. The lateral parabrachial nucleus's relationships to
    the **medial parabrachial nucleus**, the **subparabrachial nucleus**,
    the **Kölliker-Fuse nucleus**, the **pontine respiratory group**, the
    **superior cerebellar peduncle**, the **locus coeruleus**, the
    **solitary nucleus**, the **spinoparabrachial tract**, the **central
    tegmental tract**, the **central nucleus of the amygdala**, the
    **BNST**, the **insula**, the **hypothalamus**, the **VPMpc
    thalamus**, the **periaqueductal gray**, and the **SLEA continuum**
    are documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **CGRP-expressing**,
    **PDYN-expressing**, **FoxP2-expressing**, and other **molecularly
    defined neuron populations** — and the **viscerotopic subnuclei**
    (external lateral, dorsal lateral, central lateral, ventral lateral,
    superior lateral) — are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    molecular-population-level or viscerotopic-subnucleus-level detail
    through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **lateral parabrachial nucleus** is a **single module** that
    represents the **bilateral lateral parabrachial nuclei** — the tree
    does **not** split them into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **MOLECULARLY HETEROGENEOUS — MULTIPLE molecular populations, not a
    single uniform nucleus.** The **CGRP** (aversion, food intake),
    **PDYN** (thermal sensation, pain), **FoxP2** (visceral sensation,
    taste), and other **molecular populations** serve **functionally
    distinct** sub-circuits. Consumers must **not** treat the lateral
    parabrachial nucleus as a single uniform nucleus.
*   **SLEA-FREE — but it PROJECTS TO the SLEA.** The **lateral
    parabrachial nucleus** is **not** an extended-amygdala component,
    and it carries **no SLEA warning**. **However**, the lateral
    parabrachial nucleus **projects to** the **central nucleus of the
    amygdala** and the **BNST** — these are **downstream SLEA targets**,
    not components of the lateral parabrachial nucleus. The **lateral
    parabrachial nucleus** is **upstream** of the SLEA, not part of it.
*   **NOT the fear-output — the lateral parabrachial nucleus is
    VISCERAL/PAIN/AVERSION RELAY.** The **fear-output** structure is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**; the **fear-modulatory / extinction**
    structures are the **basomedial nuclei**. The **lateral parabrachial
    nucleus** is a **pontine visceral-sensory and pain/aversion relay**
    — it is **not** part of the fear circuit. **It projects to** the
    central nucleus (a fear-output structure), but the lateral
    parabrachial nucleus itself is **not** a fear structure.
*   **No ``AREA_PATHS`` hop.** The lateral parabrachial nucleus is a
    local leaf under the parabrachial_area container, not a cross-listed
    leaf.
*   **No nested cross-listing.** The lateral parabrachial nucleus has no
    nested dual-framing module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.parabrachial_area import lateral_parabrachial_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "lateral_parabrachial_nucleus"
    )

**Do not** assume the lateral parabrachial nucleus is a **container**. It
is a **leaf** — its **CGRP**, **PDYN**, **FoxP2**, and other **molecular
populations** — and its **viscerotopic subnuclei** — are **prose**, not
structural children.

**Do not** assume the lateral parabrachial nucleus is **bilateralized at
the tree level**. The lateral parabrachial nuclei are **bilateral in real
anatomy**, but the tree wires them as a **single module** — there is **no
left/right split**. Any lateralization is **contested** and documented in
the literature, not wired.

**Do not** assume the lateral parabrachial nucleus is the **superior
cerebellar peduncle**. The **superior cerebellar peduncle** is the
**white-matter tract** that the lateral parabrachial nucleus **flanks**
— the "para-brachial" name reflects this **flanking relationship**, not
identity. They are **different structures**.

**Do not** assume the lateral parabrachial nucleus is the **medial
parabrachial nucleus** or the **subparabrachial nucleus**. Those are
**siblings** under the parabrachial_area container — the **medial
parabrachial nucleus** is the **respiratory and autonomic relay**; the
**subparabrachial nucleus** is the **pontine respiratory center**. They
are **different structures**.

**Do not** assume the lateral parabrachial nucleus is the **Kölliker-Fuse
nucleus** or the **pontine respiratory group**. Those are **structural
nephews** (children of the subparabrachial nucleus, which is a sibling of
the lateral parabrachial nucleus).

**Do not** assume the lateral parabrachial nucleus is the **locus
coeruleus**. The **locus coeruleus** is the **noradrenergic nucleus** in
the **pontine tegmentum** — it is **anatomically adjacent** to the
lateral parabrachial nucleus, but it is a **different structure**.

**Do not** assume the lateral parabrachial nucleus is the **solitary
nucleus**. The **solitary nucleus** is the **medullary visceral-afferent
hub** that **projects to** the lateral parabrachial nucleus.

**Do not** assume the lateral parabrachial nucleus is the
**spinoparabrachial tract** or the **central tegmental tract**. Those are
**white-matter tracts** that **carry** the afferents to the lateral
parabrachial nucleus.

**Do not** assume the lateral parabrachial nucleus is the **central
nucleus of the amygdala**, the **BNST**, the **insula**, the
**hypothalamus**, the **VPMpc thalamus**, or the **PAG**. Those are
**downstream targets** of the lateral parabrachial nucleus.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the lateral parabrachial nucleus. **The lateral
parabrachial nucleus is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT part of the fear circuit**. **Note**: the
lateral parabrachial nucleus **projects to** the central nucleus (a
fear-output structure), but the lateral parabrachial nucleus itself is
**not** a fear structure.

Iterating the lateral parabrachial nucleus's (empty) children
(recommended consumer pattern)::

    LATERAL_PARABRACHIAL_NUCLEUS_CHILDREN = ()
    # The lateral parabrachial nucleus is a leaf. The CGRP, PDYN, FoxP2,
    # and other molecular populations — and the viscerotopic subnuclei
    # (external lateral, dorsal lateral, central lateral, ventral
    # lateral, superior lateral) — are prose, not modules.

Reaching the medial parabrachial nucleus (recommended consumer pattern —
the sibling)::

    # The medial parabrachial nucleus is the RESPIRATORY AND AUTONOMIC
    # RELAY sibling under the parabrachial_area container:
    #
    #   .../parabrachial_area/medial_parabrachial_nucleus/
    #
    # The lateral parabrachial nucleus is the VISCERAL-SENSORY AND
    # PAIN/AVERSION sibling — different functional system, different
    # downstream targets.

Reaching the subparabrachial nucleus (recommended consumer pattern — the
sibling)::

    # The subparabrachial nucleus is the PONTINE RESPIRATORY CENTER
    # sibling under the parabrachial_area container:
    #
    #   .../parabrachial_area/subparabrachial_nucleus/
    #
    # The lateral parabrachial nucleus is the VISCERAL-SENSORY AND
    # PAIN/AVERSION sibling — different functional system, different
    # downstream targets.

Reaching the Kölliker-Fuse nucleus and pontine respiratory group
(recommended consumer pattern — the structural nephews)::

    # The Kölliker-Fuse nucleus and the pontine respiratory group are
    # STRUCTURAL NEPHEWS (children of the subparabrachial nucleus,
    # which is a sibling of the lateral parabrachial nucleus):
    #
    #   .../parabrachial_area/subparabrachial_nucleus/kolliker_fuse_nucleus/
    #   .../parabrachial_area/subparabrachial_nucleus/pontine_respiratory_group/
    #
    # They are NOT the lateral parabrachial nucleus — they are its
    # structural nephews.

Reaching the superior cerebellar peduncle (recommended consumer pattern —
the white-matter tract the nucleus FLANKS)::

    # The superior cerebellar peduncle (brachium conjunctivum) is the
    # WHITE-MATTER tract that the lateral parabrachial nucleus FLANKS:
    #
    #   .../white_matter/.../superior_cerebellar_peduncle/  (or equivalent path)
    #
    # The lateral parabrachial nucleus is GREY MATTER that flanks the
    # peduncle; the peduncle is WHITE MATTER that connects the cerebellum
    # to the midbrain and thalamus. They are DIFFERENT STRUCTURES — the
    # anatomical juxtaposition is the etymological origin of the name
    # "para-brachial" and is a classic source of confusion.

Reaching the locus coeruleus (recommended consumer pattern — the adjacent
noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the lateral parabrachial
    # nucleus, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the lateral parabrachial nucleus is glutamatergic/CGRP-ergic/PDYN-
    # ergic (visceral/pain/aversion relay). They are ANATOMICALLY
    # ADJACENT but FUNCTIONALLY DISTINCT.

Reaching the solitary nucleus (recommended consumer pattern — the
UPSTREAM source)::

    # The solitary nucleus (nucleus tractus solitarius) is the MEDULLARY
    # visceral-afferent hub that PROJECTS TO the lateral parabrachial
    # nucleus:
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #
    # The solitary nucleus is UPSTREAM; the lateral parabrachial nucleus
    # is DOWNSTREAM. They are DIFFERENT STRUCTURES.

Reaching the spinoparabrachial tract (recommended consumer pattern — the
white-matter pain/temperature afferent tract)::

    # The spinoparabrachial tract is the WHITE-MATTER ascending tract that
    # carries the lamina I pain and temperature afferents from the spinal
    # cord dorsal horn to the CONTRALATERAL lateral parabrachial nucleus:
    #
    #   .../white_matter/.../spinoparabrachial_tract/  (or equivalent path)
    #
    # The lateral parabrachial nucleus RECEIVES the spinoparabrachial
    # axons; the spinoparabrachial tract CARRIES them. They are DIFFERENT
    # STRUCTURES.

Reaching the central nucleus of the amygdala (recommended consumer
pattern — the DOWNSTREAM SLEA target)::

    # The central nucleus of the amygdala is a DOWNSTREAM SLEA target of
    # the lateral parabrachial nucleus (CGRP-expressing neurons →
    # capsular part of central nucleus):
    #
    #   .../cerebral_hemispheres/left/subcortical/medial_temporal_lobe/amygdala/central_nucleus/
    #
    # The lateral parabrachial nucleus PROJECTS TO the central nucleus;
    # the central nucleus is a DOWNSTREAM target — it is ALSO an SLEA
    # component. The lateral parabrachial nucleus itself is NOT an SLEA
    # component.

Reaching the BNST (recommended consumer pattern — the DOWNSTREAM SLEA
target)::

    # The bed nucleus of the stria terminalis (BNST) is a DOWNSTREAM SLEA
    # target of the lateral parabrachial nucleus (CGRP-expressing neurons
    # → BNST):
    #
    #   .../subcortical/extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/
    #
    # The lateral parabrachial nucleus PROJECTS TO the BNST; the BNST is
    # a DOWNSTREAM target — it is ALSO an SLEA component. The lateral
    # parabrachial nucleus itself is NOT an SLEA component.

Reaching the insula, hypothalamus, VPMpc thalamus, and PAG (recommended
consumer pattern — DOWNSTREAM targets)::

    # The insula, hypothalamus, VPMpc thalamus, and PAG are DOWNSTREAM
    # targets of the lateral parabrachial nucleus:
    #
    #   .../cerebral_hemispheres/left/cortex/insular/
    #   .../diencephalon/hypothalamus/
    #   .../diencephalon/thalamus/left/ventral_nuclear_group/ventral_posterior_nucleus/ventral_posterior_medial_nucleus/
    #   .../midbrain/tegmentum/periaqueductal_gray/
    #
    # The lateral parabrachial nucleus PROJECTS TO these structures;
    # they are DOWNSTREAM targets.

Bilateral iteration (recommended consumer pattern)::

    # The lateral parabrachial nucleus is a SINGLE module (not
    # bilateralized at the tree level). The module represents the
    # BILATERAL lateral parabrachial nuclei. Any lateralization is
    # contested and documented in the literature, not wired.
    lateral_pb_path = (
        "hindbrain.metencephalon.pons.parabrachial_area."
        "lateral_parabrachial_nucleus"
    )
    # resolve lateral_pb_path through the memory/recall layer

Molecular-population-level detail (not wired — consult references)::

    # The lateral parabrachial nucleus's molecular populations are prose,
    # not modules:
    #   CGRP-expressing (external lateral subnucleus) -> learned taste
    #       aversion, food intake suppression; projects to central
    #       nucleus of the amygdala (capsular part) and BNST
    #   PDYN-expressing (dorsal lateral subnucleus) -> thermal sensation,
    #       pain, descending pain modulation; projects to PAG and
    #       hypothalamus
    #   FoxP2-expressing (central lateral, ventral lateral, superior
    #       lateral subnuclei) -> visceral sensation, taste; projects to
    #       insula (via VPMpc thalamus) and hypothalamus
    #
    # Do not attempt to resolve these as sub-paths of the lateral
    # parabrachial nucleus — resolve them at the molecular-population
    # level through the references.

References
----------
*   **Canonical lateral parabrachial nucleus anatomy:** Saper, C.B.,
    Loewy, A.D. (1980). "Efferent connections of the parabrachial nucleus
    in the rat." *Brain Research* 197:291–317. (Lateral parabrachial
    nucleus efferents — the definitive early mapping.)
*   **Parabrachial area — review:** Saper, C.B. (2002). "The central
    autonomic nervous system: conscious visceral perception and autonomic
    function." *Annual Review of Neuroscience* 25:433–469. (Lateral
    parabrachial nucleus as the pontine visceral-sensory relay.)
*   **Visceral sensory relay:** Herbert, H., Moga, M.M., Saper, C.B.
    (1990). "Connections of the parabrachial nucleus with the nucleus of
    the solitary tract and the medullary reticular formation in the rat."
    *Journal of Comparative Neurology* 293:540–580. (Lateral parabrachial
    nucleus visceral afferents from the solitary nucleus.)
*   **Pain and temperature relay:** Craig, A.D. (2002). "How do you feel?
    Interoception: the sense of the physiological condition of the body."
    *Nature Reviews Neuroscience* 3:655–666. (Spinoparabrachial tract —
    lamina I pain and temperature afferents to the lateral parabrachial
    nucleus.)
*   **CGRP neurons — aversion and food intake:** Carter, M.E., Soden,
    M.E., Zweifel, L.S., Palmiter, R.D. (2013). "Genetic identification
    of a neural circuit that suppresses appetite." *Nature* 503:111–114.
    (CGRP-expressing lateral parabrachial neurons — learned taste
    aversion and food intake suppression.)
*   **PDYN neurons — pain and thermal sensation:** Barik, A., Thompson,
    J.H., Seltzer, Z. (2018). "Parabrachial prodynorphin neurons are
    required for thermal nociception." *Pain* 159:2287–2297.
    (PDYN-expressing lateral parabrachial neurons — thermal sensation and
    pain.)
*   **FoxP2 neurons — visceral sensation:** Geerling, J.C., Yokota, S.,
    Rukhadze, I., Roe, D., Chamberlin, N.L. (2014). "FoxP2 expression
    defines a novel subset of neurons in the parabrachial nucleus."
    *Journal of Comparative Neurology* 522:2292–2305. (FoxP2-expressing
    lateral parabrachial neurons — visceral sensation and taste.)
*   **Opioid withdrawal — lateral parabrachial nucleus involvement:**
    Liu, J., et al. (2020). "Lateral parabrachial neurons are a critical
    node for opioid withdrawal." *Nature Neuroscience* 23:1103–1111.
    (Lateral parabrachial nucleus — opioid withdrawal aversion.)
*   **Central post-stroke pain — lateral parabrachial nucleus
    involvement:** Klit, H., Finnerup, N.B., Jensen, T.S. (2009). "Central
    post-stroke pain: clinical characteristics, pathophysiology, and
    management." *Lancet Neurology* 8:857–868. (Central post-stroke pain
    — spinothalamic and spinoparabrachial pathway involvement.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    lateral parabrachial nucleus but functionally distinct.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract the
    nucleus FLANKS):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Superior cerebellar peduncle —
    brachium conjunctivum; the white-matter tract that the lateral
    parabrachial nucleus flanks.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that projects to the lateral parabrachial
    nucleus.)
*   **Central nucleus of the amygdala (contrast — the DOWNSTREAM SLEA
    target):** LeDoux, J.E. (2007). "The amygdala." *Current Biology*
    17:R868–R874. (Central nucleus of the amygdala — fear-output
    structure; downstream target of the lateral parabrachial nucleus.)
*   **BNST (contrast — the DOWNSTREAM SLEA target):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (BNST — SLEA component; downstream target of
    the lateral parabrachial nucleus.)
*   **Periaqueductal gray (contrast — the MIDBRAIN downstream target):**
    Behbehani, M.M. (1995). "Functional characteristics of the midbrain
    periaqueductal gray." *Progress in Neurobiology* 46:575–605.
    (Periaqueductal gray — midbrain pain-modulation center; downstream
    target of the lateral parabrachial nucleus.)
*   **SLEA (contrast — the lateral parabrachial nucleus is not
    included):** Alheid, G.F., Heimer, L. (1988). "New perspectives in
    basal forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA continuum
    — BNST, central nucleus, ventral pallidum, nucleus accumbens; NOT
    the lateral parabrachial nucleus. The lateral parabrachial nucleus
    PROJECTS TO the SLEA components, but is not part of the continuum.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the lateral parabrachial nucleus. **Note**: the lateral
    parabrachial nucleus projects to the central nucleus, but the lateral
    parabrachial nucleus itself is not a fear structure.)
*   NeuroNames — Lateral parabrachial nucleus; FMA — Lateral parabrachial
    nucleus.
"""