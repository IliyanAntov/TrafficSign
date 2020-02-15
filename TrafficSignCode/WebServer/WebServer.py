import threading

from DataExchange.TrafficSignConnection.TrafficSignConnectionHandler import (
    TrafficSignConnectionHandler,
)
from DataExchange.AdminConnection.AdminAppConnectionHandler import (
    AdminAppConnectionHandler,
)


def HandleAdminConnections():
    while True:
        adminConnection = adminConnections.WaitForConnection()


def HandleDeviceConnections():
    while True:
        deviceConnection = deviceConnections.WaitForConnection()


if __name__ == "__main__":

    adminConnections = AdminAppConnectionHandler()
    deviceConnections = TrafficSignConnectionHandler()

    threading.Thread(target=HandleAdminConnections).start()
    threading.Thread(target=HandleDeviceConnections).start()
