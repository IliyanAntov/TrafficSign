import threading

from DataExchange.TrafficSignConnection.TrafficSignConnectionHandler import (
    TrafficSignConnectionHandler,
)
from DataExchange.AdminConnection.AdminAppConnectionHandler import (
    AdminAppConnectionHandler,
)


def HandleDeviceConnections():
    connected = deviceConnections.WaitForConnection()
    threading.Thread(target=HandleDeviceConnections).start()


def HandleAdminConnections():
    connected = adminConnections.WaitForConnection()
    threading.Thread(target=HandleAdminConnections).start()
    if connected:
        adminConnections.WaitForLogin()


if __name__ == "__main__":

    adminConnections = AdminAppConnectionHandler()
    deviceConnections = TrafficSignConnectionHandler()

    threading.Thread(target=HandleAdminConnections).start()
    threading.Thread(target=HandleDeviceConnections).start()
