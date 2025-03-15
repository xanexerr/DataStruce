from linkedtree import LinkedTree

class CompanyHierarchy(LinkedTree):
    def display_hierarchy(self, p, level=0): 
        print("  " * level + p.element()) 
        for child in self.children(p): 
            self.display_hierarchy(child, level + 1)

company = CompanyHierarchy()
ceo = company.add_child(None, "CEO")

manager1 = company.add_child(ceo, "Manager 1")
manager2 = company.add_child(ceo, "Manager 2")

employee1 = company.add_child(manager1, "Employee 1")
employee2 = company.add_child(manager1, "Employee 2")
employee3 = company.add_child(manager2, "Employee 3")

# แสดงโครงสร้างองค์กร
print("Company Hierarchy:")
company.display_hierarchy(company.root())

# ค้นหาพนักงาน
search_name = "Employee 2"
found_employee = company.find_employee_by_name(company.root(), search_name)

if found_employee:
    print(f"\n{search_name} found in the company structure!")
else:
    print(f"\n{search_name} not found!")
