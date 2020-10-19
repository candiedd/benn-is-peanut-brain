from tkinter import *
root=Tk()
root.configure(bg='grey12')
root.geometry("1920x1080")
root.title("KJ's Basic Calc")
n1E=Entry()
n1E.insert(0, "Number 1")
operatorE=Entry()
operatorE.insert(0, "Operator")
operatorI=Label(text="Use * for multiplication, / for division, + for addition and - for subtraction.")
n2E=Entry()
n2E.insert(0, "Number 2")
n1E.pack()
operatorE.pack()
operatorI.pack()
n2E.pack()
def submit():
    global n1, n2, n1E, n2E, operatorE, ResultL, result
    n2=float(n2E.get())
    n1=float(n1E.get())
    OEstr=str(operatorE.get())
    if OEstr=="*":
        result=n1*n2
        ResultL=Label(text=str(result))
        ResultL.pack()
    if OEstr=="+":
        result=n1+n2
        ResultL=Label(text=str(result))
        ResultL.pack()
    if OEstr=="/":
        result=n1/n2
        ResultL=Label(text=str(result))
        ResultL.pack()
    if OEstr=="-":
        result=n1-n2 
        ResultL=Label(text=str(result))
        ResultL.pack()

submitButton=Button(text="Submit",command=submit)
submitButton.pack()
def reset():
    ResultL.pack_forget()
ResetButton=Button(text="Reset", command=reset)
ResetButton.pack()
root.mainloop()