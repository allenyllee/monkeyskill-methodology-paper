# Evidence-Driven Generative Development

LaTeX source for the paper:

> **Evidence-Driven Generative Development: A Closed-Loop Method for Building and Validating LLM-Generated Software**

The paper's central claim is that the durable unit of generative software should be a
human-readable behavioral contract plus replayable evidence, not one generated
implementation. Executable Demos, criteria, constrained test specifications, and
final-hash browser evidence persist while LLM-generated implementations remain
replaceable candidates.

The Related Work section compares EDGD with representative multi-agent software
engineering, test-driven intent formalization, generated-test, agent-skill evaluation,
real-environment, and prompt-injection-defense systems. It treats these components as
prior art and locates the paper's contribution in their contract-and-evidence-centered
composition.

It includes separate architecture diagrams for the per-installation security pipeline and
the longer-term Demo-first development and criterion-evolution loop, plus an explicit
role-interaction diagram for Tester A, Attacker, Tester B, Builder, Runner, and trusted
orchestration. The installation diagram distinguishes Builder-authored Public TestSpec,
fixed Developer Conformance in isolated Chromium/CDP, and fresh Independent TestSpec,
then shows approval, pre-install replay, installation, and final published-Demo evidence.
It also includes a separate generated-Runner bootstrap diagram: a readable, versioned
Bootstrap drives fresh Runner Builder/Tester roles, exact-hash atomic activation, and a generic
Host handoff, while the outer orchestrator remains responsible for application-specific acceptance.
The same figure includes the POC verified-copy boundary: the Store provides only a package
descriptor, the Extension independently re-downloads and pins the exact package and protocol, and
only Extension code constructs the prompt copied to the local agent.
The reference case study records the current three-run convergence threshold, repair
accounting, final-evidence requirements, and observed attempt counts. It also reports a
fresh real-browser run whose original/poisoned verdicts were allow/reject, whose fixed
Developer Conformance suite passed 7/7, and whose installed Demo was manually replayed
against the approved final hash.
An additional versioned repair diagram makes Builder's iterative role explicit: Builder
infers a repair from public or bounded independent diagnostics and synthesizes a complete
replacement, while trusted Runner checks remain the acceptance authority.
The real-environment section includes screenshots from a fresh published-Demo replay:
visible selection after an actual drag, successful input targeting through an overlay,
and a pasted marker retained beyond the page's rollback checkpoint. The paper labels
their provenance limits rather than treating them as evidence for an unrecorded hash.
The appendices reproduce the example MSkill package, shared TestSpec DSL, and complete
trusted non-executable Attacker template library used by the differential injection gate.
The title page and a dedicated disclosure section identify the use of OpenAI Codex
(GPT-5.6-Sol) for research and manuscript assistance while retaining Ya-Lun Li as the
sole accountable author.

A compiled PDF of the current draft is attached to the
[`v0.10.3-draft` prerelease](https://github.com/allenyllee/monkeyskill-methodology-paper/releases/tag/v0.10.3-draft).

## Build

Requirements:

- TeX Live or MiKTeX
- `latexmk`
- `pdflatex` and BibTeX

Build the PDF:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

On Windows PowerShell:

```powershell
latexmk.exe -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. To remove generated files:

```sh
latexmk -C
```

## Repository structure

- `main.tex` — complete paper source
- `references.bib` — BibTeX references
- `appendix/` — manifest, MSkill, TestSpec, Developer Conformance, grammar, and attacker examples included by the paper
- `appendix/runner-bootstrap-mskill.txt` — application-agnostic generated Runner Bootstrap excerpt
- `Makefile` — convenience build targets
- `.latexmkrc` — reproducible `latexmk` defaults
- `scripts/package-arxiv.py` — deterministic, portable arXiv source packager

## arXiv preparation

The source intentionally uses portable `pdflatex` packages and BibTeX. Before submission:

1. Update author metadata and acknowledgments.
2. Complete the preregistered multi-capability evaluation described in the paper.
3. Replace engineering-observation language with measured results only where supported.
4. Run `latexmk -C`, rebuild, and inspect every page of `main.pdf`.
5. Package and validate the source archive:

   ```sh
   python3 scripts/package-arxiv.py
   ```

   On Windows PowerShell:

   ```powershell
   python scripts/package-arxiv.py
   ```

   Alternatively, `make arxiv` builds the paper first and then packages it. The
   default output is `output/arxiv/EDGD-arxiv-source.zip`. Use `--output PATH`
   to choose a versioned filename.
6. Upload the generated ZIP according to the current arXiv submission instructions.

The packager deliberately includes only `main.tex`, `main.bbl`, `references.bib`,
and regular files under `appendix/`. It excludes PDFs and LaTeX build artifacts,
stores every archive path with POSIX `/` separators, uses deterministic ordering
and timestamps, verifies the ZIP manifest and integrity, and prints its SHA-256
digest. It fails if a required source file is missing; run `latexmk` first when
`main.bbl` has not yet been generated.

## Related implementation

- [MonkeySkill](https://github.com/allenyllee/monkeyskill)
- [MonkeySkill Store](https://github.com/allenyllee/monkeyskill-store)

## License

Paper text and figures are released under [CC BY 4.0](LICENSE).
