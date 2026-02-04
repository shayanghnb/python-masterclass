from tkinter import *

window = Tk()
window.geometry("640x640")
window.title("python calculator")


def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))


def button_clear():
    display.delete(0, END)


def equal():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

display = Entry(window,
                font=("arial", 24),
                borderwidth=5,
                relief="sunken",
                justify=LEFT,)

button0 = Button(window,
                 text="0",
                 command=lambda: button_click(0),
                 fg="black",
                 width=20,
                 height=2)

equal_button = Button(window,
                      text="=",
                      command=equal,
                      fg="black",
                      width=20,
                      height=2)
c_button = Button(window,
                  text="c",
                  command=button_clear,
                  fg="black",
                  width=20,
                  height=2)

button1 = Button(
    window,
    text="1",
    command=lambda: button_click(1),
    fg="black",
    width=20,
    height=2)

button2 = Button(
    window,
    text="2",
    command=lambda: button_click(2),
    fg="black",
    width=20,
    height=2)

button3 = Button(window,
                 text="3",
                 command=lambda: button_click(3),
                 fg="black",
                 width=20,
                 height=2)

button4 = Button(window,
                 text="4",
                 command=lambda: button_click(4),
                 fg="black",
                 width=20,
                 height=2)

button5 = Button(window,
                 text="5",
                 command=lambda: button_click(5),
                 fg="black",
                 width=20,
                 height=2)

button6 = Button(window,
                 text="6",
                 command=lambda: button_click(6),
                 fg="black",
                 width=20,
                 height=2)

button7 = Button(window,
                 text="7",
                 command=lambda: button_click(7),
                 fg="black",
                 width=20,
                 height=2)

button8 = Button(window,
                 text="8",
                 command=lambda: button_click(8),
                 fg="black",
                 width=20,
                 height=2)

button9 = Button(window,
                 text="9",
                 command=lambda: button_click(9),
                 fg="black",
                 width=20,
                 height=2)

plus_button = Button(window,
                     text="+",
                     command=lambda: button_click("+"),
                     fg="black",
                     width=10,
                     height=2)

minus_button = Button(window,
                      text="-",
                      command=lambda: button_click("-"),
                      fg="black",
                      width=10,
                      height=2)

multiply_button = Button(window,
                         text="*",
                         command=lambda: button_click("*"),
                         fg="black",
                         width=10,
                         height=2)

divide_button = Button(window,
                       text="/",
                       command=lambda: button_click("/"),
                       fg="black",
                       width=10,
                       height=2)

display.grid(row=0,
             column=0,
             columnspan=4,
             padx=30,
             pady=20,
             ipady=10,
             sticky="ew")

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

c_button.grid(row=4, column=0)
button0.grid(row=4, column=1)
equal_button.grid(row=4, column=2)

plus_button.grid(row=1, column=3)
minus_button.grid(row=2, column=3)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=4, column=3)

window.mainloop()
