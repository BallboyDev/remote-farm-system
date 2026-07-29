// #include <Arduino.h>

// // put function declarations here:
// int myFunction(int, int);

// void setup() {
//   // put your setup code here, to run once:
//   int result = myFunction(2, 3);
// }

// void loop() {
//   // put your main code here, to run repeatedly:
// }

// // put function definitions here:
// int myFunction(int x, int y) {
//   return x + y;
// }

#include <Arduino.h>

#ifndef LED_BUILTIN
#define LED_BUILTIN 2
#endif

constexpr unsigned long BLINK_INTERVAL_MS = 1000;

void setup()
{
  Serial.begin(115200);

  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println();
  Serial.println("ESP LED TEST STARTED");
  Serial.print("LED GPIO: ");
  Serial.println(LED_BUILTIN);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("LED ON");

  delay(BLINK_INTERVAL_MS);

  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("LED OFF");

  delay(BLINK_INTERVAL_MS);
}