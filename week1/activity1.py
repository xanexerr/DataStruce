my_list = [ 1 , 10 , 6 , 7 , 8 , 9 ,4 ,5 ,2 ,3,11]
print(my_list)

my_list.sort()
print(my_list)

list2 =  my_list[len(my_list)//2:] + my_list[:len(my_list)//2]
print(list2)


student_tuple = ("Fong", "Sand", "Jeff", "Toon")
print("Original tuple:", student_tuple)

try:
     student_tuple[0] = "New" 
except TypeError as e:
     print("tuple แก้ไม่ได้ :", e)

print("tuple ผลลัพธ์ :", student_tuple)  

student_dict = {
     "Fong": 80,
     "Sand": 75,
     "Jeff": 60,
}

print("ข้อมูลดั้งเดิม :", student_dict)

student_dict["Toon"]=71
print("เพิ่มแล้ว :", student_dict)

student_dict["Fong"] = 79
print("อัพเดทแล้ว :", student_dict)

del student_dict["Sand"]
print("ลบแล้ว :", student_dict)

