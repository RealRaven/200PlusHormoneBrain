"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain.anterior_perforated_substance
=====================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_forebrain
                    └── anterior_perforated_substance   <-- THIS MODULE

**Primary synonym:** Anterior perforated substance (APS); substantia
perforata anterior; preforate area (rare); "the perforated spot."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**surface region** — a grey-matter area on the ventral surface of the
hemisphere, perforated by the **lenticulostriate arteries**.
**Part of:** The **basal forebrain** container — and, in classical
anatomy, the **rhinencephalon** (it is one of the five structures the
tree's narrow rhinencephalon definition **deliberately excluded** and
placed here).
**Structural parent:** ``.../right/subcortical/basal_forebrain/`` →
**direct child** of the basal forebrain container.
**Structural children:** **None.** This is a **leaf** module. The
structures that **sit on** its surface (olfactory tubercle, olfactory
striae) are **siblings or separate modules**, not children.
**Boundary status (surface region, not a nucleus):** **Boundary case —
a ventral surface region, not a deep nucleus.** The APS is a
**rhomboid patch of grey matter on the ventral surface** of the
hemisphere, **perforated** by small arteries. It is **not** a deep
nucleus (like the basal ganglia) and **not** a homogeneous cortical
area (like the piriform cortex). It is a **surface** with a
**heterogeneous cytoarchitecture** — islands of olfactory cortex
rostrally, transitional tissue caudally — and its identity is
**topographic** (where it is) as much as **cytological** (what it
contains). Consumers must not treat the APS as a uniform nucleus.
**Boundary status (not rhinencephalon):** **Boundary case — one of the
five structures the rhinencephalon excluded.** The rhinencephalon's
narrow definition places the APS **here**, not under
``rhinencephalon/``. Consumers reconstructing the **classical full
rhinencephalon** must union the rhinencephalon with this container
(see the parent `basal_forebrain` module's
`CLASSICAL_FULL_RHINENCEPHALON` pattern).
**Boundary status (not the olfactory tubercle):** **Boundary case —
the olfactory tubercle SITS ON the APS but is wired under the basal
ganglia.** The **olfactory tubercle** is a small elevation on the
APS's **anteromedial surface**, and it is wired under
``subcortical/basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/``
— **not** here. The APS is the **surface**; the tubercle is the
**elevation on it**. Consumers that need the olfactory tubercle must
resolve it through the **basal ganglia container**, not through the
APS. See *The APS/Olfactory Tubercle Boundary* below.
**Boundary status (not the olfactory tract or striae):** **Boundary
case — the olfactory tract and its striae LIE ON the APS but are
wired under the rhinencephalon.** The **olfactory tract** and the
**lateral olfactory stria** lie on the APS's **dorsal/rostral
surface** and are wired under
``rhinencephalon/olfactory_tract/`` — **not** here. The APS is the
**surface** they lie on; they are the **axons** that cross it.
Consumers that need the olfactory tract must resolve it through the
**rhinencephalon**, not through the APS.
**Boundary status (not piriform cortex):** **Boundary case — the
rostral APS is continuous with the piriform cortex, but the piriform
cortex is a rhinencephalon leaf.** The APS's **rostral part** is
**cytoarchitecturally continuous** with the **piriform cortex** (and
with the olfactory tubercle). The piriform cortex is wired under
``rhinencephalon/piriform_cortex/`` — **not** here. The APS is the
**surface**; the piriform cortex is the **cortical mantle** that is
continuous with it rostrally. Consumers must not resolve piriform
cortex through the APS.
**Boundary status (not diagonal band):** **Boundary case — the
diagonal band of Broca crosses the APS surface, but is a sibling.**
The **diagonal band of Broca** crosses the APS surface (and is often
described as "within" it), but it is a **sibling** under
``basal_forebrain/diagonal_band_of_broca/`` — **not** a child of the
APS. Consumers that need the diagonal band must resolve it through
its own module.
**Boundary status (vascular — "perforated"):** **Boundary case — the
"perforation" is arterial, not developmental.** The APS is named for
the **numerous small holes** on its surface through which the
**lenticulostriate arteries** (and the **recurrent artery of
Heubner**) enter the brain to supply the basal ganglia and internal
capsule. The "perforation" is **vascular**, not a developmental
foramen. Consumers must not interpret "perforated" as a structural
defect.

