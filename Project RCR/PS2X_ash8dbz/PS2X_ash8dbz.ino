#include <PS2X_lib.h>  //for v1.6
#include <AFMotor.h>

/******************************************************************
 * Motor initilize.
 * 
 ******************************************************************/
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);


/******************************************************************
 * set pins connected to PS2 controller:
 *   - 1e column: original 
 *   - 2e colmun: Stef?
 * replace pin numbers by the ones you use
 ******************************************************************/
 // using analog bcoz 0-13 used by motor shield
#define PS2_DAT        A0  //13    changing this from 13 to A0
#define PS2_CMD        A1  //11    changing this from 11 to A1
#define PS2_SEL        A2  //10    changing this from 10 to A2
#define PS2_CLK        A3  //12    changing this from 12 to A3

/******************************************************************
 * select modes of PS2 controller:
 *   - pressures = analog reading of push-butttons 
 *   - rumble    = motor rumbling
 * uncomment 1 of the lines for each mode selection
 ******************************************************************/
//#define pressures   true
#define pressures   false
//#define rumble      true
#define rumble      true

PS2X ps2x; // create PS2 Controller Class

//right now, the library does NOT support hot pluggable controllers, meaning 
//you must always either restart your Arduino after you connect the controller, 
//or call config_gamepad(pins) again after connecting the controller.

int error = 0;
byte type = 0;
byte vibrate = 0;

//to control speed of vehicle
byte v_speed=255;
  
//int speed_incr(int speed)
//{
//    if(speed>=255)
//    {
//      return 255;
//    }
//    else
//    {
//      return speed+10;
//    }
//}
//
//int speed_decr(int speed)
//{
//    if(speed<=200)
//    {
//      return 200;
//    }
//    else
//    {
//      return speed-10;
//    }
//}

void setup(){

  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);


  Serial.begin(57600);
  
  delay(500);  //added delay to give wireless ps2 module some time to startup, before configuring it
   
  //CHANGES for v1.6 HERE!!! **************PAY ATTENTION*************
  
  //setup pins and settings: GamePad(clock, command, attention, data, Pressures?, Rumble?) check for error
  error = ps2x.config_gamepad(PS2_CLK, PS2_CMD, PS2_SEL, PS2_DAT, pressures, rumble);
  
  if(error == 0){
    Serial.print("Found Controller, configured successful ");
    Serial.print("pressures = ");
	if (pressures)
	  Serial.println("true ");
	else
	  Serial.println("false");
	Serial.print("rumble = ");
	if (rumble)
	  Serial.println("true)");
	else
	  Serial.println("false");
    Serial.println("Try out all the buttons, X will vibrate the controller, faster as you press harder;");
    Serial.println("holding L1 or R1 will print out the analog stick values.");
  }  
  else if(error == 1)
    Serial.println("No controller found, check wiring, see readme.txt to enable debug. visit www.billporter.info for troubleshooting tips");
   
  else if(error == 2)
    Serial.println("Controller found but not accepting commands. see readme.txt to enable debug. Visit www.billporter.info for troubleshooting tips");

  else if(error == 3)
    Serial.println("Controller refusing to enter Pressures mode, may not support it. ");
  
//  Serial.print(ps2x.Analog(1), HEX);
  
  type = ps2x.readType(); 
  switch(type) {
    case 0:
      Serial.print("Unknown Controller type found ");
      break;
    case 1:
      Serial.print("DualShock Controller found ");
      break;
    case 2:
      Serial.print("GuitarHero Controller found ");
      break;
	case 3:
      Serial.print("Wireless Sony DualShock Controller found ");
      break;
   }
}

