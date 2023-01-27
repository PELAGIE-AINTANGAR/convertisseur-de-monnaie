from tkinter import *
from math import *
from tkinter import ttk
import tkinter.messagebox



root = tkinter.Tk()
root.config(bg="lightgray")
root.title("GUI: Currency Conversion")
root.geometry("500x568")






zone_text= Label(text = "Pypower projet : Currency Converter" , bg="saddlebrown", font=1.0)
zone_text.pack(fill="x")

lblNombre1=Label(root, text="Amount :",font=1.0, bg="lightgray")
lblNombre1.place(x=100 , y=100)

entryNombre1=Entry(root)
entryNombre1.place(x=300, y=105, width=143)

lblNombre2=Label(root, text="From Currency :", font=1.0, bg="lightgray")
lblNombre2.place(x=100, y=150)

listCombox=ttk.Combobox(root, values=["euro", "dollar", "fcfa", "naira"])
listCombox.place(x=300, y=155)

lblNombre3=Label(root, text="To Currency :", font=1.0, bg="lightgray")
lblNombre3.place(x=100, y=200)

listCombox2=ttk.Combobox(root, values=["euro", "dollar", "fcfa", "naira"])
listCombox2.place(x=300, y=205)


lblNombre4=Label(root, text="Converted Amount :",font=1.0, bg="lightgray")
lblNombre4.place(x=100 , y=360)

entryNombre4=Entry(root)
entryNombre4.place(x=300, y=360, width=143)





def convert():
    
    montant =entryNombre1.get()
    print(montant)
    debut=listCombox.get()
    final=listCombox2.get()
    print(debut)
    print(final)


    if debut=="euro" and final=="dollar":
        resultat_dollar= float(montant) * 1.09
        entryNombre4.delete(0, END)
        entryNombre4.insert(0, resultat_dollar)
        print(resultat_dollar)
        
    if debut=="dollar" and final=="euro":
        resultat_euro=(float(montant) * 1) /1.09
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_euro)
        print(resultat_euro)
    
    if debut=="euro" and final=="fcfa":
        resultat_fcfa=(float(montant)* 1)/650
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_fcfa)
        print(resultat_fcfa)
        
    if debut=="fcfa" and final=="euro":
        resulatat_fc_euro=float(montant)*650
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resulatat_fc_euro)
        print(resulatat_fc_euro)
        
    if debut=="fcfa" and final=="dollar":
        resultat_fc_dollar=float(montant)* 0.0017
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_fc_dollar)
        print(resultat_fc_dollar)
        
    if debut=="dollar" and final=="fcfa":
        resultat__dollar_fc=(float(montant)*1)/0.0017
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat__dollar_fc)
        print(resultat__dollar_fc)
        
    if debut=="naira" and final=="euro":
        resultat_naira=float(montant)*0.0020
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_naira)
        print(resultat_naira)
        
    if debut=="euro" and final=="naira":
        resultat_naira_euro=(float(montant)*1)/0.0020
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_naira_euro)
        print(resultat_naira_euro)
        
    if debut=="naira" and final=="dollar":
        resultat_naira_dollar=float(montant)*0.0022
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_naira_dollar)
        print(resultat_naira_dollar)
        
    if debut=="dollar" and final=="naira":
        resultat_dollar_naira=(float(montant)*1)/0.0022 
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_dollar_naira)
        print(resultat_dollar_naira)
        
    if debut=="naira" and final=="fcfa":
        resultat_naira_fc=float(montant)* 1.32 
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_naira_fc)
        print(resultat_naira_fc)
        
    if debut=="fcfa" and final=="naira":
        resultat_fc_naira=float(montant)/1.32 
        entryNombre4.delete(0,END)
        entryNombre4.insert(0,resultat_fc_naira) 
        print(resultat_fc_naira)     
        
         
convert()


btnConver = tkinter.Button(root, text ="Convert", font=1.0, bg="blue",fg="white", command=convert)
btnConver.place(x=150, y=280, width=150, height=50)      
        
def allClear():
    montant =entryNombre1.get()
    debut=listCombox.get()
    final=listCombox2.get()
    if montant:
        entryNombre4.delete(0,END)
        entryNombre1.delete(0,END)
        listCombox.set("")
        listCombox2.set("")
        
     
btnClear = tkinter.Button(root, text ="Clear All", font=1.0, bg="white", fg="red", command=allClear)
btnClear.place(x=150, y=450, width=150, height=50)   




root.mainloop()
