import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.create_widgets()

    def create_widgets(self):
        # Create the display widget
        display = tk.Entry(self.root, textvariable=self.result_var, justify='right', font=('Arial', 16))
        display.grid(row=0, column=0, columnspan=14, padx=5, pady=5, ipady=10)

        # Create the buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for i, row in enumerate(buttons, start=1):
            for j, button_text in enumerate(row):
                button = tk.Button(self.root, text=button_text, width=6, height=2,
                                   font=('Arial', 16), command=lambda text=button_text: self.button_click(text))
                button.grid(row=i, column=j, padx=5, pady=5)

        # Create the clear button
        clear_button = tk.Button(self.root, text="C", width=6, height=2, font=('Arial', 16), command=self.clear)
        clear_button.grid(row=5, column=0, padx=5, pady=5)

    def button_click(self, text):
        if text == '=':
            try:
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                self.expression = "Math Error"
            except:
                self.expression = "Error"
            self.result_var.set(self.expression)
        elif text == 'C':
            self.clear()
        else:
            self.expression += text
            self.result_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_var.set("0")

    def run(self):
        ''' run the calculator in loop until the user press X'''
        self.root.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
