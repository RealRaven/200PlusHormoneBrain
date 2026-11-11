"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.rhinencephalon
===========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            ├── cortex
            ├── rhinencephalon   <-- THIS MODULE
            ├── subcortical
            └── white_matter

**Primary synonym:** Rhinencephalon; olfactory brain; smell brain;
olfactory lobe (classical).
**Classical designation:** Lobus olfactorius — a lobe-level subdivision
of the cerebral hemisphere in classical anatomy.
**Part of:** The **olfactory system** (exclusively, in this tree's
narrow definition — see *Boundary status* below).
**Structural parent:** ``.../cerebral_hemispheres/right/`` → **sibling of
``cortex/``, ``subcortical/``, and ``white_matter/``**. The rhinencephalon
is a **lobe-level container**, **not** a subregion of ``cortex/``.
**Structural children (six, closed set):**
``anterior_olfactory_nucleus``, ``olfactory_bulb``, ``olfactory_tract``,
``periamygdaloid_cortex``, ``piriform_cortex``, ``uncus``.
**Boundary status:** **Boundary case — narrow olfactory definition,
not the classical full smell-brain.** The tree retains the rhinencephalon
as a lobe-level container but restricts it to **primary olfactory
structures** (bulb, tract, anterior olfactory nucleus, piriform and
periamygdaloid cortex) plus the **uncus** (the olfactory/limbic
junction). The **limbic archipallium** — amygdala, hippocampus, septal
nuclei, olfactory tubercle, anterior perforated substance — is **NOT**
wired here; it lives under ``subcortical/``. Consumers must not assume
the rhinencephalon is the full classical "smell brain + limbic lobe."

Overview
--------
The rhinencephalon ("nose brain") is the part of the telencephalon
devoted to **primary olfactory processing**. In classical anatomy it was
a lobe-level subdivision of the hemisphere that included both the
**olfactory apparatus** and the **archipallial structures**
(hippocampus, septum, amygdala) that phylogenetically share an
olfactory origin. In modern anatomy, the term has largely been
**dissolved**: the olfactory components are treated as the **olfactory
system**, and the archipallial components are treated as the **limbic
system**.

**The tree takes a deliberate middle position.** It retains the
rhinencephalon as a lobe-level container — a sibling of ``cortex/``,
not a child — but restricts its contents to the **primary olfactory
structures proper**: the olfactory bulb, tract, and anterior olfactory
nucleus, the piriform and periamygdaloid cortex, and the uncus. The
limbic archipallium is **excluded** and lives under ``subcortical/``:
the amygdala under ``subcortical/medial_temporal_lobe/amygdala/``, the
hippocampus under ``subcortical/medial_temporal_lobe/hippocampus/``,
the septal nuclei under ``subcortical/basal_forebrain/septal_nuclei/``,
the olfactory tubercle under
``subcortical/basal_forebrain/striatum/ventral_striatum/olfactory_tubercle/``,
and the anterior perforated substance under
``subcortical/basal_forebrain/anterior_perforated_substance/``.

**This is a narrow, defensible definition.** The rhinencephalon here is
the **telencephalic primary olfactory substrate** — the "smell brain"
proper, not the "smell brain + limbic lobe" of older texts. Consumers
that expect the classical grouping (with amygdala and hippocampus as
children) will be **misled**; those structures are elsewhere in the tree.

**Placement outside ``cortex/``.** The rhinencephalon is a **sibling**
of the ``cortex/`` container, not a child. This reflects the
**allocortical** nature of its components: the piriform and
periamygdaloid cortex are three-layered allocortex, not neocortex. The
tree reserves ``cortex/`` for neocortical structures and places the
rhinencephalon directly under ``.../right/`` as a lobe-level subdivision.

Container Contents (closed set of six children)
-----------------------------------------------
The rhinencephalon has **exactly six children** in this tree. Consumers
may iterate them, but should not assume any others exist:

*   **``olfactory_bulb``** — the first relay station, receiving axons
    from olfactory receptor neurons in the olfactory epithelium. In
    humans it is a small, flattened structure on the orbital surface of
    the frontal lobe.

*   **``olfactory_tract``** — the bundle of axons connecting the
    olfactory bulb to the primary olfactory cortex. It divides into the
    **lateral, medial, and intermediate olfactory striae** at the
    olfactory trigone.

