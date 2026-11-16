"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right
===================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── ventral_respiratory_group
                └── right   <-- THIS MODULE
                    ├── botzinger_complex
                    ├── nucleus_para_ambiguus
                    ├── nucleus_retroambiguus
                    ├── nucleus_retrofacialis
                    ├── pre_botzinger_complex
                    └── retrotrapezoid_nucleus

**Primary synonym:** Right ventral respiratory group; right VRG;
right ventral respiratory column; right ventral respiratory column
group; right rostrocaudal respiratory column (right side).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter container** — the **right-side** group of
**six respiratory rhythm and pattern generator nuclei** in the
**right ventrolateral medulla oblongata**, comprising the **right
Bötzinger complex**, **right nucleus para-ambiguus**, **right
nucleus retroambiguus**, **right nucleus retrofacialis**, **right
pre-Bötzinger complex**, and **right retrotrapezoid nucleus
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
**right** container is one of the **two** structural children of
the container (the other is ``left``).
**Structural children:** **Six —** each a **leaf** representing
the **right** side of one of the six respiratory nuclei:
1. ``botzinger_complex`` — the **right Bötzinger complex** —
   **expiratory** rhythm / pattern generator.
2. ``nucleus_para_ambiguus`` — the **right nucleus para-ambiguus**
   — **expiratory premotor** neurons.
3. ``nucleus_retroambiguus`` — the **right nucleus retroambiguus**
   — **expiratory / abdominal** premotor neurons.
4. ``nucleus_retrofacialis`` — the **right nucleus retrofacialis**
   — **expiratory** neurons.
5. ``pre_botzinger_complex`` — the **right pre-Bötzinger complex**
   — the **primary respiratory rhythm generator** — the
   **"master clock"** of **breathing**.
6. ``retrotrapezoid_nucleus`` — the **right retrotrapezoid
   nucleus (RTN)** — the **primary central chemoreceptor** —
   **CO₂/H⁺** sensor at the **right ventral medullary surface**.
