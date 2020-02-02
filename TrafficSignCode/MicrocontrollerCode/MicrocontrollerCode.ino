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
const int defaultSpeedLimit = 50;

#include <TinyGsmClient.h>

// Server details
const char server[] = "37.157.168.186";
const int port = 65432;

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);
TinyGsm modem(SerialAT);
TinyGsmClient client(modem);

void setup() {

  InitSerial();

  //ConnectToServer();

  InitMatrix();
  //delay(500);
  matrix.fillScreen(matrix.Color333(0, 0, 0));
  //VisualizeForwardOnlyWarning();
  // for(int i = 0; i < 200; i++){
  //   VisualizeSpeedLimit(i);
  //   delay(500);
  // }
  //matrix.fillScreen(matrix.Color333(0, 0, 0));
  
}

void loop() {

  // while(client.connected()){
  //   if(client.available()){
  //     ReadCommand();
  //   }
  // }
  // RestartModule();
  // ConnectToServer();
}

void RestartModule() {
  digitalWrite(8, LOW);
  delay(500);
  digitalWrite(8, HIGH);
  delay(2000);
}

void ConnectToServer() {
  InitModem();

  ConnectToAPN();

  AttemptConnect();

  SendIMEI();
}

void InitSerial() {
  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH);

  SerialAT.begin(9600);
  delay(1000);
}

void InitModem() {
  modem.init();
}

void ConnectToAPN() {
  modem.gprsConnect(apn, gprsUser, gprsPass);
  if (!modem.waitForNetwork(240000L)) {
    delay(10000);
    setup();
    return;
  }
}

void AttemptConnect() {
  if (!client.connect(server, port)) {
    delay(10000);
    setup();
    return;
  }
  delay(2000);
}

void SendIMEI() {
  String IMEI = modem.getIMEI();
  client.print("IMEI: " + IMEI);
}

void InitMatrix(){
  matrix.begin();
  matrix.setTextColor(matrix.Color333(7,7,7));
  matrix.setTextSize(1);
  matrix.setCursor(0, 0);
  matrix.setTextWrap(false);
  matrix.println(F("Wait"));
  matrix.setCursor(0, 8);
  matrix.println(F("for"));
  matrix.setCursor(0, 16);
  matrix.println(F("data"));
  matrix.setCursor(0, 24);
  matrix.println(F("..."));
  //delay(2000);
  //matrix.fillScreen(matrix.Color333(0, 0, 0));
}

char command[4];
char request[4];
char value[4];
int index = 0;
char current;

char currentState[8] = {"unk unk"};

void ReadCommand(){
  current = (char) client.read();
  while(current != '\n' && current != ' '){
    command[index] = current;
    index++;
    if(index > 3){
      index = 0;
    }
    current = (char) client.read();
  }
  command[index] = '\0';
  if(strcmp(command, "END") == 0){
    client.stop();
    modem.gprsDisconnect();
    return;   
  }


  index = 0;
  current = (char) client.read();
  while(current != '\n' && current != ' '){
    request[index] = current;
    index++;
    if(index > 3){
      index = 0;
    }
    current = (char) client.read();
  }
  request[index] = '\0';
  index = 0;

  if(strcmp(command, "SET") == 0){
    HandleSet();
  }
  else if(strcmp(command, "GET") == 0){
    HandleGet();
  }
  else{
    VisualizeSpeedLimit(0);
    return;
  }

}

void HandleSet(){
  if(strcmp(request, "spd") == 0){
    int limit = ReadSpeed();
    VisualizeSpeedLimit(limit);
    ChangeCurrentState();
    client.print('k');
  }
  else{
    return;
  }
}

void HandleGet(){
  if(strcmp(request, "dtl") == 0){
    client.print(currentState);
  }
  else{
    return;
  }
}

int ReadSpeed(){
  current = (char) client.read();
  while(current != '\n' && current != ' '){
    value[index] = current;
    index++;
    if(index > 3){
      index = 0;
    }
    current = (char) client.read();
  }
  value[index] = '\0';
  index = 0;
  while(client.available()){
    client.read();
  }
  return atoi(value);
}

void ChangeCurrentState(){

  int i = 0;
  for(; i < 3; i++){
    currentState[i] = request[i];
  }
  currentState[i] = ' ';
  i++;
  for(; i < (strlen(value) + 4); i++){
    currentState[i] = value[i-4];
  }
  currentState[i] = '\0';
  return;
}

void VisualizeSpeedLimit(int speedLimit){
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

  matrix.setTextColor(matrix.Color333(7, 7, 7));

  if(speedLimit < 10){
    matrix.setTextSize(3);
    matrix.setCursor(9,6);
  }
  else if(speedLimit >= 10 && speedLimit < 100){
    matrix.setTextSize(2);
    if(speedLimit < 20){
      matrix.setCursor(5, 9);
    }
    else if(speedLimit%10 == 1){
      matrix.setCursor(7, 9);
    }
    else{
      matrix.setCursor(6, 9);
    }
  }
  else{
    matrix.setTextSize(1);
    matrix.setCursor(8, 13);
  }
  matrix.println(speedLimit);
}

void VisualizeGeneralWarning(){
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  matrix.drawTriangle(1, 31, 16, 0, 31, 31, matrix.Color333(7, 0, 0));
  
  matrix.drawRect(15, 11, 3, 12, matrix.Color333(7, 7, 7));
  matrix.drawRect(15, 26, 3, 3, matrix.Color333(7, 7, 7));
}

void VisualizeTrafficLightWarning(){
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  matrix.drawTriangle(1, 31, 16, 0, 31, 31, matrix.Color333(7, 0, 0));

  matrix.fillCircle(16, 14, 2, matrix.Color333(7, 0, 0));
  matrix.fillCircle(16, 20, 2, matrix.Color333(7, 7, 0));
  matrix.fillCircle(16, 26, 2, matrix.Color333(0, 7, 0));

}

void VisualizeNoEntryWarning(){
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

  matrix.fillRect(6, 14, 21, 5, matrix.Color333(7, 7, 7));

}

void VisualizeForwardOnlyWarning(){
  matrix.fillScreen(matrix.Color333(0, 0, 0));

  matrix.drawCircle(16, 16, 15, matrix.Color333(0, 0, 7));
  matrix.drawCircle(16, 16, 14, matrix.Color333(0, 0, 7));

  matrix.drawPixel(4, 8,    matrix.Color333(0, 0, 7));
  matrix.drawPixel(4, 24,   matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 4,    matrix.Color333(0, 0, 7));
  matrix.drawPixel(8, 28,   matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 8,   matrix.Color333(0, 0, 7));
  matrix.drawPixel(28, 24,  matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 4,   matrix.Color333(0, 0, 7));
  matrix.drawPixel(24, 28,  matrix.Color333(0, 0, 7));

  matrix.fillRect(15, 14, 3, 13, matrix.Color333(7, 7, 7));

  matrix.fillRect(12, 13, 9, 1, matrix.Color333(7, 7, 7));
  matrix.fillRect(13, 11, 7, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(14, 9, 5, 2, matrix.Color333(7, 7, 7));
  matrix.fillRect(15, 7, 3, 2, matrix.Color333(7, 7, 7));
  matrix.drawPixel(16, 6, matrix.Color333(7, 7, 7));

}