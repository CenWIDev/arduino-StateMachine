#include <StateMachine.h>

StateMachine sm;

void setup() {

  Serial.begin(9600);

  sm.AddState("State1"/*This is the name of the state to be created*/, [] () {

    //This is where "State1"'s behavior code would go

    //Example: Print a line to the serial monitor
    Serial.println("State 1's behavior code was called.");

  });

  sm.AddState("State2"/*This is the name of the state*/, [] () {

    //This is where "State2"'s behavior code would go

    //Example: Print a line to the serial monitor
    Serial.println("State 2's behavior code was called.");

  });

  sm.AddTransition("State1"/*This is the name of the state to transition from*/, "State2"/*This is the name of the state to transition to*/, []() -> bool {

    //This function should return a boolean that is true when the 
    //transition should be made
    return true;

  });

  //sets the current state of the state machine
  sm.SetCurrentState("State1");

}

void loop() {

  //GetNextState() returns a state
  //The returned state is either the current state if no transition is needed, or a new state if a transition is triggered
  auto nextState = sm.GetNextState();

  //Sets the current state of the state machine to the state returned by the line above
  sm.SetCurrentState(nextState);

  //Runs the behavior code of the state machine's current state
  sm.RunCurrentState();

}
