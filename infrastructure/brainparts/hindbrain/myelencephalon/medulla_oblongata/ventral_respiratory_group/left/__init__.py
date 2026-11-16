"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left
==================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── ventral_respiratory_group
                └── left   <-- THIS MODULE
                    ├── botzinger_complex
                    ├── nucleus_para_ambiguus
                    ├── nucleus_retroambiguus
                    ├── nucleus_retrofacialis
                    ├── pre_botzinger_complex
                    └── retrotrapezoid_nucleus

**Primary synonym:** Left ventral respiratory group; left VRG;
left ventral respiratory column; left ventral respiratory column
group; left rostrocaudal respiratory column (left side).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter container** — the **left-side** group of
**six respiratory rhythm and pattern generator nuclei** in the
**left ventrolateral medulla oblongata**, comprising the **left
Bötzinger complex**, **left nucleus para-ambiguus**, **left
nucleus retroambiguus**, **left nucleus retrofacialis**, **left
pre-Bötzinger complex**, and **left retrotrapezoid nucleus
(RTN)**. It is **NOT** a single nucleus — it is a **container**
of six functionally distinct **respiratory** nuclei — **NOT** a
somatosensory relay, **NOT** a circumventricular organ, **NOT**
a sympathetic premotor center, **NOT** a visceral afferent
relay, **NOT** a reticular nucleus, and **NOT** a
sleep-promoting region.
**Part of:** The **ventral_respiratory_group** bilateral container
(``.../medulla_oblongata/ventral_respiratory_group/``) — which is
part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**. It is a **direct child**
of the VRG container.
**Structural parent:** ``.../ventral_respiratory_group/`` →
**direct child** of the ventral_respiratory_group container. The
**left** container is one of the **two** structural children of
the container (the other is ``right``).
**Structural children:** **Six —** each a **leaf** representing
the **left** side of one of the six respiratory nuclei:
1. ``botzinger_complex`` — the **left Bötzinger complex** —
   **expiratory** rhythm / pattern generator.
2. ``nucleus_para_ambiguus`` — the **left nucleus para-ambiguus**
   — **expiratory premotor** neurons.
3. ``nucleus_retroambiguus`` — the **left nucleus retroambiguus**
   — **expiratory / abdominal** premotor neurons.
4. ``nucleus_retrofacialis`` — the **left nucleus retrofacialis**
   — **expiratory** neurons.
5. ``pre_botzinger_complex`` — the **left pre-Bötzinger complex**
   — the **primary respiratory rhythm generator** — the
   **"master clock"** of **breathing**.
6. ``retrotrapezoid_nucleus`` — the **left retrotrapezoid
   nucleus (RTN)** — the **primary central chemoreceptor** —
   **CO₂/H⁺** sensor at the **left ventral medullary surface**.
