"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
=============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── ventral_respiratory_group   <-- THIS MODULE
                ├── botzinger_complex
                │   ├── left
                │   └── right
                ├── nucleus_para_ambiguus
                │   ├── left
                │   └── right
                ├── nucleus_retroambiguus
                │   ├── left
                │   └── right
                ├── nucleus_retrofacialis
                │   ├── left
                │   └── right
                ├── pre_botzinger_complex
                │   ├── left
                │   └── right
                └── retrotrapezoid_nucleus
                    ├── left
                    └── right

**Primary synonym:** Ventral respiratory group; VRG; ventral
respiratory column; ventral respiratory column; rostrocaudal
respiratory column of the ventrolateral medulla.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter container** in the **ventrolateral medulla
oblongata** — the **respiratory rhythm and pattern generator
group** of the **brainstem**, comprising **six bilateral
subnuclei** that together **generate** the **respiratory rhythm**
(primarily the **pre-Bötzinger complex**) and **shape** the
**respiratory pattern** (inspiratory and expiratory, via the
**Bötzinger complex**, **pre-Bötzinger complex**, **nucleus
para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, and **retrotrapezoid nucleus**). It is **NOT**
a somatosensory relay (that is the **cuneate** / **gracile
nuclei**), **NOT** a circumventricular organ (that is the **area
postrema** / **CTZ**), **NOT** a sympathetic premotor center
(that is the **RVLM**), **NOT** a visceral afferent relay (that
is the **NTS**), **NOT** a reticular nucleus (that is the
**Gi** / **paramedian reticular nucleus**), and **NOT** a
sleep-promoting region (that is the **parafacial zone**).
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**. It is a **direct child**
of ``medulla_oblongata`` — **NOT** a child of
``respiratory_center`` and **NOT** a child of any other
container. It is a **sibling** of ``respiratory_center``,
``rostral_ventrolateral_medulla``,
``caudal_ventrolateral_medulla``, ``solitary_nucleus``, and
other medullary containers.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Six —** each a **bilateral container**
with ``left/`` and ``right/`` leaf children:
1. ``botzinger_complex`` — the **Bötzinger complex** —
   **expiratory** rhythm / pattern generator.
2. ``nucleus_para_ambiguus`` — the **nucleus para-ambiguus** —
   **expiratory premotor** neurons.
3. ``nucleus_retroambiguus`` — the **nucleus retroambiguus** —
   **expiratory / abdominal** premotor neurons.
4. ``nucleus_retrofacialis`` — the **nucleus retrofacialis** —
   **expiratory** neurons.
5. ``pre_botzinger_complex`` — the **pre-Bötzinger complex** —
   the **primary respiratory rhythm generator** — the **"master
   clock"** of **breathing**.
6. ``retrotrapezoid_nucleus`` — the **retrotrapezoid nucleus
   (RTN)** — the **primary central chemoreceptor** —
   **CO₂/H⁺** sensor at the **ventral medullary surface**.