*   **``anterior_olfactory_nucleus``** — a small nucleus at the
    posterior end of the olfactory bulb that receives and modulates
    bulb output. It is the **first central relay** in the olfactory
    pathway, projecting bilaterally to the olfactory bulbs and
    ipsilaterally to the piriform cortex.

*   **``piriform_cortex``** — the **primary olfactory cortex** proper,
    receiving input from the lateral olfactory stria. It is
    **three-layered allocortex** and includes the prepiriform and
    periamygdaloid cortices (in some classifications).

*   **``periamygdaloid_cortex``** — a subregion of the primary
    olfactory cortex adjacent to the amygdala. It receives lateral
    olfactory stria input and is often grouped with the piriform
    cortex functionally. The tree separates it from ``piriform_cortex``
    as a sibling, which is a **fine-grained but non-standard**
    distinction — classical anatomy often treats periamygdaloid cortex
    as part of the piriform cortex.

*   **``uncus``** — the medial-most, hook-like anterior end of the
    parahippocampal gyrus. It is the **olfactory/limbic junction**:
    the uncus contains the primary olfactory cortex (piriform,
    periamygdaloid) on its surface and the amygdala and hippocampal
    head beneath. The tree places it under the rhinencephalon rather
    than under ``cortex/temporal/gyri/parahippocampal_gyrus/`` — a
    **deliberate boundary choice** that emphasizes its olfactory
    identity over its gyral identity.

**Not children (deliberately excluded):** The olfactory tubercle, septal
nuclei, anterior perforated substance, amygdala (nuclear complex), and
hippocampal formation are **not** wired as rhinencephalon children. They
live under ``subcortical/``. See *Boundary status* for the rationale.

The Olfactory Pathway Context
-----------------------------
The rhinencephalon is the **telencephalic component** of the primary
olfactory pathway. The full pathway is:

1.  **Olfactory receptor neurons** in the olfactory epithelium send
    axons through the cribriform plate to the **olfactory bulb**.
2.  The **olfactory bulb** relays via the **olfactory tract** to the
    **anterior olfactory nucleus** (local modulation) and to the
    **primary olfactory cortex** (piriform and periamygdaloid).
3.  The piriform cortex projects to the **amygdala**, **hippocampus**,
    **orbitofrontal cortex**, **insula**, and **hypothalamus** — all
    of which are **outside** the rhinencephalon in this tree's narrow
    definition, and are documented in their own modules.

**Olfaction is unique among sensory systems in projecting directly to
cortex without a thalamic relay** (though thalamic modulation occurs
via the mediodorsal nucleus). This is why the rhinencephalon is the
"fastest" sensory pathway to affect and memory — a fact that matters
for the amygdala and hippocampus modules, not for this one.

Function in the Human Brain
---------------------------
The rhinencephalon's functions are **primary olfactory** (the limbic
functions historically attributed to it are documented under
``subcortical/``):

*   **Odor Detection and Discrimination (Primary Function):** The
    olfactory bulb, tract, and anterior olfactory nucleus support the
    **initial sensory processing** of odors — detection threshold,
    concentration coding, and early discrimination.

*   **Odor Identification and Memory (Cortical Component):** The
    piriform and periamygdaloid cortex support **odor identification**
    and contribute to **odor memory** via their projections to the
    amygdala and hippocampus (which are documented elsewhere).

*   **Olfactory-Limbic Interface (Uncus):** The uncus is the
    **structural interface** between the rhinencephalon and the limbic
    system. Its surface is olfactory cortex; beneath it lie the
    amygdala and hippocampal head. Seizures arising in the uncus
    produce **olfactory auras** — the classic "uncinate fit."

*   **NOT a limbic or emotional system in its own right.** The
    rhinencephalon's emotional, mnemonic, and autonomic functions are
    properties of the **amygdala, hippocampus, and hypothalamus**,
    which are documented under ``subcortical/``. The rhinencephalon
    feeds these systems; it does not implement them.

**The unifying theme:** the rhinencephalon is the **telencephalic
primary olfactory substrate**. It is **not** a motor, language,
somatosensory, or visual area, and in this tree's narrow definition it
is **not** the substrate for emotional or mnemonic processing either —
those are downstream.

