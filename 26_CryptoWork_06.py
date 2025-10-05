import tkinter as tk
from tkinter import messagebox

myWindow = tk.Tk()
myWindow.geometry("300x500+530+50")
myWindow.resizable(False, True)
myWindow.title("X Files")
myWindow.configure(background="pink4")
myPhoto = tk.PhotoImage(file="../utWithCars_160_120.png")
labelForPhoto = tk.Label(image=myPhoto)
labelForPhoto.pack()
entryForTitleTextVariable = tk.StringVar()
entryForTitleTextVariable.set("")
entryForMasterKeyTextVariable = tk.StringVar()
entryForMasterKeyTextVariable.set("")


labelForTitle = tk.Label(myWindow,text="Enter Title",
                         font=("Arial", 15), bg="light blue", borderwidth=1, relief="solid",
                         fg="dark blue")
labelForTitle.pack(pady=2)
entryForTitle = tk.Entry(myWindow,width=20,
                      font=('Arial', 12, 'bold'),
                      justify="center",
                      bg="azure",
                      fg="black",
                      textvariable = entryForTitleTextVariable)
entryForTitle.pack()
labelForText = tk.Label(myWindow,text="Enter Your Text",
                        bg="light blue",  relief="solid",
                        fg="dark blue", font=('Arial', 12, 'bold'),
                        justify="center")
labelForText.pack(pady=2)
multilineText = tk.Text(myWindow,width=30,
                        height=8,
                        bg="light gray", borderwidth=1,
                        relief="solid",
                        fg="black", font=('Arial', 11,
                        ))
multilineText.pack(pady=5)

labelForMasterKeyText = tk.Label(myWindow,text="Enter Master Key",
                                  bg="light blue", borderwidth=1, relief="solid",
                                  fg="dark blue", font=('Arial', 12, 'bold'))
labelForMasterKeyText.pack(pady=5)
entryForMasterKeyText = tk.Entry(myWindow,width=20,
                                 font=('Arial', 12, 'bold'),
                                 justify="center",
                                 bg="azure",
                                 fg="black",
                                 textvariable = entryForMasterKeyTextVariable)
entryForMasterKeyText.pack(pady=2)
listOrdValues =[]


def saveAndEncrypt():
    global listOrdValues
    listKeyOrder =0
    titleName = str(entryForTitle.get())
    masterKeyText = str(entryForMasterKeyText.get())
    myText = (multilineText.get("1.0","end-1c"))

    print(f"titleName : {titleName}")
    print(f"masterKeyText : {masterKeyText}")
    print(f"myText : {myText}")

    if len(titleName) >0 and len(masterKeyText) >0 and len(myText) >0:
        listRaw = multilineText.get("1.0", tk.END)
        listFromRaw = listRaw[:-1]

        listKey= entryForMasterKeyText.get()
        listOrdValues = []
        listOrdValues.clear()
        listEncrypted = []
        for element in listFromRaw:
            print("******************************************************")
            print("element : {}".format(element))
            print("listkeyOrder : {}".format(listKeyOrder))
            print("lenListKey: {}".format(len(listKey)))
            listKeyElementValue = listKey[listKeyOrder%len(listKey)]
            print("listKeyElementValue : {}".format(listKeyElementValue))
            encryptOrdValue = ord(element) + ord(listKeyElementValue)
            print("ord(element) : {}".format(ord(element)))
            print("ord(listKeyElementValue) : {}".format(ord(listKeyElementValue)))
            listOrdValues.append(encryptOrdValue)
            encryptChrValue = chr(encryptOrdValue)
            print("encryptOrdValue : {}".format(encryptOrdValue))
            print("encryptChrValue : {}".format(encryptChrValue))
            listEncrypted.append(encryptChrValue)
            encryptedText = "".join(listEncrypted)
            listKeyOrder+=1

        print(f"listFromRaw: {listFromRaw}")
        print(f"listEncryted: {listEncrypted}")
        print(f"listOrdValues: {listOrdValues}")
        # entryForTitle.config(state="disabled")
        multilineText.delete("1.0", tk.END)
        multilineText.insert(1.0,listEncrypted)
        # multilineText.config(state="disabled")
        entryForMasterKeyText.delete(0, tk.END)
        # buttonForSaveAndEncryption.config(state="disabled")
        buttonForDecryption.config(state="normal")

        with open(f"{titleName}.txt", "w", encoding="utf-8") as f:
            f.write(encryptedText)

    else:
        myColor = "red"
        entryForTitle.config(background=myColor, fg="white")
        entryForMasterKeyText.config(background=myColor, fg="white")
        multilineText.config(bg=myColor, fg="white")
        print("Enter Title and Master Key")
        tk.messagebox.showerror("Warning", "Please Fill All Fields !")





def openAndDecrypt():
    global listOrdValues
    print("listOrdValues From saveAndEncrypt: {}".format(listOrdValues))
    listKeyOrder = 0
    listOrgOrdValues = []
    listOrgChrValues = []
    # entryForTitle.config(state="disabled")

    listKey= entryForMasterKeyText.get()
    for element in listOrdValues:
        print("*******************************************************")
        listKeyElementValue = str(listKey[listKeyOrder%len(listKey)])
        ordValueListKey = ord(listKeyElementValue)
        print("ordValue : {}".format(element))
        orgOrdValue = int(element)- int(ordValueListKey)
        if orgOrdValue >=0:
            print("orgOrdValue : {}".format(orgOrdValue))
            orgChrValue = chr(orgOrdValue)
            listOrgOrdValues.append(orgOrdValue)
            listOrgChrValues.append(orgChrValue)
            listKeyOrder+=1
            print(f"ln 116 listOrgOrdValues : {listOrgOrdValues}")
            print(f"ln 117 listOrgChrValues : {listOrgChrValues}")
        else:
            continue
        strOrgChrValue = "".join(listOrgChrValues)
    multilineText.config(state="normal")
    multilineText.delete("1.0",tk.END)
    multilineText.insert(1.0,strOrgChrValue)
    listOrdValues = []
    listOrgOrdValues = []
    listOrgChrValues = []
    listKey= ""
    entryForMasterKeyText.delete(0,tk.END)
    # buttonForDecryption.config(state="disabled")
    buttonForSaveAndEncryption.config(state="normal")


buttonForSaveAndEncryption = tk.Button(myWindow,text="Save & Encrypt",
                                    bg="light blue", fg="dark blue",
                                    borderwidth=1,border="1", relief="raised",font=('Arial', 12, 'bold'),
                                    highlightcolor="azure",
                                    command=saveAndEncrypt)
buttonForSaveAndEncryption.pack(pady=5)
buttonForDecryption = tk.Button(myWindow,text="Decrypt",font=('Arial', 12, 'bold'),bg="light blue",fg="dark blue",
                                borderwidth=1, relief="raised",
                                highlightcolor="azure",
                                command=openAndDecrypt)
buttonForDecryption.pack(pady=5)



myWindow.mainloop()
