from time import time
start_time = time()

print("::::::::::Process::::::::::")
###############################

# with open('employees.txt', 'r') as file:
#      print(file.read())
     
     # def nlogn_sort(arr):
     #      return sorted(arr)  # Python's built-in sort is N*log(N)

     # Read lines into list and sort them
     # with open('employees.txt', 'r') as file:
     #      lines = file.readlines()
     #      sorted_lines = nlogn_sort(lines)
          
     # Extract age and create tuples of (age, line)
     # employee_data = []
     # for line in lines:
     #      parts = line.strip().split(',')  
     #      # Assuming comma-separated values
     #      if len(parts) >= 2:  
     #           # Make sure there's an age field
     #           try:
     #                age = int(parts[1])  
     #                # Assuming age is the second field
     #                employee_data.append((age, line))
     #           except ValueError:
     #                continue

     # Sort by age
     # sorted_employees = sorted(employee_data, key=lambda x: x[0])

     # print("\nEmployees sorted by age:")
     # for _, line in sorted_employees:
     #      print(line.strip())
          
     # Get employee name from user input
     # search_name = input("Enter employee name to search: ").strip().lower()

     # # Search for employee
     # found = False
     # for line in lines:
     #      if search_name in line.lower():
     #           print("Found employee:")
     #           print(line.strip())
     #           found = True
     #           break

     # if not found:
     #      print("Employee not found")
     
def find_max(data):
     biggest = data[0]
     for val in data:
          if val > biggest:
               print(f"Found : {val} > {biggest}")
               biggest = val
               # print(f"Biggest so far is {biggest}")
     return biggest

data = [3, 5, 1, 9, 2, 67, 23, 88, 45, 12, 91, 34, 78, 50]

print("The Biggest Number is ",find_max(data))

###############################

end_time = time()
elapsed_time = end_time - start_time
print(":::::::::::Times:::::::::::")
print(f"This programs used : {elapsed_time:.5f} seconds")