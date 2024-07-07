from tkinter import *

def calculate():
    if wentr.get().isdigit() and hentr.get().isdigit():
        weight = int(wentr.get())
        height = int(hentr.get()) / 100
        bmi = weight / height ** 2
        condition =  "overweight" if bmi > 25 else "underweight" if bmi < 18.5 else "normal"
        bmilbl.config(text=f"BMI : \t{bmi} \t {condition}", fg= "red" if condition !='normal' else "#00ff00")

        remedy = f"add about {abs(22 * height ** 2 - weight)} Kg's" if condition == 'underweight' else \
        "continue eating healthy brother" if condition == 'normal' else \
        f"cut about {abs(22 * height ** 2 - weight)} Kg's" 

        remedylbl = Label(window, bg="black", fg="orange", text= f"Remedy    : {remedy}", font=23, width=40)
        remedylbl.place(x=150, y=250)
    else:
        remedylbl = Label(window, bg="black", fg="RED", text= "INVALID ENTRY !!!", font=33, width=40)
        remedylbl.place(x=150, y=250)

window = Tk()
window.geometry("600x600")
window.config(bg='black')
window.title("BMI Calculator")

bmilbl = Label(window, text="BMI : ", font=24, bg="black", fg="#00ff00")
bmilbl.place(x=150, y=100)

wLbl = Label(window, bg="black", fg="#00ff00", text="Weight : ", font=43)
wLbl.place(x=150, y=150)

wentr = Entry(window, fg="black", bg="#999999", font=24)
wentr.place(x=250, y=150)

wLbl1 = Label(window, bg="black", fg="#00ff00", text="Kg", font=43)
wLbl1.place(x=450, y=150)

hLbl = Label(window, bg="black", fg="#00ff00", text="Height : ", font=43)
hLbl.place(x=150, y=200)

hentr = Entry(window, fg="black", bg="#999999", font=4)
hentr.place(x=250, y=200)

hLbl1 = Label(window, bg="black", fg="#00ff00", text="Cm", font=43)
hLbl1.place(x=450, y=200)

calcbt = Button(window, text="calculate" ,activebackground='#00ff00', bg="white", command=calculate)
calcbt.place(x=280, y=300)

window.mainloop()