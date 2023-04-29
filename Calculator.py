from tkinter import *
from tkinter.font import *
from tkinter import messagebox
import math
from math import *
from re import *
from sympy import *

window = Tk()
window.title("Expression Calculator")
window.geometry("770x297")
window.config()

#defining variable entry box
variable_label = Label(window, font=("oswald",12,BOLD), bd=0, text= "Variables :", bg="white", fg="#292929", height=1, width=13)
variable_label.grid(row=1, column=1, padx=0.5, pady=0.5, columnspan=2, ipady= 5)
variable_box = Entry(window, font=("oswald",12, BOLD), bd=0, fg="#292929", width= 60)
variable_box.grid(row=1, column=3, padx=0.5, pady=0.5, columnspan=8, ipady=4.5)

#example for variable box
def add_example():
    variable_box.config(font=(NORMAL),fg="#0d0d0d")
    variable_box.insert(END,"eg x=2;y=4")
def remove_example():
    if variable_box.get() =="eg x=2;y=4":
        variable_box.delete(0,END)
        variable_box.config(font=(BOLD),fg="#292929")
add_example()
variable_box.bind("<FocusIn>",remove_example())

#defining example for variable box
variable_box.insert(END,'for eg, x=2; y=3; z=4')
def remove_example(event):
    if variable_box.get() == 'for eg, x=2; y=3; z=4':
        variable_box.delete(0,END)
        variable_box.config(fg="#666666")
variable_box.bind("<FocusIn>",remove_example)

#defining input entry box
input_box = Entry(window, font=("oswald",20, BOLD), bd=0, width=45, fg="#292929", justify="right")
input_box.grid(row=2, column=1, padx=0.5, pady=0.5, columnspan=10, ipady=7)
input_box.focus_set()

#defining a function to enter input in entries
def enter_str(str):
    widget = window.focus_get()
    if widget == variable_box:
        variable_box.insert(INSERT,str)
    elif widget == input_box:
        input_box.insert(INSERT,str)
    elif widget == diff_entry_wrt:
        diff_entry_wrt.insert(INSERT,str)
    elif widget == int_entry_wrt:
        int_entry_wrt.insert(INSERT,str) 

#defining buttons to enter string
button_list = [(0,7,4),(1,4,3),(2,4,4),(3,4,5),(4,5,3),(5,5,4),(6,5,5),(7,6,3),(8,6,4),(9,6,5),('π',3,1),('e',3,2),('(',3,3),(')',3,4),('/',4,6),('*',5,6),('-',6,6),('+',7,6),('.',7,5)]
for i in range (0, len(button_list)):
    button_raw = button_list[i]
    number = button_raw[0]
    row = button_raw[1]
    column = button_raw[2]
    button_name = "button_"+str(number)
    globals()[button_name] =  Button(window, bd=0, font=("oswald",12,BOLD), text=number, width=6, height=2, bg="white", fg="#292929", command=lambda n=number: enter_str(n))
    (globals()[button_name]).grid(row=row, padx=0.5, pady=0.5, column=column)
    
#defining algebric functions

#square
square_button = Button(window, bd=0, font=("oswald",12,BOLD), text="x\u00b2", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("\u00b2"))
square_button.grid(row=5, padx=0.5, pady=0.5, column=2)

#square root 
square_root_button = Button(window, bd=0, font=("oswald",12,BOLD), text="2√x", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("2√"))
square_root_button.grid(row=6, padx=0.5, pady=0.5, column=2)

#ln x
ln_button = Button(window, bd=0, font=("oswald",12,BOLD), text="lnx", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("ln("))
ln_button.grid(row=7, padx=0.5, pady=0.5, column=1)

#og x
log_button = Button(window, bd=0, font=("oswald",12,BOLD), text="log10(x)", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("log10("))
log_button.grid(row=7, padx=0.5, pady=0.5, column=2)

#factorial
factorial_button = Button(window, bd=0, font=("oswald",12,BOLD), text="x!", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("!"))
factorial_button.grid(row=4, padx=0.5, pady=0.5, column=2)
def replace_factorial(expr):
    return sub(r'(\d+|\w+)\s*!', lambda m: f'factorial({m.group(1)})', expr)


#nth root 
nth_root_button = Button(window, bd=0, font=("oswald",12,BOLD), text="n√x", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("√"))
nth_root_button.grid(row=6, padx=0.5, pady=0.5, column=1)
def replace_root(expr):
    return sub(r'(\d+)√(\w+)', r'pow(\2,1/\1)', expr)


#nth power 
nth_power_button = Button(window, bd=0, font=("oswald",12,BOLD), text="x\u207f", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("^"))
nth_power_button.grid(row=5, padx=0.5, pady=0.5, column=1)

# mod
mod_button = Button(window, bd=0, font=("oswald",12,BOLD), text="|x|", width=6, height=2, bg="white", fg="#292929", command=lambda : enter_str("|"))
mod_button.grid(row=4, padx=0.5, pady=0.5, column=1)
#replace mod function
def replace_mod(expr):
    while search(r'\|(.+?)\|', expr):
        expr = sub(r'\|(.+?)\|', lambda m: f'mod({replace_mod(m.group(1))})', expr)
    return expr
