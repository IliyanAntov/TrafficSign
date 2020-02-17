import threading

from DataExchange.TrafficSignConnection.TrafficSignConnectionHandler import (
    TrafficSignConnectionHandler,
)
from DataExchange.AdminConnection.AdminAppConnectionHandler import (
    AdminAppConnectionHandler,
)


# Handles admin application connections
def HandleAdminConnections():
    # Wait for a connection
    adminSocketTuple = adminConnections.WaitForConnection()
    # Create a thread for another connection
    threading.Thread(target=HandleAdminConnections).start()
    if adminSocketTuple:
        # Handle the login process for the established connection
        adminConnections.WaitForLogin(adminSocketTuple[0], adminSocketTuple[1])

# Handles traffic sign device connections
def HandleDeviceConnections():
    # Wait for a connection
    connected = deviceConnections.WaitForConnection()
    # Create a thread for another connection
    threading.Thread(target=HandleDeviceConnections).start()

# Main method of the application - executes first
if __name__ == "__main__":

    # Create an AdminAppConnectionHandler() object
    adminConnections = AdminAppConnectionHandler()
    # Create a TrafficSignConnectionHandler() object
    deviceConnections = TrafficSignConnectionHandler()

    # Create a thread for handling admin application connections
    threading.Thread(target=HandleAdminConnections).start()
    # Create a thread for handling traffic sign device connections
    threading.Thread(target=HandleDeviceConnections).start()