**Boundary status (NOT the right ventral respiratory group
container — the contralateral container):** **Boundary case —
the left VRG container is NOT the right VRG container.** The
**right VRG container**
(``.../ventral_respiratory_group/right/``) is the
**contralateral container** — the right-side group of six
respiratory nuclei in the **right ventrolateral medulla**. **They
are DIFFERENT CONTAINERS** — the ``left`` and ``right`` modules
are the two sides of the **bilateral parent container**.
Consumers must **not** conflate the **left** container with the
**right** — resolve the right side via
``ventral_respiratory_group.right``.
**Boundary status (NOT the parent ventral_respiratory_group
container — a SIDE of it):** **Boundary case — the left VRG
container is NOT the parent ventral_respiratory_group container.**
The **parent** (``.../ventral_respiratory_group/``) is the
**unpaired bilateral container** — it contains **both** the
``left`` and ``right`` sides. The **left** container (here) is
**one side** of that parent. Consumers must **not** conflate the
**left container** with the **parent container** — the parent
contains **both sides**; the left container contains **only the
left side**.
**Boundary status (NOT a single nucleus — a CONTAINER of six
nuclei):** **Boundary case — the left VRG container is a
CONTAINER, not a single nucleus.** It contains **six distinct
leaf nuclei** — the **left Bötzinger complex**, **left nucleus
para-ambiguus**, **left nucleus retroambiguus**, **left nucleus
retrofacialis**, **left pre-Bötzinger complex**, and **left
retrotrapezoid nucleus**. Each is a **separate structure** with
**different functions** (expiratory rhythm, expiratory premotor,
inspiratory rhythm, central chemoreception). Consumers must
**not** treat the **left** container as a single uniform nucleus
— it is a **container** of **six functionally distinct
nuclei**.
**Boundary status (NOT the left dorsal respiratory group (DRG) —
a DIFFERENT structure in a DIFFERENT container):** **Boundary
case — the left VRG container is NOT the left DRG.** The **left
DRG** (``.../respiratory_center/dorsal_respiratory_group/left/``)
is the **left dorsal respiratory** group in the **left NTS
region** — it **relays pulmonary stretch receptor input** to the
respiratory rhythm generator. The **left VRG container** (here)
is the **left ventrolateral** respiratory group — it
**generates** the **respiratory rhythm** (left pre-Bötzinger
complex) and **shapes** the **respiratory pattern**. **They are
DIFFERENT STRUCTURES at DIFFERENT dorsoventral positions** —
the **left DRG** is **dorsal** (in the **left NTS region**); the
**left VRG** is **ventrolateral**. They are **functionally
coupled** — the left DRG **projects to** the left VRG to
**modulate** the **respiratory rhythm** — but they are
**anatomically distinct**. Consumers must **not** conflate the
two. This is the **most consequential** left VRG boundary — the
**dorsal vs. ventrolateral** distinction is the **primary
axis** of the **medullary respiratory network**.
**Boundary status (NOT the left RVLM — the RVLM is the
SYMPATHETIC PREMOTOR center):** **Boundary case — the left VRG
container is NOT the left RVLM.** The **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
sympathetic premotor / vasomotor** center — the **efferent
limb** of the **left medullary baroreflex arc**. The **left VRG
container** (here) is the **left respiratory rhythm and pattern
generator group**. **They are DIFFERENT STRUCTURES** — both are
**ventrolateral**, but they are **functionally distinct** — the
**left RVLM** is **autonomic (sympathetic premotor)**; the
**left VRG** is **respiratory**. They are **anatomically
overlapping** in the **left rostral ventrolateral medulla** —
the **left pre-Bötzinger complex** is **adjacent** to the **left
RVLM** — but they are **distinct functional systems** wired
under **different containers**. Consumers must **not** conflate
the two.
**Boundary status (NOT the left solitary nucleus (NTS) — the NTS
is the VISCERAL AFFERENT relay):** **Boundary case — the left
VRG container is NOT the left NTS.** The **left NTS**
(``.../solitary_nucleus/left/``) is the **left visceral afferent
relay** — it **receives** taste, baroreceptor, chemoreceptor,
and gastrointestinal afferents. The **left VRG container**
(here) is the **left respiratory rhythm and pattern generator
group**. **They are DIFFERENT STRUCTURES** — the **left NTS**
is the **afferent** relay; the **left VRG** is the
**respiratory** generator. They are **functionally coupled** —
the left NTS **projects to** the left VRG to **modulate** the
**respiratory rhythm** in response to **visceral** signals —
but they are **anatomically distinct**. Consumers must **not**
conflate the two.
**Boundary status (NOT the left parafacial zone (PZ) — the PZ is
a SLEEP-PROMOTING region, and is NOT the parafacial respiratory
group (pFRG)):** **Boundary case — the left VRG container is
NOT the left parafacial zone (PZ).** The **left parafacial
zone** (``.../parafacial_zone/left/``) is a **left GABAergic /
glycinergic sleep-promoting** region — **NOT** a respiratory
rhythm generator. **The "parafacial zone" (PZ) is a DIFFERENT
structure from the "parafacial respiratory group" (pFRG)** —
the **pFRG** is a **respiratory** structure (pre-inspiratory
and expiratory-modulating neurons) that is **often grouped with
the retrotrapezoid nucleus (RTN)** as the **RTN/pFRG complex**.
**In this tree, the left pFRG is NOT wired as a separate
module** — it is documented as part of the **left retrotrapezoid
nucleus** prose (see
``.../ventral_respiratory_group/left/retrotrapezoid_nucleus/``).
**The left parafacial zone (PZ) is a DIFFERENT structure** — it
is **wired separately** under ``.../parafacial_zone/left/`` as a
**sleep-promoting** region. **Consumers must not conflate the
left parafacial zone (PZ, sleep-promoting) with the left
parafacial respiratory group (pFRG, respiratory) — they share
the name "parafacial" but are DIFFERENT STRUCTURES.** The **left
PZ** is **sleep-promoting**; the **left pFRG** is **respiratory**
(and wired as part of the **left RTN complex** in this tree).
**The left VRG container** (this module) is **distinct from
both**.
**Boundary status (NOT the left Gi or left paramedian reticular
nucleus — reticular nuclei in DIFFERENT containers):** **Boundary
case — the left VRG container is NOT the left gigantocellular
reticular nucleus (Gi) or the left paramedian reticular nucleus.**
Those are **left reticular** nuclei with **broader** functions —
the **left Gi**
(``.../respiratory_center/gigantocellular_reticular_nucleus/left/``)
is **respiratory**, **autonomic**, and **pain-modulatory**;
the **left paramedian reticular nucleus**
(``.../paramedian_reticular_nucleus/left/``) is a **left
cerebellar projection** nucleus with **nociceptive** and
**autonomic** roles. The **left VRG container** (here) is a
**group of specific respiratory rhythm and pattern generator
nuclei** — it is **NOT** a **reticular** nucleus. Consumers must
**not** conflate the left VRG with either left reticular nucleus.
**Boundary status (NOT the other left respiratory_center children
— DIFFERENT structures):** **Boundary case — the left VRG
container is NOT the other left respiratory_center children** —
the **left DRG**, **left Gi**, **left cuneate nucleus**, **left
gracile nucleus**, **left area postrema**, and **left
chemoreceptor trigger zone**. Each is a **different structure** —
see the respective modules. Consumers must **not** conflate the
left VRG with any of these.
**Boundary status (NOT the whole medulla oblongata — a
respiratory generator container within it):** **Boundary case —
the left VRG container is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the left VRG container (via
the VRG container) **plus** the RVLM, CVLM, NTS,
respiratory_center, cranial nerve nuclei, olivary body,
medullary pyramid, arcuate nucleus, parafacial zone, paramedian
reticular nucleus, perihypoglossal nuclei, and other structures.
The **left VRG container** is **one left respiratory generator
container** within the medulla. Consumers must **not** conflate
the **left VRG** with the **whole medulla**.