#mod function
def mod(x):
    if x >= 0:
        return x
    elif x<0:
        return -x


#sign change
def sign_change():
    sign_change_temp = input_box.get()
    input_box.delete(0,END)
    input_box.insert(0,"-("+ sign_change_temp + ")")
    
sign_change_button = Button(window, bd=0, font=("oswald",12,BOLD), text="+/-", width=6, height=2, bg="white", fg="#292929", command=lambda : sign_change())
sign_change_button.grid(row=7, padx=0.5, pady=0.5, column=3)


#back
def back():
    focus = window.focus_get()
    if focus == input_box:
        index_input_box = input_box.index(INSERT)
        input_box.delete(index_input_box-1,index_input_box)
    elif focus == variable_box:
        index_variable_box = variable_box.index(INSERT)
        variable_box.delete(index_variable_box-1,index_variable_box)
back_button = Button(window, bd=0, font=("oswald",12,BOLD), text="Back", width=6, height=2, bg="white", fg="#292929", command=lambda : back())
back_button.grid(row=3, padx=0.5, pady=0.5, column=6)


#clear
def clear():
    focus = window.focus_get()
    if focus == input_box:
        input_box.delete(0,END)
    elif focus == variable_box:
        variable_box.delete(0,END)
clear_button = Button(window, bd=0, font=("oswald",12,BOLD), text="Clear", width=6, height=2, bg="white", fg="#292929", command=lambda : clear())
clear_button.grid(row=3, padx=0.5, pady=0.5, column=5)


#function to delete existing buttons at coordinates in row_column list
def delete_button():
    row_column_list = [(4,7),(4,8),(4,9),(4,10),(5,7),(5,8),(5,9),(5,10),(6,7),(6,8),(6,9),(6,10)]
    for i in range(0,len(row_column_list)):
        row_column = row_column_list[i]
        row = row_column[0]
        column = row_column[1]
        for widget in window.grid_slaves(row,column):
            if isinstance(widget, Button):
                widget.destroy()
            elif isinstance(widget, Label):
                widget.destroy()
            elif isinstance(widget, Entry):
                widget.destroy()
            
#variables
def call_variables():
    delete_button()
    variable_list = [("x",4,7),("y",5,7),("z",6,7),("a",4,8),("b",5,8),("c",6,8),("α",4,9),("β",5,9),("ɣ",6,9),("θ",4,10),("ϕ",5,10),("λ",6,10)]
    for i in range (0, len(variable_list)):
        variable_raw = variable_list[i]
        variable = variable_raw[0]
        variable_row = variable_raw[1]
        variable_column = variable_raw[2]
        variable_button = "button_"+str(variable)
        globals()[variable_button] =  Button(window, bd=0, font=("oswald",12,BOLD), text=variable, width=6, height=2, bg="white", fg="#292929", command=lambda n=variable: enter_str(n))
        (globals()[variable_button]).grid(row=variable_row, padx=0.5, pady=0.5, column=variable_column)


#trignometric functions
def call_trigo():
    delete_button()
    trigo_list = [("sin",4,7),("cos",5,7),("tan",6,7),("asin",4,8),("acos",5,8),("atan",6,8),("sinh",4,9),("cosh",5,9),("tanh",6,9),("asinh",4,10),("acosh",5,10),("atanh",6,10)]
    for i in range (0, len(trigo_list)):
        trigo_raw = trigo_list[i]
        trigo = trigo_raw[0]
        trigo_row = trigo_raw[1]
        trigo_column = trigo_raw[2]
        trigo_button = "button_"+str(trigo)
        globals()[trigo_button] =  Button(window, bd=0, font=("oswald",12,BOLD), text=str(trigo)+"()", width=6, height=2, bg="white", fg="#292929", command=lambda n=trigo: enter_str(n+"("))
        (globals()[trigo_button]).grid(row=trigo_row, padx=0.5, pady=0.5, column=trigo_column)

        
#differentiation
def call_differentiation():
    #defining a function for differentiate button
    def differentiate():
        expression = input_box.get()    
        expression = expression.replace("^","**")
        expression = expression.replace("\u00b2","**2")
        expression = replace_factorial(expression)
        expression = replace_mod(expression)
        expression = replace_root(expression)
        
        globals()[diff_entry_wrt.get()] = Symbol(diff_entry_wrt.get().strip())
        expression_diff = diff(expression, diff_entry_wrt.get())
        
        input_box.delete(0,END)
        input_box.insert(0,expression_diff)
    
    delete_button()
    diff_label_wrt = Label(window, font=("oswald",12,BOLD), bd=0, text= "diff wrt to :", bg="white", fg="#292929", height=2, width=13)
    diff_label_wrt.grid(row=4, column=7, padx=0.5, pady=0.5, columnspan=2, ipady=3)
    diff_entry_wrt = Entry(window, font=("oswald",12,BOLD), bd=0, bg="white", fg="#292929", width=15)
    diff_entry_wrt.grid(row=4, column=9, padx=0.5, pady=0.5, columnspan=2, ipady=13)
    #example for diff_entry_wrt
    def add_example():
        diff_entry_wrt.config(font=(NORMAL),fg="#0d0d0d")
        diff_entry_wrt.insert(END,"eg x")
    def remove_example(event):
        if diff_entry_wrt.get() =="eg x":
            diff_entry_wrt.delete(0,END)
            diff_entry_wrt.config(font=(BOLD),fg="#292929")
    add_example()
    diff_entry_wrt.bind("<FocusIn>",remove_example)
    
    diff_button = Button(window, bd=0, font=("oswald",12,BOLD), text="Differentiate", width=26, height=2, bg="white", fg="#292929", command=lambda : differentiate())
    diff_button.grid(row=6, column=7, padx=0.5, pady=0.5, columnspan=4, ipadx=2)