**Boundary status (NOT the dorsal respiratory group (DRG) — the
DRG is the DORSAL respiratory group):** **Boundary case — the
VRG is NOT the dorsal respiratory group (DRG).** The **DRG**
(``.../respiratory_center/dorsal_respiratory_group/``) is the
**dorsal respiratory** group in the **NTS region** — it
**relays pulmonary stretch receptor input** to the respiratory
rhythm generator. The **VRG** (here) is the **ventrolateral
respiratory** group — it **generates** the **respiratory
rhythm** (pre-Bötzinger complex) and **shapes** the
**respiratory pattern**. **They are DIFFERENT STRUCTURES at
DIFFERENT dorsoventral positions** — the **DRG** is **dorsal**
(in the **NTS region**); the **VRG** is **ventrolateral**. They
are **functionally coupled** — the DRG **projects to** the VRG
(via the **NTS** and **direct** projections) to **modulate**
the **respiratory rhythm** — but they are **anatomically
distinct**. Consumers must **not** conflate the two. This is the
**most consequential** VRG boundary — the **dorsal vs.
ventrolateral** distinction is the **primary axis** of the
**medullary respiratory network**.
**Boundary status (NOT the RVLM — the RVLM is the SYMPATHETIC
PREMOTOR center):** **Boundary case — the VRG is NOT the rostral
ventrolateral medulla (RVLM).** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor / vasomotor** center — the **efferent limb** of the
**medullary baroreflex arc**. The **VRG** (here) is the
**respiratory rhythm and pattern generator group**. **They are
DIFFERENT STRUCTURES** — both are **ventrolateral**, but they
are **functionally distinct** — the **RVLM** is **autonomic
(sympathetic premotor)**; the **VRG** is **respiratory**. They
are **anatomically overlapping** in the **rostral
ventrolateral medulla** — the **pre-Bötzinger complex** is
**adjacent** to the **RVLM** — but they are **distinct
functional systems** wired under **different containers**.
Consumers must **not** conflate the two.
**Boundary status (NOT the solitary nucleus (NTS) — the NTS is
the VISCERAL AFFERENT relay):** **Boundary case — the VRG is
NOT the solitary nucleus (NTS).** The **NTS**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it **receives** taste, baroreceptor, chemoreceptor, and
gastrointestinal afferents. The **VRG** (here) is the
**respiratory rhythm and pattern generator group**. **They are
DIFFERENT STRUCTURES** — the **NTS** is the **afferent** relay;
the **VRG** is the **respiratory** generator. They are
**functionally coupled** — the NTS **projects to** the VRG to
**modulate** the **respiratory rhythm** in response to
**visceral** signals — but they are **anatomically distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the parafacial zone (PZ) — the PZ is a
SLEEP-PROMOTING region, and is NOT the parafacial respiratory
group (pFRG)):** **Boundary case — the VRG is NOT the parafacial
zone (PZ).** The **parafacial zone**
(``.../parafacial_zone/``) is a **GABAergic / glycinergic
sleep-promoting** region — **NOT** a respiratory rhythm
generator. **The "parafacial zone" (PZ) is a DIFFERENT
structure from the "parafacial respiratory group" (pFRG)** —
the **pFRG** is a **respiratory** structure (pre-inspiratory
and expiratory-modulating neurons) that is **often grouped with
the retrotrapezoid nucleus (RTN)** as the **RTN/pFRG complex**.
**In this tree, the pFRG is NOT wired as a separate module** —
it is documented as part of the **retrotrapezoid nucleus**
prose (see
``.../ventral_respiratory_group/retrotrapezoid_nucleus/``).
**The parafacial zone (PZ) is a DIFFERENT structure** — it is
**wired separately** under ``.../parafacial_zone/`` as a
**sleep-promoting** region. **Consumers must not conflate the
parafacial zone (PZ, sleep-promoting) with the parafacial
respiratory group (pFRG, respiratory) — they share the name
"parafacial" but are DIFFERENT STRUCTURES.** The **PZ** is
**sleep-promoting**; the **pFRG** is **respiratory** (and wired
as part of the **RTN complex** in this tree). **The VRG** (this
container) is **distinct from both** — the VRG **contains** the
**RTN** (which includes the pFRG prose), and it is **separate
from** the **parafacial zone (PZ)**.
**Boundary status (NOT the Gi or the paramedian reticular nucleus
— reticular nuclei in DIFFERENT containers):** **Boundary case —
the VRG is NOT the gigantocellular reticular nucleus (Gi) or the
paramedian reticular nucleus.** Those are **reticular** nuclei
with **broader** functions — the **Gi**
(``.../respiratory_center/gigantocellular_reticular_nucleus/``)
is **respiratory**, **autonomic**, and **pain-modulatory**; the
**paramedian reticular nucleus**
(``.../paramedian_reticular_nucleus/``) is a **cerebellar
projection** nucleus with **nociceptive** and **autonomic**
roles. The **VRG** (here) is a **group of specific respiratory
rhythm and pattern generator nuclei** — it is **NOT** a
**reticular** nucleus. Consumers must **not** conflate the VRG
with either reticular nucleus.
**Boundary status (NOT the other respiratory_center children —
DIFFERENT structures):** **Boundary case — the VRG is NOT the
other respiratory_center children** — the **DRG**,
**Gi**, **cuneate nucleus**, **gracile nucleus**, **area
postrema**, and **chemoreceptor trigger zone**. Each is a
**different structure** — see the respective modules. Consumers
must **not** conflate the VRG with any of these.
**Boundary status (NOT the whole medulla oblongata — a
respiratory generator group within it):** **Boundary case — the
VRG is NOT the whole medulla oblongata.** The **medulla
oblongata** (``.../medulla_oblongata/``) is the **parent
container** — it contains the VRG (here) **plus** the
respiratory_center, the RVLM, the CVLM, the NTS, the cranial
nerve nuclei, the olivary body, the medullary pyramid, the
arcuate nucleus, the parafacial zone, the paramedian reticular
nucleus, the perihypoglossal nuclei, and other structures. The
**VRG** is **one respiratory generator group** within the
medulla. Consumers must **not** conflate the **VRG** with the
**whole medulla**.
**Boundary status (BILATERAL container with SIX BILATERAL
CHILDREN):** **Boundary case — the VRG is a BILATERAL container
with SIX BILATERAL CHILDREN.** Each of the **six subnuclei** is
itself a **bilateral container** with ``left`` and ``right``
leaves. The **left VRG subnuclei** are in the **left
ventrolateral medulla**; the **right VRG subnuclei** are in the
**right ventrolateral medulla**. **The left / right split is
ANATOMICAL, not a wiring convention.** Consumers must **not**
infer **midline wiring convention** from the VRG (that
convention applies to the area postrema / CTZ, NOT the VRG).

