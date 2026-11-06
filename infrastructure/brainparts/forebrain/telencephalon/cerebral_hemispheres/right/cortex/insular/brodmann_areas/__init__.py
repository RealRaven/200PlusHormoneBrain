"""
Insular Brodmann Areas — Right Hemisphere
==========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── insular
                              └── brodmann_areas   ← THIS PACKAGE

This is a **cytoarchitectonic-collection parent** — a registry package
whose children are the six Brodmann-area packages assigned to the right
insular lobe. It is **not** a gyral or sulcal parent: the insula is a
buried lobe, and its parcellation by Brodmann areas is the primary
structural decomposition the architecture uses.

Parent: ``..insular`` — the right insular lobe. Sibling to
``..primary_gustatory_cortex``, which is a **functional-field** child of
the insular lobe (not a child of this package).

This package is the **structural mirror** of
``../../left/cortex/insular/brodmann_areas``. The six BA children, their
names, their BA numbers, and their ``INSULAR_REGION`` labels are
identical on both sides; the **functional emphasis** and **clinical
significance** of each BA diverge between hemispheres.

Direct children (6)
-------------------
::

    brodmann_areas
    ├── brodmann_area_13_middle_insula    [interoception, pain, taste]
    ├── brodmann_area_14                  [olfactory-gustatory, autonomic]
    ├── brodmann_area_16                  [anterior insula, inconstant]
    ├── brodmann_area_41_posterior_insula [insular-opercular transition]
    ├── brodmann_area_42_posterior_insula [insular-opercular transition]
    └── brodmann_area_43_anterior_insula  [primary gustatory area]

The **six children are not equal in importance** on the right:

  * ``brodmann_area_43_anterior_insula`` is the **classical primary
    gustatory area**, and on the right it is the BA most directly tied
    to the right PGC's **taste-intensity / concentration** role — the
    mirror of the left's taste-recognition role.
  * ``brodmann_area_13_middle_insula`` is the **largest and most
    functionally diverse** insular BA, and on the right it is the BA
    most strongly associated with **interoceptive accuracy** — the
    cortical node whose activity best predicts heartbeat-evoked
    potentials and interoceptive sensitivity (Critchley et al. 2004).
  * ``brodmann_area_14`` is the ventral anterior insula, the **most
    agranular** insular BA, and on the right it participates in the
    **sympathetic** autonomic network — the pressor / tachycardic side
    of the right insula's autonomic role.
  * ``brodmann_area_16`` is **inconstant in humans** — present in
    some parcellations and absent in others. Its package must
    therefore carry a ``PRESENCE_PROBABILITY`` field. When present, it
    contributes to the right salience-network emphasis.
  * ``brodmann_area_41_posterior_insula`` and
    ``brodmann_area_42_posterior_insula`` are the **naming-collision
    packages** (see below). They describe the insular-opercular
    transition, not the auditory cortex. On the right, the
    insular-opercular transition is more strongly engaged during
    **thermoreceptive autonomic challenge** and during
    **body-ownership violations** than on the left.

--------------------------------------------------------------------------------
THE BA NUMBERING CAVEAT — WHY THIS PACKAGE IS "CONVENTIONAL"
--------------------------------------------------------------------------------

Brodmann's original 1–52 scheme **did not include a dedicated insular
series**. BA 13–16 are the areas he assigned to the region, but:

  * Brodmann himself did not publish detailed architectonic boundaries
    for the insula; BA 13–16 were delineated by later anatomists
    working within his numbering.
  * **Modern parcellations** (Öngür & Price 2000; Petrides & Pandya;
    the Human Connectome Project's 180-area scheme) use entirely
    different labels and boundaries — HCP labels the insula with
    areas ``Ig`` (granular), ``Id`` (dysgranular), ``AAIC``
    (anterior agranular insular complex), and so on.
  * The BA numbers used in this package are therefore
    **conventional labels**, not precise architectonic entities.

**Consequence for the architecture**: no downstream code may treat a
BA number as a stand-in for a modern parcel. The parent ``..insular``
package exposes a ``MODERN_PARCELATION_CROSSWALK`` dict, and this
package's children must carry a ``MODERN_CROSSWALK`` field of their
own so that any code that needs an HCP or Öngür-Price parcel goes
through the crosswalk rather than through the BA number.

**This caveat text is byte-identical to the left sibling's** — the
numbering caveat is a property of the Brodmann scheme, not of the
hemisphere.

--------------------------------------------------------------------------------
BA 41 / BA 42 NAMING COLLISION — THIS PACKAGE'S CRITICAL CONTRACT
--------------------------------------------------------------------------------

BA 41 and BA 42 are **classically auditory areas** of the superior
temporal gyrus — the primary and secondary auditory cortex. Their
appearance here as ``posterior_insula`` packages reflects a
**parcellation choice**: the posterior insula and the temporal
operculum are anatomically continuous across the circular sulcus, and
some atlases extend the BA 41/42 label into the insular-opercular
transition zone.

This is the **only cross-package naming collision in the cortex tree**,
and it must be handled explicitly on both sides:

  * The **insular** BA 41/42 packages (children of this package)
    describe the insular-opercular transition. They are NOT the
    auditory cortex.
  * The **temporal** BA 41/42 packages (under
    ``temporal/brodmann_areas/``) describe the classical auditory
    areas of the superior temporal gyrus.
  * Both sets of packages must carry a
    ``NAMING_COLLISION_WITH`` field naming the other set.
  * The parent ``..insular`` and the parent ``..temporal`` must both
    document the collision in their own cross-references.
  * **No global BA index may merge insular BA 41/42 with temporal
    BA 41/42.** The ``BA_TO_INSULAR_REGION`` index exposed by
    ``..insular`` and the temporal equivalent must be kept separate.

**This contract text is byte-identical to the left sibling's** — the
collision is a property of the BA numbering scheme, not of the
hemisphere. The two ``NAMING_COLLISION_WITH`` fields must also be
byte-identical across hemispheres.

--------------------------------------------------------------------------------
BA → INSULAR REGION (structural — identical to the left sibling)
--------------------------------------------------------------------------------

    BA    Region label                       Notes
    ----  ----------------------------------  -----------------------
    13    middle_insular                      Largest insular BA;
                                              granular/dysgranular;
                                              interoception, pain,
                                              taste
    14    anterior_ventral                    Most agranular; ventral
                                              anterior insula;
                                              olfactory-gustatory,
                                              autonomic
    16    anterior_inconstant                 Inconstant in humans;
                                              anterior insula; present
                                              in some parcellations
    41    insular_opercular_transition        Posterior insula /
                                              temporal operculum
                                              junction; naming
                                              collision with temporal
                                              BA 41
    42    insular_opercular_transition        Same as BA 41; naming
                                              collision with temporal
                                              BA 42
    43    anterior_opercular                  Anterior insula /
                                              postcentral operculum;
                                              classical primary
                                              gustatory area

This table is the ``BA_TO_INSULAR_REGION`` index exposed by
``..insular``. It is **hand-written, not derived** — the BA-to-region
mapping is a convention, and the parent insular package is where it
lives. This package re-exports it for convenience but does **not**
redefine it. It is byte-identical to the left sibling's.

--------------------------------------------------------------------------------
BA → FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

Each child package declares a ``FUNCTIONAL_DOMAINS`` tuple. The
**right-hemisphere emphasis** for each BA is:

    BA 13    interoception, nociception_and_pain_affect, gustatory,
             multimodal_integration, vestibular_and_self_location
             On the right, BA 13 is the BA most strongly associated
             with **interoceptive accuracy** — the cortical node
             whose activity best predicts heartbeat-evoked
             potentials and interoceptive sensitivity
             (Critchley et al. 2004). The right BA 13 also
             contributes to body-ownership and vestibular
             self-location, which the left BA 13 does not emphasize
             to the same degree.

    BA 14    gustatory, autonomic_control (sympathetic),
             social_emotional
             On the right, BA 14 participates in the
             **sympathetic** autonomic network — the pressor /
             tachycardic side of the right insula's autonomic role.
             This is the mirror of the left BA 14's parasympathetic
             emphasis.

    BA 16    salience_network, social_emotional
             Inconstant; when present, it contributes to the
             **right salience-network emphasis** — the right
             anterior insula is the more strongly engaged node
             during stimulus-driven reorienting and affective-
             salience detection.

    BA 41    nociception_and_pain_affect, thermoreception,
             autonomic_control (sympathetic)
             (insular-opercular transition component only; NOT
             audition). On the right, the BA 41 transition zone is
             more strongly engaged during **thermoreceptive
             autonomic challenge** (e.g., cold pressor) than on the
             left.

    BA 42    nociception_and_pain_affect, thermoreception,
             autonomic_control (sympathetic)
             (insular-opercular transition component only; NOT
             audition). Same as BA 41.

    BA 43    gustatory (primary), multimodal_intraoral_integration,
             hedonic_valuation_interface
             **The right BA 43 is the BA that most directly overlaps
             with the right PGC** — but on the right, the emphasis is
             on **taste intensity / concentration**, not on taste
             recognition. The right BA 43 is the architectonic
             substrate of the right PGC's concentration-processing
             specialization.

**Right-specific caveat on `speech_articulation`**: the left anterior
insula's role in **apraxia of speech** (Dronkers 1996) is a
**left-lateralized functional domain** and **does not exist on the
right**. Right insular lesions do **not** produce apraxia of speech,
and no right-hemisphere BA carries the domain. The right BA packages
must therefore **omit** `speech_articulation` entirely from their
`FUNCTIONAL_DOMAINS`, and the right parent's
`SPEECH_ARTICULATION_CAVEAT` must state the **absence** of the domain
(not the "belongs to the lobe as a whole" formulation used on the
left). This asymmetry is intentional and is one of the "MUST differ"
entries in the symmetry contract.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..insular
    The parent insular lobe. This package's parent and the source of
    the ``BA_TO_INSULAR_REGION``, ``DOMAIN_TO_CHILDREN``, and
    ``MODERN_PARCELATION_CROSSWALK`` indices. This package **re-exports**
    those indices; it does not redefine them.

..primary_gustatory_cortex
    The **functional-field sibling** of this package, a direct child
    of ``..insular`` rather than a child of ``..brodmann_areas``.
    The relationship is **overlap, not nesting**:
        BA 43 (this package)  = architectonic territory
        PGC (sibling)         = functional gustatory field that
                                spans BA 43 + area G + opercula +
                                (conditionally) base of central
                                sulcus + right-emphasized caudolateral
                                OFC
    On the right, the PGC's dominant role is **taste intensity /
    concentration**, while the left PGC's dominant role is **taste
    recognition**. Downstream code must query the right PGC for
    intensity processing and the left PGC for recognition; the two
    are complementary, not competing.

..cortex.temporal.brodmann_areas
    The **other half of the BA 41/42 naming collision**. Every
    right insular BA 41/42 package must carry
    ``NAMING_COLLISION_WITH`` pointing at the corresponding temporal
    package, and the right temporal parent must carry the
    reciprocal reference.

..cortex.insular (parent)
    The right parent insular package. Its own checklist requires
    that every BA child declare ``FUNCTIONAL_DOMAINS`` as a subset
    of the eleven canonical insular domains, **with the exception
    of `speech_articulation`**, which is left-only and must not
    appear in any right BA. This package's checklist adds the
    right-side emphasis per BA and the speech-articulation omission
    check.

../../subcortical/medial_temporal_lobe/amygdala
    The **right** amygdala → right anterior insula projection is the
    more strongly engaged substrate of **affective-interoceptive
    integration**, and BA 13/BA 14 are the receiving BAs. The
    amygdala package must declare the right anterior insula as a
    cortical target.

../../subcortical/diencephalon/thalamus
    The **right VMpo** → right insula projection is the dominant
    interoceptive-nociceptive substrate, and BA 13 is the receiving
    BA. The thalamus package must declare the right BA 13 as a
    cortical target.

../../left/cortex/insular/brodmann_areas
    The left-hemisphere homologue. Structural fields
    (``BA_TO_INSULAR_REGION``, child names, BA numbers,
    ``INSULAR_REGION`` labels, ``NAMING_COLLISION_WITH``) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the right BAs are weighted toward sympathetic
    autonomic control, interoceptive awareness, taste intensity,
    body ownership, and salience; the left BAs are weighted toward
    parasympathetic control, taste recognition, speech articulation
    (functional, not BA-specific), and language-linked awareness.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "insular"
    HEMISPHERE          = "right"

    BA_CHILDREN         = (
                              "brodmann_area_13_middle_insula",
                              "brodmann_area_14",
                              "brodmann_area_16",
                              "brodmann_area_41_posterior_insula",
                              "brodmann_area_42_posterior_insula",
                              "brodmann_area_43_anterior_insula",
                          )

    BA_TO_INSULAR_REGION = {   # identical to left; re-exported from
                               # ..insular, not redefined
                              13: "middle_insular",
                              14: "anterior_ventral",
                              16: "anterior_inconstant",
                              41: "insular_opercular_transition",
                              42: "insular_opercular_transition",
                              43: "anterior_opercular",
                          }

    NAMING_COLLISIONS   = {   # identical to left
                              "brodmann_area_41_posterior_insula":
                                  ("temporal.brodmann_areas."
                                   "brodmann_area_41",),
                              "brodmann_area_42_posterior_insula":
                                  ("temporal.brodmann_areas."
                                   "brodmann_area_42",),
                          }

    FUNCTIONAL_DOMAIN_EMPHASIS = {   # right-side emphasis per BA
                              "brodmann_area_13_middle_insula":
                                  ("interoception",
                                   "nociception_and_pain_affect",
                                   "gustatory",
                                   "multimodal_integration",
                                   "vestibular_and_self_location"),
                              "brodmann_area_14":
                                  ("gustatory",
                                   "autonomic_control_sympathetic",
                                   "social_emotional"),
                              "brodmann_area_16":
                                  ("salience_network",
                                   "social_emotional"),
                              "brodmann_area_41_posterior_insula":
                                  ("nociception_and_pain_affect",
                                   "thermoreception",
                                   "autonomic_control_sympathetic"),
                              "brodmann_area_42_posterior_insula":
                                  ("nociception_and_pain_affect",
                                   "thermoreception",
                                   "autonomic_control_sympathetic"),
                              "brodmann_area_43_anterior_insula":
                                  ("gustatory",
                                   "multimodal_intraoral_integration",
                                   "hedonic_valuation_interface"),
                          }

    SPEECH_ARTICULATION_CAVEAT = (
        "speech_articulation is a LEFT-LATERALIZED functional domain "
        "of the insular lobe and DOES NOT EXIST on the right. Right "
        "insular lesions do not produce apraxia of speech. No right "
        "BA child should declare speech_articulation in its "
        "FUNCTIONAL_DOMAINS. The domain is omitted entirely from the "
        "right hemisphere."
    )

    __all__ = [
        "LOBE",
        "HEMISPHERE",
        "BA_CHILDREN",
        "BA_TO_INSULAR_REGION",
        "NAMING_COLLISIONS",
        "FUNCTIONAL_DOMAIN_EMPHASIS",
        "SPEECH_ARTICULATION_CAVEAT",
    ]

No behaviour. This package is a declarative registry; all computation
that references the insular BA packages lives in ``cortex/`` or
``memory/``.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``brodmann_areas/__init__.py`` must:

1. Import the six BA children (no side effects):
       from . import brodmann_area_13_middle_insula
       from . import brodmann_area_14
       from . import brodmann_area_16
       from . import brodmann_area_41_posterior_insula
       from . import brodmann_area_42_posterior_insula
       from . import brodmann_area_43_anterior_insula

2. Re-export ``BA_TO_INSULAR_REGION`` from ``..insular`` — **do not
   redefine it**. The right parent insular package is the single
   source of truth for the BA→region mapping.

3. Expose the ``NAMING_COLLISIONS`` dict — byte-identical to the
   left sibling's — so that downstream code that needs to resolve a
   BA 41/42 reference can see the collision in one place.

4. Expose the ``FUNCTIONAL_DOMAIN_EMPHASIS`` dict as a **right-side
   view** of the children's ``FUNCTIONAL_DOMAINS``. This is
   hand-written and is the place where right-side emphasis is
   captured. It differs from the left sibling's by:
       - adding `vestibular_and_self_location` to BA 13
       - replacing `autonomic_control_parasympathetic` with
         `autonomic_control_sympathetic` for BA 14
       - adding `autonomic_control_sympathetic` to BA 41 and BA 42

5. Re-export ``MODERN_PARCELATION_CROSSWALK`` from ``..insular`` —
   do not redefine it.

6. Define ``__all__`` as shown in the implementation contract.

7. Contain **no** logic beyond the above.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/cortex/insular/brodmann_areas``:

    MUST be identical (byte-for-byte):
        LOBE                          "insular"
        BA_CHILDREN                   the same six child names, in
                                      the same order
        BA_TO_INSULAR_REGION          the same six BA→region mappings
        NAMING_COLLISIONS             the same two collision entries
        The BA numbering caveat (Brodmann's scheme is conventional;
                                      modern parcellations differ)
        The BA 41/42 naming-collision contract text
        The MODERN_PARCELATION_CROSSWALK (re-exported from ..insular)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                    "right" vs "left"
        FUNCTIONAL_DOMAIN_EMPHASIS    right: BA 14 emphasizes
                                      sympathetic autonomic control;
                                      BA 13 emphasizes interoceptive
                                      accuracy and adds
                                      vestibular_and_self_location;
                                      BA 43 emphasizes taste
                                      intensity; BA 41/42 add
                                      sympathetic autonomic control.
                                      left: BA 14 emphasizes
                                      parasympathetic autonomic
                                      control; BA 13 emphasizes the
                                      PGC's hedonic-valuation
                                      interface; BA 43 emphasizes
                                      taste recognition.
        SPEECH_ARTICULATION_CAVEAT    right: the field **does not
                                      exist** on the right; right
                                      insular lesions do not produce
                                      apraxia of speech; no right BA
                                      declares the domain.
                                      left: the field belongs to the
                                      insular lobe as a whole, not
                                      to any BA; the critical
                                      structure is the precentral
                                      gyrus of the insula, which
                                      straddles BA 13, BA 16, and
                                      the opercular transition.
        CLINICAL_ANCHORS              right: ipsilateral taste-
                                      intensity deficit; pressor /
                                      tachycardic responses; body-
                                      ownership and vestibular
                                      deficits (asomatognosia,
                                      somatoparaphrenia); smoking-
                                      addiction disruption; right
                                      insula taste-cognition
                                      hypometabolism in Alzheimer's
                                      disease.
                                      left: apraxia of speech
                                      (functional, not BA-specific);
                                      bilateral taste-recognition
                                      deficit; depressor / bradycardic
                                      responses; left-dominant
                                      conditioned taste aversion.

Any deviation from the "MUST be identical" list is a bug — the BA
packages are structurally symmetric. Any unexpected similarity in the
"MUST differ" list is also a bug — the insula is the most
functionally lateralized lobe, and if the left and right BA registries
end up with the same ``FUNCTIONAL_DOMAIN_EMPHASIS`` or the same
speech-articulation caveat, the hemisphere split has collapsed.

**The speech-articulation asymmetry is the sharpest single entry in
this contract.** The left caveat says "the field belongs to the lobe
as a whole"; the right caveat says "the field does not exist on the
right." These are not paraphrases of each other — they are
**different claims**, and both must be present and correct. A
right-hemisphere package that copies the left caveat verbatim is a
bug.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/insular/brodmann_areas/`` (right) —
    a sibling of ``primary_gustatory_cortex``, not a parent of it.
[ ] All six BA children are imported and registered.
[ ] ``BA_CHILDREN`` lists the six child names in the canonical order
    (13, 14, 16, 41, 42, 43) and is byte-identical to the left
    sibling's.
[ ] ``BA_TO_INSULAR_REGION`` is **re-exported** from ``..insular``,
    not redefined, and is byte-identical to the left sibling's.
[ ] ``NAMING_COLLISIONS`` is present and byte-identical to the left
    sibling's.
[ ] ``FUNCTIONAL_DOMAIN_EMPHASIS`` captures the **right-side
    emphasis**:
    - BA 13: interoception, nociception, gustatory,
      multimodal_integration, **vestibular_and_self_location**
    - BA 14: gustatory, **autonomic_control_sympathetic**,
      social_emotional
    - BA 16: salience_network, social_emotional
    - BA 41: nociception, thermoreception,
      **autonomic_control_sympathetic**
    - BA 42: nociception, thermoreception,
      **autonomic_control_sympathetic**
    - BA 43: gustatory, multimodal_intraoral_integration,
      hedonic_valuation_interface
[ ] ``FUNCTIONAL_DOMAIN_EMPHASIS`` does **not** contain
    `speech_articulation` for any BA.
[ ] ``SPEECH_ARTICULATION_CAVEAT`` states that the field **does not
    exist on the right** and that no right BA declares it. It must
    **not** copy the left's "belongs to the lobe as a whole"
    formulation verbatim.
[ ] The BA numbering caveat is documented (byte-identical to the
    left sibling's).
[ ] ``MODERN_PARCELATION_CROSSWALK`` is **re-exported** from
    ``..insular``, not redefined.
[ ] The **BA 43 ↔ PGC relationship** is documented as **overlap,
    not nesting**, with the right-side emphasis on **taste
    intensity / concentration**.
[ ] The **BA 41/42 naming-collision contract** is documented in
    full, byte-identical to the left sibling's, with
    ``NAMING_COLLISION_WITH`` fields on the two affected children.
[ ] The right-side **clinical anchors** are present as a distinct
    list from the left sibling's: ipsilateral taste-intensity
    deficit, pressor / tachycardic responses, asomatognosia /
    somatoparaphrenia, smoking-addiction disruption, right insula
    taste-cognition hypometabolism in AD.
[ ] The right-side **interoceptive accuracy** anchor (Critchley et
    al. 2004) is documented for BA 13.
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the left sibling; ``FUNCTIONAL_DOMAIN_EMPHASIS``, the
    speech-articulation caveat (which must be **substantively
    different**, not just paraphrased), and clinical emphasis
    deliberately differ.
[ ] No global BA index is created by this package — the BA 41/42
    collision is a per-lobe concern and must never be silently
    resolved by this package or by ``..insular``.
"""