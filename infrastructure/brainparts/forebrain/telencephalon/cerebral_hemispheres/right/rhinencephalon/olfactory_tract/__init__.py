"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon.olfactory_tract
==========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── rhinencephalon
                └── olfactory_tract   <-- THIS MODULE

**Primary synonym:** Olfactory tract; tractus olfactorius; olfactory
peduncle (in older usage — see *Boundary status*).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**primarily white-matter bundle** — the axonal connection between the
olfactory bulb and the primary olfactory cortex.
**Part of:** The **primary olfactory pathway** — the **middle segment**
of the olfactory peduncle.
**Structural parent:** ``.../right/rhinencephalon/`` → **direct child** of
the rhinencephalon container.
**Structural children:** **None.** This is a **leaf** module. The
tract's **three striae** (lateral, medial, intermediate) are documented
as **prose**, not as structural children.
**Boundary status:** **Boundary case — a white-matter bundle with grey
matter embedded in it.** The olfactory tract is primarily axonal, but
it **contains the pars externa of the anterior olfactory nucleus** as a
grey-matter layer **within** the bundle. It is therefore **not a pure
white-matter tract** in the way the corticospinal tract or optic
radiation are. Consumers must not treat the tract as a homogeneous
axonal conduit.
**Boundary status (peduncle):** **Boundary case — continuous with the
olfactory bulb caudally and with the olfactory trigone/striae
rostrally.** The bulb–tract junction is **cytoarchitecturally
continuous** (the bulb's caudal pole narrows into the tract), and the
tract–striae junction at the **olfactory trigone** is where the bundle
**splays into three named striae**. The tree treats the tract as a
distinct leaf, but the peduncle is a **continuous structure** — see
*Boundary status (peduncle)* under Design Contract.

Overview
--------
The olfactory tract is the **axonal bundle** connecting the olfactory
bulb to the primary olfactory cortex. It carries the axons of the
bulb's **mitral and tufted cells** caudally along the **olfactory
sulcus** of the orbitofrontal cortex and terminates at the
**olfactory trigone**, where it **splays into three striae** —
lateral, medial, and intermediate — that distribute olfactory
information to different cortical and limbic targets.

**The tract is short and thin in humans.** In macrosmatic mammals it
is a prominent peduncle; in humans it is a **short, thin bundle**
running a few centimeters along the orbital surface of the frontal
lobe. Its **relative** prominence is reduced compared with macrosmatic
mammals, but its **absolute** axonal content is conserved — like the
bulb, the tract is **proportionately smaller but not vestigial**.

**The tract is not a simple cable.** It contains:

*   **Bulb efferents** — mitral and tufted cell axons projecting
    caudally to the primary olfactory cortex.
*   **AON efferents** — axons from the anterior olfactory nucleus
    projecting to the piriform cortex and beyond.
*   **AON pars externa grey matter** — a thin layer of **neurons**
    embedded **within** the lateral olfactory tract, which is the
    anatomical substrate of the **cross-hemispheric olfactory
    projection**.
*   **Centrifugal afferents** — fibers from the piriform cortex,
    diagonal band, and brainstem nuclei projecting **back** to the
    bulb, which travel **within** the tract alongside the bulb
    efferents.

**This mixed composition is the tract's defining anatomical fact.**
The tract is **not** a one-way bulb→cortex cable; it is a **two-way,
grey-matter-containing bundle** that carries feedforward, feedback,
and cross-hemispheric signals in a single anatomical structure.

The Three Striae (prose, not structural children)
-------------------------------------------------
At the **olfactory trigone** — a small triangular expansion at the
caudal end of the tract — the bundle **splays into three striae**:

*   **Lateral olfactory stria (LOS)** — the **largest** and
    **functionally dominant** stria. It carries bulb and AON axons to
    the **primary olfactory cortex**: the **piriform cortex**,
    **periamygdaloid cortex**, and **entorhinal cortex**, and to the
    **corticomedial amygdala**. It is the **main olfactory projection
    pathway**. The LOS is also the **stria that contains the AON's
    pars externa** — the cross-hemispheric projection runs **within**
    the lateral stria, not beside it.

*   **Medial olfactory stria (MOS)** — the **smallest** stria in
    humans, often **poorly developed**. It projects to the
    **septal nuclei**, the **diagonal band of Broca**, and the
    **paraolfactory area** (subcallosal gyrus). In macrosmatic
    mammals the MOS is a major limbic-olfactory pathway; in humans it
    is **reduced** and its functional contribution to olfaction is
    **modest**.

*   **Intermediate olfactory stria** — an **inconstant** stria,
    **present in some individuals and absent in others**. When
    present, it projects to the **olfactory tubercle** (on the
    anterior perforated substance). Its **variability** is one reason
    the olfactory tubercle is **not** a reliable rhinencephalon child
    — the tree places it under ``subcortical/`` instead.

**These three striae are prose, not structural children.** The tree
does **not** wire LOS, MOS, or intermediate stria as sub-modules. The
tract is a **single leaf**; the striae are its **terminal
arborizations**, documented here so consumers know what the tract
becomes **caudally**.

**The lateral stria is the clinically dominant pathway.** Lesions of
the LOS produce **ipsilateral anosmia** (or, more precisely,
**ipsilateral hyposmia**); lesions of the MOS or intermediate stria
produce **subtle or no detectable olfactory deficit** in humans,
because their targets are limbic and their contribution to conscious
olfaction is **modest**. A consumer that treats all three striae as
equivalent will **overestimate the clinical significance of the MOS
and intermediate stria**.

The Olfactory Peduncle Context
------------------------------
The tract is the **middle component** of the olfactory peduncle, and
the tree separates the peduncle's three components into three sibling
leaves:

*   ``olfactory_bulb`` — the **laminated rostral expansion**.
*   ``olfactory_tract`` — the **axonal bundle** running caudally
    (this module).
*   ``anterior_olfactory_nucleus`` — the **grey matter embedded
    within** the tract/peduncle.

**These three are anatomically continuous.** The bulb's **caudal pole**
narrows into the **tract**, and the tract's **pars externa grey
matter** is the AON. There is **no sharp boundary** between bulb and
tract, or between tract and AON, in many species. The tree's three-way
split is a **useful abstraction**, not a sharp anatomical boundary. A
consumer that treats the bulb, tract, and AON as cleanly separable
will **misunderstand the peduncle** — they are better understood as
**regions of a continuous olfactory peduncle**.

Function in the Human Brain
---------------------------
The tract's functions are **conduction and distribution**, with a
small but real **modulatory** component:

*   **Axonal Conduction (Primary Function):** The tract carries
    mitral and tufted cell axons from the bulb to the primary
    olfactory cortex. It is the **conduction pathway** of the
    olfactory system — the analogue of the optic nerve or optic
    radiation, but **shorter and less prominent** in humans.

*   **Distribution via the Striae:** At the olfactory trigone, the
    tract **distributes** olfactory information to three targets:
    the piriform/periamygdaloid cortex (LOS), the septal/diagonal
    band region (MOS), and the olfactory tubercle (intermediate
    stria, when present). The tract is a **distribution hub**, not a
    single cable.

*   **Cross-Hemispheric Conduction (Pars Externa):** The tract
    **contains** the AON's pars externa, which projects to the
    **contralateral olfactory bulb**. The tract is therefore the
    **anatomical substrate** of the cross-hemispheric olfactory
    projection — but the **neurons** doing the projection belong to
    the AON, not to the tract proper.

*   **Centrifugal Feedback Conduction:** The tract carries
    **centrifugal afferents** from the piriform cortex, diagonal
    band, locus ceruleus, and raphe nuclei **back** to the bulb,
    where they modulate **glomerular gain** and **attention-dependent
    olfactory processing**. The tract is a **two-way** bundle, not a
    one-way cable.

*   **NOT a processing structure.** The tract **conducts and
    distributes**; it does **not** process olfactory information.
    **Odor identification and memory** are properties of the
    **piriform cortex** and its limbic targets, documented elsewhere.
    The tract's only grey matter — the pars externa — is an **AON
    component** that happens to be embedded in the tract, not a
    tract-intrinsic processor.

**The unifying theme:** the tract is the **conduction and distribution
segment** of the olfactory peduncle. It is **not** a processing
structure, **not** a primary sensory cortex, and **not** a limbic
structure. It is a **mixed white-matter bundle** that carries
feedforward, feedback, and cross-hemispheric signals, and that
**contains** a small grey-matter component (pars externa) belonging
to the AON.

Associated Disorders
--------------------
Olfactory tract disorders are **primary olfactory**, and are
**clinically dominated by the lateral stria**:

*   **Anosmia and Hyposmia from Tract Lesions:** **Olfactory groove
    meningioma**, **anterior cranial fossa trauma**, and **surgical
    injury** can compress or sever the tract, producing **unilateral
    anosmia** (often unnoticed) and, if large, **Foster Kennedy
    syndrome** (ipsilateral anosmia + ipsilateral optic atrophy +
    contralateral papilledema).

*   **Olfactory Groove Meningioma — Tract Compression:** The tract is
    the **primary structure compressed** by olfactory groove
    meningiomas. The bulb is often **displaced or atrophic**; the
    tract is **directly compressed** between the tumor and the
    orbital surface of the frontal lobe. **Unilateral anosmia** is
    the classic presentation.

*   **Post-Traumatic Anosmia — Tract Shearing:** **Traumatic brain
    injury** (especially **occipital impact** causing
    **contrecoup** injury at the frontal pole) can **shear the
    olfactory tract** at the cribriform plate or along the orbital
    surface, producing **anosmia** that is often **permanent**.
    Tract shearing is one of the **most common causes of post-
    traumatic anosmia**.

*   **Neurodegenerative Tract Pathology:** The tract is **affected**
    in **Parkinson's disease** and **Alzheimer's disease** alongside
    the bulb and AON. **α-Synuclein** and **tau** pathology can be
    seen in tract fibers, contributing to **prodromal olfactory
    deficits**.

*   **Kallmann Syndrome — Tract Aplasia:** In **Kallmann syndrome**,
    the **olfactory tract fails to form** along with the bulb
    (secondary to failed GnRH neuron migration). **Tract aplasia**
    accompanies **bulb agenesis** and **anosmia**.

**What is NOT here:** The tract is **not** the substrate for
**temporal lobe epilepsy** (hippocampal/amygdalar), **Kluver-Bucy
syndrome** (amygdala), **semantic dementia** (anterior temporal
neocortex), or **Wernicke's aphasia** (BA22). Its clinical footprint
is **olfactory**, and even there it is a **conduction structure**, not
a processing one — the primary substrates for odor identification are
the **piriform cortex** (LOS target) and **amygdala** (LOS target).

Lateralization Notes
--------------------
This is the **right** olfactory tract module. The tract is
**bilaterally symmetric** and **functionally non-lateralized**:

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the olfactory tract has **no documented left-lateralized or
    right-lateralized function**.

*   **Ipsilateral Projection:** Each tract projects **ipsilaterally**
    to the piriform cortex (via the LOS). The two tracts are
    **functionally symmetric** for odor detection and discrimination.
    **Unilateral anosmia** from a unilateral tract lesion is the
    clinical expression of this symmetry.

*   **Pars Externa Exception (Not a Tract Asymmetry):** The pars
    externa of the AON — which is **embedded** in the lateral tract —
    projects to the **contralateral** bulb. **For this right tract,
    the pars externa crosses to the left bulb** — but the
    **left tract's** pars externa crosses to the **right bulb**, so
    the crossing is **symmetric across the two sides**. This is a
    **functional cross-hemispheric projection**, not a
    **lateralization** of the tract itself. The tract is structurally
    symmetric; the pars externa's crossing is **symmetric in both
    tracts** (each side crosses to the other).

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the tract. Do not import them into the tract.

**A consumer that assumes "right tract = left tract" will be
structurally and functionally correct** — the two tracts are
symmetric, and the only crossing in the system (pars externa) is
**symmetric across the two sides**. The tract is one of the most
cleanly symmetric structures in the rhinencephalon.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The tract's
    projections to the piriform cortex, periamygdaloid cortex,
    entorhinal cortex, septal nuclei, diagonal band, and olfactory
    tubercle are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The tract's **three
    striae** (LOS, MOS, intermediate) are documented as **prose**, not
    as sub-modules. Consumers must not assume they exist as children;
    resolve strial detail through the references.
*   **Boundary case — white-matter bundle with grey matter embedded.**
    The tract is **primarily axonal** but **contains the AON's pars
    externa** as a grey-matter layer. Do not treat it as a pure
    white-matter tract.
*   **Boundary case — continuous with the olfactory peduncle.** The
    bulb–tract junction and the tract–AON junction are
    **cytoarchitecturally continuous**. Consumers must not assume
    sharp boundaries among ``olfactory_bulb``, ``olfactory_tract``,
    and ``anterior_olfactory_nucleus``. The tree's three-way split is
    a **useful abstraction**.
*   **The intermediate stria is inconstant — flagged.** The
    intermediate olfactory stria is **present in some individuals and
    absent in others**. Do not assume it exists in every brain.
    Consumers resolving the olfactory tubercle should go through
    ``subcortical/basal_forebrain/striatum/ventral_striatum/olfactory_tubercle/``,
    not through an intermediate-stria path.
*   **The MOS is reduced in humans — flagged.** The medial olfactory
    stria is **small and often poorly developed** in humans. Do not
    treat it as equivalent to the lateral stria; the lateral stria is
    the **clinically dominant** pathway.
*   **No ``AREA_PATHS`` hop.** The tract is a local leaf under the
    rhinencephalon, not a cross-listed leaf.
*   **No nested cross-listing.** The tract has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with left olfactory tract.** Right and left
    tract modules are **structurally identical** — same leaf status,
    same three-striae prose, same grey-matter-within-white-matter
    caveat, same peduncle-continuity warning.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon import olfactory_tract

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.rhinencephalon."
        "olfactory_tract"
    )

