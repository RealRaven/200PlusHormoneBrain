"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.median_eminence
Anatomical Role:
    The median eminence is a specialized neurohemal structure at the base
    of the hypothalamus, at the floor of the third ventricle. It is the
    functional interface between the hypothalamus and the anterior
    pituitary: the site where parvocellular neurosecretory neurons release
    their hormones into the hypophyseal portal blood, which then carries
    them to the anterior pituitary.

    The median eminence is NOT a processing region and NOT a hormone
    source in its own right. It is a release surface and a barrier
    interface:
        - The hormones released here (CRH, TRH, GnRH, GHRH, somatostatin,
          dopamine) are PRODUCED by upstream hypothalamic nuclei (PVN,
          arcuate, preoptic area) and transported to the median eminence
          via their axons. The median eminence receives them and releases
          them; it does not synthesize them.
        - The hypophyseal portal system (superior hypophyseal artery →
          primary capillary plexus in the median eminence → portal veins
          → secondary capillary plexus in the anterior pituitary) is the
          delivery route.
        - The median eminence is a circumventricular-adjacent structure:
          its capillaries are fenestrated (unlike the blood-brain barrier
          proper), allowing peptide hormones to enter the portal blood.
          This is the anatomical basis of neuroendocrine secretion.
        - Tanycytes (specialized ependymal cells lining the floor of the
          third ventricle) regulate the median eminence: they form a
          barrier that can be opened or closed, gate portal hormone
          access, and contribute to the seasonal and metabolic plasticity
          of the hypothalamic-pituitary axis.

    The median eminence is therefore an INTERFACE, not a processor: it
    neither computes nor stores; it is the anatomical and functional
    junction through which hypothalamic neurosecretion reaches the
    anterior pituitary.

Functional Mode:
    - Neurohemal release site (primary function): the axon terminals of
      parvocellular neurosecretory neurons (from PVN, arcuate, preoptic
      area) release CRH, TRH, GnRH, GHRH, somatostatin, and dopamine into
      the primary capillary plexus of the hypophyseal portal system.
      These hormones then travel via portal veins to the anterior
      pituitary, where they regulate ACTH, TSH, LH/FSH, GH, and prolactin
      release.
    - Blood-brain barrier interface: fenestrated capillaries here allow
      peptide hormones (which cannot cross the blood-brain barrier
      elsewhere) to enter the portal blood. This is the anatomical basis
      of the neuroendocrine system.
    - Tanycyte gating: tanycytes regulate portal hormone access, can
      retract or extend their processes to modulate the release surface,
      and contribute to the plasticity of the hypothalamic-pituitary axis
      across the estrous/menstrual cycle, photoperiod, and metabolic
      state.
    - Retrograde signaling (minor, less characterized): some evidence
      suggests the median eminence participates in retrograde signaling
      from the pituitary to the hypothalamus, but the functional
      significance is not established. Document as a minor role, not an
      anchor.
    - The median eminence is a RELEASE SITE, not an endocrine organ: it
      does not produce the hormones it releases, and it does not have
      its own endocrine output. Its functional identity is "the place
      where hypothalamic hormones enter the portal blood."

Hormonal Modulation (minimal; the median eminence is a release surface,
not a source or a target in the usual sense):
    - The six releasing/inhibiting hormones pass through here as
      RELEASED SUBSTANCES, not as modulators of the median eminence
      itself: CRH, TRH, GnRH, GHRH, somatostatin, dopamine.
    - Tanycyte plasticity is modulated by estradiol (cycle-dependent
      remodeling), thyroid hormones (metabolic state), and photoperiod
      (melatonin, seasonal). These are modulators of the *release
      surface*, not of the median eminence as a processing region.
    - The median eminence is NOT a principal target of the 12 endocrine
      axes. It is a *conduit and release site*. Do not list CRH, cortisol,
      etc. as modulators in the usual sense.
    - Direction summary: the six releasing/inhibiting hormones exit
      through the median eminence; tanycyte plasticity is modulated by
      estradiol, thyroid hormones, and melatonin (release-surface
      modulators). Do not add additional endocrine "modulators" beyond
      these.