Overview
--------
The anterior perforated substance is a **rhomboid grey-matter patch on
the ventral surface** of the hemisphere, located at the **junction of
the orbital surface of the frontal lobe and the anterior perforated
region of the temporal lobe**. It is bounded:

*   **Anteriorly** — by the **olfactory tract** and the
    **olfactory trigone** (rhinencephalon leaves that lie on its
    rostral edge).
*   **Laterally** — by the **limen insulae** and the **lateral
    olfactory stria** (the stria runs along its lateral margin).
*   **Medially** — by the **optic chiasm**, the **lamina
    terminalis**, and the **septum pellucidum** region.
*   **Posteriorly** — by the **optic tract** and the **cerebral
    peduncle** (midbrain).

**The APS is the structural base on which the olfactory tubercle
sits.** The **olfactory tubercle** is a small elevation on the APS's
**anteromedial surface**, and it is wired under the **basal ganglia**
(as part of the **ventral striatum**) — **not** here. The APS is the
**surface**; the tubercle is the **elevation on it**. This is the
tree's **most consequential split** for consumers building an
olfactory registry: the **olfactory tubercle** is a **basal ganglia
child**, and the **APS** is a **basal forebrain child**, even though
the tubercle sits **on** the APS.

**The APS is the surface through which the lenticulostriate arteries
enter the brain.** This is its **defining vascular role** and its
**most clinically consequential property**. The **lenticulostriate
arteries** (from the M1 segment of the middle cerebral artery) and the
**recurrent artery of Heubner** (from the anterior communicating
artery) pass through the APS to supply the **basal ganglia** and the
**internal capsule**. **Hypertensive hemorrhage** in this territory is
the classic **putaminal hemorrhage** — a **neurosurgical emergency**
that is the APS's **signature clinical association**, alongside its
olfactory one.

**The APS is classically rhinencephalic.** In classical anatomy, the
APS is part of the **rhinencephalon** — it is the surface on which the
olfactory tract and striae lie, and its rostral part is continuous
with the piriform cortex. The tree's narrow rhinencephalon definition
**excludes** it and places it here under the **basal forebrain** —
because the basal forebrain is where the **olfactory-relay surface**
and the **lenticulostriate gateway** co-occur. This is a **deliberate
boundary choice**: the APS is **not** wired under the rhinencephalon,
and consumers that need the **classical rhinencephalon** must union
the two containers.

**The APS is not the olfactory tubercle.** This is the **most common
confusion** for consumers looking for the olfactory tubercle in its
classical basal-forebrain location. The tubercle is under
``basal_ganglia/striatum/ventral_striatum/`` — the **basal ganglia**,
not the basal forebrain. The APS is the **surface** the tubercle sits
on; it is not the tubercle itself. See *The APS/Olfactory Tubercle
Boundary* below.

**The APS is not the olfactory tract or striae.** The **olfactory
tract** and the **lateral olfactory stria** lie **on** the APS's
dorsal/rostral surface, and they are wired under
``rhinencephalon/olfactory_tract/``. The APS is the **surface**; they
are the **axons** that cross it. Consumers must not resolve the
olfactory tract through the APS.

Surface Topography (prose, not structural children)
---------------------------------------------------
The APS's **surface** carries or is crossed by **several structures**,
all wired **elsewhere**:

*   **Olfactory tract** (rostral) — ``rhinencephalon/olfactory_tract/``.
    The tract lies on the APS's rostral margin and divides into the
    striae at the olfactory trigone.

*   **Lateral olfactory stria** (lateral) —
    ``rhinencephalon/olfactory_tract/``. The LOS runs along the APS's
    lateral margin.

*   **Medial olfactory stria** (medial, when present) —
    ``rhinencephalon/olfactory_tract/``. The MOS runs along the APS's
    medial margin toward the septal area.

*   **Olfactory tubercle** (anteromedial elevation) —
    ``subcortical/basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/``.
    The tubercle is an **elevation** on the APS surface, wired under
    the **basal ganglia**.

*   **Diagonal band of Broca** (crossing the surface) —
    ``subcortical/basal_forebrain/diagonal_band_of_broca/``. The
    band crosses the APS surface and is a **sibling** of the APS,
    not a child.

