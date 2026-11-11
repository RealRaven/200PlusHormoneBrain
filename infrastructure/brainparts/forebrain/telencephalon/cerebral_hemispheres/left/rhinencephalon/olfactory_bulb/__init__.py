"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.rhinencephalon.olfactory_bulb
========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── rhinencephalon
                └── olfactory_bulb   <-- THIS MODULE

**Primary synonym:** Olfactory bulb (OB); bulbus olfactorius; main
olfactory bulb (MOB).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**laminated cortical-like structure** — the **first relay station** of
the olfactory pathway[reference:0].
**Part of:** The **primary olfactory pathway** — the **rostral-most**
telencephalic structure in the olfactory system.
**Structural parent:** ``.../left/rhinencephalon/`` → **direct child** of
the rhinencephalon container.
**Structural children:** **None.** This is a **leaf** module. The
bulb's **layers** and **glomeruli** are documented as **prose and
functional units**, not as structural children.
**Boundary status:** **Boundary case — the bulb is a laminated
"cortex-like" structure, not a homogeneous nucleus.** Classical
anatomy treats the bulb as a **laminated cortical region** (five or
six layers), while the tree treats it as a **single leaf**. Consumers
must not assume the bulb is a uniform nucleus; its function is
**layer-specific and glomerulus-specific**.
**Boundary status (human):** **Boundary case — the "microsmatic
human" label is contested.** Humans were long classified as
**microsmatic** because the bulb is **proportionately smaller**
relative to the brain than in macrosmatic mammals[reference:1].
Modern work argues that **absolute bulb size and neuron number** are
**comparable to many mammals**, and that **poor human olfaction is a
19th-century myth**[reference:2]. The tree treats the bulb as a
**fully functional primary olfactory structure**, not a vestigial one.

Overview
--------
The olfactory bulb is the **first central relay** of the olfactory
system and the **only sensory relay that projects directly to cortex
without a thalamic intermediary**[reference:3]. It sits on the
**ventral surface of the frontal lobe** in the olfactory sulcus of the
medial orbitofrontal cortex, connected to the hemisphere by the
**olfactory tract**[reference:4].

**The human bulb is small but not vestigial.** In young adults it is
approximately **50–60 mm³ per side**[reference:5], containing roughly
**8,000 glomeruli and 40,000 mitral cells**[reference:6]. It is
**proportionately smaller** than in macrosmatic mammals, but its
**absolute neuron number** is comparable to many mammals, and its
**intrinsic laminar organization is conserved**[reference:7]. The
"microsmatic human" label reflects **relative scaling**, not
**functional absence** — a distinction the tree preserves.

**The bulb is the site of the first olfactory code.** Olfactory
sensory neurons expressing the **same receptor subtype** converge on
**the same few glomeruli**, creating a **stereotyped glomerular map**
in which each glomerulus receives input from **one receptor type**
[reference:8]. This map is the **functional unit** of the bulb: the
glomerulus is where **peripheral odorant identity** is first
translated into a **central neural representation**.

**Adult neurogenesis in the human bulb is controversial.** In
rodents, the bulb receives **continuous new neurons** from the
subventricular zone. In humans, carbon-dating studies suggest that
**long-term neuronal survival from adult neurogenesis is extremely
limited**[reference:9], and some authors conclude that **human olfactory
function is not neurogenesis-dependent**[reference:10]. The tree does
**not** take a position on this controversy; the bulb is documented as
a **structurally stable relay**, not as a neurogenic structure.

Laminar Architecture (prose, not structural children)
------------------------------------------------------
The bulb has **five well-defined layers**, from superficial to deep
[reference:11]:

*   **Olfactory nerve layer (ONL)** — axons of olfactory sensory
    neurons (OSNs) running on the bulb surface[reference:12].

*   **Glomerular layer (GL)** — the **functional unit** of the bulb.
    OSN axons terminate here on the **apical dendrites of mitral and
    tufted cells**[reference:13]. Each glomerulus receives input from
    **one receptor subtype**[reference:14]. **Periglomerular cells**
    (juxtaglomerular interneurons) modulate transmission within and
    between glomeruli[reference:15].

*   **External plexiform layer (EPL)** — somata of **tufted cells**
    and the **secondary (basal) dendrites** of mitral and tufted
    cells, plus **apical dendrites of granule cells**[reference:16].
    This is where **dendrodendritic reciprocal synapses** between
    mitral/tufted cells and granule cells implement **lateral
    inhibition**.

*   **Mitral cell layer (MCL)** — somata of **mitral cells**, the
    principal **projection neurons** of the bulb[reference:17].

*   **Granule cell layer (GCL)** — **granule cells**, the main
    **inhibitory interneurons** of the bulb, forming reciprocal
    dendrodendritic synapses with mitral/tufted cells.