**Boundary status (NOT the left ventral respiratory group
container — the contralateral container):** **Boundary case —
the right VRG container is NOT the left VRG container.** The
**left VRG container**
(``.../ventral_respiratory_group/left/``) is the
**contralateral container** — the left-side group of six
respiratory nuclei in the **left ventrolateral medulla**. **They
are DIFFERENT CONTAINERS** — the ``right`` and ``left`` modules
are the two sides of the **bilateral parent container**.
Consumers must **not** conflate the **right** container with the
**left** — resolve the left side via
``ventral_respiratory_group.left``.
**Boundary status (NOT the parent ventral_respiratory_group
container — a SIDE of it):** **Boundary case — the right VRG
container is NOT the parent ventral_respiratory_group container.**
The **parent** (``.../ventral_respiratory_group/``) is the
**unpaired bilateral container** — it contains **both** the
``left`` and ``right`` sides. The **right** container (here) is
**one side** of that parent. Consumers must **not** conflate the
**right container** with the **parent container** — the parent
contains **both sides**; the right container contains **only the
right side**.
**Boundary status (NOT a single nucleus — a CONTAINER of six
nuclei):** **Boundary case — the right VRG container is a
CONTAINER, not a single nucleus.** It contains **six distinct
leaf nuclei** — the **right Bötzinger complex**, **right nucleus
para-ambiguus**, **right nucleus retroambiguus**, **right nucleus
retrofacialis**, **right pre-Bötzinger complex**, and **right
retrotrapezoid nucleus**. Each is a **separate structure** with
**different functions** (expiratory rhythm, expiratory premotor,
inspiratory rhythm, central chemoreception). Consumers must
**not** treat the **right** container as a single uniform
nucleus — it is a **container** of **six functionally distinct
nuclei**.
**Boundary status (NOT the right dorsal respiratory group (DRG) —
a DIFFERENT structure in a DIFFERENT container):** **Boundary
case — the right VRG container is NOT the right DRG.** The
**right DRG**
(``.../respiratory_center/dorsal_respiratory_group/right/``) is
the **right dorsal respiratory** group in the **right NTS
region** — it **relays pulmonary stretch receptor input** to the
respiratory rhythm generator. The **right VRG container** (here)
is the **right ventrolateral** respiratory group — it
**generates** the **respiratory rhythm** (right pre-Bötzinger
complex) and **shapes** the **respiratory pattern**. **They are
DIFFERENT STRUCTURES at DIFFERENT dorsoventral positions** —
the **right DRG** is **dorsal** (in the **right NTS region**);
the **right VRG** is **ventrolateral**. They are **functionally
coupled** — the right DRG **projects to** the right VRG to
**modulate** the **respiratory rhythm** — but they are
**anatomically distinct**. Consumers must **not** conflate the
two. This is the **most consequential** right VRG boundary — the
**dorsal vs. ventrolateral** distinction is the **primary
axis** of the **medullary respiratory network**.
**Boundary status (NOT the right RVLM — the RVLM is the
SYMPATHETIC PREMOTOR center):** **Boundary case — the right VRG
container is NOT the right RVLM.** The **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
sympathetic premotor / vasomotor** center — the **efferent
limb** of the **right medullary baroreflex arc**. The **right VRG
container** (here) is the **right respiratory rhythm and pattern
generator group**. **They are DIFFERENT STRUCTURES** — both are
**ventrolateral**, but they are **functionally distinct** — the
**right RVLM** is **autonomic (sympathetic premotor)**; the
**right VRG** is **respiratory**. They are **anatomically
overlapping** in the **right rostral ventrolateral medulla** —
the **right pre-Bötzinger complex** is **adjacent** to the
**right RVLM** — but they are **distinct functional systems**
wired under **different containers**. Consumers must **not**
conflate the two.
**Boundary status (NOT the right solitary nucleus (NTS) — the NTS
is the VISCERAL AFFERENT relay):** **Boundary case — the right
VRG container is NOT the right NTS.** The **right NTS**
(``.../solitary_nucleus/right/``) is the **right visceral
afferent relay** — it **receives** taste, baroreceptor,
chemoreceptor, and gastrointestinal afferents. The **right VRG
container** (here) is the **right respiratory rhythm and pattern
generator group**. **They are DIFFERENT STRUCTURES** — the
**right NTS** is the **afferent** relay; the **right VRG** is
the **respiratory** generator. They are **functionally coupled**
— the right NTS **projects to** the right VRG to **modulate**
the **respiratory rhythm** in response to **visceral** signals —
but they are **anatomically distinct**. Consumers must **not**
conflate the two.
**Boundary status (NOT the right parafacial zone (PZ) — the PZ
is a SLEEP-PROMOTING region, and is NOT the parafacial
respiratory group (pFRG)):** **Boundary case — the right VRG
container is NOT the right parafacial zone (PZ).** The **right
parafacial zone** (``.../parafacial_zone/right/``) is a **right
GABAergic / glycinergic sleep-promoting** region — **NOT** a
respiratory rhythm generator. **The "parafacial zone" (PZ) is a
DIFFERENT structure from the "parafacial respiratory group"
(pFRG)** — the **pFRG** is a **respiratory** structure
(pre-inspiratory and expiratory-modulating neurons) that is
**often grouped with the retrotrapezoid nucleus (RTN)** as the
**RTN/pFRG complex**. **In this tree, the right pFRG is NOT wired
as a separate module** — it is documented as part of the **right
retrotrapezoid nucleus** prose (see
``.../ventral_respiratory_group/right/retrotrapezoid_nucleus/``).
**The right parafacial zone (PZ) is a DIFFERENT structure** — it
is **wired separately** under ``.../parafacial_zone/right/`` as a
**sleep-promoting** region. **Consumers must not conflate the
right parafacial zone (PZ, sleep-promoting) with the right
parafacial respiratory group (pFRG, respiratory) — they share
the name "parafacial" but are DIFFERENT STRUCTURES.** The
**right PZ** is **sleep-promoting**; the **right pFRG** is
**respiratory** (and wired as part of the **right RTN complex**
in this tree). **The right VRG container** (this module) is
**distinct from both**.
**Boundary status (NOT the right Gi or right paramedian reticular
nucleus — reticular nuclei in DIFFERENT containers):** **Boundary
case — the right VRG container is NOT the right gigantocellular
reticular nucleus (Gi) or the right paramedian reticular
nucleus.** Those are **right reticular** nuclei with **broader**
functions — the **right Gi**
(``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
is **respiratory**, **autonomic**, and **pain-modulatory**;
the **right paramedian reticular nucleus**
(``.../paramedian_reticular_nucleus/right/``) is a **right
cerebellar projection** nucleus with **nociceptive** and
**autonomic** roles. The **right VRG container** (here) is a
**group of specific respiratory rhythm and pattern generator
nuclei** — it is **NOT** a **reticular** nucleus. Consumers must
**not** conflate the right VRG with either right reticular
nucleus.
**Boundary status (NOT the other right respiratory_center
children — DIFFERENT structures):** **Boundary case — the right
VRG container is NOT the other right respiratory_center
children** — the **right DRG**, **right Gi**, **right cuneate
nucleus**, **right gracile nucleus**, **right area postrema**,
and **right chemoreceptor trigger zone**. Each is a **different
structure** — see the respective modules. Consumers must **not**
conflate the right VRG with any of these.
**Boundary status (NOT the whole medulla oblongata — a
respiratory generator container within it):** **Boundary case —
the right VRG container is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the right VRG container (via
the VRG container) **plus** the RVLM, CVLM, NTS,
respiratory_center, cranial nerve nuclei, olivary body,
medullary pyramid, arcuate nucleus, parafacial zone, paramedian
reticular nucleus, perihypoglossal nuclei, and other structures.
The **right VRG container** is **one right respiratory generator
container** within the medulla. Consumers must **not** conflate
the **right VRG** with the **whole medulla**.

Overview
--------
The **right ventral respiratory group (right VRG) container** is
the **right-side** group of **six respiratory rhythm and pattern
generator nuclei** in the **right ventrolateral medulla
oblongata**. It is the **right-side** of the **ventral
respiratory group**, and it is a **container** (not a leaf)
with **six leaf children** (the six respiratory nuclei).

**The right VRG container is a CONTAINER of six nuclei, NOT a
single nucleus.** The six **right** nuclei are:

*   **Right pre-Bötzinger complex** — the **right primary
    respiratory rhythm generator** — the **"master clock"** of
    the **right side** of breathing.
*   **Right Bötzinger complex** — the **right expiratory** rhythm
    / pattern generator.
*   **Right nucleus para-ambiguus** — **right expiratory premotor**
    neurons.
*   **Right nucleus retroambiguus** — **right expiratory /
    abdominal** premotor neurons.
*   **Right nucleus retrofacialis** — **right expiratory**
    neurons.
*   **Right retrotrapezoid nucleus (RTN)** — the **right primary
    central chemoreceptor** — **CO₂/H⁺** sensor at the **right
    ventral medullary surface**.

**The right VRG container is RESPIRATORY — its name is
FUNCTIONALLY ACCURATE.** Unlike the **respiratory_center** (a
**heterogeneous tree-wiring cluster** containing somatosensory
and circumventricular structures alongside true respiratory
ones), the **right VRG** is **genuinely** a **respiratory**
group — **all six subnuclei** are **respiratory-related**
structures.

**The right VRG container is the VENTROLATERAL respiratory group
— the right DRG is the DORSAL respiratory group.** The **right
VRG** is in the **right ventrolateral medulla**; the **right
DRG** is in the **right dorsal medulla** (in the **right NTS
region**). The **right VRG** **generates** the **respiratory
rhythm** (primarily the **right pre-Bötzinger complex**) and
**shapes** the **respiratory pattern**; the **right DRG**
**relays pulmonary stretch receptor input** to the **right
VRG**.

**The right VRG container is one side of the bilateral parent
container.** The **parent** (``.../ventral_respiratory_group/``)
contains **both** the ``left`` and ``right`` sides; the
**right** container (here) contains **only the right side**.

**The right VRG container is TRULY BILATERAL — the right / left
split is ANATOMICAL.** Unlike the **area postrema** (a
**midline** organ wired as left/right by convention), the
**right** and **left** VRG subnuclei are **anatomically
separate structures** — the **right pre-Bötzinger complex** is
in the **right ventrolateral medulla**; the **left
pre-Bötzinger complex** is in the **left ventrolateral
medulla**.

Structural Children (Six Leaves)
--------------------------------
The right VRG container has **six structural children**, each a
**leaf**:

*   ``botzinger_complex`` — **right Bötzinger complex** —
    **expiratory** rhythm / pattern generator.
*   ``nucleus_para_ambiguus`` — **right nucleus para-ambiguus** —
    **expiratory premotor** neurons.
*   ``nucleus_retroambiguus`` — **right nucleus retroambiguus** —
    **expiratory / abdominal** premotor neurons.
*   ``nucleus_retrofacialis`` — **right nucleus retrofacialis** —
    **expiratory** neurons.
*   ``pre_botzinger_complex`` — **right pre-Bötzinger complex** —
    the **primary respiratory rhythm generator**.
*   ``retrotrapezoid_nucleus`` — **right retrotrapezoid nucleus
    (RTN)** — the **primary central chemoreceptor** (and the
    **right RTN/pFRG complex**).

**Each child is a leaf.** The six nucleus modules are **single
structures** — they have **no structural children** of their
own. Consumers that need **nucleus-level** resolution descend
into one of the six leaves; consumers that need **side-level**
resolution use this container as a whole; consumers that need
**bilateral** resolution iterate over both ``left`` and
``right``.

The Right VRG / Left VRG Boundary
---------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right VRG container** (this module) — the right-side group
    of six respiratory nuclei in the **right ventrolateral
    medulla**.

*   **Left VRG container**
    (``.../ventral_respiratory_group/left/``) — the left-side
    group of six respiratory nuclei in the **left ventrolateral
    medulla**.

**They are the SIDES of the bilateral
ventral_respiratory_group container.** They are **structurally
symmetric mirror containers** — same six leaf nuclei, same
cytoarchitecture, same projections (with some crossed
components), same functions. Consumers must **not** conflate the
right container with the left — resolve the left side via
``ventral_respiratory_group.left``.

The Right VRG / Right Dorsal Respiratory Group (DRG) Boundary
------------------------------------------------------------
This is the **most consequential** dorsoventral respiratory
boundary:

*   **Right VRG container** (this module) — the **right
    ventrolateral** respiratory rhythm and pattern generator
    group.

*   **Right DRG**
    (``.../respiratory_center/dorsal_respiratory_group/right/``)
    — the **right dorsal** respiratory group in the **right NTS
    region**.

**They are DIFFERENT STRUCTURES at DIFFERENT dorsoventral
positions** — the **right DRG** is **dorsal** (in the **right
NTS region**); the **right VRG** is **ventrolateral**. They are
**functionally coupled** — the right DRG **projects to** the
right VRG to **modulate** the **respiratory rhythm** — but they
are **anatomically distinct**. Consumers must **not** conflate
the two.

The Right VRG / Right RVLM Boundary
-----------------------------------
This is the **respiratory / autonomic** boundary:

*   **Right VRG container** (this module) — the **right
    respiratory rhythm and pattern generator group**.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``)
    — the **right sympathetic premotor / vasomotor** center.

