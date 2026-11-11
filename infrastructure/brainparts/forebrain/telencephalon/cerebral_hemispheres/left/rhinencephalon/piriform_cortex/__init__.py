"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.rhinencephalon.piriform_cortex
=========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── rhinencephalon
                └── piriform_cortex   <-- THIS MODULE

**Primary synonym:** Piriform cortex; prepiriform cortex; primary
olfactory cortex (in most modern usage); cortex piriformis.
**Cytoarchitectonic designation:** **Not a single Brodmann area.**
Classically overlaps **BA27** (prepiriform) and the region Von Economo
called **BA51** (piriform/prepiriform); the tree wires **BA27
separately** under ``cortex/temporal/brodmann_areas/brodmann_area_27/``.
This module is the **allocortical primary olfactory cortex proper**,
**not** the Brodmann-area abstraction — see *Boundary status*.
**Part of:** The **primary olfactory cortex** — the **principal
cortical target** of the lateral olfactory stria (LOS), and (in most
modern usage) the structure referred to as *the* olfactory cortex.
**Structural parent:** ``.../left/rhinencephalon/`` → **direct child** of
the rhinencephalon container.
**Structural children:** **None.** This is a **leaf** module. The
classical subdivisions (prepiriform, periamygdaloid, and the
anterior/posterior piriform divisions) are documented as **prose**, not
as structural children.
**Boundary status (allocortical):** **Boundary case — three-layered
allocortex, not six-layered neocortex.** The piriform cortex has
**three layers** (molecular, pyramidal, polymorphic) and is
**phylogenetically older** than neocortex. It is therefore a
**rhinencephalon leaf**, **not** a child of ``cortex/``. Consumers
must not resolve piriform cortex through the neocortical ``cortex/``
container.
**Boundary status (piriform vs. periamygdaloid):** **Boundary case —
sibling of periamygdaloid cortex, not a subregion.** Classical anatomy
often treats the periamygdaloid cortex as the
**"periamygdaloid part of the piriform lobe."** The tree splits them
into **two sibling leaves**. This is **non-standard but deliberate** —
the tree preserves a finer granularity so that the olfactory–limbic
boundary can be documented **at the periamygdaloid cortex** rather
than folded into a piriform module. Consumers that need the
**piriform lobe** as a unit must **union** ``piriform_cortex`` and
``periamygdaloid_cortex``.
**Boundary status (BA27):** **Boundary case — not Brodmann area 27.**
BA27 is wired separately under
``cortex/temporal/brodmann_areas/brodmann_area_27/``. In some maps
BA27 corresponds to prepiriform cortex; in others it is the
presubicular region. **This module is the allocortical cortical
region, not the Brodmann-area abstraction.** Consumers that need
Brodmann-area resolution should resolve ``brodmann_area_27``;
consumers that need the **primary olfactory cortex** should resolve
this module. The two are **not interchangeable**.
**Boundary status (entorhinal):** **Boundary case — not the
entorhinal cortex.** The entorhinal cortex (BA28/BA34) is wired
separately under ``cortex/temporal/gyri/entorhinal_cortex/``. The
piriform cortex is **rostral** to the entorhinal cortex; the boundary
between them is **cytoarchitecturally gradual**, but they are
**distinct** in the tree. Consumers must not resolve piriform cortex
as an entorhinal child, or vice versa.
**Boundary status (olfactory_cortex under anterior_temporal_lobe):**
**Boundary case — not the ``olfactory_cortex`` under
``cortex/temporal/cortex/anterior_temporal_lobe/``.** The tree wires
a **second** "olfactory cortex" leaf under the neocortical
``cortex/temporal/`` partition. That leaf is **not** the piriform
cortex — it is a **neocortical** olfactory association area, distinct
from the **allocortical** primary olfactory cortex documented here.
Consumers must not conflate the two; they live in different partitions
for a reason.

