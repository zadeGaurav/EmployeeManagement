from emp import Emp
from os import path 

class EmpMgnt:
    def addEmp(self, e):                                                  
        fp = open("Empinfo.txt", "a")
        fp.write(str(e))
        fp.write("\n")
        fp.close()                  

    def showAllemp(self):
        try:
            fp = open("Empinfo.txt", "r")
        except:
            print("File not found: ")
        else:
            data = fp.read()
            print("These are the employes")
            print(data)
            fp.close()
 
    def searchEmpById(self, id):
        if path.exists ("Empinfo.txt"):
            with open("Empinfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    data = line.split(",")
                    if (data[0] == str(id)):               # str --DATATYPE
                        print("Record found.", line.strip())   # no need of strip
                        flag = True
                        break
            if (flag == False):
                print("Record not found.")
        else:
            print("File not found.")

    def searchEmpByName(self, name):
        if path.exists("Empinfo.txt"):
            with open("Empinfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    if (name in line):
                        flag = True
                        print("Record found.\n", line.strip())
                    
                    
            if (flag == False):
                print("Record not found.")       
        else: 
            print("File not found.")

    def editEmpByid(self, id):
        empList = []
        Flag = False
        if (path.exists("Empinfo.txt")):
            with open ("Empinfo.txt", "r") as fp:  
                for line in fp:
                    data = line.split(",")
                    if (data[0] == str(id)):
                        print("Record found", line.strip())
                        Flag = True
                        ans = input("Do you want to edit emp name?(y/n): ")
                        if (ans.lower() == "y"):
                            data[1] = input("Enter new emp name: ")
                        ans = input("Do you want to edit the salary?(y/n): ")
                        if (ans.lower() == "y"):
                            data[2] = input("Enter new emp salary: ")
                        line = ",".join(data)
                        line += "\n"
                    empList.append(line)
            if (Flag == True):
                with open("Empinfo.txt", "w") as fp:
                    for emp in empList:
                        fp.write(emp)
                        print("Empinfo.txt has been updated.")
            else:
                print("Record not found.")
        else:
            print("File not exist")

    def deleteEmpById(self, id):
        empList = []
        flag = False
        if (path.exists("Empinfo.txt")):
            with open("Empinfo.txt", "r")as fp:
                for line in fp:
                    data = line.split(",")
                    if (data[0] == id):
                        flag = True
                        continue     
                    empList.append(line)
            if (flag == True):
                with open("Empinfo.txt", "w") as fp:
                    for emp in empList:
                        fp.write(emp)
                        print("Emp id has been deleted.")
            else:
                print("Id not found.")
        else: 
            print("File not found.")






    