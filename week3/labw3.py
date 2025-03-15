import time
import random
import matplotlib.pyplot as plt

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

def binary_search(arr,target):
        low,high=0, len(arr)-1
        while low<=high:
                mid=(low+high)//2
                
                if arr[mid]==target:
                        return mid
                elif arr[mid]<target:
                        low=mid+1
                else:
                        high=mid-1
        return -1

def measure_time(func,arr,target):
        start_time=time.perf_counter()
        func(arr,target)
        end_time=time.perf_counter()
        return end_time - start_time

input_sizes=[100,500,1000,5000,10000]
linear_times=[]
binary_times=[]

for size in input_sizes:
        arr = [random.randint(1,100000) for _ in range(size)]
        target=random.choice(arr)
        sorted_arr=sorted(arr)

        linear_times.append(measure_time(linear_search,arr,target))
        binary_times.append(measure_time(binary_search,sorted_arr,target))

print(linear_times)
print(binary_times)

# Plotting Methods

plt.figure(figsize=(10,6))
plt.plot(input_sizes,linear_times,label='Linear Search',marker='o')
plt.plot(input_sizes,binary_times,label='Binary Search',marker='s')
plt.title("Runtime Comparison: Linear Search vs Binary Search")
plt.xlabel("Input Size(n)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid()
plt.show()