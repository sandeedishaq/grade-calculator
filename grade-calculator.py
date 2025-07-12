score = float(input("Enter the student's score: "))

if score >= 90:
    grade = "A"
    if score == 100:
        print("Perfect Score!")
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    if score < 40:
        print("Needs Serious Improvement!")

print(f"Score: {score}, Grade: {grade}")