Memory Interfaces:
    None. The median eminence is a release site and does not read or
    write episodic, semantic, procedural, or reinforcement-learning
    memory. It does not participate in the memory circuits. Do not add
    memory interfaces; the hypothalamic nuclei it serves carry their own
    memory interfaces (PVN, arcuate, preoptic area).

Model Integration (Gemma-4-E2B):
    None directly. The median eminence does not emit its own prompt
    fragment. The hormones released here are documented in the fragments
    of the nuclei that PRODUCE them:
        - CRH → PVN's HPA fragment.
        - TRH, somatostatin → PVN's HPT/growth fragment.
        - GnRH → PeN/MPN/MnPO's reproductive fragment.
        - Dopamine (prolactin inhibition) → arcuate's fragment (when
          drafted).
        - GHRH → arcuate's fragment (when drafted).
    The median eminence is a *physical gateway*, not a signal-emitting
    node; the model prompt does not need a median-eminence block. The
    pituitary_gland fragment (from the pituitary's own file) carries the
    output state; the median eminence does not.

Reciprocal Connections:
    - ← hypothalamus/anterior/medial_area/left|right/
      paraventricular_nucleus (CRH, TRH, somatostatin axon terminals;
      the principal PVN → median eminence edge).
    - ← hypothalamus/tuberal/medial_area/left|right/arcuate_nucleus
      (GnRH-adjacent kisspeptin relay to GnRH neurons is upstream, but
      arcuate is the source of GHRH and dopamine to the median eminence;
      the arcuate → median eminence edge carries dopamine and GHRH).
    - ← hypothalamus/anterior/lateral_area/left|right/
      periventricular_preoptic_nucleus and
      hypothalamus/anterior/medial_area/left|right/preoptic_area
      (GnRH neurons project to the median eminence; the GnRH → median
      eminence edge is the final common pathway of the HPG axis).
    - → pituitary_gland/anterior (via the hypophyseal portal system; the
      median eminence → anterior pituitary edge is the neuroendocrine
      output pathway).
    - ↔ pituitary_gland/neurohypophysis (the neurohypophysis sits
      adjacent to the median eminence at the base of the pituitary
      stalk; they are anatomically distinct but contiguous — the
      neurohypophysis receives magnocellular axon terminals from SON/PVN,
      not portal hormones).
    - ↔ hypothalamus/pituitary_stalk (the infundibulum carries both the
      portal vessels and the magnocellular axons; the pituitary stalk is
      a Tier 3 conduit).

Notes:
    - Single-file structure. The median eminence is unpaired and midline;
      do not create left/ or right/ children.
    - Shape: specialized interface (a Tier 2 organ / Tier 3 conduit
      hybrid). Its defining property is that it is a RELEASE SITE, not a
      source or processor. Do not draft it as if it were an endocrine
      gland (it doesn't produce the hormones it releases) and do not
      draft it as if it were a fiber tract (it is not a passive
      conduit — the fenestrated capillaries and tanycytes make it an
      active interface).
    - The median eminence's functional identity is "the place where
      hypothalamic hormones enter the portal blood." That sentence is
      the anchor for the whole file.
    - The six releasing/inhibiting hormones are documented in their
      PRODUCING nuclei (PVN, arcuate, preoptic area) and in their
      TARGET (anterior pituitary). The median eminence file carries the
      interface, not the hormones. Do not duplicate.
    - The tanycyte gating role is a real functional contribution of the
      median eminence (it is not a passive capillary bed) and should be
      documented. But it is a regulatory role, not a processing role.
    - The neurohypophysis is NOT served by the median eminence: it
      receives magnocellular axon terminals directly from SON/PVN, not
      via the portal system. The median eminence serves the
      ADENOHYPOPHYSIS (anterior pituitary). Do not conflate.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, GnRH), 02_* (HPA, CRH), 03_*
      (HPT, TRH, somatostatin, GHRH, thyroid hormones), 04_* (satiety,
      dopamine-adjacent, ghrelin/leptin modulate tanycytes), 10_*
      (circadian, melatonin); memory/stores/ is not applicable here
      (no memory interface); gateway/.
    - Connects upward to hypothalamus/.
"""