*   **Lenticulostriate arteries** (perforating) — **not a module**;
    they are the **vessels** that give the APS its name and its
    vascular role. They are documented as **prose** here; they are
    **not** a structural child.

*   **Recurrent artery of Heubner** (perforating, when present) —
    **not a module**; another **perforating vessel** documented as
    prose.

**These structures are prose, not structural children.** The tree
does **not** wire them as APS children — each is either a **sibling**
under the basal forebrain, a **child of another container** (basal
ganglia, rhinencephalon), or a **vessel** (not a module). Consumers
must resolve each at its **own path**.

The APS/Olfactory Tubercle Boundary
-----------------------------------
This is the **most consequential boundary** in the APS module:

*   **APS** (this module) — a **surface region** under
    ``basal_forebrain/``; its identity is **topographic and
    vascular** (the lenticulostriate gateway) as much as olfactory.

*   **Olfactory tubercle** —
    ``subcortical/basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/``
    — an **elevation on the APS surface**, wired under the **basal
    ganglia** (ventral striatum). Its identity is **striatal**
    (it is part of the ventral striatum) as much as olfactory.

**The tubercle sits on the APS, but they are siblings in different
containers.** This is a **deliberate boundary choice** that reflects
the tubercle's **striatal-like cytoarchitecture** — it is a
**ventral striatum structure** with an olfactory function, not a
**basal forebrain surface** with an olfactory function. The APS is the
**surface**; the tubercle is the **elevation on it** with **striatal
identity**.

**Consumers that need the "olfactory tubercle" must resolve it through
the basal ganglia.** Consumers that need the **"anterior perforated
substance"** must resolve it through the basal forebrain. **They are
different structures** in different containers, even though they are
**anatomically adjacent** and often **functionally coupled**
(olfactory input reaches both).

The APS/Rhinencephalon Boundary
-------------------------------
The APS is one of the **five structures the rhinencephalon
excluded**. The other four are the **amygdala**, **hippocampus**,
**septal nuclei**, and **olfactory tubercle**. The APS is the
**olfactory-relay surface** — the **ventral surface** on which the
olfactory tract and striae lie and through which the lenticulostriate
arteries pass. The rhinencephalon modules **redirect** the APS to the
basal forebrain; this module **receives** it. The parent
`basal_forebrain` module's `CLASSICAL_FULL_RHINENCEPHALON` pattern
documents the full union.

Function in the Human Brain
---------------------------
The APS's functions are **surface-dependent** — there is no single
"APS function":

*   **Olfactory Relay Surface (Surface Function):** The APS is the
    **ventral surface** on which the **olfactory tract** and its
    **striae** lie. It provides the **anatomical substrate** for the
    olfactory tract's **distribution** into the LOS, MOS, and
    intermediate stria. The **processing** happens in the olfactory
    tract and the primary olfactory cortex (piriform, periamygdaloid),
    not in the APS per se.

*   **Vascular Gateway (Vascular Function):** The APS is the surface
    through which the **lenticulostriate arteries** (from the M1
    segment of the MCA) and the **recurrent artery of Heubner** (from
    the ACoA) enter the brain to supply the **basal ganglia** and the
    **internal capsule**. This is the APS's **most clinically
    consequential function** — it is a **vascular gateway**, not a
    neural processor.

*   **Olfactory Tubercle Base (Structural Function):** The APS is the
    **structural base** on which the olfactory tubercle sits. The
    tubercle is wired under the basal ganglia; the APS is its
    **surface**. This topographic relationship is not a "function" in
    the physiological sense, but it is the APS's **defining structural
    role** — it is the **surface** the tubercle sits on.

*   **Rostral Continuation into Piriform Cortex (Transitional
    Function):** The APS's **rostral part** is **cytoarchitecturally
    continuous** with the **piriform cortex**. The APS is the
    **transitional surface** between the basal forebrain's vascular
    region and the rhinencephalon's piriform cortex — but the piriform
    cortex itself is a rhinencephalon leaf, not an APS child.

*   **NOT a neural processor.** The APS is a **surface region**, not a
    neural processing structure. Its surface cortex (rostral) is
    piriform-adjacent; its vascular perforations are arterial. It is
    a **relay surface and vascular gateway**, not a processor.

