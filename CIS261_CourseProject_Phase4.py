#Michael Dupuis CIS261 Course Project Phase 4

from datetime import datetime

def createUsers():
    print("Create users, passwords, and roles")
    userFile = open("Users.txt", "a+")
    while True:
        userName = getUserName()
        if (userName.upper() == "END"):
            break
        userPassword = getUserPassword()
        userRole = getUserRole()
        
        userDetails= userName + "|" + userPassword + "|" + userRole + "\n"
        userFile.write(userDetails)
        
    userFile.close()
    printuserinfo()

def getUserName():
    userName = input("Enter a username or 'End' to quit:  ")
    return userName

def getUserPassword():
    password = input("Enter a password:  ")
    return password

def getUserRole():
    userRole = input("Enter a role (Admin or User):  ")
    while True:
        if (userRole.upper() == "ADMIN" or userRole.upper() == "USER"):
            return userRole
        else:
            userRole = input("Enter a user role (Admin or User): ")
            
def printuserinfo():
    userFile = open("users.txt", "r")
    while True:
        userDetails = userFile.readline()
        if not userDetails:
            break
        userDetails = userDetails.replace("\n", "")
        userList = userDetails.split("|")
        userName = userList[0]
        userPassword = userList[1]
        userRole = userList [2]
        print("User Name: ", userName, "Password: ", userPassword, "Role: ", userRole)
        
def login():
    userFile = open("users.txt", "r")
    userList = []
    userName = input("Enter username: ")
    userPassword = input("Enter password: ")
    userRole = "None"
    while True:
        userDetails = userFile.readline()
        if not userDetails:
            return userRole, userName, userPassword
        userDetails = userDetails.replace("\n", "")
        
        userList = userDetails.split("|")
        if userName == userList[0] and userPassword == userList[1]:
            userRole = userList[2]
            return userRole, userName
        
    return userRole, userName

def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate
    
def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate:  "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    empFile = open("employees.txt", "r")
    while True:
        runDate = input("Enter start date for report (MM/DD/YYYY) or 'ALL' for all data")
        if (runDate.upper() == "ALL"):
            break
        try:
            runDate = datetime.strptime(runDate, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format. Try again: ")
            print()
            continue
        
    while True:
        empDetail = empFile.readline()
        if not empDetail:
            break
        empdetail = empDetail.replace("\n", "")
        empList = empDetail.split("|")
        fromdate = empList[0]
        if(str(runDate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < runDate):
                continue      
        endDate = empList[1]
        empName = empList[2]
        hours = float(empList[3])
        hourlyRate = float(empList[4])
        taxRate = float(empList[5])
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxRate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incometax
        totalNetPay += netpay
        
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        detailsPrinted = True
        
    if (detailsPrinted):
        printTotals(empTotals)
    else:
        print("no detailed information to print")

def printTotals(empTotals):
    print()
    print(f'Total Number of Employees: {empTotals["totEmp"]}')
    print(f'Total Hours of  Employees: {empTotals["totHours"]}')
    print(f'Total Gross Pay of Employees: {empTotals["totGross"]:,.2f}')
    print(f'Total Tax of Employees: {empTotals["totTax"]:,.1%}')
    print(f'Total Net Pay of Employees: {empTotals["totNet"]:,.2f}')
    
if __name__ == "__main__":
    createUsers()
    print()
    print("Data Entry")
    userRole, UserName = login()
    detailsPrinted = False
    empTotals = {}
    if (userRole.upper() == "NONE"):
        print(UserName, "is invalid. ")

    else:
        if (userRole.upper() == "ADMIN"):
            empFile = open("employees.txt", "a+")
            while True:
                empName = getEmpName()
                if (empName.upper() == "END"):
                    break
                fromDate, endDate = getDatesWorked()
                hours = getHoursWorked()
                hourlyrate = getHourlyRate()
                taxrate = getTaxRate()
                empDetails = fromDate + "|" + endDate + "|" + empName + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
                empFile.write(empDetails)
                
            empFile.close()
            
        printInfo(detailsPrinted)

