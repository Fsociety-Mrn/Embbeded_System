#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4); //Bago ito

//Sonar Sensor 1
int Trig1 = 2;
int Echo1 = 3;

//Sonar Sensor 2
int Trig2 = 4;
int Echo2 = 5;

//float switch
int Float1 = 6; //float switch 1
int Float2 = 7; //float switch 2

//Ph sensor analog pin
int phSensor = A0;

//water pump
int waterPump = 8;

//solenoid valve
int solenoidValve = 9;

void setup() {
  Serial.begin(9600);
  lcd.init(); 
  lcd.backlight(); 

// Sonar Sensors
  pinMode(Trig1, OUTPUT);
  pinMode(Echo1, INPUT);
  pinMode(Trig2, OUTPUT);
  pinMode(Echo2, INPUT);

//float sensor
  pinMode(Float1, INPUT_PULLUP);
  pinMode(Float2, INPUT_PULLUP);

//solenoid valve
  pinMode(solenoidValve, OUTPUT);

//water pump
  pinMode(waterPump, OUTPUT);  
}

void loop() {
//PH Level
   float phLvl = phLevel();

// tank levels
  int tank1 = tankOneLevel(digitalRead(Float1)), 
      tank2 = tankTwoLevel(digitalRead(Float2));


//LCD print  
  LCD_PRINT(
    tank1, //sonar 1
    tank2, //sonar 2
    phLvl, //Ph Level
    );

}

//call this function to print something in my LCD
void LCD_PRINT(
  int sonar1,
  int sonar2,
  float phLvl
  ){

    
  lcd.clear();

//  Tank Level
  lcd.print("T1: " + String(sonar1) + "%");
  lcd.print(" ");
  lcd.print("T2: " + String(sonar2) + "%");

  lcd.setCursor(0,1);

// PH Level
  lcd.print("pH level :" + String(phLvl));
  
  lcd.setCursor(0,2);

//tank 1
  if (sonar1 <= 100 || sonar1 >= 80){
      lcd.print("T1 level is Good");
      Serial.println("T1 level is Good");
  }else if(sonar1 < 80 || sonar1 >= 30){
      lcd.print("T1 is moderate level");
      Serial.println("T1 is moderate level");
  }else{
      lcd.print("T1 is critical level");
      Serial.println("T1 is critical level");
  }

//tank 2
  lcd.setCursor(0,3);
  if (sonar2 <= 100 || sonar1 >= 80){
      lcd.print("T2 level is Good");
      Serial.println("T2 level is Good");
  }else if(sonar2 < 80 || sonar1 >= 30){
      lcd.print("T2 is moderate level");
      Serial.println("T2 is moderate level");
  }else{
      lcd.print("T2 is critical level");
      Serial.println("T2 is critical level");
  }
  
  delay(500);
}

// Group 1: Tank Filteration 

//for tank level
int tankOneLevel(int level){
  
  digitalWrite(Trig1, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig1, HIGH);
  delayMicroseconds(10);
  digitalWrite(Echo1, LOW);

//  duration
  long duration = pulseIn(Echo, HIGH);

//return an inches
    int cm = duration * 0.034 / 2;
    int inch = cm * 0.3937;
    int percent = inch*100/21;
    if (level){
      percent <= 30? digitalWrite(waterPump,HIGH) : digitalWrite(waterPump,LOW);
      return 100 - percent;
    }else{ 
      digitalWrite(waterPump,LOW);
      return 100;
    }
    
}

int tankTwoLevel(int level){
  digitalWrite(Trig2, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig2, HIGH);
  delayMicroseconds(10);
  digitalWrite(Echo2, LOW);

//  duration
  long duration = pulseIn(Echo, HIGH);

//return an inches
    int cm = duration * 0.034 / 2;
    int inch = cm * 0.3937;
    int percent = inch*100/20;
    if (level){
      digitalWrite(solenoidValve,HIGH);
      return 100 - percent;
    }else{ 
      digitalWrite(solenoidValve,LOW);
      return 100;
    }  
}


//for ph sensor
int buffer_arr[10],temp;

float phLevel(){
  float calibration_value = 21.34 + 1.80;
//    float calibration_value = 21.34;
  unsigned long int avgval = 0; 
  
  for(int i=0;i<10;i++) 
    { 
      buffer_arr[i]=analogRead(phSensor); //push the ph raw data to array
      delay(30);
    }

//ascending the raw data from ph sensor
  for(int i=0;i<9;i++)
    {
      for(int j=i+1;j<10;j++)
        {
          if(buffer_arr[i]>buffer_arr[j])
            {
              temp=buffer_arr[i];
              buffer_arr[i]=buffer_arr[j];
                buffer_arr[j]=temp;
            }
        }
      }    

// pass the raw ascending to avgVal
  for(int i=2;i<8;i++) avgval+=buffer_arr[i];

// compute the raw data into pH level
  float volt=(float)avgval*5.0/1024/6;
  float ph_act = -5.70 * volt + calibration_value;

  return ph_act;
}
