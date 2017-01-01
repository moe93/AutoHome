
#include <NewPing.h>
#include <stdio.h>

#define LED       10
#define BUZZER    11
#define TRIGGER   12
#define ECHO      13
#define MIN_DIST  50
//#define ON        1
//#define OFF       0
#define SPEED     115200
#define TIMEOUT   50

String  inByte;
char    buff[50]  = {0};
//byte    state     = 0;
boolean inData    = false;

enum states { ARM, DISARM, ON, OFF };

NewPing sonar(TRIGGER, ECHO); // Initiate distance sensor

#include "functions.h"

void setup() {

  Serial.begin( SPEED );
  Serial.setTimeout( TIMEOUT );

  pinMode(BUZZER, OUTPUT);
  pinMode(LED, OUTPUT);

}
void loop() {
  if (Serial.available()) readSerial();
  execute();
}