Overview
--------
The **left ventral respiratory group (left VRG) container** is
the **left-side** group of **six respiratory rhythm and pattern
generator nuclei** in the **left ventrolateral medulla
oblongata**. It is the **left-side** of the **ventral
respiratory group**, and it is a **container** (not a leaf)
with **six leaf children** (the six respiratory nuclei).

**The left VRG container is a CONTAINER of six nuclei, NOT a
single nucleus.** The six **left** nuclei are:

*   **Left pre-Bötzinger complex** — the **left primary
    respiratory rhythm generator** — the **"master clock"** of
    the **left side** of breathing.
*   **Left Bötzinger complex** — the **left expiratory** rhythm
    / pattern generator.
*   **Left nucleus para-ambiguus** — **left expiratory premotor**
    neurons.
*   **Left nucleus retroambiguus** — **left expiratory /
    abdominal** premotor neurons.
*   **Left nucleus retrofacialis** — **left expiratory**
    neurons.
*   **Left retrotrapezoid nucleus (RTN)** — the **left primary
    central chemoreceptor** — **CO₂/H⁺** sensor at the **left
    ventral medullary surface**.

**The left VRG container is RESPIRATORY — its name is
FUNCTIONALLY ACCURATE.** Unlike the **respiratory_center** (a
**heterogeneous tree-wiring cluster** containing somatosensory
and circumventricular structures alongside true respiratory
ones), the **left VRG** is **genuinely** a **respiratory**
group — **all six subnuclei** are **respiratory-related**
structures.

**The left VRG container is the VENTROLATERAL respiratory group
— the left DRG is the DORSAL respiratory group.** The **left
VRG** is in the **left ventrolateral medulla**; the **left DRG**
is in the **left dorsal medulla** (in the **left NTS region**).
The **left VRG** **generates** the **respiratory rhythm**
(primarily the **left pre-Bötzinger complex**) and **shapes** the
**respiratory pattern**; the **left DRG** **relays pulmonary
stretch receptor input** to the **left VRG**.

**The left VRG container is one side of the bilateral parent
container.** The **parent** (``.../ventral_respiratory_group/``)
contains **both** the ``left`` and ``right`` sides; the **left**
container (here) contains **only the left side**.

**The left VRG container is TRULY BILATERAL — the left / right
split is ANATOMICAL.** Unlike the **area postrema** (a
**midline** organ wired as left/right by convention), the
**left** and **right** VRG subnuclei are **anatomically
separate structures** — the **left pre-Bötzinger complex** is
in the **left ventrolateral medulla**; the **right
pre-Bötzinger complex** is in the **right ventrolateral
medulla**.

Structural Children (Six Leaves)
--------------------------------
The left VRG container has **six structural children**, each a
**leaf**:

*   ``botzinger_complex`` — **left Bötzinger complex** —
    **expiratory** rhythm / pattern generator.
*   ``nucleus_para_ambiguus`` — **left nucleus para-ambiguus** —
    **expiratory premotor** neurons.
*   ``nucleus_retroambiguus`` — **left nucleus retroambiguus** —
    **expiratory / abdominal** premotor neurons.
*   ``nucleus_retrofacialis`` — **left nucleus retrofacialis** —
    **expiratory** neurons.
*   ``pre_botzinger_complex`` — **left pre-Bötzinger complex** —
    the **primary respiratory rhythm generator**.
*   ``retrotrapezoid_nucleus`` — **left retrotrapezoid nucleus
    (RTN)** — the **primary central chemoreceptor** (and the
    **left RTN/pFRG complex**).

**Each child is a leaf.** The six nucleus modules are **single
structures** — they have **no structural children** of their
own. Consumers that need **nucleus-level** resolution descend
into one of the six leaves; consumers that need **side-level**
resolution use this container as a whole; consumers that need
**bilateral** resolution iterate over both ``left`` and
``right``.

The Left VRG / Right VRG Boundary
---------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left VRG container** (this module) — the left-side group of
    six respiratory nuclei in the **left ventrolateral medulla**.

*   **Right VRG container**
    (``.../ventral_respiratory_group/right/``) — the right-side
    group of six respiratory nuclei in the **right
    ventrolateral medulla**.

