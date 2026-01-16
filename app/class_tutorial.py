class User:
    def __init__(self, user_id: str, name: str) -> None:
        self.user_id = user_id
        self.name = name

u = User("u_123", "Ayomi")


class Budget:
    def __init__(self, monthly_limit: int) -> None:
        self.monthly_limit = monthly_limit
        self.spent = 0

    def add_spend(self, amount: int) -> None:
        self.spent += amount

    def remaining(self) -> int:
        return self.monthly_limit - self.spent

b = Budget(500)
b.add_spend(120)
print(b.remaining())  # 380



from dataclasses import dataclass
from datetime import date
from decimal import Decimal


ALERT_THRESHOLD = Decimal("0.80")


@dataclass
class Transaction:
    booked_at: date
    merchant: str
    amount_pennies: int


@dataclass
class MonthlyBudget:
    month_key: str
    limit_pennies: int
    spent_pennies: int = 0

    def add(self, tx: Transaction) -> None:
        if tx.amount_pennies > 0:
            self.spent_pennies += tx.amount_pennies

    def remaining(self) -> int:
        return self.limit_pennies - self.spent_pennies


class BudgetAlertService:
    def __init__(self, budgets: dict[str, MonthlyBudget]) -> None:
        self.budgets = budgets

    def apply_transactions(self, txs: list[Transaction]) -> list[str]:
        alerts = []
        for tx in txs:
            mk = tx.booked_at.strftime("%m-%Y")
            budget = self.budgets.get(mk) or MonthlyBudget(mk)
            budget.add(tx)
            if budget.spent_pennies / budget.limit_pennies >= ALERT_THRESHOLD:
                alerts.append(f"ALERT {mk}: spent {budget.spent_pennies} of {budget.limit_pennies}")
        return alerts


if __name__ == "__main__":
    budgets = {
        "01-2026": MonthlyBudget("01-2026", limit_pennies=50_000),
    }

    txs = [
        Transaction(date(2026, 1, 3), "Tesco", 12_500),
        Transaction(date(2026, 1, 10), "Uber", 30_000),
        Transaction(date(2026, 1, 12), "Refund", -5_000),
    ]

    svc = BudgetAlertService(budgets)
    print(svc.apply_transactions(txs))

