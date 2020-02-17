import socket
import ssl
import yaml
import hashlib
from DataExchange.Connection import Connection
from DataExchange.AdminConnection.AdminAppDataExchange import AdminAppDataExchange

# This class is responsible for:
#  - Creating and discarding sockets used for admin application connections
#  - Establishing connections to the admin applications
#  - Authenticating connected clients
#  - Creating threads for every authenticated client
class AdminAppConnectionHandler:

    # Constructor method
    def __init__(self):
        super().__init__()
        self.address = "0.0.0.0"  # IPv4 address used for the web server socket (listen on all addresses)
        self.port = 26418  # Admin application port

        # Create an unwrapped IPv4 TCP socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow the server to bind to an address which is in a TIME_WAIT state
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the given address and port
        self.socket.bind((self.address, self.port))
        # Enable the server to accept connections
        self.socket.listen()

        self.users = {}  # Known users
        # Load all known users
        self.LoadUsers()

    # Loads all known users from the Users.yaml file
    def LoadUsers(self):
        # Open the Users.yaml file as a readable stream
        with open("../Secrets/Users.yaml", "r") as stream:
            try:
                # Convert the contents of the file to a python object
                loaded = yaml.safe_load(stream)
                # Add every loaded entry to the users dictionary
                for key, value in loaded.items():
                    self.users[key] = value
            # File loading failed
            except yaml.YAMLError as exc:
                print(exc)

    # Waits for an incoming admin application connection
    def WaitForConnection(self):
        print("Listening for client . . .")
        # Accept the connection
        adminSocket, adminAddress = self.socket.accept()
        # Create an SSLContext object
        context = ssl.SSLContext(
            ssl.PROTOCOL_TLS_SERVER  # Server side connection (auto-negotiate highest supported SSL/TLS version)
        )
        # Load the certificate and private key used for the admin application connection
        context.load_cert_chain(
            certfile="../Secrets/Certificates/TrafficSignAppAdminConnectionCert.pem",
            keyfile="../Secrets/Certificates/TrafficSignAppAdminConnectionKey.pem",
        )
        # Create a protected SSL/TLS TCP socket (server side)
        adminSocket = context.wrap_socket(adminSocket, server_side=True)
        print("Connected to client at ", adminAddress)
        # Return the socket and address of the connection
        return (adminSocket, adminAddress)

    # Handles login requests sent by an admin application user
    def WaitForLogin(self, adminSocket, adminAddress):
        maxLoginAttempts = 5  # Maximum login attempts before the connection is closed
        loginAttemptCount = 1  # Current login attempt
        while True:
            # Check if the username and password are correct and save the return code
            returnCode = self.AuthenticateUser(adminSocket, adminAddress)

            # Username or password incorrect:
            if returnCode == 0:
                # Increment login attempt count
                loginAttemptCount += 1
                # If the attempts exceeded the maximum:
                if loginAttemptCount > maxLoginAttempts:
                    print("Too many login attempts, closing connection...")
                    # Send a refuse message to the client
                    Connection().SendMessage(adminSocket, b"refuse")
                    # Close the socket
                    adminSocket.close()
                    return False
                else:
                    # Send a no authentication (nauth) message to the client
                    Connection().SendMessage(adminSocket, b"nauth")

            # Username and password correct:
            elif returnCode == 1:
                print("Authenticated")
                # Send an authentication (auth) message to the client
                Connection().SendMessage(adminSocket, b"auth")
                # Create a data exchange thread for the connection
                adminThread = AdminAppDataExchange(adminSocket)
                # Start the thread
                adminThread.start()
                return True

            # Connection closed by client:
            elif returnCode == 2:
                print("Connection closed by remote client")
                return False

            # Something went wrong:
            else:
                # Close the socket
                adminSocket.close()
                return False

    # Checks the credentials that the user provided against the known usernames/passwords
    def AuthenticateUser(self, adminSocket, adminAddress):
        # Receive a username from the client
        username = Connection().ReceiveMessage(adminSocket)
        if username == None:
            return 2  # Connection closed by client code
        # Receive a password from the client
        password = Connection().ReceiveMessage(adminSocket)
        # Decode the username and password to utf-8 format
        username = username.decode("utf-8")
        password = password.decode("utf-8")
        # If the username does not exist:
        if username not in self.users:
            print("Username not found")
            return 0  # Username or password incorrect code

        # Load the salt and password hash of the given user
        salt = self.users[username]["salt"]
        knownHash = self.users[username]["password"]
        # Generate a new hash with the client's password
        newHash = self.GetPasswordHash(password, salt)
        # If the hashes are the same:
        if newHash == knownHash:
            # Authorize user
            print("Client at ", adminAddress, " authorized")
            return 1  # Username and password correct code
        else:
            # Do not authorize user
            print("Client at ", adminAddress, " not authorized")
            return 0  # Username or password incorrect code

    # Generates the hash of the given password by using the given salt
    def GetPasswordHash(self, password, salt):
        # Generate the password hash using pbkdf2
        return hashlib.pbkdf2_hmac(
            "sha512",  # Hash algorithm
            password.encode("utf-8"),  # Convert the password to bytes
            salt,  # Salt
            100000,  # Iterations of the hash algorithm
        )
