import csv

# File name for storing employee data
FILE_NAME = 'employee_data.csv'

# Load data from the CSV file
def load_data():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        # Return an empty list if the file doesn't exist
        return [["Name", "Hire Date", "Department", "Performance", "Salary"]]

# Save data to the CSV file
def save_data(data):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Display all employee data
def display_data(data):
    print("\nEmployee Data:")
    for row in data:
        print(", ".join(row))
    print()

# Add a new employee
def add_employee(data):
    name = input("Enter employee name: ")
    hire_date = input("Enter hire date (YYYY-MM-DD): ")
    department = input("Enter department: ")
    performance = input("Enter performance score: ")
    salary = input("Enter salary: ")
    data.append([name, hire_date, department, performance, salary])
    print("Employee added successfully!")

# Remove an employee
def remove_employee(data):
    display_data(data)
    index = int(input("Enter the row number of the employee to remove (starting from 1): "))
    if 1 <= index < len(data):
        removed = data.pop(index)
        print(f"Employee {removed[0]} removed successfully!")
    else:
        print("Invalid row number!")

# Edit an employee
def edit_employee(data):
    display_data(data)
    index = int(input("Enter the row number of the employee to edit (starting from 1): "))
    if 1 <= index < len(data):
        row = data[index]
        print(f"Editing Employee: {', '.join(row)}")
        row[0] = input(f"Enter new name (current: {row[0]}): ") or row[0]
        row[1] = input(f"Enter new hire date (current: {row[1]}): ") or row[1]
        row[2] = input(f"Enter new department (current: {row[2]}): ") or row[2]
        row[3] = input(f"Enter new performance (current: {row[3]}): ") or row[3]
        row[4] = input(f"Enter new salary (current: {row[4]}): ") or row[4]
        print("Employee updated successfully!")
    else:
        print("Invalid row number!")

# Perform math operations
def perform_math(data):
    print("\nMath Operations:")
    print("1. Total Salary")
    print("2. Average Performance")
    choice = input("Select an option (1 or 2): ")
    if choice == "1":
        total_salary = sum(float(row[4]) for row in data[1:] if row[4])
        print(f"Total Salary: {total_salary}")
    elif choice == "2":
        avg_performance = sum(float(row[3]) for row in data[1:] if row[3]) / len(data[1:])
        print(f"Average Performance: {avg_performance}")
    else:
        print("Invalid choice!")

# Main menu
def main():
    data = load_data()
    while True:
        print("\nEmployee Management System")
        print("1. Display Employee Data")
        print("2. Add Employee")
        print("3. Edit Employee")
        print("4. Remove Employee")
        print("5. Perform Math Operations")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_data(data)
        elif choice == "2":
            add_employee(data)
        elif choice == "3":
            edit_employee(data)
        elif choice == "4":
            remove_employee(data)
        elif choice == "5":
            perform_math(data)
        elif choice == "6":
            save_data(data)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    main()