**They are the SIDES of the bilateral
ventral_respiratory_group container.** They are **structurally
symmetric mirror containers** — same six leaf nuclei, same
cytoarchitecture, same projections (with some crossed
components), same functions. Consumers must **not** conflate the
left container with the right — resolve the right side via
``ventral_respiratory_group.right``.

The Left VRG / Left Dorsal Respiratory Group (DRG) Boundary
-----------------------------------------------------------
This is the **most consequential** dorsoventral respiratory
boundary:

*   **Left VRG container** (this module) — the **left
    ventrolateral** respiratory rhythm and pattern generator
    group.

*   **Left DRG**
    (``.../respiratory_center/dorsal_respiratory_group/left/``) —
    the **left dorsal** respiratory group in the **left NTS
    region**.

**They are DIFFERENT STRUCTURES at DIFFERENT dorsoventral
positions** — the **left DRG** is **dorsal** (in the **left NTS
region**); the **left VRG** is **ventrolateral**. They are
**functionally coupled** — the left DRG **projects to** the left
VRG to **modulate** the **respiratory rhythm** — but they are
**anatomically distinct**. Consumers must **not** conflate the
two.

The Left VRG / Left RVLM Boundary
---------------------------------
This is the **respiratory / autonomic** boundary:

*   **Left VRG container** (this module) — the **left respiratory
    rhythm and pattern generator group**.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``) —
    the **left sympathetic premotor / vasomotor** center.

**They are DIFFERENT STRUCTURES** — both are **ventrolateral**,
but they are **functionally distinct** — the **left RVLM** is
**autonomic (sympathetic premotor)**; the **left VRG** is
**respiratory**. They are **anatomically overlapping** in the
**left rostral ventrolateral medulla** — the **left
pre-Bötzinger complex** is **adjacent** to the **left RVLM** —
but they are **distinct functional systems** wired under
**different containers**. Consumers must **not** conflate the
two.

The Left VRG / Left Solitary Nucleus (NTS) Boundary
---------------------------------------------------
This is the **respiratory / visceral afferent** boundary:

*   **Left VRG container** (this module) — the **left respiratory
    rhythm and pattern generator group**.

*   **Left NTS** (``.../solitary_nucleus/left/``) — the **left
    visceral afferent relay**.

**They are DIFFERENT STRUCTURES** — the **left NTS** is the
**afferent** relay; the **left VRG** is the **respiratory**
generator. They are **functionally coupled** — the left NTS
**projects to** the left VRG to **modulate** the **respiratory
rhythm** — but they are **anatomically distinct**. Consumers
must **not** conflate the two.

The Left VRG / Left Parafacial Zone (PZ) Boundary
-------------------------------------------------
This is the **respiratory / sleep-promoting** boundary, with the
**PZ vs. pFRG** name-collision caveat:

*   **Left VRG container** (this module) — the **left respiratory
    rhythm and pattern generator group** — **contains the left
    RTN**, which is the **left pFRG's** **home region** in this
    tree.

*   **Left parafacial zone (PZ)** (``.../parafacial_zone/left/``)
    — the **left sleep-promoting** region — **NOT** the **left
    parafacial respiratory group (pFRG)**.

**They are DIFFERENT STRUCTURES** — the **left PZ** is
**sleep-promoting**; the **left VRG** is **respiratory**. **The
left PZ is NOT the left pFRG** — they share the name
"parafacial" but are **different structures**. **The left pFRG
is a respiratory structure** — **not wired as a separate
module** in this tree, but **documented** as part of the **left
RTN/pFRG complex** under
``.../ventral_respiratory_group/left/retrotrapezoid_nucleus/``.
Consumers must **not** conflate the left VRG with the left
parafacial zone (PZ), **and must not** conflate the left
parafacial zone (PZ) with the left parafacial respiratory group
(pFRG).

The Left VRG / Left Gi and Left Paramedian Reticular Nucleus Boundary
---------------------------------------------------------------------
This is the **respiratory generator / reticular** boundary:

*   **Left VRG container** (this module) — the **left respiratory
    rhythm and pattern generator group**.

*   **Left Gi**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/left/``)
    — the **left large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

*   **Left paramedian reticular nucleus**
    (``.../paramedian_reticular_nucleus/left/``) — the **left
    smaller**, **more medial** reticular nucleus.

**They are DIFFERENT STRUCTURES** — the **left Gi** and **left
paramedian reticular nucleus** are **reticular** nuclei with
**broader** functions; the **left VRG** is a **group of specific
respiratory rhythm and pattern generator nuclei**. Consumers must
**not** conflate the left VRG with either left reticular nucleus.

The Left VRG / Other Left Respiratory Center Children Boundary
-------------------------------------------------------------
This is the **respiratory generator / other-respiratory-center**
boundary:

*   **Left VRG container** (this module) — the **left
    ventrolateral** respiratory generator group.

