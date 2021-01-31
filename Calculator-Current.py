from tkinter import *
from math import *
from datetime import *
win = Tk() 
win.title("Calculator") # this title will be displayed on the top of the app
win.colormapwindows
#win.geometry("300x400") # this defines the size of the app of window
input_box = StringVar() # It gets the contents of the entry box
e = Entry(win,width = 50,  borderwidth = 5, textvariable = input_box) # this defines the size of the entry box for user input
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # this displays the entry box on the top
expression = "" # Initiate the variable expression

def button_click(num): # this function generates expression when any button is clicked
    global expression
    expression = expression + str(num)
    e.delete(0,END)
    input_box.set(expression)
    return
def Button_Clear(): # clears the contents of the entry box
    global expression
    expression = ""
    input_box.set(expression)
    return
def Button_Equal():
    global expression
    result = str(eval(expression))
    expression = result
    input_box.set(expression)
    return
def button_fac1():
    ec= int(eval(e.get()))
    Button_Clear()
    listfactors = []
    for var in range(1,ec+1):
            if ec%var== 0:
                listfactors.append(var)
    srl=str(listfactors)
    ec= str(ec)
    srl1= srl.strip("["+"]")
    #ecs= ec+"'s factors are "+srl1
    listfactors.clear()
    input_box.set(srl1)
    return
def button_fac2():
    prod= int(eval(e.get()))
    e.delete(0,END)
    #prod1= str(prod)
    prodcounter= prod-1
    while prodcounter>=1:
        prod= prod*prodcounter
        prodcounter=prodcounter-1
    prod= str(prod)
    #prs= prod1+"'s factorial is "+prod
    global expression
    expression= prod
    input_box.set(expression)
    return
def pn():
    ec= int(eval(e.get()))
    Button_Clear()
    listfactors = []
    for var in range(1,ec+1):
            if ec%var== 0:
                listfactors.append(var)
    ec=str(ec)
    #if len(listfactors)>=1:
    if len(listfactors)==2:
        input_box.set(ec+" is a prime number")
    else:
        input_box.set(ec+" is a composite number")
    if len(listfactors)==1:
        input_box.set(ec+" is neither prime nor composite")
'''def sqrt():
    n= int(e.get())
    c= n
    while c>0:
        if c*c==n:
            n= c
        else:
            c=c-1
    input_box.set(n)
    return'''
def pi_():
    global expression
    expression= str(22/7)
    input_box.set(str(expression))
    return
def sqrt_():
    '''ec= int(eval(e.get()))
    Button_Clear()
    listfactors = []
    for var in range(1,ec+1):
            if ec%var== 0:
                listfactors.append(var)
    s="Decimal Value"
    for i in listfactors:
        if i*i==ec:
            s=i'''
    s= sqrt(eval(e.get()))
    input_box.set(str(s))
    return
'''def sq():
    x=int(e.get())
    Button_Clear()
    input_box.set("Enter the exponent")
    global expression
    expression=""
    ex= int(e.get())
    Button_Clear()
    j=x
    while ex>1:
        x=x*j
        ex=ex-1
    input_box.set(x)'''
'''def sq(x,xx):
    x= int(eval(e.get()))
    Button_Clear()
    input_box.set("Enter the Exponent")
    xx= int(eval(e.get()))
    a= pow(x,xx)
    expression=a
    input_box.set(a)
    x=int(e.get())
    x= x*x
    input_box.set(x)
    return'''
def C():
    f=list(e.get())
    ff= str(f.pop(0))
    global expression
    expression= ff.strip("["+"]")
    input_box.set(expression)
    return
def Ab():
    absv= abs(eval(e.get()))
    e.delete(0,END)
    global expression
    expression= absv
    input_box.set(expression)
    return
'''def r():
    r= eval(e.get())
    e.delete(0,END)
    input_box.set("Decimal place to be rounded to:")
    r2= eval(e.get())
    global expression
    expression=round(r,r2) 
def rd():
    rdd=floor(eval(e.get()))
    global expression
    expression=rdd
    print(expression)
    input_box.set(expression)
    return
def ru():
    ruu=floor(eval(e.get))
    global expression
    expression=ruu
    input_box.set(expression)'''
def mf():
    mff=modf(eval(e.get( )))
    global expression
    expression=mff 
    input_box.set(expression)
    return
button_1 = Button(win, text="1", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White", command = lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White", command = lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(4))
button_5 = Button(win, text="5", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(5))
button_6 = Button(win, text="6", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(6))
button_7 = Button(win, text="7", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(7))
button_8 = Button(win, text="8", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(8))
button_9 = Button(win, text="9", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(9))
button_0 = Button(win, text="0", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(0))
button_sum = Button(win, text="+", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('+'))
button_diff = Button(win, text="-", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('-'))
button_equal = Button(win, text="=", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: Button_Equal())
button_clear = Button(win, text="AC", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: Button_Clear())
button_mul = Button(win, text="x", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('*'))
button_div = Button(win, text="÷", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('/'))
button_mod = Button(win, text="%", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('%'))
button_flo = Button(win, text="/", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('//'))
button_rb = Button(win, text="(", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('('))
button_lb = Button(win, text=")", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click(')'))
button_Fac1 = Button(win, text="Factor", padx=40, font= ("Courier",10), bg="Black", fg= "White",  pady=20, command = lambda: button_fac1())
button_Fac2 = Button(win, text="Factrl", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_fac2())
button_pn = Button(win, text="P/C", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: pn())
button_dot = Button(win, text=".", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('.'))
sq=Button(win, text="^", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: button_click('**'))
sq2=Button(win, text="√", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: sqrt_())
pI=Button(win, text="π", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: pi_())
ab = Button(win, text="|", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: Ab())
roundoff = Button(win, text="|", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: Ab())
be= Button(win, text="C", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: C())
R= Button(win, text="RND", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: r())
Ru= Button(win, text="⬆", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: ru())
Rd= Button(win, text="⬇", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: rd())
Modf= Button(win, text="x.y", padx=40, pady=20, font= ("Courier",10), bg="Black", fg= "White",  command = lambda: mf())
#To display buttons
#The following code displays the buttons creat
button_sum.grid(row=5, column=2)
button_diff.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_clear.grid(row=8, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=4, column=0)
button_mod.grid(row=8, column=0)
button_1.grid(row=1, column=0)
button_0.grid(row=4, column=1)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_div.grid(row=4, column=2)
button_flo.grid(row=8, column=2)
button_Fac1.grid(row=11, column=0)
button_Fac2.grid(row=11, column=2)
button_pn.grid(row=11, column=1)
button_lb.grid(row=6, column=2)
button_rb.grid(row=6, column=0)
button_dot.grid(row=6, column=1)
sq2.grid(row=7, column=2)
sq.grid(row=7, column=0)
pI.grid(row=10, column=0)
ab.grid(row=10, column=2)
be.grid(row=7, column=1)
Modf.grid(row=10, column=1)
'''R.grid(row=9, column=1)
Rd.grid(row=9, column=0)
Ru.grid(row=9, column=2)'''
win.mainloop()
