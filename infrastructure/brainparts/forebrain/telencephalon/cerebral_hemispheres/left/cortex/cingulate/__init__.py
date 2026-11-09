"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate
=============================================================================================

The CINGULATE CORTEX of the left hemisphere — the salience and control lobe.

The cingulate sits on the medial wall above the corpus callosum, wrapped around
the limbic structures. Functionally it is the cortex's *arbiter*: it monitors
what the other lobes are doing, detects conflict and error, registers pain and
threat affect, decides how much control to allocate, and issues the resulting
"pay attention here / slow down / re-evaluate" signals. It is the only lobe
whose primary output is not a representation of the world but a *modulation of
the rest of the cortex*.

It publishes one slice, `salience`, but that slice carries both a
representation (what is currently significant) and a control demand (how much
processing effort to allocate).

FUNCTIONAL SUB-UNITS (the documented exception to one-node-per-lobe)
--------------------------------------------------------------------
Unlike the other five lobes, the cingulate's internal tree maps onto genuinely
distinct computations, so it is modelled as **three runtime sub-modules**, not
one. This is a deliberate exception to the granularity rule — justified because
these three systems have different inputs, different outputs, and different
failure modes:

    anterior_cingulate/    conflict monitoring, error detection, performance
                           evaluation, pain affect, and control allocation.
                           Brodmann 24/32 (cognitive division) and 25
                           (subgenual/affective division) live here as
                           constants. Outputs: conflict signal, error signal,
                           control demand, affective pain/negative-valence
                           weight.
    posterior_cingulate/   self-referential and contextual evaluation,
                           episodic/autobiographical recall cueing, and
                           environmental monitoring (the default-mode hub on
                           this side). Brodmann 23/31. Reads memory-relevant
                           state from the medial temporal lobe; outputs a
                           context/familiarity estimate and a self-relevance
                           weight.
    retrosplenial_cortex/  spatial context, heading, scene recognition, and
                           translation between egocentric and allocentric
                           frames. Brodmann 26/29/30. Outputs a spatial-context
                           tag used to bind the current scene to memory.

    indusium_griseum      NOT a runtime sub-module. A thin vestigial grey
                          matter remnant on the corpus callosum surface; keep
                          it as a named constant / anatomical annotation only.

The cingulate slice is therefore assembled from three sub-encodes:

    salience = {
        "conflict":       ACC conflict/error signal        (scalar 0..1)
        "control_demand": ACC allocated control            (scalar 0..1)
        "affect":         ACC pain/negative-valence weight (scalar 0..1)
        "self_relevance": PCC self/context relevance       (scalar 0..1)
        "familiarity":    PCC context familiarity          (scalar 0..1)
        "spatial_context":RSC heading/scene tag            (vector)
    }

INPUTS
------
The cingulate is a hub; it reads widely but shallowly:

    from frontal/    current goals, plans, and predicted outcomes
                     (to compute conflict = goal vs. actual)
    from parietal/   spatial attention and body state (feeds RSC)
    from insular/    interoceptive/affective state (feeds ACC affect)
    from temporal/   object identity and memory cues (feeds PCC recall)
    from subcortical/ feedback on action outcomes (error signal source);
                     this is the one lobe with a legitimate same-tick read of
                     subcortical evaluation results

CONTROL OUTPUT (intra-cortical, one tick delayed)
-------------------------------------------------
The `control_demand` and `conflict` channels do not go to motor output. They
are consumed by the Cortex base class and applied as an **attention/gain
modulation on the next tick** to whichever lobes the conflict implicates. This
keeps `step()` non-recursive: the cingulate influences the cortex one tick
later, never within its own tick. It is not a substitute for the basal
forebrain's global gain — cingulate gain is *targeted* (this lobe, this
feature), basal forebrain gain is *global* (arousal).

LEFT-SPECIFIC BIAS
------------------
The sub-modules are the same code as the right hemisphere; the LEFT config
changes the weights:

    ACC    slightly higher weight on language/lexical conflict and
           verbally-mediated control; slightly lower weight on autonomic
           and visceral affect (which the right ACC carries more strongly)
    PCC    higher weight on verbal/autobiographical context; lower on
           spatial/environmental monitoring
    RSC    mildly lower weight than the right on heading and scene layout

These are weights, not branches. The same Cingulate class runs both sides.

CROSS-MIDLINE RULE
------------------
No import or read of the right hemisphere's cingulate. Note that ACC conflict
signals are a classic commissural traffic case: when the two hemispheres
disagree, that disagreement is itself a conflict signal, but the exchange must
go through `telencephalon/commissures/`, not by direct access.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the three sub-modules, build
  LEFT_CINGULATE_CONFIG, instantiate the shared Cingulate class, expose it.
- The Cingulate class calls each sub-module's `encode(inputs, config)` and
  assembles the `salience` dict. No sub-module logic lives in the parent.
- Brodmann numbers, subgenual area 25, and indusium griseum are constants in
  the relevant sub-module, not classes. If area 25 ever needs its own state
  (e.g. to model its role in treatment-resistant depression and DBS), it
  becomes a field inside anterior_cingulate/, not a new package.
- The control-output channels are returned in the slice; the *application* of
  targeted gain is the Cortex base class's job, one tick later. Cingulate must
  not mutate other lobes.
- The same-tick read of subcortical action-outcome feedback is the only
  permitted upward read from subcortical; document any other as a bug.
- LEFT_CINGULATE_CONFIG mirrors RIGHT_CINGULATE_CONFIG (identical keys,
  complementary weights); assert this in tests.
"""