**Two principal projection-neuron types.** **Mitral cells** (MCL) and
**tufted cells** (EPL) are the **efferent neurons** of the bulb; their
axons form the **olfactory tract** and project to the primary olfactory
cortex[reference:18][reference:19]. They are **functionally similar but
not identical**: tufted cells generally respond to **lower odorant
concentrations** and project to **more anterior** cortical targets,
while mitral cells respond to **higher concentrations** and project
**more broadly**. The tree documents both as **prose**; it does not
split the bulb into mitral and tufted sub-modules.

**These layers and cell types are prose, not structural children.**
The tree does **not** wire ONL, GL, EPL, MCL, or GCL as sub-modules.
Consumers that need laminar resolution should consult the references,
not the tree.

The Olfactory Peduncle Context
------------------------------
The bulb is the **rostral expansion** of the **olfactory peduncle**,
and the tree separates the peduncle's three components into three
sibling leaves:

*   ``olfactory_bulb`` — the **laminated rostral expansion** (this
    module).
*   ``olfactory_tract`` — the **axonal bundle** running caudally.
*   ``anterior_olfactory_nucleus`` — the **grey matter embedded
    within** the tract/peduncle.

**These three are anatomically continuous.** The bulb's **caudal
pole** merges into the **anterior olfactory nucleus** with **no sharp
cytoarchitectural boundary** in many species, and the **olfactory
tract** proper is a mix of **bulb efferents, AON efferents, and AON
dendrites**. The tree's three-way split is a **useful abstraction**,
not a sharp anatomical boundary. A consumer that treats the bulb,
tract, and AON as cleanly separable will **misunderstand the
peduncle** — they are better understood as **regions of a continuous
olfactory peduncle**.

Function in the Human Brain
---------------------------
The bulb's functions are **early olfactory coding and relay**:

*   **First Central Relay (Primary Function):** The bulb receives the
    **first synapse** of the olfactory pathway — OSN axons terminate
    in glomeruli on mitral/tufted dendrites[reference:20]. It is the
    **first site of central olfactory processing**.

*   **Glomerular Odor Map (Functional Unit):** Each glomerulus
    receives input from **one receptor subtype**, creating a
    **stereotyped spatial map** of odorant identity
    [reference:21]. This map is the **functional unit** of the bulb,
    not a structural child.

*   **Lateral Inhibition and Contrast Enhancement:** **Granule cells**
    and **periglomerular cells** implement **dendrodendritic
    reciprocal inhibition** that **sharpens** the glomerular response
    and enhances **odorant contrast**[reference:22].

*   **Concentration Coding:** Mitral and tufted cells have **different
    concentration sensitivities**, allowing the bulb to encode
    **odorant intensity** across a wide dynamic range.

*   **Centrifugal Modulation:** The bulb receives **centrifugal
    afferents** from the **anterior olfactory nucleus**, **diagonal
    band of Broca**, **locus ceruleus** (noradrenergic), and **raphe
    nuclei** (serotonergic), which modulate **glomerular gain** and
    **attention-dependent olfactory processing**[reference:23].

*   **NOT a primary olfactory cortex.** The bulb is a **relay and
    early-coding structure**; **odor identification and memory** are
    properties of the **piriform cortex** and its limbic targets,
    documented elsewhere. The bulb **shapes** the olfactory signal; it
    does not **interpret** it.

**The unifying theme:** the bulb is the **first central olfactory
relay** and the **site of the glomerular odor map**. It is **not** a
primary sensory cortex in the classical sense, **not** a limbic
structure, and **not** a motor area. It is a **laminated, glomerular
relay** that transforms **peripheral receptor activity** into a
**central odor representation**.

Associated Disorders
--------------------
Olfactory bulb disorders are **primary olfactory**:

*   **Post-Viral Anosmia (COVID-19 and Others):** COVID-19 anosmia
    likely arises from **infection of non-neuronal support cells**
    (sustentacular cells, pericytes) rather than direct neuronal
    infection, with **bulbar involvement** contributing to persistent
    dysfunction[reference:24]. **Olfactory bulb volume reduction** and
    **shape changes** have been reported in COVID-19 patients
    [reference:25]. Other viruses can damage the bulb directly.

*   **Parkinson's Disease — Braak Stage I:** **α-Synuclein deposits**
    are present in the **olfactory bulb and anterior olfactory
    nucleus at Braak stage I**, **before** substantia nigra
    involvement (stage III)[reference:26][reference:27]. The bulb is a
    **gateway** for prion-like spread of PD pathology.

*   **Alzheimer's Disease:** The bulb and **anterior olfactory
    nucleus** are among the **earliest affected structures**,
    contributing to **prodromal olfactory deficits**. **Neurofibrillary
    tangles** and **amyloid plaques** appear in the bulb early in the
    disease course.