*   **Left DRG, left Gi, left cuneate nucleus, left gracile
    nucleus, left area postrema, left chemoreceptor trigger
    zone** — the **other left children** of
    ``respiratory_center``.

**Each is a DIFFERENT STRUCTURE** — the **left DRG** is
**dorsal respiratory**; the **left Gi** is **reticular**; the
**left cuneate** and **left gracile nuclei** are
**somatosensory**; the **left area postrema** and **left
chemoreceptor trigger zone** are **circumventricular**.
Consumers must **not** conflate the left VRG with any of these.

The Left VRG / Whole VRG Container, Whole Medulla Oblongata Boundary
-------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Left VRG container** (this module) — one **child** of the
    ``ventral_respiratory_group`` container.

*   **Ventral respiratory group**
    (``.../ventral_respiratory_group/``) — the **bilateral
    container** of the left + right VRG.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the VRG container and other
    medullary structures.

**The left VRG container is a CONTAINER in a CHAIN of
containers.** Consumers must **not** conflate the **container**
with any of the **parent containers**.

Function in the Human Brain
---------------------------
The left VRG container's function is **left respiratory rhythm
generation** and **left respiratory pattern generation** —
**NOT autonomic regulation** and **NOT visceral afferent relay**:

*   **Left respiratory rhythm generation (left pre-Bötzinger
    complex):** The **left pre-Bötzinger complex** is the **left
    primary respiratory rhythm generator** — it **generates**
    the **left inspiratory rhythm**.

*   **Left expiratory pattern generation (left Bötzinger
    complex, left nucleus para-ambiguus, left nucleus
    retroambiguus, left nucleus retrofacialis):** These four
    nuclei **shape** the **left expiratory pattern** — the
    **left active expiration** (via **left abdominal** muscles,
    **left internal intercostals**) and the **left premotor**
    control of **left expiratory** muscles.

*   **Left central chemoreception (left RTN / pFRG):** The **left
    RTN** — the **left retrotrapezoid nucleus** — is the **left
    primary central chemoreceptor** — it **senses** **CO₂/H⁺** at
    the **left ventral medullary surface** and **drives** **left
    inspiration** in response to **hypercapnia**.

*   **Integration with higher centers:** The **left VRG**
    **receives** descending input from the **pons (pneumotaxic
    center)**, the **cortex**, the **hypothalamus**, and the
    **limbic** system — and it **integrates** these with
    **chemosensory** (left RTN) and **visceral** (left NTS)
    input to **produce** the **left respiratory pattern**
    adapted to **behavioral** and **metabolic** demands.

*   **NOT autonomic regulation:** The **autonomic regulation** is
    the **left RVLM**, **left CVLM**, and **left NTS** — **NOT**
    the left VRG.

*   **NOT visceral afferent relay:** The **visceral afferent
    relay** is the **left NTS** — **NOT** the left VRG.

**The unifying theme:** the left VRG container is the
**left-side** **respiratory rhythm and pattern generator group**
of the **left ventrolateral medulla** — it **generates** the
**left respiratory rhythm** (left pre-Bötzinger complex),
**shapes** the **left respiratory pattern** (left Bötzinger,
left nucleus para-ambiguus, left nucleus retroambiguus, left
nucleus retrofacialis), and **senses** **CO₂/H⁺** (left RTN) —
**NOT** an autonomic center, **NOT** a visceral afferent relay,
and **NOT** a reticular nucleus.

Associated Disorders
--------------------
The left VRG container is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**, via
**left respiratory rhythm** and **pattern** dysfunction (though
the **whole-body** phenotypes — CCHS, central sleep apnea, etc.
— are typically **bilateral** because the VRGs work together):

*   **Congenital central hypoventilation syndrome (CCHS — via
    left pre-Bötzinger complex and left RTN dysfunction):**
    **CCHS** — the **"Ondine's curse"** — is a **genetic
    disorder** (typically **PHOX2B** mutations) causing **failure
    of automatic breathing** during **sleep**. The **left
    pre-Bötzinger complex** and **left RTN** contribute — their
    dysfunction impairs **left central respiratory rhythm
    generation** and **left central chemoreception** — **the
    right side and higher centers** can partially compensate.

*   **Central sleep apnea (via left pre-Bötzinger complex and
    left RTN dysfunction):** **Central sleep apnea** — **cessation**
    of **breathing** during **sleep** — is a **disorder** of
    the **central respiratory rhythm generator** and the
    **central chemoreceptors** (left pre-Bötzinger complex and
    left RTN).

*   **Rett syndrome (via left pre-Bötzinger complex and left RTN
    dysfunction):** **Rett syndrome** — an **X-linked**
    neurodevelopmental disorder — **frequently** involves
    **respiratory dysrhythmias** via **dysfunction** of the
    **left pre-Bötzinger complex** and **left RTN/pFRG**.

*   **Sudden infant death syndrome (SIDS — via left pre-Bötzinger
    complex and left RTN involvement):** **SIDS** has been
    **associated** with **abnormalities** in the **medullary
    respiratory network** — including the **left pre-Bötzinger
    complex** and **left RTN**.

