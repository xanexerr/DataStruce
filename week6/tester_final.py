from array_stack import ArrayStack

# LAB 6
# Natthapumin Klammat
# 6787028

expression = [
        "(a+b) * (c+d)", #true
        "({[a+b]}-c )", #true
        "((a+b)", #false
        "(a+b))", #false
        "{[()]}", #true
]

def is_balanced(expr):
        S = ArrayStack()  # สร้าง stack ว่าง
        lefts = "({[<"    # กำหนดวงเล็บเปิด
        rights = ")}]>"   # กำหนดวงเล็บปิดที่ตรงกับวงเล็บเปิด
        
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