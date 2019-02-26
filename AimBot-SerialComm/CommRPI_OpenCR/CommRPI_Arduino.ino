#include <Communication.h>
/* Constantes */
#define UPDATE_PERIOD_GEN  100  // Periode (ms) d'envoie d'etat general
#define BAUD                115200  // Fréquence de transmission sérielle (bauds)
#define UPDATE_PERIOD_MS    100     // Periode (ms) d'envoie d'etat general

Servo myservo;  // create servo object to control a servo 

//Definition des pins
const byte pinPWMMot = 5;
const byte pinDirMot = 7;
const byte encoderA = 2;
const byte encoderB = 3;
const byte obSwitch1 = 34;
const byte pinServo = 9;

float actualTime =0;
float lastTime =0;

float pulsePerRev = 464.64;

int countPulseA =0;
int countPulseB =0;
int lastCount =0;

int comm = 0;
//=================================================================================
//============Valeur pour le controlleur PID=======================================
float KpSpeed = 0.8;
float KiSpeed = 0.002;
float KdSpeed = 0;
float lastErrSpeed = 0;



float errISpeed = 0;
float minI = 0;
float maxI = 100;

float actualSpeed = 0;

//=================================================================================
//=================================================================================
//communication
void updateState(){
  
  state_msg["setPoint"] = setPoint;  

  //Envoie de la commande en cours vers RPI
  send_state_data();
  should_send_ = false;
}
//====================================================
//controle
inline void encoderPulseA(void){
  countPulseA ++;
}

inline void encoderPulseB(void){
  countPulseB ++;
}

int getEncoderCount(void){
  int pulse =0;

  pulse = countPulseA + countPulseB;
  //countPulseA =0;
  //countPulseB =0;
  
  return(pulse);
}

int getMotorSpeed(void){
  int actualCount =0;
  float motorSpeed =0;

  actualCount = getEncoderCount();

  motorSpeed = (actualCount - lastCount)/(actualTime-lastTime);// pulse par ms
  motorSpeed = (motorSpeed/ pulsePerRev)* 1000*60; //tr/min

  lastCount = actualCount;

  return(motorSpeed);
}

float speedController(){
  /* Fonction du controlleur de position */
  
  /* les valeurs de SP, PV et CO sont tous converti en pourcentage afin d'avoir des unité de base commune pour le controle.
   * le CO est converti de pourcentage vers puissance moteur .
   */
  float cmdMot = 0.0;
  float error = 0;

  float setPointPourc;
  float actualSpeedPourc;

  float P_;
  float I_;
  float D_;
  
  setPointPourc = map(setPoint, 1030 , 0, 100 ,0);
  actualSpeedPourc = map(actualSpeed, 1030 , 0, 100 ,0);
  
  error = setPointPourc - actualSpeedPourc;

  P_ = error * KpSpeed;
  errISpeed += error;
  I_ = errISpeed * KiSpeed;

  if (I_ > maxI) 
    I_ = maxI;

  if (I_< minI)
    I_ = minI;
    
  D_ = (error - lastErrSpeed) *KdSpeed;

  cmdMot = P_ + I_ + D_;
  lastErrSpeed = error;

  cmdMot = map(cmdMot, 100 , 0 , 255, 0);



 //On s'assure que la commande ne depasse pas les valeurs extremes   
  if(cmdMot < -255)
    cmdMot = -255;

  if(cmdMot > 255)
    cmdMot = 255;

  analogWrite(pinPWMMot, cmdMot);
    
}

void feedBall() {
  int pos;

  for(pos = 0; pos <= 50; pos += 1) // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(10);                       // waits 15ms for the servo to reach the position 
  } 
  for(pos = 50; pos>=0; pos-=1)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  delay(1000);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  myservo.attach(pinServo);  // attaches the servo on GIO2 to the servo object 

  pinMode(encoderA, INPUT);
  pinMode(encoderB, INPUT);

  attachInterrupt(digitalPinToInterrupt(encoderA),encoderPulseA, RISING);
  attachInterrupt(digitalPinToInterrupt(encoderB),encoderPulseB, RISING);
  
}


void loop() {

 
 actualTime = millis();
 //Serial.println(countPulseA);
 //Serial.println(countPulseB);
 //Serial.println(actualTime);
 //Serial.println("*************");

 actualSpeed = getMotorSpeed();
 speedController();
 analyseMessage(pi_msg);
 updateState();
 
 if(digitalRead(obSwitch1)){
  //Serial.println("feed ball");
  feedBall();
 }
 //Serial.println(actualSpeed);
 //Serial.println(lastTime);
 //Serial.println("#############");

 lastTime = actualTime;
 delay(200);

}
