import sqlite
import ContactContract
import Crypt
import time
from os import system, name
import os
import tkinter as tk
from threading import *

def clear():
    _ = system('clear')


# Load the database, if it exists.
database_exists = True

try:
	self.con=sqlite3.connect("/app/db/contact_contract.db")
except:
	database_exists = False

# Collect user data.
user_name = input("Enter your name: ")
if !database_exists:
	user_email = input("Enter your email: ")
contract_name = input("Enter the name of the contract: ")

# Load contract key.
try:
	keyFile = open('./.' + contract_name + '/contract.key', "r")
	contract_key = keyFile.read()
	keyFile.close()
except:
	contract_key = Crypt.newContract(contract_name)
	
# Use the key to encrypt user and contract name.
user_name_digest = Crypt.encrypt(user_name, user_name, contract_name)
contract_name_digest = Crypt.encrypt(user_name, contract_name, contract_name)

# Instantiate the client.
contract = ContactContract.ContactContract(user_name_digest, contract_name_digest)

# Create the main window.
window=tk.Tk()

# Create the contract name label frame.
contract_name_frame=tk.Frame()
contract_name=tk.Label(text=contract.contract_name,master=contract_name_frame,width=40)
contract_name.pack()

# Create the chatlog frame.
chatlog_frame=tk.Frame()
message_box=tk.Listbox(master=chatlog_frame, width=40, height=20, justify="left", bg="white",)
message_box.pack()

# Create the textentry frame.
textentry_frame=tk.Frame()
textentry=tk.Entry(master=textentry_frame,width=30)
textentry.pack()

# Define the function to collect text from the entry widget.
def send_message():
    contract.addMessage(Crypt.encrypt(textentry.get()))
    textentry.delete(0, tk.END)

# Create the send message button.
send_button=tk.Button(text="Send Message",master=textentry_frame,width=10,command=send_message)
send_button.pack()

# Cram all the frames into the window.
contract_name_frame.pack(side=tk.TOP)
chatlog_frame.pack()
textentry_frame.pack(side=tk.BOTTOM)

running=True

# Define the function to fill the message log widget with the messages and to validate new users.
def show_messages():
    c=0;
    d=0;
    while running:
        if c!=len(contract.showMessages()):
            message_box.insert(c, for x in contract.showMessages()[c]: Crypt.decrypt(user_name, x, contract_name))
            c+=1
        elif d!=len(contract.getUserList()):
            ContactContract.validateUser(user_name, Crypt.addNewUser(contract.showUserKeys()[d], contract_name))
        else:
            time.sleep(2)

# Begin updating the message log.
message_update=Thread(target=show_messages)
message_update.start()

window.mainloop()

running=False
