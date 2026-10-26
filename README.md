# Louisville 2026 Pokémon TCG analysis

A deck decision study for the Pokémon TCG Louisville Regional (October 2026, Standard format), written October 3, 2026 before the event.

It compares two competitive decks (Kang/Crustle control and Mega Starmie/Froslass aggro) using:

- **Field-share models** built from dated public results across three Regionals (Baltimore, Frankfurt, Brisbane), reported as ranges rather than point estimates.
- **A seeded Monte Carlo opening-hand simulator** (100,000 iterations) for opening hands, mulligans, prizes and search sequencing, with sampling error reported.
- **Exact 60-card decklists** and card-legality validation.
- **Evidence labels** on every claim in the report: verified fact, simulation result, data-based inference, or strategic judgment.

Start with [`final_report.md`](final_report.md). Sources are listed in [`sources.md`](sources.md).

---

# Louisville 2026 preparation project

This project deliberately limits computation to opening hands, mulligans, prizes, search sequencing, field weighting, and sensitivity. It does **not** contain a fake full-game Pokémon engine.

Run the opening study:

```sh
python3 simulator/opening_sim.py --iterations 100000 --seed 20261003
```

Outputs:

- `final_report.md`: findings, matchup strategy, deck changes, decision framework and testing plan
- `meta_data.csv`: dated raw event shares used in the field model
- `decklists/`: exact 60-card submitted and candidate lists
- `results/opening_simulation.json`: raw Monte Carlo output
- `testing_sheet.csv`: physical-game log

The opponent opening-board inputs in `simulator/config.json` are editable assumptions. They must be replaced with observed opening data before treating the donk estimate as Louisville-specific.
