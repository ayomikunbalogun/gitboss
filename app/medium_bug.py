from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

SPIKE_MULTIPLIER =  2.0

@dataclass
class Tx:
    user_id: str
    booked_at: str  # "YYYY-MM-DD"
    amount_cents: int  # spend is negative, income is positive

def month_key(date_str: str) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return f"{dt.year}-{dt.month:02d}"

def spike_alerts(txs: List[Tx], month: str) -> Dict[str, List[str]]:
    by_day: Dict[str, Dict[str, int]] = {}
    for tx in txs:
        if month_key(tx.booked_at) != month:
            continue
        if tx.amount_cents > 0:
            continue
        by_day.setdefault(tx.user_id, {})
        by_day[tx.user_id][tx.booked_at] = by_day[tx.user_id].get(tx.booked_at, 0) + tx.amount_cents

    alerts: Dict[str, List[str]] = {}
    for user_id, days in by_day.items():
        total_spend = sum(days.values())
        avg_daily = total_spend / max(len(days), 1)

        for day, spend_cents in days.items():
            spend_abs = spend_cents
            if spend_abs >= SPIKE_MULTIPLIER * avg_daily:
                msg = f"Spike on {day}: {spend_abs}c vs avg {int(avg_daily)}c"
                alerts.setdefault(day, []).append(msg)
    return alerts

if __name__ == "__main__":
    txs = [
        Tx("u1", "2026-01-01", -500),`
        Tx("u1", "2026-01-02", -1000),
        Tx("u1", "2026-01-05", -4000),
        Tx("u1", "2026-01-07", +2000),
        Tx("u2", "2026-01-03", -1500),
        Tx("u2", "2026-01-04", -3000),
        Tx("u2", "2026-01-06", -6000),
        Tx("u2", "2025-12-31", -999),
    ]
    print(spike_alerts(txs, "2026-01"))
