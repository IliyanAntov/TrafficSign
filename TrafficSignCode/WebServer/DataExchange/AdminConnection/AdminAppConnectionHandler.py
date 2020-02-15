import socket
import ssl
import yaml
import hashlib
from DataExchange.Connection import Connection
from DataExchange.AdminConnection.AdminAppDataExchange import AdminAppDataExchange


class AdminAppConnectionHandler:
    def __init__(self):
        super().__init__()
        self.address = "0.0.0.0"
        self.port = 26418
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.address, self.port))
        self.socket.listen(5)
        self.users = {}
        self.LoadUsers()

    def LoadUsers(self):
        with open("../Secrets/Users.yaml", "r") as stream:
            try:
                loaded = yaml.safe_load(stream)
                for key, value in loaded.items():
                    self.users[key] = value
            except Exception as exc:
                print(exc)

    def WaitForConnection(self):
        print("Listening for client . . .")
        self.adminSocket, self.adminAddress = self.socket.accept()

        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile="./DataExchange/Certificates/TrafficSignAppAdminConnectionCert.pem",
            keyfile="./DataExchange/Certificates/TrafficSignAppAdminConnectionKey.pem")

        self.adminSocket = context.wrap_socket(
            self.adminSocket,
            server_side=True
        )

        print("Connected to client at ", self.adminAddress)
        maxConnectionAttempts = 5
        connectionAttemptsCount = 1
        while True:
            returnCode = self.AuthenticateUser()
            if returnCode == 0:  # Username or password incorrect
                connectionAttemptsCount += 1
                if connectionAttemptsCount > maxConnectionAttempts:
                    print("Too many login attempts, closing connection...")
                    Connection().SendMessage(self.adminSocket, b"refuse")
                    self.adminSocket.close()
                    return False
                else:
                    Connection().SendMessage(self.adminSocket, b"nauth")
            elif returnCode == 1:  # Username and password correct
                print("Authenticated")
                Connection().SendMessage(self.adminSocket, b"auth")
                adminThread = AdminAppDataExchange(self.adminSocket)
                adminThread.start()
                return True
            elif returnCode == 2:  # Connection closed by client
                print("Connection closed by remote client")
                return False
            else:
                self.adminSocket.close()
                return False

    def AuthenticateUser(self):
        username = Connection().ReceiveMessage(self.adminSocket)
        if username == None:
            return 2  # Connection closed by client

        password = Connection().ReceiveMessage(self.adminSocket)
        username = username.decode()
        password = password.decode()

        if username not in self.users:
            print("Username not found")
            return 0

        salt = self.users[username]["salt"]
        knownHash = self.users[username]["password"]

        newHash = self.GetPasswordHash(password, salt)

        if newHash == knownHash:
            print("Client at ", self.adminAddress, " authorized")
            return 1  # Username and password correct
        else:
            print("Client at ", self.adminAddress, " not authorized")
            return 0  # Username or password incorrect

    def GetPasswordHash(self, password, salt):
        return hashlib.pbkdf2_hmac(
            "sha512",  # The hash digest algorithm for HMAC
            password.encode("utf-8"),  # Convert the password to bytes
            salt,  # Salt
            100000,  # Iterations
        )
