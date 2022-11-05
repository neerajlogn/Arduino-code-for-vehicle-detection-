
// arduino code for vehicle counter using IR sensor 
// designing parking system with Arduino , IR sensor , Servo Motor




#include <Wire.h>
#include <LiquidCrystal.h>
#include <Servo.h>
LiquidCrystal lcd(42,44,52,50,48,46);
int sensor1 = 22;//out sensor
int sensor2 = 24;//in sensor
Servo myservo;
int totalslot = 4;          
int count = 0;
int count2 = 0;

void setup() {
analogWrite(40,70 );
lcd.begin(16,2);
pinMode(sensor1, INPUT);
pinMode(sensor2, INPUT);
myservo.attach(28);
lcd.setCursor (0,0);
lcd.print("   IIT DHANBAD ");
lcd.setCursor (0,1);
lcd.print(" PARKING SYSTEM ");
delay (2000);
lcd.clear();  
}

void loop(){

if(digitalRead(sensor1) == LOW && count==0){
if(totalslot>0){
count=1;
if(count2==0)
{myservo.write(100); totalslot = totalslot-1;}
}
else{
lcd.setCursor (0,0);
lcd.print("    SORRY :(    ");  
lcd.setCursor (0,1);
lcd.print("  Parking Full  ");
delay (3000);
lcd.clear();
}
}

if(digitalRead(sensor2) == LOW && count2==0)
{
count2=1;
if(count==0)
{myservo.write(0); totalslot=totalslot+1;}
}

if(count==1 && count2==1){
delay (1000);
myservo.write(100);
count=0, count2=0;
}

lcd.setCursor (0,0);
lcd.print("    WELCOME!    ");
lcd.setCursor (0,1);
lcd.print("Slot Left: ");
lcd.print(totalslot);
}
