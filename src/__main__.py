import zmq

from fascia import Fascia
from morsel_messenger import MorselMessenger

CONDUCTOR_ENDPOINT = "tcp://0.0.0.0:44440"
PERFORMER_ENDPOINT = "tcp://0.0.0.0:44449"


def main():
    context = zmq.Context()
    performer_messenger = MorselMessenger(context, PERFORMER_ENDPOINT)
    conductor_messenger = MorselMessenger(context, CONDUCTOR_ENDPOINT)
    fascia = Fascia(performer_messenger, conductor_messenger)
    fascia.start()


if __name__ == '__main__':
    main()
