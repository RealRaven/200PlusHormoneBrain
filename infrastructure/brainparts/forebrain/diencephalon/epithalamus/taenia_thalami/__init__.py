"""
Package: infrastructure.brainparts.forebrain.diencephalon/epithalamus/taenia_thalami
Anatomical Role:
    Tier 3 fiber tract. The taenia thalami is a thin band of white matter
    on the dorsal surface of the thalamus, running along the roof of the
    third ventricle toward the habenula. It carries a subset of afferents
    into the habenular nuclei, complementary to the larger stria
    medullaris. It is a conduit, not a processor: it does not compute,
    modulate, or store anything.

Functional Mode:
    - Conduction only: dorsal thalamic surface afferents → habenular
      nuclei (left and right). Direction is inbound to the habenula.
    - Relative to the stria medullaris: the taenia thalami is the smaller
      of the two habenular afferent bundles. Where both are present, treat
      the stria medullaris as primary and the taenia thalami as secondary
      in any connectivity summary.
    - No intrinsic processing, no neurotransmitter release of its own,
      no state. Tier 3 convention: role-only docstring.

Hormonal Modulation:
    None. Tier 3 fiber tracts are not hormone targets or sources. Do not
    add a hormone section to a Tier 3 file.

Memory Interfaces:
    None. Tier 3 fiber tracts do not read or write memory stores. Do not
    add a memory section to a Tier 3 file.

Model Integration (Gemma-4-E2B):
    None. Tier 3 fiber tracts do not contribute prompt fragments. Their
    downstream targets (habenular nuclei) emit fragments; the tract
    itself does not.

Children (Tier 3 deltas — ~3 lines each):
    - left/    Left taenia thalami. Same role as this parent, left
                 hemisphere. See left/__init__.py.
    - right/   Right taenia thalami. Same role as this parent, right
                 hemisphere. See right/__init__.py.

Notes:
    - Tier 3 container. Keep short. The taenia thalami is a minor afferent
      bundle; its documentation's value is presence, not detail.
    - Distinguish from stria_medullaris/: both are Tier 3 habenular
      afferents, but the stria medullaris is the primary conduit (septal,
      preoptic, hypothalamic sources) and the taenia thalami is secondary
      (dorsal thalamic surface). Stage 4 audit should confirm both are
      referenced by habenular_nuclei/left|right, with the stria medullaris
      listed first.
    - Connects upward to epithalamus/ and downward to left/ and right/.
"""