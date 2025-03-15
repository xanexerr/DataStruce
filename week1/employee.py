while True:
     try:
          print(":::::Menu:::::")
          print("1. View All employees record")
          print("2. Add a new employee record")
          print("3. Search for an employee by name")
          print("4. Update employee record")
          print("5. Exit")
          number = int(input())
          if 1 <= number <= 5:
               if number == 1:
                    print(":::::View All employees record:::::")
                    
                    with open('employees.txt', 'r') as file:
                         all_emp = file.readlines()
                         
                    for employee in all_emp:
                         print("Name :", employee.split(',')[0],", Age :", employee.split(',')[1],", Major :", employee.split(',')[2].strip())
                    file.close()
                    
               if number == 2:
                    print(":::::Add a new record:::::")
                    thisrecord = input("Enter Name,Age,Major : ")
                    thisrecord = thisrecord + "\n"
                    
                    with open('employees.txt', 'a') as file:
                         file.write(thisrecord)
                    file.close()
                    
               if number == 3:
                    print(":::::Search for an employee by name:::::")
                    search = input("Enter Name : ")
                    with open('employees.txt', 'r') as file:
                         all_emp = file.readlines()
                         
                    found = False
                    for employee in all_emp:
                         if search.lower() in employee.split(',')[0].lower():
                              print("Name :", employee.split(',')[0],", Age :", employee.split(',')[1],", Major :", employee.split(',')[2].strip())
                              found = True
                    if not found:
                         print(search, "Not found")
                              
                    file.close()
                    
               if number == 4:
                    def update_employee():
                         print(":::::Update employee record:::::")
                         search = input("Enter Name : ")
                         all_emp = read_employees()
                         
                         found = False
                         updated_employee = None
                         
                         for employee in all_emp:
                              if search.lower() in employee.split(',')[0].lower():
                                   found = True
                                   display_employee(employee)
                                   updated_employee = get_new_employee_info()
                                   all_emp.remove(employee)
                                   all_emp.append(updated_employee)
                                   break
                         
                         if not found:
                              print(search, "Not found")
                         else:
                              write_employees(all_emp)
                              
                    def read_employees():
                         with open('employees.txt', 'r') as file:
                              return file.readlines()

                    def write_employees(employees):
                         with open('employees.txt', 'w') as file:
                              for employee in employees:
                                   file.write(employee)

                    def display_employee(employee):
                         print("Name:", employee.split(',')[0], 
                                ", Age:", employee.split(',')[1], 
                                ", Major:", employee.split(',')[2].strip())

                    def get_new_employee_info():
                         update = input("Enter Name,Age,Major : ")
                         return update + "\n"

                    if number == 4:
                         update_employee()
                    
               if number == 5:
                    exit()
                    
          else:
               print("Invalid. Please Input Again : ")
     except ValueError:
          print("Invalid. Please Input Again : ")
          