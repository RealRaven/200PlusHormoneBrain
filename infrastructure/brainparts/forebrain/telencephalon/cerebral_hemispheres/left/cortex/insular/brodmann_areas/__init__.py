"""
Insular Brodmann Areas — Left Hemisphere
=========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── insular
                              └── brodmann_areas   ← THIS PACKAGE

This is a **cytoarchitectonic-collection parent** — a registry package
whose children are the six Brodmann-area packages assigned to the left
insular lobe. It is **not** a gyral or sulcal parent: the insula is a
buried lobe, and its parcellation by Brodmann areas is the primary
structural decomposition the architecture uses.

Parent: ``..insular`` — the left insular lobe. Sibling to
``..primary_gustatory_cortex``, which is a **functional-field** child of
the insular lobe (not a child of this package).

This package is the **structural mirror** of
``../../right/cortex/insular/brodmann_areas``. The six BA children, their
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

The **six children are not equal in importance** on the left:

  * ``brodmann_area_43_anterior_insula`` is the **classical primary
    gustatory area** and the BA most directly tied to the left PGC's
    taste-recognition role.
  * ``brodmann_area_13_middle_insula`` is the **largest and most
    functionally diverse** insular BA — it spans interoception, pain,
    and taste on both sides, and on the left it is the BA most
    strongly associated with the **left PGC's hedonic-valuation
    interface**.
  * ``brodmann_area_14`` is the ventral anterior insula, the **most
    agranular** insular BA, closest in structure to the olfactory
    cortex; on the left it participates in the parasympathetic
    autonomic network.
  * ``brodmann_area_16`` is **inconstant in humans** — present in
    some parcellations and absent in others. Its package must
    therefore carry a ``PRESENCE_PROBABILITY`` field.
  * ``brodmann_area_41_posterior_insula`` and
    ``brodmann_area_42_posterior_insula`` are the **naming-collision
    packages** (see below). They describe the insular-opercular
    transition, not the auditory cortex.

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

The two ``NAMING_COLLISION_WITH`` fields must be **byte-identical to
the left sibling's** — this is a property of the BA numbering scheme,
not of the hemisphere.

--------------------------------------------------------------------------------
BA → INSULAR REGION (structural — identical to the right sibling)
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
redefine it.

--------------------------------------------------------------------------------
BA → FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

Each child package declares a ``FUNCTIONAL_DOMAINS`` tuple. The
**left-hemisphere emphasis** for each BA is:

    BA 13    interoception, nociception_and_pain_affect, gustatory,
             multimodal_integration
             On the left, BA 13 is the BA most strongly tied to the
             **left PGC's hedonic-valuation interface** — the
             projection from the left gustatory field into the
             affective-value network.

    BA 14    gustatory, autonomic_control (parasympathetic),
             social_emotional
             On the left, BA 14 participates in the
             **parasympathetic** autonomic network — the depressor /
             bradycardic side of the left insula's autonomic role.

    BA 16    salience_network, social_emotional
             Inconstant; when present, it contributes to the left
             salience-network emphasis.

    BA 41    nociception_and_pain_affect, thermoreception
             (insular-opercular transition component only; NOT
             audition)

    BA 42    nociception_and_pain_affect, thermoreception
             (insular-opercular transition component only; NOT
             audition)

    BA 43    gustatory (primary), multimodal_intraoral_integration,
             hedonic_valuation_interface
             **The left BA 43 is the BA that most directly overlaps
             with the left PGC.** But the two packages are not
             identical: BA 43 is the architectonic territory, while
             the left PGC is a functional field spanning BA 43 plus
             area G plus the opercula plus (conditionally) the base
             of the central sulcus. Downstream code must query the
             PGC for functional taste processing and BA 43 for
             architectonic territory.

**Left-specific caveat on `speech_articulation`**: the left anterior
insula's role in **apraxia of speech** (Dronkers 1996) is **not
cleanly captured by any single BA number**. The critical structure is
the "precentral gyrus of the insula" — a dysgranular/granular
anterior-insular territory that straddles BA 13, BA 16, and the
opercular transition, and that does not have its own BA number. No
child of this package should claim `speech_articulation` as its
primary functional domain; the domain belongs to the **functional
insular lobe** (``..insular``), not to any BA. This is a case where
the BA decomposition fails, and the architecture must be honest about
it rather than forcing the field into an ill-fitting BA package.

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
                                sulcus
    Downstream code must query the PGC for functional taste
    processing and BA 43 for architectonic territory. The two are
    complementary, not competing.

..cortex.temporal.brodmann_areas
    The **other half of the BA 41/42 naming collision**. Every
    insular BA 41/42 package must carry ``NAMING_COLLISION_WITH``
    pointing at the corresponding temporal package, and the temporal
    parent must carry the reciprocal reference.

..cortex.insular (parent)
    The parent insular package. Its own checklist requires that
    every BA child declare ``FUNCTIONAL_DOMAINS`` as a subset of
    the eleven canonical insular domains. This package's checklist
    adds the left-side emphasis per BA.

../../right/cortex/insular/brodmann_areas
    The right-hemisphere homologue. Structural fields
    (``BA_TO_INSULAR_REGION``, child names, BA numbers,
    ``INSULAR_REGION`` labels, ``NAMING_COLLISION_WITH``) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the left BAs are weighted toward parasympathetic
    autonomic control, taste recognition, and language-linked
    awareness; the right BAs are weighted toward sympathetic
    control, interoceptive awareness, taste intensity, and body
    ownership.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "insular"
    HEMISPHERE          = "left"

    BA_CHILDREN         = (
                              "brodmann_area_13_middle_insula",
                              "brodmann_area_14",
                              "brodmann_area_16",
                              "brodmann_area_41_posterior_insula",
                              "brodmann_area_42_posterior_insula",
                              "brodmann_area_43_anterior_insula",
                          )

    BA_TO_INSULAR_REGION = {   # identical to right; re-exported from
                               # ..insular, not redefined
                              13: "middle_insular",
                              14: "anterior_ventral",
                              16: "anterior_inconstant",
                              41: "insular_opercular_transition",
                              42: "insular_opercular_transition",
                              43: "anterior_opercular",
                          }

    NAMING_COLLISIONS   = {
                              "brodmann_area_41_posterior_insula":
                                  ("temporal.brodmann_areas."
                                   "brodmann_area_41",),
                              "brodmann_area_42_posterior_insula":
                                  ("temporal.brodmann_areas."
                                   "brodmann_area_42",),
                          }

    FUNCTIONAL_DOMAIN_EMPHASIS = {   # left-side emphasis per BA
                              "brodmann_area_13_middle_insula":
                                  ("interoception",
                                   "nociception_and_pain_affect",
                                   "gustatory",
                                   "multimodal_integration"),
                              "brodmann_area_14":
                                  ("gustatory",
                                   "autonomic_control_parasympathetic",
                                   "social_emotional"),
                              "brodmann_area_16":
                                  ("salience_network",
                                   "social_emotional"),
                              "brodmann_area_41_posterior_insula":
                                  ("nociception_and_pain_affect",
                                   "thermoreception"),
                              "brodmann_area_42_posterior_insula":
                                  ("nociception_and_pain_affect",
                                   "thermoreception"),
                              "brodmann_area_43_anterior_insula":
                                  ("gustatory",
                                   "multimodal_intraoral_integration",
                                   "hedonic_valuation_interface"),
                          }

    SPEECH_ARTICULATION_CAVEAT = (
        "speech_articulation is a left-lateralized functional domain "
        "of the insular lobe as a whole, not of any single BA. The "
        "critical structure is the precentral gyrus of the insula, "
        "which straddles BA 13, BA 16, and the opercular transition "
        "and has no dedicated BA number. No child of this package "
        "should claim speech_articulation as its primary functional "
        "domain; the domain belongs to ..insular."
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
   redefine it**. A single source of truth is essential because
   the parent insular package's ``DOMAIN_TO_CHILDREN`` inversion
   depends on the same mapping.

3. Expose the ``NAMING_COLLISIONS`` dict so that downstream code
   that needs to resolve a BA 41/42 reference can see the collision
   in one place.

4. Expose the ``FUNCTIONAL_DOMAIN_EMPHASIS`` dict as a **left-side
   view** of the children's ``FUNCTIONAL_DOMAINS``. This is
   hand-written and is the place where left-side emphasis is
   captured. The right sibling's version will differ.

5. Re-export ``MODERN_PARCELATION_CROSSWALK`` from ``..insular`` —
   do not redefine it. The crosswalk is a property of the insular
   lobe as a whole, not of this registry.

6. Define ``__all__`` as shown in the implementation contract.

7. Contain **no** logic beyond the above.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/cortex/insular/brodmann_areas``:

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
        HEMISPHERE                    "left" vs "right"
        FUNCTIONAL_DOMAIN_EMPHASIS    left: BA 14 emphasizes
                                      parasympathetic autonomic
                                      control; BA 13 emphasizes the
                                      PGC's hedonic-valuation
                                      interface; BA 43 emphasizes
                                      taste recognition.
                                      right: BA 14 emphasizes
                                      sympathetic autonomic
                                      control; BA 13 emphasizes
                                      interoceptive accuracy; BA 43
                                      emphasizes taste intensity.
        SPEECH_ARTICULATION_CAVEAT    this package's caveat explicitly
                                      says the speech-articulation
                                      field is **left-lateralized**
                                      and belongs to ``..insular``,
                                      not to any BA. The right
                                      sibling's caveat says the
                                      speech-articulation field is
                                      **absent** on the right and no
                                      right BA claims it.
        CLINICAL_ANCHORS              left: apraxia of speech
                                      (functional, not BA-specific);
                                      bilateral taste-recognition
                                      deficit; depressor / bradycardic
                                      responses; left-dominant
                                      conditioned taste aversion.
                                      right: ipsilateral taste-
                                      intensity deficit; pressor /
                                      tachycardic responses; body-
                                      ownership and vestibular
                                      deficits; smoking-addiction
                                      disruption.

Any deviation from the "MUST be identical" list is a bug — the BA
packages are structurally symmetric. Any unexpected similarity in the
"MUST differ" list is also a bug — the insula is the most
functionally lateralized lobe, and if the left and right BA registries
end up with the same ``FUNCTIONAL_DOMAIN_EMPHASIS`` or the same
clinical emphasis, the hemisphere split has collapsed.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/insular/brodmann_areas/`` — a
    sibling of ``primary_gustatory_cortex``, not a parent of it.
[ ] All six BA children are imported and registered.
[ ] ``BA_CHILDREN`` lists the six child names in the canonical order
    (13, 14, 16, 41, 42, 43) and is byte-identical to the right
    sibling's.
[ ] ``BA_TO_INSULAR_REGION`` is **re-exported** from ``..insular``,
    not redefined. The single-source-of-truth rule is required so
    that ``..insular``'s ``DOMAIN_TO_CHILDREN`` inversion stays in
    sync.
[ ] ``NAMING_COLLISIONS`` is present and names the temporal BA 41
    and BA 42 packages.
[ ] ``FUNCTIONAL_DOMAIN_EMPHASIS`` is present and captures the
    **left-side emphasis**: parasympathetic autonomic control for
    BA 14, hedonic-valuation interface for BA 13, taste recognition
    for BA 43.
[ ] ``SPEECH_ARTICULATION_CAVEAT`` is present and explicitly states
    that ``speech_articulation`` is a **left-lateralized functional
    domain of the insular lobe as a whole**, not of any single BA.
    **No child of this package claims it.**
[ ] The BA numbering caveat is documented: Brodmann's scheme is
    conventional, modern parcellations (HCP, Öngür-Price, Petrides)
    use different boundaries, and downstream code must route
    through ``MODERN_PARCELATION_CROSSWALK``.
[ ] ``MODERN_PARCELATION_CROSSWALK`` is **re-exported** from
    ``..insular``, not redefined.
[ ] The **BA 43 ↔ PGC relationship** is documented as **overlap,
    not nesting**: BA 43 is the architectonic territory; PGC is the
    functional field. The PGC is a sibling of this package (under
    ``..insular``), not a child.
[ ] The **BA 41/42 naming-collision contract** is documented in
    full, with ``NAMING_COLLISION_WITH`` fields on the two affected
    children and a reciprocal note expected on the temporal side.
[ ] The contract text is byte-identical to the left sibling's — the
    collision is a numbering-scheme property, not a hemisphere
    property.
[ ] The **per-BA left-side functional emphasis** is captured for
    all six BAs (BA 13: interoception/pain/gustatory/multimodal;
    BA 14: gustatory/parasympathetic autonomic/social-emotional;
    BA 16: salience/social-emotional; BA 41: nociception/
    thermoreception; BA 42: nociception/thermoreception;
    BA 43: gustatory/multimodal/hedonic).
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the right sibling; ``FUNCTIONAL_DOMAIN_EMPHASIS``, the
    speech-articulation caveat, and clinical emphasis deliberately
    differ.
[ ] No global BA index is created by this package — the BA 41/42
    collision is a per-lobe concern and must never be silently
    resolved by this package or by ``..insular``.
"""