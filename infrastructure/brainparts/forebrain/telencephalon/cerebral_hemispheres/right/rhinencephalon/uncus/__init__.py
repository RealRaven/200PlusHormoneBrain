"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon.uncus
===============================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── rhinencephalon
                └── uncus   <-- THIS MODULE

**Primary synonym:** Uncus; uncus hippocampi; uncinate gyrus; hook of
the parahippocampal gyrus; "the hook."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A **gyral
landmark** — the medial-most, hook-like anterior end of the
parahippocampal gyrus.
**Part of:** The **olfactory–limbic junction** at the gyral level —
the surface region that carries primary olfactory cortex **over** the
amygdala and hippocampal head.
**Structural parent:** ``.../right/rhinencephalon/`` → **direct child** of
the rhinencephalon container.
**Structural children:** **None.** This is a **leaf** module. The
uncal subdivisions (semilunar gyrus, ambient gyrus, uncal apex, uncal
notch) and the **contents** of the uncus — piriform and periamygdaloid
cortex on the surface; amygdala and hippocampal head beneath — are
documented as **prose**, not as structural children.
**Boundary status (structural type):** **Boundary case — a gyral
landmark, not a tissue-type-defined structure.** The uncus is the
**only rhinencephalon leaf** defined by its **gyral surface** rather
than by a tissue type. Every other leaf is a cortical area
(``piriform_cortex``, ``periamygdaloid_cortex``), a white-matter bundle
(``olfactory_tract``), a grey-matter nucleus (``anterior_olfactory_nucleus``),
or a laminated relay (``olfactory_bulb``). The uncus is a **named
region** whose **contents are heterogeneous** — primary olfactory
cortex on the surface, amygdala and hippocampal head beneath. Consumers
must not treat the uncus as a homogeneous structure.
**Boundary status (parahippocampal gyrus):** **Boundary case — the
anterior hooked end of the parahippocampal gyrus, wired separately.**
The uncus is the **medial, hooked anterior end** of the
parahippocampal gyrus. The tree splits them: the parahippocampal gyrus
proper is under ``cortex/temporal/gyri/parahippocampal_gyrus/``; the
uncus is here under ``rhinencephalon/``. This is a **deliberate
boundary choice** emphasizing the uncus's olfactory identity over its
gyral identity. Consumers iterating temporal gyri and expecting the
uncus there will **miss it**.
**Boundary status (surface cortex):** **Boundary case — carries
piriform and periamygdaloid cortex on its surface, but those are
siblings.** The uncus's **surface** is primary olfactory cortex —
piriform anteriorly, periamygdaloid superiorly. Those cortices are
**sibling leaves** of the uncus, not children. Consumers that need the
surface cortex should resolve ``piriform_cortex`` and
``periamygdaloid_cortex``; the uncus is the **gyral region** that
carries them.
**Boundary status (deep contents):** **Boundary case — contains the
amygdala and hippocampal head, but those are under ``subcortical/``.**
The uncus's **deep** contents are the **amygdala** (corticomedial and
basolateral nuclei) and the **hippocampal head** (CA1, CA3, dentate
gyrus). Those are wired under
``subcortical/medial_temporal_lobe/amygdala/`` and
``subcortical/medial_temporal_lobe/hippocampus/``, **not** under the
uncus. The uncus is the **gyral surface over them**; it is not their
parent.
**Boundary status (entorhinal):** **Boundary case — blends into the
entorhinal cortex posteriorly, but entorhinal is separate.** The
uncus's **posterior part** (ambient gyrus) blends into the
**entorhinal cortex**, which is wired separately under
``cortex/temporal/gyri/entorhinal_cortex/``. The boundary is
**cytoarchitecturally graded**, not sharp.
**Boundary status (Brodmann):** **Not a Brodmann area.** The uncus is
a **gyral landmark**, not a cytoarchitectonic area. Brodmann areas 28,
34, and 27 cover parts of the uncal surface, but those are wired
separately under ``cortex/temporal/brodmann_areas/``. Do not conflate
the gyral landmark with the Brodmann-area abstractions.

Overview
--------
The uncus is the **medial-most, hook-like anterior end** of the
parahippocampal gyrus — a small, curved region on the **medial
temporal surface** that protrudes medially toward the
**tentorial edge**. It is the **olfactory–limbic junction at the
gyral level**: its **surface** is primary olfactory cortex (piriform
and periamygdaloid), its **deep contents** are the amygdala and
hippocampal head, and its **posterior continuation** is the entorhinal
cortex.

