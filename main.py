import tkinter as tk

root = tk.Tk()
root.geometry('325x500')

label = tk.Label(root, text='Calculator', font='Arial,19')
label.pack(padx=15, pady=15)

text_box = tk.Text(root, height=1, font='Arial,29')
text_box.pack(fill='x')

button_frame = tk.Frame(root)
button_frame.pack(fill='both', expand=True)

# Configure columns to expand
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# Configure rows to expand
button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.rowconfigure(3, weight=1)

# Create buttons with sticky parameter for expansion
button1 = tk.Button(button_frame, font='Arial 19', text='1')
button1.grid(row=0, column=0, sticky='nsew')
button2 = tk.Button(button_frame, font='Arial 19', text='2')
button2.grid(row=0, column=1, sticky='nsew')
button3 = tk.Button(button_frame, font='Arial 19', text='3')
button3.grid(row=0, column=2, sticky='nsew')
button4 = tk.Button(button_frame, font='Arial 19', text='4')
button4.grid(row=1, column=0, sticky='nsew')
button5 = tk.Button(button_frame, font='Arial 19', text='5')
button5.grid(row=1, column=1, sticky='nsew')
button6 = tk.Button(button_frame, font='Arial 19', text='6')
button6.grid(row=1, column=2, sticky='nsew')
button7 = tk.Button(button_frame, font='Arial 19', text='7')
button7.grid(row=2, column=0, sticky='nsew')
button8 = tk.Button(button_frame, font='Arial 19', text='8')
button8.grid(row=2, column=1, sticky='nsew')
button9 = tk.Button(button_frame, font='Arial 19', text='9')
button9.grid(row=2, column=2, sticky='nsew')
button_equals = tk.Button(button_frame, font='Arial 19', text='=')
button_equals.grid(row=3, column=0, sticky='nsew')
button_C = tk.Button(button_frame, font='Arial 19', text='C')
button_C.grid(row=3, column=1, sticky='nsew')
button0 = tk.Button(button_frame, font='Arial 19', text='0')
button0.grid(row=3, column=2, sticky='nsew')
button9 = tk.Button(button_frame, font='Arial 19', text='9')
button9.grid(row=2, column=2, sticky='nsew')
button9 = tk.Button(button_frame, font='Arial 19', text='9')
button9.grid(row=2, column=2, sticky='nsew')
button9 = tk.Button(button_frame, font='Arial 19', text='9')
button9.grid(row=2, column=2, sticky='nsew')
button9 = tk.Button(button_frame, font='Arial 19', text='9')
button9.grid(row=2, column=2, sticky='nsew')

root.mainloop()
