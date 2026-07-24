def check_water_level(location, level_metres):
    if level_metres < 3:
        status = "Safe"
    elif level_metres <= 5:
        status = "Warning — Alert nearby villages"
    else:
        status = "DANGER — Evacuate immediately!"

    print(f"{location} ({level_metres} m): {status}")
    return status


sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]

for location, level in sensors:
    check_water_level(location, level)
