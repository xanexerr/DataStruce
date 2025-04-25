# ทำ hash table ทำไม
# Hash table เป็น data structure ที่ใช้ในการเก็บข้อมูลในรูปแบบ key-value pairs
# โดยใช้ hash function ในการแปลง key ให้เป็น index ใน array ที่ใช้เก็บข้อมูล
# ทำให้สามารถเข้าถึงข้อมูลได้อย่างรวดเร็ว โดยไม่ต้องค้นหาทั้งหมดใน array
# Hash table มีประสิทธิภาพในการค้นหาข้อมูลที่ดีกว่า data structure อื่น ๆ เช่น linked list หรือ array
# โดยเฉพาะเมื่อข้อมูลมีขนาดใหญ่

# สร้าง hash table สำหรับเก็บข้อมูลนักศึกษา
students = {
    "1001": "Alice",
    "1002": "Bob",
    "1003": "Charlie",
    "1004": "David",
    "1005": "Eve",
    "1006": "Frank",
    "1007": "Grace",
    "1008": "Hannah",
    "1009": "Ivy",
}
# Map จะเป็นการเก็บข้อมูลในรูปแบบ key-value pairs
# เรียงข้อมูลใน hash table โดยใช้ key เป็นรหัสนักศึกษา
# และเรียงข้อมูลในลำดับที่ต้องการ
# ค้นหานักศึกษาใน hash table โดยใช้รหัสนักศึกษา

# ถ้าไม่กระจายจะชนกัน
# ต้องแก้ปัญหาการชนกัน (collision) โดยการใช้การจัดการการชนกัน (collision resolution)
# เช่น การใช้ chaining หรือ open addressing 
# 1.liner probing, ค่าจะไปอยู้ที่ index ถัดไป
# 2.quadratic probing, ค่าจะไปอยู่ที่ index ถัดไปของ index ที่ชนกัน โดยเอา index ที่ชนกันเป็น 2 เท่า
# 3.double hashing ค่าจะไปอยู่

# open addressing: การใช้การค้นหาที่มีความซับซ้อนมากขึ้น โดยการใช้ฟังก์ชัน hash ที่แตกต่างกันในแต่ละขั้นตอน
# chaining: การใช้การเก็บข้อมูลในรูปแบบ linked list ในแต่ละ index ของ hash table
# การใช้ hash table ในการเก็บข้อมูลนักศึกษา
# ฟังก์ชันค้นหานักศึกษาโดยใช้รหัสนักศึกษา



# ฟังก์ชันค้นหานักศึกษาที่รหัสลงท้ายด้วย 01-09
def find_students_by_suffix(suffix_range):
    result = []
    for suffix in suffix_range:
        key = f"100{suffix}"  # สมมติว่ารหัสนักศึกษาเริ่มต้นด้วย 100
        if key in students:
            result.append(students[key])
    return result

# เรียกใช้งานฟังก์ชัน
suffix_range = range(1, 10)  # 01-09
found_students = find_students_by_suffix(suffix_range)
print(found_students)