Overview
--------
The piriform cortex is the **primary olfactory cortex** — the
**principal cortical target** of the lateral olfactory stria and, in
most modern usage, *the* olfactory cortex. It is a **three-layered
allocortical** structure lying on the **ventral surface of the
temporal lobe**, extending from the **frontal lobe rostrally** to the
**entorhinal cortex caudally**, and occupying the **uncus and
anterior parahippocampal gyrus** region.

**The piriform cortex is the largest single olfactory cortical
area.** It is the **primary site of odor identification** — the
cortical stage at which the glomerular odor map of the bulb is
**transformed into a perceptual representation** of odorant identity.
It is also a **major site of olfactory learning and memory**, a
**major epileptogenic substrate**, and a **convergence point** for
olfactory, gustatory, and limbic inputs that underlie **flavor** and
**emotional odor associations**.

**The piriform cortex is allocortical, not neocortical.** It has
**three layers** (molecular, pyramidal, polymorphic) rather than six,
and it is **phylogenetically older** than neocortex. This is why the
tree places it under the **rhinencephalon**, not under ``cortex/`` —
the ``cortex/`` container is reserved for neocortex. Consumers must
resolve piriform cortex through the rhinencephalon path, **not**
through ``cortex/temporal/``.

**The piriform cortex is not the periamygdaloid cortex.** This is the
most important sibling boundary. Classical anatomy often treats the
periamygdaloid cortex as the **"periamygdaloid part of the piriform
lobe."** The tree splits them into **two sibling leaves**:
``piriform_cortex`` and ``periamygdaloid_cortex``. The piriform cortex
is the **larger, more rostral, more "olfactory-identification"**
component; the periamygdaloid cortex is the **smaller, more caudal,
more "olfactory–limbic-relay"** component (it projects into the
amygdala). If the **piriform lobe** is the unit of interest,
**union** the two leaves.

**The piriform cortex is not the entorhinal cortex.** The entorhinal
cortex (BA28/BA34) is wired separately under
``cortex/temporal/gyri/entorhinal_cortex/``. The piriform cortex is
**rostral** to the entorhinal cortex; the boundary is **gradual** in
cytoarchitecture, but the tree treats them as **distinct**. The
piriform cortex is **primary olfactory**; the entorhinal cortex is
**olfactory-hippocampal interface** (a gateway to the hippocampus).

**The piriform cortex is not the ``olfactory_cortex`` under
``cortex/temporal/cortex/anterior_temporal_lobe/``.** The tree wires a
**second** "olfactory cortex" leaf in the neocortical ``cortex/``
partition. That leaf is a **neocortical olfactory association area**,
**not** the allocortical primary olfactory cortex documented here. The
two "olfactory cortices" in the tree are **different structures in
different partitions**; consumers must not conflate them.

**The piriform cortex is not the olfactory tubercle or cortical
amygdala.** Those are **subcortical** structures (the olfactory
tubercle is under
``subcortical/basal_forebrain/striatum/ventral_striatum/olfactory_tubercle/``,
the cortical amygdala under
``subcortical/medial_temporal_lobe/amygdala/``). They are also primary
olfactory targets, but they are **not** piriform cortex and must not
be resolved through this module.

Subdivisions (prose, not structural children)
---------------------------------------------
The piriform cortex is classically divided into **subdivisions**
whose boundaries are **cytoarchitecturally subtle and inconsistently
named**:

*   **Prepiriform cortex** — the **rostral** part, adjacent to the
    olfactory tubercle and anterior perforated substance. Receives
    strong LOS input. In some maps this is BA27.

*   **Periamygdaloid part** — the **caudal** part, overlying the
    amygdala (documented **separately** in the tree as
    ``periamygdaloid_cortex``; see *Boundary status*).

*   **Anterior piriform cortex (APC)** vs. **posterior piriform
    cortex (PPC)** — a **functional** division that does **not**
    correspond cleanly to the cytoarchitectural subdivisions. The
    **APC** is more **olfactory-recipient** (stronger bulb input); the
    **PPC** is more **associative** (stronger amygdala, orbitofrontal,
    and hippocampal connections) and is the **more epileptogenic**
    region.

