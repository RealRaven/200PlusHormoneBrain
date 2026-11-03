"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.posterior.medial_area.mammillary_nuclei.right
Anatomical Role:
    Right posterior-division compartment of the mammillary bodies. This
    node EXISTS as a pointer; it has no substantive content of its own.
    It refers to the SAME anatomical structure as
    hypothalamus/mammillary_bodies/right/, documented in two tree
    locations for two different purposes:
        - hypothalamus/mammillary_bodies/right/ — the FULL memory-hub
          leaf (role, function, hormones, memory interfaces, model
          fragment with confabulation guardrail, all reciprocal
          connections).
        - THIS node — the posterior-division compartment. Records that
          the mammillary bodies sit in the posterior division of the
          hypothalamus (for tree completeness). Points to the full leaf
          for all substantive content.

    STRUCTURAL IDENTITY TRAP (reproduced from
    posterior/medial_area/__init__.py, ../../__init__.py, and
    ../left/__init__.py — the trap must be declared at every level
    where it appears, on both hemispheres):
    THIS node and hypothalamus/mammillary_bodies/right/ are the SAME
    anatomical structure. Stage 4 audit MUST treat them as ONE
    structure. Do not flag as duplicates. Do not merge the nodes. Do
    not duplicate content. The full content lives at
    mammillary_bodies/right/.

Functional Mode:
    Same as hypothalamus/mammillary_bodies/right/ § Functional Mode.
    See that file for the Papez circuit relay, Korsakoff syndrome,
    head-direction, theta-rhythm participation, and mammillotegmental
    output. Do NOT restate here.

Hormonal Modulation:
    Same as hypothalamus/mammillary_bodies/right/ § Hormonal Modulation.
    Minimal by design (thiamine is the defining clinical modulator).
    See that file. DO NOT duplicate.

Memory Interfaces:
    Same as hypothalamus/mammillary_bodies/right/ § Memory Interfaces.
    Reads episodic, short_term, temporal_sequence_learning; writes
    episodic INDIRECTLY via the Papez circuit (relay, not encoder).
    The indirect episodic write is the mammillary bodies' most
    important memory feature — do not lose it in the
    compartmentalization. See that file for the full statement.

Model Integration (Gemma-4-E2B):
    No fragment emitted here. The mammillary memory-relay fragment
    (with its confabulation guardrail) is emitted by
    hypothalamus/mammillary_bodies/right/ at the hypothalamic level. Do
    not emit a duplicate memory fragment from this compartment; doing
    so would double-count the memory-relay signal. The left and right
    mammillary fragments are aggregated at the hypothalamic level (see
    mammillary_bodies/left/ § Model Integration for the bilateral
    aggregation note).

Reciprocal Connections:
    - ↔ hypothalamus/mammillary_bodies/right (SAME STRUCTURE; Stage 4
      must treat as one; do not flag as duplicate; the full edge list
      — fornix, anterior thalamus, tegmental nuclei, hippocampus,
      subiculum, presubiculum, medial septal nuclei,
      mammillothalamic tract, medial forebrain bundle — is declared in
      mammillary_bodies/right/, NOT here).
    - ↔ ../../medial_area/__init__.py (upward to the sub-container;
      the sub-container declares this compartment's membership in the
      posterior division).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - DELTA OF A POINTER, right side. Short by design (~45 lines). All
      content lives in hypothalamus/mammillary_bodies/right/. This
      file records only the posterior-division compartmentalization and
      reproduces the trap.
    - MAMMILLARY-NUCLEI IDENTITY TRAP — BOTH HEMISPHERES NOW COMPLETE:
      with this file, the only dual-location structure in the entire
      tree is fully declared across all three levels (sub-container →
      container → delta) on both hemispheres. The trap is fully
      resolved; no content is duplicated; the canonical full leaf lives
      at mammillary_bodies/left|right/.
    - The trap declaration is reproduced above in abbreviated form. The
      full text is in posterior/medial_area/__init__.py; this delta
      points there and to mammillary_bodies/right/.
    - The Korsakoff clinical fact (thiamine deficiency → bilateral
      mammillary body lesions) is abbreviated to one sentence in the
      Hormonal Modulation pointer. The full clinical description
      (Wernicke encephalopathy, anterograde amnesia, confabulation,
      preserved procedural memory) lives in mammillary_bodies/right/
      and is NOT duplicated here. The bilateral nature of the clinical
      fact applies equally to both hemispheres.
    - DO NOT write this as a full leaf. If you find yourself
      restating the Papez circuit, the Korsakoff description, or the
      fornix/anterior-thalamus/tegmental-nuclei edges, stop — that
      content belongs in mammillary_bodies/right/.
    - No independent fragment; no hormone directions; no memory
      interface details (all inherited via pointers). Strict delta
      discipline at the leaf level.
    - The thalamic PVT vs. hypothalamic PVN trap does NOT apply here
      (that is a posterior/lateral_area/ concern, not a
      mammillary-nuclei concern).
    - Vocabulary used above is defined in Stage 0 files; see
      hypothalamus/mammillary_bodies/right/ § Notes for the full list.
    - Connects upward to hypothalamus/posterior/medial_area/
      mammillary_nuclei/.
"""