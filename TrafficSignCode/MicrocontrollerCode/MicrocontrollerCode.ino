#define TINY_GSM_MODEM_SIM800
#define TINY_GSM_DEBUG SerialMon

#define SerialMon Serial
#define SerialAT SoftwareSerial

#include <SoftwareSerial.h>
SoftwareSerial SerialAT(3, 2); // RX, TX


// Your GPRS credentials
// Leave empty, if missing user or pass
const char apn[]  = "internet.vivacom.com";
const char gprsUser[] = "VIVACOM";
const char gprsPass[] = "VIVACOM";

// Server details
const char server[] = "37.157.168.186";

#include <TinyGsmClient.h>

TinyGsm modem(SerialAT);
TinyGsmClient client(modem);
const int port = 65432;


void setup() {

  InitSerial();

  InitModem();

  ConnectToAPN();

  AttemptConnect();

  SendIMEI();

  ReadData();

  SerialMon.println("Disconnected, stopping...");
  client.stop();
  modem.gprsDisconnect();


}

void loop() {

  // Shutdown

  //client.stop();
  //SerialMon.println(F("Server disconnected"));
    //modem.gprsDisconnect();
    //SerialMon.println(F("GPRS disconnected"));

  // Do nothing forevermore
  while (true) {
    delay(1000);
  }
}


void RestartModule() {
  digitalWrite(8, LOW);
  delay(500);
  digitalWrite(8,HIGH);
}

void InitSerial() {
  SerialMon.begin(115200);
  delay(10);
  SerialMon.println("Wait...");

  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);

  SerialAT.begin(9600);
  delay(3000);

}

void InitModem() {
  SerialMon.println("Initializing modem...");
  //modem.restart();
  modem.init();
}

void ConnectToAPN() {
  SerialMon.print(F("Connecting to "));
  SerialMon.print(apn);
  if (!modem.gprsConnect(apn, gprsUser, gprsPass)) {
    SerialMon.println(" fail");
    setup();
    return;
  }
  SerialMon.println(" OK");
}

void AttemptConnect() {
  SerialMon.print("Connecting to ");
  SerialMon.println(server);
  if (!client.connect(server, port)) {
    SerialMon.println(" fail");
    setup();
    return;
  }
  SerialMon.println(" OK");

  delay(2000);
}

void SendIMEI() {
  SerialMon.println("Sending IMEI...");
  String IMEI = modem.getIMEI();
  client.print("IMEI: " + IMEI);
}

void ReadData() {
  unsigned long timeout = millis();
  while (client.connected()){ //&& millis() - timeout < 10000L) {
    // Print available data
    int incomingDataLength = client.available();
    if(incomingDataLength){
      char command[3] = "";
      char request[3] = "";
      char value[3] = "";
      for (int i = 0; i < 3; i++){
          char current = client.read();
          command[i] = current;
          SerialMon.print(current);
      }
      client.read();
      SerialMon.print('\n');
      for (int i = 0; i < 3; i++){
          char current = client.read();
          request[i] = current;
          SerialMon.print(current);
      }
      client.read();
      SerialMon.print('\n');
      int i = 0;
      while(client.available()){
        char current = client.read();
        value[i] = current;
        i++;
        SerialMon.print(current);
      }
      SerialMon.print('\n');
    }
  }
}