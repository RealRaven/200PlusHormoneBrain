"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.optic_chiasm
Anatomical Role:
    Tier 3 sensory decussation. The optic chiasm is a midline X-shaped
    crossing point at the base of the hypothalamus, ventral to the third
    ventricle and just anterior to the median eminence and pituitary
    stalk. Fibers from the nasal retina of each eye cross to the
    contralateral side; fibers from the temporal retina remain
    ipsilateral. The result is that the left visual field is represented
    in the right hemisphere and vice versa.

    The optic chiasm is NOT a nucleus and NOT a processing region: it is
    a decussation of axons, with no intrinsic neural processing, no
    endocrine secretion, and no memory function. It does nothing with
    the visual signal beyond routing it.

Functional Mode:
    - Decussation only: nasal retinal ganglion cell axons cross; temporal
      retinal ganglion cell axons remain ipsilateral. Direction is
      ascending (retina → optic tract → LGN → V1), not hypothalamic.
    - Retinohypothalamic tract branch-off (the one functional relevance
      to this tree): at the optic chiasm, a subset of retinal ganglion
      cell axons — the intrinsically photosensitive retinal ganglion
      cells (ipRGCs) expressing melanopsin — branch off to form the
      retinohypothalamic tract (RHT) and project to the suprachiasmatic
      nucleus (SCN). This is the anatomical basis of light entrainment
      of the circadian clock.
    - The optic chiasm itself does not process the light signal — it is
      the crossing point where the RHT branches off. The SCN is the
      processing target; the chiasm is the anatomical gateway.

Hormonal Modulation:
    None. The optic chiasm is not a hormone target or source. Do not add
    a hormone section to this Tier 3 file.

Memory Interfaces:
    None. The optic chiasm does not read or write memory. Do not add a
    memory section to this Tier 3 file. (The SCN's temporal_sequence_
    learning interface is documented in the SCN file, not here.)

Model Integration (Gemma-4-E2B):
    None. The optic chiasm does not contribute a prompt fragment. The
    circadian fragment is emitted by the SCN; the chiasm is upstream of
    the SCN's input, not a state contributor.

Reciprocal Connections:
    - ← retina (optic nerve from both eyes; retinal ganglion cell axons;
      the retina is NOT a tree node — document as a named external
      relay here, same convention as the pineal's SCG note).
    - → thalamus/left|right/metathalamus/lateral_geniculate_body (optic
      tract; the visual pathway continues to the thalamus and cortex;
      this is a boundary edge — the visual system proper is not the
      focus of this tree).
    - → hypothalamus/anterior/medial_area/left|right/
      suprachiasmatic_nucleus (retinohypothalamic tract; the RHT
      branches off at the chiasm and is the sole functionally relevant
      edge for this tree; the SCN file reciprocates this edge).
    - ↔ hypothalamus/median_eminence and hypothalamus/pituitary_stalk
      (anatomical adjacency; no signaling edge — they sit next to the
      chiasm at the base of the hypothalamus).

Notes:
    - Tier 3 SENSORY DECUSSATION subtype. This is the purest Tier 3
      shape in the tree: a decussation with no processing, no secretion,
      no memory, and no fragment. It is the template for other pure
      decussations if any are added later (e.g., the pyramidal
      decussation at the medulla, if a brainstem-level node is added).
    - The visual system proper (retina, LGN, V1, V2, V3, V4) is largely
      OUT OF SCOPE for this tree. The tree includes LGN as a thalamic
      relay (metathalamus/lateral_geniculate_body) and visual cortex
      Brodmann areas, but the optic chiasm file should NOT attempt to
      map the visual pathway — it names the boundary edges (retina in,
      LGN out) and the one functionally relevant hypothalamic branch
      (RHT → SCN).
    - The retinohypothalamic tract branch-off is the ONE piece of
      content that makes this file more than a stub. It is the
      anatomical basis of circadian light entrainment. Document it
      clearly; do not pad the file with visual-pathway content.
    - The retina is not a tree node; document it as a named external
      relay, same convention as the pineal's superior cervical ganglion
      note. Do not create retina/ as a child of optic_chiasm/.
    - Unpaired midline structure. Do not create left/ or right/
      children.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/10_* (circadian, melanopsin, ipRGCs); memory/
      stores/ is not applicable here; gateway/.
    - Connects upward to hypothalamus/.
"""