**The uncus is a surface region, not a homogeneous structure.** This
is its defining anatomical fact. Its **surface cortex** is olfactory;
its **deep contents** are limbic; its **medial edge** is the
tentorial edge; and its **posterior continuation** is the
parahippocampal gyrus. The uncus is a **named region** whose identity
changes depending on **which layer** you examine — and the tree wires
it as a **single leaf** because that is how it is named in the
literature, not because it is structurally homogeneous.

**The tree places the uncus under the rhinencephalon, not under the
temporal gyri.** This is a **deliberate boundary choice** that
emphasizes the uncus's **olfactory identity** — its surface carries the
primary olfactory cortex — over its **gyral identity** — it is the
anterior end of the parahippocampal gyrus. Consumers iterating
``cortex/temporal/gyri/parahippocampal_gyrus/`` and expecting to find
the uncus there will **miss it**. Consumers iterating the rhinencephalon
and expecting a cortical area will find a **gyral surface region**
instead. Both are correct for their framing; the tree has chosen the
olfactory framing.

**The uncus is the classic substrate for uncinate fits.** Seizures
arising in the uncus or its adjacent cortex produce **olfactory and
gustatory auras** — the "uncinate fit" — which are among the most
recognizable **focal seizure auras** in neurology. The aura is the
uncus's **signature olfactory clinical association**.

**The uncus is also the structure that herniates.** In **uncal
(transtentorial) herniation**, the uncus is displaced **medially and
inferiorly over the tentorial edge** by a supratentorial mass,
compressing the **midbrain**, **oculomotor nerve**, and **posterior
cerebral artery**. This is a **neurosurgical emergency** and arguably
the uncus's **most medically critical clinical association** — more
time-sensitive than the olfactory aura, though less "olfactory" in
character. The module documents both.

**The uncus is not the amygdala, not the hippocampus, and not the
piriform or periamygdaloid cortex.** It is the **gyral surface** that
carries the piriform and periamygdaloid cortex on its surface and
overlies the amygdala and hippocampal head beneath. Consumers must not
resolve any of those structures through the uncus; they live in their
own modules, and the uncus's relationship to them is **topographic**
(the uncus is the surface over them), not **structural** (they are not
its children).

Subdivisions (prose, not structural children)
---------------------------------------------
The uncus is classically divided into **subdivisions** whose boundaries
are **gyral and sulcal**, not cytoarchitectural:

*   **Semilunar gyrus** (gyrus semilunaris) — the **anterosuperior**
    part of the uncus, overlying the amygdala. Its **surface** is
    **periamygdaloid cortex**. It is the **most olfactory** part of
    the uncal surface.

*   **Ambient gyrus** (gyrus ambiens) — the **posterior** part of the
    uncus, continuous with the **parahippocampal gyrus** posteriorly.
    Its **surface** is **entorhinal cortex**. It is the **most
    limbic** part of the uncal surface.

*   **Uncal apex** — the **medial-most point** of the uncus, the part
    that protrudes toward the tentorial edge. It is the part that
    **herniates** in transtentorial herniation.

*   **Uncal notch** — the **cleft** between the semilunar and ambient
    gyri. It is a **gyral landmark**, not a functional boundary.

*   **Uncal sulcus** — the **sulcus** separating the uncus from the
    ambient gyrus in some descriptions. Its prominence is variable.

*   **Intralimbic gyrus** — a small gyrus sometimes described within
    the uncal notch; its presence and prominence are variable.

**These subdivisions are prose, not structural children.** The tree
does **not** wire them as sub-modules. Consumers that need
subdivision-level resolution should consult the references, not the
tree. The boundaries between subdivisions — and between the uncus and
its neighbors (parahippocampal gyrus posteriorly, entorhinal cortex
posteriorly, amygdala deeply) — are **graded**, not sharp.

Surface vs. Deep Contents (prose, not structural children)
----------------------------------------------------------
The uncus's **contents** are layered, and the layers belong to
**different modules**:

*   **Surface (olfactory cortex):**
    *   **Anterior surface** → **piriform cortex**
        (``rhinencephalon/piriform_cortex/``).
    *   **Superior surface** (semilunar gyrus) → **periamygdaloid
        cortex** (``rhinencephalon/periamygdaloid_cortex/``).
    *   **Posterior surface** (ambient gyrus) → **entorhinal cortex**
        (``cortex/temporal/gyri/entorhinal_cortex/``).

