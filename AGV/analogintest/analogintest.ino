int enA = 10;
int in1 = 9;
int in2 = 8;
// motor two
int enB = 5;
int in3 = 7;
int in4 = 6;

void setup() 
{
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);
  
  // set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

void loop() 
{
  int val0 = analogRead(A0);//forward
  int val1 = analogRead(A1);//right
  int val2 = analogRead(A2);//left
  int val3 = analogRead(A3);//slightRight
  if (val0>450)
  {
    forward();
    //delay(100);
  }
  else if(val1>450)
  {
    turnRight();
//    delay(1000);
  }
  else if(val2>450)
  {
    turnLeft();
//    delay(1000);
  }
  else if(val3>450)
    {
    slightRight();
    //delay(300);
    }
  else if(val0&&val1&&val2<450)
  {
    stop(); 
//    delay(1000);
  }
}
