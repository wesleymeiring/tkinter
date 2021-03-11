from tkinter import *

calculator = Tk()

calculator.title("Calculator")

result_window = Entry(calculator, width=45, borderwidth=10)
result_window.grid(row=0, column=0, columnspan=3, padx=8, pady=8)


def button_click(number):
    current_number = result_window.get()
    result_window.delete(0, END)
    result_window.insert(0, str(current_number) + str(number))


def button_clear():
    result_window.delete(0, END)


def button_add():
    first_num = result_window.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    result_window.delete(0, END)


def button_subtract():
    first_num = result_window.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    result_window.delete(0, END)


def button_multiply():
    first_num = result_window.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    result_window.delete(0, END)


def button_divide():
    first_num = result_window.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    result_window.delete(0, END)


def button_equal():
    second_num = result_window.get()
    result_window.delete(0, END)

    if math == "addition":
        result_window.insert(0, f_num + int(second_num))
    if math == "subtraction":
        result_window.insert(0, f_num - int(second_num))
    if math == "multiplication":
        result_window.insert(0, f_num * int(second_num))
    if math == "division":
        result_window.insert(0, f_num / 0)
        result_window.insert(0, f_num / int(second_num))




# Button aesthetics

button_1 = Button(calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(calculator, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(calculator, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(calculator, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(calculator, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(calculator, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(calculator, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(calculator, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(calculator, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(calculator, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(calculator, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(calculator, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(calculator, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(calculator, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(calculator, text="/", padx=40, pady=20, command=button_divide)

# Put buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_addition.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

calculator.mainloop()