*   **Deep (limbic structures):**
    *   **Amygdala** — the **corticomedial** and **basolateral**
        nuclei lie beneath the semilunar gyrus
        (``subcortical/medial_temporal_lobe/amygdala/``).
    *   **Hippocampal head** — CA1, CA3, and the dentate gyrus lie
        beneath the posterior uncus
        (``subcortical/medial_temporal_lobe/hippocampus/``).
    *   **Temporal horn of the lateral ventricle** — lies beneath the
        uncus, between it and the hippocampus
        (``.../lateral_ventricles/``).

**These contents are prose, not structural children.** The tree does
**not** wire them as uncus children. The uncus is the **gyral surface**
over them; they belong to their own modules, and the uncus's
relationship to them is **topographic**, not **structural**. A
consumer that resolves the uncus and expects to find the amygdala or
hippocampus as children will be **misled**; a consumer that resolves
the amygdala or hippocampus and expects to find the uncus as a parent
will be **equally misled**. The uncus is the **surface region** they
sit beneath, not their container.

Function in the Human Brain
---------------------------
The uncus's functions are **surface-dependent** and **region-dependent**
— there is no single "uncus function":

*   **Olfactory Reception (Surface Function):** The uncus's **surface**
    carries piriform and periamygdaloid cortex — both **primary
    olfactory cortical areas** receiving **lateral olfactory stria**
    input. The uncus **contributes** to **odor identification** and
    **olfactory–limbic relay** via its surface cortex, but the
    **processing** happens in the piriform and periamygdaloid modules,
    not in the uncus per se.

*   **Olfactory Aura Generation (Epileptic Function):** The uncus is a
    **classic substrate for uncinate fits** — focal seizures with
    **olfactory and gustatory auras**. The aura is the uncus's
    **signature epileptic function**, and it is the reason the uncus
    is clinically recognized as an **olfactory structure**.

*   **Topographic Relationship to Limbic Structures (Structural
    Function):** The uncus **overlies** the amygdala and hippocampal
    head, and its **medial edge** sits at the **tentorial edge**.
    This topographic position is not a "function" in the
    physiological sense, but it is the uncus's **defining structural
    role** — it is the **surface** at the olfactory–limbic junction.

*   **Transtentorial Herniation (Pathological Function):** The uncus
    is the **structure that herniates** over the tentorial edge in
    **uncal herniation** — a **mass-effect** phenomenon, not a
    physiological function. See *Associated Disorders* for the full
    herniation syndrome.

*   **NOT a processor in its own right.** The uncus is a **gyral
    surface**, not a functional unit. Its surface cortex processes
    olfaction (documented in the piriform and periamygdaloid modules);
    its deep contents process limbic functions (documented in the
    amygdala and hippocampus modules). The uncus itself is the
    **topographic region** that carries them — it is not a processor.

**The unifying theme:** the uncus is the **gyral surface at the
olfactory–limbic junction**. It is **olfactory on its surface**,
**limbic beneath**, and **mechanically critical at the tentorial
edge**. No single functional label fits; the uncus's identity is
**layered**, and the module documents each layer in its own module.

Associated Disorders
--------------------
Uncal disorders are **olfactory, epileptic, and herniation-related** —
and the herniation association is the **most time-critical**:

*   **Uncinate Fits (Temporal Lobe Epilepsy):** The uncus is a
    **classic epileptogenic substrate**. **Olfactory and gustatory
    auras** ("uncinate fits") arise from uncinate discharges. The
    seizure itself propagates into the **amygdala** and
    **hippocampus** (documented under ``subcortical/``), but the
    **aura** is uncinate. **Uncinate fits** are among the most
    recognizable **focal seizure auras** in neurology.

