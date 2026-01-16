from datetime import datetime


def parse_amount(amount_str: str) -> float:
    # Bug: fails on "£1,200.50", " 12.00 ", and negative amounts like "-£5.00"
    cleaned = amount_str.replace("£", "").replace(",", "")
    return float(cleaned)


def parse_date(date_str: str) -> datetime:
    # Bug: assumes DD/MM/YYYY but input is sometimes YYYY-MM-DD
    return datetime.strptime(date_str, "%d/%m/%Y")