*   **Kallmann Syndrome — Bulb Agenesis:** **GnRH neurons** fail to
    migrate from the nasal placode to the hypothalamus because the
    **olfactory bulb does not form**; the result is **anosmia plus
    hypogonadotropic hypogonadism**[reference:28][reference:29].
    **Olfactory bulb aplasia** is the **structural hallmark** of
    Kallmann syndrome.

*   **Age-Related Olfactory Decline:** Glomerular number and mitral
    cell number **decrease progressively with age**; in individuals
    over 90, **fewer than 30%** of glomeruli and mitral cells remain
    recognizable[reference:30]. This contributes to **presbyosmia**.

*   **Olfactory Groove Meningioma:** Compression of the bulb/tract
    produces **unilateral anosmia**, often unnoticed, and **Foster
    Kennedy syndrome** if large.

**What is NOT here:** The bulb is **not** the substrate for
**temporal lobe epilepsy** (hippocampal/amygdalar), **Kluver-Bucy
syndrome** (amygdala), **semantic dementia** (anterior temporal
neocortex), or **Wernicke's aphasia** (BA22). Its clinical footprint
is **olfactory**, and even there it is a **gateway and early relay**,
not the primary substrate for odor identification (piriform cortex) or
odor memory (amygdala/hippocampus).

Lateralization Notes
--------------------
This is the **left** olfactory bulb module. The bulb is **not
functionally lateralized in the classical sense**, but **volume
asymmetries** are real and behaviorally meaningful:

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the olfactory bulb has **no documented left-lateralized or
    right-lateralized function**.

*   **Volume Asymmetry Correlates with Sensitivity:** In a study of
    164 healthy volunteers, **right-sided bulb volume was larger** in
    39 cases, **left-sided** in 29; subjects with a **larger right
    bulb** were **more sensitive to right-nostril stimulation**, and
    those with a **larger left bulb** were **more sensitive on the
    left**[reference:31]. This is a **volume–function correlation**, not
    a **lateralized specialization**.

*   **Functional Symmetry (Presumed):** Each bulb projects
    **ipsilaterally** to the piriform cortex, and the two sides are
    **functionally symmetric** for odor detection and discrimination.
    **Unilateral anosmia** from a unilateral bulb lesion is the
    clinical expression of this symmetry.

**A consumer that assumes "left bulb = right bulb" will be
approximately correct functionally, but not volumetrically.** The two
bulbs are **structurally similar but not identical in volume**, and
volume differences can track **nostril-specific sensitivity**. Do not
import **cortical-level** lateralization claims into the bulb; the
bulb's lateralization is **volumetric and peripheral**, not
**functional-specialization**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The bulb's
    projections to the piriform cortex, periamygdaloid cortex,
    amygdala, and entorhinal cortex are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The bulb's **layers**
    (ONL, GL, EPL, MCL, GCL) and **cell types** (mitral, tufted,
    periglomerular, granule) are documented as **prose**, not as
    sub-modules. Consumers must not assume they exist as children;
    resolve laminar detail through the references.
*   **Boundary case — laminated "cortex-like" structure, not a uniform
    nucleus.** The bulb has **layer-specific and glomerulus-specific**
    function. A consumer that treats it as a homogeneous relay will
    **miss the glomerular map and the lateral-inhibition circuitry**.
*   **Boundary case — the "microsmatic human" label is contested.**
    The bulb is **proportionately smaller** than in macrosmatic
    mammals but **absolutely comparable in neuron number**. Do not
    treat the human bulb as **vestigial**.
*   **Adult neurogenesis — flagged, not resolved.** Human adult bulbar
    neurogenesis is **controversial**[reference:32]. The tree documents
    the bulb as a **structurally stable relay**, not as a
    **neurogenic structure**. Do not assume rodent neurogenesis
    findings transfer to humans.
*   **Continuous with the olfactory peduncle — flagged.** The bulb's
    caudal pole merges into the **anterior olfactory nucleus** and the
    **olfactory tract**. Consumers must not assume sharp boundaries
    among ``olfactory_bulb``, ``olfactory_tract``, and
    ``anterior_olfactory_nucleus``.
*   **No ``AREA_PATHS`` hop.** The bulb is a local leaf under the
    rhinencephalon, not a cross-listed leaf.
*   **No nested cross-listing.** The bulb has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with right olfactory bulb.** Left and right
    bulb modules are **structurally identical** — same leaf status,
    same laminar prose, same glomerular-map note, same
    microsmatic/human caveat. **Volume asymmetry** is documented as a
    **functional fact**, not as a structural difference.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.rhinencephalon import olfactory_bulb

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.rhinencephalon."
        "olfactory_bulb"
    )

