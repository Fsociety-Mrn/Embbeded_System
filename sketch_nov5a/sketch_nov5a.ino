#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4); 

#define FLOAT_SENSOR  D6     // the number of the pushbutton pin
#define pump7           D8 
#define pump6           D7 

#define pump4           D4 
//Sonar Sensor 1
#define Trig1 D5
#define Echo1 D3
#define pump1           5

void setup() 
{
     Serial.begin(9600);
  lcd.init(); 
  lcd.backlight(); 
  // initialize the LED pin as an output:
  pinMode(pump7, OUTPUT);

     pinMode(pump4, OUTPUT);
      pinMode(Trig1, OUTPUT);
       pinMode(Echo1, OUTPUT);
  // initialize the pushbutton pin as an input:
}

void loop() 
{
  
   LCD_PRINT(
     

   tankLevel(Trig1,Echo1), //sonar 1
  digitalRead(FLOAT_SENSOR)
    );
  if(digitalRead(FLOAT_SENSOR) == LOW) 
  {
    
    digitalWrite(pump7, HIGH);
 
      digitalWrite(pump4, HIGH);
    Serial.println("Turn On WATER pump");
  } 
  else 
  {
    
    digitalWrite(pump7, LOW);

    digitalWrite(pump4, LOW);
    Serial.println("Turn Off WATER pump");
  }

}

void LCD_PRINT(
  int sonar1,
  int sonar2

  ){
  lcd.clear();

//  Tank Level
  lcd.print("T1: " + String(sonar1) + "%");
  lcd.print(" ");
  lcd.print("T2: " + String(sonar2) + "%");

  lcd.setCursor(0,1);

// PH Level

  
  lcd.setCursor(0,2);
  

  delay(1000);
}

int tankLevel(int Trig, int Echo){
  
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);

//  duration
  long duration = pulseIn(Echo, HIGH);

//return an inches
  int inches = duration / 74 / 2;
inches;
}
