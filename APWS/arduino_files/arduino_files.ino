//ALL PINS FOR SENSORS AND OTHER DEVICES
int smSensor = A0;
int wlSensor = A1;
int buzzPin = 8;
int relayPin = 7;
//SENSOR VALUES
int smVal = 0;
int wlVal = 0;
//COMMANDS
String rawCmd;
int raspCmd;
//CONDITIONAL VALUES
int exeOnce = 0;
void setup() 
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  pinMode(smSensor, INPUT);
  pinMode(wlSensor, INPUT);
  pinMode(buzzPin, OUTPUT);
}

void loop() 
{
  // put your main code here, to run repeatedly:
  smVal = analogRead(smSensor);
  wlVal = analogRead(wlSensor);
  if (exeOnce == 0){
    digitalWrite(relayPin, HIGH);
    exeOnce = 1;
    }
  if (Serial.available()){
    rawCmd = Serial.readString();
    raspCmd = rawCmd.toInt();
    switch(raspCmd){
      case 11:
        Serial.println(smVal);
        break;
      case 12:
        Serial.println(wlVal);
        break;
      case 21:
        digitalWrite(relayPin, LOW);
        Serial.println("ACK");
        break;
      case 22:
        digitalWrite(relayPin, HIGH);
        Serial.println("ACK");
        break;
      case 23:
        digitalWrite(buzzPin, HIGH);
        Serial.println("ACK");
        break;
      case 24:
        digitalWrite(buzzPin, LOW);
        Serial.println("ACK");
        break;
      default:
        Serial.println("error");
        break;
      }
    } 
}