*   **Opioid-induced respiratory depression (via left
    pre-Bötzinger complex μ-opioid receptor activation):**
    **Opioids** **suppress** the **left pre-Bötzinger complex** —
    **reducing** the **respiratory rate** and **causing**
    **central apnea** in **overdose**.

*   **Brainstem stroke (via left VRG involvement):** **Left
    medullary stroke** can **involve** the **left VRG** —
    contributing to **left respiratory pattern** abnormalities,
    **central apnea**, and **sleep-disordered breathing**.

*   **No Named "Left VRG Syndrome":** The left VRG container is
    a **left respiratory generator group** — its clinical
    syndromes are **named for the broader clinical entity**
    (CCHS, central sleep apnea, Rett syndrome, SIDS) or the
    **broader lesion** (brainstem stroke) — **NOT** for the left
    VRG itself.

**What is NOT here:** The left VRG container is **not** the
substrate for **sympathetic premotor** function (left RVLM),
**sympathoinhibition** (left CVLM), **visceral afferent relay**
(left NTS), **emesis** (left area postrema / left CTZ),
**somatosensory loss** (left cuneate / left gracile nuclei),
**tongue weakness** (left hypoglossal nucleus), or **sleep
promotion** (left parafacial zone). Its clinical relevance is
the **left respiratory rhythm** and **pattern** functions
listed above.

Lateralization Notes
--------------------
This is the **left** VRG container. The ventral respiratory group
is a **bilateral container** whose two sides are **ANATOMICALLY
SEPARATE** — **not** a wiring convention for a midline organ
(unlike the area postrema / CTZ) — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right** VRG
    containers are **structurally symmetric** — they are **mirror
    pairs** with the **same** six leaf nuclei, **same**
    cytoarchitecture, **same** projections (with some crossed
    components), and **same** functions. The **left** VRG
    container holds the **six left-side** respiratory nuclei;
    the **right** VRG container holds the **six right-side**
    respiratory nuclei.

*   **Partly Crossed Projections:** Some **VRG** projections are
    **ipsilateral** (to the **ipsilateral** phrenic / intercostal
    motor neurons via the **ipsilateral** bulbospinal pathway)
    and some are **crossed**. The **VRG** functions
    **bilaterally** in **respiratory rhythm generation** and
    **pattern generation** — the **left and right VRG**
    together ensure that **breathing** is **synchronized** across
    both sides of the **diaphragm** and **chest wall**.

*   **NO Lateralization Warning:** The VRG has **no known
    functional lateralization** in humans — the **left** and
    **right** subnuclei are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the left VRG — the **left**
    and **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left VRG
    container is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left VRG container.

*   **NO Fear-Output Warning:** The left VRG container is **not**
    a fear-output structure — it is a **left respiratory rhythm
    and pattern generator group**. Consumers must **not**
    conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "left VRG = right VRG" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The VRG is
a **strict-mirror container with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left VRG container is a
    **container** — it does **not** import from ``.../right/``
    or any other right-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../respiratory_center/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../solitary_nucleus/``,
    ``.../parafacial_zone/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../cranial_nerve_nuclei/``, or any other container. The
    left VRG container's relationships to the left DRG, left
    RVLM, left CVLM, left NTS, left parafacial zone, left Gi,
    left paramedian reticular nucleus, and other left medullary
    structures are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with six leaf children.** The structural
    children are the six **respiratory nuclei** — each a
    **leaf**. Consumers **should** descend into them for
    **nucleus-level** resolution.
*   **NOT the right VRG container.** The right VRG container is a
    **separate module** under
    ``.../ventral_respiratory_group/right/``. Consumers must
    **not** conflate the left container with the right.
*   **NOT the parent ventral_respiratory_group container.** The
    parent is the **unpaired bilateral container**; the **left**
    module is **one side** of it.
*   **RESPIRATORY, NOT a tree-wiring artifact.** The left VRG is
    **genuinely respiratory** — all six subnuclei are
    respiratory-related structures.
*   **NOT the left DRG.** The **left DRG** is the **left dorsal
    respiratory** group in the **left NTS region** — a
    **different** structure. This is the **most consequential**
    left VRG boundary.
*   **NOT the left RVLM.** The **left RVLM** is the **left
    sympathetic premotor** center — **autonomic**, not
    **respiratory**.
*   **NOT the left NTS.** The **left NTS** is the **left visceral
    afferent** relay — not the **respiratory** generator.
*   **NOT the left parafacial zone (PZ).** The **left PZ** is a
    **sleep-promoting** region — **NOT** the **left parafacial
    respiratory group (pFRG)**. **The PZ and pFRG share the
    name "parafacial" but are DIFFERENT STRUCTURES.**
*   **NOT the left Gi or the left paramedian reticular nucleus.**
    Those are **reticular** nuclei with **broader** functions.
