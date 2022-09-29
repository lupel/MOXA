import tkinter as tk
window = tk.Tk()
window.geometry("800x800")
window.title("ioLogic E1210 #1")
# window.resizable(False, False)
# window.configure(background="white")


def first_print():
    text = "  ◌     ◌     ◌      ◌      ◌      ◌      ◌     ◌"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 15))
    text_output.grid(row=9900, column=0, sticky="W")
    text = "  DI8      DI9     DI10     DI11     DI12     DI13     DI14     DI15"
    text_output = tk.Label(window, text=text, fg="green", font=("Garamond", 10))
    text_output.grid(row=9990, column=0, sticky="W")

def second_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=1150, column=12, padx=0, sticky="W")


def three_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=1150, column=12, padx=0, sticky="W")

def for_function():
        text = " [▀]"
        text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
        text_output.grid(row=3150, column=12, padx=0, sticky="W")

def five_function():
        text = " [▄]"
        text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
        text_output.grid(row=3150, column=12, padx=0, sticky="W")


def six_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=6150, column=12, padx=0, sticky="W")

def seven_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=6150, column=12, padx=0, sticky="W")

def eight_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=9150, column=12, padx=0, sticky="W")

def nine_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=9150, column=12, padx=0, sticky="W")

def ten_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=9150, column=9012, padx=0, sticky="W")

def eleven_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=9150, column=9012, padx=0, sticky="W")

def thirteen_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=6150, column=9012, padx=0, sticky="W")

def fourteen_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=6150, column=9012, padx=0, sticky="W")


def fiveteen_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=1150, column=9012, padx=0, sticky="W")

def sixteen_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=1150, column=9012, padx=0, sticky="W")


def seventeen_function():
    text = " [▀]"
    text_output = tk.Label(window, text=text, fg="red", font=("Garamond", 17))
    text_output.grid(row=3150, column=9012, padx=0, sticky="W")

def eighteen_function():
    text = " [▄]"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 17))
    text_output.grid(row=3150, column=9012, padx=0, sticky="W")



dIO_button = tk.Button(text="Status of digital Input", command=first_print)
dIO_button.grid(row=9900, column=2700, sticky="W")




d11_button = tk.Button(text="On DO 11", command=eight_function)
d11_button.grid(row=9000, column=10, pady=20, sticky="W")

d11_button = tk.Button(text="Off DO 11", command=nine_function)
d11_button.grid(row=9300, column=10, pady=20, sticky="W")


dO8_button = tk.Button(text="On DO 08", command=second_function)
dO8_button.grid(row=1000, column=10, pady=20, sticky="W")

dO8_button = tk.Button(text="Off DO 08", command=three_function)
dO8_button.grid(row=1300, column=10, pady=20, sticky="W")



dO9_button = tk.Button(text="On DO 09", command=for_function)
dO9_button.grid(row=3000, column=10, pady=20, sticky="W")

dO9_button = tk.Button(text="Off DO 09", command=five_function)
dO9_button.grid(row=3300, column=10, pady=20, sticky="W")



d10_button = tk.Button(text="On DO 10", command=six_function)
d10_button.grid(row=6000, column=10, pady=20, sticky="W")

d10_button = tk.Button(text="Off DO 10", command=seven_function)
d10_button.grid(row=6300, column=10, pady=20, sticky="W")



d15_button = tk.Button(text="On DO 15", command=ten_function)
d15_button.grid(row=9000, column=9000, pady=20, sticky="W")

dO15_button = tk.Button(text="Off DO 15", command=eleven_function)
dO15_button.grid(row=9300, column=9000, pady=20, sticky="W")


dO12_button = tk.Button(text="On DO 12", command=fiveteen_function)
dO12_button.grid(row=1000, column=9000, pady=20, sticky="W")

dO12_button = tk.Button(text="Off DO 12", command=sixteen_function)
dO12_button.grid(row=1300, column=9000, pady=20, sticky="W")



dO13_button = tk.Button(text="On DO 13", command=seventeen_function)
dO13_button.grid(row=3000, column=9000, pady=20, sticky="W")

dO13_button = tk.Button(text="Off DO 13", command=eighteen_function)
dO13_button.grid(row=3300, column=9000, pady=20, sticky="W")



dO14_button = tk.Button(text="On DO 14", command=thirteen_function)
dO14_button.grid(row=6000, column=9000, pady=20, sticky="W")

dO14_button = tk.Button(text="Off DO 14", command=fourteen_function)
dO14_button.grid(row=6300, column=9000, pady=20, sticky="W")







if __name__ == "__main__":
    window.mainloop()