**Do not** assume the bulb has structural children. It is a **leaf**.
The layers (ONL, GL, EPL, MCL, GCL) and cell types (mitral, tufted,
periglomerular, granule) are **prose only** — they are not wired as
modules.

**Do not** assume the bulb is a uniform nucleus. It is a **laminated,
glomerular structure** whose function is **layer-specific and
glomerulus-specific**. Consumers that need laminar or glomerular
resolution must consult the references.

**Do not** assume sharp boundaries among ``olfactory_bulb``,
``olfactory_tract``, and ``anterior_olfactory_nucleus``. The peduncle
is a **continuous structure**; the tree's three-way split is a
**useful abstraction**.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        bulb_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon."
            f"olfactory_bulb"
        )
        # resolve bulb_path through the memory/recall layer

Reaching the bulb's downstream targets (recommended consumer
pattern)::

    # The bulb projects to structures documented elsewhere in the tree.
    # Resolve them at their own paths:
    #
    #   rhinencephalon.piriform_cortex
    #   rhinencephalon.periamygdaloid_cortex
    #   subcortical.medial_temporal_lobe.amygdala
    #   cortex.temporal.gyri.entorhinal_cortex
    #   rhinencephalon.anterior_olfactory_nucleus
    #
    # These are NOT bulb children. They are downstream targets.

Laminar / glomerular detail (not wired — consult references)::

    # The bulb's layers are prose, not modules:
    #   ONL  -> olfactory nerve layer (OSN axons)
    #   GL   -> glomerular layer (functional unit; one receptor per glomerulus)
    #   EPL  -> external plexiform layer (tufted cells; dendrodendritic synapses)
    #   MCL  -> mitral cell layer (principal projection neurons)
    #   GCL  -> granule cell layer (inhibitory interneurons)
    #
    # Do not attempt to resolve these as sub-paths of the bulb module.

References
----------
*   **Canonical anatomy:** Doty, R.L. (2015). *Handbook of Olfaction
    and Gustation*, 3rd ed. (Human olfactory bulb anatomy, layers,
    and function.)
*   **Human bulb morphometry:** Meisami, E., Mikhail, L., Baim, D.,
    Bhatnagar, K.P. (1998). "Human olfactory bulb: aging of glomeruli
    and mitral cells and a search for the accessory olfactory bulb."
    *Annals of the New York Academy of Sciences* 855:708–715.
    (8,000 glomeruli, 40,000 mitral cells; age-related decline.)
*   **Human bulb volume:** Turetsky, B.I., et al. (2000). "Volumetric
    and metric assessment of the olfactory bulb in schizophrenia."
    *Biological Psychiatry* 47:105–113. (50–60 mm³ per side.)
*   **Laminar organization:** Shepherd, G.M., Chen, W.R., Greer, C.A.
    (2004). "Olfactory bulb." In *The Synaptic Organization of the
    Brain*, 5th ed. (Definitive laminar and synaptic anatomy.)
*   **Glomerular map:** Mori, K., Nagao, H., Yoshihara, Y. (1999).
    "The olfactory bulb: coding and processing of odor molecule
    information." *Science* 286:711–715. (One receptor per glomerulus;
    glomerular map.)
*   **Microsmatic debate:** McGann, J.P. (2017). "Poor human olfaction
    is a 19th-century myth." *Science* 356:eaam7263. (Human olfactory
    ability is comparable to many mammals.)
*   **Adult neurogenesis:** Bergmann, O., et al. (2012). "The age of
    olfactory bulb neurons in humans." *Neuron* 74:634–639. (Adult
    human bulbar neurogenesis is extremely limited.)
*   **COVID-19:** Brann, D.H., et al. (2020). "Non-neuronal expression
    of SARS-CoV-2 entry genes in the olfactory system suggests
    mechanisms underlying COVID-19-associated anosmia." *Science
    Advances* 6:eabc5801. (Support-cell infection, not neuronal.)
*   **Parkinson's disease:** Braak, H., et al. (2003). "Staging of
    brain pathology related to sporadic Parkinson's disease."
    *Neurobiology of Aging* 24:197–211. (Bulb at Braak stage I.)
*   **Kallmann syndrome:** Schwanzel-Fukuda, M., Pfaff, D.W. (1989).
    "Origin of luteinizing hormone-releasing hormone neurons."
    *Nature* 338:161–164. (GnRH migration failure and bulb agenesis.)
*   **Lateralization:** Hummel, T., et al. (2013). "Lateralized
    differences in olfactory bulb volume relate to lateralized
    differences in olfactory function." *Neuroscience* 237:51–55.
    (Volume asymmetry correlates with nostril-specific sensitivity.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Olfactory bulb in the olfactory pathway.)
*   NeuroNames — Olfactory bulb (left); FMA — Olfactory bulb (left
    member).
"""