*   **NOT the other left respiratory_center children.** The **left
    DRG, left Gi, left cuneate nucleus, left gracile nucleus,
    left area postrema, and left chemoreceptor trigger zone**
    are **different structures**.
*   **NOT the whole VRG container or whole medulla oblongata.**
    The left VRG container is a **container** in a **chain** of
    containers.
*   **No ``AREA_PATHS`` hop.** The left VRG container is a
    **local container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left VRG container has no
    nested dual-framing module. It is a **container** with **six
    leaf children**.
*   **Structural parity with the right VRG container — strict
    mirror with NO warning.** The left and right containers are
    **structurally identical** — same six leaf children, same
    **respiratory** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "ventral_respiratory_group.left"
    )

**Do not** expect the six nuclei to be wired directly under
``ventral_respiratory_group``. The **left** and **right**
containers are **intermediate** — the six nuclei are leaf
children of those containers. Resolve them via
``ventral_respiratory_group.left.<nucleus>``.

**Do not** assume the left VRG container is the **right VRG
container**. The right VRG container is the **separate module**
at ``.../ventral_respiratory_group/right/``.

**Do not** assume the left VRG container is the **left DRG**.
The left DRG is the **left dorsal respiratory** group in the
**left NTS region** — a **different** structure. This is the
**most consequential** left VRG boundary.

**Do not** assume the left VRG container is the **left RVLM**.
The left RVLM is the **left sympathetic premotor** center —
**autonomic**, not **respiratory**.

**Do not** assume the left VRG container is the **left NTS**.
The left NTS is the **left visceral afferent** relay — not the
**respiratory** generator.

**Do not** assume the left VRG container is the **left
parafacial zone (PZ)**. The left PZ is a **sleep-promoting**
region — **NOT** the **left parafacial respiratory group
(pFRG)**. **The PZ and pFRG share the name "parafacial" but are
DIFFERENT STRUCTURES.**

**Do not** assume the left VRG container is the **left Gi** or
the **left paramedian reticular nucleus**. Those are
**reticular** nuclei with **broader** functions.

**Do not** assume the left VRG container is the **left DRG, left
Gi, left cuneate nucleus, left gracile nucleus, left area
postrema, or left chemoreceptor trigger zone**. Each is a
**different structure** — see the respective modules.

**Do not** assume the left VRG container has **structural
children beyond the six respiratory nuclei**. It is a
**container** with **six leaf children** — no further
sub-containers.

Iterating the left VRG container's structural children
(recommended consumer pattern)::

    LEFT_VENTRAL_RESPIRATORY_GROUP_CHILDREN = (
        "botzinger_complex",
        "nucleus_para_ambiguus",
        "nucleus_retroambiguus",
        "nucleus_retrofacialis",
        "pre_botzinger_complex",
        "retrotrapezoid_nucleus",
    )
    # Each child is a leaf module representing the LEFT side of
    # one of the six respiratory nuclei.

Reaching the six left nuclei (recommended consumer pattern)::

    # The six left nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.botzinger_complex
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.nucleus_para_ambiguus
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.nucleus_retroambiguus
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.nucleus_retrofacialis
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.pre_botzinger_complex
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.retrotrapezoid_nucleus
    #
    # Each is a leaf module representing the LEFT side of that
    # nucleus.

Reaching the right VRG container (recommended consumer pattern —
the contralateral container)::

    # The right VRG container is the CONTRALATERAL container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right
    #
    # The left and right VRG containers are structurally symmetric
    # mirror pairs with the same six leaf nuclei.

Reaching the left DRG (recommended consumer pattern — NOTE the
DIFFERENT container, most consequential left VRG boundary)::

    # The left dorsal respiratory group is a CHILD of
    # respiratory_center — NOT wired under
    # ventral_respiratory_group:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.left
    #
    # The left VRG (ventral respiratory group) and the left DRG
    # (dorsal respiratory group) are DIFFERENT STRUCTURES at
    # DIFFERENT dorsoventral positions.

