"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.brodmann_areas.brodmann_area_23
=========================================================================================================================

Brodmann area 23 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. This package
declares the canonical identity of area 23, says which functional sub-module
owns it, and supplies the per-area weights that the owning sub-module's
`encode()` reads. It defines no classes and no functions; the entire public
surface is the four names listed under "EXPORTS" below.

If you are looking for the computation area 23 participates in, it is in
`.../cingulate/posterior_cingulate/` — area 23 is one of the two areas (with
area 31) that make up the PCC's contextual/self-referential system. This
package is the *label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 23
    NAME      = "Brodmann area 23"
    SYSTEM    = "posterior_cingulate"
    LOBE      = "cingulate"
    SIDE      = "left"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 23",
        "system": "posterior_cingulate",
        "location": "posterior cingulate gyrus, ventral to area 31",
        "cytoarchitecture": "granular cortex, six layers, prominent layer IV",
        "notes": (
            "Core PCC node. Dense reciprocal connectivity with the medial "
            "temporal lobe (subiculum, parahippocampal gyrus) and with "
            "precuneus (medial parietal). Implicated in contextual "
            "associative memory, scene construction, and self-referential "
            "evaluation. Together with area 31 it constitutes the PCC "
            "hub whose dysfunction is associated with early Alzheimer's "
            "pathology; that clinical link is why its familiarity/context "
            "signal is modelled explicitly rather than collapsed into a "
            "generic 'memory' channel."
        ),
    }

CONFIG (LEFT)
-------------
    LEFT_CONFIG = {
        # relative weight of this area within the PCC system's
        # `familiarity` and `self_relevance` channels
        "pcc_weight":            0.55,   # complementary to area 31's 0.45

        # feature emphases inside this area's contribution.
        # LEFT bias: verbal/autobiographical context, lower spatial/visual.
        "verbal_context":        0.70,
        "autobiographical":      0.75,
        "scene_construction":    0.40,   # left PCC less scene/spatial weighted
        "self_reference":        0.65,
        "subjective_familiarity":0.60,

        # connectivity priors to partner structures, used when the PCC
        # system combines area contributions
        "to_hippocampus":        0.65,
        "to_precuneus":          0.50,
        "to_anterior_cingulate": 0.30,
        "to_retrosplenial":      0.45,
    }

    Notes on the weights:
      - `pcc_weight` is the share of the PCC system's aggregate signal that
        this area contributes, relative to area 31. The two sum to 1.0.
      - Feature weights are used as multipliers on the corresponding
        features extracted by the PCC sub-module, not as stand-alone
        quantities.
      - All values are plausible priors, not measured constants. They are
        expected to be tuned via experiments; the key constraint is that
        they mirror RIGHT_CONFIG with complementary values.

EXPORTS
-------
    from .brodmann_area_23 import BRODMANN_23     # int, == AREA_ID
    from .brodmann_area_23 import ANATOMY
    from .brodmann_area_23 import LEFT_CONFIG
    from .brodmann_area_23 import SYSTEM          # str, "posterior_cingulate"

Consumers should use these names directly. Do not reach into the module
namespace for any other attribute; anything not listed here is private and
may change.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `posterior_cingulate/` (that would create a cycle; the
      PCC imports from here, not the other way round).
    - Must not contain runtime logic of any kind. All logic belongs in the
      owning sub-module.
    - Must not diverge in structure from the right hemisphere's area-23
      package — same AREA_ID, same SYSTEM, same anatomy; only LEFT_CONFIG
      vs. RIGHT_CONFIG differ.
"""