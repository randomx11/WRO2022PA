// Include the library
#include <Servo.h>

int pos = 0;

#define S0 8
#define S1 7
#define S2 4
#define S3 2
#define sensorOut 13

// Stores frequency read by the photodiodes
int redFrequency = 0;
int greenFrequency = 0;
int blueFrequency = 0;

bool buttonpressed = false;

// Create the servo object
Servo myservo;
Servo myservo2;
Servo myservo3;


// Setup section to run once
void setup() {
  myservo.attach(9); // attach the servo to our servo object
  myservo2.attach(10); // attach the servo to our servo object
  myservo3.attach(11);
  Serial.begin(9600);
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  
  pinMode(12, INPUT_PULLUP);
  
  pinMode(sensorOut, INPUT);
  
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  myservo.write(90); 
  myservo2.write(90);
  
}

// Loop to keep the motor turning!
void loop() {
  sensor();
for(pos = 0; pos <= 180; pos += 1)
if (Serial.available()){
 int state = Serial.parseInt();
 if(digitalRead(12) == HIGH){
 buttonpressed = true;
 Serial.println("Button Pressed");
 }
if(buttonpressed == true){
myservo.write(360);
myservo2.write(-360); // rotate the motor counterclockwise    
if (state < 5){
Serial.print(">");
Serial.println(state);
Serial.println("cannot execute, too low");
}

if (state >= 5 && state < 170)
{
  Serial.print(">");
  Serial.println(state);
  Serial.print("turning servo to ");
  Serial.print(state);
  Serial.println(" degrees");
  myservo3.write(state); 
  delay(2000);
  myservo3.write(90);
}
if (state >= 180 || state <= 10){
 int state = 0; 
}
if (redFrequency <= 32 && greenFrequency <= 45 && blueFrequency <= 36){
  myservo3.write(120);
}
if (redFrequency <= 48 && greenFrequency <= 49 && blueFrequency <= 35){
  myservo3.write(90);
}
}
}
}
void sensor() {
  // Setting RED (R) filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  
  // Reading the output frequency
  redFrequency = pulseIn(sensorOut, LOW);
  
   // Printing the RED (R) value
  //Serial.print("R = ");
  //Serial.print(redFrequency);
  delay(100);
  
  // Setting GREEN (G) filtered photodiodes to be read
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  
  // Reading the output frequency
  greenFrequency = pulseIn(sensorOut, LOW);
  
  // Printing the GREEN (G) value  
  //Serial.print(" G = ");
  //Serial.print(greenFrequency);
  delay(100);
 
  // Setting BLUE (B) filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  
  // Reading the output frequency
  blueFrequency = pulseIn(sensorOut, LOW);
  
  // Printing the BLUE (B) value 
  //Serial.print(" B = ");
  //Serial.println(blueFrequency);
  delay(100);
}