Overview
--------
The **ventral respiratory group (VRG)** is the **respiratory
rhythm and pattern generator group** of the **brainstem**, in
the **ventrolateral medulla oblongata**. It is the **primary
central respiratory pattern generator** — the **pre-Bötzinger
complex** is the **"master clock"** of **breathing** — and it
**shapes** the **respiratory pattern** (inspiratory and
expiratory) via its **six subnuclei**.

**The VRG is a respiratory structure — its name is FUNCTIONALLY
ACCURATE.** Unlike the **respiratory_center** (a **heterogeneous
tree-wiring cluster** containing somatosensory and
circumventricular structures alongside true respiratory ones),
the **VRG** is **genuinely** a **respiratory** group — **all six
subnuclei** are **respiratory-related** structures. The **name
"ventral respiratory group"** is a **functionally accurate**
label.

**The VRG is the VENTROLATERAL respiratory group — the DRG is the
DORSAL respiratory group.** The **VRG** is in the **ventrolateral
medulla**; the **DRG** is in the **dorsal medulla** (in the
**NTS region**). The **VRG** **generates** the **respiratory
rhythm** (primarily the **pre-Bötzinger complex**) and **shapes**
the **respiratory pattern**; the **DRG** **relays pulmonary
stretch receptor input** to the **VRG**. They form the **dorsal
(DRG) / ventrolateral (VRG)** axis of the **medullary
respiratory network**.

**The VRG is a BILATERAL container with SIX BILATERAL
CHILDREN.** Each of the six subnuclei — **Bötzinger complex**,
**nucleus para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, **pre-Bötzinger complex**, and **retrotrapezoid
nucleus** — is itself a **bilateral container** with ``left`` and
``right`` leaves. **The left / right split is ANATOMICAL** —
**NOT** a midline wiring convention.

**The VRG is TRULY BILATERAL — the left / right split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **left** and **right**
VRG subnuclei are **anatomically separate structures** — the
**left pre-Bötzinger complex** is in the **left ventrolateral
medulla**; the **right pre-Bötzinger complex** is in the
**right ventrolateral medulla**. **The left / right split here
reflects anatomy** — **NOT** a **tree-wiring convention**.

**The VRG is functionally coupled to the DRG, the NTS, the RVLM,
the CVLM, the parafacial zone (PZ), the RTN/pFRG complex, the
pons (pneumotaxic center), and the higher respiratory centers.**
It is **part of** the **ponto-medullary respiratory network** —
a **distributed system** for **breathing**.

**The VRG contains the PARAFACIAL RESPIRATORY GROUP (pFRG) —
but the pFRG is NOT wired as a separate module in this tree.**
The **pFRG** is a **respiratory** structure (pre-inspiratory and
expiratory-modulating neurons) that is **often grouped with the
retrotrapezoid nucleus (RTN)** as the **RTN/pFRG complex**. **In
this tree**, the pFRG is documented as part of the
**retrotrapezoid nucleus** prose — see
``.../ventral_respiratory_group/retrotrapezoid_nucleus/``.
**The parafacial zone (PZ)** is a **DIFFERENT structure** — a
**sleep-promoting** region wired separately under
``.../parafacial_zone/``. **Consumers must not conflate the
parafacial zone (PZ, sleep-promoting) with the parafacial
respiratory group (pFRG, respiratory).**

