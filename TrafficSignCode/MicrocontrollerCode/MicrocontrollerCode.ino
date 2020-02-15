// The GPRS module model
// (Required by the TinyGsmClient.h library)
#define TINY_GSM_MODEM_SIM800

#include <RGBmatrixPanel.h>
#include <TinyGsmClient.h>

// The interface on which AT commands will be sent
#define SerialAT Serial

// LED matrix pins
#define CLK 11
#define OE 9
#define LAT 10
#define A A0
#define B A1
#define C A2
#define D A3

// The APN of the ISP's GPRS network
const char apn[] = "internet.vivacom.com";
// The username of the ISP's GPRS network
const char gprsUser[] = "VIVACOM";
// The password of the ISP's GPRS network
const char gprsPass[] = "VIVACOM";

// Server details
// Static public IPv4 address of the web server
const char server[] = "3.125.80.10";
// Connection port
const int port = 19119;

// LED matrix object (RGBmatrixPanel.h library)
RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);
// GPRS modem object (TinyGsmClient.h library)
TinyGsm modem(SerialAT);
// GPRS connection client object (TinyGsmClient.h library)
TinyGsmClient client(modem);

// Performs initial device setup
void setup() {
  // Initialize the serial communication
  InitModulePins();

  // Initialize the GPRS module and connect to the web server
  bool state = RunConnectionProcedure();
  // Until a connection is established:
  while (!state) {
    // Restart the GPRS module
    RestartModule();
    // Retry the connection
    state = RunConnectionProcedure();
  }
  // Initialize the LED matrix panel
  InitMatrix();
}

// Main program loop
// (keeps running until the device is turned off)
void loop() {
  // While the GPRS module is connected to the web server:
  while (client.connected()) {
    // If information is available to receive:
    if (client.available()) {
      // Read and handle incoming request
      ReadRequest();
    }
  }
  // If the GPRS module disconnects from the server:
  // Restart the module
  RestartModule();
  // Attempt another connection to the web server
  RunConnectionProcedure();
}

// Initializes the GPRS module's pins
void InitModulePins() {
  pinMode(8, OUTPUT);  // RST pin
  // Set the default RST pin state - HIGH (normal operation)
  digitalWrite(8, HIGH);
  // Begin the serial communication at 9600 baud rate
  SerialAT.begin(9600);
  // Wait 1000ms
  delay(1000);
}

// Defines the server connection procedure
bool RunConnectionProcedure() {
  // Initialize the GPRS modem
  InitModem();

  // Connect to the ISP's GPRS network
  bool state = ConnectToAPN();
  // If the connection was unsuccessful - abort the procedure
  if (!state) {
    return false;
  }

  // Connect to the web server
  state = ConnectToServer();
  // If the connection was unsuccessful - abort the procedure
  if (!state) {
    return false;
  }

  // Send the device's IMEI to the web server
  SendIMEI();
  // Procedure successful
  return true;
}

// Initializes the GPRS module
void InitModem() {
  // Initialize the modem
  modem.init();
}

// Attempts to establish a connection to the ISP's GPRS network
bool ConnectToAPN() {
  // Connect the modem to the GPRS network
  modem.gprsConnect(apn, gprsUser, gprsPass);
  // If the network doesn't respond within 24s:
  if (!modem.waitForNetwork(240000L)) {
    return false;
  }
  return true;
}

// Attempts to establish a connection to the web server
bool ConnectToServer() {
  // Try connecting to the web server
  // If the connection is unsuccessful:
  if (!client.connect(server, port)) {
    return false;
  }
  // Wait 2000ms
  delay(2000);
  return true;
}

// Sends the device's IMEI to the web server
void SendIMEI() {
  // Retrieve and store the IMEI
  String IMEI = modem.getIMEI();
  // Send the IMEI to the server in the correct format
  client.print("IMEI: " + IMEI);
}

// Hard resets the GPRS module via the RST pin
void RestartModule() {
  // Pull the RST pin low (Reset the module)
  digitalWrite(8, LOW);
  // Wait 500ms
  delay(500);
  // Pull the RST pin high (Enable normal operation)
  digitalWrite(8, HIGH);
  // Wait 2000ms while the module turns on
  delay(2000);
}

