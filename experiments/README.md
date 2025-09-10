
## Experiments

This folder contains small, focused experiments for the Shauffeur project. Each experiment should be:

- Config-driven (YAML configs under `experiments/configs/` when needed).
- Reproducible (explicit seed, logging, versioned config file).
- Small and focused (one responsibility per script).

Included experiments:

- `01_explain_event.py` — demonstrates converting a simple ADAS event into an LLM prompt and measuring latency.
- `00_template_experiment.py` — a template experiment showing config-driven execution, seeding, and artifact output. Use this as a starting point for new experiments.

See `../docs/meta_prompt.md` for the project meta-prompt that guides experiment design and expected outputs.

When adding an experiment, update this README and `docs/research_notes.md` with assumptions, config used, and results.
