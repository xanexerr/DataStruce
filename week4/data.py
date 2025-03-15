n = int(input())

def find_n(n):
     n1 = n // 2
     if n > n1:  # First check
          n2 = n1 // 2
          if n1 > n2:  # Second check
               n3 = n2 // 2
               if n2 > n3:  # Third check
                    if n3 == n:  # Check if result equals input
                         return n3
     return None

result = find_n(n)
if result is not None:
     print(result)
else:
     print("Not found")