Bilateral Structure (Six Children × Left/Right Leaves)
------------------------------------------------------
The ventral respiratory group is a **bilateral container** in
this tree with **six structural children**, each a **bilateral
container** with ``left`` and ``right`` leaf children:

*   ``botzinger_complex`` (container) → ``left`` / ``right`` —
    the **Bötzinger complex** — **expiratory** rhythm / pattern
    generator.
*   ``nucleus_para_ambiguus`` (container) → ``left`` / ``right``
    — **expiratory premotor** neurons.
*   ``nucleus_retroambiguus`` (container) → ``left`` / ``right``
    — **expiratory / abdominal** premotor neurons.
*   ``nucleus_retrofacialis`` (container) → ``left`` / ``right``
    — **expiratory** neurons.
*   ``pre_botzinger_complex`` (container) → ``left`` / ``right``
    — the **pre-Bötzinger complex** — the **primary respiratory
    rhythm generator**.
*   ``retrotrapezoid_nucleus`` (container) → ``left`` / ``right``
    — the **RTN** — the **primary central chemoreceptor**.

**Two-level container structure:** ``ventral_respiratory_group``
→ **six child containers** → ``left`` / ``right`` → **leaf
nuclei**. Consumers that need **nucleus-level** resolution
descend into ``ventral_respiratory_group.<child>.{left,right}``;
consumers that need **child-level** resolution descend into
``ventral_respiratory_group.<child>``; consumers that need the
**whole container** use ``ventral_respiratory_group``.

**The six subnuclei are functionally distinct** — the
**pre-Bötzinger complex** is the **primary rhythm generator**;
the **Bötzinger complex**, **nucleus para-ambiguus**, **nucleus
retroambiguus**, and **nucleus retrofacialis** are **expiratory**
pattern / premotor structures; the **RTN** is the **primary
central chemoreceptor** (and the **RTN/pFRG complex**).

The VRG / Dorsal Respiratory Group (DRG) Boundary
-------------------------------------------------
This is the **most consequential** dorsoventral respiratory
boundary:

*   **VRG** (this module) — the **ventrolateral** respiratory
    rhythm and pattern generator group.

*   **DRG** (``.../respiratory_center/dorsal_respiratory_group/``)
    — the **dorsal** respiratory group in the **NTS region**.

**They are DIFFERENT STRUCTURES at DIFFERENT dorsoventral
positions** — the **DRG** is **dorsal** (in the **NTS region**);
the **VRG** is **ventrolateral**. They are **functionally
coupled** — the DRG **projects to** the VRG to **modulate** the
**respiratory rhythm** — but they are **anatomically distinct**.
Consumers must **not** conflate the two.

The VRG / RVLM Boundary
-----------------------
This is the **respiratory / autonomic** boundary:

*   **VRG** (this module) — the **respiratory rhythm and pattern
    generator group**.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **sympathetic premotor / vasomotor** center.

**They are DIFFERENT STRUCTURES** — both are **ventrolateral**,
but they are **functionally distinct** — the **RVLM** is
**autonomic (sympathetic premotor)**; the **VRG** is
**respiratory**. They are **anatomically overlapping** in the
**rostral ventrolateral medulla** — the **pre-Bötzinger complex**
is **adjacent** to the **RVLM** — but they are **distinct
functional systems** wired under **different containers**.
Consumers must **not** conflate the two.

The VRG / Solitary Nucleus (NTS) Boundary
-----------------------------------------
This is the **respiratory / visceral afferent** boundary:

*   **VRG** (this module) — the **respiratory rhythm and pattern
    generator group**.

*   **NTS** (``.../solitary_nucleus/``) — the **visceral afferent
    relay**.

**They are DIFFERENT STRUCTURES** — the **NTS** is the
**afferent** relay; the **VRG** is the **respiratory**
generator. They are **functionally coupled** — the NTS
**projects to** the VRG to **modulate** the **respiratory
rhythm** — but they are **anatomically distinct**. Consumers must
**not** conflate the two.