**The unifying theme:** the APS is the **vascular and olfactory relay
surface** of the basal forebrain. It is **olfactory on its surface**
(where the tract and striae lie), **vascular through its
perforations** (the lenticulostriate gateway), and **structurally
continuous** with the piriform cortex rostrally. No single functional
label fits; the APS's identity is **surface-dependent**, and the
module documents each layer.

Associated Disorders
--------------------
APS disorders are **vascular and olfactory** — and the **vascular
association is the most clinically consequential**:

*   **Hypertensive Putaminal Hemorrhage — the signature emergency:**
    The **lenticulostriate arteries** — which perforate the APS — are
    the **classic site of hypertensive hemorrhage**. **Charcot-Bouchard
    microaneurysms** on these vessels rupture under hypertensive
    stress, producing **putaminal hemorrhage** with **contralateral
    hemiparesis**, **hemianesthesia**, and **hemianopia**. **This is
    the APS's most time-critical clinical association** — the
    lenticulostriate territory is the **most common site of
    hypertensive intracerebral hemorrhage**.

*   **Recurrent Artery of Heubner Infarct:** The **recurrent artery of
    Heubner** (which perforates the APS from the ACoA) supplies the
    **head of the caudate** and the **anterior limb of the internal
    capsule**. Its occlusion produces **contralateral hemiparesis**
    (with or without **caudate** involvement). **ACoA aneurysm
    clipping** can injure this artery.

*   **Anterior Communicating Artery (ACoA) Aneurysm Rupture:** ACoA
    aneurysms are **near the APS**, and their rupture can produce
    **subarachnoid hemorrhage** that **damages the APS** and its
    perforating vessels. **Basal forebrain amnesia** (septal and
    diagonal band involvement) is a **recognized complication** of
    ACoA aneurysm rupture and clipping, and **olfactory dysfunction**
    can accompany it.

*   **Olfactory Dysfunction:** As the surface on which the olfactory
    tract lies, the APS can be **involved** in **anosmia**, **hyposmia**,
    and **olfactory agnosia** — but its contribution is **secondary**
    to the olfactory tract and bulb. It is a **contributor**, not the
    primary substrate.

*   **Olfactory Groove Meningioma — Indirect:** Olfactory groove
    meningiomas can **compress the olfactory tract** against the APS,
    contributing to **unilateral anosmia**. The APS itself is **not**
    the tumor site; it is **adjacent** to the compression.

*   **Rostral APS/Piriform Transition Pathology:** The APS's rostral
    continuity with the **piriform cortex** means that **piriform
    pathology** (Alzheimer's, Parkinson's, epilepsy) can **extend into
    the APS** — but the APS itself is **not** the primary syndrome
    substrate. Its clinical footprint is **vascular** first,
    **olfactory** second.

**What is NOT here:** The APS is **not** the substrate for
**parkinsonism** (substantia nigra, basal ganglia), **Huntington's**
(striatum), **Korsakoff syndrome** (mammillary body, anterior
thalamus), **basal forebrain amnesia** (septal nuclei, diagonal
band), or **piriform epilepsy** (piriform cortex). It contributes the
**lenticulostriate hemorrhage** and the **olfactory-relay surface**
— both are **APS-specific** — and the rest belongs to its neighbors,
documented elsewhere.

Lateralization Notes
--------------------
This is the **right** APS module. The APS is **bilaterally symmetric**
and **functionally non-lateralized** in both its olfactory and its
vascular roles:

*   **Bilateral Olfactory Projection:** Each APS carries the
    **ipsilateral** olfactory tract and its striae. The two sides are
    **functionally symmetric** for olfactory relay.

*   **Bilateral Vascular Gateway:** Each APS is perforated by the
    **ipsilateral** lenticulostriate arteries and the **ipsilateral**
    recurrent artery of Heubner. The two sides are **structurally
    symmetric** as vascular gateways.

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the APS has **no documented left-lateralized or right-lateralized
    function**. **Putaminal hemorrhage** is **bilateral in
    distribution** (either side can bleed); **olfactory relay** is
    **bilateral**.

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the APS. Do not import them into the APS.

