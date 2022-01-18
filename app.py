import ContactContract
import time
from os import system, name
import tkinter as tk
#from tkinter import ttk
from threading import *

def clear():
    _ = system('clear')

'''

contract = ContactContract.ContactContract()

while True:
    clear()
    contract.showMessages()
    message = input("")
    contract.addMessage(message)
    clear()

'''

# Instantiate the client.
contract = ContactContract.ContactContract()

# Create the main window.
window=tk.Tk()

# Create the contract name label frame.
contract_name_frame=tk.Frame()
contract_name=tk.Label(text=contract.contract_name,master=contract_name_frame,width=40)
contract_name.pack()

# Create the chatlog frame.
chatlog_frame=tk.Frame()
#chatlog=tk.Label(text="Initializing.\n", master=chatlog_frame, width=40, height=50, justify="left", bg="white")
message_box=tk.Listbox(master=chatlog_frame, width=40, height=20, justify="left", bg="white",)
#message_box_scrollbar=tk.Scrollbar(window)
#message_box_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
message_box.pack()

# Create the textentry frame.
textentry_frame=tk.Frame()
textentry=tk.Entry(master=textentry_frame,width=30)
textentry.pack()

# Define the function to collect text from the entry widget.
def send_message():
    contract.addMessage(textentry.get())
    textentry.delete(0, tk.END)

# Create the send message button.
send_button=tk.Button(text="Send Message",master=textentry_frame,width=10,command=send_message)
send_button.pack()

# Cram all the frames into the window.
contract_name_frame.pack(side=tk.TOP)
chatlog_frame.pack()
textentry_frame.pack(side=tk.BOTTOM)

running=True

# Define the function to fill the message log widget with the messages.
def show_messages():
    c=0;
#    for message in contract.showMessages():
#        message_box.insert(c, message)
#        chatlog["text"]+=(message)
#        chatlog["text"]+="\n"
#        c+=1;
    while running:
        if c!=len(contract.showMessages()):
            message_box.insert(c, contract.showMessages()[c])
#            chatlog["text"]+=(contract.showMessages()[c])
#            chatlog["text"]+="\n"
            c+=1
        else:
            time.sleep(2)

# Begin updating the message log.
message_update=Thread(target=show_messages)
message_update.start()

#print(show_messages())

window.mainloop()

running=False
