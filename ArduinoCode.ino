#include<LiquidCrystal.h>

LiquidCrystal lcd(2,3,4,5,6,7);

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.home();

  Serial.setTimeout(50);
  lcd.print("Total affected :");
}

void loop() {
String x;

lcd.setCursor(0,2);
if(Serial.available()>0)
{
  x = Serial.readString();
  }
lcd.print(x);

}