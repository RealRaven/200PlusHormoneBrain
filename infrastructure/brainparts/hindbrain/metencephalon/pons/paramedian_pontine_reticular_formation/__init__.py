"""
infrastructure.brainparts.hindbrain.metencephalon.pons.paramedian_pontine_reticular_formation
============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── paramedian_pontine_reticular_formation   <-- THIS MODULE

**Primary synonym:** Paramedian pontine reticular formation; PPRF;
paramedian zone of the pontine reticular formation; pontine horizontal
gaze center; "the horizontal saccadic burst generator."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem reticular formation region** — **not a single anatomically
delimited nucleus**, but a **functionally defined group of premotor
saccadic burst neurons** in the **paramedian pontine tegmentum**, near
the **midline**, just **ventral to the abducens nucleus** and the
**medial longitudinal fasciculus (MLF)**. It is the **horizontal
saccadic burst generator** — the **premotor command node** that **drives
the abducens nucleus** for **horizontal saccades** and **horizontal
pursuit**.
**Part of:** The **pons** container — specifically, the **pontine
tegmentum** (the **paramedian zone** of the **dorsal pontine
tegmentum**). The **pons** is the **metencephalic** brainstem segment.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **None.** This is a **leaf** module. The
**excitatory burst neurons (EBNs)**, **inhibitory burst neurons
(IBNs)**, and **other premotor populations** are documented as
**prose**, not as structural children — they are the **functionally
distinct neuron populations** within the region.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
PPRF is a LEAF, not a container.** It has **no structural children**.
The **EBNs**, **IBNs**, and **other premotor populations** are **prose**
populations, not structural children. Consumers must **not** treat the
PPRF as a container, and must **not** assume the neuron populations
exist as sub-modules.
**Boundary status (FUNCTIONALLY DEFINED REGION — NOT a cytologically
distinct nucleus):** **Boundary case — the PPRF is a FUNCTIONALLY
DEFINED REGION, NOT a cytologically distinct nucleus.** Unlike the
**abducens nucleus** (a compact somatic motor nucleus) or the
**vestibular nuclei** (a compact special sensory complex), the **PPRF**
is a **functionally defined group of premotor saccadic burst neurons**
in the **paramedian pontine tegmentum** — it is defined by its
**axonal projections** (to the abducens nucleus) and its **functional
role** (horizontal saccadic burst generation), rather than by a
**distinct cytoarchitectonic boundary**. This **diffuse organization**
is **prose**, not structural children. Consumers must **not** expect a
compact, cytologically distinct nucleus — the **PPRF** is a **functional
population** defined by its **targets** and its **premotor role**.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the PPRF is a SINGLE module at the tree level, even
though the PPRF is BILATERAL in real anatomy.** Unlike the
**cranial_nerve_nuclei** module (which has explicit ``left`` and
``right`` structural children), the **paramedian_pontine_reticular_formation**
module (here) is a **single module** that represents the **bilateral
PPRF** (left and right paramedian pontine tegmentum). The tree does
**not** split them into left/right. Consumers must **not** assume a
left/right split exists at the tree level — the module is a **single,
bilateral representation**.
**Boundary status (PREmotor COMMAND NODE — NOT the motor output node):**
**Boundary case — the PPRF is the PREMOTOR COMMAND NODE, NOT the motor
output node.** The **PPRF** (here) is the **burst generator** that
**generates the velocity command** for **horizontal saccades** — it
**projects to** the **abducens nucleus**, which is the **motor output
node** that **drives the extraocular muscles** (via the abducens nerve
and the internuclear neurons). The **PPRF** and the **abducens nucleus**
are **DIFFERENT STRUCTURES** — the **PPRF** is **upstream premotor**;
the **abducens nucleus** is **downstream motor**. **This distinction is
clinically load-bearing** — a **PPRF lesion** causes **ipsilateral
horizontal gaze palsy** (the eyes cannot look toward the lesion side);
an **abducens nucleus lesion** causes **ipsilateral horizontal gaze
palsy** as well (because the internuclear neurons are lost) — but the
**PPRF lesion** is **not** accompanied by **abducens nerve palsy** and
may have **different associated brainstem signs** (e.g. **Foville
syndrome** vs. **abducens nerve palsy**). Consumers must **not**
conflate the PPRF with the abducens nucleus.
**Boundary status (NOT the abducens nucleus — that is the DOWNSTREAM
MOTOR OUTPUT NODE):** **Boundary case — the PPRF is NOT the abducens
nucleus; the abducens nucleus is the DOWNSTREAM MOTOR OUTPUT NODE.** The
**abducens nucleus** (``.../cranial_nerve_nuclei/left/abducens_nucleus/``
and ``.../right/``) is the **somatic motor** nucleus for the
**lateral rectus** — it is the **final common pathway** for
**horizontal gaze** and the **efferent node** of the **horizontal VOR**.
The **PPRF** (here) is the **upstream premotor burst generator** — it
**drives** the abducens nucleus for **voluntary horizontal saccades**
and **horizontal pursuit** (but not for the **VOR**, which is driven by
the **vestibular nuclei**). They are **DIFFERENT STRUCTURES** —
different functional roles (premotor burst generation vs. motor output).
**This distinction is clinically load-bearing** — a **PPRF lesion**
causes **ipsilateral horizontal gaze palsy** (the eyes cannot look
toward the lesion side); an **abducens nucleus lesion** also causes
**ipsilateral horizontal gaze palsy**, but the **associated signs**
differ — **PPRF lesions** may accompany **contralateral hemiparesis**
(**Foville syndrome**) or **ipsilateral facial palsy** (**Foville
syndrome**), while **abducens nucleus lesions** may accompany
**ipsilateral facial palsy** and **contralateral hemiparesis**
(**Foville syndrome** — same syndrome, overlapping structures).
Consumers must **not** conflate the PPRF with the abducens nucleus.
**Boundary status (NOT the MLF — that is the WHITE-MATTER TRACT carrying
internuclear axons):** **Boundary case — the PPRF is NOT the medial
longitudinal fasciculus (MLF).** The **MLF** is the **white-matter
tract** that carries the **internuclear neuron axons** from the
**abducens nucleus** to the **contralateral medial rectus subnucleus**
of the oculomotor nucleus. The **PPRF** (here) is the **grey-matter
premotor burst generator** that **drives** the abducens nucleus. They
are **DIFFERENT STRUCTURES** — the **PPRF** is grey matter and
**upstream of the abducens nucleus**; the **MLF** is white matter and
**downstream of the abducens nucleus** (it carries the internuclear
axons). **This distinction is clinically load-bearing** — an **MLF
lesion** causes **internuclear ophthalmoplegia (INO)**; a **PPRF
lesion** causes **ipsilateral horizontal gaze palsy**. Consumers must
**not** conflate the PPRF with the MLF.
**Boundary status (NOT the vestibular nuclei — those are the VOR input,
not the voluntary saccade input):** **Boundary case — the PPRF is NOT
the vestibular nuclei.** The **vestibular nuclei**
(``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``
and ``.../right/``) are the **special sensory** nuclei for **balance and
spatial orientation** — they **drive** the **vestibulo-ocular reflex
(VOR)** by projecting to the **abducens nucleus** and the **oculomotor
nucleus** (via the MLF). The **PPRF** (here) is the **voluntary saccadic
burst generator** — it **drives** the abducens nucleus for
**voluntary horizontal saccades** and **horizontal pursuit**. They are
**DIFFERENT STRUCTURES** — the **vestibular nuclei** drive the **VOR**
(reflexive, vestibular-driven eye movements); the **PPRF** drives
**voluntary saccades** (cortical and collicular-driven eye movements).
**The two systems converge on the abducens nucleus** but **subserve
different functions** — **VOR** vs. **voluntary saccades**. **This
distinction is clinically load-bearing** — a **vestibular nuclei
lesion** causes **vestibular syndrome** (vertigo, nystagmus, VOR
deficit); a **PPRF lesion** causes **horizontal gaze palsy** (loss of
voluntary saccades, but the VOR may be preserved). Consumers must
**not** conflate the PPRF with the vestibular nuclei.
**Boundary status (NOT the NPH — that is the NEURAL INTEGRATOR):**
**Boundary case — the PPRF is NOT the nucleus prepositus hypoglossi
(NPH).** The **NPH**
(``.../medulla_oblongata/perihypoglossal_nuclei/prepositus_nucleus/``) is
the **horizontal gaze neural integrator** — it **converts** the
**velocity** command from the PPRF into a **position** command that
**holds the eyes in eccentric gaze**. The **PPRF** (here) is the
**velocity command generator** — it **generates** the **saccadic
velocity burst** that the NPH **integrates**. They are **DIFFERENT
STRUCTURES** — the **NPH** is the **integrator**; the **PPRF** is the
**velocity command generator**. **This distinction is clinically
load-bearing** — an **NPH lesion** causes **gaze-evoked nystagmus**
(the eyes cannot **hold** eccentric gaze); a **PPRF lesion** causes
**horizontal gaze palsy** (the eyes cannot **move** toward the lesion
side). Consumers must **not** conflate the PPRF with the NPH.
**Boundary status (NOT the superior colliculus — that is the MIDBRAIN
saccade generator):** **Boundary case — the PPRF is NOT the superior
colliculus.** The **superior colliculus**
(``.../midbrain/tectum/corpora_quadrigemina/left/superior_colliculus/``
and ``.../right/``) is the **midbrain sensorimotor integration center**
for **saccades** — it **receives** visual, auditory, and somatosensory
inputs and **generates** the **saccade command** (the **desired
displacement**) that is then **relayed** to the **PPRF** (for
horizontal saccades) or the **rostral interstitial nucleus of the MLF
(riMLF)** (for vertical saccades). The **PPRF** (here) is the **pontine
burst generator** — it **receives** the superior colliculus command and
**generates** the **velocity burst** that drives the abducens nucleus.
They are **DIFFERENT STRUCTURES** — the **superior colliculus** is
**upstream** (in the midbrain); the **PPRF** is **downstream** (in the
pons) and **burst-generating** (not **command-generating**). **This
distinction is clinically load-bearing** — a **superior colliculus
lesion** causes **saccadic deficits** (impaired saccade initiation) but
not typically **full horizontal gaze palsy**; a **PPRF lesion** causes
**complete ipsilateral horizontal gaze palsy** (loss of both voluntary
saccades and horizontal pursuit). Consumers must **not** conflate the
PPRF with the superior colliculus.
**Boundary status (NOT the frontal eye fields — those are CORTICAL
saccade generators):** **Boundary case — the PPRF is NOT the frontal eye
fields.** The **frontal eye fields** (FEF — the **caudal part of the
middle frontal gyrus**, Brodmann area 8)
(``.../cerebral_hemispheres/left/cortex/frontal/gyri/middle_frontal_gyrus/``
and ``.../right/``) are the **cortical saccade generators** — they
**receive** high-level cognitive inputs (attention, working memory,
decision-making) and **project** to the **superior colliculus** and,
via the **corticobulbar** and **corticopontine** pathways, to the
**PPRF** (directly and indirectly). The **PPRF** (here) is the **pontine
burst generator** — it **receives** the frontal eye field command
(indirectly, via the superior colliculus and the **nucleus reticularis
tegmenti pontis (NRTP)**) and **generates** the **velocity burst**.
They are **DIFFERENT STRUCTURES** — the **frontal eye fields** are
**cortical** and **upstream**; the **PPRF** is **pontine** and
**downstream**. Consumers must **not** conflate the PPRF with the
frontal eye fields.
**Boundary status (NOT the nucleus reticularis tegmenti pontis — that is
a BASILAR PONS relay to the cerebellum):** **Boundary case — the PPRF is
NOT the nucleus reticularis tegmenti pontis (NRTP).** The **NRTP**
(``.../pons/.../nucleus_reticularis_tegmenti_pontis/`` — **prose
location** in the **basilar pons**, not a structural child of the pons
in the tree) is the **cortico-ponto-cerebellar relay** that **receives**
cortical inputs (including from the **frontal eye fields**) and
**projects to the cerebellum** (especially the **oculomotor vermis** and
the **fastigial nucleus**) — it **contributes** to **saccade
adaptation** and **cerebellar control of eye movements**. The **PPRF**
(here) is the **pontine burst generator** — it **receives** the
superior colliculus and frontal eye field commands (indirectly, via the
NRTP and other relays) and **generates** the **velocity burst**. They
are **DIFFERENT STRUCTURES** — the **NRTP** is a **basilar pons relay
to the cerebellum**; the **PPRF** is a **dorsal tegmental burst
generator** to the abducens nucleus. Consumers must **not** conflate the
PPRF with the NRTP.
**Boundary status (NOT the rostral interstitial nucleus of the MLF — that
is the VERTICAL saccade generator in the MIDBRAIN):** **Boundary case —
the PPRF is NOT the rostral interstitial nucleus of the MLF (riMLF).**
The **riMLF**
(``.../midbrain/tegmentum/rostral_interstitial_nucleus_mlf/left/`` and
``.../right/``) is the **vertical saccadic burst generator** in the
**midbrain** — it **drives** the **oculomotor nucleus** and the
**trochlear nucleus** for **vertical saccades** and **vertical
pursuit**. The **PPRF** (here) is the **horizontal saccadic burst
generator** in the **pons** — it **drives** the **abducens nucleus** for
**horizontal saccades** and **horizontal pursuit**. They are
**DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
midbrain), different functional systems (horizontal vs. vertical
saccades). **This distinction is clinically load-bearing** — a **PPRF
lesion** causes **horizontal gaze palsy**; a **riMLF lesion** causes
**vertical gaze palsy** (including **Parinaud syndrome** when the
**dorsal midbrain** is involved). Consumers must **not** conflate the
PPRF with the riMLF.
**Boundary status (NOT the central mesencephalic reticular formation —
that is a MIDBRAIN premotor region):** **Boundary case — the PPRF is
NOT the central mesencephalic reticular formation (cMRF).** The **cMRF**
(``.../midbrain/tegmentum/.../central_mesencephalic_reticular_formation/``
— **prose location** in the **midbrain tegmentum**, not a structural
child of the midbrain in the tree) is a **premotor region** in the
**midbrain** that **contributes** to **saccade generation** (especially
**contralateral horizontal saccades** — it is **upstream** of the PPRF
in some models). The **PPRF** (here) is the **pontine burst generator**
— it **receives** the cMRF and superior colliculus commands and
**generates** the **velocity burst**. They are **DIFFERENT STRUCTURES**
— different brainstem levels (midbrain vs. pons), different functional
roles (premotor region vs. burst generator). Consumers must **not**
conflate the PPRF with the cMRF.
**Boundary status (NOT the pontine nuclei — those are basilar-pons
cortico-ponto-cerebellar relays):** **Boundary case — the PPRF is NOT
the pontine nuclei.** The **pontine nuclei**
(``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons** — they
**receive** corticopontine fibers from the cerebral cortex and
**project** to the **contralateral cerebellar cortex** via the
**middle cerebellar peduncle**. The **PPRF** (here) is the **dorsal
tegmental** premotor burst generator. They are **DIFFERENT STRUCTURES**
— different anatomical locations (basilar pons vs. dorsal tegmentum),
different functional systems (cortico-ponto-cerebellar vs. horizontal
saccades). Consumers must **not** conflate the PPRF with the pontine
nuclei.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the PPRF is NOT the locus
coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain —
it is in the **pontine tegmentum**, **dorsolateral** to the PPRF. The
**PPRF** (here) is the **horizontal saccadic burst generator**. They are
**DIFFERENT STRUCTURES** — different neurotransmitters (glutamate, etc.
vs. norepinephrine), different functional systems (horizontal saccades
vs. noradrenergic arousal). They are **anatomically adjacent** — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the PPRF with the locus coeruleus.
**Boundary status (NOT the parabrachial area — that is the visceral-
sensory and respiratory relay):** **Boundary case — the PPRF is NOT the
parabrachial area.** The **parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral-sensory and
respiratory-relay complex** — the **lateral parabrachial nucleus**
(visceral-sensory and pain/aversion relay), the **medial parabrachial
nucleus** (respiratory and autonomic relay), and the **subparabrachial
nucleus** (pontine respiratory center). The **PPRF** (here) is the
**horizontal saccadic burst generator**. They are **DIFFERENT
STRUCTURES** — different functional systems (horizontal saccades vs.
visceral-sensory/respiratory). They are **anatomically adjacent** —
this proximity is a **classic source of confusion** — consumers must
**not** conflate the PPRF with the parabrachial area.
**Boundary status (NOT the superior olivary complex — that is an
auditory brainstem relay):** **Boundary case — the PPRF is NOT the
superior olivary complex.** The **superior olivary complex**
(``.../pons/superior_olivary_complex/left/`` and ``.../right/``) is the
**auditory brainstem relay** — it **receives** cochlear nuclei
projections and **processes interaural time and intensity differences**
for **sound localization**. The **PPRF** (here) is the **horizontal
saccadic burst generator**. They are **DIFFERENT STRUCTURES** —
different functional systems (auditory vs. horizontal saccades).
Consumers must **not** conflate the PPRF with the superior olivary
complex.
**Boundary status (NOT the whole pons — the pons is the parent):**
**Boundary case — the PPRF is NOT the whole pons; the pons is the
PARENT.** The **pons** (``.../pons/``) is the **whole metencephalic
brainstem segment** — it contains the **basilar pons**, the **pontine
tegmentum**, the **pontine nuclei**, the **corticospinal /
corticobulbar tracts**, the **middle cerebellar peduncle**, the
**cranial_nerve_nuclei**, the **parabrachial area**, and the **PPRF**.
The **PPRF** (here) is the **paramedian pontine tegmental premotor burst
generator** only. Consumers must **not** conflate the PPRF with the
**whole pons**.
**Boundary status (MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — EBNs and
IBNs):** **Boundary case — the PPRF is NOT a single uniform neuron
population; it contains MULTIPLE functionally distinct populations.**
The **excitatory burst neurons (EBNs)** — the **premotor neurons** that
**generate the velocity command** for **ipsilateral horizontal
saccades** and **project to the ipsilateral abducens nucleus** (and,
via the abducens internuclear neurons, to the **contralateral medial
rectus subnucleus**) — they are the **primary output** of the PPRF for
**ipsilateral horizontal saccades**. The **inhibitory burst neurons
(IBNs)** — the **premotor neurons** that **project to the
contralateral abducens nucleus** and the **contralateral PPRF** — they
**inhibit** the **contralateral abducens nucleus** during **ipsilateral
horizontal saccades**, **preventing** the **contralateral eye** from
**moving in the wrong direction** (they **coordinate** the **yoked
conjugate eye movement**). **These populations are prose, not structural
children.** Consumers must **not** treat the PPRF as a single uniform
population — it is a **functionally heterogeneous complex** with
**distinct** sub-circuits.
**Boundary status (SLEA-FREE — the PPRF is NOT an extended-amygdala
component):** **Boundary case — the PPRF is SLEA-FREE.** The **SLEA
overlap** belongs to the **central nucleus** (the **only SLEA
component** in the amygdala) and to the **BNST**, **ventral pallidum**,
and **nucleus accumbens** (wired elsewhere). The **PPRF** is a
**pontine horizontal saccadic burst generator** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the PPRF — it is
**SLEA-free**.

Overview
--------
The PPRF is the **horizontal saccadic burst generator** of the **pons** —
a **functionally defined region** of **premotor burst neurons** in the
**paramedian pontine tegmentum**, just **ventral to the abducens
nucleus** and the **MLF**. It is a **leaf** module under the pons
container, and it is the **velocity-command generator** for **horizontal
saccades** and **horizontal pursuit** — the **premotor node** that
**drives** the abducens nucleus for voluntary and visually guided
horizontal eye movements.

**The PPRF is a LEAF, not a container.** It has **no structural
children**. The **EBNs**, **IBNs**, and **other premotor populations**
are **prose populations**, not structural children.

**The PPRF is a FUNCTIONALLY DEFINED REGION, NOT a cytologically
distinct nucleus.** Unlike the abducens nucleus (compact somatic motor)
or the vestibular nuclei (compact special sensory complex), the PPRF is
a **functionally defined group of premotor burst neurons** in the
paramedian pontine tegmentum — it is defined by its **axonal
projections** (to the abducens nucleus) and its **functional role**
(horizontal saccadic burst generation), rather than by a **distinct
cytoarchitectonic boundary**.

**The PPRF is a PREMOTOR COMMAND NODE, NOT the motor output node.** The
PPRF is the **burst generator** that generates the velocity command for
horizontal saccades — it **projects to** the **abducens nucleus**, which
is the **motor output node** that **drives the extraocular muscles**.
**This distinction is clinically load-bearing** — a **PPRF lesion**
causes **ipsilateral horizontal gaze palsy** (the eyes cannot look
toward the lesion side); an **abducens nucleus lesion** also causes
**ipsilateral horizontal gaze palsy**, but the **associated signs**
differ.

**The PPRF is NOT the abducens nucleus, the MLF, the vestibular nuclei,
the NPH, the superior colliculus, or the frontal eye fields.** Those are
**upstream** or **downstream** structures — the **frontal eye fields**
and **superior colliculus** are **upstream** command generators; the
**abducens nucleus** is the **downstream motor output node**; the
**MLF** is the **white-matter tract** carrying the internuclear axons;
the **vestibular nuclei** drive the **VOR**; the **NPH** is the **neural
integrator**. The PPRF is the **pontine burst generator** that sits
**between** the upstream command generators and the downstream motor
output node.

**The PPRF is a TWO-POPULATION complex.** The **EBNs** (excitatory burst
neurons) drive **ipsilateral horizontal saccades** via the **ipsilateral
abducens nucleus**; the **IBNs** (inhibitory burst neurons) inhibit the
**contralateral abducens nucleus** and the **contralateral PPRF** during
**ipsilateral horizontal saccades**, coordinating the **yoked conjugate
eye movement**.

**The PPRF is SLEA-FREE.** It is **not** an extended-amygdala component,
and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The PPRF contains **two functionally distinct neuron populations** —
documented as **prose**, not as structural children:

*   **Excitatory burst neurons (EBNs)** — the **premotor neurons** that
    **generate the velocity command** for **ipsilateral horizontal
    saccades** and **project to the ipsilateral abducens nucleus** (and,
    via the abducens internuclear neurons, to the **contralateral medial
    rectus subnucleus**). They are the **primary output** of the PPRF
    for **ipsilateral horizontal saccades** — they **drive** the
    ipsilateral abducens nucleus **to abduct the ipsilateral eye** and
    (via the internuclear neurons) **to adduct the contralateral eye**.
    **Ipsilateral horizontal saccades are the functional system**
    subserved primarily by the EBNs.

*   **Inhibitory burst neurons (IBNs)** — the **premotor neurons** that
    **project to the contralateral abducens nucleus** and the
    **contralateral PPRF**. They **inhibit** the contralateral abducens
    nucleus during **ipsilateral horizontal saccades**, preventing the
    contralateral eye from moving in the wrong direction (they
    coordinate the **yoked conjugate eye movement**). They also inhibit
    the **contralateral PPRF** during **ipsilateral horizontal
    saccades** — this **reciprocal inhibition** ensures that the **two
    PPRFs** do not **co-activate** (which would cause **bilateral
    horizontal gaze**). **Contralateral inhibition and conjugate eye
    movement coordination are the functional systems** subserved
    primarily by the IBNs.

**These populations are prose, not structural children.** The tree wires
the **PPRF** as a **single leaf** under the pons container — the
**EBNs** and **IBNs** are **prose**, not structural children. Consumers
that need **neuron-population-level** resolution should consult the
references, not the tree.

The PPRF / Abducens Nucleus Boundary
------------------------------------
This is the **premotor vs. motor output** boundary:

*   **PPRF** (this module) — the **premotor burst generator** that
    generates the velocity command for horizontal saccades.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/`` and
    ``.../right/``) — the **somatic motor** nucleus for the **lateral
    rectus** — the **final common pathway** for **horizontal gaze**.

**They are DIFFERENT STRUCTURES** — the **PPRF** is **upstream
premotor**; the **abducens nucleus** is **downstream motor**. **This
distinction is clinically load-bearing** — a **PPRF lesion** causes
**ipsilateral horizontal gaze palsy** (the eyes cannot look toward the
lesion side); an **abducens nucleus lesion** also causes **ipsilateral
horizontal gaze palsy**, but the **associated signs** differ — **PPRF
lesions** may accompany **contralateral hemiparesis** (Foville syndrome)
or **ipsilateral facial palsy** (Foville syndrome); **abducens nucleus
lesions** may accompany **ipsilateral facial palsy** and **contralateral
hemiparesis** (Foville syndrome — same syndrome, overlapping
structures). Consumers must **not** conflate the PPRF with the abducens
nucleus.

The PPRF / MLF Boundary
-----------------------
This is the **premotor vs. white-matter tract** boundary:

*   **PPRF** (this module) — the **grey-matter premotor burst
    generator** that **drives** the abducens nucleus.

*   **Medial longitudinal fasciculus (MLF)** — the **white-matter
    tract** that carries the **internuclear neuron axons** from the
    abducens nucleus to the **contralateral medial rectus subnucleus**
    of the oculomotor nucleus.

**They are DIFFERENT STRUCTURES** — the **PPRF** is grey matter and
**upstream of the abducens nucleus**; the **MLF** is white matter and
**downstream of the abducens nucleus**. **This distinction is clinically
load-bearing** — an **MLF lesion** causes **internuclear ophthalmoplegia
(INO)**; a **PPRF lesion** causes **ipsilateral horizontal gaze palsy**.
Consumers must **not** conflate the PPRF with the MLF.

The PPRF / Vestibular Nuclei Boundary
-------------------------------------
This is the **voluntary saccade vs. VOR** boundary:

*   **PPRF** (this module) — the **voluntary saccadic burst generator**
    — it drives the abducens nucleus for **voluntary horizontal
    saccades** and **horizontal pursuit**.

*   **Vestibular nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``
    and ``.../right/``) — the **special sensory** nuclei for **balance
    and spatial orientation** — they drive the **vestibulo-ocular
    reflex (VOR)** by projecting to the abducens nucleus and the
    oculomotor nucleus (via the MLF).

**They are DIFFERENT STRUCTURES** — the **vestibular nuclei** drive the
**VOR** (reflexive, vestibular-driven eye movements); the **PPRF**
drives **voluntary saccades** (cortical and collicular-driven eye
movements). The two systems **converge** on the abducens nucleus but
**subserve different functions** — **VOR** vs. **voluntary saccades**.
**This distinction is clinically load-bearing** — a **vestibular nuclei
lesion** causes **vestibular syndrome** (vertigo, nystagmus, VOR
deficit); a **PPRF lesion** causes **horizontal gaze palsy** (loss of
voluntary saccades, but the VOR may be **preserved**). Consumers must
**not** conflate the PPRF with the vestibular nuclei.

The PPRF / NPH Boundary
-----------------------
This is the **velocity command vs. neural integrator** boundary:

*   **PPRF** (this module) — the **velocity command generator** that
    generates the saccadic velocity burst.

*   **Nucleus prepositus hypoglossi (NPH)**
    (``.../medulla_oblongata/perihypoglossal_nuclei/prepositus_nucleus/``)
    — the **horizontal gaze neural integrator** that **converts** the
    velocity command from the PPRF into a **position** command that
    **holds the eyes in eccentric gaze**.

**They are DIFFERENT STRUCTURES** — the **NPH** is the **integrator**;
the **PPRF** is the **velocity command generator**. **This distinction
is clinically load-bearing** — an **NPH lesion** causes **gaze-evoked
nystagmus** (the eyes cannot **hold** eccentric gaze); a **PPRF lesion**
causes **horizontal gaze palsy** (the eyes cannot **move** toward the
lesion side). Consumers must **not** conflate the PPRF with the NPH.

The PPRF / Superior Colliculus Boundary
---------------------------------------
This is the **pontine burst generator vs. midbrain command generator**
boundary:

*   **PPRF** (this module) — the **pontine burst generator** that
    generates the velocity burst that drives the abducens nucleus.

*   **Superior colliculus**
    (``.../midbrain/tectum/corpora_quadrigemina/left/superior_colliculus/``
    and ``.../right/``) — the **midbrain sensorimotor integration
    center** for **saccades** — it receives visual, auditory, and
    somatosensory inputs and **generates** the **saccade command** (the
    desired displacement) that is **relayed** to the PPRF (for
    horizontal saccades) or the **riMLF** (for vertical saccades).

**They are DIFFERENT STRUCTURES** — the **superior colliculus** is
**upstream** (in the midbrain); the **PPRF** is **downstream** (in the
pons) and **burst-generating** (not command-generating). **This
distinction is clinically load-bearing** — a **superior colliculus
lesion** causes **saccadic deficits** (impaired saccade initiation) but
not typically **full horizontal gaze palsy**; a **PPRF lesion** causes
**complete ipsilateral horizontal gaze palsy** (loss of both voluntary
saccades and horizontal pursuit). Consumers must **not** conflate the
PPRF with the superior colliculus.

The PPRF / Frontal Eye Fields Boundary
--------------------------------------
This is the **pontine burst generator vs. cortical command generator**
boundary:

*   **PPRF** (this module) — the **pontine burst generator** that
    generates the velocity burst that drives the abducens nucleus.

*   **Frontal eye fields (FEF)** — the **cortical saccade generators**
    — they receive high-level cognitive inputs (attention, working
    memory, decision-making) and **project** to the superior colliculus
    and, via the **corticobulbar** and **corticopontine** pathways, to
    the PPRF (directly and indirectly).

**They are DIFFERENT STRUCTURES** — the **frontal eye fields** are
**cortical** and **upstream**; the **PPRF** is **pontine** and
**downstream**. Consumers must **not** conflate the PPRF with the
frontal eye fields.

The PPRF / NRTP Boundary
------------------------
This is the **burst generator vs. basilar pons relay** boundary:

*   **PPRF** (this module) — the **pontine burst generator** that
    generates the velocity burst that drives the abducens nucleus.

*   **Nucleus reticularis tegmenti pontis (NRTP)** — the
    **cortico-ponto-cerebellar relay** in the **basilar pons** that
    **receives** cortical inputs (including from the frontal eye
    fields) and **projects to the cerebellum** (especially the
    **oculomotor vermis** and the **fastigial nucleus**) — it
    **contributes** to **saccade adaptation** and **cerebellar control
    of eye movements**.

**They are DIFFERENT STRUCTURES** — the **NRTP** is a **basilar pons
relay to the cerebellum**; the **PPRF** is a **dorsal tegmental burst
generator** to the abducens nucleus. Consumers must **not** conflate the
PPRF with the NRTP.

The PPRF / riMLF Boundary
-------------------------
This is the **horizontal vs. vertical** boundary:

*   **PPRF** (this module) — the **horizontal saccadic burst
    generator** in the **pons** — it drives the **abducens nucleus** for
    **horizontal saccades** and **horizontal pursuit**.

*   **Rostral interstitial nucleus of the MLF (riMLF)**
    (``.../midbrain/tegmentum/rostral_interstitial_nucleus_mlf/left/``
    and ``.../right/``) — the **vertical saccadic burst generator** in
    the **midbrain** — it drives the **oculomotor nucleus** and the
    **trochlear nucleus** for **vertical saccades** and **vertical
    pursuit**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
midbrain), different functional systems (horizontal vs. vertical
saccades). **This distinction is clinically load-bearing** — a **PPRF
lesion** causes **horizontal gaze palsy**; a **riMLF lesion** causes
**vertical gaze palsy** (including **Parinaud syndrome** when the
**dorsal midbrain** is involved). Consumers must **not** conflate the
PPRF with the riMLF.

The PPRF / cMRF Boundary
------------------------
This is the **pontine burst generator vs. midbrain premotor region**
boundary:

*   **PPRF** (this module) — the **pontine burst generator** — it
    receives the cMRF and superior colliculus commands and **generates**
    the **velocity burst**.

*   **Central mesencephalic reticular formation (cMRF)** — a
    **premotor region** in the **midbrain** that **contributes** to
    **saccade generation** (especially **contralateral horizontal
    saccades** — it is **upstream** of the PPRF in some models).

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
midbrain), different functional roles (premotor region vs. burst
generator). Consumers must **not** conflate the PPRF with the cMRF.

The PPRF / Pontine Nuclei Boundary
----------------------------------
This is the **dorsal tegmental vs. basilar pons** boundary:

*   **PPRF** (this module) — the **dorsal tegmental** premotor burst
    generator.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/left/`` and
    ``.../right/``) — the **cortico-ponto-cerebellar relay** in the
    **basilar pons** — they receive corticopontine fibers from the
    cerebral cortex and **project** to the **contralateral cerebellar
    cortex** via the **middle cerebellar peduncle**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. horizontal saccades). Consumers must
**not** conflate the PPRF with the pontine nuclei.

The PPRF / Locus Coeruleus Boundary
-----------------------------------
This is the **anatomically adjacent** boundary — **horizontal saccades
vs. noradrenergic nucleus**:

*   **PPRF** (this module) — the **horizontal saccadic burst
    generator**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of
    norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, etc. vs. norepinephrine), different functional systems
(horizontal saccades vs. noradrenergic arousal). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the PPRF with the locus
coeruleus.

The PPRF / Parabrachial Area Boundary
-------------------------------------
This is the **anatomically adjacent** boundary — **horizontal saccades
vs. visceral-sensory/respiratory relay**:

*   **PPRF** (this module) — the **horizontal saccadic burst
    generator**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex**.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal saccades vs. visceral-sensory/respiratory). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the PPRF with the
parabrachial area.

The PPRF / Superior Olivary Complex Boundary
--------------------------------------------
This is the **horizontal saccades vs. auditory** boundary:

*   **PPRF** (this module) — the **horizontal saccadic burst
    generator**.

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/left/`` and ``.../right/``) —
    the **auditory brainstem relay** for **sound localization**.

**They are DIFFERENT STRUCTURES** — different functional systems
(horizontal saccades vs. auditory). Consumers must **not** conflate the
PPRF with the superior olivary complex.

The PPRF / Pons Boundary
------------------------
This is the **leaf vs. parent** boundary:

*   **PPRF** (this module) — the **paramedian pontine tegmental
    premotor burst generator** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal /
    corticobulbar tracts**, the **middle cerebellar peduncle**, the
    **cranial-nerve nuclei**, the **parabrachial area**, and the
    **PPRF**.

**The PPRF is a child of the pons.** Consumers must **not** conflate the
PPRF with the **whole pons**.

The PPRF / SLEA Boundary
------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **PPRF** (this module) — **SLEA-FREE**. It is **not** an
    extended-amygdala component, and it carries **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The PPRF is NOT part of the SLEA continuum.** It is a **pontine
horizontal saccadic burst generator**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the PPRF.

Function in the Human Brain
---------------------------
The PPRF's functions are **the generation of the horizontal saccadic
velocity command** and **the coordination of conjugate horizontal eye
movements** — **NOT a single unified function**:

*   **Horizontal Saccade Generation (EBNs):** The **excitatory burst
    neurons (EBNs)** **generate** the **velocity command** for
    **ipsilateral horizontal saccades** — they **drive** the
    **ipsilateral abducens nucleus** to **abduct the ipsilateral eye**
    and (via the abducens internuclear neurons) **adduct the
    contralateral eye**. This is the **primary function** of the PPRF —
    the **voluntary and visually guided horizontal saccades** that move
    the eyes to a new target.

*   **Conjugate Eye Movement Coordination (IBNs):** The **inhibitory
    burst neurons (IBNs)** **inhibit** the **contralateral abducens
    nucleus** and the **contralateral PPRF** during **ipsilateral
    horizontal saccades** — they **coordinate** the **yoked conjugate
    eye movement** (both eyes move in the same direction) and **prevent
    co-activation** of the **two PPRFs** (which would cause **bilateral
    horizontal gaze**).

*   **Horizontal Pursuit:** The PPRF also **contributes** to
    **horizontal pursuit** — the **slow, continuous eye movements**
    that track a moving target. The **EBNs** and **other PPRF neurons**
    **generate** the **velocity command** for **horizontal pursuit**
    (with different dynamics from **saccades** — **pursuit** is a
    **continuous** velocity command, **saccades** are a **pulsed**
    velocity command).

*   **Saccade Adaptation:** The PPRF **receives** inputs from the
    **cerebellum** (via the **NRTP** and the **fastigial nucleus**) —
    it **contributes** to **saccade adaptation** — the **cerebellar
    recalibration** of saccade amplitude in response to **visual
    errors**.

*   **NOT a neural processor in the classical sense.** The PPRF is a
    **premotor burst generator** — it **receives** the **saccade
    command** from the **superior colliculus** (and, via the
    **NRTP**, from the **frontal eye fields**) and **generates** the
    **velocity burst** that drives the abducens nucleus. The
    **processing** of the **saccade command** happens in the
    **superior colliculus** (sensorimotor integration), the **frontal
    eye fields** (cognitive control), and the **cerebellum** (saccade
    adaptation). The PPRF is the **pontine burst generator** — the
    **premotor output node** that **converts** the **saccade command**
    into a **velocity command**.

**The unifying theme:** the PPRF is the **horizontal saccadic burst
generator** — the **pontine premotor command node** that **drives** the
abducens nucleus for **horizontal saccades** and **horizontal pursuit**.
It is a **functionally heterogeneous complex** (EBNs for ipsilateral
saccades; IBNs for contralateral inhibition and conjugate
coordination), **SLEA-free**, and **NOT the abducens nucleus** — the
**abducens nucleus** is the **downstream motor output node**; the
**PPRF** is the **upstream premotor command node**.

Associated Disorders
--------------------
The PPRF has **no named "PPRF syndrome"** — its clinical associations
are **nucleus-specific**, and they are **distinguishable from
nerve-level, MLF-level, and other brainstem-level lesions**:

*   **PPRF Lesion — Ipsilateral Horizontal Gaze Palsy:** A lesion of the
    **left PPRF** causes **leftward horizontal gaze palsy** — **both
    eyes cannot look left** (the left eye cannot abduct because the
    abducens nucleus is not driven; the right eye cannot adduct because
    the abducens internuclear neurons are not driven). **This is the
    classic "PPRF lesion" pattern** — **voluntary horizontal saccades
    and horizontal pursuit** are **lost** toward the lesion side. **The
    VOR may be preserved** (because the vestibular nuclei project
    directly to the abducens nucleus, bypassing the PPRF) — this is the
    **key clinical distinction** between a **PPRF lesion** and an
    **abducens nucleus lesion** (in which the VOR is also lost).

*   **Abducens Nucleus Lesion — Ipsilateral Horizontal Gaze Palsy:**
    A lesion of the **left abducens nucleus** also causes **leftward
    horizontal gaze palsy** — but the **VOR is lost** (because the
    abducens nucleus is the **final common pathway** for both voluntary
    saccades and VOR). **This is the key clinical distinction** from a
    PPRF lesion — a **PPRF lesion** causes **gaze palsy with preserved
    VOR**; an **abducens nucleus lesion** causes **gaze palsy with lost
    VOR**.

*   **MLF Lesion — Internuclear Ophthalmoplegia (INO):** A lesion of the
    **left MLF** causes **left INO** — **impaired adduction of the left
    eye** with **dissociated nystagmus of the right (abducting) eye**.
    **This is distinct from** a **PPRF lesion** — the **left eye can
    still abduct** (the left PPRF and abducens nucleus are intact); the
    **deficit** is in **adduction** (the left MLF is damaged).

*   **One-and-a-Half Syndrome — PPRF/Abducens Nucleus + Adjacent MLF
    Lesion:** A lesion of the **left PPRF** (or **left abducens
    nucleus**) **plus** the **adjacent left MLF** causes
    **one-and-a-half syndrome** — **leftward horizontal gaze palsy**
    (the "one") **plus** **left INO** (the "half"). The only preserved
    horizontal movement is **rightward abduction of the right eye**.
    **The PPRF is the substrate of the "one" component** (when the
    lesion involves the PPRF) or the **abducens nucleus** (when the
    lesion involves the abducens nucleus) — the "half" component is the
    MLF.

*   **Foville Syndrome — PPRF/Abducens Nucleus + Facial Fibers +
    Corticospinal Tract:** A lesion of the **left pontine tegmentum**
    involving the **left PPRF** (or **left abducens nucleus**), the
    **left facial nerve fibers** (which loop around the abducens
    nucleus), and the **left corticospinal tract** causes **Foville
    syndrome** — **leftward horizontal gaze palsy** + **left facial
    palsy** + **right hemiparesis**. **The PPRF is the substrate of the
    gaze palsy component** (when the lesion involves the PPRF) — the
    **associated facial palsy and hemiparesis** reflect the **broader
    pontine tegmentum** involvement.

*   **Wernicke's Encephalopathy — PPRF Involvement:** **Wernicke's
    encephalopathy** (thiamine deficiency) can affect the **PPRF**
    (among other brainstem and diencephalic structures), contributing
    to **horizontal gaze palsy** and **nystagmus**.

*   **Parinaud Syndrome (Dorsal Midbrain Syndrome) — NOT a PPRF
    Syndrome:** **Parinaud syndrome** is a **dorsal midbrain
    syndrome** caused by **lesions of the superior colliculus, the
    pretectum, or the posterior commissure** — it causes **vertical
    gaze palsy** (**upgaze palsy** is the classic sign),
    **light-near dissociation** of the pupils, and **convergence-
    retraction nystagmus**. **Parinaud syndrome does NOT involve the
    PPRF** — it is a **vertical gaze** disorder (the **riMLF** in the
    midbrain is the **vertical** saccadic burst generator, not the
    PPRF). Consumers must **not** conflate a **PPRF lesion**
    (**horizontal gaze palsy**) with **Parinaud syndrome** (**vertical
    gaze palsy**).

*   **Internuclear Ophthalmoplegia (INO) — NOT a PPRF Syndrome:** **INO**
    is caused by a **lesion of the MLF** — it causes **impaired
    adduction** of the ipsilateral eye with **dissociated nystagmus**
    of the abducting eye. **INO does NOT involve the PPRF** — the
    **PPRF** is **upstream of the MLF** (the PPRF drives the abducens
    nucleus; the MLF carries the abducens internuclear axons to the
    contralateral oculomotor nucleus). Consumers must **not** conflate
    a **PPRF lesion** (**horizontal gaze palsy**) with **INO** (an
    **MLF** lesion).

*   **Abducens Nerve Palsy — NOT a PPRF Syndrome:** **Abducens nerve
    palsy** (a **nerve-level** lesion) causes **ipsilateral lateral
    rectus palsy** — **inability to abduct the ipsilateral eye** with
    **esotropia** at rest. **Abducens nerve palsy does NOT involve the
    PPRF** — the **abducens nerve** is **downstream of the abducens
    nucleus** (which is **downstream of the PPRF**). Consumers must
    **not** conflate a **PPRF lesion** (**horizontal gaze palsy**) with
    an **abducens nerve palsy** (**lateral rectus palsy**).

*   **Locked-in Syndrome — NOT a PPRF Syndrome:** **Locked-in
    syndrome** is caused by a **bilateral ventral pontine lesion**
    (e.g. **basilar artery occlusion**) — it causes **quadriplegia**
    and **bulbar palsy** with **preserved consciousness** and
    **preserved vertical eye movements** and **blinking**. **Locked-in
    syndrome does NOT involve the PPRF** — the **PPRF** is in the
    **dorsal pontine tegmentum** (the **ventral pons** is affected in
    locked-in syndrome, sparing the **dorsal tegmentum**). Consumers
    must **not** conflate a **PPRF lesion** (**horizontal gaze palsy**)
    with **locked-in syndrome** (**bilateral ventral pontine lesion**).

*   **No Named "PPRF Syndrome":** The PPRF is a **functionally defined
    region** — it has **no named clinical syndrome** of its own. Its
    clinical relevance is **horizontal-gaze-specific** — **ipsilateral
    horizontal gaze palsy** (which is the **same symptom** as an
    **abducens nucleus lesion**, distinguishable by **VOR preservation**
    and **associated brainstem signs**).

**What is NOT here:** The PPRF is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN
VIII nerve), **trigeminal neuralgia** (trigeminal nerve root),
**Parinaud syndrome** (dorsal midbrain — vertical gaze), **INO** (MLF),
**abducens nerve palsy** (CN VI nerve), or **locked-in syndrome**
(bilateral ventral pons). Its clinical relevance is
**horizontal-gaze-specific**, via the **ipsilateral horizontal gaze
palsy** it causes. **No named PPRF syndrome exists.**

Lateralization Notes
--------------------
This is the **single** PPRF module. The PPRF is **bilateral in real
anatomy** (left and right paramedian pontine tegmentum), but the tree
wires it as a **single module** — and the module carries **NO warning at
the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **paramedian_pontine_reticular_formation** module (here) is a
    **single module** that represents the **bilateral PPRF** (left and
    right paramedian pontine tegmentum). The tree does **not** split
    them into left/right. Consumers must **not** assume a left/right
    split exists at the tree level — the module is a **single, bilateral
    representation**.

*   **Ipsilateral Saccade Generation and Contralateral Inhibition
    (Structural Fact, NOT a Lateralization Warning):** The **left PPRF**
    **drives** the **ipsilateral (left) abducens nucleus** for
    **leftward horizontal saccades** (the left eye abducts; the right
    eye adducts via the abducens internuclear neurons). The **left PPRF
    IBNs** **inhibit** the **contralateral (right) abducens nucleus**
    and the **contralateral (right) PPRF** during **leftward horizontal
    saccades**. This **ipsilateral drive and contralateral inhibition**
    is a **structural fact** of the **horizontal saccade generator** —
    it is **not** a functional lateralization. It is the **neural
    substrate** of the **yoked conjugate eye movement** and of the
    **ipsilateral horizontal gaze palsy** in **PPRF lesions**.

*   **Reciprocal Inhibition between the Two PPRFs (Structural Fact, NOT
    a Lateralization Warning):** The **two PPRFs** (left and right) are
    **reciprocally inhibited** by their **IBNs** — when the **left PPRF**
    is **active** (for **leftward saccades**), the **right PPRF** is
    **inhibited**; when the **right PPRF** is **active** (for
    **rightward saccades**), the **left PPRF** is **inhibited**. This
    **reciprocal inhibition** ensures that the eyes move **conjugately**
    (both eyes in the **same direction**) rather than **bilaterally**
    (both eyes moving **toward the midline** or **away from the
    midline**, which would be **dysconjugate**). **This is a structural
    fact** of the horizontal saccade generator — it is **not** a
    functional lateralization.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The PPRF is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the PPRF.

*   **NO Amygdala-Lateralization Warning of their own (the PPRF is
    HORIZONTAL SACCADE GENERATION, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The PPRF is a **pontine
    horizontal saccadic burst generator** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**.

**A consumer that sees "paramedian_pontine_reticular_formation" must
understand that the module is a SINGLE, BILATERAL representation** — it
is **not** a left/right split at the tree level. The **ipsilateral
saccade generation**, the **contralateral inhibition**, and the
**reciprocal inhibition between the two PPRFs** are **structural
facts**, not lateralizations. The PPRF is a **strict-single module with
NO warning at the module level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** PPRF as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/``, ``.../pons/tegmentum/``,
    ``.../midbrain/``, ``.../medulla_oblongata/``, ``.../cortex/``, or
    any other container. The PPRF's relationships to the **abducens
    nucleus**, the **MLF**, the **vestibular nuclei**, the **NPH**, the
    **superior colliculus**, the **frontal eye fields**, the **NRTP**,
    the **riMLF**, the **cMRF**, the **pontine nuclei**, the **locus
    coeruleus**, the **parabrachial area**, the **superior olivary
    complex**, the **pons**, and the **SLEA continuum** are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **EBNs**, **IBNs**,
    and **other premotor populations** are documented as **prose**, not
    as sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **PPRF** is a **single module** that represents the **bilateral
    PPRF** — the tree does **not** split it into left/right. Consumers
    must **not** assume a left/right split exists at the tree level.
*   **FUNCTIONALLY DEFINED REGION — NOT a cytologically distinct
    nucleus.** The **PPRF** is a **functionally defined group of
    premotor burst neurons** in the **paramedian pontine tegmentum**,
    defined by its **axonal projections** (to the abducens nucleus) and
    its **functional role** (horizontal saccadic burst generation) —
    not by a **distinct cytoarchitectonic boundary**. Consumers must
    **not** expect a **compact, cytologically distinct nucleus**.
*   **PREMOTOR COMMAND NODE — NOT the motor output node.** The **PPRF**
    is the **burst generator** that generates the **velocity command**
    for horizontal saccades — it **projects to** the **abducens
    nucleus**, which is the **motor output node**. Consumers must
    **not** conflate the PPRF with the abducens nucleus.
*   **TWO FUNCTIONALLY DISTINCT POPULATIONS — EBNs vs. IBNs.** The
    **EBNs** (excitatory burst neurons) drive **ipsilateral horizontal
    saccades** via the **ipsilateral abducens nucleus**; the **IBNs**
    (inhibitory burst neurons) inhibit the **contralateral abducens
    nucleus** and the **contralateral PPRF** during **ipsilateral
    horizontal saccades**, coordinating the **yoked conjugate eye
    movement**. These populations are **prose**, not structural
    children. Consumers must **not** treat the PPRF as a single uniform
    population.
*   **NOT the abducens nucleus — that is the DOWNSTREAM MOTOR OUTPUT
    NODE.** The **abducens nucleus** is the **final common pathway**
    for horizontal gaze. Consumers must **not** conflate the PPRF with
    the abducens nucleus.
*   **NOT the MLF — that is the WHITE-MATTER TRACT carrying internuclear
    axons.** The **MLF** is **downstream of the abducens nucleus**;
    the **PPRF** is **upstream**. Consumers must **not** conflate the
    PPRF with the MLF.
*   **NOT the vestibular nuclei — those are the VOR input.** The
    **vestibular nuclei** drive the **VOR** (reflexive eye movements);
    the **PPRF** drives **voluntary saccades** (cortical and collicular
    eye movements). Consumers must **not** conflate the PPRF with the
    vestibular nuclei.
*   **NOT the NPH — that is the NEURAL INTEGRATOR.** The **NPH**
    integrates the velocity command from the PPRF into a position
    command. Consumers must **not** conflate the PPRF with the NPH.
*   **NOT the superior colliculus or the frontal eye fields — those are
    UPSTREAM command generators.** The **superior colliculus** is the
    **midbrain sensorimotor integration center** for saccades; the
    **frontal eye fields** are the **cortical saccade generators**.
    Consumers must **not** conflate the PPRF with the superior colliculus
    or the frontal eye fields.
*   **NOT the NRTP, the riMLF, or the cMRF — those are different pontine
    or midbrain structures.** The **NRTP** is a **basilar pons relay to
    the cerebellum**; the **riMLF** is the **vertical saccadic burst
    generator** in the midbrain; the **cMRF** is a **midbrain premotor
    region**. Consumers must **not** conflate the PPRF with any of them.
*   **NOT the pontine nuclei, the locus coeruleus, the parabrachial area,
    or the superior olivary complex — those are different pontine
    structures.** The **pontine nuclei** are the **cortico-ponto-
    cerebellar relay**; the **locus coeruleus** is the **noradrenergic
    nucleus**; the **parabrachial area** is the **visceral-sensory and
    respiratory-relay complex**; the **superior olivary complex** is the
    **auditory brainstem relay**. Consumers must **not** conflate the
    PPRF with any of them.
*   **SLEA-FREE — no extended-amygdala relationship.** The PPRF is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the PPRF is HORIZONTAL SACCADE
    GENERATION.** The **fear-output** structure is the **central
    nucleus**; the **fear-learning** structures are the **basolateral
    nuclei**; the **fear-modulatory / extinction** structures are the
    **basomedial nuclei**. The **PPRF** is a **pontine horizontal
    saccadic burst generator** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The PPRF is a local leaf under the pons
    container, not a cross-listed leaf.
*   **No nested cross-listing.** The PPRF has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import paramedian_pontine_reticular_formation

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons."
        "paramedian_pontine_reticular_formation"
    )

**Do not** assume the PPRF is a **container**. It is a **leaf** — the
**EBNs**, **IBNs**, and **other premotor populations** are **prose**,
not structural children.

**Do not** assume the PPRF is **bilateralized at the tree level**. The
PPRF is **bilateral in real anatomy**, but the tree wires it as a
**single module** — there is **no left/right split**.

**Do not** assume the PPRF is a **compact, cytologically distinct
nucleus**. The **PPRF** is a **functionally defined group of premotor
burst neurons** in the **paramedian pontine tegmentum** — it is defined
by its **axonal projections** (to the abducens nucleus) and its
**functional role** (horizontal saccadic burst generation), not by a
**distinct cytoarchitectonic boundary**.

**Do not** assume the PPRF is the **abducens nucleus**. The **abducens
nucleus** is the **downstream motor output node** — the **final common
pathway** for horizontal gaze. The **PPRF** is the **upstream premotor
command node**. They are **different structures**.

**Do not** assume the PPRF is the **MLF**. The **MLF** is the
**white-matter tract** that carries the internuclear axons from the
**abducens nucleus** to the **contralateral medial rectus subnucleus** —
it is **downstream of the abducens nucleus**. The **PPRF** is
**upstream of the abducens nucleus**.

**Do not** assume the PPRF is the **vestibular nuclei** or the **NPH**.
The **vestibular nuclei** drive the **VOR**; the **NPH** is the
**neural integrator**. They are **different structures**.

**Do not** assume the PPRF is the **superior colliculus**, the **frontal
eye fields**, the **NRTP**, the **riMLF**, or the **cMRF**. Those are
**upstream command generators** (superior colliculus, frontal eye
fields), **different relays** (NRTP), or **different premotor regions**
(riMLF, cMRF). They are **different structures**.

**Do not** assume the PPRF is the **pontine nuclei**, the **locus
coeruleus**, the **parabrachial area**, or the **superior olivary
complex**. Those are **different pontine structures** — the **pontine
nuclei** are the **cortico-ponto-cerebellar relay**; the **locus
coeruleus** is the **noradrenergic nucleus**; the **parabrachial area**
is the **visceral-sensory and respiratory-relay complex**; the
**superior olivary complex** is the **auditory brainstem relay**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the PPRF. **The PPRF is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the PPRF's (empty) children (recommended consumer pattern)::

    PARAMEDIAN_PONTINE_RETICULAR_FORMATION_CHILDREN = ()
    # The PPRF is a leaf. The EBNs, IBNs, and other premotor populations
    # are prose, not modules.

Reaching the abducens nucleus (recommended consumer pattern — the
DOWNSTREAM MOTOR OUTPUT NODE)::

    # The abducens nucleus is the DOWNSTREAM MOTOR OUTPUT NODE for
    # horizontal gaze — the final common pathway that the PPRF drives:
    #
    #   .../cranial_nerve_nuclei/left/abducens_nucleus/  (and right/)
    #
    # The PPRF is the PREMOTOR COMMAND NODE; the abducens nucleus is the
    # MOTOR OUTPUT NODE. They are DIFFERENT STRUCTURES.

Reaching the MLF (recommended consumer pattern — the white-matter
tract)::

    # The MLF is the WHITE-MATTER tract that carries the internuclear
    # axons from the abducens nucleus to the contralateral medial rectus
    # subnucleus:
    #
    #   .../white_matter/.../medial_longitudinal_fasciculus/  (or equivalent path)
    #
    # The PPRF is UPSTREAM of the abducens nucleus; the MLF is DOWNSTREAM
    # of the abducens nucleus. They are DIFFERENT STRUCTURES.

Reaching the vestibular nuclei (recommended consumer pattern — the VOR
input)::

    # The vestibular nuclei are the SPECIAL SENSORY nuclei that drive the
    # VESTIBULO-OCULAR REFLEX (VOR):
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/  (and right/)
    #
    # The vestibular nuclei drive the VOR; the PPRF drives VOLUNTARY
    # SACCADES. They are DIFFERENT STRUCTURES.

Reaching the NPH (recommended consumer pattern — the neural
integrator)::

    # The NPH is the HORIZONTAL GAZE NEURAL INTEGRATOR that converts the
    # velocity command from the PPRF into a position command:
    #
    #   .../medulla_oblongata/perihypoglossal_nuclei/prepositus_nucleus/
    #
    # The NPH is the INTEGRATOR; the PPRF is the VELOCITY COMMAND
    # GENERATOR. They are DIFFERENT STRUCTURES.

Reaching the superior colliculus (recommended consumer pattern — the
UPSTREAM midbrain command generator)::

    # The superior colliculus is the MIDBRAIN SENSORIMOTOR INTEGRATION
    # CENTER for saccades — it is UPSTREAM of the PPRF:
    #
    #   .../midbrain/tectum/corpora_quadrigemina/left/superior_colliculus/  (and right/)
    #
    # The superior colliculus is UPSTREAM (midbrain); the PPRF is
    # DOWNSTREAM (pons) and BURST-GENERATING. They are DIFFERENT
    # STRUCTURES.

Reaching the frontal eye fields (recommended consumer pattern — the
UPSTREAM cortical command generator)::

    # The frontal eye fields are the CORTICAL SACCADE GENERATORS — they
    # are UPSTREAM of the PPRF (via the superior colliculus and the
    # NRTP):
    #
    #   .../cerebral_hemispheres/left/cortex/frontal/gyri/middle_frontal_gyrus/  (and right/)
    #
    # The frontal eye fields are CORTICAL; the PPRF is PONTINE. They are
    # DIFFERENT STRUCTURES.

Reaching the riMLF (recommended consumer pattern — the VERTICAL saccadic
burst generator)::

    # The riMLF is the VERTICAL SACCADIC BURST GENERATOR in the MIDBRAIN
    # — it drives the oculomotor nucleus and the trochlear nucleus for
    # VERTICAL saccades:
    #
    #   .../midbrain/tegmentum/rostral_interstitial_nucleus_mlf/left/  (and right/)
    #
    # The riMLF is the VERTICAL generator; the PPRF is the HORIZONTAL
    # generator. They are DIFFERENT STRUCTURES.

Bilateral iteration (recommended consumer pattern)::

    # The PPRF is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL PPRF.
    pprf_path = (
        "hindbrain.metencephalon.pons.paramedian_pontine_reticular_formation"
    )
    # resolve pprf_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The PPRF's neuron populations are prose, not modules:
    #   excitatory burst neurons (EBNs) -> generate velocity command for
    #                                     ipsilateral horizontal saccades;
    #                                     project to ipsilateral abducens
    #                                     nucleus (and via abducens
    #                                     internuclear neurons to
    #                                     contralateral medial rectus
    #                                     subnucleus); drive ipsilateral
    #                                     horizontal saccades
    #   inhibitory burst neurons (IBNs) -> project to contralateral
    #                                     abducens nucleus and
    #                                     contralateral PPRF; inhibit
    #                                     the contralateral side during
    #                                     ipsilateral saccades; coordinate
    #                                     the yoked conjugate eye movement
    #
    # Do not attempt to resolve these as sub-paths of the PPRF — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical PPRF anatomy:** Büttner-Ennever, J.A. (ed.) (1988).
    *Neuroanatomy of the Oculomotor System*. (PPRF — premotor burst
    generator for horizontal saccades.)
*   **Horizontal saccade generation — review:** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (PPRF, EBNs, and
    IBNs — the horizontal saccadic burst generator.)
*   **Saccadic burst neurons — classical:** Keller, E.L. (1974).
    "Participation of medial pontine reticular formation in eye movement
    generation in monkey." *Journal of Neurophysiology* 37:316–332.
    (PPRF — medial pontine reticular formation and horizontal saccade
    generation.)
*   **EBNs and IBNs — review:** Scudder, C.A., Kaneko, C.R.S., Fuchs,
    A.F. (2002). "The brainstem burst generator for saccadic eye
    movements: a modern synthesis." *Experimental Brain Research*
    142:439–462. (PPRF — EBNs and IBNs; the horizontal saccadic burst
    generator.)
*   **Superior colliculus to PPRF pathway:** Sparks, D.L. (2002). "The
    brainstem control of saccadic eye movements." *Nature Reviews
    Neuroscience* 3:952–964. (Superior colliculus — command generator;
    PPRF — burst generator.)
*   **Frontal eye fields to PPRF pathway:** Segraves, M.A. (1992).
    "Activity of monkey frontal eye field neurons projecting to
    oculomotor regions of the pons." *Journal of Neurophysiology*
    68:1967–1985. (Frontal eye fields — cortical saccade generators;
    projections to PPRF.)
*   **NPH — neural integrator:** Cannon, S.C., Robinson, D.A. (1987).
    "Loss of the neural integrator of the oculomotor system from brain
    stem lesions in monkey." *Journal of Neurophysiology*
    57:1383–1409. (NPH — horizontal gaze neural integrator.)
*   **Abducens nucleus and MLF:** Büttner-Ennever, J.A. (ed.) (1988).
    *Neuroanatomy of the Oculomotor System*. (Abducens nucleus — motor
    output; MLF — internuclear axons.)
*   **Clinical — horizontal gaze palsy:** Pierrot-Deseilligny, C.,
    Milea, D., Müri, R.M. (2019). *Eye Movement Disorders: A Practical
    Guide*. (PPRF vs. abducens nucleus vs. MLF lesions — horizontal
    gaze palsy patterns.)
*   **Foville syndrome:** Foville, A.L.F. (1858). "Note sur une
    paralysie peu connue des six derniers nerfs crâniens." *Bulletin de
    la Société Anatomique de Paris* 33:289–302. (Foville syndrome —
    pontine tegmentum lesion involving PPRF/abducens nucleus, facial
    nerve fibers, and corticospinal tract.)
*   **One-and-a-half syndrome:** Fisher, C.M. (1967). "Some
    neuro-ophthalmological observations." *Journal of Neurology,
    Neurosurgery, and Psychiatry* 30:383–392. (One-and-a-half syndrome
    — PPRF/abducens nucleus + MLF lesion.)
*   **Wernicke's encephalopathy — PPRF involvement:** Victor, M.,
    Adams, R.D., Collins, G.H. (1989). *The Wernicke-Korsakoff
    Syndrome*. (Wernicke's encephalopathy — brainstem involvement
    including the PPRF.)
*   **Parinaud syndrome (contrast — NOT a PPRF syndrome):** Parinaud,
    H. (1883). "Paralysie des mouvements associés des yeux." *Archives
    de Neurologie* 5:145–172. (Parinaud syndrome — dorsal midbrain
    lesion; vertical gaze palsy — NOT a PPRF syndrome.)
*   **INO (contrast — NOT a PPRF syndrome):** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (Internuclear
    ophthalmoplegia — MLF lesion; NOT a PPRF lesion.)
*   **Abducens nerve palsy (contrast — NOT a PPRF syndrome):** Leigh,
    R.J., Zee, D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Abducens nerve palsy — nerve-level lesion; NOT a PPRF lesion.)
*   **Locked-in syndrome (contrast — NOT a PPRF syndrome):** Plum, F.,
    Posner, J.B. (1980). *The Diagnosis of Stupor and Coma*, 3rd ed.
    (Locked-in syndrome — bilateral ventral pontine lesion; NOT a PPRF
    lesion.)
*   **NRTP (contrast — the basilar pons relay to the cerebellum):**
    Thier, P., Möck, M. (2006). "The oculomotor role of the pontine
    nuclei and the nucleus reticularis tegmenti pontis." *Progress in
    Brain Research* 151:293–320. (NRTP — cortico-ponto-cerebellar relay;
    distinct from the PPRF.)
*   **riMLF (contrast — the vertical saccadic burst generator):**
    Büttner-Ennever, J.A., Büttner, U. (1988). "The reticular formation."
    In *Neuroanatomy of the Oculomotor System*. (riMLF — vertical
    saccadic burst generator; distinct from the PPRF.)
*   **cMRF (contrast — the midbrain premotor region):** Waitzman, D.M.,
    Silakov, V.L., Cohen, B. (1996). "Central mesencephalic reticular
    formation (cMRF) neurons discharging before and during eye
    movements." *Journal of Neurophysiology* 75:1546–1572. (cMRF —
    midbrain premotor region; distinct from the PPRF.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the PPRF
    but functionally distinct.)
*   **Parabrachial area (contrast — the visceral-sensory and respiratory
    relay):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Parabrachial area —
    visceral-sensory and respiratory relay; distinct from the PPRF.)
*   **SLEA (contrast — the PPRF is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the PPRF.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the PPRF.)
*   NeuroNames — Paramedian pontine reticular formation; FMA — Paramedian
    pontine reticular formation.
"""
