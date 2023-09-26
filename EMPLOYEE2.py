from collections import defaultdict
from ast import Break, Delete
from math import radians
from operator import index, or_
import datetime
from pickle import TRUE
from re import search
# from termios import OFDEL
from tkinter import CENTER, W
emp_name=[]
emp_id=[]
emp_joiningdate=[]
emp_department=[]
emp_salary=[]
# this is a range to enter a year of joining  of employee ,the year must enter  from range this list
range_of_year=range(2000,2022)
# this is a range to enter a month of joining  of employee ,the month must enter  from range this list
range_of_month=range(1,13)
# this is a range to enter a day of joining  of employee ,the day must enter  from range this list
range_of_day=range(1,31)
# the first employee create
name="Salm"
emp_name.append(name)
id=1
emp_id.append(id)
j=datetime.date(2020,3,6)
emp_joiningdate.append(j)
department="Front_end"
emp_department.append(department)
salary=2000
emp_salary.append(salary)
#the second employee create
name="Abdo"
emp_name.append(name)
id=2
emp_id.append(id)
j=datetime.date(2019,1,5)
emp_joiningdate.append(j)
department="Back_end"
emp_department.append(department)
salary=3000
emp_salary.append(salary)
# view employee by id
while True:
     try:
       view=input("Did you need to view  employee by id ,enter (yes) OR (no): ").lower().strip()
       while view!='yes' and view !='no':
        view=input("Try again if you need to view  employee by id ,enter (yes) OR (no):").lower().strip()
       if view=='yes':
        id=int(input("Enter the id of employee you need to view: "))
        while id not in emp_id:
          id=int(input("The id of employee you entered not found in the company,check the list of emp_id and enter correct id again: "))
        for n in emp_id:
         if id in emp_id:
          s=emp_id.index(n)
        print("Emp_ID: "+str(emp_id[s])+"  Name:  "+emp_name[s]+"  Joining Date:  "+str(emp_joiningdate[s])+"  Department:  "+emp_department[s]+"  Salary:  "+str(emp_salary[s]))
       break
     except:
          print("Erorr inpute......Try again")
 #create employee
while True:
     try:
          create=input("Did you need to create a new employees enter (yes) OR (no): ").lower().strip()
          while create !="yes" and create !="no":
               create=input(" Try again,are you need to create a new employee enter (yes) OR (no): ").lower().strip()
          if create=="yes":
            num =int(input("Enter the number of emloyees you want to create: "))
            for n in range(num):
             x = input("Enter  emp_name\n").lower().capitalize()

             emp_name.append(x)
             i = int (input("Enter  emp_id\n"))
             while i in emp_id:
               i = int (input("Please try again,id must be uique,enter another id: "))
             emp_id.append(i)
             yt=int(input("Enter year of joiningdate: "))
             for n in range_of_year:
               while yt not in range_of_year:
                    yt=int(input("Try again...Enter year of joiningdate the year must be from(2000) to (2021): "))

             mt=int(input("Enter month of joiningdate: "))
             for n in range_of_month:
                  while mt not in range_of_month:
                    mt=int(input("Try again...Enter month of joiningdate the month must be from(1) to (12): "))


             dt=int(input("Enter the day of joiningdate: "))
             for n in range_of_day:
                  while dt not in range_of_day:
                    dt=int(input("Try again...Enter day of joiningdate the day must be from (1) to (30): "))
             j=datetime.date(yt,mt,dt)
             emp_joiningdate.append(j)
             d = input("Enter  emp_department\n").lower().capitalize()
             while d !="Back_end" and d!="Front_end" :
                    d = input("Try again enter emp_department (front_end) or (back_end)\n").lower().capitalize()
             emp_department.append(d)
             s = int(input("Enter  emp_salary\n"))
             emp_salary.append(s)
             print("\t....You Create a new employee....")

          break
     except:
      print("Erorr inpute......Try again")
# #update employee
while True:
     try:
          update=input("Did you need update employee enter (yes) OR (NO): ").lower().strip()
          while update !="yes" and update !="no":
               update=input(" Try again,if you need to update  employee enter (yes) OR (no): ").lower().strip()
          if update=="yes":
           upd_emp_name=input("Enter the name of employee you need to upate\n").lower().capitalize()
           while upd_emp_name not in emp_name:
               upd_emp_name=input("The name of employee you entered not found in the company,check the list of emp_name and enter correct name\n").lower().strip()
           upd_emp_id =int(input("Enter the new ID of employee\n"))
           while upd_emp_id in emp_id:
               upd_emp_id = int (input("Please try again,id must be unique,enter another id: "))
           upd_yt=int(input("Enter the new year of joiningdate: "))
           for n in range_of_year:
               while upd_yt not in range_of_year:
                    upd_yt=int(input("Try again...enter year of joiningdate the year must be from(2000) to (2021) "))

           upd_mt=int(input("Enter the new month of joiningdate: "))
           for n in range_of_month:
                while upd_mt not in range_of_month:
                    upd_mt=int(input("Try again...Enter month of joiningdate the month must be from(1) to (12) "))

           upd_dt=int(input("Enter new day of joiningdate: " ))
           for n in range_of_day:
                while upd_dt not in range_of_day:
                     upd_dt=int(input("Try again...Enter day of joiningdate the day must be from(1) to (30) " ))

           upd_j=datetime.date(upd_yt,upd_mt,upd_dt)
          #  emp_joiningdate.append(j)
           upd_emp_department=input("Enter the new department of employee \n").lower().capitalize()
           while upd_emp_department !="Back_end" and upd_emp_department!="Front_end" :
                    upd_emp_department = input("Try again enter emp_department (front_end) or(back_end)\n").lower().capitalize()
           upd_emp_salary=int(input("Enter the new salary of employee \n"))
           for n in emp_name:
               if upd_emp_name in emp_name :
                    u=emp_name.index(upd_emp_name)
                    emp_id[u]=upd_emp_id
                    # upd_j=datetime.date(upd_yt,upd_mt,upd_dt)
                    emp_joiningdate[u]=upd_j
                    emp_department[u]=upd_emp_department
                    emp_salary[u]=upd_emp_salary
           print("\t....You Update employee....")

          break
     except:
      print("Erorr inpute......Try again")