**Do not** assume the tract has structural children. It is a **leaf**.
The three striae (LOS, MOS, intermediate) are **prose only** — they
are not wired as modules.

**Do not** assume the tract is a pure white-matter bundle. It contains
the AON's **pars externa** as embedded grey matter. Consumers that
need to resolve the pars externa should resolve it through
``anterior_olfactory_nucleus``, not through the tract.

**Do not** assume sharp boundaries among ``olfactory_bulb``,
``olfactory_tract``, and ``anterior_olfactory_nucleus``. The peduncle
is a **continuous structure**; the tree's three-way split is a
**useful abstraction**.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        tract_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon."
            f"olfactory_tract"
        )
        # resolve tract_path through the memory/recall layer

Reaching the tract's downstream targets (recommended consumer
pattern)::

    # The tract distributes to structures documented elsewhere in the
    # tree. Resolve them at their own paths:
    #
    #   Lateral stria (LOS) targets:
    #     rhinencephalon.piriform_cortex
    #     rhinencephalon.periamygdaloid_cortex
    #     cortex.temporal.gyri.entorhinal_cortex
    #     subcortical.medial_temporal_lobe.amygdala
    #
    #   Medial stria (MOS) targets:
    #     subcortical.basal_forebrain.septal_nuclei
    #     subcortical.basal_forebrain.diagonal_band_of_broca
    #
    #   Intermediate stria target (when present):
    #     subcortical.basal_forebrain.striatum.ventral_striatum.olfactory_tubercle
    #
    # These are NOT tract children. They are downstream targets.

