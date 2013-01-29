/* 
  Sergei remote activator
  Author: Pete Milne
  Date: 17-12-2011
  Version: 1.0  
*/

const int RELAY = 13;     // Relay on pin 13

void setup() {
  Serial.begin(9600);
  pinMode(RELAY, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    if (Serial.read() == 'D') {
      activate();
      Serial.flush();
    }
  }
}

// Set relay pin high for 2 secs
void activate() {
    digitalWrite(RELAY, HIGH);
    delay(2000);
    digitalWrite(RELAY, LOW);    
}

