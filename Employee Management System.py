import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost", user="root", passwd = "tiger",database ="s1")
mycur = mycon.cursor()

def displayall():
    mycur.execute("select * from employee")
    data = mycur.fetchall()
    count = mycur.rowcount
    print("Total number of rows retrieved in resultset:", count)
    for row in data:
        print(row)

def displayone(eid):
    mycur.execute("select * from employee where E_ID = %s",%(eid))
    data = mycur.fetchone()
    print(data)

def menu():
    print("\n *** Menu ***")
    print("1. Display records")
    print("2. Delete records")
    print("3. Update records")

def deleterec():
    print("\n *** Delete ROW FROM TABLE ***")
    print("\n Records of employee table before deletion:")
    displayall()
    eid = int(input("\n Enter employee id whose record you want to delete::"))
    data1 = (eid,)
    delquery = "DELETE FROM employee WHERE E_ID= %s"
    mycur.execute(delquery, data1)
    count = mycur.rowcount
    if count == 0:
        print("Sorry! employee id not found in the table")
    else:
        mycon.commit()
        print("Rows affefcted::", mycur.rowcount)
        print("\n Records of employee table after deletion:")
        displayall()

def updaterec():
    print("\n **** UPDATE ROW INTO TABLE ***")
    print("\n Records of employee table before updation: ")
    eid = int(input("\n Enter employee id whose records you want to UPDATE::"))
    query = "SELECT * from employee where E_ID=%s"%(eid)
    mycur.execute(query)
    result = mycur.fetchall()
    if mycur.rowcount == 0:
        print("Sorry! Employee with ",eid,"not found")
    else:
        for row in result:
            print(row)
        print("You can change only Department and Salary")
        dept = input("Enter new department, leave blank if you do not want to change::")
        if dept == " ":
            dept = str(row[3])
            print(dept)
        try:
            sal = int(input("Enter new salary, leave blank if you do not want to change:: "))
        except:
            sal = row[5]
            updatequery = "UPDATE employee SET department=%s, salary =%s WHERE E_ID=%s"%(dept,sal,eid)
            mycur.execute(updatequery)
            mycon.commit()
            print("Rows affefcted::", mycur.rowcount)
            print("\n Contents of updated record:")
            displayone(eid)

opt = "y"
while (opt == "y"):
    menu()
    choice = int(input("\n Enter your choice::"))
    if (choice == 1):
        displayall()
    if (choice == 2):
        deleterec()
    if (choice == 3):
        updaterec()
    opt = input("Do you want to continue::")

mycon.close()