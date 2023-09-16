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

