#ifndef Comm
#define Comm

#include "SimpleTimer.h"    // Librairie de chronomètres
#include "ArduinoJson.h"    // Librairie de syntaxe JSON

//========================================================================================================
//========================================================================================================
//======================Variables communication===========================================================

// Contrôle du temps
bool    should_send_ ;        // Indique qu'on est prêt à transmettre l'état.
SimpleTimer timer;                  // objet du chronomètre

// Message objects
StaticJsonBuffer<500> jsonBuffer;
JsonVariant pi_msg = jsonBuffer.createObject();
JsonObject& state_msg = jsonBuffer.createObject();



//========================================================================================================
//========================================================================================================
//======================Fonction de communication=========================================================
void timerCallback(){
  /* Rappel du chronometre */
  should_send_ = true;          // Indique qu'on est prêt à mettre à jour et transmettre
}

void analyseMessage(JsonVariant msg){
  /* Fonction d'analyse du message recu */
  JsonVariant parse_msg;
  // Determiner si le message est un succes
  if (!msg.success()) {
    // Condition d'erreur : On ignore.
    return;
  }

 
  parse_msg =  msg["ini_spd"];
  if(parse_msg.success()){
    setPointSpeed = msg["ini_spd"];
    
  }
}


void serialEvent(){
  /* Rappel lors de reception sur port serie */
  StaticJsonBuffer<500> jsonBuffer;
  JsonObject& root = jsonBuffer.parseObject(Serial);
  pi_msg = root;
}


void send_state_data(){
  /* Fonction pour envoie de l'etat */
  state_msg.printTo(Serial); // Met le message en attente dans le port serie
  Serial.println();// Envoie le message
}


#endif