**They are DIFFERENT STRUCTURES** — both are **ventrolateral**,
but they are **functionally distinct** — the **right RVLM** is
**autonomic (sympathetic premotor)**; the **right VRG** is
**respiratory**. They are **anatomically overlapping** in the
**right rostral ventrolateral medulla** — the **right
pre-Bötzinger complex** is **adjacent** to the **right RVLM** —
but they are **distinct functional systems** wired under
**different containers**. Consumers must **not** conflate the
two.

The Right VRG / Right Solitary Nucleus (NTS) Boundary
-----------------------------------------------------
This is the **respiratory / visceral afferent** boundary:

*   **Right VRG container** (this module) — the **right
    respiratory rhythm and pattern generator group**.

*   **Right NTS** (``.../solitary_nucleus/right/``) — the **right
    visceral afferent relay**.

**They are DIFFERENT STRUCTURES** — the **right NTS** is the
**afferent** relay; the **right VRG** is the **respiratory**
generator. They are **functionally coupled** — the right NTS
**projects to** the right VRG to **modulate** the **respiratory
rhythm** — but they are **anatomically distinct**. Consumers
must **not** conflate the two.

The Right VRG / Right Parafacial Zone (PZ) Boundary
---------------------------------------------------
This is the **respiratory / sleep-promoting** boundary, with the
**PZ vs. pFRG** name-collision caveat:

