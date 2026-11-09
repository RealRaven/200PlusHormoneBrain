"""
Package: infrastructure.brainparts.forebrain.diencephalon.pituitary_gland.pars_intermedia
Anatomical Role:
    The pars intermedia is the thin strip of tissue between the
    adenohypophysis (anterior pituitary) and the neurohypophysis
    (posterior pituitary), derived embryologically from the posterior
    wall of Rathke's pouch (like the adenohypophysis, but from a
    distinct region). It is RUDIMENTARY IN HUMANS: in non-human species
    it produces melanocyte-stimulating hormone (MSH) and endorphins,
    but in adult humans it is vestigial and its functional contribution
    is minimal.

    This is a Tier 2 organ leaf for a rudimentary structure. It is
    documented for anatomical completeness (it is a subdivision of the
    pituitary gland) and for anatomical precision (it is distinct from
    both of its neighbors), not because it is a functional hub. Do not
    over-write it: the pars intermedia has thin functional literature
    in humans.

    DISTINCTIONS (reproduced from the parent pituitary_gland/
    container; critical — apply at every level):

    - PARS INTERMEDIA vs. ADENOHYPOPHYSIS: distinct subdivisions. The
      adenohypophysis is the glandular anterior pituitary (six
      hormones; functional in humans); the pars intermedia is a thin
      intervening strip (MSH/endorphins; rudimentary in humans). Do
      not merge.

    - PARS INTERMEDIA vs. NEUROHYPOPHYSIS: distinct subdivisions. The
      neurohypophysis is the neural posterior pituitary (two stored
      hormones; functional); the pars intermedia sits between them.
      Do not merge.

    - PARS INTERMEDIA vs. NEUROHYPOPHYSIS (a common anatomical
      confusion): some older anatomy texts grouped the pars intermedia
      with the posterior pituitary, but the pars intermedia is derived
      from Rathke's pouch (oral ectoderm) like the adenohypophysis,
      NOT from neural ectoderm like the neurohypophysis. The pars
      intermedia is not part of the neurohypophysis; it is a distinct
      third subdivision.

Functional Mode:
    - MSH (melanocyte-stimulating hormone; rudimentary in humans): in
      non-human species, pars intermedia MSH regulates skin
      pigmentation (melanin synthesis and dispersal in melanocytes).
      In humans, MSH is produced primarily by the arcuate nucleus POMC
      neurons (via POMC cleavage) and by the skin itself, NOT by the
      pars intermedia; the pars intermedia's MSH contribution is
      negligible in adult humans.
    - Endorphins (rudimentary in humans): in non-human species, pars
      intermedia produces beta-endorphin and related peptides. In
      humans, endorphins are produced primarily by the arcuate POMC
      neurons and the pituitary corticotropes, not by the pars
      intermedia.
    - No functional role in adult humans: the pars intermedia is
      vestigial in adult humans. Its contribution to circulating
      MSH/endorphins is minimal. Document this factually; do not
      invent functional roles.
    - The pars intermedia is therefore a Tier 2 organ with minimal
      human functional content. It is documented for tree completeness
      and for the anatomical distinctions from its two neighbors;
      nothing else.

Hormonal Modulation:
    - MSH (output; rudimentary in humans): in non-human species,
      regulated by hypothalamic dopamine (inhibitory) and TRH
      (stimulatory). In humans, the pars intermedia's MSH production
      is minimal; the main human MSH sources are the arcuate POMC
      neurons and the skin.
    - Endorphins (output; rudimentary in humans): in non-human
      species, co-produced with MSH. In humans, the arcuate POMC
      neurons and the pituitary corticotropes are the main sources.
    - Direction summary: dopamine ↓ MSH, TRH ↑ MSH (in non-human
      species); minimal in humans. Do not pad with hormonal detail
      that the human literature does not support.
    - The pars intermedia is NOT a significant endocrine source in
      adult humans. Do not pad the section with the 12 axes.

Memory Interfaces:
    None. The pars intermedia has no documented memory interface. Do
    not invent one.

Model Integration (Gemma-4-E2B):
    None. The pars intermedia does not emit a prompt fragment. It is a
    rudimentary organ; it has no state to report to the model. The
    parent pituitary_gland container and the two sibling leaves
    (adenohypophysis, neurohypophysis) specify the pituitary's
    contributions; the pars intermedia does not.

Reciprocal Connections:
    - ↔ adenohypophysis/ (anatomically adjacent within the pituitary
      gland; distinct subdivisions; do not merge; no documented
      signaling edge beyond anatomical adjacency in humans).
    - ↔ neurohypophysis/ (anatomically adjacent; distinct subdivisions;
      do not merge; no documented signaling edge beyond anatomical
      adjacency in humans).
    - ↔ hypothalamus/arcuate_nucleus and hypothalamus/paraventricular_
      nucleus (via their POMC-derived MSH/endorphin production, which
      is the dominant human source; the pars intermedia's contribution
      is supplementary in humans).
    No other reciprocal edges are documented for the pars intermedia
    in humans. Do not invent them.

Notes:
    - Tier 2 organ leaf — the RUDIMENTARY variant. Distinct from
      pineal_gland/ (single-hormone synthesis), adenohypophysis/
      (six-hormone synthesis), and neurohypophysis/ (neurohemal
      storage). The pars intermedia's defining property is that it is
      functionally vestigial in adult humans.
    - SINGLE FILE. Midline/unpaired; no left/ or right/ children.
    - SHORT LEAF BY DESIGN (~50 lines). The pars intermedia has thin
      functional literature in humans. Do not over-write it. Same
      discipline as inah_1/ and the tuberal nucleus.
    - THE THREE DISTINCTIONS are the file's substance: distinct from
      adenohypophysis; distinct from neurohypophysis; distinct from
      the neurohypophysis by EMBRYONIC ORIGIN (pars intermedia is
      from Rathke's pouch, like the adenohypophysis, not from neural
      ectoderm like the neurohypophysis). This third distinction is
      the subtle one and is often confused in older texts.
    - NO FUNCTIONAL HUB ROLE in adult humans. The pars intermedia
      produces MSH/endorphins in non-human species; in humans, these
      are produced mainly by the arcuate POMC neurons and the
      corticotropes. Do not claim a significant human endocrine role.
    - Do not add a prompt fragment. The pars intermedia has no state to
      report.
    - CLOSES THE PITUITARY GLAND SUBTREE: with this file, the pituitary
      gland subtree is complete — container + adenohypophysis +
      neurohypophysis + pars intermedia. The pituitary gland is fully
      documented across all three subdivisions.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, POMC-adjacent), 03_* (HPT, TRH),
      04_* (satiety, POMC, MSH-adjacent), 05_* (dopamine, endorphins);
      memory/stores/ is not applicable; gateway/.
    - Connects upward to diencephalon/pituitary_gland/.
"""