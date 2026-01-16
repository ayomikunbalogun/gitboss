from datetime import datetime
from app.ledger import Transaction
from app.report import spend_by_merchant, most_recent


def test_spend_by_merchant_normalizes_names_and_includes_refunds():
    txs = [
        Transaction("Amazon", 10.0, datetime(2026, 1, 10)),
        Transaction(" amazon ", 5.0, datetime(2026, 1, 11)),
        Transaction("AMAZON", -3.0, datetime(2026, 1, 12)),  # refund
    ]
    totals = spend_by_merchant(txs)
    assert totals["amazon"] == 12.0


def test_most_recent_returns_latest():
    txs = [
        Transaction("A", 1.0, datetime(2026, 1, 1)),
        Transaction("B", 1.0, datetime(2026, 1, 3)),
    ]
    assert most_recent(txs).merchant == "B"