// Initializes the LED matrix panel and displays default information
void InitMatrix() {
  // Initialize the matrix
  matrix.begin();
  // Set the text color to white
  matrix.setTextColor(matrix.Color333(7, 7, 7));
  // Set the font size to 1 (8 pixels)
  matrix.setTextSize(1);
  // Move the cursor to the (x=0, y=0) position
  matrix.setCursor(0, 0);
  // Disable text wrap
  matrix.setTextWrap(false);

  // Display a "Wait for data..." message until
  // information is received from the web server
  matrix.println(F("Wait"));
  matrix.setCursor(0, 8);
  matrix.println(F("for"));
  matrix.setCursor(0, 16);
  matrix.println(F("data"));
  matrix.setCursor(0, 24);
  matrix.println(F("..."));
}

char command[4];  // Last received command
char request[4];  // Last received request
char value[4];    // Last received value
int index = 0;    // Index (Used for loops)
char current;     // Current char (Used for reading from the serial port)

char currentState[8] = {"unk unk"};  // Current device state (Default)

// Reads a request received from the web server
void ReadRequest() {
  // Read the incoming command:
  //
  // Read the first character
  current = (char)client.read();
  // Keep reading characters until whitespace or newline is received
  while (current != '\n' && current != ' ') {
    // Store the character
    command[index] = current;
    // Increment the index
    index++;
    // If the command was longer than 3 chars (This shouldn't happen):
    if (index > 3) {
      // Reset the index to prevent out of bounds write
      index = 0;
    }
    // Read another character
    current = (char)client.read();
  }

  // Set the last character to a terminating zero
  // (required for proper storage of char array)
  command[index] = '\0';

  // If the received command is "END":
  if (strcmp(command, "END") == 0) {
    // Close the connection to the web server
    client.stop();
    // Disconnect from the network
    modem.gprsDisconnect();
    return;
  }

  // Reset the index
  index = 0;

  // Read the incoming request:
  //
  // Read the first character
  current = (char)client.read();
  // Keep reading characters until whitespace or newline is received
  while (current != '\n' && current != ' ') {
    // Store the character
    request[index] = current;
    // Increment the index
    index++;
    // If the request was longer than 3 chars (This shouldn't happen):
    if (index > 3) {
      // Reset the index to prevent out of bounds write
      index = 0;
    }
    // Read another character
    current = (char)client.read();
  }

  // Set the last character to a terminating zero
  // (required for proper storage of char array)
  request[index] = '\0';

  // Reset the index
  index = 0;

  // If the incoming command is "SET":
  if (strcmp(command, "SET") == 0) {
    // Handle the SET request
    HandleSet();
  }
  // If the incoming command is "GET":
  else if (strcmp(command, "GET") == 0) {
    // Handle the GET request
    HandleGet();
  }
  // If something went wrong:
  else {
    // Do nothing
    return;
  }
}

// Handles a SET command received from the server
void HandleSet() {
  // Read the value of the command
  ReadValue();

  // If the request is "spd" (Speed limit sign):
  if (strcmp(request, "spd") == 0) {
    // Convert the received value to int for easier calculations later
    int limit = ConvertSpeed();
    // Visualize the speed limit traffic sign with the appropriate value
    VisualizeSpeedLimit(limit);
  }
  // If the request is "wrn" (Warning sign):
  else if (strcmp(request, "wrn") == 0) {
    // Visualize the appropriate warning traffic sign
    VisualizeWarning();
  }
  // If something went wrong:
  else {
    // Do nothing
    return;
  }

  // Update the currently stored device state
  ChangeCurrentState();
  // Send confirmation to the web server
  client.print('k');
}

// Handles a GET command received from the server
void HandleGet() {
  // If the request is "dtl" (Device details):
  if (strcmp(request, "dtl") == 0) {
    // Send the current device details to the web server
    client.print(currentState);
  }
  // If something went wrong:
  else {
    // Do nothing
    return;
  }
}

