employees = {}
flag = True
while flag:  # While loop initially set to True to mimic do-while loop
    choice = int(input("Enter the choice: "))
    if choice == 1:
        employee_name = input("Enter the employee name: ")
        salary = input("Enter the salary: ")
        employees[employee_name] = salary  # Creating dictionary from inputs
    elif choice == 2:
        print(employees)
    elif choice == 3:
        employee_name = input("Enter the employee name to remove: ")
        employees.pop(employee_name)  # Removes element by key given by user
    elif choice == 4:
        employee_name = input("Enter the employee's name: ")
        salary = input("Enter the salary: ")
        employees.update({employee_name: salary})  # Adding with update method
    elif choice == 5:
        print("Employees names: ", *employees.keys(), sep=',')
        # Prints only keys, unpacked using *
        print("Employees salaries: ", *employees.values(), sep=',')
        # Prints only values, unpacked using *
    else:
        flag = False