*   **Right VRG container** (this module) — the **right
    respiratory rhythm and pattern generator group** — **contains
    the right RTN**, which is the **right pFRG's** **home
    region** in this tree.

*   **Right parafacial zone (PZ)**
    (``.../parafacial_zone/right/``) — the **right
    sleep-promoting** region — **NOT** the **right parafacial
    respiratory group (pFRG)**.

**They are DIFFERENT STRUCTURES** — the **right PZ** is
**sleep-promoting**; the **right VRG** is **respiratory**. **The
right PZ is NOT the right pFRG** — they share the name
"parafacial" but are **different structures**. **The right pFRG
is a respiratory structure** — **not wired as a separate
module** in this tree, but **documented** as part of the **right
RTN/pFRG complex** under
``.../ventral_respiratory_group/right/retrotrapezoid_nucleus/``.
Consumers must **not** conflate the right VRG with the right
parafacial zone (PZ), **and must not** conflate the right
parafacial zone (PZ) with the right parafacial respiratory group
(pFRG).

The Right VRG / Right Gi and Right Paramedian Reticular Nucleus Boundary
------------------------------------------------------------------------
This is the **respiratory generator / reticular** boundary:

*   **Right VRG container** (this module) — the **right
    respiratory rhythm and pattern generator group**.

