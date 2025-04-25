
class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def insort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr
    
    
    # def sortfrommax(self):
    #     for i in range(1, len(self.arr)):
    #         key = self.arr[i]
    #         j = i - 1
    #         while j >= 0 and key > self.arr[j]:
    #             self.arr[j + 1] = self.arr[j]
    #             j -= 1
    #         self.arr[j + 1] = key
    #     return self.arr
A = InsertionSort([12, 11, 13, 5, 6])
print(A.insort())

B = InsertionSort([12, 11, 13, 5, 6])
# print(B.sortfrommax())