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

  SerialMon.begin(115200);
  delay(10);
  SerialMon.println("Wait...");

  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);

  SerialAT.begin(9600);
  delay(3000);

  SerialMon.println("Initializing modem...");
  //modem.restart();
  modem.init();

  // SerialMon.print("Waiting for network...");
  // if (!modem.waitForNetwork(240000L)) {
  //   SerialMon.println(" fail");
  //   delay(10000);
  //   return;
  // }
  // SerialMon.println(" OK");

  // if (modem.isNetworkConnected()) {
  //   SerialMon.println("Network connected");
  // }

  SerialMon.print(F("Connecting to "));
  SerialMon.print(apn);
  if (!modem.gprsConnect(apn, gprsUser, gprsPass)) {
    SerialMon.println(" fail");
    delay(10000);
    return;
  }
  SerialMon.println(" OK");


  SerialMon.print("Connecting to ");
  SerialMon.println(server);
  if (!client.connect(server, port)) {
    SerialMon.println(" fail");
    delay(10000);
    return;
  }
  SerialMon.println(" OK");

  delay(2000);
  // Make a HTTP GET request:
  SerialMon.println("Sending ICCID...");
  String IMEI = modem.getIMEI();
  //client.println();
  client.println("IMEI: " + IMEI);

  unsigned long timeout = millis();
  while (client.connected() && millis() - timeout < 10000L) {
    // Print available data
    while (client.available()) {
      char c = client.read();
      SerialMon.print(c);
      timeout = millis();
    }
  }
  SerialMon.println();

  client.stop();
  modem.gprsDisconnect();


}

void loop() {

  // Shutdown

  //client.stop();
  //SerialMon.println(F("Server disconnected"));

//#if TINY_GSM_USE_GPRS
    //modem.gprsDisconnect();
    //SerialMon.println(F("GPRS disconnected"));
//#endif

  // Do nothing forevermore
  while (true) {
    delay(1000);
  }
}