#Integration
def call_integration():
    #definig a function for integrate button
    def integration():
        expression = input_box.get()    
        expression = expression.replace("^","**")
        expression = expression.replace("\u00b2","**2")
        expression = replace_factorial(expression)
        expression = replace_mod(expression)
        expression = replace_root(expression)
        
        x = Symbol(int_entry_wrt.get())
        int_expression= integrate(expression,x)
        
        input_box.delete(0,END)
        input_box.insert(0,int_expression)
    
    delete_button()
    int_label_wrt = Label(window, font=("oswald",12,BOLD), bd=0, text= "int wrt to :", bg="white", fg="#292929", height=2, width=13)
    int_label_wrt.grid(row=4, column=7, padx=0.5, pady=0.5, columnspan=2, ipady=3)
    int_entry_wrt = Entry(window, font=("oswald",12,BOLD), bd=0, bg="white", fg="#292929", width=15)
    int_entry_wrt.grid(row=4, column=9, padx=0.5, pady=0.5, columnspan=2, ipady=13)
    #example for int_entry_wrt
    def add_example():
        int_entry_wrt.config(font=(NORMAL),fg="#0d0d0d")
        int_entry_wrt.insert(END,"eg x")
    def remove_example(event):
        if int_entry_wrt.get() =="eg x":
            int_entry_wrt.delete(0,END)
            int_entry_wrt.config(font=(BOLD),fg="#292929")
    add_example()
    int_entry_wrt.bind("<FocusIn>",remove_example)

    int_button = Button(window, bd=0, font=("oswald",12,BOLD), text="Integrate", width=26, height=2, bg="white", fg="#292929", command=lambda : integration())
    int_button.grid(row=6, padx=0.5, pady=0.5, column=7, columnspan=4, ipadx=2)

#Creating option menu
selected_option = StringVar()
selected_option.set(value="Variables")

def menu_command(option):
    if option == "Variables":
        call_variables()
    elif option == "Trignometric Function":
        call_trigo()
    elif option == "Differentation":
        call_differentiation()
    elif option == "Integration":
        call_integration()

option_menu = OptionMenu(window, selected_option, "Variables", "Trignometric Function", "Differentation", "Integration",command=lambda option: menu_command(option))
option_menu.configure(font=("oswald",12,BOLD), width=25, height=2, bg="white", fg="#292929", bd=0)
option_menu.grid(row=3, column=7, padx=0.5, pady=0.5, columnspan=4, ipadx=2)
call_variables()


#Calculate
def calculate():
    expression = input_box.get()    
    replace_list = [("^","**"),("\u00b2","**2"),("π",str(math.pi)),("e",str(math.e)),("ln","math.log"),("sin","math.sin"),("cos","math.cos"),("tan","math.tan"),("asin","math.asin"),("acos","math.acos"),("atan","math.atan"),("sinh","math.sinh"),("cosh","math.cosh"),("tanh","math.tanh"),("asinh","math.asinh"),("acosh","math.acosh"),("atanh","math.atanh")]    
    
    for pair in replace_list:
        expression =  expression.replace(pair[0],pair[1])
            
    variable_raw = variable_box.get()
    if "=" in variable_raw and "eg x=2;y=4" not in variable_raw:
        variable_list = variable_raw.split(";")
        variables = {}
        for variable in variable_list:
            variable = variable.strip(" ")
            key,value = variable.split("=")
            expression = expression.replace(key,value)

    expression = replace_factorial(expression)
    expression = replace_mod(expression)
    expression = replace_root(expression)
        
    try:
        result = eval(expression)
        input_box.delete(0, END)
        variable_box.delete(0,END)
        input_box.insert(0, result)
    except NameError:
        messagebox.showerror("Error", "Please define the variables")
    except ValueError:
        messagebox.showerror("Domain error", "Please check domain of the functions")
    except ZeroDivisionError:
        messagebox.showerror("Zero Division Error", "Division by zero is not defined")
    except SyntaxError:
        messagebox.showerror("Syntax error", "Please enter the correct syntax")

calculate_button = Button(window, bd=0, font=("oswald",12,BOLD), text="Calculate", width=26, height=2, bg="white", fg="#292929", command=lambda : calculate())
calculate_button.grid(row=7, column=7, padx=0.5, pady=0.5, ipadx=2, columnspan=4)

window.mainloop()
