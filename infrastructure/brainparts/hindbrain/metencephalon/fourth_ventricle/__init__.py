"""
infrastructure.brainparts.hindbrain.metencephalon.fourth_ventricle
==================================================================

Anatomical Hierarchy
--------------------
::

    metencephalon
    ├── cerebellum
    ├── fourth_ventricle                     <-- THIS MODULE
    │   └── median_aperture
    └── pons

**Primary synonym:** Fourth ventricle; ventriculus quartus;
ventricle IV; the fourth CSF cavity; the rhombencephalic
ventricle; the cerebellar ventricle; the ventricle of the
pons and medulla; the metencephalic–myelencephalic CSF cavity.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
grey-matter or white-matter structure.** A **midline
fluid-filled cavity** — the **rhombencephalic CSF space**
between the **pons/medulla** (ventrally) and the **cerebellum**
(dorsally), **lined by ependyma** and **containing choroid
plexus** (the **choroid plexus of the fourth ventricle** — the
**median aperture** — the **foramen of Magendie** and the two
**lateral apertures** — the **foramina of Luschka** — are its
**CSF outflow apertures**).
**Part of:** The **metencephalon** container — the **rostral**
of the two rhombencephalic sub-vesicles, **spanning** the
**metencephalon** (the pons/cerebellum level) and continuing
into the **myelencephalon** (the medulla oblongata level —
the caudal portion of the fourth ventricle is the **myelencephalic
floor**). The **metencephalon** is the **rostral** of the **two
rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../metencephalon/`` → **direct child**
of the metencephalon container.
**Structural children:** **One** — ``median_aperture/``. The
**median aperture (foramen of Magendie)** is the **midline
CSF outflow aperture** of the fourth ventricle — the **opening**
through which the CSF exits the fourth ventricle into the
**subarachnoid space** (the **cisterna magna**). The **two
lateral apertures (foramina of Luschka)** — the **lateral CSF
outflow apertures** — are documented as **prose** (not as
structural children). The **fourth-ventricle choroid plexus**,
the **fourth-ventricle ependyma**, the **fourth-ventricle CSF**,
the **superior medullary velum**, the **inferior medullary
velum**, the **facial colliculus**, the **vestibular area**, the
**hypoglossal trigone**, the **vagal trigone**, the **locus
coeruleus** (as a floor landmark), the **striae medullares**,
the **obex**, the **tela choroidea**, and the **recesses**
(lateral recesses, the **lateral recess** extending to the
foramina of Luschka) are documented as **prose**, not as
structural children.
**Boundary status (CSF CAVITY — NOT the pons or cerebellum):**
**Boundary case — the fourth ventricle is a CSF CAVITY, NOT the
pons or the cerebellum.** The **pons** (``.../metencephalon/
pons/``) is the **ventral brainstem structure**; the
**cerebellum** (``.../metencephalon/cerebellum/``) is the
**dorsal suprasegmental structure**. The **fourth ventricle**
(here) is the **CSF cavity** **between** them — the **fluid
space** that the pons and cerebellum **surround**. **The
ventricle is the CAVITY; the pons and cerebellum are the
NEURAL TISSUE that surrounds it.** Consumers must **not**
conflate the fourth ventricle with the pons or the cerebellum —
the **pons** and **cerebellum** are the **neural tissue**; the
**fourth ventricle** is the **CSF cavity** between them.
**Boundary status (RHOMBENCEPHALIC — NOT the third ventricle):**
**Boundary case — the fourth ventricle is the RHOMBENCEPHALIC
CSF cavity, NOT the third ventricle.** The **third ventricle**
(``.../forebrain/diencephalon/third_ventricle/``) is the
**diencephalic** CSF cavity between the thalami. The **fourth
ventricle** (here) is the **rhombencephalic** CSF cavity between
the pons/medulla and the cerebellum. **They are DIFFERENT
VENTRICLES in DIFFERENT developmental compartments** — the
**third ventricle** is **diencephalic**; the **fourth
ventricle** is **rhombencephalic**. They are **connected** via
the **mesencephalic aqueduct** (the **cerebral aqueduct** —
``.../midbrain/mesencephalic_aqueduct/``) — that aqueduct is a
**connection**, not an identity. Consumers must **not** conflate
the fourth ventricle with the third ventricle.
**Boundary status (RHOMBENCEPHALIC — NOT the lateral
ventricles):** **Boundary case — the fourth ventricle is the
RHOMBENCEPHALIC CSF cavity, NOT the lateral ventricles.** The
**lateral ventricles**
(``.../forebrain/telencephalon/lateral_ventricles/``) are the
**telencephalic** paired CSF cavities. The **fourth ventricle**
(here) is the **rhombencephalic** CSF cavity. **They are
DIFFERENT VENTRICLES in DIFFERENT developmental compartments**
— the **lateral ventricles** are **telencephalic**; the
**fourth ventricle** is **rhombencephalic**. They are
**connected** only indirectly (via the **third ventricle** and
the **mesencephalic aqueduct**). Consumers must **not**
conflate the fourth ventricle with the lateral ventricles.
**Boundary status (RHOMBENCEPHALIC — NOT the mesencephalic
aqueduct):** **Boundary case — the fourth ventricle is the
RHOMBENCEPHALIC CSF cavity, NOT the mesencephalic aqueduct.**
The **mesencephalic aqueduct (cerebral aqueduct)**
(``.../midbrain/mesencephalic_aqueduct/``) is the **midbrain**
CSF channel connecting the **third ventricle** to the **fourth
ventricle**. The **fourth ventricle** (here) is the
**rhombencephalic** CSF cavity that the aqueduct **empties
into**. **They are DIFFERENT CSF spaces** — the **aqueduct**
is the **midbrain channel**; the **fourth ventricle** is the
**rhombencephalic cavity**. Consumers must **not** conflate the
fourth ventricle with the mesencephalic aqueduct.
**Boundary status (INTERNAL CSF — NOT the subarachnoid space):**
**Boundary case — the fourth ventricle is an INTERNAL CSF
space, NOT the subarachnoid space.** The **subarachnoid space**
is the **external** CSF space between the arachnoid and pia
mater (surrounding the brain). The **fourth ventricle** (here)
is the **internal** CSF space **within** the brainstem and
cerebellum. **They are DIFFERENT CSF compartments** — the
**fourth ventricle** is **internal**; the **subarachnoid
space** is **external**. They **communicate** via the **CSF
outflow apertures** (the **median aperture — the foramen of
Magendie** — and the **two lateral apertures — the foramina
of Luschka**) — those apertures are **connections**, not
identities. Consumers must **not** conflate the fourth
ventricle with the subarachnoid space.
**Boundary status (CAVITY — NOT the choroid plexus):** **Boundary
case — the fourth ventricle is the CAVITY, NOT the choroid
plexus.** The **choroid plexus** — the **CSF-producing
epithelial tissue** — is the **tissue within the fourth
ventricle** (the **choroid plexus of the fourth ventricle** —
a **midline** choroid plexus formed by the **tela choroidea**
and the **inferior medullary velum**). The **fourth ventricle**
(here) is the **cavity** that **contains** the choroid plexus.
**The choroid plexus is a tissue INSIDE the fourth ventricle;
the fourth ventricle is the fluid space.** Consumers must
**not** conflate the fourth ventricle with the choroid plexus
— the **ventricle** is the **cavity**; the **choroid plexus**
is the **CSF-producing tissue within it**.
**Boundary status (CAVITY — NOT the ependyma):** **Boundary
case — the fourth ventricle is the CAVITY, NOT the ependyma.**
The **ependyma** — the **ciliated simple cuboidal/columnar
epithelium** — is the **lining** of the fourth ventricle (and
of the entire ventricular system). The **fourth ventricle**
(here) is the **cavity** that the ependyma **lines**. **The
ependyma is the wall; the fourth ventricle is the lumen.**
Consumers must **not** conflate the fourth ventricle with the
ependyma.
**Boundary status (CONTAINER — NOT the CSF):** **Boundary case
— the fourth ventricle is the CONTAINER, NOT the CSF.** The
**CSF** — the **fluid** — **fills** the fourth ventricle (and
the entire ventricular system and the subarachnoid space). The
**fourth ventricle** (here) is the **cavity** — the
**container** of the CSF. **The CSF is the content; the fourth
ventricle is the container.** Consumers must **not** conflate
the fourth ventricle with the CSF.
**Boundary status (CAVITY — NOT the superior or inferior
medullary velum):** **Boundary case — the fourth ventricle is
the CAVITY, NOT the superior or inferior medullary velum.**
The **superior medullary velum** and the **inferior medullary
velum** are the **thin white-matter laminae** that **form the
roof** of the fourth ventricle. The **fourth ventricle** (here)
is the **cavity** beneath that roof. **The vela are the ROOF of
the fourth ventricle; the fourth ventricle is the cavity they
roof.** Consumers must **not** conflate the fourth ventricle
with the medullary vela.
**Boundary status (CAVITY — NOT the facial colliculus or the
floor landmarks):** **Boundary case — the fourth ventricle is
the CAVITY, NOT the facial colliculus or the other floor
landmarks.** The **facial colliculus**, the **vestibular
area**, the **hypoglossal trigone**, the **vagal trigone**,
the **locus coeruleus** (floor landmark), the **striae
medullares**, and the **obex** are the **floor landmarks** of
the fourth ventricle — the **neural structures on the floor
of the fourth ventricle**. The **fourth ventricle** (here) is
the **cavity** above those floor structures. **The floor
landmarks are the FLOOR of the fourth ventricle; the fourth
ventricle is the cavity above them.** Consumers must **not**
conflate the fourth ventricle with its floor landmarks.
**Boundary status (CAVITY — NOT the tela choroidea):**
**Boundary case — the fourth ventricle is the CAVITY, NOT the
tela choroidea.** The **tela choroidea** is the **vascular
pia-mater fold** that **forms the choroid plexus of the
fourth ventricle** (the **CSF-producing tissue** within the
fourth ventricle). The **fourth ventricle** (here) is the
**cavity** that the tela choroidea (and the choroid plexus
formed from it) **is inside of**. Consumers must **not**
conflate the fourth ventricle with the tela choroidea.
**Boundary status (APERTURES — the MEDIAN APERTURE is a
STRUCTURAL CHILD; the LATERAL APERTURES are PROSE):**
**Boundary case — the median aperture (foramen of Magendie)
is a structural child of the fourth ventricle; the lateral
apertures (foramina of Luschka) are prose.** The **median
aperture**
(``.../fourth_ventricle/median_aperture/``) is the **midline
CSF outflow aperture** of the fourth ventricle — the
**opening** through which the CSF exits the fourth ventricle
into the **cisterna magna** (part of the subarachnoid space).
The **lateral apertures (foramina of Luschka)** — the two
**lateral CSF outflow apertures** — are documented as
**prose**, not as structural children. **The median aperture
is a structural child; the lateral apertures are prose.**
Consumers must **not** assume the lateral apertures exist as
structural children — they are **prose**.
**Boundary status (NOT the pons or cerebellum — the ventricle
is BETWEEN them):** **Boundary case — the fourth ventricle is
BETWEEN the pons and cerebellum (and between the medulla and
cerebellum), NOT the pons or the cerebellum.** The **pons**
(``.../metencephalon/pons/``) is the **ventral brainstem**
structure; the **cerebellum**
(``.../metencephalon/cerebellum/``) is the **dorsal
suprasegmental** structure; the **medulla oblongata**
(``.../hindbrain/myelencephalon/medulla_oblongata/``) is the
**caudal brainstem** structure. The **fourth ventricle**
(here) is the **CSF cavity** **between** the pons/medulla
(ventral wall) and the cerebellum (dorsal roof). Consumers
must **not** conflate the fourth ventricle with the pons or
the cerebellum — it is the **cavity between them**.
**Boundary status (NOT the myelencephalon — the fourth
ventricle SPANS metencephalon and myelencephalon):** **Boundary
case — the fourth ventricle SPANS the metencephalon and the
myelencephalon — it is NOT a metencephalon-only structure.**
The **metencephalon** (``.../metencephalon/``) contains the
**rostral portion** of the fourth ventricle (the **superior
portion** — between the pons and the cerebellum); the
**myelencephalon** (``.../hindbrain/myelencephalon/``) contains
the **caudal portion** of the fourth ventricle (the **inferior
portion** — between the medulla and the cerebellum). **The
fourth ventricle is a SHARED CSF cavity across the metencephalon
and myelencephalon.** The **tree wires the fourth ventricle as
a child of the metencephalon** (the **rostral portion**), but
the **fourth ventricle's caudal portion** extends into the
**myelencephalon**. Consumers must **not** treat the fourth
ventricle as exclusively a metencephalon structure — it is a
**shared rhombencephalic CSF cavity**.
**Boundary status (NOT a neural-processing structure — the
fourth ventricle is a CSF CAVITY, not a processor):** **Boundary
case — the fourth ventricle is NOT a neural-processing
structure.** It does **not** compute, **modulate**, or
**transmit** neural signals in the classical sense. It is a
**fluid-filled cavity** that **houses the choroid plexus**,
**contains CSF**, and **serves as a CSF conduit** in the CSF
flow path (from the third ventricle and the mesencephalic
aqueduct, through the fourth ventricle, to the subarachnoid
space via the median aperture and the lateral apertures).
Consumers must **not** treat the fourth ventricle as a
**grey-matter or white-matter processing structure** — it is a
**ventricular space**.
**Boundary status (SLEA-FREE — the fourth ventricle is NOT an
extended-amygdala component):** **Boundary case — the fourth
ventricle is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **fourth
ventricle** is a **CSF cavity** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into
the fourth ventricle — it is **SLEA-free**.

Overview
--------
The fourth ventricle is the **rhombencephalic CSF cavity** —
the **midline fluid-filled space** between the **pons/medulla**
(ventrally) and the **cerebellum** (dorsally), **lined by
ependyma** and **containing choroid plexus** (the **choroid
plexus of the fourth ventricle** — formed from the **tela
choroidea** and the **inferior medullary velum**), with the
**median aperture (foramen of Magendie)** and the **two lateral
apertures (foramina of Luschka)** as its **CSF outflow
apertures** into the **subarachnoid space**. It is a
**container module** with **one structural child**
(``median_aperture/``).

**The fourth ventricle is the CSF CAVITY, not the neural
tissue.** The **pons**, **medulla oblongata**, and
**cerebellum** are the **neural tissue** that **surrounds**
the fourth ventricle — the fourth ventricle is the **fluid
space** *between* them. **The ventricle is the cavity; the
pons, medulla, and cerebellum are the tissue.**

**The fourth ventricle is the RHOMBENCEPHALIC CSF cavity, distinct
from the third ventricle (diencephalic) and the lateral
ventricles (telencephalic).** The **third ventricle**
(``.../forebrain/diencephalon/third_ventricle/``) is
**diencephalic**; the **lateral ventricles**
(``.../forebrain/telencephalon/lateral_ventricles/``) are
**telencephalic**; the **fourth ventricle** (here) is
**rhombencephalic**. **They are DIFFERENT VENTRICLES in
DIFFERENT developmental compartments.**

**The fourth ventricle SPANS the metencephalon and the
myelencephalon.** The **metencephalon** contains the **rostral
portion** (between the pons and cerebellum); the
**myelencephalon** contains the **caudal portion** (between the
medulla and cerebellum). The **tree wires the fourth ventricle
as a child of the metencephalon** (the rostral portion), but
the **fourth ventricle is a shared rhombencephalic CSF cavity**.

**The fourth ventricle is the CSF conduit between the third
ventricle and the subarachnoid space.** The **CSF flow path** —
lateral ventricles → third ventricle (via the foramina of
Monro) → **mesencephalic aqueduct** → **fourth ventricle** →
**median aperture (Magendie)** and **lateral apertures
(Luschka)** → **subarachnoid space** → **arachnoid
granulations** → dural venous sinuses. The **fourth ventricle**
is a **key compartment** in this flow path.

**The fourth ventricle is NOT a neural processor.** It is a
**fluid space** — CSF production (choroid plexus within), CSF
circulation, buoyancy, metabolic waste clearance, and **volume
transmission**. The **processing** happens in the **pons**
(pontine nuclei, cranial nerve nuclei V–VIII), the **medulla
oblongata** (autonomic control, cranial nerve nuclei IX–XII),
and the **cerebellum** (motor coordination, motor learning,
cognition, vestibular control) that **surround** the fourth
ventricle.

Fourth-Ventricle Composition (sub-containers and prose)
-------------------------------------------------------
The fourth ventricle is a **CSF cavity** with **one structural
child** — documented as a **structural child**
(``median_aperture/``) — and **many prose-defined
sub-structures** documented as **prose**:

*   **Median aperture (foramen of Magendie)**
    (``.../fourth_ventricle/median_aperture/``) — the
    **midline CSF outflow aperture** of the fourth ventricle —
    the **opening** through which the CSF exits the fourth
    ventricle into the **cisterna magna** (part of the
    subarachnoid space). Documented as a **structural child**.

*   **Lateral apertures (foramina of Luschka)** — the two
    **lateral CSF outflow apertures** of the fourth ventricle —
    the **openings** at the **lateral recesses** of the
    fourth ventricle, through which the CSF exits into the
    **subarachnoid space** (the **cerebellopontine angle
    cistern**). Documented as **prose** — **NOT** a structural
    child.

*   **Superior medullary velum** — the **thin white-matter
    lamina** that **forms the rostral roof** of the fourth
    ventricle (between the cerebellum and the superior
    cerebellar peduncles). Documented as **prose**.

*   **Inferior medullary velum** — the **thin white-matter
    lamina** that **forms the caudal roof** of the fourth
    ventricle (between the cerebellum and the inferior
    cerebellar peduncles), **containing the tela choroidea**
    and the **choroid plexus of the fourth ventricle**.
    Documented as **prose**.

*   **Tela choroidea** — the **vascular pia-mater fold**
    that **forms the choroid plexus of the fourth ventricle**
    — documented as **prose**.

*   **Choroid plexus (of the fourth ventricle)** — the
    **CSF-producing epithelial tissue** within the fourth
    ventricle (formed from the **tela choroidea** and the
    **inferior medullary velum**) — documented as **prose**.

*   **Ependyma (of the fourth ventricle)** — the **ciliated
    simple cuboidal/columnar epithelium** that **lines** the
    fourth ventricle — documented as **prose**.

*   **CSF (of the fourth ventricle)** — the **fluid** that
    **fills** the fourth ventricle — documented as **prose**.

*   **Facial colliculus** — the **floor landmark** of the
    fourth ventricle over the **abducens nucleus** and the
    **facial nerve fibers** (the **internal genu of the facial
    nerve**) — documented as **prose**.

*   **Vestibular area** — the **floor landmark** of the fourth
    ventricle over the **vestibular nuclei** — documented as
    **prose**.

*   **Hypoglossal trigone** — the **floor landmark** of the
    fourth ventricle over the **hypoglossal nucleus** —
    documented as **prose**.

*   **Vagal trigone** — the **floor landmark** of the fourth
    ventricle over the **dorsal motor nucleus of the vagus**
    — documented as **prose**.

*   **Striae medullares** — the **floor landmark** of the
    fourth ventricle (the **medullary striae** — the
    **auditory pathway fibers** crossing the floor) —
    documented as **prose**.

*   **Obex** — the **caudal-most portion** of the fourth
    ventricle floor (the **point** where the fourth ventricle
    narrows into the **central canal of the medulla**) —
    documented as **prose**.

*   **Lateral recesses** — the **lateral extensions** of the
    fourth ventricle (the **recesses** that **lead to the
    lateral apertures — the foramina of Luschka**) —
    documented as **prose**.

*   **Locus coeruleus (floor landmark)** — the **noradrenergic
    nucleus** visible as a **floor landmark** on the fourth
    ventricle (in the rostral floor) — documented as **prose**
    (the **locus coeruleus** is a **pons structure** —
    ``.../metencephalon/pons/tegmentum/locus_coeruleus/``
    — visible through the fourth-ventricle floor).

**These sub-structures are prose (or the one structural child),
not direct structural children of the fourth ventricle.** The
tree wires the **fourth ventricle** as a **container** with
**one structural child** (``median_aperture/``) — the
**lateral apertures**, the **superior and inferior medullary
vela**, the **tela choroidea**, the **choroid plexus**, the
**ependyma**, the **CSF**, the **floor landmarks**, the
**obex**, and the **lateral recesses** are **prose**, not
structural children. Consumers that need **aperture-level** or
**floor-landmark-level** resolution should consult the
references, not the fourth ventricle container.

The Fourth Ventricle / Pons Boundary
------------------------------------
This is the **CSF-cavity-vs-ventral-brainstem** boundary:

*   **Fourth ventricle** (this module) — the **CSF cavity**.

*   **Pons** (``.../metencephalon/pons/``) — the **ventral
    brainstem** structure (basis pontis, pontine tegmentum,
    cranial nerve nuclei V–VIII, etc.).

**The pons is the VENTRAL WALL of the fourth ventricle; the
fourth ventricle is the cavity dorsal to the pons.** Consumers
must **not** conflate the fourth ventricle with the pons — the
**pons** is the **neural tissue**; the **fourth ventricle** is
the **CSF cavity**.

The Fourth Ventricle / Cerebellum Boundary
------------------------------------------
This is the **CSF-cavity-vs-dorsal-suprasegmental** boundary:

*   **Fourth ventricle** (this module) — the **CSF cavity**.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **dorsal suprasegmental** structure.

**The cerebellum is the DORSAL ROOF of the fourth ventricle (via
the superior and inferior medullary vela); the fourth ventricle
is the cavity ventral to the cerebellum.** Consumers must **not**
conflate the fourth ventricle with the cerebellum — the
**cerebellum** is the **neural tissue**; the **fourth
ventricle** is the **CSF cavity**.

The Fourth Ventricle / Medulla Oblongata Boundary
-------------------------------------------------
This is the **CSF-cavity-vs-caudal-brainstem** boundary:

*   **Fourth ventricle** (this module) — the **CSF cavity**
    (extending caudally into the **myelencephalon**).

*   **Medulla oblongata**
    (``.../hindbrain/myelencephalon/medulla_oblongata/``) —
    the **caudal brainstem** structure.

**The medulla oblongata is the VENTRAL WALL of the caudal
portion of the fourth ventricle; the fourth ventricle is the
cavity dorsal to the medulla.** Consumers must **not** conflate
the fourth ventricle with the medulla oblongata — the
**medulla** is the **neural tissue**; the **fourth ventricle**
is the **CSF cavity**.

The Fourth Ventricle / Third Ventricle Boundary
-----------------------------------------------
This is the **rhombencephalic-vs-diencephalic** boundary:

*   **Fourth ventricle** (this module) — the **rhombencephalic**
    CSF cavity.

*   **Third ventricle**
    (``.../forebrain/diencephalon/third_ventricle/``) — the
    **diencephalic** CSF cavity.

**They are DIFFERENT VENTRICLES in DIFFERENT developmental
compartments**, connected via the **mesencephalic aqueduct**.
Consumers must **not** conflate the fourth ventricle with the
third ventricle — the **aqueduct** is a **connection**, not an
identity.

The Fourth Ventricle / Lateral Ventricles Boundary
--------------------------------------------------
This is the **rhombencephalic-vs-telencephalic** boundary:

*   **Fourth ventricle** (this module) — the **rhombencephalic**
    CSF cavity.

*   **Lateral ventricles**
    (``.../forebrain/telencephalon/lateral_ventricles/``) —
    the **telencephalic** paired CSF cavities.

**They are DIFFERENT VENTRICLES in DIFFERENT developmental
compartments**, connected only indirectly (via the **third
ventricle** and the **mesencephalic aqueduct**). Consumers must
**not** conflate the fourth ventricle with the lateral
ventricles.

The Fourth Ventricle / Mesencephalic Aqueduct Boundary
------------------------------------------------------
This is the **rhombencephalic-cavity-vs-midbrain-channel**
boundary:

*   **Fourth ventricle** (this module) — the **rhombencephalic**
    CSF cavity.

*   **Mesencephalic aqueduct (cerebral aqueduct)**
    (``.../midbrain/mesencephalic_aqueduct/``) — the
    **midbrain** CSF channel connecting the third ventricle
    to the fourth ventricle.

**They are DIFFERENT CSF spaces** — the **aqueduct** is the
**midbrain channel**; the **fourth ventricle** is the
**rhombencephalic cavity** that the aqueduct **empties into**.
Consumers must **not** conflate the fourth ventricle with the
mesencephalic aqueduct.

The Fourth Ventricle / Subarachnoid Space Boundary
--------------------------------------------------
This is the **internal-vs-external CSF** boundary:

*   **Fourth ventricle** (this module) — the **internal** CSF
    space *within* the brainstem and cerebellum.

*   **Subarachnoid space** — the **external** CSF space
    between the arachnoid and pia mater.

**They are DIFFERENT CSF compartments** — the **fourth
ventricle** is **internal**; the **subarachnoid space** is
**external**. They **communicate** via the **median aperture**
and the **lateral apertures** — those apertures are
**connections**, not identities. Consumers must **not** conflate
the fourth ventricle with the subarachnoid space.

The Fourth Ventricle / Choroid Plexus Boundary
----------------------------------------------
This is the **cavity-vs-CSF-producing-tissue** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **Choroid plexus (of the fourth ventricle)** — the
    **CSF-producing epithelial tissue** within the ventricle
    (prose).

**The choroid plexus is a tissue within the fourth ventricle;
the fourth ventricle is the fluid space that contains it.**
Consumers must **not** conflate the fourth ventricle with the
choroid plexus.

The Fourth Ventricle / Ependyma Boundary
----------------------------------------
This is the **cavity-vs-lining** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **Ependyma** — the **ciliated simple cuboidal/columnar
    epithelium** that **lines** the cavity (prose).

**The ependyma is the wall; the fourth ventricle is the lumen.**
Consumers must **not** conflate the fourth ventricle with the
ependyma.

The Fourth Ventricle / CSF Boundary
-----------------------------------
This is the **container-vs-content** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **CSF** — the **fluid** that **fills** the ventricle (and
    the entire ventricular system and the subarachnoid space).

**The CSF is the content; the fourth ventricle is the
container.** Consumers must **not** conflate the fourth
ventricle with the CSF.

The Fourth Ventricle / Superior Medullary Velum Boundary
--------------------------------------------------------
This is the **cavity-vs-roof** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **Superior medullary velum** — the **thin white-matter
    lamina** that **forms the rostral roof** of the fourth
    ventricle (prose).

**The superior medullary velum is the ROOF of the fourth
ventricle; the fourth ventricle is the cavity beneath it.**
Consumers must **not** conflate the fourth ventricle with the
superior medullary velum.

The Fourth Ventricle / Inferior Medullary Velum Boundary
--------------------------------------------------------
This is the **cavity-vs-roof** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **Inferior medullary velum** — the **thin white-matter
    lamina** that **forms the caudal roof** of the fourth
    ventricle (prose — **containing the tela choroidea** and
    the **choroid plexus of the fourth ventricle**).

**The inferior medullary velum is the ROOF of the fourth
ventricle (caudal portion); the fourth ventricle is the cavity
beneath it.** Consumers must **not** conflate the fourth
ventricle with the inferior medullary velum.

The Fourth Ventricle / Facial Colliculus and Floor Landmarks Boundary
---------------------------------------------------------------------
This is the **cavity-vs-floor-landmark** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **Facial colliculus**, **vestibular area**, **hypoglossal
    trigone**, **vagal trigone**, **striae medullares**,
    **obex**, **locus coeruleus (floor landmark)** — the
    **floor landmarks** of the fourth ventricle (prose).

**The floor landmarks are the FLOOR of the fourth ventricle;
the fourth ventricle is the cavity above them.** Consumers must
**not** conflate the fourth ventricle with its floor landmarks.

The Fourth Ventricle / Median Aperture Boundary
-----------------------------------------------
This is the **cavity-vs-aperture** boundary:

*   **Fourth ventricle** (this module) — the **container**
    (the whole cavity).

*   **Median aperture (foramen of Magendie)**
    (``.../fourth_ventricle/median_aperture/``) — the
    **midline CSF outflow aperture** — a **structural child**
    of the fourth ventricle.

**The median aperture is a STRUCTURAL CHILD of the fourth
ventricle** — the **outflow opening** through which the CSF
exits the fourth ventricle. Consumers must **not** conflate
the fourth ventricle with the median aperture — the **fourth
ventricle** is the **cavity**; the **median aperture** is the
**outflow aperture**.

The Fourth Ventricle / Lateral Apertures Boundary
-------------------------------------------------
This is the **cavity-vs-aperture** boundary:

*   **Fourth ventricle** (this module) — the **container**
    (the whole cavity).

*   **Lateral apertures (foramina of Luschka)** — the two
    **lateral CSF outflow apertures** (prose).

**The lateral apertures are PROSE** (not structural children) —
the **outflow openings** through which the CSF exits the
fourth ventricle into the **cerebellopontine angle cistern**.
Consumers must **not** conflate the fourth ventricle with the
lateral apertures — the **fourth ventricle** is the **cavity**;
the **lateral apertures** are the **outflow apertures**.

The Fourth Ventricle / Tela Choroidea Boundary
----------------------------------------------
This is the **cavity-vs-CSF-producing-tissue** boundary:

*   **Fourth ventricle** (this module) — the **cavity**.

*   **Tela choroidea** — the **vascular pia-mater fold** that
    **forms the choroid plexus** of the fourth ventricle
    (prose).

**The tela choroidea is the CSF-producing tissue within the
fourth ventricle; the fourth ventricle is the cavity that
contains it.** Consumers must **not** conflate the fourth
ventricle with the tela choroidea.

The Fourth Ventricle / Myelencephalon Boundary
----------------------------------------------
This is the **shared-rhombencephalic-CSF-cavity** boundary:

*   **Fourth ventricle** (this module) — the **shared
    rhombencephalic CSF cavity** (spanning the metencephalon
    and the myelencephalon).

*   **Myelencephalon** (``.../hindbrain/myelencephalon/``) —
    the **caudal hindbrain sub-container** (medulla oblongata).

**The fourth ventricle's caudal portion extends into the
myelencephalon** — the fourth ventricle is a **shared
rhombencephalic CSF cavity**, not exclusively a metencephalon
structure. The **tree wires the fourth ventricle as a child of
the metencephalon** (the rostral portion); the **myelencephalon
portion is documented as prose** in this module. Consumers must
**not** treat the fourth ventricle as exclusively a
metencephalon structure.

The Fourth Ventricle / SLEA Boundary
------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Fourth ventricle** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The fourth ventricle is NOT part of the SLEA continuum.** It
is a **CSF cavity**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the fourth
ventricle.

Function in the Human Brain
---------------------------
The fourth ventricle's functions are **CSF production, CSF
circulation, buoyancy, waste clearance, and volume
transmission** — **NOT neural processing**:

*   **CSF Production (Choroid Plexus of the Fourth Ventricle):**
    The **choroid plexus of the fourth ventricle** (formed
    from the **tela choroidea** and the **inferior medullary
    velum**) **produces** a portion of the **cerebrospinal
    fluid** — the **fluid** that **fills** the ventricular
    system and the subarachnoid space.

*   **CSF Circulation (CSF Flow Path):** The **fourth
    ventricle** is a **key compartment** in the **CSF flow
    path** — **lateral ventricles** → **third ventricle**
    (via the foramina of Monro) → **mesencephalic aqueduct**
    → **fourth ventricle** → **median aperture (Magendie)**
    and **lateral apertures (Luschka)** → **subarachnoid
    space** → **arachnoid granulations** → dural venous
    sinuses.

*   **Buoyancy and Cushioning:** The **CSF-filled fourth
    ventricle** **reduces the effective weight** of the
    brain (from ~1400 g to ~50 g) and **cushions** it against
    mechanical trauma.

*   **Metabolic Waste Clearance (Glymphatic System):** The
    **CSF** **clears** metabolic waste (including
    **amyloid-β**) from the brain via the **glymphatic
    system** — the fourth ventricle is a **key compartment**
    in this clearance pathway.

*   **Volume Transmission:** The **CSF** is a
    **volume-transmission channel** — neuroactive substances
    (hormones, neuromodulators, cytokines) can **diffuse**
    through the CSF to reach **distant targets**. The fourth
    ventricle is a **CSF compartment** in this signaling
    pathway.

*   **NOT a neural processor.** The fourth ventricle does
    **not** compute, **modulate**, or **transmit** neural
    signals in the classical sense. The **processing** happens
    in the **pons** (pontine nuclei, cranial nerve nuclei
    V–VIII), the **medulla oblongata** (autonomic control,
    cranial nerve nuclei IX–XII), and the **cerebellum**
    (motor coordination, motor learning, cognition, vestibular
    control) that **surround** the fourth ventricle.

**The unifying theme:** the fourth ventricle is the
**rhombencephalic CSF cavity** — the **fluid space** between
the **pons/medulla** and the **cerebellum** — that **produces
and circulates CSF** (via the choroid plexus of the fourth
ventricle and the CSF flow path from the third ventricle to
the subarachnoid space), **cushions the brain**, **clears
metabolic waste**, and **supports volume transmission**. It is
a **cavity**, **NOT neural tissue**, and **NOT a processing
structure**.

Associated Disorders
--------------------
The fourth ventricle has **no single named clinical syndrome**
— its clinical associations are **direct** (as the **CSF
compartment**) or **indirect** (as a **radiological marker**):

*   **Hydrocephalus (Direct — the Fourth Ventricle):**
    **Enlargement** of the fourth ventricle due to **CSF
    accumulation** — **obstructive** (e.g., **fourth
    ventricle outlet obstruction** — the **median aperture**
    or the **lateral apertures** obstructed) or
    **communicating** (impaired CSF absorption at the
    **arachnoid granulations**). The **fourth ventricle** is
    a **primary radiological compartment** for hydrocephalus.

*   **Intraventricular Hemorrhage (Direct — the Fourth
    Ventricle):** **Bleeding into the fourth ventricle** —
    in **premature infants** (germinal matrix hemorrhage) and
    in **adults** (hypertensive hemorrhage with
    intraventricular extension, or **aneurysm rupture**). The
    **fourth ventricle** is a **substrate**.

*   **Choroid Plexus Tumors (Direct — the Fourth Ventricle):**
    **Choroid plexus papilloma** and **carcinoma** — tumors
    **arising from the choroid plexus** *within* the fourth
    ventricle. The **fourth ventricle** is a **substrate**.

*   **Ependymoma (Direct — the Fourth Ventricle Floor):**
    **Ependymoma** — a **pediatric posterior fossa tumor** —
    arises from the **ependyma** of the **fourth ventricle
    floor**. The **fourth ventricle** is the **substrate**.

*   **Medulloblastoma (Direct — Adjacent to the Fourth
    Ventricle Roof):** **Medulloblastoma** — the most common
    **malignant pediatric brain tumor** — typically arises
    in the **vermis** (the **roof of the fourth ventricle**)
    — the **fourth ventricle** is **adjacent** to the
    substrate.

*   **Meningitis / Ventriculitis (Direct — the Fourth
    Ventricle):** **Infection** of the CSF — the fourth
    ventricle is a **CSF compartment** that can be
    **infected** (ventriculitis), especially in **neonates**
    and **immunocompromised** patients.

*   **Dandy-Walker Malformation (Direct — the Fourth
    Ventricle):** **Dandy-Walker malformation** — a
    **congenital malformation** of the cerebellum and the
    fourth ventricle — with **cystic dilation** of the
    fourth ventricle (the **posterior fossa cyst**),
    **cerebellar vermis hypoplasia**, and **hydrocephalus**.
    The **fourth ventricle** is the **primary substrate**.

*   **Chiari Malformation (Direct — the Fourth Ventricle):**
    **Chiari malformation** — the **tonsillar herniation**
    through the **foramen magnum** — can **compress** the
    fourth ventricle (along with the **cerebellar tonsil**
    and the **medulla**). The **fourth ventricle** is a
    **substrate**.

*   **Normal Pressure Hydrocephalus (Direct — Ventricular
    Enlargement):** **Ventricular enlargement** with
    **normal CSF pressure** — a **reversible cause of
    dementia** (the **Hakim-Adams triad**: gait disturbance,
    urinary incontinence, cognitive decline). The **fourth
    ventricle** is a **radiological marker**.

*   **Cerebellar Cognitive-Affective Syndrome (Indirect —
    Adjacent Structures):** **CCAS** — the **cerebellar
    cognitive-affective syndrome** — is caused by **cerebellar
    lesions** (the **posterior lobe** of the hemispheres and
    the **vermis**) — the **fourth ventricle** is **adjacent**
    to the substrate (it is the CSF cavity that the
    **cerebellum** surrounds), but **CCAS** is **NOT** a
    fourth-ventricle syndrome.

*   **No Named "Fourth Ventricle Syndrome" (singular):** The
    fourth ventricle has **multiple named clinical syndromes**
    (hydrocephalus, intraventricular hemorrhage, choroid
    plexus tumors, ependymoma, medulloblastoma, meningitis /
    ventriculitis, Dandy-Walker malformation, Chiari
    malformation, normal pressure hydrocephalus) — but **no
    single "fourth ventricle syndrome."** Its clinical
    relevance is **direct** (as the **CSF compartment**)
    and **indirect** (as a **radiological marker** and as
    the **CSF conduit** adjacent to the **pons**,
    **cerebellum**, and **medulla**).

**What is NOT here:** The fourth ventricle is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's
disease** (substantia nigra, in the midbrain). Its clinical
relevance is **ventricular CSF pathology** and **radiological
markers** — **no named fourth ventricle syndrome exists**.

Lateralization Notes
--------------------
This is the **fourth ventricle** container module. The fourth
ventricle is a **midline CSF cavity** — the **median** fluid
space **between** the **pons/medulla** and the **cerebellum**
— and it carries **NO warning**:

*   **Midline CSF Cavity (Not a Pair):** The **fourth
    ventricle** is the **midline** CSF cavity — the **median**
    fluid space **between** the left and right brainstem /
    cerebellar structures. The **fourth ventricle** is **not
    a paired structure** — it is a **midline CSF cavity**.

*   **Bilateral Apertures (Not a Pair):** The **lateral
    apertures (foramina of Luschka)** — the two **lateral
    CSF outflow apertures** — are **bilaterally paired**
    (the **left** and **right** foramina of Luschka).
    The **median aperture (foramen of Magendie)** is the
    **midline** aperture — the **structural child** of the
    fourth ventricle. The **median aperture** is a **midline
    structure**; the **lateral apertures** are **bilateral**.
    The **lateral apertures** are documented as **prose** in
    this module — they are **NOT** structural children.

*   **NO Extended-Amygdala Warning (SLEA-free):** The fourth
    ventricle is **NOT** an extended-amygdala component. It
    carries **no SLEA warning**. Consumers must **not**
    import the SLEA warning into the fourth ventricle.

*   **NO Amygdala-Lateralization Warning:** The fourth
    ventricle is **NOT** the fear-output or the fear-learning
    structure. It is a **CSF cavity** — consumers must
    **not** conflate it with the **amygdala** or the **fear
    circuit**.

**A consumer that assumes "left fourth ventricle = right
fourth ventricle" should be reminded that the fourth ventricle
is a MIDLINE CSF cavity, not a paired structure** — there is
**one fourth ventricle**, spanning the **midline** of the
rhombencephalon. The fourth ventricle carries **NO warning**
— **no SLEA warning**, **no amygdala-lateralization warning**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **container** does
    **not** import from any ``left/`` or ``right/``
    sub-container — it is a **namespace container**. The
    fourth ventricle is a **midline CSF cavity**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../metencephalon/`` (parent),
    ``.../metencephalon/pons/`` (sibling),
    ``.../metencephalon/cerebellum/`` (sibling),
    ``.../hindbrain/myelencephalon/`` (the caudal portion of
    the fourth ventricle extends into the myelencephalon —
    the relationship is documented as **prose**, not as a
    structural parent or child),
    ``.../forebrain/diencephalon/third_ventricle/``,
    ``.../forebrain/telencephalon/lateral_ventricles/``,
    ``.../midbrain/mesencephalic_aqueduct/``,
    ``.../hindbrain/``, ``.../midbrain/``,
    ``.../forebrain/``, or any other container. The fourth
    ventricle's relationships to the pons, cerebellum,
    medulla oblongata, third ventricle, lateral ventricles,
    mesencephalic aqueduct, subarachnoid space, choroid
    plexus, ependyma, CSF, superior and inferior medullary
    vela, tela choroidea, floor landmarks, obex, lateral
    recesses, median aperture, and lateral apertures are
    documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — one structural child.** The
    ``median_aperture/`` is a **structural child**. The
    **lateral apertures**, the **superior and inferior
    medullary vela**, the **tela choroidea**, the **choroid
    plexus**, the **ependyma**, the **CSF**, the **floor
    landmarks**, the **obex**, and the **lateral recesses**
    are **prose**. Consumers must not assume any exist as
    direct children of the fourth ventricle; resolve
    aperture-level or floor-landmark-level detail through
    the references.
*   **CSF CAVITY — NOT neural tissue.** The fourth ventricle
    is the **CSF space**; the **pons**, **cerebellum**, and
    **medulla oblongata** are the **neural tissue** that
    surrounds it.
*   **RHOMBENCEPHALIC — NOT the third ventricle or the
    lateral ventricles.** The **third ventricle** is
    **diencephalic**; the **lateral ventricles** are
    **telencephalic**; the **fourth ventricle** (here) is
    **rhombencephalic**. They are connected via the
    **mesencephalic aqueduct** (third → fourth) and the
    **foramina of Monro** (lateral → third) — those are
    **connections**, not identities.
*   **SHARED RHOMBENCEPHALIC CSF CAVITY — spans the
    metencephalon AND the myelencephalon.** The **tree
    wires the fourth ventricle as a child of the
    metencephalon** (the rostral portion); the **caudal
    portion extends into the myelencephalon**.
*   **NOT the choroid plexus — the choroid plexus is the
    CSF-PRODUCING TISSUE inside the fourth ventricle.**
*   **NOT the ependyma — the ependyma is the LINING.**
*   **NOT the CSF — the CSF is the FLUID CONTENT.**
*   **NOT the superior or inferior medullary velum — those
    are the ROOF.**
*   **NOT the floor landmarks (facial colliculus, vestibular
    area, hypoglossal trigone, vagal trigone, striae
    medullares, obex, locus coeruleus) — those are the
    FLOOR.**
*   **NOT the subarachnoid space — the subarachnoid space is
    the EXTERNAL CSF space.**
*   **NOT a neural-processing structure.** The fourth ventricle
    is a **fluid space** — it **produces and circulates
    CSF**, **cushions the brain**, **clears waste**, and
    **supports volume transmission**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The fourth ventricle is a
    **local container** under the metencephalon, not a
    **cross-listed container**.
*   **No nested cross-listing.** The fourth ventricle has
    **no nested dual-framing module**. It is a **single
    container** with one structural child.
*   **No lateralization warning.** The fourth ventricle is a
    **midline CSF cavity** — it carries **no warning** —
    **no SLEA warning**, **no amygdala-lateralization
    warning**, and **no rhinencephalon-exclusion flag**.
    The **midline nature** of the fourth ventricle and the
    **bilateral nature** of the lateral apertures are
    documented as **structural fact**, not as a
    **lateralization warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.fourth_ventricle import median_aperture

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.fourth_ventricle"
    )
    median_aperture_path = (
        "hindbrain.metencephalon.fourth_ventricle.median_aperture"
    )

**Do not** assume the fourth ventricle is the **pons** or the
**cerebellum**. The **pons** and **cerebellum** are the
**neural tissue**; the **fourth ventricle** is the **CSF
cavity** between them.

**Do not** assume the fourth ventricle is the **third
ventricle** or the **lateral ventricles**. The **third
ventricle** is **diencephalic**; the **lateral ventricles**
are **telencephalic**; the **fourth ventricle** is
**rhombencephalic**. They are connected only indirectly (via
the **third ventricle** and the **mesencephalic aqueduct**).

**Do not** assume the fourth ventricle is the **mesencephalic
aqueduct**. The **mesencephalic aqueduct** is the **midbrain
CSF channel**; the **fourth ventricle** is the
**rhombencephalic CSF cavity** that the aqueduct **empties
into**.

**Do not** assume the fourth ventricle is the **subarachnoid
space**. The **subarachnoid space** is the **external CSF
space**; the **fourth ventricle** is the **internal CSF
cavity**. They communicate via the **median aperture** and
the **lateral apertures** — **connections**, not identities.

**Do not** assume the fourth ventricle is the **choroid
plexus**, the **ependyma**, the **CSF**, the **superior or
inferior medullary velum**, the **tela choroidea**, the
**floor landmarks**, or the **lateral apertures**. Those are
**prose** — tissues, structures, floor landmarks, or
apertures related to the fourth ventricle.

**Do not** assume the fourth ventricle is the **median
aperture**. The **median aperture (foramen of Magendie)** is
a **structural child** of the fourth ventricle — the
**outflow aperture**. The **fourth ventricle** is the
**cavity**; the **median aperture** is the **outflow
opening**.

**Do not** assume the fourth ventricle is the **pons**,
**cerebellum**, **medulla oblongata**, **metencephalon**,
**myelencephalon**, **hindbrain**, **midbrain**, or
**forebrain**. The **fourth ventricle** is a **shared
rhombencephalic CSF cavity** spanning the **metencephalon**
and the **myelencephalon** — the tree wires it as a **child
of the metencephalon** (the rostral portion).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the fourth ventricle.
**The fourth ventricle is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the fourth ventricle's children (recommended
consumer pattern)::

    FOURTH_VENTRICLE_CHILDREN = ("median_aperture",)
    # The median_aperture (foramen of Magendie) is the midline
    # CSF outflow aperture — the one structural child of the
    # fourth ventricle. The lateral apertures (foramina of
    # Luschka) are prose, not structural children.

Reaching the metencephalon (recommended consumer pattern — the
parent)::

    # The metencephalon is the CONTAINER (pons + cerebellum +
    # fourth ventricle):
    #
    #   hindbrain.metencephalon
    #
    # The fourth ventricle is a CHILD sub-container of the
    # metencephalon.

Reaching the pons (recommended consumer pattern — NOTE the
CSF-cavity-vs-ventral-brainstem boundary)::

    # The pons is the VENTRAL WALL of the fourth ventricle:
    #
    #   hindbrain.metencephalon.pons
    #
    # The pons is the NEURAL TISSUE; the fourth ventricle is the
    # CSF CAVITY dorsal to the pons.

Reaching the cerebellum (recommended consumer pattern — NOTE
the CSF-cavity-vs-dorsal-suprasegmental boundary)::

    # The cerebellum is the DORSAL ROOF of the fourth
    # ventricle (via the superior and inferior medullary
    # vela):
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellum is the NEURAL TISSUE; the fourth ventricle
    # is the CSF CAVITY ventral to the cerebellum.

Reaching the medulla oblongata (recommended consumer pattern —
NOTE the CSF-cavity-vs-caudal-brainstem boundary)::

    # The medulla oblongata is the VENTRAL WALL of the CAUDAL
    # portion of the fourth ventricle:
    #
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The medulla is the NEURAL TISSUE; the fourth ventricle is
    # the CSF CAVITY dorsal to the medulla.

Reaching the median aperture (recommended consumer pattern —
the structural child)::

    # The median aperture (foramen of Magendie) is the MIDLINE
    # CSF OUTFLOW APERTURE of the fourth ventricle:
    #
    #   hindbrain.metencephalon.fourth_ventricle.median_aperture
    #
    # The median aperture is the OUTFLOW OPENING; the fourth
    # ventricle is the CAVITY.

Reaching the third ventricle (recommended consumer pattern —
NOTE the rhombencephalic-vs-diencephalic boundary)::

    # The third ventricle is the DIENCEPHALIC CSF cavity —
    # connected to the fourth ventricle via the mesencephalic
    # aqueduct:
    #
    #   forebrain.diencephalon.third_ventricle
    #
    # The third ventricle is DIENCEPHALIC; the fourth ventricle
    # is RHOMBENCEPHALIC. The mesencephalic aqueduct is a
    # CONNECTION, not an identity.

Reaching the lateral ventricles (recommended consumer pattern —
NOTE the rhombencephalic-vs-telencephalic boundary)::

    # The lateral ventricles are the TELENCEPHALIC paired CSF
    # cavities — connected to the fourth ventricle only
    # indirectly (via the third ventricle and the
    # mesencephalic aqueduct):
    #
    #   forebrain.telencephalon.lateral_ventricles
    #
    # The lateral ventricles are TELENCEPHALIC; the fourth
    # ventricle is RHOMBENCEPHALIC.

Reaching the mesencephalic aqueduct (recommended consumer
pattern — NOTE the rhombencephalic-cavity-vs-midbrain-channel
boundary)::

    # The mesencephalic aqueduct (cerebral aqueduct) is the
    # MIDBRAIN CSF channel connecting the third ventricle to
    # the fourth ventricle:
    #
    #   midbrain.mesencephalic_aqueduct
    #
    # The aqueduct is the MIDBRAIN CHANNEL; the fourth
    # ventricle is the RHOMBENCEPHALIC CAVITY that the
    # aqueduct empties into.

Reaching the subarachnoid space (recommended consumer pattern —
NOTE the internal-vs-external CSF boundary)::

    # The subarachnoid space is the EXTERNAL CSF space —
    # connected to the fourth ventricle via the median
    # aperture and the lateral apertures:
    #
    #   (prose) subarachnoid_space
    #
    # The fourth ventricle is INTERNAL; the subarachnoid space
    # is EXTERNAL. The median aperture and the lateral
    # apertures are CONNECTIONS, not identities.

Reaching the choroid plexus (recommended consumer pattern —
NOTE the cavity-vs-CSF-producing-tissue boundary)::

    # The choroid plexus (of the fourth ventricle) is the
    # CSF-PRODUCING TISSUE inside the fourth ventricle
    # (prose — formed from the tela choroidea and the inferior
    # medullary velum):
    #
    #   (prose) hindbrain.metencephalon.fourth_ventricle.
    #   <choroid_plexus>
    #
    # The choroid plexus is the CSF-PRODUCING TISSUE; the
    # fourth ventricle is the CAVITY that contains it.

Reaching the superior medullary velum (recommended consumer
pattern — NOTE the cavity-vs-roof boundary)::

    # The superior medullary velum is the THIN WHITE-MATTER
    # LAMINA that forms the ROSTRAL ROOF of the fourth
    # ventricle (prose):
    #
    #   (prose) hindbrain.metencephalon.fourth_ventricle.
    #   <superior_medullary_velum>
    #
    # The superior medullary velum is the ROOF; the fourth
    # ventricle is the CAVITY beneath it.

Reaching the inferior medullary velum (recommended consumer
pattern — NOTE the cavity-vs-roof boundary)::

    # The inferior medullary velum is the THIN WHITE-MATTER
    # LAMINA that forms the CAUDAL ROOF of the fourth ventricle
    # (prose — containing the tela choroidea and the choroid
    # plexus of the fourth ventricle):
    #
    #   (prose) hindbrain.metencephalon.fourth_ventricle.
    #   <inferior_medullary_velum>
    #
    # The inferior medullary velum is the ROOF; the fourth
    # ventricle is the CAVITY beneath it.

Reaching the floor landmarks (recommended consumer pattern —
NOTE the cavity-vs-floor-landmark boundary)::

    # The floor landmarks of the fourth ventricle (prose):
    #   facial colliculus -> over the abducens nucleus and the
    #                        internal genu of the facial nerve
    #   vestibular area -> over the vestibular nuclei
    #   hypoglossal trigone -> over the hypoglossal nucleus
    #   vagal trigone -> over the dorsal motor nucleus of the
    #                    vagus
    #   striae medullares -> the medullary striae (auditory
    #                        pathway fibers)
    #   obex -> the caudal-most portion of the fourth ventricle
    #           floor
    #   locus coeruleus (floor landmark) -> the noradrenergic
    #                                      nucleus visible
    #                                      through the floor
    #
    # The floor landmarks are the FLOOR; the fourth ventricle
    # is the CAVITY above them.

Reaching the myelencephalon (recommended consumer pattern —
NOTE the shared-rhombencephalic-CSF-cavity boundary)::

    # The myelencephalon is the CAUDAL hindbrain sub-container
    # (medulla oblongata) — the fourth ventricle's CAUDAL
    # portion extends into the myelencephalon:
    #
    #   hindbrain.myelencephalon
    #
    # The fourth ventricle is a SHARED rhombencephalic CSF
    # cavity spanning the metencephalon (rostral portion) and
    # the myelencephalon (caudal portion). The tree wires the
    # fourth ventricle as a child of the metencephalon (the
    # rostral portion).

Reaching the brainstem (recommended consumer pattern — NOTE
the CSF-cavity-vs-segmental-neuraxis boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons
    # + medulla) — the fourth ventricle is the CSF cavity
    # BETWEEN the pons/medulla (ventral) and the cerebellum
    # (dorsal):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The brainstem is the NEURAL TISSUE; the fourth ventricle
    # is the CSF CAVITY.

Component-level detail (not wired — consult references)::

    # The fourth ventricle's component-level detail is prose,
    # not modules:
    #   median aperture (foramen of Magendie) -> structural
    #                                            child
    #   lateral apertures (foramina of Luschka) -> prose
    #   superior medullary velum -> prose
    #   inferior medullary velum -> prose
    #   tela choroidea -> prose
    #   choroid plexus of the fourth ventricle -> prose
    #   ependyma of the fourth ventricle -> prose
    #   CSF of the fourth ventricle -> prose
    #   facial colliculus, vestibular area, hypoglossal
    #   trigone, vagal trigone, striae medullares, obex,
    #   locus coeruleus (floor landmark) -> prose
    #   lateral recesses -> prose
    #
    # Do not attempt to resolve these as sub-paths of the
    # fourth ventricle.

Midline iteration note (the fourth ventricle is NOT a paired
structure — the lateral apertures ARE paired)::

    # The fourth ventricle is a MIDLINE CSF cavity — NOT a
    # paired structure. The "left"/"right" iteration patterns
    # are NOT applicable to the fourth ventricle itself. The
    # lateral apertures (foramina of Luschka) are paired (left
    # and right), but they are PROSE (not structural children
    # of the fourth ventricle) — see the references for the
    # lateral apertures.

References
----------
*   **Canonical fourth ventricle anatomy:** Standring, S.
    (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Fourth ventricle — floor,
    roof, lateral recesses, median aperture, lateral
    apertures, choroid plexus, tela choroidea, medullary
    vela, floor landmarks.)
*   **Ventricular system overview:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Ventricular system — fourth ventricle, CSF flow,
    apertures, choroid plexus, ependyma.)
*   **CSF physiology and choroid plexus:** Damkier, H.H.,
    Brown, P.D., Praetorius, J. (2013). "Cerebrospinal
    fluid secretion by the choroid plexus."
    *Physiological Reviews* 93:1847–1892. (Choroid plexus —
    the CSF-producing tissue within the fourth ventricle.)
*   **Glymphatic system and CSF clearance:** Iliff, J.J., et
    al. (2012). "A paravascular pathway facilitates CSF flow
    through the brain parenchyma and the clearance of
    interstitial solutes, including amyloid β." *Science
    Translational Medicine* 4:147ra111. (CSF clearance —
    the fourth ventricle as a key compartment.)
*   **Dandy-Walker malformation:** Dandy, W.E., Blackfan,
    K.D. (1914). "Internal hydrocephalus: an experimental,
    clinical and pathological study." *American Journal of
    Diseases of Children* 8:406–482. (Dandy-Walker
    malformation — cystic dilation of the fourth ventricle,
    cerebellar vermis hypoplasia, hydrocephalus.)
*   **Ependymoma (fourth ventricle floor):** Louis, D.N., et
    al. (2016). "The 2016 World Health Organization
    Classification of Tumors of the Central Nervous System:
    a summary." *Acta Neuropathologica* 131:803–820.
    (Ependymoma — pediatric posterior fossa tumor; arises
    from the fourth ventricle floor.)
*   **Medulloblastoma (fourth ventricle roof):** Louis, D.N.,
    et al. (2016). "The 2016 World Health Organization
    Classification of Tumors of the Central Nervous System:
    a summary." *Acta Neuropathologica* 131:803–820.
    (Medulloblastoma — pediatric cerebellar tumor; typically
    arises in the vermis — the fourth ventricle roof.)
*   **Choroid plexus tumors:** Wolff, J.E.A., et al. (2002).
    "Choroid plexus tumours." *British Journal of Cancer*
    87:1086–1091. (Choroid plexus papilloma and carcinoma
    within the fourth ventricle.)
*   **Hydrocephalus:** Rekate, H.L. (2009). "A contemporary
    definition of hydrocephalus: is it time?" *Cerebrospinal
    Fluid Research* 6:5. (Hydrocephalus — ventricular
    enlargement due to CSF accumulation.)
*   **Intraventricular hemorrhage:** Volpe, J.J. (2008).
    "Intraventricular hemorrhage in the premature infant —
    current concepts." *Annals of Neurology* 25:3–11.
    (Germinal matrix / intraventricular hemorrhage in
    premature infants.)
*   **Chiari malformation:** Chiari, H. (1891). "Über
    Veränderungen des Kleinhirns infolge von Hydrocephalie
    des Grosshirns." *Deutsche Medizinische Wochenschrift*
    17:1172–1175. (Chiari malformation — tonsillar
    herniation through the foramen magnum; fourth ventricle
    compression.)
*   **Normal pressure hydrocephalus:** Hakim, S., Adams, R.D.
    (1965). "The special clinical problem of symptomatic
    hydrocephalus with normal cerebrospinal fluid pressure."
    *Journal of the Neurological Sciences* 2:307–327. (The
    Hakim-Adams triad; ventricular enlargement with normal
    CSF pressure.)
*   **SLEA (contrast — the fourth ventricle is NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens;
    NOT the fourth ventricle.)
*   NeuroNames — Fourth ventricle; FMA — Fourth ventricle.
"""