**These subdivisions are prose, not structural children.** The tree
does **not** wire them as sub-modules. Consumers that need
subdivision-level resolution should consult the references, not the
tree. The boundaries between subdivisions — and between the piriform
cortex and its neighbors (olfactory tubercle rostrally, periamygdaloid
caudally, entorhinal caudally) — are **graded**, not sharp.

**The "piriform" vs. "prepiriform" terminology is contested.** Some
authors use "piriform cortex" to refer to the **entire** primary
olfactory cortical region (including periamygdaloid), and
"prepiriform" to refer to the **rostral** part only. Others use
"piriform" for the **rostral** part and reserve "periamygdaloid" for
the caudal part. The tree follows the **second** convention: piriform
cortex is the **rostral primary olfactory cortex proper**,
periamygdaloid is the **caudal sibling**. Consumers should be aware
that **many sources will use "piriform" more broadly**.

Function in the Human Brain
---------------------------
The piriform cortex's functions are **olfactory identification,
memory, and association**:

*   **Odor Identification (Primary Function):** The piriform cortex
    is the **principal cortical site of odor identification** — the
    stage at which the bulb's glomerular map is transformed into a
    **perceptual representation** of odorant identity. Bilateral
    piriform lesions impair **odor identification** while leaving
    basic detection relatively intact.

*   **Synthetic Odor Coding (Defining Function):** The piriform
    cortex uses a **distributed, "synthetic" code** — odorants are
    represented by **spatially distributed ensembles** of pyramidal
    cells, not by a topographic map. This architecture supports
    **pattern separation** (distinguishing similar odors),
    **pattern completion** (recognizing odors from partial cues), and
    **associative learning** (odor–reward, odor–emotion). It is one
    of the best-studied examples of **distributed cortical coding**.

*   **Olfactory Learning and Memory:** The piriform cortex is a
    **major site of olfactory learning** — odor–reward, odor–fear,
    and odor–odor associations. It has **direct reciprocal
    connections** with the **amygdala** (emotional odor memory), the
    **hippocampus and entorhinal cortex** (episodic odor memory),
    and the **orbitofrontal cortex** (odor–taste and odor–reward
    associations).

*   **Flavor Perception (with Orbitofrontal Cortex):** The piriform
    cortex is a **convergence point** for **olfactory and gustatory**
    inputs; its projections to the **orbitofrontal cortex** support
    **flavor perception** (the combination of smell and taste) and
    **food-related reward**.

*   **Social Odor Processing (with Amygdala):** The piriform cortex
    projects to the **amygdala** and supports **social odor
    processing** — kin recognition, mate selection, and
    **emotional odor associations** (the "Proust phenomenon").

*   **NOT a primary sensory cortex in the neocortical sense.** The
    piriform cortex is **allocortical** — it does not have the
    **columnar/laminar organization** of neocortex, and its coding is
    **distributed rather than topographic**. It is a **primary
    sensory cortex** in the functional sense (first cortical stage of
    olfaction) but **not** in the cytoarchitectural sense (it is not
    neocortex).

**The unifying theme:** the piriform cortex is the **primary olfactory
cortex proper** — the **largest single olfactory cortical area**, the
**principal site of odor identification**, and a **major substrate
for olfactory learning, memory, and association**. It is **allocortical**
(three-layered), **not neocortical**, and it is the **"olfactory
cortex"** in the sense that matters for conscious smell perception.

Associated Disorders
--------------------
Piriform cortex disorders are **olfactory and epileptic**:

