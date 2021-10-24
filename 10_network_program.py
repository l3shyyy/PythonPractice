import ipaddress
import scapy
import socket
import tkinter as tk
from tkinter import filedialog, messagebox, Text
import os

hostname = socket.gethostname()
fqdn_hostname = socket.getfqdn(hostname)
ip_addr = socket.gethostbyname(hostname)
domain = fqdn_hostname.split('.', 1)[1]

def print_networkinfo():
	msg = messagebox.showinfo("Information","Your hostname is: " + hostname + '\n\n' + 
	  "Your FQDN is: " + fqdn_hostname +'\n\n'+ 
	  "Your IP address is: " + ip_addr +'\n\n'+ 
	  "Your domain is: " +domain )

root = tk.Tk()

canvas = tk.Canvas(root, height=350, width=450, bg="#187bcd")
canvas.pack()

frame = tk.Frame(root, bg="#2a9df4")
frame.place(relwidth=0.7, relheight=0.7, relx=0.1, rely=0.1)

testButton1 = tk.Button(root, text="testButton",padx=10, pady=5, fg="white", bg="#263D42", command=print_networkinfo)
testButton1.pack()


root.mainloop()








