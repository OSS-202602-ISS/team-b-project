# Project Plan

## 1. The tool

- **Name**: Library Book Return Tracker
- **One sentence**: A tool that reads a library book list, identifies borrowed and overdue books, and reports which books need to be returned.
- **Category**: management
- **Track**: A only

## 2. Scope - input, one processing step, output

| | Our project |
|---|---|
| **Input** | `books.csv` (book_id, title, author, status, due_date) |
| **Processing step** | Find borrowed books and identify which have passed their due dates |
| **Output** | A terminal table showing borrowed and overdue books, and `library_report.xlsx` |

**Definition of done**: Run the program with one command, read `books.csv`, identify borrowed and overdue books, and generate the terminal table and Excel report.

## 3. Open source we plan to use

| Library | Why we need it | On the whitelist? |
|---|---|---|
| pandas | Reads and filters book information from `books.csv` | yes |
| rich | Displays book information in a formatted terminal table | yes |
| openpyxl | Exports the book report to an Excel file | yes |

## 4. Team and roles

| Role | Who |
|---|---|
| PM | @monkeypradip23 |
| Developer | @Rima6 |
| Documentation | @prismaa07 |
| Reviewer | @shresthaissu2005-tech |

## 5. Schedule

| Chapter | What we finish |
|---|---|
| 11 | Repository set up, plan written, 3 issues opened, first feature branch |
| 12 | Core feature works end to end (the two blanks are filled) |
| 13 | Peer review, error handling, documentation complete, tests pass |
| Final submission | Final tag, "My contribution" written, peer evaluation done |

## 6. Risks

| What could go wrong | What we will do about it |
|---|---|
| The CSV file may contain missing or incorrect due dates or book statuses | Check the required columns and validate the data before processing |