*   **Olfactory Agnosia and Impaired Odor Identification:** Bilateral
    piriform lesions produce **impaired odor identification** and
    **olfactory agnosia** — the inability to recognize odors despite
    intact detection. **Pure olfactory agnosia** is rare; more often
    it is part of a **broader olfactory-cognitive deficit** (e.g.,
    in Alzheimer's disease or anterior temporal lobectomy).

*   **Temporal Lobe Epilepsy — Piriform Kindling:** The piriform
    cortex is one of the **most epileptogenic structures in the
    brain**. It is a **classic substrate** for **kindling** (the
    experimental model of epilepsy) and a **common site of seizure
    onset** in **temporal lobe epilepsy**. **Uncinate fits**
    (olfactory/gustatory auras) can arise from piriform or uncinate
    discharges.

*   **Focal Cortical Dysplasia:** The piriform cortex is a **frequent
    site of focal cortical dysplasia** in **drug-resistant temporal
    lobe epilepsy**. Surgical resection of the piriform region is a
    common epilepsy surgery.

*   **Parkinson's Disease:** The piriform cortex is **affected early**
    in Parkinson's disease (Braak stage 1–3), contributing to
    **prodromal olfactory deficits**. **α-Synuclein pathology** can
    be seen in piriform neurons.

*   **Alzheimer's Disease:** The piriform cortex is **affected early**
    in Alzheimer's disease, with **neurofibrillary tangles** and
    **amyloid plaques** appearing in the olfactory cortex before
    widespread neocortical involvement. **Olfactory identification
    deficits** are an early clinical sign.

*   **Post-Viral Olfactory Dysfunction (COVID-19 and Others):** The
    piriform cortex can be **involved** in post-viral olfactory
    dysfunction, contributing to **persistent odor identification
    deficits** after infection.

**What is NOT here:** The piriform cortex is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala proper), **fear conditioning**
(amygdala proper), **semantic dementia** (anterior temporal
neocortex), **Wernicke's aphasia** (BA22), or **hippocampal amnesia**
(hippocampus). It contributes to **odor identification**, **olfactory
memory**, and **epileptogenesis** — but it is **not** the primary
substrate for emotional, semantic, language, or episodic-memory
disorders.

Lateralization Notes
--------------------
This is the **left** piriform cortex module. The piriform cortex is
**bilaterally symmetric** and **functionally non-lateralized**:

*   **No Lateralized Syndrome:** Unlike BA22 (left Wernicke's), BA37
    (left VWFA / right FFA), or BA38 (left semantic / right social),
    the piriform cortex has **no documented left-lateralized or
    right-lateralized function**.

*   **Ipsilateral Olfactory Projection:** Each piriform cortex
    receives **ipsilateral** LOS input from its own bulb. The two
    sides are **functionally symmetric** for odor identification.

*   **Bilateral Redundancy (Unilateral Lesions):** **Unilateral
    piriform lesions** produce **minimal or no detectable olfactory
    deficit**, because the contralateral piriform cortex is sufficient
    for identification. **Bilateral** piriform damage is required for
    **severe odor-identification deficits** — a striking demonstration
    of the **functional symmetry** of the two sides.

*   **No Cortical-Level Asymmetries:** The subtle left-verbal /
    right-emotional asymmetries reported for **orbitofrontal** and
    **insular** odor processing are **cortical-level** phenomena
    **downstream** of the piriform cortex. Do not import them into the
    piriform cortex.

**A consumer that assumes "left piriform = right piriform" will be
structurally and functionally correct** — the two sides are symmetric,
no lateralized function has been demonstrated, and the **clinical
evidence of bilateral redundancy** (unilateral lesions being silent)
is direct evidence of this symmetry.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``subcortical/``, or ``white_matter/``. The piriform
    cortex's projections to the orbitofrontal cortex, amygdala,
    entorhinal cortex, hippocampus, and hypothalamus are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The classical
    subdivisions (prepiriform, periamygdaloid, anterior/posterior
    piriform) are documented as **prose**, not as sub-modules.
    Consumers must not assume they exist as children; resolve
    subdivision-level detail through the references.
*   **Allocortical — not a child of ``cortex/``.** The piriform cortex
    is three-layered allocortex, not six-layered neocortex. It is
    wired under ``rhinencephalon``, not under ``cortex/``. Consumers
    must not resolve it through the neocortical container.
*   **Boundary case — sibling of ``periamygdaloid_cortex``, not a
    subregion.** Classical anatomy often treats the periamygdaloid
    cortex as part of the piriform lobe. The tree splits them into two
    sibling leaves. Consumers that need the **piriform lobe** as a
    unit must **union** ``piriform_cortex`` and
    ``periamygdaloid_cortex``.
*   **Boundary case — not Brodmann area 27.** BA27 is wired separately
    under ``cortex/temporal/brodmann_areas/brodmann_area_27/``. This
    module is the **allocortical cortical region**, not the
    Brodmann-area abstraction. The two overlap in some maps but are
    **not interchangeable**.
*   **Boundary case — not the entorhinal cortex.** The entorhinal
    cortex (BA28/BA34) is wired separately under
    ``cortex/temporal/gyri/entorhinal_cortex/``. The piriform cortex
    is **rostral** to the entorhinal cortex; the boundary is
    **graded** but the tree treats them as **distinct**.
*   **Boundary case — not the ``olfactory_cortex`` under
    ``cortex/temporal/cortex/anterior_temporal_lobe/``.** That leaf is
    a **neocortical** olfactory association area, **distinct** from
    the allocortical primary olfactory cortex documented here.
    Consumers must not conflate them.
*   **No ``AREA_PATHS`` hop.** The piriform cortex is a local leaf
    under the rhinencephalon, not a cross-listed leaf.
*   **No nested cross-listing.** The piriform cortex has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right piriform cortex.** Left and right
    piriform cortex modules are **structurally identical** — same leaf
    status, same subdivisions documented as prose, same allocortical
    caveat, same sibling-boundary flags, same non-lateralized
    caveat.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.rhinencephalon import piriform_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.rhinencephalon."
        "piriform_cortex"
    )

