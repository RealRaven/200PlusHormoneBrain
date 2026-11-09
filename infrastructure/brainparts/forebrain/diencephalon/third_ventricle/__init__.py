"""
Package: infrastructure.brainparts.forebrain.diencephalon.third_ventricle
Anatomical Role:
    The third ventricle is a midline, slit-like cerebrospinal fluid (CSF)
    space at the center of the diencephalon, bordered laterally by the
    left and right thalami and hypothalami, superiorly by the tela
    choroidea and fornix, anteriorly by the lamina terminalis, and
    posteriorly by the cerebral aqueduct (which connects it to the
    fourth ventricle).

    It is a CSF SPACE, not a neural structure. It contains:
        - CSF, produced primarily by the choroid plexus of the lateral
          ventricles (and secondarily by the third ventricle's own
          choroid plexus).
        - The third ventricle's choroid plexus (tela choroidea), which
          contributes to CSF production.
        - The circumventricular organs that border it (see below).

    The third ventricle is bordered by SEVEN circumventricular organs or
    their adjacent structures, making it the diencephalon's CSF-CONTACT
    hub:
        - Subfornical organ (SFO; hypothalamus/subfornical_organ/): at
          the anterior-dorsal roof, near the interventricular foramen.
        - Organum vasculosum of the lamina terminalis (OVLT;
          lamina_terminalis/vascular_organ_of_lamina_terminalis/): at
          the anterior wall.
        - Median eminence (hypothalamus/median_eminence/): at the floor.
        - Subcommissural organ (SCO; subcommissural_organ/): at the
          posterior-dorsal junction with the cerebral aqueduct.
        - Pineal gland (epithalamus/pineal_gland/): posterior to the
          SCO, above the cerebral aqueduct (adjacent to the third
          ventricle's posterior wall).
        - Posterior pituitary / neurohypophysis (pituitary_gland/
          neurohypophysis/): at the floor, connected via the pituitary
          stalk.
        - Choroid plexus of the third ventricle: not a circumventricular
          organ in the standard sense, but a CSF-producing structure
          within the ventricle.
    The third ventricle is therefore the anatomically central CSF space
    of the diencephalon, and the space through which Reissner's fiber
    (from the SCO) passes caudally toward the cerebral aqueduct.

Functional Mode:
    - CSF space (primary role): the third ventricle is one of the four
      brain ventricles (with the two lateral ventricles and the fourth
      ventricle). Its role is CSF containment, flow, and distribution:
        * CSF flows from the lateral ventricles (via the interventricular
          foramina of Monro) into the third ventricle.
        * CSF flows from the third ventricle (via the cerebral aqueduct)
          into the fourth ventricle.
        * The third ventricle's choroid plexus contributes to CSF
          production.
    - CSF-mediated signaling hub (secondary role): the third ventricle
      is the CSF compartment adjacent to seven circumventricular organs
      (SFO, OVLT, median eminence, SCO, pineal, neurohypophysis). These
      organs exchange signals with the CSF (SFO and OVLT sense blood-side
      signals and report them; SCO secretes SCO-spondin into CSF; median
      eminence releases hypothalamic hormones into portal blood adjacent
      to the ventricle; pineal releases melatonin into the systemic
      circulation adjacent to the ventricle). The third ventricle is
      therefore the shared CSF compartment of the diencephalon's
      circumventricular organ family.
    - Structural context for Reissner's fiber: Reissner's fiber
      (secreted by the SCO into the third ventricle) passes caudally
      through the third ventricle, into the cerebral aqueduct, into the
      fourth ventricle, and into the central canal of the spinal cord.
      The third ventricle is therefore the proximal segment of
      Reissner's fiber's path.

Hormonal Modulation:
    None. The third ventricle is a CSF space; it is not a hormone target
    or source. Do not add a hormone section.

Memory Interfaces:
    None. The third ventricle does not read or write memory. Do not add
    a memory section.

Model Integration (Gemma-4-E2B):
    None. The third ventricle does not contribute a prompt fragment. It
    is a structural CSF space, not a state-emitting or state-processing
    structure. The circumventricular organs that border it emit their
    own contributions (via their downstream target nuclei); the third
    ventricle itself does not.

Reciprocal Connections:
    - ↔ telencephalon/.../lateral_ventricles/left and right (via the
      interventricular foramina of Monro; CSF flows from the lateral
      ventricles into the third ventricle; the lateral ventricles are
      Tier 4 structural spaces).
    - ↔ midbrain/.../mesencephalic_aqueduct (via the cerebral
      aqueduct; CSF flows from the third ventricle into the aqueduct;
      the aqueduct is a Tier 4 structural space).
    - ↔ hindbrain/.../fourth_ventricle (downstream of the cerebral
      aqueduct; CSF flows from the third ventricle, through the
      aqueduct, into the fourth ventricle).
    - ↔ hypothalamus/subfornical_organ (borders the anterior-dorsal
      third ventricle; the SFO is a circumventricular organ).
    - ↔ lamina_terminalis/vascular_organ_of_lamina_terminalis (borders
      the anterior third ventricle; the OVLT is a circumventricular
      organ).
    - ↔ hypothalamus/median_eminence (borders the floor of the third
      ventricle; the median eminence is a circumventricular organ).
    - ↔ subcommissural_organ (borders the posterior-dorsal third
      ventricle at the aqueduct junction; the SCO is a circumventricular
      organ).
    - ↔ epithalamus/pineal_gland (posterior to the third ventricle; the
      pineal is a circumventricular organ).
    - ↔ pituitary_gland/neurohypophysis (the neurohypophysis is below
      the third ventricle's floor, connected via the pituitary stalk).

Notes:
    - Tier 4 structural space. Keep this file short (~45 lines). The
      value of Tier 4 documentation is that it exists and says "CSF
      space, no function" — not that it is elaborate.
    - THE THIRD VENTRICLE IS A CSF SPACE, NOT A NUCLEUS, NOT A GLAND,
      NOT A CONDUIT. Do not add hormone, memory, or model-fragment
      sections; the explicit "None" sections above are the correct
      treatment.
    - THE THIRD VENTRICLE IS THE CSF CONTACT HUB OF THE DIENCEPHALON'S
      SEVEN CIRCUMVENTRICULAR ORGANS. It is the shared CSF compartment
      through which the SFO, OVLT, median eminence, SCO, pineal,
      neurohypophysis, and the third ventricle's own choroid plexus
      interact with the CSF. This is the third ventricle's one
      substantive contribution to the tree — not a function, but a
      shared anatomical context.
    - THE THIRD VENTRICLE IS THE PROXIMAL SEGMENT OF REISSNER'S FIBER'S
      PATH: Reissner's fiber (from the SCO) passes through the third
      ventricle, the cerebral aqueduct, the fourth ventricle, and the
      central canal. The third ventricle is not a producer or processor
      of Reissner's fiber — it is the first CSF compartment the fiber
      traverses.
    - UNPAIRED MIDLINE STRUCTURE. Do not create left/ or right/
      children. The third ventricle is a single midline space.
    - THE THIRD VENTRICLE IS DISTINCT FROM THE LATERAL VENTRICLES (in
      the telencephalon; two paired spaces) AND FROM THE FOURTH
      VENTRICLE (in the metencephalon; one midline space below the
      cerebellum). Three distinct Tier 4 CSF spaces; do not merge.
    - THE THIRD VENTRICLE IS DISTINCT FROM THE CEREBRAL AQUEDUCT (the
      narrow channel connecting it to the fourth ventricle; the
      aqueduct is documented under midbrain/.../mesencephalic_aqueduct/).
    - Vocabulary used above is defined in Stage 0 files:
      memory/stores/ is not applicable; chemicals_hormones/ is not
      applicable (except as named targets of the adjacent
      circumventricular organs, documented in their own files);
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * third_ventricle ↔ telencephalon/.../lateral_ventricles/left
          and right (CSF flow via the interventricular foramina).
        * third_ventricle ↔ midbrain/.../mesencephalic_aqueduct (CSF
          flow via the cerebral aqueduct).
        * third_ventricle ↔ hindbrain/.../fourth_ventricle (downstream
          CSF flow).
        * third_ventricle ↔ hypothalamus/subfornical_organ (adjacency).
        * third_ventricle ↔ lamina_terminalis/vascular_organ_of_lamina_
          terminalis (adjacency).
        * third_ventricle ↔ hypothalamus/median_eminence (adjacency).
        * third_ventricle ↔ subcommissural_organ (adjacency; Reissner's
          fiber path).
        * third_ventricle ↔ epithalamus/pineal_gland (adjacency).
        * third_ventricle ↔ pituitary_gland/neurohypophysis (adjacency
          via the pituitary stalk).
    - Connects upward to diencephalon/.
"""