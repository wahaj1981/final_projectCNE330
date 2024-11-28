import csv
from datetime import datetime

# File paths
employees_file = r'C:\Users\Wahaj\Documents\GitHub\final_projectCNE330\employees.csv'
UPDATED_employees_file = r'C:\Users\Wahaj\Documents\GitHub\final_projectCNE330\updated_employees.csv'

# Load data from the original CSV file
def load_data():
    try:
        with open(employees_file, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"File {employees_file} not found. Creating a new file.")
        data = [["ID", "First Name", "Last Name", "Hire Year (YYYY)", "Department", "Performance", "Salary"]]
        save_data(data)
        return data

# Load updated data from the new CSV file
def load_updated_data():
    try:
        with open(UPDATED_employees_file, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Updated file {UPDATED_employees_file} not found.")
        return []

# Save data to a CSV file
def save_data(data, file_name=employees_file):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Display employee data
def display_data(data):
    print("\nEmployee Data:")
    for row in data:
        print(", ".join(row))
    print()

# Add a new employee
def add_employee(data):
    employee_id = input("Enter employee ID: ").strip()
    first_name = input("Enter employee first name: ").strip()
    last_name = input("Enter employee last name: ").strip()
    hire_year = input("Enter hire year (YYYY): ").strip()
    department = input("Enter department: ").strip()
    performance = input("Enter performance score (1-5): ").strip()
    salary = input("Enter salary: ").strip()

    data.append([employee_id, first_name, last_name, hire_year, department, performance, salary])
    save_data(data)  # Save changes to the original file
    print("Employee added successfully!")

# Remove an employee
def remove_employee(data):
    display_data(data)
    employee_id = input("Enter the Employee ID to remove: ").strip()
    for index, record in enumerate(data[1:], start=1):
        if record[0] == employee_id:
            removed = data.pop(index)
            save_data(data)
            print(f"Employee {removed[0]} removed successfully!")
            return
    print("Employee ID not found!")

# Perform salary calculations
def salary_calculations(data):
    if len(data) <= 1:
        print("No employee data available for salary calculations.")
        return

    updated_data = [data[0] + ["New Salary", "Salary Increase Percentage"]]
    for row in data[1:]:
        try:
            performance = int(row[5])
            salary = float(row[6])
            hire_year = int(row[3])
            years_of_service = datetime.now().year - hire_year

            increase_percentage = 0.15 if performance == 5 else 0.10 if performance == 4 else 0.05 if performance == 3 else 0.0

            if years_of_service >= 5:
                increase_percentage += 0.05

            updated_salary = salary * (1 + increase_percentage)
            salary_increase_percentage = increase_percentage * 100

            updated_row = row + [f"{updated_salary:.2f}", f"{salary_increase_percentage:.2f}%"]
            updated_data.append(updated_row)
        except (ValueError, IndexError) as e:
            print(f"Error processing row {row}: {e}")
            continue

    save_data(updated_data, UPDATED_employees_file)
    print("Updated salaries and percentage increases saved.")

    # Print the blue comment explanation
    print("\033[94m")  # Start blue text
    print("Salary Increase Calculation Details:")
    print("- Performance Score (1-5):")
    print("  * 5 : 15% salary increase.", "  * 4: 10% salary increase.", "  * 3 : 5% salary increase.", "  * 2-1 : 0% salary increase.")
    print("- Years of Service:")
    print("  * If the employee has 5 or more years of service, an additional 5% increase is added.")
    print("\033[0m")  # Reset text color to default

# Main menu
def main():
    data = load_data()
    while True:
        print("\033[38;5;220m")  # Start gold text
        print("\nEmployee Management System")
        print("1. Display Employee Data")
        print("2. Add Employee")
        print("3. Remove Employee")
        print("4. Salary Calculations")
        print("5. Display Updated Employee Data","  *** After salary increase, the update for all the options above will be applied to the new employee's file.")
        print("6. Exit")
        print("\033[0m")  # Reset text color to default


        # Red color for prompt
        choice = input("\033[91mEnter your choice: \033[0m")  # Red color for prompt

        if choice == "1":
            display_data(data)
        elif choice == "2":
            add_employee(data)
        elif choice == "3":
            remove_employee(data)
        elif choice == "4":
            salary_calculations(data)
        elif choice == "5":
            updated_data = load_updated_data()
            if updated_data:
                display_data(updated_data)
        elif choice == "6":
            save_data(data)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    main()