**Do not** assume the piriform cortex is under ``cortex/``. It is an
**allocortical** leaf under the **rhinencephalon**. A consumer that
iterates ``cortex/temporal/`` and expects to find the primary olfactory
cortex there will **miss it**.

**Do not** assume the piriform cortex is a **subregion of
``periamygdaloid_cortex``** or vice versa. They are **sibling
leaves**. Classical anatomy often groups them as the "piriform lobe";
the tree splits them. If the piriform lobe is the unit of interest,
**union** the two leaves.

**Do not** assume the piriform cortex is **Brodmann area 27**. BA27 is
wired separately. The two overlap in some maps but are **not
interchangeable**.

**Do not** assume the piriform cortex is the **entorhinal cortex**.
Entorhinal is wired separately under ``cortex/temporal/gyri/``.

**Do not** assume the piriform cortex is the **``olfactory_cortex``
under ``cortex/temporal/cortex/anterior_temporal_lobe/``**. That is a
neocortical olfactory association area; this is the allocortical
primary olfactory cortex.

**Do not** assume the piriform cortex has structural children. It is
a **leaf**. The classical subdivisions (prepiriform, periamygdaloid,
APC/PPC) are **prose only** — they are not wired as modules.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pir_path = (
            f"telencephalon.cerebral_hemispheres.{side}.rhinencephalon."
            f"piriform_cortex"
        )
        # resolve pir_path through the memory/recall layer

Reaching the piriform cortex's downstream targets (recommended
consumer pattern)::

    # The piriform cortex projects to structures documented elsewhere
    # in the tree. Resolve them at their own paths:
    #
    #   cortex.frontal.cortex.prefrontal_cortex.orbitofrontal_cortex
    #   subcortical.medial_temporal_lobe.amygdala
    #   cortex.temporal.gyri.entorhinal_cortex
    #   subcortical.medial_temporal_lobe.hippocampus
    #   diencephalon.hypothalamus
    #
    # These are NOT piriform cortex children. They are downstream
    # targets.

Piriform-lobe-level iteration (recommended consumer pattern)::

    # If the piriform lobe is the unit of interest, union the two
    # sibling leaves:
    PIRIFORM_LOBE_LEAVES = (
        "piriform_cortex",
        "periamygdaloid_cortex",
    )
    # Classical anatomy often treats periamygdaloid as part of
    # piriform; the tree splits them for finer granularity.

