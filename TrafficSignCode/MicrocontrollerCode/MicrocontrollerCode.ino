#include <RGBmatrixPanel.h>

#define TINY_GSM_MODEM_SIM800

#define SerialAT Serial

#define CLK 11
#define OE  9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

const char apn[]  = "internet.vivacom.com";
const char gprsUser[] = "VIVACOM";
const char gprsPass[] = "VIVACOM";

#include <TinyGsmClient.h>

// Server details
const char server[] = "37.157.168.186";
const int port = 65432;

//RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);

void setup() {
  TinyGsm modem(SerialAT);
  TinyGsmClient client(modem);

  InitSerial();

  InitModem(modem);

  ConnectToAPN(modem);

  AttemptConnect(client);

  SendIMEI(modem, client);
  
  //Visualize(client);

  //ReadData();

  //SerialMon.println("Disconnected, stopping...");
  //client.stop();
  //modem.gprsDisconnect();

}

char command[4];
int index = 0;
char current;


void loop() {
  int currentValue = 30;
  RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);
  matrix.begin();
  matrix.drawCircle(16, 16, 15, matrix.Color333(1, 0, 0));
  matrix.setTextColor(matrix.Color333(1,1,1));
  matrix.setTextSize(2);
  matrix.setCursor(6, 9);
  matrix.println(currentValue);
  int newValue = 0;
  while(true){
    if(SerialAT.available()){
      //newValue = ReadData(currentValue);
      newValue = currentValue+1;
      matrix.fillScreen(matrix.Color333(0,0,0));
      matrix.drawCircle(16, 16, 15, matrix.Color333(1, 0, 0));
      matrix.setTextColor(matrix.Color333(1,1,1));
      matrix.setCursor(6, 9);
      matrix.println(newValue);
      currentValue = newValue;
    }
  }
}

void Visualize(TinyGsmClient client){
  int currentValue = 30;
  RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);
  matrix.begin();
  matrix.drawCircle(16, 16, 15, matrix.Color333(1, 0, 0));
  matrix.setTextColor(matrix.Color333(1,1,1));
  matrix.setTextSize(2);
  matrix.setCursor(6, 9);
  matrix.println(currentValue);
  int newValue = 0;
  while(true){
    if(client.available()){
      //newValue = ReadData(currentValue);
      newValue = currentValue+1;
      matrix.fillScreen(matrix.Color333(0,0,0));
      matrix.drawCircle(16, 16, 15, matrix.Color333(1, 0, 0));
      matrix.setTextColor(matrix.Color333(1,1,1));
      matrix.setCursor(6, 9);
      matrix.println(newValue);
      currentValue = newValue;
    }
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
  delay(1000);

}

void InitModem(TinyGsm modem) {
  modem.restart();
}

void ConnectToAPN(TinyGsm modem) {
  modem.gprsConnect(apn, gprsUser, gprsPass);
  if (!modem.waitForNetwork(240000L)) {
    delay(10000);
    setup();
    return;
  }
}

void AttemptConnect(TinyGsmClient client) {
  if (!client.connect(server, port)) {
    delay(10000);
    setup();
    return;
  }
  delay(2000);
}

void SendIMEI(TinyGsm modem, TinyGsmClient client) {
  String IMEI = modem.getIMEI();
  client.print("IMEI: " + IMEI);
}

int ReadData(int currentValue){

  while(SerialAT.available() > 0){
    current = (char) SerialAT.read();
    if(current == '\n'){
      command[index] = '\0';
      index = 0;
      return 1;
    }
    else{
      command[index] = current;
    }
    index++;
    if(index >= 3){
      index = 0;
      return 2;
    }
  }
  return 0;
  //   Serial.read();
  //   if(command != 'S'){
  //     return currentValue+1;
  //   }

  //   request = Serial.read();
  //   Serial.read();

  //   int i = 0;
  //   while (Serial.available())
  //   {
  //     char current = Serial.read();
  //     Serial.print(current);
  //     if(current == '\n'){
        
  //     }
  //     else{
  //       value[i] = current;
  //     }
  //     i++;
  //   Serial.println(current);
  //   }
  // }
  //return atoi(value);
}