**A consumer that assumes "right APS = left APS" will be
structurally and functionally correct** — the two sides are symmetric,
no lateralized function has been demonstrated, and the APS's
**bilateral symmetry** is directly reflected in the **bilateral
occurrence of putaminal hemorrhage**. This is a **strict-mirror pair**:
unlike the periamygdaloid, uncus, and subcortical container pairs, the
APS carries **no right-side-specific misconception** a consumer is
likely to import, so the right module is a **word-for-word mirror** of
the left (with only the path, hemisphere labels, and FMA member
changed).

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``rhinencephalon/``, ``basal_ganglia/``, ``cortex/``,
    ``subcortical/`` (other than via prose redirects), or
    ``.../diencephalon/``. The APS's relationships to the olfactory
    tract, olfactory tubercle, diagonal band, and piriform cortex are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The structures that
    **sit on** the APS surface (olfactory tubercle, olfactory tract,
    striae, diagonal band) are **siblings or separate modules**, not
    children. Consumers must not assume they exist as children;
    resolve each at its own path.
*   **Surface region — not a nucleus, not a cortical area.** The APS
    is a **ventral surface patch** with heterogeneous
    cytoarchitecture (olfactory cortex islands rostrally, transitional
    tissue caudally) and **vascular perforations**. Consumers must
    not treat it as a uniform nucleus or a uniform cortical area.
*   **Boundary case — one of the five rhinencephalon-excluded
    structures.** The APS is **here**, not under ``rhinencephalon/``.
    Consumers reconstructing the **classical full rhinencephalon**
    must union the rhinencephalon with this container.
*   **Boundary case — the olfactory tubercle sits on the APS but is
    NOT here.** The tubercle is under
    ``basal_ganglia/striatum/ventral_striatum/``. This is the **most
    common confusion** for consumers looking for the tubercle in its
    classical basal-forebrain location.
*   **Boundary case — the olfactory tract and striae lie on the APS
    but are NOT here.** They are under
    ``rhinencephalon/olfactory_tract/``. The APS is the surface; they
    are the axons.
*   **Boundary case — the diagonal band crosses the APS but is a
    sibling.** The diagonal band is under
    ``basal_forebrain/diagonal_band_of_broca/``.
*   **"Perforated" is vascular, not developmental.** The APS's name
    comes from the **lenticulostriate arteries** and the **recurrent
    artery of Heubner** perforating its surface. The "perforation" is
    **arterial**, not a developmental defect.
*   **No ``AREA_PATHS`` hop.** The APS is a local leaf under the
    basal forebrain, not a cross-listed leaf.
*   **No nested cross-listing.** The APS has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with left anterior perforated substance.**
    Right and left APS modules are **structurally identical** — same
    leaf status, same surface topography, same vascular role, same
    olfactory-tubercle redirect, same diagonal-band redirect, same
    non-lateralized caveat. **This is a strict mirror pair** — there
    is no right-side-specific misconception to import, so the prose
    is word-for-word identical apart from hemisphere labels.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_forebrain import anterior_perforated_substance

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_forebrain.anterior_perforated_substance"
    )

**Do not** assume the APS **contains** the olfactory tubercle. The
tubercle is under
``basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/`` — it
**sits on** the APS surface, but it is a **basal ganglia child**, not
an APS child. This is the **most common confusion**.

