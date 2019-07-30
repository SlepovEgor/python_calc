import tkinter as tk
from calc_v2.engine import engine
import time

class App:
    """"""
    eng = engine()
    parent = None
    label = None

    def set_gui(self):
        self.parent = tk.Tk()
        """Конструктор"""

        control_frame = tk.Frame(self.parent)

        numeric_frame = tk.Frame(control_frame)
        calc_frame = tk.Frame(control_frame)
        numeric_frame.grid(row = 0, column = 0, sticky = 'nsew')
        calc_frame.grid(row = 1, column = 0, sticky = 'nsew')
        numeric_frame.grid_rowconfigure(0, weight = 1)
        numeric_frame.grid_rowconfigure(1, weight = 1)
        numeric_frame.grid_rowconfigure(2, weight = 1)
        numeric_frame.grid_rowconfigure(3, weight = 1)
        numeric_frame.grid_columnconfigure(0, weight = 1)
        numeric_frame.grid_columnconfigure(1, weight = 1)
        numeric_frame.grid_columnconfigure(2, weight = 1)
        calc_frame.grid_columnconfigure(0, weight = 1)
        calc_frame.grid_columnconfigure(1, weight = 1)
        calc_frame.grid_columnconfigure(2, weight = 1)
        calc_frame.grid_columnconfigure(3, weight = 1)
        calc_frame.grid_rowconfigure(0, weight = 1)

        control_frame.grid(row = 1, column = 0, sticky = 'nwes',)
        control_frame.grid_rowconfigure(0, weight = 1)
        control_frame.grid_rowconfigure(1, weight = 1)
        control_frame.grid_columnconfigure(0, weight = 1)

        label_frame = tk.Frame(self.parent)
        self.label = tk.Label(label_frame, font = 'helvetica-bold 16', width = 15, height = 3, anchor = 'e', bg = 'yellow')
        self.label.grid(row= 0, column = 0, sticky = 'nsew')
        label_frame.grid(row = 0, column = 0, sticky = 'swen')
        label_frame.grid_rowconfigure(0, weight = 1)
        label_frame.grid_columnconfigure(0, weight = 1)

        plus = tk.Button(calc_frame, text='+', width=5, height=3)
        minus = tk.Button(calc_frame, text='-', width=5, height=3)
        equal = tk.Button(calc_frame, text='=', width=5, height=3)
        clear = tk.Button(calc_frame, text='C', width=5, height=3)

        plus.bind('<Button-1>', lambda event, op=plus['text']: self.set_op(op))
        minus.bind('<Button-1>', lambda event, op=minus['text']: self.set_op(op))
        equal.bind('<Button-1>', lambda event: self.get_result())
        clear.bind('<Button-1>', lambda event: self.clear())

        plus.grid(row=0, column=0, sticky = 'swen')
        minus.grid(row=0, column=1, sticky = 'swen')
        equal.grid(row=0, column=2, sticky = 'swen')
        clear.grid(row=0, column=3, sticky = 'swen')

        num_btn = []
        i = 1

        for row in range(0, 3):
            for column in range(0, 3):
                btn = tk.Button(
                    numeric_frame,
                    text=str(i),
                    width=3,
                    height=4,

                )
                btn.bind('<Button-1>', lambda event, nu=i: self.add_value(nu))
                # btn.bind('<Button-1>', lambda event, nu = i: printNum(str(nu)))
                # btn.bind('<Button-1>', lambda event: print('lalala'))
                btn.grid(row=row, column=column,sticky='nsew')
                num_btn.append(btn)
                i += 1

        self.parent.grid_rowconfigure(0, weight = 1)
        self.parent.grid_rowconfigure(1, weight = 1)
        self.parent.grid_columnconfigure(0, weight = 1)



        num_btn.append(tk.Button(numeric_frame, text='0', width=3, height=4))
        num_btn[len(num_btn) - 1].bind('<Button-1>', lambda event, nu=0: self.add_value(nu))
        num_btn[len(num_btn) - 1].grid(row=3, column=1, sticky = 'swen')

    def add_value(self, value):
        self.label['text'] += str(value)

    def set_op(self, op):
        send = self.label['text']
        self.eng.set_arg(str(send))
        self.eng.set_op(str(op))
        self.label['text'] = ''

    def get_result(self):
        send = self.label['text']
        self.eng.set_arg(str(send))
        self.eng.do_math()
        self.label['text'] = self.eng.get_result()

    def clear(self):
        self.label['text'] = ''
        self.eng.clear()

    def __init__(self):
        self.set_gui()
        self.parent.mainloop()
