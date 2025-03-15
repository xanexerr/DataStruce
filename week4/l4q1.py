def walking(arr,i=0,j=0,list=None):
    if list is None:
        list = []
    n = len(arr)
    if arr[i][j]==1:
        list.append((i,j))
        arr[i][j] = '*'
        
    if i+1 < n and arr[i+1][j] == 1:
        return walking(arr,i+1,j,list)
    if j+1 < n and arr[i][j+1] == 1 :
        return walking(arr,i,j+1,list)

    if arr[n-1][n-1] == '*':
        print("Solution Path: ",list)
        print("Maze with Solution Path:")
        for x in range(len(arr)):
            for y in range(len(arr)):
                print(arr[x][y],end = ' ')
            print()
    else:
        print("No solutions exists for the maze.")
    return ""

caseA = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]

caseB = [
    [1,1,0,0],
    [0,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]

caseC = [
    [1,1,1,0],
    [0,1,1,1],
    [0,0,1,1],
    [1,0,0,1]
]

caseD = [
    [1,1,1,0],
    [0,1,1,0],
    [0,1,0,1],
    [1,1,0,1]
]

print(walking(caseA,0,0))
print(walking(caseB,0,0))
print(walking(caseC,0,0))
print(walking(caseD,0,0))