// Converts the request value to integer
int ConvertSpeed() {
  // Returns the received value converted to int
  return atoi(value);
}

// Reads the value at the end of a SET request
void ReadValue() {
  // Read the first character
  current = (char)client.read();
  // Keep reading characters until whitespace or newline is received
  while (current != '\n' && current != ' ') {
    // Store the character
    value[index] = current;
    // Increment the index
    index++;
    // If the value was longer than 3 chars (This shouldn't happen):
    if (index > 3) {
      // Reset the index to prevent out of bounds write
      index = 0;
    }
    // Read another character
    current = (char)client.read();
  }
  // Set the last character to a terminating zero
  // (required for proper storage of char array)
  value[index] = '\0';

  // Reset the index
  index = 0;

  // Flush the receive buffer (This also shouldn't happen)
  while (client.available()) {
    client.read();
  }
}

// Changes the device state to reflect the currently visualized information
void ChangeCurrentState() {
  int i = 0;  // Index

  // Copy the last received request ot the currentState char array
  for (; i < 3; i++) {
    currentState[i] = request[i];
  }

  // Add a whitespace
  currentState[i] = ' ';
  // Increment the index
  i++;
  // Copy the last received value ot the currentState char array
  for (; i < (strlen(value) + 4); i++) {
    currentState[i] = value[i - 4];
  }

  // Add a terminating zero at the end of the array
  currentState[i] = '\0';
  return;
}

// Displays a speed limit traffic sign with the requested speedLimit
void VisualizeSpeedLimit(int speedLimit) {
  // Draw a large red circle
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  matrix.drawCircle(16, 16, 15, matrix.Color333(7, 0, 0));
  matrix.drawCircle(16, 16, 14, matrix.Color333(7, 0, 0));

  matrix.drawPixel(4, 8, matrix.Color333(7, 0, 0));
  matrix.drawPixel(4, 24, matrix.Color333(7, 0, 0));
  matrix.drawPixel(8, 4, matrix.Color333(7, 0, 0));
  matrix.drawPixel(8, 28, matrix.Color333(7, 0, 0));
  matrix.drawPixel(28, 8, matrix.Color333(7, 0, 0));
  matrix.drawPixel(28, 24, matrix.Color333(7, 0, 0));
  matrix.drawPixel(24, 4, matrix.Color333(7, 0, 0));
  matrix.drawPixel(24, 28, matrix.Color333(7, 0, 0));

  // Draw the speed limit inside the circle in white
  matrix.setTextColor(matrix.Color333(7, 7, 7));

  // Single digit speed limit:
  if (speedLimit < 10) {
    // Set a large font size (24 pixels)
    matrix.setTextSize(3);
    matrix.setCursor(9, 6);
  }
  // Double digit speed limit:
  else if (speedLimit >= 10 && speedLimit < 100) {
    // Set a medium font size (16 pixels)
    matrix.setTextSize(2);
    if (speedLimit < 20) {
      matrix.setCursor(5, 9);
    } else if (speedLimit % 10 == 1) {
      matrix.setCursor(7, 9);
    } else {
      matrix.setCursor(6, 9);
    }
  }
  // Triple digit speed limit:
  else {
    // Set a small font size (24 pixels)
    matrix.setTextSize(1);
    matrix.setCursor(8, 13);
  }

  //
  matrix.println(speedLimit);
}

// Displays the requested warning traffic sign
void VisualizeWarning() {
  if (strcmp(value, "stp") == 0) {
    // Display a stop sign
    VisualizeStopSignWarning();
    return;
  } else if (strcmp(value, "gnr") == 0) {
    // Display a general warning sign (exclamation mark)
    VisualizeGeneralWarning();
    return;
  } else if (strcmp(value, "tfl") == 0) {
    // Display a traffic light warning sign
    VisualizeTrafficLightWarning();
    return;
  } else if (strcmp(value, "nen") == 0) {
    // Display a no entry sign
    VisualizeNoEntryWarning();
    return;
  } else if (strcmp(value, "fon") == 0) {
    // Display a forward only sign
    VisualizeForwardOnlyWarning();
    return;
  } else if (strcmp(value, "lon") == 0) {
    // Display a left only sign
    VisualizeLeftOnlyWarning();
    return;
  } else if (strcmp(value, "ron") == 0) {
    // Display a right only sign
    VisualizeRightOnlyWarning();
    return;
  } else {
    return;
  }
}

