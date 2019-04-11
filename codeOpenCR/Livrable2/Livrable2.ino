/* Constantes */
#define UPDATE_PERIOD_MS    100     // Periode (ms) d'envoie d'etat general
#include <Servo.h>
#include <ros.h>
#include <filtre/toOpenCR.h>
#include <filtre/fromOpenCR.h>

Servo myservo;  // create servo object to control a servo

//Definition des pins
const byte pinPWMMot = 6;
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

int mode =0;
bool launch = false;
//=================================================================================
//============Valeur pour le controlleur PID=======================================
float KpSpeed = 0.5;
float KiSpeed = 0.2;
float KdSpeed = 0;
float lastErrSpeed = 0;

float setPoint = 0;

float errISpeed = 0;
float minI = 0;
float maxI = 100;

float actualSpeed = 0;
float lastSpeed =0;

int cmdMot = 0;

float error = 0;

//=================================================================================
//=================================================================================

//=================================================================================
//============Valeur moteur Dynamixel==============================================
#include <DynamixelWorkbench.h>
#define DEVICE_NAME ""
const char *empty = NULL;
uint32_t baud = 57600; 

DynamixelWorkbench dxl_wb;

uint8_t IDPan = 10;
float KpPan = 0.4;
float KiPan = .02;
float KdPan = 0;
float goalPan = 0;

uint8_t IDTilt = 20;
float KpTilt = 0.4;
float KiTilt = .02;
float KdTilt = 0;
float goalTilt = 0;

float tiltGearRatio = 4.1;





//=================================================================================
//=================================================================================

//=================================================================================
//=====Variable, objet et fonctions ROS============================================
ros::NodeHandle nh;
filtre::fromOpenCR toRPI;

ros::Publisher fromOpenCR("fromOpenCR", &toRPI);

void publishToRPI(){
//Envoyer au RPI via topic "fromOpenCR"
  toRPI.actKp = KpSpeed;
  toRPI.actKi = KiSpeed;
  toRPI.actKd = KdSpeed;
  toRPI.actSpd = actualSpeed;

fromOpenCR.publish(&toRPI);
}


 void subToRPI_cb(const filtre::toOpenCR &fromRPI){
  //Recoit les données du RPI
    KpSpeed = fromRPI.kpSpeed;
    KiSpeed = fromRPI.kiSpeed;
    KdSpeed = fromRPI.kdSpeed;
    KpTilt = fromRPI.kpTilt; 
    KiTilt = fromRPI.kiTilt;
    KdTilt = fromRPI.kdTilt;
    KpPan = fromRPI.kpPan;
    KiPan = fromRPI.kiPan;
    KdPan = fromRPI.kdPan;
    setPoint = fromRPI.ini_spd;
    mode = fromRPI.mode;
    launch = fromRPI.launch;

    goalTilt = fromRPI.tilt_angle;
    goalPan = fromRPI.pan_angle;
    
  
 }

 ros::Subscriber<filtre::toOpenCR> sub("msgToOpenCR", &subToRPI_cb );



//=================================================================================
//=================================================================================


//Fonction d'interruption pour lire les pulses d'encodeur
inline void encoderPulseA(void){
  countPulseA ++;
}

inline void encoderPulseB(void){
  countPulseB ++;
}


int getEncoderCount(void){
  int pulse =0;

  pulse = countPulseA + countPulseB;
  
  return(pulse);
}

int getMotorSpeed(void){
  int actualCount =0;
  float motorSpeed =0;

  actualCount = getEncoderCount();

  motorSpeed = (actualCount - lastCount)/(actualTime-lastTime);// pulse par ms
  motorSpeed = (motorSpeed/ pulsePerRev)* 1000*60; //tr/min

  lastCount = actualCount;

  return(motorSpeed*2);
}

