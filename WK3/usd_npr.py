# Exchange rate: 1 USD to NPR
exchange_rate = 152.58

# List of USD amounts to convert
usd_amounts = [5, 50, 500, 5000]

print("--- USD to NPR Conversion (Without Function) ---")
for usd in usd_amounts:
    npr = usd * exchange_rate
    print(f"${usd} USD = {npr:,.2f} NPR")