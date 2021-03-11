import subprocess

passs = input("enter mysql password :: --> ")

# logging into the server

subprocess.call("bash", shell=True)
subprocess.call("sudo mysql", shell=True)
subprocess.call(passs, shell=True)

# Create table
subprocess.call("create database employee", shell=True)
subprocess.call("use employee", shell=True)
subprocess.call("create table employee(E_ID int, Name varchar(10), Salary int, DOJ date, Gender char(1));", shell=True)

# Data to feed
emp_id = [117001, 117002, 117003, 117004 , 117005, 117006, 117007, 117008]
emp_name = ["\"Neel\"", "\"Ronika\"", "\"Saili\"", "\"Samiula\"", "\"Dilgit\"", "\"Hamlata\"", "\"Kalpash\"", "\"Humaira\""]
emp_salary = ["67000", "60000", "55000", "65000", "66000", "40000", "45000", "45000"]
emp_DOF = ["21-3-2003", "3-7-2004", "18-10-2005", "16-6-2010", "10-4-2003", "15-12-2015", "01-2-2012", "11-1-2011"]
emp_gender = ["\"M\"", "\"F\"", "\"M\"", "\"F\"", "\"M\"", "\"F\"", "\"M\"", "\"F\""]

counter = 0

# filler loop
while counter < 9 :
    print(emp_id[counter], emp_name[counter], emp_salary[counter], emp_DOF[counter], emp_gender[counter])
    query = ("insert into employee values(", emp_id[counter], emp_name[counter], emp_salary[counter], emp_DOF[counter], emp_gender[counter],");")
    subprocess.call(query , shell=True)
    counter = counter + 1


print("***  Task completed successfully ***")