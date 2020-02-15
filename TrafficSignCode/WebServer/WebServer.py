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
    adminSocketTuple = adminConnections.WaitForConnection()
    threading.Thread(target=HandleAdminConnections).start()
    if adminSocketTuple:
        adminConnections.WaitForLogin(adminSocketTuple[0], adminSocketTuple[1])


if __name__ == "__main__":

    adminConnections = AdminAppConnectionHandler()
    deviceConnections = TrafficSignConnectionHandler()

    threading.Thread(target=HandleAdminConnections).start()
    threading.Thread(target=HandleDeviceConnections).start()
