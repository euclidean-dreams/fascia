from time import sleep

from gpiozero import MCP3008, Button


class Fascia:
    def __init__(self, performer_messenger, conductor_messenger):
        self.__performer_messenger = performer_messenger
        self.__conductor_messenger = conductor_messenger
        self.__potentiometers = [
            MCP3008(channel=0),
            MCP3008(channel=1),
            MCP3008(channel=2),
            MCP3008(channel=3),
            MCP3008(channel=4)
        ]
        self.__buttons = [
            Button(2),
            Button(3),
            Button(4),
            Button(5),
            Button(6),
            Button(7)
        ]
        for button in self.__buttons:
            button.when_released = self.__button_pressed

    def __button_pressed(self, device):
        # button fields are 100 - 105
        pin = int(device.pin._number) - 2 + 100
        self.__performer_messenger.send_float_morsel(int(pin), 1)

    def start(self):
        while True:
            sleep(0.1)
            # send pot 0
            self.__performer_messenger.send_float_morsel(10, self.__potentiometers[0].value)

            # send pot 1
            self.__performer_messenger.send_float_morsel(11, self.__potentiometers[1].value)

            # send equalizer values
            equalizer_values = [
                self.__potentiometers[2].value * 2,
                self.__potentiometers[3].value * 2,
                self.__potentiometers[4].value * 2
            ]
            self.__conductor_messenger.send_float_array_morsel(0, equalizer_values)
