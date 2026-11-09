"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brocas_area.brodmann_area_44
=================================================================================================================================

Brodmann area 44 (pars opercularis) — left hemisphere.

A CONSTANT + CONFIG HOLDER inside the brocas_area nested registry
sub-package. No compute, no state, no lifecycle. Declares the canonical
identity of area 44, says which compute sub-region owns it, and supplies
the per-area weights that the owning sub-region's `encode()` reads. It
defines no classes and no functions; the public surface is the exports
listed under "EXPORTS".

If you are looking for the computation area 44 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`
— area 44 is the pars opercularis component of Broca's area, and Broca's
area is a Brodmann-area-level label on a sub-region of VLPFC. This
package is the *label*, not the *agent*.

If you are looking for the other half of Broca's area, it is
`brodmann_area_45/` (pars triangularis), in the same brocas_area
sub-package. The two are the two halves of a single coupled unit, and
the coupling is expressed through their `brocas_weight` shares and their
`to_area_45` / `to_area_44` connectivity priors, not through imports.

IDENTITY
--------
    AREA_ID    = 44
    NAME       = "Brodmann area 44 (pars opercularis)"
    SYSTEM     = ["prefrontal_cortex"]     # single system; see below
    SUB_REGION = "ventrolateral_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = "brocas_area"             # nested sub-package membership

Note on SYSTEM: it's a list, consistent with the frontal registry pattern,
even though area 44 belongs to a single compute sub-region. The list form
is used uniformly across the frontal registry so that multi-system areas
(6, 8, 47) and single-system areas (44, and most others) have the same
shape and consumers can iterate without special-casing. Here the list has
exactly one element.

Note on SUB_REGION: this field is NOT present in the cingulate registry
entries. In the cingulate, `SYSTEM` sufficed because each functional
system (ACC, PCC, RSC) was a single compute sub-module. In the frontal
lobe, `"prefrontal_cortex"` is a *family* of five sub-regions, and the
specific sub-region that owns the area matters — area 44 goes to VLPFC,
area 46 to DLPFC, area 11/12 to OFC, and so on. SUB_REGION names the
specific sub-region that imports this area's config. It is consumed by
the owning sub-region's area-iteration code and by the frontal lobe's
assembly of the `intent` slice.

Note on GROUPING: also new relative to the cingulate. This field names
the *named sub-grouping* within the owning sub-region that this area
belongs to. Area 44's GROUPING is `"brocas_area"`; area 45's is the same;
area 46's would be `None` (or omitted) because DLPFC has no such
sub-grouping. GROUPING lets code that iterates Broca's-area components
(e.g. the VLPFC sub-module's language-production pathway) filter by
`entry.GROUPING == "brocas_area"` without hardcoding `{44, 45}`. The
field is shared across the entire frontal registry even though most
entries will have it as `None`.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 44 (pars opercularis)",
        "system": "prefrontal_cortex",
        "sub_region": "ventrolateral_prefrontal_cortex",
        "grouping": "brocas_area",
        "location": "posterior part of the inferior frontal gyrus, "
                    "just anterior to the ventral precentral gyrus",
        "cytoarchitecture": "dysgranular cortex; transitional between the "
                            "agranular motor cortex (area 4, immediately "
                            "posterior) and the granular prefrontal cortex "
                            "(area 45, immediately anterior)",
        "notes": (
            "Pars opercularis — the posterior half of Broca's area, and "
            "the more motor-speech-like of the two areas. Its cytoarchi-"
            "tecture is transitional: it sits directly anterior to the "
            "ventral precentral gyrus (area 4's face/mouth "
            "representation), and its layer V projection neurons are "
            "more motor-like than area 45's. Functionally it is the "
            "phonological and articulatory component of language "
            "production: the part that sequences speech sounds and "
            "drives the articulators (lips, tongue, jaw, larynx). The "
            "distinction from area 45 is between 'how to say it' (44) "
            "and 'what to say' (45). On the left, area 44 carries the "
            "dominant motor-speech production role; on the right, its "
            "role is prosodic (expressive intonation, emotional tone), "
            "with a much smaller articulatory contribution. The "
            "left/right split is directional, not complementary — the "
            "right's area 44 is prosody-forward, not 'the left's at "
            "reduced weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 44's config has three parts: (a) its share within Broca's area's
contribution to VLPFC, summing to 1.0 with area 45's share; (b) its
feature emphases within that contribution; and (c) its connectivity
priors to partner structures.

    LEFT_CONFIG = {
        # ---- share within Broca's area's contribution to VLPFC ----
        # 44 : 45  sum to 1.0. On the left, 44 takes the larger share
        # because it is the more motor-speech-like of the two, and the
        # left's language production is more articulatory-dominant than
        # its lexical-selection component.
        "brocas_weight":          0.55,   # area 45: 0.45

        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: strong phonological and articulatory weights (the
        # core of left-lateralised speech production); the lexical and
        # prosodic weights are area 45's / the right hemisphere's
        # business, and are present here only at low levels.
        "phonological":           0.80,   # phoneme sequencing
        "articulatory":           0.80,   # articulator motor commands
        "lexical_selection":      0.35,   # area 45's primary role, small here
        "prosodic":               0.15,   # right hemisphere's role, tiny here
        "syntactic":              0.40,   # some grammatical-sequencing role
        "verbal_working_memory":  0.30,   # contribution to the
                                          # phonological loop buffer

        # ---- connectivity priors to partner structures ----
        "to_primary_motor":       0.75,   # to area 4 face/mouth
                                          # representation; the direct
                                          # motor-speech output path
        "to_premotor_cortex":     0.65,   # premotor planning of speech
                                          # gestures
        "to_area_45":             0.70,   # coupling within Broca's area
        "to_arcuate_fasciculus":  0.70,   # the dorsal language pathway;
                                          # connects to superior temporal
                                          # (Wernicke's area) for
                                          # phonological-motor mapping
        "to_insula":              0.45,   # insular contribution to
                                          # articulatory planning
        "to_dlpfc":               0.35,   # via area 45 and VLPFC broadly
        "to_basal_ganglia":       0.40,   # gating of speech acts
        "to_commissures":         0.50,   # cross-midline speech
                                          # coordination (prosody from
                                          # the right)
    }

    Notes on the weights:
      - `brocas_weight` sums to 1.0 across areas 44 and 45. On the left
        the split is 0.55 / 0.45; the right's split is the mirror
        (0.45 / 0.55) because the right's Broca's-area contribution is
        more prosody-anchored and area 45 carries the prosodic-lexical
        interface there. The invariant is per-hemisphere: 44 + 45 = 1.0
        on each side, and the two sides' splits together are not
        constrained to complement.
      - Feature weights are multipliers on features extracted by the
        VLPFC sub-module. The left's `phonological` and `articulatory`
        weights are the highest feature weights in Broca's area on
        either side — they are what area 44 is FOR on the left.
      - The `lexical_selection` and `prosodic` weights are present and
        non-zero even on the left, because language production is
        integrated and even the left's area 44 receives some lexical
        and prosodic input. But they are much lower than area 45's
        lexical weight and the right area 44's prosodic weight.
      - Connectivity priors parameterise how strongly this area's
        signal reaches partner structures. The `to_primary_motor`
        prior is the highest, because area 44's articulatory output
        drives area 4's face/mouth representation directly — that's
        the anatomical basis for Broca's role in speech motor control.
        The `to_arcuate_fasciculus` prior reflects the dorsal language
        pathway that links Broca's area to Wernicke's area for
        phonological-motor mapping.
      - All values are plausible priors, not measured constants. The
        key constraints are the brocas_weight sum-to-1 invariant and
        the left/right directional mirror.

EXPORTS
-------
    from .brodmann_area_44 import BRODMANN_44    # int, == AREA_ID
    from .brodmann_area_44 import ANATOMY
    from .brodmann_area_44 import LEFT_CONFIG
    from .brodmann_area_44 import SYSTEM         # list, ["prefrontal_cortex"]
    from .brodmann_area_44 import SUB_REGION     # str
    from .brodmann_area_44 import GROUPING       # str, "brocas_area"

The `SUB_REGION` and `GROUPING` exports are additions relative to the
cingulate registry entries, documented in the IDENTITY section above.
Both are consumed by the owning sub-region's area-iteration code; no
cingulate-shaped consumer will break on them because the cingulate
entries don't have them (cingulate compute iterates by SYSTEM, which
still exists here).

Consumers should prefer the flat re-export path
(`from ...brodmann_areas import BRODMANN_44`) over reaching into the
brocas_area nesting; the nesting is a tree-organisation detail and the
flat path is the stable API.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in VLPFC, not here.
    - Must not import `prefrontal_cortex/` or any of its sub-regions
      (cycle; the compute imports from here, not the other way round).
    - Must not import `brodmann_area_45/` (sibling; the coupling is via
      the VLPFC compute layer, not via registry-to-registry imports).
      The `to_area_45` connectivity prior in LEFT_CONFIG is the
      expression of the coupling; there is no runtime import between
      the two areas.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-44
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only the
      feature/connectivity weights and the brocas_weight share.
"""