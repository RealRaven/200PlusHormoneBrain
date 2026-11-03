"""
Package: infrastructure.brainparts.forebrain.diencephalon.subcommissural_organ
Anatomical Role:
    The subcommissural organ (SCO) is a small circumventricular organ
    located at the DORSAL ANTERIOR JUNCTION of the third ventricle and
    the cerebral aqueduct, just caudal to the pineal gland and ventral
    to the posterior commissure. It is a CSF-SECRETING STRUCTURAL ORGAN:
    it secretes glycoproteins — principally SCO-spondin — into the
    cerebrospinal fluid, where they polymerize to form REISSNER'S FIBER,
    a structural filament that extends caudally through the cerebral
    aqueduct, the fourth ventricle, and the central canal of the spinal
    cord.

    The SCO is a member of the circumventricular organ family, but with
    a distinct mechanism: it is primarily a SECRETOR into CSF, not a
    SENSOR from blood (contrast with the subfornical organ and OVLT,
    which are blood-side sensors). Its capillaries have some
    fenestrations, but its dominant role is ependymal secretion, not
    vascular sensing.

    Circumventricular organ family (this file is a new variant):
        - Pineal gland (epithalamus/): hormone SECRETION into blood.
        - Median eminence (hypothalamus/): hormone RELEASE into portal
          blood.
        - Adenohypophysis (pituitary_gland/): hormone SYNTHESIS into
          blood.
        - Neurohypophysis (pituitary_gland/): neurohemal STORAGE/
          RELEASE into systemic blood.
        - Subfornical organ (hypothalamus/): blood-side SENSING.
        - Subcommissural organ (THIS FILE): CSF-side STRUCTURAL
          SECRETION.

    DISTINCTIONS (critical — three adjacent structures could be
    confused):

    - SCO vs. PINEAL GLAND: the pineal gland is just rostral/adjacent
      to the SCO. The pineal SECRETES MELATONIN into blood (hormone);
      the SCO SECRETES SCO-spondin into CSF (structural glycoprotein).
      Different products, different release environments, different
      functions. Do not merge.

    - SCO vs. THIRD VENTRICLE / CEREBRAL AQUEDUCT: the SCO is a
      secretory organ AT the junction of these two CSF spaces, not a
      part of either. It contributes to CSF composition (via Reissner's
      fiber) but is a distinct anatomical organ. Do not merge with
      third_ventricle/ or midbrain/mesencephalic_aqueduct/.

    - SCO vs. EPITHALAMUS: the SCO is anatomically near the epithalamus
      (the epithalamus contains the pineal gland and habenula), but the
      SCO is a distinct diencephalon child, NOT an epithalamus child.
      The tree places it at diencephalon/subcommissural_organ/, not at
      diencephalon/epithalamus/subcommissural_organ/. Do not move it.

Functional Mode:
    - SCO-spondin secretion into CSF (primary function): the SCO's
      ependymal cells secrete SCO-spondin (a large glycoprotein) into
      the third ventricle CSF. SCO-spondin polymerizes to form
      Reissner's fiber, a filament that extends caudally through the
      aqueduct → fourth ventricle → central canal of the spinal cord.
    - Reissner's fiber (three documented functions, in decreasing
      order of confidence):
        * CSF FLOW REGULATION (established): Reissner's fiber is
          implicated in regulating CSF flow through the aqueduct and
          fourth ventricle; disruption is associated with altered CSF
          dynamics.
        * AXON GUIDANCE AND NEURONAL PATTERNING (moderate evidence):
          SCO-spondin has been shown to influence axon guidance and
          neuronal migration during development; the developing
          nervous system uses SCO-spondin as a substrate.
        * CSF HOMEOSTASIS (less established): Reissner's fiber may
          contribute to CSF protein composition and clearance; the
          specific mechanism is not fully established.
    - Circadian modulation (presumed; less established than the SCN's
      other outputs): the SCN leaf declares an SCN → SCO edge
      suggesting circadian gating of TGF-β secretion and CSF-flow
      circadian output. The functional evidence for circadian
      modulation of SCO secretion is weaker than the SCN's other
      circadian outputs (sleep, cortisol, melatonin, LH surge,
      feeding). Document as presumed, not established. (See Notes for
      the three corrections to the SCN leaf's framing of this edge.)
    - DEVELOPMENTAL INVOLUTION (the defining developmental fact): the
      SCO is well-developed in the FETAL brain and INVOLUTES in
      ADULTHOOD. In fetal life, Reissner's fiber is prominent and
      plays an active role in neural development (axon guidance,
      neuronal patterning). In adult humans, the SCO persists but is
      greatly reduced; its secretory output is much lower than in
      fetal development; Reissner's fiber is much less prominent. This
      is the correct developmental trajectory: fetal-functional →
      adult-rudimentary (contrast with the pars intermedia's
      rudimentary-throughout trajectory).
    - The SCO is therefore a CSF-secreting structural organ with a
      DEVELOPMENTAL TRAJECTORY: active in fetal development, reduced
      in adulthood. It is documented for tree completeness, for the
      anatomical distinctions from the pineal and the CSF spaces, and
      for its developmental role. It is not a functional hub in adult
      humans.

Hormonal Modulation (minimal — this is a CSF-secreting organ, not a
hormone-secreting one):
    - The SCO does not secrete hormones. Its output is SCO-spondin, a
      structural glycoprotein, into CSF. Do not list hormones as
      modulators or as outputs.
    - Developmental modulation (not hormonal in the usual sense): the
      SCO's secretory activity is highest in fetal and early postnatal
      life and declines with maturation. Document as developmental
      trajectory, not as a hormonal axis.
    - TGF-β family members are also produced by the SCO (co-secreted
      with SCO-spondin) and have been proposed as mediators of the
      SCN → SCO circadian modulation. The evidence is less established
      than for the tree's other circadian outputs (see the SCN
      corrections in Notes).
    - The SCO is NOT a significant endocrine source or target. Do not
      pad the section with the 12 axes.

Memory Interfaces:
    None. The SCO has no documented memory interface. It is a
    structural secretor into CSF, not a memory structure. Do not
    invent one.

Model Integration (Gemma-4-E2B):
    None. The SCO does not emit its own prompt fragment. Its
    contribution is CSF-level (Reissner's fiber formation, CSF flow
    regulation), not state-level. The circadian gating of its
    secretion, if any, would be carried by the SCN's circadian
    fragment (per the deferred SCN → SCO edge). Do not add an SCO
    fragment.

Reciprocal Connections:
    - ↔ anterior/medial_area/left|right/suprachiasmatic_nucleus (SCN →
      SCO; circadian modulation of SCO secretion; THE DEFERRED EDGE
      declared from the SCN leaf; see Notes for the three corrections
      to the SCN framing; SCN is midline-adjacent — verify).
    - ↔ third_ventricle (adjacent CSF space; the SCO secretes into the
      third ventricle CSF; the third ventricle is downstream of the
      SCO's secretion).
    - ↔ midbrain/mesencephalic_aqueduct (adjacent CSF space; Reissner's
      fiber extends caudally through the aqueduct; the aqueduct is
      downstream of the SCO's secretion).
    - ↔ epithalamus/pineal_gland (anatomically adjacent; the pineal is
      just rostral to the SCO; distinct organs with distinct
      functions; do not merge; no signaling edge).
    - ↔ epithalamus (anatomical adjacency to the epithalamus region;
      the SCO is a diencephalon child, not an epithalamus child; do
      not move it).

Notes:
    - Tier 2 organ leaf — the CSF-SECRETING STRUCTURAL variant with
      DEVELOPMENTAL INVOLUTION. This is a NEW Tier 2 variant,
      distinct from:
        * pineal_gland/ — single-hormone synthesis into blood.
        * adenohypophysis/ — six-hormone synthesis into blood.
        * neurohypophysis/ — two-hormone neurohemal storage/release.
        * pars_intermedia/ — rudimentary throughout (minimal human
          function).
        * subfornical_organ/ — blood-side sensing.
      The SCO is the tree's first Tier 2 organ that SECRETES INTO CSF
      and has a DEVELOPMENTAL TRAJECTORY (fetal-functional →
      adult-involuted). The "circumventricular organ family" now has
      six exemplars across its variants.
    - SINGLE FILE. The SCO is midline/unpaired; no left/ or right/
      children.
    - THREE CORRECTIONS to the SCN leaf's framing of the SCN → SCO
      edge (Stage 4 should apply these):
        (1) PATH CORRECTION: the SCN leaf (in
            anterior/medial_area/left|right/suprachiasmatic_nucleus/)
            declares an edge to "hypothalamus/subcommissural_organ".
            The correct path is diencephalon/subcommissural_organ/.
            The SCO is a diencephalon child, not a hypothalamus child.
            Stage 4 should correct the SCN path.
        (2) "ADJACENT" FRAMING CORRECTION: the SCN leaf describes the
            SCO as "adjacent." The SCN is in the anterior hypothalamus;
            the SCO is at the dorsal third ventricle / cerebral
            aqueduct junction, with the pineal gland between them.
            They are not locally adjacent; any functional relationship
            (circadian modulation of SCO secretion) must be via
            neural projections or CSF-mediated signaling, not local
            adjacency. Stage 4 should correct the "adjacent" framing.
        (3) CIRCADIAN FUNCTIONAL STATUS: the SCN leaf asserts
            "TGF-β and CSF-flow circadian output" from the SCO. The
            functional evidence for circadian modulation of SCO
            secretion is less established than the SCN's other
            circadian outputs (sleep, cortisol, melatonin, LH surge,
            feeding). The SCO file documents this as "presumed; less
            established." Stage 4 should soften the SCN leaf's
            assertion to match.
    - The three corrections are the same pattern as the LPO path
      correction (from earlier in the hypothalamus work): a deferred
      edge declared from one side, closed from the other side, with
      the closer noting corrections to the declarer's framing. Stage
      4 should apply all three.
    - The SCO's developmental involution (fetal-functional →
      adult-rudimentary) is the defining developmental fact. Unlike
      the pars intermedia (rudimentary throughout), the SCO has a real
      fetal role and loses it with maturation. This is a new
      developmental pattern in the tree.
    - The circumventricular organ family is now complete across its
      variants: pineal (secreting hormone), median eminence (portal
      release), adenohypophysis (synthesizing), neurohypophysis
      (neurohemal storage), subfornical organ (blood sensing), and
      SCO (CSF secreting). The OVLT (documented under
      lamina_terminalis/ in basal forebrain) will be the seventh and
      final circumventricular organ when drafted.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/10_* (circadian, SCN); memory/stores/ is not
      applicable; gateway/.
    - Connects upward to diencephalon/.
"""