void loop() {
  /* You must Read Gamepad to get new values and set vibration values
     ps2x.read_gamepad(small motor on/off, larger motor strenght from 0-255)
     if you don't enable the rumble, use ps2x.read_gamepad(); with no values
     You should call this at least once a second
   */  

   
  if(error == 1) //skip loop if no controller found
    return; 
  
  else { //DualShock Controller
    
    ps2x.read_gamepad(false, vibrate); //read controller and set large motor to spin at 'vibrate' speed
    //ps2x.read_gamepad();  //changed this.ash8dbz
    
//    if(ps2x.Button(PSB_START))         //will be TRUE as long as button is pressed      
//      {
//        Serial.println("Start is being held");
//      }
//    if(ps2x.Button(PSB_SELECT))
//      Serial.println("Select is being held");      
//
//    if(ps2x.Button(PSB_PAD_UP)) {      //will be TRUE as long as button is pressed
//      Serial.print("Up held this hard: ");
//      Serial.println(ps2x.Analog(PSAB_PAD_UP), DEC);
//    }
    if(ps2x.ButtonPressed(PSB_PAD_RIGHT)){
      //Serial.print("Right held this hard: ");
      //Serial.println(ps2x.Analog(PSAB_PAD_RIGHT), DEC);
      Serial.println("Right Move");
          motor1.run(BACKWARD);
          motor4.run(BACKWARD);
          motor2.run(FORWARD);
          motor3.run(FORWARD);
          motor1.setSpeed(v_speed);  
          motor2.setSpeed(v_speed);  
          motor3.setSpeed(v_speed);  
          motor4.setSpeed(v_speed);  
          delay(10);
    }
    if(ps2x.ButtonReleased(PSB_PAD_RIGHT))              //will be TRUE if button was JUST released
      {
        Serial.println("Right Stop");
          motor1.setSpeed(0);  
          motor2.setSpeed(0);  
          motor3.setSpeed(0);  
          motor4.setSpeed(0);  
          delay(10); 
      }
   // if(ps2x.Button(PSB_PAD_LEFT)){
      //Serial.print("LEFT held this hard: ");
      //Serial.println(ps2x.Analog(PSAB_PAD_LEFT), DEC);
    //}
       if(ps2x.ButtonPressed(PSB_PAD_LEFT)){
      //Serial.print("Right held this hard: ");
      //Serial.println(ps2x.Analog(PSAB_PAD_RIGHT), DEC);
      Serial.println("Left Move");
          motor2.run(BACKWARD);
          motor3.run(BACKWARD);
          motor1.run(FORWARD);
          motor4.run(FORWARD);
          motor1.setSpeed(v_speed);  
          motor2.setSpeed(v_speed);  
          motor3.setSpeed(v_speed);  
          motor4.setSpeed(v_speed);  
          delay(10);
    }
    if(ps2x.ButtonReleased(PSB_PAD_LEFT))              //will be TRUE if button was JUST released
      {
        Serial.println("Left Stop");
          motor1.setSpeed(0);  
          motor2.setSpeed(0);  
          motor3.setSpeed(0);  
          motor4.setSpeed(0);  
          delay(10); 
      }
//    if(ps2x.Button(PSB_PAD_DOWN)){
//      Serial.print("DOWN held this hard: ");
//      Serial.println(ps2x.Analog(PSAB_PAD_DOWN), DEC);
//    }   
    //Serial.print(ps2x.Analog(PSAB_TRIANGLE));    
    //vibrate = ps2x.Analog(PSAB_TRIANGLE);  //this will set the large motor vibrate speed based on how hard you press the blue (X) button
//    if (ps2x.NewButtonState()) {        //will be TRUE if any button changes state (on to off, or off to on)
//      if(ps2x.Button(PSB_L3))
//        Serial.println("L3 pressed");
//      if(ps2x.Button(PSB_R3))
//        Serial.println("R3 pressed");
//      if(ps2x.Button(PSB_L2))
//        Serial.println("L2 pressed");
//      if(ps2x.Button(PSB_R2))
//        Serial.println("R2 pressed");
//      if(ps2x.Button(PSB_TRIANGLE))
//        Serial.println("Triangle pressed");        
    }

    if(ps2x.ButtonPressed(PSB_CROSS))               //will be TRUE if button was JUST pressed
      {
        Serial.println("Forward");
          motor1.run(FORWARD);
          motor2.run(FORWARD);
          motor3.run(FORWARD);
          motor4.run(FORWARD);
          motor1.setSpeed(v_speed);  
          motor2.setSpeed(v_speed);  
          motor3.setSpeed(v_speed);  
          motor4.setSpeed(v_speed);  
          delay(10);
         
      }
    if(ps2x.ButtonReleased(PSB_CROSS))              //will be TRUE if button was JUST released
      {
        Serial.println("Forward Stop");
          motor1.setSpeed(0);  
          motor2.setSpeed(0);  
          motor3.setSpeed(0);  
          motor4.setSpeed(0);  
          delay(10); 
      }

      if(ps2x.ButtonPressed(PSB_SQUARE))               //will be TRUE if button was JUST pressed
      {
        Serial.println("Forward");
          motor1.run(BACKWARD);
          motor2.run(BACKWARD);
          motor3.run(BACKWARD);
          motor4.run(BACKWARD);
          motor1.setSpeed(v_speed);  
          motor2.setSpeed(v_speed);  
          motor3.setSpeed(v_speed);  
          motor4.setSpeed(v_speed);  
          delay(10);
         
      }
    if(ps2x.ButtonReleased(PSB_SQUARE))              //will be TRUE if button was JUST released
      {
        Serial.println("Forward Stop");
          motor1.setSpeed(0);  
          motor2.setSpeed(0);  
          motor3.setSpeed(0);  
          motor4.setSpeed(0);  
          delay(10); 
      }
        
    /*if(ps2x.NewButtonState(PSB_CROSS))               //will be TRUE if button was JUST pressed OR released
      Serial.println("X just changed");
    if(ps2x.ButtonReleased(PSB_SQUARE))              //will be TRUE if button was JUST released
      Serial.println("Square just released");     
    */
    if(ps2x.Button(PSB_R1)) { //print stick values if either is TRUE
//      Serial.print("Stick Values:");
//      Serial.print(ps2x.Analog(PSS_LY), DEC); //Left stick, Y axis. Other options: LX, RY, RX  
//      Serial.print(",");
//      Serial.print(ps2x.Analog(PSS_LX), DEC); 
//      Serial.print(",");
//      Serial.print(ps2x.Analog(PSS_RY), DEC); 
//      Serial.print(",");
//      Serial.println(ps2x.Analog(PSS_RX), DEC);
//         v_speed=speed_incr(v_speed);                                                               --ash8dbz

        vibrate = 255;
    }
    else if(ps2x.Button(PSB_R2)) { //print stick values if either is TRUE
//      Serial.print("Stick Values:");
//      Serial.print(ps2x.Analog(PSS_LY), DEC); //Left stick, Y axis. Other options: LX, RY, RX  
//      Serial.print(",");
//      Serial.print(ps2x.Analog(PSS_LX), DEC); 
//      Serial.print(",");
//      Serial.print(ps2x.Analog(PSS_RY), DEC); 
//      Serial.print(",");
//      Serial.println(ps2x.Analog(PSS_RX), DEC);
//         v_speed=speed_decr(v_speed);                                                               --ash8dbz
        vibrate = 0;
    }
     else if(ps2x.Button(PSAB_TRIANGLE)) { 
        Serial.print(ps2x.Analog(PSAB_TRIANGLE));                                     
        
    }             
  
  delay(50);  
}