*   **Right Gi**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
    — the **right large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

*   **Right paramedian reticular nucleus**
    (``.../paramedian_reticular_nucleus/right/``) — the **right
    smaller**, **more medial** reticular nucleus.

**They are DIFFERENT STRUCTURES** — the **right Gi** and **right
paramedian reticular nucleus** are **reticular** nuclei with
**broader** functions; the **right VRG** is a **group of
specific respiratory rhythm and pattern generator nuclei**.
Consumers must **not** conflate the right VRG with either right
reticular nucleus.

The Right VRG / Other Right Respiratory Center Children Boundary
----------------------------------------------------------------
This is the **respiratory generator / other-respiratory-center**
boundary:

*   **Right VRG container** (this module) — the **right
    ventrolateral** respiratory generator group.

*   **Right DRG, right Gi, right cuneate nucleus, right gracile
    nucleus, right area postrema, right chemoreceptor trigger
    zone** — the **other right children** of
    ``respiratory_center``.

**Each is a DIFFERENT STRUCTURE** — the **right DRG** is
**dorsal respiratory**; the **right Gi** is **reticular**; the
**right cuneate** and **right gracile nuclei** are
**somatosensory**; the **right area postrema** and **right
chemoreceptor trigger zone** are **circumventricular**.
Consumers must **not** conflate the right VRG with any of these.

The Right VRG / Whole VRG Container, Whole Medulla Oblongata Boundary
---------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Right VRG container** (this module) — one **child** of the
    ``ventral_respiratory_group`` container.

*   **Ventral respiratory group**
    (``.../ventral_respiratory_group/``) — the **bilateral
    container** of the right + left VRG.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the VRG container and other
    medullary structures.

**The right VRG container is a CONTAINER in a CHAIN of
containers.** Consumers must **not** conflate the **container**
with any of the **parent containers**.

Function in the Human Brain
---------------------------
The right VRG container's function is **right respiratory rhythm
generation** and **right respiratory pattern generation** —
**NOT autonomic regulation** and **NOT visceral afferent relay**:

*   **Right respiratory rhythm generation (right pre-Bötzinger
    complex):** The **right pre-Bötzinger complex** is the
    **right primary respiratory rhythm generator** — it
    **generates** the **right inspiratory rhythm**.

*   **Right expiratory pattern generation (right Bötzinger
    complex, right nucleus para-ambiguus, right nucleus
    retroambiguus, right nucleus retrofacialis):** These four
    nuclei **shape** the **right expiratory pattern** — the
    **right active expiration** (via **right abdominal** muscles,
    **right internal intercostals**) and the **right premotor**
    control of **right expiratory** muscles.

*   **Right central chemoreception (right RTN / pFRG):** The
    **right RTN** — the **right retrotrapezoid nucleus** — is
    the **right primary central chemoreceptor** — it **senses**
    **CO₂/H⁺** at the **right ventral medullary surface** and
    **drives** **right inspiration** in response to
    **hypercapnia**.

