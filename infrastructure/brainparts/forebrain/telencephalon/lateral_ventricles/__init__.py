"""
infrastructure.brainparts.forebrain.telencephalon.lateral_ventricles
=====================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    ├── cerebral_hemispheres
    ├── commissures
    └── lateral_ventricles                    <-- THIS MODULE
        ├── left
        └── right

**Primary synonym:** Lateral ventricles; ventriculus lateralis;
first and second ventricles; ventricles I and II; the telencephalic
ventricles.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
grey-matter or white-matter structure.** A **paired fluid-filled
cavity system** — the **CSF spaces** of the **telencephalon**,
lined by **ependyma** and containing **choroid plexus**.
**Part of:** The **telencephalon** — specifically, the
**telencephalic ventricular system**. The lateral ventricles are
**telencephalic derivatives** (they develop from the **telencephalic
vesicle**), distinct from the **third ventricle** (diencephalic)
and the **fourth ventricle** (metencephalic).
**Structural parent:** ``.../telencephalon/`` → **direct child** of
the telencephalon container.
**Structural children:** **Two** — ``left/`` and ``right/``. Each
is a **mirrored leaf module**. The **horns** (anterior, posterior,
inferior), the **body**, the **atrium/trigone**, the **choroid
plexus**, the **ependyma**, and the **foramina of Monro** are
documented as **prose**, **not** as structural children.
**Boundary status (NOT the cerebral hemispheres — the ventricles
are the CAVITIES, the hemispheres are the TISSUE):** **Boundary
case — the lateral ventricles are NOT the cerebral hemispheres.**
The **cerebral hemispheres** (``.../cerebral_hemispheres/``) are
the **neural tissue** — the cortex, the white matter, the basal
ganglia, the hippocampus, the amygdala. The **lateral ventricles**
(here) are the **fluid-filled cavities** *within* the hemispheres.
**The ventricles are the CSF spaces; the hemispheres are the
neural parenchyma that surrounds them.** Consumers must **not**
conflate the two — the **cerebral hemispheres** are the tissue;
the **lateral ventricles** are the cavities.
**Boundary status (NOT the third ventricle — the third ventricle is
DIENCEPHALIC):** **Boundary case — the lateral ventricles are NOT
the third ventricle.** The **third ventricle**
(``.../diencephalon/third_ventricle/``) is the **diencephalic**
midline CSF cavity between the thalami. The **lateral ventricles**
(here) are the **telencephalic** paired CSF cavities. **They are
DIFFERENT VENTRICLES in DIFFERENT developmental compartments.**
The lateral ventricles communicate with the third ventricle via
the **interventricular foramen (foramen of Monro)** — that
foramen is a **connection**, not an identity. Consumers must
**not** conflate the lateral ventricles with the third ventricle.
**Boundary status (NOT the fourth ventricle — the fourth ventricle
is METENCEPHALIC):** **Boundary case — the lateral ventricles are
NOT the fourth ventricle.** The **fourth ventricle**
(``.../hindbrain/metencephalon/fourth_ventricle/``) is the
**metencephalic** CSF cavity between the pons/medulla and the
cerebellum. The **lateral ventricles** (here) are the
**telencephalic** paired CSF cavities. **They are DIFFERENT
VENTRICLES in DIFFERENT developmental compartments**, connected
only indirectly via the **third ventricle** and the
**mesencephalic aqueduct (cerebral aqueduct)**. Consumers must
**not** conflate the lateral ventricles with the fourth ventricle.
**Boundary status (NOT the mesencephalic aqueduct — the aqueduct
is MESENCEPHALIC):** **Boundary case — the lateral ventricles are
NOT the mesencephalic aqueduct.** The **mesencephalic aqueduct**
(``.../midbrain/mesencephalic_aqueduct/``) is the **midbrain**
CSF channel connecting the **third ventricle** to the **fourth
ventricle**. The **lateral ventricles** (here) are the
**telencephalic** paired CSF cavities, **upstream** of the
aqueduct in the CSF flow. **They are DIFFERENT CSF spaces.**
Consumers must **not** conflate the lateral ventricles with the
aqueduct.
**Boundary status (NOT the choroid plexus — the choroid plexus is
the CSF-PRODUCING TISSUE INSIDE the ventricles):** **Boundary
case — the lateral ventricles are NOT the choroid plexus.** The
**choroid plexus** is the **CSF-producing epithelial tissue**
(found in the body, atrium, and inferior horn of each lateral
ventricle). The **lateral ventricles** (here) are the **cavities
that CONTAIN the choroid plexus**. **The choroid plexus is a
tissue INSIDE the ventricle; the ventricle is the fluid space.**
Consumers must **not** conflate the lateral ventricles with the
choroid plexus — the **ventricle** is the **cavity**; the
**choroid plexus** is the **CSF-producing tissue within it**.
**Boundary status (NOT the ependyma — the ependyma is the
LINING):** **Boundary case — the lateral ventricles are NOT the
ependyma.** The **ependyma** is the **ciliated simple
cuboidal/columnar epithelium** that **lines** the ventricular
cavity. The **lateral ventricles** (here) are the **cavities
themselves** — the spaces **bounded** by the ependyma. **The
ependyma is the wall; the ventricle is the lumen.** Consumers
must **not** conflate the lateral ventricles with the ependyma —
the **ventricle** is the **cavity**; the **ependyma** is the
**lining**.
**Boundary status (NOT the CSF — the CSF is the FLUID CONTENT):**
**Boundary case — the lateral ventricles are NOT the
cerebrospinal fluid.** The **CSF** is the **fluid** that **fills**
the ventricles and the subarachnoid space. The **lateral
ventricles** (here) are the **cavities** — the **containers** of
the CSF. **The CSF is the content; the ventricle is the
container.** Consumers must **not** conflate the lateral
ventricles with the CSF — the **ventricle** is the **space**; the
**CSF** is the **fluid within it**.
**Boundary status (NOT the subarachnoid space — the subarachnoid
space is EXTERNAL):** **Boundary case — the lateral ventricles
are NOT the subarachnoid space.** The **subarachnoid space** is
the **external** CSF space between the arachnoid and pia mater,
surrounding the brain. The **lateral ventricles** (here) are the
**internal** CSF spaces **within** the cerebral hemispheres.
**They are DIFFERENT CSF compartments** — the **ventricles** are
**internal**; the **subarachnoid space** is **external**. Consumers
must **not** conflate the lateral ventricles with the
subarachnoid space.
**Boundary status (NOT the septum pellucidum — the septum
pellucidum SEPARATES the two ventricles):** **Boundary case —
the lateral ventricles are NOT the septum pellucidum.** The
**septum pellucidum** is the **thin midline membrane** that
**separates** the **left and right lateral ventricles**
anteriorly. The **lateral ventricles** (here) are the **paired
cavities on either side of the septum**. **The septum is the
partition; the ventricles are the spaces it separates.**
Consumers must **not** conflate the lateral ventricles with the
septum pellucidum.
**Boundary status (NOT the fornix — the fornix runs along the
FLOOR / MEDIAL WALL):** **Boundary case — the lateral ventricles
are NOT the fornix.** The **fornix** is the **white-matter
bundle** that runs along the **floor and medial wall** of the
lateral ventricles (and is documented in
``.../white_matter/fornix/``). The **lateral ventricles** (here)
are the **cavities** adjacent to the fornix. **The fornix is a
white-matter tract; the ventricle is the fluid space beside it.**
Consumers must **not** conflate the lateral ventricles with the
fornix.
**Boundary status (NOT the caudate nucleus — the caudate forms
the LATERAL WALL of the lateral ventricle):** **Boundary case —
the lateral ventricles are NOT the caudate nucleus.** The
**caudate nucleus** (``.../subcortical/basal_ganglia/striatum/
dorsal_striatum/caudate_nucleus/``) is the **grey-matter
structure** whose **head** bulges into the **anterior horn** of
the lateral ventricle (the **caudate impression**). The **lateral
ventricles** (here) are the **cavities** adjacent to the caudate.
**The caudate is grey matter; the ventricle is the fluid space it
borders.** Consumers must **not** conflate the lateral ventricles
with the caudate nucleus.
**Boundary status (NOT the subventricular zone — the SVZ is the
NEUROGENIC NICHE lining the ventricles):** **Boundary case — the
lateral ventricles are NOT the subventricular zone (SVZ).** The
**SVZ** is the **neurogenic niche** (a residual germinal layer)
that **lines** the lateral ventricles in the adult brain and
gives rise to **olfactory bulb interneurons** (via the rostral
migratory stream). The **lateral ventricles** (here) are the
**cavities** that the SVZ lines. **The SVZ is a neurogenic tissue;
the ventricle is the fluid space it borders.** The SVZ is
documented as **prose** (not a structural child of the ventricle).
Consumers must **not** conflate the lateral ventricles with the
SVZ.
**Boundary status (NOT a neural-processing structure — the
ventricles are FLUID SPACES, not processors):** **Boundary case —
the lateral ventricles are NOT a neural-processing structure.**
They do **not** compute, **modulate**, or **transmit** neural
signals in the classical sense. They are **fluid-filled
cavities** that **house the choroid plexus**, **contain CSF**,
and **provide a neurogenic niche (SVZ) and a volume-transmission
channel**. Consumers must **not** treat the lateral ventricles as
a **grey-matter or white-matter processing structure** — they are
**ventricular spaces**.

Overview
--------
The lateral ventricles are the **paired CSF-filled cavities** of
the **telencephalon** — one in each cerebral hemisphere, C-shaped,
the **largest** of the **ventricular system**. They are a
**container module** with two **mirrored leaf children**
(``left/`` and ``right/``).

**The lateral ventricles are the CAVITIES, not the tissue.** The
**cerebral hemispheres** (``.../cerebral_hemispheres/``) are the
neural tissue; the **lateral ventricles** (here) are the fluid
spaces *within* the hemispheres. The **choroid plexus** (the
CSF-producing tissue) and the **ependyma** (the lining) are
**inside** the ventricles — **tissues within the cavity**, not the
cavity itself.

**The lateral ventricles are TELENCEPHALIC, not diencephalic or
metencephalic.** They are **distinct** from the **third
ventricle** (``.../diencephalon/third_ventricle/``) and the
**fourth ventricle** (``.../hindbrain/metencephalon/
fourth_ventricle/``). They connect to the third ventricle via the
**interventricular foramen (foramen of Monro)** — a **connection**,
not an identity.

**The lateral ventricles are a paired structure.** Each hemisphere
has its own lateral ventricle, separated anteriorly by the
**septum pellucidum**. The two are **bilaterally symmetric** in
their basic anatomy, with **normal asymmetry** (the **left** is
often slightly larger than the right — "normal ventricular
asymmetry"). See *Lateralization Notes*.

**The lateral ventricles are NOT a neural processor.** They are
**fluid spaces** — CSF production (choroid plexus), CSF
circulation, buoyancy, metabolic waste clearance, **volume
transmission**, and the **SVZ neurogenic niche**. The **processing**
happens in the **cerebral hemispheres** (cortex, basal ganglia,
hippocampus, amygdala) that **surround** the ventricles.

Ventricular Composition (prose, not structural children)
--------------------------------------------------------
Each lateral ventricle is a **C-shaped cavity** with **five
prose-defined regions** — documented as **prose**, not as
structural children:

*   **Anterior horn (frontal horn)** — anterior to the **foramen
    of Monro**, bordered laterally by the **head of the caudate
    nucleus**, medially by the **septum pellucidum**, and rostrally
    by the **genu of the corpus callosum**.

*   **Body** — the central portion, from the **foramen of Monro**
    to the **atrium/trigone**, bordered laterally by the **body of
    the caudate** and the **thalamus** (the **thalamostriate
    groove** separates them), medially by the **septum pellucidum**
    and the **fornix**, and roofed by the **corpus callosum**.
    Contains the **choroid plexus** (the **body** portion).

*   **Atrium / trigone** — the **junction** of the body, posterior
    horn, and inferior horn, containing the **choroid plexus**
    (the **atrial** portion) and the **glomus** (the **choroid
    plexus enlargement**).

*   **Posterior horn (occipital horn)** — posterior extension into
    the occipital lobe, bordered by the **forceps major** (the
    **posterior radiation of the corpus callosum**) and the
    **calcarine sulcus** (the **calcar avis** impression).

*   **Inferior horn (temporal horn)** — the **largest** horn,
    curving anteriorly into the **temporal lobe**, bordered by the
    **hippocampus** (medially), the **collateral eminence** (the
    **hippocampal fissure** impression), and the **tapetum** of the
    corpus callosum (laterally). Contains the **choroid plexus**
    (the **temporal** portion).

**These regions are prose, not structural children.** The tree
wires the **lateral ventricles** as a **container** with **two
mirrored leaves** (``left/`` and ``right/``) — the **horns**,
**body**, **atrium**, **choroid plexus**, and **ependyma** are
**prose**, not structural children. Consumers that need
**horn-level** resolution should consult the references, not the
tree.

The Lateral Ventricles / Cerebral Hemispheres Boundary
------------------------------------------------------
This is the **cavity-vs-tissue** boundary:

*   **Lateral ventricles** (this module) — the **paired
    CSF-filled cavities** *within* the hemispheres.

*   **Cerebral hemispheres** (``.../cerebral_hemispheres/``) —
    the **neural tissue** (cortex, white matter, basal ganglia,
    hippocampus, amygdala).

**The ventricles are the cavities; the hemispheres are the tissue
that surrounds them.** Consumers must **not** conflate the two —
the **cerebral hemispheres** are the **neural parenchyma**; the
**lateral ventricles** are the **CSF spaces**.

The Lateral Ventricles / Third Ventricle Boundary
-------------------------------------------------
This is the **telencephalic-vs-diencephalic** boundary:

*   **Lateral ventricles** (this module) — the **telencephalic**
    paired CSF cavities.

*   **Third ventricle** (``.../diencephalon/third_ventricle/``) —
    the **diencephalic** midline CSF cavity.

**They are DIFFERENT VENTRICLES in DIFFERENT developmental
compartments**, connected via the **foramen of Monro**. Consumers
must **not** conflate the lateral ventricles with the third
ventricle — the **foramen of Monro** is a **connection**, not an
identity.

The Lateral Ventricles / Fourth Ventricle Boundary
--------------------------------------------------
This is the **telencephalic-vs-metencephalic** boundary:

*   **Lateral ventricles** (this module) — the **telencephalic**
    paired CSF cavities.

*   **Fourth ventricle** (``.../hindbrain/metencephalon/
    fourth_ventricle/``) — the **metencephalic** midline CSF
    cavity.

**They are DIFFERENT VENTRICLES in DIFFERENT developmental
compartments**, connected only indirectly (via the **third
ventricle** and the **mesencephalic aqueduct**). Consumers must
**not** conflate the lateral ventricles with the fourth ventricle.

The Lateral Ventricles / Choroid Plexus Boundary
------------------------------------------------
This is the **cavity-vs-CSF-producing-tissue** boundary:

*   **Lateral ventricles** (this module) — the **cavities**.

*   **Choroid plexus** — the **CSF-producing epithelial tissue**
    *inside* the ventricles (prose).

**The choroid plexus is a tissue within the ventricle; the ventricle
is the fluid space that contains it.** Consumers must **not**
conflate the lateral ventricles with the choroid plexus — the
**ventricle** is the **cavity**; the **choroid plexus** is the
**CSF-producing tissue within it**.

The Lateral Ventricles / Ependyma Boundary
------------------------------------------
This is the **cavity-vs-lining** boundary:

*   **Lateral ventricles** (this module) — the **cavities**.

*   **Ependyma** — the **ciliated simple cuboidal/columnar
    epithelium** that **lines** the cavities (prose).

**The ependyma is the wall; the ventricle is the lumen.** Consumers
must **not** conflate the lateral ventricles with the ependyma.

The Lateral Ventricles / CSF Boundary
-------------------------------------
This is the **container-vs-content** boundary:

*   **Lateral ventricles** (this module) — the **cavities**.

*   **CSF** — the **fluid** that **fills** the ventricles (and the
    subarachnoid space).

**The CSF is the content; the ventricle is the container.**
Consumers must **not** conflate the lateral ventricles with the
CSF.

The Lateral Ventricles / Subarachnoid Space Boundary
----------------------------------------------------
This is the **internal-vs-external CSF** boundary:

*   **Lateral ventricles** (this module) — the **internal** CSF
    spaces *within* the cerebral hemispheres.

*   **Subarachnoid space** — the **external** CSF space between
    the arachnoid and pia mater.

**They are DIFFERENT CSF compartments** — the **ventricles** are
**internal**; the **subarachnoid space** is **external**.
Consumers must **not** conflate the lateral ventricles with the
subarachnoid space.

The Lateral Ventricles / Fornix Boundary
----------------------------------------
This is the **cavity-vs-white-matter-tract** boundary:

*   **Lateral ventricles** (this module) — the **cavities**.

*   **Fornix** (``.../white_matter/fornix/``) — the
    **white-matter bundle** running along the **floor and medial
    wall** of the lateral ventricles.

**The fornix is a white-matter tract; the ventricle is the fluid
space beside it.** Consumers must **not** conflate the lateral
ventricles with the fornix.

The Lateral Ventricles / Caudate Nucleus Boundary
-------------------------------------------------
This is the **cavity-vs-grey-matter** boundary:

*   **Lateral ventricles** (this module) — the **cavities**.

*   **Caudate nucleus** (``.../subcortical/basal_ganglia/
    striatum/dorsal_striatum/caudate_nucleus/``) — the
    **grey-matter structure** whose **head** bulges into the
    **anterior horn**.

**The caudate is grey matter; the ventricle is the fluid space it
borders.** Consumers must **not** conflate the lateral ventricles
with the caudate nucleus.

The Lateral Ventricles / Subventricular Zone Boundary
-----------------------------------------------------
This is the **cavity-vs-neurogenic-niche** boundary:

*   **Lateral ventricles** (this module) — the **cavities**.

*   **Subventricular zone (SVZ)** — the **neurogenic niche**
    (residual germinal layer) that **lines** the lateral ventricles
    in the adult brain.

**The SVZ is a neurogenic tissue; the ventricle is the fluid space
it borders.** The SVZ is **prose**, not a structural child.
Consumers must **not** conflate the lateral ventricles with the
SVZ.

Function in the Human Brain
---------------------------
The lateral ventricles' functions are **CSF production, CSF
circulation, buoyancy, waste clearance, volume transmission, and
neurogenic niche** — **NOT neural processing**:

*   **CSF Production (Choroid Plexus):** The **choroid plexus**
    (in the body, atrium, and inferior horn of each lateral
    ventricle) **produces** the majority of the **cerebrospinal
    fluid** — the **fluid** that **fills** the ventricular system
    and the subarachnoid space.

*   **CSF Circulation:** The lateral ventricles are the **first**
    chamber in the **CSF flow path** — lateral ventricles →
    **foramen of Monro** → third ventricle → **mesencephalic
    aqueduct** → fourth ventricle → **foramina of Luschka and
    Magendie** → subarachnoid space → **arachnoid granulations** →
    dural venous sinuses.

*   **Buoyancy and Cushioning:** The CSF-filled ventricles
    **reduce the effective weight** of the brain (from ~1400 g to
    ~50 g) and **cushion** it against mechanical trauma.

*   **Metabolic Waste Clearance (Glymphatic System):** The CSF
    **clears** metabolic waste (including **amyloid-β**) from the
    brain via the **glymphatic system** — the ventricles are a
    **key compartment** in this clearance pathway.

*   **Volume Transmission:** The CSF is a **volume-transmission
    channel** — neuroactive substances (hormones, neuromodulators,
    cytokines) can **diffuse** through the CSF to reach **distant
    targets**. The lateral ventricles are a **CSF compartment** in
    this signaling pathway.

*   **Neurogenic Niche (SVZ):** The **subventricular zone (SVZ)**
    — the **residual germinal layer** lining the lateral
    ventricles — is a **major adult neurogenic niche** (giving
    rise to **olfactory bulb interneurons** via the **rostral
    migratory stream**). The **ventricle** is the **cavity that
    the SVZ lines**.

*   **NOT a neural processor.** The lateral ventricles do **not**
    compute, **modulate**, or **transmit** neural signals in the
    classical sense. The **processing** happens in the **cerebral
    hemispheres** (cortex, basal ganglia, hippocampus, amygdala)
    that **surround** the ventricles.

**The unifying theme:** the lateral ventricles are the **paired
telencephalic CSF cavities** — the **fluid spaces** that **produce
and circulate CSF**, **cushion the brain**, **clear metabolic
waste**, **support volume transmission**, and **host the SVZ
neurogenic niche**. They are **cavities**, **NOT neural tissue**,
and **NOT a processing structure**.

Associated Disorders
--------------------
The lateral ventricles have **no single named clinical syndrome**
— their clinical associations are **direct** (as the **CSF
compartment**) or **indirect** (as a **radiological marker**):

*   **Hydrocephalus (Direct — the Ventricles):** **Enlargement**
    of the lateral ventricles due to **CSF accumulation** —
    **obstructive** (e.g., **foramen of Monro** obstruction,
    **aqueductal stenosis**) or **communicating** (impaired CSF
    absorption at the **arachnoid granulations**). The lateral
    ventricles are the **primary radiological compartment** for
    hydrocephalus.

*   **Intraventricular Hemorrhage (Direct — the Ventricles):**
    **Bleeding into the lateral ventricles** — most commonly in
    **premature infants** (germinal matrix hemorrhage) and in
    **adults** (hypertensive hemorrhage with intraventricular
    extension, or **aneurysm rupture**).

*   **Choroid Plexus Tumors (Direct — the Ventricles):** **Choroid
    plexus papilloma** and **carcinoma** — tumors **arising from
    the choroid plexus** *within* the lateral ventricles (most
    commonly in the **atrium/trigone** in adults).

*   **Colloid Cyst (Direct — the Ventricles):** A **benign cyst**
    typically at the **foramen of Monro** — it can **obstruct**
    CSF flow and cause **hydrocephalus**.

*   **Meningitis / Ventriculitis (Direct — the Ventricles):**
    **Infection** of the CSF — the lateral ventricles are a
    **CSF compartment** that can be **infected** (ventriculitis),
    especially in **neonates** and **immunocompromised** patients.

*   **Normal Pressure Hydrocephalus (Direct — the Ventricles):**
    **Ventricular enlargement** with **normal CSF pressure** —
    a **reversible cause of dementia** (the **Hakim-Adams
    triad**: gait disturbance, urinary incontinence, cognitive
    decline). The lateral ventricles are the **radiological
    marker**.

*   **Alzheimer's Disease (Indirect — Ventricular Enlargement):**
    **Ventricular enlargement** *ex vacuo* (due to **brain
    atrophy**) is a **radiological marker** of
    **neurodegeneration** — the lateral ventricles are an
    **indirect** index of **hippocampal and cortical atrophy**.

*   **Schizophrenia (Indirect — Ventricular Enlargement):**
    **Ventricular enlargement** is a **replicated** (but
    **contested** in its specificity) **radiological finding** in
    **schizophrenia** — the lateral ventricles are an **indirect**
    index of **neurodevelopmental abnormality**.

*   **No Named "Lateral Ventricle Syndrome":** The lateral
    ventricles are a **paired cavity system**, not a **single
    structure** — they have **no named clinical syndrome**. Their
    clinical relevance is **direct** (as the **CSF compartment**)
    and **indirect** (as a **radiological marker**).

**What is NOT here:** The lateral ventricles are **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's disease**
(substantia nigra). Their clinical relevance is **ventricular CSF
pathology** and **radiological markers** — **no named lateral
ventricle syndrome exists**.

Lateralization Notes
--------------------
This is the **lateral_ventricles** container module. The lateral
ventricles are **bilaterally symmetric** and **partially
asymmetric** — and they carry **NO warning**:

*   **Bilateral Symmetry:** Each hemisphere has its own lateral
    ventricle, separated anteriorly by the **septum pellucidum**.
    The two sides are **structurally symmetric** — same horns,
    same body, same atrium, same choroid plexus.

*   **Normal Asymmetry (Left Often Larger):** The **left** lateral
    ventricle is **often slightly larger** than the right in
    healthy adults — **normal ventricular asymmetry**, documented
    in the **radiology literature** (not at the container level).

*   **NO Extended-Amygdala Warning (SLEA-free):** The lateral
    ventricles are **NOT** an extended-amygdala component. They
    carry **no SLEA warning**. Consumers must **not** import the
    SLEA warning into the lateral ventricles.

*   **NO Amygdala-Lateralization Warning:** The lateral ventricles
    are **NOT** the fear-output or the fear-learning structure.
    They are **CSF cavities** — consumers must **not** conflate
    them with the **amygdala** or the **fear circuit**. The
    **lateral ventricles** are **CSF spaces**, not the **fear
    circuit**.

**A consumer that assumes "left lateral ventricle = right lateral
ventricle" will be structurally correct** — the two sides are
**symmetric** and **partially asymmetric** (the asymmetry is
documented in the radiology literature). The lateral ventricles
are a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **container** does
    **not** import from ``left/`` or ``right/`` — it is a
    **namespace container**.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cerebral_hemispheres/``, ``.../commissures/``,
    ``.../diencephalon/third_ventricle/``,
    ``.../hindbrain/metencephalon/fourth_ventricle/``,
    ``.../midbrain/mesencephalic_aqueduct/``,
    ``.../white_matter/fornix/``,
    ``.../subcortical/basal_ganglia/striatum/dorsal_striatum/
    caudate_nucleus/``, or any other container. The lateral
    ventricles' relationships to the cerebral hemispheres, third
    ventricle, fourth ventricle, aqueduct, choroid plexus,
    ependyma, CSF, subarachnoid space, septum pellucidum, fornix,
    caudate nucleus, and SVZ are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — two structural children.** The
    ``left/`` and ``right/`` are **mirrored leaves**. The
    **horns** (anterior, posterior, inferior), the **body**, the
    **atrium/trigone**, the **choroid plexus**, the **ependyma**,
    and the **foramina of Monro** are **prose**, not structural
    children. Consumers must not assume any exist as children;
    resolve horn-level detail through the references.
*   **CAVITIES — NOT neural tissue.** The lateral ventricles are
    the **CSF spaces**; the **cerebral hemispheres** are the
    **neural tissue**. Consumers must **not** conflate the two.
*   **NOT the choroid plexus — the choroid plexus is the
    CSF-PRODUCING TISSUE inside the ventricles.** The ventricle is
    the **cavity**; the choroid plexus is the **tissue within it**.
*   **NOT the ependyma — the ependyma is the LINING.** The
    ventricle is the **cavity**; the ependyma is the **wall**.
*   **NOT the CSF — the CSF is the FLUID CONTENT.** The ventricle
    is the **container**; the CSF is the **content**.
*   **NOT the third or fourth ventricle — those are DIFFERENT
    developmental compartments.** The lateral ventricles are
    **telencephalic**; the third is **diencephalic**; the fourth
    is **metencephalic**.
*   **NOT a neural-processing structure.** The lateral ventricles
    are **fluid spaces** — they **produce and circulate CSF**,
    **cushion the brain**, **clear waste**, **support volume
    transmission**, and **host the SVZ neurogenic niche**. They do
    **not** compute, **modulate**, or **transmit** neural signals.
*   **SLEA-FREE — no extended-amygdala relationship.** The lateral
    ventricles are **not** an extended-amygdala component, and
    they carry **no SLEA warning**.
*   **NO ``AREA_PATHS`` hop.** The lateral ventricles are a local
    container under the telencephalon, not a cross-listed
    container.
*   **No nested cross-listing.** The lateral ventricles have no
    nested dual-framing module. They are a single container with
    two mirrored leaves.
*   **Structural parity with the right/left leaves — strict mirror
    with NO warning.** The ``left/`` and ``right/`` leaf modules
    are **structurally identical** — same leaf status, same
    **cavity** framing, same **SLEA-free** status, same **no
    warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.lateral_ventricles import (
        left, right,
    )

Or by fully-qualified path string::

    path = (
        "telencephalon.lateral_ventricles"
    )
    left_path = (
        "telencephalon.lateral_ventricles.left"
    )
    right_path = (
        "telencephalon.lateral_ventricles.right"
    )

**Do not** assume the lateral ventricles are the **cerebral
hemispheres**. The **cerebral hemispheres** are the **neural
tissue**; the **lateral ventricles** are the **CSF cavities**
*within* the hemispheres.

**Do not** assume the lateral ventricles are the **choroid
plexus**. The **choroid plexus** is the **CSF-producing tissue
inside** the ventricles; the **ventricles** are the **cavities**
that contain it.

**Do not** assume the lateral ventricles are the **ependyma** or
the **CSF**. The **ependyma** is the **lining**; the **CSF** is
the **fluid content**; the **ventricles** are the **cavities**.

**Do not** assume the lateral ventricles are the **third
ventricle** or the **fourth ventricle**. The **third ventricle**
is **diencephalic**; the **fourth ventricle** is **metencephalic**;
the **lateral ventricles** are **telencephalic**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the lateral ventricles.
**The lateral ventricles are SLEA-FREE** — they are **not** an
extended-amygdala component, and they are **NOT the fear-output
structure**.

Iterating the lateral ventricles' children (recommended consumer
pattern)::

    LATERAL_VENTRICLE_CHILDREN = ("left", "right")
    # The left and right lateral ventricles are mirrored leaves.
    # The horns, body, atrium, choroid plexus, and ependyma are
    # prose, not modules.

Reaching the cerebral hemispheres (recommended consumer pattern —
NOTE the cavity-vs-tissue boundary)::

    # The cerebral hemispheres are the NEURAL TISSUE that
    # surrounds the ventricles:
    #
    #   telencephalon.cerebral_hemispheres.left
    #   telencephalon.cerebral_hemispheres.right
    #
    # The lateral ventricles are the CAVITIES within those
    # hemispheres.

Reaching the third ventricle (recommended consumer pattern — NOTE
the telencephalic-vs-diencephalic boundary)::

    # The third ventricle is the DIENCEPHALIC midline CSF cavity:
    #
    #   telencephalon.diencephalon.third_ventricle
    #
    # The lateral ventricles connect to it via the foramen of
    # Monro — a connection, not an identity.

Reaching the fourth ventricle (recommended consumer pattern — NOTE
the telencephalic-vs-metencephalic boundary)::

    # The fourth ventricle is the METENCEPHALIC midline CSF cavity:
    #
    #   telencephalon.hindbrain.metencephalon.fourth_ventricle
    #
    # The lateral ventricles connect to it only indirectly (via
    # the third ventricle and the mesencephalic aqueduct).

Reaching the choroid plexus (recommended consumer pattern — NOTE
the cavity-vs-tissue boundary)::

    # The choroid plexus is the CSF-PRODUCING TISSUE inside the
    # lateral ventricles (prose — not a structural child):
    #
    #   (prose) lateral_ventricles.<left|right> — choroid plexus
    #   in the body, atrium, and inferior horn.
    #
    # The ventricle is the CAVITY; the choroid plexus is the
    # TISSUE WITHIN IT.

Reaching the fornix (recommended consumer pattern — NOTE the
cavity-vs-white-matter boundary)::

    # The fornix is the WHITE-MATTER BUNDLE along the floor and
    # medial wall of the lateral ventricles:
    #
    #   telencephalon.cerebral_hemispheres.<left|right>.
    #   white_matter.fornix
    #
    # The fornix is a white-matter tract; the ventricle is the
    # fluid space beside it.

Reaching the caudate nucleus (recommended consumer pattern — NOTE
the cavity-vs-grey-matter boundary)::

    # The caudate nucleus is the GREY-MATTER STRUCTURE whose head
    # bulges into the anterior horn of the lateral ventricle:
    #
    #   telencephalon.cerebral_hemispheres.<left|right>.
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.
    #   caudate_nucleus
    #
    # The caudate is grey matter; the ventricle is the fluid space
    # it borders.

Subventricular-zone detail (not wired — consult references)::

    # The SVZ is the neurogenic niche lining the lateral
    # ventricles (prose, not a structural child):
    #   SVZ -> adult neurogenesis -> rostral migratory stream ->
    #   olfactory bulb interneurons
    #
    # Do not attempt to resolve the SVZ as a sub-path of the
    # lateral ventricles.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        lv_path = (
            f"telencephalon.lateral_ventricles.{side}"
        )
        # resolve lv_path through the memory/recall layer

References
----------
*   **Canonical ventricular anatomy:** Standring, S. (ed.) (2020).
    *Gray's Anatomy: The Anatomical Basis of Clinical Practice*,
    42nd ed. (Lateral ventricles — horns, body, atrium, choroid
    plexus, ependyma.)
*   **Ventricular system overview:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Ventricular system — lateral, third, fourth ventricles;
    CSF flow.)
*   **CSF physiology and choroid plexus:** Damkier, H.H., Brown,
    P.D., Praetorius, J. (2013). "Cerebrospinal fluid secretion
    by the choroid plexus." *Physiological Reviews* 93:1847–1892.
    (Choroid plexus as the CSF-producing tissue within the
    ventricles.)
*   **Glymphatic system and CSF clearance:** Iliff, J.J., et al.
    (2012). "A paravascular pathway facilitates CSF flow through
    the brain parenchyma and the clearance of interstitial
    solutes, including amyloid β." *Science Translational
    Medicine* 4:147ra111. (CSF clearance — the ventricles as a
    key compartment.)
*   **Subventricular zone neurogenesis:** Lois, C., Alvarez-Buylla,
    A. (1994). "Long-distance neuronal migration in the adult
    mammalian brain." *Science* 264:1145–1148. (SVZ — the
    neurogenic niche lining the lateral ventricles; rostral
    migratory stream.)
*   **Normal ventricular asymmetry:** Zipursky, R.B., Lim, K.O.,
    Pfefferbaum, A. (1990). "Volumetric assessment of cerebral
    asymmetry from CT scans in manic and schizophrenic patients."
    *Psychiatry Research* 36:71–81. (Left-often-larger normal
    ventricular asymmetry.)
*   **Hydrocephalus:** Rekate, H.L. (2009). "A contemporary
    definition of hydrocephalus: is it time?" *Cerebrospinal
    Fluid Research* 6:5. (Hydrocephalus — ventricular
    enlargement due to CSF accumulation.)
*   **Intraventricular hemorrhage:** Volpe, J.J. (2008).
    "Intraventricular hemorrhage in the premature infant —
    current concepts." *Annals of Neurology* 25:3–11.
    (Germinal matrix / intraventricular hemorrhage in premature
    infants.)
*   **Choroid plexus tumors:** Wolff, J.E.A., et al. (2002).
    "Choroid plexus tumours." *British Journal of Cancer*
    87:1086–1091. (Choroid plexus papilloma and carcinoma within
    the lateral ventricles.)
*   **Colloid cyst:** Pollock, B.E., Schreiner, D. (2012). "Colloid
    cysts of the third ventricle." *Neurosurgery* 71:1–9.
    (Colloid cyst at the foramen of Monro — obstruction and
    hydrocephalus.)
*   **Normal pressure hydrocephalus:** Hakim, S., Adams, R.D.
    (1965). "The special clinical problem of symptomatic
    hydrocephalus with normal cerebrospinal fluid pressure."
    *Journal of the Neurological Sciences* 2:307–327. (The
    Hakim-Adams triad; ventricular enlargement with normal CSF
    pressure.)
*   **Ventricular enlargement in Alzheimer's disease:** Fox,
    N.C., et al. (2000). "Imaging of onset and progression of
    Alzheimer's disease with voxel-compression mapping of serial
    magnetic resonance images." *The Lancet* 358:201–205.
    (Ventricular enlargement *ex vacuo* as a marker of
    neurodegeneration.)
*   **Ventricular enlargement in schizophrenia:** Shenton, M.E.,
    et al. (2001). "A review of MRI findings in schizophrenia."
    *Schizophrenia Research* 49:1–52. (Ventricular enlargement in
    schizophrenia — replicated but contested in specificity.)
*   **SLEA (contrast — the lateral ventricles are NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral
    pallidum, nucleus accumbens; NOT the lateral ventricles.)
*   NeuroNames — Lateral ventricle; FMA — Lateral ventricle.
"""