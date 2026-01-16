from decimal import Decimal 

def amount_to_cents(amount_str: str) -> int:
    cleaned = amount_str.replace("$", "").strip()
    
    
    return int(cleaned)

print(amount_to_cents("$12.34"))
