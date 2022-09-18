#include "DHT.h"

#define dhtPin 12

#define dhtType DHT11

DHT dht(dhtPin, dhtType);

#include <LiquidCrystal.h>

const int rs = 10, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int svetlost = analogRead(A0);

float vlaga;
float temperatura;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16, 2);
}

void loop() {
  svetlost = analogRead(A0);
  vlaga = dht.readHumidity();
  temperatura = dht.readTemperature();

  if (isnan(vlaga) || isnan(temperatura)) {
    Serial.println("Napaka");
    return;
  }
  Serial.print(temperatura);
  Serial.print("&");
  Serial.print(vlaga);
  Serial.print("&");
  Serial.print(svetlost);
  Serial.println();

  lcd.setCursor(0, 0);
  lcd.print("Temp: " + String(temperatura));
  lcd.setCursor(0, 1);
  lcd.print("Vlaga: " + String(vlaga) + "%");

  delay(1000);

}
