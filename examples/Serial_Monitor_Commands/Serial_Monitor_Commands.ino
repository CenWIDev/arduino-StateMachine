#include <StateMachine.h>

StateMachine sm;
StateMachine commands;

String input;

int executionCount = 0;

void setup() {

  Serial.begin(9600);

  sm.AddState("Message", [] () {

    //This is where "State1"'s behavior code would go

    //Example: Print a line to the serial monitor
    Serial.println("Enter the information you would like printed:");

  });

  sm.AddState("Read", [] () {

    if(Serial.available())
    {
      input = Serial.readString();
      input.trim();
    }

  });

  sm.AddState("Execute", [] () {

    Serial.println("The information you input is: " + input);
    auto commandState = commands.GetNextState();
    commands.SetCurrentState(commandState);
    Serial.println("Current state is: " + commandState);
    commands.RunCurrentState();
    commands.SetCurrentState("none");
    executionCount++;

  });

  sm.AddTransition("Message", "Read", []() -> bool {

    return true;

  });

  sm.AddTransition("Read", "Execute", []() -> bool {

    //This function should return a boolean that is true when the 
    //transition should be made
    return !input.equals("");

  });

  sm.AddTransition("*", "Message", []() -> bool {

    //This function should return a boolean that is true when the 
    //transition should be made
    return input.equals("repeat");

  });

  sm.AddTransition("Execute", "Message", []() -> bool {

    bool transition = false;
    if(executionCount>0)
    {
      transition = true;
      executionCount = 0;
    }
    ClearInput();
    return transition;
    
  });

  SetUpCommands();

  sm.SetCurrentState("Message");
  sm.RunCurrentState();

}

void loop() {

  auto nextState = sm.GetNextState();
  sm.SetCurrentState(nextState);
  sm.RunCurrentState();

}

//----------------------------------------------------------------------------------------------------------------------------------

void ClearInput()
{
  input = "";
}

void SetUpCommands()
{

  commands.AddState("none", [] () {

  });

  commands.AddState("printMessage", [] () {
    Serial.println("This is the message for the printMessage command");
  });

  commands.AddTransition("*", "printMessage", []() -> bool {

    return input.equals("printMessage");   
    
  });

  commands.AddState("printMessage2", [] () {
    Serial.println("This is the message for the printMessage2 command");
  });

  commands.AddTransition("*", "printMessage2", []() -> bool {

    return input.equals("printMessage2");   
    
  });

  commands.SetCurrentState("none");
  
}
