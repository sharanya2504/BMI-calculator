from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("BMI Calculator")
root.geometry("250x100")
root.resizable(0,0)

def calculate_bmi():
    wt = int(weightentry.get())
    ht = int(heightentry.get()) / 100
    bmi = wt / (ht * ht)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi}. You are Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi}. You are Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi}. you are Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi}. You are Obese')
    else:
        messagebox.showerror('BMI Calculator', 'Please enter valid input!')

def reset_entry():
    heightentry.delete(0, 'end')
    weightentry.delete(0, 'end')

f1=Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f1.grid()

f2=Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f2.grid()

weight=Label(f1,text="Weight in kgs")
height=Label(f2,text="height in cms")
weight.grid(row=0)
height.grid(row=1)

weightvalue=StringVar()
heightvalue=StringVar()

weightentry=Entry(root,textvariable=weightvalue)
heightentry=Entry(root,textvariable=heightvalue)

weightentry.grid(row=0,column=1)
heightentry.grid(row=1,column=1)

cal_btn = Button(text='Calculate',command=calculate_bmi)
cal_btn.grid(row=3,column=0,columnspan=1)

reset_btn = Button(text='Reset',command=reset_entry)
reset_btn.grid(row=3,column=1,columnspan=1)

exit_btn = Button(text='Exit',command=lambda: root.destroy())
exit_btn.grid(row=3,column=2,columnspan=1)


root.mainloop()