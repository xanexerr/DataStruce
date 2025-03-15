# Natthapumin Klammat
# 6787028
# Section 1

def count_region(matrix, x, y):
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 1: Check base conditions
        if x < 0 or y < 0 or x >= rows or y >= cols or matrix[x][y] != 1:
                return 0
         # Step 2: Mark as visited
        matrix[x][y] = -1  
        
        # Step 3: : Count this cell + explore all 8 directions
        size = 1
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]:
                size += count_region(matrix, x + dx, y + dy)
        return size

def largest_region(matrix):
        max_region = 0
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                        if matrix[i][j] == 1:
                                max_region = max(max_region, count_region(matrix, i, j))
        return max_region


# find element of region
def FindRegion(matrix):
        hot_spot = []
        for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                        if matrix[row][col] == 1:
                                hot_spot.append((row,col))

        connected_regions = []
        visited = set()

        def explore_region(spot, region):
                if spot in visited:
                        return
                row, col = spot
                visited.add(spot)
                region.add(spot)

                for r in range(max(0, row-1), min(len(matrix), row+2)):
                        for c in range(max(0, col-1), min(len(matrix[0]), col+2)):
                                if matrix[r][c] == 1 and (r,c) not in visited:
                                        explore_region((r,c), region)

        for spot in hot_spot:
                if spot not in visited:
                        region = set()
                        explore_region(spot, region)
                        connected_regions.append(region)
        region_spot = len(connected_regions)
        
        region_element = []
        for e in connected_regions:
                region_element.append(e)
        return region_spot , region_element

binary_matrix = [
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 0, 1]
]

binary_matrix2 = [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]]

find1,e1 = FindRegion(binary_matrix)
find2,e2 = FindRegion(binary_matrix2)
print("This Matrix Found : ",find1)
print("Spots Found :")
for i in range(len(e1)):
        print("Spot",i+1,":",e1[i])
print("Largest Region Size:", largest_region(binary_matrix),"\n")
print("This Matrix Found : ",find2)
print("Spots Found :")
for i in range(len(e2)):
        print("Spot",i+1,":",e2[i])
print("Largest Region Size:", largest_region(binary_matrix2),"\n")

# Discussion Questions
# 1. If you change the matrix so that all elements are 1, the function will return the size of the entire matrix as the largest region.\
# Answer: ใช่ จะได้ขนาดของ matrix ทั้งหมดเป็น region ที่ใหญ่ที่สุด

# 2. To modify the function to return all connected regions instead of just the largest one, you can collect the sizes of all regions in a list and return that list.
# Answer: ใช่ สามารถเก็บขนาดของ region ทั้งหมดไว้ใน list แล้ว return ออกมาได้