float speedController(){
  /* Fonction du controlleur de position */
  
  /* les valeurs de SP, PV et CO sont tous converti en pourcentage afin d'avoir des unité de base commune pour le controle.
   * le CO est converti de pourcentage vers puissance moteur .
   */
  

  float setPointPID;
  float setPointPourc;
  float actualSpeedPourc;

  float P_;
  float I_;
  float D_;

  setPointPID = setPoint;

  setPointPID = setPointPID * 60 / (2*3.1416);
  
  setPointPourc = map(setPointPID, 0 , 1030, 0 ,100);
  actualSpeedPourc = map(actualSpeed, 0 , 1030, 0 ,100);

  
  
  error = setPointPourc - actualSpeedPourc;

  P_ = error * KpSpeed;
  errISpeed += error;
  errISpeed = constrain(errISpeed,-100, 100);
  //errISpeed = constrain(errISpeed,-1030, 1030);
  I_ = errISpeed * KiSpeed;

  if (I_ > maxI) 
    I_ = maxI;

  if (I_< minI)
    I_ = minI;
    
  D_ = (error - lastErrSpeed) *KdSpeed;

  cmdMot = P_ + I_ + D_;
  lastErrSpeed = error;

  cmdMot = map(cmdMot, 0 , 100 , 0, 255);



 //On s'assure que la commande ne depasse pas les valeurs extremes   
  if(cmdMot < 0)
    cmdMot = 0;

  if(cmdMot > 255)
    cmdMot = 255;
  digitalWrite(pinDirMot, HIGH);
  analogWrite(pinPWMMot, cmdMot);
    
}

void feedBall() {
  int pos;

  for(pos = 50; pos>=0; pos-=1)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 

  delay(50);
  
  for(pos = 0; pos <= 50; pos += 1) // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(10);                       // waits 15ms for the servo to reach the position 
  } 

  delay(1000);
}

void updateTiltAngle(){
  float goal;
  goal = map(goalTilt, 0, 360, 0, 4095);
  goal = goal*tiltGearRatio; //Apply gear ratio

  if(goal > 3498){
    goal = 3498;
  }
  dxl_wb.goalPosition(IDTilt, (int32_t)goal, &empty);
  
}

void updatePanAngle(){
  float goal;
  goal = map(goalPan, -10, 350, 0, 4095);
  //goal = goal*tiltGearRatio; //Apply gear ratio

  if(goal > 319){
    goal = 319;
  }
  dxl_wb.goalPosition(IDPan, (int32_t)goal, &empty);
  
}



bool test = false;

void setup() {
//Serial.begin(57600);
//while(!Serial);

//================ROS=====================
  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.advertise(fromOpenCR);
  nh.subscribe(sub);

//========================================
//================Dynamixel===============
  dxl_wb.init(DEVICE_NAME, baud, &empty);
  //Serial.println(empty);
  dxl_wb.ping(IDPan, &empty);
  dxl_wb.ping(IDTilt, &empty);
  //Serial.println(empty);
  dxl_wb.torqueOff(IDPan, &empty);
  dxl_wb.torqueOff(IDTilt, &empty);
  //Serial.println(empty);
  dxl_wb.jointMode(IDPan,(int32_t)0, (int32_t)0, &empty);
  dxl_wb.jointMode(IDTilt,(int32_t)0, (int32_t)0, &empty);
  //Serial.println(empty);
  dxl_wb.torqueOn(IDPan, &empty);
  dxl_wb.torqueOn(IDTilt, &empty);
  //Serial.println(empty);
  dxl_wb.ledOn(IDPan, &empty);
  dxl_wb.ledOn(IDTilt, &empty);
  //Serial.println(empty);

//========================================
  
  pinMode(encoderA, INPUT);
  pinMode(encoderB, INPUT);
  pinMode(pinDirMot, OUTPUT);
  pinMode(pinPWMMot, OUTPUT);

  myservo.attach(pinServo);  // attaches the servo on GIO2 to the servo object 
  myservo.write(50);

  attachInterrupt(digitalPinToInterrupt(encoderA),encoderPulseA, RISING);
  attachInterrupt(digitalPinToInterrupt(encoderB),encoderPulseB, RISING);
  
}


void loop() {

 
 actualTime = millis();

 updateTiltAngle();
 updatePanAngle();
 //Serial.println(empty);

 actualSpeed = getMotorSpeed();

 if(actualSpeed > 1030){
  actualSpeed = lastSpeed;
 }
 
 speedController();

 if(digitalRead(obSwitch1) or launch){
  feedBall();
 }

 
 lastTime = actualTime;
 lastSpeed = actualSpeed;

 publishToRPI();
 nh.spinOnce();
 
 delay(50);

}
