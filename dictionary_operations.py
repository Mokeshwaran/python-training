print(dir(dict()))

employees = {}

flag = True
while flag:
    choice = int(input("Enter the choice: "))
    if choice == 1:
        employee_name = input("Enter the employee name: ")
        salary = input("Enter the salary: ")
        employees[employee_name] = salary
    elif choice == 2:
        print(employees)
    elif choice == 3:
        employee_name = input("Enter the employee name to remove: ")
        employees.pop(employee_name)
    elif choice == 4:
        employee_name = input("Enter the employee's name: ")
        salary = input("Enter the salary: ")
        employees.update({employee_name: salary})
    elif choice == 5:
        print("Employees names: ", *employees.keys(), sep=',')
        print("Employees salaries: ", *employees.values(), sep=',')
    else:
        flag = False
