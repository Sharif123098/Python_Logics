def convert_date(date_str, from_cal, to_cal):
    if from_cal == to_cal:
        return date_str

    year, month, day = date_str.split("-")

    if from_cal == "AD" and to_cal == "BS":
        year = str(int(year) + 56)
    elif from_cal == "BS" and to_cal == "AD":
        year = str(int(year) - 56)

    return f"{year}-{month}-{day}"


def format_date(date_str, style, cal):
    year, month, day = date_str.split("-")
    month_index = int(month) - 1

    if style == "iso":
        return f"{date_str} {cal}"
    elif style == "full":
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        day_int = int(day)
        suffix = suffixes.get(day_int, "th") if day_int <= 3 else "th"
        return f"{day_int}{suffix} {bs_months[month_index]}, {year} {cal}"
    elif style == "nepali":
        return f"{bs_months[month_index]} {day}, {year} {cal}"


bs_months = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24",
        "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10",
        "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30",
        "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05",
        "cal": "BS", "need": "AD", "style": "full"},
]

for customer in customers:
    converted = convert_date(
        customer["date"], customer["cal"], customer["need"])
    formatted = format_date(converted, customer["style"], customer["need"])
    print(
        f"{customer['name']} | Original: {customer['date']} {customer['cal']} | Converted: {formatted}")