Associated Disorders
--------------------
Rhinencephalon disorders are **primary olfactory** in this tree's
narrow definition:

*   **Anosmia and Hyposmia:** Loss or reduction of smell from
    **olfactory bulb/tract damage** — traumatic brain injury,
    olfactory groove meningioma, viral infection including COVID-19.
    **Kallmann syndrome** — congenital anosmia with
    hypogonadotropic hypogonadism — results from **olfactory bulb
    agenesis** and failed migration of GnRH neurons.

*   **Olfactory Groove Meningioma:** A tumor arising from the arachnoid
    of the olfactory groove, compressing the olfactory bulb/tract and
    producing **unilateral anosmia** (often unnoticed) and, if large,
    **Foster Kennedy syndrome**.

*   **Uncinate Fits (Temporal Lobe Epilepsy):** The uncus is a classic
    **epileptogenic substrate**. **Olfactory and gustatory auras**
    ("uncinate fits") arise from uncinate discharges. The seizure
    itself propagates into the amygdala and hippocampus (documented
    under ``subcortical/``), but the **aura** is uncinate.

*   **Neurodegenerative Olfactory Dysfunction:** **Parkinson's
    disease** and **Alzheimer's disease** feature **early olfactory
    deficits** that often precede motor/cognitive symptoms. The
    olfactory bulb and piriform cortex are among the earliest
    affected structures.

**What is NOT here:** The rhinencephalon is **not** the substrate for
**temporal lobe epilepsy proper** (that is hippocampal/amygdalar),
**semantic dementia** (anterior temporal neocortex), **Kluver-Bucy
syndrome** (amygdala), or **Wernicke's aphasia** (BA22). Those are
documented in their own modules. The rhinencephalon contributes the
**olfactory aura** to temporal lobe epilepsy and the **olfactory
deficit** to neurodegeneration — it is not the primary syndrome
substrate for either.

Lateralization Notes
--------------------
This is the **right** rhinencephalon module. The rhinencephalon is
**bilaterally symmetric** and **functionally non-lateralized**:

*   **Bilateral Olfactory Projection:** Each olfactory bulb projects
    **ipsilaterally** to the piriform cortex. The two sides are
    **functionally symmetric** for odor detection and discrimination.
    **Unilateral anosmia** is the typical presentation of unilateral
    olfactory bulb/tract lesions — a fact that reflects the
    non-lateralized organization.

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the rhinencephalon has **no documented left-lateralized or
    right-lateralized function**.

*   **Subtle Cortical Asymmetries (Contrast):** Some studies report
    **left-hemisphere advantages for verbal odor naming** and
    **right-hemisphere advantages for emotional odor processing**, but
    these are **cortical-level asymmetries** in orbitofrontal and
    insular regions, **not** asymmetries of the rhinencephalon itself.
    Do not import cortical lateralization claims into the
    rhinencephalon.

**A consumer that assumes "right rhinencephalon = left rhinencephalon"
will be structurally and functionally correct** — the two sides are
symmetric in this tree, and no lateralized function has been
demonstrated.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The
    rhinencephalon's relationships to the amygdala, hippocampus,
    septal nuclei, olfactory tubercle, and anterior perforated
    substance are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Lobe-level container — sibling of ``cortex/``, not a child.**
    The rhinencephalon sits directly under ``.../right/`` because its
    components are **allocortical**, not neocortical. Consumers must
    not assume it is a subregion of ``cortex/``.
*   **Boundary case — narrow olfactory definition, not the classical
    full smell-brain.** The rhinencephalon here contains **only**
    primary olfactory structures plus the uncus. The limbic
    archipallium (amygdala, hippocampus, septal nuclei, olfactory
    tubercle, anterior perforated substance) is **not** wired here;
    it lives under ``subcortical/``. Consumers must not assume the
    classical grouping.
*   **Closed set of six children.** The rhinencephalon has exactly six
    children. Consumers may iterate them, but should not assume any
    others exist or that any are added dynamically.
*   **Uncus is placed here, not under temporal gyri.** The tree
    places the uncus under the rhinencephalon rather than under
    ``cortex/temporal/gyri/parahippocampal_gyrus/``. This is a
    deliberate boundary choice emphasizing its olfactory identity
    over its gyral identity. Consumers iterating temporal gyri and
    expecting the uncus there will **miss it**.
