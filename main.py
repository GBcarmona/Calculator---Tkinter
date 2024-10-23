import tkinter as tk


root = tk.Tk()
root.geometry('325x500')
root.resizable(0, 0)
label = tk.Label(root, text='Calculator', font='Arial, 19')
label.pack(padx=15, pady=15)

display_widget = tk.Label(root, text='', font='Arial, 19', height=3)
display_widget.pack(padx=15, pady=15)

entry = ''
new_entry = ''
operator = ''

def button_click_(value):
    global entry
    entry += str(value)
    display_widget.config(text=entry)

def set_operator(op):
    global entry, new_entry, operator
    operator = op
    new_entry = entry
    entry = ''
    display_widget.config(text=op)

def calculate():
    global entry, new_entry, operator
    try:
        if operator == '+':
            entry = str(float(new_entry) + float(entry))
        elif operator == '-':
            entry = str(float(new_entry) - float(entry))
        elif operator == '*':
            entry = str(float(new_entry) * float(entry))
        elif operator == '/':
            if float(entry) != 0:
                entry = str(float(new_entry) / float(entry))
            else:
                display_widget.config(text='Error: Div by 0')
                return
        display_widget.config(text=entry)
        operator = ''
    except Exception as e:
        display_widget.config(text=f'Error: {e}')

def clear():
    global entry, new_entry, operator 
    entry = ''
    new_entry = ''
    operator = ''
    display_widget.config(text='')

button_frame = tk.Frame(root)
button_frame.pack(fill='both', expand=True)


button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

button1 = tk.Button(button_frame, font='Arial 19', text='1', command=lambda: button_click_('1'))
button1.grid(row=0, column=0, sticky='nsew')
button2 = tk.Button(button_frame, font='Arial 19', text='2', command=lambda: button_click_('2'))
button2.grid(row=0, column=1, sticky='nsew')
button3 = tk.Button(button_frame, font='Arial 19', text='3', command=lambda: button_click_('3'))
button3.grid(row=0, column=2, sticky='nsew')
button4 = tk.Button(button_frame, font='Arial 19', text='4', command=lambda: button_click_('4'))
button4.grid(row=1, column=0, sticky='nsew')
button5 = tk.Button(button_frame, font='Arial 19', text='5', command=lambda: button_click_('5'))
button5.grid(row=1, column=1, sticky='nsew')
button6 = tk.Button(button_frame, font='Arial 19', text='6', command=lambda: button_click_('6'))
button6.grid(row=1, column=2, sticky='nsew')
button7 = tk.Button(button_frame, font='Arial 19', text='7', command=lambda: button_click_('7'))
button7.grid(row=2, column=0, sticky='nsew')
button8 = tk.Button(button_frame, font='Arial 19', text='8', command=lambda: button_click_('8'))
button8.grid(row=2, column=1, sticky='nsew')
button9 = tk.Button(button_frame, font='Arial 19', text='9', command=lambda: button_click_('9'))
button9.grid(row=2, column=2, sticky='nsew')
button0 = tk.Button(button_frame, font='Arial 19', text='0', command=lambda: button_click_('0'))
button0.grid(row=3, column=0, sticky='nsew')
button_equals = tk.Button(button_frame, font='Arial 19', text='=', command=calculate)
button_equals.grid(row=2, column=1, sticky='nsew')
button_C = tk.Button(button_frame, font='Arial 19', text='C', command=clear)
button_C.grid(row=2, column=2, sticky='nsew')
button_plus = tk.Button(button_frame, font='Arial 19', text='+', command=lambda: set_operator('+'))
button_plus.grid(row=3, column=1, sticky='nsew')
button_minus = tk.Button(button_frame, font='Arial 19', text='-', command=lambda: set_operator('-'))
button_minus.grid(row=3, column=2, sticky='nsew')
button_multiply = tk.Button(button_frame, font='Arial 19', text='*', command=lambda: set_operator('*'))
button_multiply.grid(row=3, column=0, sticky='nsew')
button_divide = tk.Button(button_frame, font='Arial 19', text='/', command=lambda: set_operator('/'))
button_divide.grid(row=3, column=3, sticky='nsew')

root.mainloop()

#Not the greatest project ever but was my fisrt own made project, i used a ai to fix it sometimes but i done it =)