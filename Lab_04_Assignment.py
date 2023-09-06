class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        matching_employees = [emp for emp in self.employees if emp.age == target_age]
        return matching_employees

    def search_by_name(self, target_name):
        matching_employees = [emp for emp in self.employees if emp.name == target_name]
        return matching_employees

    def search_by_salary(self, comparison_operator, target_salary):
        valid_operators = ['>', '<', '>=', '<=']
        if comparison_operator not in valid_operators:
            return []

        if comparison_operator == '>':
            matching_employees = [emp for emp in self.employees if emp.salary > target_salary]
        elif comparison_operator == '<':
            matching_employees = [emp for emp in self.employees if emp.salary < target_salary]
        elif comparison_operator == '>=':
            matching_employees = [emp for emp in self.employees if emp.salary >= target_salary]
        else:
            matching_employees = [emp for emp in self.employees if emp.salary <= target_salary]

        return matching_employees

def main():
    database = EmployeeDatabase()

    # Add employees to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, >=, <=)")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        target_age = int(input("Enter the age to search for: "))
        result = database.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search for: ")
        result = database.search_by_name(target_name)
    elif choice == 3:
        comparison_operator = input("Enter the comparison operator (> < >= <=): ")
        target_salary = int(input("Enter the salary to compare: "))
        result = database.search_by_salary(comparison_operator, target_salary)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No matching records found.")
    else:
        print("Matching Employees:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()
