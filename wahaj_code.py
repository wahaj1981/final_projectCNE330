import csv
from datetime import datetime

# File name for storing employee data
FILE_NAME = r'C:\Users\Wahaj\Documents\GitHub\final_projectCNE330\employees.csv'
UPDATED_FILE_NAME = r'C:\Users\Wahaj\Documents\GitHub\final_projectCNE330\updated_employees.csv'

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
def save_data(data, file_name=FILE_NAME):
    with open(file_name, mode='w', newline='') as file:
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
    ID = input("Enter employee ID: ")
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")
    hire_date = input("Enter hire date (YYYY-MM-DD): ")
    department = input("Enter department: ")
    performance = input("Enter performance score: ")
    salary = input("Enter salary: ")
    data.append([ID, first_name, last_name, hire_date, department, performance, salary])
    save_data(data)  # Save changes to the original file
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
        row[0] = input(f"Enter new employee ID (current: {row[0]}): ") or row[0]
        row[1] = input(f"Enter new first name (current: {row[1]}): ") or row[1]
        row[2] = input(f"Enter new last name (current: {row[2]}): ") or row[2]
        row[3] = input(f"Enter new hire date (current: {row[3]}): ") or row[3]
        row[4] = input(f"Enter new department (current: {row[4]}): ") or row[4]
        row[5] = input(f"Enter new performance (current: {row[5]}): ") or row[5]
        row[6] = input(f"Enter new salary (current: {row[6]}): ") or row[6]
        print("Employee updated successfully!")
    else:
        print("Invalid row number!")

# Salary Calculations
def salary_calculations(data):
    if len(data) <= 1:
        print("No employee data available for salary calculations.")
        return

    updated_data = [data[0]]  # Keep the header row
    for row in data[1:]:
        try:
            performance = int(row[3])
            salary = float(row[4])
            hire_date = datetime.strptime(row[1], "%Y-%m-%d")
            years_of_service = (datetime.now() - hire_date).days // 365

            # Calculate salary increase
            if performance >= 4:
                increase_percentage = 0.15
            elif performance >= 2:
                increase_percentage = 0.10
            else:
                increase_percentage = 0.05

            # Additional bonus for departments or years of service
            if years_of_service >= 5:
                increase_percentage += 0.05

            updated_salary = salary * (1 + increase_percentage)
            row[4] = f"{updated_salary:.2f}"  # Update salary in the row
            updated_data.append(row)

        except ValueError:
            print(f"Skipping invalid row: {row}")

    # Save the updated data to a new CSV file
    save_data(updated_data, UPDATED_FILE_NAME)
    print(f"Updated salaries saved to {UPDATED_FILE_NAME}.")

# Main menu
def main():
    data = load_data()
    while True:
        print("\nEmployee Management System")
        print("1. Display Employee Data")
        print("2. Add Employee")
        print("3. Edit Employee")
        print("4. Remove Employee")
        print("5. Salary Calculations")
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
            salary_calculations(data)
        elif choice == "6":
            save_data(data)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    main()
