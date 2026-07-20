# Exchange rate: 1 USD to NPR
EXCHANGE_RATE = 152.58

# Define the conversion function


def convert_usd_to_npr(usd_amount):
    return usd_amount * EXCHANGE_RATE


# List of USD amounts to convert
usd_amounts = [5, 50, 500, 5000]

print("--- USD to NPR Conversion (With Function) ---")
for usd in usd_amounts:
    npr = convert_usd_to_npr(usd)
    print(f"${usd} USD = {npr:,.2f} NPR")
