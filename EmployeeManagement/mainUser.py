from emp import Emp
from empMgnt import EmpMgnt

def userMenuMgmt():
    empMgnt = EmpMgnt()    
    ch = 0 
    while (ch != 5):
        print('''
        1. Add New Emp
        2. Show new Emp
        3. Search Emp by Id   
        4. Search Emp by Name
        5. Exit
        ''')
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            id = int(input("Enter emp id: "))
            nm = input("Enter emp name: ")
            sal = int(input("Enter emp salary: "))
            e = Emp(id, nm, sal)
            empMgnt.addEmp(e)
        elif (ch == 2):
            empMgnt.showAllemp()
        elif (ch == 3):
            id = int(input("Enter the id you want to search: "))
            empMgnt.searchEmpById(id)
        elif (ch == 4):
            nm = int(input("Enter the name you want search: "))
            empMgnt.searchEmpByName(nm)         
        elif (ch == 5):
            print("Thank you.")

'''if (__name__ == '__main__'):
    userMenuMgmt()'''