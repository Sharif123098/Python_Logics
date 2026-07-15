# Define the student's score
score = 85

# Determine the letter grade based on the score
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

# Output the result
print(f"Score: {score} -> Grade: {grade}")
