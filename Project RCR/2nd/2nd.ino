#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup() 
{
  //Set initial speed of the motor & stop
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  
}

void loop() 
{
 

  // Turn on motor
  
  
  // Accelerate from zero to maximum speed
    motor1.setSpeed(240);  
    delay(10);
    motor2.setSpeed(240);  
    delay(10);
    motor3.setSpeed(240);  
    delay(10);  
    motor4.setSpeed(240);  
    delay(10);        

  
  
}
