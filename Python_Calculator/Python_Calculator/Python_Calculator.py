import tkinter as tk

#global variable

expression=""
#function to update the expression
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

#evaluate the expression
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("ERROR")
        expression=""

def clear():
    global expression
    expression=""
    equation.set("")


calc=tk.Tk() #creates main window
calc.geometry("225x160")
calc.title("calculator")
equation=tk.StringVar() #holds a string
ent=tk.Entry(calc,width=16,borderwidth=3,relief=tk.RIDGE,textvariable=equation)
ent.grid(pady=10,row=0,sticky="w",padx=15)
#sticky="w" string starts west
char_nine=tk.Button(text="9",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda:press(9))
char_nine.grid(row=1,sticky="w",padx=15)


Char_eight=tk.Button(text="8",width=2,borderwidth=3,relief=tk.RAISED,
                        command=lambda: press(8))
Char_eight.grid(row=1,sticky="w",padx=45)
   
Char_seven=tk.Button(text="7",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(7))
Char_seven.grid(row=1,sticky="w",padx=75)
   
     
Char_six=tk.Button(text="6",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(6))
Char_six.grid(row=2,sticky="w",padx=15)
   
Char_five=tk.Button(text="5",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(5))
Char_five.grid(row=2,sticky="w",padx=45)
   
Char_four=tk.Button(text="4",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(4))
Char_four.grid(row=2,sticky="w",padx=75)
   
Char_three=tk.Button(text="3",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(3))
Char_three.grid(row=3,sticky="w",padx=15)
   
Char_two=tk.Button(text="2",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(2))
Char_two.grid(row=3,sticky="w",padx=45)
   
Char_one=tk.Button(text="1",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(1))
Char_one.grid(row=3,sticky="w",padx=75)
   
Char_zero=tk.Button(text="0",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press(0))
Char_zero.grid(row=4,sticky="w",padx=15)
Char_dec=tk.Button(text=".",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("."))
Char_dec.grid(row=4,sticky="w",padx=45)
   
Char_clear=tk.Button(text="c",width=2,borderwidth=3,relief=tk.RAISED,
                    command=clear)
Char_clear.grid(row=4,sticky="w",padx=135)
   
Char_equal=tk.Button(text="=",width=2,borderwidth=3,relief=tk.RAISED,
                        command=equalpress)
Char_equal.grid(row=4,sticky="w",padx=75)
Char_add=tk.Button(text="+",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("+"))
Char_add.grid(row=4,sticky="w",padx=105)
   
Char_sub=tk.Button(text="-",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("-"))
Char_sub.grid(row=3,sticky="w",padx=105)
Char_mult=tk.Button(text="*",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("*"))
Char_mult.grid(row=2,sticky="w",padx=105)

#UNICODE IS USED TO INSERT DIVISON SYMBOL
Char_div=tk.Button(text=chr(247),width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("/"))
Char_div.grid(row=1,sticky="w",padx=105)
Char_floor=tk.Button(text="//",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("//"))
Char_floor.grid(row=1,sticky="w",padx=135)
Char_power=tk.Button(text="^",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("**"))
Char_power.grid(row=2,sticky="w",padx=135)
Char_mod=tk.Button(text="%",width=2,borderwidth=3,relief=tk.RAISED,
                    command=lambda: press("%"))
Char_mod.grid(row=3,sticky="w",padx=135)


calc.mainloop()


main()