**Do not** assume the APS **contains** the olfactory tract, lateral
olfactory stria, medial olfactory stria, or diagonal band. All four
**lie on** or **cross** the APS surface, but each is a **sibling**
(diagonal band) or a **separate module under rhinencephalon/** (tract,
striae).

**Do not** assume the APS is a **uniform nucleus** or a **uniform
cortical area**. It is a **ventral surface patch** with **heterogeneous
cytoarchitecture** and **vascular perforations**.

**Do not** assume "perforated" means **developmentally perforated**.
The APS's name comes from the **lenticulostriate arteries** and the
**recurrent artery of Heubner** perforating its surface.

**Do not** assume the APS is under ``rhinencephalon/``. It is one of
the **five structures the rhinencephalon excluded**, and it is under
the **basal forebrain**.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        aps_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_forebrain.anterior_perforated_substance"
        )
        # resolve aps_path through the memory/recall layer

Reaching the structures that sit on the APS surface (recommended
consumer pattern)::

    # The structures on the APS surface are NOT children of the APS.
    # Resolve them at their own paths:
    #
    #   Olfactory tubercle (basal ganglia):
    #     subcortical.basal_ganglia.striatum.ventral_striatum.olfactory_tubercle
    #
    #   Olfactory tract (rhinencephalon):
    #     rhinencephalon.olfactory_tract
    #
    #   Diagonal band of Broca (basal forebrain sibling):
    #     subcortical.basal_forebrain.diagonal_band_of_broca
    #
    #   Piriform cortex (rhinencephalon, rostral continuation):
    #     rhinencephalon.piriform_cortex
    #
    # These are SIBLINGS or SEPARATE MODULES, not APS children.

Reconstructing the classical full rhinencephalon (recommended
consumer pattern)::

    # The APS is one of the five structures the rhinencephalon
    # excluded. The full union is:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
    }
    # THIS MODULE contributes the anterior_perforated_substance entry.

The lenticulostriate territory (not a module — consult references)::

    # The lenticulostriate arteries are NOT a module. They are the
    # vessels that perforate the APS and supply the basal ganglia and
    # internal capsule. Their hemorrhagic territory is documented in
    # the references, not in the tree.
    #
    # Hypertensive putaminal hemorrhage is the classic clinical
    # association of the APS.

References
----------
*   **Canonical APS anatomy:** Gibo, H., Lenkey, C. (1981). "Anterior
    perforated substance: microsurgical anatomy." *Journal of
    Neurosurgery* 54:785–791. (Definitive microsurgical anatomy;
    lenticulostriate arteries; recurrent artery of Heubner;
    relationship to olfactory tract and tubercle.)
*   **Lenticulostriate arteries:** Marinković, S., Gibo, H., Milisavljević,
    M., Cetković, M. (2001). "The surgical anatomy of the perforating
    branches of the anterior choroidal artery." *Surgical Neurology*
    56:285–292. (Lenticulostriate and anterior choroidal perforators.)
*   **Hypertensive putaminal hemorrhage:** Kase, C.S., Mohr, J.P.
    (1986). "Hypertensive intracerebral hemorrhage." In *Stroke:
    Pathophysiology, Diagnosis, and Management* (Barnett, H.J.M.,
    et al., eds.). (Lenticulostriate territory as the most common
    site of hypertensive hemorrhage.)
*   **Charcot-Bouchard microaneurysms:** Charcot, J.M., Bouchard, C.
    (1868). "Nouvelles recherches sur la pathogénie de l'hémorragie
    cérébrale." *Archives de Physiologie Normale et Pathologique*
    1:110–127, 643–665. (Classical description of miliary aneurysms
    on lenticulostriate arteries.)
*   **Recurrent artery of Heubner:** Heubner, O. (1872). "Zur
    Topographie der Ernährungsgebiete der einzelnen
    Hirnarterien." *Centralblatt für die medizinischen
    Wissenschaften* 10:817–821. (Original description; ACoA branch
    supplying caudate head and anterior internal capsule.)
*   **ACoA aneurysm and basal forebrain amnesia:** Alexander, M.P.,
    Freedman, M. (1984). "Amnesia after anterior communicating
    artery aneurysm rupture." *Neurology* 34:752–757. (Basal
    forebrain amnesia; APS-adjacent vascular injury.)
*   **Olfactory tract and APS:** Price, J.L. (1990). "Olfactory
    system." In *The Human Nervous System* (Paxinos, G., ed.).
    (APS as the surface on which the olfactory tract and striae lie.)
*   **Olfactory tubercle:** Heimer, L., Wilson, R.D. (1975). "The
    subcortical projections of the allocortex: similarities in the
    neural associations of the hippocampus, the piriform cortex, and
    the neocortex." In *Golgi Centennial Symposium* (Santini, M.,
    ed.). (Olfactory tubercle as a ventral striatum structure on the
    APS surface.)
*   **Rhinencephalon exclusion:** Nieuwenhuys, R., Voogd, J., van
    Huijzen, C. (2008). *The Human Central Nervous System*, 4th ed.
    (Narrow olfactory definition; APS as a classical rhinencephalic
    structure.)
*   **Piriform continuity:** Haberly, L.B. (2001). "Parallel-distributed
    processing in olfactory cortex." *Chemical Senses* 26:551–576.
    (Piriform cortex continuity with the APS region.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (APS in overview.)
*   NeuroNames — Anterior perforated substance (right); FMA —
    Anterior perforated substance (right member).
"""