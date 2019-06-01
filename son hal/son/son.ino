#define pot A0

void setup() { 
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(LED_BUILTIN, OUTPUT); //make the LED pin (13) as output
  digitalWrite (LED_BUILTIN, LOW);
  //Serial.println("Hi!, I am Arduino");
  pinMode(A0, INPUT);
}

void loop() {
  int value = analogRead(pot);
  value = map(value, 0,1023, 0,150);
  Serial.println(value);
  delay(1000);  
  if(Serial.available()){
   char data = Serial.read();
   int value = analogRead(pot);
   value = map(value, 0,1023, 0,150);
   Serial.println(value);
   delay(150);  
  //Serial.println(data);
  if(data == 'o'){
    digitalWrite (LED_BUILTIN, HIGH);
}
  else if(data == 'c'){
    digitalWrite (LED_BUILTIN, LOW);

}
}

}
