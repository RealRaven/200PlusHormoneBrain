"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres
=======================================================================

The CEREBRAL HEMISPHERES are the two halves of the cerebrum. In this project
they are modelled as two *independent processors*, each with its own complete
copy of cortical and subcortical state, its own sensory input and motor output,
and its own memory buffers. The two sides are near-identical in structure but
not in weighting: they run the same code with different configuration, which is
what produces the functional asymmetries of the intact brain.

This package's job is to instantiate and hold those two processors:

    left/    one hemisphere instance (default: language/sequence weighting)
    right/   the other hemisphere instance (default: spatial/holistic weighting)

Each hemisphere, in turn, contains the same four subsystems, and the data flow
between them is what a single `step()` of a hemisphere must implement:

    sensory input
        -> cortex/          represent the world (six lobes, see telencephalon doc)
        -> rhinencephalon/  fast ipsilateral smell/affect channel
        -> subcortical/     gate actions, set gain, bind percepts, encode memory
        -> white_matter/    route the results within this hemisphere
        -> motor / effector output

Note the ordering: subcortical structures sit *between* representation and
output. The basal ganglia must approve an action before it leaves the
hemisphere; the basal forebrain sets the gain on the cortex before the next
tick; the medial temporal lobe writes the episode after the tick resolves.
A hemisphere step is therefore represent -> evaluate -> commit, not a pure
feed-forward pass.

1. LEFT (default configuration)
-------------------------------
The "sequential/detail" processor. Default weightings favour:
  - language production and comprehension (Broca/Wernicke dominance)
  - fine-grained, sequential, rule-based reasoning
  - local/detail processing and categorical classification
  - contralateral (right-hand) fine motor control
  - positive-valence approach and reward tracking
These are defaults, not hard rules: the same classes run on both sides, only
the weights and lateralised specialisations differ.

2. RIGHT (default configuration)
--------------------------------
The "spatial/holistic" processor. Default weightings favour:
  - spatial attention, navigation, and body schema
  - holistic/gestalt pattern recognition and face processing
  - emotional prosody, humour, and metaphor
  - arousal, vigilance, and novelty detection
  - negative-valence avoidance and threat tracking
Again: same code, different weights. The asymmetry is a configuration
difference, so it can be tuned or ablated for experiments.

3. INTRA-HEMISPHERIC SUBSYSTEMS (identical on both sides)
---------------------------------------------------------
  cortex/         six lobes = the representation layer (frontal, parietal,
                  temporal, occipital, insular, cingulate). See the
                  telencephalon package docstring for the per-lobe spec.
  rhinencephalon/ olfaction, wired directly to limbic structures; the only
                  sense that bypasses the thalamus, so model it as a
                  low-latency affect channel that can pre-empt cortical
                  processing.
  subcortical/    the evaluation and commitment layer:
                    basal_ganglia      select and commit an action
                    basal_forebrain    set cortical gain/attention
                    claustrum          bind distributed percepts
                    extended_amygdala  sustain threat/stress state
                    medial_temporal_lobe encode and recall episodes
  white_matter/   named intra-hemispheric tracts (capsules, cingulum, fornix,
                  corona radiata, etc.) — the routing layer for this side.

4. INTERHEMISPHERIC ISOLATION (the one hard rule)
-------------------------------------------------
A hemisphere must never read the other hemisphere's state directly. The only
sanctioned cross-midline path is the `commissures` package in the parent
(`telencephalon/commissures/`), which models transfer delay and bandwidth.
This keeps lateralisation honest: if the two sides agree, it is because they
communicated, not because they share memory.


Programming contract for this package
-------------------------------------
- This __init__.py is declarative: it instantiates `left` and `right` from a
  single Hemisphere class with two configs, and exposes both. No runtime
  logic lives here.
- The Hemisphere class owns its four subsystems and exposes one entry point,
  `step(sensory_input) -> motor_output`, which executes the
  represent -> evaluate -> commit order described above.
- Cross-hemisphere state exchange goes exclusively through the commissure
  API exported by the parent package; direct attribute access across the
  midline is a bug.
- Lateralised specialisation is expressed as config weights, not as code
  branches, so both hemispheres remain testable with identical unit tests.
"""