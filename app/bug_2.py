from decimal import Decimal

def parse_amount(amount_str: str) -> Decimal:
    cleaned = amount_str.replace("$", "").replace(",", "").strip()
    return (Decimal(cleaned))

def daily_spend_and_subscriptions(transactions: list[dict], subscriptions: set[str]) -> tuple[dict, dict]:
    daily = {}
    subscription_spend = {}

    for tx in transactions:
        date = tx.get("date")
        merchant = tx.get("merchant", "")
        amount = parse_amount(tx.get("amount", "0"))

        if not date or not merchant:
            continue

        if amount > 0:
            continue

        amount = abs(amount)
        daily[date] = daily.get(date, 0) + Decimal(amount)

        merchant_key = merchant.strip().lower()
        if merchant in subscriptions:
            subscription_spend[merchant_key] = subscription_spend.get(merchant_key, 0) + Decimal(amount)

    return daily, subscriptions

if __name__ == "__main__":
    txs = [
        {"id": "t1", "date": "2026-01-14", "merchant": "Netflix", "amount": "-$9.99"},
        {"id": "t2", "date": "2026-01-14", "merchant": "Tesco",   "amount": "-$12.50"},
        {"id": "t3", "date": "2026-01-14", "merchant": "Salary",  "amount": "$1200.00"},
        {"id": "t4", "date": "2026-01-15", "merchant": "SPOTIFY", "amount": "-$10.99"},
    ]
    subs = {"netflix", "spotify"}
    print(daily_spend_and_subscriptions(txs, subs))

