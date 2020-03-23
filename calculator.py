#importing packages
from tkinter import *
import re


#initiate windows
root = Tk()
root.geometry("379x278")
root.title("Basic Calculator")

#global declaration
#flag just keep track that multiple sign not pressed at a time and eqal is not pressed after a sign
flag=False
#after the result of expression clear the display
end=False
#expreesin is the variable that stores the buttones those are clicked,initially empty
global expression
expression=''





#button for numeric input

button_1=Button(root,text="1",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(1)).grid(row=3,column=0)
button_2=Button(root,text="2",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(2)).grid(row=3,column=1)
button_3=Button(root,text="3",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(3)).grid(row=3,column=2)

button_4=Button(root,text="4",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(4)).grid(row=2,column=0)
button_5=Button(root,text="5",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(5)).grid(row=2,column=1)
button_6=Button(root,text="6",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(6)).grid(row=2,column=2)


button_7=Button(root,text="7",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(7)).grid(row=1,column=0)
button_8=Button(root,text="8",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(8)).grid(row=1,column=1)
button_9=Button(root,text="9",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(9)).grid(row=1,column=2)
button_0=Button(root,text="0",padx=40,pady=20, borderwidth=1,command=lambda :fun_num(0)).grid(row=4,column=0)





#button for calculatopn button

button_mul=Button(root,text="*",padx=40,pady=20, borderwidth=1,command=lambda:fun_cal('*')).grid(row=3,column=3)
button_sub=Button(root,text="-",padx=42,pady=20, borderwidth=1,command=lambda:fun_cal('-')).grid(row=2,column=3)
button_add=Button(root,text="+",padx=40,pady=20, borderwidth=1,command=lambda:fun_cal('+')).grid(row=1,column=3)
button_divide=Button(root,text="/",padx=40,pady=20, borderwidth=1,command=lambda:fun_cal('/')).grid(row=4,column=1)


button_clear=Button(root,text="clear",padx=30,pady=20, borderwidth=1,command=lambda:fun_clrscrn()).grid(row=4,column=2)
button_equal=Button(root,text="=",padx=41,pady=20, borderwidth=1,command=lambda:fun_equal()).grid(row=4,column=3)





#entry for display result
result=Entry(root,borderwidth=5,width=60)
result.grid(row=0,column=0,columnspan=30)









#function for get the numeric button's value
def fun_num(num):
    global expression
    global flag
    global end
    if end:
        result.delete(0, END)
    pre_num=result.get()
    result.delete(0,END)
    result.insert(0,str(pre_num)+str((num)))
    expression=(result.get())
    print(expression)
    flag=True
    end=False




#function for get the sign button's value
def fun_cal(num):
    global flag
    global end
    if end:
        result.delete(0, END)
    if flag:
        global expression
        pre_num=result.get()
        result.delete(0,END)
        result.insert(0,str(pre_num)+str(num))
        expression=result.get()
        flag= False
        end=False

        print(expression)





#function for clear the screen
def fun_clrscrn():
    result.delete(0,END)


#function for removing leading zeroes of a number as it indicates octal
def remove_leading_zero(txt):

    new = ""
    count = 1
    x = re.split(r"\D+", txt)
    print(x)
    #print(txt)
    y = re.split("\d+", txt)
    # y = re.sub("\s", "", txt)
    print(y)
    sign_len = len(y)
    for i in range(0, len(x)):
        x[i] = str(int(x[i]))
    print(x)
    for i in x:
        new = new + i

        if sign_len != 1:
            new = new + y[count]
            sign_len - 1
            count += 1
    return new




#function for evaluate the  expression
def fun_equal():
    global expression
    global flag
    global end
    global s
    expression = remove_leading_zero(expression)

    if flag:
        try:
            result.delete(0, END)
            result.insert(0,eval(expression))
            print(expression)
        except Exception as e:
            s=str(e)
            result.insert(0,s)
            print(s)

        finally:
            end=True
            flag = False








root.mainloop()