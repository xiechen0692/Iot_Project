byte number = 0;
String inputString = "";
int stringComplete = 0;
void setup()
{
  Serial.begin(115200);
  inputString.reserve(200);
  pinMode(12 , OUTPUT);
  pinMode(10 , OUTPUT);

}

void loop()
{
  if (stringComplete==1)
  {
    inputString = "";    
    digitalWrite(12 , HIGH );
    //delay( 5000 );
    //stringComplete=false;
  }
  else if (stringComplete==2)
  {
    inputString = "";    
    digitalWrite(12 , LOW );
  }
  else if (stringComplete==3)
  {
    inputString = "";    
    digitalWrite(10 , HIGH);
  }
  else if (stringComplete==4)
  {
    inputString = "";    
    digitalWrite(10 , LOW );
  }
}
void serialEvent()
{
  while (Serial.available())
  {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inputString == "1")
    {
      stringComplete = 1;
    }
    else if (inputString == "2")
    {
      stringComplete = 2;
    }
     else if (inputString == "3")
    {
      stringComplete = 3;
    }
     else if (inputString == "4")
    {
      stringComplete = 4;
    }
  }

}

