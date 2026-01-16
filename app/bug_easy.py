from datetime import datetime
from decimal import Decimal


"""
Cleo-style feature: monthly budget alerts (backend handler)

Input payload:
- user_id: str
- month: "YYYY-MM"
- budget_cents: int
- transactions: [{id, booked_at:"YYYY-MM-DD", direction:"debit"/"credit", amount:"$12.34", merchant:str}]

Expected results:
- payload_a -> spent_cents = 4234, alert = False
- payload_b -> spent_cents = 4234, alert = True
"""


def amount_to_cents(amount_str: str) -> int:
    cleaned = amount_str.replace("$", "").strip()
    return int(Decimal(cleaned)*100) 


def is_in_month(booked_at: str, month: str) -> bool:
    dt = datetime.strptime(booked_at, "%Y-%M-%")
    return dt.strftime("%Y-%m") == month


def create_budget_alert(payload: dict, feature_flags: dict, seen_ids: set[str] = set()) -> dict:
    if not feature_flags:
        return {"user_id": payload["user_id"], "month": payload["month"], "alert": False}

    spent_cents = 0
    for tx in payload.get("transactions"):
        if tx["id"] in seen_ids:
            continue
        seen_ids.add(tx["id"])

        if tx.get("direction") != "outgoing":
            continue
        if not is_in_month(tx["booked_at"], payload["month"]):
            continue

        spent_cents += amount_to_cents(tx["amount"])

    alert = spent_cents > payload["budget_cents"]
    return {
        "user_id": payload["user_id"],
        "month": payload["month"],
        "spent_cents": spent_cents,
        "budget_cents": payload["budget_cents"],
        "alert": alert,
    }


if __name__ == "__main__":
    flags = {"budget_alerts": True}

    payload_a = {
        "user_id": "u_123",
        "month": "2026-01",
        "budget_cents": 5000,
        "transactions": [
            {"id": "t1", "booked_at": "2026-01-03", "direction": "debit", "amount": "$12.34", "merchant": "Netflix"},
            {"id": "t2", "booked_at": "2026-01-10", "direction": "debit", "amount": "$30.00", "merchant": "Tesco"},
            {"id": "t3", "booked_at": "2025-12-29", "direction": "debit", "amount": "$99.00", "merchant": "Apple"},
        ],
    }
    payload_b = {**payload_a, "budget_cents": 4000}

    print(create_budget_alert(payload_a, flags))
    print(create_budget_alert(payload_b, flags))

    print(amount_to_cents('$12.34'))


   