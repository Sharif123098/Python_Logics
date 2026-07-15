# Initialize an empty list to store all student data
class_records = []

# Set the number of students (You can change this to 3 just to test it quickly!)
total_students = 20

print(f"--- Enter Details for {total_students} Students ---")

# Loop to ask every student for their details
for i in range(1, total_students + 1):
    print(f"\nStudent {i} of {total_students}:")
    name = input("Enter student name: ")
    score = float(input(f"Enter {name}'s score: "))

    # Grade logic (from our previous step)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Save this student's data into a dictionary and add it to our list
    student_data = {"name": name, "score": score, "grade": grade}
    class_records.append(student_data)

# --- PRINTING THE REPORT CARD ---
print("\n" + "=" * 40)
print(f"{'FINAL CLASS REPORT CARD':^40}")
print("=" * 40)
print(f"{'Name':<20} | {'Score':<10} | {'Grade':<5}")
print("-" * 40)

# Loop through our records list to print each row
for student in class_records:
    # :<20 aligns text to the left with spaces for neat formatting
    print(
        f"{student['name']:<20} | {student['score']:<10.1f} | {student['grade']:<5}")

print("=" * 40)
