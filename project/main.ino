#include "AccelStepper.h"

// Define stepper motor connections and interface type
#define DIR_PIN_X   5
#define STEP_PIN_X  2
#define DIR_PIN_Y   6
#define STEP_PIN_Y  3
#define ENA_PIN     8

#define X_LIMIT_PIN 9
#define Y_LIMIT_PIN 10

#define ELECTRO_PIN 11 // for now it doesn't work
#define PUMP_PIN 13

float maxSpeed = 1000.0;
float maxAccel = 500.0;

float homingSpeed = 80.0;

// Create stepper instances
AccelStepper stepperX(AccelStepper::DRIVER, STEP_PIN_X, DIR_PIN_X);
AccelStepper stepperY(AccelStepper::DRIVER, STEP_PIN_Y, DIR_PIN_Y);

// Function prototypes
void enableMotors();
void disableMotors();
void enablePump();
void disablePump();
void setSpeedAccel(float speed, float accel);
bool XlimitIsPressed();
bool YlimitIsPressed();
void runSteppers();
void homing();
void moveTo(long X_coord, long Y_coord);
void gotoX(long X_coord);

void setup() {
  Serial.begin(9600);

  pinMode(ENA_PIN, OUTPUT);
  pinMode(PUMP_PIN, OUTPUT);
  disablePump();
  pinMode(X_LIMIT_PIN, INPUT_PULLUP);
  pinMode(Y_LIMIT_PIN, INPUT_PULLUP);
  delay(1000);

  disableMotors();
  Serial.println("Puzzle Bot");
  
  setSpeedAccel(maxSpeed, maxAccel);
  homing();
}

void loop() {
  // Your main code here
}

//------------------- Functions --------------------

void enableMotors(){
  digitalWrite(ENA_PIN, LOW);
  Serial.println("Driver Enabled");
}

void disableMotors(){
  digitalWrite(ENA_PIN, HIGH);
  Serial.println("Driver Disabled");
}

void enablePump(){
  digitalWrite(PUMP_PIN, LOW);
  Serial.println("Pump Enabled");
}

void disablePump(){
  digitalWrite(PUMP_PIN, HIGH);
  Serial.println("Pump Disabled");
}

void setSpeedAccel(float speed, float accel){
  stepperX.setMaxSpeed(speed);
  stepperX.setAcceleration(accel);
  stepperY.setMaxSpeed(speed);
  stepperY.setAcceleration(accel);
}

bool XlimitIsPressed(){
  if(digitalRead(X_LIMIT_PIN) == LOW){
    Serial.println("X limit pressed");
    return true;
  }
  return false;
}

bool YlimitIsPressed(){
  if(digitalRead(Y_LIMIT_PIN) == LOW){
    Serial.println("Y limit pressed");
    return true;
  }
  return false;
}

void runSteppers(){
  stepperX.run();
  stepperY.run();
}

void homing(){
  Serial.println("Homing Begin");
  enableMotors();

  // Homing X
  stepperX.setSpeed(homingSpeed);  // negative speed if limit switch is at lower position
  while(!XlimitIsPressed()){
    stepperX.runSpeed();
  }
  stepperX.stop();
  stepperX.setCurrentPosition(0);
  stepperX.runToNewPosition(-750);  // move away from switch
  Serial.println("Homing X OK");

  // Homing Y
  stepperY.setSpeed( homingSpeed);
  while(!YlimitIsPressed()){
    stepperY.runSpeed();
  }
  stepperY.stop();
  stepperY.setCurrentPosition(0);
  stepperY.runToNewPosition(-500);
  Serial.println("Homing Y OK");

  disableMotors();
}

void gotoX(long X_coord){
  enableMotors();
  stepperX.moveTo(-X_coord); // negative if inverted
  while(stepperX.distanceToGo() != 0){
    stepperX.run();
  }
  disableMotors();
}

void moveTo(long X_coord, long Y_coord){
  enableMotors();
  stepperX.moveTo(-X_coord);
  stepperY.moveTo(Y_coord);
  while(stepperX.distanceToGo() != 0 || stepperY.distanceToGo() != 0){
    stepperX.run();
    stepperY.run();
  }
  disableMotors();
}