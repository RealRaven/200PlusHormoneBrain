"""
Insular Lobe — Left Hemisphere
===============================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
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
This is the **left** hemisphere. The insular lobe is **not symmetrically
organized**. The left insula is the hemisphere of:

* **speech articulation** — the left anterior insula is a core node of
  articulatory planning; lesions produce **apraxia of speech**
  (Dronkers 1996), a disorder of speech *motor programming* distinct
  from Broca's aphasia
* **language-adjacent phonological processing** — the left anterior
  insula participates in the dorsal language pathway with the left
  inferior frontal and superior temporal cortex
* **parasympathetic cardiovascular control** — left insular
  stimulation produces **bradycardia and depressor** responses,
  the mirror-image of the right insula's sympathetic pressor responses
* **bilateral taste recognition** — left insular damage produces an
  **ipsilateral intensity deficit but a bilateral recognition
  deficit**; taste information from both sides of the tongue passes
  through the left insula
* **conditioned taste aversion consolidation** — the left insula is
  the more consequential side for taste-memory encoding

The right insula carries the complementary specializations:
**sympathetic pressor control**, **interoceptive awareness**,
**taste intensity/concentration**, **body ownership and vestibular
self-location**, and a stronger **salience-network** emphasis. See the
right sibling's docstring.

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
        field, and (on the left) speech articulation.

    posterior lobule (smaller)
        Caudal to the central insular sulcus. Composed of **one or
        two long gyri (gyri longi)**. The long gyri are the
        **agranular / dysgranular** posterior insula — the seat of
        primary interoception, thermoreception, and nociception.

A three-tier **cytoarchitectonic gradient** runs across the lobe:

    agranular        (posterior / ventral) — primary interoceptive and
                     nociceptive cortex; dysgranular in part
    dysgranular      (intermediate / middle insula) — transition zone,
                     including the middle short gyrus (eating-reflex
                     seizure zone) and the area G gustatory transition
    granular         (anterior / dorsal) — salience, gustatory,
                     language-adjacent, and social-emotional cortex

The insula is also the site of the **von Economo neurons (VENs)** —
large bipolar projection neurons concentrated in the anterior insula
and anterior cingulate. VENs are implicated in rapid
social-emotional appraisal and are selectively vulnerable in
frontotemporal dementia and in some neuropsychiatric conditions.

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
       HEMISPHERE        = "left"
       CORTICAL_TERRITORIES  (anterior insula, area G, frontal
                              operculum, base of central sulcus,
                              BA 43)
       THALAMIC_RELAY    = "VPMpc"
       FUNCTIONAL_ROLES  (taste_quality_encoding, taste_intensity,
                          taste_recognition, taste_memory,
                          taste_novelty_detection,
                          multimodal_intraoral_integration,
                          ingestive_decision_making,
                          hedonic_valuation_interface,
                          anticipatory_taste_response)
       LATERALIZATION    = "left_dominant_for_taste_recognition"

   **The left PGC's defining asymmetry**: left insular damage produces
   a **bilateral** taste-recognition deficit, while right insular
   damage produces an **ipsilateral** recognition and intensity
   deficit. The left PGC is the dominant hemisphere for taste
   recognition; the right PGC is the dominant hemisphere for taste
   intensity. Downstream code must weight each side separately and
   must **not** average them.

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
        conscious awareness of the body state.

    autonomic_control
        Regulation of sympathetic and parasympathetic outflow. The
        insula is the principal cortical site of **cardiovascular,
        respiratory, and gastrointestinal** control. **The left
        insula is parasympathetic-dominant (depressor, bradycardic);
        the right insula is sympathetic-dominant (pressor,
        tachycardic)** — one of the most robust lateralizations in the
        human cortex.

    gustatory
        Taste processing — see the ``primary_gustatory_cortex`` child.

    nociception_and_pain_affect
        The posterior insula is a primary nociceptive cortex; the
        anterior insula supports the **affective-motivational**
        dimension of pain (the "how bad it feels" component, as
        opposed to the "where and how intense" component of the
        somatosensory cortex).

    thermoreception
        Temperature sensing — posterior insula, with a
        cool/warm topography.

    vestibular_and_self_location
        Vestibular cortex and the sense of **where the body is in
        space**; the right insula is more strongly lateralized for
        body ownership and self-location.

    salience_network
        The **anterior insula** (with the dorsal anterior cingulate)
        is a core node of the salience network — the system that
        detects behaviourally relevant stimuli and switches the brain
        between default-mode and executive networks. The anterior
        insula is sometimes called the "hub of the salience network."

    social_emotional
        Empathy, disgust, fairness, social exclusion, and the
        experience of **emotional awareness** ("how do I feel?").
        The anterior insula is a core node of the emotional-awareness
        network.

    speech_articulation
        **Left-specific.** The left anterior insula (precentral gyrus
        of the insula, anterior short gyri) is a core node of
        articulatory planning. Lesions produce **apraxia of speech** —
        slow, effortful, distorted speech with intact comprehension
        and intact language content. This is the single most
        consequential left-insular clinical syndrome.

    addiction_interoceptive_awareness
        The insula is required for the **interoceptive component of
        addiction**. Insular damage — especially right insular damage
        — can disrupt smoking addiction (Naqvi et al. 2007), and the
        insula's interoceptive re-representation is thought to
        underlie the **urge** component of substance dependence.
        On the left, the insula contributes to the **language-linked
        awareness** of craving.

    multimodal_integration
        The insula integrates taste, smell, somatosensory, visceral,
        and vestibular signals into a **coherent body-state
        representation**. It is a convergence zone, not a
        single-modality cortex.

These tags map onto the memory subsystem as follows:

    interoception                   → memory/stores/short_term (body-state buffer)
    autonomic_control               → memory/stores/long_term/implicit/procedural (homeostatic set-points)
    gustatory                       → memory/stores/short_term (sensory buffer); see PGC child
    nociception_and_pain_affect     → memory/stores/long_term/implicit/emotional_valence
    thermoreception                 → memory/stores/short_term (sensory buffer)
    vestibular_and_self_location    → memory/stores/short_term (spatial buffer)
    salience_network                → memory/stores/short_term (interrupt-driven)
    social_emotional                → memory/stores/long_term/implicit/implicit_social_cognitive
    speech_articulation             → memory/stores/long_term/implicit/procedural
    addiction_interoceptive_awareness → memory/stores/long_term/implicit/reinforcement_value_based_learning
    multimodal_integration          → memory/stores/short_term (multisensory buffer)

Note that **four domains route to `short_term`** — the insula is the
cortex's **momentary body-state workspace**, and any architecture that
models a "current feeling state" must draw on the insular short-term
buffers rather than on long-term stores.

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
    as the non-BA insular areas.

..cortex.frontal
    The frontal operculum is one of the opercula that cover the
    insula. The frontal package must declare the insula as a
    **hidden neighbour** and must note the left anterior insula's
    speech-articulation role in its own ``FUNCTIONAL_ROLES``.

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
    anterior insula as its salience-network partner.

..cortex.occipital
    The posterior insula is not continuous with the occipital lobe;
    recorded here only to pre-empt a false cross-reference.

../../subcortical/medial_temporal_lobe/amygdala
    The basolateral amygdala sends direct projections to the
    anterior insula (including the PGC). The amygdala package must
    declare the insula as a cortical target, with emphasis on the
    **affective valuation** and **interoceptive** interfaces.

../../subcortical/basal_ganglia/striatum/ventral_striatum
    The anterior insula → ventral striatum pathway supports
    salience-driven reward processing and addiction.

../../subcortical/diencephalon/hypothalamus
    The insula → hypothalamus pathway supports autonomic and
    ingestive control.

../../subcortical/diencephalon/thalamus
    The **VPMpc** (gustatory) and **VMpo** (interoceptive /
    nociceptive) thalamic nuclei project to the insula. The thalamus
    package must declare these as insular afferents.

../../brainparts/hindbrain/metencephalon/pons/parabrachial_area
    The parabrachial nucleus is the brainstem gustatory and
    visceral relay that projects to the insula via the thalamus.
    Recorded as a cross-reference for the autonomic and gustatory
    domains.

../../right/cortex/insular
    The right-hemisphere homologue. The **anatomical children**
    (brodmann_areas, primary_gustatory_cortex) exist on both sides
    with the same names and the same structural fields, but the
    **functional lateralization** diverges:
        left  → parasympathetic, speech articulation, bilateral
                taste recognition, language-linked awareness
        right → sympathetic, interoceptive awareness, taste
                intensity, body ownership, salience emphasis
    The right sibling's docstring carries the full right-side
    contract.

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
        "left" (this branch) or "right" (the sibling branch).

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

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/cortex/insular``:

    MUST be identical (byte-for-byte):
        The set of child package names (brodmann_areas with the same
        six BA children; primary_gustatory_cortex).
        Each child's AREA_NAME, LOBE, BRODMANN_NUMBER (for BA
        children), INSULAR_REGION, and NAMING_COLLISION_WITH.
        The BA_TO_INSULAR_REGION index.
        The MODERN_PARCELATION_CROSSWALK.

    MUST differ (and the difference must be documented here):
        HEMISPHERE                "left" vs "right"
        LATERALIZATION            left: parasympathetic dominance,
                                  speech articulation, bilateral
                                  taste recognition;
                                  right: sympathetic dominance,
                                  interoceptive awareness, taste
                                  intensity, body ownership.
        FUNCTIONAL_DOMAINS        both sides carry all eleven domains,
                                  but the **emphasis** differs —
                                  left: speech_articulation,
                                  gustatory (recognition),
                                  language-linked awareness;
                                  right: interoception,
                                  vestibular_and_self_location,
                                  salience_network emphasis.
        CLINICAL_ANCHORS          left: apraxia of speech from left
                                  anterior insula lesions; bilateral
                                  taste-recognition deficit from left
                                  insular stroke; depressor /
                                  bradycardic responses to left
                                  insular stimulation;
                                  right: pressor / tachycardic
                                  responses; ipsilateral taste
                                  intensity deficit; body-ownership
                                  and vestibular deficits; smoking-
                                  addiction disruption from right
                                  insular damage.

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
    children and a corresponding note on the temporal side.
[ ] The **eleven functional domains** are listed with their memory-
    subsystem routings, and the four short-term routings are flagged
    as the insula's body-state workspace.
[ ] The **left lateralization profile** is documented:
    parasympathetic, speech articulation, bilateral taste
    recognition, language-linked awareness.
[ ] The **speech-articulation role** of the left anterior insula is
    flagged as the single most consequential left-insular clinical
    syndrome (apraxia of speech).
[ ] The **bilateral taste-recognition deficit** from left insular
    damage is documented, and the downstream rule that the left
    PGC is weighted for recognition and the right PGC for intensity
    is repeated here at the parent level.
[ ] The **parasympathetic / sympathetic asymmetry** is documented
    (left depressor, right pressor) as the most robust autonomic
    lateralization in the human cortex.
[ ] The **salience-network partnership** with the dorsal anterior
    cingulate is cross-referenced to ``cortex/cingulate``.
[ ] The **opercula** (frontal, parietal, temporal) are cross-
    referenced, and the opercular packages are required to declare
    the insula as a hidden neighbour.
[ ] The **von Economo neurons** are mentioned as an insular
    cytoarchitectonic feature with clinical relevance.
[ ] Every child package's docstring follows the same template used
    in the already-written ``primary_gustatory_cortex`` package.
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the right sibling; LATERALIZATION, functional emphasis, and
    clinical anchors deliberately differ.
"""