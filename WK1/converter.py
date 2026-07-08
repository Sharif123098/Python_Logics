def convert_usd_to_npr(usd_amount, exchange_rate=150, commission_rate=0.01):

    gross_npr = usd_amount * exchange_rate

    commission = gross_npr * commission_rate
    net_npr = gross_npr - commission
    return gross_npr, commission, net_npr


usd_to_convert = 500

gross, comm, net = convert_usd_to_npr(usd_to_convert)

print(f"Amount to convert: {usd_to_convert} USD")
print(f"Gross Amount:      {gross:.2f} NPR")
print(f"Agent Commission:  {comm:.2f} NPR")
print(f"---------------------------------")
print(f"Net NPR Received:  {net:.2f} NPR")
