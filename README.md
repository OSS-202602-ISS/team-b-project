# Library Book Return Tracker

A tool that reads a library book list, checks which books are available or borrowed, and reports books that need to be returned.

**Team B** · Track: **A only**

## 1. What this tool does

This project helps librarians identify borrowed books and books that are overdue for return.

| Stage | Description |
|---|---|
| Input | `books.csv` containing book ID, title, author, status, and due date |
| Process | Checks borrowed books and identifies overdue books |
| Output | Displays a report in the terminal and saves an Excel report |

## 2. Technologies

- Python
- pandas
- rich
- openpyxl

## 3. How to install and run

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Run the automated tests:

```bash
python -m pytest
```

Run the program:

```bash
python -m src.main
```

## 4. Processing functions

The `src/process.py` module contains the processing functions:

- `format_label()` – formats book labels for display.
- `filter_records()` – identifies records that need attention.
- `summarize()` – summarizes the processed book records.

## 5. Team members

- Rima6
- shresthaissu2005-tech
- prismaa07
- monkeypradip23

## 6. Project structure

- `src/` – Python source code
- `tests/` – automated tests
- `data/` – sample input data
- `docs/` – project documentation
- `config.yaml` – project configuration
- `requirements.txt` – required Python libraries
- `AI_USAGE.md` – AI usage record
- `THIRD_PARTY.md` – third-party library information

## 7. Testing

Run the tests using:

```bash
python -m pytest
```

The processing functions should pass all automated tests.

## 8. Course requirements

- Work on a feature branch, not directly on `main`.
- Submit changes through pull requests.
- Get a teammate to review your pull request.
- Explain every line of code submitted.
- Record AI assistance in `AI_USAGE.md`.
- Do not commit passwords, API keys, or personal information.