The VRG / Parafacial Zone (PZ) Boundary
---------------------------------------
This is the **respiratory / sleep-promoting** boundary:

*   **VRG** (this module) — the **respiratory rhythm and pattern
    generator group**.

*   **Parafacial zone (PZ)** (``.../parafacial_zone/``) — the
    **sleep-promoting** region — **NOT** the **parafacial
    respiratory group (pFRG)**.

**They are DIFFERENT STRUCTURES** — the **PZ** is
**sleep-promoting**; the **VRG** is **respiratory**. **The PZ
is NOT the pFRG** — they share the name "parafacial" but are
**different structures**. **The pFRG is a respiratory structure**
— **not wired as a separate module** in this tree, but
**documented** as part of the **RTN/pFRG complex** under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/``.
Consumers must **not** conflate the VRG with the parafacial zone
(PZ), **and must not** conflate the parafacial zone (PZ) with
the parafacial respiratory group (pFRG).

The VRG / Gi and Paramedian Reticular Nucleus Boundary
------------------------------------------------------
This is the **respiratory generator / reticular** boundary:

*   **VRG** (this module) — the **respiratory rhythm and pattern
    generator group**.

*   **Gi** (``.../respiratory_center/gigantocellular_reticular_nucleus/``)
    — the **large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

*   **Paramedian reticular nucleus**
    (``.../paramedian_reticular_nucleus/``) — the **smaller**,
    **more medial** reticular nucleus.

**They are DIFFERENT STRUCTURES** — the **Gi** and **paramedian
reticular nucleus** are **reticular** nuclei with **broader**
functions; the **VRG** is a **group of specific respiratory
rhythm and pattern generator nuclei**. Consumers must **not**
conflate the VRG with either reticular nucleus.

The VRG / Other Respiratory Center Children Boundary
----------------------------------------------------
This is the **respiratory generator / other-respiratory-center**
boundary:

*   **VRG** (this module) — the **ventrolateral** respiratory
    generator group.

*   **DRG**, **Gi**, **cuneate nucleus**, **gracile nucleus**,
    **area postrema**, **chemoreceptor trigger zone** — the
    **other children** of ``respiratory_center``.

**Each is a DIFFERENT STRUCTURE** — the **DRG** is **dorsal
respiratory**; the **Gi** is **reticular**; the **cuneate** and
**gracile nuclei** are **somatosensory**; the **area postrema**
and **chemoreceptor trigger zone** are **circumventricular**.
Consumers must **not** conflate the VRG with any of these.

The VRG / Whole Medulla Oblongata Boundary
------------------------------------------
This is the **child / container** boundary:

*   **VRG** (this module) — one **child** of
    ``medulla_oblongata``.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the VRG and other medullary
    structures.

**The VRG is a CHILD of medulla_oblongata, NOT the whole medulla.**
Consumers must **not** conflate the **child** with the **parent
container**.

Function in the Human Brain
---------------------------
The VRG's function is **respiratory rhythm generation** and
**respiratory pattern generation** — **NOT autonomic
regulation** and **NOT visceral afferent relay**:

*   **Respiratory rhythm generation (pre-Bötzinger complex):**
    The **pre-Bötzinger complex** is the **primary respiratory
    rhythm generator** — the **"master clock"** of **breathing**.
    It **generates** the **inspiratory rhythm** via **pacemaker
    neurons** and **network interactions** — the **inspiratory
    on-switch**, **off-switch**, and **ramp**.

*   **Expiratory pattern generation (Bötzinger complex, nucleus
    para-ambiguus, nucleus retroambiguus, nucleus
    retrofacialis):** The **Bötzinger complex**,
    **nucleus para-ambiguus**, **nucleus retroambiguus**, and
    **nucleus retrofacialis** **shape** the **expiratory
    pattern** — the **active expiration** (via **abdominal**
    muscles, **internal intercostals**) and the **premotor**
    control of **expiratory** muscles.

*   **Central chemoreception (RTN / pFRG):** The **RTN** — the
    **retrotrapezoid nucleus** — is the **primary central
    chemoreceptor** — it **senses** **CO₂/H⁺** at the **ventral
    medullary surface** and **drives** **inspiration** in
    response to **hypercapnia**. The **RTN** also contains the
    **parafacial respiratory group (pFRG)** — **pre-inspiratory**
    and **expiratory-modulating** neurons **active during high
    metabolic demand**.