*   **Integration with higher centers:** The **right VRG**
    **receives** descending input from the **pons (pneumotaxic
    center)**, the **cortex**, the **hypothalamus**, and the
    **limbic** system — and it **integrates** these with
    **chemosensory** (right RTN) and **visceral** (right NTS)
    input to **produce** the **right respiratory pattern**
    adapted to **behavioral** and **metabolic** demands.

*   **NOT autonomic regulation:** The **autonomic regulation** is
    the **right RVLM**, **right CVLM**, and **right NTS** —
    **NOT** the right VRG.

*   **NOT visceral afferent relay:** The **visceral afferent
    relay** is the **right NTS** — **NOT** the right VRG.

**The unifying theme:** the right VRG container is the
**right-side** **respiratory rhythm and pattern generator group**
of the **right ventrolateral medulla** — it **generates** the
**right respiratory rhythm** (right pre-Bötzinger complex),
**shapes** the **right respiratory pattern** (right Bötzinger,
right nucleus para-ambiguus, right nucleus retroambiguus, right
nucleus retrofacialis), and **senses** **CO₂/H⁺** (right RTN) —
**NOT** an autonomic center, **NOT** a visceral afferent relay,
and **NOT** a reticular nucleus.

Associated Disorders
--------------------
The right VRG container is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**, via
**right respiratory rhythm** and **pattern** dysfunction (though
the **whole-body** phenotypes — CCHS, central sleep apnea, etc.
— are typically **bilateral** because the VRGs work together):

*   **Congenital central hypoventilation syndrome (CCHS — via
    right pre-Bötzinger complex and right RTN dysfunction):**
    **CCHS** — the **"Ondine's curse"** — is a **genetic
    disorder** (typically **PHOX2B** mutations) causing **failure
    of automatic breathing** during **sleep**. The **right
    pre-Bötzinger complex** and **right RTN** contribute — their
    dysfunction impairs **right central respiratory rhythm
    generation** and **right central chemoreception** — **the
    left side and higher centers** can partially compensate.

*   **Central sleep apnea (via right pre-Bötzinger complex and
    right RTN dysfunction):** **Central sleep apnea** — **cessation**
    of **breathing** during **sleep** — is a **disorder** of
    the **central respiratory rhythm generator** and the
    **central chemoreceptors** (right pre-Bötzinger complex and
    right RTN).

*   **Rett syndrome (via right pre-Bötzinger complex and right
    RTN dysfunction):** **Rett syndrome** — an **X-linked**
    neurodevelopmental disorder — **frequently** involves
    **respiratory dysrhythmias** via **dysfunction** of the
    **right pre-Bötzinger complex** and **right RTN/pFRG**.

*   **Sudden infant death syndrome (SIDS — via right
    pre-Bötzinger complex and right RTN involvement):** **SIDS**
    has been **associated** with **abnormalities** in the
    **medullary respiratory network** — including the **right
    pre-Bötzinger complex** and **right RTN**.

*   **Opioid-induced respiratory depression (via right
    pre-Bötzinger complex μ-opioid receptor activation):**
    **Opioids** **suppress** the **right pre-Bötzinger complex**
    — **reducing** the **respiratory rate** and **causing**
    **central apnea** in **overdose**.

*   **Brainstem stroke (via right VRG involvement):** **Right
    medullary stroke** can **involve** the **right VRG** —
    contributing to **right respiratory pattern** abnormalities,
    **central apnea**, and **sleep-disordered breathing**.

*   **No Named "Right VRG Syndrome":** The right VRG container is
    a **right respiratory generator group** — its clinical
    syndromes are **named for the broader clinical entity**
    (CCHS, central sleep apnea, Rett syndrome, SIDS) or the
    **broader lesion** (brainstem stroke) — **NOT** for the right
    VRG itself.

**What is NOT here:** The right VRG container is **not** the
substrate for **sympathetic premotor** function (right RVLM),
**sympathoinhibition** (right CVLM), **visceral afferent relay**
(right NTS), **emesis** (right area postrema / right CTZ),
**somatosensory loss** (right cuneate / right gracile nuclei),
**tongue weakness** (right hypoglossal nucleus), or **sleep
promotion** (right parafacial zone). Its clinical relevance is
the **right respiratory rhythm** and **pattern** functions
listed above.

