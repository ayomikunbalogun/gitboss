from collections import defaultdict
from app.ledger import Transaction


def spend_by_merchant(transactions: list[Transaction]) -> dict[str, float]:
    totals = defaultdict(float)

    for tx in transactions:
        # Bug: key is not normalized; "Amazon", "amazon ", "AMAZON" become separate buckets
        if tx.amount > 0:
            totals[tx.merchant] += tx.amount

        # Bug: refunds (negative) are ignored instead of reducing totals
    return dict(totals)


def most_recent(transactions: list[Transaction]) -> Transaction | None:
    if not transactions:
        return None

    # Bug: sorts ascending, returns oldest
    transactions_sorted = sorted(transactions, key=lambda t: t.date)
    return transactions_sorted[0]
