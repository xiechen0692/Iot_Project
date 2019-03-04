void turnRight()
{
  // this function will run the motors in both directions at a fixed speed
  // turn on motor A
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  // set speed to 200 out of possible range 0~255
  analogWrite(enA, 0); //right
  // turn on motor B
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  // set speed to 200 out of possible range 0~255
  analogWrite(enB, 40); //left
  //  // now change motor directions
  //  digitalWrite(in1, LOW);
  //  digitalWrite(in2, HIGH);
  //  digitalWrite(in3, LOW);
  //  digitalWrite(in4, HIGH);
  //  delay(2000);
  //  // now turn off motor
  //  digitalWrite(in1, LOW);
  //  digitalWrite(in2, LOW);
  //  digitalWrite(in3, LOW);
  //  digitalWrite(in4, LOW);
}
