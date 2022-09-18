#include "DHT.h"

#define dhtPin 12

#define dhtType DHT11

DHT dht(dhtPin, dhtType);

float vlaga;
float temperatura;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  vlaga = dht.readHumidity();
  temperatura = dht.readTemperature();

  if (isnan(vlaga) || isnan(temperatura)) {
    Serial.println("Napaka");
    return;
  }
  Serial.print(temperatura);
  Serial.print("&");
  Serial.print(vlaga);
  Serial.println();

  delay(10000);

}
