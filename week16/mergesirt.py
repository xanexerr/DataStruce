# 85,24,63,45,17,37,69,51
# 85 24  | 63 45 | 

def merge(left, right, S):
    i = j = 0
    while i + j < len(S):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            S[i + j] = left[i]
            print(f"left[{i}] = {left[i]}", end=", ")
            i += 1
        else:
            S[i + j] = right[j]
            print(f"right[{j}] = {right[j]}", end=", ")
            j += 1
    print(f"result = {S}")

def merge_sort(S):
    print(f"merge_sort({S})")
    if len(S) < 2:
        return S
    
    mid = len(S) // 2
    left = merge_sort(S[:mid])
    right = merge_sort(S[mid:])

    result = [0] * len(S)
    merge(left, right, result)
    return result

print(merge_sort([85,24,63,45,17,37,69,51]))