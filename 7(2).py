courses = []
total_units = 0

while True:
    add_more = input("Do you want to add a course? (yes/no): ").strip().lower()
    if add_more == 'no':
        break

    name = input("Enter course name: ")
    teacher_name = input("Enter teacher's first name: ")
    teacher_surname = input("Enter teacher's surname: ")
    units = int(input("Enter number of units: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")

    if total_units + units > 17:
        print(f"Cannot add course {name}. Total units would exceed 17.")
        continue

    course = (name, {"name": teacher_name, "surname": teacher_surname}, units, start_date)
    courses.append(course)
    total_units += units

print("\nStudent's courses:")
for course in courses:
    print(f"{course[0]}  {course[1]['name']} {course[1]['surname']}  {course[2]} units")

print(f"\nTotal units: {total_units}")
