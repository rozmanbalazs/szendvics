from tkinter import *
from tkinter import ttk
import time

aktivator = ''


root = Tk()

color_get = StringVar()

def setcolor():
    color = color_get.get()
    
    with open("config.txt", "w") as file:
        file.write(color)


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







if aktivator!= None:
    root = Tk()

    root.geometry("300x400")
    root.title("szendvics számoló")
    root.resizable(False,False)
    root.config(bg="black")

    calc = 0
    calc_pez = 0

    rantott = 0
    szalami = 0
    hamburger = 0



    szendo = IntVar()


    def logic():
        global calc, calc_pez, rantott, szalami, hamburger

        szendvicsek = szendo.get()

        if szendvicsek == 0:
            szamlalo.config(text="Válassz szendvicset")

        elif szendvicsek == 1:
            calc += 1
            calc_pez += 400
            rantott += 1
            valasz_final = "rántotthús - {}".format(rantott)
            valaszto.config(text=valasz_final)
            szamlalo.config(text=calc)
            finalpez = "{} HUF".format(calc_pez)
            szamlalo_pez.config(text=finalpez)

        elif szendvicsek == 2:
            calc += 1
            calc_pez += 250
            szalami += 1
            valasz_final = "szalámis - {}".format(szalami)
            valaszto1.config(text=valasz_final)
            szamlalo.config(text=calc)
            finalpez = "{} HUF".format(calc_pez)
            szamlalo_pez.config(text=finalpez)    
    
        elif szendvicsek == 3:
            calc += 1
            calc_pez += 300
            hamburger += 1
            valasz_final = "hamburgir - {}".format(hamburger)
            valaszto2.config(text=valasz_final)
            szamlalo.config(text=calc)
            finalpez = "{} HUF".format(calc_pez)
            szamlalo_pez.config(text=finalpez)    

    szamlalo = Label(root, text="0", font=("roboto",25), fg="white", bg="black")
    szamlalo.pack(pady=50)

    gomb_hozzaad = Button(root, command=logic, text="+1 Szendvics", font=("roboto",20), fg="black", bg="lime", activebackground="green")
    gomb_hozzaad.pack(pady=20)

    valaszto = Radiobutton(root, text="rántotthúsos", variable=szendo, value=1, fg="lime", bg="black", activebackground="red")
    valaszto.pack()

    valaszto1 = Radiobutton(root, text="szalámis", variable=szendo, value=2, fg="lime", bg="black", activebackground="red")
    valaszto1.pack()

    valaszto2 = Radiobutton(root, text="hamburgir", variable=szendo, value=3, fg="lime", bg="black", activebackground="red")
    valaszto2.pack()

    szamlalo_pez = Label(root, text="0 HUF", font=("roboto",15), fg="lime", bg="black")
    szamlalo_pez.pack(pady=10)

    root.mainloop()
