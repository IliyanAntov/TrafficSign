#include <SoftwareSerial.h>
#include <RGBmatrixPanel.h>

#define SerialAT Serial

#define CLK 11
#define OE  9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

#define ConnectionString "AT+CSTT=internet.vivacom.com, VIVACOM, VIVACOM"

// Server details
const char server[] = "37.157.168.186";
const int port = 65432;

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);

void setup() {
  matrix.begin();

  // draw a pixel in solid white
  matrix.drawPixel(0, 0, matrix.Color333(1, 1, 1));
  delay(2500);
  matrix.updateDisplay();
  InitSerial();

  InitModem();

  ConnectToAPN();
  matrix.drawPixel(0, 0, matrix.Color333(1, 1, 1));
  delay(2500);
  matrix.updateDisplay();
  //AttemptConnect();

  //SendIMEI();


  //ReadData();

  //SerialMon.println("Disconnected, stopping...");
  //client.stop();
  //modem.gprsDisconnect();


}

void loop() {
    while(Serial.available()){
      char c = Serial.read();
      matrix.fillScreen(matrix.Color333(0, 0, 0));
      matrix.setTextColor(matrix.Color333(1,0,0));
      matrix.setCursor(1, 0);
      matrix.println(c);
      delay(1000);
    }

}


void RestartModule() {
  digitalWrite(8, LOW);
  delay(500);
  digitalWrite(8, HIGH);
}

void InitSerial() {

  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);

  SerialAT.begin(9600);
  delay(3000);

}

void InitModem() {
  SerialAT.print("AT+CFUN=0");
  delay(3000);
  SerialAT.print("AT+CFUN=1");
  delay(3000);
}

void ConnectToAPN() {
  // char command[80];
  // strcpy(command, "AT+CSTT=");
  // strcat(command, apn);
  // strcat(command, ", ");
  // strcat(command, gprsUser);
  // strcat(command, ", ");
  // strcat(command, gprsPass);
    ("asd");
  delay(3000);
  //SerialMon.println(" OK");
}

// void AttemptConnect() {
//   //SerialMon.print("Connecting to ");
//   //SerialMon.println(server);
//   if (!client.connect(server, port)) {
//     //SerialMon.println(" fail");
//     setup();
//     return;
//   }
//   //SerialMon.println(" OK");

//   delay(2000);
// }

// void SendIMEI() {
//   //SerialMon.println("Sending IMEI...");
//   String IMEI = modem.getIMEI();
//   client.print("IMEI: " + IMEI);
// }

// void ReadData() {
//   unsigned long timeout = millis();
//   int currentValue = 50;
//   matrix.fillScreen(matrix.Color333(1, 1, 1));
//   delay(1000);
//   matrix.fillScreen(matrix.Color333(0, 0, 0));
//   matrix.setCursor(1, 0);    // start at top left, with one pixel of spacing
//   matrix.setTextSize(1);     // size 1 == 8 pixels high
//   matrix.setTextWrap(false); // Don't wrap at end of line - will do ourselves

//   matrix.setTextColor(matrix.Color333(1,1,1));
//   matrix.println("asd");
//   while (client.connected()){ //&& millis() - timeout < 10000L) {
//     // Print available data
//     int incomingDataLength = client.available();
//     if(incomingDataLength){
//       char command[3] = "";
//       char request[3] = "";
//       char value[3] = "";
//       for (int i = 0; i < 3; i++){
//           char current = client.read();
//           command[i] = current;
//           //SerialMon.print(current);
//       }
//       client.read();
//       //SerialMon.print('\n');
//       for (int i = 0; i < 3; i++){
//           char current = client.read();
//           request[i] = current;
//           //SerialMon.print(current);
//       }
//       client.read();
//       //SerialMon.print('\n');
//       int i = 0;
//       while(client.available()){
//         char current = client.read();
//         value[i] = current;
//         i++;
//         //SerialMon.print(current);
//       }
//       //SerialMon.print('\n');
//       currentValue = atoi(value);
//       //SerialMon.print("New value: ");
//       //SerialMon.print(currentValue);
//       matrix.fillScreen(matrix.Color333(0, 0, 0));
//       matrix.setCursor(1, 0);    // start at top left, with one pixel of spacing
//       matrix.setTextColor(matrix.Color333(1,0,0));
//       matrix.println("ASd");
//     }
//   }
// }