*   **Integration with higher centers:** The **VRG** **receives**
    descending input from the **pons (pneumotaxic center)**,
    the **cortex**, the **hypothalamus**, and the **limbic**
    system — and it **integrates** these with **chemosensory**
    (RTN) and **visceral** (NTS) input to **produce** the
    **respiratory pattern** adapted to **behavioral** and
    **metabolic** demands.

*   **NOT autonomic regulation:** The **autonomic regulation** is
    the **RVLM**, **CVLM**, and **NTS** — **NOT** the VRG.

*   **NOT visceral afferent relay:** The **visceral afferent
    relay** is the **NTS** — **NOT** the VRG.

**The unifying theme:** the VRG is the **respiratory rhythm and
pattern generator group** of the **ventrolateral medulla** — it
**generates** the **respiratory rhythm** (pre-Bötzinger complex),
**shapes** the **respiratory pattern** (Bötzinger complex,
nucleus para-ambiguus, nucleus retroambiguus, nucleus
retrofacialis), and **senses** **CO₂/H⁺** (RTN / pFRG) —
**NOT** an autonomic center, **NOT** a visceral afferent relay,
and **NOT** a reticular nucleus.

Associated Disorders
--------------------
The VRG is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct**, via
**respiratory rhythm** and **pattern** dysfunction:

*   **Congenital central hypoventilation syndrome (CCHS — via
    pre-Bötzinger complex and RTN dysfunction):** **CCHS** —
    the **"Ondine's curse"** — is a **genetic disorder**
    (typically **PHOX2B** mutations) causing **failure of
    automatic breathing** during **sleep**. The **pre-Bötzinger
    complex** and **RTN** are the **primary substrates** —
    their **dysfunction** impairs the **central respiratory
    rhythm generation** and **central chemoreception**.

*   **Central sleep apnea (via pre-Bötzinger complex and RTN
    dysfunction):** **Central sleep apnea** — **cessation** of
    **breathing** during **sleep** without **airway
    obstruction** — is a **disorder** of the **central
    respiratory rhythm generator** and the **central
    chemoreceptors** (pre-Bötzinger complex and RTN).

*   **Rett syndrome (via pre-Bötzinger complex and RTN
    dysfunction):** **Rett syndrome** — an **X-linked**
    neurodevelopmental disorder (typically **MECP2** mutations)
    — **frequently** involves **respiratory dysrhythmias** —
    **hyperventilation**, **apnea**, **breath-holding** — via
    **dysfunction** of the **pre-Bötzinger complex** and
    **RTN/pFRG**.

*   **Sudden infant death syndrome (SIDS — via pre-Bötzinger
    complex and RTN involvement):** **SIDS** has been
    **associated** with **abnormalities** in the **medullary
    respiratory network** — including the **pre-Bötzinger
    complex** and **RTN**. **Impaired** **central chemoreception**
    and **rhythm generation** are **hypothesized** to
    **contribute** to **SIDS**.

*   **Opioid-induced respiratory depression (via pre-Bötzinger
    complex μ-opioid receptor activation):** **Opioids**
    (e.g., **morphine**, **fentanyl**) **suppress** the
    **pre-Bötzinger complex** — **reducing** the **respiratory
    rate** and **causing** **central apnea** and **death** in
    **overdose**. The **pre-Bötzinger complex** is the
    **primary** substrate of **opioid-induced respiratory
    depression**.

*   **Brainstem stroke (via VRG involvement):** **Medullary
    stroke** can **involve** the **VRG** — contributing to
    **respiratory pattern** abnormalities, **central apnea**,
    and **sleep-disordered breathing**.

*   **No Named "VRG Syndrome":** The VRG is a **respiratory
    generator group** — its clinical syndromes are **named for
    the broader clinical entity** (CCHS, central sleep apnea,
    Rett syndrome, SIDS) or the **broader lesion** (brainstem
    stroke) — **NOT** for the VRG itself.

**What is NOT here:** The VRG is **not** the substrate for
**sympathetic premotor** function (RVLM), **sympathoinhibition**
(CVLM), **visceral afferent relay** (NTS), **emesis** (area
postrema / CTZ), **somatosensory loss** (cuneate / gracile
nuclei), **tongue weakness** (hypoglossal nucleus), or **sleep
promotion** (parafacial zone). Its clinical relevance is the
**respiratory rhythm** and **pattern** functions listed above.

