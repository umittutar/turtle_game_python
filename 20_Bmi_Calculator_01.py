import tkinter as tk
from binascii import *

myWin = tk.Tk()
# myWin.resizable(300, 200)
myWin.configure(background="light blue",
                borderwidth=1, relief="solid",
                highlightbackground="#fff",
                highlightcolor="#fff")
myWin.title("BMI Calculator")

myH= myWin.winfo_screenheight()
myW= myWin.winfo_screenwidth()
mySH = 400
mySW = 400

x_pos = int((myW / 2) - (mySW/2))
y_pos = int((myH / 2) - (mySH/2))

myWin.geometry(f"{mySH}x{mySW}+{x_pos}+{y_pos}")
myWin.configure(padx=10, pady=10)
myLabelWeight = tk.Label(myWin, text="*** Enter Your Weight (kg) ***",
                   font=("Arial", 15, "bold"),
                   bg="brown",
                   borderwidth=2, relief="raised",
                   fg="azure",padx=1, pady=5)
myLabelWeight.pack(pady=5)
myEntryWeight = tk.Entry(myWin, font=("Arial", 15, "bold"),
                   width=10, bg="lightgray",
                   fg="black",
                   takefocus=True, justify="center")
myEntryWeight.pack()
myEntryWeight.focus()
myLabelHeight = tk.Label(myWin, text="*** Enter Your Height (cm) ***",
                         font=("Arial", 15, "bold"),
                         bg="red",
                         borderwidth=2, relief="raised",
                         fg="azure",padx=1, pady=5)
myLabelHeight.pack(pady=5)
myEntryHeight = tk.Entry(myWin, font=("Arial", 15, "bold"),
                         width=10, bg="lightgray",
                          fg="black",justify="center")
myEntryHeight.pack(pady=5)
myLabelResultTitle = tk.Label(myWin, text="*** BMI Result ***",
                         font=("Arial", 15, "bold"),
                         bg="blue",
                         borderwidth=1, relief="raised",
                         fg="azure",padx=1, pady=5,
                         justify="center")
myLabelResultTitle.pack(pady=5)

myLabelResultText = tk.Label(myWin, text="*** 0 ***",justify="center",font=("Arial", 10, "bold"))
myLabelResultText.pack(pady=5)
myLabelExplanation = tk.Label(myWin, text="*** Explanation ***")
myLabelExplanation.pack(pady=5)
def calculate():
    myResultWeight = myEntryWeight.get()
    myResultHeight = myEntryHeight.get()
    if myResultWeight.isnumeric() and myResultHeight.isnumeric():

        bmi = int(myResultWeight)/(int(myResultHeight)/100*int(myResultHeight)/100)
        floatBmi = round(bmi,2)
        myLabelResultText.config(text=floatBmi)
        if floatBmi < 18.5:
            myLabelExplanation.config(text="*** Your BMI Status : 'Zayıf (Underweight)' ***")
        if floatBmi > 18.5 and floatBmi <= 24.9:
            myLabelExplanation.config(text="*** Your BMI Status : 'Normal' ***")
        if floatBmi > 25 and floatBmi <= 29.9:
            myLabelExplanation.config(text="*** Your BMI Status : 'Fazla Kilolu (Overweight)' ***")
        if floatBmi > 30 and floatBmi <= 39.9:
            myLabelExplanation.config(text="*** Your BMI Status : 'Obez' ***")
        if floatBmi > 40:
            myLabelExplanation.config(text="*** Your BMI Status : 'Morbid Obez' ***")

        # myEntryHeight.focus()
    else:
        myLabelExplanation.config(text="Please Only Use Number")
        myEntryWeight.focus()

myResultButton = tk.Button(myWin, text="Calculate", font=("Arial", 12, "bold"),
                           borderwidth=2, relief="raised",
                           fg="black",
                           bg="darkgray",
                           command=calculate)
myResultButton.pack(pady=11)
myLabelCopyright = tk.Label(myWin, text="Ümit Tutar (C) 2025", font=("Arial", 10), bg="dark blue",fg="white")
myLabelCopyright.pack(pady=10)





myWin.mainloop()