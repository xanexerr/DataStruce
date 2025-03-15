# Martix ตัวอย่าง
binary_matrix1 = [
        [1,1,0,0,1],
        [0,1,1,0,0],
        [0,0,0,0,1],
        [1,0,0,1,1],
        [1,0,1,1,1]
]

binary_matrix2 = [
        [1,1,0,1,1],
        [0,1,1,0,0],
        [0,0,0,1,1],
        [1,0,0,1,1],
        [1,0,1,1,1]
]

binary_matrix3 = [
        [1,1,0,1,1],
        [0,1,0,0,0],
        [0,0,0,1,0],
        [1,0,0,1,0],
        [1,1,1,0,1]
]


def LargeRegion(matrix):
        hot_spot = []
        for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                        if matrix[row][col] == 1:
                                hot_spot.append((row,col))
# สร้าง list ของ hot_spot
# loop ทุกตำแหน่งใน matrix ถ้าเจอ 1 ให้เพิ่มตำแหน่งนั้นใน hot_spot

        connected_regions = []
        visited = set()
        # สร้าง list ของ connected_regions 
        # สร้าง set ของ visited ให้เป็น set ไว้เก็บตำแหน่งที่เคยเข้าไปแล้วกันการเข้าไปซ้ำ
        
        # recursive function หาไฟที่เชื่อมกัน
        def explore_region(spot, region):
                if spot in visited:
                        return
                row, col = spot
                # ถ้าตำแหน่งนี้เคยอยู่ใน visited แล้วให้ return ค่าว่างออกไปจะได้หยุด recursive
                
                # print(f"{spot}", end=' ')
                visited.add(spot)
                region.add(spot)
                # เก็บตำแหน่งนี้ไว้ใน visited และ region

                 # วนลูปเช็ค 8 ทิศรอบๆ จุดปัจจุบัน (row, col)
                for r in range(max(0, row-1), min(len(matrix), row+2)):
                        # max(0, row-1) ป้องกันไม่ให้ index ติดลบ  
                        # min(len(matrix), row+2) ป้องกันไม่ให้ index เกินขอบล่างของ matrix
                        
                        for c in range(max(0, col-1), min(len(matrix[0]), col+2)):
                                #  max(0, col-1) ป้องกันไม่ให้ index ติดลบ  
                                #  min(len(matrix[0]), col+2) ป้องกันไม่ให้ index เกินขอบขวาของ matrix
                                if matrix[r][c] == 1 and (r,c) not in visited:
                                        # ถ้าจุด `(r, c)` เป็น 1 และยังไม่ถูกเยี่ยมชม → เรียก explore_region ซ้ำ (Recursion)
                                        # กำหนดให้ spot เป็น (r,c) ต้องใส่วงเล็บเพราะ parameter เป็น tuple
                                        spot = (r,c)
                                        explore_region((spot), region)
                # วน loop ตำแหน่งที่เป็นไปได้ทั้งหมด และเรียกฟังก์ชัน explore_region ใหม่
                # ถ้าเจอตำแหน่งที่เป็น 1 และไม่ได้เข้าไปแล้วให้เรียกฟังก์ชัน explore_region ใหม่
                
                
        # print(f"Hot Spot : {hot_spot}")
        for spot in hot_spot:
                if spot not in visited:
                        region = set()
                        explore_region(spot, region)
                        connected_regions.append(region)
        # วน loop ตำแหน่งที่เป็น hot_spot ทั้งหมด และเรียกฟังก์ชัน explore_region
        # ถ้าเจอมีการ return จะเก็บ region นั้นไว้ใน connected_regions
        
        largest_size = 0
        largest_region = None
        for region in connected_regions:
                if len(region) > largest_size:
                        largest_size = len(region)
                        largest_region = region
        return largest_size , largest_region
        # สร้าง largest_size ไว้เก็บขนาดของ region ที่ใหญ่ที่สุด
        # สร้าง largest_region ไว้เก็บ region ที่ใหญ่ที่สุด
        # วน loop ทุก region ที่เก็บไว้ใน connected_regions 
        # ถ้าขนาดของ region มากกว่า largest_size 
        # ให้เปลี่ยนค่าของ largest_size และ largest_region ใหม่
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
        return region_spot 



size1, region1 = LargeRegion(binary_matrix1)
size2, region2 = LargeRegion(binary_matrix2)
size3, region3 = LargeRegion(binary_matrix3)
find1 = FindRegion(binary_matrix1)
find2 = FindRegion(binary_matrix2)
find3 = FindRegion(binary_matrix3)

print(f"Matrix 1 Find {find1} Legion,Largest Legions -> Size: {size1}")
print(f"Matrix 2 Find {find2} Legion,Largest Legions -> Size: {size2}")
print(f"Matrix 3 Find {find3} Legion,Largest Legions -> Size: {size3}")