Lateralization Notes
--------------------
The ventral respiratory group is a **bilateral container** with
**six bilateral child containers** — each with ``left`` and
``right`` leaf children.

*   **Bilateral structural children:** The **six child
    containers** (botzinger_complex, nucleus_para_ambiguus,
    nucleus_retroambiguus, nucleus_retrofacialis,
    pre_botzinger_complex, retrotrapezoid_nucleus) are each
    **bilateral containers** with ``left`` and ``right`` leaf
    children. Consumers resolve the nuclei via
    ``ventral_respiratory_group.<child>.{left,right}``.

*   **Bilateral symmetry:** Each **left** subnucleus is
    **structurally symmetric** with its **right** counterpart
    — same cytoarchitecture, same projections (with some
    crossed / contralateral components), same functions.

*   **Partly crossed projections:** Some **VRG** projections are
    **ipsilateral** (to the **ipsilateral** phrenic / intercostal
    motor neurons via the **ipsilateral** bulbospinal pathway)
    and some are **crossed** — the **VRG** functions
    **bilaterally** in **respiratory rhythm generation** and
    **pattern generation**. **Bilateral coordination** of the
    **left and right VRG** ensures that **breathing** is
    **synchronized** across both sides of the **diaphragm**
    and **chest wall**.

*   **NO lateralization warning:** The VRG has **no known
    functional lateralization** in humans — the **left** and
    **right** subnuclei are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the VRG — the **left** and
    **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The VRG is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the VRG.

*   **NO Fear-Output Warning:** The VRG is **not** a fear-output
    structure — it is a **respiratory rhythm and pattern
    generator group**. Consumers must **not** conflate it with
    the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left VRG = right VRG" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The VRG is
a **strict-mirror container with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The VRG is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and
    ``right`` leaves of each child are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../respiratory_center/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../solitary_nucleus/``,
    ``.../parafacial_zone/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../cranial_nerve_nuclei/``, or any other container. The
    VRG's relationships to the DRG, RVLM, CVLM, NTS, parafacial
    zone, Gi, paramedian reticular nucleus, and other medullary
    structures are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with SIX bilateral container children.** The
    structural children are the six **bilateral containers** —
    each with ``left`` / ``right`` leaf children. Consumers
    **should** descend into them for **nucleus-level**
    resolution.
*   **RESPIRATORY, NOT a tree-wiring artifact.** Unlike the
    `respiratory_center` (which contains somatosensory and
    circumventricular structures alongside true respiratory
    ones), the **VRG is genuinely a respiratory group** — all
    six subnuclei are respiratory-related structures.
*   **NOT the DRG.** The **DRG** is the **dorsal respiratory
    group** in the **NTS region** — a **different** structure.
    This is the **most consequential** VRG boundary.
*   **NOT the RVLM.** The **RVLM** is the **sympathetic premotor**
    center — **autonomic**, not **respiratory**.
*   **NOT the NTS.** The **NTS** is the **visceral afferent**
    relay — not the **respiratory** generator.
*   **NOT the parafacial zone (PZ).** The **PZ** is a
    **sleep-promoting** region — **NOT** the **parafacial
    respiratory group (pFRG)**. **The PZ and pFRG share the
    name "parafacial" but are DIFFERENT STRUCTURES.**
*   **NOT the Gi or the paramedian reticular nucleus.** Those are
    **reticular** nuclei with **broader** functions.
*   **NOT the other respiratory_center children.** The **DRG,
    Gi, cuneate nucleus, gracile nucleus, area postrema, and
    chemoreceptor trigger zone** are **different structures**.
*   **NOT the whole medulla oblongata.** The VRG is a **child**
    of ``medulla_oblongata``, not the container itself.
*   **No ``AREA_PATHS`` hop.** The VRG is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The VRG has no nested
    dual-framing module. It is a **bilateral container** with
    **six bilateral container children**, each with **two leaf
    children**.
*   **Structural parity with the right side — strict mirror.**
    Each ``left`` leaf is **structurally identical** to its
    ``right`` counterpart — same leaf status, same framing, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import ventral_respiratory_group

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "ventral_respiratory_group"
    )

