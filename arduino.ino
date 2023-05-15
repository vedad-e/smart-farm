// Sensor pins
#include <dht.h>
dht DHT;

#define sensorSoilPower 2
#define sensorSoil2Power 3
#define sensorRainPower 4

#define sensorPinSoil 8
#define sensorPinSoil2 7
#define sensorPinRain 6
#define sensorPinDht11 5

#define outSoil 13
#define outSoil2 12
#define outRain 11
#define outDht11 10

const int TEMP_THRESHOLD_UPPER = 27; 
const int TEMP_THRESHOLD_LOWER = 20; 

void setup() {
  pinMode(sensorSoilPower, OUTPUT);
  pinMode(sensorSoil2Power, OUTPUT);
  pinMode(sensorRainPower, OUTPUT);
  
  pinMode(outSoil, OUTPUT);
  pinMode(outSoil2, OUTPUT);
  pinMode(outRain, OUTPUT);
  pinMode(outDht11, OUTPUT);

  // Initially keep the sensor OFF
  digitalWrite(sensorSoilPower, LOW);
  digitalWrite(sensorSoil2Power, LOW);
  digitalWrite(sensorRainPower, LOW);

  Serial.begin(9600);
}

void loop() {
  //get the reading from the function below and print it
  int valSoil = readSensorSoil();
  int valSoil2 = readSensorSoil2();
  int valRain = readSensorRain();
  int valDht11 = DHT.read11(sensorPinDht11);
  
  Serial.print("Digital Output: ");
  Serial.println(valSoil);

  // Determine status of our soil moisture situation
  if (valSoil) {
    Serial.println("Status: Soil is too dry - time to water!");
    digitalWrite(outSoil, HIGH);
  } else {
    Serial.println("Status: Soil moisture is perfect");
    digitalWrite(outSoil, LOW);
  }

  Serial.print("Digital Output of second Soil sensor: ");
  Serial.println(valSoil2);

  // Determine status of our soil moisture 2 situation
  if (valSoil2) {
    Serial.println("Status: Soil2 is too dry - time to water!");
    digitalWrite(outSoil2, HIGH);
  } else {
    Serial.println("Status: Soil2 moisture is perfect");
    digitalWrite(outSoil2, LOW);
  }

  Serial.print("Digital Output: ");
  Serial.println(valRain);

  // Determine status of rain sensor
  if (valRain) {
    Serial.println("Status: Rain is too dry - time to water!");
    digitalWrite(outRain, HIGH);
  } else {
    Serial.println("Status: Rain moisture is perfect");
    digitalWrite(outRain, LOW);
  }

  // DHT11 senzor
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  
  delay(1000);
        if (DHT.temperature > 30){
        Serial.println("Otvoren prozor");
        digitalWrite(outDht11, HIGH);
        }
      else if(DHT.temperature < 30){
            Serial.println("Zatvoren prozor");
            digitalWrite(outDht11, LOW);
          }


  delay(2000);
  Serial.println();
}

int readSensorSoil() {
  digitalWrite(sensorSoilPower, HIGH);  // Turn the sensor ON
  delay(10);              // Allow power to settle
  int val = digitalRead(sensorPinSoil); // Read the analog value form sensor
  digitalWrite(sensorSoilPower, LOW);   // Turn the sensor OFF
  return val;             // Return analog moisture value
}

int readSensorSoil2() {
  digitalWrite(sensorSoil2Power, HIGH);  // Turn the sensor ON
  delay(10);              // Allow power to settle
  int val = digitalRead(sensorPinSoil2); // Read the analog value form sensor
  digitalWrite(sensorSoil2Power, LOW);   // Turn the sensor OFF
  return val;             // Return analog moisture value
}

int readSensorRain() {
  digitalWrite(sensorRainPower, HIGH);  // Turn the sensor ON
  delay(10);              // Allow power to settle
  int val = digitalRead(sensorPinRain); // Read the analog value form sensor
  digitalWrite(sensorRainPower, LOW);   // Turn the sensor OFF
  return val;             // Return analog moisture value
}
