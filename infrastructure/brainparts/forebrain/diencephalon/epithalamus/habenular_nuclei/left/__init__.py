"""
Package: infrastructure.brainparts.forebrain.diencephalon.epithalamus.habenular_nuclei.left
Anatomical Role:
    The left habenular complex, consisting of two subdivisions in a single
    anatomical node:
        - Lateral habenula (LHb): glutamatergic, projects to VTA, substantia
          nigra pars compacta, and dorsal raphe. Encodes negative reward
          prediction error and suppresses dopamine when outcomes fall short
          of expectation.
        - Medial habenula (MHb): cholinergic and substance-P rich, projects
          via the fasciculus retroflexus to the interpeduncular nucleus.
          Mediates nicotine withdrawal aversion and avoidance learning.
    Lateralization note: the functional asymmetry between left and right
    habenula in humans is not firmly established. Imaging work is mixed;
    some studies suggest left-LHb involvement in reward downshift and
    positive prediction error signaling (counter to the dominant negative-
    RPE role), while others find no reliable asymmetry. This file documents
    the region on its merits; do not assume the left habenula is a mirror
    of the right beyond what the literature supports.

Functional Mode:
    - Negative reward prediction error: LHb fires when outcome < prediction,
      suppressing VTA/SNc dopamine and biasing toward behavioral inhibition
      and re-evaluation.
    - Reward downshift: encodes omission or reduction of expected reward
      (distinct from punishment per se). Suggested left-LHb specialization
      in downshift contexts, but this is contested.
    - Aversive salience: sustained LHb activity produces learned-helplessness
      -like states; chronic hyperactivity is implicated in depression.
    - Anti-reward feedback loop: low dopamine → LHb activation → further
      dopamine suppression. The core regulatory loop of the region.
    - Nicotine withdrawal (MHb): MHb-IPN axis mediates withdrawal aversion
      and some avoidance learning.
    - Limbic-to-midbrain relay: receives septal, preoptic, and hypothalamic
      afferents via the stria medullaris and translates them into midbrain
      dopaminergic and serotonergic modulation.

Hormonal Modulation:
    - Dopamine: inverse coupling. Low DA → LHb activation; LHb activation
      → further DA suppression. The defining feedback loop; read DA level
      as an *input* and emit a suppression *signal* as output.
    - Serotonin: bidirectional with dorsal raphe. Raphe input modulates
      LHb excitability; LHb output inhibits raphe. Net effect: high LHb
      activity → reduced serotonergic tone.
    - GABA: LHb output is glutamatergic to inhibitory interneurons in VTA
      and raphe, producing net inhibition of dopamine and serotonin
      neurons. GABAergic tone within LHb modulates its own excitability.
    - Norepinephrine: increases LHb excitability under stress; couples
      arousal to aversive salience.
    - Opioids: kappa-opioid signaling in LHb produces aversive/dysphoric
      states; mu-opioid input can suppress LHb.
    - Substance P: primary neurotransmitter of the MHb-IPN axis; drives
      withdrawal-associated aversion.
    - CRH / cortisol: LHb is activated under acute stress and contributes
      to stress-induced dopamine suppression (anhedonia pathway).

Memory Interfaces:
    - Reads:
        * reinforcement_value_based_learning: prior outcomes for the
          current context, used to compute the prediction against which
          the actual outcome is compared.
        * short_term: the current prediction / expectation (working-memory
          buffer). RPE computation requires both prediction and outcome;
          both must be available at read time.
        * emotional_valence: prior aversive tags on similar contexts, to
          weight the salience of a new negative outcome.
    - Writes:
        * emotional_valence: negative tags on disappointing or aversive
          outcomes (feeds amygdala and hippocampus consolidation).
        * reinforcement_value_based_learning: the negative RPE record
          itself, so future predictions for this context are updated.
    - Does not write to episodic or semantic stores directly; negative
      valence tags propagate to hippocampus/cortex through the valence
      store.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - Prompt fragment (applied after the epithalamus-level fragments,
      before cortical reasoning fragments):
        "Aversive salience channel — left habenula:
         - Negative reward prediction error: [none / mild / strong].
         - Aversion strength (0-1): [X].
         - Dopamine suppression signal: [inactive / active / saturated].
         If non-zero, weight loss-framing over gain-framing, flag risk,
         reduce exploratory language, and prefer conservative options
         over novel ones. If strong, explicitly state uncertainty about
         optimistic projections and surface downside scenarios before
         recommending action. Do not suppress all output — aversive
         salience biases tone and recommendation, it does not silence
         reasoning."
    - The fragment is emitted only when the habenular channel is active
      (RPE < 0 or aversion strength > 0). On neutral or positive outcomes
      the fragment is omitted; the absence of the fragment is itself a
      signal (no aversive bias).
    - No multimodal input is consumed here; the fragment is text-only.

Reciprocal Connections (enforce in Stage 4 audit):
    - → midbrain/tegmentum/ventral_tegmental_area (via fasciculus
      retroflexus → interpeduncular nucleus → VTA; indirect; primarily
      inhibitory).
    - → midbrain/tegmentum/substantia_nigra/left/pars_compacta (and right;
      inhibitory).
    - → hindbrain/metencephalon/pons/tegmentum/dorsal_raphe_nucleus
      (habenulo-raphe; inhibitory).
    - → midbrain/tegmentum/interpeduncular_nucleus (MHb projection;
      direct, glutamatergic/substance-P).
    - ← epithalamus/stria_medullaris/left (primary afferent conduit from
      septal, preoptic, and hypothalamic regions; Tier 3 fiber tract).
    - ↔ right/ (hemisphere counterpart; no strong functional lateralization
      assumed, see Notes).

Notes:
    - Tier 1/2 leaf: full template. Role + hormones + memory + model
      fragment, all required. No container discipline.
    - This file is the FIRST-LEAF PATTERN EXEMPLAR: it is the shape all
      remaining ~350 Tier 1/2 leaves should follow. Copy the section
      headers, keep every section populated, replace content per region.
      Do not add new top-level sections without updating the parent
      convention first.
    - MHb and LHb are documented *within* this file, not as separate
      tree nodes. The tree splits by hemisphere, not subdivision.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, serotonin, GABA, norepinephrine,
      opioids), chemicals_hormones/02_* (CRH, cortisol), chemicals_hormones/
      01_* (substance P), memory/stores/ (reinforcement_value_based_
      learning, emotional_valence, short_term), and gateway/.
    - Connects upward to habenular_nuclei/.
"""