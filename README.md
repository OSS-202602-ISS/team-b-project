# Library Book Return Tracker

A tool that reads a library book list, checks which books are available or borrowed, and reports books that need to be returned.

**Team B** · Track: **A only**

## 1. What this tool does

This project helps librarians identify borrowed and overdue books.

| Stage | Description |
|---|---|
| Input | Library book records from a CSV file |
| Process | Checks borrowed books and identifies overdue books |
| Output | Reports book return information in the terminal and Excel |

## 2. Technologies

- Python
- pandas
- rich
- openpyxl

## 3. How to run

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest
```

Run the program:

```bash
python -m src.main
```

## 4. Processing functions

The `src/process.py` module contains:

- `format_label()` – formats book labels.
- `filter_records()` – filters records according to the configured score threshold.
- `summarize()` – calculates the count, highest score, and average score.

## 5. Team

- Rima6
- shresthaissu2005-tech
- prismaa07
- monkeypradip23

## 6. Project files

- `src/` – Python source code
- `tests/` – automated tests
- `data/` – sample input data
- `docs/` – project documentation
- `AI_USAGE.md` – AI usage record

## 7. Testing

Run:

```bash
python -m pytest
```

Current result: **3 tests passed**.
