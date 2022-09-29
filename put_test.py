# author: lupel
# date: 20.09.2022
# version: 1.0

# description: This is REST API PUT function for MOXA ioLogik E1210 device

from requests import put
from json import dumps

from time import sleep, time

class PutRequestData():
    def __init__(self, address = "http://192.168.127.12"):
        self.address = address

        self.connection_error = None # True if there is no connection for more than 1 s
        self.json_data = None # converted response to json

        self.DO = [{'doIndex': 0, 'doMode': 0, 'doStatus': 1},
                   {'doIndex': 1, 'doMode': 0, 'doStatus': 1},
                   {'doIndex': 2, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 3, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 4, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 5, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 6, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 7, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 8, 'doMode': 0, 'doStatus': 1},
                   {'doIndex': 9, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 10, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 11, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 12, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 13, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 14, 'doMode': 0, 'doStatus': 0},
                   {'doIndex': 15, 'doMode': 0, 'doStatus': 0}]

        self.DO_to_json = {'slot': 0, 'io': {'do': self.DO}}

        self.last_put_time = time()

    def put_DO(self):
        self.convert_data_to_send()
        self.put_data(api_address_extension="/api/slot/0/io/do")

    def run(self):
        # put digital outputs
        self.put_DO()

    def put_data(self, api_address_extension = "/api/slot/0/io/do"):
        #print("get time {} ms".format(round(time() - self.start_time, 2) * 1000))
        try:
            self.reply = put(self.address + api_address_extension, self.json_data,
                             headers={"Content-Type": "application/json", "Accept": "vdn.dac.v1"},
                             timeout=1
                            )

            self.replay_status_code = self.reply.status_code
            self.connection_error = False
            self.last_put_time = time()


        except Exception as ex:

            print(ex)

            self.connection_error = True

    def convert_data_to_send(self):
        self.DO_to_json = {'slot': 0, 'io': {'do': self.DO}}
        self.json_data = dumps(self.DO_to_json)

if __name__ == "__main__":
    data = PutRequestData()
    data.run()

