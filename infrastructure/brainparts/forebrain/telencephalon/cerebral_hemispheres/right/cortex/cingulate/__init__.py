"""
infrastructure/brainparts/forebrain/telencephalon.cerebral_hemispheres.right.cortex.cingulate
============================================================================================

The CINGULATE CORTEX of the right hemisphere — the salience and control lobe.

Mirror of the left cingulate package. The cingulate sits on the medial wall
above the corpus callosum and acts as the cortex's *arbiter*: it monitors what
the other lobes are doing, detects conflict and error, registers pain and
threat affect, decides how much control to allocate, and issues the resulting
"pay attention here / slow down / re-evaluate" signals. Its primary output is
not a representation of the world but a *modulation of the rest of the
cortex*.

It publishes one slice, `salience`, carrying both a representation (what is
currently significant) and a control demand (how much processing effort to
allocate).

FUNCTIONAL SUB-UNITS (the documented exception to one-node-per-lobe)
--------------------------------------------------------------------
Inherited unchanged from the left cingulate; see
`.../left/cortex/cingulate/__init__.py` for the full rationale. In short:
these three systems have different inputs, outputs, and failure modes, so they
are modelled as three runtime sub-modules rather than one:

    anterior_cingulate/    conflict monitoring, error detection, performance
                           evaluation, pain affect, control allocation.
                           Brodmann 24/32 (cognitive) and 25 (subgenual/
                           affective) as constants. Outputs: conflict, error,
                           control_demand, affective weight.
    posterior_cingulate/   self-referential/contextual evaluation, episodic
                           recall cueing, environmental monitoring. Brodmann
                           23/31. Outputs: self_relevance, familiarity.
    retrosplenial_cortex/  spatial context, heading, scene recognition,
                           egocentric<->allocentric translation. Brodmann
                           26/29/30. Outputs: spatial_context tag.

    indusium_griseum      NOT a runtime sub-module. Vestigial grey matter on
                          the corpus callosum; a named constant / anatomical
                          annotation only.

    salience = {
        "conflict":        ACC conflict/error signal        (scalar 0..1)
        "control_demand":  ACC allocated control            (scalar 0..1)
        "affect":          ACC pain/negative-valence weight (scalar 0..1)
        "self_relevance":  PCC self/context relevance       (scalar 0..1)
        "familiarity":     PCC context familiarity          (scalar 0..1)
        "spatial_context": RSC heading/scene tag            (vector)
    }

INPUTS
------
The cingulate is a hub; it reads widely but shallowly:

    from frontal/    current goals, plans, and predicted outcomes
    from parietal/   spatial attention and body state (feeds RSC strongly on
                     this side)
    from insular/    interoceptive/affective state (feeds ACC affect
                     strongly on this side)
    from temporal/   object identity, faces, and memory cues
    from subcortical/ feedback on action outcomes (error signal source); the
                     one lobe with a legitimate same-tick read of subcortical
                     evaluation results

CONTROL OUTPUT (intra-cortical, one tick delayed)
-------------------------------------------------
`control_demand` and `conflict` are consumed by the Cortex base class and
applied as *targeted* attention/gain modulation on the next tick to whichever
lobes the conflict implicates. They are not motor output and do not recurse
within the same tick. This targeted gain is distinct from the basal
forebrain's global arousal gain.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left; the RIGHT config changes the weights:

    ACC    higher weight on autonomic/visceral affect and threat-related
           conflict; slightly lower on lexical/verbal conflict
    PCC    higher weight on spatial/environmental monitoring and scene
           familiarity; lower on verbal/autobiographical context
    RSC    higher weight than the left on heading, spatial layout, and
           egocentric<->allocentric translation

These are weights, not branches. The same Cingulate class runs both sides.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's cingulate. When the two
hemispheres disagree, that disagreement is itself a conflict signal, but the
exchange must go through `telencephalon/commissures/`, not by direct access.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the three sub-modules, build
  RIGHT_CINGULATE_CONFIG, instantiate the shared Cingulate class, expose it.
- The Cingulate class calls each sub-module's `encode(inputs, config)` and
  assembles the `salience` dict. No sub-module logic lives in the parent.
- Brodmann numbers, subgenual area 25, and indusium griseum are constants in
  the relevant sub-module, not classes. Any sub-region that later needs its
  own state becomes a field inside its parent sub-module, not a new package.
- Control-output channels are returned in the slice; the Cortex base class
  applies targeted gain one tick later. Cingulate must not mutate other
  lobes.
- The same-tick read of subcortical action-outcome feedback is the only
  permitted upward read from subcortical; document any other as a bug.
- RIGHT_CINGULATE_CONFIG mirrors LEFT_CINGULATE_CONFIG (identical keys,
  complementary weights); assert this in tests.
""""""
infrastructure/brainparts/forebrain/telencephalon.cerebral_hemispheres.right.cortex.cingulate
============================================================================================

The CINGULATE CORTEX of the right hemisphere — the salience and control lobe.

Mirror of the left cingulate package. The cingulate sits on the medial wall
above the corpus callosum and acts as the cortex's *arbiter*: it monitors what
the other lobes are doing, detects conflict and error, registers pain and
threat affect, decides how much control to allocate, and issues the resulting
"pay attention here / slow down / re-evaluate" signals. Its primary output is
not a representation of the world but a *modulation of the rest of the
cortex*.

It publishes one slice, `salience`, carrying both a representation (what is
currently significant) and a control demand (how much processing effort to
allocate).

FUNCTIONAL SUB-UNITS (the documented exception to one-node-per-lobe)
--------------------------------------------------------------------
Inherited unchanged from the left cingulate; see
`.../left/cortex/cingulate/__init__.py` for the full rationale. In short:
these three systems have different inputs, outputs, and failure modes, so they
are modelled as three runtime sub-modules rather than one:

    anterior_cingulate/    conflict monitoring, error detection, performance
                           evaluation, pain affect, control allocation.
                           Brodmann 24/32 (cognitive) and 25 (subgenual/
                           affective) as constants. Outputs: conflict, error,
                           control_demand, affective weight.
    posterior_cingulate/   self-referential/contextual evaluation, episodic
                           recall cueing, environmental monitoring. Brodmann
                           23/31. Outputs: self_relevance, familiarity.
    retrosplenial_cortex/  spatial context, heading, scene recognition,
                           egocentric<->allocentric translation. Brodmann
                           26/29/30. Outputs: spatial_context tag.

    indusium_griseum      NOT a runtime sub-module. Vestigial grey matter on
                          the corpus callosum; a named constant / anatomical
                          annotation only.

    salience = {
        "conflict":        ACC conflict/error signal        (scalar 0..1)
        "control_demand":  ACC allocated control            (scalar 0..1)
        "affect":          ACC pain/negative-valence weight (scalar 0..1)
        "self_relevance":  PCC self/context relevance       (scalar 0..1)
        "familiarity":     PCC context familiarity          (scalar 0..1)
        "spatial_context": RSC heading/scene tag            (vector)
    }

INPUTS
------
The cingulate is a hub; it reads widely but shallowly:

    from frontal/    current goals, plans, and predicted outcomes
    from parietal/   spatial attention and body state (feeds RSC strongly on
                     this side)
    from insular/    interoceptive/affective state (feeds ACC affect
                     strongly on this side)
    from temporal/   object identity, faces, and memory cues
    from subcortical/ feedback on action outcomes (error signal source); the
                     one lobe with a legitimate same-tick read of subcortical
                     evaluation results

CONTROL OUTPUT (intra-cortical, one tick delayed)
-------------------------------------------------
`control_demand` and `conflict` are consumed by the Cortex base class and
applied as *targeted* attention/gain modulation on the next tick to whichever
lobes the conflict implicates. They are not motor output and do not recurse
within the same tick. This targeted gain is distinct from the basal
forebrain's global arousal gain.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left; the RIGHT config changes the weights:

    ACC    higher weight on autonomic/visceral affect and threat-related
           conflict; slightly lower on lexical/verbal conflict
    PCC    higher weight on spatial/environmental monitoring and scene
           familiarity; lower on verbal/autobiographical context
    RSC    higher weight than the left on heading, spatial layout, and
           egocentric<->allocentric translation

These are weights, not branches. The same Cingulate class runs both sides.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's cingulate. When the two
hemispheres disagree, that disagreement is itself a conflict signal, but the
exchange must go through `telencephalon/commissures/`, not by direct access.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the three sub-modules, build
  RIGHT_CINGULATE_CONFIG, instantiate the shared Cingulate class, expose it.
- The Cingulate class calls each sub-module's `encode(inputs, config)` and
  assembles the `salience` dict. No sub-module logic lives in the parent.
- Brodmann numbers, subgenual area 25, and indusium griseum are constants in
  the relevant sub-module, not classes. Any sub-region that later needs its
  own state becomes a field inside its parent sub-module, not a new package.
- Control-output channels are returned in the slice; the Cortex base class
  applies targeted gain one tick later. Cingulate must not mutate other
  lobes.
- The same-tick read of subcortical action-outcome feedback is the only
  permitted upward read from subcortical; document any other as a bug.
- RIGHT_CINGULATE_CONFIG mirrors LEFT_CINGULATE_CONFIG (identical keys,
  complementary weights); assert this in tests.
"""