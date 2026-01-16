from dataclasses import dataclass
from datetime import datetime
from app.parsing import parse_amount, parse_date


@dataclass(frozen=True)
class Transaction:
    merchant: str
    amount: float
    date: datetime


def build_transactions(raw_rows: list[dict]) -> list[Transaction]:
    txs = []
    for row in raw_rows:
        merchant = row.get("merchant", "").strip()

        # Bug: this drops valid merchants if merchant casing/spacing differs downstream
        if not merchant:
            continue

        amount = parse_amount(row["amount"])
        date = parse_date(row["date"])

        txs.append(Transaction(merchant=merchant, amount=amount, date=date))

    return txs
