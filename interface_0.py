import tkinter as tk

window = tk.Tk()
window.geometry("800x800")
window.title("ioLogic E1210 #0")
# window.resizable(False, False)
# window.configure(background="white")


from requests import put
from json import dumps
from time import sleep, time


class PutRequestData():
    def __init__(self, address="http://192.168.100.12"):
        self.address = address

        self.connection_error = None  # True if there is no connection for more than 1 s
        self.json_data = None  # converted response to json

        self.DO = [{'doIndex': 0, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 1, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 2, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 3, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 4, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 5, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 6, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 7, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 8, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 9, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 10, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 11, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 12, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 13, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 14, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 15, 'doMode': 0, 'doStatus': 0}]

        self.DO_to_json = [{'slot': 0, 'io': {'do': self.DO}}]
        self.last_put_time = time()


def put_DO(self):
    self.convert_data_to_send()
    self.put_data(api_address_extension="/api/slot/0/io/do")


def run(self):
    # put digital outputs
    self.put_DO()


def put_data(self, api_address_extension="/api/slot/0/io/do"):
    # print("get time {} ms".format(round(time() - self.start_time, 2) * 1000))
    try:
        self.reply = put(self.address + api_address_extension, self.json_data,
                         headers={"Content-Type": "application/json", "Accept": "vdn.dac.v1"},
                         timeout=0.1
                         )

        self.replay_status_code = self.reply.status_code
        self.connection_error = False
        self.last_put_time = time()

    except Exception as ex:
        print(f"Errore {ex}")
        self.connection_error = True


def convert_data_to_send(self):
    self.DO_to_json = {'slot': 0, 'io': {'do': self.DO}}
    self.json_data = dumps(self.DO_to_json)


def first_print():
    text = "  ◌     ◌     ◌     ◌     ◌     ◌     ◌     ◌"
    text_output = tk.Label(window, text=text, fg="blue", font=("Garamond", 15))
    text_output.grid(row=9900, column=0, sticky="W")
    text = "  DI0      DI1     DI2      DI3      DI4     DI5      DI6      DI7"
    text_output = tk.Label(window, text=text, fg="green", font=("Garamond", 10))
    text_output.grid(row=9990, column=0, sticky="W")


def second_function():
    address = "http://192.168.100.12/05_21.htm?CHANNEL_NO=0"
    json_data = [{'doIndex': 0, 'doMode': 0, 'doStatus': 1}]

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


dIO_button = tk.Button(text="Status of digital I/O", command=first_print)
dIO_button.grid(row=9900, column=2700, sticky="W")

dO3_button = tk.Button(text="On DO 3", command=eight_function)
dO3_button.grid(row=9000, column=10, pady=20, sticky="W")

dO3_button = tk.Button(text="Off DO 3", command=nine_function)
dO3_button.grid(row=9300, column=10, pady=20, sticky="W")

dO0_button = tk.Button(text="On DO 0", command=second_function)
dO0_button.grid(row=1000, column=10, pady=20, sticky="W")

dO0_button = tk.Button(text="Off DO 0", command=three_function)
dO0_button.grid(row=1300, column=10, pady=20, sticky="W")

dO1_button = tk.Button(text="On DO 1", command=for_function)
dO1_button.grid(row=3000, column=10, pady=20, sticky="W")

dO1_button = tk.Button(text="Off DO 1", command=five_function)
dO1_button.grid(row=3300, column=10, pady=20, sticky="W")

dO2_button = tk.Button(text="On DO 2", command=six_function)
dO2_button.grid(row=6000, column=10, pady=20, sticky="W")

dO2_button = tk.Button(text="Off DO 2", command=seven_function)
dO2_button.grid(row=6300, column=10, pady=20, sticky="W")

dO7_button = tk.Button(text="On DO 7", command=ten_function)
dO7_button.grid(row=9000, column=9000, pady=20, sticky="W")

dO7_button = tk.Button(text="Off DO 7", command=eleven_function)
dO7_button.grid(row=9300, column=9000, pady=20, sticky="W")

dO4_button = tk.Button(text="On DO 4", command=fiveteen_function)
dO4_button.grid(row=1000, column=9000, pady=20, sticky="W")

dO4_button = tk.Button(text="Off DO 4", command=sixteen_function)
dO4_button.grid(row=1300, column=9000, pady=20, sticky="W")

dO5_button = tk.Button(text="On DO 5", command=seventeen_function)
dO5_button.grid(row=3000, column=9000, pady=20, sticky="W")

dO5_button = tk.Button(text="Off DO 5", command=eighteen_function)
dO5_button.grid(row=3300, column=9000, pady=20, sticky="W")

dO6_button = tk.Button(text="On DO 6", command=thirteen_function)
dO6_button.grid(row=6000, column=9000, pady=20, sticky="W")

dO6_button = tk.Button(text="Off DO 6", command=fourteen_function)
dO6_button.grid(row=6300, column=9000, pady=20, sticky="W")

if __name__ == "__main__":

    data = PutRequestData()
    window.mainloop()

    while True:
        data.run()
        sleep(0.2)

    print("do0 {} ".format(data.DO))
    print("do1 {} ".format(data.DO))
    print("do2 {} ".format(data.DO))
    print("do3 {} ".format(data.DO))
    print("do4 {} ".format(data.DO))
    print("do4 {} ".format(data.DO))
    print("do5 {} ".format(data.DO))
    print("do6 {} ".format(data.DO))
    print("do7 {} ".format(data.DO))
