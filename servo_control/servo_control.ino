#include <Servo.h>

Servo servoX;
Servo servoY;

void setup()
{
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
}

void loop()
{
  if (Serial.available())
  {
    String input = Serial.readStringUntil('\n');
    int commaIndex = input.indexOf(',');

    if (commaIndex > 0)
    {
      int x = input.substring(0, commaIndex).toInt();
      int y = input.substring(commaIndex + 1).toInt();

      x = constrain(x, 0, 180);
      y = constrain(y, 0, 180);

      servoX.write(x);
      servoY.write(y);
    }
  }
}