# #delete employee
while True:
     try:
          delete=input("Did you need Delete employee enter (yes) OR (NO): ").lower().strip()
          while delete !="yes" and delete !="no":
               delete=input(" Try again,if you need to delete  employee enter (yes) OR (no): ").lower().strip()
          if delete=="yes":
           de_emp_name=str(input("Enter the name of employee you need to delete\n")).lower().capitalize()
           while de_emp_name not in emp_name:
               de_emp_name=input("The name of employee you entered not found in the company,check the list of emp_name and enter the correct name again\n").lower().strip()
           for n in emp_name:
               if de_emp_name in emp_name :
                    p=emp_name.index(de_emp_name)
                    emp_name.pop(p)
                    emp_id.pop(p)
                    emp_joiningdate.pop(p)
                    emp_department.pop(p)
                    emp_salary.pop(p)
           print("\t....You delete employee....")
          break
     except:
               print("Erorr inpute......Try again")

# #Search by emp_name or id
while True:
     try:
          search=input("Did you need to search about employee,enter (yes) or (no):  ").lower().strip()
          while search !="yes" and search !="no":
               search=input(" Try again,if you need to search about  employee enter (yes) OR (no): ").lower().strip()
          if search=="yes":
                    choose=input("Did you want to search by (ID) or (Name) ,enter (id) or (name) ").lower().strip()
                    while choose!="id" and choose!="name":
                     choose=input("Please try again enter (id) or (name) ").lower().strip()
                    if choose=="name":
                      search_name=input("Enter the name of employee you need to search\n").lower().capitalize()
                      while search_name not in emp_name:
                          search_name=input("The name of employee you enter not found in the company,check the list of emp_name and enter correct name again\n").lower().strip()
                      for n in emp_name:
                          if search_name in emp_name:
                            s=emp_name.index(search_name)
                      print("Emp_ID: "+str(emp_id[s])+"  Name:  "+search_name+"  Joining Date:  "+str(emp_joiningdate[s])+"  Department:  "+emp_department[s]+"  Salary:  "+str(emp_salary[s]))
                    if choose=="id":
                     search_id=int(input("Enter the id of employee you need to search\n"))
                     while search_id not in emp_id:
                         search_id=int(input("The id of employee you entered not found in the company,check the list of emp_id and enter correct id again\n"))
                     for n in emp_id:
                         if search_id in emp_id:
                          s=emp_id.index(search_id)
                     print("Emp_ID: "+str(emp_id[s])+"  Name:  "+emp_name[s]+"  Joining Date:  "+str(emp_joiningdate[s])+"  Department:  "+emp_department[s]+"  Salary:  "+str(emp_salary[s]))
          break
     except:
                print("Erorr inpute......Try again")

#   #now sorting

sort=input("Did you need to sort  employee,enter (yes) or (no):  ").lower().strip()
while sort !="yes" and sort !="no":
     sort=input(" Try again,if you need to sort  employees enter (yes) OR (no): ").lower().strip()
if sort=="yes":
 for n in emp_id:
   emp_id.sort()
 print("ID"+str(emp_id))


# #employees report
print("\t\t......NOW EMPLOYEES REPORT......\n")
for n in emp_name:
     if n in emp_name:
          s=emp_name.index(n)
          print("Emp_ID: "+str(emp_id[s])+"  Name:  "+emp_name[s]+"  Joining Date:  "+str(emp_joiningdate[s])+"  Department:  "+emp_department[s]+"  Salary:  "+str(emp_salary[s]))
print('#'*40)
#Group employees by department and get total salary
#use (defaultdict) to automatically initialize dictionary entries for each department.
total_salaries1 = defaultdict(int)
for department, salary in zip(emp_department, emp_salary):
     total_salaries1[department] += salary
print(dict(total_salaries1))
#Get first and last employee joined
print("The first employee joined is:  "+str(emp_name[0]))
print("The last employee joined is:  "+str(emp_name[-1]))
#Get employee with low and high salary
for n in emp_salary:
      s= max(emp_salary)
      ss= min(emp_salary)
      h=emp_salary.index(s)
      hh=emp_salary.index(ss)
print("The high salary is: "+str(s)+"  Name:  "+emp_name[h])
print("The low salary is: "+str(ss)+"  Name:  "+emp_name[hh])