import os
import pickle

def addItem():
    itemNo = int(input("Enter the unique item no : "))
    tId = input("Enter the tracking id : ")
    desc = input("Enter the product description : ")
    wt = input("Enter the weight of the Courier : ")
    dadr = input("Enter the destination address : ")
    sadr = input("Enter the sender address : ")
    status = "Packed"
    cost = int(input("Enter the cost of Shipping : "))

    cData = [itemNo, tId, desc, wt, dadr, sadr, status, cost]
    f = open("courier.dat", "ab")

    pickle.dump(cData, f)

    print("Details added successfully")
    f.close()

def display():
    f = open("courier.dat", "rb")
    try:
        while True:
            cData = pickle.load(f)
            print(cData[2] + " weights " + str(cData[3] + " will be delivered to " + cData[4]))
    except:
        f.close()
        print("-" * 40)

def search():
    td = input("enter tracking id to be searched : ")
    found = False
    f = open("courier.dat", "rb")
    try:
        while True:
            cData = pickle.load(f)
            if cData[1] == td:
                print("Found, Here are the details ")
                found = True
                print(cData[2] + " weights " + str(cData[3]) + " will be delivered to " + cData[4])
                break
    except:
        if found == False:
            print(" No courier found with the given Tracking Id, Please check your tracking ID ")
        f.close()
        print("-" * 40)

def remove():
    td = input("Enter tracking id to be removed : ")
    found = False
    f = open("courier.dat","rb")
    g = open("temp.dat","wb")
    try:
        while True:
            cdata = pickle.load(f)
            if cdata[1] == td:
                print("Found, Here are the details ")
                found = True
                print(cdata[2] + " weights " + str(cdata[3]) + " will be delivered to " + cdata[4])
            else:
                pickle.dump(cdata,g)
    except:
        if found == False:
            print("No Courier Found with Such a Tracking Id ")
        else:
            print("Courier Deleted Successfully")
        f.close()
        g.close()
        print("-" * 40)
        os.remove("courier.dat")
        os.rename("temp.dat","courier.dat")

def login():
    print("^" * 50)
    print("\t ABC Courier Services ")
    print("^" * 50)
    print("Press 1 - Login as Admin")
    print("Press 2 - Login as Member ")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        password = input("Enter password ")
        if password == "1221":
            usrname = input("Enter the New User name : ")
            pwd = input("Enter the new Password : ")
            f = open("users.dat","ab")
            pickle.dump([usrname,pwd],f)
            f.close()
            print("^" * 50)
            print("User Added Successfully ")
            print("^" * 50)
    elif ch == 2:
        usrname = input("Enter the User name : ")
        pwd = input("Enter the Password : ")
        f = open("users.dat","rb")
        found = False
        try:
            while True:
                d = pickle.load(f)
                if d[0] == usrname and d[1] == pwd:
                    print("Access Granted ")
                    found = True
                    break
        except:
            if found == False:
                print("Invalid User Name or Password ")
            f.close()
        return found
