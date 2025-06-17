name=(input('Enter you name : '))
age=(int(input('Enter you age : ')))



subjects = {
    "Math": int(input("Enter Math marks: ")),
    "English": int(input("Enter English marks: ")),
    "Urdu": int(input("Enter Urdu marks: "))
}

bonus=input('Do you want to add bonus marks? (yes/no): ').strip().lower()
if bonus == 'yes':
    bonus_marks = int(input("Enter bonus marks: "))
add_bonus = lambda mark: mark + 5 if bonus == "yes" else mark

# Apply the lambda to each subject
subjects = {subj: add_bonus(mark) for subj, mark in subjects.items()}

# Step 4: Function to calculate average
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

average = calculate_average(subjects)

# Step 5: Assign grade using if-elif-else
if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"

# Step 6: Write report to a file
filename = "report_card.txt"
with open(filename, "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    for subject, mark in subjects.items():
        file.write(f"{subject}: {mark}\n")
    file.write(f"Average: {average:.2f}\n")
    file.write(f"Grade: {grade}\n")

# # Step 7: Read and display report card
# print("Final Report Card:")
# with open(filename, "r") as file:
#     print(file.read())

