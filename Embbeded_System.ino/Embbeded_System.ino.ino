#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,20,4); //Bago ito
#include <Wire.h>

//Sonar Sensor 1
#define Trig1 2
#define Echo1 3
//Sonar Sensor 2
#define Trig2 4
#define Echo2 5
//float switch
#define Float1 6 //float switch 1
#define Float2 7 //float switch 2
//Ph sensor analog pin
#define phSensor A0
//water pump
#define waterPump 8
//solenoid valve
#define solenoidValve 9
// -------- SETUP -------- //
void setup() {
  Serial.begin(9600);
  lcd.init(); 
  pinMode(waterPump, OUTPUT);  
}
// -------- LOOP -------- //
void loop() {
//------------ Group 1: Tank Filteration ------------// 
 
//PH Level
   float phLvl = phLevel();
   
// floats
  int flt1 = digitalRead(Float1),
      flt2 = digitalRead(Float2);
  int tank1 = tankLevel(Trig1,Echo1,flt1,21), 
      tank2 = tankLevel(Trig2,Echo2,flt2,20);
// for turning off the Waterpumps at Solenoid
  turnOff(tank1,tank2);
// ------------ LCD print ------------ // 
  LCD_PRINT(
    tank1, //sonar 1
    tank2, //sonar 2
//  Tank Level
  lcd.print("T1: " + String(sonar1) + "%");
//  Serial.println("T1:" + String(sonar1));
  lcd.print(" ");
  lcd.print("T2: " + String(sonar2) + "%");
      lcd.print("Tank 2 is undefined");
  }
  delay(200);
}
//--------------------- Group 1: Tank Filteration ---------------------// 
//for tank level
int tankLevel(int Trig, int Echo, int level,int lvl){
    int cm = duration * 0.034 / 2;
    int inch = cm * 0.3937;
    int percent = inch*100/lvl;
    if (level == 1){
      return 100 - percent;
    }else{ 
//      digitalWrite(sole,LOW);
//turn off Water Tank and close solenoid
void turnOff(int sonar1, int sonar2){
  if(sonar1 < 100 && sonar1 > 40){
    digitalWrite(waterPump,HIGH);
  }else{
    digitalWrite(waterPump,LOW);
  }
  if(sonar2 < 100 && sonar2 > 40){
    digitalWrite(solenoidValve,HIGH);
 
  }else{
