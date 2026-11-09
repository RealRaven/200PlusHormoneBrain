"""
Package: infrastructure.brainparts.forebrain.diencephalon.epithalamus.stria_medullaris
Anatomical Role:
    Tier 3 fiber tract. The stria medullaris is the primary afferent
    bundle to the habenular nuclei. It carries axons from septal nuclei,
    the preoptic area, the hypothalamus, and the thalamus into the
    habenula. It is a conduit, not a processor: it does not compute,
    modulate, or store anything.

Functional Mode:
    - Conduction only: septal / preoptic / hypothalamic / thalamic
      afferents → habenular nuclei (left and right). Direction is
      inbound to the habenula.
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
    - left/    Left stria medullaris. Same role as this parent, left
                 hemisphere. See left/__init__.py.
    - right/   Right stria medullaris. Same role as this parent, right
                 hemisphere. See right/__init__.py.

Notes:
    - Tier 3 container. Keep this file and its children short. The value
      of Tier 3 documentation is that it *exists* and says "conduit,
      nothing more" — not that it is elaborate.
    - The stria medullaris is the reciprocal-afferent edge for
      habenular_nuclei/left|right. Stage 4 audit should confirm the
      habenular leaf files reference this tract.
    - Connects upward to epithalamus/ and downward to left/ and right/.
"""