// Displays a stop sign
void VisualizeStopSignWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Red octagon
  matrix.fillRect(9, 0, 14, 2, matrix.Color333(7, 0, 0));
  matrix.fillRect(9, 30, 14, 2, matrix.Color333(7, 0, 0));
  matrix.fillRect(0, 9, 2, 14, matrix.Color333(7, 0, 0));
  matrix.fillRect(30, 9, 2, 14, matrix.Color333(7, 0, 0));

  matrix.drawLine(0, 9, 9, 0, matrix.Color333(7, 0, 0));
  matrix.drawLine(1, 9, 9, 1, matrix.Color333(7, 0, 0));
  matrix.drawLine(22, 0, 31, 9, matrix.Color333(7, 0, 0));
  matrix.drawLine(22, 1, 30, 9, matrix.Color333(7, 0, 0));

  matrix.drawLine(0, 22, 9, 31, matrix.Color333(7, 0, 0));
  matrix.drawLine(1, 22, 9, 30, matrix.Color333(7, 0, 0));
  matrix.drawLine(22, 30, 30, 22, matrix.Color333(7, 0, 0));
  matrix.drawLine(22, 31, 31, 22, matrix.Color333(7, 0, 0));

  // White S
  matrix.fillRect(4, 11, 4, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(3, 12, 2, 4, matrix.Color333(7, 7, 7));
  matrix.fillRect(4, 15, 4, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(7, 16, 2, 4, matrix.Color333(7, 7, 7));
  matrix.fillRect(4, 19, 4, 2, matrix.Color333(7, 7, 7));

  // White T
  matrix.fillRect(9, 11, 6, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(11, 13, 2, 8, matrix.Color333(7, 7, 7));

  // White O
  matrix.fillRect(17, 11, 4, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(16, 12, 2, 8, matrix.Color333(7, 7, 7));
  matrix.fillRect(17, 19, 4, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(20, 12, 2, 8, matrix.Color333(7, 7, 7));

  // White P
  matrix.fillRect(23, 11, 5, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(27, 12, 2, 5, matrix.Color333(7, 7, 7));
  matrix.fillRect(23, 16, 5, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(23, 11, 2, 10, matrix.Color333(7, 7, 7));
}

// Displays a general warning sign (exclamation mark)
void VisualizeGeneralWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Red triangle
  matrix.drawTriangle(1, 31, 16, 0, 31, 31, matrix.Color333(7, 0, 0));

  // White exclamation mark
  matrix.drawRect(15, 11, 3, 12, matrix.Color333(7, 7, 7));
  matrix.drawRect(15, 26, 3, 3, matrix.Color333(7, 7, 7));
}

// Displays a traffic light warning sign
void VisualizeTrafficLightWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Red triangle
  matrix.drawTriangle(1, 31, 16, 0, 31, 31, matrix.Color333(7, 0, 0));

  // Red circle
  matrix.fillCircle(16, 14, 2, matrix.Color333(7, 0, 0));
  // Yellow circle
  matrix.fillCircle(16, 20, 2, matrix.Color333(7, 7, 0));
  // Green circle
  matrix.fillCircle(16, 26, 2, matrix.Color333(0, 7, 0));
}

// Displays a no entry sign
void VisualizeNoEntryWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Red circle
  matrix.drawCircle(16, 16, 15, matrix.Color333(7, 0, 0));
  matrix.drawCircle(16, 16, 14, matrix.Color333(7, 0, 0));

  matrix.drawPixel(4, 8, matrix.Color333(7, 0, 0));
  matrix.drawPixel(4, 24, matrix.Color333(7, 0, 0));
  matrix.drawPixel(8, 4, matrix.Color333(7, 0, 0));
  matrix.drawPixel(8, 28, matrix.Color333(7, 0, 0));
  matrix.drawPixel(28, 8, matrix.Color333(7, 0, 0));
  matrix.drawPixel(28, 24, matrix.Color333(7, 0, 0));
  matrix.drawPixel(24, 4, matrix.Color333(7, 0, 0));
  matrix.drawPixel(24, 28, matrix.Color333(7, 0, 0));

  // White rectangle
  matrix.fillRect(6, 14, 21, 5, matrix.Color333(7, 7, 7));
}

// Displays a forward only sign
void VisualizeForwardOnlyWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Blue circle
  matrix.drawCircle(16, 16, 15, matrix.Color333(0, 0, 7));
  matrix.drawCircle(16, 16, 14, matrix.Color333(0, 0, 7));

  matrix.drawPixel(4, 8, matrix.Color333(0, 0, 7));
  matrix.drawPixel(4, 24, matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 4, matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 28, matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 8, matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 24, matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 4, matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 28, matrix.Color333(0, 0, 7));

  // White forward arrow
  matrix.fillRect(15, 14, 3, 13, matrix.Color333(7, 7, 7));

  matrix.fillRect(12, 13, 9, 1, matrix.Color333(7, 7, 7));
  matrix.fillRect(13, 11, 7, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(14, 9, 5, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(15, 7, 3, 2, matrix.Color333(7, 7, 7));
  matrix.drawPixel(16, 6, matrix.Color333(7, 7, 7));
}

// Displays a right only sign
void VisualizeRightOnlyWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Blue circle
  matrix.drawCircle(16, 16, 15, matrix.Color333(0, 0, 7));
  matrix.drawCircle(16, 16, 14, matrix.Color333(0, 0, 7));

  matrix.drawPixel(4, 8, matrix.Color333(0, 0, 7));
  matrix.drawPixel(4, 24, matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 4, matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 28, matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 8, matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 24, matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 4, matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 28, matrix.Color333(0, 0, 7));

  // White right arrow
  matrix.fillRect(12, 13, 3, 12, matrix.Color333(7, 7, 7));
  matrix.fillRect(13, 12, 4, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(14, 11, 3, 1, matrix.Color333(7, 7, 7));

  matrix.fillRect(17, 8, 1, 9, matrix.Color333(7, 7, 7));
  matrix.fillRect(18, 9, 2, 7, matrix.Color333(7, 7, 7));
  matrix.fillRect(20, 10, 2, 5, matrix.Color333(7, 7, 7));
  matrix.fillRect(22, 11, 2, 3, matrix.Color333(7, 7, 7));
  matrix.drawPixel(24, 12, matrix.Color333(7, 7, 7));
}

// Displays a left only sign
void VisualizeLeftOnlyWarning() {
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  // Blue circle
  matrix.drawCircle(16, 16, 15, matrix.Color333(0, 0, 7));
  matrix.drawCircle(16, 16, 14, matrix.Color333(0, 0, 7));

  matrix.drawPixel(4, 8, matrix.Color333(0, 0, 7));
  matrix.drawPixel(4, 24, matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 4, matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 28, matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 8, matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 24, matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 4, matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 28, matrix.Color333(0, 0, 7));

  // White left arrow
  matrix.fillRect(18, 13, 3, 12, matrix.Color333(7, 7, 7));
  matrix.fillRect(16, 12, 4, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(16, 11, 3, 1, matrix.Color333(7, 7, 7));

  matrix.fillRect(15, 8, 1, 9, matrix.Color333(7, 7, 7));
  matrix.fillRect(13, 9, 2, 7, matrix.Color333(7, 7, 7));
  matrix.fillRect(11, 10, 2, 5, matrix.Color333(7, 7, 7));
  matrix.fillRect(9, 11, 2, 3, matrix.Color333(7, 7, 7));
  matrix.drawPixel(8, 12, matrix.Color333(7, 7, 7));
}