Lateralization Notes
--------------------
This is the **right** VRG container. The ventral respiratory group
is a **bilateral container** whose two sides are **ANATOMICALLY
SEPARATE** — **not** a wiring convention for a midline organ
(unlike the area postrema / CTZ) — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left** VRG
    containers are **structurally symmetric** — they are **mirror
    pairs** with the **same** six leaf nuclei, **same**
    cytoarchitecture, **same** projections (with some crossed
    components), and **same** functions. The **right** VRG
    container holds the **six right-side** respiratory nuclei;
    the **left** VRG container holds the **six left-side**
    respiratory nuclei.

*   **Partly Crossed Projections:** Some **VRG** projections are
    **ipsilateral** (to the **ipsilateral** phrenic / intercostal
    motor neurons via the **ipsilateral** bulbospinal pathway)
    and some are **crossed**. The **VRG** functions
    **bilaterally** in **respiratory rhythm generation** and
    **pattern generation** — the **right and left VRG** together
    ensure that **breathing** is **synchronized** across both
    sides of the **diaphragm** and **chest wall**.

*   **NO Lateralization Warning:** The VRG has **no known
    functional lateralization** in humans — the **right** and
    **left** subnuclei are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the right VRG — the **right**
    and **left** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right VRG
    container is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the right VRG container.

*   **NO Fear-Output Warning:** The right VRG container is **not**
    a fear-output structure — it is a **right respiratory rhythm
    and pattern generator group**. Consumers must **not**
    conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "right VRG = left VRG" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The VRG is
a **strict-mirror container with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right VRG container is a
    **container** — it does **not** import from ``.../left/``
    or any other left-side module. Bilateral relationships are
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
    right VRG container's relationships to the right DRG, right
    RVLM, right CVLM, right NTS, right parafacial zone, right Gi,
    right paramedian reticular nucleus, and other right medullary
    structures are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with six leaf children.** The structural
    children are the six **respiratory nuclei** — each a
    **leaf**. Consumers **should** descend into them for
    **nucleus-level** resolution.
*   **NOT the left VRG container.** The left VRG container is a
    **separate module** under
    ``.../ventral_respiratory_group/left/``. Consumers must
    **not** conflate the right container with the left.
*   **NOT the parent ventral_respiratory_group container.** The
    parent is the **unpaired bilateral container**; the **right**
    module is **one side** of it.
*   **RESPIRATORY, NOT a tree-wiring artifact.** The right VRG is
    **genuinely respiratory** — all six subnuclei are
    respiratory-related structures.
*   **NOT the right DRG.** The **right DRG** is the **right
    dorsal respiratory** group in the **right NTS region** — a
    **different** structure. This is the **most consequential**
    right VRG boundary.
*   **NOT the right RVLM.** The **right RVLM** is the **right
    sympathetic premotor** center — **autonomic**, not
    **respiratory**.
*   **NOT the right NTS.** The **right NTS** is the **right
    visceral afferent** relay — not the **respiratory**
    generator.
*   **NOT the right parafacial zone (PZ).** The **right PZ** is a
    **sleep-promoting** region — **NOT** the **right parafacial
    respiratory group (pFRG)**. **The PZ and pFRG share the
    name "parafacial" but are DIFFERENT STRUCTURES.**
*   **NOT the right Gi or the right paramedian reticular
    nucleus.** Those are **reticular** nuclei with **broader**
    functions.
*   **NOT the other right respiratory_center children.** The
    **right DRG, right Gi, right cuneate nucleus, right gracile
    nucleus, right area postrema, and right chemoreceptor trigger
    zone** are **different structures**.
*   **NOT the whole VRG container or whole medulla oblongata.**
    The right VRG container is a **container** in a **chain** of
    containers.
*   **No ``AREA_PATHS`` hop.** The right VRG container is a
    **local container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The right VRG container has no
    nested dual-framing module. It is a **container** with **six
    leaf children**.
*   **Structural parity with the left VRG container — strict
    mirror with NO warning.** The right and left containers are
    **structurally identical** — same six leaf children, same
    **respiratory** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "ventral_respiratory_group.right"
    )

**Do not** expect the six nuclei to be wired directly under
``ventral_respiratory_group``. The **right** and **left**
containers are **intermediate** — the six nuclei are leaf
children of those containers. Resolve them via
``ventral_respiratory_group.right.<nucleus>``.

