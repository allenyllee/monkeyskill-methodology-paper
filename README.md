# Evidence-Driven Generative Development

LaTeX source for the paper:

> **Evidence-Driven Generative Development: A Closed-Loop Method for Building and Validating LLM-Generated Software**

The paper's central claim is that the durable unit of generative software should be a
human-readable behavioral contract plus replayable evidence, not one generated
implementation. Executable Demos, criteria, constrained test specifications, and
final-hash browser evidence persist while LLM-generated implementations remain
replaceable candidates.

It includes separate architecture diagrams for the per-installation security pipeline and
the longer-term Demo-first development and criterion-evolution loop, plus an explicit
role-interaction diagram for Tester A, Attacker, Tester B, Builder, Runner, and trusted
orchestration. The reference case study also records the current three-run convergence
threshold, repair accounting, final-evidence requirements, and observed attempt counts.

A compiled PDF of the current draft is attached to the
[`v0.5.0-draft` prerelease](https://github.com/allenyllee/monkeyskill-methodology-paper/releases/tag/v0.5.0-draft).

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
- `appendix/` — manifest, MSkill, TestSpec, and grammar examples included by the paper
- `Makefile` — convenience build targets
- `.latexmkrc` — reproducible `latexmk` defaults

## arXiv preparation

The source intentionally uses portable `pdflatex` packages and BibTeX. Before submission:

1. Update author metadata and acknowledgments.
2. Complete the preregistered multi-capability evaluation described in the paper.
3. Replace engineering-observation language with measured results only where supported.
4. Run `latexmk -C`, rebuild, and inspect every page of `main.pdf`.
5. Upload `main.tex`, `references.bib`, and any required generated `.bbl`/figures according to the current arXiv submission instructions.

## Related implementation

- [MonkeySkill](https://github.com/allenyllee/monkeyskill)
- [MonkeySkill Store](https://github.com/allenyllee/monkeyskill-store)

## License

Paper text and figures are released under [CC BY 4.0](LICENSE).
