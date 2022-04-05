from tkinter import *
from tkinter.font import Font


LAST_OPERATOR = 'c'
FIRST_NUM = 0
SECOND_NUM = 0
DIGIT_GOT_CLICKED = False
LAST_CALC_WAS_EQUAL = False


def addition():
    global LAST_OPERATOR, FIRST_NUM, DIGIT_GOT_CLICKED, LAST_CALC_WAS_EQUAL
    # If first number hasn't been defined yet, then define it.
    if not (LAST_CALC_WAS_EQUAL or DIGIT_GOT_CLICKED):
        LAST_OPERATOR = '+'
        return
    elif LAST_OPERATOR == 'c' or (LAST_CALC_WAS_EQUAL and not DIGIT_GOT_CLICKED):
        FIRST_NUM = float(e.get())
        e.delete(0, END)
    else:
        FIRST_NUM += float(e.get())
        e.delete(0, END)
        e.insert(0, str(FIRST_NUM))

    LAST_OPERATOR = '+'
    DIGIT_GOT_CLICKED = False
    LAST_CALC_WAS_EQUAL = False


def subtraction():
    global LAST_OPERATOR, FIRST_NUM, DIGIT_GOT_CLICKED, LAST_CALC_WAS_EQUAL
    # If first number hasn't been defined yet, then define it.
    if not (LAST_CALC_WAS_EQUAL or DIGIT_GOT_CLICKED):
        LAST_OPERATOR = '-'
        return
    elif LAST_OPERATOR == 'c' or (LAST_CALC_WAS_EQUAL and not DIGIT_GOT_CLICKED):
        FIRST_NUM = float(e.get())
        e.delete(0, END)
    else:
        FIRST_NUM -= float(e.get())
        e.delete(0, END)
        e.insert(0, str(FIRST_NUM))

    LAST_OPERATOR = '-'
    DIGIT_GOT_CLICKED = False
    LAST_CALC_WAS_EQUAL = False


def multiplication():
    global LAST_OPERATOR, FIRST_NUM, DIGIT_GOT_CLICKED, LAST_CALC_WAS_EQUAL
    # If first number hasn't been defined yet, then define it.
    if not (LAST_CALC_WAS_EQUAL or DIGIT_GOT_CLICKED):
        LAST_OPERATOR = '*'
        return
    elif LAST_OPERATOR == 'c' or (LAST_CALC_WAS_EQUAL and not DIGIT_GOT_CLICKED):
        FIRST_NUM = float(e.get())
        e.delete(0, END)
    else:
        FIRST_NUM *= float(e.get())
        e.delete(0, END)
        e.insert(0, str(FIRST_NUM))

    LAST_OPERATOR = '*'
    DIGIT_GOT_CLICKED = False
    LAST_CALC_WAS_EQUAL = False


def division():
    global LAST_OPERATOR, FIRST_NUM, DIGIT_GOT_CLICKED, LAST_CALC_WAS_EQUAL
    # If first number hasn't been defined yet, then define it.
    if not (LAST_CALC_WAS_EQUAL or DIGIT_GOT_CLICKED):
        LAST_OPERATOR = '/'
        return
    elif LAST_OPERATOR == 'c' or (LAST_CALC_WAS_EQUAL and not DIGIT_GOT_CLICKED):
        FIRST_NUM = float(e.get())
        e.delete(0, END)
    else:
        try:
            FIRST_NUM /= float(e.get())
            e.delete(0, END)
            e.insert(0, str(FIRST_NUM))
        except ZeroDivisionError as error:
            msg_to_user.config(text='ERROR: {}'.format(error))
            clear()

    LAST_OPERATOR = '/'
    DIGIT_GOT_CLICKED = False
    LAST_CALC_WAS_EQUAL = False


