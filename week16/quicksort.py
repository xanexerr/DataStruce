# แบ่งเป็น patition เลือกเลขมากตัวนึงเป็น pivot value
# กรณีที่แย่ที่สุดคือ O(n^2) คือ pivotมีค่่าน้อยที่สุดหรือมากที่สุด
# กรณีที่ดีที่สุดคือ O(nlogn) คือ pivot แบ่งได้พอดดี

# แบ่งเป็น LEG L=less than E=equal to G=greater than


def quick(S):
    if len(S) <= 1:
        return S
    else:
        pivot = S[-1]
        L = [x for x in S[1:] if x < pivot]
        E = [x for x in S[1:] if x == pivot]
        G = [x for x in S[1:] if x > pivot]
        return quick(L) + [pivot] + E + quick(G)
print(quick([3, 6, 8, 10, 1, 2, 1]))

def qucickmaxtomin(S):
    if len(S) <= 1:
        return S
    else:
        pivot = S[0]
        L = [x for x in S[1:] if x < pivot]
        E = [x for x in S[1:] if x == pivot]
        G = [x for x in S[1:] if x > pivot]
        return qucickmaxtomin(G) + [pivot] + E + qucickmaxtomin(L)
print(qucickmaxtomin([3, 6, 8, 10, 1, 2, 1]))
#  ทำให้เรียงจากมากไปน้อย โดยการสลับตำแหน่งของ L และ G 

# def quicksort(S):
#     if len(S) <= 1:
#         return S
#     else:
#         pivot = S[0]
#         L = []
#         G = []
#         for x in S[1:]:
#             if x < pivot:
#                 L.append(x)
#             else:
#                 G.append(x)
#         return quicksort(L) + [pivot] + quicksort(G)
# print(quick([3, 6, 8, 10, 1, 2, 1]))