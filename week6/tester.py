from array_stack import ArrayStack

# Stack1 = ArrayStack()
# print(len(Stack1))
# print(Stack1.is_empty())
# print(Stack1.push(1))
# print(Stack1.push(2))
# print(Stack1)

# print(Stack1.top())
# print(Stack1.pop())
# print(Stack1)

# print("\nTesting ArrayStack")
# S = ArrayStack()
# S.push(5)
# S.push(3)
# print("Stack Len :",len(S))
# print(S.pop())
# print(S.top())
# print(S.is_empty())
# print("Stack Len :",len(S))

# Task
print("\nTesting Balanced Parentheses")
# expression = [
#         # "(a+b) * (c+d)",
#         # "({[a+b]}-c )",
#         # "((a+b)",
#         # "(a+b))",
#         # "{[()]}",
#         # "><"
# ]


# def is_balanced(expr):
#         S = ArrayStack()
#         left = "({[<"
#         right = ")}]>"
#         for char in expr:
#                 if char in left:
#                         S.push(char)
#                 elif char in ')}]':
#                         if S.is_empty():
#                                 return False
#                         #ถ้าเจอตัวปิด ต้องเช็คว่าตัวปิดนี้ตรงกับตัวเปิดที่อยู่ใน stack หรือไม่
#                         if right.index(char) != left.index(S.pop()):
#                                 return False
#         return S.is_empty()

# รอบสอง
# expression = [
#         "("
#         ]

expression = [
        "(a+b) * (c+d)", #true
        "({[a+b]}-c )", #true
        "((a+b)", #false
        "(a+b))", #false
        "{[()]}", #true
        
        # "(]", #false
        # "<>", #true  
        # "[{()}]",  #true
        # "{[}]", #false
        # "((()))", #true
        # ")()", #false
        # "({)}", #false
        # "<<>>", #true
        # "[[[]]", #false
        # "{{{}}", #true
        # "}{" #false
]
def is_balanced(expr):
        S = ArrayStack()  # สร้าง stack ว่าง
        lefts = "({[<"    # กำหนดวงเล็บเปิด
        rights = ")}]>"   # กำหนดวงเล็บปิดที่ตรงกับวงเล็บเปิด
        
        # for char in expr:
        #         if char in lefts:
        #                 S.push(char)
                        
        #         elif char in rights:
        #                 if S.is_empty():
        #                         return False
        #                 #ถ้าเจอตัวปิด ต้องเช็คว่าตัวปิดนี้ตรงกับตัวเปิดที่อยู่ใน stack หรือไม่
        #                 if rights.index(char) != lefts.index(S.pop()):
        #                         return False
        # return S.is_empty()
        
        for char in expr:
                if char in lefts:
                        S.push(char)
                elif char in rights:
                        if S.is_empty():
                                return False
                        charpop = S.pop()
                        if charpop == '(' and char != ')':
                                return False
                        elif charpop == '{' and char != '}':
                                return False
                        elif charpop == '[' and char != ']':
                                return False
                        elif charpop == '<' and char != '>':
                                return False
        return S.is_empty()
                        
                        

for expr in expression:
        print(f"Expression: {expr} --> Balanced: {is_balanced(expr)}")