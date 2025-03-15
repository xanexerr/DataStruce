from circular import CircularLinkList

class Task:
    def __init__(self):
        self.cll = CircularLinkList()
        
    def add_first(self, data):
        self.cll.add_first(data)
        print(f"(High Priority) Added : {data}")
        
    def add_last(self, data):
        self.cll.add_last(data)
        print(f"(Low  Priority) Added : {data} ")
        
    def complete(self, key):
        self.cll.remove_node(key)
        print(f"Task Completed : {key}")
        
    def traverse_forward(self):
        
        return self.cll.traverse_forward()  

    def traverse_backward(self):
        return self.cll.traverse_backward()  
        
    def __str__(self):
        return "\n".join(self.traverse_forward()) if self.cll.head else "Empty List"

# Test Case
t = Task()
print("\n<<<<<Task>>>>>")
print(t) 

print("\n<<<<<Task Added>>>>>")
t.add_first("Submit Assignment")
t.add_first("Submit Project")
t.add_first("Prepare Presentation")
t.add_last("Read Book")
t.add_last("Buy Groceries")
t.add_first("Plan Meeting")
t.add_last("Exercise")
t.add_first("Review Code")
t.add_last("Cook Dinner")
t.add_first("Write Report")

print("\n<<<<<Task>>>>>")
print(t) 

print("\n<<<<<Completed Task>>>>>")
t.complete("Submit Project")
t.complete("Buy Groceries")
t.complete("Exercise")

print("\n<<<<<Task>>>>>")
print(t) 
# print(t.traverse_forward()) 