Distinguishing the two "olfactory cortices" in the tree
(recommended consumer pattern)::

    # The tree wires TWO "olfactory cortex" leaves in different
    # partitions:
    #
    #   rhinencephalon.piriform_cortex
    #       -> allocortical primary olfactory cortex (THIS MODULE)
    #       -> three-layered, direct LOS input, odor identification
    #
    #   cortex.temporal.cortex.anterior_temporal_lobe.olfactory_cortex
    #       -> neocortical olfactory association area
    #       -> six-layered, downstream of piriform, associative
    #
    # They are NOT the same structure and must not be conflated.

References
----------
*   **Canonical review:** Haberly, L.B. (2001). "Parallel-distributed
    processing in olfactory cortex: new insights from morphological
    and physiological analysis of neuronal circuitry." *Chemical
    Senses* 26:551–576. (Definitive review; synthetic coding;
    distributed representation.)
*   **Piriform anatomy:** Price, J.L. (1990). "Olfactory system." In
    *The Human Nervous System* (Paxinos, G., ed.). (Piriform cortex
    as primary olfactory cortex; LOS input; subdivisions.)
*   **Synthetic coding:** Hopfield, J.J. (1999). "Odor space and
    olfactory processing: Markov processes." *Proceedings of the
    National Academy of Sciences* 96:12506–12511. (Distributed
    synthetic odor representation in piriform cortex.)
*   **Piriform learning and memory:** Schoenbaum, G., Eichenbaum, H.
    (1995). "Information coding in the rodent prefrontal cortex. I.
    Single-neuron activity in orbitofrontal cortex compared with that
    in pyriform cortex." *Journal of Neurophysiology* 74:733–750.
    (Piriform odor coding and associative learning.)
*   **Piriform epilepsy:** Löscher, W., Ebert, U. (1996). "The role of
    the piriform cortex in kindling." *Progress in Neurobiology*
    50:427–481. (Piriform cortex as a highly epileptogenic
    substrate.)
*   **Piriform and focal cortical dysplasia:** Palmini, A., et al.
    (2004). "Terminology and classification of the cortical
    dysplasias." *Neurology* 62:S2–S8. (Piriform as a site of FCD
    in temporal lobe epilepsy.)
*   **Parkinson's disease:** Braak, H., et al. (2003). "Staging of
    brain pathology related to sporadic Parkinson's disease."
    *Neurobiology of Aging* 24:197–211. (Piriform involvement in
    early PD.)
*   **Alzheimer's disease:** Price, J.L., et al. (1991). "The
    distribution of tangles, plaques and related
    immunohistochemical markers in healthy aging and Alzheimer's
    disease." *Neurobiology of Aging* 12:295–312. (Piriform
    involvement in early AD.)
*   **COVID-19:** Brann, D.H., et al. (2020). "Non-neuronal expression
    of SARS-CoV-2 entry genes in the olfactory system suggests
    mechanisms underlying COVID-19-associated anosmia." *Science
    Advances* 6:eabc5801. (Post-viral olfactory dysfunction;
    piriform involvement.)
*   **Olfactory agnosia:** Jones-Gotman, M., Zatorre, R.J. (1988).
    "Olfactory identification deficits in patients with focal
    cerebral excisions." *Neuropsychologia* 26:387–400. (Piriform
    lesions and odor identification.)
*   **Brodmann area 27:** Brodmann, K. (1909). *Vergleichende
    Lokalisationslehre der Grosshirnrinde*. (BA27 and its relation
    to prepiriform cortex; note the tree wires BA27 separately.)
*   **Human olfactory cortex:** Doty, R.L. (2015). *Handbook of
    Olfaction and Gustation*, 3rd ed. (Piriform cortex in human
    olfactory processing.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Piriform cortex in the olfactory pathway.)
*   NeuroNames — Piriform cortex (left); FMA — Piriform cortex (left
    member).
"""