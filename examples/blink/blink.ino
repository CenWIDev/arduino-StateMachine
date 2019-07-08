/**
 *  blink.ino
 * 
 *  A reference implementation of the classic Blink program 
 *  as a finite state machine.
 * 
 * 
 * State Transition Diagram:
 * 
 *               _ timeout(500) _
 *             /                  \
 *            ^                    |
 *            |                    V
 *         [ "On" ]            [ "Off" ]
 *            ^                    |
 *            |                    V
 *             \ _ timeout(500) _ /
 *             
 **/

#include <StateMachine.h>
StateMachine sm;

void BuildStateMachine() {

  // add the two states ("On" and "Off"), and define the behavior in those states
  sm.AddState("On", [] () { digitalWrite(LED_BUILTIN, HIGH); });
  sm.AddState("Off", [] () { digitalWrite(LED_BUILTIN, LOW); });

  // transition from "On" into "Off" after a 500ms timeout
  sm.AddTransition("On", "Off", []() -> bool { return sm.TimeoutSinceLastTransition(500); });

  // transition from "Off" into "On" after a 500ms timeout
  sm.AddTransition("Off", "On", []() -> bool { return sm.TimeoutSinceLastTransition(500); });

  // set the initial state to "On"
  sm.SetCurrentState("On");
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  BuildStateMachine();
}

void loop() {
  auto nextState = sm.GetNextState();
  sm.SetCurrentState(nextState);
  sm.RunCurrentState();
}