Strial detail (not wired — consult references)::

    # The tract's striae are prose, not modules:
    #   LOS -> lateral olfactory stria (largest; dominant)
    #          -> piriform, periamygdaloid, entorhinal, amygdala
    #   MOS -> medial olfactory stria (smallest; reduced in humans)
    #          -> septal nuclei, diagonal band, paraolfactory area
    #   intermediate -> inconstant; olfactory tubercle (when present)
    #
    # Do not attempt to resolve these as sub-paths of the tract module.

References
----------
*   **Canonical anatomy:** Doty, R.L. (2015). *Handbook of Olfaction
    and Gustation*, 3rd ed. (Human olfactory tract anatomy, striae,
    and clinical significance.)
*   **Olfactory tract and striae:** Price, J.L. (1990). "Olfactory
    system." In *The Human Nervous System* (Paxinos, G., ed.).
    (Definitive anatomy of the tract, trigone, and three striae.)
*   **Olfactory groove meningioma:** Bakay, L. (1984). "Olfactory
    meningiomas." In *Neurosurgery* (Wilkins, R.H., Rengachary, S.S.,
    eds.). (Tract compression and Foster Kennedy syndrome.)
*   **Post-traumatic anosmia:** Costanzo, R.M., Zasler, N.D. (1992).
    "Head trauma." In *Smell and Taste in Health and Disease*
    (Getchell, T.V., et al., eds.). (Tract shearing as a cause of
    post-traumatic anosmia.)
*   **Parkinson's disease:** Braak, H., et al. (2003). "Staging of
    brain pathology related to sporadic Parkinson's disease."
    *Neurobiology of Aging* 24:197–211. (Tract involvement alongside
    bulb and AON.)
*   **Kallmann syndrome:** Schwanzel-Fukuda, M., Pfaff, D.W. (1989).
    "Origin of luteinizing hormone-releasing hormone neurons."
    *Nature* 338:161–164. (Tract aplasia accompanying bulb agenesis.)
*   **Pars externa within the tract:** Schoenfeld, T.A., Macrides, F.
    (1984). "Topographic organization of connections between the main
    olfactory bulb and pars externa of the anterior olfactory nucleus
    in the hamster." *Journal of Comparative Neurology* 227:121–135.
    (Pars externa embedded within the lateral olfactory tract.)
*   **Centrifugal afferents:** Shipley, M.T., Ennis, M. (1996).
    "Functional organization of olfactory system." *Journal of
    Neurobiology* 30:123–176. (Feedback fibers traveling within the
    tract.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Olfactory tract in the olfactory pathway.)
*   NeuroNames — Olfactory tract (right); FMA — Olfactory tract (right
    member).
"""