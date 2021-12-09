import zmq

from fascia import Fascia
from publisher import Publisher

ENDPOINT = "tcp://0.0.0.0:44440"


def main():
    context = zmq.Context()
    publisher = Publisher(context, ENDPOINT)
    fascia = Fascia(publisher)
    fascia.start()


if __name__ == '__main__':
    main()
