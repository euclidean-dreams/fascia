from time import sleep

from gpiozero import MCP3008, Button


class Fascia:
    def __init__(self, publisher):
        self.__publisher = publisher
        self.__potentiometers = [
            # first rack
            MCP3008(channel=0),
            MCP3008(channel=1),
            MCP3008(channel=2),
            MCP3008(channel=3),
            MCP3008(channel=4),
        ]
        self.__buttons = [
            # first rack
            Button(2),
            Button(3),
            Button(4),
            Button(5),
            Button(6),
            Button(21),

            # second rack
            Button(16),
            Button(17),
            Button(18),
            Button(19),
            Button(20)
        ]
        for button in self.__buttons:
            button.when_activated = self.__button_pressed

    def __button_pressed(self, device):
        pin = int(device.pin._number) - 2
        if pin == 19:
            pin = 5
        if pin > 5:
            pin -= 8
        self.__publisher.send_phenomenon(int(pin), 1)

    def start(self):
        while True:
            sleep(0.01)
            pots = []
            for pot in self.__potentiometers:
                pots.append(pot.value)
            self.__publisher.send_axiomology(pots)
