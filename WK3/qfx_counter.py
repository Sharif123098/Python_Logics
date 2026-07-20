def ticket_price(seat_type, count):
    # Define the price per ticket for each seat type
    prices = {
        "standard": 15.00,
        "premium": 25.00,
        "vip": 50.00
    }

    # Convert input to lowercase to handle accidental uppercase inputs (e.g., "VIP" or "Vip")
    seat_lower = seat_type.lower()

    # Check if the seat type exists in our dictionary
    if seat_lower in prices:
        return prices[seat_lower] * count
    else:
        print(f"Error: '{seat_type}' is not a valid seat type.")
        return 0.0


# --- Examples of how to use it ---
print(f"Total cost: ${ticket_price('standard', 3):.2f}")  # 3 * 15.00 = 45.00
print(f"Total cost: ${ticket_price('VIP', 2):.2f}")       # 2 * 50.00 = 100.00
print(f"Total cost: ${ticket_price('luxury', 1):.2f}")    # Invalid type
