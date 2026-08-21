score = float(input("Enter your score: "))

# Range check: flag unrealistic scores
if score < 0 or score > 100:
    print("Invalid score! Please enter a value between 0 and 100.")
elif score >= 80:
    print("Grade: A+")
elif score >= 75:
    print("Grade: A")
elif score >= 70:
    print("Grade: A-")
elif score >= 65:
    print("Grade: B+")
elif score >= 60:
    print("Grade: B")
elif score >= 55:
    print("Grade: B-")
elif score >= 50:
    print("Grade: C+")
elif score >= 45:
    print("Grade: C")
elif score >= 40:
    print("Grade: D")
else:
    print("Grade: F")