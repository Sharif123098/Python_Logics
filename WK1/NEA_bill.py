def electricity_bill(past_meter_reading, current_reading_meter):
    this_year_units = past_meter_reading + current_reading_meter

    return this_year_units


past_meter_reading = 10
current_meter_reading = 15

service_charge = 100

total_amount = electricity_bill(past_meter_reading, current_meter_reading) + service_charge

print(f"Total amount :{total_amount*13} Nrs")