Reaching the left RVLM (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The left rostral ventrolateral medulla is a SEPARATE
    # container under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #
    # The left VRG is RESPIRATORY; the left RVLM is SYMPATHETIC
    # PREMOTOR.

Reaching the left NTS (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The left solitary nucleus is a SEPARATE container under
    # medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #
    # The left NTS is the VISCERAL AFFERENT relay — it PROJECTS to
    # the left VRG to modulate respiratory pattern.

Reaching the left parafacial zone (recommended consumer pattern
— NOTE the DIFFERENT container AND the pFRG caveat)::

    # The left parafacial zone (PZ) is a SLEEP-PROMOTING region —
    # a SEPARATE container under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone.left
    #
    # The left PZ is NOT the left parafacial respiratory group
    # (pFRG). The left pFRG is a RESPIRATORY structure —
    # documented as part of the left RTN/pFRG complex under
    # ventral_respiratory_group.left.retrotrapezoid_nucleus.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides and all six nuclei)::

    for side in ("left", "right"):
        for nucleus in LEFT_VENTRAL_RESPIRATORY_GROUP_CHILDREN:
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"ventral_respiratory_group.{side}.{nucleus}"
            )
            # resolve path through the memory/recall layer

References
----------
*   **Canonical VRG anatomy:** Feldman, J.L., Del Negro, C.A.
    (2006). "Looking for inspiration: new perspectives on
    respiratory rhythm." *Nature Reviews Neuroscience* 7:232–242.
    (Ventral respiratory group; pre-Bötzinger complex; respiratory
    rhythm and pattern generation.)
*   **Pre-Bötzinger complex — primary rhythm generator:** Smith,
    J.C., et al. (1991). "Pre-Bötzinger complex: a brainstem
    region that may generate respiratory rhythm in mammals."
    *Science* 254:726–729. (Pre-Bötzinger complex as the primary
    respiratory rhythm generator.)
*   **VRG — respiratory pattern generation:** Bianchi, A.L., et
    al. (1995). "Central control of breathing in mammals:
    neuronal circuitry, membrane properties, and
    neurotransmitters." *Physiological Reviews* 75:1–45.
    (Ventral respiratory group; respiratory pattern generation.)
*   **Bötzinger complex — expiratory:** Smith, J.C., et al.
    (2007). "Spatial and functional architecture of the mammalian
    brainstem respiratory network." *Trends in Neurosciences*
    30:463–471. (Bötzinger complex; expiratory pattern
    generation.)
*   **RTN — central chemoreception:** Guyenet, P.G., Stornetta,
    R.L., Bayliss, D.A. (2008). "Central respiratory
    chemoreception: the retrotrapezoid nucleus." *Trends in
    Neurosciences* 31:565–573. (RTN; central chemoreception;
    CO₂/H⁺ sensing.)
*   **RTN/pFRG complex:** Guyenet, P.G., et al. (2010). "The
    retrotrapezoid nucleus, central chemoreception and arterial
    pressure regulation." *Journal of Physiology* 588:47–58.
    (RTN/pFRG complex; central chemoreception; active
    expiration.)
*   **pFRG — active expiration:** Janczewski, W.A., Feldman,
    J.L. (2006). "Distinct rhythm generators for inspiration and
    expiration in the neonatal rat." *Journal of Physiology*
    570:407–420. (Parafacial respiratory group; pre-inspiratory
    neurons; active expiration — part of the RTN/pFRG complex.)
*   **Parafacial zone (contrast — sleep-promoting):** Anaclet,
    C., et al. (2012). "The GABAergic parafacial zone is a
    medullary slow wave sleep-promoting center." *Nature
    Neuroscience* 15:747–753. (Parafacial zone — sleep-promoting
    — DIFFERENT from the parafacial respiratory group.)
*   **CCHS — pre-Bötzinger complex and RTN:** Weese-Mayer, D.E.,
    et al. (2010). "An official ATS clinical policy statement:
    congenital central hypoventilation syndrome." *American
    Journal of Respiratory and Critical Care Medicine*
    181:626–644. (CCHS; pre-Bötzinger complex and RTN dysfunction;
    PHOX2B mutations.)
*   **Rett syndrome — respiratory dysrhythmia:** Katz, D.M., et
    al. (2009). "Breathing disorders in Rett syndrome."
    *Respiratory Physiology & Neurobiology* 168:139–145. (Rett
    syndrome; pre-Bötzinger complex and RTN dysfunction;
    respiratory dysrhythmias.)
*   **SIDS — medullary respiratory network:** Kinney, H.C., et al.
    (2003). "Sudden infant death syndrome and the medullary
    serotonergic system." *JAMA* 290:1599–1609. (SIDS; medullary
    respiratory network abnormalities; pre-Bötzinger complex and
    RTN involvement.)
*   **Opioid-induced respiratory depression — pre-Bötzinger
    complex:** Montandon, G., et al. (2016). "PreBötzinger
    complex neurokinin-1 receptor-expressing neurons mediate
    opioid-induced respiratory depression." *Nature Neuroscience*
    19:129–137. (Pre-Bötzinger complex; μ-opioid receptor
    activation; opioid-induced respiratory depression.)
*   **Dorsal respiratory group (contrast — dorsal):** Kubin, L.,
    Davies, R.O. (1988). "Central coordination of respiratory
    and sympathetic activities." *Annual Review of Physiology*
    50:63–74. (Dorsal respiratory group — different from the VRG.)
*   **RVLM (contrast — sympathetic premotor):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure." *Nature
    Reviews Neuroscience* 7:335–346. (RVLM — sympathetic premotor
    — different from the VRG.)
*   **NTS (contrast — visceral afferent):** Andresen, M.C.,
    Kunze, D.L. (1994). "Nucleus tractus solitarius — gateway
    to neural circulatory control." *Annual Review of
    Physiology* 56:93–116. (NTS — visceral afferent relay —
    different from the VRG.)
*   NeuroNames — Ventral respiratory group; FMA — Ventral
    respiratory group.
"""