def equal():
    global LAST_OPERATOR, FIRST_NUM, LAST_CALC_WAS_EQUAL
    if LAST_CALC_WAS_EQUAL:
        pass
    elif LAST_OPERATOR == '+':
        addition()
    elif LAST_OPERATOR == '-':
        subtraction()
    elif LAST_OPERATOR == '*':
        multiplication()
    elif LAST_OPERATOR == '/':
        division()
    LAST_CALC_WAS_EQUAL = True


def clear():
    global LAST_OPERATOR, FIRST_NUM, DIGIT_GOT_CLICKED, LAST_CALC_WAS_EQUAL
    FIRST_NUM = 0
    DIGIT_GOT_CLICKED = False
    e.delete(0, END)
    LAST_OPERATOR = 'c'
    LAST_CALC_WAS_EQUAL = False


def manage_click(click_input):
    global LAST_OPERATOR, DIGIT_GOT_CLICKED
    """
    Enter click_input received to the end of the entry
    :param click_input:
    :return:
    """
    if click_input.isdigit():
        digit_click(click_input)
    else:
        msg_to_user.config(text='')
    if click_input == 'c':
        clear()
    elif click_input == '=':
        equal()
    elif click_input == '+':
        addition()
    elif click_input == '-':
        subtraction()
    elif click_input == '*':
        multiplication()
    elif click_input == '/':
        division()


def digit_click(digit):
    global DIGIT_GOT_CLICKED
    e.insert(END, digit)
    DIGIT_GOT_CLICKED = True


root = Tk()
root.resizable(width=False, height=False)
root.title('Nitzan\'s\' Calculator')

ft = Font(size=20)

e = Entry(root, width=30, borderwidth=5, font=Font(size=15))
e.grid(row=0, columnspan=3)

msg_to_user = Label(root, text='', font=Font(size=15), fg='red')
msg_to_user.grid(row=10, columnspan=4)

btn1 = Button(root, text='1', padx=40, pady=20, font=ft, command=lambda: manage_click('1'))
btn2 = Button(root, text='2', padx=40, pady=20, font=ft, command=lambda: manage_click('2'))
btn3 = Button(root, text='3', padx=40, pady=20, font=ft, command=lambda: manage_click('3'))
btn4 = Button(root, text='4', padx=40, pady=20, font=ft, command=lambda: manage_click('4'))
btn5 = Button(root, text='5', padx=40, pady=20, font=ft, command=lambda: manage_click('5'))
btn6 = Button(root, text='6', padx=40, pady=20, font=ft, command=lambda: manage_click('6'))
btn7 = Button(root, text='7', padx=40, pady=20, font=ft, command=lambda: manage_click('7'))
btn8 = Button(root, text='8', padx=40, pady=20, font=ft, command=lambda: manage_click('8'))
btn9 = Button(root, text='9', padx=40, pady=20, font=ft, command=lambda: manage_click('9'))
btn0 = Button(root, text='0', padx=40, pady=20, font=ft, command=lambda: manage_click('0'))
btn_clr = Button(root, text='Clear', padx=73, pady=20, font=ft, command=lambda: manage_click('c'))
btn_add = Button(root, text='+', padx=38, pady=20, font=ft, command=lambda: manage_click('+'))
btn_sub = Button(root, text='-', padx=42, pady=20, font=ft, command=lambda: manage_click('-'))
btn_mul = Button(root, text='x', padx=40, pady=20, font=ft, command=lambda: manage_click('*'))
btn_div = Button(root, text='/', padx=42, pady=20, font=ft, command=lambda: manage_click('/'))
btn_eql = Button(root, text='=', padx=39, pady=20, font=ft, command=lambda: manage_click('='))

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn0.grid(row=4, column=0)
btn_clr.grid(row=4, column=1, columnspan=2)
btn_add.grid(row=3, column=3)
btn_sub.grid(row=2, column=3)
btn_mul.grid(row=1, column=3)
btn_div.grid(row=0, column=3)
btn_eql.grid(row=4, column=3)

mainloop()
