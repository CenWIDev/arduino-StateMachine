#include <Log.h>
#include <State.h>
#include <StateMachine.h>
#include <Transition.h>

StateMachine sm;

void setup() {

  sm.AddState("State1"/*This is the name of the state*/, [] () {

    //This is where "State1"'s behavior code would go
    
  });

  sm.AddState("State2"/*This is the name of the state*/, [] () {

    //This is where "State2"'s behavior code would go
    
  });

  sm.AddTransition("State1"/*This is the name of the state to transition from*/, "State2"/*This is the name of the state to transition to*/, []() -> bool {

    //This function should return a boolean that is true when the 
    //transition should be made
    return true;

  });

  sm.SetCurrentState("State1");
  
}

void loop() {

  auto nextState = sm.GetNextState();
  sm.SetCurrentState(nextState);
  sm.RunCurrentState();

}
