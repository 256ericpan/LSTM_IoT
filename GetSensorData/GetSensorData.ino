// potentiometer_read.ino
// reads a potentiometer and sends value over serial
/* for Grove Beginner Kit, 
A0 = sound
A1 = potentiometer
A2 = light
A3 = magnet


*/
int sensorPin = A2;  // The potentiometer on pin 0                  
int ledPin = 13;     // The LED is connected on pin 13
int sensorValue;     // variable to stores data

void setup() // runs once when the sketch starts
{
  // make the LED pin (pin 13) an output pin
  pinMode(ledPin, OUTPUT);

  // initialize serial communication
  Serial.begin(9600);
}

void loop() // runs repeatedly after setup() finishes
{
  sensorValue = analogRead(sensorPin);  // read pin A0   
  Serial.println(sensorValue);         // send data to serial

  if (sensorValue < 500) {            // less than 500?
    digitalWrite(ledPin, LOW); }     // Turn the LED off

  else {                               // greater than 500?
    digitalWrite(ledPin, HIGH); }     // Keep the LED on

  delay(100);             // Pause 100 milliseconds
}
