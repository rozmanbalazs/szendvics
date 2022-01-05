import os
from tkinter import *
from tkinter import ttk

root = Tk()

color_get = StringVar()

def setcolor():
    color = color_get.get()
    
    with open("config.txt", "w") as file:
        file.write(color)

    os.system('python ikt project.py')


root.geometry("300x400")
root.title("szendvics számoló")
root.resizable(False,False)
root.config(bg="black")

Label(root, text="Select Theme", font=("roboto",25), fg="white", bg="black").pack(pady=50)

colorselector = ttk.Combobox(root, textvariable=color_get, state="readonly")
colorselector["values"] = ["white", "blue", "green", "yellow", "red", "cyan"]
colorselector.current(0)
colorselector.pack()

button_1 = Button(root, command=setcolor, text="Apply", bg="lime", activebackground="green", font=("roboto",25))
button_1.pack(pady=60)

root.mainloop()