**Do not** assume the right VRG container is the **left VRG
container**. The left VRG container is the **separate module**
at ``.../ventral_respiratory_group/left/``.

**Do not** assume the right VRG container is the **right DRG**.
The right DRG is the **right dorsal respiratory** group in the
**right NTS region** — a **different** structure. This is the
**most consequential** right VRG boundary.

**Do not** assume the right VRG container is the **right RVLM**.
The right RVLM is the **right sympathetic premotor** center —
**autonomic**, not **respiratory**.

**Do not** assume the right VRG container is the **right NTS**.
The right NTS is the **right visceral afferent** relay — not the
**respiratory** generator.

**Do not** assume the right VRG container is the **right
parafacial zone (PZ)**. The right PZ is a **sleep-promoting**
region — **NOT** the **right parafacial respiratory group
(pFRG)**. **The PZ and pFRG share the name "parafacial" but are
DIFFERENT STRUCTURES.**

**Do not** assume the right VRG container is the **right Gi** or
the **right paramedian reticular nucleus**. Those are
**reticular** nuclei with **broader** functions.

**Do not** assume the right VRG container is the **right DRG,
right Gi, right cuneate nucleus, right gracile nucleus, right
area postrema, or right chemoreceptor trigger zone**. Each is a
**different structure** — see the respective modules.

**Do not** assume the right VRG container has **structural
children beyond the six respiratory nuclei**. It is a
**container** with **six leaf children** — no further
sub-containers.

Iterating the right VRG container's structural children
(recommended consumer pattern)::

    RIGHT_VENTRAL_RESPIRATORY_GROUP_CHILDREN = (
        "botzinger_complex",
        "nucleus_para_ambiguus",
        "nucleus_retroambiguus",
        "nucleus_retrofacialis",
        "pre_botzinger_complex",
        "retrotrapezoid_nucleus",
    )
    # Each child is a leaf module representing the RIGHT side of
    # one of the six respiratory nuclei.

Reaching the six right nuclei (recommended consumer pattern)::

    # The six right nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.botzinger_complex
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.nucleus_para_ambiguus
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.nucleus_retroambiguus
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.nucleus_retrofacialis
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.pre_botzinger_complex
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.retrotrapezoid_nucleus
    #
    # Each is a leaf module representing the RIGHT side of that
    # nucleus.

Reaching the left VRG container (recommended consumer pattern —
the contralateral container)::

    # The left VRG container is the CONTRALATERAL container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left
    #
    # The right and left VRG containers are structurally symmetric
    # mirror pairs with the same six leaf nuclei.

Reaching the right DRG (recommended consumer pattern — NOTE the
DIFFERENT container, most consequential right VRG boundary)::

    # The right dorsal respiratory group is a CHILD of
    # respiratory_center — NOT wired under
    # ventral_respiratory_group:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.right
    #
    # The right VRG (ventral respiratory group) and the right DRG
    # (dorsal respiratory group) are DIFFERENT STRUCTURES at
    # DIFFERENT dorsoventral positions.

Reaching the right RVLM (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The right rostral ventrolateral medulla is a SEPARATE
    # container under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #
    # The right VRG is RESPIRATORY; the right RVLM is SYMPATHETIC
    # PREMOTOR.

Reaching the right NTS (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The right solitary nucleus is a SEPARATE container under
    # medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # The right NTS is the VISCERAL AFFERENT relay — it PROJECTS
    # to the right VRG to modulate respiratory pattern.

Reaching the right parafacial zone (recommended consumer pattern
— NOTE the DIFFERENT container AND the pFRG caveat)::

    # The right parafacial zone (PZ) is a SLEEP-PROMOTING region
    # — a SEPARATE container under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone.right
    #
    # The right PZ is NOT the right parafacial respiratory group
    # (pFRG). The right pFRG is a RESPIRATORY structure —
    # documented as part of the right RTN/pFRG complex under
    # ventral_respiratory_group.right.retrotrapezoid_nucleus.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides and all six nuclei)::

    for side in ("left", "right"):
        for nucleus in RIGHT_VENTRAL_RESPIRATORY_GROUP_CHILDREN:
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