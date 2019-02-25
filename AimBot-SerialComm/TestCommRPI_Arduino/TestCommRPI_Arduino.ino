//Test to valide serial communication between RPI and Arduino
#define ledPinRed 7     


int cmdLedRed = 0;

int ledRed = LOW; 
float setPointSpeed = 0;

int comm = 0;

#include "Communication.h"

//Sending json String to RPI
void updateState(){
  
  state_msg["setPointSpeed"] = setPointSpeed;  

  //Envoie de la commande en cours vers RPI
  send_state_data();
  should_send_ = false;
}

void setup() {
  
  pinMode(ledPinRed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //Look for message on serial port
 analyseMessage(pi_msg);

 //Write message on serail port
 updateState();

 if (cmdLedRed == 1){
  ledRed = HIGH;
 }
 else{
  ledRed = LOW;
 }
 
digitalWrite(ledPinRed, ledRed);
delay(200);
}
