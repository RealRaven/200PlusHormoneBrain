"""
infrastructure.brainparts.forebrain.telencephalon
==================================================

The TELENCEPHALON (the "cerebrum") is the largest and most rostral division
of the brain and the substrate for higher-order cognition. In this project it
is the top-level container for everything that does *deliberate* processing:
perception, action selection, language, memory, emotion regulation, and the
executive control that ties them together. Functionally it is the part of the
system that (a) builds a model of the world, (b) evaluates that model against
goals, and (c) emits voluntary behaviour. The diencephalon below it supplies
drive/arousal and endocrine state; the telencephalon supplies *representation
and control*.

The telencephalon is organised into three direct children:

    cerebral_hemispheres/   left + right — the cortex and its subcortical
                            partners, each lateralised
    commissures/            the fibre bundles that let the two hemispheres
                            share state
    lateral_ventricles/     CSF spaces that cushion, clear waste, and host
                            neurogenesis

Each child below is described in terms of the computation it performs, so the
corresponding package can implement that computation directly.


1. CEREBRAL_HEMISPHERES  (left / right)
---------------------------------------
Two roughly symmetric halves. Each hemisphere contains four functional
systems: cortex, rhinencephalon, subcortical, and white_matter. Lateralisation
matters for programming: the left/right split is a real state boundary, not a
cosmetic one — the two hemispheres hold separate copies of cortical state and
only synchronise through the commissures. Treat each side as an independent
processor with its own working state.

1a. cortex/ — the grey-matter sheet. Six lobes, each a sensory/associative
    module:
      frontal      executive function, planning, working memory, voluntary
                   motor output, speech production (Broca), personality and
                   behavioural inhibition. The "controller" of the system.
      parietal     somatosensory integration, spatial attention, body schema,
                   multisensory convergence. The "where/how" stream.
      temporal     audition, language comprehension (Wernicke), object
                   recognition, and — via the medial temporal lobe — declarative
                   memory and emotion. The "what" stream and the memory hub.
      occipital    vision: primary visual cortex plus V2–V4 and dorsal/ventral
                   visual streams. The "sensor" for sight.
      insular      interoception (internal-body state), taste, autonomic
                   regulation, emotional awareness. The bridge between viscera
                   and feeling.
      cingulate    emotion regulation, pain affect, conflict monitoring,
                   cognitive control, autonomic drive. The "salience/conflict"
                   arbiter sitting between limbic and executive systems.

1b. rhinencephalon/ — the olfactory system and its limbic projections
    (olfactory bulb, tract, piriform cortex, periamygdaloid cortex, uncus,
    anterior olfactory nucleus). Smell is the only sense that reaches cortex
    without a thalamic relay, which is why it is wired directly into emotion
    and memory; model it as a fast, low-latency affect channel.

1c. subcortical/ — deep grey-matter partners of the cortex:
      basal_ganglia        action selection, response gating, reward-based
                           learning, habit formation (striatum, globus
                           pallidus). The "select and commit" circuit.
      basal_forebrain      cholinergic and GABAergic modulation of cortical
                           arousal, attention, and memory (nucleus basalis,
                           septal nuclei, diagonal band, substantia
                           innominata). The "gain/attention" modulator.
      claustrum            a thin sheet proposed to bind distributed cortical
                           representations into a unified percept — model it
                           as a salience/integration bus.
      extended_amygdala    sustained fear, anxiety, stress, and addiction
                           circuitry (bed nucleus of the stria terminalis).
                           The "slow, enduring threat" system, distinct from
                           the phasic amygdala proper.
      medial_temporal_lobe declarative memory (hippocampus: CA1–CA4, dentate
                           gyrus, subiculum, pre/parasubiculum) and emotion
                           (amygdala: basolateral, central, cortical nuclei).
                           The "encode and recall" engine.

1d. white_matter/ — long-range communication tracts within a hemisphere
    (corona radiata, internal/external/extreme capsules, cingulum, fornix,
    mammillothalamic tract, medial forebrain bundle, centrum semiovale).
    Implement as the routing layer: named bundles that carry typed signals
    between the grey-matter modules above.


2. COMMISSURES
--------------
The fibre bundles that synchronise the two hemispheres. This is the *only*
sanctioned path for state to cross the midline, so it is the natural place to
enforce lateralisation and to model interhemispheric transfer delay.

      corpus_callosum        the large cortical bridge; transfers sensory,
                             motor, and associative state between homologous
                             cortical areas. Model as the primary sync channel.
      anterior_commissure    connects olfactory and anterior temporal regions;
                             carries smell/emotion state across the midline.

3. LATERAL_VENTRICLES  (left / right)
-------------------------------------
The CSF-filled cavities of the telencephalon. Functionally they cushion the
brain, clear metabolic waste (glymphatic flow), and host the subventricular
zone where adult neurogenesis occurs. In the simulation they are a
maintenance/homeostasis channel and a plausible source of new "cells" for
memory or plasticity events.


Programming contract for this package
-------------------------------------
- This __init__.py should stay declarative: import the three child packages
  and expose them, but hold no runtime logic itself.
- Cerebral hemispheres are independent state machines; they must not read each
  other's variables directly — only via commissures.
- Every functional paragraph above is intended to become a class with a
  documented `step()`/`process()` entry point, so the docstring is the spec
  and the sub-packages are the implementation.
"""