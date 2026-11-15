# Financial Statement Analyzer

Upload a balance sheet and an income statement, then read the ratios that matter: liquidity, leverage, profitability and activity, a DuPont decomposition, trend analysis and red flags.

Project 1 of a finance + AI portfolio.

## Status

**Phase 0 complete** — environment, project scaffold and a working Streamlit upload screen.

Next up: the ratio engine and the DuPont breakdown.

## What works today

- Streamlit app with CSV / Excel upload and a data preview
- Sample company data in `data/sample_company.csv`
- Smoke tests covering imports and the sample dataset

## Repository layout

| Path | Contents |
|---|---|
| `app.py` | Streamlit app |
| `src/financial_analyzer/` | Package (ratio engine — in progress) |
| `data/sample_company.csv` | Sample financial data |
| `test/test_smoke.py` | Smoke tests |
| `docs/what_i_learned.md` | Build notes |

## Run locally

Requires Python 3.12 (see `.python-version`).

```bash
uv sync
uv run streamlit run app.py
```

The app opens at http://localhost:8501.

## Tests

```bash
uv run pytest
```

## Tools

Python, pandas, Streamlit, Plotly, uv, Git.
