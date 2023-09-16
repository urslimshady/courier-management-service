import os
import pickle
import tkinter as tk
from tkinter import Label, Button, Entry, messagebox

def addItem():
    itemNo = int(item_no_entry.get())
    tId = tracking_id_entry.get()
    desc = product_description_entry.get()
    wt = weight_entry.get()
    dadr = destination_address_entry.get()
    sadr = sender_address_entry.get()
    status = "Packed"
    cost = int(cost_entry.get())

    cData = [itemNo, tId, desc, wt, dadr, sadr, status, cost]
    with open("courier.dat", "ab") as f:
        pickle.dump(cData, f)

    messagebox.showinfo("Success", "Details added successfully")

def display():
    display_window = tk.Toplevel(root)
    display_window.title("Courier Details")
    
    f = open("courier.dat", "rb")
    try:
        while True:
            cData = pickle.load(f)
            details_label = Label(display_window, text=cData[2] + " weights " + str(cData[3]) + " will be delivered to " + cData[4], fg="blue")
            details_label.pack()
    except EOFError:
        f.close()

def search():
    td = search_tracking_id_entry.get()
    found = False
    f = open("courier.dat", "rb")
    try:
        while True:
            cData = pickle.load(f)
            if cData[1] == td:
                found = True
                messagebox.showinfo("Courier Found", cData[2] + " weights " + str(cData[3]) + " will be delivered to " + cData[4])
                break
    except EOFError:
        f.close()
    
    if not found:
        messagebox.showinfo("Courier Not Found", "No courier found with the given Tracking Id. Please check your tracking ID")

def remove():
    td = remove_tracking_id_entry.get()
    found = False
    f = open("courier.dat", "rb")
    g = open("temp.dat", "wb")
    try:
        while True:
            cdata = pickle.load(f)
            if cdata[1] == td:
                found = True
                messagebox.showinfo("Courier Found", cdata[2] + " weights " + str(cdata[3]) + " will be delivered to " + cdata[4])
            else:
                pickle.dump(cdata, g)
    except EOFError:
        if not found:
            messagebox.showinfo("Courier Not Found", "No Courier Found with Such a Tracking Id")
        else:
            messagebox.showinfo("Courier Deleted", "Courier Deleted Successfully")
        
        f.close()
        g.close()
        os.remove("courier.dat")
        os.rename("temp.dat", "courier.dat")

def login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    
    Label(login_window, text="^" * 50, fg="green").pack()
    Label(login_window, text="\t ABC Courier Services ", fg="green").pack()
    Label(login_window, text="^" * 50, fg="green").pack()
    
    Label(login_window, text="Press 1 - Login as Admin", fg="blue").pack()
    Label(login_window, text="Press 2 - Login as Member", fg="blue").pack()
    
    ch = Entry(login_window)
    ch.pack()
    
    def check_login():
        choice = ch.get()
        if choice == "1":
            password = input("Enter password ")
            if password == "1221":
                usrname = input("Enter the New User name : ")
                pwd = input("Enter the new Password : ")
                with open("users.dat", "ab") as f:
                    pickle.dump([usrname, pwd], f)
                messagebox.showinfo("User Added", "User Added Successfully")
        elif choice == "2":
            usrname = input("Enter the User name : ")
            pwd = input("Enter the Password : ")
            f = open("users.dat", "rb")
            found = False
            try:
                while True:
                    d = pickle.load(f)
                    if d[0] == usrname and d[1] == pwd:
                        found = True
                        messagebox.showinfo("Access Granted", "Access Granted")
                        break
            except EOFError:
                if not found:
                    messagebox.showinfo("Invalid Credentials", "Invalid User Name or Password")
                f.close()

    login_button = Button(login_window, text="Login", command=check_login, fg="green")
    login_button.pack()

root = tk.Tk()
root.title("Courier Management System")
root.geometry("600x400")  # Set window size

# Create labels and entry widgets for adding courier
item_no_label = Label(root, text="Item No:", fg="blue")
item_no_label.pack()
item_no_entry = Entry(root)
item_no_entry.pack()

tracking_id_label = Label(root, text="Tracking ID:", fg="blue")
tracking_id_label.pack()
tracking_id_entry = Entry(root)
tracking_id_entry.pack()

product_description_label = Label(root, text="Product Description:", fg="blue")
product_description_label.pack()
product_description_entry = Entry(root)
product_description_entry.pack()

weight_label = Label(root, text="Weight (Courier):", fg="blue")
weight_label.pack()
weight_entry = Entry(root)
weight_entry.pack()

destination_address_label = Label(root, text="Destination Address:", fg="blue")
destination_address_label.pack()
destination_address_entry = Entry(root)
destination_address_entry.pack()

sender_address_label = Label(root, text="Sender Address:", fg="blue")
sender_address_label.pack()
sender_address_entry = Entry(root)
sender_address_entry.pack()

cost_label = Label(root, text="Shipping Cost:", fg="blue")
cost_label.pack()
cost_entry = Entry(root)
cost_entry.pack()

add_button = Button(root, text="Add Item", command=addItem, fg="green")
add_button.pack()

# Create buttons for display, search, remove, and login
display_button = Button(root, text="Display Couriers", command=display, fg="green")
display_button.pack()

search_label = Label(root, text="Enter Tracking ID to Search:", fg="blue")
search_label.pack()
search_tracking_id_entry = Entry(root)
search_tracking_id_entry.pack()
search_button = Button(root, text="Search", command=search, fg="green")
search_button.pack()

remove_label = Label(root, text="Enter Tracking ID to Remove:", fg="blue")
remove_label.pack()
remove_tracking_id_entry = Entry(root)
remove_tracking_id_entry.pack()
remove_button = Button(root, text="Remove", command=remove, fg="green")
remove_button.pack()

login_button = Button(root, text="Login", command=login, fg="green")
login_button.pack()

root.mainloop()