*   **Periamygdaloid cortex is separated from piriform cortex.** The
    tree treats ``periamygdaloid_cortex`` as a sibling of
    ``piriform_cortex``, not a subregion. Classical anatomy often
    groups them; the tree's finer granularity is **non-standard but
    documented**.
*   **No ``AREA_PATHS`` hop.** The rhinencephalon is a local
    lobe-level container, not a cross-listed leaf.
*   **No nested cross-listing.** The rhinencephalon has no nested
    dual-framing module. It is a single container node.
*   **Structural parity with left rhinencephalon.** Right and left
    rhinencephalon modules are **structurally identical** — same six
    children, same narrow-olfactory boundary, same uncus placement,
    same non-lateralized caveat.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right import rhinencephalon

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.rhinencephalon"
    )

**Do not** assume the rhinencephalon is under ``cortex/``. It is a
**sibling** of ``cortex/``, ``subcortical/``, and ``white_matter/``.
A consumer that iterates ``cortex/`` subpackages and expects to find
the rhinencephalon there will **miss it**.

**Do not** assume the rhinencephalon contains the amygdala,
hippocampus, septal nuclei, olfactory tubercle, or anterior perforated
substance. Those are under ``subcortical/``. A consumer that iterates
the rhinencephalon and expects limbic structures will be **misled**.

Iterating the rhinencephalon's six children (recommended consumer
pattern)::

    RHINENCEPHALON_CHILDREN = (
        "anterior_olfactory_nucleus",
        "olfactory_bulb",
        "olfactory_tract",
        "periamygdaloid_cortex",
        "piriform_cortex",
        "uncus",
    )
    # Closed set. Do not assume additional children.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        rhin_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon"
        )
        # resolve rhin_path through the memory/recall layer

Reaching the limbic components (recommended consumer pattern)::

    # The amygdala, hippocampus, septal nuclei, olfactory tubercle,
    # and anterior perforated substance are NOT rhinencephalon
    # children. Resolve them under subcortical/:
    #
    #   subcortical.medial_temporal_lobe.amygdala
    #   subcortical.medial_temporal_lobe.hippocampus
    #   subcortical.basal_forebrain.septal_nuclei
    #   subcortical.basal_forebrain.striatum.ventral_striatum.olfactory_tubercle
    #   subcortical.basal_forebrain.anterior_perforated_substance

References
----------
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Rhinencephalon and olfactory pathways.)
*   **Classical definition:** Gray's Anatomy, 41st ed. —
    "Rhinencephalon" (olfactory lobe; classical full grouping
    including bulb, tract, striae, piriform cortex, and limbic
    components).
*   **Narrow olfactory definition (this tree's position):**
    Nieuwenhuys, R., Voogd, J., van Huijzen, C. (2008). *The Human
    Central Nervous System*, 4th ed. (Piriform and periamygdaloid
    cortex as three-layered allocortex; amygdala and hippocampus as
    separate limbic structures.)
*   **Human olfactory system:** Doty, R.L. (2015). *Handbook of
    Olfaction and Gustation*, 3rd ed. (Human olfactory anatomy and
    function; reduced olfactory bulb and absent vomeronasal system.)
*   **Anterior olfactory nucleus:** Brunjes, P.C., Illig, K.R.,
    Meyer, E.A. (2005). "A field guide to the anterior olfactory
    nucleus (cortex)." *Brain Research Reviews* 50:305–335.
*   **Kallmann syndrome:** Schwanzel-Fukuda, M., Pfaff, D.W. (1989).
    "Origin of luteinizing hormone-releasing hormone neurons."
    *Nature* 338:161–164.
*   **Uncinate fits:** Gloor, P. (1997). *The Temporal Lobe and
    Limbic System*. (Olfactory auras and uncinate seizures.)
*   **Parkinson's olfactory dysfunction:** Braak, H., et al. (2003).
    "Staging of brain pathology related to sporadic Parkinson's
    disease." *Neurobiology of Aging* 24:197–211.
*   NeuroNames — Rhinencephalon; FMA — Rhinencephalon (right member).
"""