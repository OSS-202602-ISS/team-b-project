
"""Processing functions for the Library Book Return Tracker."""

from __future__ import annotations

from datetime import date


def format_label(name: str) -> str:
    """Return a display label for a record name."""
    return " ".join(word.capitalize() for word in name.strip().split())


def filter_records(records: list[dict]) -> list[dict]:
    """Keep only borrowed books."""
    return [
        record for record in records
        if str(record["status"]).strip().lower() == "borrowed"
    ]


def summarize(records: list[dict]) -> dict:
    """Count borrowed books and identify overdue books."""
    today = date.today()

    overdue = [
        record for record in records
        if record.get("due_date")
        and str(record["due_date"]).strip()
        and date.fromisoformat(str(record["due_date"])[:10]) < today
    ]

    return {
        "count": len(records),
        "overdue": overdue,
        "overdue_count": len(overdue)
    }
