employees = []

def add_employee():
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")

    employee = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

    employees.append(employee)

    print("\nEmployee added successfully!")
    print(f"Name: {employee['Name']}, Department: {employee['Department']}, Salary: {employee['Salary']}\n")


def view_employees():
    if not employees:
        print("\nNo employees found.\n")
        return

    print("\n--- Employee List ---")
    for index, employee in enumerate(employees, start=1):
        print(f"{index}. Name: {employee['Name']}, Department: {employee['Department']}, Salary: {employee['Salary']}")
    print()


def main():
    while True:
        print("===== Employee Management Menu =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
