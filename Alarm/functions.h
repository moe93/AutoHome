byte siren(byte state);
void readSerial();
void execute();
enum states deviceState = ARM;

void execute() {
  switch (deviceState) {
    case ARM:
      Serial.print("Device Armed.\n");
      inData = true;
      while (inData) {
        int readings = sonar.ping_cm();
        inByte = Serial.readString();
        if (inByte == "DISARM") {
          deviceState = DISARM;
          inData = false;
          break;
        }
        if (readings <= MIN_DIST) {
          Serial.println("SIRENS ON!");
          //siren(ON);
          byte strLen = sprintf(buff, "Presence detected at %i cm away", readings);
          for (int i = 0; i <= strLen; i++) {
            Serial.print(buff[i]);
          } Serial.print("\n");
        }
      } break;

    case DISARM:
      if (!inData){
        Serial.print("Device Disarmed.\n");
        siren(OFF);
        inData = true;
      } break;

    default: break;
  }
}


// ======================== Read Serial Input ========================
void readSerial() {

  inByte = Serial.readString();

  if (inByte == "ARM") deviceState = ARM;
  else if (inByte == "DISARM") deviceState = DISARM;
  else return;
}



// ======================== SIREN ========================
byte siren(byte state) {
  if (state == ON) {
    int i;
    for (i = 0; i < 255; i = i + 2) {
      analogWrite(LED, i);
      analogWrite(BUZZER, i);
      delay(10);
    }
    for (i = 255; i > 1; i = i - 2) {
      analogWrite(LED, i);
      analogWrite(BUZZER, i);
      delay(5);
    }
    for (i = 1; i <= 10; i++) {
      analogWrite(LED, 255);
      analogWrite(BUZZER, 200);
      delay(100);
      analogWrite(LED, 0);
      analogWrite(BUZZER, 25);
      delay(100);
    }
  }
  else if (state == OFF) {
    analogWrite(BUZZER, 0);
    analogWrite(LED, 0);
  }
  else return 0;
}