*   **Uncal (Transtentorial) Herniation — the signature emergency:**
    A **supratentorial mass** (tumor, hemorrhage, edema) raises
    intracranial pressure and displaces the **uncus medially and
    inferiorly over the tentorial edge**. **For this right uncus, the
    herniation is driven by a right-sided mass.** The herniated right
    uncus compresses:
    *   **Ipsilateral (right) oculomotor nerve (CN III)** →
        **right dilated pupil** (mydriasis), **right ptosis**,
        **right ophthalmoplegia** (down-and-out eye). This is the
        **earliest and most reliable sign** of uncal herniation.
    *   **Ipsilateral (right) cerebral peduncle** → **left
        hemiparesis** (corticospinal tract compression).
        **Kernohan's notch phenomenon**: if the midbrain is displaced
        **leftward** against the **left** tentorial edge, the **left**
        cerebral peduncle is compressed →
        **paradoxical left hemiparesis** — a false localizing sign
        that is **ipsilateral** to the right-sided mass.
    *   **Ipsilateral (right) posterior cerebral artery (PCA)** →
        **right occipital infarct** (left homonymous hemianopia).
    *   **Midbrain reticular formation** → **decreased
        consciousness** (from drowsiness to coma).
    *   **Contralateral (left) cerebral peduncle** (in later stages,
        direct compression) → **bilateral hemiparesis**.

    **Uncal herniation is a neurosurgical emergency.** The uncus's
    **medial edge** is the structure that herniates, and the
    **herniation syndrome** is the most time-critical clinical
    association of any rhinencephalon leaf.

*   **Amygdala and Hippocampal Pathology (Deep Contents):**
    **Kluver-Bucy syndrome** (amygdala), **fear conditioning deficits**
    (amygdala), **temporal lobe epilepsy proper** (hippocampus), and
    **hippocampal amnesia** (hippocampus) are disorders of the
    uncus's **deep contents** — documented under ``subcortical/``,
    **not** here. The uncus is the **surface over** those structures;
    it is not their syndrome substrate.

*   **Olfactory Dysfunction:** As the surface region carrying primary
    olfactory cortex, the uncus can be **affected** in **anosmia**,
    **hyposmia**, and **olfactory agnosia** — but its contribution
    is **secondary** to the piriform cortex and bulb. It is a
    **contributor**, not the primary substrate.

**What is NOT here:** The uncus is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala proper), **fear conditioning**
(amygdala proper), **temporal lobe epilepsy proper** (hippocampus),
**hippocampal amnesia** (hippocampus), or **semantic dementia**
(anterior temporal neocortex). It contributes the **olfactory aura**
and the **herniation syndrome** — both are **uncus-specific**, and
both are documented above. The rest belongs to its deep contents,
documented elsewhere.

Lateralization Notes
--------------------
This is the **right** uncus module. The uncus is **bilaterally
symmetric** and **functionally non-lateralized** in its physiological
roles — but its **pathological** role (herniation) is **asymmetric by
nature**:

*   **No Lateralized Physiological Function:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the uncus has **no documented left-lateralized or
    right-lateralized function**. Its surface cortex (piriform,
    periamygdaloid) and its deep contents (amygdala, hippocampus) are
    **bilaterally symmetric**.

*   **Ipsilateral Olfactory Projection:** Each uncus's surface
    receives **ipsilateral** LOS input from its own bulb. The two
    sides are **functionally symmetric** for olfactory reception.

*   **Asymmetric Pathology (Herniation):** **Uncal herniation** is
    typically **unilateral** (from a unilateral mass), and the signs
    are **ipsilateral** to the herniation — **ipsilateral** dilated
    pupil, **ipsilateral** PCA infarct, **contralateral** hemiparesis
    (with the **Kernohan's notch exception** producing **ipsilateral**
    hemiparesis). **For this right uncus, the herniation is driven
    by a right-sided mass, and the herniated right uncus produces
    right-sided CN III and PCA signs and left hemiparesis** (with
    Kernohan's notch resolving to paradoxical left hemiparesis from
    midbrain displacement against the left tentorial edge). This is
    an **asymmetric clinical entity** arising from a **symmetric
    structure** — a subtle point worth flagging. A consumer that
    reads "right uncus" and expects right-sided herniation signs
    should be aware that **a right uncus herniates from a right-sided
    mass**, and that **left-sided masses herniate the left uncus**.

*   **No Amygdala or Hippocampal Lateralization Import:** The
    **right amygdala** is sometimes reported as **more involved in
    fear processing** than the left, and the **left hippocampus** as
    **more involved in verbal memory** than the right — but those are
    **amygdala and hippocampus proper**, documented under
    ``subcortical/``. **Do not import amygdala or hippocampal
    lateralization claims into the right uncus.** In particular, the
    right amygdala's fear-processing association **does not** transfer
    to the right uncus's surface cortex; the uncus is the **gyral
    surface over** the amygdala, not the amygdala itself. The uncus's
    lateralization is **not established** for its physiological roles,
    and its pathological role (herniation) is asymmetric **by
    mechanism**, not by lateralized function.

