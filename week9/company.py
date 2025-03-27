from linkedtree import LinkedTree

class CompanyHierarchy(LinkedTree):
    def display_hierarchy(self, p, level=0): 
        print("  " * level + p.element()) 
        for child in self.children(p): 
            self.display_hierarchy(child, level + 1)
            
    def find_emp(self, p, name,level=0):
        if level == 0:
            position = "CEO"
        elif level == 1:
            position = "Manager"
        elif level == 2:
            position = "Supervisor"
        elif level == 3:
            position = "Employee"

            
        if p.element() == name:
            print(f"{name} Found! at position {position}") 
            return p


        for child in self.children(p):
            result = self.find_emp(child, name , level + 1)
            if result is not None:
                return result

        if p == self.root():  
            print(name,"Not found in the Company!")
        
        return None


company = CompanyHierarchy()
ceo = company.add_child(None, "Alex")

manager1 = company.add_child(ceo, "Suphitcha")
manager2 = company.add_child(ceo, "Jeff")

supervisor1 = company.add_child(manager1, "William")
supervisor2 = company.add_child(manager2, "Sophia")
employee1 = company.add_child(supervisor1, "John")
employee2 = company.add_child(supervisor1, "Emma")
employee3 = company.add_child(supervisor2, "Michael")
employee4 = company.add_child(supervisor1, "Olivia")
employee5 = company.add_child(supervisor1, "James")
employee6 = company.add_child(supervisor2, "Isabella")

# แสดงโครงสร้างองค์กร
print("Company Hierarchy:")
company.display_hierarchy(company.root())


print("\nEmployee Searches:")
company.find_emp(company.root(), "Jeff")
company.find_emp(company.root(), "Sophia")
company.find_emp(company.root(), "Ball")
