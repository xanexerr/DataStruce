from node import Node
from node import DoubleLinkedList

node1 = Node(1)
sq1 = DoubleLinkedList()

class TrainManagementSystem(DoubleLinkedList):
        def add_train_beginning(self, train_number):
                self.add_first(train_number)

        def add_train_end(self, train_number):
                self.add_last(train_number)

        def remove_train(self, train_number):
                self.remove_node(train_number)

        def arival_forward(self):
                self.traverse_forward()

        def arival_backward(self):
                self.traverse_backward()

tms = TrainManagementSystem()
print("<<<<<Train>>>>>")
tms.add_first("Urgent(31)")
tms.add_first("Urgent(32)")
tms.add_last("Normal(128)")
tms.add_last("Normal(129)")
tms.add_last("Normal(130)")
tms.arival_forward()
tms.arival_backward()
print("<<<<<Remove Train>>>>>")
tms.remove_node("Normal(128)")
tms.arival_forward()
tms.arival_backward()

print("\nWelcome To Train Station")

def get_valid_user_input():
        print("1. Add Train")
        print("2. Remove Train")
        print("3. Display Train")
        print("4. Exit")
        user_input = input("\nWaiting for input: ....  ")
        
        while user_input not in ["1", "2", "3", "4"]:
                user_input = input("Wrong input again: ....  ")
        
        print()
        return user_input
        
user_input = get_valid_user_input()

if user_input == "4":
        total = 1
        for i in range(3):
                print("."*total,end=" ")
                total += i
        print("Good Bye")
                

while user_input != "4":
        if user_input == "1":
                print(":::::Add Train:::::")
                print("Select Train Type")
                print("1. Urgent")
                print("2. Normal")
                train_type = input("Enter Train Type: ")
                while train_type != "1" and train_type != "2":
                        train_type = input("Error! input again : ....  ")
                train_number = input("Enter Train Number: ")
                if train_type == "1":
                        while int(train_number) < 10 or int(train_number) > 100:
                                train_number = input("Error! input again : ....  ")
                        tms.add_train_beginning("Urgent("+train_number+")")
                elif train_type == "2":
                        while int(train_number) <= 100 or int(train_number) > 200:
                                train_number = input("Error! input again : ....  ")
                        tms.add_train_end("Normal("+train_number+")")
                print("Train Added Successfully")
                
                user_input = get_valid_user_input()
                
        if user_input == "2":
                print(":::::Remove Train:::::")
                tms.arival_forward
                train_number = input("Enter Train Number: ")
                tms.remove_train("Normal("+train_number+")")
                print("Train Removed Successfully")
                user_input = get_valid_user_input()
                
        if user_input == "3":
                print(":::::Display Train:::::")
                tms.arival_forward()
                tms.arival_backward()
                
                print()
                user_input = get_valid_user_input()
                
                