"""
Insular Lobe — Right Hemisphere
================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular          ← THIS PACKAGE

The **insular lobe** (insula, insular cortex, island of Reil) is the
cortical territory **buried within the lateral (Sylvian) fissure**,
hidden beneath the **frontal, parietal, and temporal opercula**. It is
the only major cortical lobe that is **not visible on the lateral
surface** of the intact brain. In this architecture the insular package
is a direct child of ``cortex/``, alongside ``frontal``, ``parietal``,
``temporal``, ``occipital``, and ``cingulate``.

The insular lobe occupies roughly **2 % of the total cortical surface**
but is disproportionately connected — it is a **hub** whose lesion
produces deficits spanning taste, interoception, autonomic control,
pain, vestibular function, speech articulation, emotion, and addiction.
It is the cortical substrate of the **salience network** (with the
dorsal anterior cingulate) and the principal cortical site of
**interoceptive awareness**.

Direct children (2)
-------------------
::

    insular
    ├── brodmann_areas          [cytoarchitectonic parcellation]
    └── primary_gustatory_cortex [functional gustatory field]

**This is a mixed-children parent.** ``brodmann_areas`` is a
**structural/cytoarchitectonic** child; ``primary_gustatory_cortex`` is
a **functional-field** child. The two are complementary, not competing:
the BA packages describe *what the cortex is built of*; the functional
field describes *what a region does*. A single functional field may
span several BA packages (the PGC spans BA 43 plus non-BA-numbered
insular areas), and a single BA package may contribute to several
functional fields (BA 13 contributes to interoception, pain, and taste).

Lateralization note
-------------------
This is the **right** hemisphere. The insular lobe is **not
symmetrically organized**. The right insula is the hemisphere of:

* **interoceptive awareness** — the conscious sense of the body's
  internal state. The right anterior insula is the cortical node whose
  activity best predicts **heartbeat-evoked potentials** and
  **interoceptive accuracy** (Critchley et al. 2004); right insular
  lesions impair heartbeat detection more than left insular lesions
* **sympathetic cardiovascular control** — right insular stimulation
  produces **pressor and tachycardic** responses, the mirror-image of
  the left insula's depressor and bradycardic responses. This is one
  of the most robust autonomic lateralizations in the human cortex
* **taste intensity / concentration** — taste concentration processing
  dominates in the right insular cortex; the right insula is more
  sensitive to intensity variations across concentrations
* **body ownership and vestibular self-location** — the right insula
  (with the right temporoparietal junction) is the more strongly
  lateralized substrate for the sense of **where the body is** and
  **which body parts belong to the self**
* **salience-network emphasis** — the right anterior insula is the
  more strongly engaged node of the salience network during
  **stimulus-driven reorienting** and **affective salience detection**
* **addiction-related interoceptive urge** — right insular damage can
  disrupt smoking addiction (Naqvi et al. 2007); the right insula's
  interoceptive re-representation is thought to underlie the **urge**
  component of substance dependence

The left insula carries the complementary specializations:
**speech articulation**, **parasympathetic control**, **bilateral
taste recognition**, and **language-linked emotional awareness**. See
the left sibling's docstring.

--------------------------------------------------------------------------------
WHAT THE INSULAR LOBE IS
--------------------------------------------------------------------------------

The insular lobe is bounded externally by the **circular sulcus**
(limiting sulcus, sulcus circularis), the ring of cortex that separates
it from the opercula. It is divided internally by the **central
insular sulcus** into two lobules:

    anterior lobule (larger)
        Rostral to the central insular sulcus. Composed of **three or
        four short gyri (gyri breves)** radiating from the
        **limen insulae** — the threshold of the insula, where
        insular cortex meets orbitofrontal and temporal cortex.
        The short gyri are the **granular / dysgranular** anterior
        insula — the seat of the salience network, the gustatory
        field, and (on the right) the strongest interoceptive
        awareness and sympathetic autonomic nodes.

    posterior lobule (smaller)
        Caudal to the central insular sulcus. Composed of **one or
        two long gyri (gyri longi)**. The long gyri are the
        **agranular / dysgranular** posterior insula — the seat of
        primary interoception, thermoreception, and nociception.
        On the right, the posterior insula's **taste intensity**
        cluster extends into the middle–posterior insula, one of the
        two clusters specialized for concentration processing.

A three-tier **cytoarchitectonic gradient** runs across the lobe:

    agranular        (posterior / ventral) — primary interoceptive and
                     nociceptive cortex; dysgranular in part
    dysgranular      (intermediate / middle insula) — transition zone,
                     including the middle short gyrus (eating-reflex
                     seizure zone) and the area G gustatory transition
    granular         (anterior / dorsal) — salience, gustatory,
                     social-emotional, and (on the left) language-
                     adjacent cortex

The insula is also the site of the **von Economo neurons (VENs)** —
large bipolar projection neurons concentrated in the anterior insula
and anterior cingulate. VENs are implicated in rapid
social-emotional appraisal and are selectively vulnerable in
frontotemporal dementia and in some neuropsychiatric conditions. **On
the right, VEN density and VEN-related functional connectivity are more
strongly associated with interoceptive and affective salience than on
the left**.

--------------------------------------------------------------------------------
DIRECT CHILDREN — SPEC
--------------------------------------------------------------------------------

1. brodmann_areas
   ~~~~~~~~~~~~~~~~
   The cytoarchitectonic parcellation of the insular lobe, as a
   collection of BA packages. The children present in this tree are:

       brodmann_area_13_middle_insula    BA 13 — middle insula,
                                         granular/dysgranular;
                                         interoception, pain, taste
       brodmann_area_14                  BA 14 — ventral anterior
                                         insula, agranular;
                                         olfactory-gustatory, autonomic
       brodmann_area_16                  BA 16 — inconstant in humans;
                                         present in some
                                         parcellations; anterior
                                         insula
       brodmann_area_41_posterior_insula BA 41 — insular-opercular
                                         transition, *named* posterior
                                         insula here
       brodmann_area_42_posterior_insula BA 42 — insular-opercular
                                         transition, *named* posterior
                                         insula here
       brodmann_area_43_anterior_insula  BA 43 — anterior insula /
                                         postcentral operculum;
                                         classical primary gustatory
                                         area

   **A caution about the BA 41/42 naming in this tree.** BA 41 and
   BA 42 are classically **auditory** areas of the superior temporal
   gyrus (the primary and secondary auditory cortex). Their appearance
   here as ``posterior_insula`` packages reflects a **parcellation
   choice**: the posterior insula and the temporal operculum are
   anatomically continuous across the circular sulcus, and some
   atlases extend BA 41/42 labelling into the insular-opercular
   transition zone. The **temporal** lobe's own BA 41/42 packages
   (under ``temporal/brodmann_areas/``) and these insular packages
   must therefore be **explicitly reconciled** — they are not the same
   cortical territory, and the naming collision must be documented in
   both. The insular packages should carry a
   ``NAMING_COLLISION_WITH = "temporal.brodmann_areas.brodmann_area_41/42"``
   field and describe only the insular-opercular *component*.

   **A caution about the insular BA packages generally.** Brodmann's
   original 1–52 scheme did not include a dedicated insular series;
   BA 13–16 are the areas he assigned to the region, but modern
   parcellations (Öngür/Price, Petrides, HCP 180-area) use entirely
   different labels and boundaries. The BA packages must therefore be
   treated as **conventional labels**, not as precise architectonic
   entities. The parent insular package should expose both a
   ``BA_TO_INSULAR_REGION`` index and a
   ``MODERN_PARCELATION_CROSSWALK`` dict.

2. primary_gustatory_cortex
   ~~~~~~~~~~~~~~~~~~~~~~~~
   The **functional gustatory field** — the cortical recipient of
   VPMpc thalamic taste projections. It is **not** a sulcus-bounded
   territory: it spans the anterior insula (granular), the parietal
   operculum (area G), the frontal operculum, and possibly the base of
   the central sulcus. It is a **direct child of this package** rather
   than a child of ``brodmann_areas`` precisely because it is a
   functional field, not an architectonic unit.

   The PGC package declares:

       AREA_NAME         = "primary_gustatory_cortex"
       HEMISPHERE        = "right"
       CORTICAL_TERRITORIES  (anterior insula, area G, frontal
                              operculum, base of central sulcus,
                              BA 43, caudolateral OFC
                              right-emphasized)
       THALAMIC_RELAY    = "VPMpc"
       FUNCTIONAL_ROLES  (taste_intensity_encoding [primary],
                          taste_quality_encoding,
                          taste_recognition_ipsilateral,
                          taste_memory, taste_novelty_detection,
                          multimodal_intraoral_integration,
                          ingestive_decision_making,
                          hedonic_valuation_interface,
                          anticipatory_taste_response)
       LATERALIZATION    = "right_dominant_for_taste_intensity_concentration"

   **The right PGC's defining asymmetry**: right insular damage
   produces an **ipsilateral** recognition and intensity deficit,
   while left insular damage produces an **ipsilateral intensity but
   bilateral recognition** deficit. The right PGC is the dominant
   hemisphere for taste intensity / concentration; the left PGC is
   the dominant hemisphere for taste recognition. Downstream code
   must weight each side separately and must **not** average them.

   See ``primary_gustatory_cortex/__init__.py`` for the full contract.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (this architecture's tags)
--------------------------------------------------------------------------------

The insular lobe is the substrate of the following functional domains.
Each domain is tagged here so that downstream code can query "what does
the insula do?" without reading every child package:

    interoception
        Sensing the internal state of the body — heartbeat, respiration,
        gastric motility, bladder fullness, visceral pain. The
        **posterior insula** is the primary interoceptive cortex; the
        **anterior insula** is the re-representation that supports
        conscious awareness of the body state. **On the right,
        interoceptive accuracy is more strongly correlated with
        anterior insula activity than on the left** (Critchley et al.
        2004), and right insular lesions impair heartbeat detection
        more than left insular lesions.

    autonomic_control
        Regulation of sympathetic and parasympathetic outflow. The
        insula is the principal cortical site of **cardiovascular,
        respiratory, and gastrointestinal** control. **The right
        insula is sympathetic-dominant (pressor, tachycardic); the
        left insula is parasympathetic-dominant (depressor,
        bradycardic)** — one of the most robust lateralizations in the
        human cortex.

    gustatory
        Taste processing — see the ``primary_gustatory_cortex`` child.
        **On the right, taste intensity / concentration is the
        dominant gustatory function**; on the left, taste
        recognition is.

    nociception_and_pain_affect
        The posterior insula is a primary nociceptive cortex; the
        anterior insula supports the **affective-motivational**
        dimension of pain (the "how bad it feels" component, as
        opposed to the "where and how intense" component of the
        somatosensory cortex). **On the right, the anterior insula
        is the more strongly engaged node during pain anticipation
        and pain-related autonomic responses.**

    thermoreception
        Temperature sensing — posterior insula, with a
        cool/warm topography. The right insula is more strongly
        activated during **thermoreceptive autonomic challenge**
        (e.g. cold pressor).

    vestibular_and_self_location
        Vestibular cortex and the sense of **where the body is in
        space**; **the right insula is the dominant hemisphere for
        body ownership and self-location**, and right insular lesions
        produce **asomatognosia** and **somatoparaphrenia** (denial of
        ownership of the contralateral limb) more frequently than
        left insular lesions.

    salience_network
        The **anterior insula** (with the dorsal anterior cingulate)
        is a core node of the salience network — the system that
        detects behaviourally relevant stimuli and switches the brain
        between default-mode and executive networks. **The right
        anterior insula is the more strongly engaged node during
        stimulus-driven reorienting and affective-salience
        detection.** The anterior insula is sometimes called the
        "hub of the salience network."

    social_emotional
        Empathy, disgust, fairness, social exclusion, and the
        experience of **emotional awareness** ("how do I feel?").
        The anterior insula is a core node of the emotional-awareness
        network. **On the right, the insula is more strongly
        associated with interoceptive-affective integration (the
        "felt" component of emotion); on the left, with
        language-linked emotional awareness (naming and narrating
        the emotion).**

    speech_articulation
        **Left-specific.** The left anterior insula (precentral gyrus
        of the insula, anterior short gyri) is a core node of
        articulatory planning. Lesions produce **apraxia of speech** —
        slow, effortful, distorted speech with intact comprehension
        and intact language content. **The right insula does not
        carry this function**; right insular lesions do not produce
        apraxia of speech.

    addiction_interoceptive_awareness
        The insula is required for the **interoceptive component of
        addiction**. **Right insular damage — especially to the
        anterior insula — can disrupt smoking addiction
        (Naqvi et al. 2007)**, and the insula's interoceptive
        re-representation is thought to underlie the **urge**
        component of substance dependence. On the right, the
        interoceptive-urge link is the dominant contribution; on the
        left, the language-linked awareness of craving is
        relatively stronger.

    multimodal_integration
        The insula integrates taste, smell, somatosensory, visceral,
        and vestibular signals into a **coherent body-state
        representation**. It is a convergence zone, not a
        single-modality cortex. **On the right, the body-state
        representation is weighted toward interoceptive and
        vestibular self-location signals; on the left, toward
        gustatory and language-linked signals.**

These tags map onto the memory subsystem as follows:

    interoception                   → memory/stores/short_term (body-state buffer)
    autonomic_control               → memory/stores/long_term/implicit/procedural (homeostatic set-points)
    gustatory                       → memory/stores/short_term (sensory buffer); see PGC child
    nociception_and_pain_affect     → memory/stores/long_term/implicit/emotional_valence
    thermoreception                 → memory/stores/short_term (sensory buffer)
    vestibular_and_self_location    → memory/stores/short_term (spatial buffer)
    salience_network                → memory/stores/short_term (interrupt-driven)
    social_emotional                → memory/stores/long_term/implicit/implicit_social_cognitive
    speech_articulation             → memory/stores/long_term/implicit/procedural  # LEFT ONLY
    addiction_interoceptive_awareness → memory/stores/long_term/implicit/reinforcement_value_based_learning
    multimodal_integration          → memory/stores/short_term (multisensory buffer)

**Right-side note on `speech_articulation`:** this domain is
**left-lateralized** and does not route to any right-hemisphere
memory store. The right insular parent must still *declare* the
domain in its `FUNCTIONAL_DOMAINS` tuple (for hemisphere-invariant
schema compliance), but must mark it `LATERALIZATION =
"left_only"` so downstream code does not attempt to instantiate it
on the right.

Note that **four domains route to `short_term`** — the insula is the
cortex's **momentary body-state workspace**, and any architecture that
models a "current feeling state" must draw on the insular short-term
buffers rather than on long-term stores. On the right, the
**body-state buffer is weighted toward interoceptive and vestibular
signals**, and the **salience-network buffer is weighted toward
stimulus-driven reorienting**.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (within this package)
    The cytoarchitectonic child. Every BA package under
    ``insular/brodmann_areas/`` must declare the insular lobe as its
    parent and must list the functional domains in which it
    participates. The BA 41/42 packages must carry the
    ``NAMING_COLLISION_WITH`` field and reconcile with
    ``temporal/brodmann_areas/``.

..primary_gustatory_cortex  (within this package)
    The functional-field child. Its ``CORTICAL_TERRITORIES`` field
    must reference the BA packages under ``..brodmann_areas`` as well
    as the non-BA insular areas, and must include the
    **right-emphasized caudolateral OFC** entry.

..cortex.frontal
    The frontal operculum is one of the opercula that cover the
    insula. The frontal package must declare the insula as a
    **hidden neighbour** and must note the right anterior insula's
    interoceptive-affective integration role in its own
    ``FUNCTIONAL_ROLES``.

..cortex.parietal
    The parietal operculum (including area G) is one of the
    opercula. The parietal package must declare the insula as a
    hidden neighbour and must note the area G gustatory transition.

..cortex.temporal
    The temporal operculum (including the classical auditory BA 41
    and 42) is one of the opercula. **The temporal package is the
    other half of the BA 41/42 naming collision** — both packages
    must document the reconciliation.

..cortex.cingulate
    The dorsal anterior cingulate is the other core node of the
    **salience network**. The cingulate package must declare the
    anterior insula as its salience-network partner, and must note
    that the **right anterior insula** is the more strongly engaged
    node during stimulus-driven reorienting.

..cortex.occipital
    The posterior insula is not continuous with the occipital lobe;
    recorded here only to pre-empt a false cross-reference.

../../subcortical/medial_temporal_lobe/amygdala
    The basolateral amygdala sends direct projections to the
    anterior insula (including the PGC). The amygdala package must
    declare the insula as a cortical target, with emphasis on the
    **affective valuation** and **interoceptive** interfaces.
    **On the right, the amygdala → insula projection is the more
    strongly engaged substrate of affective-interoceptive
    integration.**

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The anterior insula → ventral striatum pathway supports
    salience-driven reward processing and addiction. **On the right,
    this pathway is the dominant interoceptive-urge substrate.**

../../subcortical/diencephalon/hypothalamus
    The insula → hypothalamus pathway supports autonomic and
    ingestive control. **On the right, the insula → hypothalamus
    pathway is weighted toward sympathetic outflow** (pressor and
    tachycardic responses).

../../subcortical/diencephalon/thalamus
    The **VPMpc** (gustatory) and **VMpo** (interoceptive /
    nociceptive) thalamic nuclei project to the insula. The thalamus
    package must declare these as insular afferents. **On the right,
    the VMpo → insula projection is the dominant interoceptive-
    nociceptive substrate.**

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem gustatory and
    visceral relay that projects to the insula via the thalamus.
    Recorded as a cross-reference for the autonomic and gustatory
    domains.

../../left/cortex/insular
    The left-hemisphere homologue. The **anatomical children**
    (brodmann_areas, primary_gustatory_cortex) exist on both sides
    with the same names and the same structural fields, but the
    **functional lateralization** diverges:
        right → sympathetic, interoceptive awareness, taste
                intensity, body ownership, salience emphasis
        left  → parasympathetic, speech articulation, bilateral
                taste recognition, language-linked awareness
    The left sibling's docstring carries the full left-side contract.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child of ``insular/`` MUST expose the following module-level
names so the rest of the system can query the lobe uniformly. The
fields differ by child type (architectonic vs functional field), so the
contract is specified for each.

Architectonic child (``brodmann_areas/*``):

    AREA_NAME : str
        Canonical snake_case name, identical to the folder name.
        Example: "brodmann_area_13_middle_insula"

    HEMISPHERE : str
        "right" (this branch) or "left" (the sibling branch).

    LOBE : str
        "insular"

    BRODMANN_NUMBER : int
        The BA number (13, 14, 16, 41, 42, 43).

    INSULAR_REGION : str
        One of "anterior_granular", "middle_dysgranular",
        "posterior_agranular", "insular_opercular_transition".

    NAMING_COLLISION_WITH : tuple[str, ...]
        For BA 41 and BA 42 only: the sibling temporal-lobe package
        whose BA number is the same but whose territory is different.
        Empty tuple for all other BA children.

    FUNCTIONAL_DOMAINS : tuple[str, ...]
        Subset of the eleven functional-domain tags listed above.
        **Must mark `speech_articulation` as `LATERALIZATION =
        "left_only"` if present** — this domain does not route to
        any right-hemisphere store.

    CONNECTIVITY : dict[str, tuple[str, ...]]
        Thalamic afferents and cortical/subcortical targets.

    __all__ : list[str]
        Every public name above.

Functional-field child (``primary_gustatory_cortex/*``):

    AREA_NAME, HEMISPHERE, LOBE, CORTICAL_TERRITORIES,
    BRODMANN_AREAS, THALAMIC_RELAY, FUNCTIONAL_ROLES, CONNECTIVITY,
    LATERALIZATION, SUBDIVISIONS, __all__
        As specified in ``primary_gustatory_cortex/__init__.py``.

The child's ``__init__.py`` should additionally contain a docstring
following the same template used in the child package already written:
hierarchical location → what the field is → territories → BA
adjacency → extent → variants → clinical significance →
cross-references → implementation contract → checklist.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``insular/__init__.py`` is a namespace + registry. It must:

1. Import the two children (no side effects):
       from . import brodmann_areas
       from . import primary_gustatory_cortex

2. Expose a registry of architectonic children:

       INSULAR_BA_PACKAGES = {
           "brodmann_area_13_middle_insula":  brodmann_areas.brodmann_area_13_middle_insula,
           "brodmann_area_14":                brodmann_areas.brodmann_area_14,
           "brodmann_area_16":                brodmann_areas.brodmann_area_16,
           "brodmann_area_41_posterior_insula": brodmann_areas.brodmann_area_41_posterior_insula,
           "brodmann_area_42_posterior_insula": brodmann_areas.brodmann_area_42_posterior_insula,
           "brodmann_area_43_anterior_insula":  brodmann_areas.brodmann_area_43_anterior_insula,
       }

3. Expose a registry of functional-field children:

       INSULAR_FUNCTIONAL_FIELDS = {
           "primary_gustatory_cortex": primary_gustatory_cortex,
       }

4. Expose a **BA → insular region** index (hand-written, because the
   BA-to-region mapping is a convention, not a derivation):

       BA_TO_INSULAR_REGION = {
           13: "middle_insular",
           14: "anterior_ventral",
           16: "anterior_inconstant",
           41: "insular_opercular_transition",
           42: "insular_opercular_transition",
           43: "anterior_opercular",
       }

5. Expose a **functional domain → child packages** index, derived
   from the children's ``FUNCTIONAL_DOMAINS`` / ``FUNCTIONAL_ROLES``
   fields (do not hand-write this; it must stay in sync with the
   children):

       DOMAIN_TO_CHILDREN = {
           # computed at import time by inverting FUNCTIONAL_DOMAINS /
           # FUNCTIONAL_ROLES on each child
           "interoception":               (...),
           "autonomic_control":           (...),
           "gustatory":                   ("primary_gustatory_cortex", ...),
           "nociception_and_pain_affect": (...),
           ...
       }

   The inversion must fail loudly if a child declares a domain that
   is not in the canonical domain list above.

6. Expose the **modern-parcellation crosswalk**:

       MODERN_PARCELATION_CROSSWALK = {
           # BA label → modern label(s) in HCP / Öngür-Price /
           # Petrides schemes
       }

   This is required because the BA numbering is a historical
   convention, not a modern architectonic map. The crosswalk makes
   explicit that BA 13 ≠ HCP area "Ig" ≠ Öngür-Price "Iai", and so
   on. Downstream code that needs a modern parcel must go through
   this crosswalk, not through BA numbers.

7. Define ``__all__ = ["brodmann_areas", "primary_gustatory_cortex",
                      "INSULAR_BA_PACKAGES", "INSULAR_FUNCTIONAL_FIELDS",
                      "BA_TO_INSULAR_REGION", "DOMAIN_TO_CHILDREN",
                      "MODERN_PARCELATION_CROSSWALK"]``

8. Contain **no** logic beyond the above. Any behaviour belongs in
   the child packages or in ``cortex/``.

--------------------------------------------------------------------------------
BA 41 / BA 42 NAMING-COLLISION CONTRACT
--------------------------------------------------------------------------------

This is the only cross-package naming collision in the cortex tree, and
it must be handled explicitly on both sides:

  * The **insular** BA 41 and BA 42 packages describe the
    **insular-opercular transition** — the cortex at the junction of
    the posterior insula and the temporal operculum. They are NOT
    the auditory cortex.
  * The **temporal** BA 41 and BA 42 packages (under
    ``temporal/brodmann_areas/``) describe the **classical auditory**
    areas of the superior temporal gyrus. They are the primary and
    secondary auditory cortex.
  * Both sets of packages must carry the
    ``NAMING_COLLISION_WITH`` field naming the other set.
  * Both parents must document the collision in their own
    cross-references.
  * No downstream code may resolve "BA 41" or "BA 42" to a single
    package without specifying the lobe. The ``BA_TO_INSULAR_REGION``
    and the temporal equivalent must therefore never be merged into
    a single global BA index.

**This contract is byte-identical to the left sibling's.** The naming
collision is a property of the BA numbering scheme, not of the
hemisphere — the reconciliation must be identical on both sides, or the
symmetry test fails.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/cortex/insular``:

    MUST be identical (byte-for-byte):
        The set of child package names (brodmann_areas with the same
        six BA children; primary_gustatory_cortex).
        Each child's AREA_NAME, LOBE, BRODMANN_NUMBER (for BA
        children), INSULAR_REGION, and NAMING_COLLISION_WITH.
        The BA_TO_INSULAR_REGION index.
        The MODERN_PARCELATION_CROSSWALK.

    MUST differ (and the difference must be documented here):
        HEMISPHERE                "right" vs "left"
        LATERALIZATION            right: sympathetic dominance,
                                  interoceptive awareness, taste
                                  intensity, body ownership, salience
                                  emphasis; left: parasympathetic
                                  dominance, speech articulation,
                                  bilateral taste recognition,
                                  language-linked awareness.
        FUNCTIONAL_DOMAINS        both sides carry all eleven domains,
                                  but the **emphasis** differs —
                                  right: interoception,
                                  vestibular_and_self_location,
                                  salience_network,
                                  autonomic_control (sympathetic)
                                  emphasis; left: speech_articulation,
                                  gustatory (recognition),
                                  language-linked awareness,
                                  autonomic_control (parasympathetic).
        CLINICAL_ANCHORS          right: pressor / tachycardic
                                  responses to right insular
                                  stimulation; ipsilateral taste
                                  intensity deficit; body-ownership
                                  and vestibular deficits
                                  (asomatognosia,
                                  somatoparaphrenia); smoking-
                                  addiction disruption from right
                                  insular damage; right insula
                                  taste-cognition hypometabolism in
                                  Alzheimer's disease;
                                  right-lateralized caudolateral
                                  OFC secondary taste area;
                                  left: apraxia of speech from left
                                  anterior insula lesions; bilateral
                                  taste-recognition deficit from
                                  left insular stroke; depressor /
                                  bradycardic responses to left
                                  insular stimulation; left-
                                  dominant conditioned taste
                                  aversion memory.

Any deviation from the "MUST be identical" list is a bug — the
insular lobe has the same anatomical children on both sides, and the
BA numbering is symmetric. Any unexpected similarity in the "MUST
differ" list is also a bug — the insula is the **most functionally
lateralized** lobe in the human cortex, and if left and right insula
end up with the same LATERALIZATION or the same clinical anchors, the
hemisphere split has collapsed.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/insular/``, directly under
    ``cortex/`` — not under ``gyri`` or ``sulci``.
[ ] The two children (``brodmann_areas``,
    ``primary_gustatory_cortex``) are imported and registered.
[ ] ``INSULAR_BA_PACKAGES`` has exactly the six BA children present
    in the tree: 13, 14, 16, 41, 42, 43.
[ ] ``INSULAR_FUNCTIONAL_FIELDS`` has exactly the one functional-field
    child: ``primary_gustatory_cortex``.
[ ] ``BA_TO_INSULAR_REGION`` maps every BA child to a region label.
[ ] ``DOMAIN_TO_CHILDREN`` is **derived**, not hand-written, and
    fails loudly on unknown domains.
[ ] ``MODERN_PARCELATION_CROSSWALK`` is present — the BA numbering
    is a historical convention, not a modern architectonic map.
[ ] The **BA 41 / BA 42 naming collision** is documented in
    full, with ``NAMING_COLLISION_WITH`` fields on the affected
    children and a corresponding note on the temporal side. The
    contract text must be byte-identical to the left sibling's.
[ ] The **eleven functional domains** are listed with their memory-
    subsystem routings, and the four short-term routings are flagged
    as the insula's body-state workspace.
[ ] `speech_articulation` is declared in `FUNCTIONAL_DOMAINS` but
    marked `LATERALIZATION = "left_only"` — the right insular parent
    does not route it to any right-hemisphere store.
[ ] The **right lateralization profile** is documented:
    sympathetic, interoceptive awareness, taste intensity, body
    ownership, salience emphasis, addiction interoceptive urge.
[ ] The **right insular pressor / tachycardic response** to
    stimulation is documented as the mirror of the left's depressor
    / bradycardic response.
[ ] The **ipsilateral taste intensity deficit** from right insular
    damage is documented, and the downstream rule that the right
    PGC is weighted for intensity and the left PGC for recognition
    is repeated here at the parent level.
[ ] The **interoceptive accuracy correlation** (Critchley et al.
    2004) is documented as a right-lateralized anchor.
[ ] The **addiction-related interoceptive urge** (Naqvi et al.
    2007) is documented as a right-lateralized anchor.
[ ] The **body ownership / vestibular self-location** role is
    documented as a right-lateralized anchor, with asomatognosia
    and somatoparaphrenia as the lesion signature.
[ ] The **salience-network partnership** with the dorsal anterior
    cingulate is cross-referenced to ``cortex/cingulate``, with
    emphasis on the right anterior insula's stimulus-driven
    reorienting role.
[ ] The **opercula** (frontal, parietal, temporal) are cross-
    referenced, and the opercular packages are required to declare
    the insula as a hidden neighbour.
[ ] The **von Economo neurons** are mentioned, with the right-side
    interoceptive-affective emphasis.
[ ] The **caudolateral OFC right-lateralized secondary taste area**
    is cross-referenced from the insular parent (not only from the
    PGC child).
[ ] Every child package's docstring follows the same template used
    in the already-written ``primary_gustatory_cortex`` package.
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the left sibling; LATERALIZATION, functional emphasis, and
    clinical anchors deliberately differ.
[ ] No global BA index merges the insular BA 41/42 with the
    temporal BA 41/42 — the collision is a per-lobe concern and must
    never be silently resolved.
"""