**A consumer that assumes "right uncus = left uncus" will be
structurally and physiologically correct** — the two sides are
symmetric, and no lateralized function has been demonstrated. But a
consumer that assumes **"right uncus herniation = right-sided
neurological signs"** must be aware that **the herniation is
ipsilateral to the mass**, not to the uncus's hemisphere **as a
rule** — the right uncus herniates from a **right-sided** mass, and
its CN III and PCA signs are **right-sided**, while the hemiparesis is
**left-sided** (contralateral), or **left-sided and paradoxical** under
Kernohan's notch. This is a **mechanistic asymmetry**, not a
**functional-lateralization** asymmetry.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The uncus's
    **surface cortex** (piriform, periamygdaloid, entorhinal) and its
    **deep contents** (amygdala, hippocampus) are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The uncal subdivisions
    (semilunar gyrus, ambient gyrus, uncal apex, uncal notch) are
    documented as **prose**, not as sub-modules. The uncal **contents**
    (piriform, periamygdaloid, entorhinal, amygdala, hippocampus) are
    documented as **prose and sibling redirects**, not as children.
    Consumers must not assume either exists as children; resolve
    subdivisions through the references, and resolve contents through
    their own modules.
*   **Gyral landmark — not a tissue-type-defined structure.** The
    uncus is a **named region** whose **contents are heterogeneous**.
    It is the **only rhinencephalon leaf** of this kind. Consumers
    must not treat the uncus as a homogeneous cortical area, white
    matter, or nucleus.
*   **Boundary case — the anterior hooked end of the parahippocampal
    gyrus, wired separately.** The parahippocampal gyrus proper is
    under ``cortex/temporal/gyri/parahippocampal_gyrus/``; the uncus
    is here under ``rhinencephalon/``. This is a **deliberate boundary
    choice** emphasizing the uncus's olfactory identity over its gyral
    identity.
*   **Boundary case — surface cortex are siblings, not children.**
    The uncus's **surface** is piriform and periamygdaloid cortex
    (siblings), and its **posterior continuation** is entorhinal
    cortex (under ``cortex/temporal/gyri/``). None are uncus
    children.
*   **Boundary case — deep contents are under ``subcortical/``, not
    children.** The uncus's **deep contents** are the amygdala and
    hippocampal head (under
    ``subcortical/medial_temporal_lobe/``). None are uncus children.
*   **Boundary case — not a Brodmann area.** BA27, BA28, and BA34
    cover parts of the uncal surface but are wired separately under
    ``cortex/temporal/brodmann_areas/``. The uncus is a **gyral
    landmark**, not a cytoarchitectonic area.
*   **No ``AREA_PATHS`` hop.** The uncus is a local leaf under the
    rhinencephalon, not a cross-listed leaf.
*   **No nested cross-listing.** The uncus has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with left uncus.** Right and left uncus
    modules are **structurally identical** — same leaf status, same
    subdivisions documented as prose, same surface/deep boundary
    flags, same herniation-asymmetric-by-mechanism caveat, same
    non-lateralized caveat. **The herniation asymmetry paragraph is
    direction-reversed** — the right module documents herniation from
    a right-sided mass, with right CN III and PCA signs and left
    hemiparesis.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon import uncus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.rhinencephalon."
        "uncus"
    )

**Do not** assume the uncus is under ``cortex/temporal/gyri/``. It is
a **gyral surface** leaf under the **rhinencephalon**, not under the
temporal gyri. A consumer that iterates
``cortex/temporal/gyri/parahippocampal_gyrus/`` and expects to find
the uncus there will **miss it**.

**Do not** assume the uncus has structural children. It is a **leaf**.
The uncal subdivisions (semilunar gyrus, ambient gyrus, uncal apex,
uncal notch) are **prose only** — they are not wired as modules.

**Do not** assume the uncus **contains** the piriform cortex,
periamygdaloid cortex, amygdala, or hippocampus as children. They are
**siblings** (piriform, periamygdaloid) or **separate modules**
(amygdala, hippocampus under ``subcortical/``). The uncus is the
**gyral surface** that carries or overlies them; it is not their
parent.