**Do not** assume the VRG is the **dorsal respiratory group
(DRG)**. The DRG is the **dorsal respiratory** group in the
**NTS region** — a **different** structure. This is the **most
consequential** VRG boundary.

**Do not** assume the VRG is the **RVLM**. The RVLM is the
**sympathetic premotor** center — **autonomic**, not
**respiratory**.

**Do not** assume the VRG is the **solitary nucleus (NTS)**. The
NTS is the **visceral afferent** relay — not the **respiratory**
generator.

**Do not** assume the VRG is the **parafacial zone (PZ)**. The
PZ is a **sleep-promoting** region — **NOT** the **parafacial
respiratory group (pFRG)**. **The PZ and pFRG share the name
"parafacial" but are DIFFERENT STRUCTURES.**

**Do not** assume the VRG is the **Gi** or the **paramedian
reticular nucleus**. Those are **reticular** nuclei with
**broader** functions.

**Do not** assume the VRG is the **DRG, Gi, cuneate nucleus,
gracile nucleus, area postrema, or chemoreceptor trigger zone**.
Each is a **different structure** — see the respective modules.

**Do not** expect the nuclei to be wired directly under
``ventral_respiratory_group``. The **six children** are
**intermediate bilateral containers** — the nuclei are **leaf
children** of those containers. Resolve them via
``ventral_respiratory_group.<child>.{left,right}``.

**Do not** infer **midline wiring convention** from the VRG
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** VRG subnuclei are **truly separate
bilateral structures** (unlike the area postrema / CTZ, which
are midline organs wired as left/right by convention).

Iterating the VRG's structural children (recommended consumer
pattern)::

    VENTRAL_RESPIRATORY_GROUP_CHILDREN = (
        "botzinger_complex",
        "nucleus_para_ambiguus",
        "nucleus_retroambiguus",
        "nucleus_retrofacialis",
        "pre_botzinger_complex",
        "retrotrapezoid_nucleus",
    )
    # Each child is a BILATERAL CONTAINER with left/ and right/
    # leaf children.

Iterating the leaf modules per child (recommended consumer
pattern)::

    for child in VENTRAL_RESPIRATORY_GROUP_CHILDREN:
        for side in ("left", "right"):
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"ventral_respiratory_group.{child}.{side}"
            )
            # resolve path through the memory/recall layer

Reaching the DRG (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The dorsal respiratory group is a CHILD of respiratory_center
    # — NOT wired under ventral_respiratory_group:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group
    #
    # The VRG (ventral respiratory group) and the DRG (dorsal
    # respiratory group) are DIFFERENT STRUCTURES at DIFFERENT
    # dorsoventral positions — the DRG is dorsal (in the NTS
    # region); the VRG is ventrolateral. They form the dorsal /
    # ventrolateral axis of the medullary respiratory network.

Reaching the RVLM (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The rostral ventrolateral medulla is a SEPARATE container
    # under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #
    # The VRG is RESPIRATORY; the RVLM is SYMPATHETIC PREMOTOR.

Reaching the NTS (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The solitary nucleus is a SEPARATE container under
    # medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The NTS is the VISCERAL AFFERENT relay — it PROJECTS to the
    # VRG to modulate respiratory pattern.

Reaching the parafacial zone (recommended consumer pattern —
NOTE the DIFFERENT container AND the pFRG caveat)::

    # The parafacial zone (PZ) is a SLEEP-PROMOTING region —
    # a SEPARATE container under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone
    #
    # The PZ is NOT the parafacial respiratory group (pFRG). The
    # pFRG is a RESPIRATORY structure — documented as part of the
    # RTN/pFRG complex under
    # ventral_respiratory_group.retrotrapezoid_nucleus.

Reaching the respiratory_center (recommended consumer pattern —
NOTE the SIBLING container)::

    # The respiratory center is a SIBLING container of the VRG
    # under medulla_oblongata — NOT a parent of the VRG:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #
    # The VRG contains the pre-Bötzinger complex (the primary
    # respiratory rhythm generator) and the RTN (the primary
    # central chemoreceptor) — the RESPIRATORY_CORE of the
    # medullary respiratory network.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides and all six children)::

    for child in VENTRAL_RESPIRATORY_GROUP_CHILDREN:
        for side in ("left", "right"):
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"ventral_respiratory_group.{child}.{side}"
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