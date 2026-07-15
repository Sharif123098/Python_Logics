# Define the defined rates per unit
RATE_1 = 5.00   # For the first 50 units
RATE_2 = 7.50   # For units between 51 and 100
RATE_3 = 10.00  # For any units above 100

# Ask how many offices you need to calculate for
num_offices = int(input("Enter the total number of offices: "))
building_records = []

print("\n--- Gathering Consumption Data ---")

for i in range(1, num_offices + 1):
    office_name = input(f"\nEnter name or number for Office {i}: ")
    units = float(input(f"Enter total units consumed by {office_name}: "))

    # Calculate bill using progressive tiered logic
    if units <= 50:
        # Everything falls into Tier 1
        bill = units * RATE_1
    elif units <= 100:
        # First 50 units at Rate 1 + the remaining units at Rate 2
        bill = (50 * RATE_1) + ((units - 50) * RATE_2)
    else:
        # First 50 at Rate 1 + next 50 at Rate 2 + anything left at Rate 3
        bill = (50 * RATE_1) + (50 * RATE_2) + ((units - 100) * RATE_3)

    # Save the data
    building_records.append(
        {"office": office_name, "units": units, "bill": bill})

# --- PRINTING THE ELECTRICITY REPORT ---
print("\n" + "=" * 50)
print(f"{'COMMERCIAL BUILDING ELECTRICITY REPORT':^50}")
print("=" * 50)
print(f"{'Office':<15} | {'Units Used':<12} | {'Total Bill ($)':<12}")
print("-" * 50)

total_building_bill = 0

for record in building_records:
    print(
        f"{record['office']:<15} | {record['units']:<12.1f} | ${record['bill']:<12.2f}")
    total_building_bill += record['bill']

print("-" * 50)
print(f"{'TOTAL BUILDING':<15} | {'':<12} | ${total_building_bill:<12.2f}")
print("=" * 50)
