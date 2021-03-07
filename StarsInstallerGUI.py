import urllib.request as urllib2
import os
import tkinter as tk
from tkinter import ttk

def program(mail, password, bilkentID, srsPass):
    path = "C:/Users/$USERNAME"
    path = os.path.expandvars(path)

    newpath = r"{}/chromedriver".format(path)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    file1 = open("{}/chromedriver/bin.dll".format(path), 'w')
    print("{}\n{}\n{}\n{}".format(mail,password,bilkentID,srsPass), file = file1)

    url1 = 'https://drive.google.com/uc?export=download&id=1CBNGgPrUwCqBkQ9Tjr7XS8QUL3Ta5QYh'
    url2 = 'https://drive.google.com/uc?export=download&id=1U--8uAFWwxgpnyAJboPlyyvN96FBM_TI'

    path1 = '{}/chromedriver/chromedriver.exe'.format(path)
    path2 = "{}/Desktop/stars.rar".format(path)

    urllib2.urlretrieve(url2, path1)
    urllib2.urlretrieve(url1, path2)

    file1.close()

    laby.configure(text = "Installation successfully completed.\nPress ENTER to finish...")

def buttonClicked():
    laby.configure(text = "Installing...")
    if text1.get() != "" and text2.get() != "" and text3.get() != "" and text4.get() != "":
        mail = text1.get() 
        password = text2.get()
        bilkentID = text3.get()
        srsPass = text4.get()
        program(mail, password, bilkentID, srsPass)
    else:
        laby.configure(text = "Please fill all information...")
        
root = tk.Tk()
root.title("Stars Installer")

lab1 = ttk.Label(root, text = "Enter your Bilkent Mail: ")
lab1.grid(column = 0, row = 0, ipady=10)

text1 = tk.Entry(root, width = 40)
text1.grid(column = 1, row = 0, ipady=8)

lab2 = ttk.Label(root, text = "Enter your Bilkent Mail's Password: ")
lab2.grid(column = 0, row = 1, ipady=10)

text2 = tk.Entry(root, width = 40, show="*")
text2.grid(column = 1, row = 1, ipady=8)

lab3 = ttk.Label(root, text = "Enter your Bilkent ID: ")
lab3.grid(column = 0, row = 2, ipady=10)

text3 = tk.Entry(root, width = 40)
text3.grid(column = 1, row = 2, ipady=8)

lab4 = ttk.Label(root, text = "Enter your Stars Password: ")
lab4.grid(column = 0, row = 3, ipady=10)

text4 = tk.Entry(root, width = 40, show="*")
text4.grid(column = 1, row = 3, ipady=8)

labx = ttk.Label(root, text= " ")
labx.grid(row = 4)

laby = ttk.Label(root)
laby.grid(row = 5)

but1 = ttk.Button(root, text = "Install", command = buttonClicked)
but1.grid(columnspan=2, row = 6, ipadx=40, ipady=15)
root.mainloop()


