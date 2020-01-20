#include <SoftwareSerial.h>

//Create software serial object to communicate with SIM800L
SoftwareSerial mySerial(3, 2); //SIM800L Tx & Rx is connected to Arduino #3 & #2

void setup()
{
  //Begin serial communication with Arduino and Arduino IDE (Serial Monitor)
  Serial.begin(9600);
  
  //Begin serial communication with Arduino and SIM800L
  mySerial.begin(9600);

  Serial.println("Initializing...");
  delay(1000);

  mySerial.println("AT");
  updateSerial();
  mySerial.println("AT+CFUN=1");
  updateSerial();
  mySerial.println("AT+CSTT=\"internet.vivacom.com\",\"VIVACOM\",\"VIVACOM\"");
  updateSerial();
  mySerial.println("AT+CIICR");
  updateSerial();
  mySerial.println("AT+CIPSTART=\"TCP\",\"37.157.168.186\",65432");
  updateSerial();
 
}

void loop()
{
  updateSerial();
}

void updateSerial()
{
  delay(500);
  while (Serial.available()) 
  {
    mySerial.write(Serial.read());//Forward what Serial received to Software Serial Port
  }
  while(mySerial.available()) 
  {
    int data = 0;
    data = mySerial.read();
    Serial.write(data);//Forward what Software Serial received to Serial Port
  }
}