**Do not** import **amygdala or hippocampal lateralization claims**
into the uncus. The right uncus is not the right amygdala — the right
amygdala's fear-processing association **does not** transfer to this
module.

**Do not** read "right uncus" as implying "right-sided neurological
signs in herniation." The right uncus herniates from a **right-sided
mass**, producing **right CN III and PCA signs** and **left
hemiparesis** (or paradoxical **left** hemiparesis under Kernohan's
notch).

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        uncus_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon."
            f"uncus"
        )
        # resolve uncus_path through the memory/recall layer

Reaching the uncus's surface cortex (recommended consumer pattern)::

    # The uncus's surface cortex is NOT a child of the uncus. Resolve
    # the surface cortices at their own paths:
    #
    #   rhinencephalon.piriform_cortex          (anterior surface)
    #   rhinencephalon.periamygdaloid_cortex    (superior surface)
    #   cortex.temporal.gyri.entorhinal_cortex  (posterior surface)
    #
    # These are SIBLINGS or SEPARATE MODULES, not uncus children.

Reaching the uncus's deep contents (recommended consumer pattern)::

    # The uncus's deep contents are NOT children of the uncus. Resolve
    # them at their own paths:
    #
    #   subcortical.medial_temporal_lobe.amygdala
    #   subcortical.medial_temporal_lobe.hippocampus
    #   .../lateral_ventricles/right   (temporal horn)
    #
    # These are SEPARATE MODULES under subcortical/, not uncus
    # children.

Reaching the parahippocampal gyrus (recommended consumer pattern)::

    # The uncus is the ANTERIOR HOOKED END of the parahippocampal
    # gyrus, but the gyrus proper is a SEPARATE module:
    #
    #   cortex.temporal.gyri.parahippocampal_gyrus
    #
    # The uncus is under rhinencephalon/ (olfactory identity); the
    # gyrus proper is under cortex/temporal/gyri/ (gyral identity).

Subdivision-level detail (not wired — consult references)::

    # The uncal subdivisions are prose, not modules:
    #   semilunar gyrus   -> anterosuperior; periamygdaloid surface
    #   ambient gyrus     -> posterior; entorhinal surface
    #   uncal apex        -> medial-most point; herniates
    #   uncal notch       -> cleft between semilunar and ambient
    #
    # Do not attempt to resolve these as sub-paths of the uncus.

References
----------
*   **Canonical anatomy:** Amaral, D.G., Insausti, R. (1990). "The
    hippocampal formation." In *The Human Nervous System*
    (Paxinos, G., ed.). (Uncal anatomy; relation to amygdala,
    hippocampus, and parahippocampal gyrus.)
*   **Uncal anatomy and subdivisions:** Duvernoy, H.M. (2005). *The
    Human Hippocampus*, 3rd ed. (Uncal surface, subdivisions, deep
    contents.)
*   **Uncinate fits:** Gloor, P. (1997). *The Temporal Lobe and
    Limbic System*. (Olfactory auras and uncinate seizures; uncal
    substrate.)
*   **Uncal herniation:** Plum, F., Posner, J.B. (1980). *The
    Diagnosis of Stupor and Coma*, 3rd ed. (Transtentorial herniation
    syndrome; CN III, cerebral peduncle, PCA compression.)
*   **Kernohan's notch phenomenon:** Kernohan, J.W., Woltman, H.W.
    (1929). "Incisura of the crus due to contralateral brain tumor."
    *Archives of Neurology and Psychiatry* 21:274–287. (Paradoxical
    ipsilateral hemiparesis.)
*   **Olfactory cortex:** Price, J.L. (1990). "Olfactory system." In
    *The Human Nervous System* (Paxinos, G., ed.). (Piriform and
    periamygdaloid cortex on the uncal surface.)
*   **Human olfactory cortex:** Doty, R.L. (2015). *Handbook of
    Olfaction and Gustation*, 3rd ed. (Uncal surface as primary
    olfactory cortex.)
*   **Brodmann areas 27, 28, 34:** Brodmann, K. (1909).
    *Vergleichende Lokalisationslehre der Grosshirnrinde*. (Brodmann
    areas covering the uncal surface; note the tree wires them
    separately.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the right uncus.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Uncus in the olfactory and limbic pathways.)
*   NeuroNames — Uncus (right); FMA — Uncus (right member).
"""